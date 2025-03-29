import logging
from concurrent.futures import ThreadPoolExecutor

import requests
from flask import current_app

logger = logging.getLogger(__name__)


def summarize_text(text, model='mistral', prompt="Summarize this document:"):
    """Send text to the local Ollama model for summarization."""
    ollama_url = current_app.config.get('OLLAMA_BASE_URL', 'http://localhost:11434')
    api_endpoint = f"{ollama_url}/api/generate"
    full_prompt = f"{prompt}\n\n{text}"
    payload = {
        "model": model,
        "prompt": full_prompt,
        "stream": False
    }
    try:
        timeout_seconds = int(current_app.config.get('OLLAMA_TIMEOUT', 120))
        response = requests.post(api_endpoint, json=payload, timeout=timeout_seconds)
        response.raise_for_status()
        data = response.json()
        if "response" in data:
            summary = data["response"].strip()
            logger.info(f"Summary received from model {model}.")
            return summary
        else:
            logger.error(f"Response from model {model} missing 'response' key: {data}")
            return f"[Error: Unexpected response format from model {model}]"
    except requests.exceptions.Timeout:
        logger.error(f"Timeout calling model {model}.")
        return f"[Error: Timeout calling model {model}]"
    except requests.exceptions.RequestException as e:
        logger.error(f"Error calling model {model}: {e}")
        return f"[Error calling model {model}: {e}]"
    except Exception as e:
        logger.exception(f"Unexpected error with model {model}: {e}")
        return f"[Error: Unexpected error with model {model}: {e}]"


def summarize_with_models(text, models, prompt, sequential=False):
    """Summarize text using multiple models."""
    results = {}
    if sequential:
        for model in models:
            results[model] = summarize_text(text, model, prompt)
    else:
        max_workers = int(current_app.config.get('OLLAMA_MAX_WORKERS', 4))
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = {executor.submit(summarize_text, text, model, prompt): model for model in models}
            for future in futures:
                model = futures[future]
                try:
                    results[model] = future.result()
                except Exception as e:
                    logger.exception(f"Error processing model {model}: {e}")
                    results[model] = f"[Error processing model {model}: {e}]"
    return results

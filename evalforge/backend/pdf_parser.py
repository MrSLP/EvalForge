import logging

import fitz  # PyMuPDF
import pytesseract
from pdf2image import convert_from_path

logger = logging.getLogger(__name__)


def extract_text_from_pdf(pdf_path):
    """Extract text using PyMuPDF; fall back to OCR if needed."""
    logger.info(f"Extracting text from PDF: {pdf_path}")
    text = ""
    try:
        doc = fitz.open(pdf_path)
        for page in doc:
            page_text = page.get_text("text")
            text += page_text + "\n"
        doc.close()
        if len(text.strip()) > 10:
            return text.strip()
        else:
            logger.warning("No text extracted with PyMuPDF; falling back to OCR.")
    except Exception as e:
        logger.error(f"Error with PyMuPDF extraction: {e}")

    # Fallback: OCR using pdf2image and pytesseract
    try:
        pages = convert_from_path(pdf_path)
        ocr_text = ""
        for img in pages:
            ocr_text += pytesseract.image_to_string(img) + "\n"
        return ocr_text.strip()
    except Exception as ocr_e:
        logger.error(f"OCR extraction failed: {ocr_e}")
        raise RuntimeError(f"Failed to extract text using both methods: {ocr_e}")

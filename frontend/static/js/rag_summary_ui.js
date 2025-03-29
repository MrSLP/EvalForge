// rag_summary_ui.js

async function generateSummary() {
  const evalText = document.getElementById("evalText").value;
  const model = document.getElementById("modelSelect").value;
  const sanitize = document.getElementById("sanitizeToggle").checked;
  if (!evalText.trim()) {
    alert("Please enter evaluation text.");
    return;
  }
  try {
    const response = await fetch("/api/summarize_with_rag", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text: evalText, model: model, sanitize: sanitize })
    });
    const data = await response.json();
    document.getElementById("summaryOutput").textContent = data.summary;
  } catch (error) {
    console.error("Error generating summary:", error);
    alert("Error generating summary: " + error.message);
  }
}

async function saveSummary() {
  const summary = document.getElementById("summaryOutput").textContent;
  if (!summary.trim()) {
    alert("No summary to save.");
    return;
  }
  try {
    const response = await fetch("/api/save_summary", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text: summary })
    });
    const data = await response.json();
    alert(data.message);
  } catch (error) {
    console.error("Error saving summary:", error);
    alert("Error saving summary: " + error.message);
  }
}

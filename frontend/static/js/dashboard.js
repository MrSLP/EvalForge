// dashboard.js

async function loadLogs() {
  try {
    const response = await fetch("/api/logs");
    if (!response.ok) throw new Error("Failed to load logs.");
    const data = await response.json();
    const summaryDiv = document.getElementById("logSummary");
    const fullLogsDiv = document.getElementById("fullLogs");
    summaryDiv.innerHTML = "";
    fullLogsDiv.innerHTML = "";

    if (data.summary) {
      summaryDiv.textContent = JSON.stringify(data.summary, null, 2);
    }
    if (data.logs && data.logs.length > 0) {
      data.logs.forEach(log => {
        const p = document.createElement("p");
        p.textContent = `${log.timestamp}: ${log.event} - ${JSON.stringify(log.data)}`;
        fullLogsDiv.appendChild(p);
      });
    } else {
      fullLogsDiv.textContent = "No log entries.";
    }
  } catch (error) {
    console.error("Error loading logs:", error);
    alert("Error loading logs: " + error.message);
  }
}

document.addEventListener("DOMContentLoaded", loadLogs);

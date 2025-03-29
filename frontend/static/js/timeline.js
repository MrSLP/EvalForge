// timeline.js

async function loadTimeline() {
  const studentId = document.getElementById("studentSelect").value;
  if (!studentId) {
    alert("Please select a student.");
    return;
  }
  try {
    const response = await fetch(`/api/timeline/${studentId}`);
    if (!response.ok) throw new Error("Failed to load timeline.");
    const timeline = await response.json();
    const container = document.getElementById("timelineContainer");
    container.innerHTML = "";
    timeline.forEach(entry => {
      const div = document.createElement("div");
      div.className = "timeline-entry";
      div.textContent = `${entry.timestamp}: ${entry.summary}`;
      container.appendChild(div);
    });
  } catch (error) {
    console.error("Error loading timeline:", error);
    alert("Error loading timeline: " + error.message);
  }
}

document.addEventListener("DOMContentLoaded", loadTimeline);

// vault.js

document.getElementById("uploadForm").addEventListener("submit", async function(e) {
  e.preventDefault();
  const studentId = document.getElementById("studentSelect").value;
  if (!studentId) {
    alert("Please select a student.");
    return;
  }
  const formData = new FormData(this);
  try {
    const response = await fetch(`/upload_documents/${studentId}`, {
      method: "POST",
      body: formData
    });
    const result = await response.json();
    document.getElementById("uploadResult").textContent = JSON.stringify(result, null, 2);
  } catch (error) {
    console.error("Error uploading files:", error);
    alert("Error uploading files: " + error.message);
  }
});

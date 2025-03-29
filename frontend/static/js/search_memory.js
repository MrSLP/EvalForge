// search_memory.js

async function searchMemory() {
  const query = document.getElementById("query").value;
  if (!query.trim()) {
    alert("Please enter a search query.");
    return;
  }
  try {
    const response = await fetch("/api/search_memory", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ query: query })
    });
    const data = await response.json();
    const outputDiv = document.getElementById("searchResults");
    outputDiv.innerHTML = "";
    if (data.results && data.results.length > 0) {
      data.results.forEach(item => {
        const p = document.createElement("p");
        p.textContent = item.summary;
        outputDiv.appendChild(p);
      });
    } else {
      outputDiv.textContent = "No results found.";
    }
  } catch (error) {
    console.error("Error searching memory:", error);
    alert("Error searching memory: " + error.message);
  }
}

// eligibility_viewer.js

async function compareEligibility() {
  const code = document.getElementById("eligibilityCode").value;
  const studentState = document.getElementById("studentState").value;
  const compareState = document.getElementById("compareState").value;
  if (!code.trim() || !studentState.trim() || !compareState.trim()) {
    alert("Please fill in all fields.");
    return;
  }
  try {
    const response = await fetch(`/api/compare_eligibility/${code}/${studentState}/${compareState}`);
    if (!response.ok) throw new Error("Failed to compare eligibility.");
    const data = await response.json();
    const outputDiv = document.getElementById("eligibilityOutput");
    outputDiv.innerHTML = `
      <h3>Eligibility Code: ${data.code}</h3>
      <h4>${data.state1_code} Criteria</h4>
      <p>${data.state1_criteria ? data.state1_criteria.definition : "No data found."}</p>
      <h4>${data.state2_code} Criteria</h4>
      <p>${data.state2_criteria ? data.state2_criteria.definition : "No data found."}</p>
    `;
  } catch (error) {
    console.error("Error comparing eligibility:", error);
    alert("Error comparing eligibility: " + error.message);
  }
}

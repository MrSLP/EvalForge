// students.js

async function addStudent() {
  const name = document.getElementById("name").value;
  const dob = document.getElementById("dob").value;
  const state = document.getElementById("state").value;
  const district = document.getElementById("district").value;
  const ard = document.getElementById("ard").value;
  const iep = document.getElementById("iep").value;
  const eligibilities = document.getElementById("eligibilities").value;

  if (!name || !dob) {
    alert("Name and DOB are required.");
    return;
  }

  try {
    const response = await fetch("/api/students", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        name: name,
        dob: dob,
        state: state,
        district: district,
        ard_date: ard,
        iep_date: iep,
        eligibilities: eligibilities.split(",").map(e => e.trim()).filter(e => e)
      })
    });
    if (!response.ok) throw new Error("Failed to add student.");
    document.getElementById("addStudentForm").reset();
    loadStudents();
  } catch (error) {
    console.error("Error adding student:", error);
    alert("Error: " + error.message);
  }
}

async function loadStudents() {
  try {
    const response = await fetch("/api/students");
    if (!response.ok) throw new Error("Failed to load students.");
    const students = await response.json();
    const tableBody = document.querySelector("#studentTable tbody");
    tableBody.innerHTML = "";
    if (students.length === 0) {
      const row = tableBody.insertRow();
      const cell = row.insertCell();
      cell.colSpan = 8;
      cell.textContent = "No students found.";
    } else {
      students.forEach(student => {
        const row = tableBody.insertRow();
        row.insertCell().textContent = student.id || "N/A";
        row.insertCell().textContent = student.name || "";
        row.insertCell().textContent = student.dob || "";
        row.insertCell().textContent = student.ard_date || "";
        row.insertCell().textContent = student.iep_date || "";
        row.insertCell().textContent = student.state || "";
        row.insertCell().textContent = student.district || "";
        row.insertCell().textContent = (student.eligibilities || []).join(", ");
      });
    }
  } catch (error) {
    console.error("Error loading students:", error);
  }
}

document.addEventListener("DOMContentLoaded", loadStudents);

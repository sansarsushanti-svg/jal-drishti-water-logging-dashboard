const wardData = [
    { ward: "Rajouri Garden", risk: "Red", status: "Severe" },
    { ward: "Lajpat Nagar", risk: "Yellow", status: "Moderate" },
    { ward: "Karol Bagh", risk: "Red", status: "Severe" },
    { ward: "Dwarka", risk: "Green", status: "Resolved" },
    { ward: "Rohini", risk: "Yellow", status: "Moderate" },
    { ward: "Saket", risk: "Red", status: "Severe" }
];

const table = document.getElementById("wardTable");

wardData.forEach(item => {
    const row = document.createElement("tr");

    row.innerHTML = `
        <td>${item.ward}</td>
        <td class="${item.risk.toLowerCase()}">${item.risk}</td>
        <td>${item.status}</td>
    `;

    table.appendChild(row);
});


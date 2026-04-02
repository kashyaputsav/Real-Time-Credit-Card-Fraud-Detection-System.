document.getElementById("fraudForm").addEventListener("submit", async function(e) {
    e.preventDefault();

    const data = {
        Amount: parseFloat(document.getElementById("amount").value),
        Time: parseFloat(document.getElementById("time").value)
    };

    const response = await fetch("http://127.0.0.1:8000/predict", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(data)
    });

    const result = await response.json();

    document.getElementById("result").innerText =
        `Fraud Probability: ${result.fraud_probability.toFixed(2)} | Prediction: ${result.prediction}`;
});
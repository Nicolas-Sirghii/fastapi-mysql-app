document.getElementById("btn").addEventListener("click", async () => {
    const res = await fetch("/api/message");
    const data = await res.json();
    document.getElementById("msg").innerText = data.message;
});
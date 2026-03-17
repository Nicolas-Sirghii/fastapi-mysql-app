// const HOST = "http://127.0.0.1:8000"
const HOST = "/api"





document.getElementById("btn").addEventListener("click", async () => {
    const res = await fetch(`${HOST}/message`);
    const data = await res.json();
    document.getElementById("msg").innerText = data.message;
});




document.getElementById("gre").addEventListener("click", async () => {
    const res2 = await fetch(`${HOST}/griting`);
    const data2 = await res2.json();
    document.getElementById("sec").innerText = data2.griting;
});
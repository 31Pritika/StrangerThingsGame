const music = document.getElementById("bg-music");

const saved = localStorage.getItem("musicTime");

if (saved){
    music.currentTime = parseFloat(saved);
}

windows.addEventListener("beforeunload", () => {
    localStorage.setItem("musicTime", music.currentTime);
});
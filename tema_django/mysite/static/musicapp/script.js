document.addEventListener("DOMContentLoaded", () => {
    const songItems = document.querySelectorAll("li");
    const player = document.getElementById("player");

    songItems.forEach(song => {
        song.addEventListener("click", () => {
            const youtubeUrl = song.dataset.youtubeUrl;
            player.innerHTML = `
                <iframe width="560" height="315" src="${youtubeUrl}?autoplay=1" frameborder="0" allowfullscreen></iframe>
            `;
        });
    });
});

let player;

function onYouTubeIframeAPIReady() {
    player = new YT.Player('player', {
        height: '390',
        width: '640',
        videoId: '', // Initially empty, will be set when a song is clicked
        events: {
            'onReady': onPlayerReady,
        }
    });
}

function onPlayerReady(event) {
    // The player is ready, you can add any additional functionality here if needed
}

document.addEventListener("DOMContentLoaded", () => {
    const songItems = document.querySelectorAll("li");

    songItems.forEach(song => {
        song.addEventListener("click", () => {
            const youtubeUrl = song.dataset.youtubeUrl;
            const videoId = youtubeUrl.split('/').pop(); // Extract the videoId from the YouTube URL
            player.loadVideoById(videoId); // Load the video into the player
        });
    });
});

function addSong(title, artist, youtubeUrl) {
    const li = document.createElement("li");
    li.textContent = `${artist} - ${title}`;
    li.dataset.youtubeUrl = youtubeUrl;
    li.addEventListener("click", () => {
        const videoId = youtubeUrl.split("/").pop();
        player.loadVideoById(videoId);
    });
    document.querySelector("ul").appendChild(li);
}

document.getElementById("search-form").addEventListener("submit", async (event) => {
    event.preventDefault();
    const query = document.getElementById("query").value;
    if (!query) return;

    const response = await fetch(`/search/?query=${encodeURIComponent(query)}`);
    const data = await response.json();
    if (data.youtube_url) {
        const searchResult = document.getElementById("search-result");
        const title = prompt("Enter song title:");
        const artist = prompt("Enter artist name:");
        addSong(title, artist, data.youtube_url);

        // Save the song to the database
        const formData = new FormData();
        formData.append("title", title);
        formData.append("artist", artist);
        formData.append("youtube_url", data.youtube_url);
        fetch("/", { method: "POST", body: formData });
    } else {
        alert("No results found");
    }
});
const API_URL = "https://api4.binance.com/api/v3/ticker/24hr";

const coinTableBody = document.getElementById("coinTableBody");
const searchInput = document.getElementById("searchInput");
const allBtn = document.getElementById("allBtn");
const favBtn = document.getElementById("favBtn");

let coins = [];
let favorites = JSON.parse(localStorage.getItem("favorites")) || [];
let currentTab = "all";

async function fetchCoins() {
    try {
        const response = await fetch(API_URL);
        const data = await response.json();

        coins = data.filter(function (coin) {
            return coin.symbol.endsWith("USDT");
    });

    renderCoins();
} catch (error) {
    console.log("API 요청 실패:", error);
    }
}

function renderCoins() {
    const searchText = searchInput.value.toUpperCase();

    let filteredCoins = coins.filter(function (coin) {
        return coin.symbol.includes(searchText);
    });

    if (currentTab === "favorite") {
        filteredCoins = filteredCoins.filter(function (coin) {
            return favorites.includes(coin.symbol);
        });
    }

    coinTableBody.innerHTML = "";

    filteredCoins.forEach(function (coin) {
        const changeRate = Number(coin.priceChangePercent);
        const changeClass = changeRate >= 0 ? "up" : "down";
        const isFavorite = favorites.includes(coin.symbol);

    const row = `
        <tr>
            <td>
                <span 
                    class="star ${isFavorite ? "active" : ""}" 
                    onclick="toggleFavorite('${coin.symbol}')"
                >
                ★
            </span>
            </td>
            <td class="symbol">${coin.symbol}</td>
            <td>${Number(coin.lastPrice).toLocaleString()}</td>
            <td class="${changeClass}">${changeRate.toFixed(2)}%</td>
            <td>${Number(coin.highPrice).toLocaleString()}</td>
            <td>${Number(coin.lowPrice).toLocaleString()}</td>
        </tr>
    `;

    coinTableBody.innerHTML += row;
    });
}

function toggleFavorite(symbol) {
    if (favorites.includes(symbol)) {
        favorites = favorites.filter(function (item) {
            return item !== symbol;
        });
    } else {
        favorites.push(symbol);
    }

    localStorage.setItem("favorites", JSON.stringify(favorites));
    renderCoins();
}

searchInput.addEventListener("input", function () {
    renderCoins();
});

allBtn.addEventListener("click", function () {
    currentTab = "all";
    allBtn.classList.add("active");
    favBtn.classList.remove("active");
    renderCoins();
});

favBtn.addEventListener("click", function () {
    currentTab = "favorite";
    favBtn.classList.add("active");
    allBtn.classList.remove("active");
    renderCoins();
});

fetchCoins();
setInterval(fetchCoins, 1000);
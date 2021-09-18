let title = document.getElementsByClassName("title")[0];
let contenttext = document.getElementsByClassName("text")[0];
function sortAll() {
    title.innerHTML = "All";
    let i = 0;
    if (cards[0]) {
        let t = setInterval(() => {
            cards[i].style.display = "flex";
            cards[i].style.opacity = 1;
            i++;
            if (i >= cards.length) { clearInterval(t); }
        }, 100);
    }
    else
        contenttext.innerHTML = "No Scholarships available currently.";
}
function sortApplied() {
    title.innerHTML = "Applied";
    let removed = [];
    let i = 0;
    while (i < cards.length) {
        if (!cards[i].children[0].innerHTML.includes("applied")) {
            cards[i].style.opacity = 0;
            removed.push(cards[i]);
        }
        else {
            cards[i].style.opacity = 1;
            cards[i].style.display = "flex";
        }
        i++;
    }
    setTimeout(() => {
        while (removed[0]) {
            removed.shift().style.display = "none";
            i--;
        }
    }, 500);
    if (!i)
        contenttext.innerHTML = "No Scholarships available currently.";
    else
        contenttext.innerHTML = "";
}
function sortUpcoming() {
    title.innerHTML = "Upcoming";
    let removed = [];
    let i = 0;
    while (i < cards.length) {
        if (!cards[i].children[0].innerHTML.includes("upcoming")) {
            cards[i].style.opacity = 0;
            removed.push(cards[i]);
        }
        i++;
    }
    setTimeout(() => {
        while (removed[0]) {
            removed.shift().style.display = "none";
            i--;
        }
        if (!i)
            contenttext.innerHTML = "No Scholarships available currently.";
        else
            contenttext.innerHTML = "";
    }, 500);
}

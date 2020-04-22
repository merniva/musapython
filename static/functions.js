
// new search by searchword from infobox
function newSearch(haettava) {
    let siivottuArvo = haettava
        .replace(" & ", "&")
        .replace(" + ", "+");
    document.getElementById("close").click();
    document.getElementById("searchfield").value = siivottuArvo;
    document.getElementById("searchbutton").click();
    moveUp();
}

// show results from Artist search
function showArtist(artisti, naytaTiedot) {
    let laatikko = document.createElement("div");
    laatikko.innerHTML = `
        <div class='resultbox'>
        <a>
            <img src="../static/black-1296338_640.png" alt="artistin default-kuva" width="150" height="150"></img>
            <h3>${artisti.name}</h3>
        </a>
        <button id="seemore">Katso lisää</button>
        </div>
        `;
    laatikko.onclick=()=> naytaTiedot(artisti.name)
    document.getElementById('results').appendChild(laatikko)
}


// show results from Album search
function showAlbum(albumi, naytaTiedot) {
    let laatikko = document.createElement("div");
    laatikko.innerHTML = `
        <div class='resultbox'>
        <a>
            <img src="${albumi.image[2]["#text"]}" width="160" height="160"></img>
            <h3>${albumi.artist.name}:<br></h3>
            <p class = "searchresult">${albumi.name}</p>
        </a>
        <button id="seemore">Katso lisää</button>
        </div>
        `;
    laatikko.onclick=()=> naytaTiedot(albumi.name, albumi.artist.name)
    document.getElementById('results').appendChild(laatikko)
}

// show back to top-button
function scrollFunction(showUpButton) {
    if (document.body.scrollTop > 50 || document.documentElement.scrollTop > 50) {
      showUpButton.style.display = "block";
    } else {
      showUpButton.style.display = "none";
    }
  }
  
  // move back to top
function moveUp() {
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
}
  
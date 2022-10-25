console.log('f*** yeah DBS TCG')
const URL = "https://pokeapi.co/api/v2/pokemon/"

function get_poke(event) {
    event.preventDefault()
    console.log("submitted")
    const pokeResultDiv = document.querySelector("#pokeResult")
    pokeResultDiv.innerHTML = "Loading...."
    const pokeName = document.querySelector("#pokeName").value
    console.log(pokeName)
    fetch(URL + pokeName)
        .then(response => response.json())
        .then(pokeData => {
            console.log(pokeData)
            pokeResultDiv.innerHTML = `
            <h3> number ${pokeData.id} ${pokeData.name}</h3>
            <img src="${pokeData.sprites.front_default}">
            <h2> Type(s): </h2>
            `
            for (type of pokeData.types) {
                console.log(type.type.name)
                pokeResultDiv.innerHTML += `<p>${type.type.name}</p>`
            }
        })
        .catch(err => SVGComponentTransferFunctionElement.log(err))
}

async function randPoke(event) {
    console.log("connected Func")
    const pokeResultDiv = document.querySelector("#pokeResult")
    pokeResultDiv.innerHTML = "Loading...."
    let rand = Math.floor(Math.random() * 905)
    let response = await fetch(URL + rand)
    let pokeData = await response.json()
    console.log(pokeData)
    pokeResultDiv.innerHTML = `
    <h3> number ${pokeData.id} ${pokeData.name}</h3>
    <img src="${pokeData.sprites.front_default}">
    <h2> Type(s): </h2>
    `
    for (type of pokeData.types) {
        console.log(type.type.name)
        pokeResultDiv.innerHTML += `<p>${type.type.name}</p>`
    }
}
const myChoice = 'Rock'
const enemyChoice = 'Scissors' 
let random = Math.floor(Math.random()*3);
let chosenOne = weapons[random];

const weapons = {
   Rock: {weakTo: 'Paper', strongTo: 'Scissors'},
   Paper: {weakTo: 'Scissors', strongTo: 'Rock'},
   Scissors: {weakTo: 'Rock', strongTo: 'Paper'}
}

if (weapons[myChoice].strongTo === enemyChoice) {
    // I won
    return;
}

if (weapons[myChoice].weakTo === enemyChoice) {
    // I Lost
    return;
}

// tie

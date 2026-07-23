// REAL LIFE EXAMPLE: KATAMARAN
// Kung may gana ko,
// manglimpyo ko kwarto.
// Kung wala gana,
// tan-awon ko kung may bisita.
// Kung may bisita,
// mapanglimpyo gid ko.
// Pero kung wala man,
// buwas na lang. 😂

let mayGana = false;
let mayBisita = false;

const readline = require("readline");

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.question("May gana ka maglimpyo? (hou/wala): ", (answer) => {
    mayGana = answer.toLowerCase() === "hou";

    if (mayGana) {
        console.log("Manglimpyo ta bala.");
        rl.close();
    } else {
        rl.question("May bisita nga maabot? (hou/wala): ", (answer) => {
            mayBisita = answer.toLowerCase() === "hou";

            if (mayBisita) {
                console.log("Wala choice, manglimpyo dulang.");
            } else {
                console.log("May bwas pa ah.");
            }

            rl.close();
        });
    }
});
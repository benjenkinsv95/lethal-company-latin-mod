import romanNumerals from 'roman-numerals';
import yada from './lookup.json' assert { type: "json" };
import fs from 'fs';

console.log('yada')

function capitalizeFirstWord(s) {
    if (!s) return s;
    let words = s.split(" ");
    words[0] = words[0].charAt(0).toUpperCase() + words[0].slice(1);
    return words.join(" ");
}

function aureusOrAurei(num) {
    return num > 1 ? "aureī" : "aureus";
}

function generateTranslationPatterns(maxNum, filename) {
    let data = "";
    for (let i = 0; i <= maxNum; i++) {
        let roman = romanNumerals.toRoman(i);
        let latinWord = capitalizeFirstWord(yada[`${i}`].Cardinal);
        let aureus_plural = aureusOrAurei(i);
        let pattern = `r:"^\\$${i}$"=<size=10>${roman} AU</size>\\n<size=8>(${latinWord} ${aureus_plural})</size>\n`;
        data += pattern;
    }
    fs.writeFileSync(filename, data, 'utf8');
}

// Generate patterns up to 3,999 and write to money.txt
generateTranslationPatterns(3999, "money.txt");

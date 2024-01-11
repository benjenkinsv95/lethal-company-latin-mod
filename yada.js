import romanNumerals from 'roman-numerals';
import yada from './lookup.json' assert { type: "json" };
import fs from 'fs';

console.log('yada')

function capitalizeFirstWord(s) {
    if (!s) return s;
    let words = s.split(" ");
    words[0] = words[0].charAt(0).toUpperCase() + words[0].slice(1).toLowerCase();
    return words.join(" ");
}

function aureusOrAurei(num) {
    return num > 1 ? "aureī" : "aureus";
}

function generateTranslationPatterns(maxNum, filename, createPattern) {
    let data = "";
    for (let i = 0; i <= maxNum; i++) {
        let roman = romanNumerals.toRoman(i);
        let cardinalWord = capitalizeFirstWord(yada[`${i}`].Cardinal);
        let ordinalWord = capitalizeFirstWord(yada[`${i}`].Ordinal);
        let aureus_plural = aureusOrAurei(i);
        let pattern = createPattern(i, roman, cardinalWord, ordinalWord, aureus_plural);
        data += pattern;
    }
    fs.writeFileSync(filename, data, 'utf8');
}

const convertToMasculine = (words, num) => {
    const ending = num > 1 ? "ī" : "us";

    const wordsArr = words.split(' ');
    const masculineWords = wordsArr.map(word => {
        if (word.endsWith('a')) {
            return word.slice(0, word.length - 'a'.length) + ending;
        } else if (word.endsWith('um')) {
            return word.slice(0, word.length - 'um'.length) + ending;
        } else {
            return word;
        }
    })
    return masculineWords.join(' ')
}

const convertToFeminine = (words, num) => {


    const ending = num > 1 ? "ae" : "a";

    const wordsArr = words.split(' ');
    const masculineWords = wordsArr.map(word => {
        if (word.toLowerCase() === 'centum') return word;
        if (word === 'duo') return 'duae'
        if (word === 'tria') return 'trēs'
        if (word === 'Duo') return 'Duae'
        if (word === 'Dria') return 'Trēs'

        if (word.endsWith('us')) {
            return word.slice(0, word.length - 'us'.length) + ending;
        } else if (word.endsWith('um')) {
            return word.slice(0, word.length - 'um'.length) + ending;
        } else {
            return word;
        }
    })
    return masculineWords.join(' ')
}

const convertToNeuter = words => {
    const wordsArr = words.split(' ');
    const masculineWords = wordsArr.map(word => {
        if (word.endsWith('a')) {
            return word.slice(0, word.length - 'a'.length) + 'um';
        } else if (word.endsWith('us')) {
            return word.slice(0, word.length - 'us'.length) + 'um';
        }
    })
    return masculineWords.join(' ')
}

function generateTimeTranslationPatterns(filename) {
    let data = "";
    for (let hour = 1; hour <= 12; hour++) {
        for (let minutes = 0; minutes <= 59; minutes++) {
            const paddedMinutes = String(minutes).padStart(2, '0');

            let hourOrdinal = yada[`${hour}`].Ordinal.toLowerCase();
            let minutesOrdinal = convertToNeuter(yada[`${minutes}`].Ordinal.toLowerCase()).replace(' ', '\\n');

            const amPattern = `r:"^${hour}:\\s*${paddedMinutes}\\s*AM"=<size\\=14>Hora ${hourOrdinal}\\nmomentum</size>\\n<size\\=11>${minutesOrdinal} AM</size>\n`
            const pmPattern = `r:"^${hour}:\\s*${paddedMinutes}\\s*PM"=<size\\=14>Hora ${hourOrdinal}\\nmomentum</size>\\n<size\\=11>${minutesOrdinal} PM</size>\n`

            data += amPattern;
            data += pmPattern;
        }
    }
    fs.writeFileSync(filename, data, 'utf8');
}

// Generate patterns up to 3,999 and write to money.txt
generateTranslationPatterns(3999, "money.txt", createMoneyPattern);
generateTranslationPatterns(3999, "weight.txt", createWeightPattern);
generateTranslationPatterns(3999, "weight-nota.txt", createWeightWithNotesPattern);
// generateTimeTranslationPatterns('time.txt')

function createMoneyPattern(i, roman, cardinalWord, ordinalWord, aureus) {
    const money = i === 0 ? capitalizeFirstWord(convertToMasculine(roman, i)) : roman;
    return `r:"^\\$${i}$"=<size\\=15>${money} AU</size>\n`;
}

function createWeightPattern(i, roman, cardinalWord, ordinalWord, aureus_plural) {
    const weight = i === 0 ? capitalizeFirstWord(roman) : roman;
    if (i === 0) {
        return `r:"^${i} lb$"=<size\\=18>${weight} lb</size>\n`;
    }
    const cardinal = convertToFeminine(cardinalWord, i);
    const ordinal = convertToFeminine(ordinalWord, i)

    return `r:"^${i} lb$"=<size\\=18>${roman} lb</size>\\n<size\\=12>${cardinal} lb</size>\n`;
}

function createWeightWithNotesPattern(i, roman, cardinalWord, ordinalWord, aureus_plural) {
    const weight = i === 0 ? capitalizeFirstWord(roman) : roman;
    if (i === 0) {
        return `r:"^${i} lb$"=<size\\=18>${weight} lb</size>\n`;
    }
    const cardinal = convertToFeminine(cardinalWord, i);
    const ordinal = convertToFeminine(ordinalWord, i)

    return `r:"^${i} lb$"=<size\\=18>${roman} lb</size>\\n\\n<size\\=13>Nota grammaticae:\\n\'${cardinal}\' est numerus, cuius ordinalis est \'${ordinal}\'</size>\n`;
}
// <size\=18>CLVI lb</size>\n<size\=10>Centum quīnquāgintā sex lb</size><size\=9>\n\nCentēsima quīnquāgēsima sexta libra portata est</size>




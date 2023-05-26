import fetch from "node-fetch";
import cheerio from "cheerio"
// function to get the raw data
const getRawData = (URL) => {
   return fetch(URL)
      .then((response) => response.text())
      .then((data) => {
         return data;
      });
}

const URL = "https://buff.163.com/market/csgo#tab=selling&page_num=1";

// start of the program
const getSiteInfo = async () => {
    const RawData = await getRawData(URL);
    const parsedData = cheerio.load(RawData)

    const itemArea = parsedData('li, .card_csgo').text()
    console.log(itemArea);
}

// invoking the main function
getSiteInfo();
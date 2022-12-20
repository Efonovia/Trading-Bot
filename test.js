import fetch from "node-fetch";

// function to get the raw data
const getRawData = (URL) => {
   return fetch(URL)
      .then((response) => response.text())
      .then((data) => {
         return data;
      });
}

const URL = "https://en.wikipedia.org/wiki/Cricket_World_Cup";

// start of the program
const getSiteInfo = async () => {
   const RawData = await getRawData(URL);
   console.log(RawData);
}

// invoking the main function
getSiteInfo();
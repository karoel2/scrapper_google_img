var Scraper = require('images-scraper');
fs = require('fs');
var args = process.argv.slice(2);
var web = args[0];
var amount = args[1];
const google = new Scraper({
  puppeteer: {
    headless: false,
  },
});

(async () => {
  var results = await google.scrape(web.toString(), parseInt(amount,10));
  var res = results

  fs.writeFile('data.json', JSON.stringify(res), function (err) {
    if (err) return console.log(err);
    console.log('Done!');
  });
})();

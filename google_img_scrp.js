var Scraper = require('images-scraper');
fs = require('fs');
var args = process.argv.slice(2);
var amount = args.slice(-1)[0];
var web = args.join(' ').replace(amount, '')
console.log(web);
console.log(amount);

const google = new Scraper({
  puppeteer: {
    headless: true,
  },
});

(async () => {
  var results = await google.scrape(web, parseInt(amount,10));
  var res = results

  fs.writeFile('data.json', JSON.stringify(res), function (err) {
    if (err) return console.log(err);
    console.log('Done!');
  });
})();

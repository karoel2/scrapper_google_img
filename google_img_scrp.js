var Scraper = require('images-scraper');
fs = require('fs');

const google = new Scraper({
  puppeteer: {
    headless: false,
  },
});

(async () => {
  var results = await google.scrape('desert', 50);
  var res = results

  fs.writeFile('data.json', JSON.stringify(res), function (err) {
    if (err) return console.log(err);
    console.log('Done!');
  });
})();

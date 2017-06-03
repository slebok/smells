TOP_TEXT = "<html><meta charset=\"UTF-8\"><meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">" +\
    "<meta name=\"description\" content=\"An attempt to present a taxonomy of software smells by cataloging, classifying, and " +\
                    "inter-relating smell definitions present in existing literature.\">" +\
    "<meta name=\"keywords\" content=\"Code smells, architecture smells, database smells, configuration smells, test smells, catalog, taxonomy, classification\">" +\
"<link rel=\"stylesheet\" href=\"https://www.w3schools.com/w3css/4/w3.css\">" +\
"<link rel=\"stylesheet\" href=\"https://fonts.googleapis.com/css?family=Poppins\">"\
"<style>body,h1,h2,h3,h4,h5 {font-family: \"Poppins\", sans-serif}" +\
"body {font-size: 16px;}" +\
    ".w3-half img {margin-bottom: -6px;margin-top: 16px;opacity: 0.8;cursor: pointer}" +\
    ".w3-half img:hover {opacity: 1}"+\
"</style>"+\
"<head><title>A Taxonomy of Software Smells</title></head>"

BODY_TOP_PART = "<body>" +\
    "<nav class=\"w3-sidebar w3-gray w3-collapse w3-top w3-large w3-padding\" style=\"z-index:3;width:300px;font-weight:bold;\" id=\"mySidebar\"><br>" +\
        "<div class=\"w3-container\">" +\
            "<h3 class=\"w3-padding-64\"><b>A Taxonomy of Software Smells</b></h3></div>" +\
        "<div class=\"w3-bar-block\">"

BODY_INDEX = "<a href=\"index.html\" class=\"w3-bar-item w3-button w3-hover-white\">Home</a>"

BODY_LOW_PART = "</div>" +\
        "<hr>" +\
        "<div class=\"w3-bar-block\"><a href=\"http://www.tusharma.in\" class=\"w3-bar-item w3-button w3-hover-white\">Tushar's Blog</a></div>" +\
        "<hr>" +\
        "<div class=\"w3-bar-block\"><a href=\"http://bit.ly/DesignSmells\"><img src=\"book_cover.png\" style=\"width:220px;\"></a></div>" +\
        "<hr>" +\
        "<div>Detect smells using Designite<a href=\"http://www.designite-tools.com\"><img src=\"designite.png\" style=\"width:220px;\"></a></div>" +\
    "<hr></nav>"

BODY_MAIN_TOP = "<div class=\"w3-main\" style=\"margin-left:340px;margin-right:40px\">"

ATTRIBUTION_TEXT = "<div class=\"w3-light-grey w3-container w3-padding-32\" style=\"margin-top:75px;padding-right:58px\">"+\
                   "<p class=\"w3-right\">All rights reserved (c) <a href=\"http://www.tusharma.in\">Tushar Sharma</a> 2017.</p></div>"
HTML_END_TEXT = "</body></html>"

TRACKING_TEXT = "<script>" +\
  "(function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){" +\
  "(i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o)," +\
  "m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)" +\
  "})(window,document,'script','https://www.google-analytics.com/analytics.js','ga');" +\
  "ga('create', 'UA-56403135-3', 'auto');" +\
  "ga('send', 'pageview');"+\
"</script>"

SOCIAL_TEXT = "<script type=\"text/javascript\" src=\"//s7.addthis.com/js/300/addthis_widget.js#pubid=ra-592f963a3394864d\"></script>"

ADDITIONAL_TEXT = "<p>This taxonomy is evolving. I plan to add more smells and populate other relevant information such as tool support. " +\
    "If you would like to see something relevant which is currently missing, feel free to offer a pull request. " +\
    "<b>Here is the URL to the <a href=\"https://github.com/tushartushar/smells\">open-source repository</a></b>. " +\
    "You may also contact me at tusharsharma@ieee.org.</p>"

ACKOWLEDGEMENTS = "<p><h4>Acknowledgements:</h4> I would like to thank Prof. Diomidis Spinellis for suggesting me many improvements.</p>" +\
    "<p>My sincere thanks to the following contributors: Neil Ernst.</p>"

HOW_TEXT = "<p>The taxonomy is generated by a python program that I wrote to generate html pages. " +\
                   "I provide smell description as well as corresponding references in a specific format and " +\
                   "supply them to the python program. The program generates required html pages with links " +\
                   "that inter-relate the generated html pages. I used basic CSS to look the collection of the html files a little better.</p>"

INTRO_TEXT = "<h1>A Taxonomy of Software Smells</h1>" +\
            "<img src=\"smells.png\" style=\"width:700px;\">" +\
        "<p>Kent Beck coined the term \"code smell\" in the popular <a href=\"http://amzn.to/2rblDm3\" target=\"_blank\"> " +\
                    "Refactoring book by Martin Fowler</a> and defined it informally as certain structures in the code " +\
                    "that suggest (sometimes they scream for) the possibility of refactoring. " +\
                    "Since then, various smells have been reported that impair software quality in one or more ways. " +\
                    "I attempt to prepare and present a taxonomy of software smells by cataloging, classifying, and " +\
                    "inter-relating smell definitions present in existing literature with their references.</p>"

function loadData() {

    var $body = $('body');
    var $wikiElem = $('#wikipedia-links');
    var $nytHeaderElem = $('#nytimes-header');
    var $nytElem = $('#nytimes-articles');
    var $greeting = $('#greeting');

    // clear out old data before new request
    $wikiElem.text("");
    $nytElem.text("");

    // assign streetStr to value of the text inputed in the form with id="street"
    var streetStr = $('#street').val();
    var cityStr  = $('#city').val();
    // create full address
    var address = streetStr + ', ' + cityStr;
    console.log(address);

    $greeting.text('Do you want to live in ' + address + '?');

    //create URL
    var streetviewUrl = 'http://maps.googleapis.com/maps/api/streetview?size=600x300&location=' + address + '';
    $body.append('<img class="bgimg" src="' + streetviewUrl + '"/>');
    return false;

    var streetviewURL = 'https://maps.googleapis.com/maps/api/streetview?size=600x400&location=' + loc + '&key=AIzaSyD26gIGcZOJpPCBDGVrQLt_Pwhcl56nzE4';
    $body.append('<img class="bgimg" src="'+ streetviewURL + '">');


    // New York Times Articles
    var nytimesUrl = 'http://api.nytimes.com/svc/search/v2/articlesearch.json?q='+ cityStr + '&sort=newest&api-key=2c73c53d428343089d7481de12b1f645';
    $.getJSON(nytimesUrl, function(data){
        $nytHeaderElem.text('New York Times Articles About ' + cityStr);
        articles = data.response.docs;
        for (var i = 0; i < articles.length; i++) {
            var article = articles[i];
            $nytElem.append('<li class="article">'+
                '<a href="'+article.web_url+'">'+article.headline.main+'</a>'+
                '<p>' + article.snippet + '</p>'+
                '</li>');
            };
    }).error(function(e){
        $nytHeaderElem.text('New York Times Articles Could Not Be Loaded');
    });



    return false;
};



// when user clicks submit the loadData function will run
$('#form-container').submit(loadData);

//API: 2c73c53d428343089d7481de12b1f645
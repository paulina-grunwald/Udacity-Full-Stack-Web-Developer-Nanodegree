
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

    $greeting.text('Do you want to live in ' + address + '?');

    //create URL
    var streetviewUrl = 'http://maps.googleapis.com/maps/api/streetview?size=600x300&location=' + address + '';
    $body.append('<img class="bgimg" src="' + streetviewUrl + '"/>');
    return false;
};

// when user clicks submit the loadData function will run
$('#form-container').submit(loadData);

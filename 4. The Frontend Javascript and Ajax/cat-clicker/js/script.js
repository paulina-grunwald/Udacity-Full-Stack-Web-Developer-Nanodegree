
var elem = document.getElementById('img');
var i = 0;
elem.addEventListener('click', function(){
  i++
  console.log(i);
  document.getElementById("count").innerHTML = i;
}, false);



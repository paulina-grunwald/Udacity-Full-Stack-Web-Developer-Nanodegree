
var elemMisza = document.getElementById('Misza');
var elemChewie = document.getElementById('Chewie');
var i = 0;

elemChewie.addEventListener('click', function(){
  i++
  console.log(i);
  document.getElementById("count1").innerHTML = i;
 }, false);

elemMisza.addEventListener('click', function(){
  i++
  console.log(i);
  document.getElementById("count2").innerHTML = i;
 }, false);




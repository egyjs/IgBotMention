// open `https://www.instagram.com/{username}/followers/` and paste this code in console:


  var div = document.querySelector('.isgrP');
  div.scrollTop = div.scrollHeight - div.clientHeight;
  var El = document.getElementsByClassName('FPmhX');
  var i;
  var list = ''
  for (i = 0; i < El.length; i++) {
    list += El[i].innerText + "\n";
  }
  console.log(list)
  // save as list.txt
  create(list, "list.txt");
  function create(text, name) {
    let a = document.createElement('a');
    a.href = "data:text/plain,"+encodeURIComponent(text);
    a.download = name;
    a.click();
  }

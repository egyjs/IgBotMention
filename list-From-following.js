// open `https://www.instagram.com/[username]/followers/` and paste this code in console:

  function sleep(milliseconds) {
    var start = new Date().getTime();
    for (var i = 0; i < 1e7; i++) {
      if ((new Date().getTime() - start) > milliseconds){
        break;
      }
    }
  }
  function create(text, name) {
    let a = document.createElement('a');
    a.href = "data:text/plain,"+encodeURIComponent(text);
    a.download = name;
    a.click();
  }

//   var div = document.querySelector('.isgrP');
//   div.scrollTop = div.scrollHeight - div.clientHeight;
//   div.scrollTop = div.scrollHeight - div.clientHeight;
//   div.scrollTop = div.scrollHeight - div.clientHeight;
//   div.scrollTop = div.scrollHeight - div.clientHeight;
//   div.scrollTop = div.scrollHeight - div.clientHeight;
//   div.scrollTop = div.scrollHeight - div.clientHeight;
//   div.scrollTop = div.scrollHeight - div.clientHeight;
//   div.scrollTop = div.scrollHeight - div.clientHeight;
  sleep(6000);
  var El = document.querySelectorAll('a[title]')
  var i;
  var list = ''
  for (i = 0; i < El.length; i++) {
    list += El[i].text + "\n";
  }
  console.log(list)
  // save as list.txt
  create(list, "list.txt");


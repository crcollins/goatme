var xmlhttp = new XMLHttpRequest();
xmlhttp.open('GET','http://localhost:4000/fetch?url='+document.URL, true);
xmlhttp.send();
xmlhttp.onreadystatechange=function()
  {
  if (xmlhttp.readyState==4 && xmlhttp.status==200)
    {
	alert(xmlhttp.responseText);
    }
  }

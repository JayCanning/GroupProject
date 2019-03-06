function addFile(){

var data = "hello";
var xhr = new XMLHttpRequest();
xhr.withCredentials = true;
xhr.open('POST', 'admin');
xhr.send(data);
};
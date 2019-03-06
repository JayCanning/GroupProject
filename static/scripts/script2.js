function addFile(){
	var xhttp = new XMLHttpRequest();
	xhttp.onreadystatechange = function() {

	xhttp.open("POST", "admin");
	xhttp.send();
	}
};
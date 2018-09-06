var modal = document.getElementById('id02');
var modal1 = document.getElementById('id03');
var modal4 = document.getElementById('id04');
var modal5= document.getElementById('id05');

window.onclick = function (event) {
    if (event.target == modal || event.target==modal1 || event.target == modal4 || event.target == modal5  ) {
        modal.style.display = "none";
    }
}


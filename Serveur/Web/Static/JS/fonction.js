var bouton_capture = document.getElementById("capture");
let radar = document.getElementById("radar");

function updateRadar(){
    fetch('/radar')
    .then(response=>response.json())
    .then(data=>{
        radar.textContent="distance : "+data["val"]
    });
}

bouton_capture.onclick = function(){
    console.log("test")
    var xhr=new XMLHttpRequest();
    xhr.open("POST","/capture");
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.send(null);
}

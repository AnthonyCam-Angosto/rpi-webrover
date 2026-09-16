let gamepads = {};
let launch=false;
let radar = document.getElementById("radar");

let clicked=Array()

function gamepadHandler(event, connecting) {
    let gamepad = event.gamepad;

    if (connecting) {
    gamepads[gamepad.index] = gamepad;
    } else {
    delete gamepads[gamepad.index];
    }
    console.log(gamepads)

    if(connecting && !launch){
        launch=true
        for (const button of gamepad.buttons) {
            clicked.push(false)
        }
        setInterval(mainloop_button,100)
        mainloop()
    }
}

window.addEventListener("gamepadconnected",function (e) {gamepadHandler(e, true);},false,);
window.addEventListener("gamepaddisconnected",function (e) {gamepadHandler(e, false);},false,);

let x1=0
let y1=0
let x2=0
let y2=0

function mainloop(){
    let gp=gamepads[0];

    let axesV=gp.axes[0].toFixed(2)
    let axesH=gp.axes[1].toFixed(2)

    stick(axesV,axesH,true)


    let axesH2=gp.axes[2].toFixed(2)
    let axesV2=gp.axes[3].toFixed(2)

    stick(axesV2,axesH2,false)

    requestAnimationFrame(mainloop)
}

function mainloop_button(){
    let gp=gamepads[0];

    if(gp.buttons[3].pressed && clicked[3]==false){
        clicked[3]=true
        var xhr=new XMLHttpRequest();
        xhr.open("GET","/type?val=auto");
        xhr.send();
    }else{
        clicked[3]=false;
    }

    if(gp.buttons[2].pressed && clicked[2]==false){
        clicked[2]=true;
        var xhr=new XMLHttpRequest();
        xhr.open("GET","/type?val=rgb");
        xhr.send();
    }else{
        clicked[2]=false;
    }


    if(gp.buttons[7].pressed && clicked[7]==false && gp.buttons[7].value==1){
        clicked[7]=true;
        var xhr=new XMLHttpRequest();
        xhr.open("GET","/torch?val=True");
        xhr.send()
    }else{
        if(gp.buttons[7].value<0.8 && clicked[7]==true){
            var xhr=new XMLHttpRequest();
            xhr.open("GET","/torch?val=False");
            xhr.send()
            clicked[7]=false;   
        }
    }

}


function stick(axesV,axesH,left) {
    if(axesV<0.07 && axesV>-0.07){
        axesV=0.00
    }
    if(axesH<0.07 && axesH>-0.07){
        axesH=0.00
    }
    let tempx=null
    let tempy=null

    if(!left){
        if(axesV!=x2){
            x2=axesV
            tempx=x2
        }
        if(axesH!=y2){
            y2=axesH
            tempy=y2
        }
    }else{
        if(axesV!=x1){
            x1=axesV
            tempx=x1
        }
        if(axesH!=y1){
            y1=axesH
            tempy=y1
        }
    }

    if(tempx!=null || tempy!=null){
        var xhr=new XMLHttpRequest();
        if(left){
            xhr.open("POST","/deplacement");
        }else{
            xhr.open("POST","/rotate");
        }
        xhr.setRequestHeader("Content-Type", "application/json");

        let body;
        if(tempx==null){
            body = JSON.stringify({ vertical: null,horizontal:tempy});
        }
        else if(tempy==null){
            body = JSON.stringify({ vertical: tempx,horizontal:null});
        }
        else{
            body = JSON.stringify({ vertical: tempx,horizontal:tempy});
        }
        xhr.send(body);
    }
}
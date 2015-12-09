/**
 * Created by lxflxf on 12/8/15.
 */
$(function () {
    var username = $("#username");
    var password = $("#password");
    var yzCode = $("#yzCode");
    $("#btn-login").click(function () {
        if(username.val() == ""){
            username.focus();
        }else if(password.val() == ""){
            password.focus();
        }else if(yzCode.val() == ""){
            yzCode.focus();
        }else{

        }
    });

    $("#yzImg").click(function () {
       this.src =  'randomcode/'+Math.random();
    });

});
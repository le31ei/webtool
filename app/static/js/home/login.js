/**
 * Created by lxflxf on 12/8/15.
 */
$(function () {
    function yzCodeGet(){
        //验证码刷新

    }

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
            $.ajax({
                url:"login",
                type:"POST",
                contentType: "application/json",
                data:JSON.stringify({
                    username:username.val().trim(),
                    password:password.val().trim(),
                    yzCode:yzCode.val().trim()
                }),
                async:false,
                success: function (msg) {
                    if(msg.status == "success"){
                        window.location.href = msg.url;
                    }else{
                        $("#yzImg").click(); //验证码错误刷新
                        $("#error").html(msg.msg);
                    }
                }
            });
        }
    });

    $("#yzImg").click(function () {
        this.src = 'randomcode/'+Math.random();
    });





});
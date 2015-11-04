$(function () {
    $("#btn-login").click(function () {
        var username = $("#username");
        var password = $("#password")
        if(username.val() == ""){
            username.focus();
        }else if(password.val()==""){
            password.focus();
        }else{
            $.ajax({
                url:'/fcknsf/login',
                type:"POST",
                contentType: "application/json",
                data:JSON.stringify({
                    username:username.val().trim(),
                    password:password.val().trim()
                }),
                async:false,
                success: function (msg) {
                    if(msg.msg == "success"){
                        window.location.href = msg.url;
                    }else{
                        $("#error").html("用户名或密码错误");
                    }
                }
            });
        }
    });
});
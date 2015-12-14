/**
 * Created by lxflxf on 12/14/15.
 */
$(function () {
    var invitecode = $("#inviteCode");
    var username = $("#username");
    var email = $("#email");
    var password = $("#password");
    var repass = $("#repass");
    var error = $("#error");
   $("#btn-reg").click(function () {
        if(invitecode.val()==""){
            error.html("请输入邀请码");
            invitecode.focus();
        }else if (username.val() == ""){
            error.html("请输入用户名");
            username.focus();
        }else if(email.val()==""){
            error.html("请输入邮箱");
            email.focus();
        }else if(password.val()==""){
            error.html("请输入密码");
            password.focus();
        }else if(repass.val()==""){
            error.html("请重复密码");
            repass.focus();
        }else if(repass.val() != password.val()){
            error.html("两次密码不一致");
        }else{
            $.ajax({
                url:"register",
                type:"POST",
                contentType: "application/json",
                data:JSON.stringify({
                    invitecode:invitecode.val().trim(),
                    username:username.val().trim(),
                    email:email.val().trim(),
                    password:password.val().trim()
                }),
                async:false,
                success: function (msg) {
                    if(msg.status == "success"){
                        window.location.href = msg.url;
                    }else{
                        $("#error").html(msg.msg);
                    }
                }
            });
        }
   }); 
});
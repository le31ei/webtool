$(function () {
    $("#btn-send").click(function () {
        $.getJSON('send', function (data){

            }
        );
    });
    $("#btn-adduser").click(function () {
        var adduser = $("#adduser");
        var usermail = $("#useremail");
        if(adduser.val() == ""){
            adduser.focus();
        }else if(usermail.val() == ""){
            usermail.focus();
        }else{
            $.ajax({
                url:'sendmail',
                type:"POST",
                contentType: "application/json",
                data:JSON.stringify({
                    adduser:adduser.val().trim(),
                    usermail:usermail.val().trim()
                }),
                async:false,
                success: function (msg) {
                    if(msg.msg == "success"){
                        alert("add success");
                    }else{
                        //
                    }
                }
            });
        }
    });
});
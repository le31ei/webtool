/**
 * Created by lxflxf on 12/16/15.
 */
$(function () {
    var location = (window.location+'').split('/');
    var basePath = location[3];

    $("#btn-generate").click(function () {
        //点击生成验证码
        if($("#code_num").val() != ""){
            $.ajax({
                url:'/'+basePath+'/invitecontrol/generate',
                type:"POST",
                contentType: "application/json",
                data:JSON.stringify({
                    num:$("#code_num").val().trim()
                }),
                async:false,
                success: function (data) {
                    if(data.status == "success"){
                        alert("添加成功");
                        window.location.reload();
                    }
                }
            });
        }
    });
});
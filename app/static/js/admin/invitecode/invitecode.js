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

    //清空所有邀请码
    $("#btn-clear").click(function () {
        alert("click");
        $.getJSON('/'+basePath+'/invitecontrol/deletecodes', function (data) {
            if(data.status == "success"){
                //删除成功
                $("#clear-modal").modal("hide");
                window.location.reload();
            }
        });
    });
});
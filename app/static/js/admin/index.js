var time;
$(function () {
   $('#btn-exit').click(function () {
       window.location.href="logout";
   });

    run();

});
    function run(){
        timer = setInterval(setCpu,2000);
    }

    function setCpu(){
        $.getJSON("getServerInfo", function (data) {
            $("#cpu-use").html(data.cpu);
        });

    }
$('.form-control').keyup(function (e){
    var content = $(this).val();
    $('#counter').html("("+content.length+"/500)");    //글자수 실시간 카운팅

    if (content.length > 500){
        alert("최대 500자까지 입력 가능합니다.");
        $(this).val(content.substring(0, 500));
        $('#counter').html("(500 / 최대 500자)");
    }
});

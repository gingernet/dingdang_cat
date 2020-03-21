    //打开搜索
    $(".Top002434 .open-search").click(function(e) {
        $(".Top002434 .search_box").stop(true, true).slideToggle();
        $(document).on("click", function() {
            $(".Top002434 .search_box").stop(true, true).slideUp();
        });
        e.stopPropagation();
    });
    $(".Top002434 .search_box").on("click", function(e) {
        e.stopPropagation();
    });
    //打开语言版本
    $(".Top002434 .top-language dd").bind("mouseover", function() {
        $(this).next("dt").stop(true, true).slideDown();
    });
    $(".Top002434 .top-language").bind("mouseleave", function() {
        $(this).find("dt").stop(true, true).slideUp();
    });
    //搜索
    $("#TopBtn").jqSearch({
        TxtVal: "请输入关键词",
        KeyTxt1: "输入关键词搜索！",
        KeyTxt2: "输入的关键词字数不要过多！",
        KeyTxt3: "您输入的内容存在特殊字符！",
        KeyId: "TopKey", //输入框id
        KeyUrl: "/search.aspx", //跳转链接
        KeyHref: "key", //链接传值
        Static: false //是否静态站
    });
    $(document).ready(function(){
  $(window).scroll(function(){
    if($(window).scrollTop() >= 130){
       $('.Top002434').addClass('color');
       $('.Top002434 .header-menu li em a').addClass('color_a');

    } else{
       $('.Top002434').removeClass('color');
        $('.Top002434 .header-menu li em a').removeClass('color_a');
    }
    });
});



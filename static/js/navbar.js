$(document).ready(function() {
    $("#mobile-nav-btn").click(function() {
        $("#mobile-nav-bar").toggle()
        if($("#mobile-search-bar").css("display") == "block"){
            $("#mobile-search-bar").css("display", "none")
        }
    });
    $("#mobile-search-btn").click(function() {
        $("#mobile-search-bar").toggle()
        if($("#mobile-nav-bar").css("display") == "block"){
            $("#mobile-nav-bar").css("display", "none")
        }
    });
    $("#main-navbar-list .list-inline-item").hover(function(){
        $(this).find(".navbar-icon").css("display", "none")
        $(this).find("p").css("display", "block")
    }, function(){
        $(this).find(".navbar-icon").css("display", "block")
        $(this).find("p").css("display", "none")
    })
});
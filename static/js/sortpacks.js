$(document).ready(function(){
        document.body.onscroll = function() {
            var yOffset = window.pageYOffset;
            if(yOffset > 75){
                $('.btt-button').css("display","block");
            }
            else {
                $('.btt-button').css("display","none")
            }
        };
        $('.btt-link').click(function(e) {
			window.scrollTo(0,0)
		})
        $("#sortbyoptions").change(function(){
            var sortelement = $(this);
            var currentUrl = new URL(window.location);
            var selectedSort = sortelement.val();
            if(selectedSort != "-"){
                currentUrl.searchParams.set("sort", selectedSort);
                window.location.replace(currentUrl)
            }
        })
        $("#changedirection").click(function(){
            var currentUrl = new URL(window.location);
            var currentDir = currentUrl.searchParams.get("direction");
            if(currentDir == "desc"){
                var newDir = "asc";
            } else {
                newDir = "desc";
            }
            currentUrl.searchParams.set("direction", newDir);
            window.location.replace(currentUrl)
        })
        $(".pack-card").click(function(){
            var windowHeight = $(window).height();
            console.log(windowHeight);
            if(windowHeight > 650){
                var heightDiff = (windowHeight-650)/2;
                $(".modal-dialog").css("margin-top", `${heightDiff}px`);
            } else {
                console.log("Window to small")
                $(".modal-dialog").css("height", `${windowHeight}px`);
                $(".modal-content").css("height", `${windowHeight}px`);
                $(".modal-body").css("overflow: scroll");
            }
        })
        $(window).resize(function(){
            var windowHeight = $(window).height();
            var modalHeight = $(".modal-dialog").height();
            if(windowHeight > modalHeight){
                var heightDiff = (windowHeight-modalHeight)/2;
                $(".modal-dialog").css("margin-top", heightDiff);
            }
        })
})

function checkWindowHeight(){
    var yOffset = window.pageYOffset;
    if(yOffset != 0){
        $('.btt-button').css("display","")
    }
}

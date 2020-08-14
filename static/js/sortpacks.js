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
            if(windowHeight > 650){
                var heightDiff = (windowHeight-650)/2;
                $(".pack-detail-modal").css("margin-top", `${heightDiff}px`);
            } else {
                $(".pack-detail-modal").css("margin-top", 0);
                $(".pack-detail-modal").css("height", `${windowHeight}px`);
                $(".pack-detail-modal .modal-content").css("height", `${windowHeight}px`);
            }
        });
        $("#delete-pack-btn").click(function(){
            var windowHeight = $(window).height();
            if(windowHeight > 650){
                var smallheightDiff = ((windowHeight-650)/2)+278;
                $(".confirm-delete-modal").css("margin-top", `${smallheightDiff}px`);
            } else {
                smallheightDiff = ((windowHeight-94)/2);
                $(".confirm-delete-modal").css("margin-top", `${smallheightDiff}px`);
            }
        });
        $(window).resize(function(){
            var windowHeight = $(window).height();
            var modalHeight = $(".pack-detail-modal").height();
            if(windowHeight > modalHeight){
                var heightDiff = (windowHeight-modalHeight)/2;
                var smallheightDiff = ((windowHeight-650)/2)+278;
                $(".pack-detail-modal").css("margin-top", heightDiff);
                $(".pack-detail-modal").css("height", `650px`);
                $(".confirm-delete-modal").css("margin-top", `${smallheightDiff}px`);
            } else {
                smallheightDiff = ((windowHeight-94)/2);
                $(".pack-detail-modal").css("margin-top", 0);
                $(".pack-detail-modal").css("height", `${windowHeight}px`);
                $(".pack-detail-modal .modal-content").css("height", `${windowHeight}px`);
                $(".confirm-delete-modal").css("margin-top", `${smallheightDiff}px`);
            }
        });
        
})

function checkWindowHeight(){
    var yOffset = window.pageYOffset;
    if(yOffset != 0){
        $('.btt-button').css("display","")
    }
}

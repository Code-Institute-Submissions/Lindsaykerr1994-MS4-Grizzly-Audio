$(document).ready(function(){
        var audioPlaying = false;
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
        $(window).resize(function(){
            var windowHeight = $(window).height();
            var modalHeight = $(".pack-detail-modal").height();
            if(windowHeight > modalHeight){
                var heightDiff = (windowHeight-modalHeight)/2;
                var smallheightDiff = ((windowHeight-650)/2)+278;
                $(".pack-detail-modal").css("margin-top", heightDiff);
                $(".pack-detail-modal").css("height", `650px`);
            } else {
                smallheightDiff = ((windowHeight-94)/2);
                $(".pack-detail-modal").css("margin-top", 0);
                $(".pack-detail-modal").css("height", `${windowHeight}px`);
                $(".pack-detail-modal .modal-content").css("height", `${windowHeight}px`);
            }
        });
        $(".pack-detail-img").hover(function(){
            $(".button-container").removeClass("d-none").addClass("d-block");
        }, function(){
            $(".button-container").removeClass("d-block").addClass("d-none");
        })
        $(".pack-detail-img").click(function(){
            var packID = $(this).children("img").attr("id");
            var pack = packID.split("-")[1];
            var audio = document.getElementById(`audio_track${pack}`);
            if (audioPlaying==false){
                audio.play();
                $(this).find(".play-button").addClass("pause")
                audioPlaying = true;
            } else {
                audio.pause();
                $(this).find(".play-button").removeClass("pause")
                audioPlaying = false;
            }
        })
        $(".close-btn").hover(function(){
            $(".text-close").removeClass("d-block")
            $(".text-close").addClass("d-none")
            $(".close-btn i").removeClass("d-none")
            $(".close-btn i").addClass("d-block")
        }, function(){
            $(".close-btn i").removeClass("d-block")
            $(".close-btn i").addClass("d-none")
            $(".text-close").removeClass("d-none")
            $(".text-close").addClass("d-block")
        })
        $(".add-btn").hover(function(){
            $(".text-price").removeClass("d-block")
            $(".text-price").addClass("d-none")
            $(".add-btn i").removeClass("d-none")
            $(".add-btn i").addClass("d-block")
        }, function(){
            $(".add-btn i").removeClass("d-block")
            $(".add-btn i").addClass("d-none")
            $(".text-price").removeClass("d-none")
            $(".text-price").addClass("d-block")
        })
})

function checkWindowHeight(){
    var yOffset = window.pageYOffset;
    if(yOffset != 0){
        $('.btt-button').css("display","")
    }
}

$(document).ready(function(){
        var audioPlaying = false;
        // When the user scrolls the page
        document.body.onscroll = function() {
            var yOffset = window.pageYOffset;
            // If the user scrolls more than 75px, change the display of the back-to-top button
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
        // When user clicks on the sort by select element
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
        // When opening modal window, resize margin-top to fit in the middle of the window.
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
        // When user hovers over the img, show the play/pause button.
        $(".pack-detail-img").hover(function(){
            $(".button-container").removeClass("d-none").addClass("d-block");
        }, function(){
            $(".button-container").removeClass("d-block").addClass("d-none");
        })
        // When modal window open:
        $('.modal').on('show.bs.modal', function (e) {
            //Get modal ID
            var getID = $(this).attr("id");
            var ID = getID.replace("pack","").replace("Modal","");
            // Check if there is an audio file in modal.
            if($(`#pack${ID}Modal audio`).length == 1) {
                $(`#pack${ID}Modal .pack-detail-img`).click(function(){
                    var audio = document.getElementById(`audio_track${ID}`);
                    // If audio file is paused, play. Vice versa
                    if (audioPlaying==false){
                        audio.play();
                        // Change play button icon to paused.
                        $(this).find(".play-button").addClass("pause");
                        audioPlaying = true;
                        // If user closes the modal, pause the audio file.
                        $(`#pack${ID}Modal`).on('hide.bs.modal', function (e) {
                            audio.pause();
                            audioPlaying = false;
                        });
                    } else {
                        audio.pause();
                        $(this).find(".play-button").removeClass("pause");
                        audioPlaying = false;
                    }
                });
            };
        });
        // Change icon/text when hovering
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

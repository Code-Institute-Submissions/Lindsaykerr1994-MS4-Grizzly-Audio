$(document).ready(function(){
    $('input[name=image]').change(function(){
        var file = $('input[name="image"]')[0].files[0];
        $(this).parent().next().text(`Image choosen: ${file.name}`);
    });
    $('input[name=sample_track]').change(function(){
        var file = $('input[name=sample_track]')[0].files[0];
        $(this).parent().next().text(`File choosen: ${file.name}`);
    });
    $('#id_on_sale').click(function(){
        if($(this).prop("checked") == true){
            $('#id_reduced_price').prop('disabled', false);
        }
        else {
            $('#id_reduced_price').prop('disabled', true);
        }
    });
    $('#add-pack-btn').tooltip();
    $(".cancel-btn").hover(function(){
        $(this).children("p").removeClass("d-block");
        $(this).children("p").addClass("d-none");
        $(this).children("i").removeClass("d-none");
        $(this).children("i").addClass("d-block");
    }, function(){
        $(this).children("i").removeClass("d-block");
        $(this).children("i").addClass("d-none");
        $(this).children("p").removeClass("d-none");
        $(this).children("p").addClass("d-block");
    });
    $(".save-btn").hover(function(){
        $(this).children("p").removeClass("d-block");
        $(this).children("p").addClass("d-none");
        $(this).children("i").removeClass("d-none");
        $(this).children("i").addClass("d-block");
    }, function(){
        $(this).children("i").removeClass("d-block");
        $(this).children("i").addClass("d-none");
        $(this).children("p").removeClass("d-none");
        $(this).children("p").addClass("d-block");
    });
});
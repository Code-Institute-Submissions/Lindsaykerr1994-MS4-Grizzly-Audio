$(document).ready(function(){
    $('input[name=image]').change(function(){
        var file = $('input[name="image"]')[0].files[0]
        $(this).parent().next().text(`Image choosen: ${file.name}`);
    });
    $('input[name=sample_track]').change(function(){
        var file = $('input[name=sample_track]')[0].files[0]
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
    $("#cancel-btn").hover(function(){
        $("#text-cancel").removeClass("d-block")
        $("#text-cancel").addClass("d-none")
        $("#cancel-btn i").removeClass("d-none")
        $("#cancel-btn i").addClass("d-block")
    }, function(){
        $("#cancel-btn i").removeClass("d-block")
        $("#cancel-btn i").addClass("d-none")
        $("#text-cancel").removeClass("d-none")
        $("#text-cancel").addClass("d-block")
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
});
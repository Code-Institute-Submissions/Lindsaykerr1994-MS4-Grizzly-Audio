/* All Stripe Documentation can be found here: */
/* https://stripe.com/docs/payments/accept-a-payment */
/* https://stripe.com/docs/stripe-js */

/* The implementation of this following Javascript code was instructed by following along the following videos:
    https://courses.codeinstitute.net/courses/course-v1:CodeInstitute+FSF_102+Q1_2020/courseware/4201818c00aa4ba3a0dae243725f6e32/90cda137ebaa461894ba8c89cd83291a/?activate_block_id=block-v1%3ACodeInstitute%2BFSF_102%2BQ1_2020%2Btype%40sequential%2Bblock%4090cda137ebaa461894ba8c89cd83291a
*/

/* Import required keys from document */
/* These variables are camel case to adher to following code */
var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripePublicKey);

/* Assign necessary elements */
var elements = stripe.elements();

/* Style necessary aspects */
var style = {
    base: {
        /* Changed this colour to match established theme */
        color: '#292929',
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
        color: '#aab7c4'
    }
},
    invalid: {
        /* Changed this colour to match established theme */
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};
/* Create card element */
var card = elements.create('card', {style: style});
/* Mount Stripe elements */
card.mount('#card-element');
/* Display any errors with card element */
card.addEventListener('change', function(event){
    var errorDiv = document.getElementById('card-errors');
    if (event.error) {
        var html = `
            <span class="icon" role="alert">
            <i class="fas fa-times"></i>
            </span>
            <span>${event.error.message}</span>`;
        $(errorDiv).html(html);
    } else {
        errorDiv.textContent = '';
    }
});
/* Create a form to submit payment */
var form = document.getElementById('payment-form');

form.addEventListener('submit', function(ev) {
    ev.preventDefault();
    /* Disable the card element and submit button to prevent multiple payments */
    card.update({'disabled': true});
    $('#submit-button').attr('disabled', true);
    $('#payment-form').fadeToggle(100);
    $('#loading-overlay').fadeToggle(100);
    /* Check if 'save-info' input is checked */
    var saveInfo = Boolean($('#id-save-info').attr('checked'));
    /* Retrieve the csrf_token from the form */
    var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
    var postData = {
        'csrfmiddlewaretoken': csrfToken,
        'client_secret': clientSecret,
        'save_info': saveInfo,
    };
    var url = '/checkout/cache_checkout_data/';
    /* Post the url to save this information to cache */
    /* Wait to see that the action is completed before progressing */
    $.post(url, postData).done(function () {
        /* Then proceed with the payment */
        stripe.confirmCardPayment(clientSecret, {
            payment_method: {
                card: card,
                billing_details: {
                    name: $.trim(form.full_name.value),
                    phone: $.trim(form.phone_number.value),
                    email: $.trim(form.email.value),
                    address: {
                        line1: $.trim(form.street_address1.value),
                        line2: $.trim(form.street_address2.value),
                        city: $.trim(form.town_or_city.value),
                        state: $.trim(form.county.value),
                        country: $.trim(form.country.value),
                    }
                }
            },
            shipping: {
                name: $.trim(form.full_name.value),
                phone: $.trim(form.phone_number.value),
                address:{
                    line1: $.trim(form.street_address1.value),
                    line2: $.trim(form.street_address2.value),
                    city: $.trim(form.town_or_city.value),
                    state: $.trim(form.county.value),
                    postal_code: $.trim(form.post_code.value),
                    country: $.trim(form.country.value),
                }
            },
        /* After collecting all the necessary data from the form, we present an errors (if necessary), or we submit the form to Stripe */
        }).then(function(result) {
            if (result.error) {
                var errorDiv = document.getElementById('card-errors');
                var errorHtml = `
                    <span class="icon" role="alert">
                    <i class="fas fa-times"></i>
                    </span>
                    <span>${result.error.message}</span>`;
                $(errorDiv).html(errorHtml);
                $('#payment-form').fadeToggle(100);
                $('#loading-overlay').fadeToggle(100);
                card.update({ 'disabled': false});
                $('#submit-button').attr('disabled', false);
            } else {
                if (result.paymentIntent.status === 'succeeded') {
                    form.submit();
                }
            }
        });
    /* If the post method fails, then reload the page, and the error message will display */
    }).fail(function(){
        location.reload();
    });
});
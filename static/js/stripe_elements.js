/* All Stripe Documentation can be found here: */
/* https://stripe.com/docs/payments/accept-a-payment */
/* https://stripe.com/docs/stripe-js */

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
/* Create a form to submit payment */
var form = document.getElementById('payment-form');

form.addEventListener('submit', function(ev) {
  ev.preventDefault();
    /* Disable the card element and submit button to prevent multiple payments */
    card.update({'disabled': true});
    $('#submit-button').attr('disabled', true)
  stripe.confirmCardPayment(clientSecret, {
    payment_method: {
      card: card,

    }
  }).then(function(result) {
    if (result.error) {
      // Show error to your customer (e.g., insufficient funds)
      var errorDiv = document.getElementById('card-errors');
            var html = `
                <span class="icon" role="alert">
                <i class="fas fa-times"></i>
                </span>
                <span>${result.error.message}</span>`;
            $(errorDiv).html(html);
            /* Re-enable the card and submit button to try again */
            card.update({ 'disabled': false});
            $('#submit-button').attr('disabled', false);
    } else {
      // The payment has been processed!
      if (result.paymentIntent.status === 'succeeded') {
        // Show a success message to your customer
        // There's a risk of the customer closing the window before callback
        // execution. Set up a webhook or plugin to listen for the
        // payment_intent.succeeded event that handles any business critical
        // post-payment actions.
        form.submit();
      }
    }
  });
});
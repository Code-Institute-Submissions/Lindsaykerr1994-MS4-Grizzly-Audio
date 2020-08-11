/* All Stripe Documentation can be found here: */
/* https://stripe.com/docs/payments/accept-a-payment */
/* https://stripe.com/docs/stripe-js */

/* Import required keys from document */
var stripe_public_key = $('#id_stripe_public_key').text().slice(1, -1);
var client_secret_key = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripe_public_key);
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


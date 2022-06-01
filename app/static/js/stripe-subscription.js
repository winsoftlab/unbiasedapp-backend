var createCheckoutSession = function(priceId) {
    
    return fetch("/stripy/create-checkout-session",{
        method: "POST",
        headers:{
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            priceId : priceId
        })
    }).then((result) => {
        return result.json()
    });
};



const PREMIUM_PRICE_ID = "price_1KepM1HSCh2fFcDYEN6KDSXV";

const BASIC_PRICE_ID = "price_1KddHBHSCh2fFcDYGd3kg9WU";


$("#checkoutbasic").click(function () {
    $.ajax({
        url : "/stripy/config",
        type:"POST",
        success: function(response){
            const stripe = Stripe(response.publicKey)
            window.alert(response.publicKey)
            createCheckoutSession(BASIC_PRICE_ID).then((data) => {
                stripe.redirectToCheckout({ sessionId: data.sessionId })
            });
        }
    })
});

$("#checkoutpremium").click(function () {
    $.ajax({
        url : "/stripy/config",
        type :"GET",
        success: function(response){
            const stripe = Stripe(response.publicKey)

            createCheckoutSession(PREMIUM_PRICE_ID).then((data) => {
                stripe.redirectToCheckout({ sessionId: data.sessionId })
            });
        }
    })
});

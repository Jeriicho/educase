

$(function () {
    function runEffect() {

        var selectedEffect = "blind"

        // Most effect types need no options passed by default
        var options = {};

        // Run the effect
        $("#effect").toggle(selectedEffect, options, 500);
    };

    //callback function to bring a hidden box back
    function callback() {
        setTimeout(function () {
            $("#effect:visible").removeAttr("style").fadeOut();
        }, 1000);
    };

    // Set effect from select menu value
    $(".navbar-toggle").on("click", function () {
        console.log("Clicked on the button.")
        runEffect();
    });

    $("#effect").hide();
});
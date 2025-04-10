document.addEventListener("DOMContentLoaded", function() {
    const counterSets = document.querySelectorAll(".counter-set");

    counterSets.forEach(function(counterSet) {
        const counterElement = counterSet.querySelector(".counter");
        const plusButton = counterSet.querySelector(".plus-button");
        const minusButton = counterSet.querySelector(".minus-button");

        let count = 0;

        plusButton.addEventListener("click", function() {
            count++;
            counterElement.textContent = count;
        });

        minusButton.addEventListener("click", function() {
            if (count > 0) {
                count--;
                counterElement.textContent = count;
            }
        });
    });
});
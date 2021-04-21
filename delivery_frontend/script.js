function processForm(e) {
    if (e.preventDefault) e.preventDefault();
    let from = document.getElementById("from_input").value;
    let to = document.getElementById("to_input").value;
    console.log(from);
    console.log(to);
    if(isNotEmpty(from) && isNotEmpty(to)) {
        httpAsync("../api/queries/distance/", "POST", {
            location_from: from,
            location_to: to
        }, function(response) {
            if(response.status >= 200 && response.status < 300)
                showResultsFromApi(response.responseText)
            else
                showResults("Server error with status " + response.status
                            + '. Response was: ' + response.responseText)
        })
    } else {
        showResults("Empty values for addresses")
    }

    return false;
}

var form = document.getElementById('calculate-distance-form');
if (form.attachEvent) {
    form.attachEvent("submit", processForm);
} else {
    form.addEventListener("submit", processForm);
}

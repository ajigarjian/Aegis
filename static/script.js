// Creates a function that, as a user types in an answer, filters the table to return only the clues that start with the search
document.querySelector("#ans_search").addEventListener('keyup', function(e){

    //list of answers taken from the answers table column
    const answers = document.querySelectorAll(".table_body .body_row .table_answers");

    //makes search from search bar lowercase
    var search_item = e.target.value.toLowerCase();

    //for each answer in the list (aka in each row of table), checks if it starts w the search item. If it does, ensure it's visible.
    for (let i = 0; i < answers.length; i++) {
        if (answers[i].innerHTML.toLowerCase().trim().startsWith(search_item))  {
            answers[i].parentNode.style.visibility = "visible";
        }

        //if it doesn't, hide it.
        else {
            answers[i].parentNode.style.visibility = "collapse";
        }
    }
});

//Similar function but for dates
document.querySelector("#date_start").addEventListener("change", function() {
    var input = new Date(this.value);
    const dates = document.querySelectorAll(".table_body .body_row .table_dates");

    for (let i = 0; i < dates.length; i++) {
        var date = new Date(dates[i].innerHTML)
        if (date >= input) {
            dates[i].parentNode.style.visibility = "visible";
        }

        else {
            dates[i].parentNode.style.visibility = "collapse";
        }
    }
});




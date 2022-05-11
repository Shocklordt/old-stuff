let s = "";
let questionData;
let questionURL = "questions.json"

let responce = $.getJSON(questionURL)
responce.done(function(data) {
    questionData = data;
    for (let [i, question] of questionData.entries()) {
        s += `<h6 name="q" class="form-label">${question.question}<\h6>`;
        for (let [j, choice] of question.choices.entries()) {
            // unique id for each choice
            // q_0_0 first question, first choice; q_0_1 first question, second choice...
            let id = `q_${i}_${j}`;
            s += `<label for="${id}" class ="form-check-label"><input type="radio" class="form-check-input" id="${id} "name="q_${i}" value="${id}"> ${choice.text}</label>`;
        }
    }
    s += '<button class="ui-btn ui-shadow" onclick="answer(event, questionData)">' +
        'Answer<\/button>';
    document.getElementById("form_container").innerHTML = s;
})


function answer(event, questionData) {
    r = 0;
    result = 0;
    event.preventDefault()
    checked = ($('.form-check-input:checked')).length
    if (checked > 2) {
        let answers = $(":checked");
        for (let answer of answers) {
            let idMatch = answer.id.match(/q_(\d+)_(\d+)/);
            let questionN = idMatch[1];
            let choiceN = idMatch[2];
            let points = questionData[questionN].choices[choiceN].points;
            r = result += points
            document.getElementById("result_line").innerHTML = "You have scored:" + r
        }
    } else if (checked <= 2) {
        document.getElementById("result_line").innerHTML = "<p>Please answer all questions!</p>"
    } else {}
}
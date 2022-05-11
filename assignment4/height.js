function showValue1(newValue) {
    document.getElementById("height1").innerHTML = newValue;
}

function changeRangeValue(val) {
    document.getElementById("range").value = isNaN(parseInt(val, 10)) ? 0 : parseInt(val, 10);
    showValue1(val);
}

function changeInputValue(val) {
    document.getElementById("number").value = isNaN(parseInt(val, 10)) ? 0 : parseInt(val, 10);
    showValue1(val);
}
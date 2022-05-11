while (true) {
    var input = promt("?", "");
    if (!input) break;
    try {
        var result = eval(input);
        alert(input + "=\n" + result);
    } catch (error) {
        alert("Error: " + error);
    }
}
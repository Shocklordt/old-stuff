s = prompt("Number?", "");
n = Number(s);
n += 0.1;
n = n + 0.1;
n += .1;
if (Math.abs( n ) > 0.0001) alert("your number + 0.1 + 0.1 + 0.1 is one");
else alert("your number + 0.1 + 0.1 + 0.1 is not one");
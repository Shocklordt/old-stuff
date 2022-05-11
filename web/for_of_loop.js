/* This code iterates through the object and unpacks keys with values, then prints them.*/

d = { Ford: 1, Toyota: 2, Nissan: 3 }

for (let [key, value] of Object.entries(d)) {
    console.log(key, value);
}
let csv = `Star Wars - A New Hope,1977,Lucas
Die Hard,1988,McTiernan
Ghostbusters,1984,Reitman`


for (let line of csv.split("\n")) console.log(line.split(","));
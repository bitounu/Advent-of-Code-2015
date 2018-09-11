var fs = require('fs'), filename = process.argv[2];
var arr = fs.readFileSync(filename).toString().split("");
var coordArr = [[0,0]];
var x = 0, y = 0, presents = 1, len = arr.length;
for (var i = 0; i < len; i++){
    if (arr[i] === "<"){
     x--;
     presents++;
     var newArr = [x,y];
     coordArr.push(newArr);
} else if(arr[i] === ">"){
    x++;
    presents++;
    var newArr = [x,y];
    coordArr.push(newArr);
} else if(arr[i] === "v"){
    y--;
    presents++;
    var newArr = [x,y];
    coordArr.push(newArr);
}else if(arr[i] === "^"){
    y++;
    presents++;
    var newArr = [x,y];
    coordArr.push(newArr);
}
}

console.log("total presents delivered: " + presents + "\n" +  "coordinates visited: " + JSON.stringify(coordArr));
var filteredArr = removeDuplicates(coordArr);
//console.log("filtered arr: " + JSON.stringify(filteredArr));
var houses = filteredArr.length;
console.log("Houses receiving at least 1 present: " + houses);


function removeDuplicates(arr){
 var i, len=arr.length,
    out = [],
    obj={};
    for (i = 0;i<len;i++){
	//	console.log(obj);
		obj[arr[i]]=0;
	}
	console.log(obj);
	for (i in obj) {
		out.push(i);
	}
 return out;
}

var fruits = ["Banana", "Orange", "Apple", "Mango"];
dupa={};
fruits.push("Kiwi");
console.log(fruits);
fruits.push("Banana");
console.log(fruits);
var len = fruits.length;
    for (i = 0;i<len;i++){
		dupa[fruits[i]]=0;
	}
console.log(dupa);


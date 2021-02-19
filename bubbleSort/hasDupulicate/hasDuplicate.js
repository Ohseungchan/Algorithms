function hasDuplicateValue(array){
    var steps = 0;
    for(var i = 0; i < array.length; i++){
        for(var j =0; j < array.length; j++){
            steps++;
            if(i !== j && array[i] == array[j]){
                return true;
            }
        }
    }
    console.log(steps);
    return false;
}

function hasDuplicateValue1(array){
    var steps = 0;
    var existingNumbers =  [];
    for(var i = 0; i < array.length; i++){
        steps++;
        if(existingNumbers[array[i]] === undefined){
            existingNumbers[array[i]] = 1;
        } else {
            return true;
        }
    }
    console.log(steps);
    return false;
}

hasDuplicateValue([1,2,3]);
hasDuplicateValue1([1,2,3]);
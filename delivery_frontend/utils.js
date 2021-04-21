function httpAsync(url, method, data, callback)
{
    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() { 
        callback(xhr);
    }
    xhr.open(method, url, true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.send(JSON.stringify(data));
}

function isNotEmpty(str) {
    return (str && str.length > 0);
}

function showResultsFromApi(str) {
    json = JSON.stringify(JSON.parse(str), undefined, 4);
    var div = document.getElementById('results');
    div.innerHTML = json;
}

function showResults(str) {
    var div = document.getElementById('results');
    div.innerHTML = str;
}
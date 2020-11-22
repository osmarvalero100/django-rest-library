var portSite = (window.location.port == '')? '' : ':'+window.location.port
var baseUrl = window.location.protocol+'//'+window.location.hostname+portSite+'/'

function fetchData (endpoint) {
    const fetchedData = fetch(baseUrl+endpoint)
      .then(result => result.json())
      .then(data => {
          return data;
    })
  
    return fetchedData;
}
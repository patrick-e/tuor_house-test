function sendTextToDjango(text) {
    return fetch('/tables/', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({'text': text})
    })
    .then(response => response.json())
    .then(data => {
      console.log(data);
      return data;
    })
    .catch(error => console.error(error));
  };
  
  function Edit(id) {
    var currentValue = document.getElementById(id).textContent;
    var input = document.createElement("input");
    input.type = "text";
    input.value = currentValue;
    document.getElementById(id).replaceWith(input);
    input.addEventListener("keypress", function(e) {
      if (e.key === "Enter") {
        sendTextToDjango(input.value)
        .then(() => {
          var newText = document.createElement("span");
          newText.id = "nameforedit";
          newText.textContent = input.value;
          input.replaceWith(newText);
        });
      }
    });
  };
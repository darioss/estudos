const backWay = document.getElementById("selectYourBackDestiny");
const frontWay = document.getElementById("selectYourFrontDestiny");
const index = document.getElementById("selectYourDestiny");
const vue = document.getElementById("vueCarrier");
const csharp = document.getElementById("csharpCarrier");
const java = document.getElementById("javaCarrier");
const react = document.getElementById("reactCarrier");
const labelFront = document.getElementById("labelFrontTech");
const labelBack = document.getElementById("labelBackLanguages");
const labeIndex = document.getElementById("labelPrefers");
const startVue = document.getElementById("getStartVue");
const startReact = document.getElementById("getStartReact");
const startJava = document.getElementById("getStartJava");
const startCsharp = document.getElementById("getStartCsharp");
const technologies = document.getElementById("technologies");
const labelQuestions = document.getElementById("labelQuestions");
const labelForLanguages = document.getElementById("counter");
const questions = document.getElementById("questions");
const decisionPhrases = [
       "Trust your instincts?",
       "Confidence is key?",
       "Take a leap of faith?",
       "Believe in your choices?",
       "Commit with conviction?",
       "Embrace your decision?",
       "Stand by your judgment?",
       "Be resolute in your choice?",
       "Decide with certainty?",
       "Have faith in your decision?",
       "Own your choices?",
       "Stay true to your decision?",
       "Decisiveness breeds success?",
       "Be unwavering in your choice?",
       "Choose with confidence?",
       "Don't second-guess yourself?",
       "Commitment leads to success?",
       "Be sure, be bold?",
       "Trust your decision-making skills?"
     ];

//First Page action butons
labeIndex.innerHTML = `Choose your destiny, little locust`;
index.addEventListener("submit", function (event) {
       event.preventDefault();
       index.style.display = "none";
       let carrier = event.submitter.value;
       if(carrier=="Frontend"){
              frontWay.style.display = "block";
              labelFront.innerHTML = `Choose a javascript technology, little locust`;
       }else if(carrier=="Backend"){
              backWay.style.display = "block";
              labelBack.innerHTML = `Choose a programming language, little locust`;
       }
});

//Select  Front way action butons
frontWay.addEventListener("submit", function (event) {
       event.preventDefault();
       frontWay.style.display = "none";
       let carrier = event.submitter.value;
       if(carrier=="Vue.js"){
              vue.style.display = "block";
              startVue.innerHTML = `Get Start with Vue.js, little locust`;
       }else if(carrier=="React.js"){
              react.style.display = "block";
              startReact.innerHTML = `Get Start with React.js, little locust`;
       }
});

//Select  Back way action butons
backWay.addEventListener("submit", function (event) {
       event.preventDefault();
       backWay.style.display = "none";
       let carrier = event.submitter.value;
       if(carrier=="Java"){
              java.style.display = "block";
              startJava.innerHTML = `Get Start with Java, little locust`;
       }else if(carrier=="CSharp"){
              console.log(event.submitter.value);
              csharp.style.display = "block";
              startCsharp.innerHTML = `Get Start with C#, little locust`;
       }
});

//Vue Carrier action butons
vue.addEventListener("submit", function (event) {
       event.preventDefault();
       vue.style.display = "none";
       let carrier = event.submitter.value;
       if(carrier=="Stay Front"){
              questions.style.display = "block";
              labelQuestions.textContent = "What are the best technologies for you?";
       }else if(carrier=="FullStack"){
              backWay.style.display = "block";
              labelBack.innerHTML = `Choose a programming language, little locust`;
       }
});

//React Carrier action butons
react.addEventListener("submit", function (event) {
       console.log("Cheguei aqui");
       event.preventDefault();
       react.style.display = "none";
       let carrier = event.submitter.value;
       if(carrier=="Stay Front"){
              questions.style.display = "block";
              labelQuestions.textContent = "What are the best technologies for you?";
       }else if(carrier=="FullStack"){
              backWay.style.display = "block";
              labelBack.innerHTML = `Choose a programming language, little locust`;
       }
});

//Csharp Carrier action butons
csharp.addEventListener("submit", function (event) {
       console.log("Cheguei aqui");
       event.preventDefault();
       csharp.style.display = "none";
       let carrier = event.submitter.value;
       if(carrier=="Stay Back"){
              questions.style.display = "block";
              labelQuestions.textContent = "What are the best technologies for you?";
       }else if(carrier=="FullStack"){
              frontWay.style.display = "block";
              labelFront.innerHTML = `Choose a programming language, little locust`;
       }
});

//Java Carrier action butons
java.addEventListener("submit", function (event) {
       console.log("Cheguei aqui");
       event.preventDefault();
       java.style.display = "none";
       let carrier = event.submitter.value;
       if(carrier=="Stay Back"){
              questions.style.display = "block";
              labelQuestions.textContent = "What are the best technologies for you?";
       }else if(carrier=="FullStack"){
              frontWay.style.display = "block";
              labelFront.innerHTML = `Choose a programming language, little locust`;
       }
});


/*
       Questions -  Is needed correct combine 3 technologies for win
*/ 
let counter = 1;
technologies.addEventListener("submit", function (event) {
       event.preventDefault();
       //Get Form values
       let languages = document.getElementById("languages").value;
       let framework = document.getElementById("framework").value;
       let porpose = document.getElementById("porpose").value;
       let match = false;

       //Combinations analisys       
       if(framework == "Angular" && languages == "Typescript" || languages == "Javascript" && porpose == "Web"){
              match = true;
       }else if(framework == "Backbone" && languages == "Javascript" && porpose == "Web"){
              match = true;
       }else if(framework == "Laravel" && languages == "PHP" && porpose == "Web"){
              match = true;
       }else if(framework == "Rails" && languages == "Ruby" && porpose == "Multi Porpose"){
              match = true;
       }else if(framework == "Play" && languages == "Java" && porpose == "Multi Porpose"){
              match = true;
       }else if(framework == "Gin" && languages == "Go" && porpose == "Multi Porpose"){
              match = true;
       }else if(languages == "Python" || framework == "Django" && framework == "Flesk" && porpose == "Multi Porpose"){
              match = true;
       }else if(framework == "Entity" && languages == "C#"  && porpose == "Multi Porpose"){
              match = true;
       }else if(framework == "Javalin" && languages == "Kotlin" && porpose == "Mobile"){
              match = true;
       }
       if(match==true && counter<=3){
              technologies.style.display = "none";
              questions.innerHTML = "<h2 id='labelQuestions'>Congratulations little locust! Your choices are matched!</h2> <img class='finishImagem success' src='./img/success.png'><button id='successRetry'>Retry</button>";
              document.getElementById("successRetry").addEventListener("click", function(event){
                     window.location.reload();
              });
       }else{
              counter++;
              if(counter>3){
                     technologies.style.display = "none";
                     questions.innerHTML = "<h2 id='labelQuestions'>Wow little locust. You really need study!</h2> <img class='finishImagem fail' src='./img/fail.png'><button id='failRetry'>Retry</button><button id='scape'>Scape</button>";
                     document.getElementById("failRetry").addEventListener("click", function(event){ 
                            window.location.reload();
                     });

                     document.getElementById("scape").addEventListener("click", function(event){
                            response()
                     });
              }else{
                     //Reset form filds
                     document.getElementById("languages").value="";
                     document.getElementById("framework").value="";
                     document.getElementById("porpose").value = "";
                     labelForLanguages.textContent = ` ${counter}/3`;
              }                     
       }
});

/*
       Asks the user questions until they type yes
*/ 
function response(){
       let response = prompt("Don't you want to try again?");
       const expressionRegular = /yes/gi;
       const result = response.match(expressionRegular);
       while (response != result){
              response = prompt(decisionPhrases[Math.floor(Math.random() * 19)]);
              result = response.match(expressionRegular);
       }
       window.location.reload();
}
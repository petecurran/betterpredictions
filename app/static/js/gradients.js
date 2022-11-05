//Variable references for slider and and output percentage
var slider=document.getElementById("rainSlider");
var output=document.getElementById("prediction");
//Set output percentage to 0
output.innerHTML = slider.value;

//Initial sunny and rainy colours for transition, stored as hsl values
var sunnyColour = [196,33,60];
var rainyColour = [208,42,19];

//Calculate the hsl difference between the two colours.
function calculateValuesForTransition(sunnyColour,rainyColour){
    
    var colourDifference = 
    [sunnyColour[0]-rainyColour[0],
    sunnyColour[1]-rainyColour[1],
    sunnyColour[2]-rainyColour[2]];
    //Return an array with the differences in values.
    return colourDifference;
};

//Get the differences between the two colours
var colourDifference = calculateValuesForTransition(sunnyColour,rainyColour);

//Calculate the current background colour
function calcBackground(sliderValue,sunnyColour,colourDifference){
    
    //Current colour is sunny colour plus difference values.
    //Difference values are divided by 100 so they can be multiplied by slider
    var currentBG = 
    [sunnyColour[0]-((colourDifference[0]/100)*sliderValue),
    sunnyColour[1]-((colourDifference[1]/100)*sliderValue),
    sunnyColour[2]-((colourDifference[2]/100)*sliderValue)];
    
    //Format a string for the new hsl
    var newBG = `hsl(${currentBG[0]}, ${currentBG[1]}%, ${currentBG[2]}%)`;
    //Return an element change for the background
    return document.getElementById('rainBackground').style.background= newBG;
};

//When the slider is moved, update the bg colour and percent display.
slider.oninput = function(){
    calcBackground(this.value,sunnyColour,colourDifference);
    output.innerHTML = this.value;
}

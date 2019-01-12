// Select color input
// Select size input
const submitButton = document.getElementById('sizePicker');
const colorSelector = document.getElementById('colorPicker');
const canvas = document.getElementById('pixelCanvas');
var fillColor = '#000000';
function makeGrid() {
var columns = 'grid-template-columns: ';
var height = submitButton.inputHeight.value;
var width = submitButton.inputWidth.value;
while (canvas.childElementCount > 0){
  canvas.removeChild(canvas.lastChild)
  }
  canvas.insertAdjacentHTML('beforeend','<div class="grid-container">');
  const grid = document.getElementsByClassName('grid-container');
  for (var r = 1; r<= width; r++){
    columns += ' auto';
  }
  grid[0].setAttribute('style',columns);
  for (var c = 1; c <= (width*height); c++){
    canvas.lastElementChild.insertAdjacentHTML('beforeend','<div class="grid-item" id="' + c + '"></div>');
}
}
// When size is submitted by the user, call makeGrid()
submitButton.addEventListener("submit",function (){makeGrid()},false)
colorSelector.addEventListener("change",function (assignColor){fillColor = colorSelector.value},false);
canvas.addEventListener('click',function(e){e.path[0].style.backgroundColor = fillColor},false)
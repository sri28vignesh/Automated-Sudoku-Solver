/*  ==========================================
    SHOW UPLOADED IMAGE
* ========================================== */
function readURL(input) {
    
    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function (e) {
            $('#imageResult')
                .attr('src', e.target.result);
            

        };

        reader.readAsDataURL(input.files[0]);
        var fileName = input.files[0].name;
        var validFileExtensions = [".jpg", ".jpeg", ".bmp", ".gif", ".png"];
        //console.log("Check");
        //console.log(fileName);
        if (fileName.length > 0) {
              var blnValid = false;
              for (var j = 0; j < validFileExtensions.length; j++) {
                  var sCurExtension = validFileExtensions[j];
                  if (fileName.substr(fileName.length - sCurExtension.length, sCurExtension.length).toLowerCase() === sCurExtension.toLowerCase()) {
                      blnValid = true;
                      break;
                  }
              }
              
              if (!blnValid) {
                  //console.log("Result"+blnValid);
                  document.getElementById("upload-txt").innerHTML =  "<font color='#FF0000'> Sorry, " + fileName + " is invalid, allowed extensions are: " + validFileExtensions.join(", ") + "</font>";
                  //return false;
              }
              else{
                document.getElementById("upload-txt").innerHTML = "Uploaded Sudoku Puzzle Image";
              }
          }


    }
    
    /*var _validFileExtensions = [".jpg", ".jpeg", ".bmp", ".gif", ".png"];
    if (filename.length>0){
        var blnValid = false;
                for (var j = 0; j < _validFileExtensions.length; j++) {
                    var sCurExtension = _validFileExtensions[j];
                    if (fileName.substr(fileName.length - sCurExtension.length, sCurExtension.length).toLowerCase() == sCurExtension.toLowerCase()) {
                        
                        
                        }
                    }
                }
                if (!blnValid) {
                    alert("Sorry, " + fileName + " is invalid, allowed extensions are: " + _validFileExtensions.join(", "));
                    return false;
                }
    }*/
    
}

$(function () {
    $('#upload').on('change', function () {
        readURL(input);
    });
});


/*  ==========================================
    SHOW UPLOADED IMAGE NAME
* ========================================== */
var input = document.getElementById( 'upload' );
//var infoArea = document.getElementById( 'upload-label' );

input.addEventListener( 'change', showFileName );
function showFileName( event ) {
  var input = event.srcElement;
  var fileName = input.files[0].name;
  console.log("check2");    
  //infoArea.textContent = 'File name: ' + fileName;
}
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
    
    
}

$(function () {
    $('#upload').on('change', function () {
        readURL(input);
    });
});




async function disp_solved_image(){

    let domain = "http://127.0.0.1:5000";
    let url = domain + "/get-solved-res";
    let response = await fetch(url);

    console.log(response.ok);
    
    if (response.ok) { // if HTTP-status is 200-299
    // get the response body (the method explained below)
    let json_res = await response.json();
    //json_res.resp
    console.log(json_res.resp);
    $("#imageSolved").attr('src', 'data:image/jpeg;base64,' + json_res.resp);
    } 
    
    else {
    //alert("HTTP-Error: " + response.status);
    document.getElementById("sol-txt").innerHTML = "<font color='#FF0000'>Sorry there is a problem in displaying the solved puzzle image </font>";
    }

}

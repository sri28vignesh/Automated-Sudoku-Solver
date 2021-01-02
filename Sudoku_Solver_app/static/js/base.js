/*  ==========================================
    SHOW UPLOADED IMAGE
* ========================================== */
function readURL(input) {
    
    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function (e) {
            $('#imageResult')
                .attr('src', e.target.result);
            $('#submit-btn').attr('disabled',false);
            $('#submit-btn').css('cursor','default');

            

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

    $(document).ready(function () { 
        $('#upload').on('change', function () {
            input = document.getElementById('upload');
            readURL(input);
        });
    });

/*
$(document).ready(function () {
    $('#submit-btn').on('click', function () {
        alert("clicked");
        console.log("clicked");
    });
}); */

$(document).ready(function() {

    $('#submit-btn').click(function(event){

    $('#submit-btn').attr('disabled',true);
    $('#submit-btn').css('cursor','no-drop');
    
    // Loading Overlay
    $.LoadingOverlay("show",{
        background  : "rgba(85, 0, 85, 0.6)",
        image : "",
        fontawesome : "fa fa-cog fa-spin",
        fontawesomeColor : "rgba(51 , 0, 51, 1)"
    }); 

    var post_url = '/get-solved-res'; //get form action url
    //var request_method = $(this).attr("method"); //get form GET/POST method
    var input = document.getElementById("upload");
    var img_file = input.files[0];
    var reader = new FileReader();
    var img_res;

    reader.readAsDataURL(img_file);
    reader.onload = function () {
        img_res   = reader.result;
         //console.log("Image readed!");

            $.ajax({
                url: post_url,
                type: "GET",
                data: {jsdata: img_res},
                success: function(response) {

                    //console.log("Success "+ response);
                    if (response ==  'No Puzzle Found, Use proper sudoku puzzle image'){
                            //console.log('Inside if Success '+ response);
                            document.getElementById('sol-txt').innerHTML = "<font color='#FF0000'>"+response+"</font>";
                            $("#sol-img").attr('src','');
                            $('#submit-btn').attr('disabled',true);
                            $('#submit-btn').css('cursor','no-drop');
                    }
                    else if (response ==  'No Solution Found'){
                        document.getElementById('sol-txt').innerHTML = "<font color='#FF0000'>"+response+", Use proper sudoku puzzle image</font>";
                        $("#sol-img").html('');
                        $('#submit-btn').attr('disabled',true);
                        $('#submit-btn').css('cursor','no-drop');
                    }
                    else{
                    //console.log('Inside Else');
                    $("#sol-img").html(response);
                    
                    document.getElementById('sol-txt').innerHTML = "Solved Sudoku Puzzle";
                    $('#submit-btn').attr('disabled',false);
                    $('#submit-btn').css('cursor','pointer');
                    }
                    $.LoadingOverlay("hide");
                    //$('#submit-btn').attr('disabled',false);
                    //$('#submit-btn').css('cursor','pointer');
                },
                
                error: function(xhr) {
                //Do Something to handle error
                }
            });
            
        


        };
    reader.onerror = function(){
        console.log(reader.error);
    };    

    //var form_data = new FormData(this);
   
   
    }); 

});


/*
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
*/
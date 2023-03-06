var code;
              function createCaptcha() {
                var buttoncheck= document.getElementById("login");
                buttoncheck.disabled = true;
                //clear the contents of captcha div first 
                document.getElementById('captcha').innerHTML = "";
                var charsArray =
                "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ@!#$%^&*";
                var lengthOtp = 6;
                var captcha = [];
                for (var i = 0; i < lengthOtp; i++) {
                  //below code will not allow Repetition of Characters
                  var index = Math.floor(Math.random() * charsArray.length + 1); //get the next character from the array
                  if (captcha.indexOf(charsArray[index]) == -1)
                    captcha.push(charsArray[index]);
                  else i--;
                }
                var canv = document.createElement("canvas");
                canv.id = "captcha";
                canv.width = 100;
                canv.height = 50;
                var ctx = canv.getContext("2d");
                ctx.font = "25px Georgia";
                ctx.strokeText(captcha.join(""), 0, 30);
                //storing captcha so that can validate you can save it somewhere else according to your specific requirements
                code = captcha.join("");
              
                
                document.getElementById("captcha").appendChild(canv); // add the canvas to the body element
                document.getElementById("canvas").style.color = 'red';
              }


              passwordInput.addEventListener("input", function() {
  if (passwordInput.validity.patternMismatch) {
    passwordInput.setCustomValidity("Password must contain at least 8 characters, including a lowercase letter, an uppercase letter, a number, and a special character (@, #, $, %, ^, &, +, =).");
  }
       else {
            alert("Succesfully signed");
          
            
          }
          
        })
      
         
              function validateCaptcha() {
                event.preventDefault();
                debugger
                var buttoncheck= document.getElementById("login");
                buttoncheck.disabled = true;
                if (document.getElementById("cpatchaTextBox").value == code) {
                  buttoncheck.disabled= false;
                  // alert(" succesful")
                  return true
             

         
                }
              
                else
                {
                  // alert("Invalid try Again");
                 
                  createCaptcha();
                  return false

                }
              }
              

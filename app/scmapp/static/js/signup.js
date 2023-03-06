function verify()
{
    var username = document.getElementById("username").value;
    var email = document.getElementById("email").value;
    var password = document.getElementById("password").value;
    var confirmpassword = document.getElementById("cpassword").value;

    //validation for all fields
    if (username == "" && email == "" && password == "" && confirmpassword =="") 
    {
      document.getElementById("errorMsg").innerHTML = "Please fill the required fields";
      return false;       
    }
    else 
    {
      document.getElementById("errorMsg").innerHTML = "";
    }
    
    //validation for UserName
    if(username=="")
    {
      document.getElementById("userMsg").innerHTML = "Please Username!";
      return false;       
    }
    else 
    {
      document.getElementById("userMsg").innerHTML = "";
    }
    
    //validation for Email
    if(email=="")
    {
      document.getElementById("emailMsg").innerHTML = "Please enter Email!";
      return false;  
    }
    else if(ValidateEmail(document.getElementById("email"))==false)
    {
      document.getElementById("emailMsg").innerHTML = "Email not Valid!";
      // alert("condition")
      return false; 
    }
    else
    {
      document.getElementById("emailMsg").innerHTML = "";
    }


    //password validation
    if(password=="")
    {
      document.getElementById("passMsg").innerHTML = "Please enter Password!";
      return false;
    }
    else if(CheckPassword(document.getElementById("password"))==false)
    {
      document.getElementById("passMsg").innerHTML = "Must have one Upper, LowerCase, Special Character and length must be greater than 8 and less than 15";
      return false;
    }
    else
    {
      document.getElementById("passMsg").innerHTML = "";
    }

    //Confirm password validation
    if(confirmpassword=="")
    {
      document.getElementById("cpassMsg").innerHTML = "Please ReEnter Password!";
      return false;
    }
    else if(password!=confirmpassword)
    {
      document.getElementById("cpassMsg").innerHTML = "Password not Matched";
      return false;
    }
    else{
      document.getElementById("cpassMsg").innerHTML = "Password not Matched";
    }
}

function CheckPassword(inputtxt) 
{ 
  var paswd=  /^(?=.*[0-9])(?=.*[!@#$%^&*])[a-zA-Z0-9!@#$%^&*]{8,15}$/;
  if(inputtxt.value.match(paswd)) 
  { 
    return true;
  }
  else
  { 
    return false;
  }
} 

function ValidateEmail(inputText)
{
  var mailformat = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
  if(inputText.value.match(mailformat))
  {
    return true;
  }
  else
  {
    return false;
  }
}


  // else
  // {
  //   document.getElementById("emailMsg").innerHTML = "Email not Valid!";
  //   return false;
  // }

// passwordInput.addEventListener("input", function() {
//   if (passwordInput.validity.patternMismatch) {
//     passwordInput.setCustomValidity("Password must contain at least 8 characters, including a lowercase letter, an uppercase letter, a number, and a special character (@, #, $, %, ^, &, +, =).");
//   }
//        else {
//             alert("Succesfully signed");
          
            
//           }
          
//         })
//       }
//       function matchPassword() {  
//         var pw1 = document.getElementById("pswd1");  
//         var pw2 = document.getElementById("pswd2");  
//         if(pw1 != pw2)  
//         {   
//           alert("Passwords did not match");  
//         } else {  
//           alert("Password created successfully");  
//         }  
//       }  
      

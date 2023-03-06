function auth()
     {
      var shipment_invoice_number  = document.getElementById("shipment_invoice_number").value;
      var container_number = document.getElementById("container_number").value;

	var description = document.getElementById("description").value;
  var route_details  = document.getElementById("route_details").value;
  var goods_type = document.getElementById("goods_type").value;
	var device = document.getElementById("device").value;
	var start = document.getElementById("start").value;
  var po_number = document.getElementById("po_number").value;
  var delivary_number = document.getElementById("delivary_number").value;
  
  var ndcnumber = document.getElementById("ndcnumber").value;
	var batch_id = document.getElementById("batch_id").value;
	var serialnumberofgoods  = document.getElementById("serialnumberofgoods").value;
  if (shipment_invoice_number == "" || container_number == "" || description == ""|| route_details==""||
      goods_type == "" || device == "" || start == ""|| po_number=="" || delivary_number=="" || ndcnumber ==""||batch_id==""||serialnumberofgoods==""){
  
  
		document.getElementById("errorMsg").innerHTML = "Please fill the required fields"
		return false;
    
    }
   
}

// $("input.numbers").keypress(function(event) {
//   return /\d/.test(String.fromCharCode(event.keyCode));
// });

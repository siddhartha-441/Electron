// import path from 'path';
// import python from 'python-shell';
function get_district(){
   
    var python = require("python-shell")
    var path = require("path")

    var district_name = document.getElementById("district_name").value
    document.getElementById("district_name").value = "";

    var options = {
        scriptPath : path.join(_dirname,'/../backend/'),
        args : [district_name]
    }

    var dis = new python('district.py',options);

    dis.on('message', function(message) {
        swal(message);
    })
}


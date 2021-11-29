$(document).ready(function () {

    var specialelement = {
        "#editor": function (element, renderer) {
            return true
        }
    };
    $("#pdf").click(function () {
        html2canvas(document.getElementById('topdf') ,{
            onrendered: function (canvas) {

                var img = canvas.toDataURL("image/png");
                var docs = new jsPDF({ format: 'letter', orientation: 'landscape'})
                docs.addImage(img,'JPEG',5,5);
                docs.save("report.pdf")
            }
            });
            });
    });
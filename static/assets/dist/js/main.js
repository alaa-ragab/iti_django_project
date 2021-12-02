$(document).on('click','button[data-toggle="modal"]', function () {
    var action = $(this).attr('href');
    $('.confirm-modal').attr('action', action);
})
$('.confirm-modal button[type="submit"]').on('click', function () {
    $('.confirm-modal').submit();
})
var specialelement={
        "#editor":function (element,renderer){
            return true
        }
    };
    $("#pdf").click(function (){
        var docs=new jsPDF()
        docs.fromHTML($("#topdf").html(),{
            "width":170,
            "elementHandler":specialelement
        })
        docs.save("report.pdf")
    });
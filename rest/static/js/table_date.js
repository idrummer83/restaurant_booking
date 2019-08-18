$(document).ready(function(){
   // Retrieve
   var class_checked = sessionStorage.getItem("class_checked");
   var id_checked = sessionStorage.getItem("id_checked");
    $("#"+id_checked +" > span").addClass(class_checked);
    $("#"+id_checked).attr('href', '/');


   $('.border .badge').on('click', function(){
       var date = $('#datepicker').val();
       if ( $(this).hasClass('.reserved.badge-danger') ) {
            $(this).removeClass('.reserved.badge-danger')
       } else {
           $(this).addClass('reserved badge-danger');
           var field_id = $(this).parent('a').attr('id');
           // Store
           sessionStorage.setItem("class_checked", "reserved badge-danger");
           sessionStorage.setItem("id_checked", field_id);

       }
   });
});
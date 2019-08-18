$(document).ready(function(){

    function compare(){
        var date = $('#datepicker').val();
        $('.border .badge').each(function(){
            var q = $(this).data('table-date');
            if (q == date) {
                $(this).hide()
            } else {
                $(this).show()
            }
        })
    }

    $('#datepicker').val(moment().format('MM/DD/YYYY'));
    $('#datepicker').datepicker({
        onSelect: function() {
                    compare();
        },
    });

    compare();

   $('.next-day').on('click', function () {
       var date = $('#datepicker').datepicker('getDate');
       date.setDate(date.getDate() +1);
       $('#datepicker').datepicker('setDate', date);

       compare();
   });

   $('.prev-day').on('click', function () {
       var date = $('#datepicker').datepicker('getDate');
       date.setDate(date.getDate() -1);
       $('#datepicker').datepicker('setDate', date);

       compare();
   });

   $('.today-date').on('click', function () {
       var date = moment().format('MM/DD/YYYY');
       $('#datepicker').datepicker('setDate', date);

       compare();
   });

   $('.border .badge').on('click', function(){
       var date = $('#datepicker').val();
       if ( $(this).hasClass('.reserved.badge-danger') ) {
            $(this).removeClass('.reserved.badge-danger')
       } else {
           $(this).addClass('reserved badge-danger');
           var field_id = $(this).parent('a').attr('id');
   //         Store
           sessionStorage.setItem("class_checked", "reserved badge-danger");
           sessionStorage.setItem("id_checked", field_id);
       }
   });
});
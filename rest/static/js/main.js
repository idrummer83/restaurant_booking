$(document).ready(function(){

    function compare(date){
        console.log('in date-', date);
        $('.get-table .badge').each(function(){
            var q = $(this).data('table-date');
            var a = q.split(',');
            a.pop();
            console.log(a);

            for (let i = 0; i < a.length; i++){
                if (a[i] == date) {
                    console.log(a[i]);
                    $(this).parent('div').addClass('badge-danger');
                    break
                } else {
                    $(this).parent('div').removeClass('badge-danger')
                }
            }
        })
    }

    $('#datepicker').datepicker({
        dateFormat: "dd/mm/yy",
        onSelect: function () {
            var qwe = $(this).val();
            compare(qwe);
        }
    });

    // compare();

   $('.next-day').on('click', function () {
       var date = $('#datepicker').datepicker('getDate');
       date.setDate(date.getDate() +1)
       $('#datepicker').datepicker('setDate', date);
       var qqq = $('#datepicker').val();

       compare(qqq);
   });

   $('.prev-day').on('click', function () {
       var date = $('#datepicker').datepicker('getDate');
       date.setDate(date.getDate() -1)
       $('#datepicker').datepicker('setDate', date);
       var qqq = $('#datepicker').val();

       compare(qqq);
   });

   $('.today-date').on('click', function () {
       var qwe = $('#datepicker').val(moment().format('DD/MM/YYYY'));

       compare(qwe.val());
   });

   /* new */

   $('.get-table').on('click', function(){
       $(this).toggleClass('badge-danger');
   });

});
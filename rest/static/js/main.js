$(document).ready(function(){

    function compare(date){
        $('.get-table .badge').each(function(){
            var q = $(this).data('table-date');
            var a = q.split(',');
            a.pop();

            for (let i = 0; i < a.length; i++){
                if (a[i] == date) {
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
       date.setDate(date.getDate() -1);
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
        var this_t = $(this);
        $(this_t).toggleClass('badge-danger');
        var t_id = $(this_t).attr('id');
        var form = $('.form_template').clone()[0];
        var act_form = $(form).attr('action');

        if ($('.form_list .form_template').length ){

            for (var i=0;i<$('.form_list .form_template').length;i++){
                if ( $('.form_list .form_template')[i].getAttribute('id') == 'id-'+t_id ){
                    $('.form_list .form_template')[i].remove();
                    return false;
                }
            }
            $('.form_list').append($(form).attr('action', act_form + t_id).attr('id', 'id-'+t_id));
            form = null;

        } else {
            $('.form_list').append($(form).attr('action', act_form + t_id).attr('id', 'id-'+t_id));
            form = null;
        }
   });

});
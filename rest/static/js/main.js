$(document).ready(function(){

    function compare(date){
        $('.get-table .badge').each(function(){
            let q = $(this).data('table-date');
            let a = q.split(',');
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
                    let qwe = $(this).val();
                    compare(qwe);
                    $('.control-date').text(qwe);
                }
    });

    compare($('#datepicker').val());
    $('.control-date').text($('#datepicker').val());

   $('.next-day').on('click', function () {
       let date = $('#datepicker').datepicker('getDate');
       date.setDate(date.getDate() +1);
       $('#datepicker').datepicker('setDate', date);
       let qqq = $('#datepicker').val();

       compare(qqq);
       $('.control-date').text(qqq);
   });

   $('.prev-day').on('click', function () {
       let date = $('#datepicker').datepicker('getDate');
       date.setDate(date.getDate() -1);
       $('#datepicker').datepicker('setDate', date);
       let qqq = $('#datepicker').val();

       compare(qqq);
       $('.control-date').text(qqq);
   });

   $('.today-date').on('click', function () {
       let qwe = $('#datepicker').val(moment().format('DD/MM/YYYY'));

       compare(qwe.val());
       $('.control-date').text(qwe.val());
   });

   /* new */

    $('.get-table').on('click', function(e){

        if ($(this).hasClass('badge-danger')) {
            return false;
        } else {
            // let q = $(this).children('.badge').data('table-date');
            // let a = q.split(',');
            // a.pop();
            // console.log(a[1]);

            let this_t = $(this);
            $(this_t).toggleClass('badge-success');
            let t_id = $(this_t).attr('id');
            let form = $('.form_template').clone()[0];
            let act_form = $(form).attr('action');

            if ($('.form_list .form_template').length ){

                for (let i=0;i<$('.form_list .form_template').length;i++){
                    if ( $('.form_list .form_template')[i].getAttribute('id') == 'id-'+t_id ){
                        $('.form_list .form_template')[i].remove();
                        return false;
                    }
                }
                $('.form_list').append(
                    $(form).attr('action', act_form + t_id).attr('id', 'id-'+t_id)
                );
                let zzz = $('.control-date').text().toString();
                $('.form_list #id-'+ t_id + ' #date').val(zzz);
                $('.form_list #id-'+ t_id + ' #table').val(t_id);
                form = null;

            } else {
                $('.form_list').append($(form).attr('action', act_form + t_id).attr('id', 'id-'+t_id));
                let zzz = $('.control-date').text().toString();
                $('.form_list #id-'+ t_id + ' #date').val(zzz);
                $('.form_list #id-'+ t_id + ' #table').val(t_id);
                    form = null;
            }
        }


   });

});
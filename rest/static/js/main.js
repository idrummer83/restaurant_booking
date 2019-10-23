$(document).ready(function(){

    function compare(date){
        $('.get-table .badge').each(function(){
            let tabledate = $(this).data('table-date');
            let tabledatesplit = tabledate.split(',');
            tabledatesplit.pop();

            for (let i = 0; i < tabledatesplit.length; i++){
                if (tabledatesplit[i] == date) {
                    $(this).parent('div').addClass('badge-danger');
                    break
                } else {
                    $(this).parent('div').removeClass('badge-danger')
                }
            }
        })
    }

    function selected(date){
        $('.form_list #id_visitor_table_date').each(function(){
            $(this).val(date);
        });
    }

    function compare_selected(){
        for (var x = 0; x < $('.get-table').length; x++){
            var div = $('.get-table')[x];
            var id = $(div).attr('id');
            if ($(div).hasClass('badge-danger')) {
                $('.form_list #id-'+ id).find('button').attr('disabled','disabled');
            } else if ($(div).hasClass('badge-success')) {
                $('.form_list #id-'+ id).find('button').removeAttr('disabled');
            }
        }
    }

    $('#datepicker').datepicker({
        dateFormat: "dd/mm/yy",
        onSelect: function () {
                    let selectval = $(this).val();
                    compare(selectval);
                    selected(selectval);
                    compare_selected();
                    $('.control-date').text(selectval);
                }
    });

    compare($('#datepicker').val());
    $('.control-date').text($('#datepicker').val());

    $('.next-day').on('click', function () {
        let date = $('#datepicker').datepicker('getDate');
        date.setDate(date.getDate() +1);
        $('#datepicker').datepicker('setDate', date);
        let dateval = $('#datepicker').val();

        compare(dateval);
        selected(dateval);
        compare_selected();
        $('.control-date').text(dateval);
    });

    $('.prev-day').on('click', function () {
        let date = $('#datepicker').datepicker('getDate');
        date.setDate(date.getDate() -1);
        $('#datepicker').datepicker('setDate', date);
        let dateval = $('#datepicker').val();

        compare(dateval);
        selected(dateval);
        compare_selected();
        $('.control-date').text(dateval);
    });

   $('.today-date').on('click', function () {
       let qwe = $('#datepicker').val(moment().format('DD/MM/YYYY'));

       compare(qwe.val());
       selected(qwe.val());
       compare_selected();
       $('.control-date').text(qwe.val());
   });

   /* new */

    $('.get-table').on('click', function(e){

        if ($(this).hasClass('badge-danger')) {
            return false;
        } else {

            let this_t = $(this);

            $(this_t).toggleClass('badge-success');
            let controldate = $('.control-date').text().toString();
            let t_id = $(this_t).attr('id');
            $(this_t).attr( 'data-' + controldate.replace(/\//g, ''), t_id);
            let form = $('.form_template').clone()[0];

            if ($('.form_list .form_template').length ){

                for (let i=0;i<$('.form_list .form_template').length;i++){
                    if ( $('.form_list .form_template')[i].getAttribute('id') == 'id-'+t_id ){
                        $('.form_list .form_template')[i].remove();
                        return false;
                    }
                }
                $('.form_list').append($(form).attr('id', 'id-'+t_id));
                $('.form_list #id-'+ t_id + ' #id_visitor_table_date').val(controldate);
                $('.form_list #id-'+ t_id + ' #id_visitor_table').val(t_id);
                form = null;

            } else {
                $('.form_list').append($(form).attr('id', 'id-'+t_id));
                $('.form_list #id-'+ t_id + ' #id_visitor_table_date').val(controldate);
                $('.form_list #id-'+ t_id + ' #id_visitor_table').val(t_id);
                    form = null;
            }
        }
    });

    $(document).on("click", ".form_list .del-form" , function() {
        let table_id = $(this).parent().attr('id').slice(3);
        $(this).parent().remove();
        $('.table-wrap').find('#'+table_id).removeClass('badge-success');
    });

});
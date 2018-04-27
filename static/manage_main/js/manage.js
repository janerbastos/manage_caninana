//Gerenciador de conteúdo no site.
$('#form_modal_comum').on('show.bs.modal', function(event) {
	var button = $(event.relatedTarget);

	var username = button.data('username');
	var full_name = button.data('full_name');
	var action = button.data('action');
	var url = button.data('url');
	var view = button.data('view');
    path = '';

	var modal = $(this);
	var form = modal.find('form');
	//var action = form.attr('data-url-base')

    if(view=='usuarios'){
        path = url+'?view='+view+'&action='+action+'&username='+username;
        if(action == 'desvincular-usuario'){
            modal.find('.modal-title').html('Desvincular usuário do(s) evento(s).')
        }
        if(action == 'reset-pessaword'){
            modal.find('.modal-title').html('Resetar senha do usuário.')
        }
    }
	form.attr('action', path);

	modal.find('.modal-body h4').html(full_name)

    action_ajax(path, modal)
})

function action_ajax(url, modal) {
        $.ajax({
        url: url,
        data: {},
        dataType: 'json',
        success: function (data) {
            modal.find('.modal-body p').html(data.result);
        }
    });
}
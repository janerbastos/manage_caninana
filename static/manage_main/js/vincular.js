//Vincular usuario ao site
$('#vincular_usuario_site').on('show.bs.modal', function(event) {
	var button = $(event.relatedTarget);

	var username = button.data('username');
	var full_name = button.data('full_name');

	var modal = $(this);
	var form = modal.find('form');
	//var action = form.attr('data-url-base')

	form.attr('action', '/manage_main/?view=usuarios&action=vincular-usuario&username='+username);

	modal.find('.modal-body h4').html(full_name)
})
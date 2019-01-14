var dtLanguage = {
	"sProcessing":     "Procesando...",
	"sLengthMenu":     "Mostrar _MENU_ registros",
	"sZeroRecords":    "No se encontraron resultados",
	"sEmptyTable":     "Ningún dato disponible en esta tabla",
	"sInfo":           "Mostrando registros del _START_ al _END_ de un total de _TOTAL_ registros",
	"sInfoEmpty":      "Mostrando registros del 0 al 0 de un total de 0 registros",
	"sInfoFiltered":   "(filtrado de un total de _MAX_ registros)",
	"sInfoPostFix":    "",
	"sSearch":         "Buscar:",
	"sUrl":            "",
	"sInfoThousands":  ",",
	"sLoadingRecords": "Cargando...",
	"oPaginate": {
		"sFirst":    "|<",
		"sLast":     ">|",
		"sNext":     ">",
		"sPrevious": "<"
	},
	"oAria": {
		"sSortAscending":  ": Activar para ordenar la columna de manera ascendente",
		"sSortDescending": ": Activar para ordenar la columna de manera descendente"
	}
};


$(document).ready(function() {
  $('a.active').removeClass('active');
  $('a[href="' + location.pathname + '"]').closest('a').addClass('active'); 

  setTimeout(function() {
        $(".alert").alert('close');
  }, 5000);

  $('#dtHistory').DataTable({"language": dtLanguage, info: false, searching: false, pageLength: 25, pagingType: "first_last_numbers"});
  $('.dataTables_length').addClass('bs-select');

  $('#dtAlerts').DataTable({"language": dtLanguage, info: false, searching: false, pageLength: 25, pagingType: "first_last_numbers"});
  $('.dataTables_length').addClass('bs-select');
});

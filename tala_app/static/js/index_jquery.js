// use this to fix routing issues: 
	$(document).ready(function() {

		// menu
		$('#menu-button').sidr({
			name: 'menu-sidr',
			source: '#menu-content',
			side: 'right',
		});
		
		$("#main-body, #menu-sidr").click(function() {
			$.sidr('close', 'menu-sidr');
		});

	});



var valido = true;	

$(document).ready(function(){	    
	$('#nombres').focus();		
});

function valida_nombres() {
	if ( $('#nombres').val().trim().length < 3 ) {
		$('#nombre_mensaje').text("Nombre muy corto");
		switch_class($("#nombre_mensaje"), $('#nombres'), false)
		valido = false;
	} else {
		$('#nombre_mensaje').text("");
		switch_class($("#nombre_mensaje"), $('#nombres'), true)
		valido = true;
	}
};

function valida_email() {
	if ( $('#email').val().trim().length == 0 ) {
		$('#email_mensaje').text("Campo obligatorio");
		switch_class($("#email_mensaje"), $('#email'), false)
		valido = false;
	} else {
		$.getJSON($SCRIPT_ROOT + '/verifica_email', {
           	email : $("#email").val()
        }, function(data) {
	        if (data.result == false) {
	        	$("#email_mensaje").text("Email ya se encuentra registrado");
	        	switch_class($("#email_mensaje"), $('#email'), false)
	        	valido = false;
	        } else {
	        	$("#email_mensaje").text("");
	        	switch_class($("#email_mensaje"), $('#email'), true)
	        	valido = true;
	        }
	    });			    	
	} 
};

function valida_usuario() {
	if ( $('#usuario').val().trim().length < 6) {
		$("#usuario_mensaje").text("Mínimo 6 caracteres");
        switch_class($("#usuario_mensaje"), $('#usuario'), false)
        valido = false;
	} else {	        
        $.getJSON($SCRIPT_ROOT + '/verifica_usuario', {
           	usuario : $("#usuario").val()
        }, function(data) {
	        if (data.result == false) {
	        	$("#usuario_mensaje").text("Usuario no disponible");
	        	switch_class($("#usuario_mensaje"), $('#usuario'), false)
	        	valido = false;
	        } else {
	        	$("#usuario_mensaje").text("Usuario disponible");
	        	switch_class($("#usuario_mensaje"), $('#usuario'), true)
	        	valido = true;
	        }
	    });		    
	}
};

function valida_pass() {
	if ( $('#password').val().trim().length == 0 ) {
		$('#password_mensaje').text("Campo obligatorio");
		switch_class($("#password_mensaje"), $('#password'), false);
		valido = false;
	} else {
		$('#nombre_mensaje').text("");
		switch_class($("#password_mensaje"), $('#password'), true);
		valido = true;
	}
};

function comparar_pass() {
	var pass1 = $('#password').val();
	if ( $('#password2').val() == pass1 ) {
		$('#password_mensaje2').text("Contraseñas coinciden");
		switch_class($("#password_mensaje2"), $('#password2'), true)
		valido = true;
	} else {
		$('#password_mensaje2').text("Contraseñas no coinciden");
		switch_class($("#password_mensaje2"), $('#password2'), false)
		valido = false;
	}
};

function switch_class(span_id, input_id, disponible) {
	if ( disponible ) {
    	span_id.removeClass('respuesta-formulario-error');
    	span_id.addClass('respuesta-formulario-correcto');	    	
    	input_id.removeClass('error-input-formulario');
		input_id.addClass('correcto-input-formulario');
    } else {
    	span_id.removeClass('respuesta-formulario-correcto');
		span_id.addClass('respuesta-formulario-error');
		input_id.removeClass('correcto-input-formulario');
    	input_id.addClass('error-input-formulario');						
    }		
};

function validar_datos() {
	valida_nombres();
	valida_email();
	valida_usuario();
	valida_pass();		
	if ( valido == true ) {
		$('#submit_mensaje').text("");
		document.sign_up.submit();
	} else {
		$('#submit_mensaje').text("Revise el formulario de registro antes de continuar");
	}	
};


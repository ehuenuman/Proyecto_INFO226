$(document).ready(function(){                         
        var consulta;
            
        //hacemos focus
        $("#usuario").focus();
                                                 
        // Cuando este onBlur
        $("#usuario").blur(function(e){
            //obtenemos el texto introducido en el campo
            consulta = $("#usuario").val();
            $.ajax({
                type: "GET",
                url: "verifica_usuario.php?usuario=" + consulta,                             
                dataType: "html",
                error: function(){
                    alert("Error Petición AJAX");
                },
                success: function(data){
                    $("#msj").html(data);                    
                }
            });
       });
});
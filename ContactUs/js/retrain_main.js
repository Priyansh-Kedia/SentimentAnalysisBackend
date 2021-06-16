(function($) {

	"use strict";


  // Form
	var contactForm = function() {
		if ($('#contactForm').length > 0 ) {
			$( "#contactForm" ).validate( {
				rules: {
					review: "required"
				},
				messages: {
					review: "Please enter a review"
				},
				/* submit via ajax */
				
				submitHandler: function(form) {		
					var $submit = $('.submitting'),
						waitText = 'Submitting...';

					let url = "/add_review/"
					console.log(document.getElementById("review").placeholder)
					console.log(parseInt(document.getElementById("prediction_actual").value))
					$.ajax({   	
				      type: "POST",
				      url: url,
					  contentType: "application/json",
       				  dataType: "json",
					  data: JSON.stringify({
						  'review' : document.getElementById("review").placeholder,
						  'prediction': parseInt(document.getElementById("prediction_actual").value)
					  }),
				      beforeSend: function() { 
				      	$submit.css('display', 'block').text(waitText);
				      },
				      success: function(msg) {
		               	$('#form-message-warning').hide();
				            setTimeout(function(){
		               		$('#contactForm').fadeIn();
		               	}, 1000);
						   $('#form-message-success').text(msg)
				            setTimeout(function(){
				               $('#form-message-success').fadeIn();   
		               	}, 1400);

		               	setTimeout(function(){
				               $('#form-message-success').fadeOut();   
		               	}, 8000);
						
		               	setTimeout(function(){
				               $submit.css('display', 'none').text(waitText);  
		               	}, 1400);

		               	setTimeout(function(){
		               		$( '#contactForm' ).each(function(){
											    this.reset();
											});
		               	}, 1400);
				      },
				      error: function(e) {
				      	$('#form-message-warning').html("Something went wrong. Please try again.");
				         $('#form-message-warning').fadeIn();
				         $submit.css('display', 'none');
				      }
			      });    		
		  		} 
			});
		}
	};
	contactForm();

})(jQuery);

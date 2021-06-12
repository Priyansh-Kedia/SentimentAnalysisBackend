(function($) {

	"use strict";


  // Form
	var contactForm = function() {
		if ($('#contactForm').length > 0 ) {
			$( "#contactForm" ).validate( {
				rules: {
					// name: "required",
					// subject: "required",
					// email: {
					// 	required: true,
					// 	email: true
					// },
					// message: {
					// 	required: true,
					// 	minlength: 5
					// }
					review: "required"
				},
				messages: {
					// name: "Please enter your name",
					// subject: "Please enter your subject",
					// email: "Please enter a valid email address",
					// message: "Please enter a message"
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
					  data: JSON.stringify({
						  'review' : document.getElementById("review").placeholder,
						  'prediction': parseInt(document.getElementById("prediction_actual").value)
					  }),
					  dataType: 'json',
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

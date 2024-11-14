"use strict";

var KTSignupGeneral = function () {
    var form, submitButton, validation, passwordMeter;

    var checkPasswordStrength = function () {
        return passwordMeter.getScore() > 50;
    };

    return {
        init: function () {
            form = document.querySelector("#kt_sign_up_form");
            submitButton = document.querySelector("#kt_sign_up_submit");
            passwordMeter = KTPasswordMeter.getInstance(form.querySelector('[data-kt-password-meter="true"]'));

            validation = FormValidation.formValidation(form, {
                fields: {
                    email: {
                        validators: {
                            notEmpty: { message: "Email address is required" },
                            regexp: {
                                regexp: /^[^\s@]+@[^\s@]+\.[^\s@]+$/,
                                message: "The value is not a valid email address"
                            }
                        }
                    },
                    password: {
                        validators: {
                            notEmpty: { message: "The password is required" },
                            callback: {
                                message: "Please enter valid password",
                                callback: function (input) {
                                    if (input.value.length > 0) return checkPasswordStrength();
                                }
                            }
                        }
                    },
                    "confirm-password": {
                        validators: {
                            notEmpty: { message: "The password confirmation is required" },
                            identical: {
                                compare: function () {
                                    return form.querySelector('[name="password"]').value;
                                },
                                message: "The password and its confirm are not the same"
                            }
                        }
                    },
                    toc: {
                        validators: {
                            notEmpty: { message: "You must accept the terms and conditions" }
                        }
                    }
                },
                plugins: {
                    trigger: new FormValidation.plugins.Trigger(),
                    bootstrap: new FormValidation.plugins.Bootstrap5({
                        rowSelector: ".fv-row",
                        eleInvalidClass: "",
                        eleValidClass: ""
                    })
                }
            });

            submitButton.addEventListener("click", function (e) {
                e.preventDefault();

                // Revalidate password field
                validation.revalidateField("password");

                // Validate form before submission
                validation.validate().then(function (status) {
                    if (status === "Valid") {
                        // Show loading indication
                        submitButton.setAttribute("data-kt-indicator", "on");
                        submitButton.disabled = true;

                        var csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
                        axios.post(form.getAttribute("action"), new FormData(form), {
                            headers: {
                                "X-CSRFToken": csrfToken
                            }
                        })
                        .then(function (response) {
                            // Check for successful response
                            if (response.status === 200) {
                                form.reset(); // Reset the form

                                // Redirect or show success popup
                                var redirectUrl = form.getAttribute("data-kt-redirect-url");
                                if (redirectUrl) {
                                    location.href = redirectUrl;
                                } else {
                                    Swal.fire({
                                        text: "You have successfully signed up!",
                                        icon: "success",
                                        buttonsStyling: false,
                                        confirmButtonText: "Ok, got it!",
                                        customClass: { confirmButton: "btn btn-primary" }
                                    });
                                }
                            }
                        })
                        .catch(function (error) {
                            Swal.fire({
                                text: error.response.data.message,
                                icon: "error",
                                buttonsStyling: false,
                                confirmButtonText: "Ok, got it!",
                                customClass: { confirmButton: "btn btn-primary" }
                            });
                        })
                        .finally(function () {
                            // Remove loading indication
                            submitButton.removeAttribute("data-kt-indicator");
                            submitButton.disabled = false;
                        });
                    } else {
                        Swal.fire({
                            text: "Please fill out the form correctly before submitting.",
                            icon: "error",
                            buttonsStyling: false,
                            confirmButtonText: "Ok, got it!",
                            customClass: { confirmButton: "btn btn-primary" }
                        });
                    }
                });
            });
        }
    };
}();

// On document ready
KTUtil.onDOMContentLoaded(function () {
    KTSignupGeneral.init();
});

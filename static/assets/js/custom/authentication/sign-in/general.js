"use strict";
var KTSigninGeneral = (function () {
    var t, e, r;
    return {
        init: function () {
            (t = document.querySelector("#kt_sign_in_form")),
                (e = document.querySelector("#kt_sign_in_submit")),
                (r = FormValidation.formValidation(t, {
                    fields: {
                        email: {
                            validators: {
                                regexp: {
                                    regexp: /^[^\s@]+@[^\s@]+\.[^\s@]+$/,
                                    message: "The value is not a valid email address",
                                },
                                notEmpty: { message: "Email address is required" },
                            },
                        },
                        password: {
                            validators: { notEmpty: { message: "The password is required" } },
                        },
                    },
                    plugins: {
                        trigger: new FormValidation.plugins.Trigger(),
                        bootstrap: new FormValidation.plugins.Bootstrap5({
                            rowSelector: ".fv-row",
                            eleInvalidClass: "",
                            eleValidClass: "",
                        }),
                    },
                })),
                !(function (t) {
                    try {
                        return new URL(t), !0;
                    } catch (t) {
                        return !1;
                    }
                })(e.closest("form").getAttribute("action"))
                    ? e.addEventListener("click", function (i) {
                        i.preventDefault();
                        r.validate().then(function (validationResult) {
                            if (validationResult === "Valid") {
                                e.setAttribute("data-kt-indicator", "on");
                                e.disabled = true;
                                axios
                                    .post(
                                        e.closest("form").getAttribute("action"),
                                        new FormData(t)
                                    )
                                    .then(function (response) {
                                        if (response.status === 200) {
                                            // Successful login
                                            Swal.fire({
                                                text: "You have successfully logged in!",
                                                icon: "success",
                                                buttonsStyling: false,
                                                confirmButtonText: "Ok, got it!",
                                                customClass: { confirmButton: "btn btn-primary" },
                                            }).then(function () {
                                                // Reset form and redirect if URL exists
                                                t.reset();
                                                var redirectUrl = t.getAttribute(
                                                    "data-kt-redirect-url"
                                                );
                                                if (redirectUrl) {
                                                    location.href = redirectUrl;
                                                }
                                            });
                                        } else {
                                            // Show the message from the response
                                            Swal.fire({
                                                text:
                                                    response.data.message ||
                                                    "An error occurred, please try again.",
                                                icon: "error",
                                                buttonsStyling: false,
                                                confirmButtonText: "Ok, got it!",
                                                customClass: { confirmButton: "btn btn-primary" },
                                            });
                                        }
                                    })
                                    .catch(function (error) {
                                        // Handle network or other errors
                                        
                                        Swal.fire({
                                            text: error.response.data.message,
                                            icon: "error",
                                            buttonsStyling: false,
                                            confirmButtonText: "Ok, got it!",
                                            customClass: { confirmButton: "btn btn-primary" },
                                        });
                                    })
                                    .finally(function () {
                                        e.removeAttribute("data-kt-indicator");
                                        e.disabled = false;
                                    });
                            } else {
                                Swal.fire({
                                    text: "Sorry, looks like there are some errors detected, please try again.2",
                                    icon: "error",
                                    buttonsStyling: false,
                                    confirmButtonText: "Ok, got it!",
                                    customClass: { confirmButton: "btn btn-primary" },
                                });
                            }
                        });
                    })
                    : e.addEventListener("click", function (i) {
                        i.preventDefault();
                        r.validate().then(function (validationResult) {
                            if (validationResult === "Valid") {
                                e.setAttribute("data-kt-indicator", "on");
                                e.disabled = true;
                                const csrfToken = document
                                    .querySelector('meta[name="csrf-token"]')
                                    .getAttribute("content");
                                    axios
                                    .post(
                                        e.closest("form").getAttribute("action"),
                                        new FormData(t),
                                        {
                                            headers: {
                                                "X-CSRFToken": csrfToken, // CSRF token
                                            },
                                        }
                                    )
                                    .then(function (response) {
                                        if (response.status === 200) {
                                            Swal.fire({
                                                text: "You have successfully logged in!",
                                                icon: "success",
                                                buttonsStyling: false,
                                                confirmButtonText: "Ok, got it!",
                                                customClass: { confirmButton: "btn btn-primary" },
                                            }).then(function () {
                                                t.reset();
                                                var redirectUrl = t.getAttribute("data-kt-redirect-url");
                                                if (redirectUrl) {
                                                    location.href = redirectUrl;
                                                }
                                            });
                                        }
                                    })
                                    .catch(function (error) {
                                        let message = "Sorry, looks like there are some errors detected, please try again.3";
                                        
                                        // Check if there's a specific error message in the server's response
                                        if (error.response && error.response.data && error.response.data.message) {
                                            message = error.response.data.message;
                                        }
                                        
                                        Swal.fire({
                                            text: message,
                                            icon: "error",
                                            buttonsStyling: false,
                                            confirmButtonText: "Ok, got it!",
                                            customClass: { confirmButton: "btn btn-primary" },
                                        });
                                    })
                                    .finally(function () {
                                        e.removeAttribute("data-kt-indicator");
                                        e.disabled = false;
                                    });
                                
                            } else {
                                Swal.fire({
                                    text: "Sorry, looks like there are some errors detected, please try again.4",
                                    icon: "error",
                                    buttonsStyling: false,
                                    confirmButtonText: "Ok, got it!",
                                    customClass: { confirmButton: "btn btn-primary" },
                                });
                            }
                        });
                    });
        },
    };
})();
KTUtil.onDOMContentLoaded(function () {
    KTSigninGeneral.init();
});

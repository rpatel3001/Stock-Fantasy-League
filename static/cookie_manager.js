/*var user_profile;
function onSignIn(googleUser) {
  user_profile = googleUser.getBasicProfile();
  console.log('ID: ' + user_profile.getId()); // Do not send to your backend! Use an ID token instead.
  console.log('Name: ' + user_profile.getName());
  console.log('Image URL: ' + user_profile.getImageUrl());
  console.log('Email: ' + user_profile.getEmail()); // This is null if the 'email' scope is not present.
}*/
/**
 * The Sign-In client object.
 */
var auth2;

/**
 * Initializes the Sign-In client.
 */
var initClient = function() {
    gapi.load('auth2', function(){
        /**
         * Retrieve the singleton for the GoogleAuth library and set up the
         * client.
         */
        auth2 = gapi.auth2.init({
            client_id: 'CLIENT_ID.apps.googleusercontent.com'
        });

        // Attach the click handler to the sign-in button
        auth2.attachClickHandler('signin-button', {}, onSuccess, onFailure);
    });
};

/**
 * Handle successful sign-ins.
 */
var onSuccess = function(user) {
    console.log('Signed in as ' + user.getBasicProfile().getName());
 };

/**
 * Handle sign-in failures.
 */
var onFailure = function(error) {
    console.log(error);
};
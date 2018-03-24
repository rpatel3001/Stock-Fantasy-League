var user_profile;
function onSignIn(googleUser) {
  user_profile = googleUser.getBasicProfile();
  console.log('ID: ' + user_profile.getId()); // Do not send to your backend! Use an ID token instead.
  console.log('Name: ' + user_profile.getName());
  console.log('Image URL: ' + user_profile.getImageUrl());
  console.log('Email: ' + user_profile.getEmail()); // This is null if the 'email' scope is not present.
}
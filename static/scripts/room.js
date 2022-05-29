// Video tutorial/codealong here: https://youtu.be/fCpw5i_2IYU

$( '.friend-drawer--onhover' ).on( 'click',  function() {
  
  $( '.chat-bubble' ).hide('slow').show('slow');
  var objDiv = document.getElementById("chat-panel");
  objDiv.scrollTop = objDiv.scrollHeight;
  
});

var objDiv = document.getElementById("chat-panel");
objDiv.scrollTop = objDiv.scrollHeight;

// Video tutorial/codealong here: https://youtu.be/fCpw5i_2IYU
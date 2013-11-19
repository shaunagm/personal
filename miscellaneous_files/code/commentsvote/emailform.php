<?php
include('../../../wp-config.php')
?>
<html>
<body>

<?php


if (isset($_POST['message']))
//if "email" is filled out, send email
  {
  // gets comment info
   $cLink = get_comment_link($_POST['cID']);

  //send email
  $email = 'insertemailhere@insertemailhere.com';
  $subject = 'Hathor Legacy: Flagged Comment';
  $message = 'Link to comment: ' . $cLink . ' reasons given: ' . 
$_POST['message'] ;
  mail($email, $subject, $message, "From:" . 
$email);
  echo "Thank you!  Your response has been sent to a moderator.";
  }
else
//if "email" is not filled out, display the form
  {
  ?>
  <form method='post' action='emailform.php'>
  <input type="hidden" name="cID" id="cID" value="<?php echo 
$_GET['cID']; ?>" />
  Please give your reasons for flagging the message:<br />
  <textarea name='message' rows='15' cols='40'>
  </textarea><br />
  <input type='submit' value='Submit'/>
  </form>
<?php  }
?>

</body>
</html> 

<?php

class user {
  var $name;
  var $pass;
  var $secret;
}

$new_user = new user();

$new_user->name = "admin";
$new_user->pass = &$new_user->secret;

echo (serialize($new_user));

?>
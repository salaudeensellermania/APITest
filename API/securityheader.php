<?php

// Coded By: Salaudeen
// Version: 1.0
// Submission Date: 07/jan/2020
// Revised Date:
// Purpose: To fetch the security header


ECHO "\n";

//$u = readline("Enter username: ");

//$p = readline("Enter password: ");

$u=$argv[1];
$p=$argv[2];

//$u="picoSC@yopmail.com";
//$p="64ddfe0fd8df3cf6311e4056dd74c767f3b4a48d6c30c7685d0f80bcec9f47ee";


   function _generateWSSecurity($user, $password)
   {
      // Creating date using yyyy-mm-ddThh:mm:ssZ format
      $timezone = date_default_timezone_get();
      date_default_timezone_set('Europe/Paris');
      $tm_created = gmdate('Y-m-d\TH:i:s\Z', time());
      $tm_expires = gmdate('Y-m-d\TH:i:s\Z', time() + 180);
      date_default_timezone_set($timezone);

      // Generating, packing and encoding a random number
      $simple_nonce = mt_rand();
      $encoded_nonce = base64_encode(pack('H*', $simple_nonce));

      // Compiling WSS string
      $passdigest = base64_encode(pack('H*',
            sha1(pack('H*', $simple_nonce) . pack('a*', $tm_created) . pack('a*', $password))));

      // Initializing namespaces
      $ns_wsse = 'http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd';
      $ns_wsu = 'http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd';
      $password_type = 'http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-username-token-profile-1.0#PasswordDigest';
      $encoding_type = 'http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-soap-message-security-1.0#Base64Binary';

      // Creating WSS identification header using SimpleXML
      $root = new \SimpleXMLElement('<root/>');

      $security = $root->addChild('wsse:Security', null, $ns_wsse);

      $timestamp = $security->addChild('wsu:Timestamp', null, $ns_wsu);
      $timestamp->addAttribute('wsu:Id', 'Timestamp-28');
      $timestamp->addChild('wsu:Created', $tm_created, $ns_wsu);
      $timestamp->addChild('wsu:Expires', $tm_expires, $ns_wsu);

      $usernameToken = $security->addChild('wsse:UsernameToken', null, $ns_wsse);
      $usernameToken->addChild('wsse:Username', $user, $ns_wsse);

      $password = $usernameToken->addChild('wsse:Password', $passdigest, $ns_wsse);
      $password->addAttribute('Type', $password_type);

      $nonce = $usernameToken->addChild('wsse:Nonce', $encoded_nonce, $ns_wsse);
      $nonce->addAttribute('EncodingType', $encoding_type);

      $usernameToken->addChild('wsu:Created', $tm_created, $ns_wsu);

      // Recovering XML value from that object
      $root->registerXPathNamespace('wsse', $ns_wsse);
      $full = $root->xpath('/root/wsse:Security');
      $auth = $full[0]->asXML();

      return $auth;
   }

ECHO _generateWSSecurity($u,$p);

ECHO "\n";
ECHO "\n";
?>

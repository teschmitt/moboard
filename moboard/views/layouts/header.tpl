<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="moboard -- the tiny moNNT.py viewer">
    <meta name="author" content="Thomas Schmitt">
    <link rel="shortcut icon" href="/favicon.ico">

    <title>moboard | a simple moNNT.py viewer</title>
    <link href="/css/application.css" rel="stylesheet" type="text/css">

  </head>

  <body>
    <main class="container">
    % from config import config
    % if config["show_page_header"]:
        <nav>
          <ul>
            <li><strong><a href="/" role="button">moboard</a> a simple moNNT.py viewer</strong></li>
            <li>|</li>
            <li><a role="button"  class="outline" href="/newsgroups">Go to Newsgroups</a></li>
          </ul>
        </nav>
    % else:
    %     pass


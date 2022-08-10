% include('layouts/header.tpl', title='HomePage')

<h1>Newsgroups</h1>

<ul>
  % for group in newsgroups:
    <li><a href="/newsgroups/{{group}}">{{group}}</a></li>
  % end
</ul>

% include('layouts/footer.tpl')

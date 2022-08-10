% include('layouts/header.tpl', title='HomePage')

<hgroup>
  <h2>Articles</h2>
  <h3>{{newsgroup_name}}</h3>
</hgroup>

<ul>
  % for article in articles:
    <li>{{article}}</li>
  % end
</ul>

% include('layouts/footer.tpl')

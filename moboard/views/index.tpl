% include('layouts/header.tpl', title='HomePage')

<hgroup>
  <h2>Welcome to moboard</h2>
  <h3>A simple moNNT.py viewer</h3>
</hgroup>


<table role="grid">
   <thead>
    <tr>
      <th scope="col">#</th>
      <th scope="col">Date</th>
      <th scope="col">Newsgroup</th>
      <th scope="col">Subject</th>
      <th scope="col">From</th>
    </tr>
  </thead>
  <tbody>
% for num, article in enumerate(articles):
    <tr>
      <th scope="row">{{num + 1}}</th>
      <td>{{article["date"]}}</td>
      <td>{{article["newsgroup_name"]}}</td>
      <td><a href="/article/{{article['message-id']}}">{{article["subject"]}}</a></td>
      <td>{{article["from"]}}</td>
    </tr>
% end
   </tbody>
</table>

% include('layouts/footer.tpl')

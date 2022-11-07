% include('layouts/header.tpl', title='HomePage')

<hgroup>
  <h2>Articles</h2>
  <h3>{{newsgroup_name}}</h3>
</hgroup>


<table role="grid">
   <thead>
    <tr>
      <th scope="col">Date</th>
      <th scope="col">Subject</th>
      <th scope="col">From</th>
    </tr>
  </thead>
  <tbody>
% for num, article in enumerate(articles):
    <tr>
      <td>{{article["date"]}}</td>
      <td><a href="/article/{{article['message-id']}}">{{article["subject"]}}</a></td>
      <td>{{article["from"]}}</td>
    </tr>
% end
   </tbody>
</table>

% include('layouts/footer.tpl')

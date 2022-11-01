% include('layouts/header.tpl', title='HomePage')

<hgroup>
  <h2>Reading</h2>
  <h3><a href="/newsgroups/{{article['newsgroups']}}">{{article['newsgroups']}}</a></h3>
</hgroup>

<article>
<pre style="padding: 2em">
Date:       {{article["date"]}}
From:       {{article["from"]}}
Subject:    {{article["subject"]}}
Newsgroups: {{article['newsgroups']}}

-----------------------------------------------

{{article["body"].replace("\n", "<br \>")}}</pre>
</article>


% include('layouts/footer.tpl')

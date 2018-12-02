<!DOCTYPE html>
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
<header>

<ul class="nav nav-pills">
  <li role="presentation" class="active"><a href="#">Home</a></li>
  <li role="presentation"><a href="#">Messages</a></li>
  <li role="presentation"><a href="#">Profile</a></li>
</ul>
</header>

<body>
    <h1>Welcome Shopfloor</h1>
    {% for item in data %}
    <div class="container">
        <h3>
        <tr>
            <td>{{item[0]}}</td>
            <td>{{item[1]}}</td>
            <td>{{item[2]}}</td>
            <td>{{item[3]}}</td>
            <td>{{item[4]}}</td>
            <td>{{item[5]}}</td>
            <td>{{item[6]}}</td>
            <td>{{item[7]}}</td>
            <td>{{item[8]}}</td>
        </tr>
        </h3>
    </div>

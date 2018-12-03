<!DOCTYPE html>
<link rel="stylesheet"
      href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css"
      integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u"
      crossorigin="anonymous">
<head>
    <style>
th, td {
    padding: 10px;
    text-align: left;
}
</style>
</head>
<header>

    <ul class="nav nav-pills">
        <li role="presentation" class="active"><a href="#">Home</a></li>
        <li role="presentation"><a href="#">Messages</a></li>
        <li role="presentation"><a href="#">Profile</a></li>
    </ul>
</header>

<body>
    <h1>Welcome Shopfloor</h1>
    <div class="container">
        <table style="border-collapse: separate; border-spacing: 10px;" >
            <tr>
                <th><b>UserID</b></th>
                <th><b>Username</b></th>
                <th><b>Password</b></th>
                <th><b>Role</b></th>
                <th><b>First</b></th>
                <th><b>Last</b></th>
                <th><b>eMail</b></th>
                <th><b>Phone #</b></th>
                <th><b>Gender</b></th>
            </tr>
            {% for item in data %}
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
            {% endfor %}
        </table>
    </div>
</body>

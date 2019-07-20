<!DOCTYPE html>
<html lang="en">
<head>

    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <title>InstaBot</title>

    <meta name="description" content="">
    <meta name="author" content="">

    <!-- Favicon -->
    <link rel="icon" href="">

    <!-- Bootstrap 4 -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-alpha.6/css/	bootstrap.min.css" integrity="sha384-rwoIResjU2yc3z8GV/NPeZWAv56rSmLldC3R/AZzGRnGxQQKnKkoFVhFQhNUwEyJ" crossorigin="anonymous">

    <!-- Font Awesome -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.9.0/css/all.css" integrity="sha256-PF6MatZtiJ8/c9O9HQ8uSUXr++R9KBYu4gbNG5511WE=" crossorigin="anonymous" />

    <style>

        .content {
            margin-top: 50px;
        }

    </style>

</head>
<body>

<nav class="navbar navbar-toggleable-md navbar-light bg-faded">
    <button class="navbar-toggler navbar-toggler-right" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
    </button>
    <a class="navbar-brand" href="#">InstaBot</a>

<!--    <div class="collapse navbar-collapse" id="navbarSupportedContent">-->
        <!-- Navbar Left -->
<!--        <ul class="navbar-nav mr-auto">-->
<!--            <li class="nav-item">-->
<!--                <a class="nav-link" href="#">Link</a>-->
<!--            </li>-->
<!--            <li class="nav-item">-->
<!--                <a class="nav-link" href="#">Link</a>-->
<!--            </li>-->
<!--        </ul>-->
        <!-- Navbar Right -->
<!--        <ul class="navbar-nav">-->
<!--            <li class="nav-item">-->
<!--                <a class="nav-link" href="#">Link</a>-->
<!--            </li>-->
<!--            <li class="nav-item">-->
<!--                <a class="nav-link" href="#">Link</a>-->
<!--            </li>-->
<!--        </ul>-->
<!--    </div>-->
</nav>

<div class="content">
    <div class="container">

        <form class="">
            <h1>Start bot</h1>
            <div class="row">
                <div class="form-group col-6">
                    <label for="username">username</label>
                    <input type="text" class="form-control" id="username" name="username">
                </div>
                <div class="form-group col-6">
                    <label for="ROWS">Password</label>
                    <input type="password" class="form-control" id="password" name="password">
                </div>
            </div>


            <div class="form-group ">
                <label for="MENTION">list of posts urls</label>
                <textarea class="form-control"  rows="5" name="URLS"  placeholder="As List"></textarea>
            </div>

            <div class="form-group ">
                <label for="MENTION">NO. of mention ber 1 comments</label>
                <select class="form-control" id="MENTION" name="MENTION">
                    <option value="1" >1</option>
                    <option value="2" >2</option>
                    <option value="3" >3</option>
                    <option value="4" >4</option>
                    <option value="5" >5</option>
                </select>
            </div>
            <div class="form-group ">
                <label for="ROWS">NO. of comments</label>
                <input type="text" class="form-control" id="ROWS" name="ROWS">
            </div>
        </form>

    </div>
</div>

<!-- jQuery -->
<script src="https://code.jquery.com/jquery-3.1.1.slim.min.js" integrity="sha384-A7FZj7v+d/sdmMqp/nOQwliLvUsJfDHW+k9Omg/a/EheAdgtzNs3hpfag6Ed950n" crossorigin="anonymous"></script>

<!-- Tether -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/tether/1.4.0/js/tether.min.js" integrity="sha384-DztdAPBWPRXSA/3eYEEUWrWCy7G5KFbe8fFjk5JAIxUYHKkDx6Qin1DkWx51bBrb" crossorigin="anonymous"></script>

<!-- Bootstrap 4 -->
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-alpha.6/js/bootstrap.min.js" integrity="sha384-vBWWzlZJ8ea9aCX4pEW3rVHjgjt7zpkNpZk+02D9phzyeVkE+jo0ieGizqPLForn" crossorigin="anonymous"></script>

</body>
</html>



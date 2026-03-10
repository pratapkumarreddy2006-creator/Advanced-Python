from flask import Flask, request, render_template_string

app = Flask(__name__)

html = """

<!DOCTYPE html>
<html>
<head>
<title>Nishan Clothing Store</title>

<style>

body{
font-family:Arial;
background:#f2f2f2;
margin:0;
}

header{
background:black;
color:white;
text-align:center;
padding:20px;
}

.container{
display:flex;
flex-wrap:wrap;
justify-content:center;
gap:30px;
padding:30px;
}

.card{
background:white;
width:250px;
border-radius:10px;
box-shadow:0 2px 10px rgba(0,0,0,0.1);
padding:15px;
text-align:center;
}

.card img{
width:100%;
border-radius:10px;
}

.price{
color:green;
font-size:18px;
font-weight:bold;
}

select,input{
width:100%;
padding:7px;
margin-top:5px;
}

button{
background:black;
color:white;
padding:10px;
border:none;
margin-top:10px;
width:100%;
cursor:pointer;
}

button:hover{
background:#333;
}

</style>

</head>

<body>

<header>
<h1>Nishan Clothing Store</h1>
<p>Buy Stylish Clothes Online</p>
</header>

<div class="container">

<div class="card">

<img src="https://images.unsplash.com/photo-1521572163474-6864f9cf17ab">

<h3>Casual T-Shirt</h3>

<p class="price">₹499</p>

<form method="POST">

<label>Size</label>

<select name="size">
<option>S</option>
<option>M</option>
<option>L</option>
<option>XL</option>
</select>

<label>Custom Name</label>

<input type="text" name="custom">

<input type="hidden" name="product" value="T-Shirt">

<button type="submit">Buy Now</button>

</form>

</div>

<div class="card">

<img src="https://images.unsplash.com/photo-1602810318383-e386cc2a3ccf">

<h3>Winter Hoodie</h3>

<p class="price">₹1299</p>

<form method="POST">

<label>Size</label>

<select name="size">
<option>M</option>
<option>L</option>
<option>XL</option>
</select>

<label>Custom Name</label>

<input type="text" name="custom">

<input type="hidden" name="product" value="Hoodie">

<button type="submit">Buy Now</button>

</form>

</div>

</div>

</body>
</html>

"""

@app.route("/", methods=["GET","POST"])
def home():

    if request.method == "POST":

        product = request.form.get("product")
        size = request.form.get("size")
        custom = request.form.get("custom")

        print("Order:", product, size, custom)

    return render_template_string(html)


if __name__ == "__main__":
    app.run(debug=True)
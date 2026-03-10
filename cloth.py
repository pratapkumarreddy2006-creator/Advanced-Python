from flask import Flask, request, render_template_string

app = Flask(__name__)

html = """
<!DOCTYPE html>
<html>
<head>
<title>Clothing Store</title>

<style>
body{font-family:Arial;background:#f5f5f5;margin:0}

header{
background:black;
color:white;
text-align:center;
padding:15px
}

.container{
display:flex;
flex-wrap:wrap;
gap:20px;
justify-content:center;
padding:20px
}

.card{
background:white;
padding:15px;
border-radius:10px;
width:240px;
box-shadow:0 2px 8px rgba(0,0,0,0.1);
text-align:center
}

.price{
color:green;
font-weight:bold
}

input,select{
width:100%;
padding:6px;
margin-top:5px;
border-radius:5px;
border:1px solid #ccc
}

button{
margin-top:10px;
padding:8px 12px;
background:black;
color:white;
border:none;
border-radius:6px
}

</style>

</head>

<body>

<header>
<h1>My Clothing Store</h1>
<p>Customize Your Clothes</p>
</header>

<div class="container">

<div class="card">
<h3>Casual T-Shirt</h3>
<p class="price">₹499</p>

<form method="post">
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

<button type="submit">Buy</button>
</form>

</div>

<div class="card">
<h3>Winter Hoodie</h3>
<p class="price">₹1299</p>

<form method="post">
<label>Size</label>
<select name="size">
<option>M</option>
<option>L</option>
<option>XL</option>
</select>

<label>Custom Name</label>
<input type="text" name="custom">

<input type="hidden" name="product" value="Hoodie">

<button type="submit">Buy</button>
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

        print(f"Order: {product}, Size: {size}, Custom: {custom}")

    return render_template_string(html)


if __name__ == "__main__":
    app.run(debug=True)
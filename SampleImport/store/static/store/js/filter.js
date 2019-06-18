$(document).ready(function(){
    list_all_products();    
});

function list_all_products(){
    $.get("/product/api").success(function(data){
        var lista_producto = "";
        for (producto in data.results) {
            lista_producto += "<div class='col-md-4 col-xs-6'><div class='product'><div class='product-img'>";
            lista_producto += "<img src='../static/store/images/" + data.results[producto].principalCode + ".jpg' alt=''></div>";
            lista_producto += "<div class='product-body'><p class='product-category'>" + "tipo producto" +"</p>";
            lista_producto += "<h3 class='product-name'><a href='../product/" + data.results[producto].id + "'>" + data.results[producto].name + "</a></h3>";
            lista_producto += "<div class='product-rating'><i class='a fa-star'></i><i class='fa fa-star'></i><i class='fa fa-star'></i></div>";
            lista_producto += "</div></div></div>";
            lista_producto += "<div class='clearfix visible-sm visible-xs'></div>";
        }
        if (lista_producto!== "") {
            $("#productos").html(lista_producto);
        }

        var info_paginacion ="<span class='store-qty'>Pag "+ data.current + " de " + data.num_pages + "</span>";
        info_paginacion += "<ul class=store-pagination'>";
        if (data.previous > 0) {
            info_paginacion += "<li><a href='?page="+ data.previous + "'><</a></li>";
        }
        for (let index = 0; index < array.length; index++) {
            const element = array[index];
            
        }        
    });
}

/*
<div class="store-filter clearfix" id="paginacion">
					<span class="store-qty">Pag {{products.number}} de {{products.paginator.num_pages}}</span>
					<ul class="store-pagination">
					{% if products.has_previous %}
						<li><a href="?page={{ products.previous_page_number }}"><</a></li>						
					{% endif %}
					{% for pagenum in products.paginator.page_range %}
						<li class="{% if products.number == pagenum %} active {% endif %}" >
							<a href="?page={{ pagenum}}">{{pagenum}}</a>
						</li>
					{% endfor %}
										
					</ul>
				</div>
 */
/*
<div class="col-md-4 col-xs-6" >
    <div class="product" type="{{producto.model.brand.id}}">
        <div class="product-img">
            <img src="{% static 'store/images/' %}{{producto.principalCode}}.jpg" alt="">
        </div>
        <div class="product-body">
            <p class="product-category">{{producto.model.brand.typeProduct}}</p>
            <h3 class="product-name"><a href="{% url "detail_product" producto.id %}">{{producto.name}}</a></h3>
            <div class="product-rating">
                <i class="fa fa-star"></i>
                <i class="fa fa-star"></i>
                <i class="fa fa-star"></i>
            </div>
            <div class="product-btns">
                {% for store in stores %}
                    {% show_prices producto.id store.id %}
                {% endfor %}									
            </div>
        </div>
    </div>
</div>
<!-- /product -->
<div class="clearfix visible-sm visible-xs"></div>
*/
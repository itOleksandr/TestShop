// Код буде виконуватися коли загрузиться вся сторінка
$(document).ready(function () {

    let form = $('#form_buying_product');
    console.log(form);
    form.on('submit', function (e) {
        e.preventDefault();
        console.log('123');
        let nmb = $('#number').val();
        console.log(nmb);
        let submit_btn =$('#submit_btn');
        let product_id = submit_btn.data("product_id");
        let product_name = submit_btn.data("name");
        let product_price= submit_btn.data("price");
        console.log(product_id);
        console.log(product_name);
        console.log(product_price);

        $('.basket-items ul').append('<li>'+product_name+', '+ nmb +'шт. '+'по '+ product_price + 'грн  ' +
            '<a class="delete-item" href="">X</a>'+
            '</li>')
    });
    function shovingBasket(){
         $('.basket-items').removeClass('hidden');
    }

    $('.basket-container').on('click', function (e) {
        e.preventDefault();
        shovingBasket();
    });

    $('.basket-container').mouseover(function () {
       shovingBasket();
    });

    // $('.basket-container').mouseout(function () {
    //     shovingBasket();
    // });
    $(document).on('click', '.delete-item',function (e) {
        e.preventDefault();
        $(this).closest('li').remove();
    });
});



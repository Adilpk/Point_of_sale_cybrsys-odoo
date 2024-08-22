{
    'name': 'Product Brand',
    'version': '17.0.1.0.0',
    'summary': 'Brand Products',
    'author': 'Adil P k',
    'depends': ['point_of_sale'],
    'data': [
        'views/product_product.xml',
        'views/pos_category_discount_limit.xml',
    ],
    'description': 'Add a product Brand names in POS order line',
    'installable': True,
    'application': True,
    'assets': {
       'point_of_sale._assets_pos': [
           'pos_brand/static/src/js/pos.js',
           'pos_brand/static/src/xml/brand_order_line.xml',
       ],
    },

}

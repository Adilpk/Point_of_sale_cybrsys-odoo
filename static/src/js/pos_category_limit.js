   /** @odoo-module */
import { Order } from "@point_of_sale/app/store/models";
import { patch } from "@web/core/utils/patch";

patch(Order.prototype,{
    async pay(){
        var order_line = this.get_orderlines();
        console.log('orderline',order_line)
        var count =0;
        order_line.forEach(element =>{
            var category = element.product.pos_categ_ids;
            console.log('category',category)
            console.log('discount given',element.discount);
            console.log('conf.discount',this.pos.config.discount_limit);
            if (category in this.pos.config.limit_categ_ids){
                console.log("category not included")
                count += 0
            }
            else if(element.discount < this.pos.config.discount_limit)
            {
                console.log("category  inclued")
                count += 1
            }
            else{
                count += 1
                console.log("deiscount check")
                }
            })
            console.log(count)
            if (count == 0){
                super.pay()
            }
            }
})
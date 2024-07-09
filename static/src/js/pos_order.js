   /** @odoo-module */
import { Order } from "@point_of_sale/app/store/models";
import { patch } from "@web/core/utils/patch";

patch(Order.prototype,{
    async pay(){
    var order_line = this.get_orderlines();
    var sum = 0
    order_line.forEach(element =>{
        sum += element.price
    })
    if(sum > 1000){
        console.log("check your limit")
    }
    else{
        super.pay()
    }
    }
})
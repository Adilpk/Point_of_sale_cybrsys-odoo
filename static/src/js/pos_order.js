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
    console.log("line",order_line)
    }
})
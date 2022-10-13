let updateBtns = document.getElementsByClassName("update-cart")

for (let i=0; i<updateBtns.length; i++){
    
    updateBtns[i].addEventListener("click", function(){
        let productId = this.dataset.product;
        let action = this.dataset.action;
        console.log(`Product Id: ${productId}`)
    })
    console.log('User: ', user)
}
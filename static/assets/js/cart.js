let updateBtns = document.getElementsByClassName("update-cart")

for (let i=0; i<updateBtns.length; i++){
    
    updateBtns[i].addEventListener("click", function(){
        let productId = this.dataset.product;
        let action = this.dataset.action;
        if (user === 'AnonymousUser'){
            console.log('User not logged in');
        } else {
            updateUserOrder(productId, action)
        }    
    })
}

function updateUserOrder(productId, action) {

    let url = '/updatecart'

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type':'application/json'
        },
        body:JSON.stringify({'productId': productId, 'action': action})
    })

    .then((response) => response.json())
    .then((data) => {
        console.log('Second THen')
        console.log('data: ', data)
    })
}
let updateBtns = document.getElementsByClassName("update-cart")

for (let i=0; i<updateBtns.length; i++){
    
    updateBtns[i].addEventListener("click", function(){
        let productId = this.dataset.product;
        let action = this.dataset.action;
        let slider = this.dataset.slider;
        if (user === 'AnonymousUser'){
            alert('User not logged in')
        } else {
            updateUserOrder(productId, action, slider)
        }    
    })
}

function updateUserOrder(productId, action, slider) {

    let url = '/updatecart'

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type':'application/json'
        },
        body:JSON.stringify({'productId': productId, "action": action})
    })

    .then((response) => response.json())
    .then((data) => {
        if (slider != "true"){
            alert(data["Message"]);
        }
        location.reload()
    })
}
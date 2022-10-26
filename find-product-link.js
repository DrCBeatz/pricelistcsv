let productItemLinks = document.querySelectorAll('.products-item-link');
let productSKU = "EJ38H"
let searchURL = `https://www.long-mcquade.com/?page=search&SearchTxt=${productSKU}`;

window.open(searchURL);

    for (item of productItemLinks) {
    
        for (childNode of item.childNodes) {
            
            if (childNode.textContent.trim() == `Model: ${productSKU}`) {
                window.open(childNode.parentElement.href);
            }
    
        }
    }

let productHeaderName = document.getElementById('product-header-name').textContent;
console.log("Product title: " + productHeaderName);

let productModel = document.getElementById('product-model').textContent;
console.log("Product SKU: " + productModel);

let productRegularPrice = document.getElementById("product-regular-price").textContent;
console.log("Price :" + productRegularPrice);

let descriptionTab = document.getElementById("Description-tab").innerHTML;
console.log("Description: " + descriptionTab);

let productImage = document.getElementById("product-image").src;
console.log("Image URL: " + productImage);

let thumbnails = document.querySelectorAll('.product-thumbnail.imgs')

document.querySelector('.product-thumbnail-imgs').children[1].href
// const one = document.getElementById('first')
// const two = document.getElementById('second')
// const three = document.getElementById('third')
// const four = document.getElementById('fourth')
// const five = document.getElementById('fifth')
// const form = document.querySelector('.rate-form')
// const confirmBox = document.getElementById('confirm-box')
// const csrf = document.getElementsByName('csrfmiddlewaretoken')
//
// const handleStarSelect = (size) => {
//         const children = form.children
//         console.log(children[0])
//         for (let i = 0; i < children.length; i++) {
//             if (i <= size) {
//                 children[i].classList.add('checked')
//             } else {
//                 children[i].classList.remove('checked')
//             }
//         }
//     }
//      const handleSelect = (selection) => {
//         switch (selection) {
//             case 'first': {
//                 handleStarSelect(1)
//                 return
//             }
//             case 'second': {
//                 handleStarSelect(2)
//                 return
//             }
//             case 'third': {
//                 handleStarSelect(3)
//                 return
//             }
//             case 'fourth': {
//                 handleStarSelect(4)
//                 return
//             }
//             case 'fifth': {
//                 handleStarSelect(5)
//                 return
//             }
//             default: {
//                 handleStarSelect(0)
//             }
//         }
//
//     }
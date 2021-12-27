document.addEventListener('DOMContentLoaded',() => {

            // Making the 'enter' key to submit messages

            let msg = document.querySelector('#user_message');
            msg.addEventListener('keyup', event => {
                event.preventDefault();
                if (event.keyCode === 13){
                    event.querySelector('#send_message').click();
                }
            })
})
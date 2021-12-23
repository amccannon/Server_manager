
// Adding just a simple event listing

document.addEventListener('DOMContentLoaded', () => {

    // crate a variable to be connected to the socket io server.
    var socket = io.connect('http://' + document.domain + ':' + location.port);

    //Event bucket 
    socket.on('message', data =>{
        //displaying the words

        const p = document.createElement('p');
        const br = document.createElement('br');
        p.innerHTML = data;
        document.querySelector('#display-message-section').append(p);
    }); 

    // Creating the custom event:
    socket.on('some-event', data => {
        console.log(data);
    });

    // Adding a standard javascript event listener for the button
    // Send message
    document.querySelector('#send_message').onclick = () => {
        // we want to sent it to the server the txt we receive
        socket.send({'msg':document.querySelector('#user_message').value, 'firstname': firstname});
    }
})
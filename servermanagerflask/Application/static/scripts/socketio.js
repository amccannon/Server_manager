
// Adding just a simple event listing

document.addEventListener('DOMContentLoaded', () => {

    // crate a variable to be connected to the socket io server.
    var socket = io.connect('http://' + document.domain + ':' + location.port);


    let room;


    //Message event, prints the message to the console/Displaying messages
    socket.on('message', data => {

        const p = document.createElement('p');
        const span_firstname = document.createElement('span');
        const span_timestamp = document.createElement('span');
        // line breaks (custom)
        const br = document.createElement('br');
        // access to the firstname
        span_firstname.innerHTML = data.firstname;
        span_timestamp.innerHTML = data.timestamp;
        // to access the message text
        p.innerHTML = span_firstname.outerHTML+ data.msg + br.outerHTML + span_timestamp.outerHTML;
        document.querySelector('#display-message-section').append(p);
        
        //console.log(`Message received: ${data}`);
    });

    // Send messages
    //we are listening for on click
    document.querySelector('#send_message').onclick = () => {
        socket.send({'msg': document.querySelector('#user_message').value, 'firstname': firstname, 'room': room });
        
    }

    document.querySelector('select-room').forEach(p => {
        p.onclick = () => {
            let newRoom = p.innerHTML;
            // Checking if the user is already in the room
            if (newRoom == room) {
                msg = `You are already in ${room} room.`;
                printSysMsg(msg);
            }else {
                leaveRoom(room);
                joinRoom(newRoom);
                //Update the new room
                room = newRoom;
            }
        }
    });

    //Leaving the room
    function leaveRoom(room){
        // We want it to go to a custom event
        socket.emit('leave', {'firstname': firstname, 'room': room});
    }

    //Joining the room
    function joinRoom(room) {
        socket.emit('join', {'firstname': firstname, 'room': room});
        // Clear messages
        document.querySelector('#display-message-section').innerHTML = ' '
    }

    // Print system message

    function printSysMsg(msg){
        const p = document.createElement('p');
        p.innerHTML = msg;
        document.querySelector('#display-message-section').append(p);
    }

})
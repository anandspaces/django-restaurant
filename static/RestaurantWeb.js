// Function to handle form submission on the "Reserve a Table" page
document.addEventListener('DOMContentLoaded', function() {
    const submitButton = document.getElementById('submit_button');
    if (submitButton) {
        submitButton.addEventListener('click', function(event) {
            event.preventDefault();
            reserveTable();
            sendEmail();
        });
    }
});

function reserveTable() {
    const dateOfArrival = document.getElementById('dateOfArrival').value;
    const timeOfArrival = document.getElementById('timeOfArrival').value;
    const noOfDiners = document.getElementById('noOfDiners').value;
    const firstName = document.getElementById('firstName').value;
    const lastName = document.getElementById('lastName').value;
    const emailID = document.getElementById('emailID').value;
    const phoneNo = document.getElementById('phoneNo').value;

    // Store the form data in the session storage
    sessionStorage.setItem('dateOfArrival', dateOfArrival);
    sessionStorage.setItem('timeOfArrival', timeOfArrival);
    sessionStorage.setItem('noOfDiners', noOfDiners);
    sessionStorage.setItem('firstName', firstName);
    sessionStorage.setItem('lastName', lastName);
    sessionStorage.setItem('emailID', emailID);
    sessionStorage.setItem('phoneNo', phoneNo);

    // Confitions
    if(dateOfArrival.trim()==="" || timeOfArrival.trim()==="" || noOfDiners.trim()==="" || firstName.trim()=="" || lastName.trim()==="" || emailID.trim()==="" || phoneNo.trim()===""){
        // Fill Details Alert
        window.alert("Fill the Details properly!");
    } else {
        // Out for Delivery Alert
        window.alert("Out for Deivery!");

        // Redirect to Reservation Information page
        window.location.href = "information";
    }
}

// async function sendEmail() {
//     const email = document.getElementById('emailID').value;
//     const message = document.getElementById('phoneNo').value;

//     try {
//         const response = await fetch('/send-email', {
//             method: 'POST',
//             headers: {
//                 'Content-Type': 'application/json',
//             },
//             body: JSON.stringify({ email, message }),
//         });

//         if (response.ok) {
//             alert('Email sent successfully!');
//         } else {
//             alert('Failed to send email.');
//         }
//     } catch (error) {
//         console.error('Error:', error);
//     }
// }


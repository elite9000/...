<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $name = $_POST['name'];
    $email = $_POST['email'];
    $phone = $_POST['phone'];
    $cabin = $_POST['cabin'];
    $checkin = $_POST['checkin'];
    $checkout = $_POST['checkout'];
    
    // Aquí procesarías los datos (por ejemplo, guardarlos en una base de datos)
    // y enviarías una confirmación por email
}
?>

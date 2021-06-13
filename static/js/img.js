document.querySelector('#id_image').addEventListener('change', upload);


function upload() {
    var file = document.getElementById("id_image").files[0];
    if (file) {
        var reader = new FileReader();
        reader.readAsDataURL(file);
        reader.onloadend = function() {
            $('#userProfileImage').css('background-image', 'url("' + reader.result + '")');
            console.log('url("' + reader.result + '")')
        }
    }
};
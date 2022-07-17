function toggleHeading(currentLoginHeading){
    let loginpopupheading = document.getElementById('loginpopupheader');
    if(currentLoginHeading == 'login'){
        loginpopupheading.innerHTML = 'Login';
    }else if(currentLoginHeading == 'register'){
        loginpopupheading.innerHTML = 'Register';
    }
}
function updateModel(visitorId){
    visitorId=visitorId.getAttribute('data-visitorId');
    document.getElementById('visitorId').value = visitorId;
}
function checkUserType(userType){
    let membershipdiv = document.getElementById('membershipdiv');
    let customeramtdiv = document.getElementById('customeramtdiv');
    let trainigpaydiv = document.getElementById('trainigpaydiv');
    let remainigtimediv = document.getElementById('remainigtimediv');
    let paymentdatediv = document.getElementById('paymentdatediv');
    let curUpdateFormData = document.getElementById('curUpdateFormData');
    let trainerDiv = document.getElementById('trainerDiv');
    if(userType == 'Trainer'){
        membershipdiv.style.display="none";
        customeramtdiv.style.display="none";
        remainigtimediv.style.display="none";
        trainerDiv.style.display="none";
        trainigpaydiv.style.display="block";
        paymentdatediv.style.display="block";
        curUpdateFormData.value="trainerData";

    }else if (userType == 'Customer') {
        trainigpaydiv.style.display="none";
        paymentdatediv.style.display="none";
        membershipdiv.style.display="block";
        customeramtdiv.style.display="block";
        trainerDiv.style.display="block";
        remainigtimediv.style.display="block";
        curUpdateFormData.value="customerData";
    }else if (userType == 'customerData') {
        trainigpaydiv.style.display="none";
        paymentdatediv.style.display="none";
        membershipdiv.style.display="block";
        customeramtdiv.style.display="block";
        remainigtimediv.style.display="block";
        trainerDiv.style.display="block";
        curUpdateFormData.value="customerData";
    }else if(userType == 'trainerData'){
        membershipdiv.style.display="none";
        customeramtdiv.style.display="none";
        remainigtimediv.style.display="none";
        trainerDiv.style.display="none";
        trainigpaydiv.style.display="block";
        paymentdatediv.style.display="block";
        curUpdateFormData.value="trainerData";

    }
}
var modalDiv = $("#modal-div")
$(".open-model").on("click", function(){
    $.ajax({
        type:'GET',
        url: $(this).attr("data-url"),
        success: function(data){
            modalDiv.html(data);
            $("#updateClassesModal").modal();
        }
    });
    
});

$('#modal-div').on('show.bs.modal',function(e){
    var userType = document.getElementById('curUpdateFormData').value;
    checkUserType(userType);
})

var modalTrainerDiv = $("#modal-trainerdiv")
$(".open-model-trainee-session").on("click", function(){
    $.ajax({
        type:'GET',
        url: $(this).attr("data-trainerurl"),
        success: function(data){
            modalTrainerDiv.html(data);
            $("#updateClassesModalTrainer").modal();
        }
    });
    
});

$('#modal-div').on('show.bs.modal',function(e){
    var userType = document.getElementById('curUpdateFormData').value;
    checkUserType(userType);
})

// background set function
$('.set-bg').each(function () {
    var bg = $(this).data('setbg');
    $(this).css('background-image', 'url(' + bg + ')');
});

function calculateBMI(){
    var weight = document.getElementById('bmiWeight').value;
    var height = document.getElementById('bmiHeight').value;
    height = height/100
    var BMI = 0;
    BMI = weight/(height * height);
    document.getElementById('bmiCalculated').value=BMI;

}
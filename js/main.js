//Device ID: 51ff6f065082554910260887
//Access Code: 2228662ce1e5a04e7fb21f9b81aa3bc390b72506

$(document).ready(function () {
    var x = $('#onOff').prop('checked')
    var jsonString;
    $.get("http://192.168.0.102:8181/?params=-1,0", function (data) { //Device 0 turns off, 0 times an hour.
        jsonString = data;
        console.log(jsonString);
    });

    setTimeout(function () {
        var freshener1 = jsonString[0];
        var freshener2 = jsonString[1];
        console.log(freshener1, freshener2);

    }, 1000);
    hide();
});

function hide(f1, f2) {
    if (f1 == 0 && f2 == 0) {
        $(".card").fadeOut();
        $('#onOff').prop('checked', false);
    }
    $("#onOff").change(function () { //When the switch is activated
        var x = $('#onOff').prop('checked')
        if (x == false) {
            $(".empty").animate({ opacity: 1 })
            $(".empty").fadeIn();
            $(".card").fadeOut();
            $.get("http://192.168.0.102:8181/?params=0,0", function (data) { //Device 0 turns off, 0 times an hour.
                console.log(data);
            });
            $.get("http://192.168.0.102:8181/?params=0,1", function (data) { //Device 1 turns off, 0 times an hour.
                console.log(data);
            });
            
        } else {
            $(".empty").animate({ opacity: 0 })
            $(".card").fadeIn();
            $.get("http://192.168.0.102:8181/?params=20,0", function (data) { //Device 0 turns on, 3 times an hour. (every 20mins)
                console.log(data);
            });
            $.get("http://192.168.0.102:8181/?params=20,1", function (data) { //Device 1 turns on, 3 times an hour.
                console.log(data);
            });
            
        }

    });
}

function printValue() {
    var x = $('#onOff').prop('checked')
    console.log(x);
}

function freshener1Submit() {
    var onOff = $('#onOff1').prop('checked');
    var frequency = 0;
    var device = 0;

    frequency = 60 / ($('#f1DDValues').val());
    if (onOff == false) {
        frequency = 0;
        device = 0;
        var url = "http://192.168.0.102:8181/?params=" + frequency + "," + device;
        console.log(url);
        $.get(url, function (data) {
            console.log(data);
        });
    }
    if (onOff1 && frequency != Infinity) {

        console.log(device, frequency);

        var url = "http://192.168.0.102:8181/?params=" + frequency + "," + device;
        $("#freq1").text(frequency);
        $("#status1").text("On");
        console.log(url);

        $.get(url, function (data) {
            console.log(data);
        });
    }
}

function freshener2Submit() {
    var onOff = $('#onOff2').prop('checked');
    var frequency = 0;
    var device = 1;

    frequency = 60 / ($('#f2DDValues').val());
    if (onOff == false) {
        frequency = 0;
        device = 1;
        var url = "http://192.168.0.102:8181/?params=" + frequency + "," + device;
        console.log(url);
        $.get(url, function (data) {
            console.log(data);
        });
    }
    if (onOff && frequency != Infinity) {
        console.log(device, frequency);
        var url = "http://192.168.0.102:8181/?params=" + frequency + "," + device;
        $("#freq2").text(frequency);
        $("#status2").text("On");
        console.log(url);
        $.get(url, function (data) {
            console.log(data);
        });
    }


}

function send() {
    $.get("http://192.168.0.102:8181/?params=5,11", function (data) {
        console.log(data);
        Materialize.toast('Sent', 4000);
    });
}
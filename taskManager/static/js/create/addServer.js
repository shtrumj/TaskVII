function myfunc(){
    let mycustomer = document.getElementById("mycustomer");
    let myselect= mycustomer.value;
    // console.log("i have choose customer nuimber " + myselect)
    hyperfetch()

}




async function hyperfetch(){
        const response = await fetch(
        'http://' + window.location.host + '/hypers',
        {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json'
            },
            mode: 'cors',
            cache : 'default'}
    );
        const Myhypers = await response.json();
        console.log(Myhypers.data)
}
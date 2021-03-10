
document.addEventListener("DOMContentLoaded", function(event) {

    const openMenuBtn = document.querySelector('.site-header__menu-icon__middle');
    const closeMenuBtn = document.querySelector('.close-nav');

    console.log(window.screen.availWidth)

    // if(window.screen.availWidth < 798){
    //     document.getElementById('menu_mobile').style.width = '0';
    // }

    openMenuBtn.addEventListener('click', show_mobile_menu);
    closeMenuBtn.addEventListener('click', close_mobile_menu);

    function show_mobile_menu(){
        document.getElementById('menu_mobile').classList.add('menu_mobile_expansion_width');
        document.getElementById('main_content').style.marginLeft = '250px';

    
    }

    function close_mobile_menu(){
        document.getElementById('menu_mobile').classList.remove('menu_mobile_expansion_width');
        document.getElementById('main_content').style.marginLeft = '0';
    }

    // Footer Year Date
    const year = new Date();
    document.querySelector('.year').innerHTML = year.getFullYear();

})



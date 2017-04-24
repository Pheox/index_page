
kieName="page_scroll"
expdays=365


window.onload = init;
window.onunload = finish;

function init() {
    // console.log("WTF");
    // loadScroll();
}


function finish() {

    saveScroll();
}


/* Handlers */
function openTab(url) {
    var win = window.open(url, '_blank');
    win.focus();
}


/***** JQUERY *****/

/* Highlight selected tab. */
$(function(){

    var $page = window.location.pathname;
    $('#menu ul li a').each(function(){
        var $href = $(this).attr('href');
        if ( ($href == $page) || ($href == '') ||
             ($page == '/' && $href == '/')) {
            $(this).addClass('on');
        } else {
            $(this).removeClass('on');
        }
    });
});


function saveScroll(){
    console.log("saveScroll");
    var expdate = new Date();
    expdate.setTime (expdate.getTime() + (expdays*24*60*60*1000));

    var x = (document.pageXOffset?document.pageXOffset:document.body.scrollLeft);
    var y = (document.pageYOffset?document.pageYOffset:document.body.scrollTop);
    Data=x + "_" + y;
    setCookie(cookieName,Data,expdate);
}


function loadScroll(){
    console.log("loadScroll");
    inf = getCookie(cookieName)
    if(!inf){
        console.log("??");
        return;
    }
    var ar = inf.split("_");
    console.log(ar);
    if(ar.length == 2){
        window.scrollTo(parseInt(ar[0]), parseInt(ar[1]));
    }
}

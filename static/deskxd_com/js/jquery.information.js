window.onload=function(){
    var cmenu = document.getElementById("c-menu");
    var ctxt = document.getElementById("c-txt");
    var ctitle = cmenu.getElementsByTagName("div");
    var ctext = ctxt.getElementsByTagName("div");
    for (var i=0;i<ctitle.length;i++)
    {
        ctitle[i].index=i;
        ctitle[i].onclick=function(){
            for (var i=0; i<ctitle.length; i++)
            {
                ctitle[i].id="";
                $(ctext[i]).slideUp("fast");
            }
            this.id="company-active"
            $(ctext[this.index]).slideDown("slow");
        }
    }
}
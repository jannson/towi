/*图片随数字轮换，页面加载时，图片就随数字一起换，显示的图片的数字变橙色，当鼠标经过数字时，就显示此数字对应的图片，离开时又恢复原来的动作，悬停在图片和数字上时，图片就停止轮换，离开时又恢复。*/
 var index=null;
 var i=0;
 var t=null;
   $(function(){
       index=$(".img li").length-1;
      cycshow();
  $(".tip li").mouseover(function(){
     i=$(".tip li").index(this);
      show();
     });
	
	$("#banner li").hover(function(){
	  clearTimeout(t);
	},function(){
	   cycshow();
	
	});
	
	//导航菜单
	$("#nav ul li").mouseover(function(){
	  $(this).children("ul").show();								   
  }).mouseout(function(){
	   	  $(this).children("ul").hide();								   

	  });
     $("#seaText").focus(function(){
		 $(this).val("");	
		 
	  }).blur(function(){
		 
		  if($(this).val()==""){
		    $(this).val("贴子搜索");	  
		 }  
	  });
	 
   });
   //显示某单个索引的图片
  function show(){
        $(".img li").eq(i).show().siblings().hide();
	$(".tip li").eq(i).addClass("rtip").siblings().removeClass("rtip");
	
	
  }
  //循环显示所有索引图片
  function cycshow(){
  show();
	i++;
	if(i>index){
	   i=0;
	}  
    
    t=setTimeout("cycshow()",4000);
  }
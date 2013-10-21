 var INDEX=null;
 var I=0;
 var T=null;
   $(function(){
       INDEX=$(".img li").length-1;
      cycshow();
  $(".tip li").mouseover(function(){
     I=$(".tip li").index(this);
      show();
     });
	
	$("#banner li").hover(function(){
	  clearTimeout(T);
	},function(){
	   cycshow();
	
	});
	
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
  function show(){
    $(".img li").eq(I).show().siblings().hide();
	$(".tip li").eq(I).addClass("rtip").siblings().removeClass("rtip");
  }
  function cycshow(){
    show();
	I++;
	if(I>INDEX){
	   I=0;
	}  
    
    T=setTimeout("cycshow()",4000);
  }

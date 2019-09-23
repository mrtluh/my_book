/**
 * Created by Administrator on 2017/5/11.
 */
//顶部导航
var navarr=['20px','130px','240px','350px','460px']
$('.headr-nav li').mouseover(function(){
    $('.headr-nav li a').eq($(this).index('li')).css('color','#4AB344')
    $('.spbottom:eq(0)').css('left',navarr[$(this).index()])
}).mouseout(function(){
    $('.headr-nav li a').eq($(this).index('li')).css('color','')
    $('.spbottom:eq(0)').css('left','20px')
})

$('.headr-right:eq(0)').mouseover(function(){
    $(this).css('overflow','visible')
}).mouseout(function(){
    $(this).css('overflow','hidden')
})
//顶部导航结束
//果园推荐开始
$('.rcr-top').mousemove(function(){
    $('.rcr-top').eq($(this).index('.rcr-top')).css('margin-left','0')

}).mouseout(function(){
    $('.rcr-top').eq($(this).index('.rcr-top')).css('margin-left','10px')

})
//果园推荐结束
//每日新品特卖轮播
var banner=document.getElementsByClassName('banner_1')[0]
var site=['0px','-1424px']
var bon = document.getElementsByClassName('banner-bottom')[0]
var ali = bon.getElementsByTagName('li')
var len = site.length
var num  = 0
for(i=0;i<len;i++){
    bon.innerHTML += '<li>'+(i+1)+'</li>'
}
ali[0].className = 'active'
for(i=0;i<len;i++){
    ali[i].index = i
    ali[i].onmouseover = function () {
        num = this.index
        picshow()
    }
}
function picshow(){
    for(j=0;j<len;j++){
        ali[j].className = ''
    }
    ali[num].className ='active'
    banner.style.marginLeft = site[num]
}
var time = null
function pp() {
    time = setInterval(function () {
        num++
        if (num >= len) {

            num=0
        }
        picshow()
    }, 5000)
}
pp()
banner.onmouseover = function () {
    clearInterval(time)
}
banner.onmouseout = function () {
    clearInterval(time)
    pp()
}
//每日新品特卖轮播结束
$('.nw-b').mousemove(function(){
    $('.nw-b img').eq($(this).index('.nw-b')).css('margin-left','-8px')

}).mouseout(function(){
    $('.nw-b img').eq($(this).index('.nw-b')).css('margin-left','0px')

})

$(".txtMarquee-top").slide({mainCell:".bd ul",autoPlay:true,effect:"topMarquee",vis:5,interTime:50,trigger:"click"});
$(".slideBox").slide({mainCell:".bd ul",autoPlay:true,trigger:"click"});
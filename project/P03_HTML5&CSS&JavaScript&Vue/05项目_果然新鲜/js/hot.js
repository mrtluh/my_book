/**
 * Created by Administrator on 2017/5/13.
 */
//顶部导航
var navarr=['20px','130px','240px','350px','460px']
$('.headr-nav li').mouseover(function(){
    $('.headr-nav li a').eq($(this).index('li')).css('color','#4AB344')
    $('.spbottom:eq(0)').css('left',navarr[$(this).index("")])
}).mouseout(function(){
    $('.headr-nav li a').eq($(this).index('li')).css('color','')
    $('.spbottom:eq(0)').css('left','130px')
})

$('.headr-right:eq(0)').mouseover(function(){
    $(this).css('overflow','visible')
}).mouseout(function(){
    $(this).css('overflow','hidden')
})
//顶部导航结束
//切换菜单
$('.hd li').click(function(){
    $('.bd1').css('display','none')
    $('.hd li a').removeClass('active')
    $('.bd1 ').eq($(this).index()).css('display','block')
    $('.hd li a').eq($(this).index()).addClass('active')

})
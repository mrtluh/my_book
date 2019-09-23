// JavaScript Document

//格式化后制定格式的日期和时间 ----封装一个函数

// 获取制定格式的时间
		function getDate(){
			var dt=new Date();// 创建时间的对象
			//获取年
			var year = dt.getFullYear();		
			//获取月
			var month = dt.getMonth() + 1;	
			//获取日
			var day = dt.getDate();
			//获取小时
			var hour =dt.getHours();
			//获取分钟
			var minutes = dt.getMinutes();
			//获取秒
			var seconds = dt.getSeconds();
			//获取星期
			var week = dt.getDay();
			
			// 时间格式化
			month=month<10?"0"+month:month;
			day=day<10?"0"+day:day;
			hour=hour<10?"0"+hour:hour;
			minutes=minutes<10?"0"+minutes:minutes;
			seconds=seconds<10?"0"+seconds:seconds;
			// 星期格式化
			var dict={
				0:"日",
				1:"一",
				2:"二",
				3:"三",
				4:"四",
				5:"五",
				6:"六",
			};
			week=parseInt(week);
			var week1;
			for (var key in dict){
				week1 = dict[week];
			}
			return year+"年"+month+"月"+day+"日  "+hour+":"+minutes+":"+seconds+"   星期"+week1;
		}
		
	
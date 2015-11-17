$(function(){
    var timeStamps = [];
    var requestCounts = [];
    for (var i=0; i<result.length; i++){
        timeStamps.push(result[i][0]);
        requestCounts.push(result[i][1])
    };
    var data = [
                {
                    name : 'PV',
                    value:requestCounts,
                    color:'#0d8ecf',
                    line_width:2
                }
             ];
     
    var labels = timeStamps;
    
    var line = new iChart.LineBasic2D({
        render : 'canvasDiv',
        data: data,
        align:'center',
        title : 'ichartjs官方网站最近5天PV流量趋势',
        subtitle : '平均18:00-22:00访问量达到最大值(单位：万)',
        footnote : '数据来源：模拟数据',
        width : 1800,
        height : 400,
        sub_option:{
            smooth : true,//平滑曲线
            point_size:10
        },
        tip:{
            enable:true,
            shadow:true
        },
        legend : {
            enable : false
        },
        crosshair:{
            enable:true,
            line_color:'#62bce9'
        },
        coordinate:{
            width:1600,
            valid_width:1500,
            height:260,
            axis:{
                color:'#9f9f9f',
                width:[0,0,2,2]
            },
            grids:{
                vertical:{
                    way:'share_alike',
                    value:12
                }
            },
            scale:[{
                 position:'left',   
                 start_scale:0,
                 end_scale:100,
                 scale_space:10,
                 scale_size:2,
                 scale_color:'#9f9f9f'
            },{
                 position:'bottom', 
                 labels:labels
            }]
        }
    });
//开始画图
line.draw();
});
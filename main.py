from pyecharts import options as opts
from pyecharts.charts import Map
from pyecharts.faker import Faker
import os
# 基础数据
quxian = ['尧都区', '曲沃县', '翼城县', '襄汾县', '洪洞县', '古县', '安泽县', '浮山县', '吉县', '乡宁县',
          '大宁县', '隰县', '永和县', '蒲县', '汾西县', '侯马市', '霍州市']
values3 = [944050, 237033, 311471, 442614, 733420, 91798, 82012, 127831, 106407, 233167, 64501, 103617,63649,107339,144791,240005,282905]

c = (
    Map()
        .add("临汾", [list(z) for z in zip(quxian, values3)], "临汾")
        .set_global_opts(
        title_opts=opts.TitleOpts(title="临汾地图"), visualmap_opts=opts.VisualMapOpts(min_=50000,max_=1000000,is_piecewise=True)
    )
        .render()
)
# 打开html
os.system("render.html")

#写在最后分析人口变化原因：
#①首先就是山西经济发展相对落后，就业岗位比较少导致部分年轻人离开家乡
#②近一年人口流失只要原因是山西师范大学从临汾搬往太原，学生人口减少，学校周边的店铺也相应的变少，人口也逐渐流失。
#③从图中也可以看出临汾市人口主要集中在尧都区跟洪洞县，其他地区的人口相对较少，也都逐渐的流向了附近的省市例如太原市、西安市等等。

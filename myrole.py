import tkinter as tk
from tkinter import messagebox
import random

# 定义各个类的选项
locations = [
    "日本东海岸", "巴黎郊区", "埃及沙漠", "纽约市中心", "喜马拉雅山脉",
    "伦敦塔桥", "罗马斗兽场", "悉尼歌剧院", "墨西哥城", "巴西雨林",
    "洛杉矶", "开罗", "上海", "旧金山", "阿姆斯特丹",
    "首尔", "东京", "北京", "新德里", "莫斯科",
    "伊斯坦布尔", "华盛顿", "大连", "香港", "台北",
    "悉尼", "新加坡", "吉隆坡", "曼谷", "雅加达",
    "马德里", "巴塞罗那", "布宜诺斯艾利斯", "里约热内卢", "圣保罗",
    "赫尔辛基", "布拉格", "布加勒斯特", "萨格勒布", "维也纳"
]

family_occupations = [
    "医生家庭",
    "商人家庭",
    "农民家庭",
    "艺术家家庭",
    "科学家家庭",
    "教师家庭",
    "工程师家庭",
    "军人家庭",
    "音乐家家庭",
    "作家家庭",
    "厨师家庭",
    "演员家庭",
    "律师家庭",
    "建筑师家庭",
    "运动员家庭",
    "航天工程师家庭",
    "街头艺人家庭",
    "流浪者家庭",
    "同性恋家庭",
    "总统家庭",
    "富商家庭",
    "外交官家庭",
    "环保主义者家庭",
    "赛车手家庭",
    "探险家家庭",
    "魔术师家庭",
    "渔夫家庭",
    "渔民家庭",
    "园艺师家庭",
    "陶艺家家庭",
    "摄影师家庭",
    "木匠家庭",
    "消防员家庭",
    "警察家庭",
    "神职人员家庭",
    "珠宝设计师家庭",
    "珠宝商家庭",
    "古董商家庭",
    "矿工家庭",
    "船长家庭",
    "飞行员家庭",
    "潜水员家庭",
    "记者家庭",
    "时尚设计师家庭",
    "游戏开发者家庭",
    "电脑程序员家庭",
    "人工智能研究员家庭",
    "宇航员家庭",
    "遗传学家家庭",
    "海洋生物学家家庭",
    "历史学家家庭",
    "考古学家家庭",
    "非政府组织工作者家庭",
    "慈善家家庭",
    "社会活动家家庭",
    "瑜伽教练家庭",
    "营养师家庭",
    "健身教练家庭",
    "舞蹈家家庭",
    "戏剧导演家庭",
    "电影制片人家庭",
    "动画师家庭",
    "漫画家家庭",
    "插画师家庭",
    "配音演员家庭",
    "配音导演家庭",
    "电台主持人家庭",
    "电视节目主持人家庭",
    "新闻主播家庭",
    "电台DJ家庭",
    "播客制作人家庭",
    "街头杂技演员家庭",
    "街头小丑家庭",
    "街头音乐家家庭",
    "街头舞者家庭"
]

complexions = [
    "黑皮肤", "白皮肤", "黄皮肤", "褐皮肤", "浅棕色皮肤",
    "深褐色皮肤", "红色皮肤", "橄榄色皮肤", "乳白色皮肤", "金色皮肤",
    "浅黄色皮肤", "中等肤色", "古铜色皮肤", "肉色皮肤", "灰色皮肤",
    "粉色皮肤", "青色皮肤", "象牙色皮肤", "棕褐色皮肤", "暗棕色皮肤",
    "酒红色皮肤", "橙色皮肤", "暗红色皮肤", "青灰色皮肤", "黄褐色皮肤",
    "紫色皮肤", "黑褐色皮肤", "深黄色皮肤", "浅绿色皮肤", "淡黄色皮肤",
    "暗紫色皮肤", "中棕色皮肤", "淡紫色皮肤", "浅蓝色皮肤", "深蓝色皮肤",
    "雪白色皮肤", "青色肤色", "灰白色皮肤", "淡棕色皮肤", "象牙黄皮肤",
    "深象牙色皮肤", "青棕色皮肤", "鲜红色皮肤", "玫瑰色皮肤", "珊瑚色皮肤"
]

son_daughter = [
    "儿子", "女儿",
    "长子", "长女", "次子", "次女", "小儿子"
]

hobbies = [
    "弹钢琴", "画画", "编码", "探险",
    "登山", "游泳", "阅读", "烹饪", "钓鱼",
    "跑步", "摄影", "旅行", "写作", "跑酷",
    "音乐创作", "舞蹈", "陶艺", "做手工", "编程",
    "设计", "演讲", "学习新语言", "园艺", "玩游戏",
    "集邮", "下棋", "雕刻", "练习魔术", "跑马拉松",
    "做实验", "玩乐器", "制作视频", "玩桌游", "做瑜伽",
    "学习武术", "写诗", "剪纸", "修理", "打篮球",
    "打羽毛球", "看电影", "探索古迹", "创作音乐", "进行科学研究"
]

limitations = [
    "在战斗中不能使用武器", 
    "必须和宠物狗一起行动",
    "不能离开家乡",
    "只能在白天行动",
    "不能使用电子设备",
    "不能接触任何类型的水",
    "只能用纸笔记录",
    "只能在室外活动",
    "不能使用现代交通工具",
    "不能使用任何形式的广告",
    "必须穿着印有盗版米奇衣服",
    "不能与陌生人交谈",
    "只能通过手势而非言语沟通",
    "不能接受任何形式的帮助",
    "不能食用含有糖的食物",
    "必须保持静默",
    "不能直接接触地面",
    "只能在指定区域内移动",
    "不能阅读或书写",
    "不能携带任何金钱",
    "不能进行任何形式的身体接触",
    "不能使用火源",
    "必须始终佩戴眼罩",
    "不能进入建筑物内部",
    "必须时刻保持微笑",
    "不能使用手部",
    "不能改变自己的发型",
    "不能使用钥匙开门",
    "必须穿拖鞋行走",
    "不能使用镜子或其他反射物",
    "不能在雨天外出",
    "必须使用单脚跳动前进",
    "不能吃热食",
    "不能观看电视或电影",
    "不能使用电话进行通信",
    "不能剪指甲",
    "不能在没有监督的情况下行动",
    "不能参与任何形式的比赛",
    "不能唱歌或吹口哨"
]

# 添加新的目标任务
targets = [
    "在众目睽睽下用水自杀",
    "阻止对手自杀",
    "和对手在山上合照",
    "把对方推下山",
    "继承对手的家庭职业",
    "在巴黎铁塔上跳伞",
    "让对手成为网红",
    "成为网红",
    "与对手一起参加马拉松",
    "成为市长",
    "让对手赢得一场辩论赛",
    "让对手在公共场合演讲",
    "不让对手任何在公共场合（镜头前）发表看法或演说 3 次。对方做到则对方直接获胜",
    "让对手学会一项古老的技能",
    "独自完成一场马拉松",
    "不使用任何电子设备到达北京",
    "不使用任何电子设备到达洛杉矶",
    "不使用任何电子设备到达新加坡",
    "不使用任何电子设备到达伦敦",
    "让对手拥抱陌生人",
    "与对手吃饭并主动买单",
    "与对手吃饭并让对方主动买单",
    "帮助对手完成任务，你将率先获得胜利",
    "让家里破产",
    "帮助对手财富自由",
    "用火杀对手",
    "参加一次中国高考",
    "编写任意脚本,使github有1k star",
    "活到第15回合",
    "让对方活到第15回合,你直接获得胜利",
]

def generate_character(name):
    location = random.choice(locations)
    family_occupation = random.choice(family_occupations)
    complexion = random.choice(complexions)
    gender = random.choice(son_daughter)
    hobby = random.choice(hobbies)
    limitation = random.choice(limitations)
    target = random.choice(targets)

    # 生成描述文本，并为不同部分添加不同的标签
    character_description = (f"{name}，是来自 {location} 的 {family_occupation} 的 {complexion}{gender}，"
                             f"{name} 对 {hobby} 十分擅长，但 {limitation}。\n他的目标是 \n\t┌{target}┐\n")

    return character_description, location, family_occupation, complexion, gender, hobby, limitation, target

def on_submit(text_widget, name_entry):
    name = name_entry.get().strip()
    if name:
        character, location, family_occupation, complexion, gender, hobby, limitation, target = generate_character(name)
        text_widget.delete(1.0, tk.END)
        text_widget.insert(tk.END, f"{name}，是来自 ")
        text_widget.insert(tk.END, location, "colored_text")
        text_widget.insert(tk.END, " 的 ")
        text_widget.insert(tk.END, family_occupation, "colored_text")
        text_widget.insert(tk.END, " 的 ")
        text_widget.insert(tk.END, complexion, "colored_text")
        text_widget.insert(tk.END, gender)
        text_widget.insert(tk.END, f".{name} 对 ")
        text_widget.insert(tk.END, hobby, "colored_text")
        text_widget.insert(tk.END, " 十分擅长，但 ")
        text_widget.insert(tk.END, limitation, "colored_text")
        text_widget.insert(tk.END, "。")
        text_widget.insert(tk.END, " 目标是 \n\t┌")
        text_widget.insert(tk.END, target, "colored_text_2")
        text_widget.insert(tk.END, "┐\n\t")
    else:
        messagebox.showwarning("输入错误", "请输入角色姓名！")
        # 应用标签颜色配置
    text_widget.tag_configure("colored_text", foreground="#A52A2A")  # 红褐色
    text_widget.tag_configure("colored_text_2", foreground="#FFA500")  # 橙色

def toggle_visibility(text_widget, mask_button):
    # 定义 'hidden' 标签，如果它还没有被定义的话
    if not text_widget.tag_names() or "hidden" not in text_widget.tag_names():
        text_widget.tag_configure("hidden", foreground="white")

    # 查找目标部分的文本
    target_start = "┌"
    target_end = "┐"

    # 查找目标部分的开始位置
    start_index = text_widget.search(target_start, "1.0", stopindex=tk.END)
    if not start_index:
        print("未能找到目标部分")
        return

    # 计算目标部分的结束位置
    end_index = text_widget.search(target_end, start_index, stopindex=tk.END)
    if not end_index:
        print("未能找到目标部分的结束标记")
        return

    # 确定目标部分的结束位置
    end_index = text_widget.index(f"{end_index} + {len(target_end)} chars")

    # 检查目标部分是否已经被隐藏
    tags = text_widget.tag_names(start_index)
    if "hidden" in tags:
        # 如果目标部分被隐藏，则显示它
        text_widget.tag_remove("hidden", start_index, end_index)
        mask_button.config(text="隐藏目标")
    else:
        # 如果目标部分未被隐藏，则隐藏它
        text_widget.tag_add("hidden", start_index, end_index)
        mask_button.config(text="显示目标")

def lock_buttons(lock_button, submit_button, mask_button):
    if submit_button["state"] == tk.NORMAL:
        submit_button["state"] = tk.DISABLED
        lock_button.config(text="解锁")
    else:
        submit_button["state"] = tk.NORMAL
        lock_button.config(text="锁定")
    if mask_button["state"] == tk.NORMAL:
        mask_button["state"] = tk.DISABLED
        lock_button.config(text="解锁")
    else:
        mask_button["state"] = tk.NORMAL
        lock_button.config(text="锁定")

# 创建主窗口
root = tk.Tk()
root.title("游戏角色生成器")

# 设置窗口大小和位置
window_width = 800
window_height = 800
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
position_right = int(screen_width / 2 - window_width / 2)
position_down = int(screen_height / 2 - window_height / 2)
root.geometry(f"{window_width}x{window_height}+{position_right}+{position_down}")

# 创建两个角色的Frame
frame1 = tk.Frame(root)
frame1.pack(side=tk.LEFT, padx=10, pady=20)
frame2 = tk.Frame(root)
frame2.pack(side=tk.RIGHT, padx=10, pady=20)

# 创建角色1的输入框和按钮
name_label1 = tk.Label(frame1, text="请输入角色1的姓名:")
name_label1.pack(pady=10)
name_entry1 = tk.Entry(frame1, width=30)
name_entry1.pack(pady=5)
submit_button1 = tk.Button(frame1, text="生成角色", command=lambda: on_submit(text_widget1, name_entry1))
submit_button1.pack(pady=10)
text_widget1 = tk.Text(frame1, wrap=tk.WORD, height=40, width=45)
text_widget1.pack(pady=10)
mask_button1 = tk.Button(frame1, text="隐藏目标", command=lambda: toggle_visibility(text_widget1, mask_button1))
mask_button1.pack(side=tk.LEFT, padx=5)
lock_button1 = tk.Button(frame1, text="锁定", command=lambda: lock_buttons(lock_button1, submit_button1, mask_button1))
lock_button1.pack(side=tk.RIGHT, padx=5)

# 创建角色2的输入框和按钮
name_label2 = tk.Label(frame2, text="请输入角色2的姓名:")
name_label2.pack(pady=10)
name_entry2 = tk.Entry(frame2, width=30)
name_entry2.pack(pady=5)
submit_button2 = tk.Button(frame2, text="生成角色", command=lambda: on_submit(text_widget2, name_entry2))
submit_button2.pack(pady=10)
text_widget2 = tk.Text(frame2, wrap=tk.WORD, height=40, width=45)
text_widget2.pack(pady=10)
mask_button2 = tk.Button(frame2, text="隐藏目标", command=lambda: toggle_visibility(text_widget2, mask_button2))
mask_button2.pack(side=tk.LEFT, padx=5)
lock_button2 = tk.Button(frame2, text="锁定", command=lambda: lock_buttons(lock_button2, submit_button2, mask_button2))
lock_button2.pack(side=tk.RIGHT, padx=5)

# 运行主循环
root.mainloop()
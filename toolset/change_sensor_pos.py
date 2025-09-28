import pymongo

# MongoDB连接配置
MONGODB_URI = "mongodb://localhost:28018"
EGO_VEHICLE_ID = "5c7fb3b0-1fd4-4943-8347-f73a05749718"

# 连接数据库
client = pymongo.MongoClient(MONGODB_URI)
db = client["WISE"]
col_vehicles = db["vehicles"]

# 获取车辆对象
vehicle_obj = col_vehicles.find_one({"cid": EGO_VEHICLE_ID})
if not vehicle_obj:
    print("未找到指定ID的车辆")
    exit(1)

# 收集带有transform的传感器
sensors_with_transform = []
sensors = vehicle_obj["data"]["sensors"]
for sensor in sensors:
    if "transform" in sensor:
        sensors_with_transform.append(sensor["name"])

# 显示可修改的传感器
print("你可以修改以下传感器的位置:")
for sensor in sensors_with_transform:
    print("*", sensor)

# 输入要修改的传感器名称
sensor_to_change = input("请输入传感器名称: ")
if sensor_to_change not in sensors_with_transform:
    print("无效的传感器名称")
    exit(1)

# 获取当前位置信息
current_transform = None
for sensor in sensors:
    if sensor["name"] == sensor_to_change:
        current_transform = sensor["transform"]
        break

print(f"当前位置: x={current_transform['x']}, y={current_transform['y']}, z={current_transform['z']}")

# 输入新的位置信息
try:
    new_x = float(input("请输入新的x坐标: "))
    new_y = float(input("请输入新的y坐标: "))
    new_z = float(input("请输入新的z坐标: "))
except ValueError:
    print("输入的坐标必须是数字")
    exit(1)

# 确认修改
confirmation = input(
    f"确定要将{sensor_to_change}的位置修改为x={new_x}, y={new_y}, z={new_z}吗? (y/n): "
)
if confirmation.lower() != "y":
    print("操作已取消")
    exit(0)

# 更新传感器位置
for sensor in vehicle_obj["data"]["sensors"]:
    if sensor["name"] == sensor_to_change:
        sensor["transform"]["x"] = new_x
        sensor["transform"]["y"] = new_y
        sensor["transform"]["z"] = new_z
        break

# 保存到数据库
col_vehicles.update_one(
    {"cid": EGO_VEHICLE_ID}, {"$set": {"data.sensors": vehicle_obj["data"]["sensors"]}}
)

print("传感器位置修改成功")

Python API Reference
# Python API Reference

[TOC]
## fc.fcapi
| 类型 | 内容 |
| ---- | :--- |
| 描述 |      |

### get_version
| 类型 | 内容                   |
| ---- | :--------------------- |
| 描述 | 返回当前API的版本(str) |

[^示例1]: 
```python
import fc
fcapi = fc.fcapi()
fcapi.get_version()
```


## fc.fcapi.app

| 类型 | 内容              |
| ---- | :---------------- |
| 描述 | App窗口相关的方法 |

### start_fcDesktop

| 类型 | 内容                          |
| ---- | :---------------------------- |
| 描述 | 运行桌面程序fcDesktop App窗口 |
| 参数 | 无参数                        |
| 返回 | 无返回项                      |

[^示例1]: 

```python
import fc
fcapi = fc.fcapi()
fcapi.app.start_fcDesktop()
```



### start_fcGlobalSettings

| 类型 | 内容                          |
| ---- | :---------------------------- |
| 描述 | 运行桌面程序fcGlobalSettings App窗口 |
| 参数 | 无参数                        |
| 返回 | 无返回项                      |


[^示例1]: 

```python
import fc
fcapi = fc.fcapi()
fcapi.app.start_fcGlobalSettings()
```

## fc.fcapi.rds

| 类型 | 内容                |
| ---- | :------------------ |
| 描述 | 阿里云RDS相关的方法 |

### set_config

| 类型 | 内容                                 |
| ---- | :----------------------------------- |
| 描述 | 将config下级的配置yml上传到阿里云RDS |
| 参数 | 无参数                               |
| 返回 | 无返回项                             |


[^示例1]: 

```python
import fc
fcapi = fc.fcapi()
fcapi.rds.set_config()
```
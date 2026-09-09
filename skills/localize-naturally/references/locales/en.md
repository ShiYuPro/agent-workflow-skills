# English — United States

适用：en-US；共享英文保持国际读者可理解。不要把美国英语自动等同于美元、英制单位或美国服务范围。

这是语言审校参考，不是已批准的产品译文。用户与项目已确认用法优先；示例用于说明方法，不用于自动替换。

## 语言与场景

- 用美式拼写；同一产品保持 sentence case 或已批准标题样式。按钮写动作，状态写发生了什么；不要把所有 UI 标签改成完整句。
- 英文自己就是目标语言：不要拿中文词序作底稿。区分 log a meal（记录动作）、meal log（记录集合）、record（单条数据）。
- 前置影响操作的条件，省略没有作用的 please；保留 must、may、only、not 的真实约束。自然缩写可依产品语气使用，不能为了简短制造生僻缩写。
- 无障碍标签须说清目标；避免单独的 Click here。泛指用户可用 singular they，不猜测用户性别。

## 格式与语法验收

动态日期、数字、单位和价格使用平台 formatter；静态跨地区说明优先写明月份，避免 09/08 的歧义。plural 常见 one/other；0 不能按 1 处理。

## 场景例

- 场景：首页热量余量标签
- 待改表达：`Today’s room`
- 参考表达：`Calories left today`
- 判断：表达每日剩余热量；不把 room 字面译为房间。

## 来源与取舍

核阅：2026-09-08。以下是所读文件；非全仓库背书，未声称母语者审定本档案。

- [Angular writing skill](https://github.com/angular/angular/blob/9a58353b1b680f162a55969965ae6a90ae20316d/.agent/skills/adev-writing-guide/SKILL.md)

不迁入：不迁入 Angular 专用 Markdown、强制 Oxford comma 或所有场景必须用第二人称的项目约定。

数量规则共同依据：[Unicode CLDR cardinal rules](https://github.com/unicode-org/cldr-json/blob/main/cldr-json/cldr-core/supplemental/plurals.json)，本轮读取2026-09-08；运行时可能使用不同CLDR版本，以实际目标平台验证。

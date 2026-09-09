# العربية — فصحى معاصرة متعددة المناطق

适用：共享ar采用清楚、现代的标准阿拉伯语；不要自行转成沙特／Najdi方言。数字系统、地区与日历独立确认。

这是语言审校参考，不是已批准的产品译文。用户与项目已确认用法优先；示例用于说明方法，不用于自动替换。

## 语言与场景

- 用清楚的现代书面语，短按钮如حفظ；不把正式理解成古雅，也不因消费者产品就自动改方言。
- 性别、双数、数词后的词形与完整句一致；未知用户性别不能靠猜测或采集新资料来解决，优先自然无性别的动作表达。
- 整句翻译，不把名字、数字与动词碎片拼接；动态拉丁品牌、URL及编号须检查双向隔离和屏幕朗读顺序。
- 存储逻辑字符顺序，让Unicode/平台排版；不要手动倒转阿拉伯文字，不使用展示形式字符或用空格断开连写。

## 格式与语法验收

验证zero/one/two/few/many/other，至少0、1、2、3、11、100及小数。数字字形和历法使用实际地区设置；ar不能硬映射ar-SA。检查括号、负号、单位、方向性图标。

## 场景例

- 场景：保存按钮
- 待改表达：`القيام بعملية الحفظ`
- 参考表达：`حفظ`
- 判断：动词名词式短标签即可；不引入特定方言。

## 来源与取舍

核阅：2026-09-08。以下是所读文件；非全仓库背书，未声称母语者审定本档案。

- [Arabic skill：仅选取语域区分](https://github.com/majiayu000/claude-skill-registry/blob/50a687710e3a360055ab0f358755698220b9e7af/skills/design/arabic-localization-muneer911-saas-skills/SKILL.md)
- [W3C Arabic layout（本轮核对方向与数字地区差异）](https://github.com/w3c/alreq/blob/gh-pages/index.html)

不迁入：拒绝skill中海湾消费者必用Najdi、硬编码月份/地区的建议。Mozilla docs/ar/README.md含KiArabic与斯瓦希里语例句污染，本轮整份排除，不作语言依据。

数量规则共同依据：[Unicode CLDR cardinal rules](https://github.com/unicode-org/cldr-json/blob/main/cldr-json/cldr-core/supplemental/plurals.json)，本轮读取2026-09-08；运行时可能使用不同CLDR版本，以实际目标平台验证。

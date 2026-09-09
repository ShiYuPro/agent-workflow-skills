# 한국어 — 대한민국

适用：ko-KR；面向韩国用户的产品语言。

这是语言审校参考，不是已批准的产品译文。用户与项目已确认用法优先；示例用于说明方法，不用于自动替换。

## 语言与场景

- 正文选择一致的礼貌等级，按钮可用저장、확인等简短形式；保留项目现有合适语气，不把整个产品改成命令口吻。
- 核对助词与前词收音。动态名称不能永远拼接同一个은/는、이/가；可改成“항목: {name}”一类真正的标签布局，或使用项目的助词处理。
- 减少被动叠加（되어진다）及生硬的에 있어서、通过式抽象表述；是否改由实际语义与文体决定，不按出现次数判错。
- 空格按韩语词组书写；避免英文代词照译和中英混写。保留否定、推测和可能性，不能把할 수 있다自动改为必然。

## 格式与语法验收

核对韩文断词、计数单位、日期和带拉丁品牌的助词；无英语式复数不等于任何数量都可删。屏幕状态和完整错误句分别审校。

## 场景例

- 场景：保存完成的状态提示
- 待改表达：`저장이 되어졌습니다`
- 参考表达：`저장되었습니다`
- 判断：修正双重被动；不改变已完成状态。

## 来源与取舍

核阅：2026-09-08。以下是所读文件；非全仓库背书，未声称母语者审定本档案。

- [Korean skill](https://github.com/w00ing/skills/blob/c94791aa5cc49acafc05c8e097b33e948c6b1eb6/humanize-korean/SKILL.md)
- [Korean quick rules](https://github.com/w00ing/skills/blob/c94791aa5cc49acafc05c8e097b33e948c6b1eb6/humanize-korean/references/quick-rules.md)
- [Mozilla 韩国指南](https://github.com/mozilla-l10n/styleguides/blob/50ad513b1fe0c67d10cc9ade5a5ef8078153889b/docs/ko/README.md)

不迁入：排除来源的固定修改率、AI 自评分、按频次禁词和“推测改断言”规则；不用英文大写判断所有词是否应保留。

数量规则共同依据：[Unicode CLDR cardinal rules](https://github.com/unicode-org/cldr-json/blob/main/cldr-json/cldr-core/supplemental/plurals.json)，本轮读取2026-09-08；运行时可能使用不同CLDR版本，以实际目标平台验证。

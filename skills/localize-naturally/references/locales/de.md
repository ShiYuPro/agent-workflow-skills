# Deutsch — Deutschland

适用：de-DE 为本项目基线；de-AT／de-CH另行确认。瑞士ß规则不可套用德国，语言也不决定货币。

这是语言审校参考，不是已批准的产品译文。用户与项目已确认用法优先；示例用于说明方法，不用于自动替换。

## 语言与场景

- 明确du／Sie／无称呼的既有约定；短按钮常用不定式Speichern，正文不能无缘由切换称呼。
- 减少名词化叠加，把die Durchführung der Erfassung改成具体动作；按德语语序重建，不能只逐词替换。
- 名词正常大写，标题不逐词 Title Case；正确使用ä、ö、ü、ß，不因工具方便退成ae／oe／ue。
- 复合词和长修饰语要可读；不能只靠缩小字号解决超长按钮，也不能机械拆错德语复合词。

## 格式与语法验收

德国常见数字1.234,56，静态日期须分清日月；真实值由 formatter 处理。检查1与其他数量、长单词窄屏换行。

## 场景例

- 场景：保存记录按钮
- 待改表达：`Die Speicherung des Eintrags durchführen`
- 参考表达：`Eintrag speichern`
- 判断：用明确动词动作，保留保存对象。

## 来源与取舍

核阅：2026-09-08。以下是所读文件；非全仓库背书，未声称母语者审定本档案。

- [German skill](https://github.com/w00ing/skills/blob/c94791aa5cc49acafc05c8e097b33e948c6b1eb6/humanize-german/SKILL.md)
- [Mozilla 德语指南](https://github.com/mozilla-l10n/styleguides/blob/50ad513b1fe0c67d10cc9ade5a5ef8078153889b/docs/de/README.md)

不迁入：不迁入“绝不能用du”、固定禁用Darüber hinaus或全部英式词禁令。

数量规则共同依据：[Unicode CLDR cardinal rules](https://github.com/unicode-org/cldr-json/blob/main/cldr-json/cldr-core/supplemental/plurals.json)，本轮读取2026-09-08；运行时可能使用不同CLDR版本，以实际目标平台验证。

# Français — France par défaut

适用：fr-FR 用于项目商店；加拿大、比利时、瑞士等地区需各自确认，不能把法国规则当全部法语。

这是语言审校参考，不是已批准的产品译文。用户与项目已确认用法优先；示例用于说明方法，不用于自动替换。

## 语言与场景

- 确定tu／vous并保持段落一致；保存等按钮通常用不定式Enregistrer。普通文案不要无依据提高正式程度。
- 核对名词性别、形容词及过去分词配合；动态名词需要完整句或语法分支，不把英语片段连成法语。
- 保留重音及大写重音；标题通常使用句式大小写，已有品牌名称例外。
- 别把生效、可用、已完成、可能完成混在一起；优先常用产品动词而非抽象名词串。

## 格式与语法验收

法国语境核对冒号、分号、问号、感叹号和« »附近的不可断空格，具体空格宽度遵循平台／项目。数字用 formatter。0/1与百万类别需依CLDR；不能硬写 n==1。

## 场景例

- 场景：保存按钮
- 待改表达：`Sauvez vos modifications maintenant`
- 参考表达：`Enregistrer`
- 判断：按钮只负责保存时的精简样例；不是禁止完整指令或vous。

## 来源与取舍

核阅：2026-09-08。以下是所读文件；非全仓库背书，未声称母语者审定本档案。

- [Zulip 法语指南](https://github.com/zulip/zulip/blob/371b2ff9840988c4a128491d4c076d2e008a2be3/docs/translating/french.md)
- [Mozilla 法语入口](https://github.com/mozilla-l10n/styleguides/blob/50ad513b1fe0c67d10cc9ade5a5ef8078153889b/docs/fr/README.md)

不迁入：Zulip 要求跟随英文大小写不迁入；Mozilla 链接的 wiki 本轮读取失败，不能声称读过其内容。

数量规则共同依据：[Unicode CLDR cardinal rules](https://github.com/unicode-org/cldr-json/blob/main/cldr-json/cldr-core/supplemental/plurals.json)，本轮读取2026-09-08；运行时可能使用不同CLDR版本，以实际目标平台验证。

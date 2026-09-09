# Português — Brasil

适用：明确pt-BR；不能降为模糊pt后套用pt-PT用词和复数。

这是语言审校参考，不是已批准的产品译文。用户与项目已确认用法优先；示例用于说明方法，不用于自动替换。

## 语言与场景

- 使用巴西产品常用词，如arquivo、tela、aplicativo、baixar；不要机械替换已批准专业词，也不混入ficheiro／ecrã等葡萄牙地区词。
- 短按钮可用Salvar、Excluir等不定式，帮助说明使用自然指令；若用você，动词保持相应人称，不混搭tu的屈折。
- 避免假朋友：library在软件场景是biblioteca，不是livraria；登录、日志与食物记录按含义分别处理。
- 检查省略与增译：下载不等于下载并安装；自然化不能添加安装、付款或已完成动作。

## 格式与语法验收

巴西地区数字／日期／货币用formatter；pt-BR的0及小数可能走one，不能套用pt-PT或英语规则。复数按运行时CLDR，含百万many类别。

## 场景例

- 场景：下载软件库的按钮
- 待改表达：`Baixar e instalar essa livraria Python`
- 参考表达：`Baixar essa biblioteca Python`
- 判断：修正领域词并移除源文没有的安装动作。

## 来源与取舍

核阅：2026-09-08。以下是所读文件；非全仓库背书，未声称母语者审定本档案。

- [Mozilla 巴西指南](https://github.com/mozilla-l10n/styleguides/blob/50ad513b1fe0c67d10cc9ade5a5ef8078153889b/docs/pt-BR/general.md)
- [Mozilla 巴西术语](https://github.com/mozilla-l10n/styleguides/blob/50ad513b1fe0c67d10cc9ade5a5ef8078153889b/docs/pt-BR/glossary.md)
- [专项 skill 审查但不采用](https://github.com/rborcherds/wdd130-instructor/blob/7dab33deb489b9e14aad6efd4c645e0a22f711a8/.claude/skills/add-pt-translation/SKILL.md)

不迁入：不采用专项skill的句子拆成HTML碎片、alt保留英文及pt/pt-BR混用；不迁入浏览器私有词或允许文字截断的做法。

数量规则共同依据：[Unicode CLDR cardinal rules](https://github.com/unicode-org/cldr-json/blob/main/cldr-json/cldr-core/supplemental/plurals.json)，本轮读取2026-09-08；运行时可能使用不同CLDR版本，以实际目标平台验证。

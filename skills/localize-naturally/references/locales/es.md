# Español — UI neutral; tienda España

适用：共享 es UI 使用广泛可理解的西语；es-ES 商店按西班牙地区。不能默认所有西语用户来自西班牙。

这是语言审校参考，不是已批准的产品译文。用户与项目已确认用法优先；示例用于说明方法，不用于自动替换。

## 语言与场景

- 先继承tú／usted的项目约定；按钮一般可用Guardar等不定式。不要把“正式／非正式”视为全语言强制标准。
- 避免逐字翻译软件隐喻：主页通常是Inicio，不是住宅意义的Hogar；词表按具体功能建立。
- 共用 UI 避免局部俚语与不必要的vosotros等地区绑定；地区商店文案允许使用当地惯例。
- 标题按西语大小写与重音处理，不能照搬 English Title Case；保留¿?和¡!的成对标点。

## 格式与语法验收

数字／日期通过选定地区 formatter；plural 不只凭英语复制：CLDR 包含 one/many/other，百万类按实际引擎。金额不因语言改币种。

## 场景例

- 场景：导航主页
- 待改表达：`Hogar`
- 参考表达：`Inicio`
- 判断：软件导航而非家居／住宅场景。

## 来源与取舍

核阅：2026-09-08。以下是所读文件；非全仓库背书，未声称母语者审定本档案。

- [Zulip 西语](https://github.com/zulip/zulip/blob/371b2ff9840988c4a128491d4c076d2e008a2be3/docs/translating/spanish.md)
- [Mozilla 西班牙指南](https://github.com/mozilla-l10n/styleguides/blob/50ad513b1fe0c67d10cc9ade5a5ef8078153889b/docs/es-ES/README.md)

不迁入：两个来源敬称策略不同，均不直接设为我们的统一政策；不继承旧版solo重音绝对规则或聊天产品术语。

数量规则共同依据：[Unicode CLDR cardinal rules](https://github.com/unicode-org/cldr-json/blob/main/cldr-json/cldr-core/supplemental/plurals.json)，本轮读取2026-09-08；运行时可能使用不同CLDR版本，以实际目标平台验证。

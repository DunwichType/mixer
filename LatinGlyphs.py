#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Lists of Latin Glyphs for use with Mixer

# Basic Latin Alphabet

majbasic = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

minbasic = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

allbasic = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# DTF Latin Character Set

majuscules = [u'A', u'À', u'Á', u'Â', u'Ã', u'Ä', u'Å', u'Æ', u'Ā', u'Ă', u'Ą', u'Æ', u'Ǽ', u'Z', u'B', u'C', u'Ç', u'Ć', u'Ĉ', u'Ċ', u'Č', u'D', u'Ď', u'Đ', u'E', u'È', u'É', u'Ê', u'Ë', u'Ē', u'Ĕ', u'Ė', u'Ę', u'Ě', u'F', u'G', u'Ĝ', u'Ğ', u'Ġ', u'Ģ', u'H', u'Ĥ', u'Ħ', u'I', u'Ì', u'Í', u'Î', u'Ï', u'Ĩ', u'Ī', u'Ĭ', u'Į', u'J', u'Ĵ', u'K', u'Ķ', u'L', u'Ĺ', u'Ļ', u'Ľ', u'Ł', u'Ŀ', u'M', u'N', u'Ń', u'Ņ', u'Ň', u'Ŋ', u'Ñ', u'Ò', u'Ó', u'Ô', u'Õ', u'Ö', u'Ō', u'Ŏ', u'Ő', u'Ø', u'Ǿ', u'Œ', u'P', u'Q', u'Þ', u'R', u'Ŕ', u'Ř', u'Ŗ', u'S', u'Ś', u'Ŝ', u'Ş', u'Š', u'Ș', u'T', u'Ţ', u'Ť', u'Ŧ', u'Ț', u'U', u'Ù', u'Ú', u'Û', u'Ü', u'Ũ', u'Ū', u'Ŭ', u'Ů', u'Ű', u'Ų', u'V', u'W', u'Ŵ', u'Ẁ', u'Ẃ', u'Ẅ', u'X', u'Y', u'Ý', u'Ŷ', u'Ÿ', u'Z', u'Ź', u'Ż', u'Ž']

minuscules = [u'a', u'à', u'á', u'â', u'ã', u'ä', u'å', u'æ', u'ā', u'ă', u'ą', u'æ', u'ǽ', u'b', u'v', u'ç', u'ć', u'ĉ', u'ċ', u'č', u'd', u'ď', u'đ', u'e', u'è', u'é', u'ê', u'ë', u'ē', u'ĕ', u'ė', u'ę', u'ě', u'f', u'g', u'ĝ', u'ğ', u'ġ', u'ģ', u'h', u'ĥ', u'ħ', u'i', u'ì', u'í', u'î', u'ï', u'ĩ', u'ī', u'ĭ', u'į', u'j', u'ĵ', u'k', u'ķ', u'l', u'ĺ', u'ļ', u'ľ', u'ł', u'ŀ', u'm', u'n', u'ń', u'ņ', u'ň', u'ŋ', u'ñ', u'o', u'ò', u'ó', u'ô', u'õ', u'ö', u'ō', u'ŏ', u'ő', u'ø', u'ǿ', u'œ', u'p', u'þ', u'q', u'r', u'ŕ', u'ř', u'ŗ', u's', u'ś', u'ŝ', u'ş', u'š', u'ș', u'ß', u't', u'ţ', u'ť', u'ŧ', u'ț', u'u', u'ù', u'ú', u'û', u'ü', u'ũ', u'ū', u'ŭ', u'ů', u'ű', u'ų', u'v', u'w', u'ŵ', u'ẁ', u'ẃ', u'ẅ', u'x', u'y', u'ý', u'ŷ', u'ÿ', u'z', u'ź', u'ż', u'ž']

# Punctuation

basicpunct = [u'.', u',', u'\"', u'!', u'?', u'&']

punct = [u'.', u'…', u',', u':', u';', u'?', u'¿', u'!', u'¡', u'\'', u'\"', u'‘', u'’', u'‚', u'“', u'”', u'„', u'‹', u'›', u'«', u'»', u'-', u'–', u'—', u'_', u'†', u'‡', u'•', u'*', u'©', u'®', u'™', u'@', u'¶', u'(', u')', u'[', u']', u'{', u'}', u'/', u'\\', u'|']

# Numbers

currency = [u'#', u'%', u'&', u'¢', u'$', u'£', u'¥', u'ƒ', u'€']

numerals = [u'0', u'1', u'2', u'3', u'4', u'5', u'6', u'7', u'8', u'9']

prebuilt = [u'½', u'¼', u'¾', u'⅓', u'⅔', u'⅛', u'⅜', u'⅝']

math = [u'<', u'+', u'−', u'=', u'÷', u'×', u'>', u'±', u'^', u'~', u'|', u'¦', u'§', u'°', u'ª', u'º', u'%']

fractions = [u'½', u'¼', u'¾', u'⅓', u'⅔', u'⅛', u'⅜', u'⅝']

# Prototyping

adhesion = [u'a', u'd', u'h', u'e', u's', u'i', u'o', u'n']

ADHESION = [u'A', u'D', u'H', u'E', u'S', u'I', u'O', u'N']

handgloves = [u'h', u'a', u'n', u'd', u'g', u'l', u'o', u'v', u'e', u's']

HANDGLOVES = [u'H', u'A', u'N', u'D', u'G', u'L', u'O', u'V', u'E', u'S']

hamburgefontivs = [u'h', u'a', u'm', u'b', u'u', u'r', u'g', u'e', u'f', u'o', u'n', u't', u'i', u'v', u's']

HAMBURGEFONTIVS = [u'H', u'A', u'M', u'B', u'U', u'R', u'G', u'E', u'F', u'O', u'N', u'T', u'I', u'V', u'S']

#Latin Extended B

majLatinXB = [u'Ɓ', u'Ƃ', u'Ƅ', u'Ɔ', u'Ƈ', u'Ɖ', u'Ɗ', u'Ƌ', u'Ǝ', u'Ə', u'Ɛ', u'Ƒ', u'Ɠ', u'Ɣ', u'Ɩ', u'Ɨ', u'Ƙ', u'Ɯ', u'Ɲ', u'Ɵ', u'Ơ', u'Ƣ', u'Ƥ', u'Ʀ', u'Ƨ', u'Ʃ', u'ƪ', u'Ƭ', u'Ʈ', u'Ư', u'Ʊ', u'Ʋ', u'Ƴ', u'Ƶ', u'Ʒ', u'Ƹ', u'ƻ', u'Ƽ', u'ǀ', u'ǁ', u'ǂ', u'ǃ', u'Ǆ', u'ǅ', u'Ǉ', u'ǈ', u'Ǌ', u'ǋ', u'Ǎ', u'Ǐ', u'Ǒ', u'Ǔ', u'Ǖ', u'Ǘ', u'Ǚ', u'Ǜ', u'Ǟ', u'Ǡ', u'Ǣ', u'Ǥ', u'Ǧ', u'Ǩ', u'Ǫ', u'Ǭ', u'Ǯ', u'Ǳ', u'ǲ', u'Ǵ', u'Ƕ', u'Ƿ', u'Ǹ', u'Ǻ', u'Ǽ', u'Ȁ', u'Ȃ', u'Ȅ', u'Ȇ', u'Ȉ', u'Ȋ', u'Ȍ', u'Ȏ', u'Ȑ', u'Ȓ', u'Ȕ', u'Ȗ', u'Ș', u'Ț', u'Ȝ', u'Ȟ', u'Ƞ', u'Ȣ', u'Ȥ', u'Ȧ', u'Ȩ', u'Ȫ', u'Ȭ', u'Ȯ', u'Ȱ', u'Ȳ', u'Ⱥ', u'Ȼ', u'Ƚ', u'Ⱦ', u'Ɂ', u'Ƀ', u'Ʉ', u'Ʌ', u'Ɇ', u'Ɉ', u'Ɋ', u'Ɍ', u'Ɏ']

minusLatinXB = [u'ƀ', u'ƃ', u'ƅ', u'ƈ', u'ƌ', u'ƍ', u'ƕ', u'ƙ', u'ƚ', u'ƛ', u'ơ', u'ƣ', u'ƥ', u'ƨ', u'ƫ', u'ƭ', u'ư', u'ƴ', u'ƶ', u'ƹ', u'ƺ', u'ƽ', u'ƾ', u'ƿ', u'ǆ', u'ǉ', u'ǌ', u'ǎ', u'ǐ', u'ǒ', u'ǔ', u'ǖ', u'ǘ', u'ǚ', u'ǜ', u'ǝ', u'ǟ', u'ǡ', u'ǣ', u'ǥ', u'ǧ', u'ǩ', u'ǫ', u'ǭ', u'ǯ', u'ǳ', u'ǵ', u'ǹ', u'ǻ', u'ǽ', u'ȁ', u'ȃ', u'ȅ', u'ȇ', u'ȉ', u'ȋ', u'ȍ', u'ȏ', u'ȑ', u'ȓ', u'ȕ', u'ȗ', u'ș', u'ț', u'ȝ', u'ȟ', u'ȡ', u'ȣ', u'ȥ', u'ȧ', u'ȩ', u'ȫ', u'ȭ', u'ȯ', u'ȱ', u'ȳ', u'ȴ', u'ȵ', u'ȶ', u'ȷ', u'ȸ', u'ȹ', u'ȼ', u'ȿ', u'ɀ', u'ɂ', u'ɇ', u'ɉ', u'ɋ', u'ɍ', u'ɏ']

#Control Characters

lc_control = [u'anon ', u'bnon ', u'cnon ', u'dnon ', u'enon ', u'fnon ', u'gnon ', u'hnon ', u'inon ', u'jnon ', u'knon ', u'lnon ', u'mnon ', u'nnon ', u'onon ', u'pnon ', u'qnon ', u'rnon ', u'snon ', u'tnon ', u'unon ', u'vnon ', u'wnon ', u'xnon ', u'ynon ', u'znon ']

controls = [u'H', u'O', u'h', u'n', u'o']
majcontrols = [u'H', u'O']
mincontrols = [u'h', u'o', u'n']
figcontrols = [u'0', u'1']
# copyrights Kunal Gaikwad
# telegram : telegram.dog/sux69sux

from flask import Flask, jsonify

app = Flask(__name__)

language_data = [
    {
        "language": "Afar",
        "code": "aa"
    },
    {
        "language": "Abkhazian",
        "code": "ab"
    },
    {
        "language": "Avestan",
        "code": "ae"
    },
    {
        "language": "Afrikaans",
        "code": "af"
    },
    {
        "language": "Akan",
        "code": "ak"
    },
    {
        "language": "Amharic",
        "code": "am"
    },
    {
        "language": "Aragonese",
        "code": "an"
    },
    {
        "language": "Arabic",
        "code": "ar"
    },
    {
        "language": "Assamese",
        "code": "as"
    },
    {
        "language": "Avaric",
        "code": "av"
    },
    {
        "language": "Aymara",
        "code": "ay"
    },
    {
        "language": "Azerbaijani",
        "code": "az"
    },
    {
        "language": "Bashkir",
        "code": "ba"
    },
    {
        "language": "Belarusian",
        "code": "be"
    },
    {
        "language": "Bulgarian",
        "code": "bg"
    },
    {
        "language": "Bihari languages",
        "code": "bh"
    },
    {
        "language": "Bislama",
        "code": "bi"
    },
    {
        "language": "Bambara",
        "code": "bm"
    },
    {
        "language": "Bengali",
        "code": "bn"
    },
    {
        "language": "Tibetan",
        "code": "bo"
    },
    {
        "language": "Breton",
        "code": "br"
    },
    {
        "language": "Bosnian",
        "code": "bs"
    },
    {
        "language": "Catalan; Valencian",
        "code": "ca"
    },
    {
        "language": "Chechen",
        "code": "ce"
    },
    {
        "language": "Chamorro",
        "code": "ch"
    },
    {
        "language": "Corsican",
        "code": "co"
    },
    {
        "language": "Cree",
        "code": "cr"
    },
    {
        "language": "Czech",
        "code": "cs"
    },
    {
        "language": "Church Slavic; Slavonic;Old Bulgarian",
        "code": "cu"
    },
    {
        "language": "Chuvash",
        "code": "cv"
    },
    {
        "language": "Welsh",
        "code": "cy"
    },
    {
        "language": "Danish",
        "code": "da"
    },
    {
        "language": "German",
        "code": "de"
    },
    {
        "language": "Divehi; Dhivehi; Maldivian",
        "code": "dv"
    },
    {
        "language": "Dzongkha",
        "code": "dz"
    },
    {
        "language": "Ewe",
        "code": "ee"
    },
    {
        "language": "Greek, Modern (1453-)",
        "code": "el"
    },
    {
        "language": "English",
        "code": "en"
    },
    {
        "language": "Esperanto",
        "code": "eo"
    },
    {
        "language": "Spanish; Castilian",
        "code": "es"
    },
    {
        "language": "Estonian",
        "code": "et"
    },
    {
        "language": "Basque",
        "code": "eu"
    },
    {
        "language": "Persian",
        "code": "fa"
    },
    {
        "language": "Fulah",
        "code": "ff"
    },
    {
        "language": "Finnish",
        "code": "fi"
    },
    {
        "language": "Fijian",
        "code": "fj"
    },
    {
        "language": "Faroese",
        "code": "fo"
    },
    {
        "language": "French",
        "code": "fr"
    },
    {
        "language": "Western Frisian",
        "code": "fy"
    },
    {
        "language": "Irish",
        "code": "ga"
    },
    {
        "language": "Gaelic; Scottish Gaelic",
        "code": "gd"
    },
    {
        "language": "Galician",
        "code": "gl"
    },
    {
        "language": "Guarani",
        "code": "gn"
    },
    {
        "language": "Gujarati",
        "code": "gu"
    },
    {
        "language": "Manx",
        "code": "gv"
    },
    {
        "language": "Hausa",
        "code": "ha"
    },
    {
        "language": "Hebrew",
        "code": "he"
    },
    {
        "language": "Hindi",
        "code": "hi"
    },
    {
        "language": "Hiri Motu",
        "code": "ho"
    },
    {
        "language": "Croatian",
        "code": "hr"
    },
    {
        "language": "Haitian; Haitian Creole",
        "code": "ht"
    },
    {
        "language": "Hungarian",
        "code": "hu"
    },
    {
        "language": "Armenian",
        "code": "hy"
    },
    {
        "language": "Herero",
        "code": "hz"
    },
    {
        "language": "Interlingua",
        "code": "ia"
    },
    {
        "language": "Indonesian",
        "code": "id"
    },
    {
        "language": "Interlingue; Occidental",
        "code": "ie"
    },
    {
        "language": "Igbo",
        "code": "ig"
    },
    {
        "language": "Sichuan Yi; Nuosu",
        "code": "ii"
    },
    {
        "language": "Inupiaq",
        "code": "ik"
    },
    {
        "language": "Ido",
        "code": "io"
    },
    {
        "language": "Icelandic",
        "code": "is"
    },
    {
        "language": "Italian",
        "code": "it"
    },
    {
        "language": "Inuktitut",
        "code": "iu"
    },
    {
        "language": "Japanese",
        "code": "ja"
    },
    {
        "language": "Javanese",
        "code": "jv"
    },
    {
        "language": "Georgian",
        "code": "ka"
    },
    {
        "language": "Kongo",
        "code": "kg"
    },
    {
        "language": "Kikuyu; Gikuyu",
        "code": "ki"
    },
    {
        "language": "Kuanyama; Kwanyama",
        "code": "kj"
    },
    {
        "language": "Kazakh",
        "code": "kk"
    },
    {
        "language": "Kalaallisut; Greenlandic",
        "code": "kl"
    },
    {
        "language": "Central Khmer",
        "code": "km"
    },
    {
        "language": "Kannada",
        "code": "kn"
    },
    {
        "language": "Korean",
        "code": "ko"
    },
    {
        "language": "Kanuri",
        "code": "kr"
    },
    {
        "language": "Kashmiri",
        "code": "ks"
    },
    {
        "language": "Kurdish",
        "code": "ku"
    },
    {
        "language": "Komi",
        "code": "kv"
    },
    {
        "language": "Cornish",
        "code": "kw"
    },
    {
        "language": "Kirghiz; Kyrgyz",
        "code": "ky"
    },
    {
        "language": "Latin",
        "code": "la"
    },
    {
        "language": "Luxembourgish; Letzeburgesch",
        "code": "lb"
    },
    {
        "language": "Ganda",
        "code": "lg"
    },
    {
        "language": "Limburgan; Limburger; Limburgish",
        "code": "li"
    },
    {
        "language": "Lingala",
        "code": "ln"
    },
    {
        "language": "Lao",
        "code": "lo"
    },
    {
        "language": "Lithuanian",
        "code": "lt"
    },
    {
        "language": "Luba-Katanga",
        "code": "lu"
    },
    {
        "language": "Latvian",
        "code": "lv"
    },
    {
        "language": "Malagasy",
        "code": "mg"
    },
    {
        "language": "Marshallese",
        "code": "mh"
    },
    {
        "language": "Maori",
        "code": "mi"
    },
    {
        "language": "Macedonian",
        "code": "mk"
    },
    {
        "language": "Malayalam",
        "code": "ml"
    },
    {
        "language": "Mongolian",
        "code": "mn"
    },
    {
        "language": "Marathi",
        "code": "mr"
    },
    {
        "language": "Malay",
        "code": "ms"
    },
    {
        "language": "Maltese",
        "code": "mt"
    },
    {
        "language": "Burmese",
        "code": "my"
    },
    {
        "language": "Nauru",
        "code": "na"
    },
    {
        "language": "Norwegian Bokmål",
        "code": "nb"
    },
    {
        "language": "Ndebele, North; North Ndebele",
        "code": "nd"
    },
    {
        "language": "Nepali",
        "code": "ne"
    },
    {
        "language": "Ndonga",
        "code": "ng"
    },
    {
        "language": "Dutch; Flemish",
        "code": "nl"
    },
    {
        "language": "Norwegian Nynorsk",
        "code": "nn"
    },
    {
        "language": "Norwegian",
        "code": "no"
    },
    {
        "language": "Ndebele, South; South Ndebele",
        "code": "nr"
    },
    {
        "language": "Navajo; Navaho",
        "code": "nv"
    },
    {
        "language": "Chichewa; Chewa; Nyanja",
        "code": "ny"
    },
    {
        "language": "Occitan (post 1500)",
        "code": "oc"
    },
    {
        "language": "Ojibwa",
        "code": "oj"
    },
    {
        "language": "Oromo",
        "code": "om"
    },
    {
        "language": "Oriya",
        "code": "or"
    },
    {
        "language": "Ossetian; Ossetic",
        "code": "os"
    },
    {
        "language": "Panjabi; Punjabi",
        "code": "pa"
    },
    {
        "language": "Pali",
        "code": "pi"
    },
    {
        "language": "Polish",
        "code": "pl"
    },
    {
        "language": "Pushto; Pashto",
        "code": "ps"
    },
    {
        "language": "Portuguese",
        "code": "pt"
    },
    {
        "language": "Quechua",
        "code": "qu"
    },
    {
        "language": "Romansh",
        "code": "rm"
    },
    {
        "language": "Rundi",
        "code": "rn"
    },
    {
        "language": "Romanian; Moldavian; Moldovan",
        "code": "ro"
    },
    {
        "language": "Russian",
        "code": "ru"
    },
    {
        "language": "Kinyarwanda",
        "code": "rw"
    },
    {
        "language": "Sanskrit",
        "code": "sa"
    },
    {
        "language": "Sardinian",
        "code": "sc"
    },
    {
        "language": "Sindhi",
        "code": "sd"
    },
    {
        "language": "Northern Sami",
        "code": "se"
    },
    {
        "language": "Sango",
        "code": "sg"
    },
    {
        "language": "Sinhala; Sinhalese",
        "code": "si"
    },
    {
        "language": "Slovak",
        "code": "sk"
    },
    {
        "language": "Slovenian",
        "code": "sl"
    },
    {
        "language": "Samoan",
        "code": "sm"
    },
    {
        "language": "Shona",
        "code": "sn"
    },
    {
        "language": "Somali",
        "code": "so"
    },
    {
        "language": "Albanian",
        "code": "sq"
    },
    {
        "language": "Serbian",
        "code": "sr"
    },
    {
        "language": "Swati",
        "code": "ss"
    },
    {
        "language": "Sotho, Southern",
        "code": "st"
    },
    {
        "language": "Sundanese",
        "code": "su"
    },
    {
        "language": "Swedish",
        "code": "sv"
    },
    {
        "language": "Swahili",
        "code": "sw"
    },
    {
        "language": "Tamil",
        "code": "ta"
    },
    {
        "language": "Telugu",
        "code": "te"
    },
    {
        "language": "Tajik",
        "code": "tg"
    },
    {
        "language": "Thai",
        "code": "th"
    },
    {
        "language": "Tigrinya",
        "code": "ti"
    },
    {
        "language": "Turkmen",
        "code": "tk"
    },
    {
        "language": "Tagalog",
        "code": "tl"
    },
    {
        "language": "Tswana",
        "code": "tn"
    },
    {
        "language": "Tonga (Tonga Islands)",
        "code": "to"
    },
    {
        "language": "Turkish",
        "code": "tr"
    },
    {
        "language": "Tsonga",
        "code": "ts"
    },
    {
        "language": "Tatar",
        "code": "tt"
    },
    {
        "language": "Twi",
        "code": "tw"
    },
    {
        "language": "Tahitian",
        "code": "ty"
    },
    {
        "language": "Uighur; Uyghur",
        "code": "ug"
    },
    {
        "language": "Ukrainian",
        "code": "uk"
    },
    {
        "language": "Urdu",
        "code": "ur"
    },
    {
        "language": "Uzbek",
        "code": "uz"
    },
    {
        "language": "Venda",
        "code": "ve"
    },
    {
        "language": "Vietnamese",
        "code": "vi"
    },
    {
        "language": "Volapük",
        "code": "vo"
    },
    {
        "language": "Walloon",
        "code": "wa"
    },
    {
        "language": "Wolof",
        "code": "wo"
    },
    {
        "language": "Xhosa",
        "code": "xh"
    },
    {
        "language": "Yiddish",
        "code": "yi"
    },
    {
        "language": "Yoruba",
        "code": "yo"
    },
    {
        "language": "Zhuang; Chuang",
        "code": "za"
    },
    {
        "language": "Chinese",
        "code": "zh"
    },
    {
        "language": "Zulu",
        "code": "zu"
    }
]

@app.route('/languages/<lang_code>')
def get_language(lang_code):
    for language in language_data:
        if language["code"] == lang_code:
            return jsonify(language)
    return jsonify({"error": "Language not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)

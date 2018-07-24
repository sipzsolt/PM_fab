from flask import flash
from wtforms import Form, StringField, FieldList, FormField, BooleanField, SelectMultipleField, widgets, RadioField, IntegerField, DateField, FileField, TextAreaField, SelectField, Field
from wtforms.validators import DataRequired, Email, ValidationError
from flask_appbuilder.fieldwidgets import BS3TextFieldWidget, DatePickerWidget
from flask_appbuilder.forms import DynamicForm
from app import db
from .models import PM_Skillset
import datetime
import re
import pdb


currencies = {
    "USD": {
        "symbol": "$",
        "name": "US Dollar",
        "symbol_native": "$",
        "decimal_digits": 2,
        "rounding": 0,
        "code": "USD",
        "name_plural": "US dollars"
    },
    "CAD": {
        "symbol": "CA$",
        "name": "Canadian Dollar",
        "symbol_native": "$",
        "decimal_digits": 2,
        "rounding": 0,
        "code": "CAD",
        "name_plural": "Canadian dollars"
    },
    "EUR": {
        "symbol": "€",
        "name": "Euro",
        "symbol_native": "€",
        "decimal_digits": 2,
        "rounding": 0,
        "code": "EUR",
        "name_plural": "euros"
    },
    "AED": {
        "symbol": "AED",
        "name": "United Arab Emirates Dirham",
        "symbol_native": "د.إ.‏",
        "decimal_digits": 2,
        "rounding": 0,
        "code": "AED",
        "name_plural": "UAE dirhams"
    },
    "AFN": {
        "symbol": "Af",
        "name": "Afghan Afghani",
        "symbol_native": "؋",
        "decimal_digits": 0,
        "rounding": 0,
        "code": "AFN",
        "name_plural": "Afghan Afghanis"
    },
    "ALL": {
        "symbol": "ALL",
        "name": "Albanian Lek",
        "symbol_native": "Lek",
        "decimal_digits": 0,
        "rounding": 0,
        "code": "ALL",
        "name_plural": "Albanian lekë"
    },
    "AMD": {
        "symbol": "AMD",
        "name": "Armenian Dram",
        "symbol_native": "դր.",
        "decimal_digits": 0,
        "rounding": 0,
        "code": "AMD",
        "name_plural": "Armenian drams"
    },
    "ARS": {
        "symbol": "AR$",
        "name": "Argentine Peso",
        "symbol_native": "$",
        "decimal_digits": 2,
        "rounding": 0,
        "code": "ARS",
        "name_plural": "Argentine pesos"
    },
    "AUD": {
        "symbol": "AU$",
        "name": "Australian Dollar",
        "symbol_native": "$",
        "decimal_digits": 2,
        "rounding": 0,
        "code": "AUD",
        "name_plural": "Australian dollars"
    },
    "AZN": {
        "symbol": "man.",
        "name": "Azerbaijani Manat",
        "symbol_native": "ман.",
        "decimal_digits": 2,
        "rounding": 0,
        "code": "AZN",
        "name_plural": "Azerbaijani manats"
    },
    "BAM": {
        "symbol": "KM",
        "name": "Bosnia-Herzegovina Convertible Mark",
        "symbol_native": "KM",
        "decimal_digits": 2,
        "rounding": 0,
        "code": "BAM",
        "name_plural": "Bosnia-Herzegovina convertible marks"
    },
    "BDT": {
        "symbol": "Tk",
        "name": "Bangladeshi Taka",
        "symbol_native": "৳",
        "decimal_digits": 2,
        "rounding": 0,
        "code": "BDT",
        "name_plural": "Bangladeshi takas"
    },
    "BGN": {
        "symbol": "BGN",
        "name": "Bulgarian Lev",
        "symbol_native": "лв.",
        "decimal_digits": 2,
        "rounding": 0,
        "code": "BGN",
        "name_plural": "Bulgarian leva"
    },
    "BHD": {
        "symbol": "BD",
        "name": "Bahraini Dinar",
        "symbol_native": "د.ب.‏",
        "decimal_digits": 3,
        "rounding": 0,
        "code": "BHD",
        "name_plural": "Bahraini dinars"
    },
    "BIF": {
        "symbol": "FBu",
        "name": "Burundian Franc",
        "symbol_native": "FBu",
        "decimal_digits": 0,
        "rounding": 0,
        "code": "BIF",
        "name_plural": "Burundian francs"
    },
    "BND": {
        "symbol": "BN$",
        "name": "Brunei Dollar",
        "symbol_native": "$",
        "decimal_digits": 2,
        "rounding": 0,
        "code": "BND",
        "name_plural": "Brunei dollars"
    },
    "BOB": {
        "symbol": "Bs",
        "name": "Bolivian Boliviano",
        "symbol_native": "Bs",
        "decimal_digits": 2,
        "rounding": 0,
        "code": "BOB",
        "name_plural": "Bolivian bolivianos"
    },
    "BRL": {
        "symbol": "R$",
        "name": "Brazilian Real",
        "symbol_native": "R$",
        "decimal_digits": 2,
        "rounding": 0,
        "code": "BRL",
        "name_plural": "Brazilian reals"
    },
    "BWP": {
        "symbol": "BWP",
        "name": "Botswanan Pula",
        "symbol_native": "P",
        "decimal_digits": 2,
        "rounding": 0,
        "code": "BWP",
        "name_plural": "Botswanan pulas"
    },
    "BYR": {
        "symbol": "BYR",
        "name": "Belarusian Ruble",
        "symbol_native": "BYR",
        "decimal_digits": 0,
        "rounding": 0,
        "code": "BYR",
        "name_plural": "Belarusian rubles"
    },
    "BZD": {
        "symbol": "BZ$",
        "name": "Belize Dollar",
        "symbol_native": "$",
        "decimal_digits": 2,
        "rounding": 0,
        "code": "BZD",
        "name_plural": "Belize dollars"
    },
    "CDF": {
        "symbol": "CDF",
        "name": "Congolese Franc",
        "symbol_native": "FrCD",
        "decimal_digits": 2,
        "rounding": 0,
        "code": "CDF",
        "name_plural": "Congolese francs"
    },
    "CHF": {
        "symbol": "CHF",
        "name": "Swiss Franc",
        "symbol_native": "CHF",
        "decimal_digits": 2,
        "rounding": 0.05,
        "code": "CHF",
        "name_plural": "Swiss francs"
    },
    "CLP": {
        "symbol": "CL$",
        "name": "Chilean Peso",
        "symbol_native": "$",
        "decimal_digits": 0,
        "rounding": 0,
        "code": "CLP",
        "name_plural": "Chilean pesos"
    },
    "CNY": {
        "symbol": "CN¥",
        "name": "Chinese Yuan",
        "symbol_native": "CN¥",
        "decimal_digits": 2,
        "rounding": 0,
        "code": "CNY",
        "name_plural": "Chinese yuan"
    },
    "COP": {
        "symbol": "CO$",
        "name": "Colombian Peso",
        "symbol_native": "$",
        "decimal_digits": 0,
        "rounding": 0,
        "code": "COP",
        "name_plural": "Colombian pesos"
    },
    "CRC": {
        "symbol": "₡",
        "name": "Costa Rican Colón",
        "symbol_native": "₡",
        "decimal_digits": 0,
        "rounding": 0,
        "code": "CRC",
        "name_plural": "Costa Rican colóns"
    },
    "CVE": {
        "symbol": "CV$",
        "name": "Cape Verdean Escudo",
        "symbol_native": "CV$",
        "decimal_digits": 2,
        "rounding": 0,
        "code": "CVE",
        "name_plural": "Cape Verdean escudos"
    },
    "CZK": {
        "symbol": "Kč",
        "name": "Czech Republic Koruna",
        "symbol_native": "Kč",
        "decimal_digits": 2,
        "rounding": 0,
        "code": "CZK",
        "name_plural": "Czech Republic korunas"
    },
    "DJF": {
        "symbol": "Fdj",
        "name": "Djiboutian Franc",
        "symbol_native": "Fdj",
        "decimal_digits": 0,
        "rounding": 0,
        "code": "DJF",
        "name_plural": "Djiboutian francs"
    },
    "DKK": {
        "symbol": "Dkr",
        "name": "Danish Krone",
        "symbol_native": "kr",
        "decimal_digits": 2,
        "rounding": 0,
        "code": "DKK",
        "name_plural": "Danish kroner"
    },
    "DOP": {
        "symbol": "RD$",
        "name": "Dominican Peso",
        "symbol_native": "RD$",
        "decimal_digits": 2,
        "rounding": 0,
        "code": "DOP",
        "name_plural": "Dominican pesos"
    },
    "DZD": {
        "symbol": "DA",
        "name": "Algerian Dinar",
        "symbol_native": "د.ج.‏",
        "decimal_digits": 2,
        "rounding": 0,
        "code": "DZD",
        "name_plural": "Algerian dinars"
    },
    "EEK": {
        "symbol": "Ekr",
        "name": "Estonian Kroon",
        "symbol_native": "kr",
        "decimal_digits": 2,
        "rounding": 0,
        "code": "EEK",
        "name_plural": "Estonian kroons"
    },
    "EGP": {
        "symbol": "EGP",
        "name": "Egyptian Pound",
        "symbol_native": "ج.م.‏",
        "decimal_digits": 2,
        "rounding": 0,
        "code": "EGP",
        "name_plural": "Egyptian pounds"
    },
    "ERN": {
        "symbol": "Nfk",
        "name": "Eritrean Nakfa",
        "symbol_native": "Nfk",
        "decimal_digits": 2,
        "rounding": 0,
        "code": "ERN",
        "name_plural": "Eritrean nakfas"
    },
    "ETB": {
        "symbol": "Br",
        "name": "Ethiopian Birr",
        "symbol_native": "Br",
        "decimal_digits": 2,
        "rounding": 0,
        "code": "ETB",
        "name_plural": "Ethiopian birrs"
    },
    "GBP": {
        "symbol": "£",
        "name": "British Pound Sterling",
        "symbol_native": "£",
        "decimal_digits": 2,
        "rounding": 0,
        "code": "GBP",
        "name_plural": "British pounds sterling"
    },
    "GEL": {
        "symbol": "GEL",
        "name": "Georgian Lari",
        "symbol_native": "GEL",
        "decimal_digits": 2,
        "rounding": 0,
        "code": "GEL",
        "name_plural": "Georgian laris"
    },
    "GHS": {
        "symbol": "GH₵",
        "name": "Ghanaian Cedi",
        "symbol_native": "GH₵",
        "decimal_digits": 2,
        "rounding": 0,
        "code": "GHS",
        "name_plural": "Ghanaian cedis"
    },
    "GNF": {
        "symbol": "FG",
        "name": "Guinean Franc",
        "symbol_native": "FG",
        "decimal_digits": 0,
        "rounding": 0,
        "code": "GNF",
        "name_plural": "Guinean francs"
    },
    "GTQ": {
        "symbol": "GTQ",
        "name": "Guatemalan Quetzal",
        "symbol_native": "Q",
        "decimal_digits": 2,
        "rounding": 0,
        "code": "GTQ",
        "name_plural": "Guatemalan quetzals"
    },
    "HKD": {
        "symbol": "HK$",
        "name": "Hong Kong Dollar",
        "symbol_native": "$",
        "decimal_digits": 2,
        "rounding": 0,
        "code": "HKD",
        "name_plural": "Hong Kong dollars"
    },
    "HNL": {
        "symbol": "HNL",
        "name": "Honduran Lempira",
        "symbol_native": "L",
        "decimal_digits": 2,
        "rounding": 0,
        "code": "HNL",
        "name_plural": "Honduran lempiras"
    },
    "HRK": {
        "symbol": "kn",
        "name": "Croatian Kuna",
        "symbol_native": "kn",
        "decimal_digits": 2,
        "rounding": 0,
        "code": "HRK",
        "name_plural": "Croatian kunas"
    },
    "HUF": {
        "symbol": "Ft",
        "name": "Hungarian Forint",
        "symbol_native": "Ft",
        "decimal_digits": 0,
        "rounding": 0,
        "code": "HUF",
        "name_plural": "Hungarian forints"
    },
    "IDR": {
        "symbol": "Rp",
        "name": "Indonesian Rupiah",
        "symbol_native": "Rp",
        "decimal_digits": 0,
        "rounding": 0,
        "code": "IDR",
        "name_plural": "Indonesian rupiahs"
    },
    "ILS": {
        "symbol": "₪",
        "name": "Israeli New Sheqel",
        "symbol_native": "₪",
        "decimal_digits": 2,
        "rounding": 0,
        "code": "ILS",
        "name_plural": "Israeli new sheqels"
    },
    "INR": {
        "symbol": "Rs",
        "name": "Indian Rupee",
        "symbol_native": "টকা",
        "decimal_digits": 2,
        "rounding": 0,
        "code": "INR",
        "name_plural": "Indian rupees"
    },
    "IQD": {
        "symbol": "IQD",
        "name": "Iraqi Dinar",
        "symbol_native": "د.ع.‏",
        "decimal_digits": 0,
        "rounding": 0,
        "code": "IQD",
        "name_plural": "Iraqi dinars"
    },
    "IRR": {
        "symbol": "IRR",
        "name": "Iranian Rial",
        "symbol_native": "﷼",
        "decimal_digits": 0,
        "rounding": 0,
        "code": "IRR",
        "name_plural": "Iranian rials"
    },
    "ISK": {
        "symbol": "Ikr",
        "name": "Icelandic Króna",
        "symbol_native": "kr",
        "decimal_digits": 0,
        "rounding": 0,
        "code": "ISK",
        "name_plural": "Icelandic krónur"
    },
    "JMD": {
        "symbol": "J$",
        "name": "Jamaican Dollar",
        "symbol_native": "$",
        "decimal_digits": 2,
        "rounding": 0,
        "code": "JMD",
        "name_plural": "Jamaican dollars"
    },
    "JOD": {
        "symbol": "JD",
        "name": "Jordanian Dinar",
        "symbol_native": "د.أ.‏",
        "decimal_digits": 3,
        "rounding": 0,
        "code": "JOD",
        "name_plural": "Jordanian dinars"
    },
    "JPY": {
        "symbol": "¥",
        "name": "Japanese Yen",
        "symbol_native": "￥",
        "decimal_digits": 0,
        "rounding": 0,
        "code": "JPY",
        "name_plural": "Japanese yen"
    },
    "KES": {
        "symbol": "Ksh",
        "name": "Kenyan Shilling",
        "symbol_native": "Ksh",
        "decimal_digits": 2,
        "rounding": 0,
        "code": "KES",
        "name_plural": "Kenyan shillings"
    },
    "KHR": {
        "symbol": "KHR",
        "name": "Cambodian Riel",
        "symbol_native": "៛",
        "decimal_digits": 2,
        "rounding": 0,
        "code": "KHR",
        "name_plural": "Cambodian riels"
    },
    "KMF": {
        "symbol": "CF",
        "name": "Comorian Franc",
        "symbol_native": "FC",
        "decimal_digits": 0,
        "rounding": 0,
        "code": "KMF",
        "name_plural": "Comorian francs"
    },
    "KRW": {
        "symbol": "₩",
        "name": "South Korean Won",
        "symbol_native": "₩",
        "decimal_digits": 0,
        "rounding": 0,
        "code": "KRW",
        "name_plural": "South Korean won"
    },
    "KWD": {
        "symbol": "KD",
        "name": "Kuwaiti Dinar",
        "symbol_native": "د.ك.‏",
        "decimal_digits": 3,
        "rounding": 0,
        "code": "KWD",
        "name_plural": "Kuwaiti dinars"
    },
    "KZT": {
        "symbol": "KZT",
        "name": "Kazakhstani Tenge",
        "symbol_native": "тңг.",
        "decimal_digits": 2,
        "rounding": 0,
        "code": "KZT",
        "name_plural": "Kazakhstani tenges"
    },
    "LBP": {
        "symbol": "LB£",
        "name": "Lebanese Pound",
        "symbol_native": "ل.ل.‏",
        "decimal_digits": 0,
        "rounding": 0,
        "code": "LBP",
        "name_plural": "Lebanese pounds"
    },
    "LKR": {
        "symbol": "SLRs",
        "name": "Sri Lankan Rupee",
        "symbol_native": "SL Re",
        "decimal_digits": 2,
        "rounding": 0,
        "code": "LKR",
        "name_plural": "Sri Lankan rupees"
    },
    "LTL": {
        "symbol": "Lt",
        "name": "Lithuanian Litas",
        "symbol_native": "Lt",
        "decimal_digits": 2,
        "rounding": 0,
        "code": "LTL",
        "name_plural": "Lithuanian litai"
    },
    "LVL": {
        "symbol": "Ls",
        "name": "Latvian Lats",
        "symbol_native": "Ls",
        "decimal_digits": 2,
        "rounding": 0,
        "code": "LVL",
        "name_plural": "Latvian lati"
    },
    "LYD": {
        "symbol": "LD",
        "name": "Libyan Dinar",
        "symbol_native": "د.ل.‏",
        "decimal_digits": 3,
        "rounding": 0,
        "code": "LYD",
        "name_plural": "Libyan dinars"
    },
    "MAD": {
        "symbol": "MAD",
        "name": "Moroccan Dirham",
        "symbol_native": "د.م.‏",
        "decimal_digits": 2,
        "rounding": 0,
        "code": "MAD",
        "name_plural": "Moroccan dirhams"
    },
    "MDL": {
        "symbol": "MDL",
        "name": "Moldovan Leu",
        "symbol_native": "MDL",
        "decimal_digits": 2,
        "rounding": 0,
        "code": "MDL",
        "name_plural": "Moldovan lei"
    },
    "MGA": {
        "symbol": "MGA",
        "name": "Malagasy Ariary",
        "symbol_native": "MGA",
        "decimal_digits": 0,
        "rounding": 0,
        "code": "MGA",
        "name_plural": "Malagasy Ariaries"
    },
    "MKD": {
        "symbol": "MKD",
        "name": "Macedonian Denar",
        "symbol_native": "MKD",
        "decimal_digits": 2,
        "rounding": 0,
        "code": "MKD",
        "name_plural": "Macedonian denari"
    },
    "MMK": {
        "symbol": "MMK",
        "name": "Myanma Kyat",
        "symbol_native": "K",
        "decimal_digits": 0,
        "rounding": 0,
        "code": "MMK",
        "name_plural": "Myanma kyats"
    },
    "MOP": {
        "symbol": "MOP$",
        "name": "Macanese Pataca",
        "symbol_native": "MOP$",
        "decimal_digits": 2,
        "rounding": 0,
        "code": "MOP",
        "name_plural": "Macanese patacas"
    },
    "MUR": {
        "symbol": "MURs",
        "name": "Mauritian Rupee",
        "symbol_native": "MURs",
        "decimal_digits": 0,
        "rounding": 0,
        "code": "MUR",
        "name_plural": "Mauritian rupees"
    },
    "MXN": {
        "symbol": "MX$",
        "name": "Mexican Peso",
        "symbol_native": "$",
        "decimal_digits": 2,
        "rounding": 0,
        "code": "MXN",
        "name_plural": "Mexican pesos"
    },
    "MYR": {
        "symbol": "RM",
        "name": "Malaysian Ringgit",
        "symbol_native": "RM",
        "decimal_digits": 2,
        "rounding": 0,
        "code": "MYR",
        "name_plural": "Malaysian ringgits"
    },
    "MZN": {
        "symbol": "MTn",
        "name": "Mozambican Metical",
        "symbol_native": "MTn",
        "decimal_digits": 2,
        "rounding": 0,
        "code": "MZN",
        "name_plural": "Mozambican meticals"
    },
    "NAD": {
        "symbol": "N$",
        "name": "Namibian Dollar",
        "symbol_native": "N$",
        "decimal_digits": 2,
        "rounding": 0,
        "code": "NAD",
        "name_plural": "Namibian dollars"
    },
    "NGN": {
        "symbol": "₦",
        "name": "Nigerian Naira",
        "symbol_native": "₦",
        "decimal_digits": 2,
        "rounding": 0,
        "code": "NGN",
        "name_plural": "Nigerian nairas"
    },
    "NIO": {
        "symbol": "C$",
        "name": "Nicaraguan Córdoba",
        "symbol_native": "C$",
        "decimal_digits": 2,
        "rounding": 0,
        "code": "NIO",
        "name_plural": "Nicaraguan córdobas"
    },
    "NOK": {
        "symbol": "Nkr",
        "name": "Norwegian Krone",
        "symbol_native": "kr",
        "decimal_digits": 2,
        "rounding": 0,
        "code": "NOK",
        "name_plural": "Norwegian kroner"
    },
    "NPR": {
        "symbol": "NPRs",
        "name": "Nepalese Rupee",
        "symbol_native": "नेरू",
        "decimal_digits": 2,
        "rounding": 0,
        "code": "NPR",
        "name_plural": "Nepalese rupees"
    },
    "NZD": {
        "symbol": "NZ$",
        "name": "New Zealand Dollar",
        "symbol_native": "$",
        "decimal_digits": 2,
        "rounding": 0,
        "code": "NZD",
        "name_plural": "New Zealand dollars"
    },
    "OMR": {
        "symbol": "OMR",
        "name": "Omani Rial",
        "symbol_native": "ر.ع.‏",
        "decimal_digits": 3,
        "rounding": 0,
        "code": "OMR",
        "name_plural": "Omani rials"
    },
    "PAB": {
        "symbol": "B/.",
        "name": "Panamanian Balboa",
        "symbol_native": "B/.",
        "decimal_digits": 2,
        "rounding": 0,
        "code": "PAB",
        "name_plural": "Panamanian balboas"
    },
    "PEN": {
        "symbol": "S/.",
        "name": "Peruvian Nuevo Sol",
        "symbol_native": "S/.",
        "decimal_digits": 2,
        "rounding": 0,
        "code": "PEN",
        "name_plural": "Peruvian nuevos soles"
    },
    "PHP": {
        "symbol": "₱",
        "name": "Philippine Peso",
        "symbol_native": "₱",
        "decimal_digits": 2,
        "rounding": 0,
        "code": "PHP",
        "name_plural": "Philippine pesos"
    },
    "PKR": {
        "symbol": "PKRs",
        "name": "Pakistani Rupee",
        "symbol_native": "₨",
        "decimal_digits": 0,
        "rounding": 0,
        "code": "PKR",
        "name_plural": "Pakistani rupees"
    },
    "PLN": {
        "symbol": "zł",
        "name": "Polish Zloty",
        "symbol_native": "zł",
        "decimal_digits": 2,
        "rounding": 0,
        "code": "PLN",
        "name_plural": "Polish zlotys"
    },
    "PYG": {
        "symbol": "₲",
        "name": "Paraguayan Guarani",
        "symbol_native": "₲",
        "decimal_digits": 0,
        "rounding": 0,
        "code": "PYG",
        "name_plural": "Paraguayan guaranis"
    },
    "QAR": {
        "symbol": "QR",
        "name": "Qatari Rial",
        "symbol_native": "ر.ق.‏",
        "decimal_digits": 2,
        "rounding": 0,
        "code": "QAR",
        "name_plural": "Qatari rials"
    },
    "RON": {
        "symbol": "RON",
        "name": "Romanian Leu",
        "symbol_native": "RON",
        "decimal_digits": 2,
        "rounding": 0,
        "code": "RON",
        "name_plural": "Romanian lei"
    },
    "RSD": {
        "symbol": "din.",
        "name": "Serbian Dinar",
        "symbol_native": "дин.",
        "decimal_digits": 0,
        "rounding": 0,
        "code": "RSD",
        "name_plural": "Serbian dinars"
    },
    "RUB": {
        "symbol": "RUB",
        "name": "Russian Ruble",
        "symbol_native": "руб.",
        "decimal_digits": 2,
        "rounding": 0,
        "code": "RUB",
        "name_plural": "Russian rubles"
    },
    "RWF": {
        "symbol": "RWF",
        "name": "Rwandan Franc",
        "symbol_native": "FR",
        "decimal_digits": 0,
        "rounding": 0,
        "code": "RWF",
        "name_plural": "Rwandan francs"
    },
    "SAR": {
        "symbol": "SR",
        "name": "Saudi Riyal",
        "symbol_native": "ر.س.‏",
        "decimal_digits": 2,
        "rounding": 0,
        "code": "SAR",
        "name_plural": "Saudi riyals"
    },
    "SDG": {
        "symbol": "SDG",
        "name": "Sudanese Pound",
        "symbol_native": "SDG",
        "decimal_digits": 2,
        "rounding": 0,
        "code": "SDG",
        "name_plural": "Sudanese pounds"
    },
    "SEK": {
        "symbol": "Skr",
        "name": "Swedish Krona",
        "symbol_native": "kr",
        "decimal_digits": 2,
        "rounding": 0,
        "code": "SEK",
        "name_plural": "Swedish kronor"
    },
    "SGD": {
        "symbol": "S$",
        "name": "Singapore Dollar",
        "symbol_native": "$",
        "decimal_digits": 2,
        "rounding": 0,
        "code": "SGD",
        "name_plural": "Singapore dollars"
    },
    "SOS": {
        "symbol": "Ssh",
        "name": "Somali Shilling",
        "symbol_native": "Ssh",
        "decimal_digits": 0,
        "rounding": 0,
        "code": "SOS",
        "name_plural": "Somali shillings"
    },
    "SYP": {
        "symbol": "SY£",
        "name": "Syrian Pound",
        "symbol_native": "ل.س.‏",
        "decimal_digits": 0,
        "rounding": 0,
        "code": "SYP",
        "name_plural": "Syrian pounds"
    },
    "THB": {
        "symbol": "฿",
        "name": "Thai Baht",
        "symbol_native": "฿",
        "decimal_digits": 2,
        "rounding": 0,
        "code": "THB",
        "name_plural": "Thai baht"
    },
    "TND": {
        "symbol": "DT",
        "name": "Tunisian Dinar",
        "symbol_native": "د.ت.‏",
        "decimal_digits": 3,
        "rounding": 0,
        "code": "TND",
        "name_plural": "Tunisian dinars"
    },
    "TOP": {
        "symbol": "T$",
        "name": "Tongan Paʻanga",
        "symbol_native": "T$",
        "decimal_digits": 2,
        "rounding": 0,
        "code": "TOP",
        "name_plural": "Tongan paʻanga"
    },
    "TRY": {
        "symbol": "TL",
        "name": "Turkish Lira",
        "symbol_native": "TL",
        "decimal_digits": 2,
        "rounding": 0,
        "code": "TRY",
        "name_plural": "Turkish Lira"
    },
    "TTD": {
        "symbol": "TT$",
        "name": "Trinidad and Tobago Dollar",
        "symbol_native": "$",
        "decimal_digits": 2,
        "rounding": 0,
        "code": "TTD",
        "name_plural": "Trinidad and Tobago dollars"
    },
    "TWD": {
        "symbol": "NT$",
        "name": "New Taiwan Dollar",
        "symbol_native": "NT$",
        "decimal_digits": 2,
        "rounding": 0,
        "code": "TWD",
        "name_plural": "New Taiwan dollars"
    },
    "TZS": {
        "symbol": "TSh",
        "name": "Tanzanian Shilling",
        "symbol_native": "TSh",
        "decimal_digits": 0,
        "rounding": 0,
        "code": "TZS",
        "name_plural": "Tanzanian shillings"
    },
    "UAH": {
        "symbol": "₴",
        "name": "Ukrainian Hryvnia",
        "symbol_native": "₴",
        "decimal_digits": 2,
        "rounding": 0,
        "code": "UAH",
        "name_plural": "Ukrainian hryvnias"
    },
    "UGX": {
        "symbol": "USh",
        "name": "Ugandan Shilling",
        "symbol_native": "USh",
        "decimal_digits": 0,
        "rounding": 0,
        "code": "UGX",
        "name_plural": "Ugandan shillings"
    },
    "UYU": {
        "symbol": "$U",
        "name": "Uruguayan Peso",
        "symbol_native": "$",
        "decimal_digits": 2,
        "rounding": 0,
        "code": "UYU",
        "name_plural": "Uruguayan pesos"
    },
    "UZS": {
        "symbol": "UZS",
        "name": "Uzbekistan Som",
        "symbol_native": "UZS",
        "decimal_digits": 0,
        "rounding": 0,
        "code": "UZS",
        "name_plural": "Uzbekistan som"
    },
    "VEF": {
        "symbol": "Bs.F.",
        "name": "Venezuelan Bolívar",
        "symbol_native": "Bs.F.",
        "decimal_digits": 2,
        "rounding": 0,
        "code": "VEF",
        "name_plural": "Venezuelan bolívars"
    },
    "VND": {
        "symbol": "₫",
        "name": "Vietnamese Dong",
        "symbol_native": "₫",
        "decimal_digits": 0,
        "rounding": 0,
        "code": "VND",
        "name_plural": "Vietnamese dong"
    },
    "XAF": {
        "symbol": "FCFA",
        "name": "CFA Franc BEAC",
        "symbol_native": "FCFA",
        "decimal_digits": 0,
        "rounding": 0,
        "code": "XAF",
        "name_plural": "CFA francs BEAC"
    },
    "XOF": {
        "symbol": "CFA",
        "name": "CFA Franc BCEAO",
        "symbol_native": "CFA",
        "decimal_digits": 0,
        "rounding": 0,
        "code": "XOF",
        "name_plural": "CFA francs BCEAO"
    },
    "YER": {
        "symbol": "YR",
        "name": "Yemeni Rial",
        "symbol_native": "ر.ي.‏",
        "decimal_digits": 0,
        "rounding": 0,
        "code": "YER",
        "name_plural": "Yemeni rials"
    },
    "ZAR": {
        "symbol": "R",
        "name": "South African Rand",
        "symbol_native": "R",
        "decimal_digits": 2,
        "rounding": 0,
        "code": "ZAR",
        "name_plural": "South African rand"
    },
    "ZMK": {
        "symbol": "ZK",
        "name": "Zambian Kwacha",
        "symbol_native": "ZK",
        "decimal_digits": 0,
        "rounding": 0,
        "code": "ZMK",
        "name_plural": "Zambian kwachas"
    }
}
emailmessage = 'Please add a correct email format!'


# <___ Custom widgets ___>

def select_multi_checkbox(field, ul_class='', **kwargs):
    kwargs.setdefault('type', 'checkbox')
    field_id = kwargs.pop('id', field.id)


    # html = [u'<input %s>' % widgets.html_params(id="skill_btn", type="button")]
    # html.append(u'<div class="checkbox" style="display: none">')

    html = [u'<a class="btn btn-primary collapsed" data-toggle="collapse" href="#skillbox" role="button" aria-expanded="false" aria-controls="skillbox">Show Skillset</a>']
    html.append(u'<div class="checkbox collapse" id="skillbox">')
    # html = [u'<div class="checkbox">']
    html.append(u'<ul %s>' % widgets.html_params(id=field_id, class_=ul_class, style="padding-left:20px;"))
    for value, label, checked in field.iter_choices():
        choice_id = u'%s-%s' % (field_id, value)
        options = dict(kwargs, name=field.name, value=value, id=choice_id, onchange='check("'+choice_id+'")')
        # radiooptions = dict(kwargs, id="ra"+choice_id, style="display: none")
        radiooptions = dict(kwargs, id="ra"+choice_id)
        if checked:
            options['checked'] = 'checked'
        html.append(u'<li><input %s/> ' % widgets.html_params(**options))
        html.append(u'<label for="%s">%s</label></li>' % (field_id, label))

        html.append(u'<div %s>' % widgets.html_params(**radiooptions))

        html.append(u'<label class="radio-inline">')
        html.append(u'<input type="radio" name="%s" id="low" value="low" checked>low' % ("ra"+choice_id))
        html.append(u'</label>')

        html.append(u'<label class="radio-inline">')
        html.append(u'<input type="radio" name="%s" id="medium" value="medium" checked>medium' % ("ra"+choice_id))
        html.append(u'</label>')

        html.append(u'<label class="radio-inline">')
        html.append(u'<input type="radio" name="%s" id="high" value="high" checked>high' % ("ra"+choice_id))
        html.append(u'</label>')


        html.append(u'</div>')
        html.append(u'<hr style="margin: 10px 0px">')
    html.append(u'</ul>')

    html.append(u'</div>')

    return u''.join(html)


def files_with_text(field, ul_class='', **kwargs):
    kwargs.setdefault('type', 'file')
    field_id = kwargs.pop('id', field.id)

    html = [u'<div %s>' % widgets.html_params(class_=field.name+'container')]

    html.append(u'<div>')
    html.append(u'<input %s>' % widgets.html_params(type='text', name=field.name + '-0', class_='form-control inputfile'))
    html.append(u'<button %s>' % widgets.html_params(type='button', class_="btn btn-default btn-sm add_form_field", id=field.name + '-btn-0', style="float: right;", onclick='addFormField("'+field.name+'","0")'))
    html.append(u'<span class="glyphicon glyphicon-plus"></span>')
    html.append(u'</button>')
    html.append(u'</div>')

    html.append(u'<input %s multiple>' % widgets.html_params(type='file', name=field.name + '-file-0', id=field.name + '-file-0', class_='fileinput', onchange='addFileName("'+field.name+'","0")'))
    html.append(u'<div %s>' % widgets.html_params(class_=field.name + '-filenames-0'))
    html.append(u'</div>')

    html.append(u'</div>')

    return u''.join(html)


def radio_with_text(field, ul_class='', **kwargs):
    kwargs.setdefault('type', 'radio')
    field_id = kwargs.pop('id', field.id)

    # html = [u'<ul %s>' % widgets.html_params(id=field_id, class_=ul_class, style="list-style-type: none;")]
    html = [u'<ul %s>' % widgets.html_params(id=field_id, class_=ul_class)]
    for value, label, checked in field.iter_choices():
        choice_id = u'%s-%s' % (field_id, value)
        options = dict(kwargs, name=field.name, value=value, id=choice_id)
        # options = dict(kwargs, name=field.name, value=value, id=choice_id, onchange='checkRadio("'+choice_id+'", "'+field.name+'")')
        # radiooptions = dict(kwargs, id="ra"+choice_id, style="display: none")
        radiooptions = dict(kwargs, id="ra"+choice_id)
        if checked:
            options['checked'] = 'checked'
        html.append(u'<li><input %s/> ' % widgets.html_params(**options))
        html.append(u'<label for="%s">%s</label></li>' % (field_id, label))

    # html.append(u'<input type="text" id="%s" name="%s" style="display: none"/>'  % (field.name+"-othertext", field.name+"-othertext"))
    html.append(u'<input type="text" id="%s" name="%s" class="form-control"/>'  % (field.name+"-othertext", field.name+"-othertext"))
    html.append(u'</ul>')

    return u''.join(html)


def text_with_select(field, ul_class='', **kwargs):
    currchoices = [str(currencies[x]['code']) for x in currencies.keys()]

    kwargs.setdefault('type', 'option')
    field_id = kwargs.pop('id', field.id)

    html = [u'<div %s>' % widgets.html_params(class_='col-sm-9', style="padding-left:0px;")]

    html.append(u'<input %s>' % widgets.html_params(type='text', id=field.name, name=field.name, class_='form-control'))

    html.append(u'</div>')

    html.append(u'<div %s>' % widgets.html_params(class_='col-sm-3'))

    html.append(u'<select %s>' % widgets.html_params(id=field.name + "-select", name=field.name + "-select", class_='form-control'))
    # for value, label, checked in field.iter_choices():
    for value in currchoices:
        # choice_id = u'%s-%s' % (field_id, value)
        # options = dict(kwargs, name=field.name, value=value, id=choice_id)
        html.append(u'<option %s/>%s</option>' % (widgets.html_params(value=value), value))
    html.append(u'</select>')

    html.append(u'</div>')
    html.append(u'<div class="form-control"></div>')

    return u''.join(html)


# <___ Custom form fields ___>

class MultiFileField(FileField):

    def pre_validate(self, form):
        """per_validation is disabled"""


class MultiCheckboxFieldWithRate(SelectMultipleField):

    def pre_validate(self, form):
        """per_validation is disabled"""


class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()

    def pre_validate(self, form):
        """per_validation is disabled"""


# <___ Forms ___>
def chk_phone(form, field):
    pattern = r'^[0-9-+]*$'
    if re.match(pattern, field.data) is None:
        raise ValidationError("Please use only numbers and '+-' characters!")

class New_PM_Customer(DynamicForm):
    company_name = StringField('Company Name', validators=[DataRequired()], widget=BS3TextFieldWidget())
    company_address = StringField('Company Street Address', validators=[DataRequired()], widget=BS3TextFieldWidget())
    company_postal_nr = StringField('Company Postal Code', validators=[DataRequired()], widget=BS3TextFieldWidget())
    company_city = StringField('Company City', validators=[DataRequired()], widget=BS3TextFieldWidget())
    company_country = StringField('Company Country', validators=[DataRequired()], widget=BS3TextFieldWidget())
    company_phone = StringField('Company Telephone', validators=[DataRequired(), chk_phone], widget=BS3TextFieldWidget())
    company_fax = StringField('Company Fax', widget=BS3TextFieldWidget())
    company_email = StringField('Company Email', validators=[DataRequired(message='Please add a Company Email!'), Email(message=emailmessage)], widget=BS3TextFieldWidget())
    company_website = StringField('Company Website', widget=BS3TextFieldWidget())
    introduction = TextAreaField('Short Introduction', validators=[DataRequired()])
    parent_company = StringField('Parent Company', widget=BS3TextFieldWidget())
    subsidiaries = TextAreaField('Subsidiaries')
    associates = TextAreaField('Associates')
    international_offices = TextAreaField('International Offices', validators=[DataRequired()])
    type_of_business = RadioField('Type of Business', choices=[("limited", "Corporate/ Limited"), ("partner", "Partnership"), ("other", "Other")], validators=[DataRequired()], widget=radio_with_text)
    nature_of_business = RadioField('Nature of Business', choices=[("limited", "Corporate/ Limited"), ("partner", "Partnership"), ("other", "Other")], validators=[DataRequired()], widget=radio_with_text)
    year_of_establishment = IntegerField('Year Established', validators=[DataRequired()], widget=BS3TextFieldWidget())
    employees = IntegerField('Number of Full-time Employees', validators=[DataRequired()], widget=BS3TextFieldWidget())
    licence_number = StringField('Licence Number', validators=[DataRequired()], widget=BS3TextFieldWidget())
    vat_tax_id = StringField('VAT No./Tax I.D', validators=[DataRequired()], widget=BS3TextFieldWidget())
    working_languages = MultiCheckboxField('Working Languages', choices=[("en", "en"), ("ge", "ge"), ("hu", "hu"), ("fr", "fr")], validators=[DataRequired()])
    compfiles = FileField(u'Company Attachments', widget=files_with_text)

    mailing_address = StringField('Mailing Street Address', validators=[DataRequired()], widget=BS3TextFieldWidget())
    mailing_postal_nr = StringField('Mailing Postal Code', validators=[DataRequired()], widget=BS3TextFieldWidget())
    mailing_city = StringField('Mailing City', validators=[DataRequired()], widget=BS3TextFieldWidget())
    mailing_country = StringField('Mailing Country', validators=[DataRequired()], widget=BS3TextFieldWidget())

    bank_name = StringField('Bank Name', validators=[DataRequired()], widget=BS3TextFieldWidget())
    branch_name = StringField('Branch Name', validators=[DataRequired()], widget=BS3TextFieldWidget())
    branch_address = StringField('Branch Street Address', validators=[DataRequired()], widget=BS3TextFieldWidget())
    branch_postal_nr = StringField('Branch Postal Code', validators=[DataRequired()], widget=BS3TextFieldWidget())
    branch_city = StringField('Branch City', validators=[DataRequired()], widget=BS3TextFieldWidget())
    branch_country = StringField('Branch Country', validators=[DataRequired()], widget=BS3TextFieldWidget())
    branch_phone = StringField('Branch Telephone', validators=[DataRequired(), chk_phone], widget=BS3TextFieldWidget())
    branch_fax = StringField('Company Fax', widget=BS3TextFieldWidget())
    bank_account_number = StringField('Bank Account Number', validators=[DataRequired()], widget=BS3TextFieldWidget())
    account_currency = StringField('Account currency', validators=[DataRequired()], widget=BS3TextFieldWidget())
    iban = StringField('International Bank Account Number (IBAN)', validators=[DataRequired()], widget=BS3TextFieldWidget())
    bic = StringField('Swift/Bank Identifier Code (BIC)', validators=[DataRequired()], widget=BS3TextFieldWidget())
    routing_bank_details = StringField('Routing Bank details', validators=[DataRequired()], widget=BS3TextFieldWidget())
    annual_value_of_total_sales = StringField('Annual Value of Total Sales for the last 3 Years', validators=[DataRequired()], widget=BS3TextFieldWidget())
    annual_value_of_export_sales = StringField('Annual Value of Export Sales for the last 3 Years', validators=[DataRequired()], widget=BS3TextFieldWidget())
    audit_reports = FileField("If available, please provide a copy of the company's three latest annual or audited Financial Report.", widget=files_with_text)
    bankruptcy_legal_action = RadioField('Do you have outstanding bankruptcy, judgment or pending legal action that could impair operating as a going concern?', choices=[("yes", "Yes"), ("no", "No")], validators=[DataRequired()])
    bankfiles = FileField(u'Banking Attachments', widget=files_with_text)


class New_PM_Supplier(DynamicForm):
    skilldb = db.session.query(PM_Skillset).all()
    skillchoices = [(x, str(x).capitalize()) for x in skilldb]

    skillset = MultiCheckboxFieldWithRate('Skillset', choices=skillchoices, validators=[DataRequired()],
                                          widget=select_multi_checkbox)

    company_name = StringField('Company Name', validators=[DataRequired()], widget=BS3TextFieldWidget())
    company_address = StringField('Company Street Address', validators=[DataRequired()], widget=BS3TextFieldWidget())
    company_postal_nr = StringField('Company Postal Code', validators=[DataRequired()], widget=BS3TextFieldWidget())
    company_city = StringField('Company City', validators=[DataRequired()], widget=BS3TextFieldWidget())
    company_country = StringField('Company Country', validators=[DataRequired()], widget=BS3TextFieldWidget())
    company_phone = StringField('Company Telephone', validators=[DataRequired(), chk_phone], widget=BS3TextFieldWidget())
    company_fax = StringField('Company Fax', widget=BS3TextFieldWidget())
    company_email = StringField('Company Email', validators=[DataRequired(message='Please add a Company Email!'), Email(message=emailmessage)], widget=BS3TextFieldWidget())
    company_website = StringField('Company Website', widget=BS3TextFieldWidget())
    introduction = TextAreaField('Short Introduction', validators=[DataRequired()])
    parent_company = StringField('Parent Company', widget=BS3TextFieldWidget())
    subsidiaries = TextAreaField('Subsidiaries')
    associates = TextAreaField('Associates')
    international_offices = TextAreaField('International Offices', validators=[DataRequired()])
    type_of_business = RadioField('Type of Business', choices=[("limited", "Corporate/ Limited"), ("partner", "Partnership"), ("other", "Other")], validators=[DataRequired()], widget=radio_with_text)
    nature_of_business = RadioField('Nature of Business', choices=[("limited", "Corporate/ Limited"), ("partner", "Partnership"), ("other", "Other")], validators=[DataRequired()], widget=radio_with_text)
    year_of_establishment = IntegerField('Year Established', validators=[DataRequired()], widget=BS3TextFieldWidget())
    employees = IntegerField('Number of Full-time Employees', validators=[DataRequired()], widget=BS3TextFieldWidget())
    licence_number = StringField('Licence Number', validators=[DataRequired()], widget=BS3TextFieldWidget())
    vat_tax_id = StringField('VAT No./Tax I.D', validators=[DataRequired()], widget=BS3TextFieldWidget())
    working_languages = MultiCheckboxField('Working Languages', choices=[("en", "en"), ("ge", "ge"), ("hu", "hu"), ("fr", "fr")], validators=[DataRequired()])
    compfiles = FileField(u'Company Attachments', widget=files_with_text)

    mailing_address = StringField('Mailing Street Address', validators=[DataRequired()], widget=BS3TextFieldWidget())
    mailing_postal_nr = StringField('Mailing Postal Code', validators=[DataRequired()], widget=BS3TextFieldWidget())
    mailing_city = StringField('Mailing City', validators=[DataRequired()], widget=BS3TextFieldWidget())
    mailing_country = StringField('Mailing Country', validators=[DataRequired()], widget=BS3TextFieldWidget())

    quality_assurance = StringField('Quality Assurance Certification (e.g. ISO 9000 or Equivalent)',
                                    validators=[DataRequired()], widget=BS3TextFieldWidget())
    certification = StringField('Certification(s)', validators=[DataRequired()], widget=BS3TextFieldWidget())
    goods_service = StringField('Goods / Services Offered', validators=[DataRequired()],
                                widget=BS3TextFieldWidget())  # http://www.unhcr.org/479a04502.pdf Sec 3
    goods_list = StringField('Core Goods Offered', validators=[DataRequired()], widget=BS3TextFieldWidget())
    service_list = StringField('Core Services Offered', validators=[DataRequired()], widget=BS3TextFieldWidget())
    servicefiles = FileField(u'Services Attachments', widget=files_with_text)

    bank_name = StringField('Bank Name', validators=[DataRequired()], widget=BS3TextFieldWidget())
    branch_name = StringField('Branch Name', validators=[DataRequired()], widget=BS3TextFieldWidget())
    branch_address = StringField('Branch Street Address', validators=[DataRequired()], widget=BS3TextFieldWidget())
    branch_postal_nr = StringField('Branch Postal Code', validators=[DataRequired()], widget=BS3TextFieldWidget())
    branch_city = StringField('Branch City', validators=[DataRequired()], widget=BS3TextFieldWidget())
    branch_country = StringField('Branch Country', validators=[DataRequired()], widget=BS3TextFieldWidget())
    branch_phone = StringField('Branch Telephone', validators=[DataRequired(), chk_phone], widget=BS3TextFieldWidget())
    branch_fax = StringField('Company Fax', widget=BS3TextFieldWidget())
    bank_account_number = StringField('Bank Account Number', validators=[DataRequired()], widget=BS3TextFieldWidget())
    account_currency = StringField('Account currency', validators=[DataRequired()], widget=BS3TextFieldWidget())
    iban = StringField('International Bank Account Number (IBAN)', validators=[DataRequired()], widget=BS3TextFieldWidget())
    bic = StringField('Swift/Bank Identifier Code (BIC)', validators=[DataRequired()], widget=BS3TextFieldWidget())
    routing_bank_details = StringField('Routing Bank details', validators=[DataRequired()], widget=BS3TextFieldWidget())
    annual_value_of_total_sales = StringField('Annual Value of Total Sales for the last 3 Years', validators=[DataRequired()], widget=BS3TextFieldWidget())
    annual_value_of_export_sales = StringField('Annual Value of Export Sales for the last 3 Years', validators=[DataRequired()], widget=BS3TextFieldWidget())
    audit_reports = FileField("If available, please provide a copy of the company's three latest annual or audited Financial Report.", widget=files_with_text)
    bankruptcy_legal_action = RadioField('Do you have outstanding bankruptcy, judgment or pending legal action that could impair operating as a going concern?', choices=[("yes", "Yes"), ("no", "No")], validators=[DataRequired()])
    bankfiles = FileField(u'Banking Attachments', widget=files_with_text)


def unique(form, field):
    skilldb = db.session.query(PM_Skillset).all()
    skills = [str(x) for x in skilldb]
    if field.data.lower() in skills:
        raise ValidationError('"{0}" is already in the database'.format(field.data.lower()))

class Add_Skill(DynamicForm):
    skill = StringField('Skill', validators=[DataRequired(), unique], widget=BS3TextFieldWidget())


def chk_date_today(form, field):
    if field.data < datetime.date.today():
        raise ValidationError('"{0}" is an earlier date! Please add a correct date!'.format(field.data))

def chk_budget_format(form, field):
    if re.match('[0-9]+$', field.data) is None:
        raise ValidationError('"{0}" is not an acceptable format. Please use only numbers. e.g.:12345'.format(field.data))

class New_PM_Project(DynamicForm):
    name = StringField('Project Name', validators=[DataRequired()], widget=BS3TextFieldWidget())
    description = TextAreaField('Project Description', validators=[DataRequired()])

    skilldb = db.session.query(PM_Skillset).all()
    skillchoices = [(x, str(x).capitalize()) for x in skilldb]

    skillset = MultiCheckboxFieldWithRate('Skillset', choices=skillchoices, validators=[DataRequired()],
                                          widget=select_multi_checkbox)

    budget = StringField("Budget",validators=[DataRequired(), chk_budget_format], widget=text_with_select)
    # budget = StringField('Project Budget', validators=[DataRequired()], widget=BS3TextFieldWidget())
    employees_need = IntegerField('Employees needed', validators=[DataRequired()], widget=BS3TextFieldWidget())
    person_days = IntegerField('Planned Person Days', validators=[DataRequired()], widget=BS3TextFieldWidget())
    responsible_person = StringField('Responsible Person', widget=BS3TextFieldWidget())
    backup_person = StringField('Backup Person', validators=[DataRequired()], widget=BS3TextFieldWidget())
    project_planned_start = DateField('Project Planned Start', validators=[DataRequired(), chk_date_today], widget=DatePickerWidget())
    project_planned_end = DateField('Project Planned End', validators=[DataRequired(), chk_date_today], widget=DatePickerWidget())


    def validate(self):
        if not super().validate():
            return False

        if self.project_planned_end.data < self.project_planned_start.data:
            self.project_planned_end.errors.append(
                '"{0}" is earlier than the start date! Please add a future date!'.format(self.project_planned_end.data))
            return False

        return True


# <___ Testing ___>


class Com(DynamicForm):

    type_of_business = RadioField('Type of Business', choices=[("limited", "Corporate/ Limited"), ("partner", "Partnership"), ("other", "Other")], widget=radio_with_text)
    nature_of_business = RadioField('Nature of Business', choices=[("limited", "Corporate/ Limited"), ("partner", "Partnership"), ("other", "Other")], widget=radio_with_text)
    company_email = StringField(('Company Email'), validators=[DataRequired(), Email(message=emailmessage)], widget=BS3TextFieldWidget())
    budget = StringField("Budget",validators=[DataRequired(), chk_budget_format], widget=text_with_select)
    # budget = StringField('Project Budget', validators=[DataRequired(), chk_budget_format], widget=BS3TextFieldWidget())
    files = FileField(u'Files', widget=files_with_text)



class CustomField(RadioField):
    widget = radio_with_text

    def _value(self):
        if self.data:
            return u', '.join(self.data)
        else:
            return u''

    def process_formdata(self, valuelist):
        if valuelist:
            self.data = [x.strip() for x in valuelist[0].split(',')]
        else:
            self.data = []




class Add_Skillt(DynamicForm):
    # skilldb = db.session.query(PM_Skillset).all()
    # skillchoices = [(x, str(x).capitalize()) for x in skilldb]
    #
    # skillset = MultiCheckboxFieldWithRate(choices= skillchoices, widget=select_multi_checkbox)
    # skillt = FormField(Skill, label="Skill information")
    #
    # company_email = StringField(('Company Email'), validators=[DataRequired(), Email(message=emailmessage)], widget=BS3TextFieldWidget())
    branch_phone = StringField('Branch Telephone', validators=[DataRequired(), chk_phone], widget=BS3TextFieldWidget())
    type_of_business = RadioField('Type of Business', choices=[("limited", "Corporate/ Limited"), ("partner", "Partnership"), ("other", "Other")], widget=radio_with_text)
    # pdb.set_trace()
    currchoices = [(str(currencies[x]['code']), str(currencies[x]['code'])) for x in currencies.keys()]
    budget = StringField("Budget",validators=[DataRequired(), chk_budget_format], widget=text_with_select)
    # test = CustomField('asd', choices=[("limited", "Corporate/ Limited"), ("partner", "Partnership"), ("other", "Other")])

    # budget = StringField('Project Budget', validators=[DataRequired(), chk_budget_format], widget=BS3TextFieldWidget())
    #
    # type_of_business = RadioField('Type of Business',
    #                               choices=[("limited", "Corporate/ Limited"), ("partner", "Partnership"),("other", "Other")],
    #                               widget=radio_with_text
    #                               )
    #
    # com = FormField(Com, label="comp")
    # com2 = FormField(Com, label="comp")
    #
    # company_email = StringField('Company Email', validators=[DataRequired(message='Please add a Company Email!'), Email(message=emailmessage)], widget=BS3TextFieldWidget())
    #
    # files = FileField(u'Files', widget=files_with_text)
    # description = TextAreaField(u'Image Description')

'''
    project_planned_start = DateField('Project Planned Start', validators=[DataRequired(), chk_date_today],
                                      widget=DatePickerWidget())

    project_planned_end = DateField('Project Planned End', validators=[DataRequired(), chk_date_today],
                                    widget=DatePickerWidget())

    def validate(self):
        if not super().validate():
            return False

        if self.project_planned_end.data < self.project_planned_start.data:
            self.project_planned_end.errors.append('"{0}" is earlier than the start date! Please add a future date!'.format(self.project_planned_end.data))
            return False

        return True
    
    def chk_budget_old():
        # result = True
        # fdata = field.data.split(' ')
        # if len(fdata) is not 2:
        #     result = False
        # else:
        #     if re.match('[0-9]+$', fdata[0]) is None or re.match('[a-zA-Z]+$', fdata[1]) is None:
        #         result = False
    
        # if result == False:
        #     raise ValidationError('"{0}" is not an acceptable format. A correct value e.g.:12345 EUR'.format(field.data))
'''
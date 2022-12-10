> Vidath Dissanayake | Sri Lanka
> Links: [Activities of Data Processing](Activities%20of%20Data%20Processing.md)

When we input data, mistakes may occur. To overcome these mistakes, programmers should include some controls called validation methods.

These methods are classified as follows.
1. [Data Validation](#1%20Data%20Validation)
2. [Data Verification](#2%20Data%20Verification)

# 1. Data Validation

Data validation is a technique to check whether the entering data is sensible and responsible for the expected processing and generate information.

# Data Validation Methods

1. Type check – This method ensures that the correct data type (text, integer, date) is entered.
2. Presence check – This proves that the data field is not blank, as some data units are very important.
3. Range check – Check whether the data is in allowed range.

E.g:

| Check          | Field Name | Value        | Validation | Value      | Validation |
| -------------- | ---------- | ------------ | ---------- | ---------- | ---------- |
| Type check     | Name       | 34579        | ❌          | Omethra    | ✔          |
| Presence check | Name       |              | ❌          | Samidi     | ✔          |
| Range check    | Tele No.   | 033422249691 | ❌          | 0332224969 | ✔          |


# 2. Data Verification

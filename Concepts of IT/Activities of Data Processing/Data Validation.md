# Data Validation

> Vidath Dissanayake | Sri Lanka

Data validation is a technique to check whether the entering data is sensible and responsible for the expected processing and generate information.

## Data Validation Methods

1. Type check – This method ensures that the correct data type (text, integer, date) is entered.
2. Presence check – This proves that the data field is not blank, as some data units are very important.
3. Range check – Check whether the data is in allowed range.

E.g:

| Check          | Field Name | Value        | Validation | Value      | Validation |
| -------------- | ---------- | ------------ | ---------- | ---------- | ---------- |
| Type check     | Name       | 34579        | ❌          | Omethra    | ✔          |
| Presence check | Name       |              | ❌          | Samidi     | ✔          |
| Range check    | Tele No.   | 033422249691 | ❌          | 0332224969 | ✔          |

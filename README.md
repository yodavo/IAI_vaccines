# Poryecto IAI vaccines
# Diplomado UTEC
  
---
 
 **About VAERS.**
 
 - The U.S. Department of Health and Human Services (DHHS) established VAERS, which is co-administered by the Food and Drug Administration (FDA) and the Centers for Disease Control (CDC), to accept all reports of suspected adverse events, in all age groups, after the administration of any U.S. licensed vaccine.
 - The primary purpose for maintaining the database is to serve as an early warning or signaling system for adverse events not detected during pre-market testing.

**Careful points about this data set**

1. VAERS data are from a *passive surveillance system and represent unverified reports* of health events that occur after vaccination.
2. The event may have been related to an underlying disease or condition, to medications being taken concurrently, or may have occurred by chance.
3. VAERS data should be used with caution as numbers and conditions do not reflect data collected during follow-up.
4. Note that the inclusion of events in VAERS data does not infer causality.

 **About the data codification**
 
 - On 1/17/2007 the VAERS coding system was converted (from an older system: Coding Symbols for a
Thesaurus of Adverse Reaction Terms (COSTART) used until 2007) to an international coding system that is used worldwide: Medical Dictionary for Regulatory Activities (MedDRA) which is more detailed.

**MedDRA** uses key words representing the medical condition(s) described in the case report and converts them to standardized codes. Here this dataset uses more than 17000 "Preferred Terms" MedDRA codes. Codes are updated semi-annually (here on COVID19, we have collected version 23.1 and 24.0).

 **About the data.**
 
About 85-90% of vaccine adverse event reports concern relatively minor events, such as fevers or redness and swelling at the injection site. The remaining reports (less than 15%) describe serious events, such as hospitalizations, life-threatening illnesses, or deaths.

> No data is provided that would allow identification of any individuals associated with these reports.

**Data Collection:** Based on 2 form versions, online version (on websites) and [printing pdf version](2021-03_VAERSForm.pdf). Referred on the data set as (VAERS 1 and VAERS 2).
 
**Structure:** The downloadable VAERS public data set consists of **3 separate data files**.
1. VAERSDATA.CSV - provides a detailed description of the data provided in each field.
2. VAERSVAX.CSV - provide the remaining vaccine information (vaccine name, manufacturer, lot number, route, site, and number of previous doses administered), for each of the vaccines listed. **VAX_DOSE was discontinued in the VAERS 2 form.**
3. VAERSSYMPTOMS.CSV - provide the adverse event coded terms utilizing the MedDRA dictionary. **Each row in the .csv will contain up to 5 MedDRA terms per VAERS ID; thus, there could be multiple rows per VAERS ID.** For each of the VAERS_ID’s listed in the VAERSDATA.CSV table, there is a matching record in this file, identified by VAERS_ID, **Duplicates may appear in data** and terms are listed in alphabetical order. In case a report has more than 5 terms multiple rows with 5 terms each will be listed for that VAERS ID.

**Data Types**
1. NUM (float64) = numeric data
2. CHAR (object) = text or "character" data
3. DATE (not formated) = date fields in mm/dd/yy format

**Data sets merged (total 51 columns)**

|:heavy_check_mark: |\# | Column | Count | Dtype | Description | Notes | Options |
|--- |--- | --- | --- | --- |--- |--- | --- |
|:heavy_check_mark: |\# | VAERS_ID| 591241 | float64 | VAERS Identification Number | Used for merging datasets | Unique for DB |
|:heavy_check_mark: | 0 | RECVDATE | 591241 | **Datetime** | Date report was received | | date |
|:heavy_check_mark: |  1 | STATE | 535248 | object | State in the USA | 2 letter code | nominal | 
|:heavy_check_mark: |  2 | AGE_YRS | 558307 | float64 | Age in Years | | integer | 
| :x:|  3 | CAGE_YR | 510323 | float64 | Calculated age of patient in years | Needs summation | integer |
| :x:|  4 | CAGE_MO | 936 | float64 | Calculated age of patient in months | Needs summation | integer |
|:heavy_check_mark: |  5 | SEX | 591241 | object | Sex | | (M, F, Unknown=Blank) |
| :x:|  6 | RPT_DATE | 315 | **Datetime** | Date Form Completed | **REJECTED**, low number records | date |
| :robot: |  7 | SYMPTOM_TEXT | 591181 | object | Reported symptom text | **In Review** | text |
|:heavy_check_mark: |  8 | DIED | 9434 | object | Died | Patient Outcomes | (Y, Blank) |
|:heavy_check_mark: |  9 | DATEDIED | 8835| **Datetime** | Date of Death | Patient Outcomes | date |
|:heavy_check_mark: |  10 | L_THREAT | 16254| object | Life-Threatening Illness | Patient Outcomes, *Medical history* | (Y, Blank) |
| :x:|  11 | ER_VISIT | 50 | object | Emergency Room or Doctor Visit| Patient Outcomes **VAERS 1 form only** | (Y, Blank) |
|:heavy_check_mark: |  12 | HOSPITAL | 53726 | object | Hospitalized | Patient Outcomes | (Y, Blank) |
|:heavy_check_mark: |  13 | HOSPDAYS | 39773 | float64 | Number of days Hospitalized | Patient Outcomes | integer |
|:x: |  14 | X_STAY |  418 | object | Prolongation of Existing Hospitalization | Patient Outcomes | (Y, Blank) |
|:heavy_check_mark:|  15 | DISABLE | 13438 |  object | Disability | Patient Outcomes, *Medical history* | (Y, Blank) |
|:heavy_check_mark: |  16 | RECOVD | 541552 | object | Recovered |  | (Y=recovered, N=not recovered, U=Blank) |
|:heavy_check_mark: |  17 | VAX_DATE | 564641 | **Datetime** | Vaccination Date | Check here for vax dosage | date |
|:heavy_check_mark:|  18 | ONSET_DATE | 570860 | **Datetime** | Adverse Event Onset Date | *DOUBLE CHECK HERE* | date |
|:x: |  19 | NUMDAYS | 548731 | float64 | Number of days (Onset date - Vax. Date) | | integer |
| :robot: |  20 | LAB_DATA | 293299 | object | Diagnostic laboratory data | *Medical history* | | nominal | 
|:heavy_check_mark: |  21 | V_ADMINBY | 591241 | object | Type of facility where vaccine was administered | | **VAERS 1.0:** PUB=Public, PVT=Private, MIL=Military, OTH=Other, UNK=Unknown. **VAERS 2.0: ++** PHM=Pharmacy, SCH=school/student health clinic, SEN=Nursing home or senior living facility, WRK=Workplace clinic. |
| :x:|  22 | V_FUNDBY | 365 | object | Type of funds used to purchase vaccines | **VAERS 1 field only** | PUB=Public, PVT=Private, MIL=Military; OTH=Other/Unknown |
|:robot:  |  23 | OTHER_MEDS | 407792 | object | Other Medications | *Medical history* | nominal | 
| :robot: | 24 | CUR_ILL | 328851 | object | Illnesses at time of vaccination | *Medical history* | nominal | 
|:robot:  |  25 | HISTORY | 422557 | object | Chronic or long-standing health conditions | *Medical history*, **VAERS 1 form only**, this field also includes pre-existing physician-diagnosed allergies | nominal |
|:robot:  |  26 | PRIOR_VAX | 36239 |  object | Prior Vaccination Event information | *Medical history* | nominal | 
| :x: |  27 | SPLTTYPE | 98610 |  object | Manufacturer/Immunization Project Report Number | **REJECTED**, not on the scope | nominal | 
| :x: |  28 | FORM_VERS | 591241 | int64 | VAERS form version 1 or 2 | (1, 2) |
| :x: |  29 | TODAYS_DATE | 588302 | **Datetime** | Date Form Completed | Not relevant **REJECTED** | date |
| :x: |  30 | BIRTH_DEFECT | 406 | object | Congenital anomaly or birth defect | Patient Outcomes, *Medical history*. **Only in VAERS2** | (Y, Blank) |
| :x: | 31 | OFC_VISIT | 136672 | object | Doctor or other healthcare provider office/clinic visit | Patient Outcomes,***Only in VAERS2*** | (Y, Blank) |
|:heavy_check_mark: |  32 | ER_ED_VISIT | 103144 | object | Emergency room/department or urgent care | Patient Outcomes,***Only in VAERS2*** | (Y, Blank) |
| :robot: |  33 | ALLERGIES |381752 | object | Allergies to medications, food, or other products |  | nominal | 
| :x:|  34 | SYMPTOM1 | 591241 | object | Adverse Event MedDRA Term 1 |  | code | 
| :x:|  35 | SYMPTOMVERSION1 | 591241 | float64 | MedDRA dictionary version number 1 | | code | 
| :x:|  36 | SYMPTOM2 | 470315 | object | Adverse Event MedDRA Term 2 | | code | 
| :x:|  37 | SYMPTOMVERSION2 | 470315 | float64 | MedDRA dictionary version number 2 | | code | 
| :x:| 38 | SYMPTOM3 | 367938 | object | Adverse Event MedDRA Term 3 | | code | 
| :x:| 39 | SYMPTOMVERSION3 | 367938 | float64 | MedDRA dictionary version number 3 | | code | 
| :x:| 40 | SYMPTOM4 | 279936 | object | Adverse Event MedDRA Term 4 | | code | 
| :x:| 41 | SYMPTOMVERSION4 | 279936 | float64 |  MedDRA dictionary version number 4 | | code | 
| :x:| 42 | SYMPTOM5 | 207749 | object | Adverse Event MedDRA Term 5 | | code | 
| :x:| 43 | SYMPTOMVERSION5 | 207749 | float64 |  MedDRA dictionary version number 5 | | code | 
| :x:| 44 | VAX_TYPE | 591241 | object | Administered Vaccine Type | | (Many, only COVID19 interested) |
| :heavy_check_mark: | 45 | VAX_MANU | 591241 | object | Vaccine Manufacturer | important | (Many, only COVID19 interested) |
|:heavy_check_mark: | 46 | VAX_LOT |  419626 | object | Manufacturer's Vaccine Lot | double check | (Many, only COVID19 interested) |
| :heavy_check_mark:| 47 | VAX_DOSE_SERIES | 588217 | object | Number of doses administered | Not completely reliable, The VAERS 1 field VAX_DOSE was discontinued in the VAERS 2 | (1 --if it was noted -- , Blank) | 
|:heavy_check_mark: | 48 | VAX_ROUTE |464076 | object | Vaccination Route | Could be important.. | (UN=Unknown, ID=Intradermal, IM=Intramuscular, SC=Subcutaneous, IN=Intranasal, PO=Per Oral, SYR=Needle and syringe (not specified further), JET=Needle free jet injector device,OT=Other)
|:heavy_check_mark: | 49 | VAX_SITE | 476756 | object | Vaccination \[Anatomic\] Site | | nominal |
| :x:| 50 | VAX_NAME | 591241 | object | Vaccination Name | **REJECTED** === VAX_MANU| (Many, only COVID19 interested) | 

---



 

---
title: "Explainable artificial intelligence models in predicting major cardiovascular events: insights from the PolyIran and PolyPars prospective studies"
collection: publications
category: journals
excerpt: "This study develops and evaluates explainable AI models for predicting major cardiovascular events over 60 months using data from the PolyIran and PolyPars prospective studies."
date: 2026-06-14
authors: "Amir Ghafari, Sadaf Sepanlou, Gholamreza Roshandel, Seyed Amir Ahmad Safavi-Naini, Fatemeh Malekzadeh, Maryam Sharafkhah, Amir Kasaeian, Aakriti Gupta, Shubhadarshini Pawar, Zahra Dehghanian, Amir Azimi, Mohammad Aghaei, Akram Pourshams, Hossein Poustchi, Nasrallah Jahangard, Hamid R. Rabiee, Reza Malekzadeh"
venue: "Scientific Reports"
teaser: "publications/images.jpeg"
pdf: "/files/s41598-026-57311-w_reference.pdf"
paperurl: "https://www.nature.com/articles/s41598-026-57311-w"
abstract: "Cardiovascular diseases are among the leading causes of global mortality and morbidity, underscoring the need for accurate and explainable predictive models. This study aimed to develop and evaluate explainable AI models for predicting major cardiovascular events (MCVE) over 60 months. We conducted a secondary analysis of two large cohort studies nested within the Golestan (northeast Iran) and Pars (south Iran) Cohorts, which followed identical protocols. After applying exclusion criteria, 9,769 participants remained. Predictors included demographic, clinical, and biochemical variables, with class imbalance addressed via SMOTE. Machine learning models (XGBoost, logistic regression, decision tree, SVM, random forest, KNN) and a multilayer perceptron were trained and evaluated. Model performance was assessed using accuracy, sensitivity, specificity, positive predictive value, negative predictive value, AUC, and F1 score. Interpretability was examined using SHapley Additive exPlanations. Machine-learning models showed variable performance across cohorts, with XGBoost demonstrating the best and most stable discrimination. In the pooled cohort, XGBoost achieved the highest AUC (0.84), with good accuracy (0.81) and specificity (0.85). Its performance remained consistent in the PolyIran and PolyPars cohorts, with AUC values of 0.83 and 0.85, respectively, suggesting good generalizability. Random Forest was the second-best model. The MLP deep-learning model showed only modest performance. SHAP analysis identified age, creatinine, and systolic blood pressure as the most important predictors across cohorts, with higher values associated with increased MCVE risk. Higher FBS, BMI, LDL/HDL ratio, male sex, and smoking were also associated with increased risk, whereas PolyPill use and greater adherence showed protective effects. Explainable AI models, particularly XGBoost, demonstrated high predictive accuracy for MCVE and revealed creatinine as a novel risk indicator not included in traditional CVD scores. These findings support incorporating kidney function screening into CVD risk stratification and highlight the potential of AI-driven tools to enhance prevention strategies."
citation: "Ghafari, A., Sepanlou, S., Roshandel, G. et al. Explainable artificial intelligence models in predicting major cardiovascular events: insights from the PolyIran and PolyPars prospective studies. Sci Rep (2026). https://doi.org/10.1038/s41598-026-57311-w"
---

## Introduction

Cardiovascular diseases are among the leading causes of global mortality and morbidity, underscoring the need for accurate and explainable predictive models. This study aimed to develop and evaluate explainable AI models for predicting major cardiovascular events (MCVE) over 60 months.

## Methods

### Study Populations

We conducted a secondary analysis of two large cohort studies nested within the Golestan (northeast Iran) and Pars (south Iran) Cohorts, which followed identical protocols. After applying exclusion criteria, 9,769 participants remained.

### AI Models

We developed and compared multiple machine learning approaches:
- XGBoost
- Logistic Regression
- Decision Tree
- Support Vector Machines (SVM)
- Random Forest
- K-Nearest Neighbors (KNN)
- Multilayer Perceptron (MLP) deep learning model

Class imbalance was addressed via SMOTE (Synthetic Minority Over-sampling Technique).

### Explainability Methods

- **SHAP** (SHapley Additive exPlanations): Global and local feature importance

## Results

### Model Performance

Machine-learning models showed variable performance across cohorts, with XGBoost demonstrating the best and most stable discrimination:

| Model | AUC (Pooled) | Accuracy | Specificity |
|-------|--------------|----------|-------------|
| XGBoost | 0.84 | 0.81 | 0.85 |
| Random Forest | 0.82 | 0.79 | 0.83 |
| MLP | 0.78 | 0.75 | 0.78 |

XGBoost performance remained consistent in the PolyIran and PolyPars cohorts, with AUC values of 0.83 and 0.85, respectively, suggesting good generalizability. Random Forest was the second-best model. The MLP deep-learning model showed only modest performance.

### Key Predictors Identified by SHAP

1. **Age** (most important predictor)
2. **Creatinine** (novel risk indicator not included in traditional CVD scores)
3. **Systolic Blood Pressure**
4. **Fasting Blood Sugar (FBS)**
5. **Body Mass Index (BMI)**
6. **LDL/HDL Ratio**
7. **Male Sex**
8. **Smoking Status**
9. **PolyPill use** (protective effect)
10. **Medication adherence** (protective effect)

### Explainability Insights

SHAP analysis identified age, creatinine, and systolic blood pressure as the most important predictors across cohorts, with higher values associated with increased MCVE risk. Higher FBS, BMI, LDL/HDL ratio, male sex, and smoking were also associated with increased risk, whereas PolyPill use and greater adherence showed protective effects.

## Discussion

Our XAI models demonstrate that:
1. Machine learning approaches, particularly XGBoost, outperform traditional risk scores
2. Model explainability through SHAP facilitates clinical adoption and trust
3. Creatinine was identified as a novel risk indicator not included in traditional CVD scores such as Framingham or ASCVD
4. These findings support incorporating kidney function screening into routine CVD risk stratification

### Clinical Implications

The proposed models can be integrated into:
- Electronic health records for real-time risk assessment
- Primary care settings, particularly in low-resource environments
- Personalized prevention strategies based on modifiable risk factors
- Screening programs that include renal function tests alongside traditional cardiovascular risk factors

## Conclusion

Explainable AI models, particularly XGBoost, demonstrated high predictive accuracy for major cardiovascular events and revealed creatinine as a novel risk indicator not included in traditional CVD scores. These findings support incorporating kidney function screening into CVD risk stratification and highlight the potential of AI-driven tools to enhance prevention strategies. The combination of high predictive performance with interpretability makes these models suitable for potential clinical implementation in cardiovascular risk assessment.

## Acknowledgements

We extend our gratitude to all participating patients and clinical staff who contributed to this research.

## Author Contributions

Amir Ghafari and Sadaf Sepanlou contributed equally to this work.

## Ethics Declarations

This study is a secondary observational analysis based on two major clinical trials: PolyIran and PolyPars. The PolyPars trial (Polypill for primary and secondary prevention of cardiovascular disease: a pragmatic cluster-randomised controlled trial) was approved by the Ethics Committees of Shiraz University of Medical Sciences and Tehran University of Medical Sciences, and all participants provided written informed consent prior to enrollment. Similarly, the PolyIran trial (Polypill for the prevention of cardiovascular disease: a pragmatic cluster-randomised controlled trial) was approved by the Ethics Committee of the Digestive Diseases Research Institute, Tehran University of Medical Sciences. Written informed consent was also obtained from all participants in this trial. Ethical approval for the current secondary analysis was obtained from the Tehran University of Medical Sciences (TUMS) under the ethical code IR.TUMS.DDRI.REC.1402.044. All data used for analysis were anonymized, ensuring no personally identifiable information was included. In the present study, all methods were carried out in accordance with relevant guidelines and regulations, including the principles of the Helsinki Declaration.

## Competing Interests

The authors declare no competing interests.

## Generative AI Declaration

During the preparation of this work, the authors used Grammarly and ChatGPT 4 to grammar check and increase the fluency of the text. After using this tool/service, the authors reviewed and edited the content as needed and take full responsibility for the content of the publication.

## Additional Information

**Publisher's Note:** Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

**Supplementary Information** is available online at: [link to supplementary material]

## Rights and Permissions

This article is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License, which permits any non-commercial use, sharing, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if you modified the licensed material. You do not have permission under this licence to share adapted material derived from this article or parts of it. The images or other third party material in this article are included in the article's Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/licenses/by-nc-nd/4.0/.
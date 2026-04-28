# Yet Another ICU Benchmark: A Flexible Multi-Center Framework for Clinical ML

- Decision: Accept
- Avg Score: 6.20
- Scores: 6, 6, 5, 8, 6

## Abstract
Medical applications of \acrfull{ml} have experienced a surge in popularity in recent years. The intensive care unit (ICU) is a natural habitat for ML given the abundance of available data from electronic health records. Models have been proposed to address numerous ICU prediction tasks like the early detection of complications. While authors frequently report state-of-the-art performance, it is challenging to verify claims of superiority. Datasets and code are often not published, and cohort definitions, preprocessing pipelines, and training setups are difficult to reproduce. This work introduces \acrfull{yaib}, a modular framework that allows researchers to define reproducible and comparable clinical \acrshort{ml} experiments; we offer an end-to-end solution from cohort definition to model evaluation.
The framework natively supports most open-access ICU datasets (\acrshort{mimic} III/IV, \acrshort{eicu}, \acrshort{hirid}, \acrshort{aumc}) and is easily adaptable to future and custom ICU datasets. Combined with a transparent preprocessing pipeline and extensible training code for multiple \acrshort{ml} and deep learning models, \acrshort{yaib} enables unified model development, transfer, and evaluation. Our benchmark comes with five predefined established prediction tasks (mortality, acute kidney injury, sepsis, kidney function, and length of stay) developed in collaboration with clinicians. Adding further tasks is straightforward by design. %and provide extensible training code that natively supports eight \acrshort{ml} architectures.
Using \acrshort{yaib}, we demonstrate that the choice of dataset, cohort definition, and preprocessing have a major impact on the prediction performance, often more so than model class, indicating an urgent need for \acrshort{yaib} as a holistic benchmarking tool.
We provide our work to the clinical \acrshort{ml} community to accelerate method development and enable real-world implementations. Use 10~point type, with a vertical
  spacing (leading) of 11~points.  The word \textbf{Abstract} must be centered,
  bold, and in point size 12. Two line spaces precede the abstract. The abstract
  must be limited to one paragraph.
\end{comment}

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces an ICU benchmark that incorporates several ICU datasets, including MIIMC, eICU, HiRID, and AUMCdb. It covers multiple tasks such as mortality risk, kidney function, sepsis, acute kidney injury, and length of stay predictions. Furthermore, the paper offers an end-to-end pipeline for data preprocessing, model construction, training, and evaluation.

### Strengths
- The paper addresses issues of comparability and reproducibility, both of which are crucial in the field of machine learning for healthcare.
- The benchmark unifies four commonly used datasets and allows transfer learning.
- The experiments on adapting task definitions clearly demonstrate the impact of cohort definitions, preprocessing strategies, and training protocols.

### Weaknesses
 - I acknolwedge the motivation of this paper and appreciate considerable effort invested in establishing such a benchmark dataset. However, while the paper's central claim is the adaptability of the YAIB benchmark to other datasets, tasks, and models, this assertion necessitates a comprehensive experience with the benchmark, which is challenging to evaluate during the brief review period.

- Datasets like MIMIC and eICU are highly complex and heterogeneous. The proposed YAIB benchmark only supports 52 clinical features (mainly vital signs and lab tests). A vast amount of other available features are ignored (like diagnosis, prescriptions, clinical notes, x-rays). This limited feature support might hinder future model advancements (which can be seen in Tables 3 & 4 where the performance between classic ML and DL models are very similar). Specifically, the restriction to only 52 features, primarily vital signs and basic lab results, neglects crucial information such as detailed diagnostic codes (ICD-9/10), medication administration records (MARs), and the rich narrative data found in clinical notes. The exclusion of these features limits the complexity of models that can be trained and evaluated within the framework, hindering the exploration of more advanced modeling techniques that could leverage this information. For example, the lack of medication data prevents the evaluation of models that might predict adverse drug events or drug-drug interactions, which are important clinical tasks.

### Questions
Refer to weaknesses section.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces Yet Another ICU Benchmark (YAIB), a modular framework which allows researchers to define and conduct clinical machine learning (ML) experiments on multiple open-source medical datasets (MIMIC III/IV, eICU, HiRID, AUMCdb). The YAIB framework includes modules for 1) clinical concept definition on harmonized datasets 2) task specification and cohort selection 3) data preprocessing and feature extraction 4) ML model training and evaluation (both traditional ML and deep learning models). Through experiments on five pre-defined clinical tasks, this work demonstrated comparable results of benchmarking baseline models on different datasets, analyzed the impact of varying task/cohort definition and showed the utility of YAIB in transfer learning via a pre-train and fine-tune paradigm.

### Strengths
**Originality**: In previous literature, the ICU data benchmarks mostly focused on a single dataset or only supported subsets of multiple datasets, and often required modifications to core codebase for adding new clinical tasks. The originality of this paper lies in that 1) it utilizes the full datasets of five open-source ICU datasets, and for the first time introduced the AmsterdamUMCdb (AUMCdb) dataset into a benchmark 2) it is built on a flexible framework which decouples each individual module and allows users to easily add new tasks or adjust current modules.

**Quality**: This paper specifically accounted for the common issues that researchers encounter when using ICU benchmarks, such as the lack of comparisons across multiple datasets, different task/cohort definitions. Via extensive experiments, this paper demonstrated the utilities of the proposed framework and analyzed the potential impact of small perturbations to the task/cohort definitions by ablation studies. The experiment results supported their claims that 1) comparable results can be achieved when different datasets are harmonized and ML pipelines are unified 2) small changes in definitions can lead to different results.

**Clarity**: This paper is clear and well-written. The tables and figures are informative and easy to understand.

**Significance**: Data processing and clinical task definition have always been a burden for researchers in machine learning for healthcare. Once made public, this work has the potential to help reduce the overhead in benchmarking and developing new ICU prediction methods. This work will also allow researchers to validate their findings by evaluating and comparing the results on multiple real-world ICU datasets. Thanks to the modular implementation, researchers working on other tasks involving ICU data, e.g. reinforcement learning or representation learning, may also benefit from some modules in the proposed framework. Thus, this work has both high technical significance and clinical relevance.

### Weaknesses
1. The definition of several terms used in the paper is not clear, including "harmonization", "clinical concepts". Though it can be inferred from later text what they may refer to, I think it would still benefit the readers if you can clearly define them the first time you use them in the paper. Specifically, the term "harmonization" lacks detail; does this refer to a simple renaming of features to have consistent labels across datasets, or does it involve more complex transformations to account for differences in data distributions or measurement protocols? Similarly, "clinical concepts" could refer to a wide range of abstractions, from simple vital signs to complex diagnoses, and a precise definition is needed to understand the scope of the framework.

2. Based on the experiments, it seems that the time series features are extracted from numeric data rather than waveform data (please correct me if I am wrong). Currently, most ICU benchmarks used numeric data for prediction tasks and only very few used waveform data, but waveform data are very informative and may greatly help improve the predictive performance. Thus I think the contribution would be more solid if waveform data can be utilized for a new ICU benchmark. The paper should clarify whether the time-series data used are the raw, high-frequency signals, or if they are already aggregated or downsampled, as this has a significant impact on the information content of the features. Furthermore, the paper should acknowledge the potential benefits of incorporating high-resolution waveform data, such as ECG or PPG signals, which are known to capture subtle physiological changes that may be missed by lower-frequency numeric data.

3. Basic statistics of the datasets, e.g. number of patients, ICU stays, and the prevalence of classes or the range of regression targets, are missing in the main paper (found them in appendix). Inclusion of such information will help readers get a general idea of the datasets and understand some of the experiment results, e.g. the discrepancy in the performances shown in Figure 2 may be due to the difference in prevalence in mortality across the datasets. Also, for the pooled dataset, is there any possibility that one dataset is dominating the training set for any task? The paper should also specify how the data was split for training, validation, and testing, and whether any measures were taken to ensure that the splits were representative of the overall data distribution. For example, were the splits stratified by dataset or by outcome variable?

### Questions
1. In Section 4, you investigated the effects of small variations in task definitions. For the three variations you tried, the first and second are variations to the cohort and the feature selection but not to the clinical task definition, only the third is varying the definition of sepsis - which I understand is the only one directly relevant to clinical task definition. In this case, you may need to change how you describe the variations or redefine what you mean by "task" to avoid the confusion.

2.  In Section 4 Preprocessing, for the aggregated features, what are the time windows for aggregation and the frequencies that you update those features? Is there any specific consideration in the choice for them?

3. In Table 4, it would be helpful to also include the range or the units of KF/LoS, or additionally show the MAEs as % relative to the valid ranges of KF/LoS (absolute MAEs do not provide much information).

4. A minor typo, a space is missing between "repository" and "to" near the bottom on Page 4.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this study, the authors present an ICU-benchmark for clinical machine learning. They employ this framework to benchmark four ICU datasets. The toolkit offered encompasses data preprocessing, model training, and evaluation.

### Strengths
The design of the benchmark framework is clear. The paper offers an exhaustive detailing of preprocessing, modeling, and experimental results. The code's structure is clear, and the authors also provide comprehensive guidelines.

### Weaknesses
My primary concerns are:

While the effort in constructing a comprehensive benchmark is great, I am uncertain about its alignment with the primary focus of ICLR. The paper appears to lean heavily towards a benchmarking contribution rather than a technical innovation. It might be more fitting for this work to be submitted to NeurIPS's benchmark track or journals such as Scientific Data.

My other comment is about the comparative scope of the study. The authors posit that their framework offers flexibility and the potential for application to other datasets, suggesting its closeness to a clinical ML toolkit. I recommend contrasting this work with existing clinical ML toolkit contributions, such as references [1,2] for a more comprehensive perspective.

### Questions
Please see the weaknesses above.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors present an innovative framework that facilitates reproducible and comparable machine learning experiments using publicly available ICU datasets. This framework offers: i) thorough and standardized definitions of cohorts and feature extractions, ii) Transparent feature engineering and preprocessing, iii) commonly compared deep learning baselines (including RNNs, TCN, Transformer) with flexibility in the network architecture and hyper-parameters optimization, and iv) performance metrics. This work addresses the growing demand for a standardized framework for comparing and reproducing widely used machine learning and deep learning benchmarks. Moreover, this framework can be further utilized to provide a standardized way of evaluating newly developed DL methods. This work will be extremely helpful in opening the door for wider adoption of recent deep learning methods in real clinical practices.

### Strengths
1.	The paper is well-written.
2.	The authors provide a very solid framework, covering from defining clinically relevant cohorts in ICU admissions to training and evaluating ML/DL methods. Moreover, this framework has the flexibility to incorporate user-specific DL networks which will be extremely useful in providing comparable and reproducible evaluations.
3.	The well-defined cohorts and harmonized datasets hold significant potential for various applications, including domain adaptation, time-series generation, and more.
4.	The experiments that emphasize the impact of incorporating different features and employing different data assembly processes (e.g., cohort/label definition) are thoroughly investigated.

### Weaknesses
1.	Although the authors incorporate a wide range of measurements from the ICU datasets, many therapeutic interventions and comorbidities are missing, which can be crucial for predicting clinical outcomes of interest. Moreover, the time-varying features are mostly continuous while there exist many binary and categorical features in these ICU datasets. Specifically, the absence of detailed medication data, such as specific drug types, dosages, and administration times, limits the framework's ability to capture the complexity of patient care. The lack of comorbidity information further restricts the model’s ability to account for pre-existing conditions that significantly impact patient outcomes. The focus on continuous features overlooks the rich information present in categorical data, such as ventilation modes or specific interventions, which can be highly predictive.

2. Minor comments: typo in p4 “repositoryto” $\rightarrow$ “repository to”

### Questions
1.	There exists a harmonized ICU dataset called BlendedICU [A] that incorporates AmsterdamUMCdb, eICU, HiRID, and MIMIC-IV. While the reviewer acknowledges that [A] has not been available online when the proposed work was submitted, what is the distinction and contribution of the proposed work from [A]?
2.	Regarding Weakness #1: As far as the reviewer is aware, variations in units and features can occur both within and across datasets due to differences in observation circumstances (e.g., using different medical devices). How did the authors handle such issues? Additionally, what is the reason for the extracted datasets having missing therapeutic interventions and comorbidities (while some of them are mentioned in Appendix C), which are often extremely important for predicting clinical outcomes?

[A] M. Oliver et al., "Introducing the BlendedICU dataset, the first harmonized, international intensive care dataset," Journal of Biomedical Informatics, 2023.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper presents a multi-dataset framework that consists of preprocessing and processing techniques to aid reproducible research with consistent data and experiment methods. The authors demonstrate that the experiment choices can have a substantial impact on model prediction performance.

### Strengths
I commend the authors for their hard work to create an open source code repository, which is not a trivial task. Based on the description in the paper, this repository could have substantial impact for streamlining research with ICU datasets. 

The paper is very easy to follow and organized well. Thorough descriptions of datasets and code are included. 

Paper includes example scripts in the appendix to demonstrate code simplicity and example use cases. 

Table 1 presents an excellent overview and comparison of the proposed methods and prior work. 

The paper demonstrates use of the proposed framework with four prominent ICU datasets in ML literature. Additionally the datasets cover a range of populations including those in US and Europe, which can promote research that is applicable across different populations.

### Weaknesses
1. The baseline table is useful for future work to compare against. However, this table does not seem relevant to motivating the proposed framework and could be included in the appendix. To better motivate the value of the proposed unifying framework, it would be useful to show more experiments regarding significant differences in model performance when different experiment methods are used (outcome labels, cohort selection, etc.). For example, you could consider an ablation study to show that model performance significantly improves or decreases based on various outcome definitions for datasets with consistent preprocessing, model choice, hyperparameters. The experiment mentioned in the paper regarding exclusion criteria would also be a good example to elaborate on and include table results comparing impact of different exclusion criteria.

2. Be specific about performance gains and losses (example: improved by XX%) and their statistical significance. A significant difference in model performance due to unaligned data preprocessing and processing pipeline would help motivate the proposed unifying framework. Stating that “differences were bigger for some datasets than others” is not a robust explanation. 

3. Novel ML research often proposes a new model that is evaluated across multiple datasets. Enabling support for new models to be easily integrated into this framework is important. The appendix provides example code for training a specific model, such as those in scikit-learn or implemented in pytorch. Including more thorough explanation and/or code examples for how to train a novel/custom model, such as pytorch-based model implemented in a separate python file, would be useful. 

4. The author mentions flexibility of the repo in allowing users to configure data preprocessing in a streamlined fashion across multiple datasets. However, does this somewhat deflate the original purpose to enable reproducible research through consistent dataset preprocessing and processing. Researchers may still conduct research with various preprocessing steps that differ across literature. The value of this framework hinges on if research exactly states the detailed use of YAIB in their paper/methods AND if future work follows these exact same steps. It would be useful if the author's address this point and potentially expand their unifying framework to include recommended approaches for how to reference/cite use of YAIB in future work that could promote reproducible research. 

The low score is mostly because of points 1-3. If these points are addressed I would be happy to raise the score.

### Questions
1. It is possible that thresholds used to define outcomes from time series data may update over time based on new knowledge, thus impacting outcome labels. Does the repo have support to enable users to define their own outcome definitions across datasets? For example, a patient AKI outcome may occur when patient creatinine falls below a specific threshold. Or are outcome labels strictly based on definitions included in the datasets?

2. Are models other than those in scikit-learn hardcoded into the repo or are there wrappers for these as well? Is there support for users to include and evaluate new/customized model architectures in the pipeline?

3. Is there a reason why this framework is limited to ICU/healthcare settings and not time series in general. I could see a pipeline like this being applicable to time series from many domains. It may be worth elaborating on why the framework is ICU-specific. It may also be useful to compare YAIB to similar non-healthcare related frameworks.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good

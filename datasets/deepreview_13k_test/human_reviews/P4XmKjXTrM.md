# ACES: Automatic Cohort Extraction System for Event-Stream Datasets

- Decision: Accept
- Scores: 8, 6, 6, 3

## Abstract
Reproducibility remains a significant challenge in machine learning (ML) for healthcare. Datasets, model pipelines, and even task/cohort definitions are often private in this field, leading to a significant barrier in sharing, iterating, and understanding ML results on electronic health record (EHR) datasets. This paper addresses a significant part of this problem by introducing the Automatic Cohort Extraction System (ACES) for event-stream data. This library is designed to simultaneously simplify the development of task/cohorts for ML in healthcare and also enable the reproduction of these cohorts, both at an exact level for single datasets and at a conceptual level across datasets. To accomplish this, ACES provides (1) a highly intuitive and expressive configuration language for defining both dataset-specific concepts and dataset-agnostic inclusion/exclusion criteria, and (2) a pipeline to automatically extract patient records that meet these defined criteria from real-world data. ACES can be automatically applied to any dataset in either the Medical Event Data Standard (MEDS) or EventStreamGPT (ESGPT) formats, or to \textit{\textbf{any}} dataset in which the necessary task-specific predicates can be extracted in an event-stream form. ACES has the potential to significantly lower the barrier to entry for defining ML tasks that learn representations, redefine the way researchers interact with EHR datasets, and significantly improve the state of reproducibility for ML studies in this modality. A short video demonstration of \toolabbr is available at: \url{https://youtu.be/i_hCaHDydqA}.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This study presents Automatic Cohort Extraction System (ACES) aiming to addresses the reproducibility in healthcare ML challenges due to the private nature of datasets and model definitions,  by providing a tool to define and reproduce ML cohorts across datasets. The tools are claimed to enable consistent cohort extraction by offering a configuration language and automatic pipeline, potentially improving reproducibility in ML studies on electronic health record data.

### Strengths
+ The study is indeed very timely and sound. It addresses a critical area of concern in ML for health, by publishing offering a pipeline to standardize common cohort extraction tasks from the health datasets.
+ The paper does a nice job of providing public and anonymized resources. 
+ The study adopts several recent prior studies, and seems to nicely complement those.

### Weaknesses
+ One major unclear aspect is providing robust evidence that the proposed tool/pipeline indeed achieves a good performance extracting the right cohort. A natural question, how one can ensure this fairly complex procedure will not miss critical samples or include incorrect ones in the final results. Is there any way to compare the results against some sort of baseline or ground truth?
+ While the paper is relatively sound and straightforward, and while some examples are provided, the whole document still seems a bit unaccessible to even an average reader. The paper stays high-level, perhaps in favor generalizability, but risks missing the readers. Here are some example ways, the paper can be further accessible. Provide more concrete examples, especially by showing the outcome cohort. Present the concept of "data stream" in a more tangible and clear way in this application. Rely less on referring too much to appendix and external links. 
+ Relatedly, the main technical contribution can be further clarified. The recursive nature of the specified algorithm seems unclear. 
+ It is suggested that subjective and not substantive statements are removed. For instance, "preliminary work on this front shows very promising results!"

### Questions
+ How the two parts of "institution-specfic" and "generalizable" work along side each other? Besides standardizing the training part of ML models, how this work helps with what's discussed in 5.3 (i.e., helping with no access to private data).

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces ACES, an open-source Python library designed for event-stream data, aimed at automating the cohort extraction process through a unified API. Users define tasks via a configuration file specifying predicates, input, trigger, gap, and target, making the system both structured and adaptable.

### Strengths
1. The paper addresses a significant barrier in healthcare ML research: the complexity of EHR data, especially in cohort extraction. The motivation is clear and relevant.
2. The authors provide an open-source Python package with thorough documentation, which will support reproducibility and benefit future research.
3. ACES is built on the MEDS format, showing potential for broad applicability across various datasets and tasks.

**Note:** I think this library could offer value to ML in healthcare by simplifying EHR cohort extraction. However, the essential factor for such tools is flexibility and support across multiple datasets and tasks. Assessing these aspects thoroughly is challenging without extensive hands-on testing, so I have adjusted my confidence rating accordingly.

### Weaknesses
A primary concern is the library’s utility for more complex tasks. For example, in the case of “CKD in diabetics within 5Y of kidney panel,” much of the effort lies in translating high-level criteria into specific medical features—a step that remains challenging and unresolved. Extracting cohorts from predefined features is relatively straightforward.

### Questions
N/A

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper introduces ACES, the Automatic Cohort Extraction System, designed to address reproducibility issues in machine learning for healthcare by streamlining task and cohort definitions in electronic health record (EHR) datasets. ACES provides a configuration language that supports dataset-specific and dataset-agnostic criteria, which enables sharing and reuse across datasets with minimal adjustments. It integrates with formats like MEDS and ESGPT, allowing users to define prediction tasks with flexibility, regardless of specific dataset schemas, and includes both Python and command-line interfaces. ACES aims to bridge gaps in interoperability, flexibility, and deep learning compatibility, potentially enhancing the reproducibility and accessibility of ML healthcare studies.

### Strengths
Overall this is a very interesting paper with some key strengths (but perhaps handicapped by some key weakness below). First considering the strengths we can identify the following

- The authors aim to improve standardization and interpretability in healthcare ML. While there have been many approaches to this including OMOP and i2b2, ACES aims to improve integration with potentially non-compliant sources by enabling reproducible task definitions across multiple datasets, which can aid in consistent benchmarking and model validation.
2. The authors propose a high level configuration language and support for Python and CLI interfaces facilitate broad adoption among researchers and compatibility with deep learning workflows. With this they aim to lower the barrier for integration
3. ACES's support for multiple data standards (like MEDS and ESGPT) and separation of dataset-specific and dataset-agnostic components allows flexible and adaptable cohort extraction across diverse clinical datasets.

### Weaknesses
Given the promising aspects, they paper can be improved upon by addressing the following

1. First, the authors may have created the classic problem of `resolving n competing standards by ending up with n + 1 competing standards`. Specifically, despite claims of flexibility, ACES requires data to be formatted in supported structures, which could necessitate pre-processing for datasets outside MEDS or ESGPT. The authors doesn't describe in details the effort in taking a new dataset and making it compliant to MEDS/ESGPT. For OMOP, the authors mention about a connector - but the authors don't discuss whether the MEDS/ESGPT transformation are exhaustive and without data loss. 
2. Next moving on to the performance and scalability, while initial results are promising, more comprehensive evaluations on larger and more varied datasets would strengthen claims about ACES's efficiency and scalability. For example the authors claim these task specific transformations are cheaper than full scale ETL of datasets, the authors doesn't discuss whether it is cheaper in the long term, especially with multiple tasks. Specifically considering the eco-system of downstream processing like OHDSI ecosystem it might be cheaper to convert to OMOP. Even for deep learning systems several efforts like https://github.com/clinicalml/omop-learn and https://github.com/BiomedSciAI/DPM360 extends the ecosystem with low barriers for integrating with OMOP systems.  
3. Finally there are some limitations currently with ACES not able to directly handle unstructured data, which limits its application scope in tasks that require insights from clinical notes or similar records.


Overall while the authors have a novel solution it is not evident they are solving the right problem or who the solution is for. Identifying these two would enable the paper to be reviewed with the full context

### Questions
Have the authors compare the effort to ETL a new dataset to an existing standard (e.g. OMOP) and model multiple downstream tasks vs their proposed method? It would be useful to compare these timings. It is also known that in some situations all elements of a new dataset may not completely map to OMOP format exhaustively - is this a problem that the authors faced and they are trying to solve this challenge? Further comparative details on this would situate the paper better

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper concentrates on enhancing the reproducibility of machine learning for healthcare research and introduces the Automatic Cohort Extraction System (ACES), a library/tool specifically developed for handling healthcare data formatted as event streams. ACES functions as a configuration language that simplifies task definitions by abstracting them into two main components: dataset-specific event predicates and dataset-agnostic inclusion/exclusion criteria. This structured approach allows ACES to support a diverse array of representative predictive tasks essential for healthcare analytics.

### Strengths
S1. The promotion of standardization and simplification in automatic cohort extraction is of considerable importance. This effort can enhance the reproducibility of machine learning applications in healthcare research. Furthermore, it has the potential to advance the digitalization of healthcare data, thereby providing substantial benefits to both clinicians and patients.

S2. The paper provides a relatively thorough overview of the current landscape of machine learning within healthcare research, including common data models, existing benchmarks, and representative applications/tasks.

S3. The ACES system is implemented as an open-source project, accompanied by comprehensive documentation.

### Weaknesses
W1. ACES primarily functions in healthcare analytics by performing preprocessing on broadly collected EHR data tailored to specific target applications, such as extracting particular features within a time window or performing aggregations. This process is ubiquitous in most EHR-related data mining tasks. ACES abstracts common dataframe transformation patterns across diverse healthcare applications, providing high-level encapsulation. Under the assumptions set by ACES, this approach simplifies the preprocessing to some extent. However, it is essential to note that this work can be seen as largely an engineering solution rooted in low-code programming concepts, with limited conceptual innovation. Additionally, it is challenging to discern any substantial transformative impact this encapsulation introduces to EHR data processing.

W2. Continuing from the previous point, ACES aims to implement a standard data extraction process for healthcare data in an event-stream format. However, the paper does not adequately articulate the specific challenges inherent to this process. This omission leaves readers uncertain of the unique problems ACES addresses, thereby diminishing the perceived contributions and impact of ACES.

W3. The paper lacks objective and quantitative evidence to substantiate the superiority of ACES over existing work aimed at solving the same research problem. This hence weakens the argument for ACES as a preferable solution in the competitive landscape of healthcare data processing and management technologies.

### Questions
Please refer to points W1 through W3 for detailed concerns and recommendations.

### Soundness
2

### Presentation
2

### Contribution
1

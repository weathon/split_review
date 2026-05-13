# ComputAgeBench: Epigenetic Aging Clocks Benchmark

- Decision: Reject
- Scores: 8, 6, 5, 6

## Abstract
The success of clinical trials of longevity drugs relies heavily on identifying integrative health and aging biomarkers, such as biological age. Epigenetic aging clocks predict the biological age of an individual using their DNA methylation profiles, commonly retrieved from blood samples. However, there is no standardized methodology to validate and compare epigenetic clock models as yet. We propose ComputAgeBench, a unifying framework that comprises such a methodology and a dataset for comprehensive benchmarking of different clinically relevant aging clocks. Our methodology exploits the core idea that reliable aging clocks must be able to distinguish between healthy individuals and those with aging-accelerating conditions. Specifically, we collected and harmonized 66 public datasets of blood DNA methylation, covering 19 such conditions across different ages and tested 13 published clock models. We believe our work will bring the fields of aging biology and machine learning closer together for the research on reliable biomarkers of health and aging.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The author introduces a benchmark designed to evaluate models of the epigenetic aging clock. The benchmark includes 66 datasets containing DNA methylation data that meet specific conditions and corresponding metadata, with a total sample size of 10,410. Four tasks are proposed to assess the models’ ability to distinguish between healthy individuals(HC) and age-accelerating conditions(ACC). Results of these four tests are summarized into Cumulative Benchmarking Score. The benchmark framework also includes 13 previously published models results.

### Strengths
The author critiques previous benchmarks for being either small in scale, limited to predicting chronological age, lacking standardized datasets, comparing only a limited number of models, or relying on mortality and disease data that have restricted access. 

The proposed benchmark seems address all of these limitations. Derived from publicly accessible data, it includes processing of data from both age accelerating condition (ACC) and healthy control (HC) groups to test model’s ability to distinguish between these conditions. Diseases with ACC are well considered. The benchmark includes 4 well-defined tasks with a summary score and evaluates 13 previously published models.

### Weaknesses
The paper is well-written and comprehensive overall, but several technical points need further clarification:

1. The selection of metrics for benchmark tasks requires more justification. Specifically, why do tasks 2, 3, and 4 report median instead of the mean? Additionally, task 4 mentions the "presence of covariate shift," but this shift is not clearly explained. Could the authors specify the covariate shift further? It would be beneficial to know if this covariate shift is consistent across all datasets used in task 4, or if it varies, and how this variability might impact the results. Furthermore, how was the presence of covariate shift determined, and what specific methods were used to detect it?

2. The rationale behind the summary benchmark score requires further explanation. Why was this scoring method chosen, and what are its advantages? Also, what does "positive bias" refer to in this context? In the Results section, it is stated that $S_{AA1}$ is adjusted by a ratio to penalize prediction bias, yet this concept of prediction bias remains unexplained. Further clarification on what prediction bias entails here would be beneficial. Specifically, how is this bias calculated, and what are the implications of this bias for the overall benchmark score? It would be helpful to see a more detailed mathematical explanation of how the bias adjustment is implemented.

3. It appears that plots C and D in Figure 3 may be incorrectly presented. Plot D should likely represent $Med(|\Delta|)$ rather than $Med(\Delta)$, as all points are above the diagonal. Please clarify if this is a mislabeling or if I have misunderstood the data shown. If the intention is to show the direction of the bias, it would be more informative to include a scatter plot of predicted age vs. chronological age, which would more clearly visualize the bias.

### Questions
Please see my questions in the above weakness section.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper benchmarks 13 different published biological clock models using a standardized test dataset that they compiled from more than 50 different publicly available studies. While no ground truth data is available for biological age (as it is a latent factor) or for age at death (as this data often isn’t published), the authors offer 4 compelling metrics by which to score the models accuracy and robustness. This paper presents a resource to the community in terms of a newly published benchmarking dataset, well-motivated metrics, and ratings for the current state of the art clock models. The paper also appropriately outlines limitations, such as the fact that some datasets had poor performance across all models, raising questions about dataset shift and for what kinds of data the clocks can be expected to make sound predictions. I believe this paper will help generate scientific discussion and progress in the aging clocks research community.

### Strengths
- This paper is written very clearly, and did a great job walking the reader through the background to the problem, definitions of biological age, and different kinds of biological clock models. It’s graphics are informative, clear, and aesthetic. Truly a pleasure to read! 
- Provides colab notebook for reproducibility
- I believe this paper will be significant to those in the biological clocks community. It is a benchmarking paper, so while it doesn't offer a new methodology itself, it does offer original tasks/metrics for assessing the performance of these models (I think they are original, I asked for clarification in the questions section) and a standardized benchmarking dataset (I asked for clarity to confirm it will in fact be published along with this paper)

### Weaknesses
 - I was disappointed that the clock models weren't all re-trained on a standardized training dataset. Without standardizing the training data, it is impossible to know whether the methodology of the clock or the training data it used are contributing to better/worse performance. This insight would be critical to the community in improving clock methodologies going forward.
- The way that the authors chose to combine benchmarks in the cumulative score requires more justification. I am not sure why the different metrics should affect each other's weights so much. A simple sum, or weighted sum, of the four variables might be more appropriate if stronger justification is not supplied.
- Requires clarification: on the one hand, authors write "Clearly, the first task [AA1] provides a more rigorous way to test aging clocks [compared to AA2]" on the other hand, they write "The most rigorous of the four, AA2 task demonstrates..."
- Your description of the biomarker paradox could be improved. When I first read your description, I was left with questions. I had trouble finding more info on the "paradox of biomarkers" using the papers you cited (possibly due to paywall issues, I couldn't see the full articles), but you might consider adding this reference _Sluiskes, Marije H., et al. "Clarifying the biological and statistical assumptions of cross-sectional biological age predictors: an elaborate illustration using synthetic and real data." BMC Medical Research Methodology 24.1 (2024): 58._ as their explanation made me fully understand the problem, namely that "a (bio)marker that perfectly correlates with chronological age is useless in estimating biological age... in principle a nearly perfect chronological age predictor can be developed, as long as the sample size is large enough [35]. In such a case all signal related to biological aging would be lost."

More broadly, while I really enjoyed the paper, I am not sure it is a great fit for the ICLR community, as this model is a predictive regression model and not in the space of representation learning.

### Questions
- Will you make your benchmarking dataset publicly available? Can you please add a link to it in your manuscript? I view this benchmarking dataset as a significant portion of your contribution in this work.
- Can you please confirm that your evaluation tasks/metrics are original, and add citations if not?
- Can you make a case for why the paper is a strong fit for ICLR, despite not truly being in the representation learning space?

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The authors present a benchmark study where they contrast different computational methods, namely aging clocks, for inferring biological age from epigenetics (methylation) data. A corpus of datasets relevant for the benchmark was built through a systematic search, and it is provided as a resource. Finally, the evaluation was performed on four different tasks, devised in such a way to capture different aspects of aging clocks' performances.

### Strengths
The benchmark is well structured: (i) a variety of datasets and methods are included, and (ii) the tasks upon which the methods are evaluated are well defined and relevant for the domain. Furthermore, such type of benchmarks are quite timely, due to a continuously growing list of available aging clocks.

### Weaknesses
My main criticism is that the paper is only marginally relevant with respect to the topics of the conference. Inferring the biological age of an individual can hardly be considered as learning representations. The machine learning methods used for deriving aging clocks are very well known and established, thus lacking novelty. The tasks presented in the paper to assess the clocks' performances are not totally novel, as the authors themselves point out in section 2.2.

From a technical point of view, an important aspect that the paper does not address is preprocessing. Several normalization methods exist for methylation data, and their impact to downstream analysis is well documented (see for example Teschendorff et al. 2013). A robust benchmark should try to evaluate the effect of different normalization methods on aging clock performances.

A minor issue the authors may want to consider: the long list of reference at page 6 could be placed in the appendix, to ease reading

### Questions
I would like to ask the authors to address the two main criticisms I listed in the "weaknesses" section:
- Overall, the opinion of this reviewer is that while the work has undoubtedly merit, it would be better suited for a forum more specific to biological age and aging clocks. 
- Regarding the normalization of methylation data, I would invite the authors to at least discuss whether the preprocessing of the included datasets match the recommended preprocessing of each aging clock (if any).

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper proposes ComputAgeBench, a unified framework and benchmark dataset for evaluating epigenetic aging clocks, which are predictive models for estimating biological age based on DNA methylation data.  The framework aggregates 66 public datasets covering 19 aging-accelerating conditions, along with 13 published epigenetic clock models, to assess model performance consistently across a standardized dataset. The methodology incorporates rigorous evaluation criteria to test each model’s ability to distinguish between healthy individuals and those with accelerated aging conditions.

### Strengths
### Strengths 

 The paper is clear and well-written, providing a solid foundation for its contributions. It presents a unified framework for evaluating epigenetic aging clocks, covering both first- and second-generation clocks. By introducing a benchmark dataset, the authors enable comprehensive testing of multiple epigenetic clock methods. 

This work has potential to significantly impact the field of biological aging, as it offers a standardized dataset that can facilitate consistent evaluation across various epigenetic clock methods. Such a resource will likely streamline method comparison and improve reliability in aging research.

### Weaknesses
In reviewing the proposed benchmark in this paper, several key areas for improvement have emerged, particularly concerning data diversity, balance, and bias.



### Weaknesses



1. **Limited Report on Data Diversity**: The paper lacks adequate details on demographic and biological diversity, such as age, ethnicity, and health variations. Including these would improve the dataset's representativeness for broader applications. Specifically, the paper does not provide a clear breakdown of the distribution of these factors across the 66 datasets, making it difficult to assess the overall diversity and potential confounding effects. For instance, the number of samples from different ethnicities or age groups within each aging-accelerating condition (AAC) is not clearly stated, hindering a thorough evaluation of the dataset's composition.


2. **Data Balance and Bias**: The authors do not address balance across categories (e.g., AACs vs. healthy controls) or potential sampling biases. This oversight may skew benchmarking results and limit generalizability. The lack of information on how the data was collected and processed within each study makes it difficult to assess potential biases. For example, if certain AAC groups are overrepresented or if the healthy control groups are not well-matched to the AAC groups in terms of age or other relevant factors, the benchmark's validity is compromised. The paper should include a detailed analysis of sample sizes and distributions across all categories to ensure that the benchmark is not biased towards specific conditions or demographics.


3. **Absence of Bias Mitigation**: No strategies are mentioned to detect or reduce dataset biases, which is crucial for fair benchmarking in aging prediction models, where demographic factors can affect DNA methylation patterns and model performance. Additional evaluation metrics for fairness would  increase the strength of this benchmark. The paper should discuss methods to identify and mitigate biases, such as using fairness-aware metrics or re-weighting samples to address imbalances. Without these considerations, the benchmark may inadvertently promote models that perform well on biased data rather than those that generalize well across diverse populations. Furthermore, the paper does not discuss how batch effects from different studies were handled, which is a critical factor in DNA methylation data analysis.


4. **Put Together Publicly Available Dataset**: The proposed dataset, to my understanding,  is a collection of existing publicly available datasets. The authors do not present to the research community a new benchmarking dataset, they rather collect existing datasets that they put together with a published harmonization technique.  

The fact that the datasets already exist publicly, reduces the novelty of the benchmark. However, I cannot ignore that putting together 66 datasets  into a single dataset is a contribution that would facitilitate the comparison of epigenetic clock methods.

### Questions
### Questions for the Authors

In evaluating the dataset and methodology presented, several questions arose that could help clarify the dataset’s potential applications and limitations.

1. **Applicability for Method Development**: Can this dataset be effectively used for developing new methods on epigenetic aging clocks, or is it primarily intended for benchmarking and evaluation? Are there features or structures in the dataset that support novel method exploration?

2. **Data Diversity and Representativeness**: How does the dataset account for demographic and biological diversity? Could the authors provide more details on the inclusion criteria to ensure the dataset is representative of a broad population?

3. **Addressing Balance and Bias**: Were any steps taken to balance the dataset across aging-accelerating conditions (AACs) and healthy controls, or to mitigate known biases in the sample selection process?

### Soundness
3

### Presentation
3

### Contribution
2

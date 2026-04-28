# Ensuring Fair Comparisons in Time Series Forecasting: Addressing Quality Issues in Three Benchmark Datasets

- Decision: Reject
- Avg Score: 4.25
- Scores: 3, 6, 5, 3

## Abstract
Time series forecasting (TSF) is critical in numerous applications; however, unlike other AI domains where benchmark datasets are meticulously standardized, TSF datasets often suffer from data inconsistencies, missing values, and improper temporal splits. These issues have an impact on model performance and evaluation. This paper addresses these challenges by proposing inconsistency-free versions of three well-known TSF datasets. Our methodology involves identifying and correcting data inconsistencies using a combination of linear interpolation and context-aware imputation strategies. Additionally, we introduce a novel cycle-inclusive data splitting method, which respects the longest cycle in each dataset, ensuring that models are evaluated over meaningful temporal patterns. Through extensive testing of multiple transformer-based models, we demonstrate that our revised datasets and cycle-inclusive splitting lead to more accurate and interpretable forecasting results, as well as fairer comparison of TSF models. Finally, our findings highlight the need for proper dataset refinement and tailored data splitting strategies in TSF tasks, and pave the way for future work in the development of more robust forecasting benchmarks.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper proposes three new benchmark datasets for time series forecasting. The proposed datasets aim to address data inconsistencies, missing values and improper temporal splits, facilitating fair evaluations for methods designed for forecasting task.

### Strengths
1)  Creating comprehensive and accurate benchmark dataset, especially for time series analysis, which is of high real-world importance is a critical and important task.

2) The paper conducts extensive experiments

### Weaknesses
1) The contribution of the paper is incremental, as it applies existing methods to three established datasets to create new benchmarks. The limitations of current benchmark datasets are well-known, and various solutions have already been developed to address these issues. However, the paper does not sufficiently articulate how the specific combination of data cleaning and temporal splitting techniques employed here constitutes a significant advancement over existing practices. The paper should provide a more detailed analysis of the novelty of their approach and how it differs from existing data preprocessing pipelines used in time series forecasting.

2) The paper lacks a systematic method for creating benchmark datasets, which limits its applicability. This raises the question: can the approach presented in the paper be applied to any existing dataset to establish it as a fair benchmark? The paper does not provide a clear methodology or guidelines for applying their approach to new datasets. The reliance on domain expert knowledge is a significant limitation, as it makes the process difficult to generalize and replicate. A more formalized approach, perhaps involving a set of objective criteria or automated checks, would be beneficial.

3) As noted in the paper, the approach relies heavily on domain expert knowledge, which limits its broader applicability. Additionally, if domain knowledge is to play a significant role, it could also be used to design new benchmark datasets. The paper should discuss the trade-offs between using domain knowledge for data cleaning versus using it for dataset creation. The current approach seems to prioritize cleaning existing datasets, but the paper does not adequately justify why this is superior to creating new, purpose-built datasets.

4) Given the limited novelty and the real-world application of the paper, I believe the paper may be a better fit for a benchmark track.

### Questions
1) Can the approach presented in the paper be applied to any existing dataset to establish it as a fair benchmark?

### Soundness
2

### Presentation
1

### Contribution
1

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper motivates the need for high quality datasets in benchmarks of Time Series Forecasting models, and through careful data analysis, provide cleaned versions of 3 datasets. By comparing existing models on the new datasets, they establish the importance of the dataset version on method relative performances.

### Strengths
1) Extensive data analysis is systematically presented in Appendix, analyzing seasonality in a multivariate context. This is precious for practitioners looking to analyze models on such datasets.
2) The task of providing clean datasets to the forecasting community is both significant and difficult, as currently each new paper benchmarks previous work in its own fashion. Standardizing training-validation-test split via data analysis is valuable in such a context.
3) Code, datasets, and figures are provided and well structured.

### Weaknesses
1) There is overall very few citations in introduction, section 2.1, section 2.3 and section 3. 
The paper makes claims on the general approaches to data processing (eg line 147). Additionally, the paper tracks variants of the three datasets through different papers. Overall, the first four pages are about existing works, concerns and approaches, yet few citations and no paper collection methodology are presented.
2) The main paper version is very vague on the proposed data correction methods. The protocol for FFT application was described in Appendix, but this would be better included in the main paper. Imputation on the other hand appears simplistic. It would be for the best if the paper could try or discuss other methods and why specifically linear interpolation and neighbourhood average should be chosen. Surveys: https://arxiv.org/abs/2402.04059, https://arxiv.org/abs/2011.11347
3) Three different methods might not be enough to see strong changes on method ranking. Additionally, 3 runs is insufficient to provide confidence on results significance.

### Questions
Seeing the correlation analysis results, would the authors say that correlation analysis is useful to measure dataset quality? I could not come to a conclusion, but I did not spend much time comparing the original and corrected plots.

(Appendix, 1870, "we can observe" and not "we can observed", this one caught my eye). As most of the paper/appendix is text without formulas, I suggest going through a spell and grammar checker.

Is there any way to measure seasonal differences on the ECL dataset?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a solution to address inconsistencies and unreasonable data splits in time series forecasting evaluation, facilitating more accurate assessments.

### Strengths
As far as I know, data inconsistency is a common issue. The use of imputation in this paper is reasonable. The paper provides comprehensive experiments comparing the original datasets with the revised ones.

### Weaknesses
1. **Generality of the problem:** The paper discusses inconsistencies and data splitting issues using only three datasets. Are these issues commonly observed across other datasets?  It is unclear if the identified inconsistencies are isolated incidents or a widespread problem affecting many time series datasets. The lack of analysis on a broader range of datasets makes it difficult to assess the generalizability of the findings and the practical impact of the proposed solution.
2. **Real-world significance:** While I agree that data inconsistency is relevant in practice, I disagree with the periodic splitting approach. As far as I know, most real-world time series applications [1-2] do not align with periodic splitting settings.  The paper's focus on periodic splitting, while useful for benchmarking, does not reflect the common practice in real-world time series forecasting where data is often split based on a continuous time window, making the practical relevance of the proposed approach questionable.
3. **Lack of related work discussion:** Many studies have discussed time series forecasting (TSF) benchmarking. At least, [3] also aim s to fair evaluation. The authors should discuss the difference in motivation and in evaluation results.  The paper fails to adequately discuss existing literature on time series benchmarking, particularly those focused on fair evaluation. This omission makes it difficult to position the contribution of this work relative to the current state-of-the-art.
4. **Limited novelty and dataset contribution:** Overall, I have concerns about the novelty of this work. Imputation is a common preprocessing technique, and the rationale for periodic splitting requires further discussion. From a dataset perspective, only three datasets are processed, and the benchmarking uses very few methods. The use of imputation, while reasonable, is not a novel contribution. The limited number of datasets and forecasting methods used in the experiments further restricts the impact and generalizability of the findings.

### Questions
Please check limitations.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper advocates for standardizing multivariate time-series forecasting evaluation, by removing inconsistencies and missing values, and by splitting data with cycle-preserving ratios. It further manually analyzes and releases cleaned versions of three commonly used datasets, and compares three recent models (NLinear, Informer and iTransformer) on them.

### Strengths
The paper tackles an **important problem**, the problem of ensuring a reliable, reproducible and consistent evaluation of time-series models.
The contributions are clearly stated, and I agree that the time-series community would benefit from standardized pre-processing and evaluation.

### Weaknesses
The paper tackles an **important problem**, the problem of ensuring a reliable, reproducible and consistent evaluation of time-series models.
The contributions are clearly stated, and I agree that the time-series community would benefit from standardized pre-processing and evaluation.

**The paper falls short in its analysis** of the impact of lack of standardization, for the following reasons:
1. It considers only three datasets, while evaluations are commonly carried out with many more datasets, as listed in Table 1 in the supplementary material. The same analysis and proprocessing should be carried out at least on the 10 most commonly used dataset for the work to have a real impact.
2. The paper’s evaluation of Section 6 does not highlight any worrying problems with using the publicly available versions of the datasets. For instance, model rankings do not change when comparing models on the old dataset versions and when comparing them on the newly proposed versions, and in general model's performance is not significantly impacted by the standardization. More strikingly, models look equally impacted by the changes which hinders the claim that current evaluation practices are not fair.
3. The paper’s evaluation of Section 6 does not provide new insights into model performance, e.g., their weaknesses and strengths wrt capturing cycles, multivariate relationships, robustness to noise, and other factors that can impact performance.
4. Only three and very recent models are considered, while there exists an extensive literature on the time-series forecasting, see e.g., survey [1].

**The proposed methodology is not original**, as it encompasses commonly used techniques, such as interpolation for missing value imputation and spectral analysis for cycle detection.
It is also heavily relies on expert knowledge and visual inspection, which hinders its applicability to new datasets.

**The work is not well positioned with respect to existing literature on standardizing time-series forecasting evaluation**. There exist at least two works, and related libraries [2][3], that provide access to standardized model implementations and datasets to facilitate a reliable, reproducible and consistent evaluation. How does the paper differ and improve upon these works?


[1] Dama, Fatoumata, and Christine Sinoquet. "Time series analysis and modeling to forecast: A survey." arXiv preprint arXiv:2104.00164 (2021).
[2] Wang, Yuxuan, et al. "Deep time series models: A comprehensive survey and benchmark." arXiv preprint arXiv:2407.13278 (2024).
[3] Alexandrov, Alexander, et al. "Gluonts: Probabilistic and neural time series modeling in python." Journal of Machine Learning Research 21.116 (2020).

### Questions
1. Two cleaned versions of the datasets are proposed. Which ones should the community use? In the effort of standardizing evaluation, it is confusing to release more than a single version.
2. Cycle-preserving splits are motivated to ensure train, validation and test sets are representative of the data distribution. This however does not account for shifts, which also create discrepancies. How should they be handled? 
3. Releasing a library is a convenient way of ensuring that pre-processing and evaluation are automatically standardized. Is there a particular reason why the authors decided not to provide one?

### Soundness
1

### Presentation
3

### Contribution
2

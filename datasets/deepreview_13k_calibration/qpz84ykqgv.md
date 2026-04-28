# EarthquakeNPP: Benchmark Datasets for Earthquake Forecasting with Neural Point Processes

- Decision: Reject
- Avg Score: 5.25
- Scores: 6, 6, 3, 6

## Abstract
Classical point process models, such as the epidemic-type aftershock sequence (ETAS) model, have been widely used for forecasting the event times and locations of earthquakes for decades. Recent advances have led to Neural Point Processes (NPPs), which promise greater flexibility and improvements over classical models. However, the currently-used benchmark dataset for NPPs does not represent an up-to-date challenge in the seismological community since it lacks a key earthquake sequence from the region and improperly splits training and testing data. Furthermore, initial earthquake forecast benchmarking lacks a comparison to state-of-the-art earthquake forecasting models typically used by the seismological community. To address these gaps, we introduce EarthquakeNPP: a collection of benchmark datasets to facilitate testing of NPPs on earthquake data, accompanied by a credible implementation of the ETAS model. The datasets cover a range of small to large target regions within California, dating from 1971 to 2021, and include different methodologies for dataset generation. In a benchmarking experiment, we compare three spatio-temporal NPPs against ETAS and find that none outperform ETAS in either spatial or temporal log-likelihood. These results indicate that current NPP implementations are not yet suitable for practical earthquake forecasting. However, EarthquakeNPP will serve as a platform for collaboration between the seismology and machine learning communities with the goal of improving earthquake predictability.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors have presented EarthquakeNPP, a group of datasets designed to evaluate/benchmark NPP models for earthquake forecasting. The authors evaluate some state-of-the-art NPP-based models against ETAS and have identified that these models demonstrate comparable temporal performance with the ETAS  model. Based on their analysis, the authors note that NPP-based models do not have a direct dependence on magnitude, in contrast to ETAS.

### Strengths
**Originality**: While all the datasets are already available, the authors have created a pipeline and baseline and state-of-the-art methods and evaluation metrics to formalize the process of evaluating earthquake forecasting methods. Standardizing the evaluation method by comparing against the ETAS method that is used in the real world is a good idea.

**Significance**: The dataset collection created by the authors can serve as a benchmark for future research in NPP-based earthquake forecasting models. The authors have highlighted the limitations of existing benchmark datasets and why they need to be improved. 

**Experiments**: The authors have also provided initial assessments of state-of-the-art NPP-based models and highlighted the limitations of existing methods.

### Weaknesses
Clarity:
1. Section 1.1 The three categories defined in related work are hard to follow. A table highlighting the differences/limitations, or better defining the categories would help. For instance, "benchmarking efforts by NPP/ML community" , "benchmarking efforts by seismology community" etc. The existing benchmark dataset can then go into the first category. 
2. Section 5: Since each of the three tests is aimed at evaluating the temporal, spatial, and magnitude components of the forecast, renaming section 5.1 to "temporal test" is suggested. The current name, "Number test" is not descriptive enough.
3. Section 3 is better summarized as a table and includes additional information such as the number of training, validation, and test data. (This is currently included in the anon. github README). Additionally, the strengths/weaknesses/challenges of each dataset can be elucidated in this format, allowing the user to understand how each dataset is different from the other. Specifically, the temporal and spatial resolution of each dataset should be included.
4. From the title, it seems as if the dataset is purely for benchmarking NPP-based methods, which might narrow the scope of the dataset. What needs to be done to generalize it for other methods capable of generating log-likelihoods such as bayesian inferencing-based methods?

### Questions
1. Is it possible that since ETAS was trained using both training + validation data while the NPP models were trained on the training data, it is performing better? What is the impact of training data size on the evaluated models? Please conduct experiments such as evaluating ETAS using only training data.
2. Including a comparison of model complexity of the NPP-based models vs ETAS models in the evaluation metrics would be of great importance.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This work introduces EarthquakeNPP, a benchmark dataset for earthquake forecasting using Neural Point Processes (NPPs), aiming to enhance existing models. It covers seismic records from 1971 to 2021 in various California regions, including timestamps, coordinates, and magnitudes. Comparing NPPs with the ETAS model, it finds that current NPP implementations do not outperform ETAS in spatial or temporal log-likelihood, indicating that NPPs are not yet ready for practical earthquake forecasting. However, EarthquakeNPP serves as a platform for collaboration between the seismology and machine learning communities to improve predictability.

### Strengths
(1) The dataset spans multiple regions in California over an extended period and includes earthquakes of various magnitudes, including smaller ones. This enhances data diversity and increases the dataset's granularity.

(2) It provides a direct comparison with the popular ETAS model, promoting collaboration between the seismology and machine learning communities.

(3) By utilizing modern seismic detection technologies, the dataset offers improved data quality.

### Weaknesses
 (1) The application of NPPs in practical earthquake forecasting is limited. For example, the high computational cost of generating repeated sequences may hinder real-world applications. I noticed that you used four A100 GPUs for training. Have you conducted any computational complexity analysis, such as comparing the training times between the baseline and NPPs? If you have other ways to present the computational cost, please include them as well.

(2) This work lacks sufficient detail on the reproducibility of experimental results, which may affect other researchers' ability to replicate the study. For instance, issues with the division of training and testing data in the existing NPPs benchmark dataset may prevent an accurate reproduction of real operational environments. Additionally, the interpretation of experimental results relies heavily on statistical data, lacking an in-depth analysis of the underlying physical mechanisms.

### Questions
Refer to weaknesses

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
The paper introduces EarthquakeNPP, the benchmark datasets designed to evaluate neural point processes (NPPs) for earthquake forecasting. It compiles earthquake data from California spanning 1971 to 2021 for model assessment. The study highlights that current NPP methods are not yet practical for real-world applications, as none outperform the Epidemic Type Aftershock Sequence (ETAS) model in terms of spatial or temporal log-likelihood performance.

### Strengths
1. The work highlights the gap between the seismology and machine learning communities in earthquake prediction, providing potential directions for future development of neural point processes (NPPs) to improve earthquake forecasting.
2. It gathers earthquake data from California from 1971 to 2021, creating a valuable resource for research in both seismology and machine learning.
3. The benchmark datasets and experiments are publicly available, facilitating further research in the field.

### Weaknesses
1. The scope of the work is limited. While the paper focuses on NPPs, various deep learning methods [1, 2] can also be applied to earthquake prediction. Including these methods would enhance the comprehensiveness of the evaluation.

2. The paper employs log-likelihood as the evaluation metric. Including metrics such as MAE and accuracy would offer a more comprehensive assessment from multiple perspectives.

3. The description of the benchmark dataset's statistics and characteristics is insufficient. A more detailed analysis, including aspects such as spatial nodes, the evolution of seismic activity, and the pattern similarity between training and testing earthquakes for each dataset, would strengthen the paper.

4. The analysis of model performance is limited. For example, why does Deep-STPP generally perform best in terms of temporal log-likelihood, while AutoSTPP excels in spatial log-likelihood?

5. Terms such as SCEDC_20, SCEDC_25, and SCEDC_30 are unclear and need clarification.

6. The paper's structure is somewhat inconsistent, with descriptions of additional datasets provided without corresponding results in the main text.

### Questions
1. Why does the paper focus only on neural point processes and exclude other model types? 
2. Could you justify the use of log-likelihood as the primary metric while excluding other metrics such as MAE and R-score? 
3. Could you provide a more detailed description of the benchmark dataset's statistics and characteristics? 
4. Could you clarify the meaning of dataset labels such as SCEDC_20, SCEDC_25, and SCEDC_30? Do these refer to SCEDC data with magnitude thresholds of 2.0, 2.5, and 3.0, respectively?
4. Is there experimental evidence indicating that the degraded performance of NPPs compared to ETAS is due to their lack of direct dependence on magnitudes, rather than other factors?

### Soundness
1

### Presentation
1

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper constructs a benchmark dataset for earthquake forecasting using machine learning. It constructs datasets of various periods, regions, and sizes and provides an evaluation method for them. It presents the results of predicting the dataset using the epidemic-type aftershock sequence (ETAS), a classical prediction method, and three Neural Point Processes (NPPs) models.

### Strengths
- Provides data over a more extended period of time, a wider area, and a wider variety of magnitude than existing benchmark datasets.
- The process of constructing the dataset was specifically explained. (Data period, scale, characteristics of each institution's data and etc.)
- The differences between the existing deep learning data split setting and the existing method were well explained.
- Various seismic domain-related experiments were conducted, such as number test, spatial test, and magnitude test.

### Weaknesses
 - An analysis should be added on which period, time, and location the NPPs models predicted accurately/inaccurately (Qualitative results).

- It would be better to provide specific experimental results or references rather than “Since the NPPs lack any direct dependence on magnitudes” as the reason why NPPs perform worse than ETAS. The claim that NPPs lack direct dependence on magnitudes needs further justification, as some NPP models can incorporate magnitude information through various mechanisms, such as embedding layers or conditional intensity functions. Without specific experiments or references, this claim is speculative.

- If a new methodology appropriate for the task is proposed through the above analysis, it would be a better study.

- It would be good to organize the advantages more useful in the machine learning community than the existing benchmark datasets and present them in a table.

- Adding real-world earthquake forecasting and response scenarios using NPPs will improve applicability.

### Questions
- Can you explain the specific benefits of using classic ETAS compared to NPPs or other machine learning methods? For example, how do they differ in terms of computational load, efficiency, and cost? It would also be helpful to include the motivation for why solving this task with machine learning methods could be beneficial.
- Is there a technical reason for applying only NPPs among the various machine learning methodologies? It would be helpful if you could justify the choice of NPPs by providing a direct technical comparison with other machine learning methods. 
- Have there been any previous studies, or do you have any experimental results, that applied other machine learning methods (e.g., spatio-temporal methods) besides NPPs?

### Soundness
2

### Presentation
3

### Contribution
2

# Merlin: Multi-View Representation Learning for Robust Multivariate Time Series Forecasting with Unfixed Missing Rates

- Decision: Reject
- Avg Score: 4.50
- Scores: 3, 6, 6, 3

## Abstract
Multivariate Time Series Forecasting (MTSF) aims to predict the future values of multiple interrelated time series and support decision-making. While deep learning models have attracted much attention in MTSF for their powerful spatial-temporal encoding capabilities, they frequently encounter the challenge of missing data resulting from numerous malfunctioning data collectors in practice. 
In this case, existing models only rely on sparse observation, making it difficult to fully mine the semantics of MTS, which leads to a decline in their forecasting performance. Furthermore, the unfixed missing rates across different samples in reality pose robustness challenges. To address these issues, we propose Multi-View Representation Learning (Merlin) based on offline knowledge distillation and multi-view contrastive learning, which aims to help existing models achieve semantic alignment between sparse observations with different missing rates and complete observations, and enhance their robustness. On the one hand, we introduce offline knowledge distillation where a teacher model guides a student model in learning how to mine semantics from sparse observations similar to those obtainable from complete observations. On the other hand, we construct positive and negative data pairs using sparse observations with different missing rates. Then, we use multi-view contrastive learning to help the student model align semantics across sparse observations with different missing rates, thereby further enhancing its robustness. In this way, Merlin can fully enhance the robustness of existing forecasting models to MTS with unfixed missing rates and achieves high-precision MTSF with sparse observations. 
Experiments on four real-world datasets validate our motivation and demonstrate the superiority and practicability of Merlin.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper presents multi-view representation learning based on offline knowledge distillation and multi-view contrastive learning.  The key idea is to achieve semantic alignment between sparse observations with different missing rates and complete observations and enhance their robustness. The experimental results demonstrate the effectiveness of the proposed method.

### Strengths
* The paper is organized.
* Time series forecasting with missing values is an important problem to study and the proposed method is technically sound.
* The experiment results showed the effectiveness of the proposed method.

### Weaknesses
 * The technical novelty is limited as this paper simply combines knowledge distillation and multi-view-based contrastive learning based on STID framework (which is also existing). From the application perspective, the proposed combination is somewhat reasonable.
* The motivation for this study is not clear (see questions below).
* Certain details about the proposed method are not provided  (see below questions).

### Questions
1. It seems the authors focus on studying high missing rates (more than 50%) for time series forecasting. However, it is not clear whether this is practical in real-world applications. Can you give a few examples of this setting? What’s the typical reason for such high missing rates?
2. It seems like the paper focuses on uniformly random missing situations. I wonder whether the proposed method also works for other types of missing, e.g., missing not at random /structural missing?
3. How do you set up the model training? Did you put 50%, 75%, and 90% missing rates in the student model to train one unified student model for different missing rates?
4. In Eq (4), I wonder whether the current weights are optimal ones

Minor suggestions:
1. Notations should be provided in the main context to make it self-contained.
2. Standard deviations are not provided in the experiment results.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper addresses time series forecasting with missing data by proposing a knowledge distillation approach to align hidden representations and forecasting results derived from both complete and incomplete data. To enhance robustness across varying missing rates, a contrastive loss is introduced, constructed using positive pairs with differing missing rates and negative pairs at different time point. Empirical experiments demonstrate the effectiveness of the proposed method.

### Strengths
- **Clear logic of the method** The paper has a clear presentation of the logic behind the proposed method.
- **Intuitive method**: The proposed approach is intuitive and easy to follow.
- **Clear ablation study**: The ablation study is thorough, clearly demonstrating the effectiveness of each component of the proposed method.

### Weaknesses
 - **Vague description of key notations and definitions**: Two crucial components of the loss function are vaguely defined, making it challenging for others to reimplement the method based solely on the method description.

  - Knowledge distillation: The teacher model is trained on complete observations, while the student model is trained on missing observations. However, the authors should clarify what constitutes a "complete observation" versus a "missing observation." Given that the focus is on time series with missing data, it is unclear if or how truly complete observations are available.

  - Contrastive learning: The definitions of positive and negative pairs are too vague and should be explicitly defined using the established notations. This would enhance clarity and replicability.

- **Vague description of method details** The missing rates for the input in student model is not clearly described and hence is diffiult to see how robust the proposed method extrapolation to other unfixed missing rates.

### Questions
- **Method** 
  - It appears that the loss functions may be defined using sliding windows on the time series. If so, it would be helpful to discuss how the size of the sliding window might impact the results.
  - The state space model [1] can effectively handle missing data. Why not consider using this model directly for forecasting in this setting?

- **Experiment**
  - Several related works mentioned in the literature review are not included in the experimental comparisons. Is there a reason for this omission?
  - How significant is the improvement of the proposed method compared to STID+GATGPT?
  - The experiments assume a "missing completely at random" pattern, but other patterns—such as "missing at random" or "missing not at random"—could yield different results. For example, what would happen if only observations above a certain threshold were missing?
  - The selected missing rates in the experiments are relatively high. How does the proposed method perform with lower missing rates? Additionally, perform forecasting when the majority of the data seems unreasonable in practice, it would be insightful to discuss how realistic this setting is.

- **Writing improvement**
  - Please refer to comments in the "Weaknesses" section for clarity improvements.
  - The LaTeX formatting in the equations could be improved for consistency and readability; for instance, in (8), use \log for log, and apply \left(...\right) for brackets within the log term.
  - Key definitions and notations should ideally be included in the main text rather than the appendix. If space is constrained, consider compressing the related work section.
  

References

[1] Efficiently Modeling Long Sequences with Structured State Spaces

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces Merlin, a robust Multi-View Representation Learning approach for multivariate time series forecasting with unfixed missing rates. This method leverages offline knowledge distillation and multi-view contrastive learning to enhance the robustness of forecasting models, particularly when sparse observations with varying missing rates are present. By aligning the semantic interpretation between sparse and complete observations and across different missing rates, Merlin significantly improves forecasting accuracy and robustness.

### Strengths
1.  The introduction of Merlin, which combines offline knowledge distillation with multi-view contrastive learning, is innovative. This framework efficiently addresses the challenge of unfixed missing rates in multivariate time series data, which is a common real-world issue.
2. The paper thoroughly validates the approach using four real-world datasets, demonstrating Merlin's superiority over existing models and imputation methods.
3. The results show that Merlin consistently outperforms traditional forecasting and imputation methods across different datasets and missing rates. This improvement highlights the ability of Merlin to handle the complexity and variability of real-world data effectively.

### Weaknesses
1. The experiment only includes 12 steps of forecasting results. It can be convincing to include different step settings such as 6 or 24.
2. I have some concerns about the two-stage settings. To ensure fairness, should we keep the teacher and student models with the same architecture? I'm also interested in whether switching backbones and applying Merlin could improve forecasting with missing data.
3. The paper could benefit from a deeper exploration of scenarios where Merlin might underperform, such as extremely high missing rates or particular types of time series data that do not conform to the assumptions made by the model.

### Questions
Minor typo: 
1. Line 86 require reconstructing reconstruct

### Soundness
3

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
This paper deals with multivariate time series forecasting (MTSF) with missing values and different missing rates. The paper proposed an interesting method called Merlin, which incorporates offline knowledge distillation and multi-view contrastive learning in the spatio-temporal identity embedding (STID) architecture. The idea of Merlin is not dependent on the STID architecture and can be transferred to any other models. Merlin learns better semantics from sparse observations using offline knowledge distillation. Merlin comprises a teacher and a student network, both based on STID architecture, where the teacher is trained with complete observations and the student is trained with sparse ones. The distillation loss between the teacher and student network helps the student network learn better semantics from the sparse observations. Merlin is further aided by multi-view contrastive learning, which helps the student network align semantics across sparse observations with different missing rates.

### Strengths
1. Merlin is an interesting approach to remove the need for imputation in MTSF.
2. The authors, to some extent, demonstrate the problem with imputation models as the missing rate increases in the data. This is an important insight to present experimentally, which can benefit the field of MTSF.
3. The writing of the paper is straightforward and easy to follow.

### Weaknesses
## Review

### summary:
 This paper deals with multivariate time series forecasting (MTSF) with missing values and different missing rates. The paper proposed an interesting method called Merlin, which incorporates offline knowledge distillation and multi-view contrastive learning in the spatio-temporal identity embedding (STID) architecture. The idea of Merlin is not dependent on the STID architecture and can be transferred to any other models. Merlin learns better semantics from sparse observations using offline knowledge distillation. Merlin comprises a teacher and a student network, both based on STID architecture, where the teacher is trained with complete observations and the student is trained with sparse ones. The distillation loss between the teacher and student network helps the student network learn better semantics from the sparse observations. Merlin is further aided by multi-view contrastive learning, which helps the student network align semantics across sparse observations with different missing rates.

### soundness:
 2

### presentation:
 1

### contribution:
 2

### strengths:
 1. Merlin is an interesting approach to remove the need for imputation in MTSF.
2. The authors, to some extent, demonstrate the problem with imputation models as the missing rate increases in the data. This is an important insight to present experimentally, which can benefit the field of MTSF.
3. The writing of the paper is straightforward and easy to follow.

### weaknesses:
 **Major Comments:**
1. The paper argues that the performance of baseline models declines substantially as the missing rate increases, as illustrated in Figure 1. However,
    1. It is difficult to compare the models in Figure 1(a) in terms of the decline value. For example, what is the decline in performance for STID+SPIN compared to MERLIN from 50%$ to 75% and 75% to 100%? It looks very close in Figure 1(a). It seems that the percentage decline of STID+SPIN is smaller compared to MERLIN from 75% to 100%. Please provide the exact decline percentage somewhere in the paper, even if it is in the supplementary. 
    2. Is there any specific reason for the chosen baseline models presented in Figure 1(a)? As shown in Table 1, STID+GATGPT and STID+MAE are better baselines in terms of performance. Why weren’t they considered for the comparison in Figure 1(a)?
    3. This observation is only shown in one dataset, PEMS04. Can the authors also present a similar trend in at least one more dataset? Showing a conclusion in only one dataset is not convincing.
2. The author mentions about two recent baseline methods in related works [1, 2] in Lines 147 and 155. However, Merlin is not compared against them. Why?
3. In the last line of section 2.2, the author mentions, “As a result, the student model’s ability to mine key semantics from sparse observations is effectively enhanced.” To support this statement, the author cites some papers. Among them, the author argues that [3] and [4] show satisfactory results using knowledge distillation even with 50% and 25% observations, respectively. If I am not wrong, [3] and [4] show their efficacy by using fewer complete observations. Spare and fewer observations are two completely different terms and concepts. It feels like the related work here is on fewer observations, however, the conclusion is made for sparse observations. The authors should justify this.
4. One of the main contributions of the paper is stated in Line 123, “we refine that robustness is the main factor contributing to the poor performance of forecasting models in MTSF with sparse observations.” I miss a justification for this contribution, either experimentally or theoretically. The authors argue that due to unfixed missing rates, the existing models give poor robustness. However, this is not a strong justification. The authors need to show this with some kind of experiment. An experiment can be done to show the performance of the baseline models, trained only once, with all unfixed missing rates. The authors can think of other appropriate experiments, too.
5. The paper uses the word semantic in multiple places. To give a few examples, semantic alignment, extract semantics, align semantics, semantic mining capabilities, key semantics, disrupt the semantics, incorrect semantics, capture the semantics, error semantics, local semantics, enhance the semantic differences, semantic similarities, high-quality semantics, additional semantic information, etc. I think a reader will benefit if the meaning of the semantics is properly defined in the paper, expanding or limiting its scope to the field of MTSF.
6. The paper uses knowledge distillation between sparse and complete observations and contrastive learning among sparse observations. It would be interesting to get insights on using complete observations for contrastive learning. The complete observations can also be an input to the student model and subsequently used in contrastive learning.
7. In step II, section 3.2, the authors mention about spatial-temporal identity embeddings, namely, $S_E, T^D_E,$ and $T^W_E$. However, there is no information about how these embeddings are generated. This is an integral part of the Merlin architecture. Therefore, the authors should discuss them in detail.
8. It is mentioned in section 3.3 that the sparse input observations are passed to the fully connected layers to generate embeddings. How are the missing values handled there? Are they just considered as zeros?
9. For offline knowledge distillation, especially the $L_{HD}$ loss, what is the rationale behind using mean squared error (MSE) loss? The most common type of loss used in this scenario is the KL-Divergence loss. How does KL-Divergence fare in comparison to MSE in Merlin?
10. The authors mention in lines 351 and 352 that “After testing, it has been found that the performance is optimal when the weight of each loss is set to 1”. However, I could not find any experiment in the rest of the paper which shows the mentioned finding.
11. The paper does not report any appropriate information about the statistical significance of the experiments. At the very least, authors should report the standard deviation along with the mean.
12. The training difference between the Merlin and baseline models is unclear. The paper in lines 422-424 states, “To demonstrate the robustness of the proposed model, we only train it once, using samples with different missing rates. For other baselines, we separately train a model for each missing rate.”  Do the authors mean that in Merlin, they incorporate the data with each missing rate in one model? That is, the authors make 3 more versions of the data with 50%, 75%, and 90% missing rates. Merlin is trained on all these 4 datasets combined. Meanwhile, the baseline model is only trained on one of the missing rates datasets individually. If that is the case, then the comparison between Merlin and baseline models is not fair since Merlin sees four times more data compared to the baseline models.
13. Section C in the Appendix presents hyperparameter analysis with the hyperparameter values used in STID+Merlin. However, there is no discussion of the process of hyperparameter searching. Additionally, the authors should also provide the hyperparameters and their search process for the baseline models. This will help in the reproducibility of the paper. 
14. Figure 4 in the Appendix presents an experiment on determining two hyperparameters of Merlin on the China AQI dataset. These hyperparameter values are then also reported as the best values in Table 5. Does this mean that similar conclusions are seen in other datasets? Please provide this information in the manuscript.

**Minor Comments:** 
1. The citation type is not appropriate. The citations should be written within brackets in most of the cases in this article. Therefore, as a reader, it became very difficult to read this paper.
2. The paper has several grammatical mistakes/typos. Here are some of them:
    1. Line 87: “…usually require reconstructing reconstruct both missing…”
    2. Line 116: “…adapt to unfixes missing…”
    3. Line 119 and 309: “…different miss rates…”
    4. Line 143: “gated recursive unit (GRU).” It should be recurrent.
    5. Line 164: “Knowledge distillation can transfer valuable Knowledge from the teacher model to the student model.” Shouldn’t the second knowledge in this line be in small letters?
    6. Line 267: “…abbove…”
    7. Line 348: “Finally, we need to effectively integrate above all Loss functions.”
    8. Line 350: “…we adopts the..”
3. What does “sudden change” mean in line 73? Do the authors mean the line drop in Figure 1(b)? The author should clarify this because there can be other reasons for sudden change, like concept drift.
4. In the paper, the authors are inconsistent with their use of capital or small letters for the full form of abbreviations. Please be consistent. Some of the examples are:
    1. graph convolutional network (GCN)
    2. gated recursive unit (GRU)
    3. Graph WaveNet (GWNet)
    4. Temporal Convolutional Network (TCN)
    5. Multi-Layer Perceptron (MLP)
5. The paper introduces a notation $N_H$ in line 210. However, the meaning of $N_H$ is not present in the subsequent text. The authors provide its meaning in Appendix A. However, for ease of reading, the author should provide the meaning in line 210. The same practice should be followed for other notations, too.

**References:**
1. Chengqing Yu, Fei Wang, Zezhi Shao, Tangwen Qian, Zhao Zhang, Wei Wei, and Yongjun Xu. Ginar: An end-to-end multivariate time series forecasting model suitable for variable missing. arXiv preprint arXiv:2405.11333, 2024a.
2. Chengqing Yu, FeiWang, YilunWang, Zezhi Shao, Tao Sun, Di Yao, and Yongjun Xu. Mgsfformer: A multi-granularity spatiotemporal fusion transformer for air quality prediction. Information Fusion, pp. 102607, 2024b. ISSN 1566-2535. doi: https://doi.org/10.1016/j.inffus.2024.102607.
3. Muhammad Ali Chattha, Ludger van Elst, Muhammad Imran Malik, Andreas Dengel, and Sheraz Ahmed. Kenn: Enhancing deep neural networks by leveraging knowledge for time series forecasting. arXiv preprint arXiv:2202.03903, 2022.
4. Alessio Monti, Angelo Porrello, Simone Calderara, Pasquale Coscia, Lamberto Ballan, and Rita Cucchiara. How many observations are enough? knowledge distillation for trajectory forecasting. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, pp. 6553–6562, 2022.

### questions:
 All the questions are listed in the weakness section.

### flag_for_ethics_review:
 ['No ethics review needed.']

### rating:
 3

### confidence:
 4

### code_of_conduct:
 Yes

### role:
 Review

### Questions
All the questions are listed in the weakness section.

### Soundness
2

### Presentation
1

### Contribution
2

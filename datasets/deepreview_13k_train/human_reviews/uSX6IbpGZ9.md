# Trend/Seasonality based Causal Structure for Time Series Counterfactual Outcome Prediction

- Decision: Reject
- Scores: 3, 6, 3, 3

## Abstract
In the causal effect estimation, most models have focused on estimating counterfactual outcomes in the static setting, and it is still difficult to predict the outcomes in the longitudinal setting due to time-varying confounder. To resolve the time-varying confounder issue, while the balance representation learning-based approaches have been primarily proposed, they inherently introduces a certain degree of selection bias since the balance representations act as confounders for both treatment and outcomes. In this paper, a new trend/seasonality decomposition based causal structure is proposed for the counterfactual outcome prediction in the time-series setting. We leverage a decomposition methodology to reduce the selection bias further. Specifically, it extracts meaningful decomposed representations such as confounders and adjustment variables, which help to yield more accurate treatment effect estimation with low variance. Inspired by the fact, the proposed causal structure learns trend/seasonality representations as the confounders/adjustment variables in the direction of minimizing the selection bias, and those representations are effective in the counterfactual outcome prediction especially under the long time sequence and high time-varying confounding settings. We evaluate the proposed causal structure with several trend/seasonality decomposition algorithms on synthetic and real-world datasets. From various experiments, the proposed causal structure achieves superior performance over the state-of-the-art algorithms.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes to tackle the counterfactual outcome prediction problem by leveraging a decomposition method to learn tread representation and seasonality representation. Existing decomposition methods can be plugged in and experiments show improved performance over existing methods that are based on balanced representations.

### Strengths
- The idea of using trend/seasonality decomposition to reduce selection bias is quite interesting and worth exploring.
- The proposed method is overall well presented and easy to follow.
- The experimental results show improved performance against SOTA baselines on both synthetic and real-world data.

### Weaknesses
 - The major motivation for adapting the decomposition method is that the balanced representation approach produces selection bias. Yet, the decomposition method, as shown in Fig. 1, has a causal trend $T_t$, which is also a confounder. In the balanced representation approach, the representation is trained not to be predictive of the treatment. However, in the proposed approach, the confounder $T_t$ is trained to be predictive of the treatment. It is hard to argue which approach has a greater selection bias. Specifically, the paper does not adequately address how the learned trend component $T_t$, which is explicitly used to predict the treatment, avoids introducing selection bias, a problem the balanced representation methods explicitly try to mitigate by decorrelating the representation from the treatment. A more detailed analysis, perhaps through visualization of the latent space or a theoretical argument, is needed to justify the claim that the proposed method reduces selection bias compared to methods that explicitly enforce treatment-representation independence.
- It is argued that the imbalance loss as in Eq. (11-12) could learn seasonality representations with no information about the treatment. This is not obvious and it needs more explanation regarding why minimizing the discrepancy could make $S_t$ independent of the treatment. The paper needs to elaborate on the mechanism by which minimizing the discrepancy between the distributions of seasonality representations conditioned on different treatment assignments leads to independence. It is unclear how this minimization process ensures that $S_t$ does not inadvertently capture information correlated with the treatment, especially given that the overall objective is to predict counterfactual outcomes which are inherently linked to the treatment.
- In experiments, no measure of uncertainty is provided. It is suggested to also report one of the following: standard deviation, confidence interval, or p-value. The lack of uncertainty measures makes it difficult to assess the statistical significance of the reported improvements. Without such measures, it is hard to determine if the observed performance differences are due to the proposed method or random variation. Reporting standard deviations, confidence intervals, or p-values would provide a more robust and reliable evaluation of the method's performance.
- It is unclear how the real dataset is used. Since counterfactual outcomes do not exist in real data, it is not clear what the "real" columns in Table 2 refer to. The paper needs to clarify how the proposed method is evaluated on real-world data where counterfactual outcomes are not directly observable. Specifically, it should explain what the "real" columns in Table 2 represent and how they are used to assess the performance of the model. The absence of a clear explanation makes it difficult to understand the practical applicability of the proposed method.

### Questions
- Why the proposed method could lead to reduced selection bias given that the imbalanced representation approaches explicitly remove the dependency of treatment on the learned representation?
- Why minimizing the discrepancy could make $S_t$ independent of the treatment?
- How to evaluate the performance on the real dataset where the counterfactual outcomes are not available?

### Soundness
2 fair

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper discusses a new method for estimating causal effects in a time-series setting, focusing on counterfactual outcome prediction. Traditional methods have struggled with this task due to time-varying confounding factors and inherent selection bias. The authors propose a trend/seasonality decomposition-based causal structure that reduces selection bias and extracts meaningful representations such as confounders and adjustment variables. This approach is expected to yield more accurate treatment effect estimations with low variance. The proposed causal structure's performance was evaluated using synthetic and real-world datasets, showing superior performance over existing state-of-the-art algorithms.

### Strengths
Originality: The paper presents a novel approach to counterfactual outcome prediction in time-series data. It introduces a trend/seasonality decomposition-based causal structure that reduces selection bias, a common issue in current methodologies. This approach seems to be the first of its kind in this domain, thus marking a high degree of originality.

Quality: The authors appear to have a strong understanding of the problem space and have organized a robust methodology to tackle the task. The proposed method is thoroughly explained and appears to be based on sound principles and previous works. The authors also provide an evaluation using synthetic and real-world datasets, indicating a high-quality experimental setup.

Clarity: Despite the complex subject matter, the authors have done a good job of explaining their methodology and the motivation behind it. The language used is clear, and the paper is well-structured, making it easier for readers to follow the authors' thought process and understand the proposed solution.

Significance: The paper addresses a critical problem in time-series data analysis and causal effect estimation. The proposed solution could have a significant impact on various fields where time-series data plays a crucial role, such as finance, healthcare, and meteorology. By reducing selection bias and improving the accuracy of counterfactual outcome prediction, this work could potentially advance the state of the art in these areas.

### Weaknesses
The assumption that trend acts as confounder while seasonality acts as adjustment variable is not theoretically justified. Counterexamples can likely be constructed, for instance, consider a scenario where a sudden, seasonal event (like a yearly festival) directly influences a long-term trend in economic activity, thus making seasonality a confounder. The paper does not provide any theoretical or empirical evidence to support this crucial assumption, which is a significant weakness.

Comparison to only two baseline models is quite limited. Testing against more causal discovery and time series forecasting methods would be useful. For example, methods that explicitly model time-varying confounders or use different forms of time-series decomposition could provide a more robust benchmark. The current comparison does not sufficiently demonstrate the superiority of the proposed method.

All evaluations use RMSE loss. Checking with other counterfactual evaluation metrics could reveal useful insights. For example, metrics that focus on the accuracy of individual treatment effect estimation, such as the average treatment effect on the treated (ATT) or the precision in estimating heterogeneous treatment effects, could provide a more comprehensive evaluation. The exclusive use of RMSE might mask potential weaknesses in these specific aspects of counterfactual prediction.

The synthetic data generation processes lack enough details for reproducibility. More implementation specifics should be provided, such as the exact functional forms used to generate the trend, seasonality, and noise components, as well as the specific parameters used. Without these details, it is impossible to independently verify the results. The lack of transparency in the data generation process undermines the credibility of the experimental results.

Analysis of the sensitivity to hyperparameters like the regularization coefficients is missing. The paper should include experiments that show how the performance of the method changes with different values of these hyperparameters. This is important to understand the robustness of the method and to provide guidelines for choosing appropriate values in practice. Without this analysis, it is difficult to assess the practical applicability of the method.

The number of datasets used for evaluation is quite small. Testing on more real-world timeseries could help generalize claims. The current evaluation is limited in scope and might not be representative of the diverse range of time-series data encountered in real-world applications. The limited number of datasets raises concerns about the generalizability of the findings.

Causality assumptions like positivity, consistency, unconfoundedness need more justification for the data. Violations can affect conclusions. The paper does not discuss the plausibility of these assumptions in the context of the datasets used. Without this discussion, the validity of the causal claims is questionable. The lack of justification for these assumptions is a serious concern.

Theoretical analysis of how modeling trend/seasonality achieves lower bias is limited. More rigorous proofs would strengthen claims. The paper lacks a formal analysis of the bias reduction achieved by the proposed method. Without this theoretical foundation, the claims about bias reduction are not fully convincing.

Societal impacts of deploying these counterfactual forecasting models should be considered.

Lack of related works:

Seedat, Nabeel, et al. "Continuous-time modeling of counterfactual outcomes using neural controlled differential equations." arXiv preprint arXiv:2206.08311 (2022).

Cao, Defu, et al. "Estimating Treatment Effects from Irregular Time Series Observations with Hidden Confounders." arXiv preprint arXiv:2303.02320 (2023).

### Questions
While this paper explores an intriguing aspect of time-series causal analysis—specifically, modeling time-series from trend and seasonality—it is not without its shortcomings, particularly in the design of experiments meant to objectively situate this work within its field. Please refer to the 'weaknesses' section for a detailed list of concerns raised by the reviewer. The reviewer would be pleased to revise their score if these issues are adequately addressed.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a methodology to include a generic trend/seasonality decomposition within a causal structure for time series. Experiments show the proposed methodology have improved results compared to causal time series models that do not explicitly consider decompositions.

### Strengths
The proposed model is fairly intuitive and shows promising experimental results.

### Weaknesses
The contributions from the paper are not clear. The proposed structure (Fig 1) is conceptually very similar to other network structures (e.g. Melnychuk et al 2022, Bica et al 2020), but with the additional of a generic trend/seasonality decomposition plug-in model. The primary innovation for the loss function appears to be the discrepancy function for seasonality, but the decision is not well motivated (why do we believe the seasonality induced by different interventions must be maximally different?). Specifically, the paper does not provide a clear justification for why maximizing the discrepancy between seasonality components under different interventions would lead to better causal identification. This choice seems arbitrary and lacks theoretical backing. It's not clear that the seasonality/trend decomposition actually recovers trends or seasonality. Either theoretical justification or additional experiments are necessary to confirm we recover the true decomposition. For example, it would be useful to show that the learned trend and seasonality components align with known ground truth trends and seasonal patterns in synthetic data, or that the learned components have interpretable properties. Three assumptions are given as standard, but are never explicitly leveraged, and it's not clear that the causal effects being measured are actually identifiable. The paper does not discuss how these assumptions are used to ensure identifiability, nor does it address potential violations of these assumptions. Furthermore, the experiments focus on predictive accuracy without any evidence that the models are recovering the true causal effects. As mentioned in Bica et al 2020, evaluating decision making (correct treatment and timing) are critical to evaluate these systems. The ablation study is focused wholly on removing components of the loss function, and only for one of the 3 plug-in models. Further ablation study for the network structure would be ideal. For example, ablating different parts of the network, such as the trend or seasonality encoders, would help understand the contribution of each component. Minor issue: No attribution given for traditional decomposition methods, despite stating they are widely used. Traditional decomposition methods are also not leveraged as a comparison point in the experiments. The lack of comparison to traditional methods makes it difficult to assess the value of the proposed approach.

### Questions
Is there any theoretical justification to the claim that the trend/seasonality representations are expected to be learned in the direction of minimizing the selection bias?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In longitudinal settings, this paper uses existing FEDformer (Zhou et al., 2022), DLinear (Zeng et al., 2023), or MICN (Wang et al., 2023) as representation networks to learn decomposed representations, i.e., confounders $T_t$ and adjustments $S_t$, from time-series data. Then, the same independent constraints (Eq. (4) in (Hassanpour & Greiner, 2020)) are employed to learn balanced representations across various treatment arms. The framework proposed in this paper is identical to that proposed by Hassanpour & Greiner (2020), and the only difference is that this paper uses existing FEDformer (Zhou et al., 2022), DLinear (Zeng et al., 2023), and MICN (Wang et al., 2023) as representation networks.

### Strengths
The trend/seasonality-based causal structure for time series is an interesting problem.

### Weaknesses
 **[Novelty]** The framework proposed in this paper is identical to that proposed by Hassanpour & Greiner (2020), and the only difference is that this paper uses existing FEDformer (Zhou et al., 2022), DLinear (Zeng et al., 2023), and MICN (Wang et al., 2023) as representation networks. The same loss function of the proposed causal structure could be found in Eqs. (3,4,5,6) in (Hassanpour & Greiner, 2020).

**[Unclear]** The authors argue that existing methods introduce a certain degree of selection bias since the balance representations act as confounders for both treatment and outcomes. However, this paper still uses the same independent constraints (Eq. (4) in (Hassanpour & Greiner, 2020), IPM loss in (Shalit et al., 2017)), contradicting their own statement.

**[Completeness 1]**  The problem settings in this paper are incomplete. The causal relationship between x, a, and y in the time series is not clear. Will the outcomes at time t+1 be influenced by all the historical data? Would using only past P time steps data lead to unmeasured confounding bias? Does the causal relationship between covariates X change over time? I suggest the authors to provide a causal diagram of the time series to further clarify the problem settings. Additionally, in the problem settings section, what is the impact of trend and seasonality on the causal relationship?

**[Completeness 2]** The simulation mechanisms of (semi-)synthetic are incomplete, as the detailed implementations of the data generation processes are not provided in the main text or appendix. The author suggests referring to Melnychuk et al. (2022) for more information.

[**Experiments**] This paper decomposes representations as Causal Trend and Causal Seasonality. However, how can we evaluate and demonstrate this? The experiments in the paper do not provide evidence for these statements.

### Questions
See Above.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
1 poor

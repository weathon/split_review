# DROSIA: Decoupled Representation on Sequential Information Aggregation for Time Series Forecasting

- Decision: Reject
- Avg Score: 4.25
- Scores: 3, 3, 5, 6

## Abstract
Time series forecasting is crucial in various fields, including finance, energy consumption, weather, transportation, and network traffic. It necessitates effective and efficient sequence modeling to encapsulate intricate temporal relationships. However, conventional methods often aggregate sequential information into representations of each time point by considering other points in the sequence, thereby ignoring the intra-individual information and suffering from inefficiency. To address these challenges, we introduce a novel approach, DROSIA: Decoupled Representation On Sequential Information Aggregation, which only integrates temporal relationships once as an additional representation for each point, achieving sequential information aggregation in a decoupled fashion. Thus balancing between individual and sequential information, along with a reduction in computational complexity. We select several widely used time series forecasting datasets, and previously top-performing models and baselines, for a comprehensive comparison. The experimental results validate the effectiveness and efficiency of DROSIA, which achieves state-of-the-art performance with only linear complexity. When provided with a fair length of input data, the channel-independent DROSIA even outperforms the current best channel-dependent model, highlighting its proficiency in sequence modeling and capturing long-distance dependencies. Our code will be made open-source in the subsequent version of this paper.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
In the papers the authors propose a MLP based time series forecasting framework named DROSIA which emphasizes the separate representations of patch (local) level information and sequence level information, i.e. the manual decoupling of the two. DROSIA prefers concatenation instead of summation to explicitly present the related info. They empirically benchmark DROSIA against other SotA methods and demonstrate its outstanding performance.

### Strengths
DROSIA as proposed in the paper is a practical architecture to use, and it is relatively convincing that it can deliver good performances.

### Weaknesses
There are weaknesses in both the theoretical motivation and the empirical study in the paper. Novelty wise, the motivation and justification behind the decoupling of sequence and patch level information is not well supported, whereas besides this point DROSIA has no outstanding distinctions from other linear (MLP) based model.

For the empirical study there lacks many details regarding, e.g. benchmark model parameters, reasons for setting up the benchmark parameters, etc, which makes the empirical support for the decoupling claim weak. Specifically, the choice of hyperparameters for DROSIA and the baseline models appears inconsistent across different experiments, raising concerns about the fairness of the comparison. The lookback window selection also seems arbitrary, with the paper using a window of 96 while other works like PatchTST employ 512, and the lack of a systematic exploration of this parameter further weakens the empirical support. The limited scope of Table 4, which focuses on only two high-dimensional datasets, and the somewhat misleading claim that PatchTST lacks patch-level representation, further detracts from the validity of the empirical results. It remains unclear whether the performance gains observed in Table 1 are due to the proposed decoupling mechanism or simply due to a more effective tuning of the linear/MLP structures, which are already known to be effective for forecasting tasks. 

Presentation wise, the writing could use some revision, specially regarding the key parts, e.g. the algorithm of DROSIA, the reasoning behind the ablation study, etc.

### Questions
Regarding the theory:
1. The dot product attention and the skip connection altogether are also capable of decoupling between the patch level presentation and its interaction with the whole sequence even when these two levels of presentations are summed together instead of concatenated. Can you provide a more rigorous or quantifiable definition on what the decoupling means here in the paper? 
2. Can you clarify the flow of the algorithm? For example, eq 3 through eq 7, where is S^j_1, assuming C^j is sequence level? How to get S^{j+1}_i?
3. Empirical study reveals no benefit from patching. What's the motivation behind it?

Regarding the empirical study:
1. The choice of DROSIA and other baseline methods' hparams are either unclear or arbitrary across different studies. It would be better to have more details to back a fair comparison, e.g. all methods are tuned to near optimal.
2. The lookback window for each tasks also seem a bit arbitrary, e.g. table 1 uses 96 whereas the original PatchTST paper reports 512. It would be more insightful to report multiple lookup for stronger empirical evidence.
3. Table 4 Effectiveness of DROSIA is too limited in the sense that (1) the benchmark datasets are two and high dimensional, and (2) "S" for PatchTST's original setting is a bit misleading for claiming no patch level presentation there.
4. Based on the current empirical study, it is unclear whether the performance edge in Table 1 is due to the decoupling or due to a better tuning of some linear / MLP structures which are already known to be also effective for forecasting tasks. Consider adding an appendix.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper presents Decoupled Representation On Sequential Information Aggregation (DROSIA) for time series forecasting. The key idea is to aggregate sequential information in a decoupled fashion, effectively balancing it with individual point information. The experimental results demonstrate the effectiveness of the proposed method.

### Strengths
* The paper is well-written and organized.
* The proposed network architecture appears to be novel.
* The method is lightweight, utilizing relatively fewer parameters than existing approaches.

### Weaknesses
 * There are clarity issues in explaining the proposed method. Some components and their roles are not clearly justified. Specifically, the interaction between the decoupled representation and the sequential aggregation is not well-defined. It's unclear how the individual point information is balanced with the aggregated sequential information, and the mechanism behind this balance requires further explanation. The specific design choices for the aggregation modules, such as the choice of specific layers or operations, are not sufficiently motivated.
* Certain comparisons may not be entirely fair. In addition, several related works are not mentioned or compared (see the questions below). The comparison with channel-dependent methods like iTransformer is questionable due to potential differences in training data or model capacity. The lack of comparison with other relevant baselines limits the assessment of the proposed method's novelty and performance.
* For datasets with a small number of variates or low complexity, the improvements over other models, such as PatchTST, are marginal. The reported results do not clearly demonstrate a significant advantage of DROSIA in these scenarios, raising concerns about its practical applicability across diverse datasets. The statistical significance of the improvements should be more thoroughly investigated.

### Questions
1. It is not clear why each component of the proposed DROSIA is designed in its current form. What advantages do the chosen design choices provide compared to potential alternatives?
2. It may not be fair to compare with channel-dependent methods e.g., iTransformer, as they have less training data.
3. Some important channel-independent and channel-dependent baselines are not mentioned or compared, such as:

[1] Unified Training of Universal Time Series Forecasting Transformers (ICML 2024)

[2] Chronos: Learning the Language of Time Series (arXiv preprint arXiv:2403.07815)

[3] One Fits All: Power General Time Series Analysis by Pretrained LM (NeurIPS 2023)

[4] S²IP-LLM: Semantic Space Informed Prompt Learning with LLM for Time Series Forecasting (ICML 2024)

[5] TimeMixer: Decomposable Multiscale Mixing for Time Series Forecasting (ICLR 2024)

4. What is the performance of DROSIA in few-shot scenarios compared to the baselines?

### Soundness
2

### Presentation
3

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
For the task of time series forecasting, authors propose decoupled representation to integrate temporal relationships once as an additional representation for each point, achieving sequential information aggregation in a decoupled fashion.

### Strengths
- Nice paper writing.
- Enough ablation study is also included.

### Weaknesses
 - The idea of decoupled representation lacks novelty. The technical implementation is relatively weak.
- Lack of in-depth analysis, e.g., channel-dependent model.
- No available codes.

### Questions
- What is the big difference between your work and PatchTST? 
- You consider iTransformer as a strong baseline, but the results in Table 1 seem to be different from the results in iTransformer. Any experimental settings changed?
- Efficiency analysis in Table 3 should include more linear-based methods: DLinear, and TiDE. It would be great to conduct more analysis like Figure 10 in iTransformer rather than only computational complexity.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
Authors proposed DROSIA a method of time-series forecasting that incorporates both point-wise and temporal information by applying the following steps:
- Patching similar to existing methods e.g., PatchTST
- DROSIA encoding 
    - Sequence aggregation I.e., applying multiple encoding layers on vectorized patches 
    - Information extraction I.e., a MLP on concatenated representation of the previous step 
    - Representation fusion i.e., layer normalization of concatenated representations of information extraction + vectorized patches followed by a fully connected transformation (similar to residual connections) 
- Decoding (projection) i.e., making predictions 

Authors studied performance of DROSIA on state-of-the-art of time series forecasting benchmarks and compared with some of the well-known methods in this area.

### Strengths
- Authors have done extensive experiments ranging from benchmarks to complexity
- DROSIA achieved better performance with relatively simpler model in Long-term forecasting task

### Weaknesses
Although average over 3 trials is reported, standard deviations are not reported. Reporting standard deviation is crucial when performance gap is small. Particularly, when authors claim “significantly outperforming” a method this needs to be confirmed by conducting a statistical test e.g., t-test or Wilcoxon test (based on assumptions).  

The proposed method needs adjustment in input length to outperform iTransformer particularly on datasets with a lot of variables and shorter horizons e.g., 96 which could be a disadvantage in applicability of the proposed method on real-world applications. Authors did not provide any instruction on how to find “sufficiently long” input length for their method. 

Recently LLM-based methods for time series forecasting have shown state-of-the-art performance [1-4] some of which also based on patching [2] but there is no indication of this category in neither related works nor compared methods. Examples are: 
Just to be clear, I am not asking authors to compare with all of these LLM-based methods but I’d like to know their at least their thoughts on positioning this line of work in their study. 

Authors have compared their method with DLinear which is based on MLP that utilizes point-wise information but there are also MLP-based models such as [5] that incorporate global and local information which to me are more similar to the proposed method but is missing from compared methods. 

One missing ablation experiment is related to the equation (7). What is the performance without this component? 

Some reproducibility information is missing such as code (cited in the abstract that it will be provided later), learning rate or any utilized regularizations. 

Original (non-averaged) results of table 1 should be provided in the appendix 


Smaller fixes: 

- Typo on page 4 “In Equation (4)” -> Equation (3)

- Typo on page 5 “In Equation (3) -> Equation (8)

- Font size in figures is too small (at least for me)

- It would be helpful to add another row “average+- standard deviation” to each table to summarize the results per analysis

### Questions
Do you have any intuition for certain behaviours in your sensitivity analysis? e.g., why patch size is not important, why for larger dataset in terms of number of channels e.g., Traffic high values of almost all hyper-parameters makes things worse? 

Is there any parameter sharing in DROSIA? 

Are observations made in table 5 going to hold for longer horizons e.g., H=720?  

What is “P” model in table 4 last column? 

Compared baselines are also applicable to other time-series tasks including classification, short-term forecasting, imputation, and anomaly detection and often competitive in said tasks, but DROSIA is only studied in long-term forecasting do you have any sense on applicability of DROSIA in other time series tasks?

I would be happy to revise my score if authors clarify questions/weaknesses particularly:
- Missing experiments e.g., ablation or potentially missing baselines as well as information to evaluate performance better e.g., standard deviation or significance test. 
- Issue with number of features/channels and input length

Update: I'd like to thank the authors for engaging during the rebuttal period to address reviewer's comments. After reading their responses and comments from other reviews, I have decided to increase my score.

### Soundness
3

### Presentation
2

### Contribution
2

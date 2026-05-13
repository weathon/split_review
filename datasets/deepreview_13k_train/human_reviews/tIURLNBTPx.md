# Repetitive Contrastive Learning Enhances Mamba's Selectivity in Time Series Prediction

- Decision: Reject
- Scores: 3, 5, 5, 6

## Abstract
The prediction of long sequences has always been a challenge in time series forecasting tasks. Due to Mamba's sequence selection capability, many Mamba-based models have been proposed, achieving state-of-the-art results in long sequence prediction problems. However, much research has focused on integrating mamba-ssm into specific model structures for better performance, while the core of mamba-ssm, its sequence selection capability, has not been deeply explored. We believe there is significant potential in Mamba's sequence selection capability and propose a Repetitive Contrastive Learning (RCL) method to enhance it. Specifically, we utilize Repeating Sequence Augmentation to expand the sequence while introducing Gaussian noise, thereby enhancing the Mamba block's sequence selection capability through both inter-sequence and intra-sequence contrastive techniques. Then our methods transfer parameters directly from a single pretrained Mamba block to a variety of Mamba-based models. This approach provides superior initialization for forecasting tasks. Our experiments consistently demonstrate that this technique improves the forecasting performance of many Mamba-based models, without imposing additional memory requirements.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper develops a pre-training technique for Mamba family of models and applies this to solve time-series forecasting task. Empirical results show lift resulting from the proposed pretraining techniques when applied to Mamba models.

### Strengths
- Improved results compared to mamba models without pretraining

### Weaknesses
 - Experiment tables lack comparison to recent baselines and reporting format is different than the accepted in the literature. It is not clear where the proposed techniques stand against current state of the art.
- Comparison against univariate baselines is missing. Does you approach beat the univariate baselines on these datasets?
- The title claims that the pretraining improves Mamba's selectivity. The word selectivity appears in two places in the paper other than the title: "we freeze the matrix A that controls the mamba’s selectivity" and "Freezing matrix A can retain the enhanced selectivity obtained during pre-training." While A controls mamba’s selectivity and authors hypothesize that pretraining results in a matrix A that improves the selectivity, there is no empirical result in the paper that would help to support the hypothesis. The claim is basically unsupported.
- There are now ablation studies of the two proposed pretraining techniques: Intra-sequence contrast and Repetitive Contrastive Learning.
- Experiments are not clearly described
- The idea of contrastive pretraining does not seem to be entirely novel, even in the time-series literature. The related work section is misleading as it puts a lot of emphasis on contrastive learning in image/textual domains. However, the following works exist in the time-series domain: https://arxiv.org/pdf/2303.11911, https://arxiv.org/pdf/2312.16424, https://arxiv.org/pdf/2206.08496.


### Questions
- Can you include the recent baselines from https://arxiv.org/pdf/2405.14616 and https://arxiv.org/pdf/2403.09898 for comparison?
- Can you provide empirical evidence that freezing pretrained matrix A indeed improves Mamba selectivity? Please define selectivity and measure the improvement. Are there qualitative results demonstrating improved selectivity?
- Can you provide ablation of Intra-sequence contrast and Repetitive Contrastive Learning. What happens when only one of them is used? Which one is more powerful? Do they exhibit synergistic effects (more than additive gain)
- Can you provide more details on the experimental setup? For example, how exactly are the metrics in Table 1 computed? Why is the presentation format different than in the other works relying on the same datasets?
- Please extend related work on time series contrastive pretraining works and explain how your work is different and novel. 
- Can you include existing time-series pretraining techniques I identified as baselines?
- In related work, the following MLP-based architectures are missing, please include in the discussion and as baselines: https://arxiv.org/pdf/1905.10437, https://arxiv.org/pdf/2201.12886
- The proposed contrastive learning techniques, are they applicable only to Mamba model, or they are more general? If they are general, why are not you exploring their effects on other model families? Is it viable to obtain evidence of accuracy lifts on other model families?

### Soundness
1

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper claims that it addresses the challenge of long-sequence prediction in time series forecasting by enhancing Mamba’s sequence selection capability. It introduces Repetitive Contrastive Learning with sequence augmentation and noise to improve performance, which is shown to universally benefit Mamba-based models without extra memory overhead.

### Strengths
1. The proposed repeating sequence augmentation and repetitive contrastive learning methods are simple, easy to implement, and transferable to various TSF model architectures.

2. Extensive experiments demonstrate that Mamba-based TSF models show significant performance improvement after applying the proposed pretraining and augmentation methods.

### Weaknesses
1. The paper contains some formatting errors, such as many mathematical symbols in Figures 1 and 2 not rendering correctly. The citation format is also inconsistent, with a lot of textual citations used in places where parenthetical citations would be more appropriate, making the paper harder to read.

2. About selection ability:

The paper claims that Mamba is chosen to be used in the paper because of its stronger temporal selection ability compared to previous architectures. However, vanilla attention, with its temporal-adaptive dynamical parameters, is clearly more suitable for selection task than Mamba. The improvement of Mamba's selective SSM in selection ability is compared against the fixed temporal weights of S4, not against the more flexible softmax attention.

Mamba’s selective SSM was designed to introduce selection capabilities, like the induction heads learned in Transformer-based LLMs, to fixed SSM-weighted models like S4. Due to time complexity constraints, Mamba is less likely to surpass standard attention, which has $O(L^2)$ complexity because it calculates unique softmax temporal weights for each token, maximizing selection and matching abilities. In contrast, near-linear complexity methods (like Mamba and linear attention variants) avoid computing unique weights for each token, inheriting attention weights from previous steps, making adjustments through methods like gating mechanisms rather than recalculating all the weights independently for each step, to decrease the time complexity. This temporal propagation of weights limits their ability to achieve the distinct selection ability of softmax attention for each token.

The paper’s argument that “Mamba's better performance in TSF comes from its selection ability, thus requiring better pretraining methods to enhance this ability for the performance improvement of downstream forecasting” lacks sufficient support. While the proposed contrastive pretraining method does improve performance, is this really due to enhanced selection ability? Contrastive learning literature more often emphasizes the maintenance of a well-structured latent space to distinguish samples. The performance improvement might stem from learning more distinguishable representations in the latent space rather than an unquantified enhancement in selection ability.

In summary, the paper would benefit from more discussion, analysis, and experiments to demonstrate that the proposed methods enhance the model's selective ability. For instance, the authors could adopt the analysis techniques from LLM literature that show when and how induction heads are learned during training to compare the selective ability before and after applying the methods in this paper. Otherwise, the paper may need rebranding to explain the performance improvement from alternative perspectives, such as emphasizing how contrastive pretraining enhances the geometric properties of the latent space to improve the representation and discrimination of time series, as suggested in prior contrastive learning literature.

### Questions
1. The proposed method seems not to be specific to the Mamba structure. Applying it to more structures like Transformer could help the community better understand its significance.

2. The paper lacks comparisons with existing time series pretraining and representation learning methods. Since the approach introduces a pre-training / data-augmentation stage rather than being end-to-end, fair comparisons with previous time series representation learning / data augmentation + downstream forecasting methods are needed.

3. Mamba is inherently a sequential SSM for ordered input tokens. It seems the authors used vanilla Mamba rather than bidirectional Mamba and did not mention whether input shuffling was applied. Without shuffling during the repeat process, as described in Figure 1, sequential SSM characteristics could lead to information leakage in the noise data generation process. Also, when treating the entire series as an embedding $X^I$, a structure like bidirectional Mamba, which is order-independent, may be more appropriate.

4. What are the basic settings for the forecasting problem in the experiments, such as input lookback length and forecasting horizon? These details are crucial for analyzing the model’s characteristics but are not provided. Additional training settings, like the train-test split, are also missing.

5. Additionally, the term “selective scan mechanism” used in the paper seems somewhat misleading. The “scan” in Mamba (associative scan) refers to hardware parallelization and is unrelated to the algorithm’s selection ability.

### Soundness
2

### Presentation
1

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
The paper under review presents an innovative approach to enhance the sequence selection capability of Mamba-based models in time series prediction tasks. The authors propose a method called Repetitive Contrastive Learning (RCL), which involves augmenting time series data by duplicating time points and introducing Gaussian noise. The RCL method aims to improve the model's ability to selectively focus on relevant moments within time series data, thereby enhancing its predictive performance. The experiments conducted demonstrate some improvements in performance across various Mamba-based models.

### Strengths
The paper tries to address a crucial gap in time series analysis by teaching models to select and prioritize key data points, which is vital for improving prediction accuracy. The authors are acknowledged for bringing attention to an issue that has often been overlooked in previous studies.

### Weaknesses
1. The paper suffers from poor writing quality，reducing its readability and comprehension. Symbols are ill-defined, and the operational flowchart lacks clear descriptions, hindering reader understanding. A revision to enhance language and clarity is needed.
2. Duplicating time points and adding noise may result in significant numerical differences between the replicated samples and the original samples, which could reduce their similarity. At the same time, the temporal correlations in the original data are disrupted. Why not use patch operations instead?
3. It is unreasonable for $X_{aug}$ to be input as a whole into the model because it contains all the duplicated time steps and enhanced noise. Directly passing it through an MLP may amplify the noise and completely disrupt the temporal correlations in the original data.
4. There are too few baseline comparisons, and they are not representative. Additionally, there is a lack of comparison with non-Mamba methods, making it difficult to demonstrate the superiority of the proposed approach.
5. The technical contribution is insufficient. The conclusions are inadequate as the experiments do not delve deeply into the core claims of the paper, such as whether the model actually achieves effective selection and prioritization of key moments in time series data as stated.

### Questions
1. Please provide a more in-depth analysis to demonstrate whether the model has indeed effectively selected and prioritized key moments in time series data, as claimed in the paper.
2. Offer results for more baselines, such as additional Mamba-based and non-Mamba-based methods.

### Soundness
2

### Presentation
1

### Contribution
1

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a contrastive learning training framework for Mamba-based models in multivariate time series forecasting (MTSF) tasks. The authors introduce a repeated data augmentation and contrastive learning approach for both inter- and intra-sequence levels. Experiments demonstrate that replacing partial blocks of Mamba models with the proposed pre-trained blocks can enhance their performance.

### Strengths
1. This is one of the first works exploring contrastive learning in Mamba models for time series.
2. The proposed method demonstrates performance gains on recent Mamba-based models for time series forecasting.
3. Based on the visualizations in Figures 3 and 4, I believe the pretraining is effective.

### Weaknesses
1. The repetitive augmentation does not seem novel, as it appears to simply create negative pairs and concatenate positive and negative pairs together. This approach likely increases the input size and, consequently, the computational cost. Traditional contrastive learning can also generate negative pairs with different strategies, and I suspect that with a smaller input size, the model might be even more efficient. (Please correct me if I am mistaken.)

2. The paper does not include comparisons with non-Mamba methods. This is crucial, as improvements over weak baselines alone may not provide strong evidence of the proposed method’s contribution.

3. The experimental evaluation may be insufficient for ICLR standards. Recent works often include either a larger variety of datasets or more comprehensive experimental setups.

Minors: There are some typos and repeated sentences, and the overall presentation could be improved.

### Questions
1, Could you clarify whether all MambaPB blocks share the same parameters, or are they trained independently during the self-training phase? If all MambaPB blocks share the same parameters, this would make the approach more interesting.

2. In what way does the proposed augmentation strategy improve upon conventional contrastive learning approaches?

3. Is there an ablation study that examines how varying levels of Gaussian noise impact performance?

### Soundness
2

### Presentation
2

### Contribution
2

# Token-Aware Inference-Time Intervention for Large Language Model Alignment

- Decision: Reject
- Scores: 8, 6, 5, 6, 5

## Abstract
Effectively mitigating the misalignment of large language models (LLMs) is crucial for ensuring secure AI applications. Inference-Time Intervention (ITI) technique, which applies interventions to internal representations along the probed alignment direction during inference, offers substantial alignment enhancements with minimal cost. However, previous ITI methods adopt coarse sentence-level analysis which neglects the misalignment discrepancy among varied tokens, resulting in deviant alignment direction and inflexible intervention strength.
In this work, we propose a Token-Aware Inference-Time Intervention (TA-ITI)  approach to fully utilize token-level alignment information, therefore realizing superior post-intervention performance. TA-ITI primarily consists of Mutual Information-Guided Token-level Graph Aggregation (MIG) and Misalignment-aware Adaptive Token-level Intervention (MAI). MIG develops a MI-guided graph to exploit the tokens' informative interaction for representation enrichment, thus improving alignment probing and facilitating subsequent intervention.
MAI comprehensively perceives the token-level misalignment degree from token representation and prediction to guide the adaptive adjustment of intervention strength, thereby enhancing final alignment performance. Extensive experiments on three alignment capabilities demonstrate the efficacy of TA-ITI, notably surpassing baseline by 25.8\% on the primary metric of truthfulness.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper proposed token level methods to conduct inference time intervention for alignment. The methods provide a new way to use mutual information to compute sentence level directions from tokens, and apply different weights to different tokens and add stronger intervention to potentially key misaligned tokens.

### Strengths
- The paper is well-written, well-motivated.
- Extensive experiments are conducted on several aspects, with proper ablation and analysis. It shows that the methods not only improve the scores, but also generate fluent questions
- The added cost of inference is acceptable giving the intervention results.

### Weaknesses
It seems there are two hyper-parameter alpha and beta that needs to be tuned. It seems that the effect can be influenced by the hyperparameter choice. For example, in beta, the performance is non-optimal when it is <0.4. If these hyperparameter behaviors do hold across different tasks, it will be harder to apply this method.



### Questions
- L210: how are the bins setup when computing the entropy?
- Also about the graph entropy propagation method, would this reach a stationary distribution after multiple rounds of propagation?

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
This paper proposes Token-Aware ITI to address the limitations of sentence-level ITI methods by utilizing information from all tokens in a sentence. It has two main components: MIG, which uses mutual information to analyze token interactions and enhance the accuracy of alignment probing and MAI, which adjusts the intervention strength based on the misalignment level of each token. Experiments on TruthfulQA, RealToxicityPrompts, and StereoSet demonstrate the effectiveness of  TA-ITI. It also proves the effectiveness of MIG and MAI by conducting ablation experiments.

### Strengths
The two main contributions of the paper, MIG and MAI prove their effectiveness with the overall performance compared to other baselines and the analysis in section 5.

The inference computation is reasonable which is critical for the inference time intervention.

### Weaknesses
The originality of this work is somewhat limited since it is an expansion of a previous paper ([1]) from sentence-level to token-level. 

More background explanations on editing-based inference-time intervention are needed in the related section and preliminaries section, rather than a simple summary of previous works with citations. 

The generalizability of MIG and MAI is limited since they rely on supervised trained misalignment probes and misalignment estimators.

### Questions
When constructing the token-level misalignment dataset, how do you decide if this token is prone to overall misalignment? Since this process is the most critical part of MAI, the data construction process needs further details.

Since the MI-based graph network is constructed based on the training samples of the particular dataset, how does the alignment probe transfer to unseen test data in inference time?

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper targets the task of inference-time intervention (ITI) of LLM. Previous ITI methods usually probe and intervene at the sentence level with uniform editing direction for all tokens, which may be deviant and inflexible. To address these problems, this paper proposes a Token-Aware Inference-Time Intervention (TA-ITI) approach, which utilizes a Mutual Information-Guided Token-level Graph Aggregation (MIG) and Misalignment-aware Adaptive Token-level Intervention (MAI) to probe and intervene at the token level. Experiments on truthfulness, harmlessness, and fairness alignment show improvement of TA-ITI over baselines.

Despite the good performance, my main concern is that some implementation details in the method seem to be unintuitive and lack a strong guarantee. More explanations of these choices may enhance the soundness of the proposed method.

### Strengths
- The general motivation for token-level intervention is reasonable.
- The experimental results look good.

### Weaknesses
 - Reasons for some designs in method implementation are unclear. Specifically, 
    - The graph propagation module in MIG lacks strong motivation. Why is the graph structure needed?
    - In lines 209-210, calculating the entropy of representations with discretized bins seems strange. Are there any other choices?

### Questions
None

### Soundness
1

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
This paper builds upon previous Inference-Time Intervention (ITI) methods by advancing from sentence-level to token-level interventions, thereby achieving higher performance in controlling the truthfulness, harmlessness, and fairness of LLM-generated content. To accomplish this, this paper first employs MI-guided Token-level Graph Aggregation (MIG) to mitigate directional deviation and obtain direction vectors for intervention. Subsequently, this paper uses Misalignment-aware Adaptive Token-level Intervention (MAI) to implement adaptive interventions across distinct tokens. In experiments, this paper validates the substantial improvement of TA-ITI in post-intervention alignment across multiple datasets.

### Strengths
1. Addressing the long-standing issue of coarse granularity in sentence-level ITI, this paper achieves fine-grained ITI at the token level. 
2. This paper innovatively combines multiple machine learning algorithms: (1) utilizing MI-guided Token-level Graph Aggregation to obtain global direction vectors, (2) and incorporating Representation Misalignment Estimation as well as Prediction Uncertainty Quantification to implement token-level adaptive intervention.
3. In the experiments, overall, this paper demonstrates a very significant improvement compared to the baselines.

### Weaknesses
1.	Some more intuitive explanations are missing. For example: Why does MI-guided aggregation work? The last token of the LLM itself is also an integration of the entire sentence information. Intuitively, why does directional deviation occur, and how does your method intuitively solve this problem? Specifically, the paper lacks a clear explanation of why using only the last token's representation for training the intervention direction leads to suboptimal results, given that the last token is influenced by all preceding tokens through the self-attention mechanism. The paper should elaborate on the limitations of the self-attention mechanism in capturing global sentence-level alignment information, and how the proposed MI-guided aggregation addresses these limitations by explicitly modeling token interdependencies.
2.	It is still limited to using directional vectors in an additive manner, and there is not much innovation in the paradigm. While the paper focuses on token-level interventions, the core intervention mechanism remains an additive adjustment of token representations using a single direction vector. This approach does not explore more complex or adaptive intervention strategies that could potentially offer greater control and flexibility. The paper should acknowledge the limitations of this additive approach and discuss potential avenues for future research that explore alternative intervention paradigms.
3.	Some functions and variables in the formulas are not clearly explained. For example, the meaning of 'P' and the role of 'y' in Formula 4, as well as the meaning and origin of 'W_LM' in Formula 7. The paper needs to provide a more detailed explanation of the universal alignment probe $\widetilde{P}$ and its training process, including the specific role of the label 'y' in the binary classification task. Furthermore, the paper should clarify that $W_{LM}$ refers to the language modeling head of the LLM and explain how it is used for uncertainty quantification.

### Questions
1. Some details in Formula 4: How is ‘P’ implemented exactly, and what role does ‘y‘ play in this context?
2. Based on Formula 8: Different tokens only vary in the strength of the intervention while maintaining the same direction. Have you attempted to make the direction adaptive?
3. Before and after performing the MI-guided aggregation, as well as before and after obtaining the direction, and before and after performing the intervention, do any steps involve vector normalization? Does applying normalization or not have any impact?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces TA-ITI to improve representation engineering in large language models by addressing token-level misalignment. Unlike sentence-level methods, TA-ITI uses Mutual Information-guided Token-level Graph Aggregation to capture detailed token interactions, creating refined alignment directions. The Misalignment-aware Adaptive Token-level Intervention then customizes intervention strength based on each token’s misalignment and prediction uncertainty. This token-level approach boosts truthfulness, harmlessness, and fairness of LLMs.

### Strengths
- Technically sound: The experiments demonstrate that the method indeed achieves performance improvements across various benchmarks.

### Weaknesses
 - This work is relatively incremental. The mutual information-based propagation method is a common approach in graph representation learning, applied here primarily to address the limitations of last-token information. Similarly, adaptive intervention during inference is also a common practice.
- The approach incurs additional inference costs due to the need to recalculate token representations multiple times using a graph aggregation algorithm. Additionally, training the Misalignment Estimator requires extra computational resources both for training and inference.

### Questions
- On what dataset is the intervention direction obtained? And what about the Misalignment Estimator? If both are derived and tested on the same dataset, the performance improvements might be unsurprising. It would be more meaningful if the authors could demonstrate that the proposed improvements generalize to benchmarks beyond the dataset used for obtaining the intervention weights, for example, to HaluEval.
- Could the authors specify the SFT setup in more detail? I noticed that Li et al. reported high loss and KL divergence when applying SFT on TruthfulQA—did the authors observe similar results?
- Is the performance improvement on RealToxicityPrompts potentially due to excessive refusal? Can ITI methods prevent over-refusal? It would be beneficial if the authors could include experiments on XSTest to address this concern.

### Soundness
3

### Presentation
3

### Contribution
2

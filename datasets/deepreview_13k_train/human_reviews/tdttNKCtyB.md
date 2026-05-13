# ROSE: Register-Assisted General Time Series Forecasting with Decomposed Frequency Learning

- Decision: Reject
- Scores: 6, 6, 6, 5

## Abstract
With the increasing collection of time series data from various domains, there arises a strong demand for general time series forecasting models pre-trained on a large number of time-series datasets to support a variety of downstream prediction tasks. Enabling general time series forecasting faces two challenges: how to obtain unified representations from multi-domian time series data, and how to capture domain-specific features from time series data across various domains for adaptive transfer in downstream tasks. To address these challenges, we propose a \underline{\textbf{R}}egister Assisted General Time Series F\underline{\textbf{o}}recasting Model with Decompo\underline{\textbf{se}}d Frequency Learning (\textbf{ROSE}), a novel pre-trained model for time series forecasting. ROSE employs  Decomposed Frequency Learning for the pre-training task, which decomposes coupled semantic and periodic information in time series with frequency-based masking and reconstruction to obtain unified representations across domains. We also equip ROSE with a Time Series Register, which learns to generate a register codebook to capture domain-specific representations during pre-training and enhances domain-adaptive transfer by selecting related register tokens on downstream tasks. After pre-training on large-scale time series data, ROSE achieves state-of-the-art forecasting performance on 8 real-world benchmarks. Remarkably, even in few-shot scenarios, it demonstrates competitive or superior performance compared to existing methods trained with full data.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper proposes a pre-trained model for time series forecasting. In this approach the pre-training is done through masked reconstruction in the frequency domain. Authors also attempt to capture domain-specific information by learning a register of cluster center vectors and then using top-k most similar vectors during the fine-tuning/prediction stage.

### Strengths
The paper is well written and easy to follow. The proposed approach is interesting and innovative. Both masked reconstruction and domain-specific register can be valuable for developing a foundational time series model. Experiments on real world datasets show that the proposed approach outperforms leading baselines. Authors conduct extensive ablation results, I found few shot generalization and register vector selection particularly interesting. It indicates that the model is robust in the low data setting and the model is transferring domain knowledge from similar datasets. Finally, authors provide both code and benchmark datasets.

### Weaknesses
My main concern is that this method is complex, it has multiple components and a multi-term loss. Balancing this loss and contributions of different components while also appropriately tuning the required hyper parameters can be a challenging task. Specifically, the interaction between the masked reconstruction loss in the frequency domain, the prediction loss, and the register loss needs further clarification. It's unclear how these losses are weighted and if the model is sensitive to these weights. Furthermore, the process of selecting the top-k most similar register vectors during fine-tuning introduces another layer of complexity and hyperparameter tuning. I'm also not convinced on why the low rank learnable matrix A needs to be added. Is this the only parameter that is adapted during the finetuning phase? How much is the accuracy impacted if A is removed?

### Questions
Is low rank learnable matrix A the only parameter that is adapted during the finetuning phase? How much is the accuracy impacted if A is removed?

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
In this paper the authors introduce ROSE, a pretrained encoder-decoder style time series forecaster. They propose to pretrain this model with frequency decomposition, a cross-domain time series register for nearest neighbor lookup, and both reconstruction and prediction heads. They complete empirical study demonstrating excellent zero-shot and few-shot performance of ROSE.

### Strengths
The paper presents a solid design of a general time series forecaster in the encoder-decoder style. In particular it shows the novelty which includes (1) a standalone registry for dimension reduction in contrast to, e.g. vector quantization or codebook learning, and (2) the multi frequency masking for representation learning. 

For the empirical section, the ablation study is also comprehensive. 

The paper has good writing quality and is easy to follow.

### Weaknesses
There are a few theoretical and empirical issues that prevent this work from being absolutely sound. Please see questions.

Regarding the design:
1. What's the justification of creating a general forecaster in an encoder-decoder style, which (1) to some extent locks in its lookback and forecast lengths thus does not handle any context + any horizon, and (2) is more well received for time-series embedding (e.g. Moment [1]).
2. Given the distinct targets of reconstruction vs prediction, is the benefit of the reconstruction loss due to better presentation learning, or just more ground truth labels touched (e.g. imagine training only using the prediction loss on (512/720) * 100% more examples)?
3. Why using 4 forecasting heads instead of 1 head with losses on 4 horizons? What's the practice when the forecast horizon is covered by multiple heads?
4. Will the registry fail when the input time series is much shorter than 512 because of the linear projection into it?
5. Is the registry a seasonality lookup eventually (Not an issue. Just curious).

Regarding the empirical study:
1. When ROSE is treated as a zero-shot foundation model, the benchmark on the 7 datasets popular for supervised learning is not sufficient. For example, benchmarks with shorter horizons or shorter lookups are missing. Something similar to Table 9 but in the zero-shot setup would be helpful.
2. Inference times of other zero-shot models seem a bit off. Likely some baseline models are not called as expected (e.g. without compilation or not on accelerators).

### Questions
Regarding the design:
1. What's the justification of creating a general forecaster in an encoder-decoder style, which (1) to some extent locks in its lookback and forecast lengths thus does not handle any context + any horizon, and (2) is more well received for time-series embedding (e.g. Moment [1]).
2. Given the distinct targets of reconstruction vs prediction, is the benefit of the reconstruction loss due to better presentation learning, or just more ground truth labels touched (e.g. imagine training only using the prediction loss on (512/720) * 100% more examples)?
3. Why using 4 forecasting heads instead of 1 head with losses on 4 horizons? What's the practice when the forecast horizon is covered by multiple heads?
4. Will the registry fail when the input time series is much shorter than 512 because of the linear projection into it?
5. Is the registry a seasonality lookup eventually (Not an issue. Just curious).

Regarding the empirical study:
1. When ROSE is treated as a zero-shot foundation model, the benchmark on the 7 datasets popular for supervised learning is not sufficient. For example, benchmarks with shorter horizons or shorter lookups are missing. Something similar to Table 9 but in the zero-shot setup would be helpful.
2. Inference times of other zero-shot models seem a bit off. Likely some baseline models are not called as expected (e.g. without compilation or not on accelerators). 

[1] Mononito Goswami, Konrad Szafer, Arjun Choudhry, Yifu Cai, Shuo Li, and Artur Dubrawski. Moment: A family of open time-series foundation models. arXiv preprint arXiv:2402.03885, 2024.

After rebuttal:
I appreciate the authors' effort addressing my concerns here. I've revised my rating accordingly.

### Soundness
2

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
4

### Summary
This paper introduces ROSE, a model designed to achieve a unified representation and effectively capture domain-specific information through two main components: Decomposed Frequency Learning and Time Series Register. Extensive experiments have demonstrated the competitive performance.

### Strengths
1. This paper is well-written and easy to follow.

2. The time series register is interesting.

3. Extensive experiments have shown that ROSE achieves competitive performance.

### Weaknesses
1. The paper should provide further explanations on how Decomposed Frequency Learning contributes to learning a unified representation.

2. For ROSE, the requirement for a different new Register for each dataset during the pretrain stage means that adding a new dataset necessitates starting a new pretrain process. This increases the computational cost, whereas previous methods primarily focus on the fine-tune stage and typically involve only one pretrain phase.

3. Additional analysis experiments for Decomposed Frequency Learning are necessary to clarify why it is beneficial for achieving a unified representation.

4. The experimental settings for Figure 1(b) are lacking.

### Questions
please see weaknesses

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper addresses the growing demand for general time series forecasting models that can be pre-trained on diverse datasets to facilitate a variety of downstream prediction tasks.

### Strengths
1. The paper is well-writen and easy to understand.

2. The paper effectively addresses the pressing need for general time series forecasting models, which is designed to be pre-trained on diverse datasets, enhancing its applicability across various prediction tasks.

3. The method in the paper facilitates the capture of domain-specific representations during pre-training, thereby improving adaptive transfer for downstream tasks.

### Weaknesses
1. The paper introduces a pre-trained method for time series forecasting, but it lacks a clear demonstration of the effectiveness of the pre-trained model in comparison to existing time series representation learning methods.

2. The evaluation is limited to only one type of downstream task, which makes it difficult to assess the robustness and generalizability of the proposed method across various applications in time series forecasting.

### Questions
1. In the pre-training stage, how to solve the problem of excessive data differences in different domains, because data with too much difference often leads to training failure？

2.  Does the dimension of the time series affect the performance?

### Soundness
3

### Presentation
3

### Contribution
2

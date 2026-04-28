# Scaling Laws for Diffusion Transformers

- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 5, 5, 6

## Abstract
Diffusion transformers (DiT) have already achieved appealing synthesis and scaling properties in content recreation, \emph{e.g.,} image and video generation. 
However, scaling laws of DiT are less explored, which usually offer precise predictions regarding optimal model size and data requirements given a specific compute budget.
Therefore, experiments across a broad range of compute budgets, from \texttt{1e17} to \texttt{6e18} FLOPs are conducted to confirm the existence of scaling laws in DiT \emph{for the first time}. Concretely, the loss of pretraining DiT also follows a power-law relationship with the involved compute.
Based on the scaling law, we can not only determine the optimal model size and required data but also accurately predict the text-to-image generation loss given a model with 1B parameters and a compute budget of \texttt{1e21} FLOPs.
Additionally, we also demonstrate that the trend of pretraining loss matches the generation performances (\emph{e.g.,} FID), even across various datasets, which complements the mapping from compute to synthesis quality and thus provides a predictable benchmark that assesses model performance and data quality at a reduced cost.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper explore the scaling laws of DiT (for text-to-image generation). The authors experiment with different computation budget and find the optimal allocation (i.e., the lowest training loss) of model parameters and training data amount for each budget. Subsequently, they plot two relationship curves: 1) parameter-FLOPs and 2) token (seen in training)-FLOPs. The conclusion is the training loss follows a power-law relationship with the computation budget. Based on this, the author claim that they can predict the best configurations of model parameter and training data for a given (larger) budget.

### Strengths
1. While some similar reports have been seen in LLMs, to my best knowledge this is the first analysis for text-to-image DiTs. The problem this paper aims to address is also a hot topic troubling the community. A good question is proposed in this paper.
2. If the conclusion is correct, then given the model size and training data, it is possible to predict in which training iteration the model will achieve the best performance. This would alleviate a lot of resource consumption in the heavy task of DiT training.
3. The experimental methods are well designed.

### Weaknesses
1. I don't know why the authors use FLOPs and token numbers as the indicators. This makes it difficult for me to intuitively estimate the computation budgets and data. In practice, GPU hours and image amount are more common and intuitive. While FLOPs and token counts are standard metrics, providing GPU hours and image counts as reference points would significantly improve the accessibility of the results. The lack of these practical metrics makes it hard to grasp the scale of the experiments. For instance, a reader might struggle to relate a given FLOP count to the actual time it would take to train a model on a specific hardware setup, or how many images are required for training.
2. I'm concerned about the power-law relationship shown in Fig 1 and 3, though the linear is so clear. How can we determine that this is not by coincidence (due to the structure of the model as well as the training data)? Even if this law is objectively universal, At what model size will it fail? For DiT, 1B is still a small scale. Can I really estimate 5B/10B if I only evaluate two points with small model sizes and get the regression line? The concern is that the observed power-law might be an artifact of the specific model sizes and training data used. The paper needs to address the potential limitations of extrapolating from small-scale experiments to much larger models. The authors should also discuss the potential for deviations from the power-law relationship at larger scales, given that the current experiments are limited to relatively small models.
3. The training loss is not equal to FID, and more different from general performance. Of course the model does not perform well at large loss values, but it is agnostic at small values. In addition, when the budget is fixed, the number of iterations for the large model decreases. What happened if a larger learning rate is used in this case? The current setting does not seem fair. The paper should provide a more thorough analysis of the relationship between training loss and metrics like FID, especially at small loss values. Furthermore, the impact of the fixed learning rate on the training dynamics of models with varying sizes and iteration counts needs to be investigated. It's not clear if the current setup is fair to all model sizes.
4. The authors should improve the writing for easy understanding. For example, I can guess that the tokens in Fig. 1 refer to the number of tokens DiT has processed during the training, it still confuses me about the figure (even though the concept is explained in Sec 3.2)

### Questions
Please also check the concerns in Weaknesses.
1. As mentioned in W.1, why not use GPU hours and text-image pairs?
2. How can we use it in practice? Can we only estimate two points at small scale and predict the configuration at large scale? I have no confidence in it.
3. Can this conclusion be validated based on the present DiT works? They usually have the model versions with different parameters.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This research investigates the scaling characteristics of diffusion transformers, focusing on a range from ($1 \times 10^{17}$) to ($6 \times 10^{18}$) Flops. The study enhances the understanding of how computational effort maps to synthesis quality.

### Strengths
1. Good Presentation: The figures clearly present the properties of the scaling model and the associated FLOPs, making the analysis easy to follow and understand.

2. Predictable Benchmarking: The introduction of a predictable benchmark for assessing model performance and data quality significantly reduces costs and aids in optimizing computational resources.

### Weaknesses
1. The largest model in the study only has 1 billion parameters. While I agree with the authors' statement that "scaling laws help us make informed decisions about resource allocation to maximize computational efficiency," a model size of 1 billion parameters is too small to verify the significance of this scaling law. We need guidance for larger model sizes, especially considering that current models, such as the Flux model, already have 8 billion parameters.

2. The discussion of reference work is not accurate. Line 097 makes claims about the masked diffusion transformers but fails to mention the first Masked Diffusion Transformer (MDT), both versions v1 and v2.

### Questions
Are there any properties by scaling DiT across different dimensions (like channels, layers, etc)? The paper should explore how scaling DiT in various dimensions affects its properties and performance. This could provide valuable insights into the scaling behavior and help in designing more efficient models.

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
3

### Summary
This work studies the scaling laws of diffusion transformer for text-to-image generation. It tries to unveil the relationship between the training budget and the optimal model size/training data quantity. Under careful designed experimental settings, the disclosed scaling laws served as a predictor for the model size/performance under given a specific training budget.

### Strengths
This is the first study of scaling laws in DiT based text-to-image generation models. It disclosed some relationships between training budget and model size/training data quantity under a specific setting. The results might be useful for the community when designing future DiT based text-to-image generation.

### Weaknesses
Experiment results are somewhat limited. All experiments were done with a very small dataset and small models (<= 1B parameters). These settings are quite different from many DiT based text-to-image models in terms of data quantity and model size. Whether the conclusion will hold for different setting is unknown to us.

### Questions
please refer to the weakness

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
4

### Summary
This work tries to reveal the scaling law of Diffusion Transformer in the field of text-to-image generation. It is based on in-context dit and rectified flow matching, and performs a series of experiments between 1e17 and 6e18 flops. By this, it finds the power law relationship between the objective function, model parameters and compute. It also uses the loss of a 1B dit at the compute of 1e21 flops to confirm the correctness of the equation. At last, it conducts a comparative test between in-context and cross-attention dit, to show that the scaling law can help to indicate the effectiveness of the model architecture's design.

### Strengths
1. This work first proposes the scaling law of Diffusion Transformer in text-to-image generation. And it gets several formulated equations between loss, parameters and compute, which is confirmed by an additional experiment.
2.  It shows that different metrics (loss, VLB, likelihood) has similar trends with regard to compute budget. And the performance of generation measured by FID does, too.
3.  It indicates the application of the scaling law: serving as a benchmark for measuring the effectiveness of model architectures.

### Weaknesses
1. The range of compute budget for experiments is a bit narrow. The count of data points is a little few for drawing a curve. According to "Scaling Laws for Autoregressive Generative Modeling"[1], they did experiments from 1e14 to 1e23 flops.
2. This work's experiment is not as sufficient as the scaling law for AR[1]. Maybe it needs some curves like [1].
3. The base setting of model architecture is not good. Recently, popular settings of in-context dit mainly refer to SD3[2] and FLUX, which only concat text and image as input but use timesteps for adaptive layernorm. This setting is important and may lead to suboptimal conclusion. 
4. It said that "scaling laws can serve as a reliable and predictable benchmark for evaluating the effectiveness of both model architectures and datasets". But it misses experiments to show how to use scaling law to choose training datasets.
5. Did not indicate the resolution of training datasets. Different resolutions may affect the conclusion.

### Questions
1. Some images in the paper only have one or two curves. Does this imply that it is already experimenting with the optimal model parameters calculated by the scaling law?
2. Why don't you use bigger models for base experiments? Common diffusion models, such as SD3 and FLUX, has 10B parameters or so. Only doing experiments with models less than 1B may is not general enough.

### Soundness
2

### Presentation
3

### Contribution
3

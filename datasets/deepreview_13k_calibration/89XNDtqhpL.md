# MatFormer: Nested Transformer for Elastic Inference

- Decision: Reject
- Avg Score: 6.00
- Scores: 5, 6, 5, 8

## Abstract
Transformer models are deployed in a wide range of settings, from multi-accelerator clusters to standalone mobile phones. The diverse inference constraints in these scenarios necessitate practitioners to train foundation models such as PaLM 2, Llama, \& ViTs as a series of models of varying sizes. Due to significant training costs, only a select few model sizes are trained and supported, limiting more fine-grained control over relevant tradeoffs, including latency, cost, and accuracy. This work introduces MatFormer\footnote{MatFormer stands for \mdoll~\textbf{Mat}ryoshka Trans\textbf{former} due to the model's inherent nested nature.}, a nested Transformer architecture designed to offer elasticity in a variety of deployment constraints. Each Feed Forward Network (FFN) block of a  MatFormer model is jointly optimized with a few nested smaller FFN blocks. 
This training procedure allows for the Mix'n'Match of model granularities across layers -- i.e., a trained universal MatFormer model enables extraction of \textit{hundreds} of accurate smaller models, which were never explicitly optimized.  We empirically demonstrate MatFormer's effectiveness across different model classes (decoders \& encoders), modalities (language \& vision), and scales (up to 2.6B parameters). We find that a 2.6B decoder-only MatFormer language model (MatLM) allows us to extract smaller models spanning from 1.5B to 2.6B, each exhibiting comparable validation loss and one-shot downstream evaluations to their independently trained counterparts. Furthermore, we observe that smaller encoders extracted from a universal MatFormer-based ViT (MatViT) encoder preserve the metric-space structure for adaptive large-scale retrieval. Finally, we showcase that speculative decoding with the accurate and {\em consistent} submodels extracted from  MatFormer can further reduce inference latency.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This research introduces MatFormer, a novel nested Transformer architecture that addresses the challenges of deploying models across diverse constraints. It optimizes each FFN block in a way that allows for the flexible use of different model sizes across layers, even when they were not explicitly optimized. MatFormer proves to be effective in various model classes, modalities, and scales, with the ability to extract smaller models from a 2.6 billion parameter decoder-only MatFormer language model. These smaller models maintain comparable performance to independently trained counterparts. Additionally, MatFormer-derived encoders maintain the metric-space structure for large-scale retrieval, and speculative decoding with submodels extracted from MatFormer reduces inference latency. This work offers a promising solution for deploying Transformers in a wide range of settings while maintaining fine-grained control over trade-offs like latency, cost, and accuracy.

### Strengths
- This paper is well-written and easy to follow.
- To my best knowledge, the research is the first work to introduce an interesting concept such as a nested Transformer architecture for LLMs. The proposed method aims to address the challenges of deploying models across diverse constraints.
- The proposed method demonstrates the ability to obtain a variety of models without the need for additional training after a single learning process.
- The study encompasses a broad spectrum of experiments, spanning both language and vision domains, and incorporating a range of modalities, classes, and scales.

### Weaknesses
The reviewer has two main concerns:

**1. Weak baselines: there is no comparison with efficient LLM techniques that enhance inference speed without fine-tuning or additional training.**
- MatFormer's baseline is limited to a vanilla transformer of the same size. However, it would be meaningful to compare it with recent techniques that improve inference speed without fine-tuning or additional training. For example, approaches like Dejavu [1], which leverages contextual sparsity during the inference phase to achieve enhanced inference speed within a given budget, could be an option. It is necessary to conduct such comparisons with several of these baselines to thoroughly evaluate the performance of MatFormer.

**2. Lack of technical contributions compared to pre-trained supernet (the largest transformer)-based hardware-aware NAS methods.**

Background: In the field of NAS, there are studies that consider the largest supernet in the search space as a nested network of subnetworks and train the supernet to provide pre-trained subnetworks optimized for inference budgets [2, 3]. The definition of a search space may vary, but it typically includes various architectural design choices such as the number of blocks, layers, and hidden dimensions of layers.

While the proposed MatFormer focuses on pre-trained LLMs, hardware-aware NAS methods [2] based on pre-trained transformers focus on traditional transformers. Therefore, their settings are not exactly the same. Nevertheless, both methods are fundamentally grounded in transformer structures, with the shared objective of constructing, training elastic transformer-based models, and delivering pre-trained transformer-based models that are optimized for specific inference budget constraints. Therefore, the reviewer finds it meaningful to compare the two in terms of their technical contributions.

- Lack of search algorithm: MatFormer leaves the search algorithm as future work and employs a rather naive method called "Mix’n’ Match" to select the final optimal model within a given inference budget. However, as well-known in NAS research, searching for an optimal model from a search space significantly impacts the final performance and is not a trivial problem. The reviewer thinks that MatFormer would be better off including an algorithm to search for the best combination among pre-trained blocks.

- Simple search space: The proposed MatFormer defines a search space by only considering the number of FFN blocks as the architectural design choice (If I am wrong, please let me know). This seems much simpler than the search spaces designed by NAS methods (e.g., [2]).

### Questions
The reviewer believes that the proposed approach is valuable because it introduces elastic LLMs that provide multiple pre-trained transformer-based models optimized for specific inference budget constraints with a single training for the first time. However, its technical contributions are limited, and the baseline models used for comparison are weak.

- Please address the concerns in Weaknesses section.
- Q. How do training time and memory usage change when using the proposed approach for model training compared to training a single model?

### Soundness
3 good

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
This paper proposes a nested Transformer architecture called MatFormer based on principle of matryoshka representation learning, designed to offer elasticity in a variety of deployment constraints. During training, each feed forward network (FFN) block of a MatFormer model is jointly optimized with a few nested smaller FFN blocks. And this paper propose to jointly optimize all the submodels together by combining their loss together. During elastic inference, MatFormer allows for the Mix’n’Match of model granularities across layers, i.e., a trained universal MatFormer model enables extraction of hundreds of accurate smaller models. The design of MatFormer can be applied to both decoder and encoder networks.

### Strengths
1. The proposed nested Transformer for elastic inference is possible to extract exponentially many submodels based on the deployment constraints rather than only few submodels. I appreciate this high flexibility of MatFormer.

2. The authors fully explore the design and extension of this solution. For example, they explore to reweight different granularities of submodels in Table 6, and evaluate MatFormer spanning from different modalities, i.e., language and vision, model classes, i.e., decoder and encoder, and scales (up to 2.6B parameters) in their main experiments.

3. I think this research is valuable and general for the LLM inference, and has a great potential impact on the design and application deployment of large foundation models in the future.

### Weaknesses
1. The parameters g in the article, i.e., logarithmically spaced granularity, is an important parameter for MatFormer. The authors selected g = 4 for experimental verification and analysis. I wonder about the impact of different values of g on the flexibility, training efficiency and effectiveness of MatFormer, and the consistency and accuracy of submodels. Specifically, how does varying 'g' affect the trade-off between the number of extractable sub-models and the individual performance of each sub-model? Does a larger 'g' consistently lead to a greater number of usable sub-models, or does it introduce diminishing returns in terms of model diversity and performance? This should be an interesting and important exploration which is currently missing.
2. The Mix'n'Match procedure can freely combine hundreds of consistent submodels based on MatFormer layers to meet various specific constraints, but the experiments in Section 4 and Appendix seem to have only 9 submodels evaluated (as shown in Figure 2 and 4). I think the author can give more model loss and consistency data results of different combinations of submodels to better support the above advantage of MatFormer. It would be beneficial to see a more comprehensive analysis of the performance landscape when combining sub-models from different layers. For example, what are the performance characteristics when combining a large sub-model from the first few layers with smaller sub-models from later layers, and vice-versa? A more detailed exploration of the combinatorial space would strengthen the claims of flexibility.
3. As mentioned in the first paragraph of the Introduction, many similar practical solutions provide models with 7B, 13B, 33B and 65B parameters, but the experiments of this paper only verify and analyze models with parameters between 0.8-2.6B. If the authors have the enough computing resource, it will be quite valuable for LLM research to evaluate the effectiveness and application potential of MatFormer over a even larger model in your future work. This is not a big concern of this work.
4. As authors say in the Introduction: “MatFormer can also form a similar sub-structure on attention heads”. It will be more clear if authors can illustrate the nested structure of attention heads just like Figure 1. A visual representation of how the attention heads are nested, similar to the FFN nesting, would greatly improve clarity. Specifically, how are the attention heads selected for each sub-model? Is it a simple selection of the first 'n' heads, or is there a more complex mechanism involved? A detailed explanation of this nesting mechanism is needed.
5. The core method is similar to a previous work NetAug [1], which expands a tiny model into several larger models, and the tiny model obtains extra supervision via additional gradients. However, the starting points of two papers are different. NetAug aims to make tiny models more accurate while MatFormer aims to allow elastic Transformer inference. If authors can explain more comparison/analysis between them, I will appreciate the value of this work even more. A more detailed comparison, focusing on the differences in training objectives, the structure of the auxiliary networks, and the resulting model properties, would be beneficial. How does the nested structure of MatFormer compare to the auxiliary networks in NetAug, and what are the implications for model performance and flexibility?
6. Although the experiments are evaluated on wide applications and settings, the baseline seems weak to support the improvement of MatFormer. I recommend authors to add more comparisons with stronger baseline methods including other elastic inference techniques. The current baselines, which are models trained from scratch, do not provide a strong enough comparison. It would be more convincing to compare against other methods that achieve model elasticity, such as those based on pruning or knowledge distillation. This would better demonstrate the advantages of MatFormer over existing techniques.

### Questions
All of my concerns are explained in the Weaknesses part above.

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper presents MatFormer, a model architecture based on the Transformer model. MatFormer employs the concept of matryoshka representation learning to introduce nested sub-structures in feed-forward network (FFN) blocks. The architecture aims to facilitate elastic inference by allowing for the extraction of numerous smaller sub-models without additional training.

### Strengths
The paper introduces an interesting idea of elastic inference within the Transformer architecture, a concept that can be potentially beneficial for a wide range of deployment scenarios.

### Weaknesses
1. Motivation and Efficiency: While the paper does address the limitations of current large foundation models, it falls short in clearly explaining the training efficiency gains provided by MatFormer. Specifically, there seems to be a lack of substantial evidence to support the claim that training costs are significantly reduced. The paper does not provide a clear breakdown of the computational costs associated with training MatFormer compared to training a standard Transformer model of equivalent size, making it difficult to assess the true efficiency gains. Furthermore, the paper does not specify the hardware used for training, which is crucial for evaluating the reported FLOPs reduction. 

2. Similarity to Existing Techniques: The paper does not sufficiently distinguish MatFormer from existing techniques such as mixture-of-experts and other conditional computation methods. This raises questions about the novelty of the work. The paper needs to clarify how the nested structure of MatFormer differs from the routing mechanisms used in MoE models, particularly in terms of how the sub-networks are activated and utilized during inference. A more detailed comparison with other conditional computation methods, such as dynamically activated networks, is also needed to highlight the unique aspects of MatFormer.

3. Scope of Applicability: The focus on FFNs leaves the attention mechanism of the Transformer model unaddressed. This limitation narrows the effectiveness of MatFormer in improving Transformers comprehensively. The paper should discuss the limitations of only applying Matryoshka representation learning to the FFN layers and how this might impact the overall performance of the Transformer, especially in tasks where the attention mechanism plays a critical role. It would be beneficial to explore the potential of extending the Matryoshka concept to the attention mechanism to achieve a more comprehensive improvement.

4. Evaluation and Support for Claims: The paper could benefit from a more rigorous evaluation to substantiate its claims. As it stands, the contributions asserted lack sufficient empirical validation. The paper needs to provide more detailed results on the performance of the extracted sub-models, including a breakdown of the performance across different granularities and tasks. The evaluation should also include a comparison with other methods for elastic inference, such as model pruning or distillation, to demonstrate the superiority of MatFormer.

5. Prior Work Comparison: The work could benefit from a clearer discussion of how MatFormer advances beyond or differentiates from key prior work, specifically Kusupati et al., 2022, in terms of the nested structure. The paper needs to provide a more detailed explanation of how the nesting of parameters in MatFormer differs from the nesting of output representations in Kusupati et al., 2022, and how this difference leads to the claimed benefits in terms of elastic inference.

### Questions
- The paper seems to use MatLM, MatFormer, and MatViT interchangeably.
- In Figure 2 and the associated text, what are the differences in model architecture / settings among MatFormer, Mix'n'Match, and baseline?
- How does the proposed method improve speculative decoding? Section 4.1.1 is missing certain details to help understand this claim.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors propose techniques for a) training Transformer models such that they have configurable hidden size inside the FFN projection after training and b) mixing/matching hidden sizes across the FFNs in a Transformer model to produce a range of quality / cost tradeoffs for Transformer serving. They evaluate their technique on text and image tasks and demonstrate potential applications like speculative decoding.

### Strengths
The paper is well written and organized. I found it easy to follow.

The most compelling part of the paper was the application to speculative decoding, I think. Potential wins from shared parameters, shared attention cache and consistency between the base/full model are very clear.

### Weaknesses
There are a number of small things I’d encourage the authors to revise to strengthen their paper.

1) Saying that MatFormer is “zero additional cost” seems inaccurate given the cost of the additional ‘g - 1’ forward passes during training. The computational overhead of these additional passes, especially with large models, could be significant and should be acknowledged.

2) The authors’ don’t explain how the mix’n’match models on the pareto frontier are selected. Given there are many candidates this seems like an important detail. The lack of a clear selection strategy makes it difficult to reproduce the results and understand the practical implications of the method. It would be helpful to know if this selection is based on a heuristic or an optimization process.

3) The claim that the FFN is responsible for the largest chunk of latency during inference seems questionable to me. I’d encourage the authors to present a more nuanced perspective on Transformer inference based on previously published data. For example, the study from Kim et. al [1] presents relevant data for CPU serving in Figures 7 and 8. The relative contribution of FFN layers to overall latency can vary significantly depending on factors such as model size, sequence length, and hardware platform. A more detailed analysis of these factors is needed.

4) In the speculative decoding experiments, I’d encourage the authors to briefly describe how consistency between the two models can translate into latency reductions. This will make the impact more clear to readers who aren’t familiar with prior work/do not read the reference you direct them to. It's not immediately obvious how the proposed method facilitates faster decoding, and a brief explanation would improve the paper's clarity.

### Questions
One ablation I would like to see is how a Transformer performs if the 'g' additional forward passes aren't used during training with your Mix'n'Match procedure. Basically, how bad does a normal Transformer perform with this post-processing if it's not trained appropriately?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent

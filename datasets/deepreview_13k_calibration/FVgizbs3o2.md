# TensorGPT: Efficient Compression of Large Language Models based on Tensor-Train Decomposition

- Decision: Reject
- Avg Score: 3.75
- Scores: 3, 3, 3, 6

## Abstract
High-dimensional token embeddings underpin Large Language Models (LLMs), as they can capture subtle semantic information and significantly enhance the modelling of complex language patterns. 
However, this high dimensionality also introduces considerable model parameters and prohibitively high model storage and memory requirements, which is particularly unaffordable for low-end devices.
Targeting no extra training data and insufficient computation cases, we propose a {\bf training-free} model compression approach based on the Tensor-Train Decomposition (TTD), 
whereby each pre-trained token embedding is converted into a lower-dimensional Matrix Product State (MPS).
We then comprehensively investigate the low-rank structures extracted by this approach, in terms of the compression ratio, the language task performance, and latency on a typical low-end device (i.e. Raspberry Pi). 
Taking GPT family models (i.e. GPT-2 and CerebrasGPT) as case studies, our approach theoretically results in $46.89\%$ fewer parameters of the entire model, with a compression ratio $39.38\times$ - $65.64\times$ for the embedding layers. With different hyperparameter choices, the model compressed with our approach can achieve a comparable language task performance to the original model with around $2.0\times$ embedding layer compression. This empirically proves the existence of low-rank structure in GPT family models, and demonstrates that about half of the parameters in the embedding layers are redundant.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper proposes using tensor-train decomposition to compress the token embedding matrix, aiming to reduce model size and accelerate inference, particularly in edge device scenarios. The technique leverages a higher-order tensor approximation method, built upon singular value decomposition (SVD), to efficiently represent embeddings while maintaining performance. This tailored approach is well-suited for resource-constrained environments, promising benefits in storage and computational efficiency.

### Strengths
The paper is well-structured and easy to follow, with a clear presentation of the methodology and its applications.

### Weaknesses
## Review

### summary:
 This paper proposes using tensor-train decomposition to compress the token embedding matrix, aiming to reduce model size and accelerate inference, particularly in edge device scenarios. The technique leverages a higher-order tensor approximation method, built upon singular value decomposition (SVD), to efficiently represent embeddings while maintaining performance. This tailored approach is well-suited for resource-constrained environments, promising benefits in storage and computational efficiency.

### soundness:
 2

### presentation:
 3

### contribution:
 2

### strengths:
 The paper is well-structured and easy to follow, with a clear presentation of the methodology and its applications.

### weaknesses:
 **Limited Novelty:** The method largely builds upon the existing TT_SVD approach, with Algorithm 1 in this paper replicating methods already established in prior literature [1]. The methodological advancements or generalizations beyond TT_SVD appear minimal based on the methodology section.

**Unconvincing Experiments:** The experiments are conducted on older and relatively small models, such as GPT-2 and models up to only 1.3B parameters. This limits the relevance of the results, as they don’t reflect performance on contemporary large language models (LLMs). Additionally, the evaluation setup lacks modern benchmarking practices; for instance, LLM harness [2] would provide a more standardized evaluation framework.

**Unintuitive Rationale:** The foundational rationale for embedding a matrix using a tensor is unclear. The method requires reshaping the matrix into a higher-order tensor before applying tensor decomposition, but the paper does not provide an intuitive explanation for why this approach is effective or reasonable. Also, the embedding matrix only occupies a small part of the model even for a mid size of model, and a common way to reduce parameter size is through weight tie, which directly reduce the parameter sizes of embedding into half. How does you method performs in this case?

**Overstatement of Contribution:** Some claims appear overstated. For instance, the authors state, "As far as we know, we are the first to compress LLMs with low-rank factorization, specifically for low-end devices." However, the cited reference [3] already demonstrates compression of LLMs using SVD for similar purposes. Furthermore, there are numerous existing works that apply low-rank decomposition for LLM compression, such as [4-6].

**Limited Impact on Overall Model Size:** The embedding matrix occupies only a small portion of the model's parameters, even in mid-sized models. A commonly used technique, weight tying, can directly halve the embedding parameter size, offering a straightforward compression approach. The paper does not address how the proposed method compares to weight tying or performs when weight tying is already applied, raising questions about its practical impact on overall model size reduction.

[1] V. Oseledets. Tensor-train decomposition. SIAM Journal on Scientific Computing, 33(5):2295–2317, 2011. doi: 10.1137/090752286.

[2] Gao, Leo, et al. "A framework for few-shot language model evaluation." Version v0. 0.1. Sept 10 (2021): 8-9.

[3] Yen-Chang Hsu, Ting Hua, Sungen Chang, Qian Lou, Yilin Shen, and Hongxia Jin. Language model
compression with weighted low-rank factorization. In International Conference on Learning
Representations, 2022.

[4] Yuan, Zhihang, et al. "Asvd: Activation-aware singular value decomposition for compressing large language models." arXiv preprint arXiv:2312.05821 (2023).

[5] Lin, Chi-Heng, et al. "MoDeGPT: Modular Decomposition for Large Language Model Compression." arXiv preprint arXiv:2408.09632 (2024).

[6] Ashkboos, Saleh, et al. "Slicegpt: Compress large language models by deleting rows and columns." arXiv preprint arXiv:2401.15024 (2024).

### questions:
 How does your method perform with weight tying?
What is the percentage of overall compression for model sizes larger than 13B?

### flag_for_ethics_review:
 ['No ethics review needed.']

### details_of_ethics_concerns:
 NA

### rating:
 3

### confidence:
 5

### code_of_conduct:
 Yes

### role:
 Review

### Questions
How does your method perform with weight tying?
What is the percentage of overall compression for model sizes larger than 13B?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The authors applied tensor train to an edge device application, and found we can use that to compress some NLP models. It reads to me that the author is simply applying a pre-existing, well-known tensor decomposition method on a problem. And I didn't see any new knowledge developed or presented (I might be wrong, so hopefully the authors could point out clearly what's the real technical contribution other than yet another application).

### Strengths
- Working on a problem that's important.

### Weaknesses
The authors applied tensor train to an edge device application, and found we can use that to compress some NLP models. It reads to me that the author is simply applying a pre-existing, well-known tensor decomposition method on a problem. And I didn't see any new knowledge developed or presented (I might be wrong, so hopefully the authors could point out clearly what's the real technical contribution other than yet another application).



soundness:
 2


presentation:
 2


contribution:
 1


strengths:
 - Working on a problem that's important.


weaknesses:
 - The authors claim "- As far as we know, we are the first to compress LLMs with low-rank factorization, specifically", which is not true to me. The architecture is the same for most NLP models and thus pardon me I really don't know what's added. I think all the tensor-train stuff has been developed and applied before. It's not immediately obvious to me what's new conclusions or findings drawn from this paper.

### Questions
- Pardon me that I really don't know what's the biggest contribution. Other than your claim of try things on LLM, what's the real technical contribution in your paper not discussed by previous works?

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper presents "TensorGPT," a model compression method using Tensor-Train Decomposition (TTD) to reduce the parameter size of Large Language Models (LLMs), particularly in embedding layers, without additional training. This training-free approach preserves model performance while significantly reducing memory requirements, demonstrated on low-end devices like Raspberry Pi.

### Strengths
1.	The approach does not require extra training, making it applicable for scenarios with limited resources or when extra data is unavailable.
2.	TensorGPT achieves substantial compression with low memory overhead, retaining performance across language modeling and sentiment analysis tasks.
3.	The paper includes experiments on low-end hardware (Raspberry Pi) and larger models, evaluating compression ratios, latency, and task-specific performance.

### Weaknesses
1.	The novelty is limited. Tensor-Train Decomposition is explored in several language model compression works. What are the differences between the proposed method and existing works?
2.	Lack important baselines. Compressing token embedding layers is studied in some papers and the paper does not compare with them. For example, [1] and baselines used in [1] should be set as baselines.
3.	The empirical evaluation is primarily on language modeling and sentiment classification, with potential limitations in representing other complex NLP tasks, such as math reasoning and multi-hop question answering.

### Questions
refer to weaknesses

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
3

### Summary
The paper presents TensorGPT, a novel approach for compressing LLMs through tensor-train decomposition of embedding layers. The key innovation is applying tensor-train decomposition to individual token embeddings without requiring additional training data or computation. The authors evaluate their method on GPT family models (GPT-2 and CerebrasGPT), demonstrating meaningful parameter reduction while maintaining or sometimes improving model performance. The work provides comprehensive evaluations on GPT-family models and demonstrates practical applicability on edge devices.

### Strengths
1. Novel training-free compression method specifically targeting embedding layers. Strong practical value for edge device deployment
2. Comprehensive experiments across multiple tasks and model sizes.  Solid theoretical foundation with clear mathematical derivations.
Thorough analysis of compression vs. performance trade-offs

### Weaknesses
1. Limited comparison with existing compression methods and baselines. The comparison would be more comprehensive by comparing with more baselines which are train-free and trained. Specifically, the paper lacks a comparison against other low-rank methods applied to the embedding matrix, such as SVD or other matrix factorization techniques. This makes it difficult to assess the relative effectiveness of the proposed tensor-train decomposition.
2. Evaluation focused mainly on GPT-family models and mainly focus on small models. The experiments are primarily conducted on GPT-2 and CerebrasGPT models, which are relatively small. The paper needs to demonstrate the effectiveness of the method on larger models to prove its practical applicability. Furthermore, the evaluation should be extended to other model architectures beyond the GPT family to show the generalizability of the approach.
3. It would be a great to combine the proposed embedding compression method with other model compression methods to check compatibility. The paper does not explore the potential interaction or compatibility of the proposed method with other compression techniques like quantization or pruning. It is important to investigate whether combining tensor-train decomposition with other methods can lead to further performance improvements.

### Questions
1. Could this approach be extended to show performance of other model architectures beyond the GPT family?
2. Could this approach compatible with other model compression methods? 
3. Have you investigated the effect on model robustness like in the multilingual setting using more diverse tokens?

### Soundness
3

### Presentation
3

### Contribution
3

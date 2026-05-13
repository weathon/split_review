# Input Compensation for Pruned Models

- Decision: Reject
- Scores: 5, 5, 5, 5

## Abstract
Though foundation models are powerful, they are large and require substantial memory and computation resources for serving.
To tackle this issue, many pruning methods have been proposed to reduce the model size, thereby achieving memory and computational efficiency. These methods either identify and retrain the important weights or \textit{adjust the unpruned weights} to compensate for the removed weights. In this paper, we propose a novel approach called input compensation (IC) to boost the performance of pruned models, i.e., \textit{adjust the input} to compensate for the removed weights. We learn a compensation pool to construct input-dependent compensation to reduce the error caused by pruning. Different from existing pruning methods, which are designed in the parameter space, the proposed IC is designed in the input space. Hence, IC is complementary to existing methods and can be integrated with them.
Extensive experiments on various tasks, including image classification, language modeling, and image generation, demonstrate that IC is effective in improving the performance of pruned models.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes an input compensation method for pruned models. which builds a compensation pool and learns the pool by minimizing the reconstruction loss. The authors empirically demonstrate the effectiveness of IC across extensive NLP and CV tasks.

### Strengths
The manuscript proposes an interesting idea that it uses input compensation to minimize the accuracy loss caused by weight pruning. The proposed IC shows good accuracy improvement on extensive experiments. In-depth analysis is conducted to investigate key components of IC.

### Weaknesses
1. The major concern is the proposed method may introduce a significant amount of additional computation cost, resulting longer inference latency. For CLIP models, while the authors claim that the pruned image encoder is used as the encoder of IC, as illustrated in Fig.1, the proposed method has to run through an additional Encoder(ViT), which is time-consuming. The authors should add the comparisons of computation cost and inference speed.
2. For structured sparsity experiments, following [1], using 2:4 pattern instead of 4:8 pattern may be better, as advanced GPUs support 2:4 pruning acceleration.
3. The proposed method is not clearly explained. More implementation details should be added.

### Questions
1. For CLIP experiments, the authors mentioned 'The compensation pool is shared across all ten tasks'. I suppose the pool is learned on one big dataset?
2. It would be better to provide the training time.
3. For NLP experiments, the authors claimed that they follow OWL[2] and focused on the case of 70\% unstructured sparsity. While the base pruning methods may fail at 70\% sparsity, it will be more fair to compare the case like 'wanda+owl' vs 'wanda+owl+IC'. Could IC be well combined with OWL?

[1] Mishra, Asit, et al. "Accelerating sparse deep neural networks." *arXiv preprint arXiv:2104.08378* (2021).
[2] Yin, Lu, et al. "Outlier weighed layerwise sparsity (owl): A missing secret sauce for pruning llms to high sparsity." *arXiv preprint arXiv:2310.05175* (2023).

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents an approach to improve pruned model performance through input compensation, offering a new perspective by optimizing the input space instead of the parameter space. Experiments and analysis on several baseline methods and benchmarks validate the effectiveness of the proposed input compensation approach.

### Strengths
- The paper is easy to follow, and the input compensation (IC) method is clearly stated.
- The method is evaluated across several tasks including image classification, language modeling, and image generation.
- The performance gain of the proposed IC over the CLIP ViT-B model on several baseline methods like SparseGPT and Wanda is notable.

### Weaknesses
- While the main goal of network pruning is to reduce computational costs, the introduction of an encoder and attention-based compensation mechanism appears to add more computational overhead during inference. It would be better for the authors to clearly quantify the additional computation and memory costs introduced by the compensation mechanism.
- The optimization process for the compensation pool needs a more detailed explanation, as the approaches described in Sections 5.1 and 5.2 seem quite different.
- The evaluation lacks testing on the widely adopted structured 2:4 sparsity setting, which is an important baseline for practical applications.
- The sparsity calculation needs clarification, especially considering the additional parameters introduced by the compensation pool and the encoder.
- It would be better to list the detailed environment for better reproducibility including hardware and software.

### Questions
- It is stated in Sec 5.1 of the paper that the compensation pool is shared across all tasks. How does the compensation vary across different input types and model architectures?
- In Table 4, only the result under 70% sparsity setting is reported. How's the performance of applying input compensation under the 50% sparsity setting? It would be better to directly compare with the result reported in the original Wanda paper for fair comparison.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper delves into pruning LLMs by focusing on input compensation rather than model parameter adjustment. The authors introduce a method that learns a compensation pool, consisting of multiple candidate compensations, using an attention mechanism on calibration data. This method has been tested on both classification and language tasks, demonstrating its ability to enhance the performance of pruning methods like Wanda and SparseGPT to a certain extent.

### Strengths
1. **Innovative Approach:** The article presents a fresh perspective on reducing reconstruction error in sparse LLMs by adjusting inputs instead of traditional parameter optimization. This approach potentially opens new avenues for LLM pruning.    

2. **Theoretical Justification:** The discussion in section 4.1 provides a solid theoretical basis. By decomposing model parameters into a sparse matrix, \(S\), and a low-rank matrix, \(AB\), the authors argue convincingly that removing the \(AB\) portion and learning it back can recover performance effectively.

### Weaknesses
1. **Similarity to Prompt Tuning:** The method bears a resemblance to prompt tuning, with the primary difference being the integration manner (addition versus concatenation). A direct comparison between the proposed method and prompt tuning could clarify their distinct advantages and limitations. 
2. **Experimental Scope:** The experiments primarily compare the proposed method with post-training sparsity methods that do not involve backpropagation. This seems limiting, as the method aligns more closely with sparse LLM fine-tuning strategies. A comparison with similar methods that also leverage fine-tuning, such as DsNot[1], would provide a more comprehensive evaluation of its effectiveness. 
3. **Unclear foundation:** Although it is interesting to model parameters as a low-rank matrix plus a sparse matrix, how exactly is the sparsity of \( S \) defined? Does it mean that all levels of sparsity (50%, 60%, 70%) are compatible with such a formulation?  Furthermore, there are many possibilities for deciding sparse matrices. Can all types of sparse matrices be adequately represented by adding a low-rank matrix (as the proposed IC method)?

[1] Dynamic Sparse No Training: Training-Free Fine-tuning for Sparse LLMs. In ICLR, 2024.

### Questions
Please see the weakness part.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
[Update]

Thanks for the authors' feedback. My questions have been answered in the authors' feedback. I can see some value of this work, based on its improvements over baseline methods on the reported benchmark datasets. However, the proposed method can be framed as a special LoRA method, to some extent. Although LoRA is applied to model weight, for a deep network the weight compensation in the current layer is actually the "Input Compensation" to the next layer. So it is hard to claim a strong novelty for this work.

Based on the above consideration, I would like to keep my initial vote.

----- Original Review ----- 

In their research, the authors introduced a new approach to enhance the precision of pruned large language models. This innovative technique involves compensating the input with a learned $\Delta_x$ value, which is calculated using a learnable attention-like linear layer. The method necessitates fine-tuning on the target dataset. To establish the effectiveness of their proposed approach, the authors conducted experiments on various popular vision and language assessment datasets.

### Strengths
* The authors presented comprehensive numerical evaluations on popular benchmarks and compared it with multiple prominent baseline methods, including magnitude pruning techniques, Wanda, and Sparse GPT.

* The proposed technique can be utilized in both vision and language models, as it is agnostic to the specific model architecture. This allows for versatility in its application across various domains of artificial intelligence and machine learning.

### Weaknesses
* The proposed method for Input Compensation (IC) has some limitations in terms of novelty. The primary idea is similar to weight compensation techniques, except it diverges from such approaches by focusing on input space. It is noteworthy that an IC method can be transformed into a weight compensation method, as the two strategies are "dual" to one another.

* While the reported improvements seem to be promising, it is essential to consider their fairness in comparison to the baseline methods. The proposed IC method necessitates re-training and fine-tuning on the target dataset, which may introduce bias in the evaluation results if the baseline methods were not similarly fine-tuned. In such cases, it would be reasonable to conclude that the proposed technique's performance could potentially be attributed to the difference in fine-tuning processes rather than solely due to its inherent merits.


* It is important to note that the proposed IC method does introduce additional learnable parameters, which might not be considered when comparing the models’ sparsity levels. This could lead to an inaccurate estimation of the actual sparsity levels of both the original model and the proposed technique. Therefore, it is crucial to consider these extra parameters when evaluating the sparsity levels and overall performance of the models in question.

### Questions
* If the baseline models were not fine-tuned in the comparison, please report the fine-tuned version of these models / methods.
* When computing the sparsity level, is the additional learnable parameters counted in the IC-related numbers?

### Soundness
2

### Presentation
2

### Contribution
1

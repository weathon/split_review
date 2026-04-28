# Two Sparse Matrices are Better than One: Sparsifying Neural Networks with Double Sparse Factorization

- Decision: Accept
- Avg Score: 6.33
- Scores: 6, 8, 5

## Abstract
Neural networks are often challenging to work with due to their large size and complexity. To address this, various methods aim to reduce model size by sparsifying or decomposing weight matrices, such as magnitude pruning and low-rank or block-diagonal factorization. In this work, we present {\bf Double Sparse Factorization (DSF)}, where we factorize each weight matrix into two sparse matrices. Although solving this problem exactly is computationally infeasible, we propose an efficient heuristic based on alternating minimization via ADMM that achieves state-of-the-art results, enabling unprecedented sparsification of neural networks. For instance, in a one-shot pruning setting, our method can reduce the size of the LLaMA2-13B model by 50\% while maintaining better performance than the dense LLaMA2-7B model. We also compare favorably with Optimal Brain Compression, the state-of-the-art layer-wise pruning approach for convolutional neural networks. Furthermore, accuracy improvements of our method persist even after further model fine-tuning.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposes Double Sparse Factorization (DSF) of the weight matrices to prune them effectively. They formulate it as an alternating optimization and optimize using ADMM. The experiments show a clear benefit of the proposed method on Llama for a language task and resnet on image classification.

### Strengths
1. The idea is nice, the problem formulation is neat, and using ADMM for optimization is elegant. 
2. On pruning LLAMA, the method shows clear benefit over the compared methods. Image classification experiments are marginally better than previous methods.

### Weaknesses
1. The SVD comparison is unfair in my opinion. SVD is more suited for low-rank compression and it may not enforce sparsity. Using the sparsity ratio as the main criterion may not be ideal. Why not use FLOPs? As FLOPS directly relates to inference speed as opposed to sparsity ratio. I would suggest that the authors include a comparison based on FLOPs in addition to the sparsity ratio. This would provide a more comprehensive evaluation of computational efficiency across different compression methods, including SVD and sparse factorization approaches.
2. ADMM optimization may be compute-intensive. Not much discussion about it unless I missed something. Could you provide an asymptotic time complexity analysis and/or empirical running time comparison of the ADMM? You may also discuss the trade-offs between computational cost and compression quality, as it would give readers a clearer understanding of practical applicability of the proposed method.

### Questions
1. Could you discuss how this is related to sparse coding?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This work introduces double sparse factorization (DSF) which combines matrix decomposition with pruning to yield compressed neural networks with better generalization performance than the baselines used for comparison. The authors demonstrate that their proposed algorithm, an extension of the alternating direction method of multipliers (ADMM) algorithm, is capable of achieving competitive results when compressing pretrained LLMs and CNNs.

### Strengths
* While pruning of factors obtained from matrix decomposition is not a novel contribution per se (Le Magoarou & Gribonval, 2016), its application to pretrained model compression is novel as far as I know. In any case, this work clearly distinguishes itself from prior art by focusing on the model compression task, particularly in the context of LLMs. 
* The paper is well written. 
* The empirical results outperform strong, SOTA baselines in a variety of contexts for LLMs and CNNS. 
* The authors take care to consider some of the practical concerns of their method, such as masking overhead. The demonstration of the generalization of DSF with a shared fixed A factor mask is particularly compelling. 
* Compression and efficient inference is of particular importance as model sizes continue to grow and scale. As such, this work addresses a timely and important topic.

### Weaknesses
Overall, I am leaning towards accept. However, I have some significant concerns regarding the practical applicability of the proposed method. Fundamentally, we require compressed models that offer advantages in one or more of the following dimensions: memory overhead, latency, and/or throughput. For each of these dimensions, we can consider both training and inference. For the following discussion, let’s consider an intermediate fully-connected layer from a decoder block in a  LLaMa 2-7B @ 50% sparsity. This layer’s weight tensor is of shape (11008, 4096).

* Fine-tuning (FT) / training memory overhead: During FT, the proposed method requires ~37% more memory to store the intermediate activations of X@A@B compared with X@W. Activations can account for a significant portion of the overall memory footprint during training and this should be acknowledged in the paper. The increased memory footprint for storing intermediate activations during backpropagation could limit the batch size that can be used during fine-tuning, potentially impacting the convergence and final performance of the model.
* Mask overheads: Assuming a bit-mask compression strategy and no shared masks between A factors, we find a similar 37% increased overhead compared to single layer sparsity. With shared A factors this overhead drops to ~1%, assuming the mask is shared across all 36 decoder blocks. From this perspective, I find the fixed-mask variant of DSF to be the most practically interesting. The overhead of storing masks, especially without sharing, could negate some of the benefits of compression, particularly for smaller models or resource-constrained environments. The paper should provide a more detailed analysis of the trade-offs between mask storage and model size.
* Indices instead of bitmasks: In the introduction, the authors suggest using indices to store the locations of non-zero elements. However, given that we require uint16 indices to represent all positions in this weight tensor, this would only be practical at sparsities >= 15/16 compared to bit-masking. Given that this is currently an unobtainable level of sparsity for LLMs and roughly the limit at which we are able to find performant CNNs I find the suggestion to use indices to store non-zero locations poorly motivated. The paper should clarify the practical scenarios where index-based storage would be beneficial, given the high sparsity requirements.
* Latency and Throughput: This is the most challenging dimension to estimate. Although the FLOPs analysis suggests similar performance to OBC, this may be misleading considering the additional matmul operations required in the low-rank decomposition and subsequent increase in overall memory bandwidth required to store and load intermediate activations between subsequent matmul kernel calls. I would be more convinced of the practical application for DSF if the authors include a discussion on runtime latency. This could be supported by preliminary benchmarking using Neural Magic’s DeepSparse Engine which would offer some empirical evidence of improved runtime properties. The paper should include a more detailed analysis of the impact of the additional matrix multiplications on overall latency, including a breakdown of the time spent in each operation.
* 2:4 support: It’s unclear if the proposed method can support 2:4 sparsity as this would require a fixed sparsity level of 50% for both factors. The authors found that a smaller level of sparsity (~33%) yields the best performance but this prohibits using 50% sparsity in both factors as required for 2:4. The inability to directly support 2:4 sparsity could limit the applicability of the method in hardware that is optimized for this format. The paper should discuss the potential for future work to explore 2:4 sparsity.
* Hyperparameter sensitivity: There are a number of specific sparsity values used in the experimental method (16% sparsity, 25% sparsity, etc.). How sensitive is DSF to these values? If DSF is applied to a new model family, is it required to perform a hyperparameter search to find the optimal sparsity level for the smaller factor? How were these sparsity levels found? Could the authors add the results of their hyperparameter sweep for these values, assuming this was how the values were determined. The paper should include a more detailed analysis of the sensitivity of the method to the sparsity levels of the factors, including a discussion of the potential impact on performance and the computational cost of hyperparameter tuning.
* Reliance on PPL: The authors claim that their method “is the first layer-wise pruning method in which the larger pruned model is better than the dense smaller model.”. I believe this claim requires more evidence to support, namely, downstream evaluation for the compressed LLMs on real-world tasks. I would be more willing to support this claim with empirical results from the pruned models on OpenLLM Leaderboard v1 or similar. Relying on perplexity alone has been shown to be misleading for compressed models [1]. The paper should include a more comprehensive evaluation of the compressed models on a range of downstream tasks to validate the claim that the pruned models outperform smaller dense models.
* LLM fine-tuning: The fine-tuning results section would benefit from expanding its scope to include fine-tuning of the compressed LLMs. I would also be interested to see what the memory overhead looks like for DSF when naive masked sparsity is used. The paper should include a more detailed analysis of the memory overhead during fine-tuning of DSF models, including a comparison with naive masked sparsity.

### Questions
* Specifically which LLaMa model is used for reporting the results in Table 1? The authors refer to both LLaMa 1 and 2 in their experimental setup. 
* Does DSF provide latency/throughput benefits over dense or typical sparse networks (single layer sparsity) when using DeepSparse Engine? 
* Can DSF be extended to 2:4 sparsity? What is the trade-off with generalization performance? 
* How do the pruned LLMs compare when evaluated on OpenLLM v1 leaderboard evaluation tasks?
* Missing results for Wanda at 70% sparsity: Why were these not included in Table 1? 
* What is the memory overhead when fine-tuning DSF LLMs in a naive way (i.e., with masked paramters intead of compressed representations)?

### Soundness
3

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
The paper proposes Double Sparse Factorization, a method that, instead of pruning the original weight matrix, factorizes it into the product of two matrices (similar to e.g. low-rank decomposition), which together satisfy the same sparsity constraint. To solve this problem, they use the ADMM method. The paper claims to improve upon existing pruning and layer-wise pruning approaches, and they back their claims with experiments on state-of-the-art language models and medium-sized vision models. In addition, they show that the superiority of their methods seems to prevail after retraining the pruned models.

### Strengths
The idea is interesting, to the best of my knowledge relatively novel, and the experiments are quite convincing. Most of the paper is fairly easy to follow and the reader is not left with many questions. I appreciate that the authors provide results before and after retraining the pruned models, as this is often not done in other papers. The proposed method is interesting, however there are open questions that I will discuss below.

### Weaknesses
I have several concerns regarding the soundness, clarity, and contribution of this work, which I detail below. I hope these remarks are helpful for improving the paper and am open to discussing my evaluation.

### Clarity
While I think that the idea proposed in this paper might be promising, I sometimes had a hard time following the paper. I think the structure as well as details could be improved.
- Section 3.1 would greatly benefit from a more detailed explanation of the ADMM method. How are Z and U initialized? I understand that it is not your job to explain ADMM in detail, but I think that nevertheless the paper would greatly benefit from more detailed remarks - at least in the appendix. Since this method is not standard (at least in the pruning literature and to my knowledge), I think it would be helpful to make this more clear.
- In two sentences (Line 149, 150) you basically explain how you find the sparsity mask. Why do you precondition? How exactly is the cubic schedule (I presume Zhu & Gupta?) implemented, over how many iterations, with which interval between the increases? I am trying my best to infer this from somewhere, but it is nowhere to be found? Either I am missing something or the paper is lacking a crucial part, namely how the sparsity mask is found.
- In Line 258, you state that you are using the Wanda saliency map, I think it would be good to give the mathematical formulation to that, especially how you "scale one of the factors back".


### Soundness
- Lines 37-39: If you replace the dense weight matrix with a product of two sparse matrices, will your model not be much slower at inference than when replacing with just a sparse matrix? For Low-rank decomposition, you at least get two linear layers which are much smaller dense matrices, but in your case, you basically have two sparse matrices. While you argue in Line 162 that the total number of multiplications is equal, this is far from realizable on the existing hardware. In practice, you incur a non-trivial overhead. I would like to hear the authors' thoughts on this.
- Line 50: "our method is the first layer-wise pruning method in which the larger pruned model is better than the dense smaller model" - Are you sure this is true? I feel like already the original SparseGPT paper gets fairly close and there have been a variety of improvements since then, e.g. using non-uniform layer-wise sparsity. Maybe this claim can or should be made more precise.


### Experimental Validation
- Missing ablations: The paper is fixing a lot of hyperparameters and making claims without ablations. That includes e.g. the selection of sparsity distribution between the matrices (Line 209) or the initialization for A and B (Lines 248-250), among others. Such ablations should be added to justify the choice of parameters.
- Table 1: Why are you not comparing to SparseGPT, am I missing something? In my experience, SparseGPT is a very strong baseline. Also, why do you omit Wanda for 30% density? Is Wanda using a "finalization" step as well, i.e., are you reconstructing the remaining weights after pruning? You get that more or less for free if you pass the calibration data through anyway.
- Section 5.4: I find the choice of hyperparameters for the retraining/fine-tuning quite arbitrary. You use a stepped schedule for most of the pretraining, then use a stepped learning rate schedule for retraining as wellf 70 total) epochs. [1] shows that if you properly choose the initial learning rate of a linear schedule, you can recover the accuracy drop of magnitude pruning in very few iterations. I am not sure if these results would withstand scrutiny. It would be good to use best practices here, i.e., for the convolutional networks you can definitely use a linear/cosine schedule for pretraining, and then choose the initial learning rate for linear-schedule-retraining adaptively, as in [1]. This will give much more realistic results.


### Minor Remarks
- Line 131: I presume it should be "**the** layer-wise pruning problem".
- In general, you do not seem to use the glossary package and define your DSF-acronym over and over again. That is a bit contrary to the purpose of an abbreviation. Also, you sometimes use DSF, and sometimes DFS (as in Double Factorization Sparse), see e.g. Line 315 or the caption in Line 686 where this happens in the same sentence.

### Questions
- In Line 465 you state that your method does not support gradual pruning with fine-tuning between pruning steps, could you elaborate why? I am not sure what I am missing here.
- In Line 196, you first "look into the projection problem". I am not quite sure I understand correctly how that is not the entire problem? A proper solution to that is what you are looking for, isn't it?

### Soundness
2

### Presentation
2

### Contribution
2

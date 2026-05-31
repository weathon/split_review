## Human Reviewer 1

### Summary
This paper proposes LoLoRA (Locally Fine-Tuned Low-Rank Adapters), a modification of LoRA that introduces local unsupervised updates for the adapter matrix A to reduce activation memory usage during fine-tuning. Instead of keeping Acompletely frozen as in LoRA-FA, LoLoRA applies Hebbian PCA (HPCA) or autoencoder-based local updates in the forward pass while updating B through backpropagation. The authors provide a theoretical analysis showing that optimal A initialization aligns with the principal subspace of the input covariance matrix and validate this through experiments on RoBERTa-Large (GLUE), LLaVA-v1.5-7B, and TinyLlama-1.1B.

### Strengths
1.	Clear theoretical grounding: The paper provides a well-formalized theoretical motivation for the proposed local learning rule, which rigorously characterize optimal conditions for the adapter matrices.
2.	Readable structure and comprehensive related work: The manuscript is well-organized, situating LoLoRA among recent LoRA variants (EVA, LoRA-FA, Adalora, etc.) and giving clear algorithmic descriptions.

### Weaknesses
1.	The main motivation is to improve LoRA-FA by locally updating the frozen A matrix, but the improvement appears incremental and not conceptually substantial. The paper may be seen as a minor extension of LoRA-FA with limited novelty.
2.	The background explanation of why freezing A reduces GPU memory is brief and could be clarified with a more detailed analysis or quantitative breakdown of memory components saved (activations vs. optimizer states).
3.	Experimental results, especially in Table 3, show negligible GPU memory savings (24.6 GB → 24.1 GB). It is unclear whether the trade-off justifies the added algorithmic complexity.
4.	The models and training scale are relatively small. For the multimodal experiment, only one epoch is trained on 10% of LLaVA 150K. This leaves uncertainty about convergence and whether LoLoRA would maintain its advantage under full-scale training or with more epochs.

### Questions
1.	What do the convergence curves look like for different methods (LoRA, LoRA-FA, LoLoRA)? Is there a noticeable difference in early-stage convergence speed?
2.	Since freezing or locally updating A yields limited memory savings, can the authors quantify the exact memory components saved (e.g., activation cache, gradient tensors, optimizer states)?
3.	In LoLoRA, the local optimizer introduces extra states for A; how significant is this overhead compared to the saved activation memory?

### Soundness
3

### Presentation
3

### Contribution
2

### Rating
4

### Confidence
4

---

## Human Reviewer 2

### Summary
The paper introduces LoLoRA, a modification of LoRA designed to reduce activation memory usage during fine-tuning. It updates the adapter matrix $A$ locally (via a Hebbian-style or PCA-like rule, or AE) during the forward pass, avoiding backpropagation and storage of input activations. Adapter $B$ is updated normally through backprop. The authors provide an analysis showing that the initialization is important and conduct experiments on GLUE, LLaVA, and TinyLLaMA to validate the method's performance and efficiency.

### Strengths
- The paper connects LoRA initialization with PCA-based optimal subspaces under a random regression model, offering insight into the asymmetry between $A$ and $B$ adapters. 
- Introducing local updates for LoRA aligns with current efforts to reduce memory in PEFT. 
- The problem this paper tackles is essential.

### Weaknesses
- The empirical results are not good enough. The claimed performance-efficiency tradeoff is not convincing, as LoLoRA's memory savings are minor (on the order of a few hundred MB) and do not justify the added algorithmic complexity; also, it underperforms. 
- The experiments are limited to very low ranks ($r={2,4,8}$). 
- The theory gives intuition but lacks empirical validation under realistic conditions. 
- The paper requires major writing improvements; phrasing needs to be improved, and organization is uneven. 
- Comparison to more baselines is needed; e.g., to other memory-efficient PEFT methods (e.g., orthonormal LoRA, rank selection, and so on). The current baseline selection is limited. 
- No runtime or compute cost analysis is given.

### Questions
Please refer to the above weaknesses.

### Soundness
2

### Presentation
1

### Contribution
2

### Rating
2

### Confidence
4

---

## Human Reviewer 3

### Summary
LoRA was developed to reduce the memory requirements for a model, reducing the size of the trained parameters at fine-tuning. However, the size of the activations is the same for fine-tuning as for LoRA. LoLoRA solves this by not storing the inputs to each linear module $z$ but instead freezes parameter $A$ and stores $Az$. Building on the work of LoRA-FA, A is initialized in a more theoretically-grounded way to assist in training. This matrix then is updated locally to regain the expressiveness of LoRA training both $A$ and $B$. Theory is developed to determine what the best update to $A$ would be, relating it to the eigen-decomposition of the empirical covariance matrix. This method is then tested against standard LoRA and LoRA where A is frozen on language models and language-vision models.

### Strengths
- The core concept of keeping A frozen to reduce memory requirements significantly while also updating A through non-gradient methods is very appealing. Prior work keeping A frozen is clearly improved upon by learning A without the same scale of gradient as is needed for standard LoRA
- The updates to A are theoretically grounded, leading to some nice theoretical understanding of what A will be learned
- All experiments are run multiple times, where every experiment has its error bars clearly listed

### Weaknesses
- Parts of the writing are quite hard to follow. The abstract mentions the "adapter" A which wasn't clear in its meaning as one of the two LoRA matrices. There are also references to "local updates", which seem to mean updates that do not involve a gradient; this understanding only came after reading much of the paper in depth
- The method is named LoLoRA, yet this name is unused in the tables, making it difficult to parse what are the results to be compared against. Using the name LoLoRA-HPCA would be much clearer
- The results aren't very strong, with Table 1 and 2 both showing that these method is typically of worse performance than simply freezing A
- Only after a number of reads was it noticed that there are no figures. While not necessary, a figure depicting how LoLoRA works and its back-and-forth between optimizing B with gradients and optimizing A with this local update would be invaluable

### Questions
- Can the memory requirements for Table 1 and 2 also be shown? In those situations, having a comparison of required memory would lend stronger credibility to LoLoRA as it uses less memory than LoRA
- What is being shown in Table 4 and 5? They seem like perplexities but it’s unclear

### Soundness
3

### Presentation
2

### Contribution
3

### Rating
4

### Confidence
3

---

## Human Reviewer 4

### Summary
This paper proposes a new LoRA finetuning method which reduces the memory usage. The idea is to use a local update rule for training the A matrix. Prior work has suggested freezing matrix but this leads to reduced performance. The method in this paper aims to bridge that gap. With the local update rule, the activations generated by A no longer need to be saved. The local update is performed using a Hebbian learning rule which in an online fashion estimates the top-r eigenspace of the input activation covariance. Using the top-r eigenspace has been previously suggested as a data-drive initialization for the A matrix. The authors prove the optimality of this setting of the A matrix under an isotropic prior for the ideal update. The B matrix is trained normally. The authors perform a variety of experiments demonstrating that their algorithm can preserve the performance of vanilla LoRA while reducing the memory usage.

### Strengths
The idea is simple and clearly motivated. The experiments are thorough. The performance does not seem to degrade when using the local rule.

### Weaknesses
The isotropic assumption on $\Delta W$ is a bit of a stretch. That said, the resulting update still seems reasonable and it unclear if there are more meaningful and tractable assumptions.

In a small setting, there could be a sanity check that the top-r eigenspace is being learned accurately by the online algorithm and there can be a comparison when the true exact eigenspace is used.

Some of the theoretical arguments could be less dense and written more clearly.

### Questions
How does the step time compare with vanilla LoRA?

### Soundness
4

### Presentation
3

### Contribution
3

### Rating
8

### Confidence
3
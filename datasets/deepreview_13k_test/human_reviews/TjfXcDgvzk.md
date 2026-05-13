# NOLA: Compressing LoRA using Linear Combination of Random Basis

- Decision: Accept
- Scores: 6, 6, 6, 6

## Abstract
Fine-tuning Large Language Models (LLMs) and storing them for each downstream task or domain is impractical because of the massive model size (e.g., 350GB in GPT-3).
Current literature, such as LoRA, showcases the potential of low-rank modifications to the original weights of an LLM, enabling efficient adaptation and storage for task-specific models. These methods can reduce the number of parameters needed to fine-tune an LLM by several orders of magnitude. Yet, these methods face two primary limitations: (1) the parameter count is lower-bounded by the rank one decomposition, and (2) the extent of reduction is heavily influenced by both the model architecture and the chosen rank. We introduce \nola{}, which overcomes the rank one lower bound present in LoRA. It achieves this by re-parameterizing the low-rank matrices in LoRA using linear combinations of randomly generated matrices (basis) and optimizing the linear mixture coefficients only. This approach allows us to decouple the number of trainable parameters from both the choice of rank and the network architecture. We present adaptation results using GPT-2, LLaMA-2, and ViT in natural language and computer vision tasks. \nola{} performs as well as LoRA models with much fewer number of parameters compared to LoRA with rank one, the best compression LoRA can archive. Particularly, on LLaMA-2 70B, our method is almost 20 times more compact than the most compressed LoRA without degradation in accuracy

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Low Rank Adaptation (LoRA) presents a series of drawbacks, particularly its constrained parameter reduction due to rank-1 matrices, which cannot be further diminished. Additionally, LoRA's parameter count is heavily reliant on the model's architecture. In response to these limitations, this paper suggests an innovative solution by advocating the use of a linear combination of random projections to replace LoRA's update matrix, effectively addressing the issues mentioned earlier. This approach is inspired by the previous paper known as PRANC. Personally, I found the paper to be a valuable source of knowledge and a unique one, appreciating its quirky yet straightforward idea

### Strengths
**Leveraging Ideas from Other Papers for Enhanced Parameter Efficiency:** This paper skillfully incorporates concepts from existing research to optimize parameter efficiency.

**Achieving Comparable or Superior Performance to NOLA:** This research attains performance levels akin to LoRA while significantly enhancing parameter efficiency.

### Weaknesses
**Poorly presented results**-  The main issue in the presentation of the results lies in their lack of clarity and explanatory depth. Firstly, the results fail to offer any substantial insights into how the method operates, leaving readers without a clear understanding of the underlying mechanisms. Additionally, Tables 1 and 5 are presented as mere lists of numbers without the necessary context or explanation, making it challenging for the audience to derive meaningful conclusions from the data. A critical element that appears to be missing is a discussion of what works better and the reasons behind it, which is crucial for a comprehensive understanding of the findings. To improve the presentation of the main results, it is essential to provide better explanations and context for the data, as well as a deeper analysis of what drives the observed outcomes.

### Questions
1. GPT2-L and GPT-2M seems to perform the same for LoRA. Is there any explanation on why this is the case?
2. The presentation of results preceding the training details in Section 3.1 seems to be an inadvertent oversight. To enhance the logical flow of the content, it is advisable to reverse the order, placing the training details before the results.What happens when you increase the number of parameters for NOLA?  - Does it perform better than LoRA. For example results of NOLA with 0.35M parameters
3. How does NOLA's performance change when the number of parameters is increased? Does it outperform LoRA? For instance, are there any results available for NOLA with 0.35 million parameters?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a new approach for fine tuning LLMs for downstream tasks. The key idea is to replace the low rank updates of LoRA with linear combinations of fixed random matrices for which only the coefficients need to be tuned and stored in memory which significantly reduces the storage cost. The authors present experiments in both language and vision tasks where their approach preserve the accuracy of LoRA while reducing the parameter count by half or more.

### Strengths
1. The authors propose a novel, intuitive, and principled approach to address the problem of task based fine tuning of transformer based models.

2. The proposed approach shows significant reduction in storage overhead without compromising on accuracy across a range of experiments in both language and vision tasks.

### Weaknesses
1. The technical novelty is relatively minor with the overall idea being a combination of prior works PRANC and NOLA. While this seems enough to provide empirical improvement, the approach itself is not that big of an innovation over prior works. 

2. While the prior approach PRANC is directly modified by the authors in this work there are no direct comparisons with it in either the language or vision tasks used to evaluate the proposed approach. There is a comparison of training loss in Section 3.4 and a comparison of the rank of possible solutions of the two approaches in Section 3.5 but without a direct comparison of test accuracy it is unclear if this approach is indeed an improvement over the baseline that it directly modifies.

### Questions
1. Why is the training time of NoLA with shared random basis similar to that of LoRA when the training time of NOLA with a unique random basis is higher? Aren't the number of coefficients being trained, the same in both cases?

2. The ablation study at the end of Section 3.1 appears inconclusive. Is there any takeaway on the effect of varying the rank in NOLA?

3. In Section 3.2 if only $\alpha$ and $\beta$ are quantized while A and B are not then won't that be less memory efficient than quantization in LORA?

4. Please highlight the entries in Table 5 with the best performance for a given scenario. Currently there are too many entries, and it is too difficult to figure out which method is better for which case.

5. If each matrix in PRANC has size $d^2$ then why do we need multiple matrices to cover the rank of the original $\Delta W$ matrix (which also has size $d^2$)?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper looked at the problem of memory requirements for Low-Rank Adaptation (LoRA) and proposed NOLA to break the rank one lower bound present in LoRA. The core concept behind NOLA is to reparameterize a neural network using a linear combination of pseudo-randomly generated weights.

Thanks to the authors for a more detailed explanation of the motivations for the paper and for some of the latest research supporting them. Therefore, I will increase the rating by 1 point.

### Strengths
1. The paper discusses related works in detail and clearly summarizes its own contributions.
2. The paper performs extensive experiments to compare NOLA and existing PEFT solutions.
3. NOLA decouples trainable parameters from the choice of rank and the network architecture.

### Weaknesses
1. The work may need more rationales upfront to motivate the problems (i.e. the rank one lower bound present in LoRA). Given that mainstream GPUs have tens of GB of memory, it is reasonable to reduce the memory requirements from tens of GB to tens of MB at the expense of model quality through LoRA, as this can indeed reduce resource consumption and greatly reduce LLM transition overhead during inference. However, I don't think it makes much sense to further reduce memory requirements to several MBs at the expense of model quality.

### Questions
If users want to use the trained model on different versions of GPUs or software, how to ensure the consistency of the trained model? In such a situation, the same seeds can not generate the same pseudo-random matrices.

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a technique to reduce the number of trainable parameters while fine-tuning large language models and large vision encoders. Their technique involves modeling the weight update matrix as a linear combination of fixed random matrices that are also rank-constrained. The fine-tuning process then involves learning just the coefficients in the linear combination. When the proposed technique is used, any updates to the models requires the communication/ storage of only the coefficients and the random seeds required to generate the codebook matrices (apart from the base weights of the original model of course). 

The authors demonstrate that the proposed technique preserves the performance on the fine-tuning task while achieving large ( up to 1/20 x baseline models) reduction in the number of trainable parameters. This is shown in both language and vision domains. In the language domain, they show it on the NLG challenge dataset. In the vision domain, they show is on CIFAR, CUB and Caltech-101 datasets.

### Strengths
- The paper is well motivated and clearly written. 
- Parameter-efficient fine-tuning is a popular area of research currently and this paper makes a good contribution to this area.
- The proposed technique is interesting and the results demonstrate that the method preserves performance while achieving a low parameter count 
- The proposed method helps overcome the some of the limitations of methods such as LoRA, as described in the paper

### Weaknesses
I appreciate the results provided in the paper. But I think that some more in-depth evaluation and some more explanation of the current results would add value to the paper. I outline some specifics below.

Language experiments: 
- Why does full fine-tuning achieve much lower performance in Table 1?
- Could the authors also provide the performance of the GPT-M, L models *without any fine-tuning* on the tasks considered? This will give the readers an idea of how much improvement is being achieved. 

Vision experiments: I find the experiments provided in this section (3.3) a bit weak. The main reason being that the ViT models pre-trianed on imagenet are already pretty powerful. Fine-tuning these models on much smaller and easier datasets such as CIFAR may not be the best way to demonstrate usefulness. In particular, I have the following comments:

1. Can the authors try their techniques on more challenging datasets? 
2. Although the number of parameters for the linear layer baseline depends on the dataset, it would be good to have this information visible in the Table. 
3. As before, can the authors provide the performance of the models considered without any fine-tuning? (0-shot classification on the downstream datasets)

### Questions
1. What is the distribution used to generate the random basis matrices? Did the authors experiments with a few different choices?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

# Encryption-Friendly LLM Architecture

- Decision: Accept
- Avg Score: 6.33
- Scores: 6, 8, 5

## Abstract
Large language models (LLMs) offer personalized responses based on user interactions, but this use case raises serious privacy concerns. Homomorphic encryption (HE) is a cryptographic protocol supporting arithmetic computations in encrypted states and provides a potential solution for privacy-preserving machine learning (PPML). However, the computational intensity of transformers poses challenges for applying HE to LLMs. In this work, we propose a modified HE-friendly transformer architecture with an emphasis on inference following personalized (private) fine-tuning. Utilizing LoRA fine-tuning and Gaussian kernels, we achieve significant computational speedups---6.94$\times$ for fine-tuning and 2.3$\times$ for inference---while maintaining performance comparable to plaintext models. Our findings provide a viable proof of concept for offering privacy-preserving LLM services in areas where data protection is crucial.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper presents optimizations to LLM architectures to make them more friendly towards Homomorphic Encryption evaluation. Concretely, first they propose to use LoRA for fine-tuning, where the data used for fine-tuning is given in encrypted form. This is useful to avoid re-training a lot of parameters, since LoRA focuses on updating only a few weights. This minimizes the amount of homomorphic operations w.r.t. plain fine-tuning. They also observe that LoRA is useful for reducing the dimension of homomorphic matrix multiplications. Secondly, they replace Softmax-based with Gaussian Kernel attention. They show that this is a simpler function to evaluate in HE, leading to significant savings with little impact in accuracy.

### Strengths
The problem statement is well motivated. Several works are currently exploring evaluation of LLMs under FHE, and the potential applications are also quite compelling. This is an extremely difficult task in terms of achieving viable efficiency, and any method that advances the state-of-the-art in this direction is welcome. The results achieved here show that several optimizations in other domains, that is, LoRA and the use of Gaussian Kernels, turn out to be useful for the evaluation of LLMs in FHE. I am not aware of this observation being made and explored in this depth in other papers (it is worth mentioning https://arxiv.org/pdf/2410.00433, which appeared after the submission deadline).

### Weaknesses
I am not particularly impressed by the novelty of this paper. It uses existing FHE tools with existing ML optimizations. This may not be a weakness on its own given the positive results of combining these techniques, but I still think the improvement factors may not be big enough for these techniques to become "enablers" of private LLM applications in practice. Put differently, I am not convinced that the gains here are a significant enough to overcome the blockers that prevent LLMs + FHE from becoming more widely spread. The paper's core contribution seems to be the observation that LoRA and Gaussian kernels, previously explored in other contexts, can be beneficial for FHE-based LLM evaluation. While this is a valuable observation, the paper does not delve deeply into the specific challenges and nuances of adapting these techniques to the FHE setting. For instance, the paper does not provide a detailed analysis of the trade-offs between the approximation accuracy of the Gaussian kernel and the computational overhead in FHE. Furthermore, the paper does not explore the limitations of LoRA in the context of FHE, such as potential issues with the accumulation of approximation errors during iterative updates or the impact of quantization on the performance of LoRA parameters in encrypted form. These aspects are crucial for assessing the practical viability of the proposed approach.

### Questions
For reproducibility, can the authors comment on the source code? Whether they intend to make it public for validation?

Also for reproducibility (and in lack of code), I am interested in understanding better the polynomial approximations used. In Section E the authors talk about penalizing the model in a "pre-training stage". I am not sure I understand how this would work, especially in the context of secure inference (no fine-tuning). What do the authors mean exactly? The model owner retrains the model using this new loss function? Most prior works take a pre-trained model, changing only its non-linearities by polynomial while keeping its weights. What are the authors proposing to do here? Does this require changing the model's weights? Re-training?

### Soundness
4

### Presentation
4

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
As LLMs surge, privacy issue becomes important considering government-level regulations. Among methods in privacy-preserving machine learning, homomorphic encryption (HE) can provide cryptographic security by computing over encrypted data directly without extra communication like MPC. However, HE is not efficient to compute matmul or non-poly operations in the transformer-level scale. This work focus on fine-tuning stage with LoRA and softmax variant to create HE-friendly transformer architecture.

### Strengths
1. Compared to MPC approaches, n on-interactive property helps HE to be feasible to compute over large-scale LLMs without including considerable communication overhead among computing parties.
2. This work has a great focus on the fine-tuning stage to make LLMs secure for users, which also concentrates on the key components like attention layers in the transformer, and it is also combined with SoTA techniques like LoRA to make the process more efficient.
3. Writing with bottleneck-improvement pattern for LoRA and GK looks good for readers to figure out key ideas.

### Weaknesses
1. When you mentioned SoTA LLMs, you should notice that decoder-based models have been proved very powerful in generative tasks. After iteration of the recent few years, BERT series is not as useful and prevalent as decoder models. Hence, the significance to protect BERT-based model is less essential in the current LLMs. Furthermore, the choice of BERT limits the applicability of this work to a specific class of models, and it is unclear how the proposed techniques would generalize to more complex architectures like those used in GPT or other decoder-based models, which are more relevant for many current applications.
2. Although this work introduces how HE and CKKS work in the secure way, this work does not specify adversary model, such ability of adversaries, type of adversaries (e.g., semi-honest or malicious) and kind of attacks (e.g., member inference attack) this architecture counters with. The absence of a clear threat model makes it difficult to assess the actual security guarantees provided by the proposed approach. For example, it is not clear if the system is robust against adaptive adversaries or if it only protects against passive eavesdropping. Moreover, the paper does not discuss the potential for side-channel attacks or other implementation-specific vulnerabilities.
3. In the conclusion, this work is too vague on the future work. For example, how cryptographic community develops helps the improvement of this work (e.g., any change on HE). Also, how LLMs itself evolve may change security issue based on this work. It lacks specific directions for future research, such as exploring alternative HE schemes, addressing the computational overhead, or investigating the impact of model size and complexity on the performance of the proposed secure fine-tuning method. The conclusion should also discuss the limitations of the current work and how future research could address them.

### Questions
N/A

### Soundness
3

### Presentation
4

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
This paper starts from the poor performance problem of homomorphic encryption (HE) in transformer architecture and focuses on optimizing the speed of HE in it. Specifically, the scheme tries to avoid CCMM computations to solve the poor performance brought by full fine-tuning. In addition, this paper aims to address the difficulty of evaluating under HE with Softmax, the core idea of which is to replace Softmax with a Gaussian kernel. Finally, this paper carried out many experiments, and the results show that their scheme is comparable to existing schemes in terms of modeling performance, while at the same time, the computational speed has been significantly improved. The overall narrative of the paper is clear, and has good logic.

### Strengths
This paper is oriented to the problem of inefficiency of transformer architecture under HE, although the existing research has produced richer results. The main contribution of this paper is to enhance the speed of transformer architecture under HE, and the authors have carried out many experiments to verify the rationality and advantages of the scheme. I think the experiments in this paper are full, and the advantages of this paper are elaborated in terms of speed and model performance, which speed is emphasized in this paper. The experimental results are thorough and well-analyzed. Overall, this paper seems to incorporate some of the SOTA approaches in the current field and apply them to a widely researched topic.

### Weaknesses
1. Insufficient innovation. First, the topic chosen for this paper is a more widely studied one. Second, the solutions in this paper seem to be a direct combination and application of existing advanced schemes, and it is not intuitively obvious in the paper that the authors have improved on existing methods.
2. The description in 2.1 does not seem to be consistent with Figure 1. Furthermore, why does the statement “LLM weights are protected in the strict cryptographic sense (line 149)” hold?
3. Although the paper proposes a privacy-protecting LLM architecture, the security considerations of the model, especially against attacks and model theft, is insufficient.

### Questions
1.	One core idea of this paper to solve the difficulty of evaluating Softmax under HE is to replace it with Gaussian kernel, however, this method is very similar to that in the literature “Chen, Yifan, et al. Skyformer: Remodel self-attention with gaussian kernel and nystr\" om method. Advances in Neural Information Processing Systems 34 (2021): 2122-2135”. However, this paper does not describe the difference with this paper or even cite this literature. Is there a difference in the performance of the two? Furthermore, the polynomial approximation method of this paper seems to be very common way.
2.	In Section 3, is the author's approach in solving Bottleneck 1 just an application of some existing methods? If not, please clarify the differences and improvements.
3.	Does the use of LoRA and Gaussian Kernel affect the interpretability of the model? How does the author balance efficiency and explainability?

### Soundness
3

### Presentation
3

### Contribution
2

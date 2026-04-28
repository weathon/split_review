# AdaRankGrad: Adaptive Gradient Rank and Moments for Memory-Efficient LLMs Training and Fine-Tuning

- Decision: Accept
- Avg Score: 7.00
- Scores: 8, 5, 8, 6, 8

## Abstract
Training and fine-tuning large language models (LLMs) come with challenges related to memory and computational requirements due to the increasing size of the model weights and the optimizer states. Various techniques have been developed to tackle these challenges, such as low-rank adaptation (LoRA), which involves introducing a parallel trainable low-rank matrix to the fixed pre-trained weights at each layer. However, these methods often fall short compared to the full-rank weight training approach, as they restrict the parameter search to a low-rank subspace. This limitation can disrupt training dynamics and require a full-rank warm start to mitigate the impact. 
In this paper, we introduce a new method inspired by a phenomenon we formally prove: as training progresses, the rank of the estimated layer gradients gradually decreases, and asymptotically approaches rank one. Leveraging this, our approach involves adaptively reducing the rank of the gradients during Adam optimization steps, using an efficient online-updating low-rank projections rule. We further present a randomized SVD scheme for efficiently finding the projection matrix. 
Our technique enables full-parameter fine-tuning with adaptive low-rank gradient updates, significantly reducing overall memory requirements during training compared to state-of-the-art methods while improving model performance in both pretraining and fine-tuning. Finally, we provide a convergence analysis of our method and demonstrate its merits for training and fine-tuning language and biological foundation models.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The authors propose AdaRankGrad that learns to adaptively perform low-rank gradient updates in order to reduce the memory requirements needed to train a large language model. They base their idea on a theorem that shows that the gradients rank reach to 1 over time. Their results on datasets like CoLA, STS-B, and MRPC show that AdaRankGrad is promising at significantly reducing memory requirements while retaining competitive performance compared to GaLore and LoRA.

### Strengths
- Reducing memory requirements is a crucial part of training LLMs
- The paper is well-written and the proofs are well designed.
- The experiments are comprehensive.

### Weaknesses
 - The results of AdaRankGrad compared to GaLore and LoRA do not seem significant in Table. 2 How do you know if it is worth having yet another memory reduction method?
- How does this method compare to BlockLLM [1]? I see a lot of similarities between the two. 
- How does the iteration speed of AdaRankGrad compare to others like LoRA, and GaLoRE. Wouldn't the method be slow given that it needs to estimate the projection matrix?
- While Adam is popular, we shouldn't always have to use it. How would AdaRankGrad generalize to other optimizers? it seems that AdaRankGrad is limited to Adam.

### Questions
Could you address the weaknesses above?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper introduces a method named AdaRankGrad, aims at enhancing the memory efficiency of fine-tuning LLMs. The authors find and formally prove that the rank of estimated gradients gradually decrease to rank one. Inspired by the phenomenon, authors proposes an online updating low-rank projections rule to help reduce memory requirements while improving model performance. The paper provides a convergence analysis and demonstrates the effectiveness of AdaRankGrad through experiments on language and biological foundation models.

### Strengths
Strengths

1. Memory Efficiency: AdaRankGrad significantly reduces memory usage during training, which is crucial for large-scale models.

2. Theoretical Foundation: The paper provides a theoretical basis for the method, leveraging the phenomenon of decreasing gradient rank.

### Weaknesses
Weaknesses

1. Experiment Design: The paper's experiments, while informative, may not be entirely convincing. The use of weak benchmarks (GLUE) and the omission of key benchmarks such as MMLU (which focuses on common sense) and GSM8K (which assesses reasoning) limit the evaluation of AdaRankGrad's effectiveness on complex capabilities. Furthermore, the experiments lack a thorough investigation into the sensitivity of the method to different learning rates and batch sizes, which are crucial for the practical application of any optimization technique. The absence of ablation studies on the different components of AdaRankGrad, such as the adaptive rank adjustment mechanism, makes it difficult to assess the contribution of each component to the overall performance gains.


### Questions
Questions

1. Have there been any experiments conducted to assess the impact of this fine-tuning method on the complex capabilities of LLMs, such as MMLU and GSM8k benchmarks?

2. How do you determine the key hyperparameters in AdaRankGrad, such as the information threshold η_{th}? Because the influence of η_{th} seems quite severe to effective rank according to Appendix D. 

3. If I understand correctly, the rank of the gradients may change. How do you ensure that AdaRankGrad can adapt to these changes without frequent manual parameter adjustments?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper introduces AdaRankGrad, a novel method aimed at optimizing memory efficiency and enhancing convergence rates and performance during the training or fine-tuning of large language models (LLMs). It addresses the issue of high memory and computational demands associated with the increasing size of model weights and optimizer states. AdaRankGrad leverages the observed phenomenon that the rank of layer gradients decreases over time, approaching rank one, to dynamically reduce the rank of gradients during Adam optimization. This is achieved through an efficient online-updating low-rank projections rule and a randomized-SVD scheme for identifying the projection matrix. The method supports full-parameter fine-tuning while significantly reducing memory usage compared to existing state-of-the-art methods.

### Strengths
1. The paper provides a theoretical foundation for the observation that the rank of the gradients in LLMs tends to decrease over the course of training, contributing to the understanding of gradient dynamics in deep learning.
2. In contrast to GaLore, which uses fixed time intervals for subspace updating and ignores momentum subspace alignment, the authors propose adaptive subspace selection and momentum subspace transformation, and experimentally illustrate the effectiveness of the two improvements.
3. The authors propose to use SSRF to replace the SVD used in Galore, which speeds up the search for subspaces.

### Weaknesses
1. According to Table 1, the main difference between this paper and Galore is the adaptive subspace dimension and adaptive subspace update. We consider that the existing experiments can illustrate the effectiveness of adaptive subspace updating but cannot illustrate the necessity of adaptive subspace dimension. Therefore, it is recommended that the authors include additional ablation studies focusing on the adaptive dimensionality to substantiate its importance.

2. The method proposed in this paper requires the computation of the subspace in each iteration of the model training, how much time overhead does this operation incur compared to full parameter training and compared to Galore?

### Questions
1. The method proposed in this paper requires the computation of the subspace in each iteration of the model training, how much time overhead does this operation incur compared to full parameter training and compared to Galore?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper studies an adaptive rank selection method for low-rank gradient update. Compared with previous low-rank gradient update methods like Galore, the proposed method involves an adaptively rank-reducing schedule to further reduce training memory. Experimental results and theoretical guarantees provide solid support for the claim in this paper.

### Strengths
The paper provides solid theoretical and numerical analysis for the design of their adaptive rank schedule. The method is effective for reducing the training memory while maintaining the training performance. The writing of the paper is clear.

### Weaknesses
My main concern is about the experiment:
- For the result in Table 2, the results of LoRA tuning seem far worse (2-3%) compared with the standard baselines. For example, the LoRA fine-tuning result for SST2 task should be around 95% based on the results reported in the original LORA paper. This result has also been validated in many other related works. I'm wondering if there exists any difference in the experiment setup that leads to this degradation. Specifically, the learning rate and number of epochs used for fine-tuning LoRA seem inconsistent with established practices, potentially leading to suboptimal performance. The discrepancy raises concerns about the validity of the comparison with the proposed method.
- Training Efficiency: I noticed that the authors mentioned the issue of training time in the paper. However, I found no numerical results showing the difference in training time compared with the LoRA or Galore method. Even though the paper provides an approximation method to calculate the SVD. I assume this adaptive subspace selection process happened every iteration may still slow down the training time significantly. Also, I'm wondering if it's possible to avoid doing this subspace selection each iteration. The lack of concrete timing comparisons makes it difficult to assess the practical benefits of the proposed method in terms of training speed. Furthermore, the overhead of the adaptive rank selection, even with approximations, could negate some of the computational advantages.

### Questions
Based on the previously mentioned weakness, I have the following questions:
- I also observed similar GLUE fine-tuning results in the Galore paper, but I didn't find the reason for the gap compared with the original LoRA paper. I'm wondering if the author could provide a detailed description of their LoRA implementation and experimental setup, including hyperparameters, training procedure, and evaluation method, and compare the accuracy here with the same setup as the original LoRA paper, which is a more widely used setup.
- For training efficiency, I know Galore slows down the training process due to the subspace transform process with a subspace frequency of 200. I'm worried the proposed method may further increase the training time due to the frequent update of subspace. Could you provide the concrete timing comparison between AdaRandGrad, LoRA and Galore for some of the GLUE tasks?
- For the training efficiency, Could you count the wall-clock time for block 1 and block 2 in Algorithm 3, compared with Block 3. I'm wondering about how much additional time is needed for the added parts.
- If possible, could you provide an ablation study showing how different frequencies of subspce selection affect the trade-off between the computational efficiency and performance? Especially, a comparison between the Galore and AdaGradRank with both a 200 subspace frequency is necessary to make the comparison fair. 

I'm happy to further consider my score if the authors could provide a further comparison for the wall-clock time and comparison with Galore under similar subspace frequency.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper presents a theoretical proof that the effective rank of the gradient matrix converges to 1. Building on this, it proposes dynamically reducing the gradient matrix rank as pre-training or fine-tuning progresses, thereby adaptively lowering memory consumption. Recognizing that SVD decomposition is computationally intensive, the paper introduces a novel randomized algorithm to efficiently approximate this decomposition. Table 1 highlights the advantages of the proposed method over LoRA and GaLore across several dimensions. Additionally, this approach is applicable to both pre-training and fine-tuning.

### Strengths
The paper presents a theoretical proof that the effective rank of the gradient matrix converges to 1. Building on this, it proposes dynamically reducing the gradient matrix rank as pre-training or fine-tuning progresses, thereby adaptively lowering memory consumption. Recognizing that SVD decomposition is computationally intensive, the paper introduces a novel randomized algorithm to efficiently approximate this decomposition. Additionally, this approach is applicable to both pre-training and fine-tuning.

### Weaknesses
Overall, this paper could be a significant algorithmic contribution, with the caveat for some clarifications on the theory and experiments. Given these clarifications in an author response, I would be willing to increase the score.

Feedback on specific claims and points for clarification:

1. The memory savings reported in Table 2 may be overstated. Since SSRF runs continuously, the runtime could exceed that of vanilla LoRA or pre-training alone. As a result, while less memory is allocated, it may be held for a longer duration. Memory savings should consider increased runtime since allocating 20% less memory for 20% longer results in only a 4% net saving.

2. It may be challenging to realize the claimed memory savings in practice. Figure 4 shows significant fluctuations in memory savings throughout fine-tuning or pre-training, making it difficult to allocate this saved memory to other concurrent tasks. A smoother, more predictable savings trend would simplify practical implementation.

3. The need for two parameters, $\eta$ and $\epsilon$, to define $(\eta, \epsilon)$-approximation is unclear. Would a single $\eta$ suffice?

### Questions
1. What do the memory savings look like when factoring in the increased running time?
2. Can the savings be fully utilized by other jobs? If so, how?
3. Why is $\epsilon$ needed in defining the $(\eta, \epsilon)$-approximation?

### Soundness
3

### Presentation
3

### Contribution
3

# AUC-CL: A Batchsize-Robust Framework for Self-Supervised Contrastive Representation Learning

- Decision: Accept
- Scores: 6, 5, 6, 6

## Abstract
Self-supervised learning through contrastive representations is an emergent and promising avenue, aiming at alleviating the availability of labeled data. Recent research in the field also demonstrates its viability for several downstream tasks, henceforth leading to works that implement the contrastive principle through innovative loss functions and methods. However, despite achieving impressive progress, most methods depend on prohibitively large batch sizes and compute requirements for good performance. 
In this work, we propose the $\textbf{AUC}$-$\textbf{C}$ontrastive $\textbf{L}$earning, a new approach to contrastive learning that demonstrates robust and competitive performance in compute-limited regimes. 
We propose to incorporate the contrastive objective within the AUC-maximization framework, by noting that the AUC metric is maximized upon enhancing the probability of the network's binary prediction difference between positive and negative samples which inspires adequate embedding space arrangements in representation learning. Unlike standard contrastive methods, when performing stochastic optimization, our method maintains unbiased stochastic gradients and thus is more robust to batchsizes as opposed to standard stochastic optimization problems.
Remarkably, our method with a batch size of 256, outperforms several state-of-the-art methods that may need much larger batch sizes (e.g., 4096), on ImageNet and other standard datasets. Experiments on transfer learning, few-shot learning, and other downstream tasks also demonstrate the viability of our method.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces AUC-CL, a new approach to self-supervised contrastive learning that seeks to mitigate the dependencies on large batch sizes required by many existing contrastive methods. By integrating the contrastive objective within the AUC-maximization framework, the method prioritizes improving the binary prediction differences between positive and negative samples. This unique approach offers unbiased stochastic gradients during optimization, suggesting a higher resilience to batch size variations. Experimental results indicate that the AUC-Contrastive Learning, even with smaller batch sizes like 256, can rival or surpass performances of other methods requiring considerably larger batch sizes.

### Strengths
1. This paper addresses an important issue in contrast learning: model performance is particularly sensitive to batch size, preferring large batch size.

2. The theoretical proof of the design in this paper is very detailed.

### Weaknesses
1. There are non-contrastive learning SSL methods (e.g., SimSiam) that are also less sensitive to batch size. Considering those methods, the novelty of this paper might be a concern.

2. There appears to be a conflict between the experimental results in the table and the figure.

### Questions
1. The contrastive learning methods (e.g., SimCLR and MoCo) are sensitive to batch size and prefer larger batch size. However, there are some self-supervised leanring methods such as SimSiam, which do not have the concept of "positive" and "negative" pairs and are more robust to smaller batch sizes. Considering those methods, the contribution of this paper is diminished.

2. In Table 3, the method proposed in this paper outperforms SimSiam in Cifar-10 dataset, with a 3.1% higher accuracy. However, if we take a look at the Figure 3, the accuracy gap between them is very small, especially in late training stage (after 400 epochs). Could you explain why there appears to be a conflict between these two results?

3. As shown in Figure 3, the accuracy advantage of the proposed method gradually disappear as training proceeds, so it actually just converges faster at early training stage. Moreover, according to the convergence trend in Figure 3, if we train the model for 1,000 epochs for complete convergence as stated in Table 3, the proposed method will not even have an advantage convergence speed.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper introduces AUC-Contrastive Learning as a method to enable self-supervised learning even with a small batch size. This proposed method optimizes the model by making binary predictions on positive and negative samples, aiming to maximize the AUC score. Despite using a significantly smaller batch size, the method shows improved performance over existing contrastive approaches.

### Strengths
- The paper presents a contrastive learning technique based on the AUC score, effectively approximating a deterministic score. Its simplicity makes it easy to implement.

- Unlike conventional contrastive learning-based self-supervised approaches, the proposed method demonstrates strong robustness to batch size variations while also showing performance enhancements.

- Through extensive experiments, such as those involving various architectures, smaller datasets, and few-shot transfer, the paper proves the effectiveness of the method across different settings.

### Weaknesses
- The paper is generally not reader-friendly and lacks clarity. In several sections, terms are not defined or are vaguely explained. Specific issues include:
    - On the second page, the terms B and T are not defined, making comprehension difficult.
    - The introduction should provide a full explanation of AUC.
    - On the third page, the term N is not explained.
    - Figure 1 is distant from its related equation, making it hard to understand terms like A_1,2,3.
    - In Eq. 8, there's a lack of clarity on how 'a' and 'b' are replaced.
    - The algorithm section doesn’t exactly mention which loss function is being optimized.
    - The paper introduces each method name without specifying which previous work it refers to.

- The experimental results appear to be unfair, and several state-of-the-art methods are not reported.
    - In Table 1, many methods didn't use the multi-crop strategy, but the proposed method did. This gives the proposed method an unjust 
 benefit as it would've seen many more images per epoch, leading to potentially improved results.
    - In Table 2, recent methods like DINO are not mentioned at all. DINO reported performance metrics (KNN: 72.8, Linear: 76.1 in 300 epochs) that are higher than the proposed method. The paper's claim that it outperforms several state-of-the-art methods is misleading, and a comprehensive comparison with all state-of-the-art methods is required.

### Questions
There needs to be a clearer explanation regarding how a(w) and b(w) are replaced in Equation 7 and what 'a' and 'b' represent in Equation 8.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes AUC-Contrastive Learning, which incorporates the contrastive objective within the AUC-maximization framework. Since it maintains unbiased stochastic gradients, it is more robust to batch sizes compared to the standard contrastive loss. It empirically shows that the method with a batch size of 256 outperforms or is on par with several state-of-the-art methods using larger batch sizes.

### Strengths
- The method is novel, and theoretically sound. It is great that there is clear link between the AUC-maximization and robustness to batch size.

- The empirical results are promising. The proposed method with a small batch size can outperform or is on par with state-of-the-art methods with large batch size, which is beneficial for the efficiency of computation power.

### Weaknesses
- Some baselines are missing in the experiments. There are other methods for self-supervised representation learning, such as MAE[1] and MAGE[2]. Some of them have better performance than the contrastive learning methods. Although this paper focuses on improving contrastive representation learning, it is still necessary to compare with non-contrastive representation learning methods. 

- Some contrastive learning methods which do not need negative samples, e.g. BYOL and DINO, also shows some robustness to batch size. I think it is necessary to list their performance with smaller batch size (e.g., 256, the same as the proposed method) in Table 1.

- Why does the paper use ViT-S on ImageNet in the experiment? As far as I aware, most of the representation learning methods use ViT-B or ViT-L for ImageNet evaluation. Also, do all methods converge at 400 epochs for ResNet-50 and 300 epochs for ViT-S? If the baseline methods can reach the same performance as the proposed method with longer epochs and larger architecture, then I don't think the paper can claim the outperformance over them.

[1] He et al. Masked Autoencoders Are Scalable Vision Learners. CVPR 2022. 

[2] Li et al. MAGE: MAsked Generative Encoder to Unify Representation Learning and Image Synthesis. CVPR 2023.

### Questions
See Weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes AUC-CL, a new batch-size robust framework for self-supervised contrastive representation learning. At first, the authors point out the limitations of existing NT-Xent objectives (i.e., performance is heavily influenced by batch size). Then, the authors theoretically analyze why SimCLR loss is sensitive to batch size from the gradient perspective. Finally, the author provides the theoretical analysis to demonstrate the convergence guarantee of AUC-CL. Although the relative performance is significant, the absolute accuracy is not competitive. Besides, the reasons why AUC-CL is batch-size robust are not clear, which seems to be an important property.

### Strengths
The paper is well-organized and easy to follow

The experimental results demonstrate the effectiveness of the proposed AUC-CL.

### Weaknesses
1. As stated in the summary, the motivations behind using the AUC framework in combination with contrastive learning, and why this is helpful for batch size robustness, are not clear.

### Questions
As I have reviewed this submission in the other venue, and most of the concerns have been addressed, I have no further questions.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

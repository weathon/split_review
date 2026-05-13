# Privacy-Preserving Personalized Federated Prompt Learning for Multimodal Large Language Models

- Decision: Accept
- Scores: 6, 6, 6, 5

## Abstract
Multimodal Large Language Models (LLMs) are pivotal in revolutionizing customer support and operations by integrating multiple modalities such as text, images, and audio. Federated Prompt Learning (FPL) is a recently proposed approach that combines pre-trained multimodal LLMs such as vision-language models with federated learning to create personalized, privacy-preserving AI systems. However, balancing the competing goals of personalization, generalization, and privacy remains a significant challenge. Over-personalization can lead to overfitting, reducing generalizability, while stringent privacy measures, such as differential privacy, can hinder both personalization and generalization. In this paper, we propose a Differentially Private Federated Prompt Learning (DP-FPL) approach to tackle this challenge by leveraging a low-rank adaptation scheme to capture generalization while maintaining a residual term that preserves expressiveness for personalization. To ensure privacy, we introduce a novel method where we apply local differential privacy to the two low-rank components of the local prompt, and global differential privacy to the global prompt. Our approach mitigates the impact of privacy noise on the model performance while balancing the tradeoff between personalization and generalization. Extensive experiments demonstrate the effectiveness of our approach over other benchmarks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a Differentially Private Federated Prompt Learning (DP-FPL) system for multimodal large language models to address the critical need of balancing the competing goals of personalization, generalization, and privacy-preserving that are involved in serving those models. By decoupling the globally learnable prompt from the personal learnable prompt, decomposing the local prompt with LoRA with an additional residual term, and employing differential privacy techniques in both local prompt learning and global prompt aggregation, DP-FPL achieves accuracy gains while meeting specific privacy budget in a distributed and heterogenous data setting.

### Strengths
The motivation of the paper is well stated, and writing is easily understood. The problem the paper tries to address is certainly important and practical in multimodal LLM deployment. The experiment setting is clear, and results support the claim the authors make.

### Weaknesses
While the problems the paper tries to address are certainly important, the paper does not provide significant scientific insight nor rigorous analysis that can help solve them in broad situations. Instead, a specific set of existing techniques are shown to be effective in a narrow setting (i.e., small-scale datasets and one model architecture). Though the introduction of the residual term in the local prompt decomposition is empirically demonstrated to be effective in the experimental settings, the paper does not give theoretical justification of why such design is beneficial and how applicable it is when applying to more complex situations (e.g., larger data heterogeneity). The privacy analysis also lacks rigorous proof of why the global gradient aggregation satisfies the DP bound.

### Questions
Are there more results on more clients, large datasets, and other models beside ViT-B16? Any theoretical justification of why the residual term preserves the expressiveness of the local prompt?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This article focuses on the issues of balancing personalization, generalization, and privacy in Federated Prompt Learning, and proposes a Differentially Private Federated Prompt Learning method to solve them, and finally proves the effectiveness of the proposed method in three datasets.

### Strengths
1. It is very important and meaningful to consider privacy in Federated Prompt Learning.
2. The proposed method is simple and easy to deploy.
3. Existing methods are discussed and compared in detail.
3. The privacy guarantee of the proposed method is given.

### Weaknesses
1. Although I appreciate the simplicity of the proposed method, compared with existing methods, it seems that only the residuals and differential privacy are added, which are commonly used strategies, making the novelty insufficient.
2. Inadequate experiments. First, the baselines are limited, and it is unclear why a range of baseline methods from related work was not used. Secondly, it is unclear about the privacy-preserving performance of the proposed method, such as its performance in the face of membership inference attacks. Furthermore, no significance tests were performed. Finally, the proposed method has a large number of components, such as global prompt, local prompt, GDP, LDP, etc., all of which require ablation experiments.
3. There are a large number of assertions that have not been confirmed and are all the author's personal conjectures. For example, "simply applying LoRA can result in loss of expressiveness during training, ...", " this approach does not protect the privacy of the prompt data..., Therefore, privacy noise must be incorporated into the gradient updates during each training step for privacy guarantee", "the impact of the GDP noise on the model utility is much smaller compared to LDP".
4. Lack of complexity discussion.
5. Minor: What is $\epsilon$ in Table 4?

### Questions
Please refer to Weaknesses.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper presents a novel approach, Differentially Private Federated Prompt Learning (DP-FPL), which aims to balance privacy, personalization, and generalization in multimodal large language models (LLMs) within federated learning frameworks. DP-FPL utilizes a low-rank adaptation (LoRA) technique with differential privacy (DP) to enable prompt tuning at both global and local levels, allowing clients to personalize prompts without directly sharing sensitive data. This method integrates both local and global differential privacy mechanisms, selectively adding noise to low-rank components to preserve model performance while ensuring data privacy.

### Strengths
- The paper combines local and global differential privacy with federated prompt learning, creating a robust privacy-preserving framework suitable for multimodal LLMs.
- By using low-rank adaptation with a residual component, DP-FPL achieves a balance between generalization for broader applicability and personalization for client-specific data.
- The experimental design demonstrates DP-FPL’s effectiveness across multiple datasets and privacy noise levels, providing evidence of the method’s performance under varying conditions.

### Weaknesses
 - The evaluation lacks statistical tests to confirm the significance of performance differences, which limits the interpretation of the reported improvements.
- The exploration of privacy-performance trade-offs is insufficient under practical, real-world conditions. While the paper discusses differential privacy noise’s impact, it does not fully assess performance under stricter privacy constraints.
- The simulation of data heterogeneity is limited; the paper relies on randomly splitting class labels, which does not capture the complexity of real-world non-IID data distributions effectively.

### Questions
- The model shows a performance trade-off between privacy, personalization, and generalization, yet this is not adequately explored in real-world applications. While the authors apply privacy noise at various levels, the impact on performance for real-world, heterogeneous data remains unclear. An experiment demonstrating this trade-off would strengthen the paper.
- The paper experiments with moderate privacy levels (ϵ=0.1,0.2,0.4), but it does not examine stricter levels (ϵ<0.1ϵ < 0.1ϵ<0.1) that may be necessary for sensitive applications like healthcare or finance. Including results for ϵ=0.05 and ϵ=0.01 would provide a fuller understanding of the model’s robustness under high privacy demands.
- The dataset heterogeneity is simulated by randomly assigning class labels to clients, which does not accurately capture real-world, non-IID data distributions. Employing a Dirichlet distribution to split the dataset would more effectively simulate realistic data diversity, enhancing the model's evaluation under practical federated learning conditions.
- Although the paper notes that DP-FPL degrades gradually as DP noise increases, a clearer breakdown of this effect on both personalization and generalization—specifically for local and neighbor classes—across different datasets would add clarity to the trade-offs involved.
- Privacy noise appears to improve generalization by reducing overfitting; however, Table 2 shows mixed effects across datasets and noise levels. For instance, generalization to neighbor classes improves with increased privacy noise on Caltech101 but is inconsistent on Oxford Flowers. Analyzing this inconsistency could provide insights into the regularization benefits of DP noise.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper introduces a Differentially Private Federated Prompt Learning (DP-FPL) approach to achieve a performance balance between personalization and generalization in FL setting. Specifically, compared to previous work on this subject, DP-FPL adds a residual term to the low-rank decomposition that achieves better balance between privacy and effectiveness.

### Strengths
1. The paper is in general well-written and easy to follow.
2. The effectiveness of proposed framework is testified by comparing with existing works, and improvements are significant.
3. DP theoretical analysis is performed.

### Weaknesses
1. Since the introduction of DP part is quite standard for privacy preservation, the novelty mostly lies in the introduction of the residual term compared to FedPGP.

2. Although the standard theoretical analysis on DP is provided, it didn't address the impact of the introduction of the residual term. The paper will be enhanced significantly if it can provide some theoretical insights on the impact of the residual on the utility-tradeoff, which will support its experimental results.

3. The experimental baselines are a bit limited. Only two methods are compared, while many federated prompt learning methods have been proposed in the past，such as PromptFL,pFedPrompt,FedOTP etc.

### Questions
If I understand correctly, FedPGP in Table 2 in the experiment section applies the original FedPGP with DP, therefore is the same as "without residual" in Table 3. Correct? In other words, are the result difference between FedPGP and DP-FPL in Table 2 due to the residual term only ?

### Soundness
3

### Presentation
3

### Contribution
2

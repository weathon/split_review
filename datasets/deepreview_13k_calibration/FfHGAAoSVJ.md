# AttentionNCE: Contrastive Learning with Instance Attention

- Decision: Reject
- Avg Score: 5.50
- Scores: 6, 5, 6, 5, 6, 5

## Abstract
Contrastive learning has found extensive applications in computer vision, natural language processing, and information retrieval, significantly advancing the frontier of self-supervised learning. However, the limited availability of labels poses challenges in contrastive learning, as the positive and negative samples can be noisy, adversely affecting model training. To address this, we introduce instance-wise attention into the variational lower bound of contrastive loss, and proposing the AttentionNCE loss accordingly. AttentioNCE incorporates two key components that enhance contrastive learning performance: First, it replaces instance-level contrast with attention-based sample prototype contrast, helping to mitigate noise disturbances. Second, it introduces a flexible hard sample mining mechanism, guiding the model to focus on high-quality, informative samples. Theoretically, we demonstrate that optimizing AttentionNCE is equivalent to optimizing the variational lower bound of contrastive loss, offering a worst-case guarantee for maximum likelihood estimation under noisy conditions. Empirically, we apply AttentionNCE to popular contrastive learning frameworks and validate its effectiveness. The code is released at: 
\url{https://anonymous.4open.science/r/AttentioNCE-55EB}

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces AttentionNCE, a contrastive learning method that incorporates attention mechanisms to generate sample prototypes, improving robustness in noisy environments. The proposed approach leverages variational lower bound optimization for contrastive loss, aiming to provide a theoretical guarantee under worst-case noisy conditions. Key innovations include flexible hard sample mining and multi-view integration through attention, enabling the model to focus on high-quality representations and challenging samples near decision boundaries. Experimental results demonstrate its effectiveness in specific scenarios.

### Strengths
1.	The paper presents an innovative integration of attention mechanisms into contrastive learning, which enhances the robustness of the model, especially in noisy environments. This approach allows the model to focus on high-quality sample representations.
2.	By optimizing the contrastive loss through a variational lower bound, the paper theoretically provides a worst-case guarantee under noisy conditions, which adds a solid theoretical foundation to the proposed AttentionNCE loss.
3.	The flexible hard sample mining mechanism helps the model to better handle samples near the decision boundary, improving the model’s accuracy in distinguishing challenging positive and negative samples.

### Weaknesses
1.	The novelty of the paper is limited, as the core methods are primarily based on a combination and refinement of existing techniques, such as attention-based prototypes, hard sample mining, and multi-view contrastive learning. The integration, while potentially effective, does not introduce a fundamentally new concept in contrastive learning, but rather combines known components. The specific way these components are combined and the extent of their synergistic effect need to be more thoroughly justified and analyzed.
2.	The generalization of the performance improvement remains to be verified, as the baselines used for comparison are from 2020, which may not represent the current state-of-the-art. The lack of comparison with more recent methods makes it difficult to assess the true advancement offered by AttentionNCE. The reported improvements might be less significant when compared against more contemporary contrastive learning techniques that have emerged since 2020.
3.	The paper lacks experiments specifically analyzing computational overhead, leaving the impact of these additional costs on real-world scalability unaddressed. The introduction of attention mechanisms and the encoding of multiple positive samples inherently increase computational complexity. Without a detailed analysis of runtime, memory usage, and GPU consumption, it's hard to determine the practical feasibility of the method, especially for large-scale datasets and real-time applications.

### Questions
•  Given that the baselines used for performance comparison are from 2020, how does the proposed method perform against more recent state-of-the-art contrastive learning approaches? Would it be possible to include comparisons with newer baselines to better validate the effectiveness of AttentionNCE?
•  The proposed approach introduces additional computational complexity due to encoding multiple positive samples and applying attention mechanisms. Have you considered conducting a computational overhead analysis? Could you provide empirical results on runtime or memory usage to demonstrate the scalability of AttentionNCE in large-scale applications?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper focused on the problem of noisy positive/negative pairs in contrastive learning, which stems from the use of strong data distortion to generate positive/negative samples during training. To mitigate this, the authors introduced AttentionNCE, a prototype-like scheme, that essentially re-weight the contribution of each positive/negative pair when computing the contrastive loss. The author claimed that this is equivalent to optimizing the variation lowering boud of standard InfoNCE loss, offering a worst-case guarantee under noisy conditions. Experiments on several small-scale datasets showed the efficacy of the AttentionNCE.

### Strengths
1. The problem of noisy positive and negative pairs is one of the important problems that affect the performance of contrastive learning methods. 

2. The proposed AttentionNCE is well-grounded theoretically from the variational lower bound aspect as well as intuitive in the sense of modulating the importance of each positive and negative pair.

3. Experiments on several small-scale datasets exhibited promising results compared to the baselines without considering the noisy conditions in contrastive learning.

### Weaknesses
1. The paper adopted different formulations for the attention of positive samples and negative samples. However, from my understanding, these two attentions could actually be unified into the same equation because they both performed re-weighting on the features, and the only difference is aggregation or not. I wonder why the authors emphasize the prototype with positive attention.

2. The idea of down-weighting the hard positive and up-weighting the hard negative relies on the premise that the anchor itself is not noisy. This, however, may not always be true in contrastive learning due to the large-scale distortion when crafting multiple views. In case the anchor is noisy, AttentionNCE might inappropriately do exactly the opposite of what it is expected to do. I wonder if the authors have any consideration for this problem.

3. It is unclear whether the comparison of AttentionNCE to Simclr/MoCo or other methods is fair since AttentionNCE uses 4 positive pairs by default while SimCLR uses two. How would this also affect the performance of the baseline?

4. The proposed method is exclusively evaluated by in-distribution dataset/task, i.e., the linear evaluation of the training datasets. I would further strengthen the paper if the authors could include more evaluations on transfer learning to other datasets (as in CMC) and other tasks (such as object detection).

### Questions
Table 5 of the Appendix suggests that AttentionNCE uses 4 positive pairs and a batch size of 256 for training by default, but the number of negative samples there is only 510 (256 x 2 - 2), not 1020 (256 x 4 - 4). Is this a typo or are there any details on the construction of positive and negative pairs missed in the paper?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
the paper introduces a new contrastive learning method called attention-nce, designed to address challenges with noisy samples in self-supervised learning. contrastive learning usually suffers from false positive and false negative samples due to noise, impacting representation learning. attention-nce integrates an instance-wise attention mechanism with a sample prototype approach. it introduces two main ideas: using prototypes of samples (instead of instance-level contrasts) to improve robustness to noise, and incorporating a flexible hard sample mining mechanism that focuses on high-quality samples. experiments across datasets like cifar-10, cifar-100, and tiny-imagenet demonstrate that attention-nce outperforms conventional contrastive loss.

### Strengths
S1 By using attention-based prototypes, attention-nce tackles the issue of noisy samples, a persistent challenge in contrastive learning. this approach is particularly beneficial for scenarios where labels are noisy or absent, as it helps maintain the semantic structure of the learned representations.


S2 The hard sample mining strategy, which focuses on both hard positive and hard negative samples, is flexible and well-explained. it shows practical improvements, especially in complex datasets where hard samples define clearer decision boundaries.


S3 Generally, the paper is well-written.

### Weaknesses
W1 While attention-nce introduces parameters like the scaling factors for positive and negative samples (dpos and dneg), there is minimal guidance on how to select these values based on dataset characteristics. for instance, in cifar-10 and cifar-100, different dneg values yield varying results, but the paper doesn’t provide specific criteria for choosing these values in practice. To enhance practical usability, it would be beneficial if the authors could provide guidelines or heuristics for selecting dpos and dneg based on dataset attributes. For example, are there any rules of thumb related to dataset size, number of classes, or expected noise levels that could guide parameter selection? The lack of a principled approach to setting these hyperparameters significantly limits the practical applicability of the method, as users are left to rely on ad-hoc tuning, which can be computationally expensive and may not lead to optimal performance. The paper should include a more detailed analysis of how these parameters interact with different dataset properties, such as the number of classes, the degree of intra-class variability, and the presence of label noise. Without such guidance, the method's effectiveness is highly dependent on the user's expertise and computational resources.

W2 The stability of the prototype features under different noise levels isn't explored. Since Attention-NCE relies on sample prototypes to mitigate noise, understanding how noise affects prototype stability could provide insights for better handling extreme noise conditions. It would strengthen the paper if the authors could perform specific experiments or analyses that evaluate prototype stability across a range of artificially introduced noise levels. This could clarify the method's robustness and offer guidance on handling extreme noise situations. Specifically, the paper lacks an analysis of how the quality of the prototypes degrades as the noise level increases, and whether the attention mechanism is still effective in such scenarios. It would be beneficial to investigate the sensitivity of the learned prototypes to different types of noise, such as random label flips, or adversarial perturbations, and to quantify the impact of these perturbations on the final performance. The paper should also explore whether there are any strategies to improve the robustness of the prototypes in high-noise environments, such as using more robust aggregation methods or incorporating noise-aware training techniques.

### Questions
Q1 how should users determine the best dpos and dneg values when working with different datasets? would a heuristic or automated method help to simplify this parameter tuning?

Q2 how does attention-nce handle cases of extremely high noise, where a large portion of both positive and negative samples might be incorrectly labeled? do the prototypes remain effective under such conditions, or does their quality degrade? Could the authors test Attention-NCE on datasets with varying levels of artificially introduced label noise (e.g., 20%, 40%, 60% incorrect labels) and compare its performance to baseline methods under these conditions? This would provide insights into its resilience in high-noise environments.

Q3: In MoCo v3, the main point of the paper is the use of ViT instead of traditional CNN architectures (otherwise, it would be MoCo v2). Could the authors clarify why they use ResNet-50 in Table 2 for MoCo v3?

### Soundness
3

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
5

### Summary
This paper introduces AttentionNCE, a new loss function for contrastive learning that addresses issues with noisy positive and negative samples. By integrating instancewise attention into the variational lower bound of contrastive loss, AttentionNCE improves performance through sample prototype contrast to reduce noise and a flexible hard sample mining mechanism that prioritizes high-quality samples.

### Strengths
The paper introduces the AttentionNCE contrastive loss, proving its equivalence to the variational lower bound of the original contrastive loss, which ensures reliable maximum likelihood estimation under noisy conditions. By incorporating attention-based sample prototype contrast, it effectively mitigates noise perturbations. Additionally, the flexible hard-sample-mining mechanism directs the model to focus on high-quality samples, enhancing learning outcomes.

### Weaknesses
1.The paper initially addresses the issue of noisy labels, yet it would benefit from further elaboration on the potential integration of the proposed approach with supervised contrastive learning algorithms like SupCon. Specifically, it would be valuable to demonstrate the performance of the proposed algorithm under varying proportions of symmetric and asymmetric label noise. The current analysis does not sufficiently explore how the attention mechanism interacts with different types of label noise, which is crucial for understanding its robustness in real-world scenarios. For instance, the paper should investigate how the attention weights are affected when the noise is concentrated in specific classes or when there are systematic biases in the noise patterns, as these scenarios can significantly impact the effectiveness of the proposed method.

2.While the paper primarily compares the proposed algorithm to traditional contrastive learning methods and includes a comparison with RINCE, which is fundamentally designed to address label noise, a comparison with existing advanced hard negative mining algorithms would provide a more compelling evaluation of the algorithm's effectiveness. The current comparisons do not fully establish the superiority of the proposed method over state-of-the-art techniques in hard negative mining. A more thorough evaluation should include a wider range of hard negative mining strategies, such as those that dynamically adjust the mining difficulty or incorporate curriculum learning techniques. This would provide a more comprehensive understanding of the advantages and limitations of the proposed approach.

3.The introduction of the attention mechanism in the proposed algorithm raises questions about computational efficiency. It is essential to visualize and quantify how much additional computation time is required compared to the original algorithms, as this information is crucial for practical implementation considerations. The paper lacks a detailed analysis of the computational overhead introduced by the attention mechanism. It is important to quantify not only the increase in training time but also the memory footprint and the impact on inference speed. This analysis should include a breakdown of the computational costs associated with different components of the attention mechanism, such as the attention weight calculation and the aggregation of features, to provide a clear understanding of the trade-offs between performance and computational resources.

### Questions
Please see the weakness.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a novel contrastive loss dubbed AttentionNCE. The authors consider adopting an attention mechanism to explore hard augmented samples, aiming to mitigate the negative influence from these samples. This approach is somewhat similar to [1] and [2], as both aim to figure out a more appropriate contrastive object compared to instance augmentation. The corresponding experimental results demonstrate that the introduced attention mechanism can bring a remarkable improvement to the original SimCLR across various datasets.

[1] Li, J., Zhou, P., Xiong, C., & Hoi, S. C. H. (2021). Prototypical Contrastive Learning of Unsupervised Representations. In International Conference on Learning Representations (ICLR).

[2]Caron, Mathilde, et al. "Unsupervised learning of visual features by contrasting cluster assignments." Advances in neural information processing systems 33 (2020): 9912-9924.

### Strengths
Strengths
- The idea of adding an attention mechanism to recognize hard samples is concise and intuitive.
- The experiments are comprehensive and strong enough to support the efficiency of the proposed idea. They demonstrate that the attention mechanism can introduce significant improvements across various datasets.
- The authors conducted an elaborate ablation study for the newly introduced parameters, which increases the completeness of this paper.
- Similar as [1], the authors present AttentionNCE can be regarded as the lower bound of MLE according to the measure classifying a positive sample from a set of $N$ negative samples using the ELOB-KL divergence decomposition framework.

[1] Li, J., Zhou, P., Xiong, C., & Hoi, S. C. H. (2021). Prototypical Contrastive Learning of Unsupervised Representations. In International Conference on Learning Representations (ICLR).

### Weaknesses
Weaknesses
- I suggest that authors reorganize the structure of the article, as they advance the derivation of the ELOB divergence to equation (14), which creates significant obstacles in grasping the core idea of the article. Specifically, the placement of the ELOB-KL divergence decomposition so early in the paper disrupts the flow and makes it difficult to follow the logical progression from the introduction of AttentionNCE to its theoretical underpinnings. While equations (6)–(10) and (14) provide a sufficient explanation of the main ideas, the detailed derivation could be positioned later to improve readability. A more intuitive introduction to the core concepts before delving into the mathematical intricacies would enhance the overall clarity of the paper.
- The notation used in equation (1) is pretty confusing. The meaning of left hand side of (1) is "The probability of classifying a positive sample from a set of $N$ negative samples", denoted as $P(X \vert \theta)$. But the authors claim that $X$ is used to indicate a set of samples $\{x^+,x_1^-, \cdots, x_N^-\}$, this inconsistency makes it awkward to read this part. Specifically, the notation $P(X \vert \theta)$ suggests a probability distribution over the set of samples $X$, while the intention seems to be to represent the probability of correctly identifying the positive sample. This could be clarified by introducing a distinct notation for the event of correct classification.
- Actually, the theoretical part of this paper is not solid enough, as the authors do not sufficiently bridge the gap between downstream classification error and the likelihood they employed, Therefore, the implications of maximizing $\mathcal{L}_{\text{AttentionNCE}}$ require further investigation. But this is ok as the practice contribution of this paper is outstanding, provided that the theoretical part does not obscure the main ideas. Meanwhile there is not any evidence to support the final attention can help us figure out relatively hard augmented samples. While the authors propose that the attention mechanism can identify and down-weight hard augmented samples, there is a lack of empirical or theoretical evidence to support this claim. Demonstrating a correlation between attention scores and the difficulty of augmented samples would strengthen the paper's core argument.
- There are some typos, first, in the third line of equation (3), deleting $d\textbf{h}$ is correct expression. Second, in the phrase "It is also important to note that when $q(\textbf{h}) = P (h|X, θ)$", $h$ should be bold.

### Questions
Questions
- Can you identify some hard augmented instances and calculate their attention scores through the pretrained model to support your standpoint? Specifically, can you demonstrate that introducing the attention mechanism can help us identify relatively hard augmented samples, aligning with your intuition?

Summary Of The Review
- This paper proposes a novel contrastive loss called AttentionNCE, which has a concise and intuitive idea. The authors conduct comprehensive and elaborate experiments to demonstrate the effectiveness of their approach. However, the writing style and mathematics explanation are not hit the nail on the head, hindering readers’ understanding of the core concept. The authors claim that the attention mechanism can identify hard samples and assign them relatively smaller attention scores, but they do not provide any evidence from either practical or theoretical perspectives. Overall, the paper has its pros and cons, and I am on the boundary, which results in a score of 5.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 6

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper focuses on improving the classical contrastive loss by introducing an attentional mechanism to focus on False positive and Hard Negative. The method is validated on a number of datasets.

### Strengths
The proposed idea is generally easy to understand.

### Weaknesses
The reviewer is uncertain whether the performance improvement mainly stems from avoiding false positive samples or mining hard negative samples. As a simple example, when there are different pictures of dogs in the dataset, for dog A, the reviewer agrees that Equations 7 and 8 may help alleviate false positives—given the right hyperparameters (e.g., a crop including only the image background after strong augmentation should not be considered a positive sample). However, Equations 9 and 10 may result in other dog images being pushed further away (these samples should not be regarded as hard negative samples but as positive samples), which would negatively impact the learned features. In theory, we can never really know where the optimal threshold is.

Overall, the reviewer considers the contribution of this paper to be marginal and are unsure whether the paper was correctly motivated. Though phrased as 'attention', the proposed method of manipulating contrastive loss addresses a longstanding problem, often referred to as 'false negative'/'class collision' cancellation.

Moreover,

1. Important related works are missing. I would recommend the authors review the following:
- "A Theoretical Analysis of Contrastive Unsupervised Representation Learning"
- "CO2: Consistent Contrast for Unsupervised Visual Representation Learning"
- "Adaptive Soft Contrastive Learning"
- "Weakly Supervised Contrastive Learning"
- "Similarity Contrastive Estimation for Self-Supervised Soft Contrastive Learning"
- "Mutual Contrastive Learning for Visual Representation Learning"
- "CompRess: Self-Supervised Learning by Compressing Representations"
- "SEED: Self-Supervised Distillation for Visual Representation"
2. Section 3.1, which reintroduces contrastive loss, can be simplified or removed as which is widely-acknowledge already.
3. The theoretical proof in Section 3.4 does not support the proposed attention mechanism but applies to any applicable contrastive loss by simply changing the inter-sample relations in Equation 12.

### Questions
See weakness.

### Soundness
2

### Presentation
2

### Contribution
1

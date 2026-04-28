# Object-aware Conditional Alignment for Cross-domain Counting

- Decision: Reject
- Avg Score: 4.40
- Scores: 3, 5, 6, 3, 5

## Abstract
Object counting is an important task in computer vision with many real-world applications. In practical settings, factors such as lighting conditions and object density can vary dramatically, leading to distribution shifts then causing inaccurate counting. We found that existing domain adaptation (DA) methods cannot be directly applied to the counting task, as they usually assume changes across different domains are task-irrelevant and focus on utilizing domain-invariant features for prediction. However, in object counting tasks, changes in object density which could happen across domains are task-relevant and cannot be ignored. Therefore, applying existing DA methods to the counting task can ignore the information about density changes, resulting in unreliable counting. To address this limitation, we propose the Binary Alignment Network (BiAN). Unlike traditional DA methods that align distributions of entire image representations, BiAN segments objects of interest and aligns the distributions of the object-specific features across domains. This targeted alignment allows us to disregard irrelevant features, such as lighting conditions, while preserving essential information about changes in object density. We theoretically demonstrate that BiAN achieves superior adaptability in counting tasks by introducing conditional alignment—aligning features conditioned on the presence of objects. Extensive experiments on two distinct counting tasks and eight dataset combinations show that BiAN outperforms state-of-the-art methods.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes the Binary Alignment Network (BiAN), addressing the shortcomings of existing domain adaptation methods in object counting. The authors emphasize that traditional approaches often overlook task-relevant factors like object density variations, critical for accurate counting. The paper provides a robust theoretical foundation for BiAN and conducts extensive experiments demonstrating its effectiveness across multiple datasets and counting scenarios.

### Strengths
1. In response to the limitations of existing methods, BiAN is specifically designed for object counting tasks. The introduction of conditional alignment and conditional consistency mechanisms effectively addresses task-related factors such as object density changes, leading to improved counting accuracy.
2. The authors offer a detailed theoretical analysis, proving that BiAN achieves a lower bound on joint decision error. This analysis illustrates how conditional alignment contributes to error reduction, thereby providing strong theoretical support for the method’s effectiveness.
3. The authors achieved significant performance improvements.

### Weaknesses
 - The core idea of the paper is to alleviate the domain shift caused by the change of object density from the source domain to the target domain. Therefore, it will be easier to understand the effectiveness of the method through some analysis that demonstrates the gain from the proposed method w.r.t. the extent of the density change? Additionally, how do we metric the extent of the density change?
- It’s unclear how segmentation is achieved in the BiAN framework. For instance, is a pre-trained model used for segmentation, or is this achieved through training within the framework? The lack of detail makes it difficult to assess the complexity and potential limitations of the segmentation component. Specifically, what is the architecture of the segmentation network and how is it trained? What loss function is used to optimize the segmentation? How does the segmentation performance affect the overall counting performance?
- L372-373: The phrase "As to the evaluation metrics, we follow the previous works' setting" is followed by a similar statement: "Following the previous research works."
The wrong best value indicated in Table 1: the SD→SR MAE and SN→FH MSE.
- Missing necessary symbols in the figures. e.g., in Fig.1, the purple feature refers to the source domain, while the green feature refers to the target domain. Still, there are no explicit symbols or texts to indicate them, resulting the difficulty in understanding the figure. This lack of clarity extends to other figures as well, where the meaning of different colors and symbols is not immediately obvious, hindering the reader's ability to grasp the proposed method's details.
- In Section 2.2, it would be better if there were 1 or 2 sentences that state the relationship/difference between the proposed method and prior works. This would help contextualize the novelty of the proposed approach and highlight its specific contributions relative to existing domain adaptation techniques for counting tasks.

### Questions
see weaknesses

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper proposes a method to address task-relevant changes in different domains, rather than only focusing on domain-invariant features. Experimental results demonstrate the outstanding DA capability of the proposed BiAN.

### Strengths
This paper addresses domain adaptation in crowd counting by focusing on task-relevant changes in different domains, which is novel when compared with the previous methods only addressing domain-invariant features.

### Weaknesses
- The description is not easy to understand since many signs are unclear.
- There is no description of the training pipeline. The loss functions are also not explained clearly.
- The results are even better than these fully supervised counting methods, which does not make sense for a DA method.

### Questions
- The description in Sec. 3.2 and Sec. 3.3 is really confusing. Many symbols are not well defined and explained when they first appear in the paper.
- An overall training process should be described at the beginning of the method section.
- What is the meaning of $G$ in $g \in G$ of Eq. (1)? How is it implemented during training?
- In line 181, is the subscript correct to denote $z_{\text{inv}}$ and $z_{\text{var}}$ as the domain-invariant and domain-variant features?
- In line 234, why can $f_c \in F$ share weights with $F$? Since $f_c$ is an element of $F$, how does it share weights? What does $F$ mean, and what are its weights?
- In line 206, $x$ is segmented into partitions $x_i$, and then divided into conditional subsets $x_{ij}^c$. In line 208, $x_i = \cup_{j=1}^k x_{ij}^c$. This part is confusing. What is the relationship between $x_{ij}$ and $x_i$? Is there any plot demonstrating the relationship between them? What is the meaning of $j$ here?
- What are $\hat{c}_s$, $\hat{c}_s^f$, and $\hat{c}_s^b$ in Eq. (6)? $\hat{c}$ is not mentioned in any part except Eq. (6).
- What is the condition set $\mathcal{C}$? Is there any description explaining its meaning?
- Are there any results on adaptation from Shanghai Tech Part A/B to UCF-QNRF?
- The results presented in Table 5 are confusing. Do you use labels in the test set of the UCF-QNRF dataset? It does not make sense to obtain a DA model achieving much better results than a model fully supervised with real data (STEERER). Similar results are also observed in Table 2. BiAN's MAE (42.3) is much better than the current SOTA (STEERER: 54.5 or PET: 49.34). Implementation details should be provided for reference.

### Soundness
2

### Presentation
1

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper introduces the Binary Alignment Network (BiAN), a novel approach for domain adaptation (DA) in object counting tasks. Traditional DA methods are ineffective in this context because they treat the distribution of object density as task-irrelevant, aiming to align domain-invariant features across domains without addressing density variations critical to counting accuracy. In contrast, BiAN segments images to isolate object-specific features, disregarding background elements. This targeted approach allows BiAN to preserve essential density-related information across domains, leading to more reliable cross-domain counting performance. The authors further provide a theoretical analysis and extensive experiments to validate BiAN’s effectiveness.

### Strengths
- The paper introduces a novel idea with strong insight, addressing a gap in domain adaptation for counting tasks.
- The focus on density variations and object-specific feature alignment represents a meaningful shift from traditional DA approaches that overlook these task-relevant factors.
- The experimental results are thorough, including multiple datasets and settings, which highlight the adaptability of BiAN across various scenarios.

### Weaknesses
- The core idea of the paper is to alleviate the domain shift caused by the change of object density from the source domain to the target domain. Therefore, it will be easier to understand the effectiveness of the method through some analysis that demonstrates the gain from the proposed method w.r.t. the extent of the density change? Additionally, how do we metric the extent of the density change?
- It’s unclear how segmentation is achieved in the BiAN framework. For instance, is a pre-trained model used for segmentation, or is this achieved through training within the framework?
- L372-373: The phrase "As to the evaluation metrics, we follow the previous works' setting" is followed by a similar statement: "Following the previous research works."
The wrong best value indicated in Table 1: the SD→SR MAE and SN→FH MSE.
- Missing necessary symbols in the figures. e.g., in Fig.1, the purple feature refers to the source domain, while the green feature refers to the target domain. Still, there are no explicit symbols or texts to indicate them, resulting the difficulty in understanding the figure.
- In Section 2.2, it would be better if there were 1 or 2 sentences that state the relationship/difference between the proposed method and prior works.

### Questions
Please see the weakness.

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper introduces the Binary Alignment Network (BiAN) to address domain shift while preserving task-relevant information. The conditional alignment mechanism helps the network align object feature distributions across domains while maintaining inter-object contextual consistency. The Condition-Consistent Mechanism (CM) refines the segment map.

### Strengths
1. The performance of the proposed method is better than the comparsion method.

### Weaknesses
1. The proposed method lacks novelty, as it simply splits the image into background and foreground before processing them separately.
2. In Table 1, the best MAE for SD→SR is not achieved by the proposed method, yet it is marked in bold. This should be corrected.
3. In Table 1, the best performance for SN→FH is also incorrectly highlighted, and the proposed method performs worse than other methods by a large margin. The authors should explain this discrepancy.
4. The experimental results are unreliable, especially in Table 1, where the MSE is significantly smaller than the MAE, which raises concerns about their validity.

### Questions
1. In Table 1 (SD→SR), why does the proposed method achieve a lower MSE than MAE, which is inconsistent with all other experiments?
2. The method relies on a regressor F for segmenting the object and background. What specific method is being used, and how is this model trained?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes a Binary Alignment Network (BiAN) designed to address the specific challenges associated with variations in object density across domains in counting tasks. The key idea of this approach is to align the distribution of object-specific features across different domains while preserving essential information regarding changes in object density, based on the segmentation of interested objects. Extensive experiments demonstrate the effectiveness of the proposed method.

### Strengths
- The proposed method shows strong performance on multiple benchmark.
 - This paper provides a theoretical demonstration of how conditional alignment enhances domain adaptability in counting tasks.

### Weaknesses
- The paper uses a smaller margin to fit in the page limit.
- The use of symbols is somewhat confusing, which makes it hard to understand. such as

  (1) This paper usies the same symbols F to represent the regressor, feature extractor, and the obtained features in lines 196 to 200.

  (2) The difference between g and F in lines 199 to 200 , which are used to extract features.

- Issues related to Eq. 6 and 7.

  (1) I suggest providing some explanations for why the counting loss needs to be divided by the alignment loss using the reversed NLL.

  (2) Why are the provided labels for the last two items in the denominator of Eq. 6 zero, while they are y_t^d in Eq. 7?

- Object-aware conditional alignment is a common approach in domain adaptation tasks, as seen in [1], [2], and [3]. Additionally, the segmentation of interested objects is accomplished using labels y_i, similar to [1] and [2]. Therefore, the innovation of this paper appears to be somewhat limited.

    [1] Decoupled adaptation for cross-domain object detection

    [2]  Undoing the Damage of Label Shift for Cross-domain Semantic Segmentation

    [3] Robust Domain Adaptive Object Detection with Unified Multi-Granularity Alignment

- The ablation experiments are not sufficiently detailed.  I suggest comparing the results of conditional alignment and style alignment, as shown in Fig. 1, to evaluate the effectiveness and necessity of conditional alignment.

### Questions
- The paper uses a smaller margin to fit in the page limit, which could result in a desk rejection.
- See the weakness part.

### Soundness
2

### Presentation
2

### Contribution
2

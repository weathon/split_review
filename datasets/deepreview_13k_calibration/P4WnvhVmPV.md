# A Unified Theoretical Framework for Understanding Difficult-to-learn Examples in Contrastive Learning

- Decision: Reject
- Avg Score: 5.00
- Scores: 3, 6, 6, 5

## Abstract
Unsupervised contrastive learning has shown significant performance improvements in recent years, often approaching or even rivaling supervised learning in various tasks. However, its learning mechanism is fundamentally different from that of supervised learning. Previous works have shown that difficult-to-learn examples (well-recognized in supervised learning as examples around the decision boundary), which are essential in supervised learning, contribute minimally in unsupervised settings. In this paper, perhaps surprisingly, we find that the direct removal of difficult-to-learn examples, although reduces the sample size, can boost the downstream classification performance of contrastive learning. To uncover the reasons behind this, we develop a theoretical framework modeling the similarity between different pairs of samples. Guided by this theoretical framework, we conduct a thorough theoretical analysis revealing that the presence of difficult-to-learn examples negatively affects the generalization of contrastive learning. Furthermore, we demonstrate that the removal of these examples, and techniques such as margin tuning and temperature scaling can enhance its generalization bounds, thereby improving performance.
Empirically, we propose a simple and efficient mechanism for selecting difficult-to-learn examples and validate the effectiveness of the aforementioned methods, which substantiates the reliability of our proposed theoretical framework.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper proposes a theoretical framework for understanding difficulty-to-learn examples in contrastive learning. This further suggests a heuristic approach to determine difficulty-to-learn examples, removes them, do margin tuning, and perform temperature scaling to improve performance.

### Strengths
- The idea of determining difficulty-to-learn examples is intuitive and interesting.

### Weaknesses
 - The terminology difficulty-to-learn examples seems to be confusing because indeed, the paper focuses on difficulty-to-learn pairs (different classes and stay closely to the boundary).
- The definitions of difficulty-to-learn or easy-to-learn pairs are not rigorous. 
- In the theory development in Theorems 3.1, 3.2, and so on, it is unclear how to train the feature extractor f for obtaining feature vectors. If it is learned using Eq. (1) similar to HaoChen et al., it is unclear how $\alpha, \beta, \gamma$ are relevant.
- The difficult-to-learn example selection is very heuristic and connects losingly to the theory development.
- The paper seems to be a combination of HaoChen et al. and Zhou et al.
- The experiments are humble and the paper does not have strong practical implication.
- Although in the main paper, we do not mention explicitly how you use the adjacency matrix in Figure 3d. However, when I check your proof for Theorems 3.1 and 3.2, in Eq. (22) and Eq. (23), you use the discretized adjacency matrix $A$ in Figure 3d for solving $|\bar{A}-FF^{T}||_{F}^{2}$ where $\bar{A}$ is the normalized matrix of $A$. This is more evident for this use because in Line 1035 to 1039, you obtain very specific eigenvalues and eigenvectors for A which is impossible for a general similarity matrix A. This means that to develop theories, you use the discretized adjacency matrix in Figure 3d which does not convince me.  Similar observation for other theorems and corollaries.

### Questions
Please address my questions in Weaknesses.

### Soundness
2

### Presentation
2

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
In this paper, the authors carefully investigated the effect of difficult-to-learn examples in unsupervised contrastive learning.
A preliminary experiment is conducted to demonstrate the negative effect of such examples, while in supervised learning it is well known that such difficult-to-learn example has positive effects.

Inspired by this preliminary experiment, the authors established a theoretical result, characterizing the effects of difficult-to-learn examples using linear probing error bounds. Their result clearly illustrated the effect of the persistence of such examples in the training set.

Further, the authors analyzed several methods for removing/neglecting the effect of difficult-to-learn examples within the established theoretical frameworks. Finally, several experiments are conducted to validate the theories, while a combined method utilizing the aforementioned methods is proposed to better handle the effect of difficult-to-learn examples.

### Strengths
- This work provided a simplified theoretical framework (i.e., to my understanding, the simplified augmentation similarity graph as illustrated in Figure 3: a graph with all entries in its adjacency matrix being one of $1$, $\alpha$, $\beta$ or $\gamma$), which allows easier (tractable) analysis with the spectral contrastive loss.
- Based on the established framework, this work further provides valuable analysis for Margin Tuning and Temperature Scaling. It provides a clear explanation of why and how those methods work for unsupervised contrastive learning.

### Weaknesses
## Theories
Despite the clarity of the established framework, its connection to real-world scenarios is weak. In the paper, the idealized adjacency matrix $A$ only has 4 possible entries: $1$, $\alpha$, $\beta$, or $\gamma$, used through out the entire paper (esp. Section 3 & 4). Where in real-world scenarios, the adjacency entries can be quite arbitrary and continuous.

The simplification is made such that the direct computation of eigenvalues of $A$ is possible, yet I feel that there lacks an intuitive, or preferably, empirical justification for the connection between the idealized theoretical framework and the practical case. The only direct explanation I could find is around Sec 3.2, "As difficult-to-learn examples lie around the decision boundary, they should have higher augmentation similarity to examples from different classes." (lines 164-166), which is a rather ambiguous intuition or belief. I'd be glad if the authors could emphasize corresponding parts that I might have overlooked.

For example, this work may potentially be improved via:
- A relaxation on the ideal adjacency matrix, e.g., allowing entries to take values such as $(\alpha - \epsilon, \alpha + \epsilon) \dots$ ; or being stochastic with some distribution.
- A visualization and/or quantitative assessment of the argumentation similarity graph in small-scale datasets (perhaps not feasible, though)

After all, I think it is important to answer questions like 1) To what extent do $\beta$ and $\gamma$ differ in real-world datasets (under this work's intuitive assumption)? 2) In what kind of dataset $\beta$ and $\gamma$ are further separated, compared to other datasets?, etc.

Nevertheless, this simplified viewpoint presented in this work still provides clear and intuitive results that are valuable for future research (besides the questions I listed below), and generalization or empirical validation might be difficult. Therefore, the points above are more suggestions rather than must-do's.

## Experiments
The experimental descriptions are a bit blurry in this work, and I think it should be written clearly. For example, the generating process of $\gamma$-Mixed CIFAR-10 is missing, where the authors only claim that it is "mixing at pixel level" (lines 106-107). Please refer to the Questions section for more details.

Furthermore, in results like Table 1, it is perhaps beneficial to show more statistics beyond classification accuracy, e.g., the number of removed datapoints (overall and in each class), etc.

### Questions
## Theories

- The inequality around line 212, $\frac{(1-\alpha)+r(\gamma-\beta)}{(1-\alpha)+n \alpha+n r \beta+n_d r(\gamma-\beta)} > \frac{1-\alpha}{(1-\alpha)+n \alpha+n r \beta}$: When does this hold? Is it practical for it to hold in most datasets?
- In line 1019, "when $n_d < k \leq n_d + r + 1$" - This seems rather a strict condition, are there further explanations on this? (or perhaps it is explained but I have overlooked?).

## Experiments

- What is the "pixel-mixing" method in Section 2 line 107?
- In line 344-345, what features are being used? Is the network being pre-trained on some dataset before the unsupervised contrastive learning process?
- In Figure4 & 5, what are the other hyper-parameters when tuning the plotted parameter?
- Is Section A.4 talking about the combined method?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The manuscript identifies a universal empirical phenomenon: removing certain training examples improves the performance of unsupervised contrastive learning. The theoretical results further show that difficult-to-learn samples can negatively impact contrastive learning performance and propose several potential solutions to address this by enhancing generalization bounds in spectral contrastive learning. Experimental results support these findings, providing empirical validation for the proposed approach.

### Strengths
- The paper offers novel insights into the impact of difficult-to-learn examples in contrastive learning.
- The theoretical analysis is robust, and the proposed solutions are straightforward to implement.

### Weaknesses
 - Although the authors find that removing certain training examples consistently improves unsupervised contrastive learning performance, the theoretical results are limited to spectral contrastive learning. It may be more accurate to reflect this focus in the title.
- The experiments are relatively small in scale, with the largest dataset being Tiny ImageNet. Evaluating the approach on larger datasets could strengthen the findings and demonstrate broader applicability. Specifically, the limited scale of the experiments makes it difficult to assess the practical impact of the proposed method on real-world applications. The use of Tiny ImageNet, while useful for initial validation, does not fully capture the complexities and challenges associated with larger, more diverse datasets commonly used in contrastive learning research. This raises questions about the generalizability of the findings to more complex scenarios.

### Questions
Please see the comment.

### Soundness
2

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
4

### Summary
This paper explores the impact of removing difficult-to-learn examples on unsupervised contrastive learning, finding that their elimination can boost classification performance. Through a theoretical framework modeling sample similarity, the study reveals that difficult examples hinder generalization in contrastive learning. Techniques such as example removal, margin tuning, and temperature scaling are shown to enhance generalization bounds and improve performance, supported by empirical validation.

### Strengths
>A theoretical framework is provided for Difficult-to-learn Examples in Contrastive Learning. Any advancement in theory is of interest to me.

>The empirical results show improvement on classification tasks.

### Weaknesses
 >The tightness of the derived bounds should be validated through experiments.


>The inferior performance of hard samples seems too natural to me from the similarity graph view, as it organizes objects through their similarity and may have a bad influence naturally due to the misconnection in the neighborhood. This phenomenon is very likely to happen when the class numbers are small or the sampled batch size is large. The experiments in Figure 1 should include datasets lie ImageNet as it has many label classes and also should discuss the impact of batch size (buffer size in MoCo).


>Some experiments on larger datasets like ImageNet are strongly encouraged to better show the effectiveness.

### Questions
>Can your analysis be generalized to InfoNCE loss? As paper [1] shows through augmentation graph that InfoNCE is also closely related to the decomposition of similarities graphs.


[1]: Contrastive Learning Is Spectral Clustering On Similarity Graph, ICLR 2024

### Soundness
3

### Presentation
3

### Contribution
3

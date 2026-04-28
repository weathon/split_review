# Jump-teaching: Ultra Robust and Efficient Learning with Noisy Labels

- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 5, 5, 5

## Abstract
Sample selection is the most straightforward technique to combat noisy labels, aiming to prevent mislabeled samples from degrading the robustness of neural networks. However, compounding selection bias and redundant selection operations have always remained challenging in robustness and efficiency. To mitigate selection bias, existing methods utilize disagreement in partner networks or additional forward propagation in a single network. For selection operations, they involve dataset-wise modeling or batch-wise ranking. Any of the above methods yields sub-optimal performance. In this work, we propose $\textit{Jump-teaching}$, a novel framework for optimizing the typical workflow of sample selection.  Firstly, Jump-teaching is the $\textit{first}$ work to discover significant disagreements within a single network between different training iterations. Based on this discovery, we propose a jump-manner strategy for model updating to bridge the disagreements. We further illustrate its effectiveness from the perspective of error flow. 
Secondly, Jump-teaching designs a lightweight plugin to simplify selection operations. It creates a detailed yet simple loss distribution on an auxiliary encoding space, which helps select clean samples more effectively. In the experiments, Jump-teaching not only outperforms state-of-the-art works in terms of robustness, but also reduces peak memory usage by $0.46\times$ and boosts training speed by up to $2.53\times$. Notably, existing methods can also benefit from the integration with our framework.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The authors introduce the concept of identifying significant disagreements within a single neural network across different training iterations. This discovery leads to the proposal of a "jump-manner" strategy for model updates, effectively bridging the gaps caused by these disagreements. Jump-Teaching simplifies the sample selection process through a lightweight plugin that generates a clear loss distribution in an auxiliary encoding space. This approach enhances the ability to select clean samples more effectively, addressing selection bias and redundancy. The framework demonstrates substantial improvements in both robustness and efficiency compared to state-of-the-art methods, specifically reducing peak memory usage by 46% and increasing training speed by up to 253%. The paper highlights that current methods can benefit from integrating with the Jump-Teaching framework, suggesting that it enhances the overall approach to learning with noisy labels.

### Strengths
1. The method achieves improved performance under high noise rates on CIFAR datasets.
2. The method demonstrates better computational and storage efficiencies during testing.

### Weaknesses
1. The experiments conducted on CIFAR-10 with 90% symmetric noise lack meaningful insight, as this setting results in random labels for each sample, effectively reducing the task to an unsupervised learning scenario. The high noise rate means that the labels are essentially random, making it difficult to assess the method's ability to handle noisy labels in a realistic weakly supervised scenario. The reported accuracy could be misleading, as the model might be learning statistical patterns unrelated to the actual class labels.
2. The presentation needs improvement. Suggested changes include:
   - The methodology section incorporates experimental analysis (Figure 4), making it difficult to discern insights related to debiasing. The inclusion of experimental results within the methodology section disrupts the logical flow, as it mixes the explanation of the method with its empirical validation. This makes it hard to understand the core principles of the approach before seeing its experimental outcomes. The purpose of the method and the experimental results should be separated for clarity.
   - The connection among the four subsections in Section 3.2 is unclear. The lack of clear transitions between the subsections makes it difficult to grasp how the codebook, auxiliary head, and sample selection mechanisms are integrated. It is not immediately evident how the subsections build upon each other to achieve the overall goal of the method.
   - The framework presented in Figure 1 contains excessive details that are not explained in the introduction; these should either be removed or relocated to the methodology section. The figure includes many components that are not introduced in the text, making it hard for the reader to understand the overall architecture and its purpose. The figure should be simplified or the introduction should provide the necessary context.
3. The authors claim that “Jump-Teaching is the first work to discover significant disagreements within a single network between different training iterations.” However, the concept of leveraging disagreements across different training iterations has been previously studied (see [1]).

### Questions
1. As indicated in Table 5, the accuracy under 90% symmetric noise on CIFAR-10 exceeds 75%, which corresponds to random labels for the training samples. This scenario can be classified as an unsupervised learning task rather than weakly supervised learning. We need to reconsider the implications of generalization in learning with noisy labels using semi-supervised learning methods, given the lack of supervision.
2. It seems unreasonable to separate the updates of the neural network parameters in steps 9-10. Combining \( L^{BCE} \) and \( L^{CE} \) and updating the neural network with respect to the total loss could be more efficient.

### Soundness
1

### Presentation
1

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes "Jump-teaching," a novel framework for robust and efficient learning with noisy labels. By introducing a jump-update strategy and a Semantic Loss Decomposition plugin, the method reduces sample selection bias and enhances efficiency. Experiments show Jump-teaching improves performance over state-of-the-art methods, particularly under high noise conditions, with notable gains in memory efficiency and processing speed.

### Strengths
- Proposes an innovative jump-update strategy that significantly reduces selection bias in single-network training.  
- Semantic Loss Decomposition provides a lightweight yet effective way to distinguish clean and noisy samples.  
- Empirically validated with improved accuracy, efficiency, and robustness across various noise levels and datasets.

### Weaknesses
 - I disagree with the claim that this work is the first to identify disagreements across different iterations within a single network. Prior studies [1,2] have leveraged these disagreements to distinguish clean samples from corrupted data in training sets. Specifically, [1] uses the concept of 'fluctuations' in predictions across training steps to identify noisy labels, and [2] uses the 'First-time k-epoch Learning' metric, which also relies on tracking prediction changes over epochs. I recommend that the authors revise this claim and include comparisons with these two works, clarifying how their approach differs in the definition and utilization of these disagreements.

- In Figure 2, the authors introduce the IoU metric to measure disagreements. Although an explanation of IoU is provided in the appendix, could the authors illustrate what range of IoU values is considered preferable? Because I notice that the IoU value of Jump-update is between the values of self-update and cross-update, the performance of Jump-update is the best (see Figure 2(c,d)). It is unclear how the IoU values relate to the effectiveness of the jump-update strategy. A more detailed analysis of the relationship between IoU values and performance is needed to justify the use of IoU as a metric for disagreement.

- Property 1.   (1) I have a question regarding the assumption in Property 1, namely that $N_A$ equals $N_{iterations}$. From past experience, the model often generates biased selections initially, then gradually corrects this bias as performance improves, given moderate noise rates (10%, 20%). Therefore, error accumulation may not persist in later iterations. The assumption that the number of accumulated errors directly corresponds to the number of iterations seems overly simplistic and does not account for the dynamic nature of model learning. (2) Additionally, the results in Figure 4(a) do not align well with the conclusion of Property 1. The highest test accuracy occurs at r = 50% rather than r = 10%. This discrepancy suggests that the relationship between the jump rate 'r' and the accumulated error is more complex than described by Property 1, and the experimental results do not fully support the theoretical claim.

- There are some concerns regarding whether the jump-update is a more effective strategy for selecting clean samples. (1) In Table 4, at typical noise ratios (e.g., CIFAR-10/100 sym. 50%, CIFAR-100 asym. 40%), J-Co-teaching does not outperform standard Co-teaching (2 networks). This raises questions about the practical advantages of the jump-update strategy in common noise scenarios. (2) While non-trivial improvements are observed in Table 1, these gains do not carry over to a semi-supervised learning setting (see Table 5). In some settings, J-DivideMix is worse than DivideMix. This inconsistency in performance across different learning paradigms suggests that the benefits of the jump-update strategy might be limited to specific training conditions.

- The compared methods in Table 1 are outdated. Comparing with more recent works is necessary; for example, ProMix (IJCAI'23). Specifically, the absence of comparisons with state-of-the-art methods that also address label noise limits the ability to assess the true contribution of the proposed method.

### Questions
see Weaknesses.

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
5

### Summary
To mitigate compounding selection bias and redundant selection operations in existing methods, the authors of this paper propose a novel framework for optimizing the typical workflow of sample selection, called Jump-teaching. Jump-teaching focuses on discovering significant disagreements within a single network between different training iterations by employing a jump-manner strategy for model updating to bridge the disagreements. Besides, Jump-teaching designs a lightweight plugin to simplify selection operations to help select clean samples more effectively. Finally, experimental results on synthetic and real-world noisy datasets, demonstrate the robustness of Jump-teaching.

### Strengths
1. This idea and motivation for discovering significant similarities within a single network between different training iterations are interesting and fascinating.

2. This paper has carried out a lot of formula derivation and proved the effectiveness of the proposed method from the theoretical knowledge level.

3. Figures 1, 2, and 3 in this paper simply and clearly express the main ideas and innovations of the paper.

### Weaknesses
1. Authors need to further provide the results of J-Co-teaching and J-DivideMix on Clothing1M in Table 3 to prove the reliable performance in real scenarios.

2. There are errors with the experimental results data. J-Co-teaching does not achieve optimal performance under some settings in Table 4, such as Sym-0.5 of CIFAR-10 and Sym-0.5 and Asym-0.4 of CIFAR100.

3. The content of the semantic loss decomposition part of this paper is not strongly related to the main motivation of this paper, Jump-update Strategy, and is more like an auxiliary trick. The connection between the jump-update strategy and the semantic loss decomposition is not clearly established, making the latter seem somewhat tangential to the core contribution.

4. There is no clear definition of I_{detection} in Eq. (8). The lack of a precise definition for this term hinders the reproducibility and understanding of the proposed method.

5. The names of the citation methods are not uniform, such as ' JoCoR ' in the relevant work section and ' JoCor ' in the experimental section.

6. It is recommended to compare the proposed method with 2024 SOTAs.

### Questions
See above weaknesses.

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
3

### Summary
This paper proposes the Jump-Teaching methodology for learning with noisy labels. 

Specifically, it investigates an efficient approach that requires only a single network. 

To achieve this, the authors introduce two key techniques: a Jump-update Strategy to mitigate selection bias and Semantic Loss Decomposition to simplify the selection operation. 

The effectiveness of the proposed approach is demonstrated through experiments on three benchmark datasets: CIFAR-10, CIFAR-100, and Clothing-1M.

### Strengths
Research on sample selection methods using a single network to reduce computational costs is an interesting research topic.

### Weaknesses
The academic novelty of this approach appears limited. It is unclear whether updating the model based on selections from the previous step offers any theoretical advantage over the naive approach of updating the model at every iteration. Specifically, the paper lacks a clear explanation of why using a delayed selection would be beneficial, and how this addresses the noisy label problem beyond simply avoiding sequential updates. Moreover, extracting useful information from models at different training epochs has already been extensively explored in the literature. A seminal work in this area, for example, is Snapshot Ensembles: Train 1, get M for free (ICLR ’17).

The experimental results are not convincingly state-of-the-art. In particular, several recent relevant papers (a, b, c) are missing from the references. Their result tables show significantly better performance on CIFAR-10 and CIFAR-100 compared to the results presented in this work.

(a) Generalized Jensen-Shannon Divergence Loss for Learning with Noisy Labels (NeurIPS’21)

(b) DISC: Learning From Noisy Labels via Dynamic Instance-Specific Selection and Correction (CVPR’23)

(c) Sample-wise Label Confidence Incorporation for Learning with Noisy Labels (ICCV’23)

### Questions
It is not clear why using data selection results from previous iterations for model updates would be beneficial. Specifically, why would the set of samples selected by the model in the previous step yield better results than the samples selected in the current step? Is the main advantage simply that it avoids sequential updates, thereby reducing the amplification of error accumulation?

### Soundness
3

### Presentation
3

### Contribution
2

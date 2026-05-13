# Concepts' Information Bottleneck Models

- Decision: Reject
- Scores: 3, 6, 1, 6, 6

## Abstract
Concept Bottleneck Models (CBMs) provide a self-explanatory framework by making predictions based on concepts that humans can understand. However, they often fall short in overall performance and interpretability because they tend to let irrelevant information seep into the concept activations. To tackle concept leakage, we introduce an information-theoretic framework to CBMs by incorporating the Information Bottleneck (IB) principle. Our method ensures that only pertinent information is retained in the concepts by limiting the mutual information between the input data and the concepts.  This shift represents a new direction for CBMs, one that not only boosts concept prediction but also reinforces the link between latent representations and comprehensible concepts, leading to a model that is both more robust and more interpretable. Our findings show that our IB-based CBMs enhance the accuracy of concept prediction and diminish concept leakage without compromising the target prediction accuracy when compared to similar models. We also introduce an innovative metric designed to evaluate the quality of concept sets by focusing on performance following interventions. This metric stands in contrast to traditional task performance measures, which can sometimes conceal the impact of concept leakage, by providing a clear and interpretable means of assessing the effectiveness of concept sets.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper proposes enhancing Concept Bottleneck Models (CBMs) using the Information Bottleneck (IB) framework, addressing the issue of concept leakage, where concept activations contain irrelevant data, compromising model interpretability and performance. This enhancement, termed Concepts’ Information Bottleneck (CIB), constrains mutual information between inputs and concepts, optimizing concept relevance. Experiments on datasets such as CUB, AwA2, and aPY demonstrate improved prediction accuracy and interpretable concept representations. Additionally, the authors introduce a novel metric to assess concept set quality by evaluating intervention performance, offering a direct measure for interpretability.

### Strengths
The idea is clear: incorporating the IB into CBMs addresses the concept leakage issue.

The experiment is extensive, evaluating the proposed method across three dimensions: accuracy, interventions, and interpretability.

Additionally, a novel metric is proposed to assess the quality of concept sets based on intervention performance.

### Weaknesses
The improvement of the proposed method compared to existing methods is marginal (Table 2), especially given that prediction accuracy is a primary evaluation metric, making the experimental results less compelling. The reported gains in accuracy are quite small, and it's unclear if these differences are statistically significant or practically meaningful, particularly when considering the added complexity of the proposed approach. A more rigorous analysis, including confidence intervals or statistical tests, should be included to support the claims of improvement.

The variational inference derivation is relatively straightforward and could be moved to the appendix. The derivation, while technically correct, does not present any novel insights or significant challenges that warrant its inclusion in the main body of the paper. Its presence interrupts the flow of the paper and could be better placed in a supplementary section.

The process of incorporating the IB into CBMs is not clearly explained; adding a diagram to illustrate this process would improve clarity. The explanation of how the Information Bottleneck is integrated into the Concept Bottleneck Model is vague and lacks sufficient detail. It is difficult to understand how the mutual information constraints are applied and how they affect the training process. A visual aid, such as a diagram, would be beneficial to clarify this process. Furthermore, the specific choices for estimating mutual information and entropy should be discussed in more detail, including the potential impact of these choices on the results.

The core idea of applying the established IB framework to CBMs limits the novelty of this work. While the application of the Information Bottleneck framework to CBMs is a reasonable idea, the core concept is not particularly innovative. The paper essentially applies an existing technique to a new domain, and the results do not demonstrate a significant advancement in the field.

### Questions
In Table 2, the improvements in prediction accuracy on most datasets are very limited compared to the baseline models. Could you provide more explanation on this? What are your thoughts on these limited improvements, and given this, how can we conclude the effectiveness of the proposed CIB method?

Additionally, since the CIBM_B model in Section 3.1 performs worse than almost all baselines, is it still necessary to devote so many pages to this method? More explanation on this could be helpful to understand the contribution of this section.

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
4

### Summary
This paper addresses the issue of information leakage in concept bottleneck models (CBMs), a significant challenge that impacts CBMs' interpretability and intervenability. The key idea is to apply Tishby’s Information Bottleneck (IB) principle in concept representation learning. Specifically, the author proposed to compress task-irrelevant information about the data X from the learned concept representation C, whereas making C maximally predictable for the label Y. This information compression is believed to be useful for controlling information leakage. The author further develop two methods to implement their IB-based framework and evaluates their efficacy on three different datasets.

### Strengths
- The work, to the best of my knowledge, is the first one who explicitly marries IB with CBMs, and is the first one that analyzes the info-plane in CBM learning;
- The proposed IB-based idea for mitigating information leakage is both natural and elegant. The IB-based framework proposed in this work seems also highly general and can potentially be implemented by a wide range of methods beyond the two suggested by the authors;
- The paper is overall well written and is easy-to-follow;
- The work has been compared against state-of-the-art methods in the field, including CEM and PCBM. Notably, it does not require additional modules (as in PCBM) or additional regularization techniques (as in CEM), being simple and easy-to-use;
- The paper also proposed a novel, general-purpose metric for evaluating the quality of the learned concepts, marking the first instance of assessing the quality of the concept set rather than individual concepts.

### Weaknesses
 - (Major) Despite the elegant framework proposed, some implementation details may lack clarity and require further justification; please see the “questions” section below;
- (Major) The technical method for minimizing mutual information (MI) in the proposed IB-based CBM method is actually not so novel and largely relies on existing methods such as [1];
- (Major) The comparison between the two IB implementations appears somewhat simplistic and may provide only limited insights. What makes the estimator-based implementation more useful than the other?
- (Minor) While the presentation is generally good, some content could be more concise and structured. For instance, the derivation in Section 3.1 could be streamlined to present only the essential final estimator used in practice, relegating the full derivation to the appendix;
- (Minor) The main experimental results are based on only three runs. While I appreciate the author’s transparency in reporting this, more runs could be considered for better robustness of the results;
- (Minor) When assessing intervenability, a comparison between the proposed CIBM method and the original CBM is lacking. How CIBM exactly helps in improving intervenability does not seem apparent.
- (Minor) Reproducibility: despite the very interesting and elegant proposal, no code repo is shared. Together with the missing technical details mentioned above, this weaken the reproducibility of the work.

### Questions
- How is the ground truth probability p(c|z) in the conditional entropy-based implementation computed, is it available from the data?
- Regarding the estimator-based implementation mentioned in Sec 3.2, what is the exact routine for optimizing I(X; C)? Do you employ an approach similar to adversarial training, where you first estimate I(X; C) before each gradient step for optimizing C? 
- Is the results for CBM in Table 2 corresponding to the case where you use hard (i.e. binary) concept label? If so, it would be beneficial to explicitly mention this;
- The proposed IB-based CBM framework for controlling information leakage appears quite general. While the method mainly used Kawaguchi’s method [1] for estimating I(X; C), could alternative methods, such as variational approximation to densities [2] and slice mutual information [3], also be applicable? These methods may be more effective in removing information from the learned concept representation. I feel the paper could benefit from a discussion on the generality of their framework.



*References:*

[1] How does information bottleneck help deep learning? ICML 2023

[2] CLUB: A Contrastive Log-ratio Upper Bound of Mutual Information, ICML 2020

[3] Scalable Infomin Learning, NeurIPS 2022

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
This paper introduces an enhancement to Concept Bottleneck Models (CBMs) through the integration of the Information Bottleneck framework, attempting to address the problem of concept leakage  in CBMs. The authors propose a Concepts' Information Bottleneck Model (CIBM) that minimizes mutual information between inputs and concepts while maximizing expressivity between concepts and labels, introducing two variants: a bounded CIB (CIBMB) and an estimator-based CIB (CIBME) Additionally, the authors propose a novel intervention scheme based on a measure of 'uncertainty', and propose two metrics to assess concept set quality based on intervention performance.

### Strengths
**Novel Research Direction**  
The paper introduces an innovative approach by studying and directly addressing the memorization-compression pattern in concept bottleneck models.

**Technical Writing Quality**  
The paper demonstrates good clarity in its presentation:
- Clear and logical flow of ideas throughout the manuscript
- Concise and grammatically sound writing
- Well-designed figures and tables that effectively complement the text
- Abstract and title that accurately capture the paper's core contributions

### Weaknesses
 **Experimental Limitations**
The experimental evaluation is insufficient, primarily relying on comparisons against a vanilla CBM with unspecified training parameters. The results are not compelling, as CEM appears to either outperform or match the proposed methods on the CUB dataset.

**Unreproducible**
The experiment section is not comprehensive enough to be reproducible, no code is supplimented.

**Intervention Strategy**
The Uncertainty Based (UB) concept interventions fail to demonstrate meaningful improvements. The method's performance is comparable to or worse than random baselines. The paper lacks crucial comparisons with contemporary intervention strategies from recent literature.

## Clarity and Novelty Issues

**Metric Formulation**
The proposed metrics lack novelty and present existing concepts in a potentially misleading way:

- The concept intervention trends (positive/negative) have been extensively documented in previous work, including the CEM paper
- AUC_TTI reduces to a simple mean, obscuring nonlinear trends that are more effectively visualized in graphical form (as evident in Figure 3)
- NAUC_TTI's formulation is problematic:
  - It simplifies to the difference between positive intervention and baseline performance
  - This comparison is standard practice in modern concept bottleneck model papers
  - The metric can paradoxically penalize superior models (e.g., CEMs would score worse despite improving baseline accuracy while maintaining intervention performance)

**Visualization Recommendation**
Rather than introducing potentially confusing metrics, intervention results would be better presented through graphs showing performance across multiple concept groups, providing clearer and more interpretable results.

### Questions
**Methodology Questions**
1. Line 278: Which CBM training scheme (joint, sequential, or independent) is used for comparison? Given that sequential training is known to reduce concept leakage (as per the pitfalls paper https://arxiv.org/pdf/2106.13314), why wasn't a comparison made against CBM using hard concept representations and independent training?
2. Line 149: Its not clear where Z is coming from under your formulation, presumably some layer before the concept bottleneck?
3. Line 300: "We use ResNet18 embeddings provided by the dataset authors and train FCN on top of them." For this dataset and the others, are the backbone networks further tuned during training? 

**Results and Comparisons**

4. Line 324-377 (Table 2): Why are baseline comparisons inconsistent across datasets?
   - PCBM comparisons only appear for some datasets. Furthermore, comparing against PCBM is not necessary nor useful, as PCBMs are not trained to be susceptible to interventions. 
   - CEM results only shown for CUB (where it outperforms the proposed methods)
   - ProbCBM results only shown for CUB

**Experimental Design**

5. Line 431: The claim about CIBME's training stability needs validation loss curves for support.

6. Line 522: Why are concept interventions varied for CUB but not for AWA2?

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper addresses a significant issue in Concept Bottleneck Models (CBMs): concept leakage. This occurs when the model encodes additional information in the concept values beyond what is necessary to solve a task. To mitigate this, the authors propose Concept Information Bottleneck Models (CIBMs), a novel training approach for CBMs that utilizes Information Bottleneck and Mutual Information techniques. By minimizing the information bottleneck between concepts, inputs, and outputs, they effectively limit the information flow, thereby reducing leakage. The framing of this approach is intriguing, and the experimental results provide promising insights into its effectiveness. Additionally, the paper introduces a new metric and its variation for evaluating how well a CBM handles interventions, which is closely related to measuring concept leakage.

### Strengths
- The paper is well-written and easy to follow. It provides a solid motivation for the problem, offering sufficient context on concept leakage and how it has been addressed by existing methods.
- Employing Mutual Information is a novel and intriguing approach to mitigate concept leakage, a critical issue in Concept Bottleneck Models (CBMs).
- The authors effectively guide the reader through the solution’s formulation, offering enough theoretical insights to understand why they arrived at the two proposed solutions: $CIBM_E$ and $\text{CIBM}_{\text{B}}$.
- The newly introduced metric is a clever addition, as it provides an automatic evaluation of what prior works have mostly assessed graphically. While the concept itself is not entirely new (as CBMs are often evaluated through plots showing model performance with increasing interventions), the metric encapsulates this idea into a single value that assesses the overall trend.

### Weaknesses
 - In the practical scenario, the architecture they employ is not entirely clear to me. I understand that the $q(\cdot)$ functions are distributions parameterized by neural networks, but the details regarding the rest of the model, particularly $z$, are unclear (see Q1). Are the concepts being supervised, and is the same set of concepts used as in traditional CBMs? A simple visual representation of the model, highlighting the differences introduced compared to CBMs, would be very helpful.
- The experimental section also raises some concerns:
	1.	The rationale behind dropping certain baselines (as seen in Table 2) is not well explained. For instance, I would have expected to see all baselines, particularly CEM, as it is one of the most powerful CBM-like models in terms of accuracy (see Q2).
	2.	Several claims are either missing supporting information (Figure 1), lack proper motivation (L426-431), or are somewhat misleading (L467-469). Regarding Figure 1, there is no discussion about $I(X;C)$, which, as far as I understood, should exhibit a lower value for CIBM later in the training compared to CBM, but this doesn’t seem to happen and isn’t discussed. Both CBM and CIBM display a similar trend in $I(C;Y)$, though the effect is less pronounced for CBM (as expected) (see Q3). Additionally, the explanation in L426-431 is unclear, especially since Figure 3 shows CBM and CIBM behaving similarly, leaving it unclear what insight the reader is supposed to take away (see Q4). Lastly, L467-469 are somewhat misleading, as there is no baseline comparison. Even a comparison with CBM would be fine here. Since CBM might also exhibit a similar trend in responsiveness to interventions while suffering from leakage, the statement “does not suffer from concept leakage” seems too strong or well not motivated (see Q5).
	3.	If the goal of the model is to reduce leakage, why isn’t it compared against other models that tackle the same issue, such as those cited in the paper (e.g., “Addressing Leakage in Concept Bottleneck Models”)? Including a comparison with at least one of these models would strengthen the experimental validation (see Q6).

Addressing these issues would significantly improve the clarity and strength of the paper, and I would be inclined to raise my score.

### Questions
**Q1**: Is $z$ simply a hidden representation extracted from a neural network (e.g., the output of a ResNet)? Does your model follow the structure: $x \rightarrow z \rightarrow c \rightarrow y$? Clarifying this would help improve understanding of the overall architecture.

**Q2**: Why did you drop certain baselines in some experiments, retaining only a few (e.g., dropping CEM in all experiments except CUB)? I would prefer a comparison with the strongest model, such as CEM, instead of weaker models like PCBM, to ensure a fair performance evaluation.

**Q3**: Could you clarify whether the trend or the higher value of $I(C;Y)$ is more significant, and explain why this matters? Additionally, what does a lower $I(X;C)$ represent in practical terms? Moreover, please standardize the x-axis range across all plots to avoid misleading comparisons between methods.

**Q4**: The plots in Figure 3 all appear quite similar, and it’s unclear what specific differences I should focus on. Could you explain your claims more clearly and point out the key takeaways?

**Q5**: Why was CBM not included as a baseline in Figure 4? Given that CBM likely exhibits a similar trend to CIBM, the statement that “CIBM does not suffer from concept leakage” feels unsupported. Could you strengthen this claim with further evidence or comparative results?

**Q6**: Why did you choose not to compare your model with other approaches specifically designed to reduce leakage, such as “Addressing Leakage in Concept Bottleneck Models”? 

**Q7**: Regarding Table 3, why is the performance on CUB so low when there are no corrupted concepts? I would expect it to be at least higher than the accuracy. Furthermore, do you have any insights into why your model’s AUC drops more than CBM’s as the number of corrupted concepts increases (at some point, CBM even surpasses CIBM)? Additionally, why did you choose to corrupt only one concept in AwA2, using a different evaluation setup compared to CUB? Please also specify the strategy used for intervention (uncertainty or random).

**Q8**: At L524, what do you mean by “trained with different concept annotation”? Were CBM and CIBM trained using the same concept annotations, or were there differences in the annotations used?

**Curiosity**: Did you happen to evaluate CEM in the experimental setup used for Figure 2? It would be interesting to observe the trend of a concept-based model with higher expressive power, such as CEM, in comparison to the models you presented.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This work proposes an enhancement to Concept Bottleneck Models (CBMs) by integrating the Information Bottleneck (IB) framework, aimed at addressing issues of concept leakage and reduced performance. Further, a model-based metric is introduced to measure concept set goodness.  Experiments conducted on CUB, AwA2, and aPY datasets demonstrate that IB-augmented CBMs improve both concept and target prediction accuracy while increasing intervenability.

### Strengths
-	The paper introduces a novel integration of the Information Bottleneck framework into CBMs, which is an interesting theoretical contribution to the area of explainable AI.

-	The paper provides sufficient experimental results on multiple datasets, demonstrating the performance of the proposed method in both concept and target prediction accuracy being on par or slightly better than current approaches

-	The introduction of a novel metric to assess the quality of concept sets based on intervention performance is a valuable addition. This metric offers a direct and interpretable evaluation of concept set goodness, addressing a gap in the current literature.

### Weaknesses
 - The integration of the Information Bottleneck framework adds complexity to the CBMs. A more detailed discussion of the computational overhead and implementation challenges associated with the proposed method would improve the paper.
- The performance of the proposed method may be sensitive to the choice of hyperparameters, such as the Lagrangian multiplier β. A more systematic approach to hyperparameter tuning could be explored to optimize performance.

- The claim of significant improvement in performance compared to vanilla CBMs and related advanced architectures lacks rigorous statistical support. It is unclear if the reported improvements are statistically significant.

### Questions
you claim to achieve significant improvement in performance compared to vanilla CBMs and related advanced architectures. How do you support this claim of being significant? Is this meant to be statistically significant?

### Soundness
3

### Presentation
3

### Contribution
3

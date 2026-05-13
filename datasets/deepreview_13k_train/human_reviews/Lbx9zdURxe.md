# Regularizing Energy among Training Samples for Out-of-Distribution Generalization

- Decision: Accept
- Scores: 6, 6, 6, 6

## Abstract
The energy-based model provides a unified framework for various learning models where an energy value is assigned to each configuration of random variables based on probability. Recently, different methods have been proposed to derive an energy value out of the logits of a classifier for out-of-distribution (OOD) detection or OOD generalization. However, these methods mainly focus on the energy difference between in-distribution and OOD data samples, neglecting the energy difference among in-distribution data samples. In this paper, we show that the energy among in-distribution data also requires attention. We propose to investigate the energy difference between in-distribution data samples. Both empirically and theoretically, we show that previous methods for subpopulation shift (\emph{e.g.}, long-tail classification) such as data re-weighting and margin control apply implicit energy regularization and we provide a unified framework from the energy perspective. With the influence function, we further extend the energy regularization framework to OOD generalization scenarios where the distribution shift is more implicit compared to the long-tail recognition scenario. We conduct experiments on long-tail datasets, subpopulation shift benchmarks, and OOD generalization benchmarks to show the effectiveness of the proposed energy regularization method. The source code will be made publically available.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes to explore the energy score between ID samples. It also theorectically suggests that previous methods for long-tail classification implicitly apply energy regularization. Some experiments are conducted to show the effectivness of the proposed engergy-based regularization.

### Strengths
1. The paper is well-written and well-structured.
2. Experiments are extensive to show the effectiveness of the method.
3. Theorectical analysis makes the paper more solid.

### Weaknesses
1. It seems that the proposed method does not perform consistently better than baseline methods and relatively unstable.

2. The designed influence function requires a large amount of time and computational recouces for approximating $\beta$.

3. In Fig 3, it can be observed that class 7 is a outlier. What cause this class significantly deviate the trend?

4. Some tables use testing error, while some use accuracy. It would be more readable to make them consistent.

### Questions
See weakness.

### Soundness
3

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
This submission presents a unified framework for energy-based models applied to both in-distribution and out-of-distribution (OOD) data. While prior methods in OOD detection focus on energy differences between in-distribution and OOD samples, this work highlights the importance of examining energy differences within in-distribution samples. The submission proposes investigating these differences, showing that techniques commonly used for subpopulation shifts—such as data re-weighting and margin control in long-tail classification—implicitly apply energy regularization. This framework is further extended to address more implicit distribution shifts, as seen in OOD generalization scenarios, using influence functions to support the approach. Experimental results on long-tail, subpopulation shift, and OOD generalization benchmarks demonstrate the effectiveness of this energy regularization method. The source code will be publicly available.

### Strengths
+ To my knowledge, this work is the early work that focuses on the energy of in-distribution data and use it as a regularization for learning models. 
+ The Figure 2 well illustrates the motivation of this submision: the existing methods on long-tail problem can be reviewed as a kind of energy regularization to learn models. 
+ The writing is clear. The related work, the derivation of unified view are also clear. 
+ The expeiments domonstrate that proposed IAER can bring some improvements over baselines.

### Weaknesses
 - The main concern lies with the experimental settings. Although the proposed IAER method shows some improvement over the standard baseline (ERM), it does not achieve competitive results compared to state-of-the-art methods. Specifically, Table 2 only includes comparisons with two works from 2019. Why are more recent works not included for comparison? This same question applies to Tables 3, 4, and 5. I would except more recent work to be included and disucssed. Just name a few: 1) Gradient Reweighting: Towards Imbalanced Class-Incremental Learning  2) Dynamic residual classifier for class incremental learning, 3) Towards principled disentanglement for domain generalization. 4) Flatness-aware minimization for domain generalization


- Lines 270–282 lack clarity. For instance, the statement “The least we can do is to prevent the model from being over-confident… note that the energy does not correspond to the prediction of the classifier (Remark 4.1), which is the reason most previous works overlook the energy disparity” requires further clarification: 1) yes, we usually do not have knowledge of test distribution. But how to prevent it from being over-confident? Specifically, what mechanism in the proposed method achieves this? 2) I am not clear why Remark 4.1 explains why most previous works overlook the energy disparity between training data samples. The remark itself states that energy doesn't correspond to prediction, but it doesn't explain why this would cause the disparity to be overlooked. 3) Additionally, the main point of Remark 4.1 is unclear. Could you clarify its purpose and significance? It seems to state the obvious, that energy is not the same as classification probability, but it's not clear what the implications of this are for the proposed method or why it's important to highlight.

### Questions
Please clarify the experimental analysis and Remark 4.1. Please see the above for more details.

### Soundness
3

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
3

### Summary
The paper addresses the issue of OOD generalization in machine learning models. It proposes a novel approach to regularize the energy among ID data samples, which is crucial for improving OOD generalization performance. The authors argue that previous methods have focused on the energy difference between ID and OOD data, neglecting the energy differences among ID data samples. They introduce an energy regularization framework that unifies various long-tail recognition methods and extends it to OOD generalization scenarios. The paper empirically and theoretically demonstrates the effectiveness of the proposed method, called Influence-Aware Energy Regularization (IAER), through experiments on long-tail datasets, subpopulation shift benchmarks, and OOD generalization benchmarks

### Strengths
1. The paper offers a novel perspective on energy-based models by focusing on the energy differences among ID data samples, which is often overlooked in favor of the energy difference between ID and OOD data.
2. It provides a unified framework that connects long-tail recognition methods like data re-weighting and margin control, interpreting them as implicit energy regularization techniques.
3. The paper supports its claims with extensive experiments on various benchmarks, datasets, and scenarios, demonstrating the effectiveness of the proposed IAER method.

### Weaknesses
1. Inconsistent symbol usage can lead to ambiguity. For instance, in line 150, the variable $y$ denotes the specific label associated with a data point $x$, whereas in Equation 2, $y$ appears to represent the set of all training classes. This lack of clarity makes it difficult to follow the mathematical derivations and understand the precise meaning of the equations. The paper should consistently use distinct symbols for individual labels and the set of all labels to avoid confusion.
2. The definition of symbols should be clear and unambiguous. For example, in line 210, it states "for a data sample $x$ suppose the ground truth is $\hat{y}$".  The term"suppose" typically implies an assumption or prediction, which might be misleading in this context. Additionally, it is important to clarify the distinction between $y$ and  $\hat{y}$. The paper needs to explicitly define what $\hat{y}$ represents, especially in relation to the true label $y$, and clarify if it's a predicted label or a target value.
3. The baselines used in the study appear to be outdated. For instance, the baseline in Table 2 dates back to 2019, and the baseline in Table 3 is from 2020. Given the rapid advancements in the field, using more recent benchmarks would provide a more accurate and relevant comparison, thereby enhancing the validity and reliability of the results. The paper should include comparisons with state-of-the-art methods to demonstrate the true effectiveness of the proposed approach.

### Questions
1. In the transition from Eq. 5 to Eq. 6, the term $\hat{\beta_x} \cdot E_\theta(x)$ appears to be missing on the left side of the equation. Could the authors please clarify the derivation process between these two equations？Additionally, what does  $\mathcal{L}$ refer to in Eq.6?  Is $\mathcal{L}$ the same as $\mathcal{L}_{ce}$ in Eq.5?

2. Is the influence function calculated at each training epoch? Table 6 shows the time used for the influence function calculation, which appears to be computationally intensive. Could the authors provide a breakdown of the computational costs, specifically comparing the time spent on influence function calculation to the overall training time? This would give a clearer picture of the method's efficiency.

3. In Tab. 3, the selection of the validation set is crucial for model performance, especially in long-tailed scenarios where the test distribution can significantly differ from the training distribution. Could the authors provide a more detailed explanation of their validation set selection strategy, including the rationale behind their choices for different datasets? In Appendix A.1, why is a balanced validation set maintained for CIFAR, and how does the number of data points in the validation set affect the IAER? For ImageNet-LT, the validation set samples are excluded from the training set, whether it break the imbalance factor? Furthermore, excluding certain specific classes will downgrade the corresponding performance in Tab. 3, decreasing the generality of the method.

4. In line 317, the terms "positive influence" and "negative influence" are used. Could the authors provide clear definitions of these terms in the context of their method? Additionally, could they explain how these influences relate to the energy values of data points, particularly for low-energy points?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper proposes a new approach to improve model performance in detecting and generalizing to out-of-distribution (OOD) data. Unlike traditional methods, which primarily focus on the energy difference between IID and OOD data, this approach also considers energy differences within IID samples. The authors explain that the re-weighting and margin-based methods commonly used in long-tailed learning implicitly apply energy regularization. Then the authors introduce Influence-Aware Energy Regularization (IAER), which adjusts energy values based on influence functions derived from training data. Empirical experiments demonstrate the effectiveness of this method.

### Strengths
- The idea of considering energy differences among in-distribution data samples is both novel and sensible.
- The authors conduct a series of experiments, spanning long-tailed datasets, subpopulation shift benchmarks, and OOD generalization benchmarks, to evaluate the effectiveness of the proposed method.

### Weaknesses
 - The connection between Sec.3 and Sec.4 appears somewhat disjointed. The motivation for the proposed method in Sec.4 seems detached from Sec.3, lacking continuity and a strong foundation. Specifically, while Sec.3 discusses energy regularization and its implicit presence in long-tail learning methods, Sec.4 introduces Influence-Aware Energy Regularization (IAER) without a clear, direct link to the preceding analysis. The transition feels abrupt, leaving the reader to infer the connection rather than having it explicitly stated and justified.

- The explanation of the re-weighting and margin control methods as implicitly affecting training energy feels somewhat forced. For instance, the paper primarily uses the first term in Eq. (6) to justify the impact of $\hat{\beta}_x$. However, the second term in Eq. (6), which also contains $\hat{\beta}_x$, influences the final loss. The argument that re-weighting and margin control are solely captured by the first term is not entirely convincing, as the second term also plays a role in the overall loss calculation. This makes the effectiveness of energy regularization, as presented, somewhat ambiguous and not fully supported by the provided analysis.

- The method's overall effectiveness is limited. For example, in Tab.3, when IAER is combined with cRT, the performance across all classes declines, and with LWS, the improvement brought by IAER across all classes is only about 0.2%. These results suggest that the proposed IAER method does not consistently improve performance across different base methods and datasets. The marginal gains, and in some cases, performance degradation, raise questions about the robustness and general applicability of the approach. The lack of substantial improvements in these experiments weakens the overall impact of the proposed method.

- There are some typos, such as in Tab.3, where "iNatrualist" should be "iNaturalist".

### Questions
Please refer to the weakness section.

### Soundness
3

### Presentation
2

### Contribution
2

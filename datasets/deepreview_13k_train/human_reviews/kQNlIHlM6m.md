# Fair Class-Incremental Learning using Sample Weighting

- Decision: Reject
- Scores: 6, 6, 3, 3

## Abstract
Model fairness is becoming important in class-incremental learning for Trustworthy AI. While accuracy has been a central focus in class-incremental learning, fairness has been relatively understudied. However, na\"ively using all the samples of the current task for training results in {\it unfair catastrophic forgetting} for certain sensitive groups including classes. We theoretically analyze that forgetting occurs if the average gradient vector of the current task data is in an ``opposite direction'' compared to the average gradient vector of a sensitive group, which means their inner products are negative. We then propose a {\it fair class-incremental learning} framework that adjusts the training weights of current task samples to change the direction of the average gradient vector and thus reduce the forgetting of underperforming groups and achieve fairness. For various group fairness measures, we formulate optimization problems to minimize the overall losses of sensitive groups while minimizing the disparities among them. We also show the problems can be solved with linear programming and propose an efficient Fairness-aware Sample Weighting (\method{}) algorithm. Experiments show that \method{} achieves better accuracy-fairness tradeoff results than state-of-the-art approaches on real datasets.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces Fairness-aware Sample Weighting (FSW), a novel approach for addressing unfair catastrophic forgetting in class-incremental learning. In class-incremental learning, the goal is to learn new classes of data without forgetting previously learned ones. The authors extend this problem to fair class-incremental learning where the goal is to satisfy fairness notions among sensitive groups and have a high classification accuracy. This method learns sample weights for current task samples based on a given fairness metric to mitigate the "unfair forgetting" problem, which arises when a model disproportionately forgets specific groups. The authors theoretically show that if the gradient direction of new task samples is misaligned with that of an underperforming group, the loss disparity between underperforming and overperforming groups could increase. To overcome this, FSW adjusts the average gradient vector by assigning optimized sample weights to current task samples, calculated based on the selected fairness metric. The proposed framework supports multiple group fairness notions, equal error rate(EOO), equalized odds(EO), and demographic parity(DP) and it can be extended to other notions. They also show that the proposed sample weighting method is equivalent to a linear program and could be solved efficiently. The authors validate FSW on several datasets and show that it achieves a favorable accuracy-fairness balance compared to existing baselines.

### Strengths
- The presentation of the paper is quite clear and well organized. The example given in the introduction and the first figure help readers understand the problem setup and the challenge. 
- To my knowledge, the problem formulation is novel and the proposed method is original. It introduces group fairness notions to class-incremental learning where the class itself can even be a sensitive attribute. Based on existing literature on gradient angle analyses for forgetting previous classes, the authors extend this to unfair forgetting by examining the gradient misalignment between the sensitive groups and new data. The authors also show that theoretically how the misaligned gradients could exacerbate the disparity of the loss between underperforming and overperforming groups.
- The proposed sample weighting algorithm is equivalent to linear programming and could be solved in polynomial time.
- The experiments section is comprehensive, the authors consider several different datasets and baselines. The experiments show that FSW has better performance in terms of balancing classification accuracy and fairness.

### Weaknesses
 - Although overall the paper is well organized, I think that several parts could have more clarification in terms of mathematical writing. For example, in Equation 1 there are two gradient vectors multiplied with a dot $\nabla_{\theta} \ell( f_{\theta}^{l-1}, G ) \cdot\nabla_{\theta} \ell( f_{\theta}^{l-1}, d_{i} )$, using a transpose could improve the clarity and readability. A similar argument can be made for the weighted gradient term as well $w_l\nabla_{\theta} \ell( f_{\theta}^{l-1}, T_{l})$, it would be helpful to introduce this notation explicitly before using it.
- The authors show that the sample weighting problem is equivalent to linear programming. Prior to this conversion, the feasible set is defined as a hypercube, $[0,1]^d$. If the conversion to a linear program does not alter this feasible set, it implies that the optimal solution for the weight vector would lie at a vertex of the hypercube, meaning all weights will be either 0 or 1. Figures 2 and 15-22 appear to support this claim. Can you clarify whether the optimal weights are indeed binary (0 or 1) in practice? If so, how does this affect the interpretation of FSW as a weighting method versus a selection method? I am not sure that it will affect the normalizing factor during the parameter update step(normalizing with the total number of samples instead of normalizing with the number of samples whose weight is 1). Additionally, if this observation/claim is true, then the visualization of the weights in Figure 2 could be improved. It could show the percentage of the active samples that have weight 1 from each group.

### Questions
You can see the points raised in the weaknesses section. I have also additional questions:
- Could authors explain why they consider the average absolute difference between the loss of a class and the average loss of all classes for group fairness notions? Have you considered using squared differences instead of absolute differences in your fairness measures? If so, what were the tradeoffs in terms of computational complexity and performance? Would this alternative formulation allow for a closed-form solution with a projection step?
- It’s unclear whether FSW is applied to each batch individually or calculated once at the beginning of each epoch, with the same weights used for all batches within that epoch. A clarification on this would be helpful.
- Although buffer size is not the main focus of the paper, it would be insightful to understand its impact on unfair forgetting. Have you considered running an ablation study varying the buffer size to examine its impact on unfair forgetting and the proportion of new data assigned non-zero weights?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper presents a novel approach to address the challenge of fairness in class-incremental learning, a subfield of continual learning where models must learn new classes over time without forgetting previously learned ones. The core contribution is the Fairness-aware Sample Weighting (FSW) algorithm, which adjusts the training weights of current task samples to mitigate unfair catastrophic forgetting for sensitive groups, including classes. The authors propose a theoretical framework to analyze the conditions under which forgetting occurs due to opposite gradient directions between current and sensitive group data. They formulate optimization problems to find sample weights that minimize loss and unfairness, supporting fairness measures like Equal Error Rate (EER), Equalized Odds (EO), and Demographic Parity (DP).

### Strengths
1. Theoretical Foundation: This paper gives good theoretical analysis of how unfair catastrophic forgetting can occur in class-incremental learning, and adjusts the training weights to reduce the forgetting of underperforming groups and achieve fairness.
2. Rigorous Experiments: The experiments are conducted across multiple datasets, which adds to the robustness of the findings. The paper demonstrates that FSW achieves a better accuracy-fairness tradeoff, which is a significant result in the context of fair machine learning.

### Weaknesses
1. Generalization to Multiple Sensitive Attributes
Issue: The paper primarily focuses on a single sensitive attribute, and the performance of the FSW algorithm in scenarios with multiple intersecting sensitive attributes is not fully explored (for ecample, race and gender in Adult dataset). The current approach of reweighting samples based on a single sensitive attribute may lead to unintended consequences when multiple sensitive attributes are present. For example, improving fairness for one attribute might inadvertently worsen fairness for another, or create new disparities within subgroups defined by the intersection of attributes. The paper lacks a discussion on how the proposed method would handle these complex scenarios, and whether the theoretical guarantees still hold.
Recommendation: The authors should conduct experiments or theoretical analysis to evaluate how the FSW algorithm performs when multiple sensitive attributes are present, such as Adult and Compas dataset.
2. Quantify the tradeoff between fairness and accuracy.
Issue: The paper does not quantify the tradeoff between fairness and accuracy. As iCaRL may outperform FSW in accuracy, the authors should quantify this tradeoff, such as the area under the fairness-accuracy curve. A more detailed analysis of the performance trade-offs is needed. Specifically, it is unclear how much accuracy is sacrificed to achieve the reported fairness gains. The paper should include a visualization of the fairness-accuracy trade-off, such as a Pareto frontier, to allow for a more comprehensive understanding of the method's performance characteristics.

### Questions
1. Generalization to Multiple Sensitive Attributes
Will the modification in gradient affect another sensitive attribute while imporving the fairness on one sensitive attribute?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper addresses fairness in class-incremental learning, proposing a Fairness-aware Sample Weighting (FSW) algorithm. In class-incremental learning, where models incrementally learn new classes, unfair catastrophic forgetting can lead to bias, especially in sensitive groups. The paper theoretically analyzes the phenomenon, identifying that forgetting occurs when gradients for new and sensitive groups diverge. FSW adjusts sample weights to align gradient directions, thus minimizing forgetting in sensitive groups. Experimental results indicate that FSW provides a better accuracy-fairness tradeoff than existing methods on various datasets.

### Strengths
1. The paper presents a new approach to incremental learning by integrating fairness considerations directly into the learning process through sample weighting. This is a creative solution that addresses a gap in the literature, as most prior work has focused on accuracy alone.

2. The theoretical analysis provided is rigorous and well-founded.

### Weaknesses
1. The convergence analysis is necessary for the proposed method. Due to the sample reweighting, the learning objective is changed, so it is not clear whether the converged point is close to the global optimum or not. Intuitively, adjusting the sample weights will encourage overfitting to a small group of "easily" learned samples. However, this small group of data may not be a good representation of the whole data distribution. The core issue is that the reweighting fundamentally alters the optimization landscape, potentially leading to convergence at a suboptimal point compared to the original, unweighted objective. This shift in the objective function needs more rigorous justification, as convergence to a stationary point of the reweighted objective does not guarantee convergence to a desirable solution for the original problem.

2. Should $m$ change according to different sample weights $w$? In some cases where $w_i=0$, this sample should not be counted as one in calculating $m$. The definition of $m$, particularly in the context of demographic parity, needs to be clarified. Specifically, if the sample weights $w_i$ are zero for certain samples, it is unclear whether these samples should still contribute to the calculation of $m$. This ambiguity can affect the accuracy of the demographic parity constraint and needs to be addressed with a clear mathematical formulation.

3. Theorem 1 assumes overperforming groups have a lower loss than underperforming groups. Where is the loss defined wrt, on training data or validation data? There might also be some overfitting issues. The assumption in Theorem 1 that overperforming groups have lower losses than underperforming groups needs further clarification. Specifically, it is not clear whether the loss is calculated on the training data or a separate validation set. If the loss is calculated on the training data, it is susceptible to overfitting, and the theorem's conclusions may not generalize well. If it is on validation data, it is not clear how the validation data is selected and if it is representative of the overall data distribution.

### Questions
Please see the weakness.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper tackles the challenge of unfair catastrophic forgetting in class-incremental learning by refining the training weights for samples from the current task. The core method involves adjusting the average gradient vector of the current task’s data by applying specific weights, aiming to minimize both unfairness and loss through the inner product of the gradient vectors. The proposed algorithm is evaluated against multiple baseline methods across various datasets and fairness metrics.

### Strengths
- This approach aims to address the issue of unfair catastrophic forgetting in class-incremental learning by modifying the average gradient vector for the current data.

- It provides a theoretical analysis of the unfair forgetting phenomenon within class-incremental learning.

- It also formalizes fairness-focused optimization problems and reformulates them as linear programming problems to identify suitable sample weights.

### Weaknesses
 - The inconsistency between the cross-entropy (CE) loss used and common fairness metrics (e.g., demographic parity, DP): In lines 212–215, the authors use the CE loss to approximate group fairness metrics. A detailed analysis clarifying the relationship between CE loss and these fairness metrics is necessary. Specifically, the paper needs to rigorously demonstrate how minimizing CE loss translates to minimizing disparities in metrics like demographic parity or equalized odds. The current justification relies on an empirical observation that CE loss can serve as a proxy, but lacks a theoretical underpinning. Additionally, in Eqs. (2)–(4), the fairness losses are defined as the loss disparities between demographic groups, which requires further explanation. The reviewer recommends the authors could provide empirical evidence demonstrating how well CE loss approximates these fairness metrics in practice, or discuss any theoretical guarantees or limitations of this approximation. For example, a formal proof or a detailed analysis of the conditions under which minimizing CE loss also minimizes fairness disparities would be beneficial.


- The theoretical analysis lacks depth and originality and shows an inconsistency with the fairness loss. The theorems provided are applicable only to the cross-entropy (CE) loss case and not to fairness metrics, leading to a disconnect between the theoretical framework and the algorithms. The optimization objective includes both fairness loss and CE loss; however, the theorems do not adequately incorporate the fairness losses. The reviewer suggests that the theorems be extended to explicitly incorporate fairness metrics or that a more rigorous justification be provided for how the CE-based theorems relate to fairness in practice. This would help bridge the gap between the theoretical framework and the proposed algorithms. For instance, the theorems could be reformulated to directly address the optimization of fairness metrics, rather than relying on CE loss as a proxy. The current theoretical analysis does not provide sufficient insight into how the proposed method directly minimizes fairness disparities.


- The paper does not mention several recent studies in the related work section, which could also adjust new samples' weightings to mitigate fairness disparity. For example, active learning may be closely related to continual learning, as shown in studies like [1-4]. The authors should clarify the differences between their approach and these active learning methods, particularly in how they handle the incremental nature of continual learning. The current discussion does not adequately address the nuances of how active learning techniques, which also involve sample weighting, relate to the proposed method in the context of continual learning.

### Questions
- Why is the loss referred to as the cost function in line 241?

- The fairness definitions used in the experiments appear to differ from those presented in Section 3.2. Are these definitions consistent? If not, why?

- It is unclear what are the sample weight variables appeared in optimization problems?

### Soundness
2

### Presentation
3

### Contribution
2

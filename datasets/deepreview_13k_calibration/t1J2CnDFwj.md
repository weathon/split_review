# Enhance Multi-View Classification Through Multi-Scale Alignment and Expanded Boundary

- Decision: Accept
- Avg Score: 5.75
- Scores: 5, 5, 5, 8

## Abstract
Multi-view classification aims at unifying the data from multiple views to complementarily enhance the classification performance. Unfortunately, two major problems in multi-view data are damaging model performance. The first is feature heterogeneity, which makes it hard to fuse features from different views. Considering this, we introduce a multi-scale alignment module, including an instance-scale alignment module and a prototype-scale alignment module to mine the commonality from an inter-view perspective and an inter-class perspective respectively, jointly alleviating feature heterogeneity. The second is information redundancy which easily incurs ambiguous data to blur class boundaries and impair model generalization. Therefore, we propose a novel expanded boundary by extending the original class boundary with fuzzy set theory, which adaptively adjusts the boundary to fit ambiguous data. By integrating the expanded boundary into the prototype-scale alignment module, our model further tightens the produced representations and reduces boundary ambiguity. Additionally, compared with the original class boundary, the expanded boundary preserves more margins for classifying unseen data, which guarantees the model generalization. Extensive experiment results across various real-world datasets demonstrate the superiority of the proposed model against existing state-of-the-art methods.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The authors propose an expanded boundary using fuzzy set theory to adaptively adjust class boundaries for ambiguous data, enhancing representation tightness and reducing boundary ambiguity. This expanded boundary also preserves more margin for unseen data, improving model generalization. Experiments across diverse datasets show the model’s superiority over state-of-the-art methods.

### Strengths
1. The technique appears sound.

2. The presentation is clear and easy to follow.

3. The experimental results are sufficient to demonstrate the effectiveness of the proposed method.

### Weaknesses
1. The model includes too many loss terms, which may limit its practicality for real-world applications, since it is often hard to set the hyperparameter to balance the contributions among them in practice. Specifically, the introduction of multiple alignment losses, while theoretically sound, adds complexity to the optimization landscape. The need to carefully tune the weights for each loss term ($\alpha$, $\beta$, and temperature coefficients) to achieve optimal performance is a significant practical hurdle. The paper lacks a clear strategy for selecting these hyperparameters, and the sensitivity of the model to these parameters is not sufficiently explored.

2. Figure 4 is unclear; I strongly suggest the authors present it in 2D for better readability.  Since there are too many dimensions making it hard to conduct the parameter sensitiveness analysis. The current 3D visualization makes it difficult to discern the relationships between different parameters and their impact on the model's performance. This lack of clarity hinders a thorough understanding of the model's behavior and makes it challenging to reproduce the results. Furthermore, the absence of a detailed parameter sensitivity analysis in the main text makes it hard to assess the robustness of the proposed approach.

3. Some relevant references are missing [1][2][3], since [1] and [3] also study multi-view classification tasks and [2] focus on multi-view learning from a fuzzy view. The authors should discuss and compare with them.

### Questions
Please address the question above.

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
4

### Summary
This paper proposes a multi-scale alignment module and an expanded boundary based on fuzzy set theory to address feature heterogeneity and information redundancy in multi-view classification. The alignment module enhances feature fusion, while the expanded boundary adapts to ambiguous data, reducing boundary ambiguity and improving generalization.

### Strengths
1. The proposed MAMC model effectively addresses feature heterogeneity by employing view-specific auto-encoders and a multi-scale alignment module, which extracts common features across views, enhancing feature fusion and improving classification performance.
2. The model introduces an expanded boundary to manage information redundancy and class ambiguity, leveraging class differences to create clearer, more adaptive decision boundaries, which aids in distinguishing classes more effectively.

### Weaknesses
1. The details of the paper need further refinement. For example, in subfigures (c) and (d) of Figure 4, the axis labels should use "temperature coefficients" instead of "penalty coefficients."
2. Equation 17 represents the overall optimization objective, involving four different loss functions. Why do the penalty coefficients apply to only two of these loss functions?
3. Figure 5 in the appendix should include variance, as it is a key aspect of stability analysis.
4. There are many minor issues that need refinement. For example, the first column in Table 1 should be labeled "datasets" instead of "methods."
5. The experiments were conducted using eight 24GB 3090 GPUs, but there are still out-of-memory issues reported in Table 1. This clearly indicates that the model's complexity and computational overhead require analysis and comparison, including metrics such as runtime, MACs, FLOPs, and parameters.

### Questions
Please see weakness.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This papers addresses two issues in multi-view data: feature heterogeneity and information redundancy, by proposing a multi-view representation learning approach that enhances multi-view classification through multi-scale alignment and boundary expansion. Specifically, to address feature heterogeneity, this paper proposes a multi-scale alignment module that aligns from both instance and prototype scales, to explore commonalities from both inter-view and inter-class perspectives, thereby mitigating the issue of heterogeneity. To address information redundancy, this paper proposes a new expanded boundary method that adaptively adjusts boundaries using fuzzy set theory to handle fuzzy data. By integrating this expanded boundary with the prototype scale alignment module, the representation can be tightened and boundary ambiguity reduced, thereby enhancing the model's generalization capabilities. Experiments show that this model outperforms existing methods on multiple datasets.

### Strengths
This article utilizes fuzzy sets to propose a novel self-adaptive expanded boundary method to enhance the separability of inter-class representations and the compactness of intra-class representations in multi-view data.

### Weaknesses
1. The multi-scale alignment module proposed in this paper is an incremental approach. It is a commonly used paradigm in existing multi-view representation learning methods to enhance the discriminability and semantic consistency of representations.
2. The comparative methods in the experimental section are not comprehensive or representative enough. A thorough investigation of related work in the past three years should be conducted to demonstrate the effectiveness of this method.
3.One of the main problems addressed in this paper is feature heterogeneity, which is explained as the fusion difficulty caused by heterogeneity among multiple different data distributions. However, the proposed multi-scale alignment module does not provide an in-depth analysis of this issue or explain how it solves the problem.
4. The explanation of symbols in the paper is not clear enough, such as in Eq.(16). 
5. The experimental section lacks an analysis of model convergence.
6.The datasets have not been cited.

### Questions
Please refer to Weaknesses.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper delves into the problems in multi-view data, namely fusion difficulty caused by feature heterogeneity and boundary ambiguity caused by information redundancy. To tackle these problems, this paper proposes a novel multi-view learning model MAMC, which reduces the fusion difficulty by introducing a multi-scale alignment strategy to mine the inter-view commonality and inter-class difference, while alleviating the boundary ambiguity by proposing an expanded boundary to learn a clear decision boundary. Overall, this model is interesting and works well to address the problems.

### Strengths
- The paper structure is logical and the motivation is clear and easy to understand.

- The design of the expanded boundary is detailed, actually, it is interesting and seems simple-yet-effective.

- The authors provide the theoretical proof to explain the construction of the expanded boundary.

- The MAMC has very good performance in the classification results and visualization.

### Weaknesses
 - It would be better for the authors to provide the additional results with the general prototype in the ablation study, which makes it easier to understand the advantage of the expanded boundary. 

- The model is simple-yet-effective, however, I don’t know whether it is efficient. So the authors could provide a complexity analysis to understand the model efficiency better.

### Questions
- Though the visualization is quite good, I am confused about how they obtained the results. They should explain how to combine the multi-view features to realize t-SNE visualization, such as concatenation or other ways.

- I find the comparative models in the paper mostly deal with uncertainty. Thus, I want to know whether the proposed model can be regarded as one robust model to handle uncertainty. And what are the differences between those models and MAMC?

- Whether the authors give the wrong symbols in Figure 4? As the caption described, the symbols in (c) and (d) should be two temperature coefficients, and the authors need to check it up.

### Soundness
4

### Presentation
3

### Contribution
4

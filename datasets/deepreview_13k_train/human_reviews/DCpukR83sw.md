# Interactive Adjustment for Human Trajectory Prediction with Individual Feedback

- Decision: Accept
- Scores: 3, 6, 6, 8

## Abstract
Human trajectory prediction is fundamental for autonomous driving and service robot. The research community has studied various important aspects of this task and made remarkable progress recently. However, there is an essential perspective which is not well exploited in previous research all along, namely individual feedback. Individual feedback exists in the sequential nature of trajectory prediction, where earlier predictions of a target can be verified over time by his ground-truth trajectories to obtain feedback which provides valuable experience for subsequent predictions on the same agent. In this paper, we show such feedback can reveal the strengths and weaknesses of the model's predictions on a specific target and heuristically guide to deliver better predictions on him. We present an interactive adjustment network to effectively model and leverage the feedback. This network first exploits the feedback from previous predictions to dynamically generate an adjuster which then interactively makes appropriate adjustments to current predictions for more accurate ones. We raise a novel displacement expectation loss to train this interactive architecture. Through experiments on representative prediction methods and widely-used benchmarks, we demonstrate the great value of individual feedback and the superior effectiveness of proposed interactive adjustment network. Our code will be made publicly available.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
In this work, an online learning methodology is proposed for trajectory prediction based on the insight that ground truth observations checking past predictions (named feedback) can be collected as time goes on. To leverage this insight, the authors propose an interactive adjustment network (IAN) and evaluate its efficacy using a variety of trajectory prediction algorithms on a set of pedestrian and athlete motion datasets.

### Strengths
The idea is sound and sensible.

The writing is clear and it is easy to follow the core idea being proposed.

There are a wide variety of baseline approaches used to demonstrate the core idea.

### Weaknesses
In contrast to the claims in the paper, this work is not the first to study feedback in trajectory predictions. Accordingly, the primary weakness of this work is a lack of discussion and comparisons to prior adaptive prediction work that investigates this same idea. Notable examples (which focus on both temporal adaptation, equivalent to individual feedback, and geographic adaptation) include:
* Y. Xu, L. Wang, Y. Wang, and Y. Fu, "Adaptive trajectory prediction
via transferable GNN," in IEEE Conf. on Computer Vision and Pattern
Recognition, 2022.
* B. Ivanovic, J. Harrison, and M. Pavone, "Expanding the deployment envelope of behavior prediction via adaptive meta-learning," in IEEE Conf. on Robotics and Automation, 2023.

The experimental setup relies primarily on small-scale pedestrian-only datasets. Further, these datasets are quite old (ETH/UCY are 10-15 years old, GCS is more than 10 years old, the NBA dataset is almost 10 years old), meaning performance has largely saturated on them and it is difficult to tell if the proposed method significantly improves upon baselines. The lack of evaluation on more modern, large-scale datasets with diverse agent types and dynamics limits the generalizability of the findings. Specifically, the absence of experiments on datasets like the Waymo Open Motion Dataset or nuPlan, which feature a mix of vehicles and pedestrians, makes it hard to assess the method's performance in complex real-world scenarios.

As stated in Section 5.4, a prediction model and the IAN are _consecutive_ modules, meaning they have to run one after the other (and not simultaneously as stated in Line 523). This means that there is a 20ms overall runtime increase as a result of adding the IAN. This additional latency is a non-negligible overhead, especially in real-time applications where prediction speed is critical. The paper should more thoroughly discuss the implications of this delay and explore potential optimizations.

### Questions
The most important question: How does this approach compare to prior works on adaptive trajectory prediction? Why is IAN better or more preferable to use by practitioners?

How does this approach perform on modern large-scale datasets with multiple types of agents and varying dynamics, e.g., Waymo Open Motion Dataset, nuPlan? These datasets also have less saturated metrics which should make it easier for the IAN's performance improvements to stand out.

### Soundness
3

### Presentation
3

### Contribution
1

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposes an Interactive Adjustment Network (IAN) that leverages individual feedback from previous predictions to improve human trajectory prediction models. The idea is to use the differences between earlier predictions and actual trajectories (ground truths) to adjust future predictions for the same agent. The authors claim that their method can be applied as an external module to various existing prediction models and that it significantly boosts performance on datasets.

### Strengths
- The concept of utilizing individual feedback from previous predictions is interesting.
- The proposed method is designed to be model-agnostic and can be applied to various trajectory prediction frameworks.
- Experiments are conducted on multiple datasets and with several baseline models.

### Weaknesses
Major issues:
- The paper's biggest assumption is the fact is that IAN relies on having immediate access to the ground truth trajectories of agents to compute feedback. In real-world applications, example autonomous driving or robotics, such ground truth data is usually never available in real-time. The authors do not adequately address the practical limitations of this assumption, particularly in scenarios where sensor data is noisy or incomplete, potentially leading to inaccurate feedback and degraded performance. The reliance on perfect ground truth data significantly restricts the applicability of the proposed method in real-world settings.
- The concept of using feedback from previous predictions is not entirely new. Adaptive models and online learning techniques have long incorporated past errors to improve future predictions. The bigger issue is the lack of adequate differentiation of IAN from existing methods i.e., a thorough literature review that situates its contributions within the broader context. The paper does not clearly articulate how IAN's approach to feedback integration differs from established methods, such as Kalman filtering or recurrent neural networks with error feedback loops, which also leverage past prediction errors to refine future estimates. This lack of clear distinction makes it difficult to assess the novelty and unique contribution of IAN.
- While the authors introduced a new loss function, there is no analysis of the properties of the displacement expectation loss or proofs of convergence and stability. The absence of theoretical analysis leaves open questions about the robustness and reliability of the training process. Specifically, it is unclear whether the proposed loss function guarantees convergence to a stable solution or if it is susceptible to oscillations or divergence during training. Furthermore, the paper lacks an analysis of the loss function's sensitivity to hyperparameter choices, which is crucial for practical implementation.
- There is a lot of poorly defined notation, making it difficult to understand the proposed method fully. It would make sense to move the table 3 from the appendix (which has the notation!) to the main paper.

There are some issues with the presentation.

Writing: 
- Section 3, Trajectory Prediction (just before equation 1): \hat{Y} of "him"
- Section 4.5, "At the beginning of this paragraph" 
- Section 5.4, Last sentence: Our approach can "inference" at a high frequency
- Personal preference: please use "Figure X represents ..." (not abbreviation) instead of "Fig. X represents..." because your captions have the former. 

Images:
- The image labels for Figure 2 are too small to read -- had to Zoom 150% to read it
- Figure 2, it is hard to tell the difference between Train Path and Test Path, the arrows look very similar, please consider a different color. 
- Figure 4, 5, it is hard to see lighter colors.

### Questions
1. How do you justify the assumption that ground truth trajectories are available in real-time for computing feedback? In what practical scenarios would this be feasible?
2. How does your method differ from existing online learning approaches that adapt models based on prediction errors?
3. How does the computational cost of IAN affect inference time in real-world applications (even a small delay in prediction can go a long way)?
4. Are there experiments to isolate the effects of each component of your model? If so, please provide detailed results.
Statistical Significance: Are the reported improvements statistically significant? Can you include variance measures or confidence intervals?
5. How does your model handle agents for whom no feedback data is available?

### Soundness
3

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
In this paper, an individual feedback framework (termed IAN) for Trajectory Prediction is proposed that dynamically adjusts the confidence score conditioned on prediction consistency between prediction and GT trajectories. Through addtional feedback generator during training, a consistency score could be derived through attention in supervising the prediction condifence. Comprehensive experiment results demonstrate the effectiveness of IAN module when collaborating with a series of state-of-the-art predictors.

### Strengths
1. Novel design for trajectory prediction pipeline considering closed-loop decoding (or individual feedback). Through proposed feedback generater and adjuster model in IAN, the multi-modal prediction garners extra feedback consistency supervisions in prediction confidence.

2. Comprehensive experimental evaluations. 1) Broad improvements are reported across various datasets when integrating IAN with several SOTA motion prediction frameworks; 2) Clear comparison with other decoding strategies.

### Weaknesses
1. Unclear writings in methodology: It is partly clear to understand the feedback mechanism by Figure 2, However, by simply go through the content the reviewer could hardly understand the feedback generation process between training and testing. Hence, it is better to provide additional Algorithm part for clearer understanding.

2. Additional evaluation for the feedback. In Tab1-2, minADE/minFDE is a direct metric in mearusing the best-case similarity for multi-modal predicted trajectory. However, it is unclear whether the confidence are well-performed by the feedback enhancement. Hence, several extra results measured by Brier-minADE/FDE, MissRate, or mAP seems needed.

### Questions
1. How is the feedback being connected (with A_F for example) in Eq3-4 and Eq9-10, and being differentiated between training and testing stage?

### Soundness
3

### Presentation
2

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
This paper introduces the concept of individual feedback in trajectory prediction problems by designing an Interaction Adjustment Network (IAN). The IAN, comprising a feedback generator, an adjuster, and a filtering process, is designed to be an external module that can be seamlessly integrated with other trajectory prediction models. To ensure its adaptability, the authors have designed a displacement loss function to train the IAN. Experiments have shown the IAN's efficacy on widely adopted benchmarks for trajectory prediction.

### Strengths
Following are the strengths of this paper:
1. The introduction of individual feedback to enhance trajectory prediction by integrating agent-specific past trajectories with groundtruth is promising.
2. Evaluation of the proposal IAN network on trajectory prediction benchmarks highlights their claim.
3. As an external module, IAN can be integrated with various trajectory prediction methods.
4. The presentation of results is good.

### Weaknesses
However, this paper provides a promising way to improve the trajectory prediction method by incorporating the agent-specific past trajectories and groundtruths, here are some comments that need to be addressed
1. Since the authors introduced the individual feedback in the paper and provided the intuition, it would be good to see any theoretical justification for why it is important. Specifically, a formal analysis of how the individual feedback impacts the prediction error would strengthen the paper. Without such justification, it is difficult to assess the generalizability of the approach beyond the empirical results presented.
2. It would be good to see if the authors can address that incorporating the agent-specific previous trajectories may not lead to overfitting the base-model prediction. While the IAN is presented as an external module, the potential for overfitting to the specific patterns of individual agents needs to be carefully considered. The paper should include an analysis of how the IAN avoids memorizing agent-specific trajectories, especially when the training data for each agent is limited.
3. Another important concern is that, since the IAN is heavily dependent on the base-model prediction if there are accumulated errors in the base-model prediction, then the proposal generated from the IAN would also be spurious. What kind of risk assessment should be incorporated into the IAN? The paper should discuss the limitations of the IAN when the base model's predictions are poor, and how the IAN handles such cases. A risk assessment mechanism, such as a confidence score for the base model's predictions, could be incorporated to mitigate the propagation of errors.
4. It would be good to see if there is more explanation on the architecture of IAN, including the feature generation network, what kind of encoder architecture is used, and the rationale behind it. The paper lacks a detailed description of the IAN's architecture. Specifically, the choice of encoder architecture, the feature generation process, and the rationale behind the design choices are not well explained. This lack of detail makes it difficult to reproduce the results and understand the inner workings of the IAN.
5. Another thing that would be good is for the authors to include at least some description of the process happening in the figures to help the reader understand the figures. The figures lack sufficient explanation, making it difficult to understand the proposed method. The paper should include more detailed captions and descriptions of the processes depicted in the figures.
6. In the conclusion, the authors should include the limitations of their work and possible future directions. It would also be good to see if authors can report the failure cases. The conclusion should include a discussion of the limitations of the proposed approach, potential failure cases, and possible future research directions. This would provide a more balanced and complete view of the work.

### Questions
However, this paper provides a promising way to improve the trajectory prediction method by incorporating the agent-specific past trajectories and groundtruths, here are some comments that need to be addressed
1. Since the authors introduced the individual feedback in the paper and provided the intuition, it would be good to see any theoretical justification for why it is important.
2. It would be good to see if the authors can address that incorporating the agent-specific previous trajectories may not lead to overfitting the base-model prediction. 
3. Another important concern is that, since the IAN is heavily dependent on the base-model prediction if there are accumulated errors in the base-model prediction, then the proposal generated from the IAN would also be spurious. What kind of risk assessment should be incorporated into the IAN?
4. It would be good to see if there is more explanation on the architecture of IAN, including the feature generation network, what kind of encoder architecture is used, and the rationale behind it.
5. Another thing that would be good is for the authors to include at least some description of the process happening in the figures to help the reader understand the figures.
6. In the conclusion, the authors should include the limitations of their work and possible future directions. It would also be good to see if authors can report the failure cases.

### Soundness
3

### Presentation
3

### Contribution
3

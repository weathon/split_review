# Learning to Teach: Improving Mean Teacher in Semi-supervised Medical Image Segmentation with Dynamic Decay  Modulation

- Decision: Reject
- Avg Score: 3.67
- Scores: 3, 3, 5

## Abstract
Medical image segmentation is essential in medical diagnostics but is hindered by the scarcity of labeled three-dimensional imaging data, which requires costly expert annotations. Semi-supervised learning (SSL) addresses this limitation by utilizing large amounts of unlabeled data alongside limited labeled samples. The Mean Teacher model, a prominent SSL method, enhances performance by employing an Exponential Moving Average (EMA) of the student model to form a teacher model, where the EMA decay coefficient is critical. However, using a fixed coefficient fails to adapt to the evolving training dynamics, potentially restricting the model's effectiveness. In this paper,
we propose Meta MeanTeacher, a novel framework that integrates meta-learning to dynamically adjust the EMA decay coefficient during training. We approach proposed Dynamic Decay Modulation (DDM) module in our Meta MeanTeacher framework, which captures the representational capacities of both student and teacher models. DDM heuristically learns the optimal EMA decay coefficient by taking the losses of the student and teacher networks as inputs and updating it through pseudo-gradient descent on a meta-objective. This dynamic adjustment allows the teacher model to more effectively guide the student as training progresses.
Experiments on two datasets with different modalities, i.e., CT and MRI, show that Meta MeanTeacher consistently outperforms traditional Mean Teacher methods with fixed EMA coefficients. Furthermore, integrating Meta MeanTeacher into state-of-the-art frameworks like UA-MT, AD-MT, and PMT leads to significant performance enhancements, achieving new state-of-the-art results in semi-supervised medical image segmentation.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper presents the 'Meta Mean Teacher', an approach for semi-supervised medical image segmentation. Building on the Mean Teacher model, which leverages exponential moving average (EMA) to create a stable teacher model from a student model, this framework introduces the Dynamic Decay Modulation (DDM) module. DDM dynamically adjusts the EMA decay coefficient based on both the student and teacher losses, improving the model's adaptability during training.

### Strengths
The paper addresses semi-supervised learning in medical image segmentation with a novel meta-learning approach, introducing the Dynamic Decay Modulation (DDM) module to adjust the EMA decay coefficient dynamically. 

The paper strengthens its empirical evaluation by testing on three datasets, covering different imaging modalities.

### Weaknesses
While the paper builds on the Mean Teacher model, which is well-established in semi-supervised learning, it may lack substantial novelty as the framework mainly modifies an existing approach. Although the Dynamic Decay Modulation (DDM) module adds a new layer of adaptability, many similar extensions to Mean Teacher already exist, potentially limiting the paper's contribution to novel methodology.


The experimental scope appears limited as it only includes limited number of baseline methods, i.e. Mean Teacher variations like UAMT with UNet and VNet, models that have already been well-explored in this context. The paper’s experiments may be restricted by a limited range of labeled-to-unlabeled data ratios, which does not fully capture the model’s performance across different semi-supervised settings. Testing with a wider variety of label-scarcity scenarios would offer more robust insights into the framework's adaptability and practical applicability in real-world cases where data availability varies.

### Questions
(1) How do you ensure that comparisons are fair in semi-supervised learning scenarios? For example, I understand that in some cases, we can control the percentage of labeled and unlabeled data, such as using 5% or 10% labeled data. However, the feature distribution of labeled and unlabeled data cannot be guaranteed to be the same.


(2) The exclusive use of VNet as the backbone may limit the generalizability of the results, as it does not reflect performance across more commonly used architectures like UNet or newer ViT-based UNets.

(3) In Table 2, I observe that VNet’s performance is significantly lower than others when only 5% of data is labeled, but it is only slightly lower when 10% is labeled. Could you explain why this discrepancy occurs? Additionally, could you provide more results for cases with 20%, 50%, 80%, and 90% labeled data, if available?

(4) In table 3, why VNet outperforms UA-MT when 20% are labeled.

### Soundness
3

### Presentation
3

### Contribution
1

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper introduces the Meta Mean Teacher framework, a novel approach to improve semi-supervised medical image segmentation. Traditional Mean Teacher models use a fixed Exponential Moving Average (EMA) decay coefficient to update the teacher model, but this fixed value often limits model effectiveness. Meta Mean Teacher addresses this limitation by introducing a Dynamic Decay Modulation (DDM) module that adaptively adjusts the EMA decay coefficient based on training dynamics. This dynamic adjustment optimizes the student-teacher learning process, enabling better performance in tasks with limited labeled data.

Key contributions of this work include:

1. Adaptive EMA Decay: The DDM module optimizes the EMA decay coefficient, enhancing the model's adaptability and enabling it to capture richer training representations.
2. Plug-and-Play Architecture: Meta Mean Teacher is designed to integrate seamlessly into existing models, improving performance across various Mean Teacher-based methods.

### Strengths
1. Dynamic Adaptability: By incorporating the Dynamic Decay Modulation (DDM) module, the framework dynamically adjusts the EMA decay coefficient (α) during training. This adaptability ensures that the teacher model evolves effectively with the student model, allowing more precise guidance as training progresses. This approach addresses a common limitation in fixed-coefficient Mean Teacher models, which often fail to account for varying training dynamics.

2. Plug-and-Play Module: The Meta Mean Teacher framework is designed as a modular system, making it highly compatible with existing models based on the Mean Teacher architecture. This modularity allows easy integration into various semi-supervised frameworks like UA-MT, AD-MT, and PMT.

3. Enhanced Stability and Robustness: The framework benefits from the Mean Teacher method’s inherent stability due to EMA but improves upon it by learning an optimal decay coefficient through meta-learning techniques.

### Weaknesses
1. High Computational Overhead: The adaptive EMA adjustment via DDM introduces complexity and requires more computational resources. The dynamic adjustment process, which includes cloning and iterative updates of both teacher and student models, may not be feasible for real-time or resource-limited applications, especially when processing large 3D medical imaging data.

2. Limited Exploration of Other Adaptive Techniques: While the paper focuses on dynamically adjusting the EMA decay coefficient, other hyperparameters (like learning rates or loss weight factors) could also impact model performance in semi-supervised learning. The focus on only one parameter might restrict the overall optimization potential, as additional adjustments could further enhance the segmentation quality.

### Questions
1. On the impact of α=0.01: Why does the model show improvement when α is set to 0.01? This result seems to contradict the explanation provided in Section 3.1.

2. The use of fixed α in the ablation experiments in Section 4.3: In Section 4.3, why was the average fixed α method chosen for comparison? From Figure 1, we can see that lower α values ​​(such as 0.03, 0.05, and 0.1) significantly degrade the performance. In contrast, α of 0.97 achieves performance higher than 0.84. Doesn't this general average comparison seem a bit biased?

3. The impact of α greater than 0.5: From Table 1, we can see that when α is greater than 0.5, its impact on performance becomes less significant. Test whether randomly selected α values ​​greater than 0.5 are beneficial, thereby potentially improving the results?

4. Suspicion about the data in Section 4.4 compared with other methods: Why is your experimental setting different from that in "Alternative Diversified Teaching of Semi-Supervised Medical Image Segmentation", but most of the state-of-the-art data (including LA and Pancreas-NIH datasets) are the same as the data in that paper? Does this indicate that the data is directly borrowed?

5. The m symbol in Figure 2: What does "m" mean in Figure 2? Is this symbol redundant?

### Soundness
2

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
This paper explores the EMA decay coefficient within the MT semi-supervised framework, fully tapping into the potential of the MT framework. Additionally, it introduces a novel meta-learning strategy to dynamically find the optimal EMA decay coefficient during the training process. Experiments conducted on two medical image datasets demonstrate that this method achieves superior performance.

### Strengths
1. This paper introduces a novel meta-learning strategy to adjust the EMA decay coefficient, fully tapping into the potential of the MT semi-supervised framework.
2. This paper introduces a strategy to adjust the EMA decay coefficient to improve semi-supervised segmentation performance, which could be a meaningful contribution to this field.
3. The extensive experimental results show the effectiveness of the proposed method.

### Weaknesses
1. I have not observed many innovative aspects in the application of meta-learning to the field of semi-supervised medical image segmentation. Part of the reason for this is the clarity of the writing; it is currently unclear what significant differences exist between the proposed DDM and previous meta-learning strategies. If there are no substantial differences, then the methodological contribution of this approach appears to be quite limited.
2. Could the authors explain what potential drawbacks a fixed EMA decay coefficient might have on the MT framework, particularly in the context of medical image processing?
3. The motivation is unclear. I do not understand why a dynamic change in $\alpha$ would have a greater advantage compared to a fixed value. $\alpha$ can be understood as the weight distribution between the teacher model’s parameters and the student model’s parameters during the iterative update process, with the teacher model’s weight being overwhelmingly dominant. I question the assumption that dynamically varying $\alpha$ between 0.95 and 0.99 is necessarily better than a fixed value of 0.97. Could you provide a plot showing how $\alpha$ changes dynamically over training iterations in the experiments?
4. In Equation 2, what criteria does DDM use to derive αm? Is there a relationship between $\alpha_m$ and these two losses? For example, if the teacher model has a lower loss, should $\alpha_m$ be larger? Please explain.
5. The notation in the paper is somewhat confusing. In Equation 1, what are the differences between $\Theta_s^*$ and $\Theta_s$, and between $\Theta_s$ and $\theta_s$? Additionally, what is meant by meta data $\mathcal{D}_m$, and how does it differ from labeled data and unlabeled data? Furthermore, the $\mathcal{L}_m$ formula is missing; I suggest adding it.
6. What is the initial value of $\alpha$? Has an ablation study been conducted to verify the impact of $\alpha$?
7. The authors mention that DDM can be promoted as a plug-and-play component for different models. However, I think DDM has limitations. For instance, how would DDM be applied to commonly used pseudo-labeling methods based on CPS (Semi-Supervised Semantic Segmentation with Cross Pseudo Supervision)?

### Questions
Please refer to the weakness.

### Soundness
3

### Presentation
3

### Contribution
2

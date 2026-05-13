# GenDataAgent: On-the-fly Dataset Augmentation with Synthetic Data

- Decision: Accept
- Scores: 3, 8, 8, 6

## Abstract
Synthetic data is increasingly employed for training dataset augmentation in computer vision. However, prior works typically perform a uniform search across the entire category space, overlooking the interaction between synthetic data generation and downstream task training. Furthermore, balancing the diversity of synthetic data while ensuring it remains within the same distribution as real data (i.e., avoiding outliers) remains a significant challenge.
In this work, we propose a generative agent to augment target training datasets with synthetic data for model fine-tuning. Our agent iteratively generates relevant data on-the-fly, aligning with the target training dataset distribution. It prioritizes sampling diverse synthetic data that complements marginal training samples, with a focus on synthetic data that exhibit higher variance in gradient updates. Evaluations across diverse supervised image classification tasks demonstrate the effectiveness of our approach.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper presents an algorithm for selecting synthetic data generated from Stable Diffusion, adjusting their contribution, and modifying the generation diversity for better closed-set classification model training as the downstream application. The main hypothesis is around the introduction of downstream training signal to provide feedback to the model generation process to better guide and use generated samples for discriminative model training.

### Strengths
The intuition of guiding the sample generation process from signals or feedback from the downstream model training process makes sense. The paper has presented results of both training completely with synthetic data and using synthetic data as augmentations. And they show the proposed method outperforms baselines compared.

### Weaknesses
Lack of technical novelty. Though the motivation of the idea makes sense, my biggest concern is on the technical novelty of the proposed algorithm. The proposed design components on ensuring sample diversity, generation distribution alignment with real data distribution, and the marginal sample selection are all coming from existing literature or prior works. 

Lack of sufficient experiment results to validate the effectiveness of the proposed methods and the claims in the contributions. The contribution claims the effectiveness of the proposed method from the three aspects of marginal sample selection, sample diversity and the distribution alignment to real data distribution. However, from the ablation study, it appears that even without these proposed improvements, the classification model trained with synthetic data also show good improvements. And the improvements from the proposed claims are relatively smaller compared to the gains from directly using synthetic samples from SD without these proposed changes, as in Table 3. It then raises the question on the effectiveness of the propose method and the claimed contributions. 

Introduction of additional information from SD. In Table 1 and 2, it shows that the classification performance does increase by adding synthetic samples following the proposed method. However, it is unclear that if the gain is indeed coming from these synthetic augmentation or just distilled information from the diverse datasets which the image generator Stable Diffusion is trained over.

### Questions
Can you explain the difference of the proposed marginal sample selection algorithm to Focal loss which also adjusts the sample weights based on the difficulty of the sample indicated by the raw softmax score of the classifier being learnt.

Line 13 of algorithm1, S_f is not defined in section 3.4, pls explain.

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper introduces the on-the-fly data augmentation method. The method first selects important samples using a marginal score. It then performs caption perturbations to increase the diversity of the data. Finally, outliers are filtered out using the gradients at the initial training iterations. The experiments show that the method effectively improves the accuracy.

### Strengths
- The paper is easy to follow. 
- The paper includes clear motivation and a detailed analysis of the proposed framework. 
- The experiments show the benefit of the proposed on-the-fly data augmentation method.

### Weaknesses
The proposed method is slow --- it can be up to 350 times slower than using only real data and 2 times slower than the comparing method (Real-Fake). Although the accuracy increases, this can be a major bottleneck.

### Questions
Related to the speed issue, I assume the reason is because it's the on-the-fly method. Can the method be adapted/switched between online and offline modes based on its need? Are there other ways to improve the speed?

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper presents a novel approach for training dataset augmentation in computer vision using a generative agent, GenDataAgent. This method addresses the limitations of previous works that uniformly search across the category space and fail to consider the interaction between synthetic data generation and downstream task training. The proposed agent generates high-quality synthetic data on-the-fly, ensuring alignment with the target training dataset distribution while prioritizing diversity and relevance. Evaluations demonstrate that this approach enhances the generalization performance of downstream models fine-tuned on the augmented datasets.

### Strengths
- The introduction of GenDataAgent for on-the-fly synthetic data generation represents a significant advancement in training dataset augmentation, addressing the critical challenges of distribution alignment and sample diversity.

- The method effectively enhances the generalization performance of downstream models by prioritizing the sampling of diverse synthetic data that complements marginal training samples, which is crucial for improving model robustness.

- Unlike prior research, this work does not rely on specific distributional assumptions, making the approach more versatile and applicable to a wider range of datasets, including those with varying class distributions and limited examples.

### Weaknesses
- There exists a conflict: tailoring synthetic data generation for specific downstream tasks limits its generality, while using it for general purposes diminishes its specialty. The authors could provide further insights to clarify this issue.

- Is it necessary for synthetic data to be in-distribution? While aligning the distribution of synthetic data with the training data is important, it does not align with the distribution of the test data, particularly in out-of-distribution (OOD) scenarios. This raises the question of whether this paper focuses solely on generalization within in-distribution contexts, potentially limiting its applicability to real-world situations where test data may vary significantly. The authors may evaluate the proposed agent's capability for OOD generalization. 

- Though the on-the-fly generation of relevant data saves the storage cost and improves relevance to the task at hand, how reusable and sustainable is synthetic data?

- For marginal training samples, synthetic data that exhibit higher variance in gradient updates are specifically chosen. Does this imply that these synthetic samples are those that the current model struggles to learn effectively? If so, it suggests that these samples may be more challenging or informative, potentially indicating areas where the model's performance is weak. This focus on high-variance samples could enhance the model's robustness by addressing its limitations and improving its ability to generalize to diverse data distributions. Further clarification on this selection strategy and its implications for model training would be beneficial, e.g., discussing it with the selection criteria in active learning.

- This paper would benefit from a more comprehensive literature review. Specifically, it overlooks some closely related works, such as [a]. I recommend that the authors include a discussion of this work and its connections to their research. This will help to contextualize their contributions within the existing body of knowledge.

[a] A New Benchmark: On the Utility of Synthetic Data with Blender for Bare Supervised Learning and Downstream Domain Adaptation. CVPR, 2023.

- The authors claim that maintaining a consistent prompt format for both adapting stable diffusion and generating synthetic data ensures greater alignment between the distribution of the generated data and the target data. However, it is not entirely clear how a consistent prompt format alone guarantees this distribution alignment. I recommend that the authors provide a more detailed explanation of this relationship.

- Additionally, it would be valuable to discuss whether incorporating domain adaptation (DA) techniques, as described in [a], during the model fine-tuning process could lead to further performance improvements. Exploring this potential synergy could enhance the robustness of the findings presented in the manuscript.

### Questions
See Weaknesses.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper investigates how to leverage synthetic data generated by text-to-image generation models, such as Stable Diffusion (SD), to enhance image classification performance in terms of both accuracy and fairness. The authors propose a sampling strategy that prioritizes sample utility, which is determined by the proximity of a sample to the decision boundary, as well as in-distributional data samples, using the VoG score. By integrating a series of reasonable treatment, the proposed method achieves state-of-the-art performance across different image classification benchmarks.

### Strengths
The paper is well-written, providing clear motivations and explanations of the proposed method. The introduced metric for valuing synthetic data samples, based on their utility and proximity to the decision boundary, is reasonable. The integration of different techniques, such as perturbing text prompts to enhance diversity and ensuring alignment with the target distribution, appears well-justified and appropriate for the stated problem. The proposed method also demonstrates state-of-the-art performance across all kinds of image classification benchmarks.

### Weaknesses
The paper's critical weakness lies in its lack of novelty, as most of the techniques employed, including the VoG metric, are derived from previous works. This aspect positions the paper more as an engineering-heavy work rather than an original contribution. Specifically, the extensively discussed VoG metric appears somewhat subjective, as the choice of using gradients from epochs 10, 20, and 30 to compute the metric lacks proper justification or guidelines for other benchmarks or tasks. Moreover, while the proposed method demonstrates significant improvement over using only real data, it performs only marginally better than other synthetic augmentation methods, such as Real-Fake and Internet Explorer, while also taking much longer GPU hours. In fact, synthetic data augmentation has been extensively studied in the context of image classification, and the observed improvement may merely be a result of overfitting to those small-scale benchmarks and may not generalize to real-world or in-the-wild settings.

### Questions
I'm willing to raise the score if the following questions are well-addressed:

1. Can you also include robustness metrics, such as accuracy under common corruptions and perturbations as well as adversarial settings? Is the proposed method still better than the baselines? 
2. Would the proposed method generalize across different Text2Image generation methods, such as SD3 and Kandinsky (does not have to be the two)?
3. Would the proposed method generalize to other discriminative CV tasks such as image retrieval or object detection? 
4. Line 474, the statement that accuracy is highly correlated with the synthetic data volume seems to be contradictory with a concurrent ICLR25 submission (Mousterian: exploring the equivalence of generative and real data augmentation in classification). In that work, they state that synthetic data is more valuable when the quantity is small, yet its value diminishes quickly rather than staying correlated with accuracy. 
5. The discussion on overfitting in line 483 requires more clarity and experimental evidence to support the strong statement made. The current evidence on Pets dataset appears quite weak and insufficient.

### Soundness
3

### Presentation
3

### Contribution
2

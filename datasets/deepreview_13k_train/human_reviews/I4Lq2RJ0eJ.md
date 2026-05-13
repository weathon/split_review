# How Far Are We from True Unlearnability?

- Decision: Accept
- Scores: 6, 6, 6

## Abstract
High-quality data plays an indispensable role in the era of large models, but the use of unauthorized data for model training greatly damages the interests of data owners. To overcome this threat, several unlearnable methods have been proposed, which generate unlearnable examples (UEs) by compromising the training availability of data. Clearly, due to unknown training purpose and the powerful representation learning capabilities of existing models, these data are expected to be unlearnable for various task models, i.e., they will not help improve the model's performance.  However, unexpectedly, we find that on the multi-task dataset Taskonomy, UEs still perform well in tasks such as semantic segmentation, failing to exhibit cross-task unlearnability. This phenomenon leads us to question: How far are we from attaining truly unlearnable examples? We attempt to answer this question from the perspective of model optimization. We observe the difference of convergence process between clean models and poisoned models on a simple model using the loss landscape and find that only a part of the critical parameter optimization paths show significant differences, implying a close relationship between the loss landscape and unlearnability. Consequently, we employ the loss landscape to explain the underlying reasons for UEs and propose Sharpness-Aware Learnability (SAL) for quantifying the unlearnability of parameters based on this explanation. Furthermore, we propose an Unlearnable Distance (UD) metric to measure the unlearnability of data based on the SAL distribution of parameters in clean and poisoned models. Finally, we conduct benchmark tests on mainstream unlearnable methods using the proposed UD, aiming to promote community awareness of the capability boundaries of existing unlearnable methods. The code is available at https://github.com/MLsecurityLab/HowFarAreFromTrueUnlearnability.git.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors investigate the limitations of current unlearnable examples (UEs), which aim to protect data ownership by making data unusable for model training. They discover that UEs generated for one task (e.g., image classification) can still contribute to performance improvement in other tasks (e.g., semantic segmentation) within multi-task learning settings. To address this, they introduce the concept of Sharpness-Aware Learnability (SAL) as a new metric to measure the unlearnability of model parameters. They further propose Unlearnable Distance (UD), a metric built on SAL, to quantify the unlearnability of data. Using UD, they benchmark existing unlearnable methods, revealing the gap between current research and the goal of creating truly unlearnable examples.

### Strengths
1. Novel perspective on unlearnability: The authors explore the concept of cross-task unlearnability. They highlight the limitations of existing unlearnable methods that primarily focus on single-task scenarios, revealing their ineffectiveness in multi-task settings. 

2. Focus on the training process: Instead of relying solely on test accuracy, the authors analyze the model optimization process during training to understand how UEs impact learning. This may provide a more in-depth understanding of the unlearnability mechanism compared to previous studies that focused on post-training model performance.

3. Introduction of new metrics: The authors propose two novel metrics:

    a. Sharpness-Aware Learnability (SAL): This metric quantifies the unlearnability of parameters by considering the impact of parameter updates on the loss landscape during training. 

    b. Unlearnable Distance (UD): This metric, built on SAL, measures the overall unlearnability of data by analyzing the proportion of learnable parameters in models trained on UEs compared to models trained on clean data.

### Weaknesses
1. Limited explanation of multi-task unlearnability failure: While the authors identify the failure of existing UEs in multi-task scenarios, they provide a limited explanation for this phenomenon. They point towards the inherent difficulties of multi-task learning, specifically conflicts between different tasks, as a potential reason. However, a more detailed analysis of how these conflicts affect unlearnability is lacking. For instance, do UEs designed for one task interfere with the learning of other tasks? Or do the shared representations learned in multi-task models somehow overcome the unlearnability effect of UEs? The authors do not fully address these questions. Specifically, the mechanism by which the gradients from different tasks interact and potentially cancel out the unlearnability effect needs further investigation. It's unclear whether the UEs are simply ineffective in the shared feature space or if the multi-task learning process actively counteracts their intended effect. A more granular analysis of the gradient flow and parameter updates in multi-task settings is needed to pinpoint the exact cause of failure.

2. Limited scope of multi-task experiments: The multi-task experiments are primarily conducted on the Taskonomy dataset using only 4 tasks, which might not be representative of all multi-task learning scenarios. Exploring the effectiveness of UEs on other multi-task datasets with more diverse tasks and complexities would strengthen the claim of cross-task unlearnability failure. The Taskonomy dataset, while useful, might not capture the full spectrum of challenges present in real-world multi-task learning scenarios. For example, tasks with vastly different input modalities or output spaces could reveal different failure modes for UEs. Furthermore, the number of tasks (4) is relatively small, and it is unclear if the observed trends would hold with a larger number of tasks or more complex task relationships. The lack of experiments on more challenging multi-task datasets limits the generalizability of the findings.

3. Lack of discussion on practical implications: The authors briefly mention the need for better data protection strategies, but they do not discuss the practical implications of their findings in detail. How can the insights from this research be translated into real-world solutions for protecting data ownership? What are the potential challenges in implementing these solutions? The paper lacks a discussion on the computational overhead of generating UEs and how this might impact their practicality. Furthermore, the authors do not address the potential for adversarial attacks on UEs, which could render them ineffective. A more thorough discussion of the limitations and challenges in deploying UEs in real-world scenarios is necessary.

4. Poor visualization of figures: Some figures are not well-visualized, especially the color, linewidth and font size are not well-chosen. For example, figures 1, 2, and 4 are hard to read in the printed version. Specifically, in Figure 1, the overlapping lines make it difficult to distinguish the performance of different methods. In Figure 2, the loss landscape is not clearly visualized, and the axes are not labeled clearly. In Figure 4, the font size is too small, making it difficult to interpret the results.

### Questions
Please refer to the weakness.

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper addresses the challenges of unlearnable examples (UEs) in the context of model training, particularly highlighting their unexpected performance in multi-task Taskonomy. The authors reveal that existing unlearnable methods fail to achieve true unlearnability, prompting an exploration of the convergence differences between clean and poisoned models through loss landscape analysis. The authors introduce two key concepts: Sharpness-Aware Learnability (SAL) for quantifying parameter unlearnability, and Unlearnable Distance (UD) for measuring data unlearnability. The paper benchmarks existing methods using UD, aiming to illuminate the limitations of current approaches and guide future research towards more effective unlearnable examples.

### Strengths
- The paper is  well written and easy to follow.
- The motivation and background is explained clearly. Arguments and claims are supported by  experimental results.
- The paper provides a new perspective  to  evaluate the data unlearnability through the introduction of SAL and UD. These metrics provide valuable insights into the effectiveness of unlearnable methods and address a gap in existing evaluation methods that rely solely on post-training performance metrics

### Weaknesses
Limited Scope of Experiments: While the paper investigates unlearnability in multi-task settings, the experiments primarily focus on specific datasets, such as CIFAR-10 and CIFAR-100. It would be valuable to see results on larger and more complex datasets, like ImageNet.



### Questions
- Revisiting Figure 1, it highlights that the Error Minimization (EM) method struggles to perform effectively in multi-task scenarios. I'm curious if any recent methods have also faced similar limitations.
- I'm curious about the  generalizability of the evaluation metrics.  The experiments predominantly emphasize classification tasks; including evaluations on other downstream tasks, such as semantic segmentation, object detection, and even applications in large language models, would enhance the study's relevance and generalizability. This narrow focus may limit the applicability of the findings to other domains or unlearnable methods not considered in this research.

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
This paper addresses the concept of “unlearnable examples” (UEs), which are data samples designed to prevent unauthorized model training by impairing their usability. While current methods produce UEs effective in single-task settings, the paper reveals their limitations in multi-task scenarios. The authors explore unlearnability through the lens of model optimization and introduce Sharpness-Aware Learnability (SAL) as a metric to measure parameter unlearnability. Additionally, they propose “Unlearnable Distance” (UD) to benchmark existing UE methods across tasks.

### Strengths
1. The paper identifies a crucial gap in current unlearnable example (UE) methods by showing their limited effectiveness in multi-task scenarios.
2. The authors present SAL as a metric that evaluates the unlearnability of parameters, providing a fresh approach that goes beyond traditional test accuracy to measure how model parameters respond to UEs during training.

### Weaknesses
While the paper highlights the limitations of existing unlearnable example (UE) methods in multi-task scenarios, it does not provide solutions or adaptations to improve UE robustness across tasks. The paper's analysis of unlearnability, while introducing the SAL metric, does not delve into the specific mechanisms by which multi-task learning exacerbates the limitations of current UEs. It remains unclear how the proposed SAL and UD metrics can be directly leveraged to design more robust UEs for multi-task settings. The paper also lacks a discussion on the computational overhead associated with calculating SAL and UD, especially in the context of large-scale multi-task models, which could be a practical concern.

### Questions
Given the identified limitations of existing unlearnable examples (UEs) in multi-task scenarios, could SAL and UD metrics be used to improve UE robustness across diverse tasks?

### Soundness
3

### Presentation
3

### Contribution
3

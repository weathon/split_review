# Selective Label Enhancement Learning for Test-Time Adaptation

- Decision: Accept
- Scores: 6, 8, 6, 6, 6

## Abstract
Test-time adaptation (TTA) aims to adapt a pre-trained model to the target domain using only unlabeled test samples. Most existing TTA approaches rely on definite pseudo-labels, inevitably introducing false labels and failing to capture uncertainty for each test sample. This prevents pseudo-labels from being flexibly refined as the model adapts during training, limiting their potential for performance improvement. To address this, we propose the Progressive Adaptation with Selective Label Enhancement (PASLE) framework. Instead of definite labels, PASLE assigns candidate pseudo-label sets to uncertain ones via selective label enhancement. Specifically, PASLE partitions data into confident/uncertain subsets, assigning one-hot labels to confident samples and candidate sets to uncertain ones. The model progressively trains on certain/uncertain pseudo-labeled data while dynamically refining uncertain pseudo-labels, leveraging increasing target adaptation monitored throughout training. Experiments on various benchmark datasets validate the effectiveness of the proposed approach.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces a new pseudo-learning algorithm that combines one-hot label learning and candidate label learning approaches. Each learning paradigm is conducted on its respective sample set, referred to as the certain set for one-hot label learning and the uncertain set for candidate learning. The key distinction from other pseudo-label learning papers is that the authors propose a theoretical guarantee to ensure that the selected labels in the pseudo-set will correspond to the ground truth if certain conditions are met (Proposition 1). In the initial learning stages, the model focuses more on candidate set learning and gradually shifts toward minimizing the one-hot label loss as it updates more on target samples. The authors provide a theory indicating that the generalization bound becomes tighter as more target samples are incorporated. Experimental results demonstrate the algorithm's performance compared to other TTA learning methods.

### Strengths
1. The proposed method is supported with a theory guarantee.
2. The experiment is diverse datasets, which confirm the effectiveness of the proposed methods.

### Weaknesses
The reviewer's main concern is the novelty of the proposed approach: adapting pseudo-learning and candidate learning is already popular in TTA and domain adaptation, as the authors discussed in Section 2. The main novelty here comes from Proposition 1, where the authors propose to ensure the correctness of pseudo labels under specific assumptions. The condition is that the learned weight and the optimal one need to be close enough (the closeness is measured by the difference in the probability of each class in the input samples, and $\tau(r)$ is the threshold). The selected pseudo labels are considered true when this condition is met. However, how can we ensure that this condition is always satisfied? If the reviewers understand correctly, this condition is based on the threshold $\tau(r)$, which is initialized to 1 and then gradually reduced to a specific value. When $\tau(r)$ is smaller than 1, how can we ensure that the distance between the learned models and the optimal one is smaller than this threshold? This is a critical point, as the entire theoretical guarantee hinges on this condition, and the paper does not provide sufficient justification for how this condition is reliably met in practice. The gradual reduction of $\tau(r)$ seems like a heuristic without a strong theoretical basis, and it's unclear how this reduction is linked to the actual convergence of the learned model towards the optimal one. Furthermore, the paper lacks a clear explanation of how the threshold $\tau(r)$ is chosen and updated, and how sensitive the performance is to the choice of this threshold. Without a more rigorous justification, the theoretical guarantee appears to be based on an assumption that may not hold in real-world scenarios.

### Questions
Please refer to the Weakness.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper studies Test-time adaptation (TTA), which aims to adapt a pre-trained model to the target domain using only unlabeled test samples. The authors proposed a new TTA framework, which assigns candidate pseudo-label sets to uncertain ones via selective label enhancement. The model is progressively trained on certain and uncertain pseudo-labeled data while dynamically refining uncertain pseudo-labels, leveraging increasing target adaptation monitored throughout training. Experiments on various benchmark datasets validate the effectiveness of the proposed approach.

### Strengths
- Instead of assigning definite pseudo-labels to test samples, candidate pseudo-label sets are assigned to uncertain ones via selective label enhancement.
- The proposed method partitions test samples into confident and uncertain subsets based on the model’s predictive confidence scores, with confident samples receiving one-hot pseudo-labels, and uncertain samples being assigned candidate pseudo-label sets
- The theory establishes a generalization bound for TTA that by incorporating a greater number of target domain samples with effective supervision, a tighter generalization bound can be achieved.

### Weaknesses
 - In the proposed method, the authors need to provide more details about the reduced threshold to improve the reliability of pseudo labels. 
- Why use image corruption datasets to validate the effectiveness of the proposed method? 15 types of common image corruptions should be shown clearly.
- This paper uses a vanilla variant that all samples annotated with candidate pseudo-labels sets excluded from model updates to demonstrate the effectiveness of the candidate pseudo-labels sets of the proposed method. More detests could be added in this ablation experiments.

### Questions
- In the proposed method, why the authors reduced to improve the reduced threshold could improve the reliability of pseudo labels.  
- In the experiments, why did the authors only adopt online test-time adaptation approaches as the baselines?

### Soundness
3

### Presentation
4

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
The problem studied in this paper is the conventional test-time adaptation. When assigning pseudo-labels to test samples, the paper assigns one label to samples with high confidence, while assigning a candidate set of labels to less confident samples. It uses a buffer to store samples that could not be labeled, allowing the model to attempt labeling them in subsequent batches. Finally, the model is updated by using cross-entropy with the one-hot encoded pseudo-labels. The effectiveness of the method is validated across multiple datasets.

### Strengths
1.	The writing of this paper is clear, and both the problem definition and the method description are well articulated.
2.	The motivation behind the proposed label enhancement method is reasonable, and there is substantial theoretical analysis provided.
3.	The experiments in the paper are relatively thorough, demonstrating the superiority of the proposed method.

### Weaknesses
1.	Despite the relatively comprehensive theoretical analysis, the design of the method in this paper is overly simplistic. Similar approaches using candidate pseudo-label sets have long existed in the field of semi-supervised learning.
2.	The maintenance of this buffer seems somewhat unfair. If a sample’s label remains undecided for an extended period, it will be repeatedly seen by the model in subsequent iterations. Although the buffer size imposes some constraints, the repeated processing of test samples could still introduce bias. Additionally, maintaining a buffer incurs significant overhead. If the buffer becomes too large, the number of samples to be predicted in each batch will be dictated more by the buffer size than by the batch size itself.

### Questions
1.	Since there are many approaches for creating pseudo-label candidate sets, has the paper compared its method with other approaches for selecting pseudo-label candidates? Does this method have any unique advantages specifically for the test-time adaptation (TTA) task? Or is it also applicable to semi-supervised or unsupervised tasks?
2.	What is the buffer size used in the experiments? Was there any ablation study conducted on the buffer size? If the buffer were removed, would this method still be effective?
3.	In the experiment section, why do ERM and T3A perform so poorly on CIFAR10-C and CIFAR100-C? In the original papers and subsequent TTA studies, their performance was not as weak.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This article proposes a method for addressing the TTA problem by dividing confident samples from uncertain samples and progressively updating pseudo-labels, alleviating errors caused by unconfident pseudo-labels in TTA scenarios. The article provides a systematic and comprehensive theoretical generalization error bound and validates its effectiveness on multiple benchmark datasets.

### Strengths
TTA is a critical research area for machine learning models to adapt to distribution shifts in real-world scenarios, particularly with wide applications in fields such as autonomous driving and medical image analysis. This article enhances model performance on TTA issues by dynamically adjusting pseudo-labels and capturing their uncertainties. Additionally, the detailed derivation of the generalization error bound in the article offers theoretical guarantees.

### Weaknesses
The paper lacks sufficient persuasive experimental evidence, suggesting the need to include relevant ablation studies, discussions on time overhead, and the rationale behind experimental settings. The novelty of the paper is not distinctly highlighted, requiring a more detailed discussion of the differences from related methods. The theoretical guidance is relatively weak; exploring the quantification of pseudo-label errors could strengthen the paper.

The main concerns are as follows:
1. The novelty of this paper should be emphasized more clearly. From the motivation perspective, dividing confident and non-confident samples and applying progressive training is a fairly conventional approach. Similar ideas have been extensively used in domain adaptation (DA) problems, and several papers in TTA focus on pseudo-labeling. The authors should pay more attention to these closely related works to highlight the novelty of this paper better.
2. The generalization error bound provided is a little general and offers limited guidance for the current problem. Based on the motivation of the paper, if the so-called more effective supervised information can be quantified? If pseudo-label error terms or confidence levels could be incorporated, it would help reveal how the label-generation process impacts generalization performance, thereby offering more practical insights. Additionally, how is the divergence term in the bound reduced in this paper? How does it influence pseudo-labeling and progressive adaptation?
3. Regarding the experimental setup, the datasets used in this paper differ from those employed in previous methods. The rationale for these choices should be explained in detail. Furthermore, for certain methods with the same settings like PROGRAM, why do the results differ from the original paper when using the same benchmark and backbone? Could it be due to different settings or other reasons? This should be clarified in the paper, as such vague experimental setups and comparisons make it difficult for readers to accurately assess the actual performance of the method.
4. The paper lacks ablation studies to evaluate the effectiveness of each module. Additionally, since the proposed method is an online model, time efficiency is an important metric that should be discussed, especially considering the additional computational overhead introduced by the approach.
5. I am also curious about the sensitivity of the threshold selection strategy. It doesn’t seem highly sensitive, but how does it perform over a broader parameter range or with different thresholding strategies? This could be a point worth discussing in the paper.

### Questions
The main concerns are as follows:
1. The novelty of this paper should be emphasized more clearly. From the motivation perspective, dividing confident and non-confident samples and applying progressive training is a fairly conventional approach. Similar ideas have been extensively used in domain adaptation (DA) problems, and several papers in TTA focus on pseudo-labeling. The authors should pay more attention to these closely related works to highlight the novelty of this paper better.
2. The generalization error bound provided is a little general and offers limited guidance for the current problem. Based on the motivation of the paper, if the so-called more effective supervised information can be quantified? If pseudo-label error terms or confidence levels could be incorporated, it would help reveal how the label-generation process impacts generalization performance, thereby offering more practical insights. Additionally, how is the divergence term in the bound reduced in this paper? How does it influence pseudo-labeling and progressive adaptation?
3. Regarding the experimental setup, the datasets used in this paper differ from those employed in previous methods. The rationale for these choices should be explained in detail. Furthermore, for certain methods with the same settings like PROGRAM, why do the results differ from the original paper when using the same benchmark and backbone? Could it be due to different settings or other reasons? This should be clarified in the paper, as such vague experimental setups and comparisons make it difficult for readers to accurately assess the actual performance of the method.
4. The paper lacks ablation studies to evaluate the effectiveness of each module. Additionally, since the proposed method is an online model, time efficiency is an important metric that should be discussed, especially considering the additional computational overhead introduced by the approach.
5. I am also curious about the sensitivity of the threshold selection strategy. It doesn’t seem highly sensitive, but how does it perform over a broader parameter range or with different thresholding strategies? This could be a point worth discussing in the paper.

If the authors can adequately respond to these concerns, I would consider increasing my score.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces the Progressive Adaptation with Selective Label Enhancement (PASLE) framework for test-time adaptation (TTA). Unlike traditional methods that assign definite pseudo-labels, PASLE assigns candidate pseudo-label sets to uncertain test samples while providing one-hot labels to confident samples. This approach allows the model to adapt progressively, refining the uncertain pseudo-labels based on the model's evolving understanding of the target domain.

### Strengths
1. PASLE effectively partitions test samples into confident and uncertain subsets, improving labeling accuracy for uncertain samples.

2. The model is trained iteratively on both certain and uncertain pseudo-labeled data, enhancing adaptation capabilities over time.

3. The paper establishes a generalization bound that suggests increased supervision from target domain samples can lead to improved model performance.

### Weaknesses
1. I am confused about some notations in theorem 1, what is the specific meaning of d_{h, H}(S,  T)? It seems that d_{h, H}(S,  T) is a constant with your algorithm. Does theorem 1 show the superiority of your algorithm because there is always a constant gap between the \epsilon_T(\hat{h}) and \epsilon_T (h_T^*)?

2. Whether using the two hyper-parameter to control the iteration is reasonable in equation 9? Since different datasets have different parameters and there is no prior knowledge to guide us in choosing suitable parameters, making hard to achieve the best results

3. More experiments about the sensitivity of the τ_start, τ_end, and batch size on other datasets are expected to be seen.

### Questions
See weakness

### Soundness
3

### Presentation
3

### Contribution
2

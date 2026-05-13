# ABAS-RAL: Adaptive BAtch Size using Reinforced Active Learning

- Decision: Reject
- Scores: 3, 3, 3, 6

## Abstract
Active learning reduces annotation costs by selecting the most informative samples, however fixed batch sizes used in traditional methods often lead to inefficient use of resources. We propose Adaptive BAtch Size using Reinforced Active Learning, a novel approach that dynamically adjusts batch sizes based on model uncertainty and performance. By framing the annotation process as a Markov Decision Process, the proposed method employs reinforcement learning to optimize batch size selection, using two distinct policies: one targeting precision and budget, and the other for adapting the batch size based on learning progress. The proposed method is evaluated on both CIFAR-10, CIFAR-100 and MNIST datasets. The performance is measured across multiple metrics, including precision, accuracy, recall, F1-score, and annotation budget. Experimental results demonstrate that the proposed method consistently reduces annotation costs while maintaining or improving performance compared to fixed-batch Active Learning methods, achieving higher sample selection efficiency without compromising model quality.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper proposes an active learning framework that uses reinforcement learning to dynamically adjust batch size. The aim is to address the limitations of fixed batch size for model adaptation and resource utilization optimization. Comparing the active learning methods with fixed batch size on three datasets, CIFAR-10, CIFAR-100 and MNIST, the proposed method is verified to be effective in reducing the labeling cost while maintaining or improving the performance.

### Strengths
Comparing the active learning methods with fixed batch size on three datasets, CIFAR-10, CIFAR-100 and MNIST, the proposed method is verified to be effective in reducing the labeling cost while maintaining or improving the performance.

### Weaknesses
1. Optimized learning is supposed to be a common advantage of active learning methods, which is less convincing as a contribution of this paper. 
2. This paper only compares with the random sample selection method and fixed batch size methods, but does not compare with other methods that dynamically adjust the batch size.

### Questions
1. There is a lack of specificity about the limitations of the previous work, especially the past approach to dynamically adjusting batch size. So that it is hard to tell what is the difference between the approach proposed and the previous one. 
2. This paper emphasizes dual policy design, but although the two reward policies appear later, it does not explain how they are combined and why to do that.

### Soundness
1

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper introduces Reinforcement Learning (RL) to dynamically adjust the batch size for data selection during active learning, aiming to reduce annotation costs and improve target model performance. Specifically, the margin score of an unlabeled subset is used as the state for a DQN, which selects the batch size as action to guide data selection. The classifier is trained with the newly labeled dataset, and the reward for DQN learning is calculated based on the improvement in model precision per annotation unit. Experimental results show that the proposed ABAS-RAL achieves better results with lower annotation costs compared to fixed-batch size active learning methods.

### Strengths
Applying RL to enhance active learning is an interesting topic, and it is a novel idea to adjust batch size of data selection with RL to reduce annotation cost.

### Weaknesses
**Proposed Method**
1. The presentation of the method is unclear. Figure 1 shows the RL decision process during active learning, but how the warm-start episode, BatchAgent training, and active learning are organized is not explained. If the DQN is only trained once before active learning, the policy might not generalize well to the unlabeled dataset, as active learning typically assumes the labeled dataset is much smaller than the unlabeled dataset [1]. On the other hand, if the DQN is trained repeatedly during active learning, it could be time-consuming. A flowchart or pseudocode showing the general framework of DQN training and active learning could improve the presentation.

**Experiment.**
1. The experimental setup is unclear. If I understand correctly, 80\% of the dataset is used for DQN or classifier training, as annotation labels are required for both warm-start and DQN training, leaving only 20% of the dataset as unlabeled for active learning. This setup does not align with the usual active learning scenario.

2. ResNet50 is only trained for 10 epochs on each dataset, which may not be sufficient for convergence. In Figure 5 of [1], ResNet18 achieves around 70\% accuracy on CIFAR-10 using 5,000 samples, even with random sampling. However, Table 1 of this paper shows only 44\% accuracy with a 50\% budget (approximately 5,000 samples). Please explain the performance gap between Table 1 and [1].

3. The experiments are insufficient to evaluate the proposed method. While DQN training could be computationally expensive, the paper does not discuss its time complexity. Additionally, the three benchmarks used are relatively simple, with consistently clean annotations and images. I recommend the authors consider using more complex datasets for further evaluation, such as ImageNet or Mini-ImageNet.

[1] Zhan, Xueying, et al. "A comparative survey of deep active learning." arXiv preprint arXiv:2203.13450 (2022).

### Questions
I have several questions regarding the paper representation and experiments:

1. The paper claims a contribution of Dual-Policy Design. From my understanding, the only RL agent introduced is for choosing batch size. Please explain which RL agent contributes to manage precision and budget? And how this differs from simply choosing batch size?

2. The proposed framework should be general for any data sampling method. Why is only the simple uncertainty-based method considered? Furthermore, it is unclear whether the proposed method could bring advantages to more recent data selection methods (e.g., selecting data with approaches other than uncertainty scores), such as LossPrediction [2] or uncertainty-diversity mixed methods.

[2] Yoo, Donggeun, and In So Kweon. "Learning loss for active learning." Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2019.

3. For the RL setting, does the state contain only the margin score or both the margin score and the data? If only the margin score is considered, the policy might not generalize well to the unlabeled dataset, as it does not learn the feature representation of the data. Please clarify exactly what information is included in the state representation and what information is included in action representation. Moreover, please explain why the RL agent trained on labeled dataset is expected to be general in unlabeled dataset.

4. DQN training is an important part of the method. I recommend that the authors include details of the Q-network architecture and the RL training curve in the experiment section. Additionally, an active learning curve, like Figure 5 in [1], would be valuable for representing active learning performance and could help clarify the contributions.

**Minor Comments**

1. In algorithm 1, is $b$ a fixed value or a randomly selected batch size? And how $L$ is updated should be included.
2. In algorithm 2, line 10, what's the meaning of "fill batch action"? Line 6-9 already select $(X_t, Y_t)$ as the new labeled set.
3. Markov decision process should be formally defined in Section 3.1.

### Soundness
1

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper presents a reinforced active learning approach ABAS-RAL that dynamically adjusts batch sizes in active learning through reinforcement learning (RL) to enhance model efficiency and performance. By framing active learning as a Markov Decision Process (MDP), the method utilizes a deep Q-network (DQN) to optimize batch sizes. The authors evaluate the proposed approach with experiments on three datasets: CIFAR-10, CIFAR-100, and MNIST.

### Strengths
1. The paper makes an interesting attempt to integrate reinforcement learning into active learning by dynamically controlling batch sizes, aiming to make the annotation process more efficient. This approach has the potential to optimize the trade-off between labeling costs and model performance, which is critical in resource-constrained settings.
 
2. The idea of balancing annotation costs with model performance in active learning is an important direction, especially as datasets grow larger and labeling costs increase. 

3. The authors have done well to provide a clear flowchart (Figure 1) and two algorithms summarizing the training process, which help clarify the step-by-step execution of the model.

### Weaknesses
* I’m not an expert in reinforcement learning, but it seems to me that the warm-start episode process incurs a significant time cost, as it necessitates extensive model retraining. I suggest the author to provide the time complexity and running time in the experiments to validate this cost is manageable.
  

* The experiments are not very solid in my opinion:
   1. Based on my understanding, the experiments are designed to terminate once they achieve a specific Target Precision or exhaust the Target Budget, both of which are determined solely by the warm-start episodes of the proposed method. Consequently, I believe that this Target Precision and Budget offer a distinct advantage to the proposed method, as they are derived from the same reinforcement learning rewards within a similar RL framework. I recommend that the authors conduct additional experiments to demonstrate that ABAS-RAL achieves the precision/budget frontier.
  2. The experiments only compared ABAS-RAL with Entropy Sampling, Uncertainty Sampling, and fixed-batch active learning method ALFA-Mix. I believe the adaptive batch size approaches discussed in Section 2.3 should also be included, as adjusting the batch size is a major contribution in this paper.
  3. In my opinion, the experiments in Section 4.4 do not provide further validation for ABAS-RAL compared with Section 4.3. 
  

* In my personal opinion, this paper is not well-written and organized, resulting in a relatively poor presentation:  
   1. The proposed method heavily relies on Markov Decision Process (MDP) and the deep Q-network (DQN), but the manuscript does not provide sufficient discussion on these topics, making the Section 3 difficult to understand.
  2. The name of Section 3 is "ADAPTIVE BATCH SIZE SELECTION USING RL", but it contains full training process including precision and budget with selection, optimal batch size selection, the overall training procedure and even the implementation details for DQN, which if very confusing for the reader to understand the relationship between different sections.
  3. The figures and tables are embedded within the text, which makes the information feel scattered.
  4. There are too many (nested) bullet points in the manuscript, resulting in a lot of blank space that could be utilized for important information, such as the discussion on MDP and DQN.
  5.The figures are inadequately captioned, and the legend in Figure 3 is barely readable.
  6. I don't understand why the authors use an independent subsection for comparing ABAS-RAL with random sampling, instead of merging random sampling with other active learning methods.
  7. Some abbreviations are used before the full name are mentioned in the manuscript, for example MDP and AB-EMCM.
  8. The reference format is not uniform. Besides, there is one reference [1] with dead link, and I can only find one abstract page for this paper.

[1] Xaolin Chun. Active learning with reinforcement learning for data-efficient classification. Available:
https://osf.io/preprints/osf/qj94x., 2023.

### Questions
* Questions: 
   1. I fail to see the why Figure 2 reveals "the model’s preference for certain sizes that it has learned to associate with higher expected returns for CIFAR-10, CIFAR-100 and MNIST," as the figure contains no information about expected returns or model performance. May I ask the authors to elaborate on this?
   2. Similarly, can the authors explain how Figure 3 shows how DQN agent optimizes learning through budget-efficient decisions?

* The current manuscript is difficult to read, epically for readers not familiar with MDP and DQN. I suggest the authors to revise the presentation of this paper and adding more experiments to validate the efficacy of ABAS-RAL across different target precision and budgets.

### Soundness
2

### Presentation
1

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
They propose Adaptive BAtch Size using Reinforced Active Learning, a novel approach that dynamically adjusts batch sizes based on model uncertainty and performance. By framing the annotation process as a Markov Decision Process, the proposed method employs reinforcement learning to optimize batch size selection, using two distinct policies: one targeting precision and budget, and the other for adapting the batch size based on learning progress.

### Strengths
1. The paper writing is good. 
2. The leverage RL to adaptively adjust batch size to achieve better usage of resources. 
3. The experimental analysis is enough.

### Weaknesses
1. The datasets used in experiment are limited. The scale of dataset is small, could you use other datasets, such as SUN, Places to enhance the evaluation ?
2. The motivation is not so clear. Why is the fixed batch size harmful to resource usage ?
3. The alternative of RL algorithm is not discussed, such as PPO, A3C?

### Questions
see the weakness:

1. Could you try more datasets ?
2. Why is the fixed batch size harmful to resource usage?
3. Do you try other RL algorithms?

### Soundness
3

### Presentation
3

### Contribution
3

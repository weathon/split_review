# Boosting Backdoor Attack with A Learnable Poisoning Sample Selection Strategy

- Decision: Reject
- Avg Score: 5.50
- Scores: 6, 6, 5, 5

## Abstract
Data-poisoning based backdoor attacks aim to insert backdoor into models by manipulating training datasets without controlling the training process of the target model.
Existing attack methods mainly focus on designing triggers or fusion strategies between triggers and benign samples. However, they often randomly select samples to be poisoned, disregarding the varying importance of each poisoning sample in terms of backdoor injection.
A recent selection strategy filters a fixed-size poisoning sample pool by recording forgetting events, but it fails to consider the remaining samples outside the pool from a global perspective. Moreover, computing forgetting events requires significant additional computing resources. 
Therefore, how to efficiently and effectively select poisoning samples from the entire dataset is an urgent problem in backdoor attacks.
To address it, firstly, we introduce a poisoning mask into the regular backdoor training loss. 
We suppose that a backdoored model training with hard poisoning samples has a more backdoor effect on easy ones, which can be implemented by hindering the normal training process (\ie, maximizing loss \wrt mask). 
To further integrate it with normal training process, we then propose a learnable poisoning sample selection strategy to learn the mask together with the model parameters through a min-max optimization.
Specifically, the outer loop aims to achieve the backdoor attack goal by minimizing the loss based on the selected samples, while the inner loop selects hard poisoning samples that impede this goal by maximizing the loss.
After several rounds of adversarial training, we finally select effective poisoning samples with high contribution.
Extensive experiments on benchmark datasets demonstrate the effectiveness and efficiency of our approach in boosting backdoor attack performance.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper addresses the inefficiency in existing data-poisoning based backdoor attacks which arbitrarily select samples from a benign dataset to poison, overlooking the varying significance of different samples.

The paper proposes a Learnable Poisoning sample Selection (LPS) strategy. The strategy employs a min-max optimization approach to understand which samples are most crucial for poisoning.

The paper sets up a two-player adversarial game: The inner optimization focuses on maximizing the loss concerning the mask, to pinpoint hard-to-poison samples. The outer optimization aims to minimize the loss with respect to the model's weight, to train the surrogate model.
Through multiple iterations of this adversarial training, the system selects samples that have a higher contribution to the poisoning process.

Comprehensive experiments on established datasets are conducted. Results showcase that the LPS strategy significantly enhances the efficiency and effectiveness of several data-poisoning based backdoor attacks.

### Strengths
- The paper proposes a novel approach to select samples for poisoning. The approach is intuitive and effective.
- The paper provides a comprehensive evaluation and solution proof.

### Weaknesses
 - The paper proposes a novel approach to select samples for poisoning. The approach is intuitive and effective.
- The paper provides a comprehensive evaluation and solution proof.

 - The problem makes some sense to me, but I am not sure how practical it is. A practical scenario will better motivate the problem.

### Questions
1. What is the practical scenario that the proposed boosted attack can be used in?

2. What is the scalability of the proposed attack? For example, the ImageNet has 1000 classes. Is the inner maximization still effective?

3. Some term usages are confusing. For example, under the context of backdoor attack, the term 'm' mask usually refers to the mask of trigger. However, in this paper, the term 'm' mask refers to the mask of sample selection. It would be better to use a different term to avoid confusion. Another example, in page 3, 'K' refers to class numbers. But Section 6 says 'K' is epoch numbers. It would be better to clarify such inconsistency.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors present a sample selection method for data poisoning aimed at enhancing backdoor attacks. A min-max optimization technique is employed to learn a poisoning mask for selecting the appropriate samples.

### Strengths
Pros:
- The manuscript is well-organized and easy to follow.
- Although the idea of sample selection for poisoning is conceptually similar to the FUS method, the two approaches diverge in their perspectives. While FUS focuses on local optimization, the proposed method aims for global sample selection.
- The empirical results are robust and substantiate the paper's claims effectively.

### Weaknesses
Cons:
- The code for replication is not provided, limiting the paper's reproducibility.
- The significant training loss gap between poisoned and clean samples might make the attack easily detectable by potential victims.
- Ethic statement is missing.

### Questions
- Does the threshold "T" vary across different datasets and model architectures?
- Is the proposed approach effective for the combination of CNN-based surrogate models and attention-based target models?
- Could the authors clarify why the method underperforms when the poisoning rate is low?
- For the ablation study, could the authors provide results of LPS\PC?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper, the authors study the data-poisoning-based backdoor attack. They propose to select the hard backdoor samples with the larger training loss on the surrogate model and formulate it as a min-max optimization problem. Extensive experiments show that it's better than the random selection and existing baseline.

### Strengths
1. It's an interesting idea to exploit hard examples to inject backdoors.
2. Experiments show it can improve existing backdoor attacks.
3. Code is provided.

### Weaknesses
 1. It seems not robust against existing defenses according to Table 4. Although it improves the robustness of existing attacks, it's still defeated by existing defenses.
2. Some other attack and defense methods may be evaluated as well, such as [FTrojan](https://dl.acm.org/doi/abs/10.1007/978-3-031-19778-9_23), [ABS](https://dl.acm.org/doi/10.1145/3319535.3363216), [Unicorn](https://arxiv.org/abs/2304.02786).
3. Because it selects training samples with larger losses, it may be easily detected by scanning the dataset.
4. It would be better to show how to formulate the strategy for all-to-all and clean labels in the appendix.
5. It's good to show the performance with different poisoning rates. However, in the tables, most of the ASRs are lower than 90%. That means they are all unsuccessful attacks and not that useful. One may want to show a different ratio range. Furthermore, the detection accuracy in Table 2 shows that the backdoor is very easy to detect, which harms the attack strength of the proposed method.

### Questions
1. Can it be detected by scanning the dataset and selecting the outliers with respect to the training loss?
2. How does the robustness look like if the ASRs are above 90%? Currently, most of the ASRs in Table 4 are very low.
3. Are the losses for the selected samples aligned well on the surrogate model and the target model? That is if the target model also considers them as hard examples. Also, how does the loss change for those hard backdoor samples? Because existing research shows the backdoor features are usually easier to learn and thus have smaller losses.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper points out a common weakness of most existing backdoor attacks, which is randomly choosing samples from the benign dataset to poison without considering how important different samples are. Instead of random selection, this paper proposes a novel strategy to choose poisoned data more efficiently by formulating it as a min-max optimization problem, called learnable poisoning sample selection strategy (LPS). Extensive experiments show that this strategy can improve data poisoning attacks with low poisoning rates.

### Strengths
1. The idea of improving backdoor attacks' efficiency by having better sample selection to inject backdoors is intriguing. 
2. The proposed method is quite interesting. By effectively choosing highly influential poisoned samples, it allows different types of backdoor attack to reach high ASRs with very few number of poisoned samples. It can also overcome the limitations of previous related work (FUS).
3. The paper includes vastly extensive experiments to show the effectiveness of the proposed method.

### Weaknesses
1. I find the results of this method with SSBA are quite underwhelming: in most experiments with SSBA, LPS could not reach high ASRs and seem to not have much improvement compared to the baselines. Therefore, I am not sure about LPS's flexibility, i.e., whether it can work with any type of backdoor trigger. Specifically, the paper lacks a thorough analysis of why LPS struggles with SSBA, especially given that SSBA uses a more complex trigger generation mechanism compared to BadNets or Blended attacks. The limited improvement raises concerns about the general applicability of LPS across different trigger types and complexities.
2. Although there are experiments with different model architectures for the surrogate model, only ResNet is used for the target model. In the paper's settings, the adversary have full control of the process of generating poisoned samples but no control in the victim model's training procedure, so I think it would make more sense if there were experiments with different victim model's architectures. This is a significant limitation because the effectiveness of backdoor attacks can vary greatly depending on the target model's architecture. The absence of experiments with diverse target models, such as transformer-based networks, makes it difficult to assess the robustness of LPS in real-world scenarios where the victim model is not known beforehand.
3. The experimental results of LPS's resistance against backdoor defenses are quite unsatisfying: in the cases of FP, ABL, NAD, and I-BAU, the ASRs are greatly degraded and/or have merely limited improvement compared to other baselines.  Also, there are experiments with 6 backdoor defenses, but none of them are data filtering defense, such as [1], [2], [3], [4]. Since the adversary in this paper acts as data provider, I think there should be also evaluations with data filtering defenses. The lack of evaluation against data filtering defenses is a crucial oversight. Since the adversary controls the data, defenses that focus on identifying and removing poisoned samples are highly relevant. The paper should include experiments with defenses like activation clustering, spectral analysis, robust statistics, and frequency-based methods to provide a comprehensive assessment of LPS's robustness.

### Questions
1. Could the authors provide any insights/explanations for LPS's low performances with SSBA? Could LPS work with any attack method, or the adversary should carefully choose a suitable type of trigger? 
2. Regarding my concerns about victim model's architecture and data filtering defenses, I would recommend adding aforementioned experiments.
3. All datasets used in this work have relatively low resolution. Could this method also work with high resolution datasets, such as CelebA, PubFig, ImageNet?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

# Bi-perspective Splitting Defense: Achieving Clean-Data-Free Backdoor Security

- Decision: Reject
- Scores: 6, 6, 6, 3, 6

## Abstract
Backdoor attacks have seriously threatened deep neural networks (DNNs) by embedding concealed vulnerabilities through data poisoning. To counteract these attacks, training benign models from poisoned data garnered considerable interest from researchers. High-performing defenses often rely on additional clean subsets, which is untenable due to increasing privacy concerns and data scarcity. In the absence of clean subsets, defenders resort to complex feature extraction and analysis, resulting in excessive overhead and compromised performance. In the face of these challenges, we identify the key lies in sufficient utilization of the easier-to-obtain target labels and excavation of clean hard samples. In this work, we propose a Bi-perspective Splitting Defense (BSD). BSD splits the dataset using both semantic and loss statistics characteristics through open set recognition-based splitting (OSS) and altruistic model-based data splitting (ALS) respectively, achieving good clean pool initialization. BSD further introduces class completion and selective dropping strategies in the subsequent pool updates to avoid potential class underfitting and backdoor overfitting caused by loss-guided split. Through extensive experiments on 3 benchmark datasets and against 7 representative attacks, we empirically demonstrate that our BSD is robust across various attack settings. Specifically, BSD has an average improvement in Defense Effectiveness Rating (DER) by 16.29\% compared to 5 state-of-the-art defenses, achieving clean-data-free backdoor security with minimal compromise in both Clean Accuracy (CA) and Attack Success Rate (ASR).

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper addresses the limitation of existing backdoor attack defenses, which typically require an auxiliary clean dataset that may be difficult to obtain. The authors propose a clean-data-free, end-to-end method to mitigate backdoor attacks. Their approach leverages two dynamically identified pools of data: one from open set recognition-based splitting and another from altruistic model-based splitting. These pools are then utilized in the main training loop, which the authors demonstrate to be effective in producing backdoor-free models, even when trained on poisoned datasets.

The authors validate their method using three benchmark datasets and test it against seven representative backdoor attacks, including both dirty-label and clean-label attacks. They compare their approach with five existing backdoor defenses and evaluate performance across two model architectures: ResNet-18 and MobileNet-v2.

### Strengths
- The paper targets a clear challenge in backdoor defense by eliminating the need for clean data, which is relevant to practical applications.

- The experimental evaluation is thorough, encompassing multiple datasets, attack types, and model architectures. The comparison against existing defense methods provides a meaningful context for the method's effectiveness.

- The authors conduct detailed ablation studies examining the impact of various hyperparameters, which helps in understanding the method's sensitivity and optimal configuration.

### Weaknesses
 - The study primarily focuses on supervised image classification tasks. This limitation should be explicitly stated in both the abstract and introduction to better set reader expectations.

- The paper's motivation could be strengthened by acknowledging recent developments in clean data acquisition methods. Notable omissions include:

  *Zeng et al. (2023, Usenix Security)* on clean subset extraction from poisoned datasets

  *Pan et al. (2023, Usenix Security)* on backdoor data detection methods

  These omissions affect the paper's premise that clean data acquisition is inherently impossible.


- Technical Issues:

  A typographical error in line 331: "Mobileent-v2" should be "MobileNet-v2"

### Questions
See weakness.

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
4

### Summary
This paper addresses the challenge of defending deep neural networks against backdoor attacks in the absence of clean data subsets. It introduces a novel defense mechanism called Bi-perspective Splitting Defense (BSD) that uses semantic and loss statistics characteristics for dataset splitting. The approach involves two innovative initial pool splitting techniques, Open Set Recognition-based Splitting (OSS) and Altruistic Model-based Splitting (ALS), and it enhances defense through subsequent updates of class completion and selective dropping strategies. The method demonstrates substantial improvements over state-of-the-art defenses across multiple benchmarks.

### Strengths
1. The paper introduces a novel method for defending against backdoor attacks without the need for clean data, addressing a significant limitation in previous methods.
2. Extensive experiments across multiple datasets and attack scenarios demonstrate the robustness and effectiveness of the proposed method, outperforming several state-of-the-art defenses.
3. The paper details multiple defensive strategies that contribute to its effectiveness, such as class completion and selective dropping, which are well-integrated into the defense strategy.

### Weaknesses
 1. The complexity of the proposed method involving multiple models and sophisticated data splitting strategies could be a barrier to practical deployment and computational efficiency.
2. While the method is empirically successful, the paper could be improved by providing deeper theoretical insights into why the specific strategies employed are effective.
3. The effectiveness of the method might depend on specific neural network architectures, and its adaptability to different or future architectures is not fully addressed.
4. The paper could benefit from a more detailed discussion on scenarios where BSD might fail or be less effective, which would be crucial for practical applications and future improvements.

### Questions
See weaknesses above.

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
Backdoor attacks threaten deep neural networks (DNNs) by embedding hidden vulnerabilities through data poisoning. While researchers have explored training benign models from poisoned data, effective defenses often rely on additional clean datasets, which are challenging to obtain due to privacy concerns and data scarcity.

To tackle these issues, the paper proposes the Bi-perspective Splitting Defense (BSD), which splits the dataset based on semantic and loss statistics using open set recognition (OSS) and altruistic model-based data splitting (ALS). This approach enhances clean pool initialization and includes strategies to prevent class underfitting and backdoor overfitting.

Extensive experiments on three benchmark datasets against seven attacks show that BSD is robust, achieving an average 16.29% improvement in Defense Effectiveness Rating (DER) compared to five state-of-the-art defenses, while maintaining minimal compromise in Clean Accuracy (CA) and Attack Success Rate (ASR).

### Strengths
- This paper explores a novel method to defend backdoor attacks which does not rely on clean subsets of data.

- The proposed method is simple but effective and the good performance obtained by the experiments strongly supports this point.

- The ablation study is organized well to clearly demonstrate the whole proposed method. And it makes the paper easy to follow.

### Weaknesses
 - I wonder **why the proposed BSD can effectively resist the clean-label backdoor attacks.** Clean-label backdoor attacks manipulate samples from the target class while keeping their labels unchanged. Since the BSD framework formulates backdoor defense within a semi-supervised learning context, it seems that whether the clean-label poisoned samples are part of the labeled or unlabeled subset, **the model can still associate the trigger with the target label in clean-label backdoor attacks.** Therefore, I am curious about how BSD manages to effectively resist the three clean-label attacks demonstrated in Table 2.

- I recommend conducting further experiments to assess whether BSD can successfully defend against backdoor attacks **with different target labels.** This could provide valuable insights into the robustness of the defense mechanism across various scenarios.

- Typos: #Line 848 --- #Line 849, 5*10e-4.

### Questions
Listed in the weakness of the paper. 

Score can be improved if concerns listed above are resolved.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper proposes an in-training clean-data-free backdoor defense method where the defender is required to train a clean model from scratch given a poisoned dataset without the need of any additional clean data. The key to success is to distinguish between clean samples and poisoned samples. To this end, they propose a novel identification mechanism which involves two main procedures. The first procedure is initializing a pool of clean samples and a pool of poisoned samples based on open set recognition-based splitting and altruistic model-based splitting. The second procedure is improving these pools with class completion and selective dropping strategy.

### Strengths
1. The proposed defense does not require any extra clean data.

2. They compare the problem of identifying clean target samples from poisoned samples with the open set recognition-based splitting problem of identifying UUCs from UKCs; inspired by which, they propose the identification mechanism.

### Weaknesses
1. Limited applied scenarios: The proposed defense is limited to backdoor attacks with a single target class. This is because the first step in identification involves identifying the single target class from other classes; however, in some popular attacks like BadNet’s all-to-all attacks, all classes are target classes, which disables the proposed defense.

2. The proposed method seems a bit complex as it includes two main steps—pool initialization and pool updating—and each step further involves two sub-steps, respectively. These steps aim to distinguish samples from different perspectives. Only after the total four steps, the poisoned samples are filtered out from clean samples. A complex mechanism is totally fine; but, there are two related issues: 1) does the necessity of pool updating validates that the effectiveness of pool initialization is not very good? 2) it seems that the effectiveness of each step highly depends on the performance of previous steps, e.g., if the identification of the target class is wrong, then all subsequent steps are useless. That is to say, accumulative errors may exist in the proposed method and which could lead to bad defense performance.

### Questions
1. In the exp setup, it’s reported to use 7 backdoor attacks while only 3 of them are presented in Table 1. That is to say, the performance against the remaining 4 attacks on the three benchmark datasets is not shown in the paper.

2. Considering the given threat model (i.e., in-training clean-data-free defense), it seems that sota defenses D-ST&D-BR [1] could also serve as baselines. These methods leverage the sensitivity of poisoned samples to transformations, which is quite different from the semantics and losses used in this paper; thus, it would be interesting to compare them and show that the proposed metrics are more accurate.

3. Is the accuracy of identifying the target class reported in the paper? What if the identified class is wrong, will it affect the performance of the following steps?

4. A type in Line 83: “first initialize” -> “first initializes”

[1] Chen, W., Wu, B., & Wang, H. (2022). Effective backdoor defense by exploiting sensitivity of poisoned samples. Advances in Neural Information Processing Systems, 35, 9727-9737.

### Soundness
3

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
4

### Summary
The paper discusses a method to defend against backdoor attacks in deep neural networks (DNNs) by training reliable models from poisoned datasets, addressing the challenge of lacking additional clean data due to privacy concerns or scarcity. It proposes a Bi-perspective Splitting Defense (BSD) that uses open set recognition-based splitting (OSS) and altruistic model-based data splitting (ALS) to divide the dataset effectively, initializing a pool of clean samples. BSD also employs class completion and selective dropping to prevent class underfitting and backdoor overfitting. Experiments on three benchmark datasets and against seven attacks show that BSD improves Defense Effectiveness Rating (DER) by an average of 16.29% compared to five state-of-the-art defenses, while maintaining high Clean Accuracy (CA) and managing Attack Success Rate (ASR) effectively, thus providing robust security without needing extra clean data.

### Strengths
The strengths of the proposed Bi-perspective Splitting Defense (BSD) method highlighted in the paper include:

1. **Efficiency in Utilizing Available Data**: BSD makes effective use of target labels and identifies clean samples from the poisoned dataset, reducing the dependency on additional clean data, which might be scarce or raise privacy concerns.

2. **Mitigation Strategies**: BSD incorporates class completion and selective dropping, helping to avoid issues like class underfitting and backdoor overfitting that could otherwise degrade model performance.

3. **Balanced Performance**: While enhancing security, BSD maintains high Clean Accuracy (CA) and manages Attack Success Rate (ASR), ensuring that the model remains accurate on clean data while defending against adversarial inputs.

### Weaknesses
The weaknesses identified in the paper are outlined as follows:

1. **Dependency on Target Recognition**: A significant limitation of the proposed methodology lies in its dependence on accurate target recognition. This dependency introduces a vulnerability; if an advanced attack manages to circumvent the existing detection mechanisms, the entire method could become ineffective. In my opinion, the superior performance is predicated on the assumption that the target class can be accurately identified.   Additionally, the framework's effectiveness diminishes when dealing with complex scenarios such as backdoor attacks that involve multiple targets, including those with dual-target labels or all-to-all attack configurations. Specifically, the reliance on open-set recognition (OSR) for splitting the dataset introduces a critical point of failure. If the OSR component misclassifies poisoned samples as clean, the subsequent training stages will be compromised. Furthermore, the method's performance under adaptive attacks, where the attacker is aware of the defense mechanism and crafts adversarial examples to specifically evade the OSR, is not sufficiently explored. The paper should include a more detailed analysis of the robustness of the target recognition component under various attack scenarios, including adaptive attacks.

2. **Absence of Comparative Analysis with Relevant Work**: The proposed dual-model training framework, which leverages an auxiliary model to support the primary model, shares similarities with the approach detailed in "[1]". However, the manuscript lacks a comparative analysis of this work. I see the proposed method has many differences from [1], but incorporating such a comparison would significantly bolster the credibility and relevance of the current submission by providing a clearer differentiation and understanding of the advantages and limitations relative to existing methodologies. The paper would benefit from a more thorough discussion of how the proposed method differs from and improves upon the techniques used in [1], particularly in terms of the splitting strategy and the use of the auxiliary model. A quantitative comparison, including performance metrics and computational cost, would be essential to understand the practical advantages of the proposed approach.

### Questions
The authors have already provided comprehensive analyses and experiments.

However, an unresolved question remains: How effectively can the proposed method be applied to scenarios involving multi-target attacks?

### Soundness
3

### Presentation
3

### Contribution
3

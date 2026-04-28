# Gradient Storm: Stronger Backdoor Attacks Through Expanded Parameter Space Coverage

- Decision: Reject
- Avg Score: 3.00
- Scores: 3, 3, 3, 3

## Abstract
Targeted data poisoning poses a critical adversarial threat to machine learning systems by enabling attackers to manipulate training data to induce specific, harmful misclassifications.  Among these threats, backdoor attacks are particularly pernicious, embedding hidden triggers in the data that lead models to misclassify only those inputs containing the trigger,  while maintaining high accuracy on benign samples.  In this paper, we propose Gradient Storm, a novel technique that facilitates the simultaneous execution of multiple backdoor attacks, while necessitating only minimal modification to the training dataset.  Our contributions are twofold: First, we introduce a method for designing adversarial poisons in modular components, each tailored based on a distinct region of the model’s parameter space. Second, we present a framework for conducting multi-trigger attacks, where each trigger  causes  misclassification  from  a  specific  source  class  to  a  distinct  target class.  We evaluate the efficacy of Gradient Storm across multiple neural network architectures and two benchmark datasets, demonstrating its robustness against eight different poisoning defense mechanisms. Additionally, we show that poisons crafted for one model can be effectively transferred to other models, demonstrating that our attack remains effective even in black-box settings.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper introduces a novel technique for enhancing backdoor attacks. Gradient Storm enables multiple backdoor triggers to be embedded within a model with minimal data manipulation. The attack leverages different regions of the model’s parameter space, facilitating multi-trigger, multi-target attacks. The paper demonstrates that Gradient Storm is effective across multiple architectures and datasets. Furthermore, the study shows that backdoors created in one model can transfer to other models.

### Strengths
Gradient Storm approach enables multi-trigger, multi-target backdoor attacks. The paper is well-written and easy to follow. The paper is supported by its experimental evaluations across various CNNs architectures and benchmark datasets,

### Weaknesses
The experimental section (4) lacks some comments on the results, i.e., the results are presented without analyzing if they support the claims presented.

Moreover, an evaluation of the trade-offs between the number of triggers and their stealthiness would strengthen the paper. The experimental design could benefit from a baseline comparison with simpler multi-trigger methods to better illustrate the advantages offered by Gradient Storm.

### Questions
- Can you please comment more on the implications of the results shown in Section 4?
- In light of Table 3, would you claim that Gradient Storm is able to bypass current defenses? Which hyperparemeters where chosen as for the defenses to do so? For instance, I-BAU and MOTH show a good performance against the attack
- Gradient Storm introduces various parameters, such as the number of triggers, poison budgets, and gradient matching thresholds. Could the authors provide guidance on tuning these parameters?
- Multi-trigger backdoors may introduce interaction effects between triggers. Can the authors provide an insight into how simultaneous or sequential activations of different triggers impact the model’s behavior?

### Soundness
2

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
3

### Summary
The paper proposes Gradient Storm, a more effective version of the Sleeper Agent backdoor. The attack achieves its high effectiveness by designing perturbations that are distributed across the parameter space. This is accomplished by introducing *cycle rounds* where perturbations are optimized on disjoint subsets of the dataset. The method's effectiveness is validated against Sleeper Agent on CIFAR-10 and GTSRB.

### Strengths
- The writing is easy to follow.
- Sleeper Agent backdoors are an interesting and very hidden backdoor type that warrant more exploration.

### Weaknesses
 - The novelty of the proposed extension to Sleeper Agent is limited.
- Limited datasets used in experiments. All experiments are done on CIFAR-10, except for one ASR experiment on GTSRB.
- The attack is very computationally intensive, requiring retraining a surrogate that approximates the attacked model (number of optimization cycles) * (number of cycle rounds) * (number of triggers) times. This implicitly assumes the attacker has access to very significant computational resources or is only able to attack small models.
- Standard ResNet-18 training uses random crop as a data augmentation [1], which is not use here. I suspect random crop would make this attack less effective.
- The paper does not describe what hyperparameters are used by each defense nor how those hyperparameters are derived. A maximally charitable evaluation of defenses would optimize hyperparameters against the attack and show how much clean data is required to remove the attack.
- The experiments in section 4.4 do not add very much beyond proving that a ResNet-18 has the capacity to learn 2-3 backdoors when training on CIFAR-10.
- It is unclear whether the increased ASR comes from the partitioning mechanism or from having multiple optimization cycles $S$ where the dataset containing the best randomized perturbations are returned.
- The paper does not provide an analysis on how different settings of cycle rounds $R$ and optimization cycles $S$ effects the success of the backdoor. The experiments section only examines one setting of these parameters without justifying how this setting is derived. This is a missed opportunity to demonstrate how valuable the proposed modification is to achieving a successful attack.

Minor
- Line 22 of algorithm 1 contains a typo.

### Questions
- Why do you use 8 retraining periods GA while only 4 for Sleeper Agent? What would be the results in tables 1 and 2 if 8 equally spaced retraining periods were used for the Sleeper Agent attack?
- What are the poisoning budgets used across the experiments ($B$ in algorithm 1)? How does using different poison budgets effect the ASR?

References

[1] He, Kaiming, et al. "Deep Residual Learning for Image Recognition," 2016.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The article introduces the concept of gradient storms, a technique that simultaneously executes multiple backdoor attacks. The authors expand upon the existing optimization-based poisoning methods, enabling them to adapt to different attack targets and various triggers.

### Strengths
1. The article reexamines the existing poisoning framework and finds that it can be further expanded to a multi-trigger setting.
2. The method proposed in the article performs very well.
3. The method proposed in the article has good reproducibility.

### Weaknesses
1. The introduction chapter mainly consists of a literature review and lacks a clear presentation of its own contributions.
2. There is a problem of symbolic ambiguity with x_i and y_i in line 135. Does x_i refer to a sample or a feature? The subscript of y_i indicates both the index of the data and the index of the label.
3. There is a confusion between \delta and \Delta in lines 133 and 144.
4. The definition of D_i in line 150 is suggested to be elaborated.
5. Why does Formula 1 impose a norm constraint on the size of noise for any given case? This seems to be an unnecessary and uncommon term.
6. Tables 1 and 2 seem to compare different methods at all; they only conducted experiments using different triggers.
7. The contribution of the article is to expand SleeperAgent to a multi-trigger, multi-target setting, and there is still room for improvement in its contribution.

### Questions
What new methods does the article propose based on SleeperAgent?

### Soundness
3

### Presentation
1

### Contribution
1

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper improves existing attack methods and introduces "Gradient Storm," a more advanced data poisoning technique. The paper evaluate the proposed attack across various neural network architectures and two benchmark datasets, demonstrating its effectiveness.

### Strengths
The paper improves existing attack methods, and evaluate the proposed methods on different datasets & models.

### Weaknesses
Although the paper claims the proposed attack is more effective, but the results do not show that (Table 3). I also have other concerns as follows:

- Novelty: The changes seem minor compared to existing methods and the proposed method lacks convincing intuition. More explanation and comparative analysis of existing work (especially technical contributions) would be appreciated.

- Contribution: the paper mentions that one of the main contribution is “Multiple Triggers, Targets, and Attack Types”, which is not well justified. No clear demonstration of why paired target-trigger combinations matter. Also, simply implementing more attacks isn't a substantial contribution

- Evaluation settings: The paper only evaluates CIFAR and GTSRB datasets, and one trigger type. Evaluation on more datasets and triggers would be helpful.

- Evaluation results: the results in Table 3 shows that the proposed attack methods fails in at least 3 defense cases. It would be helpful to include the performance of other attacks against the defense methods (based on my experience, they fail less).

### Questions
N/A

### Soundness
3

### Presentation
2

### Contribution
2

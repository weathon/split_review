# Toward Robust Defenses Against LLM Weight Tampering Attacks

- Decision: Accept
- Scores: 6, 8, 5, 5, 6, 5

## Abstract
Rapid advances in the capabilities of large language models (LLMs) have raised widespread concerns regarding their potential for malicious use. Open-weight LLMs present unique challenges, as existing safeguards lack robustness to tampering attacks that modify model weights. For example, recent works have demonstrated that refusal and unlearning safeguards can be trivially removed with a few steps of fine-tuning. These vulnerabilities necessitate new approaches for enabling the safe release of open-weight LLMs. We develop a method, called TAR, for building tamper-resistant safeguards into open-weight LLMs such that adversaries cannot remove the safeguards even after thousands of steps of fine-tuning. In extensive evaluations and red teaming analyses, we find that our method greatly improves tamper-resistance while preserving benign capabilities. Our results demonstrate that progress on tamper-resistance is possible, opening up a promising new avenue to improve the safety and security of open-weight LLMs.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper proposes a method (TAR) for improving tamper-resistance, i.e. model-level defense against adversarial finetuning attacks, of open-weight large language models. The method consists of several components: (1) initial safeguarding via _random mapping_ of harmful representations, (2) outer loop minimizing tamper-resistance and retain losses, (3) inner loop for computing tamper-resistance loss, which applies multiple finetuning attacks. Different design choices for tamper-resistance loss and its empirical significance are discussed: for weaponization knowledge restriction setting a negative _entropy_ loss is proposed, and for harmful request refusal a direct preference optimization (DPO) loss is used. The retain loss consists of language modeling loss and $l_2$-norm loss for representations of optimized and a base model. The results suggest the proposed method effectively defends the model against the majority of considered finetuning attacks, maintaining low accuracies on harmful questions post-(finetuning)-attack, although at the considerable cost of drop in accuracy on benign questions (pre-attack). Additionally, the authors acknowledge that the set of finetuning attacks during tamper-resistance training directly impacts the tamper-resistance against test-time attacks (e.g. "Retain $\rightarrow$ Forget" attack breaks the defense if it is not included in the training phase), suggesting the defense might struggle with unseen attacks (e.g. PEFT-attacks could break the defense in many of the settings).

### Strengths
1. **Significance** of the problem. The paper addresses an important and challenging problem of defending open-weight large language models against finetuning attacks. In authors words: "_This problem has been considered very challenging and by some intractable, as no method has yet provided substantial robustness to these attacks. However, making progress on this problem would provide a valuable tool to regulators and model developers by ameliorating the dual-use dilemma of open-weight models_".

2. **Originality**. Although most of the components of the proposed method are inspired from previous works (e.g. adversarial training, representation engineering), the overall approach constitutes substantial novel contribution to the field, to the best of my knowledge. The results on tamper-resistance for post-attack harmful accuracies demonstrate substantial improvement over previous methods (for most of the considered attacks).

### Weaknesses
 1. **Evaluation** against out-of-distribution attacks.
- My main concern is that the defense might be effective mostly against observed attacks, and it could break against other unseen attacks. For example, Table 4 in Appendix shows that "Retain $\rightarrow$ Forget" attack breaks the defense if it is not included in the training phase. Figure 4, and Figure 8 from Appendix show that PEFT attacks are more effective than Full Parameter attacks (in case of Biosecurity, PEFT attacks break the proposed defense method), given that the TAR used Full Parameter attacks during training.
- Therefore, more emphasis and red teaming effort should be put into unseen attacks during evaluation, e.g. the Post-Attack scores in Table 1 could be divided into "in-distribution" and "out-of-distribution" attacks, where the categorization of attacks should be agnostic to LR, LR scheduler, optimizer, number of steps, batch size. In other words, out-of-distribution attacks could be defined as those that use fundamentally different approaches or data sources than what was used during training, rather than just different hyperparameters. Testing against attacks that use different optimization algorithms, loss functions, or data distributions not seen during training could provide a more comprehensive assessment of the method's robustness. For instance, attacks employing second-order optimization methods, or those that introduce noise into the gradient updates, could reveal vulnerabilities not exposed by standard first-order methods. The current evaluation primarily focuses on variations of standard fine-tuning, which might not be sufficient to capture the full spectrum of potential adversarial strategies.
- Since PEFT finetuning is more compute-efficient than Full Parameter tuning, the variants of PEFT attacks with more optimization steps should be considered under the compute-constrained attacker setup. PEFT attacks should also be considered for harmful request refusal. The evaluation should explore a wider range of PEFT configurations, including different adapter sizes, learning rates, and optimization algorithms, to determine the limits of the proposed defense.
- Other out-of-distribution attacks could also be proposed and evaluated, e.g. initializing an attack by perturbing the weights into a random direction before following gradients to avoid local potentially gradient obfuscated region; or running a ground-truth informed attack by following a fixed worst-case direction towards the weights of a harmful model to observe how far the optimization should run to get harmful results.  Furthermore, attacks that leverage knowledge distillation from a harmful model could be explored to see if the TAR model is vulnerable to transfer attacks.
- Input-level red teaming approaches (e.g. from HarmBench benchmark) could also be evaluated as alternative attacks, which do not include gradients or weight perturbations.


2. More **detailed analysis** of the method is missing. The problem of **obfuscated gradients** should be addressed.
- The results for Chemical Security in Table 1 suggest that post-attack harmful accuracies for TAR are lower than pre-attack ones, which is unexpected and worrying. Could you provide a more detailed analysis of this phenomenon? Could you investigate whether this is due to a quirk in your evaluation setup, or if it reveals something fundamental about how your method works?  It is crucial to understand if this is a consistent behavior or an anomaly specific to the chemical domain. The authors should investigate the loss landscape around the TAR-trained model to understand why the attack performance is worse than the pre-attack performance.
- Also the plots in Figure 6 in Appendix show that the loss values first start to increase under the gradient-based attacks, which is surprising. Could the loss decrease just by switching the gradient sign in the beginning of the optimization? This might point towards the problem of obfuscated gradients [a]. Other attacks, e.g. gradient-free ones, or the exploration of the loss landscape could provide a better understanding of the phenomenon. The authors should investigate the loss surface around the TAR-trained model to understand the cause of this behavior. Specifically, the authors should explore the sharpness of the loss landscape and whether the gradients are reliable indicators of the direction to harmful model parameters.
- Section A in Appendix states that post-attack accuracy on benign questions for TAR method is low. This should be reflected in the main paper, and the reasons for this phenomenon could be studied and discussed. Section C1 of Appendix addresses the problem of benign finetuning, however it does not provide comparison with benign finetuning of the base model (or other non-TAR trained harmless models). What percentage of harmful questions could appear in finetuning to prevent the benign learning? Could benign prompts from Over-Refusal benchmark [b] cause the issues with benign finetuning?
- Over-Refusal benchmark [b] results should be included for the restricted models for full evaluation.

3. The **capability-robustness tradeoff** could be studied and discussed more in-detail, since this is the main limiting factor of applying TAR comparing to baseline methods.
- From Table 1, TAR is considerably *worse than baselines in terms of benign capabilities* in adjacent domain knowledge for about 10% in all domains. What about other capabilities such as reasoning, multi-lingual understanding, creative writing, coding etc? The authors should evaluate the impact of TAR on a broader range of capabilities, including those that are not directly related to the targeted domains. This would provide a more comprehensive picture of the trade-offs introduced by the method.
- Could the whole capabilities-robustness tradeoff curve be explored and demonstrated for TAR and for baseline methods by varying hyperparameters (e.g. such as $\lambda_{TR}$)? Could a single metric for the method's tradeoff performance be proposed and compared between baselines, similar to Accuracy-Robustness Tradeoff Score (ART-score) in [c]? The authors should investigate the sensitivity of the method to different hyperparameter settings and provide a clear understanding of how these parameters affect the trade-off between robustness and benign performance.

4. **Clarity**.
- Many important parts of the paper are in Appendix, e.g. Random Mapping, attack categories, many crucial evaluations (see above). This makes the main paper less clear and prevents it from being self-sufficient.
- Was a single model trained to be tamper-resistant against all 3 weaponization domains, or were 3 different TAR models considered (e.g. in Table 1)? Was a single model trained for both weaponization restriction and harmful request refusal, or 2 different ones? Could a single model be defended against all considered harms? How would it affect benign capabilities? Is the approach the same for baseline methods? It was not clear from the text for me. These details could be included in the experimental setup section, and you could include a diagram or table summarizing the model configurations used for different experiments.
- What are the computational costs of TAR comparing to benign PEFT, Full Parameter finetuning and other baselines? The authors should provide a detailed analysis of the computational cost of the proposed method, including training time, memory usage, and the number of parameters involved. This would allow for a more informed comparison with other methods.
- Minor comment: could the scores in Table 1 be scaled such that random model gets 0, and perfect model get 100? It would help visualizing the effectiveness of TAR more clearly.

### Questions
See weaknesses section for questions and suggestions. I would be happy to change my opinion if my main concerns regarding fair evaluation of the defense method could be addressed.

### Soundness
2

### Presentation
3

### Contribution
4

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper focuses on the robustness of open-weight LLMs and proposes a novel defense method called TAR.

### Strengths
**About contribution**

+ The experimental results shown in Table 1 are significant enough to validate the main claims of this paper. 
+ The proposed method is intuitive.  By providing detailed discussions of the related works, it is not hard to understand why the authors designed the algorithms as presented, even for readers not familiar with the defense of LLMs.

**About novelty**

According to Section 2, this paper proposes the first defense method for autoregressive LLMs against tampering attacks. To the best of my knowledge, concurrent jailbreaking attacks are mostly input-based. However, as claimed in Section 1, the tampering attacks are also posing threats to LLMs. This paper will bring new insight into the research on the robustness of LLMs.

**About presentation**

+ The preliminary part (Section 3) is brief and clear, making the technical part of this paper easy to follow.

### Weaknesses
 **About presentation**

+ The authors do not discuss the cost of the experiments, including time cost and GPU memory cost. Section B.4 mentioned that the experiments use 8 A100 with 80GB GPU memory. What is the minimum requirement for the experiments? Specifically, what is the scaling of memory usage with respect to model size, and how does the training time scale with respect to the number of inner and outer loop steps? The current discussion lacks details on the computational resources needed to reproduce the results, making it difficult to assess the practical applicability of the proposed method.
+ I suggest including a statement of contribution to make this paper easier to follow.

### Questions
+ In Figure 2, the difference between TAR and the baseline methods is significant. However, it seems that the capabilities of TAR are lower than the baseline methods. Is there a trade-off between capabilities and tamper resistance?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper focuses on the issue of the lack of robustness in open LLMs when facing model weight tampering attacks. The authors propose a method called TAR, designed to establish tamper-resistant protection mechanisms for LLMs, ensuring that attackers cannot compromise these protections after minimal optimization. Extensive experiments validate the performance of this approach, showing that it outperforms existing methods.

### Strengths
The security issues related to open LLMs are both important and intriguing; The authors present a series of solutions to address these security threats; and experiments validate the performance of the proposed mechanisms.

### Weaknesses
1. Insufficient sustainability. This paper proposes the integration of adversarial learning and meta-learning to enhance the effectiveness of defense mechanisms, making it difficult for attackers to compromise them in a short period. However, this effectiveness actually depends on the diversity of attack types included in the training data for optimizing eqn.1. In other words, the resilience of the proposed mechanism may be superficial and does not guarantee the security of open-weight LLMs. Furthermore, the authors do not provide corresponding theoretical analysis or proof.
2. Incremental technical contributions. Although the paper is expressed clearly, its innovation is not evident in terms of both technical aspects and application scenarios. Specifically, the proposed solutions are based on existing widely used methods, and the authors have not clearly articulated their unique contributions. Therefore, it is recommended that the authors provide further clarification on this matter.
3. The performance of the proposed mechanism is closely related to the adversarial training methods and data, which means its resilience remains a significant issue.
4. The presentation of the performance comparison between TAR and existing mechanisms in Figure 5 is unclear and potentially confusing. The authors should provide further analysis of this result, explaining why the performance of TAR shows a significant change as the step size increases.

### Questions
1. Insufficient sustainability. This paper proposes the integration of adversarial learning and meta-learning to enhance the effectiveness of defense mechanisms, making it difficult for attackers to compromise them in a short period. However, this effectiveness actually depends on the diversity of attack types included in the training data for optimizing eqn.1. In other words, the resilience of the proposed mechanism may be superficial and does not guarantee the security of open-weight LLMs. Furthermore, the authors do not provide corresponding theoretical analysis or proof.
2. Incremental technical contributions. Although the paper is expressed clearly, its innovation is not evident in terms of both technical aspects and application scenarios. Specifically, the proposed solutions are based on existing widely used methods, and the authors have not clearly articulated their unique contributions. Therefore, it is recommended that the authors provide further clarification on this matter.
3. The performance of the proposed mechanism is closely related to the adversarial training methods and data, which means its resilience remains a significant issue.
4. The presentation of the performance comparison between TAR and existing mechanisms in Figure 5 is unclear and potentially confusing. The authors should provide further analysis of this result, explaining why the performance of TAR shows a significant change as the step size increases.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces a novel method called TAR, designed to enhance the robustness of large language models (LLMs) against tampering attacks, addressing significant vulnerabilities in existing safeguards.

### Strengths
1. The topic studied in this paper is of great significance. Malicious LLMs can cause serious harm, such as spreading false news about public figures, causing discrimination and unfair results due to prejudice, and generating violent terrorist information. Therefore, it is necessary to apply robust safeguards to open source LLMs.

2. The proposed method successfully resists thousands of malicious fine-tuning.

### Weaknesses
1. The organization of Section 4 requires further refinement for improved readability. It would be beneficial to briefly outline the design motivation before delving into specific details, particularly regarding the content of Fig. 3. Additionally, the mathematical formulation of the loss function used is currently absent.

2. The caption of figure 1 needs to explain the difference between the two branches more clearly. For example, what's the difference between the first nodes of the two branches.

3. In Section 1, the authors assert that the proposed method can endure fine-tuning of up to 5000 steps. However, this claim does not intuitively convey the contribution of the paper. Firstly, the details surrounding fine-tuning, such as batch size and learning rate, are unclear; these parameters significantly influence the number of fine-tuning steps. Secondly, a comparative analysis with the typical number of steps required to fine-tune models on downstream tasks is lacking.

4. The threat model lacks clarity. The authors assume that the attacker is compute-bounded but do not provide a clear definition of what this entails. Furthermore, including concrete examples of the metrics for capabilities_metric and safety_metric would enhance understanding.

5. In section 4.2, the authors emphasized that the proposed method is different from standard meta-learning. However,  the differences highlighted seem minor and do not present significant technical challenges.

6. The term 'empirically' is employed multiple times in the methods section. While drawing conclusions from empirical observations is valuable for informing solution design, relying solely on empirical data, particularly in the selection of a loss function, may impose limitations on the solution's robustness. A theoretical analysis comparing the efficacy of the entropy loss function versus cross-entropy loss is necessary.

7. The performance metrics used in the experiments require clear explanation. Based on the results presented, the proposed solution appears to sacrifice task performance in favor of enhanced robustness, suggesting potential flaws in the method.

### Questions
None

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
4

### Summary
This paper studies an important problem: fine-tuning attacks on LLMs. They propose a novel defense method, TAR, to improve the robustness of LLMs against possible malicious fine-tuning attacks. This method is based on adversarial training and meta-learning, and a novel training objective combining both an adversarial objective and a retaining objective is proposed to maintain utility. Extensive experiments are conducted to illustrate the effectiveness of proposed method.

### Strengths
This paper is written well and logically. I enjoy reading this work and every detail is properly described. The large-scale experiments are comprehensive and convincing.

### Weaknesses
1. The time complexity analysis is important but not included. Both adversarial training and meta-learning are time-consuming. The proposed method can be expensive especially when the model size is increasing. This brings a concern about whether this method is practical for protecting large models. I suggest the authors provide computation analysis either empirical or theoretical. Specifically, the analysis should consider the number of forward and backward passes required, the memory footprint of the meta-learning process, and how these scale with model size and training data. The analysis should also discuss the practical implications of these costs, such as the feasibility of training on different hardware setups and the overall training time.

2. There are many hyperparameters in either objective in Eq (1) or optimizing it, such as the number of outer loops and coefficients before tamper-resistance loss and retain loss (lambda_TR and lambda_retain). How they influence the defending performance is not discussed, and I suggest including it. The discussion should include a sensitivity analysis of these hyperparameters, showing how the performance of the method changes as these parameters are varied. This should include not only the final performance but also the convergence speed and stability of the training process. Furthermore, the interaction between these hyperparameters should be explored, as they may not be independent.

### Questions
I am curious about what kind of A_train in the objective in Eq(1) is required to have a good defense. For example, how diverse attacks need to be included; how many adversarial examples for each attack need to be included, etc.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 6

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper proposes Tampering Attack Resistance (TAR) method which builds robust safe LLMs under weight tampering attacks. The method achieves superior performance on weaponization knowledge restriction and harmful refusal training.

### Strengths
1. The defense of LLM's weight tampering attacks is an important topic. This work has great significance.

### Weaknesses
1. there are to many proxy objectives, like "safety_metric", "capabilities_metric". These pre-defined metrics will limit the significance and universality of the proposed method. Unless the author can prove that TAR is still working under other "safety_metric" or "capabilities_metric".
2. From Eq.1, TAR is a simple adversarial training paradigm, with some proxy indicators. While adversarial training is an exist well known technique.

### Questions
1. Are there any experiments to validate TAR on proxy metrics has a certain degree of generalization on other safety scenes or benchmarks?
2. How about the training cost of TAR. Is it larger than original training?
3. Except for the adversarial training, are there any novel findings or modifications of TAR, which suggest the novelty.

### Soundness
3

### Presentation
2

### Contribution
2

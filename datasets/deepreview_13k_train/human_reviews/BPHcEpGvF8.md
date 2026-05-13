# Demystifying Poisoning Backdoor Attacks from a Statistical Perspective

- Decision: Accept
- Scores: 3, 6, 8, 6

## Abstract
The growing dependence on machine learning in real-world applications emphasizes the importance of understanding and ensuring its safety. Backdoor attacks pose a significant security risk due to their stealthy nature and potentially serious consequences. Such attacks involve embedding triggers within a learning model with the intention of causing malicious behavior when an active trigger is present while maintaining regular functionality without it.
This paper evaluates the effectiveness of any backdoor attack incorporating a constant trigger, by establishing tight lower and upper boundaries for the performance of the compromised model on both clean and backdoor test data. The developed theory answers a series of fundamental but previously underexplored problems, including (1) what are the determining factors for a backdoor attack's success, (2) what is the direction of the most effective backdoor attack, and (3) when will a human-imperceptible trigger succeed. Our derived understanding applies to both discriminative and generative models. We also demonstrate the theory by conducting experiments using benchmark datasets and state-of-the-art backdoor attack scenarios.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper studies backdoor attacks with a constant trigger, assuming the trained classifiers are Bayesian optimal with respect to the poisoned training set.

Through this framework, they provide the following insights for backdoor attacks using a constant trigger:
1. More backdoor data can harm clean performance and can help backdoor to success.
2. Backdoor attacks can be more successful when the constant trigger has a larger magnitude.
3. Backdoor attacks can be more successful when the direction of the constant trigger points towards less popular regions (i.e. regions with smaller density).
4. Arbitrarily small backdoor data ratios may result in successful attacks.
5. If there is a direction where for all samples the corresponding support of the marginal distribution is a single point, the magnitude of the trigger can be arbitrarily small to have a successful attack.

### Strengths
1. Theoretical understanding of backdoor attacks is an important topics.
2. The authors demonstrate their skills in using statistical tools.

### Weaknesses
While I appreciate the skills demonstrated by the authors, none of the obtained insights is interesting in a sense that they are either trivial or not true without assuming the model to be Bayesian optimal with respect to the poisoned training distribution.

To be specific, insight 1&2 listed in the above Summary section are trivial (even though it may generalize to other backdoor/poison attacks); Insight 3&4&5 are trivial only when assuming the model to be Bayesian optimal but may not generalize to other (actual) learning algorithms.

To sum up, my primary concerns regarding this submission include:
1. Some key assumptions that oversimplify the problems and make the analysis probably irrelevant to practice, e.g. models are Bayesian optimal with respect to the poisoned distribution & Assumption 3 (Ordinary convergence rate) in the submission.

2. Key insights are either trivial (insight 1&2) or likely not generalizable (insight 3&4&5).


Notably, the experiments are thin but I find it acceptable for a theory paper. The major issue is not that experiments do not provide enough supports. The issue is that there is not really much insights worth supporting.

### Questions
Please see the weakness section above.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper conducts a theoretical analysis of backdoor attacks, with a focus on addressing three key questions: (1) What are the factors that determine the effectiveness of a backdoor attack? (2) What is the optimal choice of trigger with a given magnitude? (3) What is the minimum required magnitude of the trigger for a successful attack? The paper utilizes finite-sample analysis to derive both upper and lower bounds for the success of a backdoor attack. The poisoning rate, trigger magnitude, and trigger direction are important factors influencing the success of a backdoor attack. Additionally, this paper carries out experiments on synthetic data as well as tasks involving image classification and generation. The empirical results validate the theoretical analysis.

### Strengths
1. The paper provides a theoretical analysis on backdoor attacks, an important topic of machine learning security.

2. A few factors that contribute to the success of a backdoor attack are studied in the paper. The choice of a trigger is particularly interesting. The insights shown in the paper can provide a theoretical guideline for further work.

3. The empirical results on synthetic data validate the theoretical analysis and also provide an explanation for generative models.

### Weaknesses
1. Some claims are not well validated empirically. The paper states "a large backdoor data ratio ρ will damage the performance on clean data." But there is no empirical evidence to support this claim. Also, according to the literature, a high poisoning rate usually does not significantly affect clean accuracy. It is recommended to empirically validate this claim and assess its consistency with the theories.

2. The experiment conducted in Table 2 is not clear. What does the magnitude of backdoor triggers mean? Is it the L2 norm of η, or a fixed pixel value that replaces the original pixel on the input? How large is the backdoor trigger used in this study? In addition, the formalization of backdoor trigger as η in X' = X + η is not accurate. Backdoor attacks, such as BadNets replace the original pixel values with the backdoor trigger. Otherwise, the trigger pattern is not fixed and varies on different inputs.

3. The paper seems to focus on dirty-label backdoor attacks, where the poisoned samples are assigned a target label. There is anther line of attacks that do not change the label, such as SIG [1] and reflection attack [2]. Is the proposed theoretical analysis applicable to these clean-label attacks?

### Questions
N/A

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
From the statistical perspective, this paper theoretically analyzed the efficiency of backdoor attacks. Specifically, focusing on the binary classification and generative model, the authors relied on two assumptions to calculate the tight lower and upper boundaries of the backdoor model’s performance on the clean and poisoned test data.

### Strengths
Their theoretical conclusion for the efficiency of backdoor attacks matches with the empirical results. For instance, the influence of the poisoning ratio and the magnitude of the trigger signal. Moreover, they also claimed that when fixing the poisoning ratio and the magnitude of the trigger, it is more efficient to choose the trigger along the direction the density of clean data drops quickly.

### Weaknesses
One thing I want to mention is about the reference, as far as I know, there exist some references on the backdoor efficiency. The authors should cite them.
[1] W. Guo, B. Tondi and M. Barni, "A Temporal Chrominance Trigger for Clean-Label Backdoor Attack Against Anti-Spoof Rebroadcast Detection," in IEEE Transactions on Dependable and Secure Computing, doi: 10.1109/TDSC.2022.3233519.
[2] Yinghua Gao, Yiming Li, Linghui Zhu, Dongxian Wu, Yong Jiang, and Shu-Tao Xia. Not all samples are born equal: Towards effective clean- label backdoor attacks. Pattern Recognition, 139:109512, 2023. 2, 3
[3] Pengfei Xia, Ziqiang Li, Wei Zhang, and Bin Li. Data-efficient backdoor attacks. In Proceedings of the Thirty-First International Joint Conference on Artificial Intelligence, IJCAI-22, pages 3992–3998, 2022

### Questions
Is it possible to extend this theoretical framework for multi-discriminator with more than 2 classes.

### Soundness
3 good

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper addresses the safety risks in machine learning posed by backdoor attacks, where triggers are embedded in models to activate malicious behavior under specific conditions. It focuses on evaluating the effectiveness of backdoor attacks with constant triggers and establishing performance boundaries for models on clean and compromised data. The study explores key issues: the factors determining an attack's success, the optimal strategy for an attack, and the conditions for success with human-imperceptible triggers. Applicable to both discriminative and generative models, the findings are validated through experiments using benchmark datasets and current backdoor attack scenarios.

### Strengths
- This paper focuses on an important problem. It provides a fundamental understanding of the influence of backdoor attacks.
- This paper provides extensive theoretical analysis.
- This paper is easy to follow.

### Weaknesses
 - The observation that a high poisoning ratio adversely affects the performance of clean data lacks novelty. 
- The paper lacks clarity in some sections. For instance, Section 6.2.1 discusses the impact of backdoor trigger magnitudes, but fails to specify crucial details of the attack setting, such as the size of the trigger.
- The authors assert that WaNet, Adaptive Patch, and Adaptive Blend attacks are more effective than BadNets, as evidenced by a greater relative change in dimensions with low variance. However, the term "effectiveness" needs clarification. BadNets is known for its high attack success rate, so how do these methods compare under identical attack settings, including trigger size and magnitude?
- The methodology for measuring the Mean Squared Error (MSE) between clean training images and those altered by the backdoored DDPM is unclear. Given that DDPM generation is inherently a stochastic process, a more detailed explanation of this measurement technique would be beneficial.

### Questions
See the weakness.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

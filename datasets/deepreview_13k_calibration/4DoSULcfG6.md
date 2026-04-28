# Chameleon: Increasing Label-Only Membership Leakage with Adaptive Poisoning

- Decision: Accept
- Avg Score: 5.33
- Scores: 5, 5, 6

## Abstract
\noindent
The integration of machine learning (ML) in numerous critical applications introduces a range of privacy concerns for individuals who provide their datasets for model training. One such privacy risk is Membership Inference (MI), in which an attacker seeks to determine whether a particular data sample was included in the training dataset of a model. Current state-of-the-art MI attacks capitalize on access to the model’s predicted confidence scores to successfully perform membership inference, and employ data poisoning to further enhance their effectiveness. 
In this work, we  focus on the less explored and more realistic \emph{label-only} setting, where the model provides only the predicted label on a queried sample. We show that existing label-only MI attacks are ineffective at inferring membership in the low False Positive Rate (FPR) regime. To address this challenge,  we propose a new attack \atkname\ that leverages a novel adaptive data poisoning strategy and an efficient query selection method to achieve significantly more accurate membership inference than existing label-only attacks, especially at low FPRs.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper targets at Membership Inference (MI), in which an attacker seeks to determine whether a particular data sample was included in the training dataset of a model. In contrast to the most of work in this area, the paper considers a less favorable setting: the attacker has access only to the predicted label on a queried sample, instead of the confidence level. I think this is an important problem, which should be interesting to the communities of both DP and privacy attack. To address this challenge, the paper proposes a new
attack Chameleon that leverages adaptive data poisoning to achieve better accuracy than the previous work.

### Strengths
1. The paper proposes a new attack Chameleon that leverages adaptive data poisoning to achieve better accuracy than the previous work.
2. The paper observes an interesting phenomenon: for different challenge point, the sweet spot of the number of samples needed in the data poisoning is different. The paper also proposes a theory to reflect this phenomenon.
3. Various experiments have shown the advantages of the new method.

### Weaknesses
Although the attack and the observation is interesting, I think the paper has the following weak points:

1. Time complexity. Clearly from Algorithm 1, to run the adaptive poisoning, the attacker has to run the training model much more times than the baseline algorithms, making the proposed algorithm less practical. However, the paper touches little about this topic, and does not provide any comparison in the experiment section. I think this information is crucial for the readers to better understand and appreciate the proposed algorithm. Specifically, the iterative nature of Algorithm 1, requiring retraining for each poisoning level, makes it computationally expensive. The paper should include a detailed analysis of the number of training epochs and the overall time required for the Chameleon attack compared to the baseline, perhaps broken down by the number of shadow models and poisoning iterations. This is especially important given that the attack's effectiveness hinges on this iterative process.

2. Multiple challenge points. Usually in practice, the attacker needs to attack multiple challenge points instead of the only one. Although the paper briefly discusses this in the appendix, I think it is far from enough. Specifically, Algorithm 2 is just a simple generalization of Algorithm 1, neglecting many interesting and important problems due to more than one challenge points. For example, the problem of time complexity becomes even worse. Furthermore, due to the correlations of different challenge points, it is not clear how Algorithm 2 performs. Considering an extreme case when there are two challenge points opposing each other, it is possible after k_max iterations, the algorithm can not find meaningful k_i for both points simultaneously. The paper needs to address the potential for conflicting poisoning needs across different challenge points. The current approach seems to assume that a single poisoning strategy can be effective for all challenge points, which may not be realistic. A more thorough analysis of the performance of Algorithm 2 under various correlation structures between challenge points is needed, including scenarios where the optimal poisoning strategies for different points are contradictory.

3. Clarity (minor points). The paper needs to improve the clarity. For example, many definitions are used without being defined, e.g., LIRA, challenge point, in+out model. It is better to provide those definitions in the preliminary to make the paper more self-contained.

### Questions
Please refer to the section above.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The key contribution of this paper is to present a poisoning strategy to enhance the success of label-only membership inference attacks. The paper first shows that an existing poisoning regime negatively impacts the label-only attack's success and proposes a new way to calibrate the number of poisoning points to inject. And then, the paper proposes a way to construct shadow models and perform membership inference. In evaluation, the paper demonstrates that poisoning can increase the TPR by an order of magnitude while preserving the model's performance. The paper also analyzes the impact of attack configurations and further tests if (and also shows) DP reduces the attack success.

### Strengths
1. The paper presents a new poisoning attack for enhancing label-only MIs.
2. The paper shows the poisoning can increase the attack success by 18x.
3. The paper is well-written

### Weaknesses
1. The poisoning seems to be a straightforward adaptation of Tramer et al.
2. The proposed label-only MI seems to be impractical.
3. (Sec 3.3) The claim about "theoretical" attack is unclear.


**[Straightforward Extension]**

Of course, existing poisoning could not work well against an adversary who only observes hard labels. The adversary cannot "exploit" the impacts of poisoning until there is a change in the target's label. If too many are injected, the attacker may not know whether the target is a member. So, in the label-only settings, the key is to calibrate the number of poisoning samples. It is therefore not surprising in Section 3.2 that an "adaptive" poisoning strategy is needed.


**[Practicality of This Poisoning]**

However, I believe that choosing the right threshold $t_p$ is more challenging than shown in this paper. The paper assumes that the adversary can know the "underlying distribution."

But considering that the label-only attacks are for studying the practicality in the "true black-box" settings (e.g., hard-labels), I wonder how well this attack can perform when there's a slight distributional difference between the training data an adversary uses and the victim's. Indirectly, the ablation study shows the proposed label-only attack is a bit sensitive to the choice of a poisoning threshold.

In practical scenarios, when a practitioner wants to check the risks of "practical" label-only membership leakage, the proposed attack may not be a useful one to use.


**[Theoretical Attacks (Sec 3.3)]**

(1) In most cases, the theoretical analysis means the best possible attack that an adversary can perform under a specific attack configuration. But I am not sure whether the paper presents the same.

(2) I am a bit unclear on how the paper theoretically analyzes the impact of poisoning samples on the leakage. It depends on many factors, such as the training data and/or the choice of a model and a training algorithm.

I think the section could a bit mislead readers.

### Questions
My questions are in the detailed comments in the weakness section.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a data poisoning attack, called Chameleon, to enhance the privacy leakage due to label only membership inference attacks. It first shows that current attacks that aim to enhance privacy leakage via poisoning are not effective in label-only MIA threat model. The attack fails because after poisoning both the IN and OUT models misclassify the target samples. To improve the attack efficacy, Chameleon tailors the number of replicas of poisoning samples for each challenge sample. The paper shows that such poisoning significantly improves label-only MIA accuracy especially at low FPRs.

### Strengths
- Chameleon idea is elegant and easy to implement
- Intuition and other aspects of the attack are well explained

### Weaknesses
 - Chameleon is an expensive attack
- I am not sure how will such attack be useful in practice due to the computations involved
- Some parts of the paper need to improve presentation, e.g., theoretical attack and figure 1

- For C100, Chameleon adds on average 0.6 replicas of poisoning samples, which means there are 40% data which need no poisoning. This means MIAs without any poisoning should work well. But this is not reflected in Table 1 results. Clarify.
- Minor: Given that modern ML systems have generally very large and multimodal models, it might be useful to have evaluations on large and/or multimodal models.

- Figure 1 is not readable: I could not understand what it is trying to convey. Please clarify
- Theoretical attack section currently does not clearly explain what is the attack and why this analysis is needed if the same conclusions can be drawn from empirical analysis.

- Given that label only attacks are designed to be more practical, how can attackers have the data from exactly the same distribution of the original training data? This is a strong assumption, and hence, can you provide some evaluations where attacker cannot have data from exactly the same distribution?

- Also, can you provide train and test accuracies of models you are attacking? Before and after poisoning? This is important because if for 500 challenge points, attacker introduces D_p of size 2000 (~10% of training data), and if that leads to poor model performances, such model will never be deployed, and hence, will not be available for attacker to query.

- If I understand correctly, this is a targeted label-only MIA where you report results only on the set of challenge points. If yes, how have you ensured significance of the results reported? Do you repeat the experiments before reporting results?

### Questions
The attack proposed is very elegant in that it is easy to implement and outperforms prior attacks. Also, the explanation of the attack is  clear and easy to understand. The paper also does a fair job in evaluating their proposed attack. Overall I think this is a good paper, but  I have the following concerns:

Attack computation cost and utility:
- Chameleon is an expensive attack given the number of models one has to train to find the right number of poisoning sample replicas. Can authors discuss the compute cost involved? I didn’t see any discussion in the main paper.
- Given the high computation cost and the fact that modern ML model architectures are generally huge, I wonder where will this attack be useful? Which type of adversaries can afford it? It will be good to clearly discuss these aspects.

Some concerns about the evaluations
- For C100, Chameleon adds on average 0.6 replicas of poisoning samples, which means there are 40% data which need no poisoning. This means MIAs without any poisoning should work well. But this is not reflected in Table 1 results. Clarify.
- Minor: Given that modern ML systems have generally very large and multimodal models, it might be useful to have evaluations on large and/or multimodal models.

Clarity of paper:
- Figure 1 is not readable: I could not understand what it is trying to convey. Please clarify
- Theoretical attack section currently does not clearly explain what is the attack and why this analysis is needed if the same conclusions can be drawn from empirical analysis.

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

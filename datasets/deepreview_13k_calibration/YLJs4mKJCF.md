# Towards Poisoning Fair Representations

- Decision: Accept
- Avg Score: 6.00
- Scores: 3, 5, 8, 6, 8

## Abstract
Fair machine learning seeks to mitigate model prediction bias against certain demographic subgroups such as elder and female. 
Recently, fair representation learning (FRL) trained by deep neural networks has demonstrated superior performance, whereby representations containing no demographic information are inferred from the data and then used as the input to classification or other downstream tasks. 
Despite the development of FRL methods, their vulnerability under data poisoning attack, a popular protocol to benchmark model robustness under adversarial scenarios, is under-explored. Data poisoning attacks have been developed for classical fair machine learning methods which incorporate fairness constraints into shallow-model classifiers.
Nonetheless, these attacks fall short in FRL due to notably different fairness goals and model architectures. 
This work proposes the first data poisoning framework attacking FRL. We induce the model to output unfair representations that contain as much demographic information as possible by injecting carefully crafted poisoning samples into the training data.
This attack entails a prohibitive bilevel optimization, wherefore an effective approximated solution is proposed. A theoretical analysis on the needed number of poisoning samples is derived and sheds light on defending against the attack. Experiments on benchmark fairness datasets and state-of-the-art fair representation learning models demonstrate the superiority of our attack.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The authors propose a poisoning attack strategy to compromise fair representation learning, aiming to increase the fairness gap for underprivileged groups. The attack relies on approximations to solve a bilevel optimization problem where the outer problem, which describes the attacker’s objective, aims to maximize the mutual information between the representation for the privileged and the underprivileged groups. Since the optimization of this objective is not tractable, the authors use Fisher’s Linear Discriminant (FLD) score as a proxy. Then, the whole bilevel optimization problem is approximated using a gradient matching strategy. The authors also provide some theoretical analysis on the poisoning ration required to compromise the target models.

### Strengths
+ Poisoning fair representations have received less attention in the research literature on data poisoning and preliminary works show that these attacks can have a significant impact on the fairness of the target algorithms. Exploring more scalable poisoning attack strategies capable of increasing the fairness gap for deep neural networks is timely and a topic of interest. 

+ The authors strived to provide a theoretical analysis on the ratio of poisoning points required to compromise the target algorithms.

### Weaknesses
 + The paper lacks a clear threat model. For example, it is unclear whether the attacker’s objective is useful for compromising algorithms with and without mechanisms for mitigating the fairness gap. On the other side, it is unclear what is the attacker’s objective and the relation of the attack strategy with respect to the model’s performance. Other works in the research literature, like Chang et al. or Van et al. (“Poisoning Attacks in Fair Machine Learning”) have already considered the trade-off between targeting performance and the fairness gap. 

+ In the end the attack proposed by the authors rely on the maximization of the FLD score in the outer optimization objective. This relies on strong assumptions on the distribution of the data and its representation and may not hold for many practical scenarios. In this sense, it is unclear why this strategy is better compared to other attacks already proposed in the research literature, like Solans et al., Mehrabi et al., Chang et al., or Van et al. (“Poisoning Attacks in Fair Machine Learning”), which have strong connections to this work. On the other side, there is not mention to “Subpopulation Poisoning Attacks” by Jagielski et al., which are also very relevant to this work and proposes more scalable alternatives for crafting poisoning attacks targeting fairness. 

+ Given the existing works in the research literature, I believe it is to bold that the authors claim that “We propose the first data poisoning attack on FRL as outlined in Figure 1.” I think that the authors should clarify this and position better their paper and contributions with respect to other existing works. 

+ The experimental evaluation is not convincing: In the experiments the authors just reported results evaluating the BCE loss but did not consider any of the existing metrics for measuring the fairness gap. On the other hand, there is not mention to how the attack affects the accuracy at all. Apart from that, it is necessary a more comprehensive comparison with other methods in the research literature, e.g., Solans et al., Chang et al. Van et al. (“Poisoning Attacks in Fair Machine Learning”), Jagileski et al. (“Subpopulation Poisoning Attacks”). For some of these attacks, the authors can use the same outer objective and use the same approximation for solving the bilevel optimization problem. 

+ The authors used a gradient matching strategy for approximating the solution of the bilevel optimization problem. However, Jagielski et al. (“Subpopulation Poisoning Attacks”) shows that other strategies can be more efficient for this. I think this aspect requires further analysis. 

+ The authors say: “Heuristics such as label flipping (Mehrabi et al., 2021) lack a direct connection to the attack goal, thereby having no success guarantee and often performing unsatisfactorily.” I think this is not true. Although more limited on the attacker’s capabilities, smart manipulation of the labels can lead to successful attacks. See for example “Subpopulation Poisoning Attacks” by Jagielski et al.

### Questions
+ Equation (2) relies on strong assumptions about the distribution (Gaussian distribution and continuous variables) of the different subpopulations. How is this a good proxy for approximating the original problem? How does this compare with existing attacks (as the ones mentioned before)?

+ Could the authors provide more details on the threat model (see comments above)?

+ How assumption 2 works in the current threat model for the attack? The authors say: “Before the attack, the victim is well trained.” What does this mean?

+ Also, for the theoretical analysis: Why do the authors think that assumption 3 is reasonable?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies data poisoning attacks against fair representation learning (FRL) on deep neural networks. To achieve the attack goal, the authors propose a new MI (mutual information) maximization paradigm. Besides, the experiments show that the proposed attack outperforms baselines by a large margin and raises an alert of the vulnerability of existing FRL methods.

### Strengths
This is a pioneering data poisoning attack on deep learning-based fair representation learning to degrade fairness while the existing fairness attacks are focusing on shallow-model classifiers. 

The authors propose a new attack goal based on MI to amplify the difference between representations from different subgroups. 
The authors derive the first theoretical minimal number of poisoning samples required by their attack, which is crucial for practical attacks.

### Weaknesses
The assumption of the threat model is strong. The proposed attack is under the assumption of a white-box threat model, where the attacker has full access to and control over the victim's trained model. This implies that the attack is primarily effective in scenarios where the victim has already trained a model and relies on the attacker's data for subsequent fine-tuning. Such a specific condition might limit the general applicability of the attack in diverse real-world scenarios.

Lack the reason why the method can attack FRL. The foundational principle of Fair Representation Learning (FRL) is to ensure fairness by removing sensitive features from the intermediate representation. The proposed attack, on the other hand, seeks to amplify the presence of sensitive information within these representations. The paper does not adequately elucidate why FRL techniques, designed to minimize sensitivity, are unable to counteract or mitigate the effects of the proposed attack. This leaves a gap in understanding the inherent vulnerabilities of FRL against the described attack strategy.

### Questions
Similar to weakness 1, could the authors clarify their threat model more clearly? Specifically, does the attacker need to know the victim’s trained model to generate poisoning data? If not, does the attacker only need to know the structure of the victim’s model and the model will be trained on the poisoning data from the attacker?

Similar to weakness 2, could the authors give more insight to explain why their attack cannot be mitigated by fair representation learning (FRL)?

Could the proposed attack be applied to deeper neural networks? The experiments of this paper are just on two-hidden layer CNNs.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This study proposes a novel data poisoning attack against fair representation learning algorithms. Compared to previous attack methods against fair classification, this method proposes to craft the training dataset, in order to maximize the mutual information between the learned representation and sensitive raw features. This mutual information powered attack algorithm shows superior attack performances compared to anchor attacks against 4 different fair representation learning methods.

### Strengths
1/ This is the first research effort in organising data poisoning attacks against fair representation learning attacks. Different from fair classification problems, manipulating fair representation needs to control the statistical relation between high-dimensional embeddings  and raw feature inputs. This is challenging for directly extending previous fair learning poisoning methods. I'd appreciate the efforts poured towards this difficult problem. 

2/ It is intuitive to increase the mutual information between the embeddings and sensitive raw features, in order to violate the fairness constraint of the victim embedding learning algorithm. However directly maximising mutual information of high-dimensional embeddings is very difficult. I know there are some differentiable approximation tool to MI, like MINE. But it is computationally costly and prone to the potential estimation gap. It is interesting to read the theoretical analysis and practices of using Fisher Linear Discriminator scores to bound MI. Apparently, optimising FLD scores is much easier and economic in computation. 

3/ Inspired from Geiping et al's gradient matching work, this study propoes to matching the upper and lower bound of gradients instead of solving the bi-level poisoning problem. This smart optimization strategy enables an analytical solution to the proposed attack.

### Weaknesses
One of the problem of introducing elastic penalty is how to choose properly the two penalty parameters $\lambda_{1}$ and $\lambda_2$. Though it can be chosen empirically, it can be dataset-dependent. Would it make significantly difference if we simply choose the L1 norm penalty instead?

### Questions
Discussion over the choice of the two penalty parameters $\lambda_{1}$ and $\lambda_2$ in the elastic penalty.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work studies an interesting topic i.e. how to conduct data poisoning against fair representation learning tasks. Experiments are conducted on Adult and German datasets to demonstrate its effectiveness.

### Strengths
- Motivation is well-stated and interesting.
- Authors develop related  theoretical analysis on the needed number of poisoning samples is derived and shed light on defending against the attack.
- Personally I like the organization of Introduction section : ) It's clear and easy for reviewers to know the meaning of this work.

### Weaknesses
 - Authors use their own defined vanilla metric, and lack related fairness-aware metrics like Equality odds (EO)
- Authors are encouraged to conduct more experiments on more datasets like COMPAS and Drug Comsumptionm, please kindly follow this AAAI paper which authors have cited: Exacerbating Algorithmic Bias through Fairness Attacks.
- Personally, I reckon authors are encouraged to conduct experiments on deeper NN (I think simple MLP is not that DEEP to be called "DNN"), though the datasets are relatively simple. I'm curious about these experiments to investigate ENG. Authors are encouraged to conduct more analysis on the further version of this work, which is good for community : )

### Questions
See above.

### Soundness
3 good

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper designs a new data poisoning attack tailored for fair representation learning. The key idea is to generate poisoning samples that maximizes the mutual information between the representation (of the poisoned sample) and the sensitive attribute. This can be solved by bi-level optimization, yet the outer level problem (estimating high-dimensional mutual information) is intractable. To solve this issue, the authors propose to use Fisher’s linear discriminant (FLD) score as a cheap proxy to MI, which has a closed-form solution. For inner level problem, it is solved by matching the gradients of a victim model and a clean model. Through the approximations made, the original objective is now fully tractable and can be learned by SGD. The effectiveness of the method is evaluated on two tabular datasets.

### Strengths
- **Significance**: The problem studied in this paper (data poisoning to attack the learned representation in fairly trained models) is interesting and important;
- **New information-theoretic viewpoint for poisoning attack**: The authors propose an information-theoretic objective for poisoning attack in fair machine learning. This framework, to the best of my knowledge, is new within the specific context considered and is very-well motivated. The reminder on the advantage of MI-based fairness as compared to conventional metric (e.g. DP) is also useful;
- **Cheap proxy to mutual information**: I also like the authors’ idea to use Fisher’s linear discriminant analysis (FLD) as a cheap-but-still-effective proxy to MI. I would also highly praise the authors’ efforts to mention the possibilities of other analytic proxies, as well as a discussing between FLD and these alternative methods. 
- **Feature selection for fairness**: in addition to the main contribution, the authors also show how their developed attack can be further applied to identify robust features for fair classification. This is quite interesting, especially in that it offers a new perspective for understanding and interpreting the behavior of a fairly trained model. I personally think this part deserves a separate section and can be highlighted as a 2nd main contribution of the paper.

### Weaknesses
 - **On the necessity of working at representation level**. After reading the paper, it is still unclear to me why do we need to consider I(Z; a) rather than I(Y(X); a). Here Y(X) is the prediction of the model. In fact, considering I(Y(X); a) has several benefits: first, its maximization still yields an unfair model; second, its estimation is much easier due to the low-dimensionality of Y(X) and a (for example, we can estimate it easily by the well-known KSG estimator [1] which typically works quite well in low-dimensional cases). Importantly, maximizing I(Y(X); a) also do not require an access to Y. Can the authors justify the reason behind considering I(Z; a) instead?

- **Issues in the discussion related to other MI proxies**: some comments in remark 2.1 do not seem completely sensible to me. For example, the author mention that other analytical proxies like (K)CCA and sliced mutual information suffer from differentiation difficulties. This may not be true in my view (for example, in CCA, you can first solve the optimal weights analytically, then substitute it back to the formula of CCA. The resultant formula has a structure very similar to eq2 in your paper). In addition, I think the authors miss the possibility of using non-parametric dependence measure e.g. distance correlation (dCorr) [2]. This is also fully analytical and may potentially be applicable in your scenario. Ultimately, I think the real advantage of your FLD-based method is it provably optimises a variational lower bound of MI, whereas other proxies (KCCA, slice MI, dCorr) may not. This seems to be a better justification of the use of your method. 

- **Slightly limited evaluation**: most of the evaluations in this work are conducted on tabular data where the network size is small. Whether the method developed in this work will scale to larger networks e.g. those in computer vision and NLP remain unclear to me. However, given the nature of many existing literature in fairness research, which also only focus on tabular data, this should not be a main criticism for the paper.

### Questions
How does the proposed FLD-based method scale with the dimensionality of representation d? I am concerned about this since Gaussianity assumption typically violates in high-dimensional cases. Will the method still work well for e.g. d=128?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

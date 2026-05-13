# PN-GAIL: Leveraging Non-optimal Information from Imperfect Demonstrations

- Decision: Accept
- Scores: 8, 6, 6, 8

## Abstract
Imitation learning aims at constructing an optimal policy by emulating expert demonstrations. However, the prevailing approaches in this domain typically presume that the demonstrations are optimal, an assumption that seldom holds true in the complexities of real-world applications. The data collected in practical scenarios often contains imperfections, encompassing both optimal and non-optimal examples. In this study, we propose Positive-Negative Generative Adversarial Imitation Learning (PN-GAIL), a novel approach that falls within the framework of Generative Adversarial Imitation Learning (GAIL). PN-GAIL innovatively leverages non-optimal information from imperfect demonstrations, allowing the discriminator to comprehensively assess the positive and negative risks associated with these demonstrations. Furthermore, it requires only a small subset of labeled confidence scores. Theoretical analysis indicates that PN-GAIL deviates from the non-optimal data while mimicking imperfect demonstrations. Experimental results demonstrate that PN-GAIL surpasses conventional baseline methods in dealing with imperfect demonstrations, thereby significantly augmenting the practical utility of imitation learning in real-world contexts. Our codes are available at https://anonymous.4open.science/r/PN-GAIL-3828.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This work addresses imitation learning from imperfect demonstrations, utilizing both confidence-labeled noisy demonstrations and unlabeled noisy demonstrations. It aims to overcome two primary limitations of prior work, specifically 2IWIL [A], a representative approach to this problem that employs a two-step learning process: (i) semi-confidence labeler training on the unlabeled dataset, and (ii) confidence-based generative imitation learning.

The proposed method, PN-GAIL (Positive-Negative GAIL), tackles the limitations of 2IWIL as follows:

1. **Incorporating Negative Risk to Objective**: 2IWIL overlooks the negative risk associated with imperfect demonstrations, leading the discriminator to disproportionately prioritize the positive risk of frequent samples. PN-GAIL addresses this by incorporating both positive and negative risks into the confidence-based imitation learning objective, ensuring a more reliable evaluation regarding to demonstration quality.
2. **Balanced Semi-Confidence (BSC) Classification**: In 2IWIL, semi-confidence (SC) classification is used to train a confidence labeler for unlabeled demonstrations. However, SC classification tends to overestimate the confidence of labeled data and underestimate the confidence of unlabeled data. To address this, PN-GAIL introduces a balanced semi-confidence (BSC) objective and further suggests near-optimal values for hyperparameters $\alpha$ and $\beta$, enhancing practical applicability.

[A] Wu et al., "Imitation Learning from Imperfect Demonstration," ICML 2019.

### Strengths
This work is well-motivated and effectively addresses the challenges presented in the previous study using sound methods.

A notable strength of this work is its practice-oriented design of the objective functions, which enhances applicability in real-world scenarios.
This study removes the dependence on $\eta$, the class prior $p(y=0)$ for imperfect demonstration datasets, from the primary objective. 
Since $\eta$ is generally unknown and challenging to estimate, prior work treated it as a hyperparameter, requiring practitioners to invest substantial effort in tuning it. 
By eliminating this reliance, the proposed approach reduces the overhead associated with hyperparameter optimization.

Additionally, the authors introduce near-optimal and practical choices for the parameters $\alpha$ and $\beta$ in the Balanced Semi-Confidence (BSC) objective, which can be straightforwardly calculated based on the dataset sizes $n_c$ (confidence-labeled) and $n_u$ (unlabeled). 
This adjustment simplifies the implementation process and supports the broader applicability of imitation learning with imperfect demonstrations in practical settings.

Furthermore, the manuscript includes theoretical analyses showing that (i) the proposed objective helps avoid the imitation of non-optimal data and (ii) derives a sample complexity bound for the BSC method, providing a rigorous foundation for the proposed improvements.

### Weaknesses
Despite the many strengths of this work, the empirical results presented in the manuscript do not stand out as particularly impressive.

Specifically, Figure 1 shows that the performance difference between PN-GAIL and the most competitive baseline across tasks is not significant. In my opinion, as discussed in Section 2, since baseline methods typically assume a dominant proportion of $\pi_{opt}$, exploring scenarios with a more skewed ratio (e.g., $\pi_{opt}:\pi_1=1:10$) might provide a more notable results where conventional methods fail while PN-GAIL successes. 
I think conducting experiments with more extreme demonstration ratios could more clearly demonstrate the scenarios in which PN-GAIL offers a distinct advantage over baseline methods.

**[Minor Comments]**
1. For Figures 2, 3, and 4, using distinct line colors for different methods would enhance readability.
2. In the ablation study presented in Figure 3, it would be advantageous to include results from 2IWIL—even though they are already provided in Figure 2. Since 2IWIL represents a variant of PN-GAIL that excludes both the PN objective and the BSC, its direct comparison within the same figure would clarify the incremental benefits of these components.

### Questions
Q1. In contrast to scenarios where $\pi_1$ dominates, how would the results in Figure 2 be affected if $\pi_{opt}$ were dominant, a condition under which existing methods are known to perform well? Results for PN-GAIL in the Pendulum-v1 task with various $\pi_{opt}:\pi_1$ ratios are presented in Figure 7 of the supplementary material, but a more systematic comparison between PN-GAIL and baseline methods could strengthen the manuscript. If PN-GAIL demonstrates robust performance and outperforms the baseline methods in such scenarios, it would confirm the method's reliability. This evidence would support the assertion that PN-GAIL performs consistently well across a range of dataset quality distributions, thus setting it apart from existing methods.

Q2. Instead of modifying the $\pi_{opt}:\pi_1$ ratio while maintaining a fixed total number of demonstrations, what would occur if the optimal demonstrations was kept invariant while the number of suboptimal demonstrations was varied? This setup would illustrate how PN-GAIL effectively utilizes additional suboptimal demonstrations, isolating the influence of optimal demonstrations on imitation performance. It would offer valuable insights into PN-GAIL’s ability to adapt to and leverage diverse demonstration qualities effectively.

### Soundness
3

### Presentation
4

### Contribution
4

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces an IL method that handles imperfect demos by including both the optimal and non-optimal data in training, assuming that the demos come with a confidence score. The goal is to improve policy learning when demos aren’t perfectly optimal. The method assigns weights to optimal and non-optimal examples through a semi-supervised confidence classifier.  Experiments on six control tasks show that PN-GAIL performs better than standard GAIL and other baselines under these imperfect conditions.

### Strengths
* Originality: The use of positive and negative risks to manage imperfect demos tackles some of the real-world problems of non-optimal data in a practical way.
* Quality: The paper provides theoretical analysis for the positive-negative risk approach and shows experimental results across multiple control tasks.
* Clarity: Most theoretical ideas are clearly presented with good notation.
* Significance: The approach is relevant for real-world applications. It might have a real impact on the usability of IL in practical scenarios.

### Weaknesses
 * The method’s reliance on confidence scores may limit its applicability when it’s difficult to assign confidence levels directly. Human annotation of preferences over trajectories, for instance, might be more feasible than assigning explicit confidence scores.
* The fundamental motivation of this paper is based on a claim that 'GAIL treats non-optimal demonstrations as if they were optimal'. I disagree with this claim. GAIL’s objective is to minimize the JS divergence between the expert and agent trajectory distributions, aiming to reproduce the overall distribution of expert demonstrations. When the agent policy is close to the expert policy, the discriminator's output tends to be 0.5 everywhere. If expert demos include a mix of optimal and sub-optimal trajectories, GAIL should naturally capture this mixture without necessarily assuming optimality. Could you provide a counterargument or clarification on why PN-GAIL’s approach is necessary, given this perspective?
* Lacks comparison with other advanced IL algorithms, such as f-IRL.
* Theorem 1’s bound relies on knowing the variances. However, the variances can be difficult to estimate in real-world applications. Given this dependency, how practically useful is the bound in scenarios where variance values are unknown or hard to assess?
*  Theorem 2’s bound may become quite loose if the Rademacher complexity is high, as is typical with deep and wide neural networks. Could this have negative implications for the method's reliability when using complex models?

### Questions
* Theorem 1’s bound relies on knowing the variances. However, the variances can be difficult to estimate in real-world applications. Given this dependency, how practically useful is the bound in scenarios where variance values are unknown or hard to assess?
*  Theorem 2’s bound may become quite loose if the Rademacher complexity is high, as is typical with deep and wide neural networks. Could this have negative implications for the method's reliability when using complex models?
* Related to my disagree on the claim that 'GAIL treats non-optimal demonstrations as if they were optimal' in the weaknesses section, please could you provide a counterargument?

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
4

### Summary
The authors propose PN-GAIL, an extension of the GAIL framework designed to handle the imperfect expert demonstrations. By predicting confidence scores for unlabeled data, PN-GAIL allows for more accurate imitation learning without relying solely on optimal examples. Theoretical analysis is provided for the output of the optimal discriminator in the proposed method.

### Strengths
This paper introduces a new algorithm (based on 2IWIL and IC-GAIL) supported by theoretical analysis and demonstrates its effectiveness across multiple tasks. Experiments are extensive, including different benchmarks, different $\pi_{OPT} : \pi_{1}$ ratios, different standard deviations of Gaussian noise.

### Weaknesses
Although the proposed method is based on [1], e.g., some techniques to prove Theorem 4.1, Theorem 4.2, have been explored in [1], this study sill broadens the scope of [1]. One potential weakness is: although $\alpha$ and $\beta$ are intended to play distinct roles in Theorem 4.2, they are selected to be identical in Algorithm 1, which may affect the overall applicability of the algorithm.

### Questions
1. Could the authors highlight expert performance more prominently in the figures to enhance clarity and interpretability?

2. Would varying values of $n_{u}$ and $n_{c}$ significantly impact the performance of the proposed method? Additionally, could the authors provide guidelines or criteria for selecting optimal values for these parameters in practice?

3. Figure 1 offers a valuable comparison of the proposed method against GAIL and 2IWIL. To further support this comparison, it would be better if the authors could also provide more intuition of why GAIL and 2IWIL fail but the proposed method succeed. E.g., gradient colors for different confidence scores, and why 2IWIL fails to predict them. Additionally, Why GAIL predicts 5.0 for some of theses data points?

4. To further contextualize this work within imitation learning (specifically, driver behavior imitation), it would be beneficial to incorporate additional relevant studies, such as:

[2] Ruan, Kangrui, and Xuan Di. "Learning human driving behaviors with sequential causal imitation learning." Proceedings of the AAAI Conference on Artificial Intelligence. Vol. 36. No. 4. 2022.

[3] Hawke, Jeffrey, et al. "Urban driving with conditional imitation learning." 2020 IEEE International Conference on Robotics and Automation (ICRA). IEEE, 2020.

and so on.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
Motivated by the limitation of 2IWIL in a type of scenario where certain non-optimal demonstrations have high probabilities of appearing in a set of imperfect (unlabeled) demonstrations, the paper proposes a new method named PN-GAIL, better leveraging optimal and non-optimal information from imperfect demonstrations to learn optimal reward and policy by assessing both positive and negative risks. Moreover, the paper modifies semi-conf classification in 2IWIL to establish balanced semi-conf classification to handle better the cases where certain demonstrations only exist in the confidence (known, labeled) data.

The authors conduct experiments, comparing their PN-GAIL to four baseline methods across six environments. The results show that PN-GAIL alleviates the impact of the unbalanced frequency in impact demonstrations, outperforms other methods, and maintains relatively good performances given the decreasing number of labels. Also, the outcomes demonstrate that the balanced semi-conf classifier improves performances, particularly in three out of six environments.

### Strengths
1. The main objective/purpose of this paper is articulated explicitly with the existing methods and their limitations highlighted clearly.
2. The literature review on IL, GAIL, and IL with imperfect information is comprehensive. The preliminaries provide the essential information of 2IWIL.
3. The theoretical derivations regarding the discriminator modification and classification refinement are straightforward and concise in the main body, which makes audience easy to follow; meanwhile, the supplemental materials in the appendices provide necessary, detailed explanations.
4. The experiments with three goals setup are tightly related to the main achievements that the paper wants to claim. The experiments are conducted with representative benchmarks across various environments, effectively showing the performances with well-formatted figures and table in the main context.
5. Overall, the authors identify the potential challenges of 2IWIL about certain non-optimal data with high frequencies in an unlabeled demonstration set significantly affecting reward and policy generation. The topic is likely to be of interest to a large proportion of the community. The proposed PN-GAIL creatively update the previous methods to successfully remove limitations of prior IL results to a certain extent.

### Weaknesses
1. Missing definition: in Section 3, what δ represents. Please define δ when it is first introduced in the paper.

2. Needing clarification: PN-GAIL\BSC: PN-GAIL without balanced semi-conf (BSC) classification--does this mean no classification used or SC used? Without a probabilistic classifier, how to obtain confidence scores? Please explicitly state whether a SC classification is used, and to explain how confidence scores are obtained if no classifier is used. 

3. Lack of analysis for experimental outcomes: it is necessary to provide more detailed explanations and discussions regarding those figures. For example, in Figure 3 what possible reasons (e.g., characteristics of each environment? limited number of demonstrations?) are that result in the varying performance patterns across six environments. We can observe that in some cases three colors (methods) are similar; in some cases blue and green are close; in some cases, blue and orange are close; while in some cases, blue works best. Please provide a systematic analysis of how different factors might contributing to these patterns.

### Questions
1. About clarification: PN-GAIL\BSC: PN-GAIL without balanced semi-conf (BSC) classification--does this mean no classification used or SC used? Without a probabilistic classifier, how to obtain confidence scores?   

2. To verify BSC outperform SC in 2IWIL, straightforward comparisons are PN-GAIL(BSC) vs. PN-GAIL(switch to SC) vs. 2IWIL(switch to BSC) vs. 2IWIL(SC). Why do you consider the way of comparisons that are presented in the paper?

3. It is better to provide more detailed explanations and discussions regarding those figures. For example, the statement about Figure 3 is quite short. The audience would like to learn about what possible reasons are that result in the varying performance patterns across six environments in Figure 3. We can observe that in some cases three colors (methods) are similar; in some cases blue and green are close; in some cases, blue and orange are close; while in some cases, blue works best. Could you provide a systematic analysis?

### Soundness
4

### Presentation
4

### Contribution
3

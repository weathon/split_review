# Defending Membership Inference Attacks via Privacy-aware Sparsity Tuning

- Decision: Reject
- Avg Score: 4.75
- Scores: 8, 3, 3, 5

## Abstract
Over-parameterized models are typically vulnerable to membership inference attacks, which aim to determine whether a specific sample is included in the training of a given model. Previous Weight regularizations (e.g., $\ell_1$ regularization) typically impose uniform penalties on all parameters, leading to a suboptimal tradeoff between model utility and privacy. In this work, we first show that only a small fraction of parameters substantially impact the privacy risk. In light of this, we propose Privacy-aware Sparsity Tuning (\textbf{PAST})—a simple fix to the $\ell1$ Regularization—by employing adaptive penalties to different parameters. Our key idea behind PAST is to promote sparsity in parameters that significantly contribute to privacy leakage. 
In particular, we construct the adaptive weight for each parameter based on its privacy sensitivity, i.e., the gradient of the loss gap with respect to the parameter.
Using PAST, the network shrinks the loss gap between members and non-members, leading to strong resistance to privacy attacks. Extensive experiments demonstrate the superiority of PAST, achieving a state-of-the-art balance in the privacy-utility trade-off.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper introduces Privacy-aware Sparsity Tuning (PAST), a defense mechanism against membership inference attacks (MIAs). The method relies on a key observation that only a small fraction of model parameters significantly contribute to privacy risk, measured by the loss gap between member and non-member data. PAST modifies traditional L1 regularization by applying adaptive penalties to different parameters based on their *privacy sensitivity* - how much they contribute to the member/non-member loss gap. Parameters with higher privacy sensitivity receive stronger regularization, while less sensitive parameters are spared to maintain model utility. The method is implemented as a simple fine-tuning phase after regular training. Authors perform extensive experiments on multiple datasets (Texas100, Purchase100, CIFAR-10/100, ImageNet) and various attack methods. PAST demonstrates superior privacy-utility trade-offs compared to existing defenses, while preserving accuracy. The method is also compatible with and can enhance other existing MIA defenses.

### Strengths
I believe it is a very strong paper. It combines an interesting and novel observation (privacy sensitivity is distributed unevenly across model parameters) with a simple yet effective method to utilise this observation to solve a concrete and well-known problem of defending against MIAs. The empirical evidence is also thorough and convincing.

* The paper uses clever technique - computing gradient of the loss gap - to estimate each individual parameter's contribution to the privacy risk. It yields an interesting and novel quantification of per-parameter risk, and shows that only a few parameters need to be regularized to mitigate a privacy risk
* The proposed method (PAST) is a simple yet effective adaptation of L1 regularization, making it easy to implement in practice. Additionally, authors shown computational overhead of adopting PAST to be low compared to the overall training cost.
* The evaluation setup is appropriate and convincing. Specifically, Figures 3 and 4 show the trade-off between attack advantage and model accuracy - which is probably the best way to assess and visualise risks associated with an MIA. Evaluations cover a wide range of MIAs and MIA defences.
* The results show PAST method to be strictly better than other MIA defences and regularization methods in improving privacy-utility trade-off.

### Weaknesses
As far as I can see, authors do not consider SOTA shadow-model based attacks like LiRA ([Carlini et al., 2022](https://arxiv.org/abs/2112.03570)) and Attack R ([Ye et al., 2022](https://arxiv.org/abs/2111.09679)). It would be important to understand whether their findings hold for a strong MIA adversary capable of trainings shadow models.



### Questions
* How does privacy sensitivity distribution (Fig. 1b) changes throughout PAST training? Similar to the privacy onion effect ([Carlini et al., 2022](https://arxiv.org/abs/2206.10469)), do you think the privacy could "migrate" from parameters you heavily regularize to other parameters?
* Can you clarify the computational aspects of the regularization process?
	* How do you compute $\gamma_i$ in (3)? Do you run an additional forward pass for non-members $\mathcal{S}_n$? If so, an increase of only 10% on the training time is a bit surprising, since you're effectively doubling the size of a batch, and run both forward and backward pass on it.
	* In the equations for $\gamma_i$ does $\nabla_{\theta_i} \tilde{\mathcal{G}_\theta}$ refer to the gradient norm?
* To clarify the experimental setup (4.1, Datasets). Do you use different non-member sets for PAST training and MIA evaluations?

### Soundness
3

### Presentation
4

### Contribution
4

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper aims to defend against membership inference attack using sparsity tuning.

The basis intuition is that not all model parameters are equally sensitive in terms of privacy, by empirical analysis the authors found that only a small fraction of parameters are responsible for privacy leakage.   The main idea of mitigation strategy is to prompt sparsity in the model parameter, with the aim of balancing both utility and privacy. Consequently, the sparsity regularization encourages the sensitive parameters to become small, thereby decreasing vulnerability to MIAs.

### Strengths
The authors perform a through analysis on the distribution of model parameters and its effects on privacy attacks. It is expected to see that only a small portion of parameters contribute to the privacy  leakage. The following sparsity technique also makes sense.

### Weaknesses
While I agree that in general the average loss of members and non-members are different, shrinking  this gap with  the proposed sparsity technique can be effective to those loss-based (or related) MIAs. But it may not be able to defense against  other more advanced state of the art MIAs. Here are my two main concerns:

1. The evaluation metric for privacy is out of dated, this metric has been criticized in many recent MIAs 
[R1] D. Hintersdorf, L. Struppek, and K. Kersting, “To trust or not to trust prediction scores for membership inference attacks,” in IJCAI, 2022
[R2] S. Rezaei and X. Liu, “On the difficulty of membership inference attacks,” in IEEE Conf. Comput. Vis. Pattern Recog. (CVPR), 2021
[R3] N. Carlini, S. Chien, M. Nasr, S. Song, A. Terzis, and  F. Tram `er, “Membership inference attacks from first principles,” in IEEE Symposium on Security and Privacy (S&P). IEEE, 2022

I suggest the authors to test the performance using TPR at low FPR rates for assessing the privacy risks.

2. The evaluated MIAs are also out of dated, most of them are metric based MIAs. Their performances are very close to each other and more importantly, these attacks often produce misleading results, which have been extensively explored in 
[R4] Li, Xiao, et al. "On the privacy effect of data enhancement via the lens of memorization." IEEE Transactions on Information Forensics and Security (2024).
[R5] Aerni, Michael, Jie Zhang, and Florian Tramèr. "Evaluations of Machine Learning Privacy Defenses are Misleading." arXiv preprint arXiv:2404.17399 (2024).

I suggest the authors to adopt more state of the art MIAs for example LiRA [R6]  and 
RMIA [R7] because there are shown to be effective in the TPR at low FPR regions. More importantly, the results of these attacks, particularly LiRA, align consistently with the definition of privacy risk, as well as with the concepts of differential privacy and memorization degree [R4, R5]. This contrasts with the deployed metric-based MIAs, which often yield misleading results by acting as strong non-member detectors. The reason for this discrepancy is that metric-based MIAs typically exploit the fact that models are more confident in members than non-members. However,  this confidence does not hold at a more nuanced level; members with high privacy risk are often difficult and atypical samples, which tend to have low confidence and are therefore frequently misclassified as non-members.

### Questions
How would you expect the trade-off between privacy and utility after adopting new evaluation metric and MIAs?

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes an approach called PAST. Instead of using uniform penalties, the PAST identifies and raises sparsity in parameters, which significantly contributes to privacy leakages. The paper uses the loss gap as the functional proxy of the privacy loss captured by the attack advantage. The weight for each parameter is set adaptively based on its privacy sensitivity defined as the gradient of the loss gap with respect to the parameter.

### Strengths
This paper acknowledges the different impacts of parameters on privacy leakage and proposes an adaptive approach to promote privacy-aware weight specifications for each parameter. This is an important consideration for privacy protection. In addition, the paper involves extensive numerical experiments to show the superiority of the proposed PAST.

### Weaknesses
There are flaws and issues in the motivation of considering the loss gap, the consistency between the attacker advantage and the loss gap as the functional proxy of privacy risk, the experimental setup, and the characterizations related to the privacy-utility tradeoff.

Comment 1:

The rationale for using the loss gap as a proxy risk for privacy is unclear. Specifically, the referenced paper (Sablayrolles et al., 2019) considers a specific case in which the posterior in Eq. (1) is modeled as a Boltzmann distribution, creating a direct link between the loss function and the posterior distribution. Generally, the posterior distribution is crucial in characterizing privacy risk. The work by Sablayrolles et al. (2019) assumes a direct connection between the loss function and privacy risk, with all results depending on this assumption, which does not extend to general loss functions. Therefore, using the statement, “It has been shown that the loss function can determine the optimal attacks in membership inference (Sablayrolles et al., 2019),” as justification for adopting loss gaps as a proxy for privacy loss is questionable and insufficient. In addition, the paper does not theoretically or analytically characterize the rationale for using the loss gaps as a proxy of the privacy risk in terms of attacker advantage.  

In experiments, three classes of MIA models are considered. However, the use of the loss gap as a proxy for privacy risk does not fully coincide with the privacy risk induced by these MIA models. In particular, the loss gap captures the average loss distinguishability between the member and the non-member. However, different MIA models including the three considered use a range of observations, including logits, confidence, entropy, correctness, and augmented predictions. These observations (of the attacker) capture different aspects of the mechanism's/model's output and behavior beyond just the loss values. As a result, the privacy risk represented by these attacks may involve patterns in these observations that a simple loss gap does not fully capture. For example, the augmentation-based attack depends on how the model responds to augmented inputs, which can reveal membership through consistency in the model's behavior across transformations. Loss gap does not capture this aspect of the model's sensitivity to augmented variations, so it might underestimate privacy risk in such scenarios.

Thus, it is in general possible for two different weight schemes with similar loss gaps to exhibit notably different attacker advantages.

Comment 2:

My concern regarding the feasibility of using loss gap as a proxy of privacy risk leads to the concern of adaptively setting the parameter weights based on the privacy sensitivity (i.e., the gradient of the loss gap w.r.t. the parameter). That is, the gradient might not precisely reflect the privacy sensitivity. It is suggested to provide analytical and theoretical characterizations for the feasibility of using loss gap as a proxy of privacy risk, including the possible assumptions. 


Comment 3:

The comparison between the PAST and the uniform-penality-based $\ell_1$ and $\ell_2$ baselines (or uniform baselines) needs more details. The paper clearly describes the difference between PAST and uniform baselines in terms of whether the weights of the parameters are uniform or privacy-aware. However, the impact of the magnitude of the weights on privacy risk is ignored (correct me if I am missing anything). 

Q1: In Figure 3 and Figure 4, what are the values of lambdas chosen for $\ell_1$ and $\ell_2$ baselines?

Q2: Is it possible that the performance differences between PAST and the $\ell_1$ and $\ell_2$ baselines shown in Figure 3 and Figure 4 are due to the combination of the magnitude of the weights and setting of uniform or privacy-aware penalties, rather than due to the setting of uniform penalties or privacy-aware alone?

It is intuitive that properly weighting the more-privacy-sensitive parameters more than the less-privacy-sensitive parameters might be enough to guarantee a certain degree of privacy. However, the comparison of PAST and the $\ell_1$ and $\ell_2$ baselines in terms of the privacy-utility/accuracy tradeoff without considering the magnitude of the weights could lead to unfair comparisons.

Comment 4:

Overparameterization is not the same as non-properly weighting a fixed number of parameters.  The proposed PAST applies adaptive regularization by adjusting the penalty weights of parameters based on their privacy sensitivity, which does not necessarily address the issue of overparameterization. 

Section 5 RELATED WORK discusses the relationship between the number of parameters (or model complexity) and privacy risk, particularly in the context of overparameterization. There are works that confirm the tradeoff between the number of parameters and privacy risk. However, there is limited discussion of how the specific values or magnitudes of those parameter weights might impact privacy. Adjusting the weights of parameters for fixed parameters could influence the model's tendency to memorize or generalize, which potentially affects privacy risk. However, the related work section does not discuss studies that study this trade-off between parameter weight and privacy directly. In addition, the paper is suggested to characterize this weight-privacy trade-off.

### Questions
See Weakness.

### Soundness
2

### Presentation
4

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper presents Privacy-Aware Sparsity Tuning (PAST), an approach to defending against membership inference attacks (MIAs) by introducing an adaptive regularization method that selectively applies sparsity based on privacy sensitivity of parameters. The proposed method modifies ℓ1 regularization, assigning higher penalties to parameters with greater privacy sensitivity. The authors conduct experiments across datasets (Texas100, Purchase100, CIFAR-10/100, and ImageNet) to validate the efficacy of PAST, reporting improvements in the privacy-utility trade-off over baseline defenses.

### Strengths
Clarity: The paper is easy to read.

Relevance: The paper aims to address an important topic in machine learning privacy.

### Weaknesses
1.Lack of Comparison with Recent Baselines: The current version does not compare its approach with recent baselines from the past three years, which is crucial for an ICLR 2025 submission. The paper only references MIA attacks from six years ago and defenses from three years ago, missing key recent works that are important for establishing state-of-the-art (SOTA) context. Key references to consider include:

MIA Attacks:

(a)"Low-Cost High-Power Membership Inference Attacks" (ICML 2024)

(b)"Scalable Membership Inference Attacks via Quantile Regression" (NeurIPS 2023)

(c)"Membership Inference Attacks from First Principles" (S&P 2022)

(d)"Enhanced Membership Inference Attacks against Machine Learning Models" (CCS 2022)

MIA Defenses:

(a) "MIST: Defending Against Membership Inference Attacks Through Membership-Invariant Subspace Training" (USENIX 2024)

(b) "SELENA: Mitigating Membership Inference Attacks by Self-Distillation Through a Novel Ensemble Architecture" (USENIX 2022)

These references represent a minimum set of recent works that should be discussed and included as baselines for a credible comparison.

2.Method Simplicity and Lack of Theoretical Rigor: The proposed method relies on a heuristic reweighting approach that lacks theoretical guarantees, which is a notable limitation for top conference standards. The reweighting method in Privacy-Aware Sparsity Tuning (PAST) is too simplistic and does not reach the research depth, completeness, and robustness generally expected of accepted MIA papers in top conferences. The authors are encouraged to enhance the theoretical foundation and complexity of their approach for future submissions.

3.Weak Motivation and Contribution: The paper's motivation, as shown in Figure 1(b) ("Only a small fraction of parameters substantially impacts privacy risk"), is already a well-known concept in machine learning. Given that parameters closer to the output layer naturally have more influence on gradients and results, this finding is not novel. The use of regularization as an MIA defense is also limited, as regularization is not a commonly adopted SOTA defense method in MIA. The paper does not address whether the proposed reweighting improvement would benefit more commonly used defenses, making its contribution less impactful given that it builds on a sub-optimal defense method.

### Questions
See weaknesses for details. I am giving a score of 5 (marginally below the acceptance threshold). A lower score of 3 would feel overly harsh, as the paper shows some promise. However, this version still falls short of the standards expected at a top conference like ICLR. If the authors remain enthusiastic about this work and believe in the effectiveness of their approach, I encourage them to address the above feedback and consider resubmitting to a future ML or security-focused conference. The current version, however, is far from reaching the level required for acceptance at a top-tier conference.

### Soundness
2

### Presentation
2

### Contribution
2

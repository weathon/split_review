# Communication-Efficient Heterogeneous Federated Learning with Generalized Heavy-Ball Momentum

- Decision: Reject
- Scores: 8, 6, 3, 3

## Abstract
Federated Learning (FL) has emerged as the state-of-the-art approach for learning from decentralized data in privacy-constrained scenarios.
However, system and statistical challenges hinder real-world applications, which demand efficient learning from edge devices and robustness to heterogeneity.
Despite significant research efforts, existing approaches (i) are not sufficiently robust, (ii) do not perform well in large-scale scenarios, and (iii) are not communication efficient. 
In this work, we propose a novel \textit{Generalized Heavy-Ball Momentum} (\ghb), motivating its principled application to counteract the effects of statistical heterogeneity in FL. Then, we present \fedhbm{} as an adaptive, communication-efficient by-design instance of {\ghb}.
Extensive experimentation on vision and language tasks, in both controlled and realistic large-scale scenarios, provides compelling evidence of substantial and consistent performance gains over the state of the art. \footnote{Code is provided for the review process and will be released upon acceptance}.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Th paper proposes a new Federated Learning (FL) algorithm based on heavy-ball momentum, designed to be more robust to statistical data heterogeneity without significant communication cost, compared to state-of-the-art FL techniques. The method proceeds by computing local momentum at the client level, and results in a novel algorithm called FedHBM (heavy ball momentum) which generalizes existing momentum based FL algorithms. The empirical properties of the method are illustrated on vision and NLP tasks, and compared favorably to competitors.

I have read the authors comments which clarified some important aspects of the experiments performed. Accordingly, I upgraded the "soundness" rate to 3-good, as well as my overall rating to 8.

### Strengths
- The paper is very well written, clear and dynamic. Both mathematical statements and intuitive explanation are very clear and easy to follow.
- The proposed methodology, which efficiently exploits participation of clients at multiple optimization rounds to estimate local momentum without increasing communication cost is novel and clever.
- The relation with prior work is very clear and thoroughly discussed, in terms of general properties, precise mathematical formulation and empirical performance
- The limitations of the FedHBM are discussed, particularly in the case of high cross-device settings, and alternatives are considered to alleviate them.

### Weaknesses
 - The paper does not provide any insight on how to set the values of the step sizes \eta and \beta. In addition, the authors do not mention how they set it for their experiments. This is a major limitation to practical use of the algorithm. 
- In relation with aforementioned issue, the authors do not discuss how other hyperparameters were set for competitors, thus comparisons are not easy to interpret (was their hyperparameter optimization for all algoritms ?)
- Overall, the rationale for the choice of the results presented (nb of rounds to reach accuracy level, final model accuracy) is not completely clear. For instance, the computational cost per round is not discussed, so it is difficult to understand the implication of these results. In addition, the non-iid setting is not clear. The authors mention using a Dirichlet distribution, which suggests drawing vectors of probabilities to assign samples to clients, but I don't see how this would lead to heterogeneity (only size imbalance between clients).

### Questions
- How were step sizes \eta and \beta set in the experiments ? How about similar hyperparameters of competitors ?
- Is the computational cost per round similar between algorithms ?
- What does final mean ? Are all algorithms stopped after 10000 rounds ?
- Could you provide more insight on how you designed the non iid setting ? How do you split the data ? How do you use the Dirichlet distribution ? Is it used to draw probabilities of assignment to each client ? Then, how do you assign samples to clients ? It should depend on the sample value, and I don't see it in your explanations.

### Soundness
3 good

### Presentation
3 good

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
This paper studies the problem of system and statistical (data) heterogeneity in the context of Federated Learning. Specifically, the authors propose a novel federated algorithm that utilizes a generalization of the the heavy-ball momentum method on the client side to achieve improved final accuracy and convergence speed in non-iid regimes both in cross-silo and cross-device settings. Extensive numerical results are presented both on academic data set as well as on real-world applications. These experiments showcase the superiority of the proposed FedHBM (and practical variation of this algorithm) in terms of communication cost, accuracy, and convergence speed compared to state of the art federated methods.

### Strengths
-The paper studies an important problem in the area of Federated Learning namely the combination of system and statistical heterogeneity.

-The paper is well structured and easy to follow.

-A simple and intuitive algorithm is proposed that relies on a generalization of the heavy-ball momentum on the client side.

-Both cross-silo and cross-device settings have been explored in the experiments. Both academic and real-world datasets have been studied.

-Extensive ablation study exhibits the effects of $\tau$ (captures which model is used for calculating the momentum i.e. from how many rounds in the past this model is chosen) on the performance of the algorithm.  Additionally, a practical variation of the algorithm has been presented without additional communication requirements with strong performance.

### Weaknesses
 -The main weakness of the paper lies on the absence of theoretical results. 

-The proposed algorithm is a rather simple generalization of the heavy-ball momentum and as a result the novelty is limited.

-In the cross-device setting the algorithm requires a 'proper' initial model to achieve the required improvement.

-In table 2 it seems that FEDDYN achieves higher target accuracy (90%) in the seemingly more challenging cross-device setting. I would appreciate it if the authors could elaborate on that.

-In the plots of Figure 3 and Figure 4 (a) it is hard to distinguish between some of the methods. I would recommend to either utilize different colors or increase the scale. 


Minor issues

- Page 3, paragraph 3, in "..existing algorithms can be express as special.." replace express by expressed.
- Page 6, paragraph 4, in "$\alpha = 10k$" define $k$.
- In table 5  for $C\approx 0.5$ FEDAVG's performance is in bold which appears to be a typo.

### Questions
See weakness section.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper adjusts and combines two existing momentum-based methods applied to federated learning. The first method (acceleration) is the heavy ball method (i.e., Polyak's momentum). The second method is a variance reduction technique [1]. The adjustment for these two methods is to parameterize the time step for the previous iterate of the momentum term for each client. For example, with the heavy ball, the momentum term becomes: $\frac{\beta}{\tau_i}(\theta^{t-1} - \theta^{t-{\tau_i}-1})$ where $\tau_i$ is the time step parameter for client $i$. Experiments are conducted on both iid and non-idd federated learning datasets.

[1] Cutkosky, A. and Orabona, F. Momentum-based variance reduction in non-convex SGD. 2019.



Update: I thank the authors for replying to my review/questions. I have also read through the other reviews and responses. I will maintain my score.

### Strengths
1. Explores the use of momentum for federated learning.
2. The paper is easy to read. However, the writing needs to be improved.

### Weaknesses
1. The novelty of this paper is limited. As mentioned in the summary, two existing momentum-based techniques are additively combined with the modification to adjust previous iterate time step parameter. In my opinion, to call the proposed formulation generalized heavy-ball momentum is somewhat a far-stretch.
2. Some theoretical analysis not provided. Although averaging has been applied, it is not clear why having this gap or "window" is desirable in general and particularly in the federated learning setting. Motivation/intuition needs to be given.
3. Not clear if the results are reproducible since code is not given.
4. Missing some related work:
   * Xin, R. and Khan, U. Distributed heavy-ball: a generalization and acceleration of first-order methods with grading tracking. 2018.
   * Das, R. et al. Faster non-convex federated learning via global and local momentum. 2022.
   * Kim, G. et al. Communication-Efficient Federated Learning with Acceleration of Global Momentum. 2022.

Additional: labels missing on graphs.

### Questions
Very little information is provided on setting $\tau_i$. Section A of supplemental states: $\tau_i \rightarrow \tau = 1/C$ where $C$ is the number of clients. If this is the case, then the term appears negligible under large scale setting.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes to adopt the generalization of heavy-ball momentum in FL which uses an uncertain interval according to the storage state of each local client to construct the momentum term (the current state minus the last local state). No theoretical analysis of convergence or generalization is provided. Experiments on CIFAR-10/100, Shakespeare are conducted to validate its efficiency without learning rate decay.

### Strengths
1. The proposed shift window can help to reduce the communication requirements.
2. This paper proposes a summary of the classical momentum-based method in FL, i.e., FedCM, FedADC, and MimeMom. 
3. The experiments are widely conducted on several setups to validate the efficiency.

### Weaknesses
1. In Eq.(5), what is the MVR term? Could the author explain this in detail? Its first part is a sum of $J_i$-step updates, while its second part is a sum of $j$-step updates. I know these two parts come from the additional term from $\theta_{i,j}^t-\theta_i^{t-\tau_i}$ to $\theta^{t-1}-\theta^{t-\tau_i-1}$, but how does it perform as a variance reduction? The $u$ term is the update performed in each local iteration, so the MVR term is the difference between $j$ local updates and $J_i$ local updates where $j\neq J_i$. Please provide the equivalent form in [1] and demonstrate its variance reduction efficiency in the main text.

   [1]: Momentum-based variance reduction in non-convex sgd

2. The authors claim that they propose the GHB form in Table 1. However, the same updates have been studied in [2] which adopts a multi-step momentum. By setting the specific coefficients as some fixed constants, [2] performs the same updates as the global GHB. Actually, the claimed global GHB in this paper is only a special case of [2]. It also provides some convergence analysis to understand more complicated cases. Therefore, the contribution of this paper seems to only extend the global GHB to the local GHB without any analysis of optimization or generalization, which greatly reduces the novelty of this paper.

    [2]: Enhance local consistency in federated learning: A multi-step inertial momentum approach

3. In the experiments, it indicates that the non-iid dataset split adopts a $\alpha\rightarrow 0$. While in the appendix, it shows $\alpha=0$. Please unify this statement.

4. The results are incomplete. For instance, in Table.2, 3, 4, there are no results of FedCM and FedADC. However, in Figure.3, the curves of FedCM are stated as an ablation study. As the very important baselines of this paper, the comparison with FedCM and FedADC is very necessary, which are also two SOTA methods among the momentum-based methods. Authors should add their performance tests to this paper.

5. The experiments do not adopt the learning rate decay. On page 15 in the appendix, the authors claim that all experiments do not use a learning rate scheduler for simplicity. However, this will significantly reduce the performance of some algorithms and make comparisons unfair. For instance, the ADMM-based method, i.e. FedDyn, requires to be optimized well enough on the local client. Otherwise, dual variables will be updated with very large biases. A similar phenomenon also happens in SCAFFOLD and even FedCM. I think this is the main weakness of the experiment in this paper. All results only reflect the phenomenon under a fixed learning rate. While in the current machine learning, the learning rate decay in non-convex optimization is very important and one of the major concerns. Although changing the learning rate complicates comparisons, this kind of comprehensive study can broadly reflect the performance of the proposed method.

### Questions
Thanks for this submission with the FedGBH method. My main concerns are stated in the weaknesses, mainly including the novelty with repetitive parts from the previous studies, and the lack of baselines and hyperparameter settings.

### Soundness
2 fair

### Presentation
3 good

### Contribution
1 poor

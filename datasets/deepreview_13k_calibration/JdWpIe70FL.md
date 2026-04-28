# Escaping the Sample Trap: Fast and Accurate Epistemic Uncertainty Estimation with Pairwise-Distance Estimators

- Decision: Reject
- Avg Score: 4.75
- Scores: 3, 5, 5, 6

## Abstract
In machine learning, the ability to assess uncertainty in model predictions is crucial for decision-making, safety-critical applications, and model generalizability. This work introduces a novel approach for epistemic uncertainty estimation for ensemble models using pairwise-distance estimators (PaiDEs). These estimators utilize the pairwise-distance between model components to establish bounds on entropy, which are then used as estimates for information-based criterion. Unlike recent deep learning methods for epistemic uncertainty estimation, which rely on sample-based Monte Carlo estimators, PaiDEs are able to estimate epistemic uncertainty up to 100 times faster, over a larger input space (up to 100 times) and perform more accurately in higher dimensions. To validate our approach, we conducted a series of experiments commonly used to evaluate epistemic uncertainty estimation: 1D sinusoidal data, $\textit{Pendulum-v0}$, $\textit{Hopper-v2}$, $\textit{Ant-v2}$ and $\textit{Humanoid-v2}$. For each experimental setting, an Active Learning framework was applied to demonstrate the advantages of PaiDEs for epistemic uncertainty estimation.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper introduces Pairwise-Distance Estimators (PaiDEs) as an efficient non-sampling approach to estimate epistemic uncertainty for ensemble models. PaiDEs utilize pairwise distances between ensemble component distributions to estimate entropy and mutual information, avoiding expensive Monte Carlo sampling. This enables faster uncertainty quantification that scales more favorably to high dimensions. Experiments on active learning tasks using MuJoCo environments demonstrate that the approach can accurately quantify epistemic uncertainty. Key benefits of the proposed PaiDE technique include removing dependence on sampling and improved computational performance compared to sampling-based approaches. Normalizing flow ensembles are employed to flexibly model aleatoric uncertainty while PaiDEs leverage their tractable base distributions.

### Strengths
Originality:

Proposes a novel non-sampling approach to estimate epistemic uncertainty, which is an open problem
Leverages pairwise distances in a creative way to avoid sampling limitations

Quality:
Good mathematical grounding in information theory and probability
Principled design of PaiDE estimators with entropy bounds
Careful methodology and experiment design

Clarity:
Clearly explains limitations of sampling-based approaches
Intuitive descriptions and visualizations of the methodology
Well-structured layout and organization

### Weaknesses
No comparison to other state-of-the-art uncertainty methods - It will add credibility to show benefits over existing approaches. For eg. comparing against Deterministic UQ Methods - ND-UQ (van Amersfoort et al., 2020), Active Learning Methods - BALD (Houlsby et al., 2011), MC Dropout - Estimate epistemic uncertainty using dropout at test time as a Bayesian approximation (Gal and Ghahramani, 2016), Ensembles - Compare to other ensemble approaches like Deep Ensembles (Lakshminarayanan et al., 2017).

OOD detection are not evaluated - This is a missed opportunity to demonstrate more utility of accurate epistemic uncertainty estimation.

The empirical evaluation is quite limited in scope due the first point - lacks sufficient evidence that method works in complex real domains.

Theoretical understanding is completely lacking, because the experiments are simple and toy scenarios - analysis of estimator bias, convergence, optimality properties are important.

Scaling behavior as ensemble size increases is unclear - needs more analysis on this.
it would be useful to see a study on how the performance of the proposed PaiDE method scales as the number of components in the ensemble increases. For example, the experiments in the paper use a small ensemble of 5 models. It would be interesting to additionally evaluate with larger ensembles of 10, 50+ components.
Key questions that could be investigated:
Does the accuracy of epistemic uncertainty estimates improve with more components?
Is there a point of diminishing returns where more components do not help?
How does this compare to scaling behavior of sampling-based MC approaches?

### Questions
Please see the questions

### Soundness
3 good

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
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The authors propose an ensemble method for uncertainty quantification, specifically focusing on mutual information as a measure of epistemic uncertainty. Making use of approximations of (conditional) entropy in terms of pairwise distance measures on distributions, they propose a method for approximating mutual information in terms of a sum of pairwise distances between ensemble members. If these distances can be computed in closed form, the whole approach becomes very efficient, especially in comparison to standard sampling-based methods. The authors also present promising experimental results.

### Strengths
Very interesting and timely topic.
The idea of pairwise approximation is quite appealing and theoretically justified.
The experiments are well conducted, and the results are promising.

### Weaknesses
Some parts of the paper are very concise and hard to follow. In particular, this is true for Sections 5 and 6. The combination of PaiDEs and Nflows Base is not very clear to me.

How exactly is Nflows Base used to create an ensemble? This didn’t become very clear in the paper, but I think it is an important point, because the variability of the ensemble members eventually determines the epistemic uncertainty. In standard ensemble learning, variability is normally enforced through randomisation, e.g., by resampling the training data or randomly initialising weights in a neural network. Here, the risk is that different randomisations may lead to different variability, making (epistemic) uncertainty arbitrary to some extent. So how is the variability produced by the NF ensemble controlled, and in which sense is it “meaningful” or “natural”?

Another point that puzzled me is the connection between the base distributions and the output distributions produced by Nflows Base. This connection is illustrated by Figure 1 (I was wondering why this figure is shown right in the beginning, although it is only referenced on page 6). What I suspect is that the pairwise distances between the output distributions is the same as the pairwise distances between the base distributions. This seems to be a key point of the approach. However, it is not made very explicit in the paper. Moreover, why exactly are the distances the same? The distributions actually look quite different. Shouldn’t this be shown in a formal way?

Another question in this regard, also related to the first one: Where exactly are the base distributions combing from in the first place. Again, as these distributions seem to determine the epistemic uncertainty, this looks to me like an important question.

### Questions
How exactly is Nflows Base used to create an ensemble? This didn’t become very clear in the paper, but I think it is an important point, because the variability of the ensemble members eventually determines the epistemic uncertainty. In standard ensemble learning, variability is normally enforced through randomisation, e.g., by resampling the training data or randomly initialising weights in a neural network. Here, the risk is that different randomisations may lead to different variability, making (epistemic) uncertainty arbitrary to some extent. So how is the variability produced by the NF ensemble controlled, and in which sense is it “meaningful” or “natural”?

Another point that puzzled me is the connection between the base distributions and the output distributions produced by Nflows Base. This connection is illustrated by Figure 1 (I was wondering why this figure is shown right in the beginning, although it is only referenced on page 6). What I suspect is that the pairwise distances between the output distributions is the same as the pairwise distances between the base distributions. This seems to be a key point of the approach. However, it is not made very explicit in the paper. Moreover, why exactly are the distances the same? The distributions actually look quite different. Shouldn’t this be shown in a formal way?

Another question in this regard, also related to the first one: Where exactly are the base distributions combing from in the first place. Again, as these distributions seem to determine the epistemic uncertainty, this looks to me like an important question.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes an active learning algorithm using the pairwise distances of densities (probabilities) to approximate the mutual information-like metric such as $H(y \mid x) – H(y \mid x, \theta ).$ The basic framework start from the inequalities of $H( y \mid x , \theta) \le H( y \mid x) \le H( y, \theta \mid x).$ The proposed approximation for $H( y \mid x) $ uses the distance between $p_i( y \mid x, \theta_i ) $ and $p_j ( y \mid x, \theta_j)$ where two distribution are from the uncertainty of $\theta.$ The distance between two densities utilizes the KL divergence and Bhattacharyya distance. Furthermore, normalizing flow is used to generate the ensembles for $p( y \mid x, \theta_i)$. Experiments results are promising. Relatively lower or comparable computation cost is required compared MC method. High receptive power for the unlabeled samples and high accuracy in high-dimensional data.

### Strengths
The proposed algorithm is clever, and it have the theoretical validation although the approximation cannot be tight in some cases. In the computational cost, the advantages are obvious. Considering the complexity in Bayesian approach, the proposed algorithm is superior to MC, not depending on variational inference. Also, the performance is superior to the MC approach.

### Weaknesses
The baseline-algorithms are not sufficient, Random (query), BADGE (Ash et al., 2019) and BatchBALD (Kirsch et al., 2019) can be other base-line algorithms. The author(s) claim that the proposed algorithm can be strong for the large size of queries. Therefore, I want to see the compared results with algorithms considering the diversity. If possible, you can use the multiple samples for $p(y \mid x_1, \cdots, x_d, \theta_i)$. More experiments and presentation can improve the paper, including the various acquisition sizes and trace plot of test accuracy and so on. The focus on regression tasks, while valid, limits the scope and impact of the work, as active learning is heavily utilized in classification. The absence of comparisons with methods specifically designed for high-dimensional regression within active learning is a notable gap. Furthermore, the experiments do not explore the sensitivity of the proposed method to different hyperparameter choices, particularly those related to the normalizing flow and distance metrics. The theoretical analysis, while present, could be strengthened by addressing the tightness of the approximation and its impact on the final performance.

### Questions
Q1: Is the notation of P_{b \mid b} in 31 lines on page 5 right?
Q2: Please clarify what is f(a_t, s_t) = s_{t+1} in a detailed manner.
Q3: Number of samples in Figure 3: what’s the meaning, probably, size of unlabeled samples at initial steps, right?

### Soundness
3 good

### Presentation
3 good

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
The paper is concerned with developing a new estimator for epistemic uncertainty. Epistemic uncertainty can be used as a criterion to guide active learning in the ensemble learning setting where there are multiple base learners (instantiated as neural networks). The estimator is combined with nflows base, which is a method to learn base learners. The new estimators can avoid Monte Carlo sampling. They speed up learning and can be applied to problems of larger scale.  Experiments are carried out on a variety of datasets. The proposed estimators are compared with the conventional Monte Carlo estimator.

### Strengths
* originality: the proposed estimator is based on Kolchinsky & Tracey (2017). The application is new.
* Quality: the work is of good quality. the proposed estimator has advantages over existing ones such as closed form, theoretical tie to epistemic uncertainty, efficiency, and scalability. The estimation quality is also good compared to the Monte Carlo based estimator.
* clarity: presentation is clear.
* significance: The proposed method is of good significance as it proposed a new method that is better than the existing one for this specific type of problem.

### Weaknesses
 * Given Kolchinsky & Tracey (2017), the contribution of this work is somewhat incremental.
* Only NFLows Base is considered as the base learner method for ensemble learning. It would be nice to see if the proposed estimator can also be applied to other scenarios. Specifically, the method's applicability to other ensemble methods, such as those using bagging or boosting, is unclear. The current focus on neural flow-based models limits the scope and generalizability of the findings.
* The application scenario that the proposed method applied to also appears to be quite niche. The paper focuses on active learning with epistemic uncertainty, which, while important, is not the only application where ensemble uncertainty estimation is valuable. The limited scope of the experimental evaluation does not fully demonstrate the broad utility of the proposed estimator.

### Questions
Some suggestions on the writing of the paper:
* eq 1, needs to specify pi_j  to be between 0 and 1.
* the use of \theta is somewhat confusing. It sometimes can refer to the parameters of the entire ensemble but other times it refers to the parameters of the base learner (e.g. eq1 vs the eq right before eq3).
* grammar: "in addition to the improving the lower bound"
* would be nice to list the environment dimension and other related statistics in Table 1 for readability.
* Figure 2:  show the names of the x-axis and y-axis.
* would be nice to show how eq3 is derived.

Other questions:
* any suggestions on whether one should use the lower bound or the upper bound estimator?
* How does one use eq 2 to carry out active learning? does it imply that y needs to be known for all the data points in the dataset? A pseudocode list for the entire procedure may help to explain things better.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

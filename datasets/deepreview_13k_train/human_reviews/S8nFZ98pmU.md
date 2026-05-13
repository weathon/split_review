# Contrastive Meta Learning for Dynamical Systems

- Decision: Reject
- Scores: 3, 5, 6, 5

## Abstract
Recent advancements in deep learning have significantly impacted the study of dynamical systems. Traditional approaches predominantly rely on supervised learning paradigms, limiting their scope to large scale problems and adaptability to new systems. This paper introduces a novel meta learning framework tailored for dynamical system forecasting, hinging on the concept of mapping the observed trajectories to a system-specific embedding space which encapsulates the inter-system characteristics and enriches the feature set for downstream prediction tasks. Central to our framework is the use of contrastive learning for trajectory data coupled with a series of neural network architecture designs to extract the features as augmented embedding for modeling system behavior. We present the application of zero-shot meta-learning to dynamical systems, demonstrating a substantial enhancement in performance metrics compared to existing baseline models. A notable byproduct of our methodology is the improved interpretability of the embeddings, which now carries explicit physical significance. Our results not only set a new benchmark in the field but also pave the way for enhanced interpretability and deeper understanding of complex dynamical systems, potentially opens new directions for how we approach system analysis and prediction.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper points out that it requires a novel method to apply contrastive learning to dynamical systems. Accordingly, the authors developed a contrastive meta-learning method applicable to various dynamical systems. It allows the zero-shot meta-learning on previously unobserved dynamics. This paper makes several contributions, including a novel loss function (e.g., Element-wise Square Ratio Loss (ESRL)) and other learning techniques (e.g., the covariance-based regularization, local linear feature extraction).

### Strengths
- This paper introduces a novel problem of contrastive learning on dynamics systems with the perspective of meta learning.

- Limitations on the existing meta learning methods on dynamical systems are clearly pointed out. For example, as the author mentioned in L102, many of them are relying on supervision from system coefficients or few shot adaptation, limiting the practical applications. In this light, the problem statement made by the authors are reasonable.

- Overall the paper is easy to understand and follow. In particular, the effectiveness of contrastive learning is qualitatively well presented in Figure 3, showing that learned embeddings on different trajectories with different coefficients are clearly distinguishable.

### Weaknesses
 - While the proposed loss function and the covariance-based regularizer demonstrates lower errors than other popular contrastive losses (e.g., Info-NCE, Triplet), technical contributions are not significant. Except it considers element-wise comparison in embedding space, Element-wise Square Ratio Loss (ESRL) has the almost same form with the original Square Ratio Loss (SRL). I don’t think the extension of SRL to the element-wise version is necessarily a novel contribution. The covariance-based regularization is also very well known, as the authors mentioned it is inspired from Bardes et al. (2021). Lastly, I consider local linear square feature extraction as simply linear approximation on the input space. 

- I’m not sure the unsupervision of not providing any coefficients to the models is rare and interesting problem setup in dynamical systems. While we can model better trajectory predictors using such knowledge on the systems, recent trajectory prediction models (e.g., neural ODE or RNN) are often solely trained from trajectory and perform pretty well on such synthetic systems. Basically, I disagree with the statement in L441-444 since many previous works still assume the system coefficients are unknown.

- Since the authors explore the meta learning problem, the experimental results should focus on how the proposed learning method improves generalizability on previously unobserved dynamics. For example, the model is trained on trajectories on a set of coefficients and then evaluated on them on a different set of coefficients. However, I couldn’t find such details in Table 1, 2, and 3. Overall, the experiment section is not detailed enough to support L171: "In the context of meta dynamical system learning, our goal is to develop a model that can generalize
from a set of training systems ϕtrain to new, unseen test systems with properties ϕtest."

### Questions
N/A

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes to use contrastive unsupervised learning for meta dynamical-system learning.
The authors claim that the method can unsupervisedly identify the system's coefficients and achieve zero-shot forecasting.
Experiments demonstrate the efficacy of the proposed method.

### Strengths
- The authors introduce dynamical-system-specific modules for contrastive learning, the local linear least square feature extractor and the spatial adaptive linear modulation. These are simple and may be useful for other dynamical system learning.
- The experiments demonstrate that the proposed method achieves better accuracy than the baselines and seems to be more stable. Showing learning curves may strengthen the latter.

### Weaknesses
 - It is unclear why the proposed contrastive-learning approach enables unsupervised coefficient identification and zero-shot forecasting. In particular, I could not understand how and when the model could learn organized embeddings like Figure 3. It would be interesting if the authors could characterize the dynamical systems that the proposed method could handle.

### Questions
- What is $*$ in equation 9?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper studied forecasting in dynamic systems in continuous and discrete setup via zero-shot meta learning. The proposed framework has three steps: 

1- employing contrastive learning via a modified loss Element-wise Square Ratio Loss (ESR) to derive embeddings in both intra- and inter-truncated systems (meta step 1)

2- applying this embedding model to the initial segment of the data to obtain embeddings (meta step 2)

3- utilizing the final embeddings in a prediction module for forecasting 

Some novel aspects of the work are proposing a Local Linear Least Square feature extractor for vector-based systems and a Spatial Adaptive LinEar Modulation (SALEM) for discrete systems. 
Authors conducted various experiments and ablation studies and demonstrated the utility of their framework.

### Strengths
- The paper is well-written and well-organized. 
- The paper proposed the first method of zero-shot meta learning for dynamic systems 
- There are quite a few novel aspects as well as the main contribution

### Weaknesses
The setup is highly relevant to domain generalization/out-of-distribution generalization task and there are methods of meta-learning for that tasks such as [1]. There is no indication of this in the paper/baselines. Only in the appendix one experiment is provided that compares the proposed method to a standard training setup.

Although authors studied the triplet loss and the Info-NCE loss, I think another relevant loss for this particular application is the Histogram loss [2] because of its probabilistic nature - it is defined on the similarity distributions of positive and negative pairs where distributions are estimated based on histograms. Authors should either justify that it is not relevant or include it in the experiments. 

I can understand authors viewpoint by not comparing their method to baselines in the vector-based experiments, but I still believe including those results will increase the impact of the paper. If the proposed method is still better than the baselines even though baselines require additional information, that would increase the contribution of the paper. On the other hand, if the baselines outperform the proposed method then I’d like to see a few-shot version of the method. 

There is no indication of the code and releasing it. I strongly encourage authors to either include a statement about code release plans in their paper, or provide a link to a code repository if it's already available.


There is no instruction on how to tune lambda hyper-parameter. Why 0.5 is the maximum value for it? it would be great to provide details on how they selected the lambda value, and if they explored a range of values other than 0, 0.2, or 0.5.

If Table 3 and 4 also serve as ablation for the discrete systems, then ResNet+SPADE is missing and should be added because it would represents methods that are based on spatial information compared to the proposed method that utilizes both channel embeddings and spatial information or authors need to justify why it is not necessary.

### Questions
- What would be the impact of deeper backbones for ResNet and LSTM in the driving application?

- How does the performance change by expanding the input window and/or increasing the prediction horizon in both grid-based and vector-based systems? 

- There is no indication of any regularization technique in the reproducibility details, was there any? Also, meta learning methods are often hard to train. I think providing learning curves and training dynamics would increase the reproducibility and debugging of the work for future users. 

- What makes these two different losses (ESR and Cov) combinable into one loss e.g., based on their nature and what they represent and the scale? it would be great if authors can provide more theoretical justification for combining these losses or reasoning and explain the rationale behind penalizing perfect correlation in the covariance loss.

- Meta learning models are usually time consuming and authors eluded the computational complexity of the feature extractor a bit in the conclusion, how much do you increase time/space complexity compared to standard training in the vector-based system and studied baselines in the grid-based system? 

I'd be happy to increase my score if authors respond to my questions here and points raised in the weakness, particularly:

1- Potentially missing experiments (Feel free to include them or provide your reasoning why they are not necessary) e.g., missing ablation, missing baselines in the vector-based case, or other metric learning losses. 

2- Questions and concerns related to the methodology e.g., combining losses or complexity 

3- Questions and concerns related to reproducibility

Update: I would like to thank authors for their engagement during the rebuttal period. After reading their response and other reviewers' comments I will increase my confidence and remain in favor of acceptance.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper aims to solve the following problem: if we have some time-series data from a dynamical systems at several different parameters, can we forecast the dynamics at a different parameter not in the training set. The authors achieve this by first identifying the unknown parameter from a trajectory observation using contrastive learning (embedding the trajectory to infer the parameters), they then use the inferred parameter to make forecasts.

### Strengths
Forecasting dynamical systems at previously unseen parameters is an important and challenging problem that has resisted many attempts from the nonlinear dynamics and scientific machine learning communities. This paper presents an interesting idea using contrastive learning that could prove useful towards solving this longstanding problem.

### Weaknesses
With the current experiments, I am not fully convinced that the proposed approach would work as well as claimed in complex and real-world situations. I will explain more with my questions below.

1. Figure 1 suggests that dynamical systems with the same parameter but different initial conditions have similar dynamics, while those with different parameters show distinct behaviors. However, many dynamical systems are multistable, meaning exactly the same system when starting from different initial conditions can exhibit very different dynamics (i.e., reaching different attractors). How does the proposed method address this challenge?

2. Concerning Eqs. (2) to (4), they address dimensional collapse due to linear correlations, but what about other forms of more nonlinear relation between different dimensions (which can also lead to dimensional collapse)? Specifically, the use of covariance regularization alone may not be sufficient to prevent embeddings from collapsing onto lower-dimensional manifolds due to complex nonlinear dependencies.

3. Eq. (5) relies on estimating time derivatives from data, which is known to be sensitive to noise. This raises questions about how robust the proposed method is. The method's reliance on finite difference approximations for time derivatives could be particularly problematic when dealing with noisy or high-frequency data, potentially leading to inaccurate local feature extraction.

4. The experiments were performed on a few simple systems such as the spring-mass system and the Lotka-Volterra model. What about other more complex systems? For example, chaotic ones or higher-dimensional ones? Or ones whose dynamics change dramatically with parameters (e.g., going through bifurcations). The lack of experiments on systems exhibiting chaotic behavior or bifurcations raises concerns about the generalizability of the proposed approach to more complex dynamical systems.

5. Moreover, the model space currently only contain one class of equations (e.g., the Lotka-Volterra model). What if it spans several classes of qualitatively different systems? Can the proposed method handle this more general situation? The current framework appears limited to a single class of dynamical systems, and it's unclear how it would perform if the underlying equations governing the dynamics were fundamentally different.

6. Data from how many different parameter sets are required for effective training?

### Questions
1. Figure 1 suggests that dynamical systems with the same parameter but different initial conditions have similar dynamics, while those with different parameters show distinct behaviors. However, many dynamical systems are multistable, meaning exactly the same system when starting from different initial conditions can exhibit very different dynamics (i.e., reaching different attractors). How does the proposed method address this challenge?

2. Concerning Eqs. (2) to (4), they address dimensional collapse due to linear correlations, but what about other forms of more nonlinear relation between different dimensions (which can also lead to dimensional collapse)?

3. Eq. (5) relies on estimating time derivatives from data, which is known to be sensitive to noise. This raises questions about how robust the proposed method is.

4. The experiments were performed on a few simple systems such as the spring-mass system and the Lotka-Volterra model. What about other more complex systems? For example, chaotic ones or higher-dimensional ones? Or ones whose dynamics change dramatically with parameters (e.g., going through bifurcations).

5. Moreover, the model space currently only contain one class of equations (e.g., the Lotka-Volterra model). What if it spans several classes of qualitatively different systems? Can the proposed method handle this more general situation?

6. Data from how many different parameter sets are required for effective training?

### Soundness
2

### Presentation
3

### Contribution
3

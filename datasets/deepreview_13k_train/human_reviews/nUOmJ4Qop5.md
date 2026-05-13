# Peacock: Multi-Objective Optimization for Deep Neural Network Calibration

- Decision: Reject
- Scores: 6, 3, 6, 5

## Abstract
The rapid adoption of deep neural networks underscores an urgent need for models to be safe, trustworthy and well-calibrated. Despite recent advancements in network calibration, the optimal combination of techniques remains relatively unexplored. By framing the task as a multi-objective optimization problem, we demonstrate that combining state-of-the-art methods can further boost calibration performance. We feature a total of seven state-of-the-art calibration algorithms and provide both theoretical and empirical motivation for their equal and weighted importance unification. We conduct experiments on both in and out-of-distribution computer vision and natural language benchmarks, investigating the speeds and contributions of different components.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper presents Peacock, a calibration algorithm that performs multi-objective optimization of existing calibration techniques. The method is shown to improve in and out-of-distribution calibration while retaining performance and speed on computer vision and natural language benchmarks.

### Strengths
– The paper is very well written and easy to follow

– The paper does a good job of thoroughly reviewing prior work

– The paper includes a comprehensive appendix with extensive details as well as a detailed codebase which will aid in reproducibility

– The theoretical justification for the multi-objective formulation is intuitive and well-explained

– The proposed method seems effective on a range of datasets without adding a computational overhead

### Weaknesses
– The paper framing refers to calibrating “deep neural networks” in general rather than classification models. From what I can tell the proposed approach is designed only with classification in mind – it would be helpful to either update the paper’s framing to reflect this, or to include additional discussion (or if possible, even a proof of concept experiment) demonstrating how Peacock may be generalized to other tasks (or even to specialized classification tasks such as dense prediction)

– The technical contribution of the paper is somewhat limited – 1) it shows that multi-objective optimization of existing calibration strategies is both theoretically and empirically better than or equivalent to any one in isolation (which is consistent with related findings in loss and model ensembling, as the paper acknowledges), and 2) it proposes an algorithm to compute “pareto optimal importance weights” efficiently. That said, it does a very thorough job of exploring various design choices, motivating its method, and reviewing the literature, due to which I do not consider this a significant weakness.

– The “weighted importance formulation” would benefit from additional motivation and . L306 claims that “loss terms can often be conflicting” as the motivation for importance weighting – it would be good to experimentally demonstrate this. Further, do any of the theoretical guarantees for the equal weighting formulation apply to the importance weighted version? Finally, why does importance weighting not consistently outperform equal weighting in Table 1 and 2?

– Some aspects of the method design need elaboration. For eg. why is “direction weighted self-attention” required to learn loss weights, rather than say a simple linear layer?

### Questions
Please see weaknesses above for a detailed list of questions.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper presents a comprehensive survey on “Multi-objective optimization for deep neural network optimization”. Motivated from the previous literature, this paper advocate a method of unifying the previous baselines into one, dubbed the method “Peacock”. 

This method, according to figure 1(a), encompasses a few recent works: AdaFocal, Dual Focal, and MaxEnt for entropy based one, as well as margin-based CPC and regularizers based RankMixup and Post-hoc processing AdaTS. 

Experiments are conducted on many domain shift datasets, like CIFAR10/100-C, FmoW, CivilComments and so on.

### Strengths
+ This paper presents a complete survey of previous works. 
+ It seems to be a good reading material for the newcomers to this field. 
+ Experiments shown in this paper indicates averaging some of the good methods can improve the performance further. This is good to be known for the community

### Weaknesses
There is no solid scientific contribution in terms of novel methods. Instead, it basically composes several state-of-the-art methods and constitutes as an engineering effort to unify previous methods. I think in general this paper does not have technical algorithmic novelty, and seems to be a technical report rather than a scientific paper.

There exists some presentation mistakes:
- In the figure of page 2, It should be Figure 1, but this caption is missing. 
- I am not sure why this method is called “Peacock”, it lacks of any interpretation but seems to be a meaningless shortcut.

### Questions
As above. 

My biggest concern is this paper is taking a short cut, summarizing many previous works and put them into one in a naive manner. This might take some of the works, but not the actual contribution that excites the community.

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces a framework (Peacock) designed to improve neural network calibration through multi-objective optimization. Emphasizing the importance of accurate model confidence in safety-critical applications, the framework proposes combining multiple calibration methods into a single framework. Peacock optimizes these methods to reduce calibration errors for in-distribution (ID) and OOD data. They operate in two modes: Equal Importance, where all methods are weighted equally, and Weighted Importance, where weights are dynamically adjusted using a self-attention mechanism. The results show that Peacock achieves better calibration accuracy across various datasets than any individual method.

### Strengths
1. Peacock’s approach to combining calibration methods in a multi-objective framework is novel and reflects a strong and thoughtful attempt to address the limitations of single-method approaches.
2. Provide a theoretical foundation, arguing that Peacock’s calibration error is bounded by the average error of its components. This mathematical rigor adds to the credibility and applicability of their approach however I need to see other reviewers’ opinion on it.
3. Peacock’s use of a self-attention-based weighting mechanism in its Weighted Importance formulation is a valuable addition, allowing the framework to adapt to different calibration needs.
4. The extensive evaluation on synthetic and real-world datasets, including CIFAR variants and iWildCam, demonstrates Peacock’s potential for generalizable performance in ID and OOD contexts.

### Weaknesses
1. The work could improve clarity around why certain calibration methods were selected and how they interact synergistically within Peacock. It would be helpful if the authors compared Peacock with other excluded methods to understand its compatibility and potential flexibility. Specifically, the rationale behind choosing methods like AdaFocal, MaxEnt, and RankMixup over other calibration techniques is not sufficiently justified. The paper lacks a detailed analysis of how these specific methods complement each other, especially considering that some calibration techniques may have overlapping effects or even introduce conflicting gradients during optimization. A more thorough discussion of the selection criteria, including a comparison with alternative methods and an analysis of potential interactions, is needed to strengthen the framework's design.
2. While the self-attention mechanism for adaptive weighting is innovative, the authors do not provide a clear explanation of how specific weights are adjusted in various calibration scenarios. Detailed case studies or visualizations could strengthen the interpretability of the model’s weighting adjustments. The explanation of how the self-attention mechanism dynamically adjusts weights based on different calibration needs remains superficial. The paper does not provide sufficient insight into the factors influencing weight adjustments, such as the magnitude of calibration errors or the specific characteristics of the input data. A more detailed analysis, perhaps through case studies or visualizations, is necessary to understand the mechanism's behavior under different conditions and to validate its effectiveness.
3. Peacock’s performance is documented on many typical benchmarks, but it remains unclear if it scales efficiently in more resource-constrained settings (less human supervision specially) or real-time applications. Details on Peacock’s resource usage across varying computational capacities could improve the overall proposal of framework. The paper lacks a comprehensive analysis of Peacock's computational demands, particularly in resource-constrained environments. The authors should provide details on the framework's memory footprint, training time, and inference speed across different hardware configurations. This information is crucial for determining the practical applicability of Peacock in real-time or low-resource scenarios. Without such an analysis, it is difficult to assess the framework's scalability and suitability for diverse deployment contexts.
4. The dependence on Expected Calibration Error (ECE) and related metrics is standard, yet calibration results could benefit from additional metrics or more especially contextual tests. It would be great to see the limitation of Peacock in unusual or extreme OOD scenarios. While ECE is a standard metric, relying solely on it may not fully capture the nuances of calibration performance, especially in extreme OOD scenarios. The paper should include additional metrics, such as the Brier score or negative log-likelihood, to provide a more comprehensive evaluation. Furthermore, the authors should explore the framework's behavior under more challenging OOD conditions, such as adversarial attacks or highly unstructured data, to better understand its limitations and robustness.

### Questions
1. Please clarify the selection of these specific calibration techniques. How does Peacock handle any dependencies or conflicting effects among these methods, and what might its performance look like if additional calibration techniques (e.g., ensemble-based or regularization-based) were included? It will be helpful to justify the proposed framework and provide comprehensive details for future research.
2. Interpretability of Adaptive Weighting: For the self-attention mechanism, can the authors provide insights into how weight adjustments occur across different datasets? Examples of how specific weights change or stay consistent across OOD shifts would clarify the mechanism’s adaptability.
3. Handling of Adversarial and Non-Standard OOD Scenarios: Peacock performs well in ID and standard OOD settings, but could the authors elaborate on its behavior in more adversarial or highly unstructured OOD contexts? Even very limited empirical evidence will be suffice for it.

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
The paper proposes a multi-objective calibration strategy that relies on Pareto optimal solutions that combines several losses that have been shown to provide good calibrated networks. The approach is evaluated on several small size problems (image and text).

### Strengths
- The principle of combining multiple losses designed for good calibration makes sense.

- Comprehensive evaluation and ablation study on multiple architectures and datasets.

- The results are constantly good on the evaluated problems (but only small size problems).

I rate the work as “marginally below the acceptance threshold”: I may change my score after reading the rebuttal and other reviewers' comments. .

### Weaknesses
 - The proposed approach is basically a multi-objective optimization using the latest calibration losses from the literature: the algorithm novelty is limited.

- I had a problem with the mathematical notations which are often not clearly defined. This makes the paper difficult to check. See the questions section.

- Evaluation is only for small size problems (according to current standards).



### Questions
- I had problems with the mathematical notations. For example (but not only): 
   - l.139 and 141: is $P_i(y_k | x)=P(\{y=y_k\}|x_i)$ the likelihood or score of hypothesis $k$ when $x_i$ is the input ? What is $h_i$?
  - Eq. 1: ECE is a scalar measure that characterizes globally the predictor (Naeini et al., 2015): How can it depend on a sample $x$?
  - l. 281: what is $\bar{y}$?
  - Eq.11:  I don’t understand this equation (expectation of a non random scalar).
  - Please make your mathematical notations sound.

- How does your approach scale with larger models and datasets (ImageNet) ?

- How does the approach compare with post-hoc calibration, which is a much lighter calibration strategy, for instance [1] cited in the paper or [2] not cited? 

[1] Jize Zhang, Bhavya Kailkhura, and T Yong-Jin Han. Mix-n-match: Ensemble and compositional methods
for uncertainty calibration in deep learning. In ICML, 2020.

[2] Kanil Patel, William H Beluch, Bin Yang, Michael Pfeiffer, and Dan Zhang. Multi-class uncertainty
calibration via mutual information maximization-based binning. In ICLR, 2021

### Soundness
2

### Presentation
3

### Contribution
3

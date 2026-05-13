# Weak Bisimulation Metric-based Representations for Sparse-Reward Reinforcement Learning

- Decision: Reject
- Scores: 5, 3, 1, 6

## Abstract
Recent studies have shown that bisimulation metrics possess the superiority of essentially extracting the features related to reinforcement learning tasks. However, limited by strict assumptions and the inherent conflict between metrics and sparse rewards, they suffer from serious representation degeneration and even collapse in sparse reward settings. To tackle the problems, we propose a reward-free weak bisimulation metric-based scalable representation learning approach (SRL). Specifically, we first introduce the weak bisimulation metric, which bypasses the intractable reward difference, instead leveraging a trainable Gaussian distribution to relax the traditional bisimulation metrics. Particularly, the Gaussian noise creates a flexible information margin for the metric optimization, which mitigates potential representation collapse caused by sparse rewards. Additionally, due to its pure distribution internally, the metric potentially mitigates representation degeneration resulting from inconsistent computations under strict assumptions. To tighten the metric, we accordingly consider continuous differences over the transition distribution to enhance the accuracy of the initial transition distribution difference, strengthening the extraction of equivalent task features. We evaluate SRL on challenging DeepMind Control Suite, MetaWorld, and Adroit tasks with sparse rewards. Empirical results demonstrate that SRL significantly outperforms state-of-the-art baselines on various tasks. The source code will be available later.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a weak bisimulation metric in sparse reward settings. Compared to the previously strict bisimulation metric methods, the weak bisimulation metric introduces two primary enhancements: (1) it relaxes the reward difference term through a trainable Gaussian distribution, alleviating potential representation collapse caused by sparse rewards; (2) it strengthens the extraction of equivalent task features by accumulating state transition distribution differences accordingly. Experimental results on DMC, Meta-World, and Adroit demonstrate that, the weak bisimulation metric indeed improves performance in sparse reward tasks.

### Strengths
The introduction presents a compelling motivation and provides a clear background explanation.

The proposed weak bisimulation metric is a straightforward yet effective approach, and it is easily adaptable to other bisimulation-based algorithms.

### Weaknesses
 **1. Insufficient Coverage of Related Work.** 

The current manuscript lacks adequate discussion of prior work related to bisimulation representation collapse in sparse reward tasks. Notable approaches, such as constructing bisimulation metrics through intrinsic rewards and inverse dynamics [1] or adopting action-based bisimulation to eliminate reward dependency [2], are absent. To strengthen the comparison, I recommend that the authors clarify how their proposed method differs from or improves upon these existing techniques. Specifically, they could discuss the relative advantages of their approach compared to the intrinsic reward method in [1] and the action-based method in [2].

**2. Errors and Ambiguities.** 

This paper contains several errors in expression and ambiguities that could affect clarity and accuracy. For example, “−” is used instead of “+” in Eq. (5) and Eq. (17). Additionally, in line 402, the statement "We choose complex *walker_run*, *walker_walk*, *reacher_hard*, and *quadruped_run* tasks with sparse reward properties" incorrectly categorizes *Walker* and *Quadruped* as sparse reward tasks, which are typically considered dense reward tasks as per [3]. To improve clarity, I suggest that the authors carefully review these equations and statements. It may also be helpful for them to provide clarification if their categorization of tasks differs from the standard definitions in [3], to ensure readers understand any intentional deviations from established terminology.

**3. Experimental Design and Comparison Issues.** 

The experimental setup has several issues:

(1)The selection of comparative algorithms lacks sufficient representativeness. DrQ-v2 and DrM, while valuable, are not RL algorithms specifically designed to use bisimulation for extracting task-relevant representations. It would strengthen the study to include additional bisimulation-focused algorithms, such as MICo [4] and RAP [5], as well as other methods addressing bisimulation in sparse reward tasks (e.g., [1] and [2]). I suggest that the authors clarify their rationale for the current baseline selection and consider a broader comparison with bisimulation-based approaches to provide a more comprehensive evaluation.

(2)In Figure 4, It is unfair to compare SRL (build upon DrQ-v2) proposed in this paper with DBC, as DrQ-v2 demonstrates significantly superior performance than DBC.

(3)In the selection of experimental tasks, it is necessary to include experiments with a noisy background. Additionally, a more in-depth qualitative analysis of the relationship between introduced redundant information and interference from noisy backgrounds is required.

(4)This paper would benefit from ablation experiments to analyze the contributions of individual modules. Specifically, an ablation study comparing the model's performance with and without the Gaussian distribution term in the weak bisimulation metric could clarify its impact and importance within the framework.

**4. Reliance on Assumption A.1.**

The paper’s theoretical results rely heavily on Assumption A.1, which presumes that the sparse-reward expectation remains less than or equal to a sufficiently small constant $C_1$. However, the assumption lacks precise quantification, particularly regarding what constitutes a “sufficiently small” constant, potentially limiting the applicability of the results. I recommend that the authors either provide empirical evidence from their experiments to support the validity of this assumption or discuss the possible implications if this assumption does not hold in certain environments.

### Questions
What is the specific meaning of the mean $\mu_c$ in the Eq.(5)? It appears that the mean $\mu_c$ is merely a constant without practical significance. And how can it be ensured that the weak bisimulation metric effectively extracts task-relevant features?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper investigates the problem of representation learning in deep reinforcement learning. It points out the fundamental challenges of previous (approximations of) bi-simulation metrics. It proposes SRL, which relaxes bi-simulation metric, aiming at solving the intractable reward difference and collapse in the sparse reward setting. Furthermore, it considers continuous differences over the transition distribution to tighten the metric. Finally, experiments are conducted to show the advantage of this algorithm.

### Strengths
1. Most part of this paper is easy to read and follow.
2. The experiment results shows that the resulting algorithm is consistently better than baselines.

### Weaknesses
1. The writing about some concepts can be improved. While I understand bi-simulation is not new. Detailed definitions of relevant concepts should be provided, at least in the appendix. For example one would not be able to understand Theorem 3.1 if one does not read other papers. Besides, definition 4.2 is also not strict as it contains random variable in the definition of a deterministic map by default. This makes subsequent statements unclear as well.
2. If I am understanding correctly, this paper contains overstatements on theorems. See question 2.
3. Definition 4.2 seems unnatural to me, see question 3. More explanations should be provided

Typos:
1. In definition 4.2, the minus sign should be plus.

### Questions
1. What is the formal definition of $\mathbb{M}$ in Theorem 3.1? What is the definition of $\pi$-simulation and what is a least fixed point?
2. Can you explain the logic in line 234 and 235? Theorem 4.1 only reasons about the sup over all states rather than some specific state pair.
3. By introducing a Guassian random variable in the definition 4.2, the distance can now be negative. Besides, when $s_i=s_j$, this metric does not yield zero, not even on average. Why does it make sense
4. I am assuming scalability is the ability to remain effective when performing on more complex tasks. In what sense is SRL scalable?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
The paper proposes a "reward-free" bisimulation-like metric to tackle the known representation collapse issue of bisimulation metrics in sparse reward environments. The expected-reward difference term in the $\pi$-bisimulation metric is replaced by a noise distribution and the transition distribution distance term is replaced via unrolling by a T-step discounted sum of future distances. Experiment results are shown over 3 pixel-based control suites against a few baseline algorithms.

### Strengths
- The empirical results presented in Sec. 5 seem encouraging.

### Weaknesses
1. The presentation seems too sloppy to me. The paper is littered with vague, unclear or incorrect statements that make it hard to read.
2. The introduction section is too dense and particularly lacking in good use of scientific language.

3. Some examples to the above two points:
- L13: "possess the superiority"
- L19 "intractable reward difference": Monte Carlo estimation makes this quite tractable.
- L23: "pure distribution internally": unclear what this means.
- L52: why "fundamentally"?
- L53: "equivalent" task-relevant features: equivalent how?
- L75: "certain favorable properties"?
- L78: "effective relaxation and strengthening in specific aspects"?
- L160: stacking frames does not lift partial observability
- L163: why is the reward a function of $\phi_\omega(s_t)$ and not $s_t$?
- L216: "In optional $d_\pi$": unclear what is being said here.
- L240: "But seriously,..."
- etc.

4. The motivation behind the particular alterations to the well-studied bisimulation formulation seem arbitrary and poorly motivated, sounding more like a marketing pitch than scientifically rigorous ideas. It is unclear to me how task relevance, which inherently depends on the reward function, is maintained when the reward difference term of bisimulation is replaced by some Gaussian noise arbitrarily.
5. The method is called "Scalable" Representation Learning, but it isn't clear to me how the scalability of the proposed approach is any different from prior work, e.g., MiCO by Castro et al. (2022).
6. The T-step unrolling of the transition distance seems like a hack and seems overly susceptible to high modelling errors due to compounding.
7. The identification of the representation collapse issue of $\pi$-bisimulation in sparse reward environments (the central focus of this paper) and Theorem 4.1 is incorrectly attributed to Liao et al. (2023), when in fact this was first studied by Kemertas et al. (2021); see their more general Lemma 2 with $c_R=1, c_T=\gamma$. The latter work is not mentioned until the end of Sec. 4.3 in Page 7.
8. Experiments do not compare to Kemertas et al. (2021), whose modifications of DBC (addition of embedding normalization, intrinsic rewards and inverse dynamics regularization) substantially improved performance, especially in sparse reward environments and would therefore comprise a stronger baseline. 
9. L395: unclear why "challenging size of 2e5" is selected as the replay buffer size. This may be unfairly disadvantaging baseline methods.

### Questions
Why is the assumption A.1 not included in the main text, before the theorems that rely on them are presented?

### Soundness
1

### Presentation
1

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper proposes a scalable representation learning approach (SRL) designed to improve the stability of representations under sparse-reward settings in reinforcement learning (RL). The core contribution is the introduction of a weak bisimulation metric, which relaxes traditional bisimulation metrics by eliminating the reliance on reward differences and incorporating a trainable Gaussian distribution. This relaxation is intended to address the challenges of representation collapse and degeneration that traditional bisimulation metrics face in sparse-reward environments. Additionally, the approach introduces continuous differences in the transition distribution to enhance task-relevant feature extraction. The proposed SRL is empirically validated on several sparse-reward RL benchmarks, such as DeepMind Control Suite, MetaWorld, and Adroit tasks, where it outperforms state-of-the-art methods.

### Strengths
The introduction of a weak bisimulation metric that relaxes strict assumptions while maintaining bisimulation's theoretical advantages is a novel and important step forward. The experiments are extensive, covering a variety of challenging tasks across multiple domains (DMControl, MetaWorld, Adroit), and the proposed SRL consistently outperforms baseline methods, including state-of-the-art approaches. The paper is generally well-structured, with a clear explanation of the problems with traditional bisimulation metrics and a well-motivated introduction of the weak bisimulation metric.

### Weaknesses
The paper assumes that Gaussian noise can effectively relax reward differences, but the implications of this assumption could vary across different environments. More detailed ablation studies that explore different noise distributions or parameterizations might provide further insights into the generalizability of the approach. Specifically, the choice of a Gaussian distribution, while convenient, lacks a strong theoretical justification within the context of bisimulation metrics. The paper does not sufficiently explore the sensitivity of the results to the variance of the Gaussian noise, which could significantly impact the learned representations. Furthermore, the method's reliance on continuous differences in the transition distribution, while intended to enhance feature extraction, might introduce instability or sensitivity to hyperparameter tuning, which is not thoroughly addressed in the paper.

### Questions
Are there cases where the Gaussian assumption might not hold, and what alternatives would work better in those situations?

Could the performance of SRL be further improved by considering more complex forms of the transition distribution (e.g., non-Gaussian distributions), or is the flexibility provided by the Gaussian noise sufficient for most sparse-reward settings?

How does SRL compare with methods designed for dense-reward tasks? While the paper focuses on sparse-reward environments, could the approach offer any advantages in settings where rewards are more frequent?

### Soundness
3

### Presentation
3

### Contribution
3

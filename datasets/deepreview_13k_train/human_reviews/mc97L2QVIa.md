# Offline Multi-agent Reinforcement Learning with Sequential Score Decomposition

- Decision: Reject
- Scores: 3, 3, 3

## Abstract
Offline multi-agent reinforcement learning (MARL) faces significant challenges due to distribution shift issues, exacerbated by the high dimensionality of joint actions and complex joint behavior policy distributions. 
While existing methods often focus on independent learning or offline value decomposition with conservative value estimation, they may still lead to out-of-distribution (OOD) joint actions and reduced performance. 
This is primarily due to the lack of exploration opportunity and implicit policy dependencies in offline settings. 
To address these challenges, we propose an offline policy decomposition method incorporating joint policy regularization constraints. 
Our approach utilizes a diffusion generative model to capture the joint behavior policy, followed by a decomposition of the extracted score function. 
This decomposition is then used to regularize individual policies in a decentralized manner. 
Experimental results demonstrate that our method achieves SOTA on continuous control tasks in standard offline MARL benchmarks.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
My understanding of the paper is the authors want to propose a two-stage algorithm for offline MARL:
1) use diffusion model to learn the joint behavior policy (or multiple behavior policies) mu, 
2) then apply offline RL methods with divergence-based behavior-regularization, a multiagent variant version of BRPO in this case -- where the regularizer is reverse KL:    E_{s \sim D} KL(pi_theta(s) || mu(s)).

In particularly, the authors assume the agents take actions sequentially to ease optimization. The gradient of log mu(a_i | s, a_{<i}) i.e., the score function of mu(a_i | s, a_{<i}) can be obtained by diffusion model (using score-matching formulation) with corresponding loss.

MARL is not my field, so I cannot evaluate the experiments. For the formulation and motivation, I think the work is incremental and potentially have math flaws, see my comments below. My impression is the authors gives some reasons for using diffusion model, but the motivation is not significantly strong.

### Strengths
.

### Weaknesses
MARL is not my field.  I only have some experience in single-agent offline RL & diffusion model. However, there are still several concerns about this work:

1. The authors motivated the sequential decomposition of joint policy by coordinate descent (btw, please note the optimization algorithm is called coordinate descent, not coordination descent) and multi-agent Transformer. This feels tenuous to me. For MAT, as Transformer is an AR model, it is natural to use sequential decomposition, but why do you choose diffusion model if you target a sequential problem? Also, how do you get conditional score \nabla_{a_i} mu(a_i | s, a_{<i})?  IIUC, if you train a joint-policy diffusion model, you can't get such decomposition. Do you train multiple diffusion models? That surges the computation cost.

2. The authors also motivates the use of diffusion as its expressiveness for modeling multi-modal data. This is true, however, I didn't understand the example you game. Figure 1: I guess different colors mean different actions? It's clear as the dataset quality decreases, the distribution becomes more uniform (looks like a uni-modal Gaussian for Random), instead of multi-modal as in the expert dataset. This is contradicting the caption.

3. I am worried the calculation of the gradient is off. For example, Page 16, from Equation (14) to (15), you ignored the gradient w.r.t the entropy H(pi_i). Similarly, you ignored it for the proof of proposition 2 on page 18. Page 19, you want to compute the gradient of theta_1 w.r.t pi(a_1|s) log pi(a_1|s),  but you treat the first pi(a_1|s) as a constant.

### Questions
.

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper proposes an offline MARL method based on the Behavior-Regularized Policy Optimization (BRPO) framework. Instead of extracting policies from Q-function factorization, the authors use a diffusion model to learn a score function (i.e., the gradient of the log of the behavior policy). This score function is then incorporated into the BRPO objective to extract local policies. Numerical comparisons are provided using MAMujoco’s HalfCheetah-v2.

### Strengths
The use of diffusion models to explore data distributions in MARL is interesting.

### Weaknesses
 - The proposed methodology seems incremental. The results up to Section 3.1 are well-known, and the authors mostly repeat established formulations from the BRPO framework.
- The idea of decomposing the score function lacks clear motivation and insight. It’s not evident why decomposing the score function would resolve the issues from prior work. The section on score decomposition is too brief (while other sections present mostly known results), giving the impression that the proposed method is in an early stage and lacks depth.
- The experiments are superficial. MAMujoco includes several benchmark tasks, yet the authors only provide comparisons with HalfCheetah-v2. Other widely used offline MARL benchmarks, such as MPE, SMACv1, and SMACv2, are omitted.
- The comparison lacks some recent baselines, e.g., OMIGA [1].

### Questions
- Could authors provide more detailed explanations or theoretical justifications for why score decomposition addresses the limitations of previous approaches.
- How does the proposed method perform with other MAMujoco tasks (Ant or Humanoid)? Why was HalfCheetah-v2 chosen for the experiments? Why weren’t other standard benchmarking tasks, such as SMAC and MPE, considered?
- How's your method compared to other SOTA MARL algorithms such as OMEGA [1] or even a standard BC (which might perform well in certain scenarios)?

------------------------------

**Post-Rebuttal**

The authors have made some effort to address my concerns; however, I find their responses either unconvincing or insufficient, as several of my major concerns remain unresolved. Specifically, I requested comparisons on standard SOTA benchmarks like SMAC_v1 and SMAC_v2, which are widely used in recent and state-of-the-art offline MARL studies. Unfortunately, the authors did not make an effort to address this critical point. This omission weakens the contributions of the paper, rendering them less significant. As a result, I maintain my current rating.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This work focuses on addressing OOD joint actions in Offline MARL. To this end, the authors introduce Offline MARL with Sequential Score Decomposition (OMSD) which uses diffusion models to capture multimodal policy distributions. OMSD learns a centralized critic as well as sequential diffusion models for the behavior policy, which are each used for training decentralized  target policies. Their method is evaluated on HalfCheetah where it performs on-par with or below the baselines.

### Strengths
1. The motivation for the paper is clear, and there is a nice flow between the problems with previous approaches (independent learning and IGM) and OMSD. 
1. As far as I know, there is no previous offline MARL approach which is able to learn multimodal policies, making the problem important.

### Weaknesses
1. My main concern is whether $\mathcal{L}_{OMSD}^i$ (Eq.12) actually learns multimodal policies. Even if the multimodal optimal policy can be learned through regularization with a joint behavior policy (learned by diffusion models), there is no correlation mechanism at test time. This suggests that OMSD might not be able to solve the XOR Game for example, which is considered in AlberDICE and also mentioned in the paper.
1. Related to 1, I’m having a hard time interpreting the results in Figure 2. Without this, it is not clear whether OMSD indeed does learn optimal multimodal policies.
1. The algorithm is missing some details and it is not clear where the diffusion models are used (e.g. only for learning the behavior policy or also for the target policy)
1. Lack of relevant baselines namely MADiff, which also uses diffusion models for Offline MARL and AlberDICE, where the motivation is quite similar
1. Mixed results in MAMuJoCo, especially in the Random dataset where it performs significantly lower than other baselines. Furthermore, only one setting (HalfCheetah) is considered. 
1. No open source code and details on hyperparameters
1. (Minor) SSD is used in Line 322 and in Table 1 but this is not defined.
1. (Minor) Lines 113-118 is confusing since the notation is using $x$ to denote each agent while $i$ is used elsewhere. Also $x$ is used again in 2.2.

### Questions
1. If FOP and AlberDICE uses the IGO assumption (Lines 222-223), how is OMSD able to not rely on these assumptions? In particular, which part of the algorithm allows OMSD to learn multimodal policies?
1. What is the purpose of using diffusion models? For instance, why is it better than using MLPs for learning the joint behavior policy with sequential action selection?
1. Please address each point in the Weaknesses.

### Soundness
1

### Presentation
2

### Contribution
2

# Pushing the Limit of Small-Efficient Offline Reinforcement Learning

- Decision: Reject
- Avg Score: 4.50
- Scores: 3, 6, 3, 6

## Abstract
Offline reinforcement learning (RL) has achieved notable progress in recent years. It enables learning optimized policy from fixed offline datasets and, therefore is particularly suitable for decision-making tasks that lack reliable simulators or have environment interaction restrictions. However, existing offline RL methods typically need a large amount of training data to achieve reasonable performance, and offer limited generalizability in out-of-distribution (OOD) regions due to conservative data-related regularizations. This seriously hinders the usability of offline RL in solving many real-world applications, where the available data are often limited. 
In this study, we introduce a highly sample-efficient offline RL algorithm that learns optimized policy by enabling state-stitching in a compact latent space regulated by the fundamental symmetry in dynamical systems. Specifically, we introduce a time-reversal symmetry (T-symmetry) enforced inverse dynamics model (TS-IDM) to derive well-regulated latent state representations that greatly ease the difficulty of OOD generalization. Within the learned latent space, we can learn a guide-policy to output the latent next state that maximizes the reward, bypassing the conservative action-level behavior constraints as used in typical offline RL algorithms. The final optimized action can then be easily extracted by using the guide-policy's output as the goal state in the learned TS-IDM.
We call our method Offline RL via T-symmetry Enforced Latent State-Stitching (TELS).
Our approach achieves amazing sample efficiency and OOD generalizability, significantly outperforming existing offline RL methods in a wide range of challenging small-sample tasks, even using as few as 1\% of the original data in D4RL tasks.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper proposes (1) a T-symmetry enforced dynamics model, and a (2) a advantage weighted next latent state predictor + inverse dynamics models to create an offline RL algorithms. The goal is to use both of these inductive biases to improve the sample efficiency in offline RL.

### Strengths
The quality of writing and clarity is good throughout. The main strength of this paper seem to be the results in Figure 1 on Ant-maze datasets, but I think this is partly because the baselines are chosen are just not good enough (more in questions and weaknesses).

### Weaknesses
1) The primary weakness is the complexity and the number of moving parts of this paper. The algorithm contains:
    (a)  state encoder
    (b)  state decoder
    (c)  action encoder
    (d)  action decoder
    (e) latent inverse dynamics model
    (f)  latent ODE forward model
    (g) latent ODE reverse model
    (h) latent state value function
    (i)  latent stochastic guide-policy
  As a result of this, the number of loss function terms is also very high (>6 as far as I can tell), making it extremely unclear why the algorithms is actually working. Although complex problems can justify complex architectures and loss functions, I do not think antmaze / other toy offline RL settings warrant such a arduous setup. The strong coupling between the various components, while potentially beneficial, also makes it difficult to isolate the impact of each component. For example, the T-symmetry constraint is applied to the latent forward and reverse models, but it is unclear if this is the primary driver of performance or if the performance gains are due to the complex interplay of all the components. This makes it difficult to understand the core contribution of the method and how it compares to simpler alternatives.

2) In Table 1, I think there are many important baselines missing - Goal condition Behavior cloning, HIQL (which is cited multiple times in the paper) or other hierarchical / model based methods like the decision diffuser.

### Questions
On line 148, you mention -- "making Q-function maximization the only option for policy optimization, which inevitably requires adding conservative action-level constraints", but your algorithm uses the same conservatism while training the guiding policy using advantage weighted behavior cloning. Could you clarify this?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors propose a new sample-efficient offline RL algorithm (TELS) based on a Time-Reversal Symmetry-Enforced Dynamics Model (TDM). Compared to the baseline algorithm (TSRL: Time-Reversal Symmetry Regularized Offline RL), they introduce a T-Symmetry Enforced Inverse Dynamics Model (TS-IDM) to derive regulated latent state representations that facilitate OOD generalization. Through state-stitching in a compact latent state space, they can efficiently obtain optimized next states from a guide policy. In experiments with small-sample tasks, they demonstrate superior performance compared to state-of-the-art offline RL algorithms.

### Strengths
* They address several weaknesses of existing algorithms by leveraging T-symmetry.
     * TELS separates the state-action encoder used in the TSRL algorithm into two components: a state encoder and a latent inverse dynamics module. By incorporating the state encoder in the policy optimization process, TELS promotes stable learning and improves the generalization of the state-value function (using an IQL-style method) through more compact and well-behaved representations.
     * Furthermore, by utilizing the latent inverse dynamics, the guide policy outputs the next states that maximize the reward. In action inference, no additional training process is required due to the use of the learned TS-IDM.
     * TSRL showed no noticeable performance improvement over existing offline algorithms, particularly in AntMaze. In contrast, TELS demonstrate significant performance improvements across most datasets.

### Weaknesses
 * In Equation 9, the complete training loss function of TS-IDM comprises $\ell_{s-rec}$, $\ell_{fwd}$, $\ell_{rvs}$, $\ell_{s-ode}$ and $\ell_{T-sym}$. However, despite the latent inverse dynamics model's loss ($\ell_{inv}$) being specified in Equation 4, I am unable to locate this specific loss term. I am curious whether this loss is implicitly embedded within other terms or if it was simply not explicitly indicated.
*  In Figure 3, they examine the generalizability of TELS by constructing a more challenging scenario in which a portion of samples is removed. However, even as the deletion ratio increases, it appears that all state points are still represented in each figure, though the number of samples for each state decreases. It remains questionable whether performance would improve even if certain state areas were missing. This raises concerns about the true out-of-distribution (OOD) generalization capability of the method, as the state space is still fully covered, just with varying densities of samples. A more rigorous evaluation would involve completely removing data from specific regions of the state space, not just reducing the sample density within those regions.


### Questions
In addition to questions about potential weaknesses, I would like to raise a few more questions:
* Compared between Table 1 (small data) and Table 7 (full data), Antmaze-m-p and Antmaze-l-p show slightly higher performance when using the smaller dataset. How would you interpret these results?
* In Table 3, IQL with TS-IDM representation shows improved performance (Hopper-m: 54.1, Walker2d-m: 41.3) but still underperforms compared to TELS (Hopper-m: 77.3, Walker2d-m: 62.4). Given that TELS utilizes an IQL-style state-value function update, the primary difference between TELS and IQL lies in the policy improvement or optimization process. What do you think is the key factor behind this result?
* In Algorithm 1 of the TSRL paper, they enhance policy training by adding augmented samples to the dataset. Are you proposing that your algorithm trains solely on the reduced data without any data augmentation?
* In Table 5 of the TSRL paper, they report results only for the Antmaze-u and Antmaze-u-d datasets. In contrast, in Table 1 of the TELS paper, TSRL results are included for additional datasets—such as Antmaze-m-d, m-p, l-d, and l-p. Since TELS performs well on these datasets, it seems unusual that TSRL, its baseline, shows a normalized score of zero on certain tasks. Does a zero score indicate that TSRL actually achieved no performance on these tasks, or does it mean these datasets were not evaluated?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper first proposes a T-symmetry enforced inverse dynamics model (TS-IDM) to construct a latent space. And then use the T-symmetry to regularize the guide-policy learning. The method TELS (Offline RL via T-symmetry Enforced Latent State-Stitching) exhibits exceptionally high data efficiency on D4RL with small-sample setting.

### Strengths
1. The paper provides a thorough introduction to the background and preliminaries. Combined with the clear writing logic, the entire paper is quite easy to understand.
2. The proposed method has achieved a performance that significantly surpasses all baselines under the small-sample setting, reaching the current state-of-the-art (SOTA).

### Weaknesses
The paper seems to be a **straightforward fusion** of POR (Policy-guided Offline RL) and TSRL (T-Symmetry regularized offline RL).

1. Compared with TDM in TSRL, the proposed TS-IDM introduces a latent inverse dynamics model ($h_{inv}$), which appears to be designed for the policy execution in POR. 
2. While TSRL employs the offline algorithm TD3+BC, this paper chooses POR. 

In summary, I believe the novelty and contribution of the proposed algorithm are relatively limited.

### Questions
1. In overall learning objective (9), the loss function of inverse dynamic model (4) is missing.
2. Considering TS-IDM as a specialized form of dynamic model, it is essential to compare it with model-based offline algorithms.
3. On line 361, the sentence is missing a period at the end.

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper introduces a T-symmetry enforced inverse dynamics model (TS-IDM) into offline reinforcement learning. Overall the proposed TS-IDM is a latent space inverse dynamics model, which exploits the time-reversal symmetries of the underlying dynamics system to regularize the derived representations. The authors claim that such representations encode the information about the dynamics system, and generalize well in the out-of-distribution area. Based on this interpretation, they combined the representations with POR, a former offline RL  algorithm that stitches trajectories in the state space, and outperformed all existing baseline algorithms, especially in the low-data scenario.

### Strengths
1. The motivation is clearly presented. Sufficient dataset coverage is vital for reward maximization in both action-space or state-space and fine-grained representation may help to alleviate the need for dataset coverage. 

2. The rationale behind the proposed method is plausible to me. I agree that the inductive bias of time-reversal symmetries extends beyond simple data augmentation techniques (e.g. Gaussian perturbations) and deserves more attention from the RL community. Although this is borrowed from TSRL, this paper refines several practices, such as maximizing the reward in the state space and thus constructing the latent representation based on states, rather than state-action pairs. The empirical performance looks good to me.

### Weaknesses
1. The overall objective looks extremely complex. It consists of 6 terms in total and each term is coupled with each other. Apart from the TS-IDM training, the policy optimization objective is also heavily dependent on hyper-parameters such as  $\tau$, $\alpha$, $\beta$, dropout rate and learning rates. 

2. There is no clear discussion about the potential limitations of the proposed method. For example, the time-reversal symmetries seem to require that the dynamics can be expressed as an ODE. However, such ODE formulation may no apply to certain types of control systems, e.g. systems with stochastic transitions or partial observability. The authors are encourages to include more discussions about whether the ODE formulation is universally applicable, and if it is not, what is the scope of its application.

### Questions
1. The objective defined in Eq. 9 provides gradients for all modules in the TS-IDM, right? Did the authors detach the gradient of some parts of the TS-IDM training for some components of the loss? 

2. Could the authors include performance and loss curves as supplementary materials? This would help readers comprehensively evaluate the proposed method from other perspectives, including learning dynamics, convergence speed, training stability, and also asymptotic performance.

some copy-edits: 
1. line 218, $\phi_s$ should be $\psi_s$
2. line 651, TS-IMD should be TS-IDM
3. the loss term for inverse dynamics is missing in Eq. 9

### Soundness
3

### Presentation
3

### Contribution
2

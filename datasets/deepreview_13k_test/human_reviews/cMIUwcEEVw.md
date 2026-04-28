# RAVL: Reach-Aware Value Learning for the Edge-of-Reach Problem in Offline Model-Based Reinforcement Learning

- Decision: Reject
- Scores: 3, 8, 6, 3

## Abstract
Offline reinforcement learning makes use of pre-collected datasets and has emerged as a powerful paradigm for training agents without the need for expensive or unsafe online data collection. This offline approach, however, introduces the additional challenge of evaluating values for state-actions not seen in the dataset---termed the out-of-sample problem. Model-based approaches deal with this by allowing the agent to collect additional data through rollouts in a learned dynamics model. The prevailing theoretical understanding is that this effectively resolves the out-of-sample issue, and that any remaining difficulties are due to errors in the learned dynamics model. Based on this understanding, one would expect improvements to the dynamics model to lead to improvements to the learned policy. Surprisingly, however, we find that existing algorithms completely fail when the true dynamics are provided in place of the learned dynamics model. This observation exposes a common misconception in offline reinforcement learning, namely that dynamics model errors do not explain the behavior of model-based methods. Our subsequent investigation reveals a second major and previously overlooked issue in offline model-based reinforcement learning (which we term the edge-of-reach problem), whereby values of states that are only reachable in the final step of the limited horizon rollouts are pathologically overestimated, similar to the out-of-sample problem faced by model-free methods. This new insight fills some of the gaps in existing theory and allows us to reinterpret the efficacy of prior model-based methods. Guided by this understanding, we propose Reach-Aware Value Learning (RAVL), a value-based algorithm that is able to capture value uncertainty at edge-of-reach states. Our method achieves strong performance on the standard D4RL benchmark, and we hope that the insights developed in this paper aid the future design of more accurately motivated offline algorithms.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper focuses on the model-based offline reinforcement leanring algorithms, and different with prior works, this paper finds that the current model-based offline RL algorithms still fail even if the real dynamic model is accessible and attributes this failure to the edge-of-reach problem. Then the authors propose Reach-Aware Value Learning (RAVL) to mitigate this new issue.

### Strengths
This paper proposes a surprising and potential problem in model-based offline RL;

### Weaknesses
1. Though this paper points out a novel problem that may be existed in offline RL, the theoretical and empirical evidence seem to be confusing;
2. This proposed approach, RAVL, does not appear to be reasonable for this particular edge-of-reach problem.

see below for details.

### Questions
1. This paper use two similar expressions, 'out-of-sample' and 'out-of-distribution', are these two expressions the same or different?
2. According to this paper, the edge-of-reach problem seems to be due to specific interactive schemes of some particular RL tasks, instead of applying to model-based or model-free settings in general. 
3. It's confusing that, Table.1 aims to illustrate that it is the edge-of-reach problem that  causes the failure for model-based offline RL methods, while the simple experiment in Figure.2 don't include any model-based methods (SAC is a typical model-free methods). 
4. About the proposed method, it's just the previous EDAC algorihtm which is trained with additional sythnesis rollouts through the learned dynamic model. So I can't understand how it can sovle the edge-of-reach issue. It's said to avoid overestimations at edge-of-ereach states, however, the proposed method imposes pessimisic estimation on all training data (according to Eq.3), without distinguishing whether the samples belong to edge-of-reach states or not.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper begins by presenting the surprising finding that typical model-based offline RL algorithms fail when provided with oracle dynamics, flaunting the conventional wisdom that these algorithms aim primarily to address exploitation of model inaccuracies. This finding leads to the main conceptual contribution of the paper, which is the “edge of reach” problem: in these model-based offline RL algorithms, which use short-horizon rollouts to collect additional synthetic data for training, some states can only be reached in the final step of rollouts, and thus the Bellman backup targets computed at those states are prone to estimation error. Based on this understanding, the authors propose Reach-Aware Value Learning (RAVL), which eschews explicit dynamics uncertainty quantification in favor of pessimism with respect to a critic ensemble, as in Ensemble-Diversified Actor Critic (EDAC), a model-free offline RL algorithm. RAVL is evaluated on a subset of the D4RL benchmark, where it exhibits performance competitive with the SOTA.

### Strengths
* The paper demonstrates a significant misconception in the literature of model-based offline RL, i.e. that addressing model inaccuracy is a primary reason why these algorithms can succeed. This finding, along with the identification of the edge-of-reach problem, is likely to have a substantial impact on future algorithmic work in this area.
* In addition to evaluating on a subset of the standard D4RL benchmark, the authors include a more in-depth exploration in a simple environment where the edge-of-reach issue can be cleanly studied.
* The proposed algorithm, RAVL, addresses the edge-of-reach problem and displays compelling performance without explicitly quantifying dynamics uncertainty (which is a challenging problem).

### Weaknesses
The D4RL evaluation includes only the basic MuJoCo tasks. The authors could try a more complex environment such as AntMaze or Adroit to further demonstrate the strength of the algorithm over previous methods.

### Questions
While RAVL seems to be effective at addressing the edge-of-reach problem, it may require a large ensemble (e.g. 50 models) to achieve sufficient pessimism, which could be computationally expensive. I was curious if you considered/experimented with adding a small explicit penalty to the values of states at the final step of the rollouts?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents an intriguing finding that challenges the conventional view of model-based offline reinforcement learning: the erroneous dynamical model does not account for the behavior of model-based methods; rather, it is the overestimation of the value of states that are difficult to reach that explains their behavior. This paper proposes a simple Reach-Aware Value Learning to solve the out-of-sample problem by capturing value uncertainty at edge-of-reach states. The illustration experiment is sound and makes sense.

### Strengths
+ This paper is meticulously written and excellently structured, providing ample background information and a well-defined problem statement.

+ The findings presented in this paper are interesting, revealing how the overestimation of the value of states that are difficult to reach can have a significant impact on the optimization of offline model-based RL policies.

+ The proposed solution, RAVL, is both simple to implement and highly effective in addressing this problem.

### Weaknesses
+ **The problem addressed in this paper may not be influential.**
+ **The benchmark environment used in this research is relatively simplistic.** It would be interesting to investigate whether or not the proposed method performs satisfactorily in more complex environments.
+ **The modifications made to the experiments in this paper do not appear to be particularly substantial.**

### Questions
+ I do not fully understand the Figure 3. How is the figure generated? Why is the conclusion drawn: "As desired, RAVL is effective at capturing the value uncertainty for state-actions which transition to edge-of-reach nextstates."?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies offline MBRL. The authors first show a surprising experimental result: the existing offline MBRL method MOPO does not work when replacing learned models with true dynamics models. They claim that the reason for this failure is the overestimation of values on the edge-of-reach states which are only reached at the final time steps of the limited horizon rollouts. To address this issue, they propose a new method RAVL which combines EDAC and MOPO. They validate the performance of RAVL on a simple 2D environment and D4RL benchmarks.

### Strengths
1. The experiments in Section 4.1 are very interesting and insightful. They found that MOPO surprisingly fails when replacing learned models with true dynamics models. This result provides a new understanding of offline MBRL: the model error is not the only issue in offline MBRL.  
2. The paper is well-written and easy to follow, providing clear explanations and detailed descriptions of the proposed method and experimental results.

### Weaknesses
1. The authors first reveal the key overestimation issue of values on edge-of-reach states in offline MBRL. However, as a direct combination of EDAC and MOPO, the proposed method RAVL is largely independent of the revealed issue. In particular, the only difference between RAVL and MOPO is that RAVL exhibits the Q-update rule in EDAC. However, such a Q-update rule is performed on all states in the buffer and is not tailored for edge-of-reach states. RAVL does not identify edge-of-reach states and correct the corresponding values to address the claimed issue.
2. There is a large gap between the formalization in Section 4.3 and actual offline MBRL methods. First, the definition of edge-of-reach states is very limited. Concretely, such a definition only considers the case where the starting states of model rollouts are only sampled from the initial state distribution. However, in offline MBRL,  the starting state could be any state along the trajectories in the offline dataset. Such a gap leads to a problem that the Edge-of-reach states defined in Definition 1 could be **not** edge-of-reach in model rollouts with different starting states. For instance, let $(s_0, a_0, s_1, a_1, s_2, a_2)$ be a trajectory in the offline dataset. We consider two types of model rollouts with different starting states: $(s_0, \hat{a}_0, \hat{s}_1, \hat{a}_1, \hat{s}_2, \hat{a}_2)$ and $(s_1, \tilde{a}_1, \tilde{s}_2, \tilde{a}_2,  \tilde{s}_3, \tilde{a}_3)$. Here $\hat{s}_2$ is edge-of-reach for the first type of model rollouts but could be not edge-of-reach for the second type of model rollouts.
Second, Proposition 1 considers an extremely simple case where the Q-update is performed only on a single model rollout. However, in MBRL, Q-updates are performed on multiple model rollouts where states could be overlapped. In this case, the analysis of Q-functions could be much more complicated.
    
3. The empirical performance of RAVL is not strong. In D4RL, the existing method MOBILE beats RAVL regarding the number of best-performance tasks, implying that the improvement of RAVL is limited.

### Questions
Typos:

1. In Eq.(3), $+\gamma$ should be $-\gamma$

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

# Fat-to-Thin Policy Optimization: Offline Reinforcement Learning with Sparse Policies

- Decision: Accept
- Scores: 8, 8, 3, 8

## Abstract
Sparse continuous policies are distributions that can choose some actions at random yet keep strictly zero probability for the other actions, which are radically different from the Gaussian.
They have important real-world implications, e.g. in modeling safety-critical tasks like medicine.
The combination of offline reinforcement learning and sparse policies provides a novel paradigm that enables learning completely from logged datasets a safety-aware  sparse policy. 
However, sparse policies can cause difficulty with the existing offline algorithms which require evaluating actions that fall outside of the current support.
In this paper, we propose  the first offline policy optimization algorithm that tackles this challenge: Fat-to-Thin Policy Optimization (FtTPO).
Specifically, we maintain a fat (heavy-tailed) proposal policy that effectively learns from the dataset and injects knowledge to a thin (sparse) policy, which is responsible for interacting with the environment.
We instantiate FtTPO with the general $q$-Gaussian family that encompasses both heavy-tailed and sparse policies and verify that it performs favorably in a safety-critical treatment simulation and the standard MuJoCo suite.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper introduces a novel approach for learning sparse policies within the context of offline RL. Sparse policies are crucial for enhancing safety, as they prevent the policies from considering all possible actions, which can reduce potential risks. Unlike existing methods that rely on ad hoc techniques such as reverse KL divergence or random action replacement, this study proposes the Fat-to-Thin Policy Optimization (FtTPO) algorithm. This algorithm leverages the deformed q-exponential function to parameterize policies and employs a greedy two-stage actor-critic optimization approach. The result is a method that achieves desirable sparsity and outperforms existing techniques in simulated deep offline RL tasks.

### Strengths
- The paper presents an innovate approach for learning sparse policies from logged datasets that outperform current offline RL methods.
- The work is empirical rigorous, with sufficient analysis and abalations of the proposed method on a variety of simulated tasks - including safety-critical  bencahmark and Mujoco. 
- The paper is clearly written and accessible, making it easy to understand the authors' arguments and methodology.

### Weaknesses
- It could be great if the authors can provide insight into why the combination of forward and reverse KL (with the two-stage optimization framework) helps in the first place? 
- Another element that the work is missing is to compare how the proposed method works in low-data regime. In a lot of safety-critical settings, size of the datasets are quite limited, so it would have been nice to have that analysis in the paper.

### Questions
- A primary factor contributing to the success of the proposed algorithm appears to be the use of the weighted q-exponential function in the objective. According to line 241, $ q = 0 $ is used in practice. If so, then how does that affect filtering of "bad actions"?

- In algorithm 3, won't copying $\mu_{\phi_t}$ to $\mu_{\theta_t}$ violate the original choice of the policy parametrization? Is the sampling procedure still valid after copying only parameters and not changing the associated sampling parameters? 


Minor comments: 
- How to pronounce FtTPO? 
- Typo in line 52 (algorithmsk)

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper proposes a novel approach for offline reinforcement learning with sparse policies. Sparse policies have important real-world implications but pose challenges to existing algorithms. The paper presents Fat-to-Thin Policy Optimization (FtTPO), a two-stage learning method that addresses these challenges.

### Strengths
The paper presents a novel FtTPO algorithm for handling sparse policies in offline reinforcement learning. This is a new combination of ideas as it builds on two-stage actor-critic methods and uses a fat (infinite-support) policy to inform a thin (sparse) policy. It addresses the previously less-studied problem of out-of-support actions in offline learning with sparse policies, providing a solution where prior works relied on ad hoc methods.

The paper is well-structured, with clear sections for introduction, background, method description, experiments, and related works.

### Weaknesses
The safety benefit of having a thin (sparse) policy isn't directly clear to readers. The authors somehow use 'performance' and 'safety' interchangeably and imply that a higher reward means higher safety.  A very common misunderstanding is that 'dangerous action' means 'higher dosage'. For example, the daily insulin dosage for T1 diabetic patients is around 0.5-1 unit per day. A 0.001 unit dosage can be considered a low dosage. However, if such a dosage is given per 2 min, the accumulative dosage will far exceed body tolerance and cause serious damage to the patient. In fact, 'dangerous states and actions' are precise in medicine. In domains such as dynamic treatment regimes, dangerous states are explicitly defined. I encourage the authors to define safety clearly before using it. Besides, the authors can visualize the occurrence of dangerous states following their policy versus baseline policies to see if safety is indeed enhanced.

### Questions
NA

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
This paper proposes a novel architecture for learning sparse policies in an offline RL paradigm. Specifically, the authors address issues of domain alignment when training sparse policies, whereby the sparse policy may not support actions within the offline dataset. The induced sparse policy placing measure 0 probability over part of the offline dataset can result in numerical instabilities, for example, when using a log likelihood loss.
The proposed architecture requires first learning a “fat” (or non-sparse policy) policy i.e., a policy with at least the support of the offline dataset (the authors propose a Gaussian), which is subsequently refined to a “thin” policy using existing methods for learning sparse policies i.e., using the reverse KL divergence.

### Strengths
-	Originality: To the best of my knowledge the method of induing a sparse policy from one with a larger support has not been explored and as such, the research is original. 
-	Clarity: The paper is well presented and written in the sense that relevant (to the best of my knowledge) existing work is contextualised, the proposed solution is well defined and the paper is generally easy to follow.
-	Quality and Significance: The problem is well motivated and thus assuming the solution can be demonstrated to provide significant performance improvements over existing “ad-hoc” approaches, the “fat to thin” architecture  would be of great significance to practioners aiming to learn sparse policies in an offline setting. Furthermore, the breath of evaluation benchmarks used is reasonable in the sense that a reasonable number of challenging offline RL benchmarks have been used.

### Weaknesses
The core weakness of the paper is the experimental approach. The authors consistently draw conclusions that it is “surprising” that the proposed architecture performs so well given the “sparse policy” (referenced in section 5.2) or given the relative simplicity of the proposed architecture (referenced in section 5.3). I disagree with this line of analysis for several reasons:
-	A sparse policy working “surprisingly well” is not a substantively validated claim as the authors do not explain why it is surprising. Without this additional analysis, the performance of the proposed method is inconsistent and only obtains notable performance on the Medium-Expert and Medium-Replay HalfCheetah datasets.
-	The authors have not made clear why the proposed architecture is less complex and I would contest, that given two policies are required to be maintained, the proposed architecture is actually more complex than the existing baseline approaches.
Broadly speaking, the proposed architecture appears to be overly complex and the experimental direction of demonstrating that the architecture performs “at least as well as” existing methods is not strong enough to support this additional complexity. 
Additionally, it is not completely convincing that the proposed architecture is necessary. Based on Figure 6, the proposal only policy (utilising existing and simpler methods for learning sparse policies) performs on par with the proposed architecture. Furthermore, from Figure 5, the proposal policy appears to already learn a relatively concentrated policy. As such, it is unclear why using only proposal policy and preventing actions being selected outside X standard deviations would not achieve the desired result (assuming an improper distribution of the resulting policy is reasonable).
Overall, I would encourage the authors to revisit the experiments and strive to obtain stronger results that demonstrate solid benefits of the algorithm. Deriving a novel architecture and having it reasonably converge is no mean feat however, the results presented in the paper are not yet ready for publishing. It might be worth exploring why the proposed architecture performed better on the aforementioned HalfCheetah environments to understand the types of environments where the fat-to-thin model is strongly beneficial.

### Questions
-	Understanding why the authors feel the fat-to-thin architecture is less complex than existing methods and why it is surprising the a sparse policy competes with existing methods would help in changing my opinion.

### Soundness
1

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper studies offline reinforcement learning in continuous action settings where it is desired to learn a sparse policy (that has zero probability for some actions) that is stochastic. This occurs, for instance, when there is a safety aspect and so some parts of the action space should have zero probability. This paper creates a new algorithm for this setting based on a two-stage actor-critic approach, where a non-sparse proposal policy learns and injects knowledge into a sparse actor. There are quite a few design decisions along the way. The resulting method FtTPO is compared to a large number of existing methods on both safety-motivated and general RL (Mujoco) benchmarks. On the safety benchmarks, it is the strongest, and on general RL it is very competitive.

### Strengths
- The paper is excellent at contextualizing its contributions relative to existing work.
- The description of the algorithm, the design decisions, and the motivations behind the design decisions is clear.
- FtTPO makes design decisions that are different than previous algorithms.
- Experimental results are strong against a wide variety of relevant benchmarks. There is enough task variation.
- The demonstration that there are sparse, strong, policies for Mujoco tasks is interesting and provocative.
- Hyperparameter selection is clearly explained.

### Weaknesses
- The paper is driven purely by intuition and empirical results. There are several cases where there is not a clear understanding of why a certain approach does not work (e.g., reversing the direction of the KL divergence).
- There is no comparison of computational cost (time) of the different methods.

### Questions
1. For 5.1, how many seeds where used?
2. What is shown by the shaded area on all graphs?
3. How does hyperparameter tuning FtTPO compare to the other methods? (I see Tables 1 and 2—I'm interested in a qualitative statement).
4. How do these methods compare in terms of computational time?

### Soundness
3

### Presentation
4

### Contribution
3

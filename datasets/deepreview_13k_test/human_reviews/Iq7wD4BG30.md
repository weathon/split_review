# Learning Utilities from Demonstrations in Markov Decision Processes

- Decision: Reject
- Scores: 6, 5, 5, 6

## Abstract
Our goal is to extract useful knowledge from demonstrations of behavior in
  sequential decision-making problems. Although it is well-known that humans
  commonly engage in \emph{risk-sensitive} behaviors in the presence of
  stochasticity, most Inverse Reinforcement Learning (IRL) models assume a
  \emph{risk-neutral} agent. Beyond introducing model misspecification, these
  models do not directly capture the risk attitude of the observed agent, which
  can be crucial in many applications.
   In this paper, we propose a novel model of behavior in Markov Decision
   Processes (MDPs) that explicitly represents the agent's risk attitude through
   a \emph{utility} function.
   We then define the Utility Learning (UL) problem as the task of inferring the
   observed agent's risk attitude, encoded via a utility function, from
   demonstrations in MDPs, and we analyze the partial identifiability of the
   agent's utility.
   Furthermore, we devise two provably efficient algorithms for UL in a
   finite-data regime, and we analyze their sample complexity. We conclude with
   proof-of-concept experiments that empirically validate both our model and our
   algorithms.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces a model for learning the utility functions of agents in Markov Decision Processes (MDPs) based on observed demonstrations, with a focus on capturing agents' risk attitudes through utility functions. The authors formalize the Utility Learning (UL) problem and propose two provably efficient algorithms, CATY-UL and TRACTOR-UL, to infer utilities with finite data and theoretical guarantees on sample complexity. Proof-of-concept experiments are also conducted to validate the approach.

### Strengths
The problem of inferring agents' risk attitudes is important in sequential decision-making, where traditional Inverse Reinforcement Learning (IRL) models fall short by assuming risk-neutral agents.

### Weaknesses
1. While the paper extends utility-based approaches to MDPs, the core contributions, such as incorporating risk attitudes in utility functions and the algorithms for UL, rely heavily on prior work in IRL and risk-sensitive models. This might limit the novelty of the proposed approach. Maybe highlight the technical novelty in main text can help.
2.  The assumptions made to guarantee compatibility under finite data might not hold in more complex settings. I hope the author can provide comprehensive discussion on this issue and some intuition on possible relaxation.

### Questions
1. Could the authors clarify under which specific conditions the CATY-UL and TRACTOR-UL algorithms remain effective in highly stochastic environments, especially where reward distributions are complex?
2. How do the partial identifiability limitations impact the interpretability of learned utilities? Are there ways to mitigate this in practical applications?
3. Can the authors expand on how the proposed approach compares with recent risk-sensitive IRL methods in terms of computational efficiency and empirical performance?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The authors work on the inverse RL problem for non-risk-neutral agents. They address this problem of learning the risk attitude of the agent by learning the agent's utility function. They develop two algorithms for learning the utility function from data, and also test their approach in a toy setting.

### Strengths
This work identifies an important and interesting problem setting, as existing inverse RL does not consider that experts/agents to learn from can have non-neutral risk attitudes. It presents this motivation well and it explores natural questions regarding identifiability of utility. The proposed algorithms also appear to be novel.

### Weaknesses
* I felt the notation used in this paper might be unnecessarily complicated, which makes it more difficult to read. The paper starting from section 4 could also be more organized. 
* I did not understand why the authors require a "deterministic reward function" (line 97), does this exclude any settings where the reward has noise? This seems to directly contradict the motivating example the authors present in Example 3.1 where the reward is noisy.
* I was not convinced of the practical application of this problem framing and approach. 
    * When would one have access to agent demonstrations in multiple MDP environments, for each agent, in a practical application?
    * The authors criticize previous works for not being useful in practice, and also say that their algorithm works well in practice, but the empirical evaluations are weak. For example, it is hard to tell if the calculated utility is reasonable. 
    * The Algorithms both require knowing the Lipschitz constant of the utility function U to use (Algorithm 1 needs it to set the discretization, and Algorithm 2 needs it to update the utility function). This seems like it would be difficult in practice.

### Questions
* In Example 3.1: why not just expand your state to include past rewards?
* Line 312 ("We consider the online UL problem setting"): In what way are your algorithms focused on the online setting? They are given historical trajectories. 
* I had difficulty finding the definition of $\hat{p}^i$, which is necessary for Algorithm 1. How do these estimates need to be formed for your Theorem 5.1 to hold?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper presents a model to learn utility functions from expert demonstrations within Markov Decision Processes (MDPs) which represents the agent’s risk attitude through a utility function. For this model, the paper proposes two algorithms to infer an agent’s utility based on observed behaviors and analyzes their sample complexity results.

### Strengths
1.The paper characterizes the partial identifiability of the expert’s utility by offering counterexamples in different aspects.

2.The paper proposes algorithms with sample complexity results, and conducts experiment to test the algorithms.

### Weaknesses
1. The theorems on identifiability and compatibility of utility function seem to be more like a mathematical game. In particular, I cannot think of any practical example for which Proposition 4.6 will hold. Proposition 4.6 basically says that demonstrations in multiple MDP environments have exactly the same utility function. However, I don't think that can be true in general. Utility functions, which represent risk attitudes, will change in different environments, even for the same agent. For example, the same person might have different risk attitudes when gambling with different amount of money. 

2. The numerical experiment only shows the results of the proposed algorithms for different classes of utility functions.There is no comparison with other benchmarks.

3. The paper is heavy in math notations and can be hard to read.

### Questions
1.The papers claims that it is a new framework to consider risk-sensitive IRL. I find some related papers. Could you compare with them to state the novelty in your framework, such as:
Majumdar A, Singh S, Mandlekar A, et al. Risk-sensitive Inverse Rein-
forcement Learning via Coherent Risk Models[C]//Robotics: science and
systems. 2017, 16: 117.
Grze´skiewicz M. Uncovering Utility Functions from Observational Data
with Revealed Preference Inverse Reinforcement Learning[D]. UCL (Uni-
versity College London), 2024.

In particular, could you  clarify how your framework advances the state-of-the-art in risk-sensitive IRL beyond these existing approaches?

2. Multiple demonstrations are used to address the partial identifiability issues. Of course, an oracle to demonstrations under different
environment helps to recover the utility. But there are two issues. First, as mentioned in the Weaknesses above, why would it be reasonable to assume the same utility function in multiple demonstrations? Could you provide specific examples of real-world scenarios where the same utility function would reasonably apply across multiple environments? Second, we may not have access to multiple demonstrations in reality. Could you analyze how their method’s performance degrades as the number of available demonstrations decreases, and provide guidance on the minimum number needed for reasonable results?

3. The paper uses the gradient of the upper bound $\sum_i \overline{\mathcal{C}}$ instead of the exact subgradient of $\max_i {\overline{\mathcal{C}}}$. If you are able to know which one is  maximal,  you can  estimate this subgradient in a way similar to your method. Can you explain your rationale for using the upper bound gradient instead of the exact subgradient? If there are technical difficulties in finding the maximal, could you elaborate on what those challenges are?

4. As stated in Weaknesses, I suggest you add some other benchmarks (if they exist) to compare with in the numerical experiment. Could you identify and compare against 2-3 specific baseline methods from prior work on risk-sensitive IRL or utility learning. If relevant benchmarks do not exist, could you justify why and discuss how they could otherwise demonstrate the empirical advantages of their approach. Also, could you conduct additional experiments varying the number of demonstrations from 1 to N, and report how this affects the method’s performance?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This work proposes utility learning as a more expressive framework than IRL to infer reward functions and risk attitude from demonstrations. The authors formally define the problem setup and prove basic properties of the utility learning problem. They focus on the case where the reward function is known and only the utility function (which is a function of the cumulative reward) is unknown and must be learned from demonstrations. Due to the issue of partial identifiability, the authors consider the case where the learner gets to observe demonstrations in multiple environments. The proposed algorithms are theoretically analyzed. The paper also includes a small empirical evaluation with human participants.

### Strengths
- The paper introduces a novel model of human behavior in MDPs with a focus on modeling the risk appetite of humans using a general utility function (that depends on the cumulative reward). 
- The paper provides a clear overview over the proposed framework of learning utility functions from demonstrations. In particular, the paper proves basic, intuitive properties of the utility learning problem that are analogous to what is well-known in IRL. While technically straightforward, these theoretical results are interesting and useful (to understand the differences and similarities to IRL). 
- Theoretical guarantees for the proposed algorithms are provided. 
- The algorithms are evaluated in a small-scale experiment with human participants. Even though the experiments show that the proposed approach underperforms compared to fixing a utility function by hand instead of learning it, the results are interesting and well-explained. 
- The paper is well-written and overall clear.

### Weaknesses
- Most importantly, I'm not yet convinced that explicitly learning risk-sensitive utility functions is necessary. Playing the devil's advocate here, I'd argue that a reward function is able to capture risk appetite by extending the state space (as noted by the authors themselves in footnote 3). In said footnote, you argue that we shouldn't alter the state representation, because we couldn't transfer the reward function to new environments. This is quite unconvincing in my opinion, because, after all, we get to design the state space (usually), and any similar environments that we would like to transfer the reward function to could also have, say, a feature that refers to the money we currently have in our pocket. I think that it is quite standard to alter a state representation this way (e.g., think about maze environments where the agent has to pick up a key first in order to go through a door). 
Thus, Example 3.1 may be too simple an example to highlight why we should model some problems as utility learning instead of IRL. I do hope that this prompts the authors to make a stronger case for the necessity of utility learning. It also seems important that the utility is a function of the total return and this could be explained in more detail. 

- There are some additional minor weaknesses: 
	- Even though this work wants to provide a more expressive / realistic model of human behavior in MDPs, it assumes that the expert acts *optimally* w.r.t. its utility (equation 1). 
	- It would be great to complement the existing experiments with some evaluations on simulated data just to see how well the proposed algorithms work. It would also allow you discuss more thoroughly any scaling issues the current approaches have. I do acknowledge that this is primiarly theoretical work and the experiments are not a priority. 
	- In the experiments, you should include how the participants were recruited (e.g., lab members or others). This may somewhat limit the validity and integrity of the experiments, but this is a fairly minor point of concern to me.

### Questions
- Please comment on the weaknesses that I mentioned as you find appropriate. 
- Are there any alternatives to enlarging the state space to compute the optimal policy in RS-MDPs? 
- What follows are some minor suggestions and pointers to literature that you might have overlooked. 
	- Right before and in Section 5, you refer to the situation where you get demonstrations in multiple environments as the "setting with multiple demonstrations". This could be interpreted as observing the several trajectories in the same environment (instead of trajectories in different environments). I think it woul be better to consistently refer to this as learning from demonstrations in multiple environments. There is also related work in IRL that has referred to this as such and studied learning from multiple environments: [Identifiability and Generalizability from Multiple Experts in IRL](https://proceedings.neurips.cc/paper_files/paper/2022/file/03bdba50e3741ac5e3eaa0e55423587e-Paper-Conference.pdf), [Environment Design for IRL](https://openreview.net/forum?id=Ar0dsOMStE). 
	- Note that similar results to your Proposition 4.6 have been derived for IRL: [Identifiability in IRL](https://proceedings.neurips.cc/paper/2021/hash/671f0311e2754fcdd37f70a8550379bc-Abstract.html) shows that the reward function can become identifiable when you have demonstrations under different discount factors or transitions (Theorem 2); [Interactive IRL](https://proceedings.mlr.press/v162/buning22a/buning22a.pdf) shows that any reward function is identifiable under some transition model (Theorem 2, Remark 1) 
	- In line 243 you refer to Skalse et al. 2023 in the context of reward identifiability in IRL. I'm a bit surprised because Skalse et al. 2023 studies human model misspecification. It would be more appropriate to refer to [Identifiability in IRL](https://proceedings.neurips.cc/paper/2021/hash/671f0311e2754fcdd37f70a8550379bc-Abstract.html) and [Reward Identification in IRL](https://proceedings.mlr.press/v139/kim21c.html) who both study the identifiability issue (up to an appropriate equivalence class) in IRL.

### Soundness
3

### Presentation
3

### Contribution
3

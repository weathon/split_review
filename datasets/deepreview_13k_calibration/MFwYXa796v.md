# Fewer Questions, Better Answers: Efficient Offline Preference-based Reinforcement Learning via In-Dataset Exploration

- Decision: Reject
- Avg Score: 5.00
- Scores: 6, 3, 5, 6

## Abstract
Preference-based reinforcement learning (PbRL) can help avoid sophisticated reward designs and align better with human intentions, showing great promise in various real-world applications. However, obtaining human feedback for preferences can be expensive and time-consuming, which forms a strong barrier for PbRL.  In this work, we address the problem of low query efficiency in offline PbRL, pinpointing two primary reasons: inefficient exploration and overoptimization of learned reward functions. In response to these challenges, we propose a novel algorithm, Offline PbRL via In-Dataset Exploration (OPRIDE), designed to enhance the query efficiency of offline PbRL. OPRIDE consists of two key features: a principled exploration strategy that maximizes the informativeness of the queries and a discount scheduling mechanism aimed at mitigating overoptimization of the learned reward functions. Through empirical evaluations, we demonstrate that OPRIDE significantly outperforms prior methods, achieving strong performance with notably fewer queries. Moreover, we provide theoretical guarantees of the algorithm's efficiency. Experimental results across various locomotion, manipulation, and navigation tasks underscore the efficacy and versatility of our approach.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper proposes an active learning method for offline preference-based reinforcement learning, ie. a method to select which trajectories from a dataset to label with pairwise preferences. The proposed method consists of a value difference-based query selection criterion and a discount adaptation rule based on the variance of a reward model ensemble. The paper provides a theoretical result about this algorithm as well as positive empirical results compared to alternative methods.

### Strengths
* The method is novel, well-motivated and a nice simplification compared to prior work.
* The discount adaptation schedule is a neat idea to reduce reward model overoptimization and it seems to work well in practiec.
* The empirical evaluation is thorough, looks at multiple environments and includes most of the important ablations and experiments.
	* Overall, the empirical results seem strong over a variety of environments, making this a promising method.
* The paper is well-written and easy to read.

### Weaknesses
 * The paper does not make the key contributions clear enough
  * The introduction focuses on the offline version of the PbRL problem as being the main novelty. However, prior work very commonly considers an offline setting or can be readily adapted. So, I don't think this is the important part of the contribution here.
  * Instead, I think the novel algorithm, theoretical result and empirical performance should be highlighted more. In particular, the variance-based discount scheduling is novel (at least to me) and could be highlighter more.

* The related work section should explain the differences to prior work more
  * How is the method different from disagreement based method?
  * How is the setting different from the discussed works on semi-supervised offline RL?
  * How do the theoretical results compare to prior theoretical work?

* Comparison to prior methods is lacking a bit, especially in the method section. The objective in equation (8) seems to have strong connections to prior work. In particular, Lindner et al. consider the variance over the value difference between two trajectories. The present paper considers two reward functions that maximize the value difference between trajectories. This seems very related to estimating the variance and I think it would warrent some more discussion of the differences.

* The discussion of the theoretical results needs to be improved
  * The main paper should give an intuition for the proof technique or a proof sketch and analyze the result more. As a reader, I'd like to know which parts of the algorithm are load-bearing and which components in the final bound are due to which part of the algorithm and the analysis. Currently, I cannot learn about this without reading the full proof in the appendix.
  * Currently the paper is lacking any comparison of the theoretical 
  * IIUC the variance scheduling is not part of the theoretical variant of the algorithm. The section in the main paper does not make this clear, and I only learned this from reading the appendix. This seems like an important point to clarify and discuss the limitations of.

* The experiments are only done in quite basic RL settings. PbRL is most used in LLM settings in practice, and the paper doesn't provide any evidence for the method's advantages carrying over to that setting.

* The choice of baselines and ablations has a few gaps:
  * Why not run IDRL in Antmaze or Figure 2?
  	* Why does Table 6 in the Appendix not have IDRL results?
  * What about no variance scheduling (and no PDS)? It would be interesting to see how much worse that performs.

* The proposed method has practical downsides that are not sufficiently discussed in the paper
  * A common practical problem of this kind of method is having to train ensembles of reward models and policies which can get expensive in time and computational cost. The algorithm proposed here requires training M reward, value, and Q-models, which can be a limitation.
  * The experiments are done in a quite idealised setting. For example, IIUC the data is collected from a perturbed expert policy. In practice it would be important to understand how well the algorithm can deal with less ideal data and other condition.

### Questions
**General questions**
* The focus on a return model instead of a reward model makes the setting very similar to dueling bandit problems. How does the proposed method compare to typical approaches there and could dueling bandit algorithms be adapted to serve as baselines to compare your approach to?

* How does the theoretical bound compare to results in prior work and typical results (eg., in multi-armed bandits)? Is it likely that the bound can be improved with more careful analysis? Is it possible to say something about a lower bound of the regret?

* Will code for the experiments be released to enable others to reproduce the work?

**Questions about experiments**
* Figure 2: How many datapoints are the boxplots computed over?
* Why not run IDRL in Antmaze or Figure 2?
* Why does Table 6 in the Appendix not have IDRL results?
* Could you use dueling bandit algorithms as a baseline?

**Overall assessment**: In the current status, I think this is a borderline paper but I'm tending towards accepting it. If my questions and concerns can be addressed during the discussion phase, I'll happily increase my score.

### Soundness
3

### Presentation
4

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
The paper presents OPRIDE, a novel algorithm aimed at improving query efficiency in offline preference-based reinforcement learning (PbRL). The study tackles the challenge of reducing the costs associated with obtaining human feedback by optimizing the selection of queries and addressing issues related to overoptimizing learned reward functions. OPRIDE employs an exploration strategy that leverages in-dataset trajectory analysis and a variance-based discount scheduling to ensure balanced learning outcomes. Experimental results demonstrate its effectiveness over existing approaches across various tasks in locomotion and manipulation, with a theoretical guarantee of efficiency.

### Strengths
1. The OPRIDE algorithm integrates a principled exploration mechanism that maximizes query informativeness, effectively addressing inefficiencies in query selection for offline PbRL.
2. The study includes ablation studies that delineate the contributions of each component, alongside comparative results against multiple state-of-the-art baselines, highlighting OPRIDE's query efficiency and overall robustness.
3. Though I do not checked all details of the theoretical derivations, the theorem and the proof seem rigorous.

### Weaknesses
1. This paper seems like a simple and inconsistant combination of the two loosely related methods. The main idea of this paper is to increase query efficiency of PbRL. While in-dataset query exploration is related to this main idea, the connection between reward overoptimization and query efficiency is neither straightforward nor clearly discussed in this paper. Specifically, the paper does not adequately explain why addressing reward overoptimization, which is typically associated with policy performance, directly translates to improved query efficiency. The link between a pessimistic reward function and the need for fewer queries remains unclear. 
2. The novelty of this paper is limited. The two proposed methods, namely query exploration and uncertainty-based discount scheduling, have been extensive explored in previous researches. The former is similar with the unsupervised exploration approach in PEBBEL [1]. The latter is similar with uncertainty-based methods in traditional RL methods, such as REDQ [2] in online RL and MOPO [3] in offline RL. The paper fails to articulate the specific differences and advantages of their approach compared to these existing methods. The application of uncertainty to the discount factor, while claimed as novel, lacks a strong justification for why this specific choice is superior to applying uncertainty to the reward or value function directly.
3. In theoretical analysis, the access to online queries is assumed. So the results are poorly related with the practical performance of the proposed algorithm. The theoretical analysis does not account for the practical constraints of offline PbRL, where online queries are not readily available. The assumption of online queries undermines the relevance of the theoretical results to the actual algorithm's performance in the intended offline setting.

### Questions
1. Why overoptimization of learned reward functions contributes to the low query efficiency of pbrl? How does the discount scheduling mechanism alleviate this?
2. What is the advantage of the current type of query selection compared with PEBBLE?
3. Can you provide a more empirical elaboration on the assumption of finite Eluder dimension in the theory part? Why do we need this?
4. In theoretical analysis, it is found that querying with an offline dataset can be much more sample-efficient than pure online queries. But how do such findings related to the algorithm pipeline, including in-dataset exploration and the discount scheduling?

### Soundness
3

### Presentation
3

### Contribution
1

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper presents several contributions in the context of offline preference-based reinforcement learning:
- a query selection technique to reduce the number of queries asked to a human
- a dynamic discounting approach to account for higher uncertainty of returns
- a theoretical analysis to prove the efficiency of the proposed approach

### Strengths
The paper presents two new techniques for preference-based reinforcement learning: one for selecting queries and one for handling the uncertainty of value estimation. I believe that both could also be useful in the online reinforcement learning setting. The authors may want to comment on that point in the paper. 

The paper also provides a theoretical analysis assuming that queries can be generated online, although policy training is still performed in the offline reinforcement learning setting.

### Weaknesses
I believe that the related work should mention reinforcement learning from human feedback (RLHF) since the term "RLHF" has recently become more popular than the term "preference-based reinforcement learning".

The formalization is a bit strange, may be overly complexed, and may contain some errors, e.g.:
In the presentation of MDPs, why is it important to use the non-stationary definition?
Why do we need both Bellman operators? 
Why are the returns in (6) not discounted?
What's the impact of learning a return model vs a learning a reward model? Also, do you learn a return function instead of a reward function in the experiments? If return models are used, why not use "return network" in the whole paper and notably in Algorithm 1 to make things less confusing?
On the comment about the query selection criterion, the authors state that their proposition is scale sensitive. Isn't it also the case for the variance-based criterion?

The theoretical analysis considers a different algorithm compared to Algorithm 1. In addition, the setting for the theoretical analysis is a bit strange to me. The authors assume that online interaction is possible for querying, but not for policy learning. The authors should discuss this point in more details. Does the theoretical analysis really justifies their proposed criterion in Algorithm 1?

Minor issues:
Citations between parentheses should not be part of a sentence.
With out -> Without
The discount factor is missing in (2)
Line 146: the optimal policy -> an optimal policy (since it may not be unique)
Definition 2: please recall the definition of \alpha'-independent
Line 202: Shall R be \theta?
Line 252: a space is missing before Intuitively
Line 265: r_\theta_1 -> r_\theta_i
Line 272: imitaition -> imitation
Line 329: \hat q_1 -> \hat q_R

### Questions
Here are my main questions:
1) What's the impact of learning a return model vs a learning a reward model? Also, do you learn a return function instead of a reward function in the experiments? If return models are used, why not use "return network" in the whole paper and notably in Algorithm 1 to make things less confusing?
2) On the comment about the query selection criterion, the authors state that their proposition is scale sensitive. Isn't it also the case for the variance-based criterion?
3) Does the theoretical analysis really justifies their proposed criterion in Algorithm 1?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper investigates offline preference-based reinforcement learning with the focus on two challenges, i.e., inefficient exploration and overoptimization of reward models. Specifically, this paper proposes OPRIDE, which consists of (1) an exploration strategy to select queries, and (2) a discount scheduling mechanism to avoid overoptimization. Some theoretical insights on the exploration strategy are presented. Extensive experiments are conducted to demonstrate the effectiveness of OPRIDE under an extremely constrained query budget of 10.

### Strengths
- The techniques seems simple yet effective under an extremely constrained query budget of 10.
- OPRIDE is evaluated on MetaWorld, AntMaze, MuJoCo tasks.

### Weaknesses
 - Could you demonstrate how to infer better query efficiency of OPRIDE than random query from Theorem 4?

- The design of discount scheduling seems to be trivial. Any empirical or theoretical insights to support its motivation?

- Could you provide hyper-parameter analysis on $m$?

- Why this paper limits the query budget to 10 (although enlarged to 1~20 in Fig.2)? I think this budget is far too constrained considering the practical scenarios, especially for LLMs. Could you please provide some empirical results of more query budget like 200? Will the performance of OPRIDE deteriorate in this case?

- In terms of query efficiency discussed in Fig. 2, does PT refers to random query? Could you please provide results of OPRIDE w/ random query?

### Questions
See weakness above.

### Soundness
3

### Presentation
3

### Contribution
2

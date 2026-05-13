# From Demonstrations to Rewards:  Alignment Without Explicit Human Preferences

- Decision: Reject
- Scores: 3, 6, 5, 5

## Abstract
One of the challenges of aligning large models with human preferences lies in both the data requirements and the technical complexities of current approaches. Predominant methods, such as RLHF, involve multiple steps, each demanding distinct types of data, including demonstrations data and preference data. In RLHF, human preferences are typically modeled through a reward model, which serves as a proxy to guide policy learning during the reinforcement learning stage, ultimately producing a policy aligned with human preferences. However, in this paper, we propose a fresh perspective on learning alignment based on inverse reinforcement learning principles, where the optimal policy is still derived from reward maximization. However, instead of relying on preference data, we directly learn the reward model from demonstration data. This new formulation offers the flexibility to be applied even when only demonstration data is available, a capability that current RLHF methods lack, and it also shows that demonstration data offers more utility than what conventional wisdom suggests. Our extensive evaluation, based on public reward benchmark and HuggingFace Open LLM Leaderboard, demonstrates that our approach compares favorably to state-of-the-art methods that rely solely on demonstration data.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes to learn an LLM reward model from demonstrations data only, rather than preference data as is traditional in RLHF finetuning procedures. The authors show that such a reward estimator can be 1) learned effectively and 2) used to predict preferences well in a held out dataset when compared to baselines like SFT and SPIN.

### Strengths
The paper has the following strengths:

1. Alignment to human preferences, learned from human data, is a question that is very timely in the community. The paper does a good job of overviewing the current state of approaches used in the community, including if/when they fall short of theoretically desired behaviors. However, it would be nice if the explicitly link between the generative IRL methods proposed in Sec. 2 were explicitly tied to the author's formulation in greater detail. 
2. The proposed formulation is pretty general and therefore easy to intuitively understand - the proposed reward estimator should learn a reward function that produces a policy that best serves as a MLE over the demonstrations dataset.

### Weaknesses
I have a number of concerns, which I will summarize into major and minor:

Major Weaknesses:
1. While theoretically sound, the proposed approach is intractable in most situations due to the bi-level optimization problem of both estimating the reward as well as the policy in each update (reflecting similar challenges with deploying meta-learning techniques like MaML, which follow a similar bi-level optimization procedure). As a result, the proposed algorithm for actually optimizing this objective makes a number of assumptions which I think are not likely to hold in practice, such as limited batch sampling for updating the reward estimator and policy parameters. 
2. Evaluation is not as thorough as one may hope for a LLM paper (the authors only studied two datasets with one pretrained model checkpoint). For a contribution that is mostly algorithmic, one would expect a more diverse set of tasks (say, HHH or Coding) as well as multiple models checkpointed and their baselines evaluated. 

Minor Weaknesses:
1. There are various typos scattered throughout the paper (e.g. line 148 "wo"->"two" or line 290 "detailw"->"detail"). Please ensure the resulting revisions are spell-checked!
2. Please ensure the authors are citing/discussing meta-learning techniques and their shortcomings in related work (as it's particularly important for understanding the limits of bi-level policy and reward optimization procedures such as the one the authors are proposing).

### Questions
1. Can the authors please evaluate their proposed approach more thoroughly, or if not, explain why they only evaluated the proposed algorithm on two tasks with one set of checkpointed parameters? 

2. Akin to meta-learning procedures, where the bi-level optimization problem is often intractable in practice, the proposed approach requires a series of simplifications and sampling assumptions to ensure the optimization converges in practice. Can the authors justify which situations would these assumptions cause issues, and when they would expect this to be justifiable when actually training large language models?

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
The authors apply existing Inverse RL (IRL) methods to the LLM fine-tuning problem, yielding a method of improving LLM alignment with only demonstration data that empirically outperforms SFT and SPIN.
Thus, the old result of IRL beating behavioral cloning is replicated in the LLM setting.

Theoretical connections between their method and SPIN are made.

### Strengths
Paper nicely applies existing IRL work to the LLM fine-tuning problem, yielding new insights into both.

A theoretical connection between the new method and existing work is made.

Empirical evaluation of the method is strong, it outperforms existing baselines.

The related work and preliminaries section nicely explains previous relevant methods and results, and why one might expect the proposed method to work well a priori.

Method and its motivation is clearly explained.

Strong empirical results to support the claim this method outperforms SFT/SPIN.

### Weaknesses
An analogous equation to 6 is derived in the maximum-entropy IRL literature, so it seems reasonable to be optimising it in the downstream algorithm.
However, the derivation of equation 6 from equation 5a is not clear, and lemma 4.1 is incredibly weak---it seems $C_p$ could be extremely negative and $C_r$ very positive, making the bound rather vacuous.
Furthermore, since equation 5/5a is not later referred to in the paper after lemma 4.1, it's not clear what point is being made by formulating the problem this way, beyond the sense that something approximating MLE is probably a good thing.
It seems as though you may as well just start with equation 6, cite the relevant literature as inspiration, and move on.

Equation 6 is not actually used for the optimisation process, equation 11 is.
And like going from 5a to 6, the derivation of why optimising for equation 11 is equivalent to optimising that of 6 is not given mathematically, instead motivated by intuitive reasoning.
They are in fact **not** equivalent.
The log-sigmoid in equation 11 will decrease the loss of policy-trajectory / demonstration pairs that are already well differentiated in reward, whereas equation 6 will always be trying to push them apart with 'equal force'.
Thus, whilst they would provide the same direction of update for any given pair, they would not give the same magnitude.
When this effect is considered over a dataset of many demonstrations and policy-trajectories, the overall path taken in reward model parameter space by the optimisation procedure will differ as it moves different amounts in each of the different directions.
Whilst this is unlikely to significantly harm the method---and is probably actually a desirable property---it further breaks the connection between what's actually been done (optimising equation 11) and what has been claimed to have been done (optimising equation 5a).

Numerical results, both used in tables and graphs, do not have error bars, nor is it clear that more than a single random seed has been used.

Whilst the results in the paper support the claim that the proposed method is better than SFT/SPIN, since SFT is usually supplemented by RLHF, it would be interesting to see a comparison of the IRL method + RLHF vs SFT + RLHF, or even the IRL method vs SFT + RLHF.
It would be disappointing if the advantages of this method over SFT were rendered obsolete by downstream RLHF tuning, and exciting if this method could achieve alignment comparable to SFT + RLHF without needing any preference data itself.

### Questions
Please either clarify the claims made with relation to what the method actually implements, or provide more detail on the derivation from equation 5a to 6 to 11, and what has changed / been lost along the way.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents an approach to aligning language models with human preferences using only demonstration data, bypassing the need for explicit preference data typically required in RLHF. Drawing on Inverse Reinforcement Learning, the method iteratively learns both a reward and policy model solely from demonstration data, treating ground-truth responses as implicit preferences. This setup reduces the data complexity associated with traditional RLHF pipelines, which rely on human-labeled preference data for reward modeling.

### Strengths
- The paper is generally well-written and clear.
- The experimental setup is described in detail, providing clarity on the methodology.
- The approach achieves model alignment using only demonstration data, which could simplify data requirements compared to traditional RLHF that demands extensive preference labeling

### Weaknesses
Major:
- The proposed approach appears to be a specific case of iterative DPO. In iterative DPO, two responses are generated using the current model, and an expert LLM provides the preference judgment, creating the preference dataset needed for optimization. The proposed approach differs only in:
    * treating the ground truth in the demonstration data as the preferable response
    * using PPO rather than DPO
- To establish the contribution's originality, the authors should comprehensively describe and compare their method against iterative DPO. Specifically,
    * Evaluate the performance of iterative DPO without using any demonstration data on the same datasets.
    * Evaluate an approach that uses ground-truth data as preferred responses but leverages DPO for preference optimization, to isolate the impact of using PPO versus DPO within the proposed setup.

Minor:
- The reward accuracy shown in Figure 2(a) appears notably low. A random reward model would be expected to achieve around 50% accuracy by chance, yet the highest accuracy achieved here is only 58.8%.
- The performance drop from 79.19% to 48.04% on the "Chat" task after one SPIN iteration seems unexpected. This drop suggests potential issues with fine-tuning stability or model configuration. Could author provide some explanation about that?

### Questions
- What is the performance of iterative DPO without using any demonstration data on the two datasets?
- What is the difference in performance of using PPO versus DPO in optimization?
- Some other questions are mentioned in weakness.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper shows how one my instantiate the inverse reinforcement learning (IRL) framework in the space of large language models, in place of traditional supervised learning and RLHF methods. The authors propose that a key benefit of this method is the ability to learn from implicit information present in demonstration data, and thus does not require explicit human preference labels as is commonly required in RLHF methods. Similar to conventional IRL, the authors phrase the problem as a bi-level optimization problem, where the reward and policy networks are optimized iteratively to mimic expert behavior. The paper's main contributions are a theoretical derivation of IRL in the space of LLMs, as well as empirical results on TL;DR and UltraChat datasets.

### Strengths
* The bi-level optimization framework introduced in this paper is a creative application of IRL to settings where it is not typically applied. The proposed framework replaces the need for explicit preference-based reward models without the need for any explicit preference feedback by leveraging IRL. From another perspective, this paper also extends IRL methods to new domains like summarization (TL;DR) and dialogue generation (UltraChat).
* The paper provides sound mathematical formulations and demonstrates theoretical convergence guarantees, in addition to their empirical results. Though the idea is not particularly novel (as such sample complexity bounds have been proved in other avenues of IRL), of interest is the surrogate estimation problem in Eq 6, which the authors use to derive that the IRL for LLM alignment objective (Eq. 5) can be approximated with a finite set of expert data.
* While citing SPIN as a related work, this paper shows how SPIN's approach is a specific case of their broader IRL-based framework. This may be of particular interest for the community to develop new theoretical insights into expanding the theoretical guarantees of IRL in the space of LLMs.
* The empirical experiments include reasonable metrics and are evaluated over multiple datasets, and the authors demonstrate that their IRL method beats baseline models such as SPIN over almost all metrics.
* The experiment implementations are well described, up to actual implementations, codebases, and hyperparameters, lending itself for future reproducibility.
* The paper has a well-written introduction with solid related works. The problem is adequately motivated and contributions are stated clearly.

### Weaknesses
 * As with typical IRL, there is a dependence on high-quality demonstration data (indeed, this is part of the finite-sample approximation proof using Eq. 6). It would be nice to see more discussion between the costs of acquiring high-quality demonstration data needed for the proposed IRL approach to work, versus the cost of obtaining human preference labels for RLHF methods to work. 
* Related to the point above, It would also be nice to see how the proposed method does with varying amounts of expert demonstration data (in comparison to, say, a method like IQLearn). 
* While this paper builds atop SPIN and IRL approaches, there feels to be a lack of novel insights being introduced in the algorithmic design. 
* It is well known that IRL approaches are typically rather hard to scale, due to needing to solve the hard exploration problem to optimize the reward in the inner loop. It is a bit unclear how the proposed method scales in comparison to prior work. It would have been nice to see some discussion about training/memory costs of running something like PPO in the inner loop of this bi-level optimization.
* While I understand there are slightly different assumptions being made (implicit vs explicit preference labels), it would be nice to see how current RLHF models do in comparison to the metrics produced by SPIN and the proposed method.

### Questions
1. Were there experiments investigating how the proposed method handles varying qualities of demonstration data? In typical imitation learning terms, how does the proposed method function under noisy or suboptimal data?
2. How do the synthetic preference data that your method generate compare with actual human preferences?
3. What is the computational cost of your bi-level optimization approach compared to standard RLHF pipelines? Have you profiled the memory and runtime performance of your method? For example, how long does one iteration of SPIN vs one iteration of IRL take?
4. Assumption 4.1 (Line 253) assumes bounded reward scores. Can you explain the intuitive meaning of this assumption and how it holds in practice? Does this assumption limit the applicability of your method to only certain types of reward functions?

### Soundness
3

### Presentation
2

### Contribution
3

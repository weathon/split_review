# A bi-objective perspective on controllable language models: reward dropout improves off-policy control performance

- Decision: Reject
- Scores: 5, 5, 8

## Abstract
We study the theoretical aspects of CLMs (Controllable Language Models) from a bi-objective optimization perspective. Specifically, we consider the CLMs as an off-policy RL problem that requires simultaneously maximizing the reward and likelihood objectives. Our main contribution consists of three parts. First, we establish the theoretical foundations of CLM by presenting reward upper bound and Pareto improvement/optimality conditions. Second, we analyze conditions that improve and violate Pareto optimality itself, respectively. Finally, we propose Reward Dropout, a simple yet powerful method to guarantee policy improvement based on a Pareto improvement condition. Our theoretical outcomes are supported by not only deductive proofs but also empirical results. The performance of Reward Dropout was evaluated on five CLM benchmark datasets, and it turns out that the Reward Dropout significantly improves the performance of CLMs.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
GOAL: Study Controlled Language Generation Models (CLM) through the lens of RL

OVERALL/The Main Point:

The main point of this work is to point out that CLM is basically a biobjective RL problem. They then show that this insight helps by using an RL trick in the CLM context. The trick does improve results (compared to treating it as a simple RL method). It is unclear whether reframing as an RL problem helps compared to these two baselines:

 1) other methods finetune the LLM per control code but do not frame the problem in an RL manner.

 2) The same RL trick used in this paper used to update the policy, vs only using the trick at controlled decoding time (and no finetuning involved). This baseline is needed since the RL trick used in this paper actually also exists in in other controlled decoding papers: https://aclanthology.org/2022.naacl-main.57.pdf)




OTHER CONTRIBUTIONS:
1. Frame 3 variants on CLM problems as off policy RL that has to max both likelihood of behavior policy and reward score of reward model. This means we can minimize the KL divergence of the target policy and the behavior policy + exponentiated reward. (I’m not clear to me why the reward is exponentiated, other than for math convenience in Eqs 5 and 6)
2. Frame off policy RL as a bi-objective function with a necessary Pareto frontier. 
    - Discuss tT=heoretical outcomes of 2 and empirical justification of some properties in a simple 10-turn position game.
3. Reward Dropout is an RL trick that keeps only the top %ile of rewards to guarantee improvement based on Pareto improvement condition. They show that using this RL trick helps controlled generation as motivation for why an RL framing of the CLM problem is useful.

### Strengths
1. The proofs and experimental results in Sections 4 and 5 are well written and easy to read within each section. The connection between them is a weakness (see below)

2. Reward dropout is a very simple and effective strategy used to enhance decode-time fine-tuning.  

3. CLMs are a common biobjective function, and making the connection to RL is neat.

### Weaknesses
1. The experimental results in Section 5 does not provide surprising or insightful results. Even the translation to LLM concepts doesn’t provide insight. The takeaways are that we do better when the two rewards have more overlap (so have a wide span of vocabulary and use an LLM over a smaller model) and when the two rewards have similar maxes (so line up your two rewards by training on data that fulfills both objectives). The visualization is cute, but the takeaways are already standard knowledge (bigger models do better, OOD tasks are harder). If the intent is to empirically test your proofs, then can you write this section in terms of when a policy  becomes a uniform policy (4.2), or show the pareto frontier across policies with the same reward etc. etc. The connection between 4 and 5 is weak.

2. [PRESENTATION]  I’d put a minimal version of Appendix D.2 in the main text -- enough to understand the set-up without reading the full Appendix.

3. Also this set-up described in Appendix D.2 doesn’t really allow you to modify the first part of β(τ ), and I feel that to keep with the spirit of this being a bi-objective RL problem, it should be possible to get different rewards from that first part of β(τ ).

4. [PRESENTATION]  The decoding method is quite expensive, as it involves updating the params of the entire LLM for each target objective (finetuning to be polite is one entire fine-tuning, finetuning to be a negative sentiment is one entire fine-tuning). A lot of CLM methods have the same model be able to output language under different control codes. Can you call this out more explicitly in the limitations section (because it doesn't come across until you read the Appendix)

5. [SOUNDNESS] For the NLP experiment, I’d like to see a non RL-motivated baseline method. The random dropout isn’t really a baseline. It’s nice that this trick from RL translates nicely here, but does the RL framing allow you do better than other CLM methods trained on those datasets? (ex: Perhaps FUDGE as another classifier guided CLM method, or better yet, Diffusion LM adapted to this task perhaps.).

6. [SOUNDNESS/NOVELTY] The last section (the NLP experiment) is strikingly similar to: https://aclanthology.org/2022.naacl-main.57.pdf I'm actually not sure there are any differences except that they don't then re-train the policy (please highlight the other differences for me if they exist). Do you do better than this paper (them only using the method as a controlled decoding solution, and your version fine-tuning based on the controlled decodes)? (A positive answer to this question would also help motivate your RL framing where the policy is typically updated).

7. [NOVELTY] Framing Controlled Decoding as an RL problems has been implicitly done before: https://arxiv.org/abs/1909.09492

### Questions
1. In Eq 4, why is the reward function exponentiated? Why does this make sense in context of the problem (and not only because it leads to nice cancellations in successive equations). 

2. How is R computed for each sentence?

3. Are there other RL tricks you believe would be useful? Adding those here (and beating CLM baselines AND comparing the effect of updating policy with the trick vs only controlled decoding with the trick) would better help make the case for the utility of the RL-perspective empirically. As is, I'm not convinced this framing is marginally more empirically useful.

4. My own main weakness as a reviewer is that I may be undervaluing the theoretical contributions here. Other works have already referred to controlled decoding as an RL problem, but they do not have your proofs. Either discuss why the theory alone is a solid contribution  (Why is treating CLM as an biobjective RL problem -- as past papers do --  is an unsafe assumption without these proofs established) OR make the case that the RL perspective is useful empirically (See Question 3)

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper provides some theoretical aspects of the RLMs by casting it as an offline RL problem. With the offline RL objective, the paper provides some properties of the optimal policies or pareto optimal policies. Based on these observations, the paper provides the reward dropout method to improve policies and tested on several benchmarks.

### Strengths
The reward dropout methods seem simple and widely applicable. The experiment results indicate the method is actually improving performance in practice. However, I do not conduct research on LLM at all so I am unable to judge the significance of the results from the experiment.

### Weaknesses
The technical section of the paper is poorly written and there are many questionable claims. For example,

1. The CML and RLM are still different problems. The paper should not claim that they analysis CLM by RLM because they are "intrinsically analogous". The core issue is that CLM is about generating text conditioned on some context, while RLM focuses on optimizing a reward function, which are not the same. The paper needs to clarify how these two problems are related beyond a superficial level.

2. Footnote 1 is confusing: I do not understand why the paper mentions model-based RL, and I do not understand what "the dynamics is usually assumed" means. The footnote introduces unnecessary complexity and does not clarify the relationship between model-based and model-free RL in the context of the paper.

3. Eq. 3 is a constrained optimization problem, and Eq. 4 is a KL divergence, I do not see why the paper claims that "Eq. 3 can be expressed as Eq. 4". Equation 3 describes a maximization problem with respect to model parameters, while Equation 4 defines a KL divergence between two distributions. The paper needs to provide a clear derivation or justification for this equivalence, which is not obvious.

4. $\pi$ is never defined. Also, $\Pi$ function class is never defined. The paper lacks a clear definition of the policy $\pi$ and the policy space $\Pi$, which are fundamental to the theoretical analysis. Without these definitions, the subsequent analysis is difficult to follow and verify.

5. In Eq. 6, why would taking $\lambda=1$ results in the optimal policy? It seems arbitrary to me unless I missed some important derivation proving that $\lambda=1$ is the optimal Lagrange multiplier. The paper does not provide a rigorous justification for setting $\lambda=1$, and it is not clear why this specific value leads to the optimal policy. The choice appears to be made without sufficient mathematical backing.

Also, the theory results in section 4 seem rather trivial, instead, the paper may be improved by showing why these observations are significant.

### Questions
See above.

### Soundness
3 good

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work studies a trade-off between reward and likelihood, which is an important but unexplored problem in the pertaining or finetuning of LMs. And the authors proposed a simple solution to this problem, dubbed Reward Dropout.

### Strengths
The problem studied in this work is interesting and important, and the authors provide a thorough theoretical analysis from the perspective of Pareto optimization/bi-objective optimization.

### Weaknesses
This work only focuses on a single "balanced" Pareto solution to the proposed bi-objective optimization, which weakens the motivation for using bi-objective formulation. According to the experimental results such as Fig. 3, if you only consider the reward metric and would like to relatively neglect the likelihood objective, why not consider the trade-off problem from the perspective of constrained optimization with the likelihood objective as the constraint?

One possible solution is that the authors can provide evidence reflecting some other trade-off solutions on the Pareto front are also important (e.g., plotting an approximate Pareto front and showing different behaviors of Pareto solutions).

Moreover, the experiment only uses a relatively small language model (i.e., GPT-2). LLMs can weaken the influence of the reward-likelihood trade-off due to their larger model capacity.

### Questions
Some comments:

1. for eq. (5), if the behavior policy has already maximized the reward objective, will the bi-objective optimization reduce to a single objective optimization?

2. for fig. 2, please provide additional results under a non-normal distribution behavior policy.

3. What is the core idea of reward dropout? I think the core idea is to relax the distribution of rewards in order to achieve an easier Pareto improvement. From this perspective, I wonder why the final performance is improved by the quantile dropout that sharpens the distribution.

---post-rebuttal comment---

After reading the authors' responses and their revised version, I decided to raise my score.

### Soundness
2 fair

### Presentation
3 good

### Contribution
4 excellent

# Cream: Consistency Regularized Self-Rewarding Language Models

- Decision: Accept
- Scores: 8, 6, 6, 6

## Abstract
\vspace{-0.5em}
Recent self-rewarding large language models (LLM) have successfully applied LLM-as-a-Judge to iteratively improve the alignment performance without the need of human annotations for preference data. These methods commonly utilize the same LLM to act as both the policy model (which generates responses) and the reward model (which scores and ranks those responses). The ranked responses are then used as preference pairs to train the LLM via direct alignment technologies (e.g. DPO). However, it is noteworthy that throughout this process, there is no guarantee of accuracy in the rewarding and ranking, which is critical for ensuring accurate rewards and high-quality preference data. Empirical results from relatively small LLMs (e.g., 7B parameters) also indicate that improvements from self-rewarding may diminish after several iterations in certain situations, which we hypothesize is due to accumulated bias in the reward system. This bias can lead to unreliable preference data for training the LLM. To address this issue, we first formulate and analyze the generalized iterative preference fine-tuning framework for self-rewarding language model. We then introduce the regularization to this generalized framework to mitigate the overconfident preference labeling in the self-rewarding process. Based on this theoretical insight, we propose a \textbf{C}onsistency \textbf{R}egularized s\textbf{E}lf-rewarding l\textbf{A}nguage \textbf{M}odel (\ours) that leverages the rewarding consistency across different iterations to regularize the self-rewarding training, helping the model to learn from more reliable preference data. With this explicit regularization, our empirical results demonstrate the superiority of \ours\ in improving both reward consistency and alignment performance.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
The authors propose the Consistency Regularized self-rewarding Language Model (CREAM), which incorporates regularization to improve reward consistency in order to alleviate the risks of inaccurate rewards and biased training data over time. The basic idea of the method si to add a regularization of optimizing towards a balanced binary distribution, where the weight of the regularization is determined by the  self reward ranking correlation between different optimization steps. The author provides some theoretical proof and empirical results show that CREAM enhances both alignment performance and the reliability of preference data.

### Strengths
- The proposed method is interesting and there are theoretical and empirical proofs of effectiveness.
- The method uses the ranking correlation to evaluate the consistency or uncertainty in self rewarding.

### Weaknesses
- I think first the author should add some baselines such as the original form of the method which just uses the KL constraint toward the Bernoulli distribution. It would be good to break down where the improvement comes from and how much the ranking correlation helps the methods.
 - Then another very important experiment I think is that previous self-rewarding methods can not maintain the improvement beyond 3 or 4 iterations, how will your method help this? Will there still be significant improvement for the 5th or 6th iteration?
 - Another thing I am thinking is that given the final form, in the training you use a normal DPO and a reversed DPO, and weight the loss functions. Then this is basically the same as just weight the normal DPO with a weight maybe ranging from -1<->1. Why don't the author try this for example shifting the C weight and only keeping DPO loss? This would be much more efficient in implementation I assume?

### Questions
N/A

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper attempts to propose a more consistent reward learning strategy within self-rewarding LLM settings where the same model acts as the policy generating sample responses as well as a reward model that ranks those responses. Their framework called  Consistency Regularized sElf-Rewarding lAnguage Models (CREAM) leverage reward consistency signals to make their models learn from more reliable preference
data. Their experiments suggests that CREAM-trained models outperform SRLMs as well as external reward models especially with smaller models such as LLaMa2 and 3.

### Strengths
1. The methodology section is well described with mathematical analyses for readers.
2. Formulating the challenges and corresponding analysis is organized and explained well.
3. Various experiments are conducted to show the performance of CREAM with models like LLama2 and 3, including comparison with reasonable baselines like SRLMs and external reward models.

### Weaknesses
1. In the line #244, there is a lack of information about the reason for using reversed
preference order.
2. Once again, in the line #328, The reasons for preparing a reverse DPO dataset and swapping the
best response with the worst response are somewhat unclear.

### Questions
Questions:
1. In the line #445 - 447, It describes as “SRLM with prompt rewarding is not effective”, but
the performances are increasing on the GSM8K dataset in the Table 3. Can you explain
why this could be the case?
2. In Table 4, the performance of CREAM dis not improve when we compared to Llama2
M1 on the Arc-E, Arc-C, OBQA, and SIQA datasets. What are your thoughts on why it
didn’t improve, even though CREAM showed better performance compared to Llama3
M1?

3. Regarding the reversal of the DPO dataset, if \( C = 0 \) indicates an inverse correlation between $\theta_{t-1}$ and $\theta_{t}$, isn’t learning from this strategy placing too much confidence in the assumption that reverse preferences are meaningful? This concern arises particularly when the initial inconsistency between $\theta_{t-1}$ and $\theta_{t}$ might be due to stochasticity rather than an actual flaw in the self-rewarding model being trained. As such, did the authors conduct experiments to analyze how the trend of inconsistency evolves between consecutive iterations, especially at later stages of training (e.g., around $t = 5 $ or  $t = 6$), to see if this inconsistency stabilizes later in training?



presentation/typos:

Abstract: “there is no guarantee on the accurate of the rewarding and ranking” —> accuracy 
Line 082: “we first formulates a generalized iterative preference” —> formulate
Line 139: “The objective is to iteratively minimizing the following loss” —> minimize
Line 522: “emphasizing reliable preference data and avoiding overconfident
in preference labeling.” —> overconfidence

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a modified DPO objective that considers multiple reward judgements, and penalizes disagreement across multiple reward models. The new objective is studied in the context of self-rewarding LMs, an iterative process based on DPO.

(Note: score increased from 3 to 6 based on the discussion)

### Strengths
* The idea of considering diversity across an ensemble of RMs to prevent reward hacking is sound and well motivated.
* Consideration of such a signal is supported by the experimental results.

### Weaknesses
* The biggest weakness of this paper is that it is not contextualized well with prior work on reward hacking and using ensembles to mitigate this. Given that proposing variants of DPO and related algorithms is increasingly crowded, this is especially important. Beyond discussing and comparing with this prior work, it is also important to understand how pessimism-based approaches compare, both theoretically and empirically, with the proposed methods based on agreement metrics. Similarly to this paper, there is a growing body of work that aims to mitigate reward hacking through reward model ensembles (e.g. https://arxiv.org/abs/2310.02743, https://arxiv.org/abs/2312.09244, etc.). These papers provide analysis showing various correlation metrics during RLHF. “Disagreement” between reward models can be penalized by considering pessimistic aggregations of rewards, e.g. by taking the min or some percentile (<50) over the set of RM rewards. Such concepts have also previously been integrated into DPO (e.g. https://arxiv.org/abs/2405.19316). It is not clear the relation between the proposed approach of weighting by RM agreement to this prior work which aggregates RM scores pessimistically, or whether there is any advantage. 
* The motivation for introducing the framework in 3.1 was not clear to me. How is it different from prior work, e.g. Yuan et al., 2024? Why is it necessary to introduce this new framework to evaluate the key contribution of the paper, i.e. the impact of the consistency reward? This made the experiments more difficult to analyze, because it was unclear whether the only change between "SRLM" and "CREAM" was the consistency reward or whether other factors contributed to the difference.
* The overly formal exposition of the proposed method makes the intuition difficult to follow. For example, the definition of the regularization loss, introduced in equation 3.5, does not include any intuition for why this term was chosen.

### Questions
See weaknesses for questions.

There are many grammar mistakes that would be good to resolve, e.g.:
* Abstract - “the accurate of the” -> “the accuracy of the”
* Intro - “we formulates” -> “we formulate”
* Many places - “the rewarding consistency” -> “the consistency reward”?
* Section 3.2 - “prevents the model… from overconfident”

Other nits:
* Notation - You define `[k]` as a set, but the next sentence says “Sets are denoted by calligraphic uppercase letters”. Maybe say “Other sets are…” to avoid a contradiction?
* Equation 3.4 - My understanding is that typically SFT is performed first, and then DPO, rather than optimizing both objectives jointly, as this equation implies.
* The RewardBench citation is missing a year.

### Soundness
2

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
This paper proposes a form of regularization for self-rewarding language models, which involves creating a loss that is a weighted combination of the LM's implied preferences and the reverse preferences. The weighting is determined by the rank correlation between implied rewards across adjacent training steps: if these rewards are perfectly rank-correlated then the reverse preferences are not included; to the extent that they are uncorrelated, the self reward model is deemed less trustworthy and so the reverse preferences are given more weight. The specific form of the regularizer is justified by theoretical connections to entropic regularization. The method yields improvements over the unregularized SRLM approach of Yuan et al (2024) on benchmark datasets and in head-to-head win rate (e.g., 34/21 win-loss ratio). Evaluations focus at the 7B scale.

### Strengths
- While the proposed approach seems somewhat heuristic (e.g., training on both (y, y') and (y', y)), the steps of the algorithm are justified by theoretical support.
- The "oracle" component of the evaluation helps to clarify the headroom for better reward modeling on these tasks.
- The ablations help clarify the role of the specific form of rank correlation and "prompt rewarding" vs the implicit DPO RM

### Weaknesses
It's not clear to me why one would want to use self-rewarding LMs at the 7B scale, as it would not be too difficult to get preference annotations from a larger model and train on them instead.

The algorithm appears to treat consistency as a property of the model \theta_t, but I wonder whether it would be better to treat it as a property of the *data*. That is, for any model, there will be some examples for which preference can be assessed confidently, and others for which it cannot. It would be ideal to use the full DPO loss for the first type of examples, and regularize strongly on the second type. Instead, the proposed approach seems to set the regularization parameter based on some property of the optimization path: as long as the LM has not changed its rankings from time t-1, it will use the standard DPO objective. (Thanks for the additional experiments on this.)

I would like to see more analysis of the sum of DPO losses. In particular, what is the effect to the policy of applying the update in step 14 of the algorithm when C=1/2? My guess is that the probability for both y+ and y- decreases, but it would be great to have some formal analysis because this situation could be relevant, e.g., at the beginning of training.

### Questions
The method seems to be applied to LMs that have already been post-trained (LLAMA 2 & 3), which is perhaps why the impact is less than in Yuan et al. Would it be possible to apply the method to a model immediately after pretraining or instruction tuning?

### Soundness
3

### Presentation
3

### Contribution
3

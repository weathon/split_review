# Reflect-then-Plan: Offline Model-Based Planning through a Doubly Bayesian Lens

- Decision: Reject
- Avg Score: 4.60
- Scores: 5, 5, 3, 5, 5

## Abstract
Offline reinforcement learning (RL) is essential when online exploration is costly or unsafe, but it often struggles with high epistemic uncertainty due to limited data. Existing methods learn fixed conservative policies, which limit adaptivity and generalization. To tackle these challenges, we propose __Reflect-then-Plan (RefPlan)__, a novel _doubly Bayesian_ approach for offline model-based (MB) planning that enhances offline-learned policies for improved adaptivity and generalization. RefPlan integrates uncertainty modeling and MB planning in a unified probabilistic framework, recasting planning as Bayesian posterior estimation. During deployment, it updates a belief distribution over environment dynamics based on real-time observations. By incorporating this uncertainty into MB planning via marginalization, RefPlan derives plans that account for unknowns beyond the agent's limited knowledge. Empirical results on standard benchmarks show that RefPlan significantly improves the performance of conservative offline RL policies. In particular, RefPlan maintains robust performance under high epistemic uncertainty and limited data, while demonstrating resilience to changing environment dynamics, improving the flexibility, generalizability, and robustness of offline-learned policies.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
When data coverage for offline RL algorithms is incompete, this can lead to high epistemic uncertainty. The authors aim to improve performance in such settings at deployment time by incorporating a Bayesian-based approach. Specifically, their approach, called Ref-Plan, integrates model-based planning and uncertainty modeling. An empirical evaluation on standard offline RL benchmark domains considers the  performance of RefPlan in environments where dynamics change or where data availability is limited.

### Strengths
* The problem motivating this work is important,  and to the best of my knowledge this algorithm seems like a novel contribution
*  Many parts of the paper that are nicely written, including the motivations outline in section 1, and discussion in section 3. 
* The math discussed in the work, e.g., 4.1 and 4.2 did not seem to have errors. 
* The number / types of environments seems adequate to provide rankings between algorithms (in aggregation)

### Weaknesses
 *Background / Improving Clarity:* The paper could be improved with more clarity on a lot of the background. While many algorithms / ideas were mentioned then cited, having a fuller description of these works in the paper (main body or appendix) would be beneficial, especially when these are used in the main algorithm or often referenced. E.g., BAMDP, control-as-inference framework, quantifying epistemic uncertainty. Specifically, the paper should elaborate on how these concepts are used within the Ref-Plan framework. For example, how does the control-as-inference framework specifically inform the planning process? How is the Bayesian approach to uncertainty quantification implemented and what specific assumptions are made? A more detailed explanation of how these components are integrated would significantly improve the paper's clarity.

*Experiments:*
RQ1. Further explanation connecting the environment settings chosen and resulting epistemic uncertainty would improve the flow. The paper should provide a more detailed explanation of why the chosen initialization strategy leads to high epistemic uncertainty. What specific aspects of the environment or dataset cause this uncertainty? A more in-depth analysis of the relationship between the initialization distribution and the training data would be beneficial. 
RQ3 & RQ4. Q3 seems to be comparing performance under epistemic uncertainty but when that uncertainty is produced through limited data as opposed to RQ1? Improved clarity between these RQs would be beneficial. RQ1 seems to be a superset of RQ3&4. The distinction between the sources of uncertainty in RQ1, RQ3, and RQ4 is not sufficiently clear. The paper should explicitly state what specific aspects of the experimental setup in each RQ lead to the claimed type of epistemic uncertainty. For example, how does subsampling the dataset in RQ3 specifically lead to epistemic uncertainty about the environment's dynamics, and how is this different from the uncertainty caused by OOD initialization in RQ1? Similarly, how do the changes in environment dynamics in RQ4 differ from the uncertainty in RQ1 and RQ3, and what specific mechanisms cause this difference?

Small Confusions / Errors
- the last comment in alg2 refers to line 5 in alg1, but there are no line numbers,  line 5 specifically is the beginning of a loop
- what are the error bars used in the experiments?
- bold vs underline meaning in Table 1?
- H-step is mentioned without being defined.

### Questions
RQ3 and RQ4 seem to be a superset of RQ1. Could the authors clarify this? Instead, is it the case that these RQs each consider different causes of uncertainty?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This work addresses the problem offline reinforcement learning and proposes a Bayesian-inspired model-based solution based on VariBad and control-as-inference.

Varibad is a Bayesian solution for meta-learning: given data on a set of tasks, how to quickly identify the task during testing (and do well in it).
This is done through variational inference, where an encoder is trained to capture distribution over the task (in the form of a latent variable) given a trajectory (paired with a decoder that is trained to reproduce the trajectories).
Control-as-inference models decision making as a probabilistic problem, "probability of policy given optimality", using the expected return as a likelihood measurement.

The performance is compared to typical offline model-free and model-based methods on D4RL benchmark, where they show performance comparable to "LOOP".

### Strengths
S1: The work is tackling a relevant (offline RL) problem that should be of interest to the a non-trivial section of the ICRL community.
S2: The English is easy to understand and the math is (as far as can tell) sound.

S3: I believe the proposed solution - the combination of control-as-inference and Bayesian inference over dynamics - is non-trivial and novel.
    In particular, it attempts to leverage uncertainty in (offline model-free) policy and (offline model-based) dynamics in a computationally feasible way.
    Though I am not familiar with the offline RL community/literature, the question on how to combine model-free and model-based is a long and important one in RL.
    The way it is proposed here "makes sense": a policy pre-trained should be considered a prior, and fine-tuning this online when new data comes in a Bayesian fashion is (only in hindsight) an obvious one.

### Weaknesses
W1: One room of improvement, especially for someone with lack of background, is the accessibility of the background.
    One, certain (seemingly?) important concepts were not clearly defined (e.g. "epistemic POMDPs", "BA-MDPs".)
    Second, some concepts were clearly background (e.g. "control-as-inference"), but were not introduced.
    As far as I know, they were explained as part of the method description, which  made it excessively hard to infer what was novel (and should be credited as well as scrutinized) and what was known in the literature.

W2: A major concern, in my opinion, is the lack of experiments for online learning.
    Conceptually, planning is useful if (1) it saves us computation time (plan for current states, not whole state space) or (2) we gain more information over time (improve learned model and thus our planning).
    As far as I understand, the experiments here are the initial performance, which begs the question (Q2) whether this performance could have been trained/reached offline instead.

W3: VariBad tackles meta-learning: it is assumed (and exploited) that the training data set is generated from different tasks.
    In particular, it is optimized to capture the task characteristics from different tasks, capture this in latent variables, and infer them online.
    As far as I understand, the experiments do not include this setting.
    In particular, it is not clear whether the "Bayesian" argument holds here: Varibad's encoder might just collapse - as all trajectories come from the same environment - and there should be no (latent) information to capture.
    As a result, while it is supposed to be "double Bayesian", the proposed method does not seem to have the Bayesian trait of doing optimal actions with respect to the uncertainty.

### Questions
Q1: Is 4.and 4.2 background (control as inference & varibad), or are there particular extensions / modifications hidden in there?

Q2: Given concerns of W3 (offline RL vs meta-learning), , rather little information is learn until "much data" is gathered.
    As a result, it feels as if any additional performance from online planning _could have been done offline_: refine policy by doing control-as-inference offline on Varibad's model.
    Do you have any idea how well that could or would perform?

Q3: Did you consider comparing with VariBad? How about and ablation study where you replace VariBad with other model-based approach (that does not do meta-learning)?

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
4

### Summary
To effectively incorporate the uncertainty into planning, this paper propose Reflect-then-Plan (RefPlan), a doubly Bayesian approach for offline MB planning to enhances offline-learned policies for improved adaptivity and generalization. The performance is validated on three standard benchmarks (Hopper, HalfCheetah, and Walker2d). However, it is not sure that the agent has learned a near Bayes-optimal policy. It would be better to add theoretical support and/or to include a navigation task, along with visualizations of the agent's behavior.

### Strengths
The Reflect-then-Plan (RefPlan) framework combines Bayesian modeling of epistemic uncertainty with model-based planning in a unified probabilistic approach.

### Weaknesses
1. The paper uses VariBAD's VAE structure to learn environment dynamics but lacks strong evidence that the agent has learned a near Bayes-optimal policy. It is recommended to add theoretical support or to include a navigation task, along with visualizations of the agent's behavior.

2. The paper lacks innovation; the approach of offline model-based planning as probabilistic inference is common (see [1]). Furthermore, the proposed algorithm is merely a minor modification of VariBAD, lacking novelty. In addition, related work in the field of offline meta-RL has shown adaptation and generalization across multiple tasks, which is more valuable than the single-task generalization problem addressed here (see [2][3]).

3. The paper evaluates the algorithm on only three tasks, which is insufficiently persuasive, and the experimental results show only marginal improvements over LOOP.

### Questions
See the previous section.

### Soundness
2

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
This paper proposes a principled approach based on Bayesian inference for offline MBRL. The proposed formulation uses Bayes-adaptive MDP approach, in which the uncertainty over model estimation is captured through belief representation in POMDP while planning under uncertainty for optimal actions is proposed to plan for actions that account for unknowns beyond the agent’s limited knowledge. In overall, the doubly Bayesian views are applied to both model learning and policy optimization. The writing is easy to follow. The final results are encouraging.

### Strengths
Pros:

- Clear and principled proposal for offline MBRL: The model distribution is learnt via variational inference, while the policy planning step takes into account this model uncertainty to plan for optimal actions to act under epistemic uncertainty.

- The proposed formulation is sound.

- Clear writing: It's easy to follow and understand both the technical part, e.g. maths behind, and the main proposal, e.g. Fig. 2 has a clear depiction of the proposal.

### Weaknesses
Cons:

- It's questionable that RefPlan only fine-tunes a baseline policy. Either i) why the learnt model can be used to optimize a new policy, ii) it's a bit unfair in terms of extra computation needed in comparisons to the baselines, including both model-free and model-base. Especially the latter, the model learnt using model-based methods in the baseline will be discarded or unnecessarily unused in the fine-tuning stage of RefPlan. So it is expected to have a more light-weight fine-tuning approach for test-time planning.

- Performance is mixed: RefPlan performs well on some tasks, which show clear improvements. However at some tasks e.g. Hopper the improvements are not obvious even in comparison to model-free methods. E.g Fig. 3 CQL can still perform well in Hopper though on OOD setting, without explicitly modeling epistemic uncertainty, and without doing extra training and planning at test-time. In addition, the gap to existing SOTA, LOOP which also did some extra computation, is not significant.


- Fig. 1: Misleading as could be understood that a GM is input to the encoder. There are observed nodes used as data, however the connection like graph  is also provided?

- Conceptually, how it's compared to the deterministic path and stochastic path in PlaNet and Dreamer model? The plan is also solved using sampling, which is however RefPlan can have a higher variance due to outer sampling w.r.t random variable "model m".

- Some ablations are needed to understand the effect of the whole sampling step, e.g. trade-off between variance and performance and needed computation.

- "In the offline setting, we aim to enhance the prior policy πp via MB planning at test time by inferring the posterior over": Policy and model are decoupled. Can it be revised to compute optimal policies directly from the model-based policy optimization and at least there is a comparison to this "baseline"?

- Experiment in Section 5.1: The results are encouraging to say RefPlan is acting in the face of epistemic uncertainty, however it's hard to understand the effect of which component, e.g. visualization of uncertain region, or understand how policy is selected in such situation.

### Questions
See the above two main questions in Cons.

Other major comments:

- Fig. 1: Misleading as could be understood that a GM is input to the encoder. There are observed nodes used as data, however the connection like graph  is also provided?

- Conceptually, how it's compared to the deterministic path and stochastic path in PlaNet and Dreamer model? The plan is also solved using sampling, which is however RefPlan can have a higher variance due to outer sampling w.r.t random variable "model m". 

- Some ablations are needed to understand the effect of the whole sampling step, e.g. trade-off between variance and performance and needed computation.

- "In the offline setting, we aim to enhance the prior policy πp via MB planning at test time by inferring the posterior over": Policy and model are decoupled. Can it be revised to compute optimal policies directly from the model-based policy optimization and at least there is a comparison to this "baseline"?

- Experiment in Section 5.1: The results are encouraging to say RefPlan is acting in the face of epistemic uncertainty, however it's hard to understand the effect of which component, e.g. visualization of uncertain region, or understand how policy is selected in such situation.


Minor comments:

- It would be better in Related work to discuss and include this work: "Arthur Guez, David Silver, Peter Dayan: Efficient Bayes-Adaptive Reinforcement Learning using Sample-Based Search. NIPS 2012"

-

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper incorporates Bayesian uncertainty estimation into offline model-based planning to improve the adaptivity and generalization ability of offline-trained policies. Empirical results are shown to demonstrate the claimed advantages of the proposed method.

### Strengths
1. The incorporation of uncertainty estimation into the offline model-based planning framework is well done, mathematically. As far as I know, this is the first work to do so under the variational inference framework.
2. Accounting for changes during deployment in the real environment is important in practice. In this sense, this work is well motivated.
3. The empirical performance is promising and well verifies the adaptivity of the proposed method.

### Weaknesses
1. APE-V (Ghosh et al., 2022) seems like a valid baseline for adaptive offline algorithms, however the paper does not compare with it, making the evaluation potentially incomplete and less convincing.
2. It seems like the hyperparameters need to be carefully tuned for each task, which might limit the usability of the proposed method.



### Questions
1. Section 5.1: How exactly do you test the prior policy in states sampled from the R dataset?
2. Model-based methods are usually computationally expensive in training and planning is costly when executing actions, compared to sampling from a policy network. It seems like RefPlan needs to use an additional VAE network, which may further increase the computation burden. So I wonder how is the computational efficiency of the proposed RefPlan method, in training and in executing, respectively?
3. Figure 4: I wonder what the performance will be like when you use the full dataset for LOOP and RefPlan. Maybe continuing the lines in the plots to 1M would help readers see how much and how rapidly the performance degrades when reducing the dataset size.

### Soundness
3

### Presentation
3

### Contribution
2

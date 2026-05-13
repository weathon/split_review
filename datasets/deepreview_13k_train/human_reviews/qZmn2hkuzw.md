# Bidirectional Decoding: Improving Action Chunking via Closed-Loop Resampling

- Decision: Accept
- Scores: 6, 6, 8, 8

## Abstract
Predicting and executing a sequence of actions without intermediate replanning, known as action chunking, is increasingly used in robot learning from human demonstrations. Yet, its reported effects on the learned policy are inconsistent: some studies find it crucial for achieving strong results, while others observe decreased performance. In this paper, we first dissect how action chunking impacts the divergence between a learner and a demonstrator. We find that action chunking allows the learner to better capture the temporal dependencies in demonstrations but at the cost of reduced reactivity in stochastic environments. 
To address this tradeoff, we propose {\emph{\methodname}} (\methodacro), a test-time inference algorithm that bridges action chunking with closed-loop operations.
{\methodacro} samples multiple predictions at each time step and searches for the optimal one based on two criteria: (i) backward coherence, which favors samples that align with previous decisions; (ii) forward contrast, which seeks samples of high likelihood for future plans.
By coupling decisions within and across action chunks, {\methodacro} promotes consistency over time while maintaining reactivity to unexpected changes. 
Experimental results show that {\methodacro} boosts the performance of two state-of-the-art generative policies across seven simulation benchmarks and two real-world tasks.
Code and videos are available at \url{https://bid-robot.io}.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper examines the impact of action chunking in robot learning from demonstrations, where actions are executed in sequences without intermediate replanning. While action chunking helps robots learn temporal dependencies, it can hinder adaptability in dynamic environments. To mitigate this tradeoff, the authors propose Bidirectional Decoding (BID), a test-time inference method that enhances reactivity while preserving the benefits of chunking. BID samples multiple actions per step, selecting the best based on backward coherence (consistency with prior actions) and forward contrast (alignment with stronger policy predictions and deviation from weaker ones). This approach improves temporal consistency and adaptability, yielding better results across multiple simulation benchmarks and real-world tasks. On the down-side, the approach requires significantly more compute as multiple model outputs are sampled. Authors deal with that by parallelizing the computation.

### Strengths
- Proposed method seems reasonable and well-thought of, with clear description and theoretical backing.
- Paper is well written, clear and well-structured. The motivation and the idea of the paper is clear. The approach is clearly stated and all relevant background is introduced well. The method explanation is accompanied with appropriate visualisation figures that help understanding.
- The proposed method achieves good performance on target experiments.
- The approach is tested in several simulation and real experiments.

### Weaknesses
 - The method requires significantly more compute than the base methods.
- The definition of a horizon is sometimes unclear. In Moving Horizon fields (e.g. Model Predictive Control - MPC) horizon is what is presented in the paper as $l$. Perhaps this should be also labeled on the Figure 3. The horizon $h$ in this paper is used to describe what is replanning time in MPC.
- Generally, it would be useful to back this more to the MPC field. As focus of the paper is not on the inference itself but more on using any planning/prediction model in the closed-loop. Borelli, Bemporad, Morari, Predictive control book.
- The analysis on the replanning times and prediction horizon seems to be a bit limited and not fully consistent among different ablation studies.
- A single experimental problem is used for analysing the main point of the paper (demonstration with iddle action).  Figure 5 is not clear, why the results for 3 are better than for 5.
- Backward coherence as introduced here is a standard for improving temporal consistency when replanning in many MPC approaches.
- Description of policies in 3.2. is a bit confusing. It is not exactly clear are they aligned in time and why the importance is not same for the context for the first frame before the predicitons.
- In line 316 and 318, it is stated “equally optimal” and “the most optimal” that is in contradiction with the definition of the optimality.
- Using negative sets is not motivated well. This could be also investigated with ablation studies.

### Questions
- Can you clarify the definition of horizon, and relationship to MPC.
- Can you clarify experiments  in section 3.2.
- Can you explain in more detail dirrente policies for analysis in 3.2. E.g. can you show in Figure 3 with aligned current time. For time $t_k$ you predict the sequence with some length and take context with some length.
- In Corollary 2 you claim that $\pi_{h+d}$ is more disadvantageous but you show in eq (2) that the expected loss is smaller. This seems to be contradictory.
- Why is using negative set important?
- I would suggest using bar plot for fig 6 right.

### Soundness
3

### Presentation
3

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
The paper introduces Bidirectional Decoding (BID), a test-time inference algorithm designed to improve action chunking in robotic policies by balancing long-term consistency with reactivity to unexpected changes in the environment. The authors address the tradeoff observed in action chunking, where increased chunk sizes help capture temporal dependencies but reduce the robot’s responsiveness to dynamic elements. BID operates by sampling multiple actions at each time step and selecting the optimal one based on two criteria: backward coherence (alignment with prior actions) and forward contrast (similarity to a stronger, more optimal policy and difference from a weaker one). The approach enables more flexible, closed-loop decision-making that adapts to real-time conditions. Experimental evaluations across multiple simulation benchmarks and real-world tasks show that BID consistently enhances the performance of robotic policies, demonstrating its effectiveness as a plug-and-play solution to improve the robustness and accuracy of action-chunked behavior cloning models in robotics.

### Strengths
1. The concept of "Action Chunking" is relatively new, and further research could reveal additional advantages of this technique by deepening our understanding of its potential benefits. 

2. Experimental results demonstrate the promise of the proposed method, as it outperforms several state-of-the-art (SOTA) diffusion-policy-based behavior cloning techniques, suggesting it could be a viable approach to enhancing robotic policy learning.

### Weaknesses
1. From my understanding, Action Chunking primarily focuses on capturing implicit hierarchical relationships in action sequences without needing to acquire explicit representation of reusable skills or options (where "options" refers to temporally extended actions in hierarchical reinforcement or imitation learning). The field of option/skill discovery is active an active research direction, with an aim to explore methods to learn options/skills from either environmental interactions or recorded demonstrations.

2. Because Action Chunking requires pre-defined window sizes for past state observations and future actions, option/skill discovery methods (e.g. [1][2]) are potentially more adaptive and flexible than Action Chunking. It would be valuable for the paper to discuss and compare Action Chunking theoretically and experimentally with option/skill discovery approaches. Notably, in hierarchical RL, a common approach involves an initial option discovery phase, followed by a reinforcement learning phase utilizing these options. In this work, imitation learning could replace the second phase. Two recent, notable works on option/skill discovery [1][2] could serve as relevant comparisons.

3. Another limitation is that the reported performance improvements (e.g., Table 1) are modest. For example, the difference between the results of EMA (Zhao et al., 2023) in the 3rd row and the proposed method in the 4th row is relatively small. This pattern holds in Tables 2 and 3 as well: when compared only against the weakest baseline (Vanilla), the performance gains remain minor.

4. Furthermore, Tables 2 and 3 omit results for other leading baselines, such as Warmstart (Janner et al., 2022) and EMA (Zhao et al., 2023), which would strengthen the evaluation of the proposed method.

### Questions
Why is it necessary to set the 𝑐 parameter, which represents the window size of incorporated historical states? When employing an LSTM-based policy, the incorporation of historical states becomes more flexible. This flexibility is akin to the context window size used in word2vec for planning. The advantages of using LSTMs over a fixed context window 𝑐 have been discussed in the following paper: [1].

Reference:

[1] Zhuo, Hankz Hankui, et al. "Discovering underlying plans based on shallow models." ACM Transactions on Intelligent Systems and Technology (TIST) 11.2 (2020): 1-30.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper studies the usage of action chunking when learning policies through behavior cloning of human demonstration data on robots. Action chunking is the prediction and execution of a sequence of actions over a horizon $h$ without closed loop control. Long sequences of predicted actions lead to increased temporal consistency in the policy but lack the ability to react to short-term noise in a given system; on the other hand, short sequences of action chunks allow for this reactivity but at the expense of temporal stability. This is a well-known phenomena that affects the design decisions of machine learning and robotics practitioners. This paper provides theoretical analysis of the problem and introduce bidirectional decoding, an inference time policy change that naturally balances the need for long-term consistency with short term stability. The authors test their method on various toy and scaled up domains and show their method superior.

### Strengths
This paper is written clearly and well-motivated. To my knowledge, this is the first formalism of the optimality gaps incurred when trading off context length and prediction horizon. They demonstrate some exciting results that attempt to dissolve the issue of deciding an action-horizon on multiple domains like FrankaKitchen and PushT. They also describe some real-world experiments on robots but they are not the main focus of this paper.

### Weaknesses
There are several weak points in the paper that detract from the paper's quality.

1. **Human latents**: There is some motivation surrounding the latent intentions of humans that are not directly observed. However, talk of latent intentions is not mentioned in any technical sense so it is not clear how different latents $z_t$ affect the methodology and analysis presented in the paper. The paper does not specify how these latent intentions are modeled or incorporated into the action chunking framework, making it difficult to assess their impact on the proposed method. For example, are these latents discrete or continuous? How does the model infer these latents from the observed demonstrations, and how do these inferred latents influence the bidirectional decoding process?
2. Lack of model-based/model-free discussion: In section 3.2, the authors outline their approach to theoretical analysis. It is not clear how model-free or model-based policies fit into this framework or the analysis. In my understanding of the analysis, the authors expect the policies to learn implicit dynamics models and do not ever explicitly learn them. The analysis seems to assume that the policy implicitly learns a dynamics model, but this is not explicitly stated or justified. A discussion on how the proposed method relates to model-based approaches would be beneficial, especially regarding the trade-offs between learning an explicit model and relying on implicit dynamics learned through behavior cloning.
3. Ambiguous definitions in 3.2: I understand that the appendix provides better definitions of the quantities $\alpha$ and $\epsilon$, but given that they are crucial to understanding the analysis, the definitions in the main paper are not sufficient for understanding. The main paper lacks sufficient detail on the definitions of $\alpha$ and $\epsilon$, making it difficult to grasp the theoretical analysis. Specifically, the paper should clarify how these quantities relate to the temporal dependencies in the action sequences and the stochasticity of the environment. Without a clear understanding of these terms, the theoretical results are hard to interpret.
4. Difference between Corollary 2 and Corollary 3: The inequalities in (3) and (4) are exact opposites of each other, except for their qualification in the corollary text. It is not clear mathematically why these two inequalities are opposite. The mathematical reasoning behind the opposing inequalities in Corollaries 2 and 3 is not sufficiently explained. The paper should provide a more detailed explanation of the conditions under which each inequality holds, and how these conditions relate to the properties of the environment and the learned policy. It is unclear how the deterministic vs stochastic nature of the environment leads to these opposite conclusions.
5. Minimizing loss in (5): Algorithm 1 suggests that the action selection is not used during training time and only at inference time. Would not the policy benefit from doing BC training with this action selection method? The paper does not explore the possibility of incorporating the proposed action selection method during training. It is not clear why the authors chose to only employ this method at inference time, and whether training with this selection method would lead to better performance. It is possible that the policy could benefit from being trained with the same action selection method used at inference time, which could improve the consistency between training and testing.
6. Weaker policy used for contrastive $\mathcal{L}_F$: using an older, weaker policy for a contrastive loss may lead to replacing some design decisions with equally harder decisions that must be made by the practitioner. The use of an older, weaker policy for the contrastive loss introduces a potential hyperparameter tuning problem. The paper should discuss the sensitivity of the method to the choice of the weaker policy and provide guidance on how to select this policy in practice. It is possible that the performance of the method is highly dependent on the quality of the weaker policy, which could make it difficult to use in practice.
7. No error bars: Figure 6 display main results of the superiority of the authors' method but they do not include any statistical significance on the results they report. This is a major weakness in my opinion and indicates that the experimentation was not sufficient.

### Questions
In addition to addressing the weaknesses, I would like the authors to answer the following questions:
1. In equation (6), why use MSE style loss as opposed to a KL divergence on the action distributions? Is MSE more robust in this context?
2. Can the authors describe more technically why this methodology has a focus on human demonstrations? The argument of latent intentions is not clear to me.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The study presents a theoretical exploration of action chunking. It offers valuable insights, demonstrating the feature of action chunking varies across different scenarios, particularly depending on the degree of determinism or stochasticity in the environment. The findings suggest that in deterministic environments, action chunking improves long-term consistency, whereas in highly uncertain environments, it struggles to adapt effectively to changes, as reactivity becomes more critical.

The paper introduces BID—an inference-time, model-agnostic, computationally efficient, and easy-to-use plug-and-play algorithm designed to enhance action chunking, emphasizing better closed-loop control. BID selects action chunks from samples based on two key criteria: backward coherence and forward contrast.

The experiments begin with a simple yet effective discrete one-dimensional toy policy, validating the theoretical insights on the relationship between action chunking and varying degrees of environmental determinism or stochasticity. The effectiveness of BID is further evaluated using Diffusion Policy as the base policy and compared against three other baseline action chunking strategies (vanilla, warm start, and EMA) across three simulators: Push T (single task), RoboMimic (four tasks: Lift, Can, Square, and Transport), and Kitchen.

Additional experiments explore BID’s scalability by varying batch sizes and its compatibility with different sampling strategies. The results also demonstrate BID’s generality and efficacy in real-world applications, reinforcing its practical utility.

### Strengths
The work employs well-founded models and thoughtful improvements to make a commendable attempt at uncovering the essential latent factors of action chunking, such as the environment’s degree of determinism. It offers insightful explanations of the theoretical analysis, clearly highlighting the benefits (consistency) and drawbacks (reduced reactivity) of action chunking.

The experiments are comprehensive, demonstrating BID’s effectiveness across a variety of scenarios.

### Weaknesses
I found some of the figures difficult to interpret. For example, in Figure 1, I assume the goal is to illustrate how BID combines the benefits of (a) and (b). However, the concepts introduced in the paper, such as backward coherence and forward contrast, are not intuitively reflected in the figure. Similarly, the meaning of Figure 3 is unclear.

A more significant concern is the lack of a clear connection between the BID criteria in Section 4.2 and the intended trade-off between consistency and reactivity. Specifically, the discussion on reactivity is vague, and it is not evident how the BID design enhances reactivity. I believe additional explanations are necessary to clarify how the proposed BID method addresses reactivity, providing more detailed reasoning behind the design choices.

Furthermore, the choice of using Euclidean distance for evaluating action consistency in both backward coherence and forward contrast is questionable. While Euclidean distance might be suitable for some action spaces, it is unlikely to be universally optimal, especially when dealing with robotic systems with complex action spaces involving orientations or joint angles. In such cases, metrics like L1 distance or angle-based metrics (e.g., cosine similarity) might be more appropriate. The lack of exploration into alternative metrics raises concerns about the robustness and generalizability of the proposed method across different robotic embodiments.

### Questions
I have a detailed question regarding the design of backward coherence 
$\mathcal{L}_B$ and forward contrast $\mathcal{L}_F$. Specifically, you use Euclidean distance to evaluate the consistency (similarity) of actions at individual time steps. However, there are many alternative metrics that might be more suitable depending on the nature of the values. For example, in typical 7-DoF robotic arm actions, three values represent orientation, and Euclidean distance may not be the most appropriate metric. In some cases, L1 distance or angle-based metrics (e.g., cosine similarity) might be more suitable or even more direct alternatives. Could you provide additional experiments to explore the impact of different metrics on your two criteria and their effect on the experimental outcomes?

I am also curious about the design of forward contrast. I did not clearly see its connection to your theoretical analysis, particularly in terms of its relationship with reactivity. Could you provide more insights into why you designed forward contrast this way and how it specifically enhances reactivity? Alternatively, if there are other possible designs that improve reactivity, I suggest revisiting and reworking Sec.4.2 to clarify these aspects more thoroughly.

Additionally, I am wondering whether the weighted sampling strategy used in ACT (introduced with [ALOHA](https://arxiv.org/abs/2304.13705)) could serve as a reasonable baseline for comparison. It would be helpful to see comparison results between BID and action sampling strategy used in ACT. Could you conduct further experiments to evaluate this comparison and enhance the analysis of BID’s effectiveness?

### Soundness
3

### Presentation
1

### Contribution
2

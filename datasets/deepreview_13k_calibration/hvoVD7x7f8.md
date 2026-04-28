# Uncertainty-Aware Decision Transformer for Stochastic Driving Environments

- Decision: Reject
- Avg Score: 5.00
- Scores: 6, 6, 5, 3

## Abstract
Offline Reinforcement Learning (RL) enables policy learning without active interactions, making it especially appealing for self-driving tasks. 
Recent successes of Transformers inspire casting offline RL as sequence modeling, which, however, fails in stochastic environments with incorrect assumptions that identical actions can consistently achieve the same goal. In this paper, we introduce an \textbf{\underline {UN}}certainty-awa\textbf{\underline{RE}} deci\textbf{\underline S}ion \textbf{\underline T}ransformer (UNREST) for planning in stochastic driving environments without introducing additional transition or complex generative models. Specifically, UNREST estimates uncertainties by conditional mutual information between transitions and returns. Discovering `uncertainty accumulation' and `temporal locality' properties of driving environments, we replace the global returns in decision transformers with truncated returns less affected by environments to learn from actual outcomes of actions rather than environment transitions. We also dynamically evaluate uncertainty at inference for cautious planning.
Extensive experiments demonstrate UNREST's superior performance in various driving scenarios and the power of our uncertainty estimation strategy.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper addresses a major challenge of "return-conditioned supervised learning" methods like Decision Transformers (DTs) in stochastic environments. DTs can be overly optimistic in stochastic environments when some of these expert (high reward) trajectories arise due to accidental environment transitions. The authors propose a "practical" solution for this in the self-driving domain, using 'uncertainty accumulation' and 'temporal locality' properties specific to this domain. They segment the trajectories into deterministic/certain (low uncertainty) and stochastic/uncertain (high uncertainty) regions using information theoretic metrics. In deterministic regions, they use a "truncated return conditioned DT", while in the stochastic regions, they allow the policy to cautiously follow the expert without any return conditioning. Empirical results demonstrate UNREST's superior performance in various driving scenarios compared to the state-of-the-art offline RL methods.

### Strengths
These are the strengths in my opinion:

1) Studies and proposes a practical solution to a major drawback of "return-conditioned supervised learning" methods like DTs in stochastic environments (specifically self-driving domain).
2) The segmentation based on uncertainty and associated decision-making intuitively makes sense and has not been explored before in the context of DTs, Upside Down RL [1,2] etc in stochastic environments. to the best of my knowledge.
3) The results on the CARLA simulator are strong compared to the baselines.

### Weaknesses
These are the weaknesses in my opinion:

1) Evaluated only on a single environment.
2) The idea of using truncated returns is not entirely novel though and has been used in the upside-down RL methods [1,2].
3) The algorithm assumes the data have to come from an expert if I understand correctly (especially for the logic to work in uncertain regions). The authors use expert data (from the autopilot) in the training process. Isn't this a drawback when compared to existing offline RL baselines which can also leverage suboptimal trajectories/data?

### Questions
1) Would this method scale to other stochastic environments like the ones used in baseline algorithms [3] and [4] ? 
2) Would this method be applicable if the offline dataset contains suboptimal trajectories ?? 
3) Is there a better strategy the method can follow in "uncertain" regions than just following the expert? Like somehow being able to use the expected Returns or something on that line.


**References**
[1] Schmidhuber, Juergen. "Reinforcement Learning Upside Down: Don't Predict Rewards--Just Map Them to Actions." arXiv preprint arXiv:1912.02875 (2019).

[2] Srivastava, Rupesh Kumar, et al. "Training agents using upside-down reinforcement learning." arXiv preprint arXiv:1912.02877 (2019).

[3] Sherry Yang, Dale Schuurmans, Pieter Abbeel, and Ofir Nachum. Dichotomy of control: Separating what you can control from what you cannot. In The Eleventh International Conference on Learning Representations, 2022.

[4] Keiran Paster, Sheila McIlraith, and Jimmy Ba. You can’t count on luck: Why decision transformers fail in stochastic environments. Advances in neural information processing systems, 2022.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies the problem of modeling driving as an *offline* stochastic sequence prediction problem. This is inspired by the recent success of approaches like the decision transformer. They note that for tasks like driving, existing approaches that just perform sequence prediction on an offline data set conflate the success a of a particular action with the stochastic transition necessary to replicate the success. This results in the accumulation of uncertainty in future predicted value, making existing approaches overly optimistic and unsuitable for such environments. The paper proposes explicitly modeling uncertainty in certain parts of the sequence prediction and *not* condition on the target reward in such cases. This naturally segments the problem into a sequence of tasks which as the paper points in natural in the driving context. The paper shows with several studies showing the efficacy of their approach.

### Strengths
1. The paper addresses some of the emerging concerns with naively applying sequence prediction systems such as the decision transformer to decision making tasks. Namely, that the underlying domain can be stochastic.

2. The approach is straightforward and motivates the way it builds off of existing work.

3. The method is empirically demonstrated to perform well against existing baselines including  other approaches which attempt to model uncertainty.

4. The ablation and experiment design seem sufficiently well crafted and the approach is well motivated enough that I generally believe the key results.

### Weaknesses
1. The exposition, particularly the first half of page 2 is hard to understand.
    a. For example, its not explained what a highly representative environment model is and why it might not be learnable. I understand this is related work, but the reader is completely left in the draft about why the presented approach avoids this.
    b.  Task I+II is initially presented in a manner that is unclear that + here means sequential composition, e.g. perform Task I and then Task II. This makes sense once finishing the page and the segmentation, but the exposition seems like it could be improved significantly.

2. The uncertainty threshold seems like a key hyperparameter and it seems unclear how to set it. Further, it seems that mainly driving tasks have large regions of uncertainty that should themselves be segmented, e.g., a sequences of nearby intersections. How to generalize the segmentation approach to this setting is unclear.

3. While there's ample empirical evidence for this approach's success, there isn't a clear theoretical framework to connect it to. I see a tentative connective with work on causal vs non-causal entropy regularization and it's similar effect on creating over optimistic agents. A deeper theoretical basis would be appreciated.

### Questions
The experiments and setup seem to be for the fully observable context, save for the other driver's implicit latent states.

That said, in the automotive setting a non-trivial amount of uncertainty is derived from the partial observability of the environment, e.g., where exactly is the crossing region in an intersect, what is the drivable area, what are that boundaries, where are the obscured pedestrians and bikes, etc.

How could the presented approach be adapted to such settings?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a method that adopting conditional mutual information of two network output distribution as the measure of uncertainty. And some numerical superiority is demonstrated.

### Strengths
uncertainty is an important topic in RL topics especially in autonomous driving. The general idea of separating environmental stochasticity versus action return is interesting. 
Some theoretical justifications are provided to hint some insights of the method.
Numerical experiments show some superiority.

### Weaknesses
The paper is not well written.
1. A lot of notations are used before definition. For example, section 4.2 \tau^{ret}_{<t} 
2. Some "terms" and "notation" are used without definition or even description, which makes very difficult to understand. For example, Figure 1(a) Task I and Task II (b) normalized ground Truth.
3. A lot of key contents description is very "verbal" and "handwaving", leaving huge ambiguity of the understanding of the algorithm.
4. If DT is a fundamental base of the method, having a brief introduction is more friendly to new readers.

### Questions
Does the "Transformer" term in section 4,2 means two independent network for x_{a_t} and x_{s_t}. Please give more concrete/clear description using notations flow of your method in general instead of long words description.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper addresses the challenge of utilizing offline Reinforcement Learning (RL) for autonomous driving tasks, especially in stochastic environments where unpredictable events can occur. Traditional methods, influenced by the successes of the Transformer architecture, have reimagined offline RL as sequence modeling. However, these methods, known as decision transformers, tend to make overly optimistic assumptions in unpredictable environments. They often incorrectly believe that a particular action, once successful, will always lead to the desired outcome. This is problematic because in real-world driving, identical actions can lead to vastly different outcomes based on unpredictable factors like the behavior of other vehicles. The crux of the issue lies in differentiating the outcomes resulting directly from the agent's actions versus those emerging from the unpredictable environment. Current attempts to solve this have primarily focused on creating state transition models, but these are intricate and demand highly representative environment models, which are hard to achieve for intricate driving tasks. To combat this, the paper introduces the UNcertainty-awaRE decision Transformer (UNREST). The core idea is to customize decision transformers for unpredictable driving scenarios without adding more complexity. UNREST achieves this by estimating state uncertainties via the mutual information between transitions and returns.

### Strengths
1. Using the offline RL framework to solve driving tasks is a promising and interesting direction as online training is not feasible due to the safety issue. This paper modifies a state-of-the-art framework, i.e., a decision transformer to achieve better performance considering the uncertainty of the environment.

2. The evaluation part is comprehensive, including many baseline methods and evaluation metrics. There are also many ablation studies that investigate the influence of different modules of the model.

### Weaknesses
1. Where does the uncertainty in autonomous driving come from? My understanding of uncertainty is that with the same (s, a) pairs, the environment returns different rewards. Figure 1 tries to provide an example but a lot of information is missing. For example, what is the purpose of the traffic light? What does the x-axis label “return” mean for task 1 and task 2? Do the authors mean reward to go?
2. The motivating example of the uncertainty in the driving scenario seems to involve the tradeoff between reward (reaching point) and cost (collision). In my opinion, tuning the weights in reward functions or some other parameters could dramatically influence the “uncertainty” investigated in this paper. Basically, it will lead to either aggressive or conservative driving policy. However, cost or constraint is only discussed in the appendix. Therefore, I doubt that the proposed transformer model can correctly estimate the uncertainty.
3. It seems that one important problem investigated in this paper is “Uncertainty Accumulation”, which is reasonable since the uncertainty increases as the trajectories accumulate more steps. However, why do we care about the accumulation of uncertainty in driving tasks? A normal driving algorithm just needs to make decisions based on current uncertainty and historical information. I guess one reason could be the DT framework uses reward-to-go as a condition. If this is the case, this paper may not be applicable to other frameworks.  
4. A lot of important information is missing in figures, experiments, and conclusions.

### Questions
1. After checking Property 1 and Property 2, I still cannot fully understand Figure 1. For example, what does “normalized groud truth” mean (I assume “groud” is a typo of “ground”)? I highly suggest the authors provide a simplified and intuitive example in the first figure without adding any distracting information. The detailed explanation can be put in later sections.
2. I noticed that the offline data is collected in Carla with Autopilot. How to show that the data contains uncertainty? Should the uncertainty come from the behavior of surrounding vehicles?
3. Missing information in Figure 2. What does h represent? Why does h start from 1 but end with 80, 79? 
4. Information missing in Figure 3. What does the light blue rectangle mean? Which one is the ego vehicle? What does failure mean in Figure 3(a)? It seems that the lane change is not available as there is another car in the target lane. What’s the difference between Figure 3(a) and Figure 3(b)?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

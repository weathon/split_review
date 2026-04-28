# Studying the Interplay Between the Actor and Critic Representations in Reinforcement Learning

- Decision: Accept
- Avg Score: 6.80
- Scores: 6, 6, 6, 8, 8

## Abstract
Extracting relevant information from a stream of high-dimensional observations is a central challenge for deep reinforcement learning agents. Actor-critic algorithms add further complexity to this challenge, as it is often unclear whether the same information will be relevant to both the actor and the critic. To this end, we here explore the principles that underlie effective representations for an actor and for a critic. We focus our study on understanding whether an actor and a critic will benefit from a decoupled, rather than shared, representation. 
Our primary finding is that when decoupled, the representations for the actor and critic systematically specialise in extracting different types of information from the environment---the actor's representation tends to focus on action-relevant information, while the critic's representation specialises in encoding value and dynamics information. Finally, we demonstrate how these insights help select representation learning objectives that play into the actor's and critic's respective knowledge specialisations, and improve performance in terms of agent returns.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper investigates representation learning objectives for actor and critic networks in deep reinforcement learning, specifically in the context of policy gradient algorithms. Using information-theoretic metrics, the study reveals that the actor and critic networks naturally specialize in capturing distinct information types, with the actor focusing on action-relevant features and the critic on value and environmental dynamics. This specialization is shown to enhance model architecture design and improve representation learning objectives, ultimately contributing to greater sample efficiency in reinforcement learning. In addition, this paper also how various representation learning objectives could help shaping the actor and critic's representation and improve the RL sample efficiency.

### Strengths
-  **Novel Perspective on Representation Specialization**: This paper provides a fresh and thorough analysis of actor and critic representation specialization using information-theoretic metrics. 
- **Convincing Empirical Evidence**: The authors provide substantial empirical support for their claims, with extensive experiments that effectively demonstrate the impact of decoupling actor and critic representations, as well as impacts of different representation learning objectives on the resulting representation.
- **Insightful Conclusions**: The study draws interesting and impactful conclusions regarding how specialized representation learning objectives can improve sample efficiency and generalization in RL, a great contribution to the RL community, shedding light on the design of future deep RL algorithms.

### Weaknesses
 - **Limited Scope of Algorithm Selection**: The paper exclusively focuses on online, on-policy, policy gradient algorithms (e.g., PPO, DCPG), leaving it unclear how well the conclusions apply to other RL frameworks, particularly off-policy algorithms like DDPG or SAC. Broader consideration of diverse algorithm types would strengthen the generalizability of the findings. Also, whether the same conclusion holds under different model sizes? It would be useful to add in the paper to show that this conclusion would still hold if we simply added capacity to the actor/critic network without changing any learning objectives.
- **Presentation and Clarity**: The paper’s structure and presentation could be significantly improved to make it more easier to understand for readers. The writing is currently dense, making it challenging to grasp the main takeaways and hypotheses. For instance, restructuring sections with clearer headings, especially in Sections 6.1 and 6.2, would help readers navigate the study’s conclusions. Using bullet points to highlight key hypotheses and findings, as well as starting each paragraph with a bolded summary sentence, could enhance readability and ensure that readers capture the core messages more effectively.

### Questions
- What does the delta percentage in Figure 1 represent? It would be helpful if the authors added a brief explanation to the caption.
- How is mutual information measured in this study? Currently, it’s detailed only in the appendix, but a high-level explanation in the background section would help readers understand the methodology better.
- Could the authors add a performance plot to the figures in the main paper? This would clarify how the information-theoretic metrics relate to final performance outcomes.
- Is it true that $I((Z,Z'); A)$ + $I(Z,Z')$ in general is a good indicator of the algorithm's performance? (Looks like it's the case from Figure 3 and Figure 7.) The authors seem to argue that while actor representation (decoupled) tends to have larger $I((Z,Z'); A)$ while smaller $I(Z,Z')$ and the reverse holds for critic representation, combing them in a coupled representation does not combine the best of both world and resulting in smaller $I((Z,Z'); A)$ + $I(Z,Z')$ and thus worse performance?
- Could Figures 7 and 8 be moved from the appendix into the main paper? The authors might need to shorten other parts of the text rather than placing key results in the appendix while referring back to them in the main sections.
- In Section 6.1, it would be clearer if the authors defined the dynamics prediction objective from Moon et al. with a brief equation or sentence rather than just citing the source. Similarly, in Section 6.2, could the authors introduce the MICo objective with an equation first?
- In Section 6.1, lines 466–468, the distinction between explanations (1) and (2) is unclear; both seem to attribute reduced overfitting to the larger batch size used in value distillation. If the authors hypothesize that batch size is the main factor here, could they test this by running PPO with larger batch sizes, then measuring the relevant metrics to assess any changes in overfitting?
- A broader concern is how the study's conclusions about decoupled versus coupled objectives hold across varying model sizes. For instance, in Section 6.2, the authors note that adding a dynamic prediction objective to the critic impacts certain metrics but harms performance due to an unintended specialization. Similarly, the study attributes overfitting to the coupled representation. Could these conclusions change with larger model capacity (and also training with larger batch sizes as the author claims that this results in more overfitting)? Intuitively, if the shared representation had sufficient capacity (and were trained on larger batches as discussed), could a shared representation still achieve strong performance across the information-theoretic metrics, potentially improving performance without conflicting specializations?

### Soundness
3

### Presentation
2

### Contribution
4

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper focus on the difference in representation graph between actor and critic in AC methods in RL. The authors aims to more formally validate an empirical finding where decoupling actor and critics may help with representation learning through

### Strengths
- The way in which the topic is approached in the section is well considered, I find it readable
- I appreciate the clear problem formulation and motivation of the paper
- The results, while not counter-intuitive nor surprising, gives some form of closure to the decoupling findings in earlier works, and brings this issue to attention does help clarify the topic
- Assumption seems reasonable

### Weaknesses
 - Potentially need more ground work setup, such as in the problem definition where an observation function is present, which normally implies that the MI between state and observation is not maximized, but it seems the rest of the paper operate on the assumption that it is indeed maximized and so that the environments are fully observable.
- Evaluation is lacking in breath, it would be great to include a general set of tasks.
- Why use the idea of context, if I'm not mistaken, the entire work can be done with a normal MDP and MDPs with contexts can be seen as a encompassing MDP with different starting states.
- The increased compute and parameter size of decoupled approach may also play a role in learning, is there any intuition or validation on the topic?
- I disagree that "an optimal or near-optimal representation can never be reached under a shared architecture"; from the reduced MDP point of view, I agree that a shared architecture may not be as concise, but still can be optimal (for both policy and value) given that it is a shared architecture.

### Questions
- Why use the idea of context, if I'm not mistaken, the entire work can be done with a normal MDP and MDPs with contexts can be seen as a encompassing MDP with different starting states.
- The increased compute and parameter size of decoupled approach may also play a role in learning, is there any intuition or validation on the topic?
- I disagree that "an optimal or near-optimal representation can never be reached under a shared architecture"; from the reduced MDP point of view, I agree that a shared architecture may not be as concise, but still can be optimal (for both policy and value) given that it is a shared architecture.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper analyzes how different choices of architecture and representation learning objectives affect overfitting on, transfer to, and specializing in different levels of games (ProcGen). The analysis is largely established on the mutual information between different quantities. The author concludes that actor and critic representation specialize in different information, that critic can influence exploration significantly, and that representation learning objectives (i.e., auxiliary loss) should be consistent with the specialization of actor and critic representation.

### Strengths
The analysis to representation learning based on mutual information is interesting. The conclusion drawn from this analysis is helpful for deep RL researchers on designing representation learning objectives.

### Weaknesses
Writing is very unclear. See my questions for details. Overall, there are overwhelming notations, making the presentation unnecessarily complex. The reason of defining each notation is also not clear to me. Takeaway messages in each section is also not clear. For example, in section 4.1, the author starts with lots of new definitions without explaining why these are necessary. I would suggest the author explain why we need those definitions and then say the high-level messages before diving into details.

- Line 154: Why measuring how easy it is to infer the identity of the current level from Z is a good measure of overfitting?
- Line 158: The purpose of Theorem 3.1 is not explained. Also, is it a result from the other paper or proved first time in this paper?
- Line 165: Why does a high I(Z_C, V) help optimizing the value loss?
- Line 166: What do you mean by increasing I(Z_A, V) and what's the relationship between value distillation and increasing I(Z_A, V)?
- Line 175: What do you mean by "whether it is possible to identify latents (ϕ(o), ϕ(o′))) obtained from consecutive observations from pairs stemming from non-consecutive observations?" Is it consecutive or not?
- Line 194: What's the role of linear probing here?
- Equation 6: What are $z^*_{A_0}$ and  $z^*_{A_1}$? Why I((Z^*_A, Z^*'_A); A) is guaranteed to be maximized when following the optimal policy?
- Line 256: I don't see why zero-shot transfer is evident in your example.
- Figure 3: How should one interpret these values? The higher the better? The lower the better? Better summarize the takeaway in the caption.
- Line 374: Why does maximizing J^\pi bias \pi to collect trajectories with high I(O; V)?
- Line 431: Why does actor objective promote learning invariant quantity?

### Questions
- Line 154: Why measuring how easy it is to infer the identity of the current level from Z is a good measure of overfitting?
- Line 158: The purpose of Theorem 3.1 is not explained. Also, is it a result from the other paper or proved first time in this paper?
- Line 165: Why does a high I(Z_C, V) help optimizing the value loss? 
- Line 166: What do you mean by increasing I(Z_A, V) and what's the relationship between value distillation and increasing I(Z_A, V)?
- Line 175: What do you mean by "whether it is possible to identify latents (ϕ(o), ϕ(o′))) obtained from consecutive observations from pairs stemming from non-consecutive observations?" Is it consecutive or not?
- Line 194: What's the role of linear probing here?
- Equation 6: What are $z^*_{A_0}$ and  $z^*_{A_1}$? Why I((Z^*_A, Z^*'_A); A) is guaranteed to be maximized when following the optimal policy?
- Line 256: I don't see why zero-shot transfer is evident in your example.
- Figure 3: How should one interpret these values? The higher the better? The lower the better? Better summarize the takeaway in the caption.
- Line 374: Why does maximizing J^\pi bias \pi to collect trajectories with high I(O; V)?
- Line 431: Why does actor objective promote learning invariant quantity?

### Soundness
2

### Presentation
1

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
This paper studies whether actors and critics benefit from a decoupled representation. The authors find that when decoupled, actors and critics learn representations that specialize in different types of information from the environment. Additionally, there is an interplay between these representations even when they are decoupled. The authors show how this insight helps select representation learning objectives for better performance.

### Strengths
**originality**
- although the fact that decoupled actor and critic learn different representations is not really surprising, the other findings in the paper are very interesting and novel. 
-  the four mutual information metrics are interesting and helps to understand the effect of decoupled learning. 
- the paper gives some very novel and interesting analysis and results

**quality**
- it is good that authors plan to release all data and code for better reproducibility. 
- overall great quality

**clarity**
- writing is clear and easy to follow. 

**significance**
- empirical and theoretical results are good contributions 
- the analysis and insights from the paper are especially interesting

### Weaknesses
I don't have major concerns, minor ones:
- I think it can be nice to explicitly highlight, either in the beginning or conclusion, what are the best representation learning objectives and most important specialisations with quantitative measures. 
- The paper can be even stronger if similar analysis can be done for Q-learning based methods such as DDPG/SAC/TD3 type algorithms. But I understand that might be too much extra work.

### Questions
- For the mutual information metrics, e.g., Figure 4, how much will they change if we simply change some of the hyperparameters of one algorithm? I am curious about factors other than coupled/decoupled learning and how much impact they can have on these metrics.

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
Authors systematically investigate the impact of coupling and decoupling of the representations for actors and critics in on-policy actor-critic framework.

### Strengths
1. Theoretically-grounded study with the demonstration that actor and critic should be decoupled as their objectives contradict each other.
2. Good empirical study for confirming claims using various algorithms. When result contradict assumptions, authors test and confirm different hypothesis which could explain the observations. These assumptions reveal novel things for RL community, such as the potentially underestimated role of critic in exploration.
3. Additional study on the effects of different representation learning approaches and when they benefit performance.

### Weaknesses
1. Study is only conducted using the on-policy algorithms. It would be interesting to also investigate off-policy methods
2. If I understand correctly, study is performed only on discrete state and action spaces environments. Would the conclusions change if we switch to the continuous environments? It is not clear for me whether the proposed analysis can be applied to such tasks as the computation of mutual information becomes intractable.
3. For me, it was easy to get lost in many different metrics and keeping in mind what we want to maximize and what we want to minimize for the optimal solutions.

### Questions
My questions are based on the weaknesses

1. Could authors please elaborate on weaknesses 1 and 2?
2. According to weakness 3, I would recommend authors to add some additional information to the tables and plots about whether the metric is expected to be minimized or maximized.

### Soundness
3

### Presentation
2

### Contribution
3

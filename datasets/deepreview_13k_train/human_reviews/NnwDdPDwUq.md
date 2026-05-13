# Contextual Bandits with Entropy-based Human Feedback

- Decision: Reject
- Scores: 5, 5, 3, 3

## Abstract
In recent years, preference-based human feedback mechanisms have become integral to improving model performance across a range of applications, including conversational AI systems like ChatGPT. However, existing methodologies often overlook critical factors such as model uncertainty and variability in feedback quality. To address these limitations, we propose an innovative entropy-based human feedback framework designed for contextual bandits, which balances exploration and exploitation by soliciting expert feedback when model entropy surpasses a predefined threshold. Our method is model-agnostic and adaptable to any contextual bandit agent employing stochastic policies. Through rigorous experimentation, we demonstrate that our approach requires minimal human feedback to achieve significant performance gains, even with suboptimal feedback quality. Our work not only introduces a novel feedback solicitation strategy but also underscores the robustness of integrating human guidance into machine learning systems. Our code is publicly available: \url{https://anonymous.4open.science/r/CBHF-33C5}

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces a new dimention into the contextual bandit formulation related to human feedback. The idea is that, during the training phase, human feedback can be queried and used instead of the action selected by the learning agent (or in the RM case, the human feedback may bias the reward). Experiments are conducted on a number of datasets and Learning algorithms to understand the performance of algorithms in this setting across different settings of human expertise and other parameters.

### Strengths
The setting explored in this paper seems novel to me, though I am not an expert in the Bandit space. I wonder if the area of off-policy bandits are relevant here ( see https://arxiv.org/abs/2010.12470) since by taking human feedback in some interactions, the bandit is somewat getting rewards "off-policy".

The combination of algorithms and settings explored seem quite thorough and from what I can tell, some interesting insights can be gleaned about the role of "AR" feedback vs "RM".

### Weaknesses
1. No theoretical analysis is done in this setting, which is usually the case for Bandit algoirthms, from my limited experience.

2.  There is something about the formulation I dont get. It seems the bandit algorithms will be incentivized to maximize entropy as much as possible, in order to get the benefit of as much human feedback as possible (at least for a sufficient amount of expertise from the human). In other words, the formulation does not really assign any cost  to the act of getting human feedback during training, from what I can see.



### Questions
1. I am very confused by where the human feedback come from and how this relates to the baseline. I guess the HF is just computed by accessing the ground truth labels and generating the matching feedback. What exactly is the baseline? Does it never access human feedback at all? (if not this would also be a useful baseline to look at).

2. Isn't regret a more common notion to evaluate bandit algorithms than mean cumulative reward computed AFTER training?

3. minor: lines 14-15 of Alg 1 are really not necessary in an academic paper.

4. eq 7: missing closing brackets.

### Soundness
3

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
3

### Summary
The paper proposes an entropy-based method to determine when to seek expert feedback actively and investigates the relationship between the type of expert feedback (action-based vs. preference-based) and the expert quality and their impact on bandit learning. 

Overall, even though the experiment section seems thorough, I have several concerns about the proposed methodology, which I will detail later.

### Strengths
- The paper is well-written
- The experiment is fairly thorough

### Weaknesses
Issues related to the methodology:
1. The paper didn't cite a few influential works in this area: [1] acquires value annotation for labeling actions; [2] DAGGAR, which also directly gets experts to perform an action (similar to what this paper has proposed); and [3] APO, which actively selects which data to get trajectory-level preference label from. I especially consider [1] and [3] relevant to this paper's context.
2. The methodology of simply selecting data points based on the policy's entropy lacks justification. Bayesian active learning frameworks such as BALD [4] already use entropy. How is reducing policy action entropy related to discovering arms with higher rewards? The paper offers hand-wavy justifications. The paper needs to come up with solid justifications for why the method should be chosen.

Comment on the experiment section:
1. I do think the experiment section is clean and easy to follow at a glance. The subsection titles seem to want to summarize the findings. I do still find it lacking in terms of the key takeaway from each experiment. Sec 4.2 only says "variations" but offers no conclusive findings. Maybe you can summarize the results by grouping them into a few patterns and present them that way.
2. Sec 4.4 is an interesting analysis. I agree that many bandit papers focus a lot on theory but lack comprehensive experimental ablations. This paper's experiment tries to offer insights which I see as a strength.

### Questions
Continuing from the lack of justification on the methodology, ideas like BALD or information-directed sampling [5] use entropy reduction as the selection criteria. Have you considered instead of using just entropy, use some form of entropy reduction as the criteria for asking for feedback?

[5] Russo, Daniel, and Benjamin Van Roy. "Learning to optimize via information-directed sampling." Advances in neural information processing systems 27 (2014).

### Soundness
2

### Presentation
4

### Contribution
1

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper proposes an entropy-based framework to incorporate human feedback into contextual bandits. Specifically, it extends the bandit setup by adding a human intervention component, i.e., at any time, the agent could decide whether to utilize the human expert, where the human expert can either provide the optimal action, or give certain reward penalty of the proposed action. The proposed algorithm basically utilizes any bandit algorithm as the backbone algorithm, and decides to call the human expert based on the entropy of policy $\pi$, i.e., uncertainty in the policy decision. Experiments are done on some multi-class classification problem.

### Strengths
- The proposed method is simple, easy to implement, and presented in a clear way.
- The setting of incorporating expert feedback/intervention in the classical bandit framework is interesting.

### Weaknesses
 - The paper’s presentation is somewhat unclear, particularly in the problem formulation. It seems to propose a stronger variation of bandit problems where the model can access oracle labels, but this isn’t clearly explained. Section 3.1 could be revised to clarify this new setup.

- With this revised formulation, it would also help to include a theoretical guarantee for the proposed algorithm, addressing the how it affects on overall regret, the lower bound on the new formulation, and whether the algorithm is optimal.

- While direct supervision through oracle labels is understandable, the reward manipulation is confusing. This reward shaping doesn’t change the algorithm’s selected action; rather, it modifies the reward. It’s unclear why this is necessary when the underlying reward already reflects sub-optimality. Clarifying the motivation here would strengthen the paper.

- The novelty of using entropy-based active learning is also limited; see [1] for a comprehensive review. The paper would benefit from a detailed comparison of its contributions to prior work, and highlight the novelty here.

- Further, several hyper-parameters lack clarity, such as the reward penalty $r_p$ and entropy thresholds.

- Finally, the empirical results are not presented in an especially meaningful way. For example, Figure 2 is difficult to interpret. The oracle access in action recommendation appears to give $K$ partial rewards (where $K$ is the action space), but baseline comparisons may be unfair as they lack oracle access. This makes the results less convincing.

### Questions
See weakness part.

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper proposes a new human-augmented method for solving contextual bandit problems. The idea is to use two types of human feedback to speed up identification of the best arm. The first type of feedback is “action recommendation”, where the human expert recommends a set of actions (arms) to take. Here, the algorithm selects a random action from the set to take. The second type is “reward manipulation”, which refers here to the human expert specifying a penalty that will be applied when the learner takes an action that is not in the expert’s recommended actions. Feedback is initiated by the learner, and a threshold on the entropy of the current policy is used to decide when to ask for feedback.

### Strengths
The paper tackles an important problem. Contextual bandit problems have many important applications, and the paper is right to recognise that human experts could help in solving these problems more quickly. The writing itself is good and the related work is extensive. The tasks considered in the experiments look to be realistically large and challenging.

### Weaknesses
The paper is in my view not sufficiently novel in its current form. The idea of collecting human feedback when uncertainty is high is a well-known heuristic (e.g. [A]).  I think a much larger contribution could have been achieved in one of two ways: (1) by proving some statistical guarantees, which I would expect is possible give the simplicity of the algorithm and of the model of the human, or (2) by following some of the more SOTA work in this field and achieving a more refined trade-off between the cost of human feedback (e.g. cognitive cost [B]) and its value.

Furthermore, the experiments leave a lot to be desired.
- The proposed method leverages a human expert, but there is no human subject study. Humans give feedback of varying levels of quality (both between and within subjects) with potential biases [C]. The effect this would have on the proposed method is unclear as this variability is not replicated in the simulation experiments (feedback is assumed to be of constant quality and unbiased).
- As we are discussing the addition of human feedback to an environmental reward here, I would expect to see an ablation that includes a “no feedback” setting, i.e. the standard contextual bandit setting.
- To understand the value a human can expert bring here, and how practical the proposed method is, I would want to see an experiments that measures how much feedback is needed to achieve a certain level of performance.

There are a number of issues with presentation. See also the questions below for things that were unclear in the text.
- Figure 2 lacks error bars. Subfigures showing performance of different algorithms on the same dataset have different scale y-axes, making comparison difficult.
- Section 4.4 and Figure 4 show the effect of various entropy thresholds, but what those thresholds are is never stated.
- Table 2 in the appendix is cut off at the bottom.
- Section 3.2.2 explains that for “reward manipulation” feedback, the expert given a penalty to be applied when a non recommended action is taken. However, this is not consistent with Algorithm 1, which shows the penalty being applied for any action.

### Questions
- On line 134, you assume reward is 0/1. This is a suitable assumption for multi-label classification problems, but seems needlessly restrictive for the proposed method. Could this assumption be loosened?
- You measure mean cumulative reward in various places, and figure 8 given an idea of how often expert feedback is elicited for various entropy thresholds. However, in order to understand whether the proposed method is practical, I would like have a better understanding of how much expert feedback is needed to achieve a certain level of mean reward. What does that trade-off look like?
- For the experiments with action recommendations, how many actions were recommended? What was the effect of recommending more actions?
- How was the quality of feedback parameter used within the experiments? Was it assumed to be known or latent? Were algorithms exposed to a single level of feedback, or could it change within an experiment? I ask because the RL algorithms performed quite well in your experiments, which suggests that they may have been able to adapt to the given level of feedback, even if it was not observable to them.

### Soundness
2

### Presentation
2

### Contribution
1

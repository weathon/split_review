# Influencing Humans to Conform to Preference Models for RLHF

- Decision: Reject
- Scores: 5, 6, 5, 5

## Abstract
Designing a reinforcement learning from human feedback (RLHF) algorithm for learning from preferences requires assuming a preference model, sometimes implicitly.  A preference model that poorly describes how humans generate preferences risks learning a poor approximation of the human’s unobservable reward function. In this paper, we conduct three human studies to assess whether one can influence the expression of real human preferences to more closely conform to a desired preference model. Importantly, our approach does not seek to alter the human's unobserved reward function. Rather, we change how humans use this reward function to generate preferences, such that they better match whatever preference model is assumed by a particular RLHF algorithm. We introduce three interventions: showing humans the quantities that underlie a preference model, which is normally unobservable information derived from the reward function; training people to follow a specific preference model; and modifying the preference elicitation question. All intervention types show significant effects, providing practical tools to improve preference data quality and the resultant alignment of learned reward functions.Overall we establish a novel research direction in model alignment: training humans and designing interfaces to increase human conformance with the assumptions of the algorithm that will learn from their input.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper focuses on reducing the gap between actual human behavior and the human models used in preference learning. While other work focuses on developing more complex human models, this submission focuses on changing human behavior to better conform to simple human models. The authors explore how to do this through a human study, focusing on three interventions. In the first intervention, they show annotators an explicit return or regret value for each partial trajectory in a comparison pair. In the second intervention, they train annotators to better estimate return or regret but then do not provide the actual return/regret values during annotation. In the third intervention, they simply change the language used to prompt the annotators. They find that the first two interventions lead to statistically significantly better agreement between human behavior and human models. The third also seems to increase agreement but is not statistically significant given the sample size.

### Strengths
The paper is generally quite well motivated and written. The math and experiments are clearly described. I am relatively familiar with this area and do not know of much other work which has focused on making human behavior more similar to human models rather than human models more similar to human behavior, so I think it is a novel direction. The experiments seem to be carefully designed and executed, and it seems helpful to the preference learning community to have well-grounded data on how well human models fit annotations.

### Weaknesses
The main weakness I see in the paper is that the first two proposed interventions do not actually seem to be applicable in practice. While the authors concede that the "privileged" setting is impractical, the second setting—"trained"—also seems to be impossible in practice. This is because the trained setting requires teaching people how to evaluate a particular aggregation of reward, which relies knowing the reward function in the first place; however, the entire point of preference learning is that the reward function is *unknown*. The third setting, "question," seems to be most applicable, but has the least convincing evidence.

In general, the authors argue that their interventions are focused on "training subjects to follow a preference model." However, it seems that to a large extent the authors are training subjects to follow a particular reward function—the privileged and trained experiments are both focused on helping annotators better estimate rewards. It would be more convincing that the authors are helping subjects "follow a preference model" if, for example, the subjects were trained to estimate return/regret with one reward function and tested with a different reward function. This would help disentangle the effects of simply learning more about the reward function and actually learning to follow one of the preference models.

Smaller issues/suggestions:
 * It would be helpful to include error bars in figures 5, 7, and 9.
 * There are a couple of improvements to the LaTeX math notation that could be made. For example, use `\text{loss}` instead of `loss` and `\text{regret}` instead of `regret`; use `\log` instead of `log`; and use `\mid` instead of `|`; use `\left` and `\right` with parentheses to make it clearer which parentheses match.
 * Line 345: "signficant" -> "significant"
 * Line 471: this sentence is confusing because it's referring to the experiments from Section 5.2. I think maybe it was meant to be replaced with links to the experiments in Section 5.3.

### Questions
* How could one actually implement the "trained" intervention in practice for an unknown reward function?
* How can we disentangle how much of the improvement in matching the human models is due to just learning the reward function better versus following the preference model?

### Soundness
2

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
This paper looks to test the idea that we may be able to influence people to behave more closely to target preference models. The motivation for this is twofold. (1) There remains a modelling gap in modelling human preferences, which makes learning underlying reward functions from those preferences harder and less accurate. This gap could be closed by improving said models, but — as this paper points out — it could equally be closed by making people behave more like the models we have now. (2) Even if perfect models of human preference existed, humans could still be influenced to behave like models on which inference is more tractable.

To this end, three interventions are proposed that could achieve this. Through three user studies on a grid world RL problem, it is tested for each intervention whether the intervention indeed influences people to give preferences that more closely align with a target preference model, and whether inference with the target model leads to more aligned inferred reward functions. The interventions are tested with two target preference models: one that assumes people prefer minimal regret behavior, and one that assumes people prefer maximal partial return behavior. The interventions are:
- “Privileged”, where the intervention consists of showing participants the partial return or regret of the pair of trajectories between which they must choose. This requires knowledge of the true reward function.
- “Trained”, where participants are trained through instruction to choose segments that maximise partial return or partial regret, before their preferences are elicited.
- “Question”, where how the text instruction that tells participants how to choose between the two trajectories is changed to better reflect partial return or regret comparisons.

Experimentally, the papers generally finds significant effects under all three interventions in terms of making people behave more like the target model, and in inferring a more aligned reward function.

### Strengths
I like the angle this paper takes very much. Human preference in settings such as the one considered here is very much an open problem. We only have limited understanding of how people value the options presented to them (see Knox et al. 2022) and limited understanding of how they would choose a most preferred option based on these values. With the (renewed) importance of preference learning, this is an important problem that remains unsolved in ML and even in cognitive science. The proposed solution of making people behave more like the simple preference models we have now is quite creative, and could go some way towards closing this gap, even if we must still recognise that people have inherent cognitive limitations that cannot be trained/influenced out.

The experiments are well-documented and the user study as described has been carried out to a level that is commensurate with what is expected at a top-level ML conference. The writing is clear and well-structured and the paper is easy to follow.

### Weaknesses
Primarily, I’m worried that the experiments carried out in the paper do not fully support the main claim of the paper. The stated goal is to test whether we can influence humans to follow a specific preference model. To test this, the authors check whether influencing someone towards a target preference model makes them behave more like that preference model compared to when they are not influenced (control condition). However, it is not established whether the interventions actually influence people to behave more like the target preference model as opposed to other preference models, or whether the intervention has solely influenced them to make better comparisons.

There seems to be some evidence of this in Figures 6 and 10, which show that  influencing participants to follow either one of the preference models leads to better reward inference with both, not only the targeted one. Furthermore, Figures 8 and 27, show that training people to follow a regret preference model is most effective for inferring their reward function, be that done with regret or partial return preference models. It seems to me then that although these interventions have a positive effect, this effect is not most specific to the target preference model.

In addition, the practical relevance of the proposed interventions is limited. Interventions in the “privileged” experiment are not practical because displaying true regret or true partial return is impossible without access to the unknown reward function (which the authors acknowledge). The intervention in the “trained” experiment is to train people to follow regret or partial return preferences. However, within the experiment presented here that training relies heavily on the true reward function (see questions). It is not clear how such training would work if the true reward function is not known. I see no practicality issues with the “question” experiment, but the effect size here is the most limited out of the three.

### Questions
Is training practical when the correct reward function is not known? In the experiment presented here, the true reward function was used in training, e.g. participants were corrected when they made wrong choices by saying something along the lines of “wrong, both items have equal score so far, but right option has higher possible score increase”. How would this training be implemented if the true reward function was not known?

For all three experiments, what was the mean Cross-Entropy Loss for the opposite preference model? For example, after a participant was trained to follow a partial return preference model, what was the likelihood of a regret preference model on that participant’s elicited answers?

For the question experiment, would participants have understood the difference between the question “which path has better immediate outcomes” and “which path reflects better decision-making”? The second questions seems ambiguous to me, considering the decision-making could be good in both the short or long term.

Section D.5 in the appendix suggests that people generally are better aligned with regret-based preference models. This is also in line with the work of Knox et al. 2022. Could this natural alignment towards regret-based preference have made training people to follow partial return preference less effective?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper explores methods to improve the quality of human feedback in reinforcement learning from human feedback (RLHF) by aligning human preference expressions with the preference model assumed by the RLHF algorithm. Poorly aligned preferences can lead to inaccurate approximations of a human's reward function. Through three human studies, the authors assess interventions to influence how humans express preferences without altering their underlying reward function. These interventions include displaying model-based preference quantities, training people to follow specific models, and rephrasing preference questions. All three interventions significantly improve preference alignment, introducing a novel direction in model alignment by adjusting human interaction to better match algorithmic assumptions.

### Strengths
Originality: Very original work - First one I've seen on aligning human preference expressions with the assumptions of the preference model, an interesting and out-of-the-box perspective.

Quality: Good variety of experiments to test the hypotheses, covering multiple different ways to influence human preference expressions.

Clarity: Very clear introduction, related work, description of tasks, and description of experimental interventions

Significance: Interesting and novel research direction which could lead to significant improvements in RLHF

### Weaknesses
Typos:
- Figure 5 caption: "the the"
- Line 381: "Priveleged"

I feel like the "% of partitions in which performance is near optimal" results are not very convincing to support the hypotheses presented.

PRIVILEGED EXPERIMENT
Figure 6: The difference between the P_regret and P_reward lines in both subplots is very minimal and does not hold for all number of partitions.

TRAINED EXPERIMENT
Figure 8: The P_regret trained preferences always lead to better performance -- this seems to indicate that the P_regret training paradigm leads to better understanding of the ground-truth reward function more than it supports Hypothesis 2.

QUESTION EXPERIMENT
The P_regret question does not seem to me to focus subjects on a segment's deviation from optimality. Perhaps something like "Which path is farthest from optimal?" would have been better
Figure 10: The difference between the P_regret and P_reward lines in both subplots is very minimal and does not hold for all number of partitions.

### Questions
Please address the weaknesses listed above.

### Soundness
2

### Presentation
2

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
The paper investigates methods to align human preferences with a specified preference model in RLHF by influencing how humans express preferences. This approach doesn't alter the underlying human reward function but instead modifies how preferences are generated to match an RLHF algorithm’s assumed model. Three interventions were tested across human studies: Privileged Experiment, Trained Experiment, and Question Experiment. The paper claims that each method effectively improved alignment with the target model.

### Strengths
- The paper is generally well-written and clear.
- The experimental setup is described in detail, providing clarity on the methodology.
- Thorough analysis of the experiments strengthens the overall findings.

### Weaknesses
 - RLHF’s value in aligning language models is widely recognized, but the paper’s focus on a constrained grid-world delivery domain may limit generalization to language-based agents.
    * While the proposed interventions show promise, it’s unclear how effectively these ideas could extend to more complex language-driven settings. Specifically, the discrete action space and limited state space of the grid-world environment do not capture the complexities of natural language, where actions and states are high-dimensional and continuous. The mapping from human preferences to a reward function in such a simplified environment may not translate well to the nuances of language understanding and generation.
- The environment and experiment setting closely follow prior work by Knox et al., meaning the primary contribution arises from the three interventions aimed at influencing human decision-making: the Privileged Experiment, Trained Experiment, and Question Experiment. However, concerns remain about both the novelty and practicality of these experiments:
    * The Trained Experiment, which involves training participants before they label data, is resource-intensive, with significant demands on time and cost, as noted by the authors. This raises concerns about the scalability of this approach for real-world applications where large amounts of human preference data are needed. The cost of training participants may outweigh the benefits, especially if the gains in alignment are marginal.
    * The Question Experiment has only a marginal effect, with no significant impact observed for aligning preferences with the regret model, which may limit its utility in practice. The lack of a strong effect in the Question Experiment suggests that simply prompting users with questions may not be sufficient to significantly alter their preference expression, especially when compared to the more resource-intensive Trained Experiment. This calls into question the practical value of this intervention.

### Questions
- Does influencing preferences toward a specific model potentially introduce bias in scenarios where the model may not be the best fit for human objectives?
- In the Privileged Experiment, given that users see reward information directly, is there a risk they might over-rely on this data, reducing their engagement with the task?
- Could the interventions used in the study generalize to more complex RLHF tasks (e.g., continuous environments) where users make dynamic, long-term decisions?

### Soundness
3

### Presentation
4

### Contribution
2

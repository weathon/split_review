# Truthfulness Without Supervision: Model Evaluation Using Peer Prediction

- Decision: Reject
- Scores: 5, 6, 3

## Abstract
Current evaluation methods for language models rely on supervision, but trusted supervision for difficult tasks is often unavailable, especially for superhuman models. In these cases, models have been demonstrated to exploit evaluation schemes built on such imperfect supervision, leading to deceptive evaluation results. 
However, underutilized in the context of model evaluation, a wealth of mechanism design research focuses on game-theoretic *incentive compatibility* - eliciting honest and informative answers without trusted supervision. 
Drawing from this literature, we introduce the peer prediction method for model evaluation. It tells apart honest and informative answers from deceptive and uninformative ones, using a metric based on mutual predictability and without requiring ground truth labels. 
We demonstrate the method's effectiveness and resistance to deception, with both theoretical guarantees and comprehensive empirical validation on up to 405B-parameter models.
In contrast to LLM-as-a-Judge which requires strong and trusted judges, we discover an inverse scaling property in peer prediction, where, surprisingly, resistance to deception is *strengthened* as the capability gap between the jury and participants *widens*, enabling reliable evaluation of strong models without trusted supervision.
In particular, LLM-as-a-Judge evaluations become worse than random guesses when facing deceptive models 5-20$\times$ its size, while peer prediction thrives when such gaps are large, including in cases with over 100$\times$ size difference.
Looking forward, we view this work as a step towards game-theoretic resistance to model deception in alignment and evaluation.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
When discussing evaluation methods for language models, the strong reliance on supervision and the unavailability of reliable supervision on hard tasks, particularly in scalable oversight, lead to the exploration of “evaluation methods without reliable supervision”. Therefore, this paper proposes the “peer prediction method”, which leverages “game-theoretic incentive compatibility” from mechanism design literature, to perform resistance to deception without trusted supervision.

This paper first clarifies the importance of exploring evaluation methods, explains their inspiration for leveraging “game-theoretic incentive compatibility”, and then highlights the merits of their “peer prediction method”. The “peer prediction method” applies several models as “participants” and some separate agents as “jurors”, then evaluates participants’ answers to held-out questions by assessing their ability to help jurors predict others' responses, using peer answers as targets instead of ground-truth labels. In the experiment section, the paper applied a dataset containing questions spanning across tremendous domains to test the effectiveness and resistance to deception, including a finding of “Inverse Scaling Properties” and other ablation studies on scaling properties.

### Strengths
This paper proposes a novel method that does not need reliable supervision. It is resistant to deception and has a strong scaling performance.

This paper priorly takes “game-theoretic incentive compatibility” into consideration and provides mathematical proof for their theorem

### Weaknesses
1. The scenario of exploring the topic of “evaluate models without supervision” is not well defined. According to this paper, “lack of reliable supervision” occurs in “scalable oversight”, which is well explained. Therefore, it is reasonable to discuss this scenario but only limited to it. For other scenarios, “aiming to ensure that they are safe, reliable, and beneficial” (Line 57) does not necessarily lead to the motivation to “evaluate models without supervision”. The claim of “trusted supervision for difficult tasks is often unavailable” (Line 12) in the abstract does make sense but lacks sufficient and concrete examples (only “scalable oversight” is mentioned). Further elaboration and explanation of “under what circumstances when trusted supervision is unavailable” should be provided.

2. Some of the conclusions are based on strong assumptions. Take Line 270 to Line 277 as an example, it is reasonable to have the conclusion of “peer prediction method is incentive compatible”, but the conclusion of “In particular, models are incentivised to converge upon honest and informative policies, if either (I) they are trained on the peer prediction scores as reward signals, or (II) they perform inference-time reasoning to maximize the evaluation scores” is likely to lead based on a strong assumption that efficient benign answers are required. If tremendous malicious answers are proposed, according to the “incentive capability”, the models may be incentivized to converge upon deceptive results.

3. The methodology strongly relies on the combination of several LMs. Considering the peer prediction method takes peer answers as targets instead of ground-truth labels, the results of the models are interactional. That means if one of the models is changed, the performance of other models will comparatively be changed. The provided experiments lack examples of different combinations of LMs as participants.

4. This method will be really resource-consuming when considering superhuman models. Plus,” distinguish better models from worse ones” is not a good evaluation metric to me as it is a relative result instead of an absolute one, which means it will have more limitations. For example, you need to find appropriate models for comparison when testing

### Questions
1. Could you please provide further explanation for what is mentioned in weakness 1 and weakness 2?

2. According to weakness 3, are you available to provide more experiments considering different combinations of the participant's model?

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors propose "peer prediction" as a novel method to evaluate LLMs without requiring trusted supervision or ground truth labels. The method works by measuring how well one model's answers help predict another model's answers through a jury system, with theoretical guarantees that honest and informative answers are optimal. Through theoretical analysis and experiments the authors demonstrate three key findings: (1) the method effectively distinguishes model capabilities across diverse domains, (2) it exhibits an inverse scaling property where resistance to deception actually increases as the capability gap between jury and participants grows larger, enabling reliable evaluation of superhuman models, and (3) the method's resistance to deception improves with larger participant and jury populations.

### Strengths
- The idea of exploring mechanisms that exhibit game-theoretic incentive compatibility in model evaluation is pretty interesting and sufficiently new.
- The problem is important and well-motivated.
- Section 3 is well-written and from what I was able to check technically correct.

### Weaknesses
I don't think the paper has any major technical issue, but it could be improved in terms of clarity for people not familiar with the mechanism design literature. Maybe add a background section in the appendix. The figures can also be improved by making the font larger and writing subfigure captions. Finally, I would also like to point that being more technical when defining terms like "being more truthful", "superhuman", is extremely helpful. I was able to understand the paper regardless and I understand the use of these non-technical terms has increased in this literature, but I recommend to be more precise in the final version of the work if possible.

### Questions
- Can you explain the practical implications of assumption 1? I think the paper lacks a discussion about practical implication of all the assumptions in Sec 3.
- I had a hard time understanding Fig 3, can you expand on the details of each subfigure?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes a peer prediction mechanism for evaluating LLMs: A Model A's answers are scored by how much they help a "juror" J predict other model B's answers. The authors prove that assuming a joint prior over models' "real" answers (or a known distribution over participant's priors with some regularity conditions), reporting the "real" answers is a bayesian nash equilbrium. Experiments are conducted using a variety of different LLMs of different sizes, and on multiple different LLM benchmarks. LLMs misrepresenting their "real" answer are modeled by a prompt that tells models to provide convincing false answers.

### Strengths
- Exploring methods for using LLMs to aid in the evaluation of LLMs is a very timely topic 
- The experiments cover a wide range of different tasks, as well as different models. 
- Judging from my limited expertise in peer prediction, Theorem 2 could be of independent theoretical interest (if it is indeed novel as claimed in the appendix).

### Weaknesses
 - The proposed approach seems to suffer from a lot of issues that are common for peer prediction mechanisms: 
    - The assumption of shared priors does not appear to be very realistic, and I am not convinced the generalization from Theorem 2 helps much, as it appears to require full knowledge of the distribution over priors. 
    - Honesty seems unlikely to be the only bayesian nash equilibrium. Unlike for other peer prediction mechanisms, collusion might not even be necessary for deviating from honesty in this case: If I understand correctly, a witness would obtain perfect reward if it encoded the defendant's answers in its own (in a way the juror is able to decode). However, an answer that encodes the correct answer can be very different from the correct answer in many cases. 
- If I understand the experimental setup correctly, it appears to provide an unfair advantage of the proposed method over LLM-as-a-Judge, as despite the weak judge, the peer prediction mechanism has access to strong peer models. If such models are available, it seems misleading to have LLM-as-a-Judge use the weak judge model rather than one of the stronger peer models. 
    - Some additional information on why LLM-as-a-judge was implemented the way it is (for example, no few-shot prompting) would also be helpful to better assess, whether the comparison is fair or an overly weak baseline [1] was chosen. 
 - I am worried that the inverse scaling experiment might be confounded by a similar issue: The improvements could be caused by the increasing capability of the peers rather than the increasing capability of the evaluated model. An ablation in which the peer models are fixed to the juror model's size would be useful here. 
- The experiments on incentive compatibility seem to only employ a single, non-adaptive deceptive "attack". This is insufficient to establish that the mechanism works in practice [2], especially for strong, potentially superhuman, models. 
    - Considering different approaches to deception and analyzing them in more detail would also help to ensure that the observed inverse scaling is not just an artifact of the specific deceptive attack: One potential explantation for the inverse scaling would be that small models rarely understand the instruction to be deceptive and thus simply behave very similar to the honest model, making them impossible to detect. 
- The paper at times makes very strong claims such as "the method [is] applicable to superhuman models" and "enabling reliable evaluation of superhuman models without trusted supervision." that seem too strong, even disregarding the potential issues with the experiments. 

Nitpicks: 
- The naming of the entities involved in the game is a bit confusing: Why is the Witness receiving the punishment rather than the defendant? 
- The paragraph "Scaling Properties with Jury Population Size" seems to lack some details, such as what Regression the R^2 refers to. 
- The font used for probability distributions is hard to read (D alone would be fine, but P,D and Q(?) all look pretty similar 
-  It might be useful to provide a few basic details on how the juror model is implenented in the main text rather than only in the appendix.
- I would find the statement of theorem 1 a bit more clear if the last condition on the game's scores was stated in the beggining rather than as an if-clause in the very end.  
- Figure 1 would be easier to read with subcaptions indicating the differences between subfigures. Also, the y-axis seems to show the negative of punishment for deception (otherwise, higher rather than lower would be better) 

### Questions
- Do the results shown in figure 1 look qualitatively similar when only multiple choice or only open-ended tasks are considered?
- The numbers in the experiment from section 3 are difficult to interpret without more context: For many tasks, the gap between the 70B model and the 405B one seem small, and the 70B model even performs better in about 20% of tasks. How do these gaps relate to gaps in the models' performance on these tasks according to the ground truth (as well as according to model-as-a-judge)? 
- Could you add an ablation using different models rather than instances of the same model as participants? That would be useful to rule out the following explanation for inverse scaling:
    - With its very limited training data (3 few-shot examples), the best the juror can do for honest witnesses is to predict that the defendant's answer is similar to the witness's. Meanwhile for dishonest models, it can only guess. Now assume that witness and defendant are either the same model, or a honest and a deceptive version of the same model. Then, it will be very easy to distinguish the honest and lying witness if the honest model's answers are deterministic, but harder if they have very high variance. The observed inverse scaling would now follow from the plausible assumption that larger models produce more similar answers with repeated sampling than smaller models do. However, this kind of inverse scaling would cease, as soon as models are large enough to be generally self-consistent. 
- It looks like the surplus actually increases in $\alpha$. Why are no values of $\alpha$ larger than one included? 
- What are the key elements of the proofs that distinguish them from the ones in in Schoenebeck & Yu (2023)? 
- Regarding inverse scaling, it is currently difficult to read how the method scales with juror quality. Could you add a plot with the judge size rather than the evaluated model's size varying on the x-axis? 
- In theorem 2, why is there a probability 1-$\delta$ if the equilibrium is supposed to be ex-ante? Does that mean that there are (rare) agents that have an incentive to deviate ex-ante?

### Soundness
1

### Presentation
3

### Contribution
2

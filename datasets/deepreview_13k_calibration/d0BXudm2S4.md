# Natural Counterfactuals With Necessary Backtracking

- Decision: Reject
- Avg Score: 5.33
- Scores: 5, 6, 5

## Abstract
Counterfactual reasoning is pivotal in human cognition and especially important for providing explanations and making decisions. While Judea Pearl's influential approach is theoretically elegant, its generation of a counterfactual scenario often requires too much deviation from the observed scenarios to be feasible, as we show using simple examples. To mitigate this difficulty, we propose a framework of \emph{natural counterfactuals} and a method for generating counterfactuals that are more feasible with respect to the actual data distribution. Our methodology incorporates a certain amount of backtracking when needed, allowing changes in causally preceding variables to minimize deviations from realistic scenarios. Specifically, we introduce a novel optimization framework that permits but also controls the extent of backtracking with a ``naturalness'' criterion. Empirical experiments demonstrate the effectiveness of our method.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors provide an alternative framework for reasoning about counterfactuals that is claimed to provide more natural results than the prevailing framework.

### Strengths
The paper is well-written.

### Weaknesses
The example cited in the introduction does not seem to differentiate between: (1) a reasonable approach to reasoning about an "actual cause" (an event that is a cause of the outcome in this specific case); and (2) what the authors refer to as "constructive" reasoning (identifying plausible alternative events that could have changed the outcome). These are different goals, and both are useful. The former would be useful to identify causal chains, while the second is useful to determine what, in that causal chain, would have been a reasonable point of intervention to change the outcome.  This doesn't invalidate the results of the paper, but it casts the results in a different light. The approach outlined in the paper is not a replacement for the existing theory, but instead is an elaboration of it to allow for a wider range of types of reasoning.

It seems doubtful that "naturalness" can be defined in a way that is unambiguous and will be universally agreed upon. The specific "mechanisms" of intervention are generally external to the SCM. That is, the *way that an intervention changes the model* can be represented in an SCM (e.g., an atomic intervention substitutes for the structural function of the variable intervened upon), but the *manner in which that intervention achieves that result* is not represented in the SCM. Thus, the SCM itself does not appear to contain the information necessary to decide "naturalness". For example, the event "Tom is restrained from hitting Jerry" may be unlikely (unnatural) in a bus, but it would be entirely natural in a car. Specifically, suppose that Tom and Jerry are riding in a car, Tom is sitting the in the back seat, and Jerry is in the front seat. Tom could strike Jerry in the event of a sudden stop, but he wouldn't if he was wearing a safety belt.  Yes, it is possible that "Wearing a seat belt" could be represented in the SCM, but not all such "intervention variables" would be. This is a larger issue about "what SCMs are good for." They cannot represent everything, so what should we expect them to be able to reason about? The authors propose that "naturalness" is one of those things, but this increases the number of things that the variables in a given SCM should represent. Furthermore, the proposed notion of naturalness seems to conflate the *likelihood of an event* with the *plausibility of an intervention*. An intervention might be very unlikely in a given context, but still be a perfectly plausible way to achieve a counterfactual outcome.

The paper would be improved by a more intuitive explanation of the simulation experiments and why they should provide readers with confidence that the approach outlined by the authors is valid and useful. It seems counter-intuitive that such a claim could be supported by simulation and the current text does little to explain the underlying logic. The experiments in Section 5 seem more like demonstrations and less like useful tests that, if the proposed approach did not work well, would have shown that. That is, they are not particular severe tests of the proposed approach.

### Questions
What is the underlying logic behind the experiments in Section 5? 

Why do they provide convincing evidence that we should expect the proposed methods to work well in nearly all cases?

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
1: You are unable to assess this paper and have alerted the ACs to seek an opinion from different reviewers.

### Summary
The paper proposes a new framework called "natural counterfactuals" for generating counterfactual explanations, aimed at overcoming limitations in Judea Pearl's traditional approach.  The new methodology modifies the standard nonbacktracking requirement in counterfactual reasoning. It permits alterations in variables that are causally prior to the target variables in a counterfactual scenario, but only when these changes are necessary to meet a "naturalness" criterion. To balance this flexibility, an optimization framework is introduced to minimize the extent of such backtracking. Through experiments, the paper demonstrates that this new approach is more effective in generating practical, realistic counterfactual explanations compared to the standard Pearlian method.

### Strengths
The paper provides a very clear rationale for why traditional "nonbacktracking" counterfactuals can be impractical, laying out the context and need for an alternative approach. The introduction of "natural counterfactuals" is a new take on counterfactual reasoning, addressing limitations in the standard Pearlian framework.  One of the primary goals of the paper is to produce actionable insights which would have direct implications. They formulate the problem of generating natural counterfactuals as a simple optimization problem.
The paper provides empirical results based on both simulated and real-world data, thereby demonstrating the efficacy and applicability of their methodology.

### Weaknesses
Due to my limited expertise in this area of research, I have not delved deeply into the core aspects of the paper. My question is high-level.
How does your work differ from 'Backtracking Counterfactuals'? https://arxiv.org/abs/2211.00472".

### Questions
NA

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposed a method called "natural counterfactuals" that is supposed to generate more plausible interventions compared to other methods such as the standard Pearlian approach.

### Strengths
- The proposed natural counterfactuals pose a novel and interesting approach compared to existing methods
- The paper is well written and structured

### Weaknesses
 - The authors claim that their proposed method yields more plausible interventions. However, I can not see how this claim is evaluated in the case studies. Am I missing smth.?
- Knowledge about the causal graph looks like a strong assumption to me, but I know that this is assumption is quite common the causality domain. However, I miss a little bit the relation to machine learning -- i.e. how exactly this might be applied to arbitrary machine learning systems. This is somehow mentioned in Appendix D, but I was wondering whether it might be beneficial, in order to make the paper more accessible to a larger community, to elaborate more on this in the main paper.

Minor:
- Broken reference in Section 2 second line?
- Sometimes the authors write "non-backtracking" and sometimes "nonbacktracking" -- I am not a native speaker but the first one looks more correct to me
- V-SCM Reference in A.2 on page 12 is broken?

### Questions
See Weaknesses

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

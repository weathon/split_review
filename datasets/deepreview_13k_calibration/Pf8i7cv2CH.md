# Sample Efficient Alignment for LLMs

- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 6, 6, 3

## Abstract
We study methods for efficiently aligning large language models (LLMs) with human preferences given budgeted online feedback. We first formulate the LLM alignment problem in the frame of contextual dueling bandits. This formulation, subsuming recent paradigms such as online RLHF and online DPO, inherently quests for sample-efficient algorithms that incorporate \textit{online active exploration}. Leveraging insights from bandit theory, we introduce a unified algorithm based on {\textbf{Thompson sampling}} and highlight its applications in two distinct LLM alignment scenarios. The practical agent that efficiently implements this algorithm, named \sea~(\textbf{S}ample-\textbf{E}fficient \textbf{A}lignment), is empirically validated through extensive experiments across three model scales (1B, 2.8B, 6.9B) and three preference learning algorithms (DPO, IPO, SLiC). The results demonstrate that \sea~achieves highly sample-efficient alignment with oracle's preferences, outperforming recent active exploration methods for LLMs. Additionally, we release the implementation of \sea~together with an efficient codebase designed for \textbf{\underline{o}}nline \textbf{\underline{a}}lignmen\textbf{\underline{t}} of LLMs, aiming to accelerate future research in this field.%\looseness=-1

\vspace{0

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper considers the problem of aligning LLMs to humans via online interaction and in a sample efficient manner that minimizes the overall human annotations consumed. It proposes a practical algorithm that can be implemented and using the tldr dataset shows that it can achieve extremely high win-rates when compared against the baseline alignment algorithm.

### Strengths
+ The paper builds upon the direction of aligning LLMs that considers the epistemic uncertainty of the reward function and utilizing the variance to guide the model to collect preference data in directions that maximally obtains information.
+ The algorithm is sound and theoretically solid. They build upon well performing methods for uncertainty estimates using the ensemble reward model method.
+ The results shown are promising (although see weakness for caveats).

### Weaknesses
 - The main weakenss of this paper is the lack of siginificant experimentation. The paper only considers the summarization task with the tldr dataset. It does not consider more diversity in tasks/datasets and does not utilize some of the most common tasks in the LLM literature (e.g., reasoning, code, general knowledge). Even within summarization, it does not consider > 1 datasets. Improvements in one dataset is typically very limiting.

### Questions
- Do you have results that can showcase this method on a variety of tasks and many different datasets? How generalizable is this method (in terms of how well it works)?

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
2

### Summary
This paper studies the online alignment for LLMs. It formulates the LLM alignment as a contextual dueling bandit problem. It proposes a Thompson sampling-like algorithm for both the regret minimization and best arm identification setting. For the challenge encountered when implementing this algorithm including the model constraints, the intractable operation to sample a posterior and argmax action, the paper proposes corresponding solutions to enable real-world application. Finally, the authors build a learning system for studying methods in online LLM alignment and compare the proposed method with available baselines in different scale levels of experiments. The proposed method shows superior sample efficiency compared with baselines.

### Strengths
1.	The paper studies the LLM alignment problem from an online view. It is reasonable to formulate the problem as a contextual dueling bandit problem. 
2.	The paper is inspired by the classic Thompson sampling algorithm to actively explore the preference function and proposes a corresponding version suitable for real-world application.
3.	The paper builds a learning system for studying methods in online LLM alignment. This provides efficient tools for the community on this research line.

### Weaknesses
1.	In Line 383, the authors claim they omit a baseline SELM since it shares a very similar algorithmic design as XPO. This is generally not an acceptable reason for excluding a baseline comparison.

### Questions
Please see the last part.

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
4

### Summary
This paper considers explorations by approximate TS in LLM alignment.

### Strengths
This paper is nicely written and well-executed. The details are well-presented.

### Weaknesses
This paper is a bit incremental and the idea is well expected. The contextual bandit formulation is well-known and the implementation of TS using ensemble is pretty straightforward.  

There are multiple key questions this paper fails to answer:

1. Why ensemble on the top of DPO makes sense and how good the uncertainty estimation is? This is not a standard supervise learning problem. This paper lacks a way to directly measure it. I do not think ensemble + X can quantify uncertainty in every problem.  

2. The reward model is too small (0.4B) and the base model Pythia family is outdated such that the empirical result may become useless in a practical setting. It is very common that the benefit of active exploration could disappear when the base model and reward model become much stronger. 

3. The baseline number is not comparable with other literatures since the author uses its own oracle reward model. There are tons of implementation details that could be hidden for other baselines. I think it would be good to have an apple-to-apple comparison with the same setting in the original DPO paper.

### Questions
see above.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper frames the problem of aligning LLMs with pairwise preferences as a contextual dueling bandit problem. The authors propose a method that adapts a well-know & effective bandit algorithm, Thompson sampling (TS), to LLMs. This is not trivial, because TS requires maintaining and sampling from a belief over reward functions. To address this, the authors provide tractable approximations. They evaluate their proposed approach empirically on LLMs of various sizes, and provide comparisons to related work.

### Strengths
- The contextual dueling perspective is interesting, insightful, and to the best of my knowledge, new.
- The paper does a good job of covering the most relevant related literature, and how it relates to the proposed approach.
- The description is very limited with no details in the supplementary material, but it is possible that the testbed they develop to evaluate different approaches is a valuable contribution in its own right

### Weaknesses
 - The writing could be improved significantly; parts of the paper are unclear, imprecise, and many details are omitted and should at least be present in the supplementary materials. A non-exhaustive list of examples:
    - line 144: "based on a binary stochastic feedback $z$" -> z is never referred to anywhere outside of this line as far as I see
    - line 196: "offline RL" -> I think the authors might be conflating offline RL with offline preference collection. RLHF typically uses online RL. PPO is an online algorithm.
    - I struggle to make sense of Figure 3, for example I fail to understand how (d) is meant to differ from (b).
- The posterior approximation scheme (Eq. 9) is not well motivated. I can see it is computationally attractive, but why do we believe this is a reasonable way to approximate the posterior? A cursory glance at the papers mentioned around Eq. 9 did not help. Since this is one of the central components of the proposed approach, I would expect a more rigorous justification here.
- The experiments are comprehensive, but I struggle to take them at face value. Unfortunately, few details are provided, neither in the main text, nor in the supplementary materials.
    - There are design decisions involved in setting up baselines, and these are not discussed.
    - I can't reconcile any of the curves in Figure 6 with the curves in Figure 5.
- Some of the metrics are problematic, as I see it. The "online win rate" (line 387) would make a model that deliberately samples poor responses look great.

### Questions
Concretely, in what ways does SEA differ from APL? How do you explain the large increase in sample efficiency?

### Soundness
2

### Presentation
2

### Contribution
2

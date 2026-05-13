# Pareto-Optimal Learning from Preferences with Hidden Context

- Decision: Reject
- Scores: 5, 5, 5, 6

## Abstract
Ensuring AI models align with human values is essential for their safety and functionality. Reinforcement learning from human feedback (RLHF) uses human preferences to achieve this alignment. However, preferences sourced from diverse populations can result in point estimates of human values that may be sub-optimal or unfair to specific groups. We propose Pareto Optimal Preference Learning (POPL), which frames discrepant group preferences as objectives with potential trade-offs, aiming for policies that are Pareto-optimal on the preference dataset. POPL utilizes Lexicase selection, an iterative process to select diverse and Pareto-optimal solutions. Our empirical evaluations demonstrate that POPL surpasses baseline methods in learning sets of reward functions, effectively catering to distinct groups without access to group numbers or membership labels. Furthermore, we illustrate that POPL can serve as a foundation for techniques optimizing specific notions of group fairness, ensuring inclusive and equitable AI model alignment.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces a reinforcement learning from human feedback with hidden context (RLHF-HC) framework called Pareto optimal preference learning (POPL). While marginalized distributional preference learning (MDPL) marginalizes $u(s\vert z)$ over the hidden context variable $z$ to produce a distribution $u(s)$ for each state $s\in\mathcal{S}$, POPL preserves the full conditional distributions. By leveraging these conditional probabilities, POPL can effectively capture Pareto optimal reward functions.

### Strengths
POPL can capture the Pareto optimal reward functions.

### Weaknesses
- The validity of the proposed algorithm is not theoretically explained.
- The scalability of the proposed algorithm remains uncertain.
- There is no way to determine the dimensionality of the underlying reward functions or the number of Pareto optimal policies.

### Questions
I am unsure if I fully understand the paper. If I have any misunderstandings, please let me know. I would be happy to receive clarification.

1. As I understand it, there is no learning in Algorithm 1, which represents one step of POPL. In my understanding, it solely relies on the random initialization of hypotheses and the selection of good hypotheses. With a large number of trials, it might eventually find good policy hypotheses, but I wonder if this method is truly practical.
2. In general, there are many policies that passes exactly the same preference subsets. However, Algorithm 1 only checks whether the candidates pass at least on preference or not. Then, how to determine a Pareto-optimal policy among these policies?
3. In Algorithm 1, if we use POPL to learn a set of reward functions, how can we specify the dimensionality of these reward functions and learn them from the given demonstrations?
4. Compared to the previous works, such as preference-driven MORL [1] or multi-objective alignment in LLM [2], what is the main difference and advantage of POPL?
5. I cannot understand the left side of Figure 2 (titled “MDPLs”). In this case, what does z indicate?

### References

[1] Basaklar, Toygun, Suat Gumussoy, and Umit Y. Ogras. "Pd-morl: Preference-driven multi-objective reinforcement learning algorithm." ICLR 2023.

[2] Yang, Rui, et al. "Rewards-in-context: Multi-objective alignment of foundation models with dynamic preference adjustment." arXiv preprint arXiv:2402.10207 (2024).

### Soundness
2

### Presentation
1

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
This work concentrates on the issue that human feedback data might involve noises caused by hidden information. It proposes a method named POPL that aims to learn a Pareto-optimal policy. POPL uses lexicase selection and conducts experiments on different tasks.

### Strengths
1. This work concentrates on an import problem that human feedback involves hidden information. The Pareto-optimal is indeed one possible solution.

2. Experiments on different tasks are given.

### Weaknesses
1. I found the presentation for the method is quite hard for me to understand. Lexicase selection, as key idea of the method, is not introduced clearly. I am not clear about how this selection method is conducted. Also, I think a figure for process might be better for readers to understand.

2. Similarly, I found that many concepts are used without a clear explanation. For example, I am not clear what "hypotheses" refers to as it first shows in Sec. 6.1 and also in Alg. 1. Also, as MDPL is mentioned, this formal calculation for this method is not give. I cannot under stand the illustration of Fig.3.

3. Further, if more intuition about the method is provided, it might be better for readers to understand this method.

4. Since this method concentrates on the RLHF alignment process, I am curious about the comparison between POPL and more RLHF methods like DPO. Also, the detailed information for the standard RLHF is not given.

### Questions
See the weakness part above.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
POPL enhances alignment by addressing diverse human preferences as multiple objectives, achieving solutions that are Pareto-optimal and fair across groups. It uses lexicase selection to find policies that respect varied preferences across. Empirical results show POPL’s effectiveness in aligning AI to human values safely and equitably across applications like robotics and language models.

### Strengths
- This paper provide a novel way to deal with the heterogenity among different sourses
- Various experiments under different settings are conducted to evaluate the performance

### Weaknesses
- Noations and concepts are sometimes not well-defined. For instance, $\sigma$ first occur in Section 3 without any definitions. I would suggest the authors to more clearly defined notations.
- The presentation of experiment results is quite unclear. For example, Figure 3(b) is really chaotic and I can hardly tell the information here.
- Lack of comparision with other methods. From my interpretation, many methods are proposed to solve the similar issue, e,g., Nash learning for RLHF and general preference framework. The methods should be more properly evaluated and compared.

### Questions
-  What's the formal definition of $\sigma$, is it always a $(s,a)$ pair?
- Could authors provides more clearer highlight of the technical contributions?
- For me, even though the definitions are provided, the concept is still confused. Could authors gives the mathemitical definitions of concepts and theorems in Section 5.1, e.g., optimality?

### Soundness
3

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
4

### Summary
The paper tries to solve the problem of learning from complex human preference by first formulating it as the problem of preference learning with hidden context, and then relying on the framework and techniques of multi-objective optimization. The Pareto Optimal Preference Learning (POPL) method, based on the lexicase selection algorithm, is proposed to efficiently learn and generate diverse rewards and policies. The extensive and diverse experiments are conducted to illustrate the efficiency and applicability of the method.

### Strengths
1. The problems of previous methods are clarified with a simple yet illustrative example.
2. The intuitions and theoretical formulations in Section 5.1 are interesting and may be useful for future research.
3. Experiments are diverse and persuasive, ranging from analytic environments to language model experiments, which show the proposed method’s efficiency and applicability.

### Weaknesses
1. It would be better to concisely introduce the theory proposed in Section 4 in the introduction Section.
2. Paragraph headings in Section 2 can make them more clear.
3. In line 147, the comma ahead of ‘However’ should be a full stop.
4. The process of lexicase selection for preference learning in Section 5.2 can be made more clear with figures, formulas, or diagrams.

### Questions
1. By formulating the RLHF-HC problem as a multi-objective problem, how will the method deal with (non-)**transitivity** of real-world human preference ? As this could be a problem for real-world human feedback (See ,e.g., section 7.3 of [1]).
2. ‘Theory Foundation’ in the title of Section 4 seems to be missing, or it has been formulated in Section 5 ? A re-organization may be needed.
3. Why the probability of segments in Definition 1 does not include the distributions of the states, such as $\prod_{(s,a)\in\sigma}\pi(a|s)d(s)$ ?
4. In line 258, is the word ‘illicit’ a typo ? It may be ‘elicit’.
5. In the proofs in Appendix B, what does $\pi_z$ refer to ? Is it just $\pi_z^*$ ?

### Soundness
3

### Presentation
3

### Contribution
3

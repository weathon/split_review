# Human Expertise Really Matters!  Mitigating Unfair Utility Induced by Heterogenous Human Expertise in  AI-assisted Decision-Making

- Decision: Reject
- Avg Score: 5.75
- Scores: 6, 6, 6, 5

## Abstract
AI-assisted decision-making often involves an AI model providing  confidence, which helps human decision-makers integrate these with their own confidence to make higher-utility final decisions.
However, when human decision-makers are heterogeneous in their expertise, existing AI-assisted decision-making may fail to provide fair utility across them. Such unfairness raises concerns about social welfare among diverse human decision-makers due to inequities in access to equally effective AI assistance, which may reduce their willingness and trust to engage with AI systems. In this work, we investigate how to calibrate  AI confidence to provide fair utility for human decision-makers. 
We first demonstrate that rational decision-makers with heterogeneous expertise are unlikely to obtain fair decision utility from existing AI confidence calibrations. We propose a novel confidence calibration criterion,  *inter-group-alignment*, which synergizes with human-alignment to jointly determine the upper bound of utility disparity across  human decision-maker groups.  Building on this foundation, we propose a new fairness-aware confidence calibration method, *group-level multicalibration*, which ensures a sufficient condition for achieving both inter-group-alignment and human-alignment. 
We validate our theoretical findings through extensive experiments on four real-world multimodal tasks. The results indicate that our calibrated AI confidence facilitates fairer utility, concurrently enhancing overall utility.  *The implementation code is available at*  
 [https://anonymous.4open.science/r/iclr4103](https://anonymous.4open.science/r/iclr4103).

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The work investigates the role of calibration in AI-assisted decision-making, focusing on how the alignment between AI confidence scores and accuracy impacts human decisions when human decisions vary across groups. The authors analytically show that, when different groups of users have different decision policies, using the same AI confidence alignment for both groups cannot guarantee the same "utility" across groups. They also empirically show that multicalibration of AI confidence with respect to each group improves overall calibration of the decision policy.

### Strengths
The scope of the paper is clear and the paper itself tackles an important and timely problem, definitely relevant to the ICLR community. The paper also goes deep into the details about why multicalibration --as done by previous work-- can fail. The paper also dives into the details through both analytical and empirical analyses, and the results were interesting (although more explanations about them would be helpful).

### Weaknesses
Novelty: The novelty of the paper is one of the main weaknesses. The authors propose to multicalibrate the AI confidence separately for each subgroup of users; if my understanding is correct, this could already be done by previous work just by considering the subgroup information as a feature. This is done in standard multicalibration in tabular data problems. In addition, the paper is very similar to the recent work of Benz and Rodriguez (2023). Algorithm, experiments, etc look similar. The main novelty in this work is that the authors show that the AI confidence function will not be calibrated when decision policies vary across groups and thus recommend running the multicalibration algorithm by group. Is this correct?

Clarity: Presentation can be improved. For example, in section 3 multiple definitions and theorems are presented without much descriptions or examples. In many parts, the paper is very dense and notation is heavy. The expectation is never defined, as well as other mathematical terms are not clearly explained. Some examples would help the reader. What is the explanation behind the upper bound in Theorem 3.6? Can the authors provide an intuition behind this result?

Typos: Lines 126-127, the policy is not binary. Line 192: calibration -> calibrated. There are others around the manuscript. 

I recommend adding some explanations in the code to help the reviewer or the interested reader understand what’s happening. As a reviewer, I found it really hard to navigate it.

### Questions
Questions are listed above. One additional question: The authors focus on the case where each individual belongs to one subgroup. In practice, even in the case of demographic subgroups, each individual belongs to many subgroups (eg gender, race, etc). Multicalibration handles these scenarios, but I do not get a sense of whether the authors’ algorithm extends to this case. Can the authors discuss this point?

### Soundness
3

### Presentation
2

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
The paper considers the problem of group-wise fairness in human-AI decision-making. The results show that group-wise multi-calibration ensures fairness both theoretically and empirically.

### Strengths
The question of fairness in human-AI decision-making is important. The solution is theoretically justified and empirically validated.

### Weaknesses
 * Necessity of new fairness definitions: Given that the paper achieves fairness via multi-calibration, I'm unsure if the new definitions of intergroup and human alignment are necessary. I suspect these are equivalent conditions to group-wise multi-calibration (see my question below).
* General decision space: while the paper considers binary action space, I think the result might be generalizable to general decision problems if the confidence is interpreted as a probabilistic prediction of the random variable. See 
> Ziyang Guo, Yifan Wu, Jason D. Hartline, and Jessica Hullman. 2024. A Decision-Theoretic Framework for Measuring AI Reliance. In Proceedings of the 2024 ACM Conference on Fairness, Accountability, and Transparency (FAccT '24).
* Typo: Thm 3.2 "while AI confidence function f_A is perfect calibration," => is perfectly calibrated.

The necessity of fairness definitions is not justified in this paper. The definitions are specifically tuned to a binary decision and binary state setting, and are implied by multi-calibration which is actually used to achieve fairness conditions. In fact, multi-calibration has more guarantee beyond a restricted binary decision problem. If the authors would like to justify such a weaker fairness definition, I'd expect more interesting result about the fairness definitions here beyond implied by multi-calibration, e.g. achieving fairness here is computationally easier than multi-calibration.

### Questions
* Multi-calibration implies the two fairness conditions in the paper. Are they equivalent?

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
In this work, the authors study a setting in which humans make decisions with the support of algorithmic predictions. However, the authors note that human decision-makers can have varying levels of expertise, which can imply downstream utility disparities when measuring performance w.r.t. the outcomes of decision subjects. The authors propose a multi-calibration framework that mitigates disparities in human decision-makers' utilities by adjusting risk predictions to account for heterogeneity in human decision-making. The authors provide theoretical analysis and experiments which generally justify that the proposed approach mitigates the utility disparity in question.

### Strengths
### Motivation.
The authors study a timely and important problem regarding human-algorithm decision-making in scenarios where algorithmic feedback is driving the final human decision. The notion of fairness defined w.r.t. expert decision-maker sub-populations remains under studied, and multi-calibration is a reasonable technical framework to use in this setting. 

### Soundness. 
The work is theoretically grounded and results are supported by relevant proofs. The work cites relevant related literature, clearly states (most) assumptions, and provides experiments that generally illustrate the utility of the proposed approach.  The experimental evaluation is consistent with the stated aims of the project.

### Weaknesses
### Presentation: 
- In its current form, the presentation is unnecessarily dense in a way that detracts from the core message of the work. There are a number of formal technical definitions and results that are challenging to digest. For example, Corvelo Benz & Rodriguez, 2023 cover a similar topic in theoretical depth, but the surrounding motivation and discussion is easy to follow. 
- I appreciated Figure 1 illustrating the setup with a worked example, but found the current configuration of the figure challenging to parse. I needed to read the rest of the paper before I fully understood the various components and where the numbers in the chart were originating from. 
- There are also opportunities to sharpen language and clarify terminology.
    - For example, the draft often uses terms such as “human groups”, “human populations”, and “real-world-users” etcetera without a distinction as to whether the groups in question are the decision-makers (i.e., individuals making selection decisions using algorithmic recommendations) or the decision-subjects (i.e., individuals in the population whom will receive decisions from the decision subjects). Please clarify this in the draft going forward.
    - Line 110: AI confidence facilitates fair utility => is this fair utility w.r.t. the human decision-makers or some other agent (e.g., decision subjects?)
        - E.g., lines 373-377 can be summarized and described in the appendix in more detail if the authors wish.
    - Given the widespread usage of the term alignment in current discourse, I recommend the authors provide a clear and precise definition of alignment early on in the work. The current terms “inter-group alignment” and “”human alignment” (e.g., Fig 1) are not sufficiently specific for me to understand the quantities being modeled.

### Related work: 
- This paper generally covers relevant related work. There are several works that study expert heterogeneity in other contexts. For example, Rambachan (2024), Rambachan, Coston, & Kennedy (2024), and Lakkaraju et al. (2018) use heterogeneity as an instrumental variable for identification under unobservables. De-Arteaga et al. (2023) use heterogeneity to mitigate measurement error issues. 

- There is an opportunity to sharpen the distinction between this work and Corvelo Benz & Rodriguez (2023). In particular, many results provided by the authors map to those provided by Corvelo Benz & Rodriguez (2023) with an additional conditioning operator on the decision-maker’s demographic subgroup. 
- Rambachan 2024, Identifying Prediction Mistakes in Observational Data, https://academic.oup.com/qje/article-abstract/139/3/1665/7682113.
- Rambachan, Coston, & Kennedy 2024, Robust Design and Evaluation of Predictive Algorithms under Unobserved Confounding, https://arxiv.org/abs/2212.09844.
- De-Arteaga et al., Leveraging Expert Consistency to Improve Algorithmic Decision Support, https://arxiv.org/abs/2101.09648. 

### Formal setup: 
- This framework makes a strong assumption on how humans update their confidence in response to algorithmic confidence scores (i.e., see e.q. 1 in Figure 1). Human decision-making is generally non-parametric and difficult to model. Further, the expertise of human decision-makers can also mediate how they perceive and respond to algorithmic feedback while updating their confidence scores (e.g., Albright 2019). While I appreciate that assumptions are important to drive progress, the assumptions need to be clearly stated and justified. 
- The assumption that expert sub-populations depend only upon a single demographic factor severely limits the applicability of the framework. Further, the notion of group-conditional guarantees that hold on a single demographic group is at odds with the traditional multiwcalibration setup, whereby a guarantee holds over many (intersecting) subpopulations.
- How are raw probability values converted to decisions under this framework? Because the utility function is often connected to the choice of threshold, it is important to clarify this relationship and how it impacts the proposed framework. Relatedly, I have concerns regarding how the authors discretize raw scores in the experiments, as this process of discretization implies a utility tradeoff (i.e., false positives to false negatives) that is important to model. Typically a low cutoff implies that false negatives are more costly, while a high cutoff implies that false positives are more costly. See standard cost sensitive classification frameworks for details (e.g., Fernandez et al., 2018).

Fernandez et al. 2018, Cost-Sensitive Learning, https://link.springer.com/chapter/10.1007/978-3-319-98074-4_4
Albright 2019, If You Give a Judge a Risk Score: Evidence from Kentucky Bail Decisions, https://thelittledataset.com/about_files/albright_judge_score.pdf

### Technical Results: 
- The current draft presents many technical details without providing a clear narrative motivating their importance and implications. Consider shifting some results to the Appendix and providing more description around the key takeaways. For example, Theorem 3.2 is saying that heterogeneity in human decision-making performance yields disparity in utility. However, I don’t find this result particularly surprising, as this is the relationship that I would expect. I did find Theorem 3.4 more interesting and surprising — i.e., characterizing the specific relationship between notions of alignment and utility. Consider spending more time discussing this result and others in Section 4. 
- It would be helpful to clearly state the novelty of these results w.r.t. to Corvelo Benz & Rodriguez, 2023, as they have many similar theoretical results in their work. In particular, how do these results extend our knowledge beyond adding a conditioning operator on Z

### Experiments: 
Based on figure three, it is difficult to understand whether there is a meaningful performance improvement under the proposed approach because performance bars do not have confidence intervals and the utility metric is difficult to interpret (i.e., the scaling is quite small for disparity measures).

### Questions
Can you elaborate on how predicted probabilities are thresholded to generate binary decisions under this framework? Further, can you describe the connection between predictive probabilities and utilities under this framework? See comment above for additional context. 

Can you elaborate on the specific differences between this work and Corvelo Benz & Rodriguez (2023)?

Can you describe how this framework would be extended to guarantees that hold over multiple demographic groups over experts? 

What assumptions does this framework make about how humans incorporate algorithmic feedback into their final decision?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper tackles a critical issue in AI-assisted decision-making by exploring the fairness challenges arising from human expertise disparities. The authors introduce a novel approach, group-level multicalibration, aimed at reducing utility disparity across heterogeneous groups of human experts. The concept of inter-group alignment alongside human alignment is proposed to ensure fairer utility distribution, with extensive empirical validation provided across multiple real-world datasets.

### Strengths
1. Novel Problem Definition: The paper addresses a unique aspect of AI fairness, focusing on fairness for human experts rather than the subjects of the decisions. This distinction is well-motivated and adds value to AI fairness discussions in decision-support systems.
2. Methodological Contributions: The introduction of inter-group alignment as a complement to human alignment is well-founded theoretically. The group-level multicalibration approach is an innovative addition to the calibration literature, showing promise for balancing utility across user groups with varying expertise.
3. Experimental Rigor: The empirical results demonstrate a significant improvement in utility fairness across groups, with thoughtful evaluation metrics that align well with the theoretical framework.

### Weaknesses
The paper is limited to a fairly simple setting, solving a binary decision problem without substantial innovation beyond group-level confidence multicalibration.
1. While the paper presents an interesting problem, it can be challenging to follow, especially in Section 3, which is highly mathematical without a clear exposition of the problem the math addresses. Although this section appears to build on previous research, the authors should clarify these foundations for the reader.
2. The inclusion of $lambda$-discretization may impact the efficiency of group-level multicalibration. Further discussion on its computational implications would be helpful.
3. The authors divided groups into males and females, which they justify. However, from my perspective, the group division could be more nuanced. For example, dividing the population into three or more groups might provide deeper insights, especially if the approach can maintain strong performance despite the additional computational costs.
4. All experiments should be repeated with error bars to convey the variability in results and enhance the robustness of the conclusions.

### Questions
1. How was the number of bins chosen in the experiments? Is there a principled approach to this choice?
2. In Figure 2, are there statistically significant differences between the methods, particularly in Experiments 3 and 4?

### Soundness
2

### Presentation
2

### Contribution
2

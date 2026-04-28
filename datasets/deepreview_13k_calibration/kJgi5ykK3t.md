# Measuring, Evaluating and Improving Logical Consistency in Large Language Models

- Decision: Reject
- Avg Score: 5.60
- Scores: 8, 5, 6, 6, 3

## Abstract
Recent research in Large Language Models (LLMs) has shown promising progress related to LLM alignment with human preferences. LLM-empowered decision-making systems are expected to be predictable, reliable and trustworthy, which implies being free from paradoxes or contradictions that could undermine their credibility and validity. However, LLMs still exhibit inconsistent and biased behaviour when making decisions or judgements. In this work, we focus on studying logical consistency of LLMs as a prerequisite for more reliable and trustworthy systems. Logical consistency ensures that decisions are based on a stable and coherent understanding of the problem, reducing the risk of erratic or contradictory outputs.
We first propose a universal framework to quantify the logical consistency via three fundamental proxies: transitivity, commutativity and negation invariance. We then evaluate logical consistency, using the defined measures, of a wide range of LLMs, demonstrating that it can serve as a strong proxy for overall robustness. Additionally, we introduce a data refinement and augmentation technique that enhances the logical consistency of LLMs without sacrificing alignment to human preferences. It augments noisy and sparse pairwise-comparison annotations by estimating a partially or totally ordered preference rankings using rank aggregation methods. Finally, we show that logical consistency impacts the performance of LLM-based logic-dependent algorithms, where LLMs serve as logical operators.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper's main achievement is the introduction of a method to measure the degree of consistency of a LMM, and a method to improve it. The author(s) starts by identifying three ways an LMM might not be consistent, and proposes ways to numerically evaluate the degree to which each of these inconsistencies might arise. They then go on to propose a way to improve an LLM's consistency by data refinement and augmentation,

### Strengths
In my opinion this is a good paper.
The paper is very clearly written. The author(s) succeeded very well in conveying the main ideas. They present their arguments with clear figures.
I also appreciate the definitions of s_tran, s_comm and s_neg, which make great intuitive sense to me. The authors provide clear tables that summarise their empirical findings.
The author(s) makes very clear what the objective of their paper is, and they clearly reach this goal in a very satisfying way. They motivate their approach well. The given empirical data support the claims well. Given the current interest in LLMs, I believe this work is significant for the ICLR community.

### Weaknesses
I here list the weaknesses I see in this paper. Note that I believe that they are less important than the strengths.

In the introduction, line 048, the author(s) says that consistency of its predictions is the foundation of a reliable and trustworthy system. While I certainly agree that this is *one of* the foundations, I don't think consistency alone is *the* foundation. What about a very consistently wrong system? One that consistently predicts falsehood? Certainly it is internally consitent, but it fails to accurately describe the world. I would say that calibration (or truth tracking, or something along those lines) is equally foundational to reliability and trustworthiness. If the author(s) agrees, I suggest to change this accordingly. What the authors mention on line 087 seems relevant for this, too.

On Page 3, line 150, the autor(s) mentions that if F is transitive, the corresponding relation graph is a DAG. I think this is not entirely accurate: it is a DAG when F is transitive *and irreflexive*. The author(s) seems to tacitly assume that F is irreflexive, but they should at least mention this somewhere. Also, why do they assume that this cannot be a way to measure internal consistency?
A similar remark holds in Fig 2 (b) and (d): in normal parlance, the red cycle is not intranstive, but it's just not a cycle of an order that is both transitive and irreflexive.
I wonder if the authors should not clarify this. However, even if they decide not to, despite my disagreement here, I do believe that the measure s_tran makes very good sense.

On Page 4, line 191, I think that the wording is slightly too strong, in two different ways: the metric s_tran(K) being 1 does not represent perfect transitivity, but rather (i) very likely (ii) transitivity *of cycles of size K*.

In Eqs (2) and (3), the denominator should both read |X| (|X|-1) instead of |x|(|x|-1) (so with a capital X.

On line 228, there is a space missing between "relation" and "(e.g., reversing".

One line 304, the author(s) talks about CoT prompting, which I believe stands for Chain of Thought prompting. However, this is nowhere introduced in the paper. I suggest that they introduce this somewhere.

### Questions
My only question concerns the robustness of the wording of the prompting to the results. When I use an LLM, I feel that the results, including the consistency, depends heavily on my wording. Does the author(s) have a way to measure this robustness? Are there results about this? This question naturally comes to mind when reading Sections 3 and 4, so having some ideas about this might improve the paper. Naturally, I would completely understand if this falls outside the scope of the current work.

### Soundness
3

### Presentation
4

### Contribution
4

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper evaluates the logical consistency of LLM by preference ranking, and proposes a data-enhanced method to improve the logical consistency of LLM. Experimental results show that this method can effectively improve the logical consistency without s compromising alignment with human preferences.

### Strengths
* This paper expands the evaluation scenarios of logical consistency, and evaluates LLM logical consistency in three new scenarios: abstract generation evaluation, document reordering and temporal event sequence by using preference ranking method.
* A wide range of experiments are carried out, from evaluation to enhancement, to systematically explore the logical consistency of LLM

### Weaknesses
 * In section 3.1 of the article, there is no explanation on how to use the three datasets to probe the logical consistency of LLMs. How the SummEval dataset is used to measure the negation invariance of LLMs? Is it through the form listed in Figure 1? It is suggested to supplement the relevant content.

* In section 4, the paper proposes a data refinement and augmentation method for improving the logical consistency of LLMs, which can enhance logical consistency without compromising alignment with human preferences. Human preferences are highly correlated with commutativity, and the paper does not mention that human preferences and logical consistency are contradictory relationships. In fact, human preferences should be consistent with logical consistency. Why does the paper emphasize that alignment with human preferences is not compromised? 
* The related work section mentions that "most studies have concentrated on first-order relations between only two or three statements," and it seems that the paper is only exploring and improving the logical consistency of LLMs in a new application scenario, without solving the problem of "first-order relations."

* In section 3.3, the article calculates the correlation between Transitivity consistency and self-agreement, and finds that they are highly correlated, and therefore concludes that “Transitivity serves as a useful proxy for evaluating the global reliability of LLMs. Is this conclusion reliable? Can Self-Agreement provide a comprehensive measure of model reliability?
* Why are the experimental parts of section 4 only conducted on SummEval? Additional experiments are suggested.

### Questions
* In section 3.3, the article calculates the correlation between Transitivity consistency and self-agreement, and finds that they are highly correlated, and therefore concludes that “Transitivity serves as a useful proxy for evaluating the global reliability of LLMs. Is this conclusion reliable? Can Self-Agreement provide a comprehensive measure of model reliability?
* Why are the experimental parts of section 4 only conducted on SummEval? Additional experiments are suggested.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces a comprehensive framework that measures logical consistency using three different metrics. The study evaluates these consistency measurements systematically, using the findings as indicators of overall model robustness. It also demonstrates a proof-of-concept method for improving LLM consistency through data refinement and augmentation. Finally, one practical application is showcased where more consistent LLMs could enhance performance.

### Strengths
1. **Consistency Evaluation Framework**. This paper proposed an evaluation framework to quantify the consistency of LLM output. Through a comprehensive evaluation of ten LLMs and three datasets, it compares the consistency pattern across different models, the effect of CoT prompting, and transitivity as a proxy for self-agreement.

2. **Attempt to improve Consistency**. Using the win-loss rate as a re-ranking proxy, this paper demonstrates the effectiveness of aligning a more consistent LLM through data augmentation + finetuning.

3. **Good Presentation**. The logical flow of the paper is excellent and the content is well-written. I can follow the authors' points easily by linearly reading the manuscript without dragging here and there.

### Weaknesses
There is no significant weakness in this paper. The main contribution from my perspective is the comprehensive consistency evaluation and the derived insights. The reason I will give a 6 instead of 8 is the **novelty** contributions because of the following reasons: 

1. **Reason to select these specific measurements**: In the paper the consistency metrics are straightforward but valid. The transitivity measure here is an extension of transitive ratio metrics from social network analysis and the commutativity & negation invariance are averages. I agree a good metric should be simple and direct, but the novelty contribution of the paper could be more if the authors compared different metrics and finally chose these three.

2. From Tables 2 & 3, an improved consistency could somewhat **be expected** as we have more augmented data with perfect consistency for later data types. It would be more solid to sample the same amount of perturbed data, augmented data, and augmented & negated data to make the comparison to exclude the data size as a potential factor and discuss the implications of such an experiment.

### Questions
1. Are transitivity, commutativity, and negation invariance relative to each other, or they are just equally important? Can we rank two LLM's consistency by just one (aggregated) aspect or we cannot easily compare two LLMs, say Phi-3-medium and Gemma-2-9B on SummEval, as their rank for transitivity and commutativity are different?

2. How to choose K in a real application? As a small K can miss cycles containing more than K items and from line 195 I understand transitivity empirically decreases as K increases, but the transitivity comparison between two LLMs can also be not unique. i.e. for K = 3 model A is better but when K = 4 model B is better.

minor: How to extract LLM's preference accurately using the prompt listed in Appendix F? If Figure 7 is the full instruction, the output should be a descriptive paragraph and I suspect both candidates's names, i.e. characters A and B, will be in the answer. Do we have detailed instructions like an output format instruction?

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper studies how to improve logical consistency in Large Language Models (LLMs) to make them more reliable for decision-making tasks. It introduces a framework to measure logical consistency using three key properties: transitivity (keeping decisions consistent over a series of comparisons), commutativity (order of comparison doesn’t affect results), and negation invariance (consistent handling of opposite statements). A technique for data refinement and augmentation is proposed to improve the logical consistency and then improve the performance in logic-dependent algorithms.

### Strengths
- Logical consistency is an interesting issue in LLMs, such as handling cases where both A > B and A < B appear; how should the final ranking be determined? 
- Clearly explain the main idea in Fig. 1. 
- Three types of inconsistency are proposed: transitivity (e.g., if A > B and B > C, but A < C), commutativity (e.g., A > B and A < B), and negation.

### Weaknesses
 - Win-loss rate preference ranking is one way to solve the noisy pairwise annotations. It would be interesting to explore how other models, such as Borda rule and others from social choice theory—where rankings often conflict—might help with this issue.
- There is a lack of analysis on the extent to which the proposed technique, win-loss rate preference ranking, is effective and when it may fail.

### Questions
- Could you provide more details on situations where the win-loss rate preference ranking might fail? What specific limitations did you observe?
- Could you offer more theoretical analysis on why the proposed win-loss rate preference ranking improves LLM consistency? LLMs might sometimes guess the correct answer without understanding it.
- Is it possible to have LLMs analyze why each step or change in the proposed technique works, to ensure they operate in the intended way? 
- Have you compared the win-loss rate approach to other ranking methods, such as the Borda rule or similar techniques? If so, what differences did you find in handling noisy data?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper shows an empirical study of the consistency of the LLMs using 3 metrics, transitivity, commutativity, and negation. This is an empirical work that evaluates many (10 models) over 4 datasets.  
In Section 4, the paper also suggests to use of data augmentation with a rank estimation (win-loss rates) for improving the consistency performance.

### Strengths
The paper defines 3 metrics and evaluates on large number of models over 4 datasets. Overall results are helpful to understand the current status of LLMs. For example, if we see $S_{comm}$ the scores are low in many cases which is consistent with findings from other papers. It is also good to see the results from CoT prompting that degrades the consistency performance.

### Weaknesses
This paper mostly explores the empirical behavior of LLMs given 3 performance metrics, and it mentions possible usage for fine-tuning. However, we don't see how to leverage the findings. The evaluation sets are small, and it is not sure if the findings will be applicable in general. The datasets also come with "candidates" to select. That means LLMs only need to select an answer from candidates. It is not clear if this connects to the concept of logical consistency. The paper's claim of a "universal framework" is not well-supported, as the experiments are limited to ranking tasks. The connection between the proposed metrics and actual logical consistency is not rigorously established. The paper does not provide a clear definition of logical consistency, and it's unclear how the proposed metrics quantify this concept. The relationship examined is the preference/order between two items, and it would be more precise to say "LLM as a natural language prompt of a binary preference relation" than "LLM as logical operators." The claim that this framework applies to any task where logical relations are relevant is not sufficiently demonstrated.

### Questions
The measures depend on the sampling. How do the scores vary? What are the items ($x_i$ or $x_j$) that we put in the equations?

Are the experiments only conducted in multi-choice datasets that require LLMs to rank the candidates available?

Section 4 needs more explanations. The paper doesn't show the details about the instruction-tuning settings.

### Soundness
3

### Presentation
2

### Contribution
2

# Uniform as Glass: Gliding over the Pareto Front with Neural Adaptive Preferences

- Decision: Reject
- Scores: 5, 3, 6, 3

## Abstract
Multiobjective optimization (MOO) is prevalent in numerous real-world applications, in which a Pareto front (PF) is constructed to display optima under various preferences. Previous methods commonly utilize the set of Pareto objectives (particles) to represent the entire Pareto front. However, the corresponding discrete distribution of the points on the PF is less studied, which may impede the generation of diverse and representative Pareto objectives in previous methods. To bridge the gap, we highlight in this paper the benefits of uniformly distributed Pareto objectives on the PF, which alleviate the limited diversity found in previous multiobjective optimization (MOO) approaches. In particular, we introduce new techniques for measuring and analyzing the uniformity of Pareto objectives, and accordingly propose a new method to generate asymptotically uniform Pareto objectives in an adaptive manner. Our proposed method is validated through experiments on real-world and synthetic problems, which demonstrates its efficacy in generating high-quality uniform Pareto objectives on the Pareto front.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies the problem of profiling Pareto front in multi-objective optimization. In this paper, the authors first show that traditional methods with uniformly distributed preferences does not necessarily induces uniformity in the Pareto objective space. To resolve the issue, the MMS problem is formulated to explicitly impose the iterates to be uniformly distributed in the objective space, which is then optimized by replacing the preference-to-objective mapping by a surrogate NN model. Theoretical analysis shows the asympotic uniformity property and the generalization error of the proposed method. Experiments on various numerical MOO tasks verify the effectiveness of the proposed method compared to classic evolutionary methods.

### Strengths
1. The idea of directly modeling the preference-to-PF mapping is interesting, which might inspire future research on Pareto front profiling.

2. This paper is technically sound with solid theoretical analysis.

### Weaknesses
1. The relevance to previous works is not clear enough. It seems that the technique of replacing the preference-to-objective mapping by a neural network as the surrogate model is developed from (Borodachov et al., 2019), and the generalization error analysis is adapted from prior works; hence, it would be helpful to clarify the technical difficulty or novelty compared to these works. 

2. This paper has briefly reviewed gradient-based methods for Pareto front profiling (e.g., MOO-SVGD), but the comparison seems insufficient. As I understand, the example to indicate "gradient-based methods struggle to produce globally optimal solutions" is merely concerned with the gradient aggregration method, not the MOO-SVGD or EPO methods as discussed in the main paper. The comparison should be made more comprehensively, say, comparing the performance and efficiency in experiments.

### Questions
1. It is interesting to model the preference-to-objective mapping to characterize the PF in a more direct way, but I wonder how can we generate certain Pareto solution given a specific preference from the learned Pareto front. It seems that the proposed model does not explicitly involve the solutions in the decision space.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
An approach aimed at presenting a uniformly distributed pareto front
in MOO by combining pareto front learning with uniform pareto front
selection.

### Strengths
The manuscript highlights and formalizes limitations of some of the
existing solutions, and provides arguments for the potential of the
proposed approach in overcoming these limitations.

### Weaknesses
Pareto Front Learning is introduced in the Related work section. This
is confusing, because the method has not been presented yet.  In the
general, the presentation is rather confused, with concepts being
introduced in a non clearly defined order so that one has to jump back
and forth to connect the dots and figure out the big picture.

Figure 3, which provides the overview of the framework, is not clearly
explained. The authors refer to the appendix for most details, but a
high level description should be provided, possibly including some
preliminaries earlier on (e.g., on preference angles and MOEA/D),
otherwise the paper is not self-contained.

For lemma 1, it's unclear why f shouldn't have weakly Pareto
solutions. The implications of this requirement should be better
explained.

Theorem 1 is badly presented, it's unclear from the content of the
theorem what are the constraints on h that make the pareto front
uniform.

Also, the fact that sampling uniformly from the preference vector does
not imply a uniform pareto front generation was already observed in
Liu et al, 2021 (the SVGD paper).

I am not sure pareto set learning can be dismissed by just saying that
f has many local optima. E.g. the SVGD method claims theoretical
guarantees of convergence to the paret front, and report competitive
performance on the ZDT problem set. The advantage of the proposed
solution over PSL methods should be assessed, both formally and
experimentally.

English is not entirely satisfactory (e.g. "Previous methods (Deb et
al., 2019; Blank et al., 2020) focusing on generating well-spaced
(uniform) preferences", "We first give the condition of such function
h is well defined")

### Questions
Please explain how you plan to address the weaknesses I described.

### Soundness
3 good

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Unlike directly predicting Pareto solutions from the preference vector using a neural model in previous work, MOEA/D-UAWA uses a neural model as a surrogate to estimate the final vector of objective functions from the preference vector, and adaptively adjusts the corresponding preference vectors using gradient-based optimization.

### Strengths
This paper is easy to follow. 

The idea of using a neural model as a differential surrogate to optimize the uniformity objective is novel and interesting.

### Weaknesses
The motivation of this paper assumes that the optimization problem is a black box and thus proposes a neural model as a differential surrogate. My main concern is that the above motivation is improper for neural network optimization, in which you can use a gradient descent optimizer. And the eq. (5) can also be optimized without the proposed neural surrogate model.

One possible solution is to show some additional results on large-scale neural network optimization but with a "small" neural surrogate model, which can improve computational efficiency significantly.

Moreover, the baselines used in the experiment are weak and old. A lot of work in the field of evolutionary multi-objective optimization discussed the adaptive reference/preference vectors.

### Questions
Some comments:

1. figure 1 is unclear, please improve it.

2. the claim in sec. 3.3 "whereas the proposed method aims to achieve global optimal MOO solutions" seems to be improper.

3. the main body of this paper misses an ablation study section.

---post-rebuttal comment---

According to the author's responses and the current version of the manuscript, I decided to raise my score.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents a new indicator to measure the uniformity of Pareto objectives on the Pareto front and introduces a new adaptive weight adjustment method that utilizes a neural model to represent the Pareto objective distribution, enabling the generation of uniformly distributed solutions on the Pareto front. The proposed adaptive weight adjustment method is integrated into MOEA/D and the generalization error bound of the proposed neural model is analyzed.

### Strengths
1.	A new indicator is proposed for measuring the uniformity of Pareto objectives for multi-objective optimization.
2.	A neural model is proposed to learn the relationship between preference angles and aggregated objective functions.
3.	The error bound of the proposed neural model is studied theoretically.

### Weaknesses
1.	The work related to MOEA/D with adaptive preference adjustment methods has not been adequately investigated. The most recent paper mentioned in this paper was published in 2014, which does not correspond to the extensive research MOEA/D has received over the years.
2.	The effectiveness of the proposed method needs more evaluation by considering test problems with more complicated Pareto fronts, e.g., the WFG and UF test suite, and more state-of-the-art algorithms published within the last eight years.
3.	More details of the proposed method need to be provided, e.g., when the method uses the real objective evaluation and the model-based estimation.
4.	The conclusion that MOEA/D fails to achieve uniform objectives shown in Section 4 is not rigorous, given that many MOEA/D variants have been proposed. Specific descriptions or references that hold for the conclusion should be provided.

### Questions
1.	What is the scope of the proposed adaptive weight adjustment method? Is it suitable only for decomposition-based multi-objective evolutionary algorithms? If not, how would it be used in other frameworks, e.g., dominance relation-based, indicator-based frameworks?
2.	How were the test problems in the experiments chosen? For example, for the DTLZ test suite, why were only DTLZ1-2 used, but not the more complex other problems?

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

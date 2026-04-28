# Knowledge Distillation with Perturbed Loss: From a Vanilla Teacher to a Proxy Teacher

- Decision: Reject
- Avg Score: 5.33
- Scores: 5, 6, 5

## Abstract
Knowledge distillation is a popular technique to transfer knowledge from large teacher models to a small student model. Typically, knowledge distillation employs teacher-forcing learning, where the student learns to imitate the teacher by minimizing the KL divergence of its output distribution with the teacher’s output distribution. In this work, we argue that such a learning objective is sub-optimal because there exists a discrepancy between the teacher’s output distribution and the ground truth label distribution. Therefore, forcing the student to blindly imitate the unreliable teacher output distribution leads to inferior performance. To this end, we propose a novel knowledge distillation objective PTLoss by first representing the vanilla KL-based distillation loss function via a Maclaurin series and then perturbing the leading-order terms in this series. This perturbed loss implicitly transforms the original teacher into a proxy teacher with a distribution closer to the ground truth distribution. We establish the theoretical connection between this “distribution closeness” and the student model generalizability, which enables us to select the PTLoss’s perturbation coefficients in a principled way. Extensive experiments on five datasets demonstrate PTLoss can significantly improve the distillation effectiveness for teachers of various scales.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors propose a new distillation objective (PTLoss) motivated by the inherent limitation of the KL-based distillation loss by which the student learns to match the distribution of the teacher ignoring the difference between the latter and the ground truth distribution. Their objective instead adds perturbations to the standard KL loss via a Maclaurin expansion whose (leading) coefficients are set to better match the distribution differences between the teacher and the ground truth. They provide theoretical justification for the latter, draw connections between the proposed an objective and other existing approaches, and present experiments on a variety of NLP datasets.

### Strengths
The proposed objective (PTLoss) is conceptually simple, well motivated and the theoretical results in Section 4.1 justify the motivation. Connections between the proposed approach and existing alternatives are provided (in the Supplementary Material). Experiments are (for the most part) convincing and that showing the effectiveness of the perturbation coefficient search is particularly welcome.

### Weaknesses
The quality score in (11) requires a set of labels, y, for the validation set which is described in the text as an unbiased estimator for p^*. However, it is not sufficiently clear whether these are ground-truth labels or estimated somehow. For the latter, the problem is that is not described how to obtain such unbiased estimates and for the former, that the model requires ground truth labels, which is problematic because is not consistent with the problem formulation clearly stating "we are given an unlabeled distillation set", not mentioning a validation set. Moreover, if such labels are available, one could for instance optimize the student with those and regularize with the standard distillation loss.

Though equations (8) and (9) are well motivated, a more rigorous theoretical justification (via bounding) will strengthen the claims of the proposed objective, particularly in relation to the statements that the final learned student model and the second term of (9) becoming zero. Specifically, a formal analysis bounding the approximation error introduced by replacing \(p^s\) with \(p^{t_{px}}\) in equation (9) would be beneficial. Additionally, the claim that the second term of (9) vanishes requires a more detailed justification, ideally with a proof or a clear set of conditions under which this occurs.

The results in Table 1 for all methods are an average over three trials, however, the variation is not presented.

From Figure 4(b) is not clear why the authors used M=5 in their main experiments. Moreover, it is not discussed in general how to select M or the reasoning for using M>1 given the results in Figure 4(b).

### Questions
Why using L2 in Figure 3(b) which is consistent with (11), but TVD in Figure 4(a)?

What is used as validation set in the main experiments, Dev in Table 2? Is there a relationship between the size of the validation set relative to the distillation set and performance gain?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper argues that the teacher’s output distributions can be biased from the ground truth due to various factors. Instead of forcing an out-and-out imitation of the original teacher model, the proposed PTLoss moderates the distillation objective by adding perturbations to the standard KL loss.

### Strengths
1.	This paper reviews the KL loss in knowledge distillation and proposes a good arguments that the teacher’s output distributions can be biased from the ground truth due to various factors.
2.	The proposed PTLoss implicitly transforms the original teacher into a proxy teacher with a distribution closer to the ground truth distribution.

### Weaknesses
1.	More experiments details should be given instead of putting some statistical results.

2.	Figure 3 (a) is shown to verify our assumption that the teacher outputting a distribution closer to the ground truth distribution leads to a better student. Why the OHT (grey) method achieves better accuracy than LS (yellow) with lager L2-distance between pt and p*
3.	How to quickly find a certain m in   ?
4.	In Figure 1,   is  unknown, how to make sure that “PTLoss implicitly shift   to    such that   “?
5.	How long to select the perturbation coefficients for each training dataset?
6.	The derivation from Eq.4 to Eq.5 is poor. If Eq.11, if   is known, why do not use ground-truth directly?
Concerns:
Although the proposed coefficients selection method provides a principal way to determine the perturbation hyperparameters, it remains challenging to scale up the number of classes and the perturbation order.

### Questions
1.	Figure 3 (a) is shown to verify our assumption that the teacher outputting a distribution closer to the ground truth distribution leads to a better student. Why the OHT (grey) method achieves better accuracy than LS (yellow) with lager L2-distance between pt and p*
2.	How to quickly find a certain m in   ?
3.	How to make sure that the added perturbations term is beneficial for the learning of knowledge distillation？
4.	In Figure 1,   is  unknown, how to make sure that “PTLoss implicitly shift   to    such that   “?
5.	How long to select the perturbation coefficients for each training dataset?
6.	The derivation from Eq.4 to Eq.5 is poor. If Eq.11, if   is known, why do not use ground-truth directly?
Concerns:
Although the proposed coefficients selection method provides a principal way to determine the perturbation hyperparameters, it remains challenging to scale up the number of classes and the perturbation order.

### Soundness
3 good

### Presentation
2 fair

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
The authors propose perturbing the conventional KL-divergence loss used for knowledge distillation in order to reduce the possible distributional shift between the teacher predictions and the ground-truth targets. They do so by using the Maclaurin series and perturbing the leading $M$ terms of this series and show a procedure to obtain good perturbation coefficients. They support their findings with both empirical and theoretical arguments.

### Strengths
- The idea of perturbing the Maclaurin series of the conventional KL divergence is interesting and simple.
- The empirical results (both simulated and real datasets) shows that their proposed loss indeed can improve performance across various datasets.
- The method is theoretically grounded, and in general quite simple.

### Weaknesses
 - Only the case of no known ground-truth targets (i.e. unlabeled distillation data) is considered, but this is only mentioned briefly on page 3, and should be made clear much earlier. Either way, it would be relevant to compare the proposed procedure to incorporating a weighted ground-truth loss as is common in many applications, as this also shifts the matching distribution towards the ground-truth distribution.
- There is no common consensus on the aim of distillation procedures; whether it is to match the teacher as well as possible (see e.g. [1]) or to get the best-performing student on the ground-truth data (see e.g. [2]). The success of self-distillation is due to not perfectly matching the teacher, and such nuance should be evident from your introduction. Currently, it merely states that matching an imperfect teacher is suboptimal. Also, the definition of bias here is unclear and should be explicitly stated.
- You argue in the introduction that a grid search for the temperature is computationally expensive, but your proposed method still requires a search over the perturbation coefficients. Also, how does the search-time scale with $M$, number of sample perturbations, and validation set size? The computational cost of this search should be made explicit.
- Figure 4.b.: What is the point of this experiment? Injecting perturbations and choosing such perturbations randomly is very unlikely to cause an improvement in the performance. Your method is indeed outperforming random selection, but it also should? The significance of this comparison is not clear.
- Missing references to theoretical distillation works: Phuong and Lampert "Towards Understanding Knowledge Distillation", Mobahi et al. "Self-Distillation Amplifies Regularization in Hilbert Space", and Borup and Andersen "Even your Teacher Needs Guidance: Ground-Truth Targets Dampen Regularization Imposed by Self-Distillation". Also, comparison to the continuous categorical distribution would be highly relevant; Gordon-Rodriguez et al. "The continuous categorical: a novel simplex-valued exponential family".

Minor:
- Throughout the paper (especially Sections 2 and 3) you have inconsistent use of transposes of the various vectors. E.g. should $y_n$ in (2) be transposed?
- "This observation also resonates with our intuition that an accurate, well-calibrated, and certain teacher [...]". How is well-calibrated and certain not contradictions here?

### Questions
- How does your proposed PTLoss compare to using e.g. the likelihood of the continuous categorical [3,4]?
- How does Theorem 1 differ from Proposition 3 and (8) in [5]? They appear equivalent.

[3] Gordon-Rodriguez et al. "Uses and Abuses of the Cross-Entropy Loss: Case Studies in Modern Deep Learning"

[4] Gordon-Rodriguez et al. "The continuous categorical: a novel simplex-valued exponential family"

[5] Menon et al. "A Statistical Perspective on Distillation"

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

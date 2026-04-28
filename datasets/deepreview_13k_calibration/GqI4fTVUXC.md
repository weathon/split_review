# On the Disconnect Between Theory and Practice of Overparametrized Neural Networks

- Decision: Reject
- Avg Score: 6.00
- Scores: 6, 8, 5, 5

## Abstract
The infinite-width limit of neural networks (NNs) has garnered significant attention as a theoretical framework for analyzing the behavior of large-scale, overparametrized networks. By approaching infinite width, NNs effectively converge to a linear model with features characterized by the neural tangent kernel (NTK). This establishes a connection between NNs and kernel methods, the latter of which are well understood. Based on this link, theoretical benefits and algorithmic improvements have been hypothesized and empirically demonstrated in synthetic architectures. These advantages include faster optimization, reliable uncertainty quantification and improved continual learning. However, current results quantifying the rate of convergence to the kernel regime suggest that exploiting these benefits requires architectures that are orders of magnitude wider than they are deep. This assumption raises concerns that practically relevant architectures do not exhibit behavior as predicted via the NTK. In this work, we empirically investigate whether the limiting regime either describes the behavior of large-width architectures used in practice or is informative for algorithmic improvements. Our empirical results demonstrate that this is not the case in optimization, uncertainty quantification or continual learning. This observed disconnect between theory and practice calls into question the practical relevance of the infinite-width limit.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper tests the practical validity of the theoretical connection between overparameterized (infinitely-wide) neural networks and the NTK regime. It is shown empirically that in many setups used in practice, this connection does not hold for practical network widths.
In turn, this has interesting consequences in several important fields (faster optimization, reliable uncertainty quantification and continual learning).

### Strengths
- Important research question and implications. Relevant to many recent studies.
- Well written. Clear.
- Interesting finding in CL showing that early stopping might significantly affect the conclusions drawn from CL experiments where the width is increased.

### Weaknesses
1. **Theoretical applicability.** The theory of NTKs requires not only an infinite width, but also a small step size and a large initialization scale (see the original paper by Jacot and "On Lazy Training in Differentiable Programming").  
The paper submitted here only considers the effect of increasing the width.
1. **Novelty**: It was hard for me to understand how novel the submitted paper is.  
I would appreciate a comparison to "Empirical Limitations of the NTK for Understanding Scaling Laws in Deep Learning".

Moreover, some points were not completely clear to me. See the questions in the following section.

### Questions
1. In Section 3.1, can the authors explain in what sense does NGD have "favorable convergence over GD" in theory? Does the paper refer to an appropriate source for this statement? Is this ``strict'' in some way? (otherwise it's unclear why testing only NGD is sufficient to draw conclusions on GD).
1. In Section 3.1 (Page 6), why do the authors use only a subset of the data for the CNN regression experiment?  
   (this should be explained in the paper as well).
1. Still in Section 3.1, does it make sense to somehow plot in Figure 2 (e.g., with a horizontal line) the $\lambda_{\min}$ and $C'$ in the limit where the width$\to\infty$ (i.e., in the NTK regime)? Is there perhaps a way to compute that theoretically rather than numerically? I believe it may complete the picture for this experiment.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper empirically investigates whether the theoretical predictions and assumptions based on infinite width NTK theory holds for practical widths encountered in common architectures on relevant tasks. In particular, the authors consider three areas - optimization, uncertainty quantification, and continual learning.

* For optimization, second-order methods like natural gradient are hypothesized to have faster convergence compared to first-order methods like SGD when networks approach the kernel regime. However, the authors find that common architectures do not satisfy the necessary conditions (such as Jacobian stability) for this to hold.
* In uncertainty quantification, controlling the exploration-exploitation tradeoff in neural bandits via the NTK theory leads to poor performance, while other methods like online evidence maximization work better.
* In continual learning, wide networks appear to forget less catastrophically only if not trained to high accuracy per task. So increasing width does not mitigate forgetting for practical architectures.

### Strengths
The paper is very well written and easy to follow, even if the reader does not have a very strong background in kernel and gaussian process theory. The question it addresses in an important one. Although prior papers (Fort et al arxiv.org/abs/2010.15110, Atanasov et al arxiv.org/abs/2212.12147) have studied the distinctions between infinite and finite width networks, this paper contributes novel insights. I do however recommend that the authors do a more thorough literature review and cite prior papers studying infinite vs finite width networks, and cite the above mentioned papers. The reviewer especially appreciates the empirical tests in the neural bandit and catastrophic forgetting settings, which are not commonly encountered by theorists working on NTK-related analysis.

### Weaknesses
My primary critique is the lack of distinction made between width and feature learning strength. Although it is true that in standard/NTK parameterization, wide networks converge to the NTK (as in Jacot et al), alternative parameterizations have since been considered. Firstly, (Chizat et al http://arxiv.org/abs/1812.07956) have shown even finite width networks can be reparameterized to make them behave as kernels and have identified a "laziness" parameter $\alpha$ that can control feature learning strength at any width.  

Most importantly, the mean field parameterization (Mei & Montanari https://arxiv.org/abs/1804.06561, several other concurrent works) also known as $\mu$-parameterization (Yang and Hu https://arxiv.org/abs/2011.14522) allows networks to learn features at infinite width. Moreover, (Vyas et al http://arxiv.org/abs/2305.18411) have shown that finite width networks approach the infinite-width feature learning limit very quickly and efficiently. This would imply that in that parameterization such a distinction between wider and narrower networks would be substantially less prominent. One consequence of this is hyperparameter transfer across widths (Yang and Hu http://arxiv.org/abs/2203.03466 ). 

I do not expect the authors to redo experiments in this alternative parameterization (though that would certainly be an interesting follow up). It would be very good, however, to distinguish between *overparameterized theory* not being representative of realistic finite-width networks (which I think is an incorrect claim) vs *lazy training at large widths* being non-representative of realistic finite-width networks (which is the claim that the paper very nicely supports). A few sentences in the introduction making this explicit would be very welcome.

### Questions
For optimization, besides stability conditions, were there other signs like faster convergence that second-order methods may work better? Or was SGD consistently better?

What happens if you make the tasks more similar in the continual learning setting? Does the NTK theory begin to hold?

### Soundness
4 excellent

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
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper is experimental. It is dedicated to testing assumptions of several previous papers (mostly theoretical). These previous papers exploit the NTK theory and make a number of predictions about the behavior of NNs. The main claim of the paper is that these predictions do not hold in a practical setting. Three examples of such predictions are considered: 1) the claim that second-order optimization algorithm has some advantages over 1st order in the infinite width limit (the claim from Zhang et al. (2019)); 2) setting the exploration parameter in Neural Uncertainty Quantification according to a formula by Zhou et al. (2020), that was inspired by the NTK theory, 3) the claim that "increasing
the width of a neural network reduces catastrophic forgetting".

### Strengths
The setup of experiments is clear, their description is complete. Experimental results are convincing.

### Weaknesses
I doubt the main claim of the paper: "observed disconnect between theory and practice calls into question the practical relevance of the infinite-width limit". It seems to me that this claim does not follow logically from the reported experiments.

The experimental results of Section 3.1 seem to refute the theory of Zhang et al. (2019), rather than the NTK theory. Experimental evidence that Stable Jacobian conditions (7) and (8) are never satisfied does not "call into question the practical relevance of the infinite-width limit". It refutes the claim that NGD is better than GD, but not the NTK theory. Logically, the NTK theory does not claim that (7) and (8) should be satisfied. The authors should clarify why the failure of these specific conditions, which are derived from a particular analysis of neural network training, implies a broader problem with the applicability of the infinite-width limit.

The same holds for the Neural Contextual Bandits experiments. It seems that Section 3.2 shows that the formula for the exploration parameter from Zhou et al. is not very good in a practical setting (probably, because the assumptions of Zhou et al are not satisfied). But this does not mean that "the practical relevance of the infinite-width limit" is in question. It is unclear why the specific choice of exploration parameter, derived under certain theoretical assumptions, not performing well in practice should invalidate the entire infinite-width theory. The authors need to provide a stronger link between the failure of this parameter and the broader theory.

Concerning catastrophic forgetting, there is no discussion of why the previous research (e.g. Mirzadeh et al. (2022)) somehow contradicts to experimental results of the paper. The authors should elaborate on the specific differences in experimental setup or analysis that lead to the apparently contradictory results. It is not sufficient to simply state that the prior work is contradicted; a deeper analysis of the discrepancies is needed.

### Questions
The general question is: how the irrelevance of the NTK theory follows from the fact that certain assumptions of a theory developed in a previous paper (e.g. Stable Jacobian conditions (7) and (8)) are not satisfied in current experiments.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper empirically verifies the linearization effect of wide neural networks and the challenges of applying it to practical neural networks in downstream applications. Specifically, the authors demonstrate the gap between theory and practice across three domains: Optimization (Section 3.1), Uncertainty Quantification (Section 3.2), and Continual Learning (Section 3.3). One of the fundamental reasons for this phenomenon is that practical neural networks do not satisfactorily meet the Stable Jacobian condition (Equation 8). Based on this issue, the authors highlight potential pitfalls that can arise from ideas rooted in linearization for each task.

### Strengths
* The paper is easy-to-follow, and its intended claims are clear.
* The empirical gap between linearized NNs and practical NNs tackled in this paper is timely. Additionally, the authors' approach to the problem (Stability of Jacobian) is intriguing.
* The claims made by the authors are adequately supported through experiments.
* The authors have clearly delineated the potential and limitations of their claims.

### Weaknesses
 * While each of the authors' claims is clear, the connections between them are somewhat disjointed. Specifically, it is challenging to perceive Section 3.1-3.2's issues as problems since, in reality, wide NNs experience less catastrophic forgetting, as suggested in Section 3.3. Therefore, combining Sections 3.1 and 3.2 into one section and separating Section 3.3 might help avoid this confusion.

* The title of Section 3.1, "Training: Second-order Optimization", doesn't accurately convey the content discussed within. The empirical evidence in Section 3.1 (Figures 2-3) primarily supports the instability of the Jacobian in finite NNs. While this might be one of the reasons second-order optimization methods fail when applied to NNs, the paper doesn't seem to present direct experiments that validate this. Moreover, second-order optimization can fail for more than one reason: Slow convergence and Poor generalization. The authors do not specify which of these reasons is attributed to the unstable Jacobian. To avoid confusion, it's recommended that the title of Section 3.1 be revised.

* I wanted to point out that while Sections 3.1 and 3.2 seem homogeneous as they use the same underlying assumptions, Section 3.2 appears heterogeneous due to the absence of such a discussion. According to Section 3.3, for sufficiently trained NNs, width does not help. However, this is only a counterexample to the conclusions in the kernel regime literatures and does not provide specific insights. For instance, why does width not help only in well-trained NNs? Why do less-trained NNs benefit from width? Which parts of the claim by Mirzadeh et al., 2022, are incorrect? For these reasons, the conclusions of Section 3.3 seem to be just an interesting counterexample to the theme of Connecting Theory and Practice in Section 3, without including sufficient discussion on the causes.

* Similar to Section 3.3, Section 3.2 only shows that the success of second-order optimization methods cannot be explained through the kernel regime. However, real-world second-order optimization methods [1,2] often demonstrate faster convergence than first-order optimization methods, and they do not base their theoretical superiority on the kernel regime. Considering this, the experiments and conclusions of Section 3.2 may not feel significant.

### Questions
* Have you considered restructuring the sections to more coherently present the content, possibly merging Sections 3.1 and 3.2, and separating Section 3.3?
* Second-order optimization can exhibit issues like slow convergence and poor generalization. Could you specify which of these issues the unstable Jacobian directly contributes to, based on your research?

If the issues in Weakness & Questions are addressed appropriately, I will raise the score.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

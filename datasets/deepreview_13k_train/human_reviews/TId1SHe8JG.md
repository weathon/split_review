# Provable Uncertainty Decomposition via Higher-Order Calibration

- Decision: Accept
- Scores: 8, 8, 8, 6

## Abstract
We give a principled method for decomposing the predictive uncertainty of a model into aleatoric and epistemic components with explicit semantics relating them to the real-world data distribution. While many works in the literature have proposed such decompositions, they lack the type of formal guarantees we provide. Our method is based on the new notion of higher-order calibration, which generalizes ordinary calibration to the setting of higher-order predictors that predict _mixtures_ over label distributions at every point. We show how to measure as well as achieve higher-order calibration using access to $k$-snapshots, namely examples where each point has $k$ independent conditional labels. Under higher-order calibration, the estimated aleatoric uncertainty at a point is guaranteed to match the real-world aleatoric uncertainty averaged over all points where the prediction is made. To our knowledge, this is the first formal guarantee of this type that places no assumptions whatsoever on the real-world data distribution. Importantly, higher-order calibration is also applicable to existing higher-order predictors such as Bayesian and ensemble models and provides a natural evaluation metric for such models. We demonstrate through experiments that our method produces meaningful uncertainty decompositions in tasks such as image classification.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors present a new way of decomposing aleatoric and epistemic uncertainties based on second-order distributions. They claim they are the first one to provide estimates enjoying some calibration properties that they specify, and show empirically their findings.

### Strengths
The approach is innovative, and the authors look at calibration of second-order distribution, which is still a shallow-studied subfield. The exposition is mostly clear, and the results they derive are mathematically sound.

### Weaknesses
In Definition 1.1, you write $f^*([x]):=\lbrace{f^*(\mathbf{x}) | \mathbf{x} \sim [x] }\rbrace$. Why is $\mathbf{x}$ suddenly in boldface? Is it just to separate notationally the equivalence class $[x]$ from a possible element $\mathbf{x}$ of such a class? In addition, what does $\mathbf{x} \sim [x]$ mean? From what you write before $[x]$ is just an equivalence class. In turn, the squiggle cannot mean "$\mathbf{x}$ is distributed according to $[x]$". Do you mean that $\mathbf{x}$ is a generic element of the equivalence class $[x]$? This becomes even more puzzling in Theorems 1.2 and 2.7, and Lemma 3.2, where expectations are taken w.r.t. $\mathbf{x} \sim [x]$.

Lines 145-146: "Then we cannot distinguish scenario 1 from scenario 2 if all we receive are ordinary labeled examples with a single label per image". It seems that you rediscovered the classical Fisher-Laplace paradox (see e.g. Appendix A.(i) in [1]).

The author(s) seem to be unaware of an extensive literature that studies the pitfalls of second-order distributions in quantifying and disentangling between AU and EU (see e.g. the last paragraph of [1, Section 5]). In light of this, does their method solve such shortcomings? If so, how? If not, or if only partially, it should be (i) discussed why it is still of interest to take a higher-order route, as the authors do, and (ii) compare the author's method $-$or at least introduce a discussion$-$ with others that do not suffer from these problems, such as credal-set-based uncertainty quantification (see works by Hüllermeier, Sale, Caprio, Desterke to name a few). The authors should also discuss the limitations of their approach in light of the fact that learning a level-2 predictor from level-0 samples is generally ill-posed.

How does the author's notion of calibration relates to type-2 validity [2] and credal set calibration of e.g. [3]? Specifically, how does the proposed calibration method compare to existing approaches that provide guarantees on the predicted distribution, rather than just the predicted value?

Why in line 270 the authors write $g:\mathcal{X} \rightarrow \Delta \mathcal{Y}^{(k)}$? That is, why is $k$ in parentheses?

The conceptual simplification in line 273 is not immediately clear to me. Predictor $g:\mathcal{X} \rightarrow \Delta\mathcal{Y}^k$ outputs a collection of $k$ probabilities over the labels in $\mathcal{Y}$. Does your interpretation $\Delta\mathcal{Y}^k \subseteq \Delta\Delta\mathcal{Y}$ mean that we can see $g$ as outputting an empirical second-order distribution that gives probability $q/k$ to the elements of $\Delta\mathcal{Y}$, where $q$ is the number of times a specific distribution over the outputs was returned by the predictor $g$? In other words, suppose $\mathcal{Y}=\lbrace{1,2,3}\rbrace$, and that $k=3$. Suppose also that $g(x)=((0.9,0.05,0.05), (0.9,0.05,0.05), (0.8,0.1,0.1))$. Then, this can be seen as an empirical second-order distribution giving probability $2/3$ to $(0.9,0.05,0.05)$, probability $1/3$ to $(0.8,0.1,0.1)$, and probability $0$ to all other elements of $\Delta\mathcal{Y}$. Is this what the authors mean?

The 1-Wasserstein metric is well-defined on $\Delta\Delta\mathcal{Y}$ only when $\mathcal{Y}$ is discrete. This should be mentioned.

Careful in using $G$ as any concave generalized entropy function, since in the literature it usually refers to the generalized Hartley measure (see e.g. eq (27) in [4]).

Why is there not a Conclusion?

### Questions
In Definition 1.1, you write $f^*([x]):=\lbrace{f^*(\mathbf{x}) | \mathbf{x} \sim [x] }\rbrace$. Why is $\mathbf{x}$ suddenly in boldface? Is it just to separate notationally the equivalence class $[x]$ from a possible element $\mathbf{x}$ of such a class? In addition, what does $\mathbf{x} \sim [x]$ mean? From what you write before $[x]$ is just an equivalence class. In turn, the squiggle cannot mean "$\mathbf{x}$ is distributed according to $[x]$". Do you mean that $\mathbf{x}$ is a generic element of the equivalence class $[x]$? This becomes even more puzzling in Theorems 1.2 and 2.7, and Lemma 3.2, where expectations are taken w.r.t. $\mathbf{x} \sim [x]$.

Lines 145-146: "Then we cannot distinguish scenario 1 from scenario 2 if all we receive are ordinary labeled examples with a single label per image". It seems that you rediscovered the classical Fisher-Laplace paradox (see e.g. Appendix A.(i) in [1]).

The author(s) seem to be unaware of an extensive literature that studies the pitfalls of second-order distributions in quantifying and disentangling between AU and EU (see e.g. the last paragraph of [1, Section 5]). In light of this, does their method solve such shortcomings? If so, how? If not, or if only partially, it should be (i) discussed why it is still of interest to take a higher-order route, as the authors do, and (ii) compare the author's method $-$or at least introduce a discussion$-$ with others that do not suffer from these problems, such as credal-set-based uncertainty quantification (see works by Hüllermeier, Sale, Caprio, Desterke to name a few).

How does the author's notion of calibration relates to type-2 validity [2] and credal set calibration of e.g. [3]?

Why in line 270 the authors write $g:\mathcal{X} \rightarrow \Delta \mathcal{Y}^{(k)}$? That is, why is $k$ in parentheses?

The conceptual simplification in line 273 is not immediately clear to me. Predictor $g:\mathcal{X} \rightarrow \Delta\mathcal{Y}^k$ outputs a collection of $k$ probabilities over the labels in $\mathcal{Y}$. Does your interpretation $\Delta\mathcal{Y}^k \subseteq \Delta\Delta\mathcal{Y}$ mean that we can see $g$ as outputting an empirical second-order distribution that gives probability $q/k$ to the elements of $\Delta\mathcal{Y}$, where $q$ is the number of times a specific distribution over the outputs was returned by the predictor $g$? In other words, suppose $\mathcal{Y}=\lbrace{1,2,3}\rbrace$, and that $k=3$. Suppose also that $g(x)=((0.9,0.05,0.05), (0.9,0.05,0.05), (0.8,0.1,0.1))$. Then, this can be seen as an empirical second-order distribution giving probability $2/3$ to $(0.9,0.05,0.05)$, probability $1/3$ to $(0.8,0.1,0.1)$, and probability $0$ to all other elements of $\Delta\mathcal{Y}$. Is this what the authors mean?

The 1-Wasserstein metric is well-defined on $\Delta\Delta\mathcal{Y}$ only when $\mathcal{Y}$ is discrete. This should be mentioned.

Careful in using $G$ as any concave generalized entropy function, since in the literature it usually refers to the generalized Hartley measure (see e.g. eq (27) in [4]).

Why is there not a Conclusion?

---

[1] https://openreview.net/forum?id=4NHF9AC5ui

[2] https://www.sciencedirect.com/science/article/pii/S0888613X21001195

[3] https://arxiv.org/abs/2410.12921

[4] https://link.springer.com/article/10.1007/s10994-021-05946-3

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
In this paper, the authors propose a generalization of classical (first-order) calibration by introducing notions of higher-order and $k$-th order calibration. They formulate and prove theoretical guarantees that a higher-order calibrated predictor provides accurate estimates of aleatoric uncertainty (AU), and they show similar results for $k$-th order calibrated predictors. The authors demonstrate that their theoretical results hold in experiments for image classification.

### Strengths
The main strengths of the paper are its theoretical contributions. 

Specifically, it generalizes the notion of calibration by extending it to "higher-order" calibration. The authors show that a higher-order calibrated predictor provides correct estimates of the true AU. Moreover, they show that being higher-order calibrated is the necessary and sufficient condition for producing accurate estimates of AU, which I believe is an important theoretical result. 

Since in practice we can only have finitely calibrated predictors (i.e., $k$-th order calibrated predictors), the authors additionally prove results on the accuracy of AU estimates for small $k$ for different instantiations of generalized entropies.

Also, compared to the prior work of Johnson et al. (2024), one does not need to change the output layer of the model, but can use the model's architecture as it is.

### Weaknesses
I see several weaknesses in the paper, which I list below. Additionally, there are aspects I did not fully understand (which may not necessarily be weaknesses), and I will list them in the Questions section.

### Structure and Text:

I find the structure of the paper somewhat confusing and believe it could be improved. Specifically:

- Figure 1 on page 2 is never referenced in the text. The authors might consider referencing it in the paragraph on lines 37-43, where they essentially describe it in words.

- In lines 101-102, there is a section(?) titled "Summary of main results," which is almost two pages long and is not actually a summary. Rather, it introduces relevant definitions / some theorems, and is too lengthy for a summary. I would suggest that the main results are presented in Sections 2 and 3, not in this section. 
The authors might consider renaming this section to something like "Background" or "Preliminaries."

- The paper is missing a Conclusion section. Given the substantial theoretical material presented, a conclusion would help readers to get the key takeaways. For example, the authors could outline the proved results for the correctness of the AU estimate, discuss limitations, and suggest possible further research directions.

- [Minor] Some parts of the Appendix are not referenced, e.g. the proof of Theorem 2.6 in Appendix D.4.


### Missing Related Work:

I believe the paper is missing references to prior work:

[1] Kotelevskii, N., & Panov, M. (2024). Predictive Uncertainty Quantification via Risk Decompositions for Strictly Proper Scoring Rules. arXiv preprint arXiv:2402.10727.

[2] Durasov, N., Dorndorf, N., Le, H., & Fua, P. (2022). Zigzag: Universal sampling-free uncertainty estimation through two-step inference. arXiv preprint arXiv:2211.11435.

The first reference is cited in Hofman et al. (2024) and also provides a way to decompose predictive uncertainties via proper scoring rules (which is one of the key things in the submitted paper).

The second is cited in Johnson et al. (2024) and appears to be the first work in the context of predicting pairs of labels.


### Baseline in experiments:

The current work, as mentioned by the authors, is inspired by the initial results in Johnson et al. (2024). In their approach, they propose a Cheat NN that aims to be second-order calibrated. Using their Cheat NN requires modifying the output layer to output an $l \times l$ matrix (where $l$ is the number of classes), which could be a limitation when $l$ is large. Nonetheless, it represents a third method [in addition to two proposed in line 318] to achieve higher (k-th) order calibration. It would be interesting to see how the proposed strategies compare to the one in Johnson et al. (2024). Including the Cheat NN as a baseline in the experiments would strengthen the paper by providing a direct comparison to existing methods.

### Questions
1. In lines 196-197, the authors state: "For any given instance we now have not just a single predicted distribution over outcomes, but rather a full 'posterior predictive distribution' over such distributions. In this way every Bayesian model is a higher-order predictor." I want to clarify why the posterior predictive distribution is considered a higher-order predictor. Isn't it an averaged prediction (over the posterior of the weights), hence first order? A sample from the posterior predictive distribution is a label, not a categorical vector?

2. In line 318, the authors propose two methods to achieve $k$-th order calibration: "minimizing a proper loss, or post-processing the level sets of a learned predictor." However, it seems that in the experimental section only one strategy (the post-hoc calibration algorithm) is used. Did the authors employ the first strategy? How do these two strategies perform compared to each other?

3. In line 433, the authors mention: "our epistemic uncertainty is precisely the true “variance” in $f^*(x)$ as $x \sim [x].$." I understand this informal claim, but how can we see that epistemic uncertainty indeed corresponds to the variance of the Bayesian mixture?

4. In the experimental section, the examples of "mostly epistemic" images still resemble in-distribution samples, similar to "soft-OOD" scenarios (e.g., in [1]). I think that higher-order calibration helps identify these objects. However, in practice, it is common to use estimates of EU to detect "hard-OOD" samples, where images do not resemble in-distribution ones (e.g., training images from CIFAR-10 and testing on ImageNet samples). In this case, will higher-order calibration improve out-of-distribution detection?

5. In lines 378-379, the authors state: "Let any concave generalized entropy function $G$ be given..." In prior works (Kotelevskii & Panov (2024) and Hofman et al. (2024)), several choices of generalized entropy are considered, including Shannon entropy and Brier score, but also the Zero-one score. The Zero-one score leads to a convex (but not strictly convex) generalized entropy. Will the necessary and sufficient conditions of being higher-order calibrated to produce calibrated estimates of AU still hold in this case?

[1] Kotelevskii, N., & Panov, M. (2024). Predictive Uncertainty Quantification via Risk Decompositions for Strictly Proper Scoring Rules. arXiv preprint arXiv:2402.10727.

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The authors explore the implications of higher-order calibration on decomposing the uncertainty of a predictor into aleatoric and epistemic components. In this regard they propose to approximately achieve higher-order calibration through calibrating over a finite k number of snapshots and show the convergence as k goes to infinity. This work extends the second-order calibration using pairs of labels to arbitrarily higher orders with k-snapshots. Authors validate the theoretical claims through experiments.

### Strengths
1. Presents important and interesting theoretical formalization on higher-order calibration and convergence of approximate k-order calibration to approximate higher-order calibration, preserving the mathematical rigor.
2. The approximate k-snapshot calibration is certainly important in applying the theory in practice.
2. The paper is well written with a comprehensive study on related works which can be very useful for a novice reader.
3. The experiments are well motivated and demonstrate the theoretical claims made in the paper.

### Weaknesses
1. In the experiments, it is useful to mention how the estimation of these quantities of interest were done, for example the how the entropy values were computed empirically in order to get an idea on how the estimation errors of those might affect the overall uncertainty estimation.
2. The running example can be discussed in detail in the main text or in the appendix as an aid for understanding the notation and the definitions.

### Questions
Please see Weaknesses.

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
2

### Summary
This work provides a methodology for decomposing predictive uncertainty through calibration on the conditional distribution of the label, using ``higher-order calibration" enabled by multiple samples from conditional distributions.

### Strengths
This work addresses an important problem within the area of conditional predictive inference, to my understanding, and includes rigorous theoretical analysis.

### Weaknesses
I believe it would be beneficial to improve the clarity regarding the problem setting and objective in a more formal manner.

### Questions
1. Could the authors provide some background or explanation on the importance of decomposing predictive uncertainty? Specifically, how do the results of this work guide practitioners in improving prediction or predictive inference, given some data and a trained model in practice? Is the primary aim to enhance understanding of the behavior of a given model or prediction method, rather than to directly improve things?

2. I was wondering if there might be any connection between this work and ``Distribution-free Inference with Hierarchical Data" by Lee and Barber. Specifically, their work considers a similar setting with multiple label samples for each feature observation, focusing on a form of conditional predictive inference. They propose a methodology for constructing a prediction set that achieves a `second-moment coverage guarantee' and note that a 'k-th moment coverage guarantee' can be achieved similarly when the number of repeated samples exceeds k across many groups. Although the inferential targets differ in form between the two works, I feel that there may be a connection in that both works measure conditional uncertainty through higher-order moments using multiple label observations. Could the authors perhaps share their thoughts on this?

### Soundness
3

### Presentation
2

### Contribution
3

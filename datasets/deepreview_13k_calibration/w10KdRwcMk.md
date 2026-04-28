# Revisiting the Variational Information Bottleneck

- Decision: Reject
- Avg Score: 4.25
- Scores: 3, 3, 5, 6

## Abstract
The Information Bottleneck (IB) framework offers a theoretically optimal approach to data modeling, though it is often intractable. Recent efforts have optimized supervised deep neural networks (DNNs) using a variational upper bound on the IB objective, leading to enhanced robustness to adversarial attacks. In these studies, supervision assumes a dual role: sometimes as a presumably constant and observed random variable, and at other times as its variational approximation. This work proposes an extension to the IB framework, and consequently to the derivation of its variational bound, that resolves this duality. Applying the resulting bound as an objective for supervised DNNs induces significant empirical improvements, and provides an information theoretic motivation for decoder regularization.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper claims to provide the "theoretical optimal approach to data modeling", and to extend the framework, by deriving the a variational bound to resolve some problems of the previous framework. 

My understanding is that eq. 16 (derived by eq.3)  is the contribution of this work. The paper provides derivations to justify eq. 16. 

In the experimental session, the authors evaluate the performance in image and text classification of the new loss and the robustness to adversarial attack. 

The authors claim that the new loss outperforms the previous loss.

### Strengths
If the paper were clearer, the paper presents many contributions and analyses of the proposed terms. 

Two experiments (image and text classification) compare the "vanilla" and VIB with the new loss. 

Historical overview of IB.

### Weaknesses
The paper is largely unclear.

It starts with the history of the IB, more than presenting the contribution of the work.

The presentation is not clear on the steps of the new loss.  

In the new loss, there seems to be a new contribution on the predictor, but the predictor (or classifier) is already included in the loss in the VIB. 

The impression is that the new loss introduces a new regularization term, but its justification is not clear. 

The abstract is unclear, what are the two points of the "dual role"? What is the "theoretically optimal approach to data modeling"?

### Questions
Would be nice to understand the difference of eq. 16 and the standard VIB.

### Soundness
1

### Presentation
1

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper revisits the variational information bottleneck and extends it to a supervised variational information bottleneck.  The experiment on ImageNet and text classification shows that SIB achieves better results than VIB.

### Strengths
SIB performs better than VIB regarding classification accuracy and adversarial robustness.

### Weaknesses
### Motivation

**1.VIB applies IB in supervised setting not the original IB for the unsupervised clustering.**

The proposed SVIB still focus on supervised tasks, which does not appear to address this limitation. The core issue is that the original Information Bottleneck (IB) framework was designed for unsupervised learning, where the joint distribution p(x,y) is assumed to be known, and the goal is to find a compressed representation Z that preserves information about Y. VIB adapts this to supervised learning by using a variational approximation of p(y), but the fundamental problem remains that the target variable Y is not treated as a true random variable within the IB framework. SVIB, by also focusing on supervised tasks, does not fundamentally address this mismatch between the original IB and the supervised setting.

**2. Preventing the classifier from overfitting to the representation by involving maximize  H(\hat{Y}|Z)**

Why not directly maximize H(\hat{Y}|Z) within the standard VIB framework, rather than introducing an additional information bottleneck? The paper introduces a new bottleneck with the term H(\hat{Y}|Z), but it's unclear why this term cannot be incorporated directly into the existing VIB framework. The proposed method introduces a new hyperparameter and approximation, which adds complexity without a clear justification. The core issue is whether the added complexity of the new bottleneck is necessary, or if the same effect could be achieved by directly maximizing the conditional entropy within the existing VIB framework.

### Novelty

**1. Most VIB papers deal with a single modality, and in many cases solve low dimensional data.**

For multi-modal scenarios, [1] ("Multimodal Information Bottleneck," IEEE Trans, 2022) already addresses this challenge. I believe VIB itself is capable of handling multi-modality. Additionally, I am skeptical about the effectiveness of SVIB in high-dimensional settings since its Mutual Information (MI) estimation approach is the same as VIB's. The paper claims that VIB is limited to single modality and low dimensional data, but this is not a fundamental limitation of VIB itself. The cited work demonstrates that VIB can be extended to multi-modal scenarios. Furthermore, the paper's approach to MI estimation is the same as VIB, which raises concerns about the effectiveness of SVIB in high-dimensional settings, where MI estimation can be challenging.

**2. This work is an extension of [2] ("Fixing a Broken ELBO," PMLR 2018).**

The contribution appears incremental. The paper builds upon the analysis of the ELBO in [2], which showed that the ELBO can lead to overfitting. The proposed method introduces a new term to address this issue, but it is unclear if this is a significant departure from the existing work. The core issue is whether the proposed method offers a substantial improvement over the existing analysis of the ELBO and its limitations.

### Missing References and Limited Scope.

From my understanding, the primary contribution is the constrained maximization H(\hat{Y}|Z). However, there are other IB-based methods with different MI estimation perspectives. Why not evaluate the effectiveness of maximizing H(\hat{Y}|Z) in those frameworks to validate its broader applicability? If SVIB only modifies VIB and is constrained to variational lower-bound methods, the scope of the paper appears too limited. The paper focuses on a specific modification of VIB, but it does not explore the broader landscape of IB-based methods. The paper should investigate whether the proposed approach can be generalized to other IB methods with different MI estimation techniques. The limited scope of the paper raises concerns about the general applicability of the proposed method.

### Questions
1. Could you please provide more experiments on PGD and AutoAttack?
2. Could you please visualize the latent representations of SIB and compare them with VIB?

### Soundness
1

### Presentation
1

### Contribution
1

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
- The paper picks up an issue identified in the Deep Variational Information Bottleneck paper, where the classifier can overfit to the learned representation, Z, of a VIB model, and proposes a new framework for supervised learning with IB, which they call Supervised Information Bottleneck (SIB), and a corresponding variational approach, SVIB.
- The core theoretical contribution is to add a constraint to the IB and VIB objectives that minimizes an upper bound on I(\hat{Y},Z), which is equivalent to maximizing a lower bound on H(\hat{Y}|Z). The paper shows that this new constraint is tractable in the SVIB setting.
- The paper provides experiments comparing SVIB to VIB and “vanilla” Maximum Likelihood models (trained with cross entropy) on ImageNet and natural language sentiment analysis.

### Strengths
- The paper is well-written and easy to read.
- Constrained maximization of H(\hat{Y}|Z) will clearly achieve the goal of preventing the classifier from overfitting to the representation.
- The theoretical approach is plausibly useful. A careful set of experiments could demonstrate its value beyond using VIB or CEB.

### Weaknesses
 - In general, the experiments are of the correct form (comparisons between different IB approaches and Maximum Likelihood on clean and adversarial test sets), but they are unconvincing at supporting the main claim that SVIB substantially improves on other proposed tractable IB approaches, as pointed out in more detail below.
- One shortcoming of all of the experiments is that the VIB models are not given the same amount of hyperparameter tuning as the SVIB models – it appears that in all cases, the SVIB models get three times as many runs with different hyperparameters to find a setting that outperforms the VIB models. This discrepancy in hyperparameter tuning makes it difficult to draw firm conclusions about the relative performance of SVIB and VIB.
- VIB on classification tasks often benefits from having a mixture distribution for r(z), whether learned or just distributed across part of the domain of Z, rather than having a single isotropic Gaussian distribution for r(z). It’s likely that your selected values of \beta would perform better in that setting, as it becomes easier for the model to learn to assign classes to different mixture elements as it sees fit, which makes the model more powerful (more powerful models can tolerate higher compression/higher values of \beta). This would likely benefit SVIB as well, so that it more reliably outperforms the Maximum Likelihood baseline on the test set. The use of a single isotropic Gaussian for r(z) may be limiting the performance of both VIB and SVIB.
- The paper is missing an important citation: CEB Improves Model Robustness, Entropy 2020. Overlooking this reference is a major shortcoming of the paper, since it studies the same question on one of the same datasets using the same Information Bottleneck framework, and it achieves substantially better results on that dataset than reported in this paper (its VIB results are also stronger than your VIB and SVIB results). The absence of this comparison makes it difficult to assess the true contribution of the proposed method.
- The ImageNet table highlights SVIB results in settings where the VIB results appear to strongly overlap – it seems a stretch to claim that SVIB is doing better than VIB with a result of 53.4%+/-1.8% compared to 53.5%+/-0.2% for FGS with \epsilon=0.1, for example (and similarly but to a lesser extent for FGS with \epsilon=0.5). The statistical significance of these differences is questionable, and the presentation of the results could be misleading.
- For all experiments, hyperparameter selection for VIB is questionable, as test set performance on the clean data appears to still be improving substantially at the smallest value of \beta. As \beta goes to 0, its performance should match the vanilla model on the clean data, but you stop exploring \beta when the test set performance is substantially worse than the vanilla model, indicating that probably neither the VIB nor the SVIB models are very close to optimally configured. This suggests that the reported results may not represent the true potential of VIB and SVIB.
- The Conditional Entropy Bottleneck paper showed that CEB reliably outperforms VIB on both clean and adversarial examples on a variety of image datasets. The CEB Improves Model Robustness paper further explores that in detail on ImageNet. Since implementing CEB can be made parameter-equivalent to implementing VIB (and consequently SVIB), it seems like an important point of comparison. The lack of comparison to CEB is a significant oversight.
- In Figure 1, right-hand side, the H(\hat{Y}) circle is drawn in a way that does not respect the Markov chain constraint Y-X-Z-\hat{Y}. It is not possible to have H(\hat{Y}) overlap H(Y) in any area where H(Z) does not also overlap H(Y). Compare this to the Venn diagrams in the Conditional Entropy Bottleneck paper you cite, where similarly the Markov chain Z-X-Y prevents H(Z) from overlapping H(Y) anywhere that H(X) does not also overlap H(Y). The incorrect Venn diagram undermines the conceptual clarity of the paper.
- Line 360: repeated word: “is uninformative about about Y”.

### Questions
- I think the theoretical contribution is solid and valuable to share with the community, but I think the empirical treatment is weak. I would be very happy to increase my rating if the experiments were improved, even if they did not show that SVIB is reliably better than VIB or CEB in all of the settings considered. Whatever the outcome for SVIB on more careful preliminary experiments would be a valuable scientific contribution.

### Soundness
2

### Presentation
3

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
The paper extends the variational information bottleneck by adding an entropy regularizer to the model that predicts the target y given the latent z. This is motivated by adding and variational bounding a second info bottleneck.

### Strengths
The paper boils down to a simple to implement and intuitive loss function.

### Weaknesses
 There is a lot of justification that is somewhat verbose and subjective. The derivation is long and elaborate for what boils down to an extra regularizer with an extra tuning parameter.

Here are some detailed comments and questions:

Use \log in latex and format the integral d.

The writing may be a little verbose. Examples: lines 260-264 restates things. (7) follows trivially from (4). The sentences preceding both (4) and (7) are also similar. lines 217-254 is repeat well known material.

Line 198 why carry p(x,y) around if everything is conditional on those later? I suspect dropping that saves some hassle later.

Lines 271 to 296 would be better expanded after moving lines 217-254 to an appendix. You could be explicit about the use of the chain factorization etc (although maybe the previous point about line 198 can avoid needing to deal with this?).

Line 249 who’s -> whose

Line 334 why is Z left as an r.v.? Please explain how to handle this with sampling. I feel like this is just the entropy of the y given the sampled z, so it should be written explicitly as such?

Line 452 Val column bolded wrongly, the vanilla method should be shown as the winner not the proposed method?

Table 1: it seems as though VIB best performance is at the boundary of your sweep, so we can’t tell if SVIB beats VIB?

Table 2: as previous comment.

A plot instead of tables 5 and 6 would be easier to absorb.

Tables 1 and 2: can you not fix lambda and show improvement generally? Varying this in-sample looks like overfitting to the untrained eye (but I think this is an illusion and the results are good). It just seems like sub optimal presentation given tables 5 and 6 show good robust performance over lambda. A plot >> tables of numbers.

Section 4: showing robustness is nice, and the methodology seems very good i.e. adversarial approaches.

Line 478 private -> special

### Questions
Here are some detailed comments and questions:

Use \log in latex and format the integral d.

The writing may be a little verbose. Examples: lines 260-264 restates things. (7) follows trivially from (4). The sentences preceding both (4) and (7) are also similar. lines 217-254 is repeat well known material.

Line 198 why carry p(x,y) around if everything is conditional on those later? I suspect dropping that saves some hassle later.

Lines 271 to 296 would be better expanded after moving lines 217-254 to an appendix. You could be explicit about the use of the chain factorization etc (although maybe the previous point about line 198 can avoid needing to deal with this?).

Line 249 who’s -> whose

Line 334 why is Z left as an r.v.? Please explain how to handle this with sampling. I feel like this is just the entropy of the y given the sampled z, so it should be written explicitly as such?

Line 452 Val column bolded wrongly, the vanilla method should be shown as the winner not the proposed method?

Table 1: it seems as though VIB best performance is at the boundary of your sweep, so we can’t tell if SVIB beats VIB?

Table 2: as previous comment.

A plot instead of tables 5 and 6 would be easier to absorb.

Tables 1 and 2: can you not fix lambda and show improvement generally? Varying this in-sample looks like overfitting to the untrained eye (but I think this is an illusion and the results are good). It just seems like sub optimal presentation given tables 5 and 6 show good robust performance over lambda. A plot >> tables of numbers.

Section 4: showing robustness is nice, and the methodology seems very good i.e. adversarial approaches.

Line 478 private -> special

### Soundness
3

### Presentation
3

### Contribution
2

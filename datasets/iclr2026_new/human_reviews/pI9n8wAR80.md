## Human Reviewer 1

### Summary
This paper addresses the issue of pseudo‑label bias in long‑tailed semi‑supervised learning, and identifies two core limitations in existing Logit Adjustment (LA)–based approaches: distribution estimation distortion caused by sample redundancy, and the use of a fixed overall adjustment strength. To overcome these limitations, the authors propose the CoLA framework, whose main components include: estimating the effective number of samples via the effective rank of the representation matrix to obtain a de‑duplicated class distribution; and, based on the estimated distribution, constructing a proxy validation set and optimizing the overall adjustment strength through meta‑learning so that it adapts to the characteristics of the current distribution. Furthermore, the paper provides a theoretical generalization error bound for the proposed LMC and validates the method through experiments on benchmark datasets.

### Strengths
1. The problems identified in the paper are reasonable and important, and the authors provide a detailed analysis supported by both theoretical justification and experimental evidence.
2. The paper presents a generalization bound and a convexity analysis for the meta‑learning process, which enhances the theoretical soundness of the proposed method.
3. The visualization in the ablation study is presented in a clear and comprehensive manner.

### Weaknesses
1. The computation of effective rank and the meta‑learning procedure may introduce substantial computational overhead. It would be beneficial to include an analysis of the time complexity and computational complexity, particularly with respect to runtime performance on large‑scale datasets.
2. In the downstream experimental evaluation, I notice that the SIN‑127 dataset is a down‑sampled version of ImageNet‑127. Why not perform testing directly on ImageNet‑127? I am curious about the potential results on the full ImageNet‑127 dataset.
3. The paper lacks a primary diagram illustrating the proposed method. Introducing a main figure would make the methodology clearer and facilitate reader understanding.

### Questions
See the weaknesses.

### Soundness
2

### Presentation
2

### Contribution
3

### Rating
6

### Confidence
2

---

## Human Reviewer 2

### Summary
This paper attempts to tackle an problem in Long-Tailed Semi-Supervised Learning (LTSSL): the confirmation bias driven by biased pseudo-labels. The authors claim that existing methods based on LA suffer from two critical limitations: 1) they rely on naive frequency counting to estimate the unlabeled data distribution, and 2) they treat the overall adjustment strength as a fixed hyperparameter. The authors propose CoLA, which consists of two main components: first, a De-Duplicated Distribution Estimation (DDDE) module that attempts to estimate a more accurate class distribution by calculating the effective rank of class representations to account for sample redundancy. Second, a Logit Meta-Calibration (LMC) procedure that constructs a proxy validation set and uses meta-learning to automatically optimize the overall adjustment strength. The experiment results show that their method establishes a new state-of-the-art on four public benchmarks.

### Strengths
1. The authors do identify a potentially interesting aspect of the LA mechanism, namely the interplay between the class-wise adjustment and the overall adjustment strength. This is a reasonable observation.
2. The authors evaluate their method across multiple datasets and distribution mismatch scenarios.

### Weaknesses
1. The first of my concern is novelty. The core idea of this paper is little more than a combination of existing techniques, such as effective number, dual-branch, and meta-learning for hyperparams.
2. The description of the DDDE module is overly simplistic. The authors propose computing the effective rank for the representation matrix Zy of each class y. They fail to discuss the computational cost of this procedure.
3. In Figure2 (b,d,e), after applying LMC, the slope of the pseudo-label accuracy improvement barely changes. So I think its contribution is questionable.
4. The proxy validation set Dv is resampled from the small and imbalanced labeled set Dl. For tail classes, Dl may contain only a few samples. How do you justify that such a severely constrained proxy set can effectively guide the learning of $\tau$ for a massive and differently distributed unlabeled set Du?

### Questions
See in Weaknesses.

### Soundness
2

### Presentation
3

### Contribution
2

### Rating
4

### Confidence
4

---

## Human Reviewer 3

### Summary
The authors address in their manuscript the problem of long-tailed semi-supervised learning. They analyze the weaknesses of several methods based on logit adjustment and propose an approach CoLA that is claimed to suffer less from over-suppression. They further propose DDDE to estimate the unlabeled distribution and LMC as a meta-learning strategy. They validate their method on 4 different datasets (CIFAR-10/100-LT, STL-10-LT, and SIN-127).

### Strengths
1. The paper is well-written (with exception line 090 "each class's representations") and structured (DDDE=4.1, LMC=4.2, CoLA=4.3).
2. The main hypothesis is clearly stated and the approach is presented in a plausible way.
3. Technical parts are accurately and detailed described.
4. A good set of datasets has been selected for the experiments.
5. The results are good (even if not always beating the state of the art)

### Weaknesses
1. The related work is covering a subset of the field, important references (such as [1]) are only used in the appendix, other are completely missing e.g. [2-5].
2. The premise for the main hypothesis, i.e., the negative effect of overlooking the interplay between the two types of adjustment, has not been clearly supported by experimental results. If the premise is not properly established, all subsequent claims are affected. Figure 1b) only shows that monotonicity is not fulfilled.
3. Some statements lack evidence or reference, e.g. line 085. "current work" embraces all works, see also 1. (this is not saying that any of [2-5] does).
4. The protocol (for CIFAR) chosen according to Du et al. ICML 2024 (Simpro) deviates from other, previously published protocols, e.g. from the cited paper [6], and makes comparisons difficult, in particular to state-of-the-art methods that remained un-cited and that use those previous protocols.
5. For experiments that use compatible protocols, e.g. STL-10-LT, the proposed method is inferior to e.g. [4} and rather en par with [3]. 
6. The description of erank is not sufficiently self-contained. In particular, it is not clear why the EN is estimated by erank. Line 197 just says "we quantify EN ... using ... erank" and references point to EN and erank, but not why the quantification is possible.  Also, it is not obvious why line 205 $p(i)$ is a probability and not just a point in the $m_y$-simplex.
7. 4.2 is partly written in a procedural way and the overall approach that leads to the algorithm needs to be stated more clearly.

[1] Zhang et al. Mixup: Beyond empirical risk minimization. ICLR 2018.

[2] Lazarow et al. Unifying distribution alignment as a loss for imbalanced semi-supervised learning. CVPR 2023.

[3] Chen et al. Softmatch: Addressing the quantity-quality tradeoff in semi-supervised learning. ICLR 2023.

[4] Aimar et al. Flexible distribution alignment: Towards long-tailed semi-supervised learning with proper calibration. ECCV 2024.

[5] Kim et al. Separated and Independent Contrastive Semi-Supervised Learning for Imbalanced Datasets. IEEE Access 2025.

[6] Kim et al. Distribution aligning refinery of pseudo-label for imbalanced semi-supervised learning. NeurIPS 2020.

### Questions
1. (related to weakness 2.): which are the experimental results that clearly show that the _interplay_ of the two types of LA cause the issue? 
2. (related to weakness 4.): what results are obtained with the protocol from Kim et al. 2020 or is there some other way to make the results comparable?
3. (related to weakness 5./1.): as the statement about state-of-the-art results need to be revised: in which situation does the proposed method shows its main strengths and weaknesses?
4. (related to weakness 6.): why is the quantification possible and why is $p(i)$ a proper probability?
5. (related to weakness 7.): what is the overall approach in 4.2?

### Soundness
2

### Presentation
3

### Contribution
2

### Rating
4

### Confidence
4

---

## Human Reviewer 4

### Summary
This paper focuses on improving Long-Tailed Semi-Supervised Learning (LTSSL) by employing logit-adjustment methods. The paper identifies two key issues with the logit-adjustment approaches: 1) An over-estimation of popular class probabilities can lead to over-suppression of model predictions for the popular classes; and 2) The overall adjustment factor in the logit-adjustment approach is sensitive to particular dataset and needs to selected carefully. The paper then proposes two solutions to address these two issues, namely *de-duplicated distribution estimation* (DDDE) and *logit meta-calibration* (LMC). The paper provides a generalization analysis for LMC. The paper then provides a comprehensive empirical evidence of the value of the proposed approach while comparing it with existing logit-adjustment-based approaches and other methods beyond logit-adjustment for LTSSL in the literature.

### Strengths
- The paper studies a well motivated problem by identifying key limitations of a widely popular approach in the literature.
- The empirical results in the paper clearly showcase the improvements compared to competitive baselines from the literature. 
- The paper presents ablation results to establish the value of both DDDE and LMC.

### Weaknesses
- The generalization analysis in Section 5 does not significantly enhance the overall contributions of the paper. Does the theory inspire/motivate the method proposed in the paper? If not, does the theory provide useful guarantees towards the final performance of the proposed solution? 
- The presentation of the theoretical part of the paper can be greatly improved.
   -  Could the authors expand on the Line 298 (``If our estimation is accurate,...justifying our methodology``) and make it mathematically precise. 
   - If the reviewer understand it correctly, the only optimizing parameter in Section 5 is $\tau$ and the function class $h_{\tau}$ is linear with respect to $\tau$ (since $\tau$ is the overall logit-adjustment factor). Could the author attempt to provide a more explicit characterization of the Rademarcher complexity in this case?

### Questions
- Could you please provide a description/pseudocode of your overall method in the form of an algorithmic block or a figure?
- In Line 275, the assumption is that $P\_{X\_{u} \mid Y\_{u}}(\mathbf{x}|y) =  P\_{X\_{l} \mid Y\_{l}}(\mathbf{x}|y)$ (between $u$ and $l$). However, the importance weight in 277 deals with $P\_{X\_{u}, Y\_{u}}$ and  $P\_{X\_{v}, Y\_{v}}$. Are the authors relying on the fact that since $\mathcal{D}\_{v}$ is sub-sampled from $\mathcal{D}\_{l}$ and thus share the same class conditionals? If yes, please consider making this clearer.
- Please consider making the notations consistent. E.g., Line 286 uses $R_{P\_u}$ (with lowercase $u$) while Line 294 uses $R_{P\_U}$ (with uppercase $U$).
- Did you use the logit-adjustment form in Line 234 (as opposed to the one in Eq. (1)) for your experiments?
- Why have you used the form in Line 226 for sampling? Why can one not simply use $\hat{P}\_{Y\_u}(y\_i)$ as the probability to select $(\mathbf{x}^l\_i, y\_i)$?

### Soundness
2

### Presentation
3

### Contribution
3

### Rating
6

### Confidence
3
# Input-gradient space particle inference for neural network ensembles

- Decision: Accept
- Avg Score: 7.00
- Scores: 8, 6, 8, 6

## Abstract
Deep Ensembles (DEs) demonstrate improved accuracy, calibration and robustness to perturbations over single neural networks partly due to their functional diversity. 
Particle-based variational inference (ParVI) methods enhance diversity by formalizing a repulsion term based on a network similarity kernel.
However, weight-space repulsion is inefficient due to over-parameterization, while direct function-space repulsion has been found to produce little improvement over DEs.
To sidestep these difficulties, we propose First-order Repulsive Deep Ensemble (FoRDE), an ensemble learning method based on ParVI, which performs repulsion in the space of first-order input gradients.
As input gradients uniquely characterize a function up to translation and are much smaller in dimension than the weights, this method guarantees that ensemble members are functionally different.
Intuitively, diversifying the input gradients encourages each network to learn different features, which is expected to improve the robustness of an ensemble.
Experiments on image classification datasets and transfer learning tasks show that FoRDE %with an appropriate kernel function 
significantly outperforms the gold-standard DEs and other ensemble methods in accuracy and calibration under covariate shift due to input perturbations.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a novel method for ensembling deep models that ensures diversity of the ensemble members. The paper continues the line of work in particle-based variational inference transforming the repulsion step of this approach into an input gradient space. This is different from the existing works that have done this step in weight and function spaces.

### Strengths
* A novel method for an important problem of ensembling
* Thorough empirical evaluation and comparison to the existing methods
* Drawing connections with the existing methods
* The paper is mostly well written and easy to follow
* Runtime analysis presented

### Weaknesses
 * Some presentation unclearness (see details below)
* Some transformations between theory in Section 3 and steps in Algorithm (in Appendix) are not obvious


1. What corruption is considered? CIFAR-10/100-C datasets have several types of corruptions each of which has several level of severity of corruptions. No confidence intervals (+-) for corruption results. 
2. Section 3.1 doesn't address that the target distribution \pi is not available, or am I missing something? 
3. It would help to clear some confusion of how Algorithm comes in place if steps in Algorithm would be linked to equations in Section 3. 
4. Section 3.4. "However, in practice we found no performance degradation nor convergence issues in our experiments" - though the convergence issues can easily be observed, in order to see no performance degradation one would need to compare the performance with and without mini-batches. This experiment is not presented in the paper (including Appendix). 
5. Though the code is provided, some implementation details in text are missing. For example, ECE computation details such as a number of bins. Or details of OOD experiments: what portion of OOD data (CIFAR-100 for CIFAR-100 and vice versa) was used. 
6. No reference for CINIC10 dataset

### Questions
What exact corruption has been used in reported corruption experiments?

### Soundness
3 good

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper points out that while the repulsion in the existing weight-space or function-space repulsive deep ensembles has been theoretically well-motivated, it does not lead to a practical performance improvement compared to vanilla deep ensembles. Rather than relying on repulsion in weight or function space, the authors employ a kernel comparing input gradients of particles and propose First-order Repulsive Deep Ensembles (FoRDE). Experimental results clearly indicate that FoRDE outperforms baseline methods, particularly when dealing with corrupted data.

### Strengths
1. I have experienced that although repulsive deep ensembles are theoretically well-grounded, they do not result in performance enhancements in practice. In this regard, this paper is well-motivated, as it states, "Neither weight nor function space repulsion has led to significant improvements over vanilla DEs."
2. The paper provides a comprehensive overview of the literature concerning repulsive deep ensembles. Also, the proposed approach is meticulously detailed in a step-by-step manner, as well as its practical considerations.
3. The connection to the EmpCov prior (Izmailov et al., 2021) further clarifies why the proposed FoRDE-PCA algorithm performs well for data under common corruptions.

---
Izmailov et al., 2021,  Dangers of Bayesian model averaging under covariate shift.

### Weaknesses
Despite the critique that neither weight nor function space repulsion yielded significant improvements compared to vanilla DEs, the FoRDE algorithm introduced in this context still did not result in a substantial performance enhancement over vanilla DEs. In particular, FoRDE-Identity demonstrates a performance similar to that of vanilla DE, while FoRDE-PCA excels in performance under corruption but significantly diminishes its in-distribution performance.

The authors seem to have recognized this aspect; "Hence, we believe that the optimal lengthscales for good performance on both clean and corrupted data lie somewhere between unit lengthscales (the identity) and using the inverse square root eigenvalues as lengthscales." For this paper to be considered complete, it should not just acknowledge such ideal lengthscales but also offer experimental evidence of their practical identification. Furthermore, the paper does not sufficiently explore the trade-off between in-distribution performance and robustness to corruptions. While FoRDE-PCA shows promise in handling corruptions, the significant drop in clean data performance needs more analysis and potential mitigation strategies. The lack of a clear methodology for selecting the optimal lengthscale, beyond a qualitative statement, is a critical weakness.

The paper mentions the reasons for the ineffectiveness of weight-space repulsion: (1) "Typically repulsion is done in the weight space to capture different regions in the weight posterior. However, due to the over-parameterization of neural networks, weight-space repulsion suffers from redundancy." (2) "Weight-space repulsion is ineffective due to difficulties in comparing extremely high-dimensional weight vectors and the existence of weight symmetries (Fort et al., 2019; Entezari et al., 2022)." The explanation of redundancy could be more detailed, specifically how over-parameterization leads to redundant solutions in weight space. Also, the difficulties in comparing high-dimensional weight vectors should be elaborated, perhaps by discussing the curse of dimensionality and its impact on kernel methods in such spaces. The concept of weight symmetries, while mentioned, needs a more concrete explanation of how these symmetries undermine the effectiveness of weight space repulsion.

### Questions
1. The paper mentions the reasons for the ineffectiveness of weight-space repulsion: (1) "Typically repulsion is done in the weight space to capture different regions in the weight posterior. However, due to the over-parameterization of neural networks, weight-space repulsion suffers from redundancy." (2) "Weight-space repulsion is ineffective due to difficulties in comparing extremely high-dimensional weight vectors and the existence of weight symmetries (Fort et al., 2019; Entezari et al., 2022)." Could you provide a more detailed explanation of this?

2. The paper outlines the advantages of ensemble methods in four specific areas: (1) predictive performance, (2) uncertainty estimation, (3) robustness to adversarial attacks, and (4) corruptions. In the experimental results, it delves into (1) using ACC, (2) using NLL and ECE, and (4) using cA, cNLL, and cECE. Did you carry out any experiments regarding (3) by any chance? Considering that the current experimental results are somewhat lacking in (1) and (2), it might be worthwhile to focus more on (3) and (4).

3. FoRDE-PCA exhibits robust performance in addressing common corruptions (although it shows a minor decrease in its in-distribution performance). Hence, I would like to suggest providing more detailed experimental results concerning common corruptions, e.g., if it operates similarly to EmpCov (Izmailov et al., 2021), it is worth exploring whether the most beneficial corruption type aligns as well.

---
Fort et al., 2019, Deep ensembles: A loss landscape perspective.  
Entezari et al., 2022, The role of permutation invariance in linear mode connectivity of neural networks.  
Izmailov et al., 2021,  Dangers of Bayesian model averaging under covariate shift.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper is concerned with adapting particle based variational inference for improved training of neural network ensembles.  The authors attempt to circumvent problems that have affected previous attempts to use particle based variational inference for ensembles, with a lack of effective repulsion in weight space (intended to promote functional diversity) chief among them.  This paper proposes instead to enforce diversity in the input gradients rather than in weight space, by using Wasserstein gradient descent along with an RBF kernel defined over the input gradients to guide the particles during training.  They compare against deep ensembles and other BNNs on accuracy, calibration, and robustness to covariate shift.

### Strengths
- The paper is very well written.  The potential advantages of moving to input gradient based diversity management are well introduced & well motivated, and the explanations are largely self-contained, which is no small feat considering page restrictions for conferences.
- In particular, the main contribution section (section 3) is *so* well written.  It takes time to lead the reader from the wider view of Wasserstein gradient descent, to input space gradients, and the more narrow questions of choice of kernels, and their tradeoffs.  Of all the papers I reviewed, this was by far the most enjoyable and informative to read.  Bravo for taking the time to write so clearly.

### Weaknesses
 - One thing I often worry about is that the experiments are performed only in the vision domain, on over-hygenic datasets.  While I don't want to discount the amount of work needed to extend to other domains, projects like [WILDS](https://wilds.stanford.edu/) make this easier, and build confidence that demonstrated success isn't due to some quirk of CIFAR datasets.
- One other complaint that to the authors' credit they highlight in section 3.5 is the cost of computing FoRDEs.  At a 3x computational premium to DEs, the penalty paid in compute seems to be the largest drawback of FoRDE with respect to DEs.  Do the authors have any ideas for reducing this burden? DEs themselves are expensive in both space and time to compute.
- Regarding the motivation of the RBF kernel in the \textbf{Choosing the base kernel} paragraph of section 3.2, they are good arguments for using the RBF kernel, but are there others that were considered? As the authors suggest in section 3.3 and 3.4, choosing the length scales for RBF presents its own problem.  Could this be circumvented by employing a simpler base kernel? 
- Again in section 3.3, is the median heuristic required? I’m a little unsure at the outset why this is the solution chosen over any others that would reduce the effect of the dominant eigenvalues.

### Questions
- Regarding the motivation of the RBF kernel in the \textbf{Choosing the base kernel} paragraph of section 3.2, they are good arguments for using the RBF kernel, but are there others that were considered? As the authors suggest in section 3.3 and 3.4, choosing the length scales for RBF presents its own problem.  Could this be circumvented by employing a simpler base kernel? 
- Again in section 3.3, is the median heuristic required? I’m a little unsure at the outset why this is the solution chosen over any others that would reduce the effect of the dominant eigenvalues.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Most prior research employing particle-based variational inference (ParVI) has proven to be inefficient and has not significantly improved performance. To tackle these issues, this study presents a new ParVI approach known as the First-order Repulsive Deep Ensemble (FoRDE), which integrates repulsion principles into the realm of first-order input gradients.

### Strengths
- The idea of incorporating repulsion into first-order input gradients(not a function space or a weight space repulsion which are quite common in Bayesian Neural Network literature) to enhance functional diversity is new to the community and intriguing.
- The paper is well-written, ensuring it is easy to read and understand.

### Weaknesses
 - The scale of experiments are quite small to show the effectiveness of FoRDE.
- The overall performance gain compared to other baselines looks quite marginal for the out-of-distribution datasets, especially for the TinyImageNet which is the largest dataset. And shows lower performance compared to the other baselines for the in-distribution datasets.
- Having empirical or theoretical evidence to demonstrate the effectiveness of FoRDE in enhancing input gradient diversity would be beneficial.
- Providing empirical results that illustrate how the improved input gradient diversity effectively changes into enhanced functional diversity in deep neural network scenarios would be valuable.
- Additional hyperparameters for the kernel would be another burden for this method.

### Questions
See the weakness section

Recommend
- It is recommended to include an ethics statement and a reproducibility statement right after the main paper.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

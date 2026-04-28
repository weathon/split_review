# $\sigma$-zero: Gradient-based Optimization of \\$\ell_0$-norm Adversarial Examples

- Decision: Reject
- Avg Score: 5.50
- Scores: 6, 5, 5, 6

## Abstract
Evaluating the adversarial robustness of deep networks to gradient-based attacks is challenging.
While most attacks consider $\ell_2$- and $\ell_\infty$-norm constraints to craft input perturbations, only a few investigate sparse $\ell_1$- and $\ell_0$-norm attacks.
In particular, $\ell_0$-norm attacks remain the least studied due to the inherent complexity of optimizing over a non-convex and non-differentiable constraint.
However, evaluating adversarial robustness under these attacks could reveal weaknesses otherwise left untested with more conventional $\ell_2$- and $\ell_\infty$-norm attacks.
In this work, we propose a novel $\ell_0$-norm attack, called $\sigma$\texttt{-zero}, which leverages a differentiable approximation of the $\ell_0$ norm to facilitate gradient-based optimization, and an adaptive projection operator to dynamically adjust the trade-off between loss minimization and perturbation sparsity.
Extensive evaluations using MNIST, CIFAR10, and ImageNet datasets, involving robust and non-robust models, show that $\sigma$\texttt{-zero} finds minimum $\ell_0$-norm adversarial examples without requiring any time-consuming hyperparameter tuning, and that it outperforms all competing sparse attacks in terms of success rate, perturbation size, and efficiency.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes an algorithm utilizing gradient information to generate sparse adversarial perturbations. Compared with perturbations bounded by $l_2$ or $l_\infty$ norms, sparse perturbation is more challenging because of its non-convexity nature. The authors use a continuous function to approximate the $l_0$ norm of the perturbation and design a new loss objective function that facilitates optimizing adversarial perturbations. The experiments show the effectiveness and efficiency of the proposal algorithm.

### Strengths
Robustness against sparse perturbation is an interesting problem to explore. The algorithm is well-motivated and clearly demonstrated. The experiments are conducted on various datasets and the results indicate the advantages of the proposal algorithm over the baselines considered.

### Weaknesses
1. Although the experiments are conducted in various datasets, I think more sparse attack algorithms should be included as the baselines for comparison. For example, PGD$_0$ [A] should be included as the baseline, since it is also a white-box attack for $l_0$ bounded perturbations. Sparsefool, based on constructing sparse perturbations on top of popular deep fool method, should also be studied.

[A] Francesco Croce and Matthias Hein. Sparse and imperceivable adversarial attacks. In Proceedings of the IEEE/CVF international conference on computer vision, pp. 4724–4732. 2019.

[B] Modas, Apostolos, Seyed-Mohsen Moosavi-Dezfooli, and Pascal Frossard. "Sparsefool: a few pixels make a big difference." Proceedings of the IEEE/CVF conference on computer vision and pattern recognition. 2019.

2. The comparison might not be fair. Some algorithms are proposed in a different formulation as in this paper. Some baselines (such as Sparse-RS) are proposed to generate adversarial examples such that the $l_0$ norms of the perturbations are smaller than $\epsilon$. These algorithms are not designed to minimize the $l_0$ of the perturbation, they search for a perturbation whose $l_0$ norm is smaller than a threshold. Comparing the $l_0$ norm - ASR trade-off is probably unfair for these methods.

3. In addition to $l_2$ and $l_\infty$ robust models, I think including $l_1$ robust model for evaluating the attacks would make the experiment more comprehensive, especially considering the $l_1$ norm is the closest convex $l_p$ norm to $l_0$ norm. Possible baselines include those trained by AA-$l_1$ [C] and Fast-EG-$l_1$. [D]

[C]: Croce, Francesco, and Matthias Hein. "Mind the box: $ l_1 $-APGD for sparse adversarial attacks on image classifiers." International Conference on Machine Learning. PMLR, 2021.

[D]: Jiang, Yulun, et al. "Towards Stable and Efficient Adversarial Training against $ l_1 $ Bounded Adversarial Attacks." International Conference on Machine Learning. PMLR, 2023.

### Questions
Major concerns are demonstrated in the weakness part. In addition to these concerns, I have the following questions:

1. Function $\mathcal{L}$, as defined by Equation (7), is not continuous and thus not differentiable everywhere. Will this cause some problems when calculating the gradient of $\mathcal{L}$ in line 4 of Algorithm 1? I think using a continuous and differentiable function as the loss objective would be better.

2. Regarding Sparse-RS with a super-script 100 or 85. If understood correctly, these super-scripts mean the value of k, max allowed $l_0$ norm of the perturbations, why Sparse-RS100 is worse than Sparse-RS85? And why the average $|\delta|_0$ is bigger than the corresponding k in some cases?

Due to the major concerns and questions as pointed out, I cannot recommend acceptance. I welcome the discussions with the authors and will reconsider my rating.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper proposes $\sigma$-zero, a white-box adversarial attacks for the $\ell_0$-threat model. In particular, $\sigma$-zero obtains sparse perturbations minimizing a differentiable surrogate of the $\ell_0$-norm. In the experiments on several datasets and target classifiers, $\sigma$-zero is shown to outperform existing attacks in terms of success rate and and size of the perturbations.

### Strengths
- The proposed approach of using a differentiable approximation of the $\ell_0$-norm is reasonable, and yields a simple method.

- The effectiveness of $\sigma$-zero is supported by the experimental results.

### Weaknesses
 - The configuration in which some of the competitors are used seems suboptimal:
    - BB can be initialized from an image of another class or another dataset, as done in [A, B], to avoid the issue of not finding a starting point (as mentioned in Sec. 3.2).  
    - If I understand it correctly, Sparse-RS is re-run with different sparsity levels until reaching the desired success rate (averaged over the test points), but then the results are reported for all points with the same sparsity level. In this case, the results would be suboptimal, as the binary search should ideally be done for each point individually (for comparison to $\sigma$-zero and other attacks which optimize the perturbation size independently for each test image). As a cheaper solution, one could run Sparse-RS on several $k$ values, and the select for each point the smallest $k$ which finds an adversarial perturbations. 
    - In general, while the paper uses the default parameters for all baseline attacks, it's not clear whether these are optimal: ideally, one could tune (some of) them on a small subset of test cases (models or datasets).
    - Sparse-RS is a black-box method, i.e. doesn't need a backward pass at each iteration, which means that using the same number of iteration as for the white-box attacks results in significantly lower computational cost (e.g. 2x fewer network passes). How would the results compare when equating the number of network passes?

- The overall technical contribution is limited: while the proposed algorithm has some task-specific solutions, e.g. inducing sparsity in $\delta$ by clipping the smallest components, the $\ell_0$-norm approximation has already been used in the context of adversarial robustness (Cinà et al., 2022).

### Questions
Since the experimental results are the main part of the paper, I think it is important that the configuration in which the baselines are used is clarified to provide a comprehensive comparison and assess the effectiveness of the proposed method.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes $\sigma$-zero attack, a sparse attack gained by minimizing the norm-0 of the perturbation.

### Strengths
- The idea is simple and intuitive. 

- The experimental results look good.

### Weaknesses
 -  The adversarial images created by the proposed approach do not look visually appealing according to Figure 3. It is easy to spot out highly-intensive pixels.

-  The purpose of adversarial attacks is to generate visually appealing images that is imperceptible to human vision. Therefore, less norm-0 perturbations do not mean better visually appealing adversarial images. I feel that although this approach can help to restrict the number of pixels perturbed, it tends to perturb other pixels more, leading to adversarial images as in Figure 3.

- The norm-0 solely is not adequate to measure the quality of generated adversarial images. The norm-0 of the proposed approach is smaller because it directly minimize an approximation of the norm-0. It would be better if the paper reports some other metrics such as  SSIM, PSNR, and LPIPS.

- Moreover, the robust classifiers in RobustBench are trained mostly with $\ell_\infty$ and $ell_2$, hence they cannot defend well the proposed approach. What does it happen if we train a robust classifier with 20-steps $\sigma$-zero and then evaluate on the same attack with 100 steps?

### Questions
Please refer to the weakness section.

### Soundness
3 good

### Presentation
3 good

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
This paper propose a $l_0$-norm attack, called $\sigma$-zero, which leverages an differentiable approximation of the $l_0$  norm to facilitate gradient-based optimization.

### Strengths
This paper's primary contribution lies in its application of the $l_0$ norm approximation function, as introduced by Osborne et al. (2000b), to $l_0$ attacks. The research presents thorough experiments on various robust models (e.g., C1-C8) presented in Robustbench and multiple datasets. 

When compared with existing sparse attacks, the results convincingly demonstrate that sigma-zero outperforms in terms of attack rates and offers reduced computational costs.

While the authors have included the code in the supplementary materials, I haven't personally tested it. Nonetheless, I anticipate that the broader community will benefit once the authors make their code publicly available in the future.

### Weaknesses
A primary shortcoming of the paper is its resemblance to an experimental or technical report rather than a comprehensive academic study.

The discussion about the scientific principles about why $\sigma$-zero performs better is quite sparse in the current presentation.

Additionally, the term "VRAM" is not defined. It would enhance clarity if its full name were provided initially for the readers not familiar with.

### Questions
see weakness.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

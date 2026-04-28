# Training Bayesian Neural Networks with Sparse Subspace Variational Inference

- Decision: Accept
- Avg Score: 6.67
- Scores: 6, 8, 6

## Abstract
Bayesian neural networks (BNNs) offer uncertainty quantification but come with the downside of substantially increased training and inference costs. Sparse BNNs have been investigated for efficient inference, typically by either slowly introducing sparsity throughout the training or by post-training compression of dense BNNs. The dilemma of how to cut down massive training costs remains, particularly given the requirement to learn about the uncertainty. To solve this challenge, we introduce Sparse Subspace Variational Inference (SSVI), the first fully sparse BNN framework that maintains a consistently highly sparse Bayesian model throughout the training and inference phases. 
    Starting from a randomly initialized low-dimensional sparse subspace, our approach alternately optimizes the sparse subspace basis selection and its associated parameters. While basis selection is characterized as a non-differentiable problem, we approximate the optimal solution with a removal-and-addition strategy, guided by novel criteria based on weight distribution statistics. Our extensive experiments show that SSVI sets new benchmarks in crafting sparse BNNs, achieving, for instance, a 10-20× compression in model size with under 3\% performance drop, and up to 20× FLOPs reduction during training compared with dense VI training. Remarkably, SSVI also demonstrates enhanced robustness to hyperparameters, reducing the need for intricate tuning in VI and occasionally even surpassing VI-trained dense BNNs on both accuracy and uncertainty metrics.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper, the authors present an approach to train sparse-BNNs using sparse subspace variational inference. The authors show that their approach gives computation gains during training as well as during test-time inference.

### Strengths
- The paper is well-motivated. Using BNNs in practice naively requires lot of compute which can hamper its adoption 

- The experimental results provided by the paper are impressive. Having training time benefits is extremely useful. 

- I also appreciate the fact that the authors have provided the implementation for their work.

### Weaknesses
 - I think related relevant work is missing [1, 2]. Especially the work by Vadera et al.[1], looks at sparse SGHMC for BNNs, which could be easily extended to VI and when doing so would look similar to what the authors have proposed. The authors should highlight the difference between their work and existing work. 

- The empirical results seem insufficient. The authors haven't mentioned the model architecture used in their experiments. Also, to really emphasize the usefulness of the proposed approach, it would be important to have empirical results on an expanded set of datasets + models + tasks (including UQ tasks such as OOD detection, misclassification detection, etc.)

- I think the presentation can be improved. The authors introduce complex notations, but after reading through section 3 twice, I believe that it can be greatly simplified. For e.g., where exactly is eq 2 reconciled in the algorithm? Based on my reading, the paper would have been fine to totally exclude eq 2.

### Questions
- Is eq 2 being really used somewhere directly? 

- What's the model architecture used in experiments? 

- Apart from implementation, can the authors highlight the diff between their work and that of Vadera et al.? 

- How would you extend this to other approximate Bayesian inference techniques, apart from mean-field VI? 

- It'll be useful if the authors can demonstrate the quality of uncertainty metrics coming out of the BNNs in their approach on downstream tasks. See [3] for example.

References

[3] Vadera, M., Li, J., Cobb, A., Jalaian, B., Abdelzaher, T., & Marlin, B. (2022). URSABench: A system for comprehensive benchmarking of Bayesian deep neural network models and inference methods. Proceedings of Machine Learning and Systems, 4, 217-237.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a novel inference method for sparse Bayesian neural networks based on variational inference, namely Sparse Subspace Variational Inference (SSVI). The idea, that is different to the previous sparse BNNs, is to explicitly keep the number of non-zero weights in the neural network fixed while updating which weights are included or excluded as non-significant. This is in contrast to the existing literature, where sparsity is induced by special priors and, firstly, still starts with a dense model that is sparsified during training, which still make inference during training computationally expensive. Secondly, sparsity-inducing priors do not allow to set a specific level of sparsity, which may require a user to play with hyperparameters of the prior to get the desired level of sparsity. The proposed method has a level of sparsity as a hyperparameter and it is fixed from the start of the training, saving computational efforts from the start. Experiments in CIFAR-10/100 show the superiority of the proposed method in comparison to other sparse NNs in accuracy, loss, ECE, and training FLOPs.

### Strengths
* Interesting new idea for sparse BNNs, that:
* ... is shown to be working empirically
* ... has a solid theoretical model that is intuitive
* ... brings significant benefits in terms of computational cost

Originality: The idea presented in the paper appears to be novel. 

Quality: The proposed method is well defined and all the inference steps seem to be sound. The experiments are well designed and executed. Ablation study is presented to different aspects of the method. 

Clarity: The paper is very well written and easy to follow. 

Significance: I believe the paper is of extreme interest for the Bayesian deep learning community as it addresses the problem of scaling inference of BNNs that is a known issue of the concept-appealing approach.

### Weaknesses
All of the below is not major weakness points.

Originality: A bit of context in terms of BNNs is missing. The review of the existing methods solely (though understandably) focusses on sparse models, leaving behind other approaches of making efficient Bayesian inference for NNs. E.g., Cobb, A.D. and Jalaian, B., 2021. Scaling Hamiltonian Monte Carlo inference for Bayesian neural networks with symmetric splitting. In Uncertainty in Artificial Intelligence (pp. 675-685). PMLR.

Quality: The empirical evaluation of the model though done rather thoroughly but only on 2 medium-size/complexity datasets from the same domain on 1 architecture. It would be interesting to see more experiments. 

Clarity: Though the model is mostly well-written, there are some moments that are missing. See details below.

Specific comments:
1.	Abstract. 20x compression, 20x FLOPs reduction – in comparison to what?
2.	Abstract. “surpassing VI-trained dense BNNs” – in terms of what?
3.	Figure 1. Not defined names of baselines.
4.	Eq. (3) it is better to include explicitly what is the operator in the last 2 equations
5.	Around eq. (4). What are p, B, q, W?
6.	Eq. (5). What is l?
7.	Table 1. What is the difference between row 2 and 3 and then 5 and 6?
8.	It is unclear about eq. (11) and (12) (from the appendix), which one is used at the end?

Minor:
1.	Ablation study on updating \phi. ‘… in Figure 3. the optimal …’ -> The

### Questions
I like the paper, my minor weakness findings are listed above, but there is nothing the authors should or could address during the rebuttal.

### Soundness
3 good

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a procedure for training sparse Bayesian neural networks with a factorized variational distribution. It does so by alternating between optimizing the parameters of a subset of the weight distributions, with the remaining ones zeroed out, and updating the subset of non-zero weights by adding to and removing from that subset based on a range of criteria. The experiments show improved accuracy and calibration on CIFAR10/100 over methods from the literature at higher sparsity.

Overall, I would say that the paper introduces some reasonable but not ground-breaking technical material, however it is let down by a severely limited evaluation, omitting most standard uncertainty estimation benchmarks. With some further issues around overclaiming novelty, I would argue for rejecting the paper in its current form.

POST REBUTTAL UPDATE:
Thank you for the extensive updates. These largely address my core concerns (limited evaluation, lack of demonstration of difference between pruning scores), so I will raise my score. I would suggest at least referencing Appendix D from the main text and if possible moving some figures to the experiment section.

I did not see an update to the paper reflecting W4. I completely agree that the method has limitations, my point is only that it is not a post-hoc pruning approach and the paper shouldn't misrepresent this.

### Strengths
- the paper is overall clear in what it does and why. It shouldn't be too difficult to implement the method based on the description.
- selection criteria for weight pruning may be of independent interest.
- there is a decent range of ablation studies on various aspects of the proposed method.
- performance on the datasets and metrics under consideration is better than that of the baselines.

### Weaknesses
1.  the experiments are quite bare-bones for a BNN paper, there is no evaluation of predictive uncertainty besides calibration -- we don't need a Bayesian approach do well on this metric. I would either suggest adding e.g. a temperature scaling baseline applied to a sparse deterministic net or (preferably) the usual out-of-distribution and distribution shift benchmarks. The lack of OOD evaluation is a significant oversight, as a core motivation for Bayesian methods is robust uncertainty quantification, which is not demonstrated by calibration alone. Specifically, the paper should include metrics such as AUROC and AUPR on standard OOD datasets like SVHN or CIFAR-10/100 corrupted versions.
2.  primarily testing at a single sparsity level as in Table 2 also seems a bit limited to me. In my view, there are broadly two possible goals when using sparsity: opitimizing sparsity at a given performance level, e.g. close to optimal, or optimizing performance at a given sparsity level. I would have liked to see more figures in the style of Figure 2 left and Figure 3 to cover both of these settings also for the baselines. The current evaluation does not sufficiently explore the trade-off between sparsity and performance, and it is unclear how the proposed method compares to baselines across a range of sparsity levels.
3.  I would have liked to see a bit more in-depth investigation of the pruning criteria, e.g. a plot of Spearman correlations between the preferred score and the others throughout training or a correlation matrix at various stages (say beginning, halfway through and end of training). I must say that I am not overly convinced that they matter too much, the variation of accuracy in Fig 2 seems to be only about 0.5% (although see questions). So I think it might be worth saving the page discussing the criteria in fewer of more thorough experiments. The current analysis of pruning criteria is superficial, and it's not clear if the proposed criteria offer a significant advantage over simpler alternatives. A more detailed analysis, such as tracking the evolution of the correlation between different pruning scores during training, is needed to justify the complexity of the proposed criteria.
4.  the paper makes some rather inaccurate claims vs the existing literature. In particular, it is not the first paper introducing a "fully sparse BNN framework that maintains a consistently sparse Bayesian model through- out the training and inference", this statement also applies to the (Ritter et al., 2021) paper, which is incorrectly cited as a post-hoc pruning paper (the paper does use post-hoc pruning as an optional step to further increase sparsity, but the core low-rank parameterization is maintained throughout training). This doesn't affect the contribution of course, but prior work needs to be contextualized correctly. The mischaracterization of existing work undermines the novelty claims of the paper. The paper should accurately represent the contributions of related methods, especially those that also maintain sparsity throughout training, such as the low-rank parameterization approach in Ritter et al., 2021.
5.  I don't really see the need to make such claims in the first place, it is not obvious that sparsity in training is desirable. Of course it may be the case that a larger network that would not fit into memory without sparsity performs better, but then this needs to be demonstrated (or like-wise any hypothetical training speed increases resulting from a reduced number of FLOPs - in the age of parallelized computation, that is a mostly meaningless metric if it cannot be shown that a practical implementation can lead to actual cost savings).
6.  the abstract is simultaneously wordy and vague. I did not know what the paper was doing specifically after reading it, even though it really isn't hard to describe the method in 1 or 2 sentences. I would say that the low-rank/basis terminology led me in the wrong direction of thinking and a pruning-based description would have been clearer, but this may of course differ for readers with a different background.

### Questions
- how are the mean values initialized for weights that are added to the active set? I assume 0? Do you reuse the old value if a weight had been temporarily removed?
- I'm not sure I follow the discussion of Figure 2 right. For the initialization of the variance of a mean-field Gaussian, identical considerations apply as for the initialization of weights in deterministic networks, so loosely speaking we want to scale the sum of variance of the means and the initial value of the variance parameter inversely with the number of units to avoid the activations diverging with increasing depth. So to me it seems natural, that dense VI would reach this critical threshold before a pruned variance, as the latter is simply removing terms from a positive sum and thus decreasing variance. Am I missing something/misinterpreting the figure?
- Can you demonstrate any practical benefits from sparsity during training/the FLOP reduction translating to real time speedups?

For suggestions see weaknesses.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

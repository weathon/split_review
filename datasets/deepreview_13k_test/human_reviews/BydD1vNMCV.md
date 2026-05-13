# Statistical Inference for Deep Learning via Stochastic Modeling

- Decision: Reject
- Scores: 5, 5, 5

## Abstract
Deep learning has revolutionized big data analysis in modern data science, however, how to make statistical inference for deep neural networks remains largely unclear. To this end, we explore a stochastic 
variant of the deep neural network known as the stochastic neural network (StoNet). Firstly, we show that the StoNet falls into the framework of statistical modeling. It not only enables us to address fundamental issues in deep learning, such as structure interpretability and uncertainty quantification, but also provides with us a platform for transferring the theory and methods developed for linear models to the realm of deep learning. Specifically, we show how the sparse learning theory with the Lasso penalty can be adapted to deep neural networks (DNNs) from linear models; establish that the sparse StoNet is consistent in network structure selection; and provides a recursive method to quantify the prediction uncertainty for the Stonet. Furthermore, we extend this result to the DNN by its asymptotic equivalence with the StoNet, showing that consistent sparse deep learning can be obtained by training a DNN with an appropriate Lasso penalty. Additionally, we propose to remodel the last hidden layer output and the target output of a well-trained DNN model using a StoNet on the validation dataset, and then assess the prediction uncertainty of the DNN model via the Stonet. The proposed method has been compared with conformal inference on extensive examples, and numerical results suggests its superiority.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors present a follow up on the work on StoNet, a model where the intermediate outputs of the layer are treated as latent variables.

The authors provide several results helping to understand the behaviour of StoNet and empirical simulations showing its performance on real-world data.

### Strengths
The paper involves an interesting idea of StoNet, but this appears to be heavily based on the previous work.

### Weaknesses
The differences in Table 1 look very small and I wonder if they are statistically significant at all?

I think more empirical evidence would make the paper stronger. The authors discuss scalability, but there's only one experiment with bigger networks (Table 2) where the gains are very marginal?

I don't think overparametrisation of the NNs is necessarily a bad thing, it seems more like an open research question?

The proposed MAP learning does not really utilise the power of the probabilistic model.

The authors should compare in more detail to existing approaches introducing noise to the network, e.g. Gaussian dropout. Overall, I think the work should be more linked to the existing research.

There are works considering similar treatment as section 4 that should be at least cited, e.g. [1].

The developed theory mostly relies on the convergence of MAP/MLE, which happens to be very slow in practice.

[1] Anqi Wu, Sebastian Nowozin, Edward Meeds, Richard E. Turner, José Miguel Hernández-Lobato, Alexander L. Gaunt Deterministic Variational Inference for Robust Bayesian Neural Networks

### Questions
See weaknesses.

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper is based on StoNet, a stochastic version of a deep neural network where in each layer, (Gaussian) noise is injected into the latent predictions. The authors study how sparsity regularization influences results obtained from StoNet and suggest to propagate uncertainty through the network to obtain prediction uncertainty.

### Strengths
- [S1] Originality: As far as I can tell, the authors are the first to study sparsity regularization in StoNet
- [S2] Clarity: The paper is well written and easy to read

### Weaknesses
- [W1] Soundness: 
    + Some assumptions (already in StoNet) seem to be not realistic (see C1) 
    + It's unclear, how the algorithm actually enforces sparsity (see C2)
    + The empirical experiments are limited (see C3)
    + Theoretical guarantees for selection and subsequent inference are not perfectly clear (see Q1, Q2)
- [W2] Originality / Novelty: It often does not get clear what the additional contribution is when compared to StoNet; see also first point on experiments in C3
- [W3] Quality / Presentation: quality of some graphics is really bad (Fig 2 and 3 almost not possible to read)


### Comments:

- [C1]: There is no one "true parameter" in deep neural networks given their [overparametrization-induced and hidden symmetries](https://openreview.net/pdf?id=FOSBQuXgAq) and I don't see how Assumption A2 holds in practice. While the authors recognize this, writing "Given nonidentifiability of the neural network model, Assumption A2 has implicitly assumed that each $\theta$ is unique up to the loss-invariant transformations, e.g., reordering the hidden neurons of the same hidden layer and simultaneously changing the signs of some weights and biases", it does not get clear what this restriction of the Assumption implies and does certainly not account for scaling symmetries present in ReLU networks or hidden symmetries as mentioned above.
- [C2]: How is the model optimized with a Lasso penalty given that this penalty is [non-smooth and stochastic variants hence do not yield exact-zero solutions](https://arxiv.org/pdf/2307.03571.pdf)?
- [C3]: the experiments 
    + mainly present coverage rates and calibration results and it is unclear how much of this performance comes from StoNet itself (missing ablation study)
    + only contain one simulation study with a fixed setup (restrictive)
    + do not elaborate on the selection quality except for the small simulation study (missing empirical evidence)

### Questions
- [Q1] what seems a bit like magic to me: the paper proves consistent structure selection but without any requirements on the feature matrix (writing "almost any training data"). Afaik it requires rather restrictive assumptions [e.g., here](https://arxiv.org/pdf/1603.06177.pdf) even in much simpler cases such as $l_1$-regularized linear models. Maybe I overlooked that in all the assumptions in the Appendix. Would be great if authors could elloborate on this.
- [Q2] further: how comes that it requires special techniques -- again even in the linear Lasso model -- to obtain valid inference after selection (post-selection inference) and this is not a problem in this much more complicated network?
- [Q3] See C2

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this paper, authors show how the sparse learning theory with Lasso penalty can be adapted to deep neural networks (StoNet) from linear models, and provide a recursive method named post-StoNet to quantify the prediction uncertainty for StoNet.

The numerical results suggest that the StoNet significantly improves prediction uncertainty quantification for deep learning models compared to the conformal method and other post processing calibration methods.

### Strengths
1. The work is a combination of existing methods including StoNet, IRO, ASGMCMC and Lasso penalty.
2. The background introduction, problem definition and theoretical derivation are well-described.

### Weaknesses
1. The main issues of this paper including **novelty and soundness of the results**.
2. Abstract description is not clear, and writing needs to be improved.
3. Comparision with other method is too few and experiment performance improvement is marginal.

### Questions
1. In Figure 2, there is slight difference with regard to overall distribution between StoNet and DNN. The variance of StoNet is larger than DNN, which seems like that vanilla DNN performs better than StoNet. The result is confusing.
2. Figure 3 lacks legend, what does lines of different color represent?
3. In Table 2, the ACC results (mean and std.) of 'No Post Calibration' method and 'Temp. Scaling' method are exactly the same, which is counter-intuitive and is of low probability, what is the reason.
4. As for result in Table 3, the compared method (Vovk et al., 2005) is proposed too long ago. To be more convincing, further ablation study should be done, for example, compare with vanilla StoNet or other related works.
5. In Table 1 and 2 of Liang et al. (2022), results of massive datasets and methods are listed, which is not discussed in this paper.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

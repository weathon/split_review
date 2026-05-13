# Evaluating and Improving Subspace Inference in Bayesian Deep Learning

- Decision: Reject
- Scores: 3, 6, 5

## Abstract
Bayesian neural networks incorporate Bayesian inference over model weights to account for uncertainty in weight estimation and predictions. Since full Bayesian inference methods are computationally expensive and suffer from high dimensionality, subspace inference has emerged as an appealing class of methods for approximate inference, where inference is restricted to a lower-dimensional weight subspace. Despite their benefits, existing subspace inference methods have notable pitfalls in terms of subspace construction, subspace evaluation, and inference efficiency. 
In this work, we conduct a comprehensive analysis of current subspace inference techniques and address all the aforementioned issues. 
First, we propose a block-averaging construction strategy that improves subspace quality by better resembling subspaces built from the full stochastic gradient descent trajectory. Second, to directly evaluate subspace quality, we propose novel metrics based on the Bayes factor and prior predictive, focusing on both goodness-of-fit and generalization abilities. Finally, we enhance inference within the subspace by leveraging importance sampling and quasi-Monte Carlo methods, significantly reducing computational overhead. Our experimental results demonstrate that the proposed methods not only improve computational efficiency but also achieve better accuracy and uncertainty quantification compared to existing subspace inference methods on CIFAR and UCI datasets.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The authors proposed a novel method of constructing low-dimensional subspace (BA) that allows the aggregate entire weights trajectory during SGD rather than the trajectory tail. The authors argue that their method is not only as computationally effective as the Tail Trajectory (TT) method but improves inference quality by better capturing the subspace landscape. Then the authors provide a simple method to evaluate the quality of constructed subspaces based on the Bayes Factor. They apply the proposed estimator and show that the subspaces constructed from the BA trajectory outperform those from TT. At last, the authors propose a new method of Bayesian Inference in the newly constructed subspace. They combine Importance Sampling with the randomized quasi-Monte Carlo method to get an estimator with a better convergence rate.

The authors provide multiple experiments to assess the quality of the proposed subspace as well as the RQMC-IS method and argue that those algorithms achieve higher test accuracy

### Strengths
1. The authors provide a full explanation of technical detail, including all architecture details and training process.

### Weaknesses
1. The novelty of the proposed algorithm is arguable. The only difference between the proposed Algorithm 1 and Algorithm 2 from [1] is that the latter uses the last point in each block (that is defined by the appropriate choice of hyperparameter c: moment update frequency) when Algorithm 1 uses the mean point in the block.
2. Figure 2 seems to be misleading because both BA and TT subspaces are constructed from the SGD points after some initial warm-up process that is the same in the proposed paper and in [1]. For example, for Synthetic Regression, both methods use the last 1000 points, while for the CIFAR dataset, they use the last 140 points.
3. The conclusion that the proposed BA and RQMC-IS have a better quality is based mostly on Tables 4, 5, 7, 9, 10, 12, 13, 16, and 17, where most of the numbers in each line are within the standard deviation of one another. From my point of view, the provided results don't show any statistically significant difference between BA and TT or between RQMC-IS and ESS/VI. I advise authors to provide a more detailed analysis of the metrics and show that there is a definitive difference between methods. For example, one can provide a similar Figure as Figure 4 from [1].
4. Some of the tables provide incomplete comparisons between methods. For example, TT (RQMC) is missing from Tables 7 and 8. Also, there is no comparison between RQMC and SNIS.
5. There is some inconsistency between the results from the paper and the prior work. For example, Figure 4 is used to argue that compared to the TT subspace, the BA subspace reflects higher uncertainty in data-sparse regions and higher confidence in data-rich regions. However, Figure 4 (middle) should be the same as Figure 3 (ESS, PCA Subspace) from [1], where TT captures uncertainty the same way BA does. Is there any difference in the experiment setup that caused this difference?
6. The proposed sampler RQMC-IS seems to require evaluation of $p(D|z)$ using all training data and couldn't be estimated using mini-batches, which makes this method practically useless for large neural networks and large datasets. At the same time VI can be performed by Doubly Stochastic VI using mini-batches that drastically improve speed. What type of VI did the authors use in their paper? Have they considered comparison with SVI [2] or other scalable methods?

### Questions
Please see the weaknesses for questions and improvements.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This work proposes a bayesian subspace inference method, focusing on three aspects, i.e., subspace construction, subspace evaluation, and inference efficiency. Correspondingly, the block-averaging scheme, bayes factor construction, and some importance sampling techniques are leveraged. In general, the problem studied in this work is interesting, however, the current content does not show significantly appealing advantages. Thus, the following comments in the review system are raised. I would be willing to raise my scores if my concerns or possible misunderstandings are well addressed in the rebuttal.

### Strengths
1. The problems addressed are interesting.

2. The paper is easy to read and the proposed method is quite relevant to many researches in  DL optimization.

3. The proposed evaluation metric appears to be the most interesting aspect to me, personally.

### Weaknesses
Weakness
1. The BA scheme seems not sufficiently novel, as I saw it somewhat like downsampling to the full trajectory, which is closely related to some existing works (see questions below).

2. Despite the importance and efficacy of the proposed evaluation metric, it feels hard to find the practical use and values in helping the optimization or inferencee process, rather than simply being a metric that shows one method outperforms one another, because we can also just compare the inference results with other metrics to compare  (see questions below).

3. In the current numerical experiments, the evidence to the inference efficiency is insufficient in comprehensive evaluations, as it is claimed as one of the main contribution of this work  (see questions below).

### Questions
1. Is it appropriate to interpret the proposed subspace construction method as a kind of downsampling scheme to the FT method?  

There are some recent literature missing in this work, e.g., SWA [1], TWA [2], DLDR [3]. In [1], the algorithm can be regarded as special case for TT. In [2], the subspace can be flexibly constructed by utilizing the checkpoints in the training head stage, tail stage, and even the fine tuning stage, the later of which meaning that a downsampling scheme can be applied to FT, to some extend. In [3], it samples some checkpoints in the trajectory, commonly in the stage where a descent performance is already gained (informally saying a downsampling to the “almost FT”).  

Please provide more explanations on the novelty and propertied of the proposed methods, and also more discussions w.r.t. the existing work, i.e., 

- explain how the block-averaging (BA) method differs from or improves upon SWA, TWA, and DLDR.

- provide a more thorough comparison table or discussion that highlights the key differences and potential advantages of BA over these existing methods.

-  clarify the novel aspects of BA that go beyond simple downsampling, if any.

 [1] P. Izmailov, D. Podoprikhin, T. Garipov, D. Vetrov, and A. G. Wilson, Averaging weights leads to wider optima and better generalization, UAI, 2018. 

[2] T. Li, Z. Huang, Q. Tao, Y. Wu, and X. Huang, Trainable weight averaging: Efficient training by optimizing historical solutions, ICLR, 2023. 

[3] T. Li, L. Tan, Z. Huang, Q. Tao, Y. Liu, and X. Huang, Low dimensional trajectory hypothesis is true: DNNs can be trained in tiny subspaces, IEEE TPAMI, 2022. 



2. If the answer to question 1 is yes. The results in table 1 is obvious, so I don’t see much importance of taking much length showing table 1.  

Nonetheless, it is really interesting to see the results in Figure 3, showing the significance of the proposed evaluation metric on the condition that the testing data evidence ratios are informative comparison baselines.  Since it is proposed as an evaluation metric on the quality of the constructed subspace. However, during the construction or some tuning towards obtaining the subspace, I didn’t notice how such metric is utilized, e.g., we can leverage such metric is determine the dimensions $k$ or $M$, etc. From the existing results, I only saw that this metric is simply used to show that BA is better than TT, which is less informative, as anyways we can use inference performance metrics to compare.  

Please elaborate the utility of the proposed metric, i.e.,  
- demonstrate how their proposed metric (Bayes factor and evidence ratio) can be used to guide hyperparameter selection, such as choosing optimal values for k or M.

- discuss potential applications of these metrics beyond just comparing BA to TT, such as in model selection or uncertainty quantification tasks or possibly provide examples of using these metrics during the subspace construction process to iteratively improve subspace quality.

- explain how these metrics offer insights that traditional performance metrics may not capture.


3. Some minor aspects: the computational cost of obtaining this metric can also be explained with some details; In table 2, I did’t see much advantage of BA over TT and FT; rather than comparing the performance and efficiency jointly in a simple table, I would suggest to have some comparisons specifically on the efficiency.

- a more detailed analysis of the computational costs associated with calculating the proposed evaluation metrics.

- some separate demonstration that focuses solely on comparing the computational efficiency of BA, TT, and FT methods.

- discuss potential reasons for the non-distinctively advantageous performance of BA in Table 2; are there any trade-offs involved?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposed 3 modifications to the existing subspace Bayesian inference methods, targeting at (1) subspace construction; (2) direct subspace quality evaluation; and (3) subspace sampling. Specifically, the author improves the tail trajectory subspace construction (only take the last few samples) by taking spread samples across the entire trajectory, covering broader range of dynamics. The author also propose direct evaluation of subspace quality based on the Bayes factor (evidence likelihood ratio). Last but not least, the author also proposed to use important sampling or quasi-MC for subspace sampling. Empirically, the proposed method is tested on UCI and image classification, demonstrating the improved performance compared to the existing one.

### Strengths
The paper is clearly written and very easy to follow. The idea of using separated samples to reconstruct the subspace is straight-forward but effective. The combination of block-averaging (BA) subspace reconstruction and quasi-MC is simple but seems to be effective empirically.

### Weaknesses
The overall methodology seems to be a straightforward combination of three existing (with minor modifications) approaches. To demonstrates its benefits, it would be great to cite/perform comparisons with other Bayesian inference techniques. 

Another questions I have is during the subspace reconstruction, do you need to flatten the matrix from $mxn$ to $d$? Doesn't this destroy the structural information stored in the original weight matrix? For example, matrix multiplication Wx represents each row of W is dot product with x, this is a kind of structural information stored within the matrix. If you flatten this, you loose such info. Is this because flatten W and then perform SVD can give you a much lower low-dimensional $z$, compared to performing SVD on the matrix W? 

What if you keep the matrix structure, but perform SVD on the matrix trajectory to get USV^T, and treat S as your Z? 

For the image classification and UCI, I am curious about the full trajectory performance. Why don't you report it?

### Questions
See above.

### Soundness
3

### Presentation
3

### Contribution
2

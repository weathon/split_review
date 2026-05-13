# Distribution-free Data Uncertainty for Neural Network Regression

- Decision: Accept
- Scores: 8, 5, 5, 8

## Abstract
Quantifying uncertainty is an essential part of predictive modeling, especially in the context of high-stakes decision-making. While classification output includes data uncertainty by design in the form of class probabilities, the regression task generally aims only to predict the expected value of the target variable. Probabilistic extensions often assume parametric distributions around the expected value, optimizing the likelihood over the resulting explicit densities. However, using parametric distributions can limit practical applicability, making it difficult for models to capture skewed, multi-modal, or otherwise complex distributions. In this paper, we propose optimizing a novel nondeterministic neural network regression architecture for loss functions derived from a sample-based approximation of the continuous ranked probability score (CRPS), enabling a truly distribution-free approach by learning to sample from the target's aleatoric distribution, rather than predicting explicit densities. Our approach allows the model to learn well-calibrated, arbitrary uni- and multivariate output distributions. We evaluate the method on a variety of synthetic and real-world tasks, including uni- and multivariate problems, function inverse approximation, and standard regression uncertainty benchmarks. Finally, we make all experiment code publicly available.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper presents an for modeling aleatoric uncertainty in neural network regression tasks using a nondeterministic architecture optimized with loss functions derived from the continuous ranked probability score (CRPS). The method enables learning arbitrary output distributions in a nonparametric way by training the network to generate samples from the target's aleatoric distribution and the training the underlying model for regression. The authors present interesting results on inverse MNIST and a set of synthetic and non-synthetic UCI datasets.

### Strengths
- I like the fact that this paper focuses on aleatoric uncertainty as opposed to total uncertainty or epistemic uncertainty. Aleatoric uncertainty has been largely overlooked 

- The architecture choice is very interesting and intuitive and the results presented are very useful. The loss function is also described well theoretically and it's nice to see it build upon existing literature for a new task. 

- The paper presents extensive experiments on both synthetic and real-world datasets, including univariate and multivariate problems.

### Weaknesses
- Heteroscedatic regression where we explicitly model the prediction and the uncertainty around it is very related to this line of work. However, the authors do not describe why should one prefer that line of work versus their approach. See [1] for an example on heteroscedatic regression. 

- While the authors do acknowledge it, the current method can be computationally expensive. This might be problematic as we try to scale larger architectures.

References

[1] Korattikara, A., Rathod, V., Murphy, K. and Welling, M., 2015. Bayesian dark knowledge. arXiv preprint arXiv:1506.04416.

### Questions
- Isn't heteroscedatic regression also modeling aleatoric uncertainty by explicitly putting an uncertainty on the outputs? 

- I think it'll be useful if you also explain why are we focused on cumulative distribution and expanding section 2.4 so that it's more accessible to readers. 

- Can you talk about how we would scale this to larger models?

- Can you also talk how about how this method would saturate with # of samples drawn?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The manuscript introduces 4 new architectures of nondeterministic neural networks for producing samples from the aleatoric target distribution. Furthermore, a new loss function for optimizing neural networks based on an empirical approximation of the "continuous ranked probability score" (CRPS) is introduced. Test over standard datasets for classification tasks as well as regressions tasks are discussed.

### Strengths
The idea is simple but rigorous and the implementation straightforward. The performance improvements, especially for the single-head weighted version with ensembling are small but consistent.

### Weaknesses
The presentation should be improved, see questions

### Questions
- The formulation of the problem at rows 92--96 should be more clear, in particular regarding the the definition of "small omega".
- at "The described setup provides, to our knowledge, the first nonparametric way to learn aleatoric uncertainty for neural network regression" rows 286-287. How do we know the uncertainty is aleatoric and not epistemic?
- Eq. 3: the loss is given by the difference between the cumulative distribution F of the labels for a batch and the stochastic results created by the network?
- the process of generating the different outcomes in figures 2 and 3 is not clear enough. 
- In the benchmarking, are only 5 ensembles used? Is this shown / clear to be an ensemble large enough?
- could the process of generating the underlying distribution on the NLL (row 442) be briefly summarized? It is true this comes form literature, but a reminder could help the readability.

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
UQ is important for predictive modeling. Most existing methods assume parametric distributions around the true value, limiting their ability to capture skewed, multi-modal distributions.
The paper proposes a nonparametric, nondeterministic NN regression architecture that uses a loss function based on the continuous ranked probability score to capture the aleatoric uncertainty for systems with complex distributions.
The method is evaluated on a few benchmarks, showing better performance compared over other models.

### Strengths
The paper gives a decent introduction on the general UQ concepts and offers a clear summary of the relevant work.
To the reviewer's best judge, the authors seem to have a good grasp of the theory.

### Weaknesses
1. The nondeterministic NN presented in the paper is essentially a deterministic NN with a direct noise injection to the latent representation vector. The paper doesn’t provide a strong justification for why this approach would be effective, making the idea feel somewhat arbitrary.
2. To the best of the reviewer’s knowledge, some statements in the paper seem problematic. For example, "In other words, epistemic uncertainty can be interpreted as the uncertainty of aleatoric uncertainty." (Line 139, page 4).
3. It is unclear whether the method is practically useful. As presented in the paper, the method requires multiple inferences at each training and evaluation step, introducing additional computational cost. This cost is expected to increase for more complex target distributions, making the method less practical for complex systems with skewed, multi-modal non-Gaussian distributions—precisely the motivation behind this work.

### Questions
1. Could you clarify how injecting standard normal noise into the latent vector is expected to better capture aleatoric uncertainty?
2. Considering the higher computational costs reported compared to other methods, would this make it challenging to scale up to real, complex problems?

### Soundness
3

### Presentation
1

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
The authors approach the task of modeling irreducible (aleatoric) uncertainty in deep regression models. To do this, they rely on the _continuous ranked probability score (CPRS)_ as the target loss rather than, e.g., a parametric likelihood. They introduce an efficient unbiased estimator to the CRPS with a cost of $O(n\log(n))$ compared to a naive $O(n^2)$ approach.
The method is evaluated on a range of regression tasks.


_____
_Update: Given the changes to the submission provided during the rebuttal discussion, I am increasing my score accordingly._

### Strengths
- The paper is well-written and easy to follow.
- The method is well-motivated and the proposed CRPS-based approach provides a clear and straightforward approach to settings where it is beneficial to move away from more common unimodal likelihood assumptions (although see below).
- The proposed approach is computationally scalable.
- The appendix and provided codebase seem to ensure full replicability. (However, I didn't check the code in detail and only skimmed it.)
- At least on the rather simple UCI regression tasks the model is well calibrated. It would have been interesting to see regression problems that require deeper nets, e.g., an evaluation of a depth-estimation data set from the computer vision literature.

### Weaknesses
- The major weakness is in the framing of the storyline. Again and again throughout the text, the authors claim that aleatoric has not been of interest to the literature or has been only _"treated as an afterthought"_ (l180).
I strongly disagree with this statement. Well-modeled aleatoric uncertainty has a strong presence in the literature, as is, e.g., discussed in the cited review paper by Gawlikowski et al. (2023). 
Be it in computer vision (Kendall & Gal, 2017; Gast & Roth, 2018,...), any normal likelihood-based paper that learns a homoscedastic or heteroscedastic noise model, evidential deep learning/prior network-based approaches such as Amini et al. (2020) or Malinin et al. (2020), and many more. 
Accurately modeling both aleatoric and epistemic uncertainty has, e.g., the important application of active learning, where information should be requested about data the model is uncertain in a reducible rather than an irreducible sense and other approaches. 
As such, aleatoric uncertainty is not an afterthought, but rather an integral component of those models. However, where I agree, and which would be a more correct phrasing of the problem, is that most of these focus on an assumption of a univariate noise structure rather than a multi-modal one as the authors allow for.
Yet, this constraint is not an inherent one or one of ignorance in the literature. Lakshminarayanan et al. (2017), e.g., explicitly mention the proposal of extending their method with MDNs if a uni-modal normal likelihood is too restrictive. 
This restriction is also regularly lifted in the literature. See, e.g., the work of Depeweg et al. (2018), who allow for multi-modality via latent variables to the input of BNNs, or Bouchacourt et al.'s (2016) DISCO nets, who inject noise in a later part of the deterministic nets, in an architectural similarity with the proposal by the authors. 
Non-normal likelihoods have also been the focus of, e.g., Gaussian Processes (Sendera et al., 2021), Normalizing Flows (e.g., Ardizzone et al. 2019), and other probabilistic models.
The authors' proposal is innovative and novel, but not unique in the sense that nobody has cared about aleatoric uncertainty since Bishop (1994). 
This last sentence is a slightly exaggerated version of how parts of the paper read. I don't claim that the authors think that, but both the discussion and experimental evaluation ignore this field almost completely.  
- The discussion on how the method fits into the literature, and that the proposal is primarily on nonparametric vs unimodal noise structure should be clearer.
- Given this, an experimental comparison against, e.g., a naive heteroscedastic (deterministic or Bayesian) neural net, DISCO Nets, or Depeweg et al. (2018) is necessary to evaluate the method properly.


_____
Adrizzone et al., Analyzing inverse problems with invertible neural networks, ICLR 2019  
Bouchacourt et al., DISCO Nets: DISSimilarity COefficient Networks, NeurIPS 2016  
Depeweg et al., Decomposition of Uncertainty in Bayesian Deep Learning for Efficient and Risk-sensitive Learning, ICML 2018  
Gast & Roth, Lightweight Probabilistic Deep Networks, CVPR 2018  
Malinin et al. Regression Prior Networks, 2020  
Sendera et al., Non-Gaussian Processes for Few-Shot Regression, NeurIPS 2021

### Questions
- Q1: Can the authors comment to a greater degree on the relationship between their proposal and the existing literature?
- Q2: All networks in the paper are rather small. How do the authors expect their method to scale as the architectural structure becomes deeper?

### Soundness
4

### Presentation
4

### Contribution
3

# Enhancing Uncertainty Estimation and Interpretability with Bayesian Non-negative Decision Layer

- Decision: Accept
- Scores: 8, 6, 5, 6

## Abstract
Although deep neural networks have demonstrated significant success due to their
powerful expressiveness, most models struggle to meet practical requirements for
uncertainty estimation. Concurrently, the entangled nature of deep neural net-
works leads to a multifaceted problem, where various localized explanation tech-
niques reveal that multiple unrelated features influence the decisions, thereby un-
dermining interpretability. To address these challenges, we develop a Bayesian
Nonnegative Decision Layer (BNDL), which reformulates deep neural networks
as a conditional Bayesian non-negative factor analysis. By leveraging stochastic
latent variables, the BNDL can model complex dependencies and provide robust
uncertainty estimation. Moreover, the sparsity and non-negativity of the latent
variables encourage the model to learn disentangled representations and decision
layers, thereby improving interpretability. We also offer theoretical guarantees
that BNDL can achieve effective disentangled learning. In addition, we developed
a corresponding variational inference method utilizing a Weibull variational in-
ference network to approximate the posterior distribution of the latent variables.
Our experimental results demonstrate that with enhanced disentanglement capa-
bilities, BNDL not only improves the model’s accuracy but also provides reliable
uncertainty estimation and improved interpretability.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The manuscript introduces a Bayesian Nonnegative Decision Layer (BNDL) for deep neural network classifiers, with the intent of reformulating them as a factor analysis. This is shown to enhance the interpretability and uncertainty-estimation capabilities of the networks, at least on the examined datasets.

### Strengths
The idea is rigorous and the implementation introduces a minimal overhead over an existing network.

### Weaknesses
The manuscript introduces a Bayesian Nonnegative Decision Layer (BNDL) for deep neural network classifiers, with the intent of reformulating them as a factor analysis. This is shown to enhance the interpretability and uncertainty-estimation capabilities of the networks, at least on the examined datasets.

The distinction between epistemic and aleatoric uncertainty is not clearly defined. Specifically, it's unclear how the proposed model ensures that epistemic uncertainty diminishes with increasing data, a crucial characteristic of epistemic uncertainty. The explanation of the uncertainty evaluation metric lacks clarity, particularly regarding the computation of  n_ac, n_au, n_ic, and n_iu. The difference between f_NN and f_lambda in Eq. 9 is not well-defined, making it difficult to understand their respective roles within the model. The transition from Gaussian to Gamma distributions in section 3.2 is unclear and requires further justification. The use of a fixed threshold of 10^-5 for sparsity measurement seems arbitrary; ideally, this threshold should be derived from an analysis of the weight distribution. Finally, the significant performance difference observed when applying BNDL to ResNet versus ViT is not sufficiently explained, leaving the reader to wonder about the underlying reasons for this discrepancy.

Typos:
- row 178, "uncertainty-refers" should not have a hyphen
- 282 Killback–Leibler
- 345 "descirbed"
- 355 "we uses"
- 371 "Perforamce"

### Questions
- How do we know the distinction between epistemic and aleatoric uncertainty? The epistemic uncertainty should go to zero for large data limit. Is this the case in the present modeling? 
- In Sec. "uncertainty evaluation metric", how are the various n_ac,  n_au, n_ic, n_iu actually computed?
- Eq. 9: what is the difference between f_NNand f_lambda?
- in section 3.2, the switch from Gaussian to Gamma distribution is unclear. Is the Gaussian distribution used in this work? It seems not but the sentence "Both θ and Φ are sampled from a Gaussian distribution" points otherwise. 
- in sparsity measurement a threshold of 10^-5 is defined for the weights. Shouldn't this come from the analysis of the distribution of weights, rather than just providing a number?
-in table 1, it seems the application of BNDL to ResNet introduces a significantly better improvement than when applied to ViT. Can the reason of this be understood? 

Typos:
- row 178, "uncertainty-refers" should not have a hyphen
- 282 Killback–Leibler 
- 345 "descirbed"
- 355 "we uses" 
- 371 "Perforamce"

### Soundness
4

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors focus on improving the interpretability of deterministic neural net, by inserting a probabilistic layer that provides a non-negative factorization for an interpretable classification.
They prove (partial) identifiability and evaluate the method on several image classification benchmarks.

### Strengths
- The method is generic enough to be added to an arbitrary deep architecture
- It performs well under varying experimental settings and architectures and can keep/improve upon its non-interpretable counterpart while greatly improving interpretability  


One caveat that should be noted is that I am not too familiar with the current state of the art in interpretability research. As presented, the results look significant, but they might not be.

### Weaknesses
 - The experiments are limited to a small set of interpretability baselines.
- Sec 3.1 "We first adopt a Bayesian perspective to re-examine the DNNs". This framing is rather crude. The vague fact that one could interpret the input to a softmax as a delta distribution over a latent variable alone is not enough to call something Bayesian. A Bayesian approach requires a well-specified prior combined with a posterior inference. Simply making a model (indirectly) probabilistic is not Bayesian.
- l218 "it lacks reparameterization and cannot be optimized" 
You can always rely on what is often known as the REINFORCE approach, i.e., $\nabla_a E_{x\sim q_a(x)}[f(x)] = E_{x \sim q_a(x)}[f(x)\nabla_a \log q_a(x)]$. However, you usually don't want to do this as it will punish your gradients with a huge variance, which is why your proposal is much more stable and sane. But as long as you have a density you could in theory do it. 
- (12) the left hand side should be p(Y|X), as you marginalize on the rhs over $\theta$ and $\Phi$
- Given the Bayesian framing of the paper a short discussion or mention of what is known as last-layer BNNs is missing. These combine a deterministic network trunk with a Bayesian inference over the last layer of a neural net. See, e.g., the references in Harrison et al. (2024). (This is not necessarily the best reference for this research direction that has been growing recently, but one whose references can serve as guidance for a more generic reference.)  
- In a similar direction goes the field of evidential deep learning also known as prior networks, where a prior to the last layer is inserted in a different way. See, e.g., Sensoy et al. (2018) for classification or Amini et al. (2020) and Malinin et al. (2020) for regression. Both research directions, i.e., EDL and LL-BNNs have a different aim than the authors' proposal but rely on similar mechanics.
- Regarding overconfidence in l167, I would have expected a reference to the first main study in that direction by Guo et al. (2017). (At least to my knowledge.)
- In Thm 1 $e_{(k)}$ is not introduced

_____
_Amini et al., Deep Evidential Regression (2020)_  
_Guo et al., On Calibration of Modern Neural Networks (2017)_    
_Harrison et al., Variational Bayesian Last Layers (2024)_    
_Malinin et al., Regression prior networks (2020)_    
_Sensoy et al., Evidential Deep Learning to Quantify Classification Uncertainty (2018)_    



### Typos
The paper contains a lot of typos and missing articles, which should be fixed in a thorough proofreading round. A subset of these are
- l81 Furthermore, we provide
- l105,l107 (and maybe others) the citation style is broken use \citep and \citet correctly, please follow the style guide
- most equations, e.g., (1), (2) lack proper punctuation
- l206 $\mathbb{R}_+$
- l241 "where $h_j$ is an extracted feature
- l272 of the log-likelihood
- l345 are described in
- l440 misclassification, e.g., in the
- A lot of references are broken, e.g., Dosovitskiy et al. (2020) is a published paper, so is Kingma & Ba's Adam etc.

### Questions
- Q1: The authors provide a theoretical complexity analysis. What is the practical runtime increase compared to a simple fully-connected layer?
- Q2: Can the authors provide greater detail on their relatio nto Wang et al. (2024)? There is a strong relation in the method (NMF) and aim to improve interpretability, yet within this paper it is only ever mentioned in passing without being fully introduced nor compared against. The same holds, e.g., for Duan et al. (2024).

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
2

### Summary
The authors propose a Bayesian neural network where the final layer is modeled as a non-negative matrix factorization (NMF), i.e. $y \sim \Phi\Theta$, the motivation being that such a model would provide both predictive uncertainty estimates (because we learn a posterior distribution) and interpretability (because we learn a sparse factorization for $y$). Both $\Phi$ and $\Theta$ are modeled as Gamma distributions, and approximated variationally using the Weibull distribution. The authors evaluate their model (on accuracy, uncertainty, and sparsity) on CIFAR and ImageNet.

### Strengths
1. The methodology and description of the model and inference process is soundly written. Modeling as the factorization matrices as Gamma distributions should, in theory, encourage sparsity. The variational inference process that is described makes sense. 

2. Section 4 is an interesting addition to the paper, which describes how the factorization matrices are (partially) identifiable under certain assumptions, and how the author's model satisfies such criteria.

3. I appreciate the sanity testing for uncertainty/accuracy correlation in Section 5.1.1.

### Weaknesses
My main criticisms would relate to the experimental results:

1. It is not clear to me why it is necessary to compare to non-Bayesian/point-estimate models, considering that the goal of the paper is to provide better uncertainty estimates. As such, I am not sure the ViT results are especially meaningful, i.e. it is unclear to me what I should be comparing ViT-BNDL to. The inclusion of non-Bayesian models alongside Bayesian models obscures the core contribution, which should be focused on improved uncertainty quantification. The paper should clarify the specific advantages of BNDL over other Bayesian methods, rather than simply showing that it can be incorporated into non-Bayesian architectures.

2. From Table 1, the PAvPU numbers for the ResNet model do not seem to be a huge improvement over the competing methods, especially the recent approaches (BM and CARD). The reported PAvPU gains are marginal, and the paper needs to provide a more thorough analysis of the statistical significance of these improvements. It is unclear if the observed differences are practically meaningful, or simply due to random variation in the experiments. A more rigorous comparison, including confidence intervals or statistical tests, is needed.

3. Is there a reason why sparsity values are not shown for the competing approaches in Section 5.1.2?

4. It is not clear to me that the interpretability evaluation metric in Section 5.2 is correct or useful. Specifically, why is unsupervised disentanglement important for ImageNet and CIFAR? Disentanglement does not imply interpretability, and disentangled features are not necessarily the correct ones to learn either (e.g. a spurious feature will be disentangled from a salient feature, but it doesn't mean we want to learn the former). The paper needs to justify the use of disentanglement as a proxy for interpretability, especially given that the disentangled features may not align with human-understandable concepts. The evaluation should focus on metrics that directly measure the interpretability of the learned representations, rather than relying on an indirect measure like disentanglement.

5. Relatedly, why do we not compare to competing approaches in Section 5.2? Would the authors be able to report the metric in Table 2 and the visualizations in Figure 4 for the models that BNDL was compared to earlier?

### Questions
The authors should respond to my questions in the Weaknesses section. I have no further questions, although I want to note that there are a fair number of typos in the paper that the authors should clean up.

E.g. I believe the first term inside the integral of Eq (4) should be $p(y|\Phi, \Theta)$?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The manuscript suggests using Bayesian non-negative decision layer for improving model's uncertainty evaluation and sparsity (disentanglement), with no (statistically significant) loss of accuracy.

### Strengths
Suggested BDNL seems advantageous for uncertainty evaluation and disentangled representation learning.

The authors try to perform theoretical analysis of their method.

For most paragraphs ZeroGPT score was 0%, for some 4% and 8%. Thus rather human-written.

### Weaknesses
Literature overview: why you do not cite works on DNNs and non-negative factor analysis in the interpretability framework, these are probably the closest works to your manuscript and constitute the core of your work? E.g.:
https://proceedings.neurips.cc/paper_files/paper/2022/hash/e53280d73dd5389e820f4a6250365b0e-Abstract-Conference.html

Theorem 1 is not a theorem (please check any statistical/ML literature, like AoS or NeurIPS for what is a theorem), neither is its "proof" is a proof, this is just a discussion. I would suggest you change the presentation.

The improvement of the performance does not seem to be significant at all, which is Ok, but the PAvPU might still seem questionable. How many receptions have been performed, what are your p-values? How, e.g., these numbers in Table 1 with +/- in front were calculated?

There are typos in the manuscript (which means it is human-written).

### Questions
The results on both uncertainty and disentanglement use one metric only each. Would it be possible include further metrics?

More verbal details on exactly how all experiments were performed would be appreciated.

### Soundness
3

### Presentation
3

### Contribution
2

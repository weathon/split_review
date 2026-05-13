# No Free Lunch from Random Feature Ensembles

- Decision: Reject
- Scores: 8, 8, 6, 3, 3

## Abstract
Given a budget on total model size, one must decide whether to train a single, large neural network or to combine the predictions of many smaller networks.  We study this trade-off for ensembles of random-feature ridge regression models. We prove that when a fixed number of trainable parameters are partitioned among $K$ independently trained models, $K=1$ achieves optimal performance, provided the ridge parameter is optimally tuned. We then derive scaling laws which describe how the test risk of an ensemble of regression models decays with its total size.  We identify conditions on the kernel and task eigenstructure under which ensembles can achieve near-optimal scaling laws.  Training ensembles of deep convolutional neural networks on CIFAR-10 and a transformer architecture on C4, we find that a single large network outperforms any ensemble of networks with the same total number of parameters, provided the weight decay and feature-learning strength are tuned to their optimal values.  %

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
The paper covers several theoretical and empirical analyses related to whether a parameter budget should be allocated to a single large classifier or an ensemble of smaller classifiers. 
The authors first analyse ridge regression using random-features where the ensemble prediction is the mean response of the member predictors, and the test risk is the mean squared error.  They prove that the expected test risk decreases when any of: data size, ensemble feature size, or ensemble size increases when the ridge parameter is chosen optimally for the given setting (with mild assumptions on the task eigenstructure) and show empirically the monotonicity in test error for a binarized CIFAR10 task using RELU random features. The authors then prove a “no free lunch” theorem for random feature ensembles showing that, for a fixed total parameter count, lower test risk is achieved with fewer ensemble members (with mild assumptions on the task eigen structure) and empirically show the monotonicity of test error with ensemble size fitting RELU random feature models to the binarized CIFAR10 task. 
Next the authors derive scaling laws for random feature ensembles in the width-bottlenecked regime (the number of features per ensemble member is much smaller than the data size). They show on synthetic data that for r (a parameter controlling the relative rate of decay of power in modes relative to the rate of eigenspectrum decay) greater than 0.5 (an “easy task”) then there is a growth exponent l* above which scaling laws are near optimal. Therefore ensembles with K>1 can be near optimal as long as the number of parameters per ensemble member grows quickly enough. 
Finally, the authors initialize CNNs in the maximal update parameterization and, using CIFAR10, empirically show for a fixed parameter budget, and task richness, that test accuracy typically decreases monotonically with increased ensemble size. They also show empirically that training loss increases monotonically with increased ensemble size when fitting transformers to C4 data.

### Strengths
I think the paper is in general clear and well-written, the research question is useful and the paper is of interest to ICLR.
I have not checked the proofs, but the results looked sensible and were broadly consistent with the empirical results.

### Weaknesses
In figure 5a, one of the highest performing richness parameters (although not the admittedly highest) does not show monotonic decrease with ensemble size. Given this does not fit with your other analysis, it would be useful to comment on it in the paper.

Both CIFAR10/MNIST and a CIFAR10/MNIST-derived binary classification task are included in the paper. What is the papers convention for differentiating between the binarized version and the original version? In places the paper appears to call the binary classification task “a CIFAR classification task” or “Binarized CIFAR10” but in others it then refers to this binary task just as CIFAR (I think this happens for example in line 370). Could the binary tasks have a name (for which CIFAR10 is a prefix perhaps) and then be referred to by that name to improve readability?

The same notation of learning rate and task eigen structure, and for richness and the data-size-scaled degree of freedom parameters. Giving separate notation would be preferable.

118 – “(citations)” should instead be the actual citation

228 – Figure 1: Are the non-red lines supposed to be dashed in this plot? otherwise does the legend contain a dashed line? Since none appear in the actual plot.

340 – Figure 3 – could you draw the line for l* (= 1/(1+ alpha*(2*r – 1))) in red on the plots for figure 3 A?

397 – “a” is singular, but “tasks” is plural, should remove “a”?

452 – “that at the” -> “that the”

### Questions
In Figure 2c, ensembles (K>1) appear to be relatively robust to ridge parameter, where as K=1 is highly sensitive to it. Could this correspond to it potentially being more practically expedient to train small ensembles when optimally tuning the regularising parameter is expensive?

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
2

### Summary
The present study aims to investigate the utility of training multilple shallower networks vs that of a larger network.  Theory shows that only 1 large network is appropriate and experiments validate this approach.

### Strengths
The paper gives extensive theory and experimental proof that the theory works. 

Wide variety of experiments. 

Scaling laws are given for this class of models, which is always useful.

### Weaknesses
I'd like to see experiments be ran on imagenet validating these results there. 

No results on conventional nerual network architectures.

### Questions
Would it be possible to train random feature ResNet18s or VGGs?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
- This paper studies the tradeoff between ensemble size and total feature/parameter count for random feature ensembles
- In particular, they derive the following theorems (paraphrased informally):
- Theorem 1 - larger ensembles -> better performance (this contribution is minor)
- Theorem 2 - Given a fixed feature count, it is better to have a single large model than multiple smaller ones (this is the main contribution of the paper)
- Both theorems are verified experimentally binarized Cifar-10 datasets
- The paper then uses Thm 2 to derive scaling laws, assuming a standard model of the decay of kernel's eigenspectrum. They identify differing behaviour for "simple" and "difficult" datasets, and verify this experimentally
- Finally, the paper studies the performance of non-fixed feature classifiers using ensembles of CNNs trained on CIFAR-10. They control the feature learning by controlling the richness parameter

### Strengths
- Presentation is clear and easy to follow
- Claims are verified experimentally and there is good agreement with the author's claims
- Section 5 (the section on scaling laws) I find particularly interesting as it shows how the fairly uninspiring theorems in the first two sections can be used to derive more non-trivial behaviours, such as the distinction between "easy" and "difficult" dataset scaling laws
- The use of the richness parameter to control the adherence to the assumptions in the theorems in section 6 in quite interesting, but I am unsure how applicable this work is necessarily to modern models (see weaknesses)

### Weaknesses
 - I think the authors should be very clear that the theorems do not directly "explain" the empirical results in section 6, except in the case of very small richness parameters, as their theorems do not cover feature learning. I think it would also be useful for the authors to discuss this limitation in the weaknesses section in concluding discussion.


### Questions
- Is it possible to plot the validation loss in figure 5b as opposed to the test loss?
- Could the authors discuss how for certain values for $\gamma$ in figure 5a, it seems the increasing the ensemble count improves performance, namely for larger values of $\gamma$? Is it possible that behaviour for models outside of the lazy regime do not follows the same "no free lunch" theorem?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper investigates the trade-off between employing a single large model versus an ensemble of smaller models, focusing on random feature kernel ridge regression (RF-KRR). In particular, this work studies ensembles of size $K$ with $N$ random features per ensemble member with a fixed total parameter count $M=N\cdot K$. In this setting, the paper proves rigorously and shows empirically that optimal performance is achieved by $K=1$ for an optimally tuned ridge parameter while increasing $K$ degrades the optimal test risk. Additionally, this result – referred to as “_no free lunch from random feature ensembles_” – is shown for CNNs and transformers in experiments on image classification (CIFAR10) and language modelling (C4) in the regimes of lazy training and feature learning. Furthermore, scaling laws are derived, and conditions for achieving near-optimal scaling laws for these ensembles are identified.

### Strengths
The main contribution of the paper is to add the ensemble perspective to established results on random feature kernel ridge regressions. It contributes theoretical insights and proofs for two theorems on “_more is better for RF Ensembles_” and “_No Free Lunch From Random Feature Ensembles_” (pages 4-5)  as well as scaling laws and empirical validation of adequate quality. Generally, the paper has a clear thread, with some minor adjustments required to the presentation (listed below in “weaknesses”).

### Weaknesses
Even though extending the analysis of RF-KRR to ensembles is new, the presented results align with the expectations from prior work on single models. In my opinion, this limits the novelty and significance of the contribution, which I elaborate on in more detail below.

__W1.__ _Novelty of Theorem 1 “More is better for RF Ensembles” and results in section 3_: For “non-ensemble” RF-KRR, the referenced papers by [Simon _et al_. (2023)](https://openreview.net/pdf?id=OdpIjS0vkO) and [Bordelon _et al_. (2024a)](https://arxiv.org/pdf/2402.01092) have established that decreasing the number of random features $N$ leads to a degraded optimal test risk. Could the authors elaborate on why examining ensembles adds new perspectives beyond what is already known for single models? I think a strong justification would be necessary. In particular, I view the statement of Theorem 1 and the results presented in Figure 1 of this submission as a natural consequence of (and essentially the same as) [Theorem 1 “More is better for RF regression” and Figure 1 in in Simon _et al_. (2023)](https://openreview.net/pdf?id=OdpIjS0vkO#page=6); see also point W2.1. The core issue is that the theorem appears to be a direct extension of existing results for single RF-KRR models, and it is not clear what new insights are gained by considering ensembles in this specific context. The paper needs to articulate a clear motivation for why an ensemble perspective is necessary here, beyond simply restating known results.

__W2.__ _Significance of Theorem 2 “No Free Lunch From Random Feature Ensembles” and results in section 4_: 
__W2.1.__ A main premise of the work is to have a fixed total parameter count $M$ and compare ensembles of $K$ members and $N$ random features such that $M=N\cdot K$ always holds. This is presented as a “pragmatic” approach to limit computational overhead associated with ensemble methods (lines 34-37). However, this leads to increasingly “weaker learners” when the ensemble size $K$ is increased. For this reason, it is less surprising and in line with the conclusions of [Simon _et al_. (2023)](https://openreview.net/pdf?id=OdpIjS0vkO) and [Bordelon _et al_. (2024a)](https://arxiv.org/pdf/2402.01092) that decreasing the number of random features $N$ (by increasing ensemble size $K$) leads to a degraded optimal test risk (at fixed total parameter count $M$). From this perspective, it is expected that $K=1$ leads to the optimal result. This limits the novelty and significance of theorem 2 on “No Free Lunch From Random Feature Ensembles” where specifically the number of random features are chosen as $N’=M/K’$ and $N=M/K$ with $K’<K$ leading to $N’>N$.  As this is a central result of the paper, it could strengthen the contribution to elaborate more on why ensembles provide new insights beyond what can be directly inferred from the existing work on single models. In my opinion, a more substantial justification would be required. The core issue is that the fixed parameter count setup inherently biases the results towards single, larger models, and the paper needs to justify why this setup is insightful for understanding ensemble behavior. The conclusion that $K=1$ is optimal seems almost predetermined by the experimental design.
__W2.2.__ In addition to the previous point, I believe that the interplay between the number of random features $N$, the size of the ensemble $K$ and the total parameter count $M$ make it difficult to compare the information provided in Figures 1 and 2. For instance, in Figure 2A the relationship between test error and ensemble size $K$ for different sample sizes $P$ at fixed total parameter count $M$ is considered, but with increasing $K$ the number of random features $N$ decreases. It appears that a more careful discussion would be required, which is intimately connected to the premise above. The paper needs to clarify how the competing effects of increasing $K$ and decreasing $N$ are disentangled and why the observed trends are not simply a consequence of the decreasing number of random features per ensemble member.

Minor remarks:
- “RF KRR” and “RF-KRR” are both used in the manuscript and the authors might want to make the usage consistent.
- Line 101: Missing full stop “.” at the end of the sentence.
- Line 106: The computation of $g(v_n,x)$ is mentioned, but $g$ is not defined in the main text. From Appendix A, line 690, it seems that it is another notation for $\psi^k (x)$, but its use in the main text is not clear to me.
- Line 118-119: Missing citation.
- Line 142: Wrong formatting of “f_{*} (x)”.
- Line 176-177: Double parenthesis in citation.
- Line 187: I would not recommend writing “eq’s”.
- Line 248-249 and Figure 1: The “filled” lines are quite likely supposed to be dashed lines.

In summary, I view the points raised in W1 and W2 as the main challenges in the current version of the submission and believe a major revision of the paper is required. However, I invite the authors to address my objections and clarify potential misunderstandings.

### Questions
My questions revolve around the core assumptions of the paper as outlined in W1 and W2 above. In particular, considering classical literature on RF-KRR like [Rahimi and Recht, “Weighted Sums of Random Kitchen Sinks: Replacing minimization with randomization in learning” (2008)](https://people.eecs.berkeley.edu/~brecht/papers/08.rah.rec.nips.pdf) and the referenced works of [Simon _et al_. (2023)](https://openreview.net/pdf?id=OdpIjS0vkO) and [Bordelon _et al_. (2024a)](https://arxiv.org/pdf/2402.01092), my questions are as follows:

Q1. Is there any evidence that an ensemble of random features could provide a different result than is stated in [Theorem 1 of Simon _et al_. (2023)](https://openreview.net/pdf?id=OdpIjS0vkO#page=6) for RF regression?

Q2. In connection to Theorem 2 in the submission and in the context of RF-KRR, is there any reason to assume that a larger ensemble of weak learners can outperform a small ensemble of stronger learners?

### Soundness
3

### Presentation
2

### Contribution
1

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper analyzes the ensemble of K ridge regressions on random features size M/K and one right regression on random features size M. And concludes that the later one is always the optimal under the optimal L2 regularization. This work also use some toy experiments (e.g. two to three layers CNN) to compare the ensemble of K small models and one large models.

### Strengths
- The writing is clear. The paper is easy to read.

### Weaknesses
 - In this paper, Text, Theory and Experiments are not consistent. 
In text, this paper assumes a fixed "computational budget" (line 256), which is resonable, then links this assumption to "a fixed total number of features"  (line 257).  However, a fixed computational budget is not necessary leads to a fixed total number of features. 

The theory discusses the ensemble case of regression on random features. Concludes that one right regression on random features size M is always the optimal under the **optimal L2 regularization**, compared with the ensemble of K ridge regressions on random features size M/K. However, that is trivial. Section 9.1 in [1] shows a dropout on regression equals to an ensemble of expensional number of small regressiors, equals to L2 regularization. Since **an ensemble of expensional number of small regressiors** is not worse that **M/K regressors** (same as the Eq 16 in this work), an "optimal L2 regularization" is of course not worse than "M/K regressors"

The cifar experiments in this work does not link to the theory, i.e. without neither regression nor random features. 



[1] Srivastava, N., Hinton, G., Krizhevsky, A., Sutskever, I., & Salakhutdinov, R. (2014). Dropout: a simple way to prevent neural networks from overfitting. The journal of machine learning research, 15(1), 1929-1958.



typos:
line 141  f(x)

### Questions
- The CNN experiment on CIFAR10 contains two CNN layers and one linear layer. That is already too small for CIFAR10 tasks. Reducing the size of this small network would further hurt the performance. Does the same phenomena in this paper hold on larger networks?  [2] shows the ensemble multiple small networks outperforms a large network. 


[2] Zhang, J., & Bottou, L. (2023, July). Learning useful representations for shifting tasks and distributions. In International Conference on Machine Learning (pp. 40830-40850). PMLR.

### Soundness
1

### Presentation
2

### Contribution
1

# A Coefficient Makes SVRG Effective

- Decision: Accept
- Scores: 8, 6, 6, 5

## Abstract
Stochastic Variance Reduced Gradient (SVRG), introduced by \citet{johnson2013accelerating}, is a theoretically compelling optimization method. However, as \citet{defazio2019ineffectiveness} highlights, its effectiveness in deep learning is yet to be proven. In this work, we demonstrate the potential of SVRG in optimizing real-world neural networks. Our analysis finds that, for deeper networks, the strength of the variance reduction term in SVRG should be smaller and decrease as training progresses. Inspired by this, we introduce a multiplicative coefficient $\alpha$ to control the strength and adjust it through a linear decay schedule. We name our method \approach. Our results show \approach\ better optimizes neural networks, consistently reducing training loss compared to both baseline and the standard SVRG across various architectures and image classification datasets. We hope our findings encourage further exploration into variance reduction techniques in deep learning.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper revisit SVRG in deep learning, showing how reasoning more carefully about control variates. The paper starts by a nice recap of what is believed to be variance reduction and SVRG performance in deep learning, and then guides the reader to the "additional parameter" solution. The authors complement their finding (i.e. a simple modification of SVRG can help training) experimentally on a diverse range of datasets in vision, using many architecture.

### Strengths
I like the paper, it is a simple idea yet presented very clearly:

1) The graphics and plots help the reader get the idea behind the paper. The many presented variance metrics also are very helpful in convincing the reader of the approach.

2) The authors go step by step, showing improved performance with "optimal variance reduction" and later showing why a simple coefficient can close most of the gap. This is very important, makes the investigation very scientific.

3) There are many experiments presented in the corresponding section.

### Weaknesses
I think this could be a very interesting easy reference for modern SVRG. I believe though some additional points can help delivering the idea in a more solid way:

1) As far as I understand, you are always using Adam with lr 3e-4 in your experiments. This is a quite nice lr - but it is well-known that Adam might profit from additional tuning. I do not believe your point here should be "you are better than Adam" - many papers overclaim performance as their main point, but you show much more. I think here what could be helpful is a plot of final accuracy or training loss over learning rare - comparing both with SGD and Adam. Showing this for 1 learning rate is not enough. Note that you do not have to show you are better than Adam, but just that you are better than SVRG and close most of the gap.

2) Figure 5 (SVRG with optimal alpha) is a bit weak: not much improvement over SGD id shown. Do you have an explanation for this? In a way this is the "best we can get" - yet in this specific example Adam, SGD and SVRG (with or withouth alpha) perform quite similar! the variance metrics also confirm that not much variance reduction is happening. I would personally try to find another example or compare this performance on multiple examples.

If the authors can show some improvements around these points, I am happy to raise my score!

### Questions
See above

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper observes the ineffectiveness of SVRG due to the decay of the relevance between the batch gradient and the snapshot. The paper then proposes $\alpha$-SVRG, with $\alpha$ as a conditioning multiplicator to account for the decaying relevance. The approach is shown to be effective in multiple experiments.

### Strengths
1. The flow of the paper is easy to follow.
2. There is adequate discussion about the experiment results.
3. The perspective of the gradient preconditioning is interesting.

### Weaknesses
1. The design of the scheduling of $\alpha$ may require more discussions and refinements. Specifically,
- The effect of $\alpha_0$. The following three points are a bit inconsistent as a whole: (a). From Figure 4, the optimal $\alpha_0$ seems to be almost the same for different models. (b) From Table 4 and Figure 9, it seems that $\alpha\approx0.75$ may be a better choice that $\alpha_0=0.5$ (at least for the small model that is used). (c) In the experiment that yields Table 3, however, $\alpha-0.5$ for small models and $\alpha_0=0.75$ for larger ones.
- The schedule of $\alpha$. It may be interesting to analyze different types of scheduling of $\alpha$ based on the perspective of preconditioning in Appendix G.
2. For the experiment that yields Figure 4, it would be better if the authors could conduct experiments on different datasets and try to analyze the effect of data on the optimal $\alpha$.

### Questions
In the schedule of Eq. (9), why do we use a constant of $10^{-2}$ instead of other constants? Can this constant also be tuned?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposed the $\alpha$-SVGR algorithm, which introduces a linearly decaying coefficient to adjust the scale of the correction term in SVRG. The proposed algorithm is inspired by the observation that the original SVRG does not effectively reduce the variance in the late training phase. To show the effectiveness of $\alpha$-SVRG, the authors conducted extensive experiments across various datasets and model architectures.

### Strengths
1. This paper is well-written with clear logic. It first identifies the problem with the original SVRG by monitoring the gradient variance during training. Then, it addresses the identified issue by introducing an extra coefficient that adjusts the scale of the SVRG correction.

2. The evaluation is comprehensive. The authors not only conducted extensive experiments across various datasets and model architectures but also explored other possible schedules for the introduced hyperparameter $\alpha$. However, I still have some concerns about the effectiveness and extra cost of $\alpha$-SVRG (see weaknesses).

### Weaknesses
 **Major**
1. The effectiveness of $\alpha$-SVRG: In Table 2, compared with the baseline $\alpha$-SVRG's improvement in training loss and validation accuracy is marginal. 

2. The computation and memory cost of $\alpha$-SVRG: $\alpha$-SVRG requires additional computations for the full gradient $\nabla f(\theta^{\text{past}})$ and the mini-batch gradient at $\theta^{\text{past}}$, $\nabla f_i(\theta^{\text{past}})$. Additionally, it necessitates maintaining $\theta^{\text{past}}$ and $\nabla f(\theta^{\text{past}})$ in memory. The paper fails to address or discuss these significant costs.


In summary, while the paper offers a good starting point for investigating why SVRG underperforms in deep learning, the enhancements to the original SVRG model, represented by $\alpha$-SVRG, do not sufficiently justify the substantial additional costs and provide only limited benefits compared to standard SGD or AdamW.


**Minor**:
1. The authors are advised to include the pseudo-code for AdamW + $\alpha$-SVRG rather than merely describing its use of AdamW as the base optimizer.

2. Typos in eqs (7)-(9).

### Questions
In Figure 5, the gradient variance of $\alpha$-SVRG is not lower than SGD in the late phase in terms of any metric. Does the improvement of $\alpha$-SVRG in training loss, if any, come from the reduced variance in the early phase? If this is the case, would it be more effective to employ $\alpha$-SVRG only during the initial phase and switch to standard AdamW or SGD for the later stages?

To further elaborate my question, the role of gradient noise in helping generalization is widely discussed in the literature (e.g., [1]-[5]). In the late phase of training, we even need to encourage more helpful, benign noise that drives the model parameter to better generalizing minima. From this perspective, why not altogether remove the correction term in SVRG in the late phase?

[1] Samuel Smith, Erich Elsen, and Soham De. On the generalization benefit of noise in stochastic gradient descent. ICML'2020.

[2] Alex Damian, Tengyu Ma, and Jason D. Lee. Label noise SGD provably prefers flat global minimizers. NeurIPS'2021.

[3] Zhiyuan Li, Tianhao Wang, and Sanjeev Arora. What happens after SGD reaches zero loss?–a mathematical framework. ICLR'2021.

[4] Guy Blanc, Neha Gupta, Gregory Valiant, and Paul Valiant. Implicit regularization for deep neural networks driven by an ornstein-uhlenbeck like process. COLT'2020.

[5] Xinran Gu, Kaifeng Lyu, Longbo Huang, Sanjeev Arora. Why (and When) does Local SGD Generalize Better than SGD? ICLR'2023.

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper studies a modification of the variance-reduced method SVRG. The authors attempted to fix the issue of the applicability of variance-reduced methods in deep learning which was noticed by Defazio & Bottou, 2019. The modification consists of adding a scaler to the variance term in the update of SVRG. The authors explain this change by considering an example of the reconstruction of one random variable X from another variable Y correlated to X. The authors provide the convergence guarantees for the proposed modification of SVRG and demonstrate its effectiveness for several DL benchmarks.

### Strengths
- The paper is well-written and easy to follow. 

- There is a clear intuition as to why there should be a scaler smaller than 1 in the update of SVRG from the example in (2). The authors support this change by computing theoretical values of the scaler $\alpha$ for logistic regression and MLPs. It turns out that the values of  $\alpha$ drop to the end of the training for MLP and stay stable around $1$ for logistic regression. This empirical evaluation separates convex logistic regression (where SVRG is known to perform well) and non-convex MLP (where SVRG doesn't perform well).

- The proposed $\alpha$-SVRG method was tested on several DL workloads demonstrating its potential improvement over other baselines like SGD, SGD+SVRG, and AdamW.

- The authors provide potentially useful $\alpha$-schedulers that gradually decrease the values of $\alpha$. This is explained by the fact that vanilla SVRG can reduce the variance at the beginning of the training (where the stochastic gradients are more aligned) and fails in the end.

### Weaknesses
 - SVRG-type methods do not suit the DL framework well not only because of the failure to effectively reduce the variance but also because of the necessity of full gradient computation from time to time. From this perspective, methods Zero-SARAH are more interesting to explore.

 - The convergence of $\alpha$-SVRG is presented under the assumption of bounded gradients $\|\nabla f_i(x)\|\le \sigma$. In my opinion, this assumption is strong and doesn't allow to show the theoretical benefit of using $\alpha$-SVRG instead of vanilla SVRG. The analysis does not account for the non-convexity of the loss landscape in deep learning, which is a significant limitation.

 - The authors claim that $\alpha$-SVRG decreases the variance. I don't understand why this is the case. For example, based on Figure 5 $\alpha$-SVRG can reduce the variance only in the beginning (where vanilla SVRG can do that as well) but afterward, the variance of $\alpha$-SVRG is similar to SGD which doesn't have any variance reduction mechanism inside. Moreover, the fluctuations of empirical variance of $\alpha$-SVRG are higher than that of SGD. Therefore, I believe it would make sense to average the variance across several random seeds to see the statistical error (it might happen that in the beginning $\alpha$-SVRG was a bit lucky). This would be also beneficial for the train loss dynamics to understand how significant the improvement. For example, for some workloads, the improvement in Table 3 is in the second digit after the dot which most likely is within the standard deviation which I believe cannot be used as significant (the results in table 8 seem to support my comment).

 - The comment above also relates to the claims of the form "...can reduce gradient variance significantly..." (see line 353 and other lines like this). First, since the results of one run are presented it is not possible to measure the significance (it might be that the differences in training dynamics of the algorithm and its $\alpha$-SVRG version are within standard deviation). Second, how is "significance" measured for the proposed 3 variance metrics? Can the change 0.1 be considered large? What is the threshold for being "significant"?

 - The results in Figure 10 are controversial to the claims of the paper. For small batch sizes you expect $\alpha$-SVRG to perform better since the variance should be larger. However, AdamW without any variance reduction mechanism handles the variance better than.

 - The authors use various deep learning techniques like warmup in the training and the improvement might come from a weird combination of all of those techniques with $\alpha$-SVRG update. In my view, it is important to understand if $\alpha$-SVRG procedure alone indeed helps to reduce variance.

To summarize, in my view, the authors didn't provide enough empirical evidence to showcase the usefulness of $\alpha$-SVRG even though the idea of adding a scaler is intuitively logical.  The improvement is typically marginal (within standard deviation) and comes with a significant increase in memory usage and full gradient computation.

### Questions
- Could you please elaborate how $\alpha$-SVRG update is plugged in AdamW? Do you perform $\alpha$-SVRG update on the stochastic gradient which is then used in AdamW? Or do you perform $\alpha$-SVRG trick for the updates of AdamW? In general, this would be beneficial to add a pseudocode at least in the appendix how to combine the proposed $\alpha$-SVRG update with any optimizer.

- I don't understand the connection of $\alpha$-SVRG and preconditioning. In (38) the authors define a matrix A. Could you provide the exact form for A? I believe the SVRG update cannot be presented as a linear mapping and therefore this connection seems to be misleading.

### Soundness
3

### Presentation
3

### Contribution
2

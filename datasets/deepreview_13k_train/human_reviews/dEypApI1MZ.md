# How Feature Learning Can Improve Neural Scaling Laws

- Decision: Accept
- Scores: 8, 6, 6, 8, 8

## Abstract
We develop a solvable model of neural scaling laws beyond the kernel limit. Theoretical analysis of this model shows how performance scales with model size, training time, and the total amount of available data. We identify three scaling regimes corresponding to varying task difficulties: hard, easy, and super easy tasks.  For easy and super-easy target functions, which lie in the reproducing kernel Hilbert space (RKHS) defined by the initial infinite-width Neural Tangent Kernel (NTK), the scaling exponents remain unchanged between feature learning and kernel regime models. For hard tasks, defined as those outside the RKHS of the initial NTK, we demonstrate both analytically and empirically that feature learning can improve scaling with training time and compute, nearly doubling the exponent for hard tasks. This leads to a different compute optimal strategy to scale parameters and training time in the feature learning regime. We support our finding that feature learning improves the scaling law for hard tasks but not for easy and super-easy tasks with experiments of nonlinear MLPs fitting functions with power-law Fourier spectra on the circle and CNNs learning vision tasks.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper does a mean-field analysis of feature learning in a model similar to a shallow linear network. Scaling laws are obtained, where depending on the source exponent, feature learning can lead to a improvement in the exponent.

### Strengths
The paper uses advanced theoretical tools to tackle the important question of the effect of feature learning. A complete phase diagram is obtained, showing under which condition feature learning leads to a significant advantage. The theoretical scaling laws are checked empirically, and seem to even extend to some degree to deep nonlinear networks (which are not covered by the theory).

### Weaknesses
The paper does not give much intuition for why this improvement of feature learning is observed, instead the authors simply mention the existence of a self-consistent dynamic derived in the appendix.

I also feel that the authors do not relate much to the already existing litterature on the dynamics of linear networks (e.g. https://arxiv.org/abs/2211.16980), where feature learning and self-consistent dynamics have been described in https://arxiv.org/abs/2406.06158 or https://arxiv.org/abs/2405.17580 . It would be interesting to know whether the dynamics observed in this paper is similar to the ones observed in these papers.

The effect observed in this paper differs significantly from other feature learning paper in that it does not assume any form of sparse structure (actually feature learning appears to help when the signal is closest to being of the same intensity along all directions), i.e. low-index models for shallow networks, or low-rank matrices for linear networks. This suggest that the type of feature learning observed here is quite different from these other line of results. My intuition from your paper, is that feature learning may in some sense improve the conditioning of the Hessian/NTK, allowing faster convergence, whereas in the presence of sparsity feature learning seems to rather make the NTK low-rank and more ill-conditioned. I was therefore wondering whether the effects observed here might disappear when switching from online learning to GD on a fixed dataset, because it would untangle the training speed from the number of datapoints observed, and maybe we could see there that feature learning makes convergence faster but maybe one still converges to approximately the same solution (and thus same test error).

Typos:
- on page 5: The sentence "The first terms represent bottleneck/resolution-limited scalings in the sense that taking all other quantities to infinity and studying scaling with the last ..." does not finish.

### Questions
The effect observed in this paper differs significantly from other feature learning paper in that it does not assume any form of sparse structure (actually feature learning appears to help when the signal is closest to being of the same intensity along all directions), i.e. low-index models for shallow networks, or low-rank matrices for linear networks. This suggest that the type of feature learning observed here is quite different from these other line of results. My intuition from your paper, is that feature learning may in some sense improve the conditioning of the Hessian/NTK, allowing faster convergence, whereas in the presence of sparsity feature learning seems to rather make the NTK low-rank and more ill-conditioned. I was therefore wondering whether the effects observed here might disappear when switching from online learning to GD on a fixed dataset, because it would untangle the training speed from the number of datapoints observed, and maybe we could see there that feature learning makes convergence faster but maybe one still converges to approximately the same solution (and thus same test error).

Typos:
- on page 5: The sentence "The first terms represent bottleneck/resolution-limited scalings in the sense that taking all other quantities to infinity and studying scaling with the last ..." does not finish.

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces a solvable two-layer linear model trained using a variant of stochastic gradient descent (SGD) to predict the scaling laws beyond the kernel (lazy training) regime. The authors identify three scaling regimes—hard, easy, and super easy tasks—under which feature learning can improve the scaling of the loss with respect to training time and compute. The paper also provides experimental validation of these theoretical predictions by training deep, nonlinear models to demonstrate the applicability of the scaling laws.

### Strengths
1. Tractable Theoretical Setting: The paper presents a solvable theoretical model, which allows for potentially clearer and rigorous exploration of neural scaling laws beyond the kernel regime. This tractable setting potentially makes it easier to understand and predict the dynamics of feature learning in neural networks.

2. Extension of Prior Work: The authors improve upon simpler one-layer linear models from prior work by introducing a more sophisticated two-layer model. This extension potentially can provides deeper insights into the scaling behavior of neural networks.

### Weaknesses
1. Complexity and Assumptions: The paper is difficult to follow due to the heavy reliance on prior work. This reliance can make it challenging for readers who are not deeply familiar with the specific foundational literature to fully grasp the contributions.

2. Unclear Definition of Feature Learning: Throughout the paper, the concept of "feature learning" is not clearly defined. It remains unclear how the authors measure feature learning or provide a tangible understanding of it. Although allowing 
A(t) to evolve leads to better performance, this change doesn’t adequately explain how features are being learned or evolved. The authors now state that feature learning is when the empirical NTK changes, which is not a sufficient definition. If the parameters of the model are randomly changed, the empirical NTK would change drastically, but no useful features would emerge. The authors also state that feature learning means the network is operating outside of the lazy training regime, which is also insufficient. These definitions do not explain why the NTK's evolution represents a good evolution that leads to meaningful feature learning. While improvements in loss might hint at beneficial changes, they do not serve as concrete evidence of feature learning.

3. Limited Model Scope: The model seems quite limited in its design. Allowing 
A(t) to change is reasonable, especially since the target function is 𝑊∗𝜓_{inf}(x). However, it is unclear why this is believed to represent or mimic feature learning in practical, real-world scenarios. The connection to real feature learning remains vague. This is also related to 2nd point, that I do not understand how authors define feature learning.

4. Transferability to Deep Nonlinear Models: It is not clear why the results derived from the proposed linear model are expected to transfer well to deep, nonlinear models. 

overall I feel like the paper is scattered and I can not grasp the main point authors are trying to make about feature learning.

### Questions
See weaknesses

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper studies the scaling laws of neural networks in two regimes: lazy learning and feature learning. Eq (8) and (9) describe the power-law variation of the loss with training time \( t \), number of parameters \( N \), and batch size \( B \) in these two regimes which show that feature learning accelerates the convergence of hard tasks.

### Strengths
1. This paper constructs a comprehensive scaling law framework, reveals the power law relationship between loss and the number of parameters, training time, and batch size, and provides a theoretical basis for understanding the performance of neural networks.

2. This paper conducts a series of experiments to verify the theoretical results, making the conclusions of this paper more convincing.

### Weaknesses
1. This paper ignores the impact of gamma on the feature learning scaling law.

2. The paper lacks an analysis of the critical state between the two regimes.

3. (Minor) The colors of lines in the figures are not differentiated enough.

### Questions
From the experimental results in Figures 9 and 12, we can see that the scaling law does not change suddenly at $\gamma = 0$, but changes gradually at a very small value of gamma. Can this paper's analysis cover this aspect?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper studies scaling laws of the training loss with respect to relevant parameters (training time, model size and batch size), with a focus on online training, where dataset size is assumed to be unlimited.
They study training dynamics through the lens of the eigenspace decomposition of the NTK. Such eigenspace is used both to (1) formally define capacity and source of model and task and (2) to express the loss behaviour explicitly, both in the lazy learning regime ($\gamma=0$) and in the feature learning regime ($\gamma>0$), the former can be solved explicitly while the second is approximated with DMFT. Such analysis reveals two very different regimes depending on the value of the source, specifically in the hard regime (source<1) they prove better scaling laws than state of the art. Such scaling laws are studied and discussed in each component. Empirically are shown to be tight on a variety of task, including synthetic and MNIST vision, but they are shown to no be tight in the CIFAR case.

### Strengths
The paper is very well written and easy to follow, overall very pleasant to read.
Settings and limitations are well clarified: the authors are very open about the limits of their theory and the non-success of the CIFAR experiment. This behaviour is super valuable and very helpful for future works and possible improvements.
Derivations are explained both intuitively and formally: key concepts are present in the main paper with a good trade-off between formalism and explanation; technical details not directly useful to understand the concepts are properly deferred to the appendix.
Results are clear and well discussed: for example the scaling laws are divided in several components, each of them is further discussed and empirically studied with ad-hoc experiments.

### Weaknesses
The paper is overall solid and I don't see major weakness.

A big assumption made is the online setting, and the extension to finite dataset setting in Appendix D is somehow limited. However such kind of limitation has to be expected from a theoretical paper. Of course a general case analysis would be preferable, but that would very ambitious and I don't think this assumption can be considered a major weakness.

The dynamics mean field theory is not at all explained in the main paper, understandably. An informal explanation attempt is done in Line 202-211. While I consider this attempt valuable, the Equation (in line 206) is too much out of context, the notation is not defined and it ends up being practically useless for the reader. I recommend either removing (and using that space to expand the intuition informal explanation) or extending it, explaining the terms involved.

Minor detail. In Line 133 "we then diagonalize..." can be misinterpreted as "we discard the non-diagonal elements". I think overall the message is clear because right after (in Line 134) you refer to eigenfunctions, but I'd recommend trying to reformulate this sentence to avoid ambiguities.

### Questions
In line 160 the "allow" pops a bit out of nowhere and it hard to grasp. Following with Lines 175-176, my understanding is that you choose an arbitrary kind of feature learning dynamics, with the implicit assumption that SDG is sufficient (but not necessary) to obtain such dynamics. Being sufficient means that the scaling law you derive is at least an upper bound on the loss. While not being necessary means that a different choice of modelling dynamics for $A(t)$ may lead to tighter scaling low (which may for example explain the CIFAR experiment). Is this understanding correct? Is such implicit assumption true? Can you please argument a bit more over this choice of feature learning dynamics?

The reference "Bordelon et al. (2024a)" appears very often in the paper. It would be nice to have a short paragraph (maybe in the appendix) to clarify the common point with such paper and the novel contribution of this one over that one. Can you reply with a draft of such paragraph?

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper studies a minimal model for scaling laws in generalization error under feature learning non-linear neural networks. This model induces improved scaling exponents compared to kernel regression through feature learning (only) for target functions outside of the initial NTK’s RKHS. Consequently, different scaling rules of parameters and training time are asymptotically compute-optimal. These scaling rules are empirically verified in toy settings.

### Strengths
The paper is very well written and easy to read. To the best of my knowledge, this is the first paper that theoretically explains compute-optimal scaling laws in non-linear feature learning networks beyond the lazy regime. Separating the four bottleneck mechanisms in eq. (9) and achieving improved scaling laws through feature learning are particularly interesting accomplishments.

Overall, although this paper only studies a toy learning algorithm, I believe it makes a valuable contribution towards a theory of scaling laws for finite, feature learning neural networks, which is why I recommend acceptance.

### Weaknesses
Besides partially critical questions below, I consider the following points to be the main weaknesses of this paper.

- **Artificial learning setup.** The projected gradient descent with frozen first-layer weights is a constructed training procedure. This may make the analysis easier, but it remains unclear how well the results are transferable to more practical optimization procedures like SGD or Adam on **all** weights. The analysis focuses on a simplified scenario where only the last layer is trained, which is a significant deviation from typical deep learning practice. The paper does not adequately justify this choice or explore the potential impact of training all layers on the observed scaling laws. It is unclear if the feature learning dynamics observed in this simplified setting will generalize to more complex scenarios where all network parameters are updated. Do you think your results can be generalized to realistic training? Do you train all weights in Section 5? This is not explicitly stated.
- **Oversimplifications.** The simplifications that make the paper very easy to read sometimes lead to oversimplifications and imprecision. For example, in l. 191, what is $N,B\gg 1$ formally supposed to mean? The paper uses asymptotic notation without rigorously defining the limits being taken, which can obscure the conditions under which the results hold. For example, the claim that $N, B \gg 1$ lacks a precise mathematical definition, making it difficult to assess the validity of the theoretical results in practical settings. The approach taken in the paper seems very heuristic. For example, starting with finite $M$ and taking the limit $M\to\infty$ omits many mathematical technicalities, why the claimed limiting properties and statements are well-defined and hold.
- A small limitation is that long training times are not well covered (Figure 6b). But this is acceptable as the long training regime is, in general, still very open.

**Typos in lines:** 128, 201, 202, 476.

### Questions
Partially critical questions ordered from most to least important:

1. **Large feature learning regime.** Which $\gamma_0$ is optimal and is this another hyperparameter that has to be tuned, or are there useful heuristics for choosing it? In your experiments it looks like the larger the better, but the $\gamma_0$ you consider are still pretty small. I am guessing in Figure 6 (b), larger values of $\gamma_0$ would result in a better than predicted scaling exponent even earlier in training? If so, this would be an acceptable but important limitation of the studied model, which should be acknowledged. I suggest running the experiment for larger $\gamma_0$ and discussing this limitation more deeply.
2. **Importance of constants.** While reporting the pure scalings is nice for readability, in practice, how important/huge are the omitted constants? This could arbitrarily change the global optimum of the test error given finite resources. Towards answering this question of how practically useful the results are, I suggest an experiment that compares the predicted compute-optimal scaling to empirical loss measurements like in Figure 4 but for the more practical datasets in Figure 6.
3. **Error of the approximation.** How good is your approximation in eq. (9)? In which cases does it fail?
4. **Extension to label noise.** How would label noise affect the results?
5. **Long training regime.** What is happening under long training in Figure 6b? Do you have an informed guess? Are structures in the images learned that are not covered by your simple distributional assumption?
6. In eq. (6), you state $\lambda_k\sim k^{-\alpha}$ and $\lambda_k^{-\beta}\sim k^{-\alpha \beta}$. Is this a typo?
7. In l. 192, ‘the components of $\omega^*, v^0(t)$ in the k-th eigenspace of $\Lambda$’, but $\Lambda$ was defined as a diagonal matrix in eq. (2). I guess here the k-th eigenspace of $K_\infty$ is meant?

### Soundness
2

### Presentation
3

### Contribution
3

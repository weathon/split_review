# The Inductive Bias of Minimum-Norm Shallow Diffusion Models That Perfectly Fit the Data

- Decision: Reject
- Scores: 6, 6, 5, 6

## Abstract
While diffusion models can generate high-quality images through the probability flow process, the theoretical understanding of this process is incomplete. A key open question is determining when the probability flow converges to the training samples used for denoiser training and when it converges to more general points on the data manifold. To address this, we analyze the probability flow of shallow ReLU neural network denoisers which interpolate the training data and have a minimal $\ell^2$ norm of the weights. For intuition, we also examine a simpler dynamics which we call the score flow, and demonstrate that, in the case of orthogonal datasets, the score flow and probability flow follow similar trajectories. Both flows converge to a training point or a sum of training points. However, due to early stopping induced by the scheduler, the probability flow can also converge to a general point on the data manifold. This result aligns with empirical observations that diffusion models tend to memorize individual training examples and reproduce them during testing. Moreover, diffusion models can combine memorized foreground and background objects, indicating they can learn a "semantic sum" of training points. We generalize these results from the orthogonal dataset case to scenarios where the clean data points lie on an obtuse simplex. Simulations further confirm that the probability flow converges to one of the following: a training point, a sum of training points, or a point on the data manifold.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
For three data settings in which Zeno et al. (2023) presented closed form solutions for shallow skip connected ReLU denoisers, the authors provide theoretical and empirical results on the convergence points for 1) probability flow 2) score flow, which is a simplification of the probability flow with constant step size. 

The authors first provide theoretical evidence showing that for orthogonal datasets (i.e., all samples orthogonal to each other), probability flow and score flow follow a similar trajectory starting from the same initialization point. Following that the authors provide theoretical evidence that for all three dataset settings score flow converges to the training points or sum of training points, whereas, probability flow also converges to the boundary of a hyperbox, the vertices of which are sums of the training data points, i.e., virtual points.

### Strengths
The topic is very relevant for duplication and generalization in diffusion models and their inductive biases. Paper is well organized and the contributions are novel.

### Weaknesses
While the results present in the paper have important connection with memorization/duplication in diffusion models, the presented work does not take the number of samples into account. Prior work related to memorization in practical diffusion models have often shown that i) with oversampling in the training dataset duplication increases [https://arxiv.org/pdf/2305.20086] ii) with increased number of samples in the datasets, duplication decreases [https://arxiv.org/pdf/2212.03860].

What is the connection with the number of samples in a dataset and the stable points? How would the distribution of convergence points in figure 3 b change subject to the number of training samples? We do see more convergence near training points compared to virtual points, would that be effected by a higher number of training samples? Do we expect to see more boundary points instead if training samples are increased?

Line 430: What is meant by "The decrease in percentages is due to small deviations
in the ReLU boundaries of the trained denoiser compared to the theoretical optimal denoiser."

Line 442: Why is 0.2 set as the l_inf threshold? Could the authors show how continuously changing this value affects the distribution of data points.

Line 470: "specifically in our example for the first 100 denoisers, the noise level is not small compared to the norm" would the authors be able to elaborate this part for clarity? Why is the noise level small for only the first 100 denoisers? Why are they not expected to have stable virtual points?

### Questions
Line 430: What is meant by "The decrease in percentages is due to small deviations
in the ReLU boundaries of the trained denoiser compared to the theoretical optimal denoiser."

Line 442: Why is 0.2 set as the l_inf threshold? Could the authors show how continuously changing this value affects the distribution of data points.

Line 470: "specifically in our example for the first 100 denoisers, the noise level is not small compared to the norm" would the authors be able to elaborate this part for clarity? Why is the noise level small for only the first 100 denoisers? Why are they not expected to have stable virtual points?

### Soundness
2

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
Diffusion models approximate data distributions by estimating the score of the probability density. In practice, however, rather than learning the exact empirical score, these models often learn a smoothed version of it. This paper examines when data is memorised in diffusion models and the inductive biases that emerge when minimal norm solutions of the neural network weights are considered. The findings suggest that, in such cases, empirical data points act as attractive sinks for the score function, meaning that generated samples will tend to recover the nearest empirical data point to their initialisation. Several simplified settings are explored to analyse these effects in detail.

### Strengths
This paper is well-written and effectively demonstrates that, in simplified cases, diffusion models can recover the data distribution. A particularly interesting result is that, even in these simplified settings, a diffusion model may recover the sum of the data points, which already suggests some degree of generalisation beyond the empirical data distribution. This naturally leads to an exploration of the convex hull of the data distribution, which the authors address in Section 4. I consider this a novel and valuable contribution to the literature, and I appreciate the examples provided in Section 4.2.

The simulated data experiments provided are enlightening and well motivated by the theory. There is a clear correlation between the derived theorems and the computational experiments shown, revealing that for minimal norm denoisers, data on the hypercube of the empirical dataset may be recovered.

### Weaknesses
The main weakness of this work is that the theorems rely on strong assumptions to analyse the simplified cases considered. However, this is generally well addressed in the limitations section of the paper. One concern I have about the scope of the work is that it operates in the "low noise" regime without explicitly defining what this entails. For time 
$t$ very close to zero, where the diffused density is simply a Gaussian mixture of the data distribution, I don't believe this setting is particularly interesting. However, for $t$ large enough that meaningful generalisation occurs, the results become more significant. I believe the authors investigate this in their hypercube examples, but it would be helpful for them to clarify what they mean by "low noise" to ensure they are not referring to the earlier, less informative case.

I would also encourage the authors to further explore the effect of early stopping in their simulated examples, potentially through an ablation study on the early stopping parameter and its impact on generalisation over the hypercube. While I agree that early stopping likely induces some smoothing of the empirical data distribution, it would be interesting to determine to what extent it increases the likelihood of generated samples residing on the hypercube of the empirical data. The authors' current observation of this generalisation is intriguing, but further analysis could provide more valuable insights.



### Questions
Could the authors provide an ablation study, perhaps in 2D, to demonstrate how different early stopping times influence the generalisation of the learned dataset compared to the empirical dataset? My understanding is that, before reaching an attractive sink (an empirical data point), the generated data traverses the hypercube formed by the empirical data. In this case, varying early stopping times should lead to different learned densities. Could the authors confirm whether my interpretation is correct? Including such a study in the paper would help to illustrate the implications of the theorems presented.

Additionally, could the authors comment on what they might expect if the minimal norm assumption were lifted? At present, the intuition behind why minimal norm would lead to different results from training without this constraint is unclear to me. Including a simple comparison between minimal norm training and a neural network trained without this constraint in a simplified setting might help clarify this choice and assist readers in better understanding its impact on the findings.

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
This paper studies the convergence of the probability flow and the score flow equipped with a two-layer neural network as a denoiser.
In particular, the neural network interpolates the training data with minimum representation cost.
Then for three different types of training data, namely orthogonal datasets, obtuse-angle datasets, and equilateral triangle datasets, the authors characterize the convergence of the probability flow and the score flow to either the actual training data points or certain sum of the training data points.
The theoretical analysis is supported by numerical experiments.

### Strengths
1. The problem studied in the paper is interesting, and the analysis seems original in its approach to studying the convergence of the probability flow and the score flow, and provides interesting results on the convergence of these flows for synthetic settings.
2. By leveraging the explicit form of two-layer neural networks that interpolate the training data with minimum representation cost, the results regarding the convergence of the probability flow and the score flow are theoretically well characterized and provide very quantitative characterizations.

### Weaknesses
1. Some notions in the paper lack formal definitions. For example, what are the the hyperbox defined by the data and its boundary? Also, what's the definition of normalized score flow mentioned in the second paragraph in Section 4.2? It is unclear how the normalization is performed and how it affects the analysis.
2. Some assumptions are made without dicussion about their meaning or necessity: 1) quantities like $\rho_0(\epsilon),T_0(\epsilon,\rho),T_1(\rho)$ in Theorem 2, and $\tau(y_T,\rho_T)$ in Theorem 3 lack interpretation. Similar for other quantities in the other theorems; 2) also, the assumptions on ${u_i}_{i=1}^n$, and the use of the Taylor's approximation in the small-noise level regime require more justification and discussion. It is not clear why these assumptions are necessary, and how they might limit the applicability of the results.
3. The statements of the main theorems are not very clear. Specifically, the meaning of "converge to" is unclear. For example, in Theorem 3, by "converge to this vertex", does it mean that $y_0$ is exactly the vertex? The theorems lack precise mathematical statements, making it difficult to verify their correctness and understand their implications.
4. The three types of training data seem artifical and it is not clear how they are related to real-world data. Related to this, the theoretical analyses seem to heavily rely on the explicit solution for the min-norm interpolator provided in Equation (17), and the results do not extend beyond this. It would also be helpful if the authors could discuss the technical challenges and novelty of the current paper compared to existing works. The limitations of the analysis to these specific data types and the minimum norm interpolator need to be addressed.

### Questions
1. Under Equation (11), for the approximation $\nabla \log p(y_t,\sigma_t)\approx s(y)$, the right-hand side does not depend on $t$? Also, in Equation (12), since $g_r$ takes different values at different $r$, does this suggest that we need different neural networks for different $r$? Further related to this, for the results on the probability flow, which ODE is being analyzed?
2. In Equation (16), on the right-hand of the second equality, it should also be $\inf_{\theta: h=h_\theta}$?

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
This work considers particular forms of robust score-based denoiser which map points in a ball around a training point to the training point itself. Based on the closed-form derivations of Zeno et al. (2023) for 'min-cost' robust shallow denoisers, they derive the score dynamics for three main experiments. The score is presented in the variable noise (variable robustness) as well as fixed noise (robustness) case, which have similar generalization dynamics for small noise and finite time reverse diffusion.

### Strengths
* The background is clearly presented and easy to follow. Contributions are accurate and clearly stated.
* The experiments follow the presented theory well, with illustrative figures. The experiments also exhibit interesting phenomena, such as virtual quadruplets being stable even in the case of inexact denoising, as suggested by theory.
* The theory seems correct (mostly computation of piecewise functions), but I have not checked line-by-line.

### Weaknesses
 * The nature of the work gives limited future work directions, as it is mainly deriving properties of specific closed-form solutions. I do not see how to generalize this work to e.g. minimum RKHS norm solutions, NTK, weight regularization etc., as the form of robustness considered is quite nonstandard. The analysis is confined to a very particular, almost piecewise-linear, form of denoiser, and it's unclear how these results would extend to more general classes of denoisers used in practice.
* It is unclear how the simple observation of Prop. 1 contributes to the work, as well as the comment afterwards: ``training points have high probability''. This does not follow from Prop. 1 at all, as being a stable stationary point does not imply high probability. The connection between the stability of training points and their probability under the learned distribution is not rigorously established, and the claim that the score flow will converge to training points with probability 1 requires stronger assumptions than provided.
* The experiments seem to introduce "diffusion sampling". Is this probability flow or something else? If it is, then this should be made clear. If not, diffusion sampling needs to be defined and probability flow should show up somewhere in the experiments. The description of the sampling process is vague, and it's unclear whether it aligns with standard probability flow sampling or some other method. This lack of clarity makes it difficult to assess the validity of the experimental results.

### Questions
* Typo in the reference on p.5? There is no Theorem 4 in Zeno et al. (2023).
* Eq (17, 39): Should there be a minus sign in the second ReLU? 
* Instances of 'rays' in Sec. 4.2 may be better off as 'chords', as the required condition requires that the initial point $y_0$ is almost in-between $x_i$ and 0. Rays typically refer to infinitely long half-lines of the form $\{\lambda x | \lambda >0\}$.
* "The mathematical connection between the score function and the denoiser" is sometimes referred to as "Tweedie's identity", maybe the authors would consider putting this in.

### Soundness
3

### Presentation
3

### Contribution
2

# Course Correcting Koopman Representations

- Decision: Accept
- Scores: 8, 6, 6, 8, 6

## Abstract
Koopman representations aim to learn features of nonlinear dynamical systems (NLDS) which lead to linear dynamics in the latent space. Theoretically, such features can be used to simplify many problems in modeling and control of NLDS. In this work we study autoencoder formulations of this problem, and different ways they can be used to model dynamics, specifically for future state prediction over long horizons. We discover several limitations of predicting future states in the latent space and propose an inference-time mechanism, which we refer to as Periodic Reencoding, for faithfully capturing long term dynamics. We justify this method both analytically and empirically via experiments in low and high dimensional NLDS.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors of the study investigated the use of Koopman autoencoders to model complex, nonlinear dynamical systems. They explored different approaches for making long-term predictions and showed that generating predictions solely within the latent space had two potential challenges: 1) It was unable to effectively capture the behavior of multi-stable systems that switch between multiple fixed points. 2) It violated the existence and uniqueness theorem of initial value problems, which establishes the uniqueness of solutions in dynamical systems. To address these challenges, the authors introduced a technique called "periodic reencoding." This method strikes a balance between not using reencoding at all and reencoding at every step, and it was found to yield the best practical results in their experiments.

### Strengths
- The paper is well-written, featuring a fascinating main idea, and employing innovative and effective methods with good results.

- The overview provided in the appendix is very helpful and is written in a precise and technical mathematical style.

- The visualization provided in Fig. 1 is very helpful in providing a clear illustration of their method.

### Weaknesses
 **A minor point**:  Regarding the sentence "This characteristic becomes especially significant when the dimensionality of the latent space is substantially larger than that of the original space, i.e., n >> d, ...", why is this case considered more important? While it's true that a mapping to a larger dimensional space is not surjective, as discussed in the paper, it seems that the lack of injectivity of the map is more critical. So, since a mapping to a smaller dimensional space is not injective, wouldn't the case of n << d be more problematic?

**A few questions**:

1. When it comes to learning chaotic dynamics, what are the advancements offered by the proposed method compared to using RNNs with teacher forcing, as presented in the following papers?  

[1] F. Hess, Z. Monfared, M. Brenner, D. Durstewitz, Generalized Teacher Forcing for Learning Chaotic 
Dynamics, Proceedings of Machine Learning Research (ICML 2023), (2023). 

[2] J. Mikhaeil, Z. Monfared, D. Durstewitz, On the difficulty of learning chaotic dynamics with RNNs, Advances in Neural Information Processing Systems (NeurIPS), (2022).

2. Regarding eq. (9), it apears that the Jacobian $J_{\psi}$  of  $\psi$ is assumed to be a constant matrix. If this is the case, how can one ensure that it remains a fixed matrix? It may vary depending on the specific points at which it is calculated and could differ across different points.

3. How effectively would the proposed method perform in capturing the dynamics of a multi-stable system with a stable fixed point and a periodic attractor, or possibly with two periodic attractors?

4. How changes in the hyperparameters $\Delta t$ or $k$ can impact the results? Does an optimal value always exist for that?

5. Why do the authors use an MLP instead of K (e.g., on page 6)? How does the choice of activation function affect the performance of the MLP? Were other activation functions considered, and if so, how did they compare to the chosen function? Can the MLP be replaced with other types of neural networks, such as convolutional neural networks or recurrent neural networks? How would this affect the performance of the proposed framework?

### Questions
Please see above!

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work proposes an autoencoder model for dynamical system data based on Koopman theory; observed variables are mapped to the "Koopman feature" space in which the state evolution is linear.  The authors proposed a periodic re-encoding scheme that avoid the issues of trajectory crossing in observation space and the inability to model switching dynamics.  The authors demonstrated that the proposed method with re-encoding leads to improved state prediction and controlling.

### Strengths
- This paper is mostly well-written.
- The proposed method demonstrates promising empirical performance.

### Weaknesses
 - I feel the theoretical benefits of re-encoding are not well explained.  It appears that re-encoding should be most useful in eliminating undesirable local optimas; if the model is correctly specified, the AE objective should have the same global optima with or without re-encoding.  It is thus not clear whether it is a principled solution to the switching dynamics issue, which is one of the two motivations for this work; if the dynamics cannot be (globally) linearized the model is misspecified in either case.

- While the experiments demonstrate the benefits of re-encoding for autoencoding approaches, it is not clear why we should restrict to such approaches for control. There is also a general lack of comparison with baselines, e.g. with Mondal et al (2023).

- As a minor point, the reference to deep state-space models such as S4 is slightly misleading as they are often applicable to stochastic systems, whereas this work studies deterministic systems.

### Questions
See above.

## Post-rebuttal update

Thank you for your response.  I am raising the score as my concern is largely addressed.  I remain uncertain about the interpretation of the RL experiments; while they have indeed demonstrated the utility of the proposed method in the Koopman framework, the lack of baseline comparisons makes it somewhat difficult to put them in context, i.e. to what extent it is addressing an issue in an application where the Koopman framework is of interest.  As I am not very familiar with this area, I will defer the judgement of this issue to the other reviewers.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces the concept of periodic reencoding into the field of Koopman autoencoders. The idea is that, rather than propagating the dynamical system solely in the latent space, we periodically re-encode the true-space state $x_t$ to the latent space. This overcomes possible issues with $\phi$ and $\psi$ not being exact inverses (due to lack of bijectivity).

### Strengths
- the concept of periodic re-encoding is clear and simple
- it leads to across-the-board improvements in performance

### Weaknesses
 - any underlying mechanism governing periodic re-encoding is not discussed. For example, are there deficiencies in the encoder or decoder that, if adjusted, remove the need for reencoding, or change the optimal period? It is unclear if the need for re-encoding stems from limitations in the encoder/decoder architecture, or if it is a more fundamental property of the latent space representation.
- how is the optimum period chosen? Since every step reencoding is worse in terms of performance than periodic reencoding, this is not a simple tradeoff in terms off costs. The paper does not provide a clear methodology for determining the optimal re-encoding period, and it's unclear if this is a hyperparameter that needs to be tuned for each individual system.
- what causes do we hypothesise for "long term drift"? Perhaps during training the encoder does not learn to "use" all the latent space. Thus, there exist points in latent space with a decoding that is not properly trained. This is pure conjecture, but it would be beneficial for this paper to investigate these issues. The paper does not explore the reasons for long-term drift in detail, and it is unclear if this is due to issues with the latent space representation or other factors.
- text is not legible in some figures (Fig 3, 4, 5 font size too small, Figure 6 more extreme)

### Questions
- has equation (2) been used in previous papers? I see that Lusch et al. (2018) used something similar. It would be helpful to precisely clarify.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work we study Koopman autoencoders to model nonlinear dynamics, specifically for long term state forecasting. The authors propose Periodic Reencoding, an inference-time mechanism that incorporates far future (multiple-step ahead) loss for faithfully capturing long term dynamics. The proposed method is validated both analytically and empirically via experiments in low and high dimensional NLDS.

### Strengths
The proposed Periodic Reencoding improves long term forecasting of deep Koopman autoencoders. 

It does not require long sequence training. 

The manuscript is well written.

### Weaknesses
The Periodic Reencoding works well especially with oscillator dynamics. It is likely related to the fact that those dynamics is periodic. It would be interesting to show how it works with continuous attractors.

It's worthy discussing the "optimal" $\Delta t$ and its relationship to the dynamics. For example, Fig. 5 shows the best are the middle ones.

### Questions
It's worthy discussing the "optimal" $\Delta t$ and its relationship to the dynamics. For example, Fig. 5 shows the best are the middle ones.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Given a fully observable deterministic nonlinear dynamical system described by $dx/dt = f(x)$ such as Lotka-Voltera predator prey population models or chaotic pendulums, Koopman theory states there exists a mapping to a (typically much higher, possibly infinite, dimensional) space $z = g(x)$ where the dynamics are linear, fully described by $dz/dt = Kz$. (I am loosely reminded of the use of kernels in SVMs, a binary classification dataset where classes are not linearly separable can be mapped to a higher dimensional space where classes are linearly separable).

There is an active body of work using the Koopman framework where the mapping function $z = \phi(x)$ is a learnable neural network trained with a corresponding inverse mapping $x = \psi(z)$ which together form an encoder – decoder pair in an autoencoder architecture (albeit where latent $z$ dimension may be lower or higher than the data $x$ dimension), together with this autoencoder, the method learns the transition matrix across time in state latent space $z_{t+1} = K z_t$.

From an initial datapoint $x_0$, time series prediction is performed by encoding the initial point $z_0=\phi(x_0)$, applying the latent state transitions, $z_t = K^tz_0$, and decoding the latent states $x_t = \psi(z_t)$. The authors state that this inference procedure can fail for long term prediction as latent to trajectories that do decode to a sequence of  “drifting” datapoints. Prior works have proposed heuristic solutions such as training on long sequences and restricting the eigen values of the latent space transition matrix K. The authors propose an alternative heuristic they name “periodic re-encoding” where, at every kth transition also incorporates a decoder – encoder pass, i.e. 

$z_{t+1} =$

$ K\phi(\psi(z_t))$ if $t \text{mod} k ==0$ 

$Kz_t \quad \quad \quad$ otherwise

The authors perform experiments on simple well known NLDSs with and without periodic reencoding and make a strong case for the efficacy of periodic re-encoding. The authors apply the method to more challenging datasets from D4RL library and again demonstrate the improvement in performance as a result.


## Update After Rebuttal
I sincerely apologize for missing the response period, I hope the authors can still read this!

- my initial judgement on the value of Koopman representations seems misguided, and the authors and other reviewers responses have significantly increased my appreciation and I have raised my paper score to a weak accept whilst also reducing my confidence score appropriately.

- I now understand the bilinear approach, I did not see the inverse matrix (it as a half step forward and a half step backwards taken in reverse)

### Strengths
- the experiments appear to be an ablation study on the effect of periodic re-encoding and show a clear benefit
- the inclusion of both toy and more complex examples is much appreciated.
- there are many works combining autoencoders with latent space transition models. Presumably periodic re-encoding can be applied to any model with the same autoencoder + latent space transition architecture, is it more general than the authors present? 

- I felt it was generally well structured and written, although a few minor writing comments mentioned below.

### Weaknesses
## Update After Rebuttal
See Summary

# Original Review

For context in the follow up discussion, I would like to state my intuition of Koopman theory is that any finite dimensional nonlinear system can be “lifted” into a higher dimensional space where dynamics are linear, in other words a complex low dimensional nonlinear transition function can be replaced with complex nonlinear high dimensional mapping and a simple transition function, we have just moved the “non-linearity-ness” from one place to another and Koopman theory states that this is universally possible for any NLDS, although in practice this may be very difficult or even impossible in finite dimensions.

## Major Points
- If I understand correctly, when $dim(z) > dim(x)$, the data points encode to a $dim(x)$ manifold embedded in the z-space. One interpretation is that the re-encoding takes latent points that have drifted away from this from the latent data manifold and puts them back on. However, if this were the case, re-encoding every step would have the best results.
- I struggle to agree with the conclusions drawn by the example given in Appendix C.  I view Appendix C as a special case of failure to specify good mappings. The claim that periodic reencoding solves the problem I find strange. If I understand correctly, the perturbations introduced by the decoder-encoder pass allow the latent state to jump between basins of attraction of each fixed point? Presumably these perturbations are just noise and an artefact of the (arbitrary) precision achieved by model training convergence.
- what is the benefit of periodic re-encoding, clamping latent representations to the data manifold or adding noisy perturbations?
- the authors include non-linear transitions as a baseline, while it is nice to have more baselines, as I understand, linear transitions is the only reason to use Koopman theory. As expected, the (strictly higher capacity) non-linear transition outperform the liner transitions.
- Given the re-encoding is not specific to Koopman, and that Koopman (linear) transitions predictably perform worse than non-linear transitions, this paper’s focus on the Koopman framework seems unnecessary.
- there are many many autoencoder + latent space transition models that vary mainly by application specific architectural differences (e.g. pixels/graph/vectors require CNN/GCN/MLP encoder) and their training losses (L2, ELBO, Cross entropy etc), and a quick google for "latent dynamics" and "deep kalman" yields many results, many that have linear latent transitions
  - https://papers.nips.cc/paper_files/paper/2017/hash/7b7a53e239400a13bd6be6c91c4f6c4e-Abstract.html
  - http://www.approximateinference.org/2015/accepted/KrishnanEtAl2015.pdf
  - https://arxiv.org/abs/1811.04551


## Minor Points
- Section 2, first paragraph does not help unfamiliar people understand Koopman theory or MDM (and familiar people do not need to be told). I would suggest dumbing this down as the level of Koopman theory required for this paper can be explained very easily.
- Bibliography: many of the references have titles, names and dates but are missing journal/conference information
- Appendix E is a nice addition, yet it feels somewhat arbitrary to cite a handful or RNN papers when the time series modelling literature is vast and the autoencoder + latent dynamics literature is I feel is more closely related this work than RNNs.

### Questions
- For each problem, can you state the dimensions of $x$ and $z$ in the main paper. (I couldn’t see them in Appendix B)
- given linear latent transitions are worse and periodic reencoding is more general than Koopman autoencoders, what is the justification for the authors to focus on Koopman representations? What is the benefit of the Koopman framework over any other autoencoder based time series model?
- Equation 6: it appears the transition matrix is applying ½ of a forward time step and then ½ of a backward time step? I would understand if the transition matrix was made of many incremental time steps e.g. $\textbf{K}=(I + \frac{\delta}{n}K)^n$ where $n =2$ (and consequently $\textbf{K}=exp(\delta K)$ as $n>\infty$)
- what is the benefit of periodic re-encoding, clamping (high dim) latent representations to the latent data manifold or adding noisy perturbations?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

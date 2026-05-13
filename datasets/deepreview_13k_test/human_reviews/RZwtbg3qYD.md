# HOPE for a Robust Parameterization of Long-memory State Space Models

- Decision: Accept
- Scores: 5, 8, 8, 6, 6

## Abstract
State-space models (SSMs) that utilize linear, time-invariant (LTI) systems are known for their effectiveness in learning long sequences. To achieve state-of-the-art performance, an SSM often needs a specifically designed initialization, and the training of state matrices is on a logarithmic scale with a very small learning rate.
To understand these choices from a unified perspective, we view SSMs through the lens of Hankel operator theory.
Building upon it, we develop a new parameterization scheme, called HOPE, for LTI systems that utilizes Markov parameters within Hankel operators.
Our approach helps improve the initialization and training stability, leading to a more robust parameterization.
We efficiently implement these innovations by nonuniformly sampling the transfer functions of LTI systems, and they require fewer parameters compared to canonical SSMs. When benchmarked against HiPPO-initialized models such as S4 and S4D, an SSM parameterized by Hankel operators demonstrates improved performance on Long-Range Arena (LRA) tasks. Moreover, our new parameterization endows the SSM with non-decaying memory within a fixed time window, which is empirically corroborated by a sequential CIFAR-10 task with padded noise.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This work proposes an alternative parameterization for SSMs using the Hankel operator of the dynamical system, called HOPE. HOPE learns the Hankel operator of a linear dynamical system, instead of directly learning the dynamics matrices as in other SSMs. By using techniques and results in Hankel operator theory, authors show that HOPE is more robust to noise and has long memory. Finally, experiments on LRA show that HOPE is competitive with other SSMs and outperforms baselines on several tasks.

### Strengths
This paper proposes a theoretical framework for analyzing SSMs, and there are many supporting graphs and experiments. The plots are well-executed, and the experiments are LRA has a good set of baselines. I also appreciate the noise-padded sCIFAR-10 experiment as an ablation. The algorithm is clearly written.

### Weaknesses
1. Motivation: random init in models like Mamba also works, so the initialization issues seem to be limited to certain SSMs.
2. HOPE-SSM does not have non-decaying memory: these are asymptotically stable systems, instead of marginally stable systems, so they cannot have arbitrarily long memory. This point is not clarified upfront in the paper.
3. HOPE-SSM on Path-X, which is the task with the longest memory in LRA, does not outperform S5. This raises some concerns on the long-memory capability of HOPE-SSM in practice.
4. Though authors provide expressivity results on HOPE, there is no guarantee on learning with this parameterization (convergence, etc). 

Please also see questions.

### Questions
1. In section 3 before 3.1, how should I think about $\epsilon$? Under init3, if $\epsilon=$1e-4, then the frozen model has a higher numerical rank, since there is considerable mass below 1e-4 for the trained model, but the frozen model has worse performance?
2. Why is numerical rank the correct metric instead of the sum of the smallest eigenvalues? ROM quantifies the approximation error using the latter.
3. Theorem 2's upper and lower bounds are off by n, which is significant when the hidden dimension is large (regime of interest for high-order LTIs). In addition, Theorem 4 has a $\sqrt{n}$ on the right hand side, but it's not clear whether the worse $n$ scaling for default SSM parameterization is tight. Can authors comment on this?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
The paper first examines the stability of SSM training and the recently used initialization method through the lens of Hankel operator theory. The authors argue that by decreasing the effective rank of the Hankel operator, the system loses its expressivity for modeling complex sequences. They then propose a new parametrization of LTI systems based on the Hankel operator, which improves robustness and performance due to the stable spectrum of the Hankel operator during training. Finally, they demonstrate that with this parametrization, memory remains practically constant within a fixed time window. They test this framework on the sCIFAR-10 dataset.

### Strengths
1. I believe HOPE is very well motivated by Section 3. The analysis presented in that section clearly illustrates all the issues with current methods based on standard parametrization. In a nutshell, Figures 2 and 3 perfectly summarize the entire section.

2. The three advantages of HOPE are well explained and essential. It is impressive that the authors managed to achieve all three benefits with a simple new parametrization.

3. The entire framework seems very simple, yet powerful.

### Weaknesses
Some results lack sufficient motivation. For example, the setup introduced before Theorem 1 could be better explained—why is it reasonable to sample entries of $A$ from $F_a$​ and entries of $\overline{B}\circ\overline{C}^\top$ from a standard normal distribution? Similarly, the discussion preceding Algorithm 1, as well as the algorithm itself, appears more complicated than necessary, with essentially the same information repeated three times. I would prefer having only Algorithm 1 with the full expressions for variables, as in the current prelude to Algorithm 1.

### Questions
1. If Mamba achieves SOTA performance, could you explain why there is no experimental comparison with it? If there are no technical limitations and the comparison is meaningful, including it could further enhance the quality of the paper.

2. Could you please explain how Theorem 4 guarantees the numerical stability of HOPE?

3. In Figure 6 (right), why does the memory decay of HOPE still appear significantly smaller than that of S4D after $t=n=64$? Shouldn't HOPE have no memory after $n$?

4. The Hankel matrix looks very similar to the SSM convolution kernel. Could you please explain the differences between the two?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper proposes a new parametrisation, named HOPE, for Linear Time Invariant (LTI) State Space Models (SSMs), based on the Hankel operator, that improves the performance and makes training more stable. The proposed parametrisation reduces the SSM parameters to 1/3 of the original and works in the frequency domain, hence the Fast Fourier Transform (FFT) and its inverse need to be used during the forward pass. Fortunately, the time and memory complexity of the forward pass remains the same as that of standard LTI SSMs using the convolutional form. The authors first show how current parameterisations can perform poorly both at initialisation or during training and how this can be explained by their corresponding Henkel operator being low-rank (Theorem 1, Figure 3) and the parameterisation being numerically unstable (Theorem 2, Figure 4). Then, they show how their parameterisation effectively mitigates both issues (Theorems 3-4, Figure 5) and does not have an exponentially decaying memory (Advantage III). Each claim Is supported both theoretically and empirically. Empirically, the authors test different parameterisation, initialisation and training schemes on the (noisy-padded) sequential CIFAR dataset, and on the Long Range Arena, also showing how HOPE outperforms previous LTI parameterisations in terms of Test Accuracy.

### Strengths
1. Strong empirical and theoretical evidence in favour of the proposed parameterisation.
2. Clearly written.
3. The algorithm is novel, albeit SSM working in the frequency domain have been proposed by (Agarwal et al. 2023).

### Weaknesses
1. Some limitations are not experimentally investigated. In particular, the method seems to weigh the input time steps belonging to a fixed window equally and discard the others. This could be a limitation but all tasks considered in the experiments do not seem to benefit from a recency bias (see also the first question). 
2. Limited discussion of Related works (Minor).

### Questions
1. How does the parameterisation behave in tasks where a recency bias can be beneficial? For example this is the case for generative Language Modelling.
2. Can the authors comment on the relationship between the learned discretization parameter $\Delta_t$ and the size of the window of non-discarded inputs of the HOPE SSM? Is the full input always considered? How does this change during training? Such discussion and potential experimental evidence could strengthen the paper.

Comments:
1. Information on the actual runtime could be moved the main paper since now it is quite hard to find (it is in the last page of the appendix). 
2. The paper could benefit from having a discussion on how HOPE differs from spectral SSMs (Agarwal et al.2023) and the stable parameterisation proposed by Wang & Li (2023), which are probably the closest works This could be placed in the appendix. Such discussion could potentially address pros and cons of each approach in addition to the brief discussion in the introduction.

Minor: 
- Line 159-161: Can the authors provide a definition of the function space $\ell^2(\mathbb{N})$   and $L^2([0,\infty])$?
- Line 208: imaginal axis -> imaginary axis

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper develops a new parameterization scheme to help improve training of state space models (SSMs) in sequence modeling. The new parameterization method is based on Hankel operator theory, which resolves the low-rank and numerical instability issues of an LTI system, and the parameterized SSMs could enjoy non-decaying memory. Numerical experiments are conducted on the long range arena benchmark.

### Strengths
* The paper is written clearly and the ideas have been presented in the proper order.

* The idea using Hankel operator theory to parameterize state space models is novel, which can provide more insights for other recurrent architectures on sequence modeling.

### Weaknesses
* The connections of the Hankel rank/stability and the SSM performance seem not that positively correlated in this paper. For example, from Figure we see that the numerical rank of HOPE-SSM is even lower than init3 before and after training, but these two initializations produce similar numerical performance on the sCIFAR-10 task. Does it mean that even slightly low rank Hankel matrix can achieve good results? 

* From Algorithm1, the Hankel operator method looks very similar to the convolution method, it would be better if the authors could add more discussion on these two methods. For example, [1] can be a good reference. 

* The notations for $A$ and $\bar{A}$ are not consistently used in this paper. From my understanding, $A$ is the hidden matrix for the continuous system and $\bar{A}$ is the hidden matrix for the discrete system. The HiPPO-Legs initialization is for $A$ matrix, and $\bar{A}$ contains the information of the timescale $\Delta t$. It would be better to distinguish these two notations when making statements. For example, in Figure 4, the perturbation is added to the continuous system while the Hankel singular values are calculated  for the discrete system, and the discrete system contains the information for $\Delta t$. It seems that $\Delta t$ is set to be $1$ in this paper, but in practice, the timescale is scaled based on the sequence length. So what is the reason to take $\Delta t = 1$?
Also, it would be better if the authors could add more details on how the perturbation is added here.

[1] Li, Yuhong, et al. "What Makes Convolutional Models Great on Long Sequence Modeling?." The Eleventh International Conference on Learning Representations.

### Questions
* Why do the authors choose to show the Hankel singular values of SSMs trained after 10 epochs instead of after the whole training process (e.g. Figure 3 & 5)?

* How do the authors validate the assumption on the distribution of the diagonal entry of $\bar{A}$ in Theorem 1? For linear recurrent unit [1], $\bar{A}$ is initialized such that $a_j$ is uniformly distributed in a disc $[r_{\min}, r_{\max}]$ where $r_{\min}, r_{\max}$ are both close to $1$.

* Also for Theorem 1, the theoretical bound does not indicate $\beta < 1$, but $\beta \leq 1$ instead. Is there a way to mitigate the logarithmic term in theory?





[1] Orvieto, Antonio, et al. "Resurrecting recurrent neural networks for long sequences." International Conference on Machine Learning. PMLR, 2023.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes an alternative parameterisation of the state space models, where the SSM layer's dynamics is replaced by parameterising rows of the Hankel matrix. It is shown that classical SSM parameterisation tends to give rise to Hankel matrices with fast decaying Hankel singular values, and is posited to correlate with poor performance for long memory tasks. The proposed parameterisation does not involve repeated multiplication of the state space matrix, hence avoiding this shortcoming. These are supported by theoretical results, and the proposed method is shown to improve upon existing SSM variants on sCIFAR and long range arena.

### Strengths
While the paper's identified limitation (i.e. favoring exponential decay in memory)  of SSM is widely known and studied, its use of the Hankel numerical rank to study it is interesting. The theoretical results are carefully derived and the practical results show good promise. Finally, the paper is carefully written and the explanations of their approach and results are excellent.

### Weaknesses
The main weakness, to my understanding, is the premise of the proposed approach. In classical LTI and SSM literature on system identification (e.g. Tangirala, A. K. *Principles of System Identification: Theory and Practice*), the very reason why SSMs were introduced in favor of convolutional models is its ability to handle infinite sequences with a finite parameterisation. The present approach appears to go in the reverse direction:

1. In particular, I cannot see what is the difference between HOPE-SSM and the classical convolutional model (the most basic sequence to sequence model in LTI literature, where one directly parameterises the impulse response function), with the filter size $n$ is chosen as the same the original SSM's hidden state dimension. In fact,  the parameterisation (5) via $h$ seems to be exactly the convolution filter (impulse response), since each row of the Hankel matrix is just the impulse response (shifted by 1 for each subsequent row). If this were the case, the method has little to do with Hankel matrix, but is rather just a convolutional model based on parameterising the impulse response function.
2. The HOPE-SSM model's size scales with sequence length if it must process long sequences. In particular, all memory functions that can be represented are finitely supported, so it is not accurate to say that this improves upon SSM parameterisation, which is used in preference to convolutional models *precisely* because it allows the parameterisation of memory of infinite support with finite number of parameters (albeit introducing curse of memory due to forcing an exponential decay, as observed in previous literature). 
3. The observed strengths of HOPE-SSM (non-exponential decay) are also present in convolutional networks (e.g. WaveNet with small filters but multiple layers, or single layer direct parameterisation of the impulse response), thus the numerical comparison should be made with those models, instead of just SSM variants.

### Questions
1. Can the authors clarify what is the fundamental difference, if any, of the HOPE-SSM and classical convolutional models that directly parameterises a truncated impulse response function? Looking at Alg 1, the only possible departure appears to be in the for loop in steps 6-7. 
2. Can the authors clarify how (or if) the proposed model can process long sequences without increasing the filter size, while still meaningfully extract memory structures? 
3. If different, can the authors comment and demonstrate both theoretically and numerically their advantage against convolutional-type sequence models (e.g. WaveNet/temporal CNNs, and directly paramterising the impulse response function)?
4. Is the conclusion of Theorem 1 verified by results in Fig 3 quantitatively?

Post rebuttal/revision: Appreciate the comparison with discrete convolutional models to assess the model's performance. I think while the novelty is still limited (it is at most a rescaled temporal convolution model with large filters), the performance appears good and the paper is well written. I have increased my score.

### Soundness
2

### Presentation
4

### Contribution
2

# Spectral Shaping for Neural PDE Surrogates

- Decision: Reject
- Scores: 5, 5, 5, 5

## Abstract
Neural surrogates for PDE solvers suffer from an inability to model the spectrum of solutions adequately, especially in the medium to high frequency bands. This impacts not only correct spectral shapes, but also stability and long-term rollout accuracy. We identify three convergent factors that exacerbate this phenomenon, namely: distribution shift over unrolls, spectral bias of the MSE loss, and spurious high frequency noise, or _spectral junk_, introduced by the use of pointwise nonlinearities. We find that _spectral shaping_, filtering the spectrum of activations after every layer of pointwise nonlinearities, is enough to reduce spectral junk and improve long-term rollout accuracy. We show spectral shaping not only fixes the learned spectrum (down to machine precision in some cases), but also leads to very stable neural surrogates. We validate these findings on a suite of challenging fluid dynamics problems in the field of neural PDE surrogacy, promoting a clear need for more careful attention to surrogate architecture design and adding a new and simple trick to the practitioner toolbox.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper proposes a method to post-process the spectra of the latent fields as well as the output for the predictions from a neural surrogate model (applying a low-pass filter for every latent field after activation). This is definitely an interesting paper that tries to address a commonly recognized problem for the neural surrogates model (the combination of distribution shift and the spectral bias) from an architectural pov.

### Strengths
- This paper chose interesting datasets to study. All datasets are NS-based, i.e., there will always be an energy cascade forming after a certain "burn-in" time, so one has stable statistics to play with and to compare with.
- The proposed method is simple.

### Weaknesses
There is no theoretical analysis of why low-pass filter improves the stability of the repeated application of the flow map. The lack of this sort of analysis is okay though and does not affect my final score. There are many details for experiments or methods used in the experiments missing, examples:
- No modern baselines, such as FNO or FNO variants, Transformer-based NOs (Galerkin, OFormer, GNOT, and many others), or DeepONets. 
- There should be an ablation of different filters (at least some filters with sharper cut-offs than Gaussian, Butterworth for example).
- The linearized flow map is unclear, is the linearization at the current time step?
- There are some minor notational errors, such as the PDE for the Kolmogorov flow is wrong, and the divergence-free condition in RBC is written as something else.
- I would argue differently from Figure 8 on the usage of only filtering the last layer vs every layer. RBC is a different beast than others, as one of the major difficulties for neural surrogates is the boundary conditions (not so big for periodic boxes) after repeated application. 
- The training done in fp64 for 1D problem and fp32 for 2D problem.
- The authors wrote "the choice of $\sigma$ is important", but never reported the comparison.

### Questions
- Why not making $\sigma$ learnable in the filter?
- What is a "high-frequency regularizer"?

### Soundness
2

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
2

### Summary
The paper proposes a filtering-based approach to achieve long rollouts of neural PDE solvers. Neural surrogates for PDE solvers face issues in simulating problems for large temporal domains, and autoregressive-based methods, which this paper focuses on, have an additional problem with the accumulation of errors over time steps. The proposed method applies a low-pass filter after each pointwise nonlinearity in the network to mitigate the so-called spectral junk in long rollouts. The method is presented on popular PDE problems shown as challenging in the literature.

### Strengths
The proposed method is simple, easy to implement and is shown to be effective.

The proposed filtering step can be combined with different methods and can help, in general, the long rollout of PDE solvers.

The choice of PDEs is relevant to the problem being solved.

### Weaknesses
First, a general comment is that the paper is hard to read and assumes the reader is well-read with the literature. Further explanation of concepts, such as defining how the PDE solutions' low, medium, and high-frequency bands are identified and explaining the eigenvalue spectrum of the linearized flow map, would help the reader understand the challenges and motivate them to read the work.

The chosen baselines are vanilla, and more advanced variants of the architectures could have been considered as the baseline, for e.g. advanced variants of U-Net have been applied for temporal conditioning and long rollouts.

The challenge of the long rollout is even persistent for 3D stiff problems; how well the method scales to a higher-dimensional problem still needs to be checked.

The proposed method relies on filtering strategies, however, a detailed discussion of different filters, their pros, cons, and rationale for choosing the specific filtering approach is missing.

### Questions
One of the popular methods for long rollouts is PDE-Refiner. The authors discuss it briefly but do not compare it against the method. A comparison with PDE-Refiner and the pros and cons of both methods will help the reader understand how the method fairs against the methods established in the literature.

A detailed study regarding the performance of filtering steps needs to be carried out, such as: How sensitive is the performance to the choice of filtering parameters? Would an adaptive filtering mechanism be feasible? A study with different filters and their performance in the proposed setting would also aid in understanding the robustness of the proposed approach.

Did the authors experiment with placing the filter at different stages in the network (e.g., after every few layers instead of each nonlinearity), and how did that affect performance?

Since the authors argue that MSE loss biases the model towards low frequencies, How would the proposed method behave with alternative loss functions that could complement spectral shaping? 

As a general remark, how does the proposed method guarantee that the errors are smoothed rather than smoothing out important features of the solution? For instance, how will the method perform for problems involving bifurcations?

How does the method perform regarding computational cost compared to the baselines?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper aims to improve the ability of neural PDE solvers to model high-frequency information accurately, which it claims is the reason for the long-term rollout instability of autoregressive models. The inability to model high-frequency behavior is attributed to the spectral bias of the MSE loss, distribution shift, and noise produced by non-linearities in the model. The authors conducted a study on the frequency behavior of the model, including an analysis of the eigen-spectrum. They propose to overcome the noise produced by the model by applying a fixed, preset noise filter after each non-linearity in the model. The experiments show that this helps the model to generate more accurate roll-outs which diverge from the true solution at a later point in time.

### Strengths
1. Novel analysis of the eigen-spectrum; including the insight that the unstable eigenvalues correspond to the high-frequency, noisy vectors
2. The proposed method improves the decorrelation times over the vanilla U-Net and can fix the high-frequency noise problem.
3. Easy-to-implement method

### Weaknesses
1. The presented study combines multiple known aspects of the rollout problem but has limited novelty on its own. Besides the eigen-spectrum analysis, most of the insights from the presented study have already been presented in other works. The inability to model high-frequency noise is a known problem and has been described in previous publications. (Lippe 2024, McCabe 2023). In McCabe et al. (2023), the noise problem was explicitly attributed to the non-linearity, and they proposed to learn to filter this noise out (although for FNO). In Raonić et al. (2024), formal solutions are introduced to avoid aliasing produced by non-linearities in convolutional models.
2. The proposed method is not compared against any other architectural methods that tackle the noise problem, e.g., PDERefiner, in the experiments. While the presented method is computationally cheaper, the question remains whether it can increase the decorrelation time as much as the other methods tackling the high-frequency noise problem. 
3. The method is only evaluated for a single model (U-Net). This leads to the question of whether the good experimental results are due to using a model that may be especially prone to producing high-frequency noise. For example, the paper could be improved by evaluating whether the filter helps FNO. This would also allow a comparison to the method of McCabe et al. (2023).
4. The right filter curve is found by hand and not learned.  

Lippe et al. "Pde-refiner: Achieving accurate long rollouts with neural pde solvers." Advances in Neural Information Processing Systems 36 (2024).  
McCabe et al. "Towards Stability of Autoregressive Neural Operators." Transactions on machine learning research (2023).  
Raonic et al. "Convolutional neural operators for robust and accurate learning of PDEs." Advances in Neural Information Processing Systems 36 (2024).

### Questions
1. Why did you choose to train the model in float64 precision?
2. What do the circles in the box-plot in Fig. 8 represent?

### Soundness
2

### Presentation
3

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
This paper addresses problems with using neural PDE solvers, specifically the spectrum of the solution in the mid-high frequency band.  The authors present the key findings of the paper as the discovery that  higher frequencies are introduced by point-wise nonlinearities and address this issue experimentally with the application of a Gaussian low pass filter after every non-linearity.

### Strengths
Overall, the paper does a good job of presenting the issue within the context of neural PDE solvers and the literature around using machine learning to solve PDEs is reasonably well surveyed. 

I am pleased to see the area of spectral shaping applied to neural PDE solvers being explored, and I think that the results in the paper show that it is a promising area.

If a thorough evaluation of the literature on both sides of the work (i.e. both spectral shaping and neural PDE solvers) is included then this will enrich the insights in the paper and has the potential to be a worthy addition to the literature in this area.

### Weaknesses
**Main Comments**

In contrast with the literature on neural PDE solvers, the background literature around the effect of nonlinearities on the spectrum and filtering has not been sufficiently explored. This is a major drawback of the paper and something that should be improved in order to accept it for publication and a number of related papers are referenced at the end of this review. In order to make this work worthy of publication, a much more thorough evaluation of the literature around spectral shaping should be carried out and therefore, in its current form, I would lean towards rejecting the paper unless the following points can be addressed. 

This is especially true because a survey of some of the literature around this area will not only provide a more complete background to the work, but also give a theoretical underpinning to some of the phenomena that are described. 
For example from the “integration by parts coefficient bound” described by [1], if the function is smooth up to and including its $(k-2)^\text{th}$ derivative, and its $k^\text{th}$ derivative is integrable, then the Fourier coefficients decrease as $O(\xi^{-k})$. This provides a possible reason for the increase in spectrum at mid and high frequencies due to discontinuities. In particular, I am skeptical that the post-nonlinearity increase observed at higher frequencies is indeed "noise" as the authors describe, instead they may be due to the change in spectral shape due to discontinuities. In addition, the excellent survey by [5] also links these effects back to the original observation by Gibbs [2,3] regarding the interaction between discontinuities in the time (frequency) domain and the shape in the frequency (time) domain.  In order to provide evidence for this the authors could experimentally examine the relationship between the order of the discontinuity and the shape of the spectrum.

The work by [1] also provides a motivation for the requirement for the filters to be applied after each stage, rather than once at the end; as the signal energy at the higher frequencies increases due to discontinuities, the effect of truncating the higher frequencies will be greater. This effect can be assessed by calculating the error that will be introduced by the discontinuities and comparing that to experimental observations. The work in [1,4] shows some example calculations of errors. 

In addition to this background literature on the effect of discontinuities, some of the more significant literature on the subject of filtering should be included, e.g. [4,6,7]. This can provide some theoretical justification to the ultimate selection of the Gaussian filter, such as filter orders and experimental results from testing. 

[1] J. P. Boyd. Chebyshev and Fourier Spectral Methods. Springer, Heidelberg, 2001.

[2] J. W. Gibbs. Fourier’s series. Nature, 59:200, 1898.

[3] J. W. Gibbs. Fourier’s series. Nature, 59:606, 1899.

[4] D. Gottlieb and C.-W. Shu. On the Gibbs phenomenon and its resolution. SIAM Review, 39(4):644–668, 1997.

[5] E. Hewitt and R. E. Hewitt. The Gibbs-Wilbraham phenomenon: an episode in Fourier analysis. Archive for History of Exact Sciences, 21(2):129–160,1979.

[6] E. Tadmor. Filters, mollifiers and the computation of the Gibbs phenomenon. Acta Numerica, 16:305–378, 2007.

[7] H. Vandeven. Family of spectral filters for discontinuous problems. Journal of Scientific Computing, 6(2):159–192, 1991.

**Minor Comments**

In general, the paper is well formatted and written. However, I have a few minor comments:

In acronyms are used before they are defined, e.g. the use of KS in the caption of Figure 3 before the use of Kuramoto-Shivashinsky in the text. 

In some cases the language could be slightly more formal in an academic paper. For example the use of ``sanity check"  and "probably" in Section 5.1. 

Also in Section 5.1, I would like a more formal justification for the statement "The remain [sic] divergence for the spectral-shaped model could probably be remedied with a larger model or more training data." I think it likely that the addition theoretical work suggested in Section 2 of this review will also inform this improvement.

### Questions
I would be pleased to hear the authors' feedback on my suggestions above. I think this could be a useful area of work once more work has been done on the theory around discontinuities and spectral shaping.

### Soundness
2

### Presentation
3

### Contribution
2

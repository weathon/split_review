- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 8, 6, 6
Now I have a thorough understanding of the paper and can verify all claims against the actual text. Let me write the final consolidated review.

---

## Summary

This paper identifies a previously undocumented instability in the variance propagation of deep networks using shifted ReLU and soft-thresholding activations, when initialized on the Edge of Chaos. The root cause is that for these sparsifying functions, $V'(q^*)=\chi_{1,\phi}=1$ on the EoC while $V''(q^*)>0$, making the fixed point unstable from the right and leading to exploding variance and gradients. The paper proposes magnitude-clipped variants (cReLU and cst) which decouple the EoC condition from $V'(q^*)$, yielding $V'(q^*)<1$ at the EoC. Experiments on 100-layer DNNs (MNIST) and 50-layer CNNs (CIFAR-10) verify that the clipped activations train reliably with up to 85% activation sparsity, while their unclipped counterparts fail even at moderate sparsity levels.

## Strengths

1. **Identifies a concrete, previously unreported instability in natural sparsifying activations** — The paper proves (Section 2, Table 1, Figure 2) that shifted ReLU and soft thresholding on the EoC satisfy $V'_{\phi}(q^*)=\chi_{1,\phi}=1$ with $V''_{\phi}(q^*)>0$, causing the variance fixed point to be only stable from the left. This is a novel theoretical finding grounded in the Gaussian process analysis of infinite-width networks and explains cleanly why these seemingly natural activations fail to train.

2. **Proposes a simple clipping fix with rigorous theoretical justification** — The clipped variants cReLU and cst (Eqs. 6-7) are shown analytically (Eqs. 13-14) to satisfy $\chi_{1,\phi} > V'_{\phi}(q^*)$, so at the EoC ($\chi_{1,\phi}=1$) we have $V'_{\phi}(q^*)<1$, making $q^*$ locally stable. The gap is proportional to the clipping magnitude $m$, directly decoupling the stability condition from the sparsity requirement.

3. **Verifies the theory through controlled experiments with clear failure characterization** — DNN experiments on MNIST (5 runs, mean/std reported) show that cReLU and cst achieve ~94% test accuracy at 80-85% sparsity, matching the ReLU baseline. The paper carefully documents two distinct failure modes (exploding gradients from large $V''$, and reduced expressivity from small $m$) and shows gradient-norm diagnostics (Figures 5-6) that directly connect the theoretical predictions to observed training dynamics.

4. **Covers both DNN and CNN architectures** — The analysis is carried out for both feedforward (Eq. 1) and convolutional (Eq. 2) architectures, and experiments verify the theory on both MNIST (DNNs) and CIFAR-10 (CNNs), demonstrating generality.

## Weaknesses

### Fatal
None.

### Major
None. The core theoretical contribution is sound, the experimental evidence supports the claims, and no verified flaw undermines the paper's main results.

### Minor

1. **CNN architecture is underspecified in the main text** — Section 4 describes CNNs as having "300 channels in each layer and depth 50" with no mention of kernel sizes, stride, padding, pooling operations, batch normalization, or dropout. While the theoretical framework (Eq. 2) focuses on 1D convolutions with kernel width $2k+1$, the experiments are on 2D CIFAR-10 images, and the main text provides no detail on how the 2D case is handled. This makes the CNN experiments non-reproducible from the information given. Additional architectural details (even a brief note in the main text or a reference to the appendix) would significantly strengthen the paper.

2. **CNN experiments are single-run with no error bars** — The paper states "For the 50-layer CNN experiments on CIFAR10 a single experiment was conducted for each hyperparameter combination." Since the theoretical instability is inherently stochastic (finite-width fluctuations push $q^l$ past the fixed point), multiple runs are important to assess the reliability of the CNN results. For example, the cst CNN results at $s=0.8, V'=0.9$ drop to 0.31 accuracy — is this systematic or a single unlucky draw? The DNN experiments rightly use 5 runs; the CNN experiments should follow the same standard.

3. **ReLU baseline accuracy is present but implicit** — Table 1 includes a row for $\relutau$ with $s=0.50, \tau=0.00$, which (as the paper states: "When $\tau=0$, $\relutau$ is just the standard ReLU function") serves as the ReLU baseline. However, this row is not clearly labeled as "ReLU baseline" in the table, and a reader could miss it. Given that the paper repeatedly claims "full accuracy of a standard ReLU network baseline is retained," it would be helpful to highlight the baseline row explicitly and quantify any differences in the text or table caption. The data is there, but the presentation is suboptimal.

### Trivial

1. Minor notation inconsistency: Eq. (15) on line 155 says $V'_{\cst}(q) = 2 V'_{\cst}(q)$, which appears to be a typo (should be $V'_{\cst}(q) = 2 V'_{\crelu}(q)$ based on the surrounding context). This should be corrected to avoid confusion.

## Nice-to-Haves

- **Computational efficiency context**: The paper is motivated by efficiency but provides no FLOP reduction estimates, runtime measurements, or memory savings data. Even a brief back-of-the-envelope calculation of how sparsity translates to potential speedups (referencing established results from FATReLU or sparse computation literature) would help the reader assess the practical significance of the 85% sparsity achieved.
- **Practical recipe for choosing $m$**: The paper provides $V'(m)$ and $V''(m)$ plots (Figure 3) and experiments sweep over three $V'(q^*)$ values, but a simple heuristic for choosing $m$ given a target sparsity $s$ (e.g., "set $m$ to achieve $V'(q^*)\approx0.7$") would increase immediate usability for practitioners.
- **Error bars or additional trajectories for the gradient norm plots** (Figures 4, 5-6): Showing one failed run is illustrative, but average and spread over multiple failed runs would strengthen the characterization.

## Removed Points

These points were flagged by reviewers but are removed from the main assessment for the reasons stated:

- **"Missing ReLU baseline accuracy"** — REMOVED (factually incorrect). The ReLU baseline IS in Table 1: the $\relutau$ row with $s=0.50$, $\tau=0.00$ reports DNN test accuracy 0.94 and CNN accuracy 0.70. The paper explicitly states "When $\tau=0$, $\relutau$ is just the standard ReLU function" (line 111). The baseline data is present; the critic appears to have missed these rows. The presentation could be clearer (see Minor weakness #3 above), but the data is not missing.
- **"Not comparing to L1/Hoyer regularization"** — REMOVED (scope creep). The paper focuses on activation design at initialization, not post-hoc sparsification via regularization. The related work section appropriately cites this literature.
- **"Missing derivation for CNN variance map"** — REMOVED (standard practice). The paper correctly cites Xiao 2018 for the CNN Gaussian process derivation. It is standard to reference prior work for such known results.
- **"Second failure mode analysis should be expanded"** — REMOVED (instruction: parser strips appendix; the paper references App.~\ref{sec: loss function} for further discussion, and the paper also flags this as future work in the conclusions).
- **"CNN accuracy numbers are modest"** — REMOVED (addressed by the paper: "The absolute accuracy of the networks is not the focus of these experiments, rather it is the ability to retain trainability and approximately the accuracy of standard ReLU networks").
- **"Missing computational efficiency measurements"** — DEMOTED to Nice-to-Have. The paper's core contribution is initialization theory and trainability, not systems benchmarking. The sparsity fraction is the claimed efficiency mechanism; measuring runtime speedups is outside the paper's stated scope.

## Novel Insights

None beyond the paper's own contributions. The reviews surface no perspective that the paper itself does not already articulate.

## Suggestions

1. **Add a clear "ReLU baseline" row** to Table 1 with explicit labeling, and state the accuracy difference (if any) in the caption. This takes one line and directly supports the "full accuracy retained" claim.
2. **Provide the full CNN architecture** (kernel sizes, stride, pooling, any normalization) either in Section 4 or the appendix, and specify how the 1D theoretical framework (Eq. 2) is extended to 2D CIFAR-10 images.
3. **Run at least 3-5 repeats for the CNN experiments** on a representative subset of configurations (e.g., one or two sparsity/m values per activation) to establish that the single-run results are reliable. This is important because the instability being studied is stochastic in nature.
4. **Fix the typo in Eq. (15)**: $V'_{\cst}(q) = 2 V'_{\cst}(q)$ should read $V'_{\cst}(q) = 2 V'_{\crelu}(q)$.
5. **Add a practical guideline section** (even one paragraph) suggesting how practitioners can select $m$ given a target sparsity, distilling the $V'(m)$ and $V''(m)$ analysis into a simple heuristic.

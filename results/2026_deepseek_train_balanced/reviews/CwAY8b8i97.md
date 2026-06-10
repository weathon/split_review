Now I'll produce the final consolidated review.

---

## Summary

This paper proposes Spike Accumulation Forwarding (SAF), a training paradigm for spiking neural networks that propagates only spike accumulations during the forward pass, as opposed to OTTT which requires propagating both spike trains and spike accumulations. The paper proves Theorem 1 (exact gradient equivalence between SAF-E and OTTT$_ {\rm O}$) and Theorem 2 (equivalence between SAF-F and Spike Representation up to a scale factor), and demonstrates empirically that SAF reduces memory by ~28--30% and training time by ~30--63% while maintaining accuracy on CIFAR-10 and CIFAR-100.

## Strengths

1. **Theorem 1 (SAF-E $\equiv$ OTTT$_{\rm O}$) is proven via a clean chain of gradient identities.** The derivation (Eqs. 160, 164--165) maps SAF's accumulation-based derivatives onto OTTT's spike-based derivatives. The key relation $\bm{s}^{l+1}[t] = \widehat{\bm{a}}^{l+1}[t] - \lambda\widehat{\bm{a}}^{l+1}[t-1]$ makes Eq. (160) sound — contrary to what one reviewer claimed, the derivative $\partial \bm{s}^{N}[t] / \partial \widehat{\bm{a}}^{N}[t]$ is the identity because $\bm{s}$ is a linear function of $\widehat{\bm{a}}$ at the same layer, not a Heaviside function of it. This is a stronger formal result than the positive-inner-product relation previously established between OTTT$_{\rm A}$ and Spike Representation.

2. **Theorem 2 (SAF-F $\equiv$ Spike Representation up to a known scale factor $V_{\rm th}$).** The paper shows SAF-F's gradient is exactly $V_{\rm th}$ times the Spike Representation gradient (lines 194--197), closing the theoretical gap left by prior work where only approximate gradient-direction similarity was known.

3. **Quantified memory and time reductions with accuracy maintained.** Table 1 shows SAF-E uses 1.184 GB vs. OTTT$_ {\rm O}$'s 1.656 GB (~28% reduction) and 0.468 sec vs. 0.666 sec per minibatch (~30% faster) on CIFAR-10, while achieving 93.54% vs. 93.44% accuracy. Table 2 shows SAF-F uses 1.157 GB vs. OTTT$_ {\rm A}$'s 1.656 GB (~30% reduction) and 0.247 sec vs. 0.661 sec at T=6 (~63% faster). Accuracy differences are within a few tenths of a percent.

4. **Explicit mutual convertibility between SAF forward pass and standard LIF neurons.** Equations (119)--(125) provide closed-form expressions reconstructing $\bm{u}^{l+1}[t]$ and $\bm{s}^{l+1}[t]$ from SAF's accumulation variables, meaning SAF-trained weights can be deployed on standard LIF-based neuromorphic hardware without approximation error. Tables 1 and 2 confirm near-zero accuracy changes (e.g., 0.016 points on CIFAR-10) when converting to LIF inference.

## Weaknesses

### Fatal
None.

### Major

1. **Experimental details are critically underspecified, preventing reproducibility.** The paper states (line 275): "We used the same experimental setup as \citep{Xiao2022OnlineNetworks}, including the choice of SG." It does not specify the network architecture (which VGG variant? number of layers? channels?), the optimizer, learning rate, batch size, number of epochs, weight initialization, or data augmentation. The reader cannot reproduce the results from the information provided. While the paper does not claim to achieve SOTA, reproducibility is a minimum expectation for a methods paper at a top venue.

### Minor

2. **Experimental scope is limited relative to the paper's theoretical breadth.** Experiments are confined to CIFAR-10 and CIFAR-100 with at most T=32 time steps and one unspecified architecture. The theoretical analysis of feedforward and feedback connections (Contribution D, Section 4.3) is never experimentally validated — no experiments involve non-sequential connections. The paper acknowledges this scope limitation, which is honest, but it means several of the paper's theoretical claims remain empirically untested.

3. **The "halving the number of operations" claim is stated but never quantified.** The abstract and introduction assert that SAF halves forward-pass operations, but no FLOPs counts, operation breakdown, or runtime profiling at the operation level is provided. Only aggregate training-time measurements are given (Tables 1, 2), which conflate multiple factors (memory bandwidth, kernel launches, etc.).

4. **The assumption underlying Theorem 1 needs clarification.** The paper says "Assuming that $L_E[t]$ depends only on $\widehat{\bm{a}}^l[t]$ and $\widehat{\bm{U}}^l[t]$, i.e., not on anything up to $t-1$" (line 134). However, $\bm{s}^N[t]$ depends on $\widehat{\bm{a}}^N[t-1]$ through Eq. (122): $\bm{s}^{l+1}[t] = H(\widehat{\bm{U}}^{l+1}[t] - V_{\rm th}(\lambda\widehat{\bm{a}}^{l+1}[t-1] + 1))$. While the gradient derivation remains correct under the standard online-training convention (treating past states as constants, exactly as OTTT does), the paper should explicitly discuss this, since the stated assumption is technically violated by the paper's own equations.

5. **No statistical significance testing.** The accuracy differences between SAF-E and OTTT$_ {\rm O}$ (e.g., 93.54% vs. 93.44% on CIFAR-10) are presented as supporting the theoretical equivalence, but no significance test is performed. The standard deviations partially overlap, but the mean differences — especially on CIFAR-100 (71.56% vs. 70.70%) — are non-trivial. For a paper whose central claim is that two methods are equivalent, a more rigorous comparison (e.g., paired tests, correlation measures) would strengthen the evidence.

### Trivial

6. **The claim that "SAF does not need to retain the past potential accumulation $\widehat{\bm{U}}^{l+1}[t-1]$" (line 127) is slightly imprecise.** Equation (107) shows $\widehat{\bm{U}}^{l+1}[t] = \lambda\widehat{\bm{U}}^{l+1}[t-1] + \bm{W}^l(\widehat{\bm{a}}^l[t]-\lambda\widehat{\bm{a}}^l[t-1]) + \bm{b}^{l+1}$, which is a recurrence that requires $\widehat{\bm{U}}^{l+1}[t-1]$ as input. The actual memory savings come from not needing to retain membrane potentials in the computational graph for backward passes, but this distinction is not made. The empirical memory savings (~28--30%) are real, so this is a presentation issue rather than a substantive error.

## Nice-to-Haves

- A FLOPs breakdown substantiating the "halving operations" claim.
- Controlled experiments on feedforward/feedback connections to validate Section 4.3.
- A comparison against Spike Representation methods directly, even if qualitative.
- Larger-scale experiments (e.g., ImageNet, CIFAR-100 with deeper networks) to demonstrate scalability.
- Confidence intervals or significance tests for the accuracy comparisons.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **The harsh critic's claim that Theorem 1 has a fatal proof gap (Eq. 160 is invalid due to the Heaviside).** This is factually incorrect. From Eq. 112 and Eq. 122: $\bm{s}^{l+1}[t] = \widehat{\bm{a}}^{l+1}[t] - \lambda\widehat{\bm{a}}^{l+1}[t-1]$, so $\partial \bm{s}^{l+1}[t] / \partial \widehat{\bm{a}}^{l+1}[t] = \mathbf{1}$ (treating $\widehat{\bm{a}}^{l+1}[t-1]$ as a constant, which is the standard online-training convention also used by OTTT). The Heaviside is not in the derivative path from $\widehat{\bm{a}}^{N}[t]$ to $\bm{s}^{N}[t]$ at the same layer. The critic's chain rule argument through the Heaviside is therefore misplaced.
- **The strength finder's generic statement that "this paper addresses a genuine problem."** This is superficial — removed as it lacks specific evidence.
- **The harsh critic's claim that OTTT's dual-propagation is "largely an implementation choice."** This is speculative and outside the paper's stated scope; the paper correctly identifies the computational overhead OTTT incurs when implemented efficiently on GPUs.

## Novel Insights

None beyond the paper's own contributions. The key insight — that propagating only spike accumulation during the forward pass is theoretically equivalent to propagating both spike trains and accumulations — is the paper's own core contribution and is well-articulated.

## Suggestions

1. **Fully specify the experimental setup:** Provide the exact network architecture (layers, channels, VGG variant), optimizer, learning rate schedule, number of epochs, batch size, weight initialization, and data augmentation. This is essential for reproducibility.

2. **Quantify the "halving operations" claim** with a FLOPs count or operation-level profiling to substantiate the claimed computational advantage.

3. **Add experiments on feedforward/feedback connections** to support the theoretical analysis in Section 4.3, or clearly scope Contribution D as purely theoretical.

4. **Clarify the assumption in Theorem 1:** Discuss why treating $\widehat{\bm{a}}^{l+1}[t-1]$ as a constant is consistent with the online-training paradigm (same assumption OTTT makes), and acknowledge that $\bm{s}^{l+1}[t]$ formally depends on $\widehat{\bm{a}}^{l+1}[t-1]$ even though the gradient is computed only through time-$t$ variables.

5. **Include at least one larger-scale benchmark** (e.g., CIFAR-100 with a deeper network, or ImageNet with a few epochs) to demonstrate that the method scales beyond small architectures.

## Score and Decision

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>
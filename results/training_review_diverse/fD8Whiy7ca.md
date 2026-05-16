Here is my consolidated final review after carefully verifying every claim against the paper.

---

## Summary

This paper introduces Restricted Adaptive Feedback (RAF), a learning rule that factorizes the feedback matrix in Feedback Alignment into two low-rank components \( B = QP \) and trains both factors using local update rules (a Kolen-Pollack-style rule for \( Q \), Oja's rule for \( P \)). The central claim is that neural networks—including convolutional networks that have been resistant to prior FA methods—can be trained to backpropagation (BP)-level accuracy using error signals whose dimensionality equals the task output dimensionality (e.g., the number of classes). The paper provides a theoretical analysis for linear networks and experimental results on CIFAR-10/100 with fully connected and convolutional architectures.

## Strengths

- **Rigorous theoretical analysis for the linear case.** The paper derives continuous-time dynamics (Eqs. 5, 9) and stationary-point conditions (Eq. 6) for a single-hidden-layer linear network, proving that training *both* \( Q \) and \( P \) is necessary when the feedback rank \( r \) is smaller than the output dimension \( m \). Fig. 2 cleanly demonstrates that training only \( Q \) (keeping \( P \) fixed) fails to recover the correct singular modes, while RAF succeeds. This directly motivates the algorithm.

- **Convincing demonstration that rank = number of classes suffices for matching BP.** On CIFAR-10 and CIFAR-100, constraining all feedback matrices to rank equal to the number of classes yields test accuracy indistinguishable from full BP (Figs. 3a, 3c). The scaling experiment across 50, 75, and 100 classes (Fig. 3c) directly supports the claim that required error dimensionality is tied to task complexity, not network size.

- **First successful low-dimensional feedback training of CNNs.** Prior FA methods struggle with convolutional architectures, but RAF with rank equal to class count achieves BP-level accuracy on a VGG-like network (Fig. 4a). Performance remains robust when all convolutional blocks are constrained to fractions of their width (Fig. 4b), directly addressing a long-standing limitation of FA.

- **Evidence that RAF leverages high-dimensional representations despite low-dimensional feedback.** The comparison in Fig. 3b shows that narrowing the network hurts performance more than constraining feedback, confirming that the network retains and uses its representational capacity.

## Weaknesses

### Fatal
None.

### Major

- **Missing experimental comparisons to existing learned-FA methods.** The paper cites Akrout et al. (2019) (adaptive FA via Kolen-Pollack rule), Crafton et al. (2019) (fixed sparse feedback), and Nøkland (2016) (Direct FA) in the related work section but does not experimentally compare RAF to any of them under identical conditions. Since RAF's \( Q \) update is closely related to the Akrout et al. rule, the paper's primary novelty claim rests on the addition of the \( P \) factor and its Oja-rule training. A direct comparison showing that RAF outperforms or matches these methods—especially Akrout et al. under matched rank constraints—is needed to substantiate the claim that RAF is a significant advance over prior FA variants. Without this, the contribution is not well isolated.

- **Gap between the linear theory and the nonlinear deep-network experiments.** The theoretical analysis (Section 3) covers a *single-hidden-layer linear* network and updates \( P \) using the *true labels* \( y^\mu \) (Oja's rule on outputs). In deep nonlinear networks, \( P \) is instead updated using error signals \( \delta_{l+1} \) from the next layer (Eq. 10), and the dynamics are not analyzed. The paper acknowledges this briefly ("In deeper models, hidden layers do not have ground-truth representations") but provides no argument—theoretical or empirical—that the same convergence properties hold under nonlinear activations and when \( P \) is driven by error signals rather than ground-truth outputs. The step from Eq. (9) to Eq. (10) is based on analogy, not derivation. This leaves a significant gap between the formal theory and the experimental claims.

- **The receptive-field experiment (Section 5) is qualitative and lacks rigor.** The experiment is described in a single paragraph. Receptive fields are shown for a few examples (Fig. 4d) with no quantitative metrics (e.g., center-surround index, orientation selectivity index). There is no controlled comparison to the feedforward bottleneck baseline from Lindsey et al. (2019) under the same training protocol, and no evidence that the center-surround fields are robust across runs, initializations, or hyperparameters. The section is titled "Error Dimensionality Shapes Neural Receptive Fields," but the evidence is too thin to support this conclusion.

### Minor

- **No variance or confidence intervals reported for any experiment.** Figs. 3 and 4 show single curves without error bars, and the paper does not state how many runs were performed. This makes it impossible to assess the statistical reliability of the reported results.

- **dRAF is introduced but not compared to Direct Feedback Alignment (Nøkland, 2016).** The paper notes the similarity ("analogous to Direct Feedback Alignment") and shows that dRAF matches BP (Fig. 3d), but without a comparison to actual DFA under the same architecture, it is unclear whether the direct projection scheme provides any benefit beyond the existing DFA method.

- **Experimental scope is limited relative to the paper's framing.** The title and abstract claim "Training Large Neural Networks," but the experiments use a 4-layer fully connected network with 512 units and a VGG-like CNN with four blocks, both on CIFAR-10/100. These are not "large" by current standards. While CIFAR is a reasonable testbed, the absence of larger-scale experiments (e.g., Tiny ImageNet, deeper ResNets) tempers the generalizability of the findings.

### Trivial
- In Fig. 2 caption: "simlar" → "similar."
- The BP baseline in Figs. 4a–b is shown as a dashed line but not described in the body text.

## Nice-to-Haves
- An ablation comparing RAF with only \( Q \) trained (no \( P \) update) vs. both \( Q \) and \( P \) trained for the *nonlinear* case (the linear case already has this in Fig. 2). This would directly demonstrate the necessity of the \( P \) factor in the setting that matters most.
- Additional analysis showing that the feedback weights \( P_l \) converge to the principal components of the error signals \( \delta_{l+1} \) across layers in nonlinear networks, strengthening the link to the linear theory.
- Quantitative receptive-field metrics (center-surround index, orientation selectivity) across multiple runs and rank settings.

## Removed Points

These points were flagged by the reviewer but are removed per the review guidelines (with brief justification):

1. **"The abstract's phrasing 'perform linearly parameterized as backpropagation' (likely a parsing artifact)"** — This phrase does not appear in the paper. The criticism is based on a parser artifact, not an author error. → *Removed (formatting/parser artifact).*

2. **"The third equation in (9) contains a typographical inconsistency"** — The equations in (9) are consistent as written. The notation is standard for a dynamical system with time constant \( \tau \). → *Removed (factually incorrect / overly pedantic).*

3. **"The paper does not report hyperparameters (learning rate, batch size, epochs, optimizer, etc.)"** — Per guidelines, nitpicks about undisclosed hyperparameters that are standard and addressable in a camera-ready version are removed. (Note: the broader concern about missing *all* training details has some merit; it was incorporated in weakened form under Minor as a scope concern rather than as a reproducibility accusation.) → *Removed (reproducibility nitpick per guidelines). [The hyperparameter specifics are indeed absent, but the core algorithmic contribution does not hinge on them; this is fixable in revision.]*

4. **"Fig. 3b comparing RAF with low rank to narrower networks is expected and not a new insight"** — This experiment serves to show that the network still uses high-dimensional representations despite low-dimensional feedback, which is a meaningful demonstration of the paper's thesis, not a trivial observation. → *Removed (mischaracterization of the experiment's purpose).*

5. **Criticisms about the paper not being reproducible because models/tools are unreleased** — No such criticism was present; included here for completeness. → *Not applicable.*

## Novel Insights

None beyond the paper's own contributions. The reviews identify gaps (missing baselines, theory-experiment disconnect, qualitative receptive-field analysis) rather than offering novel reinterpretations of the work.

## Suggestions

1. **Add controlled comparisons to Akrout et al. (2019) (learned FA) and Nøkland (2016) (Direct FA) under identical architectures and rank constraints.** This is the single most important addition. If RAF matches or outperforms these methods, the novelty of the \( P \)-factor training is substantiated. If not, the paper should clearly characterize where RAF provides a specific benefit.

2. **Bridge the theory-experiment gap.** Either extend the theoretical analysis to show that Oja's rule on error signals \( \delta_{l+1} \) (rather than outputs \( y \)) converges to the principal components of the error, or provide controlled experiments showing this convergence across layers in nonlinear networks.

3. **Quantify the receptive-field experiments.** Compute center-surround indices and/or orientation selectivity indices across multiple runs and rank settings, and compare directly to the Lindsey et al. (2019) feedforward bottleneck under the same protocol. Report whether the effect is statistically significant.

4. **Report error bars or confidence intervals** for all main experimental results (Figs. 3a–d, 4a–b) by running multiple trials with different seeds.

5. **Include an ablation for the nonlinear case** comparing RAF (both \( Q \) and \( P \) trained) vs. only \( Q \) trained (with \( P \) fixed), to empirically demonstrate the necessity of the \( P \) factor in deep nonlinear networks.

6. **Consider a larger-scale benchmark** (e.g., Tiny ImageNet or a subset of ImageNet with a ResNet-18) to substantiate the title's claim about "Large Neural Networks."

## Score and Decision

The paper introduces an interesting idea supported by a clean theoretical analysis for linear networks and promising initial experiments. The RAF algorithm itself is well-motivated and the demonstration that rank = number of classes suffices for matching BP on CIFAR is compelling. However, the experimental validation is incomplete in several critical ways: missing comparisons to existing learned-FA baselines (Akrout et al., Nøkland), a gap between the linear theory and the nonlinear experiments that is not addressed, and a qualitative receptive-field analysis that does not support the strength of the claims made. These are substantive weaknesses that prevent the paper from being accepted in its current form. Major revisions—particularly the addition of proper baselines—are needed.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>
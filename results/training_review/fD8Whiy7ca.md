Now I have thoroughly verified all claims against the paper. Here is my consolidated final review.

---

## Summary

This paper introduces Restricted Adaptive Feedback (RAF), a variant of Feedback Alignment that factorizes the feedback matrix into two low-rank components \(B = QP\) and trains both via local learning rules (Oja's rule / Hebbian plasticity). The central claim is that low-dimensional error signals—whose dimensionality is no larger than the task's output dimension—can match full backpropagation performance in deep nonlinear and convolutional networks. A rigorous theoretical analysis is given for linear networks, followed by experiments on CIFAR-10/100 with fully-connected and VGG-like architectures, plus a qualitative biological connection to center-surround receptive fields.

## Strengths

- **Novel conceptual contribution.** Factorizing the FA feedback matrix into \(Q\) (column space) and \(P\) (row space) and training *both* components is a genuine advance. Prior adaptive FA methods (Kolen & Pollack, Akrout et al.) only train the column space; this paper correctly identifies that training \(P\) is necessary when the feedback is low-rank, and provides a clean theoretical reason (the stationary-point condition in Eq. 6 becomes under-determined without it). This is the paper's strongest contribution.

- **Rigorous linear-theory derivation.** Sections 3.1–3.2 derive continuous-time dynamics (Eq. 5) and fixed-point conditions (Eq. 6) for low-rank FA, showing analytically that a fixed random low-rank feedback matrix leads to under-determined solutions while training both \(Q\) and \(P\) via Oja's rule recovers the correct solution. The analysis using the SVD of the input-output covariance and the alignment of singular vectors is mathematically sound and well-presented.

- **Systematic ablation of feedback rank.** The experimental design isolates the effect of error dimensionality by constraining one layer at a time (Fig. 3a) versus all layers simultaneously (Fig. 3b), and by varying the number of classes in CIFAR-100 (Fig. 3c). This controlled approach cleanly tests the hypothesis that minimal required rank equals task dimensionality.

- **Introduction of dRAF.** The direct-feedback variant (bypassing intermediate layers) is a useful extension that increases biological plausibility and flexibility. The paper correctly notes its connection to Direct Feedback Alignment (Nøkland, 2016).

- **Use of biologically plausible learning rules.** The update equations for \(Q\) and \(P\) rely on well-studied local plasticity rules (Oja's rule, Hebbian learning), grounding the framework in neuroscience literature.

## Weaknesses

### Fatal
None.

### Major

1. **No quantitative accuracy numbers reported.** The results are described only verbally ("matches BP performance") or in figures without tables. The reader cannot judge whether "matching" means within 0.5% or 5%. This is a fundamental reporting failure for an empirical paper whose central claim is that RAF *matches* BP performance.

2. **No error bars, standard deviations, or multi-run statistics.** Without these, observed differences between RAF and BP could arise from random initialization or training noise. For any claim of "matching" a baseline, basic statistical reporting is essential.

3. **Training hyperparameters are completely omitted for nonlinear experiments.** The paper specifies neither learning rate, batch size, optimizer, number of epochs, weight decay values, nor learning rate schedule for any nonlinear experiment (CIFAR-10, CIFAR-100, CNNs). This makes the experiments impossible to reproduce and raises concerns about potential cherry-picking of hyperparameters.

4. **No experimental comparison to existing FA variants for CNNs.** The paper states that FA "struggles to scale effectively in deep architectures, such as convolutional neural networks (CNNs)" (citing Bartunov et al., 2018) and that "recent work has made progress" (citing Bacho & Chu, 2024), but never actually runs FA or any prior FA variant on the same architectures to show RAF outperforms them. The reader cannot tell whether the CNN results represent genuine progress over the state of the art or simply a favorable experimental setup.

5. **No experimental comparison to Direct Feedback Alignment (DFA).** Since dRAF is positioned as analogous to DFA (Nøkland, 2016), a direct comparison to DFA (or its low-rank variants) is the most obvious baseline. Without it, the claim that RAF/dRAF is the *effective* way to use low-dimensional feedback is unsupported.

6. **Implementation of low-rank feedback in convolutional layers is underspecified.** The paper constrains feedback to ranks that are fractions of channel widths (1/2, 1/4, 1/8) but never explains how the low-rank feedback matrix interfaces with convolutional activations—whether the feedback operates on flattened spatial dimensions, is itself convolutional, or uses a different mechanism. This makes the CNN experiments irreproducible as described.

### Minor

1. **The transition from linear theory to nonlinear practice is unjustified.** The paper states the extension is "straightforward because the core principles remain applicable" (line 194), but provides no theoretical argument for why the linear dynamics analysis (which relies on MSE loss and linear activations) should predict behavior under ReLU activations and cross-entropy loss. The nonlinear experiments therefore stand as independent empirical claims, which are themselves insufficiently validated (see Major issues above).

2. **The biological receptive field experiments (Section 5) are purely qualitative.** Figure 4d shows example receptive fields under different rank constraints, but no quantitative metrics are reported (e.g., center-surround index, orientation selectivity index, spatial frequency selectivity). There is no statistical test, no comparison to biological data, and no ablation isolating the effect of feedback dimensionality from other training factors. This section does not constitute a rigorous test of the stated hypothesis.

3. **The claim about shallower layers compensating for tighter constraints (line 206) is unsupported.** The paper suggests deeper layers "compensate" for limited feedback in earlier layers, but provides no analysis of representation quality, gradient flow, or layer-wise contributions to support this interpretation.

4. **Figure 3c does not explicitly quantify BP performance on the same class subsets.** The claim that RAF "matches BP" when rank equals the number of classes is the paper's most striking result, but the reader cannot see the actual BP accuracy values for comparison on the figure or in the text.

### Trivial
None.

## Nice-to-Haves

- A direct comparison to DFA (Nøkland, 2016) as an empirical baseline would substantially strengthen the paper.
- Extending experiments to ImageNet-scale tasks and deeper architectures (e.g., ResNet) would test whether the rank constraint scales.
- Investigating whether low-rank feedback acts as an implicit regularizer by comparing generalization gaps between RAF and BP.
- Computing convergence speed / learning curves to see whether RAF requires more iterations than BP.

## Removed Points

These points were flagged for removal; treat with caution.

1. **"Omission of DFA as related work"** (Harsh Critic, Section 2 notes) — **REMOVED**: Factually wrong. The paper explicitly cites Nøkland (2016) on line 219 and discusses dRAF as "analogous to Direct Feedback Alignment."

2. **"Omission of Synthetic Gradients, weight mirror, sign-symmetry"** (Harsh Critic, Section 2 notes) — **REMOVED**: Per guidelines, missing related works cannot be confirmed as omissions without external sources. The paper is not required to cite every FA variant.

3. **Strength: "Error dimensionality shapes receptive fields"** (Strength Finder, point 5) — **MOVED TO REMOVED POINTS**: This strength conflicts with the verified weakness that the biological experiments are purely qualitative. Per guidelines, when a strength and weakness disagree, the weakness wins.

4. **"Omission of deep linear network simulations is a missed opportunity"** (Harsh Critic, Section 3.3) — **REMOVED**: The paper explicitly states this omission is intentional ("in the interest of brevity") and the extension is straightforward. The paper's main contribution is not deep linear network simulations.

5. **"Abstract overclaims — 'breakthrough,' 'reevaluation'"** (Harsh Critic) — **REMOVED**: This is a stylistic/subjective judgment about tone. The abstract's language is within the range of standard conference writing and does not constitute a technical weakness.

## Novel Insights

The central insight from synthesizing these reviews is that the paper's contribution is *bimodal*: its theoretical contribution (factorization + training of both Q and P, with linear dynamics analysis) is genuinely novel and rigorous, while its experimental validation is substantially below the standard needed to support the claimed conclusions. Prior work on FA (Lillicrap et al., Akrout et al., Kolen-Pollack) trained only the column space of the feedback matrix; this paper correctly identifies and formally proves why that fails under low-rank constraints and why training the row space is necessary. This theoretical contribution could stand on its own as a conceptual advance. However, the empirical gap—no quantitative numbers, no error bars, no comparison to FA/DFA baselines, no hyperparameter specifications—means the paper cannot yet substantiate its claim that this theoretical insight translates into effective training of deep nonlinear networks. The paper has the ingredients for a strong contribution but currently reads as an incomplete preprint whose experiments do not meet publication standards.

## Suggestions

1. **Report quantitative results in tables.** Provide exact test accuracy values (mean ± std over ≥5 runs) for all experiments, alongside the BP baseline. This is the single most important change.

2. **Specify all training hyperparameters.** Report learning rate, optimizer, batch size, number of epochs, weight decay, learning rate schedule, and any data augmentation used, for every experiment.

3. **Add direct comparisons to FA and DFA baselines** on the same architectures and datasets. Show that RAF outperforms these prior methods, especially for CNNs where FA is known to struggle.

4. **Clarify the CNN feedback implementation.** Specify how low-rank feedback matrices operate in convolutional layers (e.g., does the feedback matrix act on spatially-flattened feature maps, or is feedback itself convolutional?).

5. **Quantify the biological experiments.** Compute standard receptive-field metrics (center-surround index, orientation selectivity, spatial frequency tuning) across different rank constraints and report statistical comparisons.

6. **Provide learning curves** (training loss and test accuracy vs. epoch) to show convergence speed of RAF relative to BP.

7. **Add an ablation study** comparing: (a) train Q only, (b) train P only, (c) train both Q and P, in nonlinear settings, to empirically verify the theoretical claim that training P is necessary.

8. **Add error bars to Figure 3c** by showing BP accuracy as explicit horizontal reference lines for each class subset, so the "matches BP" claim can be evaluated visually.

## Score and Decision

**Originality:** High — factorizing FA into Q and P and identifying the need to train the row space is a novel conceptual contribution.  
**Importance of research question:** High — understanding minimal error dimensionality for learning is relevant to both efficient training and biological plausibility.  
**Claims well supported:** No — the central empirical claim (low-dimensional feedback matches BP) is not adequately supported due to missing quantitative reporting, error bars, hyperparameters, and baselines.  
**Soundness of experiments:** Low — the experimental section lacks basic reporting standards (no tables, no error bars, no hyperparameters, incomplete baselines).  
**Clarity of writing:** Fair — the theoretical sections are clear, but the experimental description is vague and underspecified.  
**Value to the research community:** Moderate — the theoretical insight is valuable and could inform future work, but as presented the paper does not provide reliable experimental evidence.

The paper introduces a genuinely novel idea with a solid theoretical foundation, but its experimental validation is severely lacking. The missing quantitative results, error bars, hyperparameter specifications, and baseline comparisons mean the central empirical claim cannot be evaluated. Major revisions involving rigorous benchmarking are needed before the paper could be considered for publication.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>
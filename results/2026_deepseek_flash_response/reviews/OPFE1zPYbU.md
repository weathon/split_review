## Summary

This paper argues that high-dimensional diffusion models do not learn statistical quantities (posterior, score, velocity field) as conventionally assumed. It identifies "weighted sum degradation" — where the empirical posterior p(x₀|xₜ) collapses to a single training sample in high dimensions — and proposes a "Natural Inference" framework that unifies existing sampling methods (DDPM, DDIM, Euler, DPM-Solver, DEIS) as autoregressive linear combinations of x₀ predictions, without requiring statistical concepts.

## Strengths

- **The paper identifies a real phenomenon and provides quantitative evidence for it.** Tables 1-2 document that at certain noise levels, the empirical posterior under a finite training set can be dominated by a single sample in high-dimensional latent spaces (ImageNet-256/512). The data itself is a useful empirical observation, regardless of how one interprets it.

- **The Natural Inference framework offers a clean algebraic unification of diverse sampling methods.** Expressing DDPM, DDIM, Euler, DPM-Solver, DPM-Solver++, and DEIS within a single lower-triangular coefficient-matrix form (Section 4.3) is a systematic encoding not previously presented in this specific form. The training-testing consistency constraint (∑cᵢᵗ ≈ √ᾱₜ, √∑(bᵢᵗ)² ≈ √1−ᾱₜ) is a nice observation.

- **The connection between Classifier-Free Guidance and classical Unsharp Masking (Section 4.1)** is a novel and intuitive analogy that reframes guidance as image enhancement rather than a probabilistic operation.

## Weaknesses

### Fatal
None. The weaknesses below are individually serious, but the paper's core observation — that the empirical posterior can be dominated by single samples in high dimensions — is a real phenomenon worth documenting. However, the paper's interpretation of this phenomenon and the conclusions drawn from it have fundamental problems.

### Major

1. **The degradation evidence (Tables 1-2) does not support the paper's central thesis and, if anything, cuts against it.**  
   For VP on ImageNet-256: at t=700–900 (high noise, where learning the distribution matters most), degradation is **0%**. At t=500–600 (moderate noise), degradation is 41–91%, but only 0–1% of those degrade *to the original X₀* — meaning the posterior is considering *multiple different* training points. Degradation reaches 100% only at t=200–400 (very low noise), where xₜ is nearly identical to the original X₀ by construction, so any reasonable posterior would naturally peak at X₀ regardless of the "curse of dimensionality." The paper asserts that "these models cannot effectively learn the underlying probability distributions" (Conclusion, line 306), yet the data shows degradation is absent at precisely the noise regime where distributional learning is most consequential. The paper never addresses this contradiction.

2. **The measurement procedure is partially tautological at low noise.**  
   The paper samples X₀, constructs xₜ = c₀·X₀ + c₁·ε, then computes μ = xₜ/c₀ = X₀ + (c₁/c₀)·ε. At low noise, (c₁/c₀) is tiny, so μ is necessarily very close to X₀. The posterior p(x₀|xₜ) then assigns highest probability to X₀ by construction (the Gaussian kernel is narrowest exactly where c₁/c₀ is smallest). Finding "degradation to X₀" under these conditions is expected and not evidence of a pathology that prevents learning. The paper then generalizes from this measurement at low noise to the sweeping conclusion that models cannot learn statistical quantities across all noise levels.

3. **The paper conflates the empirical posterior with what the model actually learns.**  
   The argument runs: because p(x₀|xₜ) under the *finite-sample* empirical distribution can collapse to one sample, the model cannot learn meaningful statistical quantities. This ignores two key facts about neural network training: (a) the model is trained on the *joint* objective 𝔼_{p(x₀,xₜ)}[∥f_θ(xₜ) − x₀∥²], which integrates across all noise levels *and* all data points — the network sees many (x₀, xₜ) pairs, not a single per-xₜ posterior estimate in isolation; (b) neural network inductive biases (smoothness, architectural priors, regularization) enable generalization beyond individual training points. The paper acknowledges that diffusion models do generalize (line 15: "achieving impressive results in high-dimensional data generation") but never reconciles this with its own argument about why they cannot.

4. **No experimental test of the core claim.**  
   The paper asserts that diffusion models "cannot effectively learn the underlying probability distributions or their key statistical quantities" but provides zero experiments that probe what trained models actually learn. A direct test would be to compare a trained model's predictions f_θ(xₜ) against the empirical posterior mean at different noise levels, or to measure whether learned representations capture distributional structure. No such experiments are presented. The only empirical content is the degradation rate in Tables 1–2, which addresses the *target* of learning, not what the model actually learns, and whose interpretation is problematic (see #1).

5. **The Natural Inference framework is descriptive, not generative, and its novelty is overstated.**  
   The framework unifies existing sampling methods by expressing each as a sequence of x₀-predictions with linear coefficients. However: (a) it is already well understood that these solvers are different discretizations of the same reverse-time ODE/SDE (Song et al., 2020b; Karras et al., 2022); expressing them in x₀-prediction form is a reformulation, not a discovery; (b) the paper derives nothing new from this framework — no novel sampling method, no improved algorithm, no testable prediction that distinguishes it from the standard statistical interpretation. The paper itself (Section 4.4) defers exploration of new parameter configurations to "future work." Claiming "a complete and fundamentally new perspective" that "opens up a promising new direction" (Section 1, contributions) is overclaimed for a descriptive reframing.

### Minor

1. **The frequency-domain analysis (Section 3.3) is qualitative and largely restates Dieleman (2024).** The observation that denoising progressively fills in frequencies from low to high is presented as a "simple way to understand the objective function," but no quantitative spectral measurements are provided (e.g., measuring what frequency components the model actually predicts at different noise levels for ImageNet).

2. **The paper's "curse of dimensionality" framing is imprecise.** The abstract claims diffusion models "seem to overcome" the curse of dimensionality, but this conflates the sample-complexity curse (formal statistical limitation) with empirical success — diffusion models require enormous datasets and compute, which is consistent with the curse. The broader question of how diffusion models work in high dimensions is valid, but the framing conflates distinct issues.

3. **Key verification of coefficient constraints (∑cᵢᵗ ≈ √ᾱₜ) is deferred to the appendix and code without concrete proof in the main text** (Section 4.3, line 284: "The calculation results show that the sum... is approximately equal to √ᾱₜ"). For a paper whose central framework relies on this claim, the main text provides surprisingly little mathematical development.

### Trivial

- Minor textual issues (e.g., a sentence fragment is repeated in the introduction at line 15).
- Figure descriptions are duplicated in the parsed text (parser artifact).

## Nice-to-Haves

- Testing a concrete prediction that distinguishes the "information enhancement" view from the standard statistical interpretation of diffusion models.
- Adding quantitative spectral analysis (e.g., measuring what frequency components the model predicts at different noise levels).
- Discussing how neural network regularization and the joint training distribution interact with the degradation phenomenon.

## Removed Points

These points were removed or demoted after verification against the paper:

- *Harsh Critic: "The paper sets up a straw man about the curse of dimensionality."* — **REMOVED**. The paper's question "how do diffusion models work so well in high dimensions?" is a genuine question studied in the literature (e.g., Karras et al., 2022). Labeling this a straw man misreads the paper's intent.
- *Harsh Critic: "Section 3.3 adds no formal analysis."* — **DEMOTED** to Minor. The section is explicitly labeled "A Simple Way to Understand" and cites Dieleman (2024); it does not claim to be formal analysis.
- *Harsh Critic: "Section 4.3 is surprisingly thin on actual mathematics."* — **DEMOTED** to Minor. The paper defers detailed calculations to Appendix C and code, which is acceptable practice for derivations.
- *Strength Finder: "Empirical validation of weighted sum degradation on high-resolution ImageNet."* — **KEPT** but qualified. The data exists but its interpretation undermines the paper's thesis (see Major #1).
- *Strength Finder: "Training-testing consistency as a design principle."* — **KEPT** as a minor supporting point; it is a straightforward constraint.
- *Strength Finder: "Self Guidance as a compositional primitive."* — **KEPT** as a minor point; this is a basic taxonomy.
- *Harsh Critic "Strengthening the Paper on Its Own Terms" section.* — **REMOVED**; these are constructive suggestions for future work, not weaknesses of the submitted paper.

## Novel Insights

None beyond the paper's own contributions. The reviewer analyses do not surface observations that the paper itself does not already articulate.

## Suggestions

1. Address the interpretation of Tables 1-2 explicitly: explain why the near-0% degradation at high noise (t=700-900) does not contradict the paper's central claim about models' inability to learn statistical quantities.
2. Add experiments that directly test what trained models learn — e.g., comparing model predictions f_θ(xₜ) to the empirical posterior mean E_{p(x₀|xₜ)}[x₀] at various noise levels, or probing whether learned representations capture distributional structure.
3. Tone down the novelty claims about the Natural Inference framework. It is a valid unification but does not constitute a "fundamentally new perspective" that generates new testable predictions.
4. Include a discussion of how neural network regularization, joint training across noise levels, and architectural inductive biases interact with — and potentially mitigate — the degradation phenomenon.

## Score and Decision

### Calibration Anchors

**Round 1 (Bracketing):**

| Path | Avg Score | Relevance |
|------|-----------|-----------|
| `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/XeGSIr7z6u.md` (On the onset of memorization to generalization transition in diffusion models) | 3.40 | Similar theoretical critique of diffusion models with evidence-interpretation issues |
| `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/rAZ3yCpc3K.md` (The Deficit of New Information in Diffusion Models) | 3.00 | Similar: makes a critical claim about diffusion models with validity issues |
| `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/X65IKSuWQo.md` (Unified Perspectives on Signal-to-Noise Diffusion Models) | 4.00 | Similar: unification/reinterpretation of diffusion models with limited novelty |
| `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/RuP17cJtZo.md` (Generator Matching) | 8.00 | Strong anchor: actual new theoretical framework with testable implications |
| `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/I5lcjmFmlc.md` (Robust Classification via a Single Diffusion Model) | 8.00 | Strong anchor |

**Bracket from Round 1:** The paper sits between the weak anchors (3.00–4.00) and the strong anchors (8.00). Most similar papers with interpretative flaws (3.00–3.40) or descriptive-only unification (4.00). Initial bracket: 3.0–4.0.

**Round 2 (Narrowing within the bracket):**

| Path | Avg Score | Relevance |
|------|-----------|-----------|
| `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/YryL3QIWWc.md` (Scaling Diffusion Models for Downstream Prediction) | 3.50 | Similar issues: limited novelty, evidence problems, reads as report |
| `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/yvxpHbydFx.md` (Understanding Diffusion-based Representation Learning) | 4.25 | Mixed reviews; theoretical claims not well-supported |

**Narrowing reasoning:** Compared to the 3.40 anchor (memorization-to-generalization), the paper under review has a similar degree of central-argument flaw but less theoretical depth. Compared to the 3.50 anchor (Scaling Diffusion Models), this paper has a more provocative central claim but significantly less empirical substance. After reading the full reviews for these anchors, the paper under review sits closest to the 3.00–3.40 level: its central claim is not supported by its own evidence, the measurement procedure has a tautological component, and it lacks experimental validation of the central thesis.

### Final Score and Decision

**Score: 3.0** — The paper asks a genuinely interesting question, but its central argument does not hold up under scrutiny. The empirical evidence presented (Tables 1-2) shows degradation is absent where learning matters most (high noise) and present where it is harmless (low noise), which contradicts the paper's thesis. The measurement procedure is tautological at low noise. The paper conflates the empirical posterior with what the model actually learns, ignoring neural network inductive biases. The Natural Inference framework is a valid but descriptive unification that does not generate new predictions. The contributions are significantly overclaimed relative to what is delivered.

**Decision: Reject**

MY FINAL SCORE: <score>3.0</score>
MY FINAL DECISION: <decision>Reject</decision>
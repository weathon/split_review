Now I have all the information I need. Let me write the consolidated review.

## Summary

This paper investigates whether generative (decoder-based) or non-generative (encoder-based) methods can achieve compositional generalization — the ability to perceive unseen combinations of concepts. The authors formalize the inductive biases needed to *guarantee* compositional generalization, proving (Theorem 3.2) that when the image dimension far exceeds the latent dimension, the derivative structure required to constrain an encoder to the appropriate function class \(\mathcal{G}_{\text{int}}\) becomes arbitrary and depends on unknown OOD manifold geometry, while the analogous constraints on a decoder are straightforward. They propose two strategies (gradient-based search and generative replay) for inverting a constrained decoder OOD. Empirically, they show that standard non-generative encoders trained from scratch or with moderate pretraining fail at compositional generalization on photorealistic PUG data, while generative methods using the same base architectures plus replay/search yield substantial OOD improvements.

## Strengths

- **Theorem 3.2 is a genuine theoretical contribution.**  It proves that when \(d_x \geq d_z^3\), the Jacobian and Hessian of inverse generators in \(\mathcal{G}_{\text{int}}\) can be arbitrary — the structure needed to guarantee OOD generalization (Eq. 3.3) for an encoder depends on the unobserved geometry of the OOD data manifold. This formalizes a fundamental asymmetry between the generative and non-generative directions that goes beyond heuristic intuition. The result is clean and non-trivial.

- **The formalization of the problem (Section 2) is clear and principled.**  Defining perception as inverting a ground-truth generator (Eq. 2.1), formalizing compositional generalization via in-/out-of-domain sets (Eq. 2.4), and connecting OOD identifiability to function class constraints (Eq. 2.5–2.6) provides a rigorous foundation that bridges compositional generalization, nonlinear ICA, and the causal/anti-causal learning literature.

- **The empirical evaluation is broad and uses photorealistic, controlled data.**  The experiments cover three compositional splits (background, texture, object) and multiple Vision Transformer backbones (DINOv1/v2, CLIP, I-JEPA, SigLIP2). Using the PUG datasets provides realistic imagery with explicit controllability over which concept combinations are seen vs. unseen. The pattern that non-generative methods often fail and generative methods with replay/search improve across architectures and splits is consistent with the theoretical asymmetry.

- **The n=0 special case provides a clean validation of the theory.**  When concepts do not interact (PUG-Object), \(\mathcal{G}_{\text{int}}\) is more structured, and indeed all non-generative methods achieve near-perfect OOD accuracy. This negative control strengthens the argument that the difficulty for non-generative methods in the \(n>0\) case stems from the structural complexity of \(\mathcal{G}_{\text{int}}\), not from the PUG data being inherently hard.

- **The search and replay strategies (Section 4) are clearly explained and practically motivated.**  The autoencoder-for-ID + search/replay-for-OOD pipeline is a well-structured recipe that connects the theoretical framework to a concrete algorithmic approach.

## Weaknesses

### Fatal

None.

### Major

- **The experiments do not directly test the paper's core theoretical claim.**  Theorem 3.2 says non-generative methods *cannot be guaranteed* to generalize OOD because enforcing \(\hat{g} \in \mathcal{G}_{\text{int}}\) via practical constraints is infeasible. The experiments show that *unconstrained* non-generative methods fail and that *constrained* generative methods with replay/search succeed. This tests a weaker claim: models without explicit compositionality constraints often fail, and extra OOD data or test-time optimization helps. The missing experiment is an attempt to constrain an encoder (e.g., via Eq. 3.3 regularization in a lower-dimensional setting, or via sparsity constraints for the n=0 case) to test whether such constraints *can* be enforced in practice, or whether they fail as predicted. Without this, the connection between theory and experiment is suggestive but not probative.

- **The improvement from generative methods is confounded with access to OOD data / test-time computation.**  The "generative" advantage in Fig. 6 comes from replay (which generates OOD-like training data by recomposing slots) and search (which optimizes at test time). The constrained decoder architecture is held constant between the non-generative autoencoder and the generative replay/search conditions. The paper does not isolate whether the improvement stems from the decoder being constrained to \(\mathcal{F}_{\text{int}}\) (the theoretical claim) or simply from having access to OOD training data (replay) or additional test-time gradient steps (search). The control experiment comparing constrained vs. unconstrained decoders in the generative setting is relegated to Appendix C (which is stripped during review) with the caveat that it is "not designed to match \(\mathcal{F}_{\text{int}}\)." This control belongs in the main paper.

### Minor

- **No error bars, confidence intervals, or multi-seed results are reported.**  All bar charts in Figs. 5 and 6 show point estimates with no variance information. Given the modest dataset size (~20K images) and the inherent variability in training slot-based models, this makes it difficult to assess the reliability of the reported improvements. Standard practice in this domain is to report results over multiple seeds.

- **The paper does not explain why SigLIP2 succeeds where other pretrained models fail.**  The observation that large-scale pretraining (SigLIP2) enables non-generative methods to achieve ~80% OOD accuracy on PUG-Background is potentially inconsistent with the theoretical claim that non-generative methods "cannot be guaranteed" to generalize. The paper attributes this to "large-scale pretraining" without analysis. Is SigLIP2 learning near-generative structure? Is it leveraging its training distribution to approximate \(\mathcal{G}_{\text{int}}\)? A deeper analysis here would strengthen the paper.

- **The claim that enforcing encoder constraints is "generally infeasible" is slightly stronger than what Theorem 3.2 proves.**  Theorem 3.2 shows that *local derivative-based constraints* (Eq. 3.3) become arbitrary when \(d_x \geq d_z^3\). The paper concludes that "enforcing such constraints on encoders is generally infeasible." This is reasonable as a claim about the specific class of constraints considered, but does not rule out other forms of global architectural biases or indirect regularization strategies. The paper hedges with "suggests" in several places but the abstract uses stronger language.

### Trivial

- The y-axis scale varies across subplots in Figs. 5 and 6 (A: 0–80%, B: 0–85%, C: 80–100%), making cross-panel comparison visually misleading. A consistent scale would be more informative.

## Nice-to-Haves

- **Qualitative evaluation of replay-generated images.**  The replay approach assumes the constrained decoder can generate realistic OOD images from recomposed slots. Showing examples of these generated images (and analyzing failures) would validate a key assumption of the approach.

- **Compute cost analysis for search.**  The gradient-based search approach requires per-image optimization. Reporting the number of gradient steps and total inference time would clarify practical applicability.

- **Test on more challenging OOD splits.**  PUG-Object saturates for all methods. Harder compositional splits (e.g., novel object-background interactions with occlusions or lighting changes) would better differentiate methods.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **Criticism that replay is "circular" because it assumes the decoder works OOD.**  This misreads the paper. The decoder is explicitly architecturally constrained to \(\mathcal{F}_{\text{int}}\) (via regularized cross-attention, per Brady et al., 2025), which gives it OOD identifiability by construction. The paper constrains the decoder architecture, it does not assume OOD generalization without justification.

2. **Criticism that the from-scratch ViT-S/36 baseline is "known to fail."**  This is one of many baselines; the main findings are driven by comparisons among pretrained models (DINOv1/v2, CLIP, I-JEPA, SigLIP2), all of which have been trained on much larger data. The from-scratch baseline is a reference point, not the main result.

3. **Criticism that supervised training on X_ID to predict categories is "standard OOD generalization, not a test of the perceptual inversion framework."**  The paper explicitly frames this task-based evaluation as a practical instantiation of the formal framework (Section 2: downstream tasks can be solved via slot-wise readout from inferred latents). The evaluation is appropriate for testing the practical consequences of the theory.

4. **Complaint about "missing proofs in appendix" or "missing appendix sections."**  The appendix is stripped by the PDF extraction pipeline; this is a parser artifact, not an author error.

5. **Claim that "autoencoders (used in Sec. 5) are a standard generative architecture" making the generative/non-generative distinction unclear.**  The paper explicitly distinguishes non-generative vs. generative by whether the representation is obtained by inverting a decoder on OOD data, not by architecture alone (lines 57–58). The VAE trained only for ID reconstruction is non-generative in this sense; the same decoder inverted via replay/search is generative. This is clearly operationalized.

## Novel Insights

The reviews do not surface insight beyond the paper's own contributions. The core tension is genuine: the theoretical result about \(\mathcal{G}_{\text{int}}\) is substantial, but the experiments do not cleanly test it, leaving the empirical argument weaker than the theoretical one. One observation that emerges from reading the reviews against the paper: the n=0 case (PUG-Object) is under-exploited in the critique — it provides the strongest empirical support for the theory (non-generative methods succeed exactly when the theory predicts they should), and none of the reviewers fully grapple with why this doesn't transfer to the n>0 case beyond task difficulty.

## Suggestions

1. **Add a controlled experiment attempting to constrain an encoder.**  Even an imperfect attempt (e.g., applying Eq. 3.3 regularization to the encoder in the \(d_x = d_z\) setting, or sparsity constraints for \(n=0\)) would directly test the theoretical claim and significantly strengthen the paper.

2. **Move the constrained vs. unconstrained decoder ablation (currently Appendix C) to the main paper.**  This directly addresses the confound between the decoder architecture and the replay/search benefits.

3. **Report all results with variance estimates over at least 3 seeds.**  Error bars are essential for interpreting the reliability of the improvements, especially given the modest dataset size.

4. **Analyze why SigLIP2 works for non-generative methods.**  Does it learn approximate \(\mathcal{G}_{\text{int}}\) structure, or does its training distribution fortuitously cover OOD combinations? This could determine whether the theory's "infeasibility" is a hardness result or a data-scale phenomenon.

## Score and Decision

**Calibration anchors (human-reviewed papers from the 2026 corpus):**

| Path | Avg Score | Comparison to this paper |
|------|-----------|--------------------------|
| `/home/wg25r/review_agent/human_reviews_2026/DcVg87ibK9.md` | 7.33 | Stronger empirically — cleaner experimental design, clearer causal claims. This paper has a weaker theory-to-experiment link. |
| `/home/wg25r/review_agent/human_reviews_2026/I3Ct1eDmVI.md` | 6.50 | Stronger overall — better theory-architecture alignment and cleaner empirical validation. This paper has a more novel theoretical result but weaker empirical execution. |
| `/home/wg25r/review_agent/human_reviews_2026/EEONns7ae4.md` | 6.40 | Stronger empirically — clearer experimental validation with controlled baselines. This paper has a more significant theoretical contribution but messier experiments. |
| `/home/wg25r/review_agent/human_reviews_2026/yi06ZiVl2H.md` | 4.80 | Very similar in structure (theory + empirical analysis of compositional generalization). This paper has a stronger theoretical result (Theorem 3.2 vs. necessary conditions for linear readout), but the anchor achieves cleaner theory-experiment alignment. |
| `/home/wg25r/review_agent/human_reviews_2026/ADeeoMY4Dn.md` | 4.50 | Similar in structure — theory with controlled experiments. This paper has a more substantive theoretical contribution, but the anchor's experiments are more directly linked to its theoretical claims. |
| `/home/wg25r/review_agent/human_reviews_2026/oSUjUvs999.md` | 4.00 | Weaker theoretically — purely empirical study. This paper has a genuine theoretical contribution that the anchor lacks. |
| `/home/wg25r/review_agent/human_reviews_2026/oMDK2F8kjH.md` | 3.50 | Weaker overall — less clear contributions and weaker experimental validation. This paper has a clearer theoretical framework and better-targeted experiments. |

**Relative positioning:** This paper sits between the stronger accepted papers (avg 6.0–7.3) and the borderline/weaker papers (avg 3.5–4.8) on related topics. Theorem 3.2 is a genuinely novel theoretical contribution that distinguishes this paper from the purely empirical studies in the 4.0 range. However, the experiments do not directly test the theory, and the main reported improvement (replay/search) is confounded with access to OOD data and test-time computation — which keeps the paper below the 6+ anchor papers where empirical claims are cleanly validated. Compared to yi06ZiVl2H (avg 4.80, very similar topic), this paper has a stronger theoretical result but weaker theory-experiment linkage, placing them at a similar level.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>
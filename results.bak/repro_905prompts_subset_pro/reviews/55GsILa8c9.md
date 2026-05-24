Now I have sufficient calibration data. Let me synthesize the final review.

**Round 1 Bracket:** The paper sits clearly above the weak band (3.0–3.5: papers with marginal results, confusing contributions) and below the strong band (7.5+: papers with rigorous theoretical contributions plus strong validation). The middle anchor hjROBHstZ3 (5.80) has stronger causal identifiability theory but weaker empirical validation; our paper has the reverse profile. This places us in the **5.5–7.0** bracket.

**Round 2 Narrowing:** 
- RankNovo (5.50): same task (de novo peptide sequencing), rejected. Modest improvements (~3.7%), high computational cost, reranking rather than fundamental advance. Our paper is stronger: larger improvements (+10-14%), more fundamental contribution.
- MADGEN (6.00): MS/MS-based generation, accepted with all 6s. Novel approach but predictive retrieval very weak, limited baselines. Our paper has more comprehensive evaluation and stronger empirical results.
- zKvrOOBouT (6.50): Erasing spurious correlations. More principled approach; our paper matches its empirical breadth.
- Bk13Qfu8Ru (7.00): Data pruning for spurious correlations. Stronger theory; our paper doesn't match this rigor.

**Final score:** 6.0 — stronger than RankNovo (5.50) and MADGEN (6.00) in empirical breadth and improvement magnitude, but the loosely operationalized causal formalism and the "enhance" step's use of privileged information prevent it from reaching the 6.5–7.0 tier.

---

## Summary

CausalNovo proposes a model-agnostic framework that learns representations of mass spectra invariant to spurious noise peaks for *de novo* peptide sequencing. The framework introduces a Causality Extraction Module (CEM) that computes per-peak importance scores, disentangling latent representations into causal ($\mathbf{z}_c$) and non-causal ($\mathbf{z}_s$) components. Three information-theoretic objectives — independence (contrastive alignment under interventions), sufficiency (cross-entropy on $\mathbf{z}_c$), and purification (cross-entropy on $\mathbf{z}_s$) — train the model to rely on true fragment ion signals. Experiments across three benchmarks and three strong Transformer baselines (CasaNovo, AdaNovo, π-HelixNovo) show consistent, substantial improvements of up to +14.2% in amino acid precision, +12.2% in peptide precision, and +15.1% in PTM precision.

## Strengths

- **Substantial, consistent empirical gains across diverse settings.** CausalNovo improves all three baselines on all three datasets (Tables 1, 2), with amino acid precision gains up to +14.2% (AdaNovo on HC-PT) and peptide precision gains up to +12.2% (π-HelixNovo on HC-PT). These are not marginal — they are large and consistent.

- **Thorough ablation design.** Table 4 cleanly isolates the contributions of independence (+1.2%), purification (+0.8%), and symmetric contrastive scheme (+0.4%). Table 5 validates the replace-and-enhance intervention design against drop-based and replace-only alternatives. These ablations give the reader a clear picture of what each component contributes.

- **Model-agnostic design convincingly demonstrated.** The framework integrates into three architecturally distinct Transformer models (CasaNovo, AdaNovo, π-HelixNovo) and improves all of them, supporting the claim of generality.

- **Multiple robustness analyses.** Cross-species validation (Table 3) shows gains across all eight held-out species. Vulnerability analyses (Figures 1, 3) demonstrate reduced dependence on non-causal peaks. NSR analysis (Figure 4) shows consistent gains across the full noise-signal ratio range. Attention analysis (Table 7) provides mechanistic evidence that CausalNovo shifts attention toward causal peaks (32.87% vs. 19.26% of predictions fully attending to causal peaks).

- **Practically relevant problem with real-world motivation.** The introduction's preliminary vulnerability analysis (Figure 1) empirically demonstrates that existing models rely on spurious noise peaks, motivating the need for the proposed approach.

## Weaknesses

### Fatal

None.

### Major

- **The "enhance" step in causal intervention uses ground-truth peptide information to construct training inputs.** Equation 4 identifies non-causal peaks by comparing against a theoretical spectrum generated from the ground-truth peptide, and the "causality enhancement" step adds all theoretical peaks into the intervened spectrum ($x_{\text{intervene}} = x_{\text{replace}} \cup x_{\text{theory}}$). This means the model sees a version of the input augmented with perfect fragment ion information during training — information unavailable at test time. Table 5 shows the method still yields improvement without enhancement (+0.6% amino acid precision from replace-only), which is reassuring, but the paper does not discuss the implications of this label-leakage-adjacent design, nor does it test whether the full framework would work without any ground-truth-derived spectrum augmentation.

### Minor

- **The causal formalism is operationalized through approximations that the paper treats as straightforward.** Using $Y$ as a proxy for unobserved $C$ (Section 3.4.2) and approximating conditional mutual information via InfoNCE are reasonable heuristics with literature precedent (Chen et al., 2022), but the paper presents them as near-equivalences without acknowledging the gap. The SCM-to-loss translation is not a derivation but a series of reasonable design choices — the paper would be stronger if it were more candid about this.

- **The purification objective ($\max I(\mathbf{z}_s; Y)$) is intuitively motivated but not theoretically grounded.** The argument that forcing $\mathbf{z}_s$ to also predict $Y$ will "purify" $\mathbf{z}_c$ makes practical sense (it incentivizes routing non-causal-but-predictive information to $\mathbf{z}_s$), but the paper does not connect this to the SCM or provide any theoretical justification. It reads as an ad-hoc regularizer that happens to work (Table 4: +0.8%).

- **Vulnerability evaluation uses perturbations similar to those seen during training.** The evaluation in Figures 1 and 3 replaces non-causal peaks — the same class of perturbation used for the contrastive training objective. The observed robustness may partly reflect training-time exposure rather than genuine causal invariance. The NSR analysis (Figure 4) partially addresses this by using a different evaluation protocol, but additional perturbation types (e.g., random peak dropping, intensity noise) would strengthen the causal-invariance claim.

- **Key hyperparameters $\alpha$ and $\gamma$ not specified in the main text.** The fraction $\alpha$ of replaced non-causal peaks and the $m/z$ tolerance $\gamma$ for identifying non-causal peaks are introduced as variables (Section 3.4.1) but their values are not stated in the main paper. These directly affect the intervention design.

### Trivial

- **Figure 1 naming scheme unexplained.** The legend uses "Baseline +", "CausalNovo (Duo)", and "CausalNovo (Duo) +" without defining these variants in the text. The "+" and "Duo" labels are disconnected from the method naming used throughout the rest of the paper.

## Nice-to-Haves

- A study training without any ground-truth-derived theoretical spectrum (e.g., using unsupervised peak-importance heuristics or the CEM's own learned scores to identify non-causal peaks) would clarify how much the privileged information matters.
- Robustness evaluation with perturbation types not seen during training (Gaussian intensity noise, peak dropping, $m/z$ shifting) would strengthen the causal-invariance narrative.
- Sensitivity analysis for $\alpha$, $\gamma$, $\tau$, and CEM architecture depth.
- Discussion of whether the ~2.3× training time increase is justified by the gains, and whether it can be reduced.
- Comparison with a simpler baseline: filter spectra to retain only b/y/a ions and train the baseline on the filtered spectra.

## Removed Points

These points are flagged to be removed, treat them with caution:

1. **"The causal formalism is not credibly operationalized" as a fatal flaw** — REMOVED as fatal, retained as minor. The paper follows established practices (Chen et al., 2022) for using $Y$ as a proxy for $C$ and InfoNCE for MI approximation. These are standard techniques in the causal representation learning literature, not fabrications. The paper is not claiming a novel theoretical derivation; it is applying existing frameworks to a new domain. The criticism is valid as a presentation weakness but not as a fatal methodological flaw.

2. **"Missing related works"** — REMOVED per hard rules (reviewer cannot verify missing references).

3. **"Table 6 shows gains come from contrastive invariance rather than identifying true causal ions"** — REMOVED. The paper already addresses this: "This is because the original three types of ions already cover most signal ones." This is a reasonable domain explanation, not a weakness.

4. **"The CEM architecture is never discussed or verified against chemical knowledge"** — REMOVED. The attention analysis in Table 7 provides exactly this verification: it shows CausalNovo increases attention to causal peaks. The paper does discuss what the CEM learns, just not at the individual-peak chemical level.

5. **Strength about "causal formulation grounded in established principles"** — KEPT but weakened. The RCCP framing provides useful intuition, but the operationalization is loose (see Minor weakness 1). This is a reasonable motivation, not a rigorous derivation.

6. **Strength about "the problem being important"** — DEMOTED. This is generic and applies to almost any paper. The paper's real strength is empirical, not problem selection.

## Novel Insights

The paper's most novel empirical insight is the vulnerability analysis (Figure 1) itself: it systematically demonstrates that current SOTA de novo sequencing models degrade substantially when non-causal peaks are perturbed, quantifying a phenomenon that the community has long suspected but not rigorously measured. Combined with the attention analysis (Table 7) showing the mechanism of improvement — CausalNovo shifts the model's top-3 attended peaks from 19% to 33% fully causal — this provides both diagnostic and mechanistic evidence that is valuable beyond the specific method proposed.

## Suggestions

- Reframe the contribution to foreground what the method actually does: a contrastive invariance objective paired with a learned peak-selection gate, rather than an exact instantiation of causal principles. The causal motivation is useful but should be presented as inspiration, not derivation.
- Add a "limitations" subsection explicitly discussing the role of ground-truth-derived theoretical spectra in the training intervention, and report results with α and γ values in the main text.
- Test robustness to at least one perturbation type not used during contrastive training (e.g., random peak intensity noise).

## Score and Decision

**Anchor comparison summary:**
- AvXrppAS2o (3.00, Round 1): Causal structure learning for outcome prediction — marginal results, unclear contributions. Our paper is substantially stronger.
- hjROBHstZ3 (5.80, Round 1): Causal representation learning from multimodal biological data — stronger theory, weaker empirics. Our paper is comparable with flipped strengths.
- 3cuJwmPxXj (8.00, Round 1): Intervention extrapolation via identifiable representations — both strong theory and validation. Our paper is clearly below this.
- RankNovo/87B3zDRMjv (5.50, Round 2): De novo peptide sequencing reranking — modest improvements, high cost. Our paper is stronger on results and contribution.
- MADGEN/78tc3EiUrN (6.00, Round 2): MS/MS molecular generation — novel but limited empirical validation. Our paper is comparable to slightly stronger.
- zKvrOOBouT (6.50, Round 2): Erasing spurious correlations — more principled approach. Our paper is slightly below on theoretical rigor.
- Bk13Qfu8Ru (7.00, Round 2): Data pruning for spurious correlations — stronger theory. Our paper is below this.

The paper delivers substantial, well-ablated empirical gains on an important problem, with a model-agnostic design demonstrated across three architectures. The loose causal formalism and the enhance-step concern are real but not fatal — the ablation shows the core method works without privileged information. The paper sits clearly above RankNovo (5.50) and is comparable to MADGEN (6.00), but with more comprehensive evaluation. The causal formalism weaknesses prevent it from reaching the 6.5+ tier where theoretical rigor is expected.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>
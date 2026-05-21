Now I have a thorough understanding of the paper and the calibration anchors. Let me write the final consolidated review.

## Summary

This paper proposes CausalNovo, a model-agnostic framework for de novo peptide sequencing that addresses the problem of models relying on spurious noise peaks rather than causal signal ions. The framework formalizes peptide sequencing using a Structural Causal Model (SCM) with two principles — independence and sufficiency — and introduces a Causality Extraction Module (CEM) with information-theoretic objectives to disentangle causal from non-causal representations. The method uses a replace-based intervention on identified noise peaks plus a causality enhancement step that adds theoretical spectrum peaks. Extensive experiments across three baseline models (CasaNovo, AdaNovo, π-HelixNovo) and three datasets (Nine-species, Seven-species, HC-PT) show consistent improvements in amino acid, peptide, and PTM-level metrics.

## Strengths

1. **Principled causal formulation grounded in an explicit SCM.** The paper formalizes de novo peptide sequencing using a Structural Causal Model (Section 3.2, Figure 2A) and derives two clear design principles — independence and sufficiency — from the structural equations (Equation 2). This goes beyond prior statistical models and provides testable conditions for causal representations.

2. **Consistent and substantial performance gains across 3 baselines × 3 datasets.** CausalNovo improves amino acid, peptide, and PTM-level metrics for CasaNovo, AdaNovo, and π-HelixNovo on all three datasets (Tables 1, 2). For instance, on HC-PT, CausalNovo raises CasaNovo's amino acid precision from 0.525 to 0.635 and AdaNovo's from 0.492 to 0.634. These improvements are consistent across all baselines, not cherry-picked.

3. **Direct evidence of robustness to noise perturbations.** When noise peaks are systematically perturbed (Figure 1, Figure 3, Table 6), baseline models drop sharply while CausalNovo maintains higher performance. Under the strictest threshold (γ=1 on HC-PT), CausalNovo achieves a 28.5% relative improvement in peptide precision (Table 6), directly showing the model learns to rely less on spurious correlations.

4. **Thorough ablation studies isolating the contribution of each component.** Table 4 shows the stepwise improvement from independence (+1.2% AA precision) to purification (+0.8%) to symmetric training (+0.4%). Table 5 separately ablates the replace-based perturbation (+0.6%) and the causality enhancement (+0.6%) in the intervention. These controlled experiments provide clear evidence that each design choice contributes.

5. **Cross-species validation demonstrates generalization to unseen organisms.** On the Nine-species leave-one-out setup (Table 3), CausalNovo improves CasaNovo's peptide precision in every species, e.g., Mouse (0.558 → 0.595), Tomato (0.506 → 0.545). This shows the framework improves out-of-distribution robustness.

6. **Attention analysis directly links the framework to better use of causal fragments.** Table 7 shows CausalNovo increases the fraction of predictions where the model's top-3 attended peaks are all causal from 19.26% to 32.87%, and reduces the fraction with zero causal peaks from 12.73% to 10.76%.

## Weaknesses

### Major

- **The purification objective (maximizing I(z_s; Y)) is poorly motivated and its reasoning is unclear.** The paper states (line 101): "However, it can reduce I(z_s; Y). To address this issue, we introduce an auxiliary objective that maximizes I(z_s; Y) which can indirectly lead to the purification of z_c." The logic is confusing: typically one would *minimize* I(z_s; Y) to enforce disentanglement. The paper does not explain *why* reducing I(z_s; Y) is a problem or how maximizing it purifies z_c, nor does it provide a theoretical justification. While Table 4 shows it empirically helps, the component's rationale is incoherent as presented, making it hard to build upon.

- **Comparison with non-retrained baselines compromises fairness of the SOTA claims.** The paper marks retrained baselines with † but directly compares against numbers for SearchNovo, DeepNovo, PointNovo, and InstaNovo taken from NovoBench without retraining under the same protocol. The retrained baselines often differ substantially from their original NovoBench numbers (e.g., CasaNovo original: 0.697 AA precision on Nine-species, retrained: 0.741). This means comparisons between CausalNovo+Baseline and non-retrained methods mix two sources of gain: the CausalNovo framework and the retraining setup. The paper should either retrain all competitors or clearly acknowledge this asymmetry and qualify the SOTA claims accordingly.

### Minor

- **Key hyperparameters (γ tolerance threshold, α replacement fraction) are not reported.** Equation (4) defines γ for identifying non-causal peaks, and Section 3.4.1 introduces α as the fraction of noise peaks replaced, but neither default value is provided in Section 4.2 (Implementation Details). The threshold values in Table 6 (8, 4, 2, 1) are also not tied to physical units (ppm, Da?), making the results hard to interpret precisely and the experiments impossible to reproduce exactly.

- **No statistical significance or variance is reported for any experiment.** All results in Tables 1–3 and 6 are single-point estimates. Given the modest absolute gains in some settings (e.g., +2.4% AA precision on Nine-species for CasaNovo), the absence of error bars or multiple trials makes it impossible to assess whether improvements are stable or could arise from random seed variation.

- **The causal intervention relies on ground-truth theoretical spectra, and the separation of the causal contrastive learning benefit from simpler label-aware augmentation is not fully established.** Table 5 shows that adding theoretical peaks (the "enhance" step) contributes +0.6% AA precision. A natural control experiment — training a baseline that naïvely adds theoretical spectrum peaks as extra input channels without the causal contrastive loss — would help substantiate the claim that the *causal* framework, and not just the injection of clean signal peaks during training, drives the gains. The existing ablation shows incremental improvement but does not isolate this confound.

### Trivial

- None that survive filtering (parser artifacts excluded, no formatting issues identified).

## Nice-to-Haves

- The causal intervention uses the ground-truth peptide's theoretical spectrum to identify noise peaks and add clean signal peaks. The paper frames this as "established domain knowledge" (line 113), which is appropriate, but a brief discussion of potential label leakage concerns and why it does not invalidate the method would strengthen the paper.
- The independence objective (Equation 5) uses Y as a proxy for the unobserved causal factors C. The justification for why Y is a valid proxy (the stable causal relationship) is brief. A more detailed discussion would help.
- The "up to 10%" claim in the abstract is actually an *understatement* for several settings (e.g., +12.0% AA precision on Seven-species, +15.1% PTM precision on Seven-species), not an overstatement as the critic suggested. The phrasing could be more precise but the actual gains are larger than claimed.

## Removed Points

These points were raised by reviewers but removed after verification against the paper:

- **"The up to 10% claim is misleading because it's relative, not absolute"** — Removed as factually incorrect. The improvements are absolute percentage points (e.g., 0.525→0.635 = +11.0% absolute on HC-PT). The claimed "10%" is actually conservative.
- **"Missing related works"** — Removed per policy (cannot verify existence of missing citations from external knowledge).
- **"Formatting and presentation nitpicks"** — Removed per policy (parser artifacts, not author errors).
- **"Strawman: the causal intervention requires ground-truth labels"** — Partially retained as a minor weakness under the proper framing (the separation of causal contrastive learning from label-aware augmentation is not fully established), but the critic's framing as a fatal flaw is removed. The paper openly acknowledges using theoretical spectra as domain knowledge (line 113) and the ablation isolates the enhance step's contribution.
- **"The SCM independence assumption is not derived"** — Removed. The paper states "C ⟂ S" in Equation (2) as a design principle derived from RCCP, which is correctly framed as a modeling assumption guiding architecture design, not an empirical finding.

## Novel Insights

None beyond the paper's own contributions. However, one interesting observation emerges from cross-referencing the reviewer inputs: the harsh critic's concern about the causal intervention being "heavily supervised by ground-truth information" sits in productive tension with the paper's framing of using theoretical spectra as "established domain knowledge." This tension — between viewing label-derived signals as privileged information versus accepted domain expertise — is a recurring issue in biomedical ML that the paper could surface more explicitly. The attention analysis (Table 7) is the most compelling evidence that CausalNovo genuinely learns different representations rather than just benefiting from cleaner inputs.

## Suggestions

1. **Add a control baseline that augments the input with theoretical spectrum peaks** without the causal contrastive loss (e.g., by concatenating theoretical peaks as extra input channels, or using a multi-task loss to predict which peaks are signal). If the full CausalNovo still outperforms this baseline, the causal disentanglement claim is strongly supported.

2. **Clarify the purification objective with a concrete derivation or intuition.** Explain why maximizing I(z_s; Y) is needed, how it avoids trivial solutions, and how it relates to standard disentanglement losses (e.g., minimizing mutual information between z_c and z_s).

3. **Report γ (default value and units), α, and add error bars** (mean ± std over ≥3 random seeds) for main results.

4. **Retrain all competitors** (SearchNovo, DeepNovo, PointNovo, InstaNovo) under the same protocol to enable fair apples-to-apples comparisons, or clearly state which numbers are from the benchmark and add a caveat about the comparison's limitations.

## Score and Decision

My round-1 bracket placed the paper between the weak anchors (avg ~2.5–3.33 for reject-range papers on mass spectrometry / peptide tasks) and strong anchors (avg 8.0 for top papers), specifically in the 4–6 range. Round-2 narrowed this to comparing against SpectraLLM (5.00), CaSBRE (4.50), and PepTri (5.50).

**Comparison to anchors:**

- **CaSBRE (4.50, Reject):** CaSBRE's core weakness was that the "causal" framing was not supported — no explicit SCM, no theoretical guarantees, heuristic do-calculus. CausalNovo is substantially stronger on this axis: it has an explicit SCM, derives two principles, and provides formal mutual-information objectives. CausalNovo also has more extensive experiments (3 baselines × 3 datasets vs. 2 datasets for CaSBRE). **CausalNovo is clearly stronger.**

- **SpectraLLM (5.00, Accept Poster):** SpectraLLM's main weakness was incremental originality (LLM fine-tuning on spectral tokens). CausalNovo has a more novel core idea (causal framework for peptide sequencing) and provides code. Both have missing hyperparameters and lack error bars. SpectraLLM's results are more dramatic (SOTA across multiple spectral modalities), but CausalNovo's ablation studies are more thorough. **CausalNovo is slightly stronger.**

- **PepTri (5.50, Accept Poster):** PepTri has a well-motivated tri-guidance approach with comprehensive evaluation. CausalNovo has a similar level of empirical thoroughness but its methodological contribution (causal disentanglement for peptide sequencing) is arguably more novel. However, PepTri's weaknesses are mostly about missing architectural details (fixable), while CausalNovo has the incoherent purification objective which is a deeper conceptual concern. **Comparable, PepTri slightly stronger on conceptual clarity.**

- **PepBenchmark (6.00, Accept Poster):** A benchmark paper with a different contribution type. Not directly comparable.

The paper makes a genuine contribution — the first causal framework for de novo peptide sequencing with extensive empirical support — but is held back by the poorly motivated purification objective, missing hyperparameters, and the need for a cleaner control experiment to separate causal learning from label-aware augmentation. These are fixable issues, not fatal flaws.

**Final score: 5.0**

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Accept</decision>
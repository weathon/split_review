Now I have enough calibration data. Let me compile the final review.

## Summary

CausalNovo proposes a model-agnostic framework for *de novo* peptide sequencing that augments existing architectures (CasaNovo, AdaNovo, π-HelixNovo) with causal representation learning. The framework distinguishes signal ("causal") from noise ("non-causal") peaks using theoretical spectrum matching, then applies contrastive learning to enforce independence (invariance to noise perturbations) and sufficiency (retaining predictive information). Experiments on three benchmark datasets show consistent improvements in amino acid, peptide, and PTM-level metrics across all baselines, supported by mechanistic evidence (attention analysis, vulnerability analysis, NSR generalization).

## Strengths

1. **Mechanistic validation via attention analysis (Table 7)**: The paper directly demonstrates that CausalNovo shifts model attention toward causal signal peaks. The baseline completely ignores causal peaks in 12.73% of predictions; CausalNovo reduces this to 10.76% and nearly doubles the fraction where all top-3 attended peaks are causal (19.26% → 32.87%). This provides internal evidence that the framework changes model behavior as intended, not just that aggregate metrics improve.

2. **Consistent gains across 3 baselines × 3 datasets × multiple metrics (Tables 1, 2)**: CausalNovo improves amino acid, peptide, and PTM-level performance for CasaNovo, AdaNovo, and π-HelixNovo on Nine-species, Seven-species, and HC-PT without exception. On Seven-species, CausalNovo boosts π-HelixNovo's amino acid precision from 0.465 to 0.536 (+7.1%) and PTM precision from 0.362 to 0.513 (+15.1%), surpassing SearchNovo.

3. **Vulnerability and NSR analysis (Figures 1, 3, 4)**: Baseline models degrade when noise peaks are perturbed, while CausalNovo variants maintain substantially higher precision. The performance gap widens at higher noise-signal ratios, confirming that focusing on causal signal peaks is what drives robustness. Average Relative Improvements of +14.9%, +15.7%, and +13.5% on HC-PT across three baselines.

4. **Cross-species validation (Table 3)**: Leave-one-out validation across all eight species in the Nine-species dataset shows CausalNovo improves CasaNovo's peptide precision on every species (average +2.6%), with largest gains on challenging species like Tomato (+3.9%).

5. **Ablation isolating each component (Tables 4, 5)**: The ablation study cleanly attributes marginal contributions to independence (+1.2% AA precision), purification (+0.8%), symmetric training (+0.4%), replace (+0.6%), and causality enhancement (+0.6%), confirming each design choice is justified.

6. **Robustness to peak-distinguish strategy (Table 6)**: Using 18 ion types instead of the default 3 yields consistent improvements (28.5% relative improvement at threshold=1), showing the framework does not depend on a specific noise-identification scheme.

## Weaknesses

### Major

1. **No variance or statistical significance reporting across all experiments**: Every result in Tables 1–7 and Figures 1–4 is reported as a single point estimate with no standard deviations, confidence intervals, or indication of multiple runs. For deep learning models trained with multiple stochastic objectives (cross-entropy, contrastive loss, two auxiliary decoding losses), performance can vary meaningfully across seeds. The retrained baselines themselves exhibit non-trivial variation relative to published values (e.g., AdaNovo on Nine-species drops from 0.698 to 0.681, while CasaNovo rises from 0.697 to 0.741), suggesting training variance that should be characterized. Without variance estimates, smaller improvements (e.g., +2.2% for π-HelixNovo on Nine-species, +1.2% for the independence principle in ablation) cannot be assessed for statistical significance.

2. **Missing hyperparameter values for core intervention parameters**: The fraction α of non-causal peaks replaced (Section 3.4.1) and the m/z tolerance threshold γ (Eq. 4) are never specified numerically. These directly control the intervention that drives the entire framework. The temperature τ is reported (τ=0.1), but α and γ are absent. This is a genuine reproducibility concern, particularly since the ablation (Table 5) shows the replace operation contributes only +0.6% to AA precision — the specific choice of α could meaningfully affect this.

### Minor

1. **Information leakage concern in the intervention design**: The intervened spectrum is defined as $x_{\text{intervene}} = x_{\text{replace}} \cup x_{\text{theory}}$, where $x_{\text{theory}}$ contains theoretical peaks computed from the **ground-truth** peptide sequence. Adding these clean, perfectly-aligned theoretical peaks into the intervened spectrum during contrastive training creates a potential shortcut: the model could learn to recognize these artificially pristine peaks as a reliable signal, rather than learning to extract causal structure from messy real data. While the ablation (Table 5) shows the "enhance" step contributes only +0.6%, this design choice deserves explicit discussion and ideally a control experiment without $x_{\text{theory}}$.

2. **Causal framing is aspirational relative to the implemented method**: The signal/noise separation (Eq. 4) is a well-established procedure from prior work (Tyanova et al., 2016; Mao et al., 2023; Qiao et al., 2021), as the paper honestly notes. The causal SCM provides a principled justification but does not itself generate the intervention strategy — the practical contribution is a noise-invariance training objective guided by domain knowledge. This is a worthwhile contribution, but the paper's framing overstates the methodological novelty of the "causality-informed" aspect. The paper would be stronger if it presented itself as a well-engineered noise-invariance training framework with mechanistic validation, rather than a fundamental causal discovery advance.

3. **Evaluation follows the standard NovoBench protocol, not the more recent out-of-distribution protocol**: As the paper acknowledges in the conclusion, recent methods (ContraNovo, RankNovo) adopt a protocol training on large-scale external corpora and evaluating on held-out distributions. Given the paper's motivation (models fail under distribution shift), this evaluation protocol would be more informative. The current evaluation (held-out species from the same distribution) is the community standard but limits the paper's claims about real-world generalization.

### Trivial

1. Perturbation thresholds in Figure 1 (16, 12, 8, 4, 2) lack defined units (m/z tolerance in what unit?), making the figure harder to interpret.
2. The "up to 10%" headline claim in the abstract is technically correct but is drawn from the Seven-species or HC-PT datasets where baseline performance is low; the gains on the more standard Nine-species benchmark are 2–6%.

## Nice-to-Haves

1. A control experiment without adding $x_{\text{theory}}$ to the intervened spectrum to isolate the information leakage concern.
2. Sensitivity analysis over α and γ values.
3. Reporting results over 3+ random seeds with standard deviations.

## Removed Points

These points from the inputs were flagged for removal, treat them with caution:

1. **"Retrained baseline inconsistency is inconsistently favorable" (Harsh Critic)**: Removed. Reporting both original and retrained baselines is standard good practice for fair comparison. The paper transparently reports both; there is no evidence of selective reporting.
2. **"Y as proxy for C is a theoretical gap" (Harsh Critic)**: Removed. The paper explicitly cites Chen et al. (2022) for this approximation and frames it as a practical design choice. This is a recognized limitation in this line of causal representation learning work.
3. **"C ⟂ S independence assumption weakens SCM fidelity" (Harsh Critic)**: Removed. Simplifying assumptions are standard in causal modeling. The empirical results validate the approach despite the simplification.
4. **"Principled derivation from Structural Causal Models" (Strength Finder)**: Partially qualified into weakness #2 above. The SCM framework provides a theoretical lens but the method is better characterized as domain-guided noise-invariance training.

## Novel Insights

The combination of attention analysis (Table 7), cross-species validation (Table 3), and NSR analysis (Figure 4) collectively tells a coherent story that goes beyond aggregate metric improvements: CausalNovo's noise-invariance training genuinely shifts model focus toward signal ions, and this behavioral change translates to consistent gains that are largest precisely where they matter most — on challenging species (Tomato: +3.9% peptide precision) and high-noise settings (+10–12% average AA precision improvement at high NSR). This suggests the framework addresses a real vulnerability in existing models (over-reliance on spurious noise peaks) rather than squeezing additional performance through other means. The ablation study's clean decomposition (each component contributes incrementally) provides a clear recipe for future method development in this space.

## Suggestions

1. Report standard deviations over 3+ random seeds for all main results.
2. Provide numerical values for α and γ, and include a sensitivity analysis over their ranges.
3. Add a control experiment that removes $x_{\text{theory}}$ from the intervened spectrum to verify the independence principle holds without potential leakage.
4. Tone down the causal framing to match the method's true nature: domain-guided noise-invariance training with mechanistic validation, rather than fundamental causal discovery.
5. Evaluate under the out-of-distribution protocol used by ContraNovo/RankNovo, as the paper acknowledges is needed.

## Calibration Report

**Round 1 (Bracketing):**
- Low band (score < 3.5): Distilling (4.25), CypST (2.0), Learning High-Order Substructure (2.5), TorSeq (3.0) — CausalNovo is clearly stronger than all of these.
- Middle band (3.5–7.5): ReNovo (6.50), RankNovo (5.50), Distilling (4.25), InvMSAFold (7.25) — CausalNovo sits between RankNovo (rejected, narrower evaluation) and ReNovo (accepted, similar empirical scope but more novel paradigm).
- High band (>7.5): Causal representation learning papers (8.0) — CausalNovo does not match the theoretical depth of these.

**Round 2 (Narrowing):**
- Query 1 (4.5–6.5): RankNovo (5.50, reject), MADGEN (6.00, accept), PepHAR (6.20, accept), Inverse Folding DPO (4.75, reject).
- Query 2 (6.0–8.0): Identifiable Exchangeable Mechanisms (6.50, accept), Neural Causal Graph (6.25, accept), Zero-Shot Learning of Causal Models (6.25, reject), Robust Causal Discovery (6.67, accept).

**Comparison against key anchors read in full:**
- **ReNovo (6.50, accept)**: Retrieval-based de novo sequencing. Similar evaluation breadth; CausalNovo has better mechanistic analysis but ReNovo's retrieval paradigm is more novel. **CausalNovo ≈ slightly weaker** (less methodological novelty, better analysis).
- **RankNovo (5.50, reject)**: Reranking framework. CausalNovo has broader, more consistent improvements and mechanistic validation. **CausalNovo is stronger.**
- **MADGEN (6.00, accept)**: Molecular generation from MS. Similar profile of real contributions with notable limitations (poor predictive retriever, missing baselines). **CausalNovo ≈ MADGEN** but with better evaluation breadth.
- **Distilling (4.25, reject)**: Engineering-oriented without strong novelty. **CausalNovo is significantly stronger.**

**Final bracket:** Round 1 placed the paper between ~4.5 and ~6.5. Round 2 narrows this to **5.5–6.5**, with CausalNovo sitting above RankNovo (5.5) and comparable to MADGEN (6.0) and slightly below ReNovo (6.5).

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>
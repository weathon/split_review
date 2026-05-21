Now I have all the information I need. Let me synthesize the final review.

## Summary

CausalNovo applies causal representation learning (independence and sufficiency principles derived from an SCM) to *de novo* peptide sequencing. It introduces a Causality Extraction Module (CEM) that disentangles causal signal peaks from non-causal noise peaks in the latent space, using contrastive learning and cross-entropy objectives. Evaluated on three benchmarks (Nine-species, Seven-species, HC-PT) across three strong baselines (CasaNovo, AdaNovo, π-HelixNovo), CausalNovo yields consistent improvements at amino acid, peptide, and PTM levels (up to +12-14% on some metrics), with convergent evidence from vulnerability, NSR generalization, and attention analyses.

## Strengths

1. **Well-motivated vulnerability analysis grounds the core claim in observable evidence.** Figure 1 shows that when noise peaks are replaced, baseline CasaNovo drops from ~0.55 to ~0.35 amino acid precision (at threshold 2), while CausalNovo maintains ~0.65 — a ~20% relative improvement. This directly demonstrates that baseline models indeed exploit spurious correlations and that the proposed method mitigates this behavior.

2. **Consistent and substantial gains across diverse settings.** Tables 1–3 show that CausalNovo improves all three baselines on all three datasets at amino acid, peptide, and PTM levels. For example, on Seven-species, CasaNovo precision rises from 0.357 to 0.477 (+12.0%); on HC-PT, AdaNovo precision rises from 0.492 to 0.634 (+14.2%). Cross-species validation (Table 3) further confirms generalizability with an average +2.6% peptide precision improvement across nine species, providing robust evidence that the gains are not dataset-specific.

3. **Convergent mechanistic evidence supports the causal claim.** Table 7 shows that CausalNovo increases the proportion of predictions where all top-3 attended peaks are causal from 19.26% to 32.87%, and reduces the proportion attending zero causal peaks from 12.73% to 10.76%. This interpretability analysis directly links the causal objectives to changed model behavior.

4. **Ablation studies decompose the contribution of each component.** Tables 4–5 show that each of independence, purification, symmetric training, and the replace/enhance intervention strategies contributes measurable improvements. The stepwise ablation provides insight into which objectives drive the gains.

5. **Honest limitation disclosure.** The paper acknowledges the ~2.3× training overhead, the current evaluation protocol's limitations, and the reliance on ground-truth theoretical spectra for peak labeling — transparency that strengthens the credibility of the claims that are made.

## Weaknesses

### Fatal
None.

### Major

1. **No control for increased model capacity.** The CEM adds 3 Transformer layers + an MLP head on top of the baseline encoder-decoder architecture. The ablation in Table 4 compares the baseline (no CEM) against variants that all include the CEM plus the causal objectives, so the first ablation step conflates an architectural increase with the independence objective. Without a control experiment that adds the same CEM to the baseline but trains only with standard cross-entropy (no causal losses), the observed improvements cannot be cleanly attributed to the causal principles rather than to extra model capacity. This is a structural gap in the experimental design, and it is the single most important issue to address.

2. **No statistical significance reporting.** No standard deviations, confidence intervals, or multiple-seed results are reported for any main table or ablation. Given that several improvements are in the 2–6% range (and that the AdaNovo retrained baseline, at 0.681, differs from its published value of 0.698), it is impossible to assess whether the reported differences are robust across training runs. Multiple random seeds (at least 3) with standard deviations for Tables 1, 2, and 4–5 are expected for this class of work.

### Minor

3. **Training tolerance threshold γ and replacement fraction α are not reported.** Equation (4) defines γ as the m/z tolerance for distinguishing causal from non-causal peaks, and Section 3.4.1 defines α as the fraction of noise peaks replaced during the causal intervention. Neither value is specified for the main training setup (the vulnerability analysis varies γ only during evaluation). This is a reproducibility gap, as these hyperparameters directly determine which peaks are labeled non-causal and thus shape the entire contrastive learning signal.

4. **AdaNovo retraining gap unaddressed.** In Table 1, the retrained AdaNovo reports 0.681 amino acid precision on Nine-species, while the published AdaNovo reports 0.698 — a 1.7% difference. This is larger than several ablation deltas in Table 4 and could inflate the apparent CausalNovo improvement. The paper should explain this discrepancy (e.g., different training configuration, hyperparameters, or dataset splits).

5. **Purification objective mechanism underspecified.** The sufficiency and purification losses (§3.3) both use cross-entropy via the same decoder ρ, but it is unclear whether the decoder weights are shared between the z_c and z_s pathways. If they are shared, gradients from the z_s cross-entropy will affect the decoder's representations for both branches, and the paper does not explain how this interaction is handled or whether separate prediction heads are used.

### Trivial
None.

## Nice-to-Haves

- The C ⟂ S independence assumption in the SCM could be discussed as a limitation, with synthetic experiments testing robustness to correlated causal/non-causal factors. This would strengthen the theoretical framing.
- Concrete inference time (ms/spectrum) would be useful beyond the qualitative "negligible" claim.
- An explanation of why mean pooling (rather than per-peak) is appropriate for the contrastive loss in Eq. (5), given that the attention analysis focuses on per-peak structure, would improve methodological clarity.

## Removed Points

*The following points raised by the reviewers were removed for the reasons stated. They are preserved here in case they are useful.*

- **"Conceptual gap: independence assumption C ⟂ S could be violated"** — This is a valid theoretical limitation but not a concrete empirical weakness; the paper's results already demonstrate practical success. Demoted to Nice-to-Have.
- **"Missing discussion of decoder weight sharing in purification objective"** — Kept as Minor above; the removal here is for the specific phrasing about "gradient affecting CEM scoring," which goes beyond what the paper omits. The core point about clarifying decoder sharing is retained.
- **"Mean pooling loses per-peak structure"** — Demoted to Nice-to-Have; the contrastive learning and attention analysis serve different purposes and the inconsistency is not harmful.
- **Strength Finder: generic strengths** (e.g., "this paper addressed an important problem") were removed. Only concrete, evidence-anchored strengths were retained.
- **Human Finder results about other papers (weaknesses about unrelated works)** — Removed as they do not pertain to this paper.

## Novel Insights

None beyond the paper's own contributions. The reviews did not surface a perspective that the paper itself does not already articulate. If anything, the reviews confirm the paper's own framing: the core contribution is the application of causal representation learning (independence + sufficiency) to de novo peptide sequencing, and the main open question — shared by both the harsh critic and a parallel review of a related de novo paper (ReNovo) — is whether such gains are driven by the causal objectives or by increased model capacity.

## Suggestions

1. **Add a capacity-controlled baseline.** Augment the baseline (CasaNovo/AdaNovo/π-HelixNovo) with the same CEM architecture (3 Transformer layers + MLP) but train with only the standard cross-entropy loss (no independence, purification, or symmetric contrastive objectives). If this augmented baseline already matches CausalNovo, the gains are architectural; if it does not, the causal losses are clearly driving improvement. This single experiment would substantially strengthen the paper.

2. **Report standard deviations over ≥3 random seeds** for the main results (Tables 1, 2, 4, 5) and for the cross-species validation.

3. **Disclose the training γ and α values** used for the main results, and briefly motivate the choice (e.g., "following standard practice in database search, we set γ = X ppm").

4. **Explain the AdaNovo retraining discrepancy** — is it a different training setup, hyperparameter, or dataset split?

5. **Clarify the purification objective implementation** — are decoder weights shared between z_c and z_s branches, or are separate prediction heads used?

## Score and Decision

### Round 1 — Bracketing

Three queries across score bands, each retrieving 4 anchors on de novo peptide sequencing and causal/proteomics topics:

**Weak band (<3.5):** TorSeq (3.0), AI Derivation (3.0), CypST (2.0), Learning High-Order Substructure (2.5). These papers have fundamental flaws and are clearly below CausalNovo.

**Middle band (3.5–7.5):** ReNovo (6.5, Accept), Distilling NAT→AT (4.25, Reject), RankNovo (5.5, Reject), MADGEN (6.0, Accept). CausalNovo is clearly stronger than the 4.25 paper and comparable to the 5.5–6.5 papers.

**Strong band (>7.5):** Identifying Representations for Intervention Extrapolation (8.0), ProtComposer (8.0), Discrete Walk-Jump Sampling (8.0), SE(3)-Stochastic Flow Matching (8.0). These are top-tier papers; CausalNovo does not match their theoretical depth or novelty breadth.

**Round-1 bracket:** 4.5–7.0.

### Round 2 — Narrowing

Two queries inside the bracket:

**Lower-middle (4.5–6.0):** RankNovo (5.5), Multi-Scale Protein LM (5.0), MSA Generation (5.67), RINGER (5.75). CausalNovo is stronger than all of these: it has clearer motivation, more consistent improvements, and deeper analysis.

**Upper-middle (6.0–7.5):** Spatial Causal Disentanglement / Celcomen (6.67), Causal Order from Interventions (7.0), CausalRivers (7.33), Causal Modelling Agents (6.25). These papers have stronger causal-theory grounding (identifiability proofs, theoretical guarantees) but CausalNovo has stronger empirical evaluation across multiple datasets and baselines.

### Final Placement

CausalNovo is comparable to ReNovo (6.5, Accept) and Celcomen (6.67, Accept) in overall quality but falls below the 7+ papers due to the unresolved capacity-control issue and missing statistical significance reporting. Within the 5.5–6.5 range of accepted de novo/causal biology papers, CausalNovo's consistent improvements and convergent evidence place it at the upper end — but the fixable weaknesses prevent a higher score. The score 6.0 reflects that the paper makes a solid contribution that would be strengthened by the suggested experiments, and the decision is Accept.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>
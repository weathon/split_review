Now I have all the information I need. Let me write the consolidated final review.

**Anchor Comparison Summary** (for scoring):
1. **ReNovo** (6.50, Accept): De novo sequencing with retrieval. CausalNovo has stronger empirical depth (3 baselines, ablation, cross-species) but its causal framing overclaim is a meaningful weakness absent in ReNovo.
2. **RankNovo** (5.50, Reject): Reranking framework. CausalNovo is methodologically more novel and empirically stronger, but the framing concern reduces confidence.
3. **Rep4Ex** (8.00, Accept): Rigorous causal representation theory. CausalNovo is far weaker on theoretical causal foundations but operates in a different (applied) setting.
4. **Feature Matching Intervention** (4.25, Reject): Causal representation learning with strong assumptions. CausalNovo has much better empirical validation.
5. **MADGEN** (6.00, Accept): Mass spec molecule generation. CausalNovo's evaluation is more thorough; MADGEN's predictive retrieval is weak.
6. **CrossNovo** (4.25, Reject): Knowledge distillation for de novo. CausalNovo is more novel and empirically stronger.
7. **Disentangled Microscopy** (2.50, Reject): Very weak. CausalNovo is incomparably stronger.

CausalNovo sits between 5.5 and 6.0 on this scale — genuine empirical contributions held back by a framing mismatch. Score: **5.5**.

---

## Summary

This paper introduces CausalNovo, a model-agnostic training framework for de novo peptide sequencing that improves robustness to spectral noise. The method formalizes the task via a Structural Causal Model (SCM), derives independence and sufficiency principles, and implements them through: (1) identifying noise peaks using theoretical spectra from ground-truth labels, (2) simulating causal intervention by replacing noise peaks, and (3) learning disentangled causal/non-causal representations via contrastive and cross-entropy objectives. Experiments across three datasets and three baseline models (CasaNovo, AdaNovo, π-HelixNovo) show consistent improvements at amino-acid, peptide, and PTM levels.

## Strengths

1. **Novel causality-inspired framework for de novo peptide sequencing.** The paper is the first to bring causal reasoning (SCM, independence/sufficiency principles, intervention simulation) into this problem domain (Section 3.2–3.3). While the causal formalism is not implemented with full theoretical rigor (see Weaknesses), it provides a principled motivation that goes beyond standard statistical modeling.

2. **Consistent and well-demonstrated empirical gains.** Tables 1 and 2 show CausalNovo improves over retrained baselines across all three datasets and all three base models, often by substantial margins (e.g., +12.0% amino acid precision on Seven-species for CasaNovo, +14.2% on HC-PT for AdaNovo). The gains are consistent at amino acid, peptide, and PTM levels.

3. **Thorough experimental analysis.** The paper provides: (a) ablation of each component (Tables 4, 5), confirming every design choice contributes; (b) cross-species validation on 8 species (Table 3); (c) attack/robustness analysis under varying Noise Signal Ratios (Figure 4) and perturbation thresholds (Figures 1, 3); (d) attention analysis showing CausalNovo attends to causal peaks more often (Table 7). This depth supports the claim that the framework behaves as intended.

4. **Model-agnostic framework.** The Causality Extraction Module (CEM) plugs into three different base architectures (CasaNovo, AdaNovo, π-HelixNovo) with consistent improvements, demonstrating the framework's generality.

5. **Vulnerability evaluation of existing models (Figure 1).** The paper demonstrates that three state-of-the-art baselines degrade when noise peaks are perturbed, providing quantitative evidence of spurious correlation reliance — a useful empirical finding independent of the proposed method.

## Weaknesses

### Fatal
None.

### Major
1. **Gap between causal framing and actual implementation.** The paper's language ("causal representations," "do-operator," "disentangle causal factors") implies a level of causal discovery and inference that the method does not deliver. The SCM in Figure 2A posits latent causal factor C that generates X jointly with non-causal S. In practice: (a) C is never inferred from data; instead, the ground-truth peptide label is used to compute theoretical spectra, which serve as an oracle to identify noise peaks for data augmentation; (b) the CEM learns importance scores via contrastive/sufficiency objectives, which is best described as *causality-inspired regularization* — the model learns to attend to peaks consistent with known domain knowledge (b, y, a ions from the theoretical spectrum) and to be invariant under noise replacement. This is a meaningful contribution, but the paper systematically overclaims by calling it "causal learning" or "disentanglement of causal factors." The mismatch between framing and substance undermines the paper's claimed novelty and would need to be resolved (by reframing honestly) for the work to meet the rigor expected at a top venue.

2. **Evaluation protocol limits support for causal generalization claims.** The paper follows the NovoBench protocol (in-distribution splits, using a single held-out species from the same training pool). As the authors acknowledge in the conclusion, recent methods (ContraNovo, RankNovo) use a more realistic protocol with training on large external corpora and out-of-distribution testing. Since the paper's core claim is that CausalNovo learns causal (and thus invariant) representations, evaluating on truly out-of-distribution data — different fragmentation methods (ETD, HCD), unseen instruments, or entirely novel organisms — would provide much stronger evidence. The cross-species validation (Table 3) partially addresses this but is limited to CasaNovo and shows modest gains (2.6% average peptide precision). The current evaluation is sufficient to show the framework works, but insufficient to fully support the causal generalization claims.

### Minor
3. **Missing comparison with a simple supervised weighting baseline.** A natural baseline would be training the same models with a loss that directly upweights peaks matching the theoretical spectrum (e.g., weighted cross-entropy). This would isolate whether the contrastive and purification objectives add value beyond simply amplifying the known signal peaks. Without this, it is unclear how much of the gain comes from the causal-inspired machinery versus from the supervised peak-selection signal.

4. **Training overhead (2.3×) noted but not fully contextualized.** The paper mentions the 2.3× training time increase but does not report absolute training times or discuss whether this overhead is practical for real-world use at scale.

5. **The sufficiency/purification objective (maximizing I(z_s; Y)) is introduced without analysis of potential information leakage.** Since z_s (non-causal) is also trained on the label, it could capture causal information that should belong exclusively to z_c, undermining the separation that the framework aims for. An analysis of what z_s actually encodes (e.g., by decoding z_s to predict noise patterns) would strengthen the paper.

### Trivial
None.

## Nice-to-Haves
- Test on a truly out-of-distribution scenario: train on a large corpus and test on a completely different fragmentation method or instrument.
- Analyze z_s (non-causal representation) to verify it captures noise patterns rather than leaking causal information.
- Compare against a weighted cross-entropy baseline that directly upweights theoretical-spectrum peaks.
- Report statistical significance (confidence intervals) for the main results.

## Removed Points

These points are flagged to be removed — treat them with caution:

1. **"The vulnerability analysis is circular and does not demonstrate that the model learns causal representations."** — REMOVED. The vulnerability analysis (Figures 1, 3) validates exactly what the training objective targets: invariance under noise-peak perturbation. Showing that the model succeeds at the behavior it was trained for is legitimate evidence, not circular. Combined with the NSR analysis (Figure 4), cross-species validation (Table 3), and attention analysis (Table 7), the evidence forms a coherent picture. The claim that it is "not evidence" mischaracterizes how empirical validation works in representation learning.

2. **Generic "evaluation lacks rigor" sweeps from the harsh critic** — REMOVED. The evaluation protocol concern is real but the paper acknowledges it; the unanchored criticisms about "confounders" and "proxy metrics" are speculative and not grounded in specific paper content.

3. **Strength Finder's generic strengths** ("the problem is important," "addressed a significant challenge") — REMOVED. These are generic and conflict with verified weaknesses.

## Novel Insights

The harsh critic's central observation — that CausalNovo's implementation does not discover latent causal factors from data but instead uses an external oracle (the theoretical spectrum computed from labels) to guide representation learning — is the key insight that separates what the paper actually achieves from what it claims. The method is more accurately characterized as *domain-knowledge-guided invariant representation learning* than *causal learning*. This reframing would make the paper's genuine contributions (robustness, improved accuracy, model-agnostic framework) stand on their own without inviting skepticism about overclaiming. The paper would benefit from acknowledging that the "causal factors" are implicitly defined by domain knowledge (the b, y, a ion model) rather than discovered, and that the novelty lies in how this knowledge is operationalized through the independence/sufficiency principles and intervention simulation.

## Suggestions
1. **Reframe the contribution honestly.** Replace "causal representation learning" with "causality-inspired invariant representation learning" or "domain-guided robust representation learning." Explicitly state that the SCM motivates the design but that causal factors are defined through domain knowledge (theoretical ion spectrum) rather than discovered from data.
2. **Add an OOD evaluation** using the protocol of recent methods (train on large external corpus, test on held-out fragmentation/instrument).
3. **Include a weighted-cross-entropy baseline** to quantify the value added by the contrastive and purification objectives beyond the supervised peak signal.
4. **Analyze z_s** (non-causal representation) to verify it captures noise patterns and does not leak causal information.

## Score and Decision

**Anchor comparisons:**

| Anchor | Avg Score | Comparison |
|--------|-----------|------------|
| ReNovo (uQnvYP7yX9) | 6.50 | Stronger empirical depth in CausalNovo but offset by causal overclaim |
| RankNovo (87B3zDRMjv) | 5.50 | CausalNovo has stronger novelty and more thorough evaluation |
| Rep4Ex (3cuJwmPxXj) | 8.00 | Much weaker on causal theoretical rigor, but applied setting is different |
| FMI (8GhwePP7vA) | 4.25 | CausalNovo is clearly stronger empirically |
| MADGEN (78tc3EiUrN) | 6.00 | Comparable domain; CausalNovo has more thorough evaluation |
| CrossNovo (I2ZYngkRW6) | 4.25 | CausalNovo is more novel and stronger empirically |
| Disentangled Microscopy (0iAZYF9hrl) | 2.50 | CausalNovo is incomparably stronger |

**Score: 5.5** — The paper makes genuine empirical contributions (consistent improvements, thorough analysis, model-agnostic framework) that advance the state of the art in de novo peptide sequencing. However, the systematic overclaiming of the causal framing (claiming causal discovery/disentanglement when the method is better described as invariant representation learning guided by domain knowledge) is a significant flaw that undermines the paper's methodological credibility at a top venue. With honest reframing and additional OOD evaluation, this would be a strong paper.

**Decision: Reject** — The paper should not be accepted in its current form due to the causal framing overclaim. The empirical work is solid and the framework is practically useful, but the mismatch between claims and implementation is substantial enough that acceptance would set a poor precedent for methodological rigor. The authors should reframe and resubmit.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>
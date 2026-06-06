Now I have enough to draft my review. Let me draft it and proceed to calibration.Now I'll perform calibration. Round 1 — bracketing.Round 1 bracket: **4.0–6.5**. The paper is clearly above the weak tier (real empirical contributions, clean method) but nowhere near the exceptional tier. Let me narrow within this range.Now I have clear anchors for comparison. I can finalize my review.

**Calibration Summary:**
- **VRCh74Liu9 (4.25, Rejected)**: Information-theoretic FL framework with unclear bound meaning, limited datasets. Fed-MADS is better — cleaner, more targeted, stronger empirical validation.
- **THUBTfSAS2 (5.25, Accepted)**: Active learning with novel metric, thorough theory with proven consistency, multi-architecture/dataset evaluation, statistical significance tests. Fed-MADS is somewhat weaker — single base model, no significance tests, no non-i.i.d. evaluation.

**Round 1 bracket: 4.0–6.5**
**Round 2 narrowing: 4.25–5.25**. Fed-MADS sits between these two anchors — empirically stronger than VRCh74Liu9, methodologically narrower than THUBTfSAS2. Score: **5.0**.

---

## Summary
Fed-MADS proposes a federated active learning (FAL) framework for explainable federated learning (XFL), using an Information Bottleneck (IB)-inspired derivation to justify selecting unlabeled samples where local and global models diverge most in both latent representation and prediction outputs. The method is instantiated on top of LR-XFL and evaluated on four benchmark datasets against six FAL baselines, achieving consistent improvements in model accuracy, rule accuracy, and rule fidelity.

## Strengths
- **Consistent and substantial empirical outperformance across all four datasets and all three metrics.** Table 1 and Figure 2 show Fed-MADS achieving the best model accuracy, rule accuracy, and rule fidelity on MNIST, MIMIC-II, V-Dem, and Credit-Card. Gains are sometimes large (e.g., rule accuracy ~7–9% above best competitor on V-Dem and Credit-Card, rule fidelity up to 8% above best on MIMIC-II).
- **XFL-specific design.** Unlike prior FAL methods treating the model as a black box, Fed-MADS uses the encoder's latent representation (which also serves as the XFL explainer) directly in its selection score (s₁ in Algorithm 1, Line 6), connecting data selection explicitly to explainability quality.
- **Communication and computation efficiency.** Section 3.4 shows that data selection is performed locally, incurs zero additional communication overhead, and scales linearly with unlabeled pool size O(|U_i|)—practically important for federated deployment.
- **Ablation validates the prediction-divergence term.** Figure 3 shows that β=0 (latent-representation divergence only) is already competitive, and adding prediction divergence (β>0) yields further gains in rule accuracy and rule fidelity, particularly on complex/imbalanced datasets (MIMIC-II, Credit-Card).

## Weaknesses

### Fatal
None.

### Major
- **Evaluation confined entirely to i.i.d. data, disadvantaging the strongest baselines in their intended setting.** Section 3.1 explicitly scopes to i.i.d. horizontal FL. Yet LoGo (Kim et al., 2023) and KSAS (Cao et al., 2023) were specifically designed for non-i.i.d. federated settings; their diversity mechanisms and class-weighted scoring are architecturally motivated by data heterogeneity, which is absent here. The i.i.d. setting is simultaneously optimal for Fed-MADS (a reliable global model) and removes the conditions that motivate the compared methods. Without non-i.i.d. experiments, the generality of the improvement is unestablished—it is unclear whether Fed-MADS's gains survive in the more common and challenging heterogeneous FL regime that motivated the field.
- **Single base model evaluation contradicts the "generally applicable" claim.** Every experiment uses LR-XFL as the sole model (Section 4.1). Section 3.3 and Section 5 claim Fed-MADS is "generally applicable," but since the selection score uses that model's specific encoder-decoder outputs, transferability to any other XFL architecture or standard FL classifier is never tested.

### Minor
- **IB derivation overstates its theoretical contribution.** The paper claims a minimax objective "derived from the IB principle" (Section 3.3, Eq. 13). However, arriving at Eq. (8) from Eq. (7) requires dropping two non-negative terms (H_{P,Q}(z|x) and the KL term for the label prediction), yielding an upper bound surrogate. What remains is a KL between encoder outputs plus cross-entropy between decoder outputs—an objective the paper itself notes (sentence after Eq. 9) "aligns with established practices in FL literature" (FedProx, knowledge distillation). The "minimax" framing is standard active learning intuition (select samples with highest loss) applied post-hoc. The derivation is valid as motivation, and the title correctly says "IB-Inspired," but the main text's stronger framing of formal derivation is overstated.
- **Discrete distribution assumption may be inconsistent with practice.** Section 3.3 invokes "p^e, p^d, q^e, q^d are discrete distributions, e.g., categorical over a finite codebook for z" to justify non-negativity of the dropped terms in Eq. (7)→(8). Whether LR-XFL actually enforces discrete latent representations in the experiments is never stated. If LR-XFL uses continuous encoders, the upper-bound argument is not formally justified.
- **No statistical significance testing for claimed "significant outperformance."** Several improvements over the second-best method fall within or near one standard deviation (e.g., rule fidelity on Credit-Card: Fed-MADS 97.201±6.214 vs. KSAS 96.271±6.142; MNIST rule accuracy: Fed-MADS 92.956±2.289 vs. Random 90.387±0.610). The language of "significantly outperforms" is not supported by formal tests.

### Trivial
- Figure 2 shows only model accuracy learning curves; rule accuracy and rule fidelity appear only as collapsed means in Table 1. Showing rule-quality learning curves would more directly evidence the explainability claims of the paper.

## Nice-to-Haves
- Non-i.i.d. experimental condition (e.g., Dirichlet partition) to test whether Fed-MADS's gains persist against LoGo and KSAS in their designed setting—this would substantially strengthen the scope of the contribution.
- A sharper component ablation: (a) local-entropy only, (b) prediction-divergence only (equivalent to a KSAS-style score with both local and global model outputs), (c) full Fed-MADS—to clarify whether the representation-level KL contributes beyond what prediction-level disagreement alone already captures.
- Explicit statement (and, if possible, enforcement) of whether LR-XFL uses discrete or continuous latent codes, resolving the gap between the theoretical assumption and the experimental setup.
- Early-round behavior analysis: since Section 5 acknowledges that the method relies on a well-trained global model, showing learning-curve stability specifically in the first few rounds (when global model is least reliable) would clarify the practical risk.

## Removed Points
*These points are flagged to be removed, treat them with caution.*

- **"The minimax framing is post-hoc and not game-theoretically meaningful" (Harsh Critic, separate major point):** Merged into the Minor IB weakness. The inner max over top-k subsets is combinatorial, but this is standard in pool-based AL minimax formulations, which the paper cites (Steven et al., 2008; Huang et al., 2014). Not a separate issue.
- **"Eq. (10)–(12) silently replaces expectation over z with deterministic encoder output" (Harsh Critic):** The paper explicitly states this is an approximation step (Eq. 10 → 11 → 12), citing that z is dependent on x. This is a standard marginalisation approximation and the paper is clear about it. Removed.
- **Strength: "Novel IB-theoretic derivation as a formal derivation" (Strength Finder):** Partially retained; downgraded to the derivation being IB-*motivated* rather than IB-*derived* and merged into the Minor weakness, since the strength overclaims the theoretical depth.
- **"Section 4.3 ablation shows β=0 is competitive" as a core strength (Strength Finder):** Retained in Strengths with appropriate framing.

## Novel Insights
The paper's most interesting structural observation is that using the global model as the variational distribution in an IB upper-bound formulation naturally yields a local-global disagreement score well-suited to the federated active learning setting—a conceptual bridge that, while not a tight derivation, is cleaner than ad hoc design and helps explain why global-model alignment is the right signal. Empirically, the finding that latent-representation divergence alone (β=0) is already competitive but prediction-level divergence further improves *explainability metrics* (rule accuracy, rule fidelity) more than *predictive accuracy* suggests that explainability in XFL is more sensitive to prediction alignment than to representation alignment—a practically useful insight for XFL system design.

## Suggestions
1. **Add at least one non-i.i.d. evaluation** (Dirichlet-partitioned data) to test whether the advantage over LoGo/KSAS persists in their intended setting—this is the single experiment that would most strengthen acceptance.
2. **Soften language from "derived from" to "motivated by" or "an instantiation of" the IB principle** in Section 3.3 and the abstract to match the actual nature of the approximations made.
3. **Clarify the discrete latent assumption**: state whether LR-XFL enforces discrete codes and, if not, note that the bound in Eq. (8) is invoked heuristically rather than formally.
4. **Report statistical tests** (e.g., paired t-tests or Wilcoxon) for Table 1 results, or moderate the language of "significant" outperformance.

---

## Anchor Papers Retrieved

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| ixXQF1jz8f.md | 2.50 | R1 (weak) | Far below; distributed learning method rejected for lack of rigor |
| tiKJsepvr0.md | 2.50 | R1 (weak) | Far below; DRL-based FL optimization without convincing theory |
| C7XoUdJ5ZC.md | 3.00 | R1 (weak) | Below; FL with VAE augmentation, rejected |
| cB9bAFGFAA.md | 3.40 | R1 (weak) | Below; client self-regulation FL, rejected |
| VRCh74Liu9.md | 4.25 | R1 (mid) / R2 | Fed-MADS is better: tighter scope, clearer experimental wins, more actionable algorithm |
| Nb7Akh3SjN.md | 4.25 | R1 (mid) | Below; FL with diffusion-based distribution disentanglement, limited theory |
| XeRvg7GQH4.md | 5.00 | R1 (mid) | Comparable; data condensation via IB guidance, also narrowly scoped |
| s6q6zX45F8.md | 5.33 | R1 (mid) | Slightly above; codebook-based FL with uncertainty, stronger breadth |
| THUBTfSAS2.md | 5.25 | R2 | Fed-MADS slightly weaker: LDM paper has multi-arch evaluation + significance tests |
| INqLJwqUmc.md | 5.25 | R2 | Fed-MADS comparable: IB + interpretability with overlapping but not decisive advantages either way |
| eOE2g28eX9.md | 4.75 | R2 | Fed-MADS better: more targeted method with stronger empirical results |
| sLNRvScGM2.md | 3.67 | R2 | Fed-MADS better: rejected FL client selection with mixed experimental support |
| bkdWThqE6q.md | 6.00 | R2 | Fed-MADS weaker: interpretable Transformer paper with broader evaluation and cleaner claims |
| f4gF6AIHRy.md | 8.00 | R1 (strong) | Far above: exceptional LLM pre-training data selection with theoretical guarantees |
| Fk5IzauJ7F.md | 8.00 | R1 (strong) | Far above: data-centric PLL with strong theory and comprehensive experiments |

**Round 1 bracket:** 4.0–6.5  
**Round 2 narrowing:** Fed-MADS sits between VRCh74Liu9 (4.25, below) and THUBTfSAS2/INqLJwqUmc (5.25, slightly above). The paper's empirical contributions are real and consistent but the methodological scope is narrow (i.i.d. only, one base model) and the theoretical claims are overstated. Placed at **5.0**, below the 5.25 accepted papers which had broader evaluation and stronger theoretical grounding.

## Score and Decision

**Originality:** Moderate. The core idea (local-global disagreement for FAL) has precedents (KSAS); the XFL-specific encoder integration and IB framing add novelty.  
**Importance:** Moderate. XFL is a nascent but meaningful subfield; reducing labeling cost in XFL is a real challenge.  
**Claims supported:** Partially. Empirical claims are well supported within the i.i.d./LR-XFL setting; generality claims are not.  
**Experiment soundness:** Adequate but narrow. Four datasets, six baselines, but one model and no heterogeneity evaluation.  
**Writing clarity:** Good overall; the derivation section is clear about its approximations.  
**Community value:** Limited by scope; non-i.i.d. extension would make it substantially more impactful.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>
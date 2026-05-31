Now let me perform calibration searches to determine the appropriate score.Now I have sufficient information to write the final review. Let me synthesize everything.

---

## Summary

CausalNovo is a model-agnostic training framework for *de novo* peptide sequencing that integrates a Causality Extraction Module (CEM) into existing encoder-decoder architectures. Grounded in a structural causal model (SCM), it operationalizes two principles — *independence* (causal representations remain invariant under noise-peak replacement interventions) and *sufficiency* (causal representations contain enough information for label prediction) — via contrastive and cross-entropy objectives. Extensive experiments on three datasets (Nine-species, Seven-species, HC-PT) and three Transformer-based baselines show consistent improvements of 2–14% across amino acid, peptide, and PTM metrics.

---

## Strengths

- **Large and consistent empirical improvements across baselines, datasets, and metrics.** On Nine-species, CausalNovo boosts CasaNovo/AdaNovo/π-HelixNovo amino acid precision by +2.4%/+6.3%/+2.2%; peptide-level precision by +3.5%/+6.9%/+3.4% (Table 1). On HC-PT, PTM recall improves by 15.9%/21.1%/18.0% (Table 2). The consistency across three architecturally distinct baselines and three benchmarks is the core empirical strength.

- **Generalization across varying noise-signal ratios.** Figure 4 shows CausalNovo maintains substantially higher amino acid precision across NSR values from 0 to 10, with average improvements of +10.2%–+12.2%, directly supporting the independence objective's effect.

- **Well-designed ablation studies with incremental analysis.** Table 4 confirms each component (independence loss, purification, symmetric training) contributes incrementally. Table 5 distinguishes the replace-perturbation and causality-enhancement steps, showing a simple drop operation fails while the proposed strategy works. This rigor is uncommon in plug-in framework papers.

- **Interpretable attention evidence.** Table 7 shows the fraction of predictions where all top-3 attended peaks are causal rises from 19.26% (baseline) to 32.87% (CausalNovo), with the fraction attending zero causal peaks dropping from 12.73% to 10.76%, providing transparent mechanistic corroboration.

- **Cross-species validation.** Table 3 demonstrates consistent peptide precision gains across all 8 held-out species (average +2.6%), with larger gains on harder species (Tomato: +3.1%), suggesting real generalization rather than dataset-specific overfitting.

---

## Weaknesses

### Fatal
None.

### Major

- **Circular vulnerability evaluation used as independent evidence (Sections 1, 4.4; Figures 1 and 3).** CausalNovo's training objective (Eq. 5) explicitly trains causal representations to be invariant under noise-peak replacement interventions. The vulnerability analysis at evaluation time (Section 4.4) measures exactly this property — the ability of the model to resist noise-peak perturbations of varying thresholds. It would be alarming if CausalNovo did *not* outperform baselines on this metric. The paper presents the vulnerability experiment (Figures 1 and 3) as *independent* corroborating evidence of robustness, but it is instead an in-distribution check of the training signal. The standard accuracy results in Tables 1–3 are genuinely independent evidence; the vulnerability experiment is not. This conflation affects how the reader should weight the "robustness" contribution — the claim is real but the evidence for it is weaker than presented.

- **Mixed evaluation protocol makes SOTA magnitude uncertain (Table 1).** Some method numbers (DeepNovo, InstaNovo, SearchNovo) come from NovoBench, while CausalNovo's baselines are retrained (†). The retrained †CasaNovo (0.741 AA precision on Nine-species) substantially outperforms NovoBench-reported CasaNovo (0.697), a +4.4 pp gap whose origin (training data split, preprocessing, hyperparameters) is not explained. Comparing CausalNovo+†π-HelixNovo (0.787) against SearchNovo's 0.746 (a NovoBench number) is therefore not clean: the margin may partly reflect the retrained baseline's superiority rather than the causal framework alone. The comparison is directionally valid (the retrained †baselines plus CausalNovo still beat SearchNovo), but the paper should acknowledge this.

### Minor

- **Model-agnosticism claim tested only on architecturally similar models.** All three baselines (CasaNovo, AdaNovo, π-HelixNovo) are Transformer encoder-decoder models. The claim of "model-agnostic" is reasonable in spirit, but applying CausalNovo to graph-based (GraphNovo) or non-autoregressive (π-PrimeNovo) architectures would substantiate it more concretely. The current evidence supports generalization across Transformer variants, not full model-agnosticism.

- **SCM framing partially overclaims the degree of causal discovery.** The SCM in Section 3.2 implies that CausalNovo *learns* to identify causal structure from data. However, the actual intervention (Eq. 4) hard-codes domain knowledge: non-causal peaks are identified via the tolerance threshold γ and the three ion types (b, y, a). What the paper proposes is domain-knowledge-driven noise-invariant representation learning via contrastive objectives. This is a genuine and useful contribution, but the SCM language suggests more automatic causal discovery than is actually occurring. This is a framing issue that can be corrected without changing the method.

- **No variance reporting across training seeds.** For gains in the 2–3% range on Nine-species (e.g., CasaNovo +2.4%, π-HelixNovo +2.2%), single-run results without confidence intervals or seed repetition leave open the question of whether gains are consistently reproducible. The larger gains (HC-PT: +9–14%) are less concerning on this front.

### Trivial

- The 2.3× training cost increase (noted in Section 5) is a meaningful practical concern for large-scale proteomics pipelines. The authors honestly acknowledge it, but no analysis of when or how to mitigate it is offered.

---

## Nice-to-Haves

- **Out-of-distribution robustness test.** A test on spectra from a genuinely different fragmentation method (e.g., ETD vs. HCD) or a different mass spectrometer type would more convincingly validate the causal representation claim vs. the augmentation invariance claim. The current vulnerability analysis perturbs test-set noise peaks from the same distribution seen during training.

- **When does the framework help most?** π-HelixNovo's gains are consistently smaller than AdaNovo's (e.g., +2.2% vs. +6.3% on Nine-species AA precision). An analysis of *why* the framework's value varies by base architecture — possibly related to the baseline's own implicit noise robustness — would deepen understanding and help practitioners choose when to apply CausalNovo.

- **Discussion of label noise in the causal intervention.** The theoretical spectrum x_theory is computed from training labels, which may themselves derive from database-search results carrying their own errors. If ground-truth labels are partially wrong, the causal intervention in Eq. (4) would misidentify some causal peaks as non-causal, corrupting the training signal. A brief discussion of this practical concern would strengthen the paper.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"C = charge state" in SCM (Harsh Critic, Section 3.2):** The parser describes Figure 2A as "C (charge state)" but the paper text clearly defines C as "causal factors" (Section 3.2). This is a parser artifact, not an author error. The criticism that charge state doesn't cause peptide sequence Y is not valid against the actual paper.

- **Causality enhancement distributional gap (Harsh Critic, Section 3.4.1):** The concern that inserting x_theory into training instances creates a distributional gap at test time is speculative — the model must still handle real test data without theoretical completeness, and the framework is evaluated exactly under those conditions. The ablation (Table 5) shows the enhancement helps. This is not a documented problem in the paper and is removed.

- **Vulnerability evidence from Strength Finder (Strength 1):** While Figures 1 and 3 do show the stated effects, this strength is partially undermined by the circularity weakness above. The evidence supports robustness to the specific perturbation trained against, not independent corroboration of general causal robustness.

---

## Novel Insights

The paper's most interesting methodological insight is that domain-specific label supervision can be repurposed as a *causal intervention oracle*: if you know the ground-truth label, you can compute the theoretical fragmentation spectrum and thereby partition observed peaks into causal and non-causal sets without any additional labeling effort. This bootstrap of label information into a perturbation strategy is generalizable beyond peptide sequencing to any structured prediction domain where a forward model exists (i.e., where the label can be used to generate predictions about the input). The CEM disentanglement then provides a clean way to inject this partition as a training signal without modifying the inference architecture. This modular design — intervene on training data using domain knowledge, train invariance via contrastive loss, preserve sufficiency via CE — is the paper's genuinely transferable contribution, cleaner than the SCM framing suggests.

---

## Suggestions

1. Add a brief methodological note distinguishing what the vulnerability evaluation actually measures (training-objective invariance, an in-distribution check) from what it would need to measure to validate causal representations (out-of-distribution robustness). Offer a single OOD experiment (different fragmentation mode or instrument) to close this gap.

2. Clarify in Table 1's caption that retrained (†) numbers reflect a different experimental setup from NovoBench-reported numbers, and add a sentence noting that absolute comparisons against SearchNovo and DeepNovo should be read accordingly.

3. Reframe the SCM section to be explicit that γ and the ion type selection (b, y, a) inject domain knowledge; claim that the causal *framing* motivates the design and provides theoretical guarantees (invariance, sufficiency), not that causal structure is being *discovered* from data.

4. Report results over at least 2–3 seeds for the smaller gains (≤3%) on Nine-species to establish reproducibility.

---

## Score Calibration

**Round 1 — Bracketing:**
- Low band (< 3.5): Causal structure learning papers averaging 3.0–3.25, all rejected, with fundamental limitations (strong assumptions, insufficient evaluation). CausalNovo is clearly stronger.
- Middle band (3.5–7.5): Neural Causal Graph (6.25, Accept), Counterfactual VCI (5.25, Accept), DiscoModel (4.25, Reject). CausalNovo fits in the upper portion of this band.
- High band (> 7.5): Identifiable representation learning papers (8.0), all with strong theoretical guarantees. CausalNovo lacks comparable theoretical depth.

**Round 1 bracket: 5.5–7.0**

**Round 2 — Narrowing:**
- RankNovo (87B3zDRMjv, avg 5.5, Reject): Also a de novo peptide sequencing plug-in framework (reranking). Rejected for modest improvements (+0.037 on peptide recall). CausalNovo has substantially larger gains (+2–14%), stronger theoretical motivation, more thorough ablations, and more independent validation experiments. **CausalNovo is clearly stronger than RankNovo.**
- ReNovo (uQnvYP7yX9, avg 6.5, Accept): Also de novo peptide sequencing, retrieval-based. Accepted for significant improvements and clean novelty; concerns were about data leakage and missing baselines. CausalNovo has a comparable level of empirical rigor and somewhat stronger ablation depth, but the mixed evaluation protocol and vulnerability-analysis circularity are genuine methodological issues. **CausalNovo is roughly comparable to ReNovo, perhaps slightly below on methodology transparency.**
- MADGEN (78tc3EiUrN, avg 6.0, Accept): Mass-spec de novo molecular generation, contrastive learning. Accepted as a clean contribution with clear improvements. Similar profile to CausalNovo in scope.

**Final assessment:** CausalNovo is stronger than RankNovo (5.5) and comparable to MADGEN (6.0) and close to but slightly below ReNovo (6.5). The mixed evaluation protocol and the circular vulnerability evidence are real but do not undermine the core contribution. The consistent multi-baseline, multi-dataset gains are compelling. I place it at **6.0**.

**Anchor summary:**
| Path | Score | Round | Comparison |
|---|---|---|---|
| deepreview_13k_calibration/AvXrppAS2o.md | 3.0 | R1 | Much weaker — causal prediction with strong assumptions, insufficient evaluation |
| deepreview_13k_calibration/TRHyAnInUC.md | 3.25 | R1 | Much weaker — causal discovery paper with limited novelty |
| deepreview_13k_calibration/nmvmPIi185.md | 6.25 | R1/R2 | Comparable — neural causal framework with empirical improvements |
| deepreview_13k_calibration/oeDcgVC7Xh.md | 5.25 | R1 | Slightly below CausalNovo — causal generative modeling, less comprehensive empirics |
| deepreview_13k_calibration/3cuJwmPxXj.md | 8.0 | R1 | Much stronger — theoretical identifiable representation learning |
| deepreview_13k_calibration/87B3zDRMjv.md | 5.5 | R2 | Weaker — de novo peptide reranking, modest gains, less rigorous |
| deepreview_13k_calibration/uQnvYP7yX9.md | 6.5 | R2 | Slightly above — retrieval-based de novo sequencing, clean novelty, comparable empirics |
| deepreview_13k_calibration/78tc3EiUrN.md | 6.0 | R2 | Similar — MS-based molecular generation with contrastive learning |
| deepreview_13k_calibration/fv9XU7CyN2.md | 5.75 | R2 | Slightly below — contrastive learning framework for biology, good but narrower scope |
| deepreview_13k_calibration/22ywev7zMt.md | 5.67 | R2 | Slightly below — causal SSL framework with OOD analysis, somewhat similar design |
| deepreview_13k_calibration/qsAckNdySL.md | 4.25 | R1 | Weaker — causal hierarchy modeling, rejected |
| deepreview_13k_calibration/cbFqqtJGtA.md | 4.25 | R1 | Weaker — causal differential networks for biology, rejected |

**Final score: 6.0 (Accept)**

---

**Originality:** Moderate-high. Applying causal ML to de novo peptide sequencing is novel and well-motivated. The framework design (SCM → CEM → contrastive + CE objectives) is principled, though the underlying building blocks (contrastive learning, data augmentation, disentanglement) are not new.

**Importance of research question:** High. Noise robustness in mass spectrometry-based peptide sequencing has direct implications for real-world proteomics, particularly for novel peptide discovery in challenging sample matrices.

**Claims well-supported:** Mostly. The main performance claims in Tables 1–3 are well-supported by multi-baseline, multi-dataset evidence. The "causal" framing is partially supported but also partially overclaimed given that domain knowledge is injected rather than discovered.

**Soundness of experiments:** Good with one notable concern. Ablations are thorough, cross-species validation is careful. The vulnerability analysis is methodologically circular as designed.

**Clarity of writing:** Good. The paper is well-organized, the SCM derivation is clearly laid out, and the experimental results are presented comprehensively.

**Value to the research community:** High. CausalNovo's model-agnostic design means practitioners can apply it to their preferred de novo sequencing model, and the consistent gains across diverse settings suggest practical value beyond benchmark optimization.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>
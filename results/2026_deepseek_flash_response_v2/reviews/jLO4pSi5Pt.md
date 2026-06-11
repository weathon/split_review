Now I have sufficient calibration data. Let me write the final consolidated review.

## Summary

This paper introduces L-TTA, the first method specifically designed for test-time adaptation (TTA) of vision-language models (VLMs) under long-tailed test distributions. L-TTA has three co-designed components: Synergistic Prototypes (SyPs) with Deterministic and Exclusionary Prototypes to enrich tail-class representations, Rebalancing Shortcuts (RSs) with a class re-allocation loss for learnable adaptation, and Balanced Entropy Minimization (BEM) with theoretical propositions guaranteeing a reduced optimization gap between head and tail classes. Extensive experiments across 15 datasets, three benchmark suites, multiple imbalance ratios (10/20/50), and five backbones show consistent improvements over existing VLM TTA methods, especially in macro-F1.

## Strengths

1. **Comprehensive and well-designed evaluation.** The paper benchmarks on 15 datasets across OOD, Cross-Domain, and Corruption benchmarks at three imbalance ratios, with 12+ baselines, 5 backbones, and 5 runs each. This is among the most thorough evaluations in the VLM TTA literature. Macro-F1 is appropriately reported alongside accuracy — essential for a long-tailed setting.

2. **Consistent gains, especially in macro-F1.** L-TTA outperforms prior methods by ~1-2% accuracy and ~2-3% macro-F1 on average. The macro-F1 advantage (e.g., 61.18 vs. 59.65 for the next best at Imb=10 on OOD average, Table 1) directly evidences the class-balancing capability the paper aims for. At Imb=50, the macro-F1 advantage is even clearer (59.78 vs. 58.08).

3. **Theoretical grounding for BEM.** Propositions 1 and 2 (Section 3.2) formalize why standard entropy minimization biases head classes and prove that BEM reduces this gap. This goes beyond prior TTA works (TPT, TDA, DPE, SCAP) that treat EM as a black-box loss without analyzing its interaction with long-tailed distributions.

4. **Clean ablation isolating each component.** Table 6 tests every combination of DP, EP, RS, and BEM. Removing EPs drops macro-F1 by ~3.22% (ViT-B/16), and the full system outperforms all ablated variants, confirming all three components are necessary. The EP design is explicitly contrasted with TDA's "negative cache" (line 110), establishing a clear conceptual difference: EPs use every view's prediction to update all classes, capturing inter-class associations.

5. **Favorable efficiency.** L-TTA completes in 1.45h vs. 18.30h for RLCF and 27.70h for WATT (Table 4), while achieving the highest HM scores. The design choice to keep prompts frozen and avoid gradient tracking through the backbone (Section 3.2) is the specific architectural decision behind this efficiency.

6. **Generalization across backbones.** Table 5 shows L-TTA works on ViT-L/14, ViT-H/14, SigLIP-L/16, and MetaCLIP-BigG with ~1.5% Acc / 1.8% Mac average gains, demonstrating the method does not overfit to a single architecture.

## Weaknesses

### Fatal
None.

### Major
- **Disconnect between failure-mode motivation and method design for modality-bias amplification.** The paper identifies "modality-bias amplification" as a core failure mode — applying unimodal LT-TTA methods to VLMs amplifies visual-textual mismatch (line 38) — and claims L-TTA addresses it (line 40: "❷ Mitigating Asp. II"). However, the method contains no explicit mechanism for aligning or rebalancing the visual and textual modalities: SyPs store visual embeddings (in the joint space, but they are visual), RSs attend over these visual prototypes, and BEM modifies the entropy objective on logits. None of these components operate on the text encoder, adjust text embeddings, or enforce cross-modal consistency. The claim that L-TTA mitigates modality-bias amplification is asserted without direct evidence (e.g., tracking visual-text embedding similarity over the adaptation stream). This does not invalidate the method — it clearly works — but the framing oversells the diagnostic connection between this failure mode and the design choices. The paper would be stronger by either providing evidence for modality-bias mitigation or reframing the motivation around head-class dominance only.

### Minor
- **Missing comparison against the unimodal methods used for motivation.** The paper cites SAR and DELTA (unimodal LT-TTA methods) as evidence for the modality-bias amplification failure mode (line 38, Figure 1b.2) but does not include them in any comparison table. While these methods are not designed for VLMs and the primary comparison against VLM methods is appropriate, including them with a reasonable adaptation would substantiate the diagnostic claim and sharpen the contrast with L-TTA.

- **No variance reporting despite 5 runs.** The paper states "5 runs for each experiment" but reports no standard deviations, confidence intervals, or any variance measure in any table. Given the stochasticity of TTA (random augmentations, stream ordering, prototype initialization), the significance of the reported margins over baseline improvements of ~1-2% cannot be assessed without variance information.

- **K hyper-parameter definition ambiguity.** K is defined as "hyper-class vectors q = {q_j}_{j=1}^K" (line 112), suggesting an integer count, but set to 0.3 in implementation (line 208) and ablated over [0.1, 1] (Section 4.2, Figure 4c). The paper never states that K is a fraction of the number of classes, which would resolve the inconsistency. A clear definition is needed since K controls the bottleneck of the cross-attention mechanism.

### Trivial
- **"Asp. I" and "Asp. II" are used without definition.** In line 40, the paper writes "❶ Mitigating Asp. I, II" and "❷ Mitigating Asp. II" without ever defining Asp. I (Text-induced Tail Erosion) and Asp. II (Modality-bias Amplification). While inferable from context, this should be explicit.

## Nice-to-Haves
- Direct comparison with SAR/DELTA adapted for VLMs would validate the modality-bias amplification diagnosis.
- Per-class accuracy distributions (head vs. tail, sorted) comparing L-TTA against top baselines would make the class-balancing claim more concrete.
- Tracking visual-text embedding similarity over the adaptation stream would either validate the modality-bias mitigation claim or suggest dropping it.
- Visualizing expert assignment distribution over hyper-class vectors would verify whether the CRA loss achieves its stated goal of more uniform attention.
- A brief discussion of the potential feedback loop in class prior estimation (pseudo-label → prior → BEM correction → pseudo-label) and evidence of its stability would strengthen the analysis.

## Removed Points
These points are flagged to be removed but kept for traceability; treat them with caution:
- **Table 7 formatting issues (8 values for 6 settings).** Likely a parser artifact from PDF extraction; the original table may be correctly formatted. REMOVED per formatting-artifact rule.
- **"HM metric not defined."** Table 4 caption explicitly defines HM as the harmonic mean of accuracy and macro-F1. This criticism is factually incorrect. REMOVED.
- **Weakness about class prior estimation feedback loop being unstable.** This is speculative — no evidence of actual instability is presented. WEAKENED to Nice-to-Have.
- **Various "Strengthening the Paper on Its Own Terms" proposals.** These are constructive suggestions, not weaknesses. MOVED to Nice-to-Haves.

## Novel Insights
None beyond the paper's own contributions. The key insight — that long-tailed TTA for VLMs requires enriched tail representations via multi-modal prototypes combined with learnable rebalancing and a modified entropy objective — is well-articulated by the paper itself.

## Suggestions
1. Clarify that K is a fraction of the number of classes, not an integer count, and state this explicitly in the method section.
2. Add standard deviations to the main tables.
3. Either provide direct evidence that L-TTA mitigates modality-bias amplification (e.g., visual-text embedding similarity over time) or reframe the motivation around head-class dominance only.
4. Add a per-class accuracy comparison figure (head vs. tail) between L-TTA and the best competing methods.

## Score and Decision

**Calibration Report:**

Round 1 (Bracketing):
- Low anchors (< 3.5): pdzHpQbGrn (2.50), HfJxXbXlYJ (3.00), ZaudLwn0Hm (2.50), FwkYeLovHk (3.33) — clearly weaker papers
- Middle anchors (3.5-7.5): kIP0duasBb / RLCF (6.67), yD2JMeKumt / DOTA (6.00), z7PhIgVmZU / BAT-CLIP (5.50), Rc3RP9OoEJ / InCPL (5.00) — VLM TTA papers
- High anchors (> 7.5): TPZRq4FALB / READ (8.00), WyEdX2R4er (8.00), uAFHCZRmXk (8.00), 5Ca9sSzuDp (8.00) — strong analytical/benchmarking papers

Round 1 bracket: 5.5–7.5. L-TTA is clearly stronger than BAT-CLIP (5.50, had fatal experimental flaws) and InCPL (5.00, marginal improvements), comparable to or above DOTA (6.00, methodological clarity issues flagged) and RLCF (6.67, incremental contribution but covers 3 tasks).

Round 2 (Narrowing within bracket):
- b20VK2GnSs / Concept Drift MLLM (7.00) — addresses long-tailed/VLM adaptation in pre-training, not TTA. Some experimental issues flagged. L-TTA's experiments are cleaner.
- 75PhjtbBdr / Multi-Label TTA BEM (6.25) — TTA for multi-label setting. L-TTA has more extensive evaluation and more novel problem formulation.
- GySIAKEwtZ / FeatRecon (6.50) — long-tail recognition theory + method. Not TTA or VLM-focused. Strong theory but less directly comparable.
- l6K688mhDT / Rethinking Bias of FM under LT (6.00) — analysis paper on foundation model bias under long-tailed distribution.
- b66P1u0k15 / Pareto DLTR (6.00) — long-tailed recognition with Pareto optimization.

Round 2 anchors confirm the paper sits in the 6.0–7.0 band. Compared to the closest VLM TTA anchors (RLCF at 6.67, DOTA at 6.00), L-TTA has a more novel problem formulation (first long-tailed TTA for VLMs), much more extensive evaluation (15 vs. 3-4 datasets), theoretical propositions for BEM, and cleaner component design. The main weaknesses (modality-bias claim-evidence gap, no variance reporting) are bounded and addressable.

**Final score: 6.5. Decision: Accept.**

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>
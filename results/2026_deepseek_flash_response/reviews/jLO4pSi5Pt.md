Now I have all the information I need. Let me write the final consolidated review.

## Summary

This paper addresses Long-Tailed Test-Time Adaptation (LT-TTA) for Vision-Language Models (VLMs), proposing three co-designed components: Synergistic Prototypes (SyPs) with Deterministic and Exclusionary prototypes for enriching tail-class representations, Rebalancing Shortcuts (RSs) for learnable adaptation via a class re-allocation loss, and Balanced Entropy Minimization (BEM) with a confidence-weighted penalty to counteract head-class bias in standard entropy minimization. The method is evaluated across 15 datasets under three imbalance ratios.

## Strengths

1. **Well-motivated identification of two VLM-specific failure modes.** The paper diagnoses "Text-induced Tail Erosion" and "Modality-bias Amplification" (Section 1, Figures 1–2), going beyond a naive application of unimodal LT methods to VLMs. These observations are empirically grounded (Figure 1(b) shows existing SOTAs degrade severely under long-tailed settings) and directly motivate the bi-modal designs in SyPs and BEM.

2. **Exclusionary Prototypes (EPs) update all classes from every view.** Unlike prior prototype caching methods (e.g., TDA's negative cache), EPs (Eq. 5) use the full prediction distribution to update prototypes for *every* class, not just the predicted class. This mechanism enriches tail-class representations even when tail samples are rare. The ablation (Table 6) confirms the full SyP (DP+EP)+RS (70.94/65.17) outperforms either DP+RS (69.76/64.12) or EP+RS (68.03/62.77) alone.

3. **BEM with a confidence-weighted penalty term is a principled variant of entropy minimization for LT settings.** BEM (Eq. 9) adds a penalty term $(1-\tilde{\mathbb{P}})^\beta$ that reduces the contribution of confident (head) classes and favors uncertain (tail) classes. The ablation (Table 6, Figure 4d) shows BEM adds +1.36/+0.66 to SyP+RS and β=1 outperforms both β=0.1 and β=8.

4. **Consistent gains across 15 datasets, 3 benchmarks, 4 backbones, and 3 imbalance ratios.** Tables 1–3 and 5 show L-TTA outperforms 11 baselines across nearly every setting. On the OOD Benchmark (Imb=10), L-TTA achieves OOD Average 65.97/61.18 versus the next best (DPE) at 64.50/57.57. Gains hold on larger backbones (Table 5, +1.5% Acc./+1.8% Mac. over DPE and SCAP) and the method is computationally efficient (Table 4, 1.45h on ImageNet vs. 18.30h for RLCF).

## Weaknesses

### Major

1. **Numerical anomalies in baseline results (Table 1) suggest an experimental pipeline error.** The MTA baseline reports *identical* ImageNet-A accuracy (57.15) and macro-F1 (51.98) across all three imbalance ratios (10, 20, 50). ImageNet-V2 macro-F1 also remains effectively identical (62.69/62.68/62.69). Since the test sets for different imbalance ratios are constructed by subsampling different images (exponentially decayed curves with different imbalance ratios, Section 4), the numbers *must* differ — even for a training-free method, because the evaluation set changes. This pattern is implausible and points to a data-processing or reporting error. While the anomaly only affects a baseline (not L-TTA's own numbers, which vary correctly), it undermines confidence in the experimental pipeline's correctness. The authors must explain or correct this before the results can be fully trusted.

2. **No standard deviations or confidence intervals reported.** The paper states "5 runs for each experiment" but reports only point estimates throughout all tables. For a method whose per-dataset margins over strong baselines are often 1–3% (e.g., L-TTA vs. DPE on ImageNet-A at Imb=10: 61.78 vs. 60.31; at Imb=50: 60.07 vs. 60.21), variance reporting is essential to determine whether gains reflect genuine improvement or random variation.

### Minor

3. **Hyperparameter K is inconsistently specified and ambiguously defined.** K is introduced as the number of hyper-class vectors (Section 3.2, line 112). In the main implementation (line 208), K=0.3 is used. The ablation (line 334) reports that "altering K from 0.1 to 1" and "setting K=0.2 yields the best performance" — yet the main experiments use K=0.3. The paper never clarifies that K is a fraction of the number of classes (the figure axes label "b" suggests a ratio), and the discrepancy between the ablation optimum (0.2) and the deployed value (0.3) is unexplained.

4. **Propositions 1 and 2 lack formal rigor.** The splitting criterion "with certain measurements" is vague; no explicit assumptions about the data distribution are stated, and the conditions under which the inequalities hold are not characterized. These read as intuitive claims about gradient behavior rather than proven theorems. The paper should either tighten these into rigorous statements with clear assumptions or reframe them as motivation rather than "theoretical propositions."

5. **The CRA loss formulation (Eq. 7) has ambiguous bracketing** that obscures the dot-product structure across the two terms, making it harder to verify the implementation.

### Trivial

6. The "first attempt to solve this problem" claim (abstract) could be more precisely scoped to "first to address long-tailed distributions within VLM-based TTA," since the paper itself cites prior non-i.i.d. TTA work (Boudiaf et al., 2022; Niu et al., 2023; Zhao et al., 2023a).

## Nice-to-Haves

- Evaluate L-TTA and the strongest baselines on the original (balanced) versions of the datasets to confirm the method does not degrade when the test distribution is not long-tailed.
- Report per-class accuracy breakdowns (head vs. tail) in the main paper rather than deferring to Appendix C.
- Include results on the full set of 16 corruption types (ImageNet-C style) in the main paper, not just gaussian noise.
- State the default test-stream ordering and whether it is randomized.

## Removed Points

- Criticisms about missing appendix content, missing proofs, or absent references (the parser strips these from all papers).
- Criticism about a missing closing parenthesis in Eq. 7 (likely a parser artifact, not an author error).
- Criticisms about unfair comparison — the asymmetry where present favors baselines, not the proposed method.
- Speculative "fatal" claims about implementation details that cannot be verified from the paper as written.
- Generic scope-creep demands (e.g., "the paper should address all corruption types in the main text").
- The weight decay concern (0.1 is unusual but not inherently wrong and the paper could justify it in rebuttal).

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Investigate and correct the MTA baseline numbers.** Verify that the subsampled test sets for different imbalance ratios are indeed different and re-run MTA. If the numbers were accidentally copied, regenerate them and update Table 1.

2. **Add standard deviations to all main tables.** Five runs is enough to compute meaningful error bars; report them.

3. **Clarify the K parameter.** Define K = α·C with α ∈ (0,1] and reconcile the discrepancy between the ablation finding (best at K=0.2) and the deployed value (K=0.3).

4. **Evaluate on balanced test sets** to establish whether L-TTA's LT-specific components degrade performance under balanced conditions.

---

## Score and Decision

**Calibration anchors:**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| `eXrUdcxfCw.md` — Continual TTA with prototypes | 4.80 | R2 | Weaker method and experiments; current paper is stronger |
| `lF9QXpfNHm.md` — ROSITA, open-set VLM TTA | 4.67 | R1 | Smaller scope; current paper has more comprehensive evaluation |
| `yD2JMeKumt.md` — DOTA, distributional VLM TTA | 6.00 | R2 | Comparable novelty; current paper has more extensive experiments but numerical issues reduce confidence |
| `kIP0duasBb.md` — RLCF, TTA with CLIP reward | 6.67 | R2 | Broader task coverage and cleaner experiments; current paper is weaker on experimental rigor |
| `b20VK2GnSs.md` — Concept drift in VLMs | 7.00 | R1 | Stronger theoretical grounding; current paper has suspicious baseline numbers |
| `TPZRq4FALB.md` — READ, multi-modal reliability bias TTA | 8.00 | R1 | Significantly more rigorous; current paper is clearly weaker |

**Round-1 bracket:** Between ~4.5 and ~7.0. The paper is clearly stronger than weak papers (2.5–3) and clearly weaker than outstanding papers (8).

**Round-2 narrowing:** Compared to DOTA (6.00, rejected), the current paper has a more novel problem formulation but also has a numerical anomaly in its main table that DOTA does not. Compared to RLCF (6.67, accepted), the current paper has weaker experimental rigor (no variance, suspicious baseline numbers). The most appropriate position is below the DOTA anchor, in the 5–6 range, due to the unresolved experimental concerns.

**Final score:** 5.5 — The paper addresses a genuinely underexplored and well-motivated problem with a sensible three-component method and extensive evaluation. However, the numerical anomaly in Table 1 and the absence of variance reporting prevent acceptance at the current level of rigor. These issues are potentially resolvable, but the paper as submitted does not meet the evidentiary standard for a top conference.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>
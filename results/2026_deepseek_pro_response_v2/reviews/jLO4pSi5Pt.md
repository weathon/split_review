Now I have good comparisons from Round 2. Let me finalize my analysis.

**Round 1 Bracket: 5.0 - 7.0**

Key Round 2 anchors:
- **DOTA** (`yD2JMeKumt.md`, avg 6.00, Reject): TTA for VLMs with distribution estimation. Has unclear methodology, hyperparameter concerns, and comparison fairness issues. L-TTA is stronger — more novel mechanism, broader evaluation.
- **ML-TTA with BEM** (`75PhjtbBdr.md`, avg 6.25, Accept): Multi-label TTA. Only 3 datasets, mathematical clarity issues, baseline concerns. L-TTA has broader evaluation (15 datasets) and clearer methodology.
- **Concept Drift** (`b20VK2GnSs.md`, avg 7.00, Accept): Created new dataset, strong theoretical grounding. L-TTA lacks a new dataset and has weaker theoretical support.

L-TTA sits between DOTA (6.00) and ML-TTA (6.25), comparable to or slightly above ML-TTA in empirical scope but with meaningful evaluation gaps (no LT-adapted baseline, no variance). I'll score at **6.0**.

---

## Summary
This paper identifies the problem of long-tailed (LT) class distributions in test-time adaptation (TTA) for vision-language models (VLMs), and proposes L-TTA, which combines three co-designed components: Synergistic Prototypes (dual prototype banks with Deterministic and Exclusionary variants), Rebalancing Shortcuts (learnable cross-attention with a Class Re-Allocation loss), and Balanced Entropy Minimization (a modified EM objective that penalizes confident predictions). The method is evaluated across 15 datasets under three benchmarks with synthetic LT distributions at three imbalance ratios.

## Strengths
- **Genuinely novel Exclusionary Prototypes mechanism**: The EP design (Eq. 5) updates prototypes for *all* classes using every sample's prediction distribution via a φ_c-weighted EMA, addressing the core problem that tail-class prototypes are rarely updated in streaming adaptation. Ablations (Table 6) confirm this contributes meaningfully: SyP(DP+EP)+RS improves over DP+RS by ~1% macro-F1 on both backbones.
- **Comprehensive evaluation scope**: 15 datasets across three distinct benchmarks (OOD, Cross-Domain, Corruption) at three imbalance ratios (10, 20, 50). The corruption benchmark (Table 3) reveals an important pattern: prior prototype-based methods collapse toward TPT-level performance under noise while L-TTA maintains its advantage.
- **Strong backbone scalability**: Table 5 demonstrates consistent gains across four additional backbones (ViT-L/14, ViT-H/14, SigLIP-L/16, MetaCLIP-BigG), with ~1.5% accuracy and ~1.8% macro-F1 improvement on average over the strongest baselines.
- **Computational efficiency relative to performance**: Table 4 shows L-TTA (1.45h, 1.89G memory) significantly outperforms much costlier methods (SCAP: 2.96h, WATT: 27.70h, RLCF: 18.30h) while achieving the best harmonic mean of accuracy and macro-F1.
- **Robustness to class-order shifts**: Table 7 demonstrates stable performance across varying tail-class sampling probabilities, important for practical streaming TTA.

## Weaknesses

### Fatal
None.

### Major
- **No baselines are adapted to the LT setting**: Every baseline (TPT, TDA, DPE, SCAP, etc.) is evaluated under long-tailed conditions using default hyperparameters tuned for balanced distributions. The paper claims these methods "suffer from significant degradation" (line 38) under LT, but a reader cannot determine whether L-TTA's gains come from its architectural innovations or simply from being the only method designed with LT in mind. Simple generic LT corrections (logit adjustment, balanced softmax, class-prior-weighted EM) applied to the strongest baseline could potentially close a meaningful fraction of the gap. The paper provides some justification in the methodology (lines 132-138) for why standard LT corrections may not trivially work with EM, but this is argued rather than demonstrated.

- **No variance reported despite 5-run experiments**: The paper states "We conduct 5 runs for each experiment" (Table 1 caption) but reports only means — no standard deviations, confidence intervals, or any variability measure. Several individual cells show L-TTA numerically losing to baselines: at imb=50, DPE beats L-TTA on ImageNet-A accuracy (60.21 vs. 60.07, line 199 vs. 204); at imb=20, MTA beats L-TTA on ImageNet-S macro-F1 (46.64 vs. 46.24, line 179 vs. 188); at imb=50, MTA beats L-TTA on ImageNet-V2 macro-F1 (62.69 vs. 62.38, line 195 vs. 204). Without variance estimates, readers cannot assess whether L-TTA's aggregate advantage is statistically reliable.

### Minor
- **Motivation-method disconnect on "rich classes"**: The introduction (line 38) identifies "Text-induced Tail Erosion" and *rich classes* that achieve high accuracy regardless of head/tail status due to text-embedding biases. This is an interesting diagnostic observation, but the proposed method never operationalizes it: SyPs operate on visual embeddings, RSs on prototypes derived from visual features, and BEM on prediction logits. None includes an explicit mechanism that identifies or corrects for text-embedding biases. The concept disappears after the introduction.

- **Theoretical propositions are underspecified in the main text**: Propositions 1 and 2 (lines 132-143) claim EM gradients are negative for head classes and positive for tail, and BEM reduces the gap. However, the head/tail split criterion is only described as "with certain measurements" (line 132), no distributional assumptions are stated, and the expectation's domain is unclear. The reader cannot assess whether the propositions hold under actual experimental conditions from the main text alone.

- **BEM pseudo-label feedback loop unaddressed**: The class prior π in BEM (Eq. 9) is estimated from current pseudo-labels (line 138). If the model is already biased toward head classes, the estimated prior will be biased, and the correction may target the wrong classes. This feedback loop is not discussed.

- **K hyperparameter discrepancy**: Implementation details (line 208) state K=0.3 as default, but the ablation study (line 334) reports K=0.2 as yielding best performance. This inconsistency should be resolved.

### Trivial
- The HM metric (harmonic mean of accuracy and macro-F1) in Table 4 is unconventional and not clearly motivated.
- The head/tail split at top-20% (line 206) is arbitrary and not justified.
- Non-i.i.d. TTA methods (LAME, SAR, DELTA) are discussed in related work but not compared experimentally, beyond SAR appearing in Figure 1(b.2).

## Nice-to-Haves
- Adding a fair-adaptation baseline (e.g., DPE + logit adjustment) would directly test whether L-TTA's components are necessary beyond generic LT corrections.
- Reporting per-class or per-decile accuracy in the main text would make balancing claims more concrete.
- Including at least one naturally long-tailed dataset (e.g., iNaturalist) would strengthen ecological validity.
- Operationalizing or addressing the "rich classes" diagnosis within the method would improve internal coherence.

## Removed Points
These points are flagged to be removed, treat them with caution:
- **Empty code link (line 9)**: Removed per hard rule — do not flag existence/release/availability of cited resources.
- **Stripped appendix containing proofs**: Removed per hard rule — the parser strips appendices; proofs exist in the original submission.
- **Criticism that "TTA precludes traditional LT strategies" is unjustified**: The paper provides context — TTA is a one-epoch streaming process (line 38). This is adequate justification.
- **Speculative EP calibration concern**: The harsh critic's concern that EPs could accumulate misleading signals for poorly calibrated models is speculative and not grounded in evidence from the paper. The paper even notes EPs have "considerable robustness against OOD semantics" via the φ_c weighting (line 111).
- **CRA-to-LT connection critique**: The paper explicitly argues the connection — CRA encourages uniform attention across hyper-class vectors preventing head-class dominance (lines 120-121). This is a design choice, not a flaw.

## Novel Insights
The identification of two specific failure modes (Text-induced Tail Erosion and Modality-bias Amplification) for VLM-based LT-TTA is a genuinely useful diagnostic framework. The empirical demonstration that applying unimodal LT-TTA (SAR) to a VLM backbone causes a 39.32%→17.85% accuracy collapse (Figure 1b.2) versus a much milder degradation on a pure visual backbone (38.36%→34.61%) provides concrete evidence that bi-modal approaches are necessary for this setting — a finding that could inform future work beyond this paper.

## Suggestions
- Add an LT-adapted baseline (e.g., DPE + logit adjustment) to directly test whether L-TTA's components are necessary beyond generic corrections. This is the single most important addition for a rebuttal.
- Report standard deviations across the 5 runs and discuss cases where L-TTA loses to baselines.
- Either operationalize the "rich classes" concept in the method or narrow the introduction's motivation to focus on class imbalance.
- Resolve the K hyperparameter discrepancy (stated default 0.3 vs. reported optimum 0.2).

---

**Anchor comparison summary:**

| Anchor | Score | Decision | Comparison |
|--------|-------|----------|------------|
| `pdzHpQbGrn.md` — Active TTA Prompt Learning | 2.50 | Reject | L-TTA substantially stronger in scope and novelty |
| `ZaudLwn0Hm.md` — Prototypical Few-Shot VLM | 2.50 | Reject | L-TTA substantially stronger |
| `FwkYeLovHk.md` — Weak-to-Strong CLIP | 3.33 | Reject | L-TTA substantially stronger |
| `BUDxvMRkc4.md` — BLG Long-tailed VLM | 4.67 | Reject | L-TTA stronger: broader evaluation, more novel mechanism |
| `eXrUdcxfCw.md` — Continual TTA Prototypes | 4.80 | Reject | L-TTA stronger: broader evaluation, multi-component design |
| `lF9QXpfNHm.md` — ROSITA Open-world TTA | 4.67 | Reject | L-TTA stronger: clearer methodology, broader datasets |
| `KNtcoAM5Gy.md` — BaFTA Backprop-Free TTA | 5.50 | Reject | L-TTA stronger: more novel mechanism (EPs vs. online clustering) |
| `k9NYnsC4Mq.md` — PROOF Class-Incremental VLM | 5.67 | Reject | L-TTA stronger: novel TTA formulation vs. standard CIL |
| `yD2JMeKumt.md` — DOTA Distributional TTA | 6.00 | Reject | L-TTA comparable but slightly stronger: broader eval, novel EP mechanism vs. distribution estimation |
| `75PhjtbBdr.md` — Multi-Label TTA BEM | 6.25 | Accept | L-TTA comparable: broader eval scope but similar-level weaknesses (clarity, baseline concerns) |
| `b20VK2GnSs.md` — Concept Drift MLLM | 7.00 | Accept | L-TTA weaker: lacks new dataset, weaker theoretical support |
| `TPZRq4FALB.md` — READ Reliability Bias TTA | 8.00 | Accept | L-TTA clearly weaker: READ has new benchmarks, new paradigm, stronger theory |
| `uAFHCZRmXk.md` — Modality Gap Analysis | 8.00 | Accept | Different paper type (analysis), not directly comparable |

**Round 1 bracket: 5.0–7.0.** Round 2 narrowed to 6.0–6.25. L-TTA is comparable to DOTA (6.00) and ML-TTA (6.25), sitting between them. Given the major weaknesses (no LT-adapted baseline, no variance) that meaningfully affect confidence in the claims, L-TTA lands at **6.0** — a borderline accept with evaluation gaps that should be addressed in rebuttal.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>
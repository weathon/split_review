## Summary
# Final Review Report

## Summary

This paper proposes CO-MOT, a method to improve end-to-end Transformer-based Multi-Object Tracking (e2e-MOT) via two innovations: (1) **Coopetition Label Assignment (COLA)** — allowing detection queries to also match tracked objects in intermediate decoder layers, thereby increasing positive training samples for detection queries and mitigating the "tracking terminal" problem; (2) **Shadow Sets** — augmenting each query with multiple noise-initialized copies (shadow queries) that jointly predict the same target, trained via max-cost representative selection to improve association robustness. The method is built on top of MOTR without adding external components.

The paper demonstrates strong results on **DanceTrack** (69.4% HOTA with CO-MOT+, +11.1% over MOTR) while maintaining the same FLOPs (173G) as MOTR and achieving 1.4x faster inference than MOTRv2 by eliminating the need for an external YOLOX detector. On **BDD100K**, CO-MOT achieves strong association accuracy (56.2% AssocA) but trails MOTRv2 on the primary TETA metric (52.8% vs 54.9%). On **MOT17**, CO-MOT improves over prior e2e methods but remains behind top non-end-to-end approaches.

**Strengths:** The core insight (detection queries can positively contribute to tracking) is well-motivated through diagnostic experiments (Table 1). The COLA design is clean and computationally free. Ablations are thorough, covering component contributions, hyperparameter sensitivity (initialization, N_S, Phi/Psi strategies), and attention-weight analysis.

**Key Weaknesses:** (1) The causal mechanism behind COLA's improvement is asserted via attention weights but not causally verified; (2) BDD100K results show a significant localization accuracy gap vs MOTRv2 that is not explained; (3) MOT17 underperformance is attributed to generic "Transformer data hunger" without concrete evidence; (4) Several claims are overstated ("always yields a tracking terminal," "superior performance," "significantly different"); (5) Missing variance/statistical significance across all experiments.

## Strengths
**S1. Well-motivated problem diagnosis.** The paper identifies a genuine limitation of existing e2e-MOT methods: the TALA assignment creates a scarcity of positive training samples for detection queries, leading to systematic tracking failures. The diagnostic experiments (Table 1) clearly show that MOTR's detection mAP increases by 18.1% when tracking queries are removed at inference, cleanly isolating the interference problem. This empirical motivation is compelling and well-articulated.

**S2. Computationally efficient solution.** COLA requires no additional parameters or FLOPs — it simply modifies the label assignment rules during training while keeping the inference architecture identical to MOTR. This is a practically attractive property for deployment. The shadow set adds moderate overhead (N_S copies per query during training only, with no extra cost at inference beyond the forward pass of the full query set). The efficiency comparison (Figure 4) convincingly shows that CO-MOT matches MOTRv2's HOTA while using only 38% of its FLOPs.

**S3. Thorough ablation study.** Table 3 provides a systematic evaluation of each component (COLA alone, Shadow alone, and their combination), allowing readers to assess the marginal contribution of each. The hyperparameter exploration for shadow initialization methods (I_rand, I_copy, I_noise), representative strategies (Phi/Psi combinations), and shadow count (N_S = 1-6) is thorough and useful for practitioners wanting to adopt the approach.

**S4. Attention-weight analysis provides mechanistic insight.** Figure 3 offers a first step toward understanding *why* COLA helps — detection queries co-predicting the same object receive disproportionately high attention from corresponding tracking queries, suggesting feature complementarity. While the causal direction is not fully established (see Weaknesses), this analysis adds value beyond pure performance reporting.

**S5. Consistent improvement across end-to-end baselines.** On all three benchmarks, CO-MOT improves over MOTR and other end-to-end methods, with particularly strong gains on DanceTrack (where appearance variation is high and association is the main challenge). The consistent +3-5% AssA improvement across settings suggests the method's core mechanism (improving association through augmented detection query training) is broadly effective.

## Weaknesses
**W1. Causal mechanism insufficiently validated (Major).** The paper claims that COLA improves tracking by having detection queries provide complementary features to tracking queries via self-attention. While Figure 3 shows attention weights consistent with this story, the analysis has a confound: D2T is defined as attention from a tracking query to detection queries whose predicted boxes have IoU > 0.7 with the tracking query's box. This selects pairs that already agree on identity, meaning high attention could be a *consequence* of good tracking rather than its *cause*. No causal intervention (e.g., ablating detection queries at inference, or perturbing them) is performed to establish direction. The paper should add such a controlled experiment or temper the causal language.

**W2. Overstated and unqualified performance claims (Major).** The abstract claims "superior performance without extra costs," but on BDD100K, CO-MOT (52.8% TETA) underperforms MOTRv2 (54.9% TETA) by 2.1 points, and on MOT17 it trails top non-end-to-end methods by 4-5 HOTA points. The claim "1.4x faster inference speed than MOTRv2" is largely due to removing the YOLOX detector (an architectural choice), not from COLA or Shadow. The FLOPs comparison (38% of MOTRv2) similarly conflates the proposed method's benefit with the baseline architecture difference. These claims should be bounded and attributed correctly.

**W3. Missing statistical significance across all experiments (Major).** No single experiment in the paper reports variance (standard deviation, confidence intervals) or significance tests. Given that many reported gains are small (e.g., +1.9% HOTA over MeMOTR on DanceTrack, +2.0% TETA over TETer on BDD100K), the reader cannot assess whether improvements are statistically reliable. This is a critical reproducibility gap.

**W4. Attention-weight analysis conflates correlation with causation (Major).** As noted in annotation 10 (Page 8), the D2T definition (IoU > 0.7) selects a non-random subset of detection queries, and the normalization (sum-to-1) means that if very few detection queries pass the IoU threshold, their normalized attention weight could be high by construction. The paper should report the number/fraction of queries passing the IoU threshold per decoder layer and add a causal test (e.g., masking detection queries).

**W5. BDD100K localization gap unexplained (Major).** CO-MOT's LocA (38.7%) is 10.8 points below MOTRv2 (49.5%). This is a large gap that is not discussed in the main text. The strong AssocA (56.2%) suggests the method prioritizes association over localization, but the paper does not analyze this trade-off or propose a mitigation. The abstract and conclusion should acknowledge this limitation.

**W6. MOT17 underperformance attributed to generic cause (Major).** The paper attributes MOT17's smaller gains to "the inherent data-hungry nature of the Transformer model," yet P3AFormer (also Transformer-based) achieves 81.2% MOTA on the same benchmark. This suggests the issue is specific to CO-MOT's design (e.g., fixed 300 queries, shadow set overhead, scale sensitivity) rather than Transformer architecture broadly. A more precise diagnosis is needed.

**W7. Shadow concept novelty boundaries unclear (Moderate).** The paper states the one-to-set strategy is "significantly different from the one-to-many manner" but Group-DETR, H-DETR, and CO-DETR all use multiple queries per ground truth. The specific novelties are (a) noise-based initialization and (b) max-cost representative selection. These are reasonable contributions but should be framed incrementally, not as a "significant" departure. Without a direct comparison against a one-to-many baseline (e.g., replacing shadow sets with Group-DETR-style group supervision), the relative advantage is unclear.

**W8. Conclusion introduces unsubstantiated "plugin" claim (Moderate).** The conclusion states "our method as a plugin significantly facilitates the research of end-to-end MOT," but COLA and Shadow are only evaluated on MOTR. No experiments on TrackFormer, MeMOTR, or other e2e-MOT frameworks are provided to support the plugin claim.

**W9. Motivation relies on qualitative examples without aggregate statistics (Moderate).** The "tracking terminal" phenomenon is illustrated with two video examples (Figure 1) but never quantified across the full dataset (e.g., average track length, terminal rate, fraction of videos affected). The key claim that e2e-MOT "always yields a tracking terminal" is too strong without aggregate evidence.

## Key Issues
The following issues are ranked by severity (research value + validity impact).

### Issue 1: Causal mechanism validation gap (Critical Fixability: Medium)
**Risk:** The central claim — that COLA improves tracking by enabling detection queries to provide complementary features to tracking queries — is supported only by correlational evidence (attention weights). Without a causal test (e.g., masking detection queries at inference, or measuring tracking accuracy when D2T attention is zeroed), a reviewer could argue that the observed association does not prove causation. This weakens the paper's main scientific contribution.

**Root cause:** The D2T definition (IoU > 0.7) pre-selects query pairs that already agree on identity, making high attention weight a potential consequence rather than cause of good tracking.

**Required action (Must):** Add a controlled experiment where detection queries are zeroed/masked during inference for selected decoder layers, and track the resulting HOTA/AssA change. Alternatively, conduct an intervention where noise is added to detection queries to disrupt their attention, and measure tracking degradation.

### Issue 2: Overstated performance claims without variance reporting (Critical Fixability: High)
**Risk:** The paper claims "superior performance" yet lacks variance across all experiments. Small gains (1.9% HOTA, 2.0% TETA) may not be statistically significant. The BDD100K LocA gap (38.7% vs 49.5%) is not disclosed.

**Root cause:** Training on a single seed with no repeated runs.

**Required action (Must):** Report mean ± std over at least 3 seeds for all main results (Tables 2a-c). Add significance tests (paired bootstrap or t-test) for the key comparison against MOTRv2 and MeMOTR.

### Issue 3: Unbalanced performance with unclear trade-offs (Major Fixability: Medium)
**Risk:** On BDD100K, CO-MOT sacrifices localization accuracy for association accuracy. Without analysis, readers cannot determine whether this trade-off is inherent to the method or addressable through hyperparameter tuning.

**Root cause:** COLA may broad detection queries' focus from precise localization to also covering tracked objects, reducing their localization specialization.

**Required action (Must):** Add analysis of the LocA vs AssocA trade-off. Report per-class performance. Propose a mitigation (e.g., adding a box regression loss weighted by query type).

### Issue 4: "Plugin" portability unsubstantiated (Major Fixability: Low)
**Risk:** The conclusion claims the method works as a "plugin," but only MOTR experiments are provided. This limits the contribution's generalizability claim.

**Root cause:** Experiments limited to a single baseline architecture.

**Required action (Must):** Either add experiments on TrackFormer or MeMOTR to demonstrate portability, or replace the "plugin" claim with a bounded statement about effectiveness on MOTR.

### Issue 5: Missing aggregate tracking-terminal statistics (Major Fixability: High)
**Risk:** The key motivational claim (tracking terminals) relies on two video examples. Without aggregate numbers, the prevalence of the problem is unclear.

**Root cause:** No systematic tracking-terminal analysis was conducted on the validation set.

**Required action (Must):** Add a table reporting per-dataset tracking-terminal statistics: average track length, terminal rate (%) for baseline MOTR vs CO-MOT, and fraction of videos with >1 terminal.

## Actionable Suggestions
### Suggestion 1 (Must) — Add causal validation for COLA's attention mechanism
**Problem:** The paper asserts detection queries improve tracking via attention-based feature sharing, but only correlational evidence is provided.
**Action:** Add an experiment where detection queries are masked (their outputs zeroed) during inference for specific decoder layers (e.g., layers 3-6 where D2T weight is highest). Report HOTA/AssA drop compared to full model. If the drop is significant, the causal claim is supported; if not, the attention weights may be incidental.
**Expected Benefit:** This single experiment would substantially strengthen the paper's core scientific contribution. Without it, the mechanism remains plausible but unproven.

### Suggestion 2 (Must) — Add variance reporting for all main results
**Problem:** No statistical significance is reported for any experiment.
**Action:** Re-run all main experiments (Tables 2a-c) with 3 different random seeds. Report mean ± std for all metrics. Add a paired bootstrap test for CO-MOT vs MOTRv2 on DanceTrack (the closest baseline).
**Expected Benefit:** Prevents dismissal of small gains as statistical noise; improves reproducibility.

### Suggestion 3 (Must) — Bound and recalibrate performance claims
**Problem:** Abstract and introduction overclaim "superior performance" and conflate architectural benefits with proposed-method benefits.
**Action (Abstract revision):** Replace "superior performance without extra costs" with "strong association improvement on DanceTrack and competitive results on BDD100K and MOT17, while maintaining MOTR's FLOPs." Separately acknowledge that on BDD100K, CO-MOT trails MOTRv2 on TETA primarily due to lower LocA.
**Action (FLOPs claim):** Clarify that the 38% FLOPs figure reflects the MOTR backbone (173G) vs MOTR+YOLOX (455G), not a reduction from the proposed modules. Add a fair comparison: CO-MOT vs MOTR with the same backbone (identical FLOPs) and vs MOTRv2.
**Expected Benefit:** Makes the paper more defensible to skeptical reviewers and accurately scopes the contribution.

### Suggestion 4 (Must) — Analyze and address BDD100K localization gap
**Problem:** LocA gap of 10.8 points vs MOTRv2 is unexplained.
**Action:** Report per-class LocA and AssocA on BDD100K (cars, pedestrians, etc.). Analyze whether COLA reduces detection query localization precision (since they also match tracked objects). Propose a fix: add a query-type-specific loss weight (e.g., higher $L_{1}$ weight for detection queries).
**Expected Benefit:** Turns a weakness into a contribution by revealing and addressing an important design trade-off.

### Suggestion 5 (Must) — Provide aggregate tracking-terminal statistics
**Problem:** The core motivation relies on qualitative examples.
**Action:** Compute on DanceTrack validation: (a) average continuous track length per video, (b) fraction of tracks that terminate before the last frame, (c) fraction of videos with >1 terminal, for MOTR vs CO-MOT. Show these in a table or bar chart.
**Expected Benefit:** Quantifies the problem's prevalence and the proposed method's impact on it, replacing anecdotal evidence with rigorous measurement.

### Suggestion 6 (Nice-to-have) — Compare against one-to-many baselines
**Problem:** The shadow concept's advantage over Group-DETR/H-DETR is asserted but not demonstrated.
**Action:** Add an ablation replacing shadow sets with Group-DETR-style group supervision (K groups per query) while keeping COLA fixed. Report HOTA/AssA. This directly tests whether the noise-initialization + max-cost strategy adds value beyond simply having multiple queries per object.
**Expected Benefit:** Quantifies the specific contribution of the shadow design beyond existing one-to-many approaches.

### Suggestion 7 (Nice-to-have) — Improve notations and fix typos
- Fix cost function notation in Section 3.2 (see annotation on Page 4)
- Fix "sparking" -> "strong" (Page 4)
- Fix "et al. (2020)" missing author name (Page 6)
- Fix "benefited" typo -> "benefited" or "benefitted" consistently

## Storyline Options + Writing Outlines
### Current Storyline Assessment

The current introduction has three paragraphs covering: (P1) traditional MOT pipeline → (P2) e2e-MOT + problem (tracking terminal) → (P3) COLA solution → (P4) Shadow solution → (P5) contributions. The main issues are:
- **Weak hook:** P1 is a dense citation list that does not set the stakes clearly.
- **Causal overreach:** P2 claims "always yields a tracking terminal" without aggregate evidence.
- **Buried insight:** The key insight ("detection queries exclusive but conducive") appears mid-P3 and could be more prominent.

### Recommended Storyline: Problem-Insight-Solution-Evidence

**Abstract Outline (5 sentences):**
- S1 (Problem): State the e2e-MOT challenge — detection queries receive scarce positive samples under TALA, leading to systematic tracking failures.
- S2 (Gap): Prior work uses external detectors (MOTRv2) to compensate, adding deployment overhead.
- S3 (Insight): Detection queries can positively contribute through self-attention even while remaining exclusive at the final decoder.
- S4 (Solution): COLA assigns tracked objects to detection queries in intermediate decoders; shadow sets augment queries with noise-initialized copies.
- S5 (Result + bound): CO-MOT achieves 69.4% HOTA on DanceTrack (+11.1% over MOTR) with same FLOPs; on BDD100K, AssocA improves to 56.2% with a noted LocA trade-off.

**Introduction Outline (4 paragraphs):**

**P1 — The MOT challenge and the e2e gap (Role: Big Picture + Gap)**
- S1: MOT is important for video understanding (applications: autonomous driving, surveillance), but the traditional decompose-then-associate pipeline lacks global optimization.
- S2: End-to-end Transformer methods (MOTR, TrackFormer) unify detection and tracking in one decoder, but still underperform non-end-to-end methods.
- S3: We identify a root cause: the TALA assignment creates a positive-sample scarcity for detection queries, making the model prone to tracking terminals — tracks that are permanently lost after occlusions.
- Evidence anchor: Table 1 (mAP jump when tracking queries removed).

**P2 — The COLA solution (Role: Solution — Part 1)**
- S1: Our key insight is that detection queries, though trained exclusively on newborns, can also assist tracking queries via self-attention.
- S2: COLA assigns tracked objects to detection queries in intermediate decoders (layers 1 to L-1), allowing detection queries to complement tracking query features.
- S3: The final decoder retains competitive matching to avoid duplicate trajectories.
- S4: This incurs zero additional FLOPs or parameters.
- Evidence anchor: Table 3a (row b vs a: +3.8% HOTA with COLA alone).

**P3 — The Shadow solution (Role: Solution — Part 2)**
- S1: The second bottleneck is insufficient positive samples from one-to-one matching.
- S2: We develop one-to-set matching: each query is augmented with NS shadow copies initialized with small Gaussian noise.
- S3: During training, max-cost representative selection focuses optimization on the hardest variant per set.
- S4: This improves association robustness without architectural changes.
- Evidence anchor: Table 3a (row c vs a: +2.6% HOTA with Shadow alone; row d: +5.4% combined).

**P4 — Contributions and roadmap (Role: Summary)**
- C1: COLA for cooperative label assignment in intermediate decoders.
- C2: One-to-set matching via shadow queries with max-cost training.
- C3: Empirical results demonstrating improved e2e-MOT with efficiency benefits.

### Alternative Storyline: Weakness-First (Option B)
If the paper wants to emphasize the problem over the solution, reorder as: P1 — the tracking terminal phenomenon (quantified with aggregate statistics) → P2 — TALA causes positive-sample starvation → P3 — our insight frees detection queries to help → P4 — contributions. This may be more compelling for a practitioner audience.

### Recommended Title Revision
Current: "CO-MOT: Boosting End-to-End Transformer-Based Multi-Object Tracking via Coopetition Label Assignment and Shadow Sets"
Revised: "CO-MOT: Cooperative Label Assignment and Shadow Queries for Efficient End-to-End Multi-Object Tracking"
The revised title better communicates the dual contribution and the efficiency angle.

## Priority Revision Plan
### P0 — Must Do Before Resubmission (Critical for Scientific Validity)

| Priority | Issue | Action | Effort | Expected Impact |
|----------|-------|--------|--------|-----------------|
| P0.1 | Causal mechanism unvalidated | Add detection-query masking experiment (Suggestion 1) | 2-3 GPU-days | High — converts correlation to evidence |
| P0.2 | No variance reporting | Re-run Tables 2a-c with 3 seeds each | 10-15 GPU-days | High — makes gains statistically evaluable |
| P0.3 | Overclaimed "superior performance" | Rewrite Abstract and Introduction to bound claims | 0.5 day | High — prevents reviewer rejection on overclaim |
| P0.4 | BDD100K LocA gap unexplained | Add per-class analysis and trade-off discussion | 1-2 days | Medium — addresses a major blind spot |

### P1 — Should Do (Important for Robustness)

| Priority | Issue | Action | Effort | Expected Impact |
|----------|-------|--------|--------|-----------------|
| P1.1 | Missing tracking-terminal statistics | Add aggregate analysis on DanceTrack validation | 1 day | Medium — strengthens problem motivation |
| P1.2 | Shadow vs one-to-many comparison | Add Group-DETR-style ablation | 3-5 GPU-days | Medium — clarifies novelty boundaries |
| P1.3 | Plugin claim unsubstantiated | Add TrackFormer + COLA experiment (or remove claim) | 5-7 GPU-days | Medium — supports generalizability |
| P1.4 | Conclusion over-claims | Rewrite with validated findings + bounded limitations | 0.5 day | Medium — improves closure quality |

### P2 — Nice to Have (Quality Improvement)

| Priority | Issue | Action | Effort | Expected Impact |
|----------|-------|--------|--------|-----------------|
| P2.1 | Notation/typo fixes | Clean up cost function notation, fix "sparking" | 2 hours | Low — readability |
| P2.2 | Citation format | Fix HOTA reference missing author name | 10 min | Low — professional polish |
| P2.3 | Related-work reorganization | Restructure by comparison axes (see Suggestion 7) | 1 day | Low — clarity improvement |

### Revision Strategy Roadmap

```text
ASCII Diagram — Revision Strategy Roadmap

[P0.1: Causal test missing] 
  -> [Add detection-query masking experiment] 
  -> [Stronger causal evidence for COLA mechanism]
  -> [Increases paper's core scientific contribution]

[P0.2: No variance reporting]
  -> [Re-run 3 seeds for Tables 2a-c]
  -> [Report mean±std + significance tests]
  -> [Makes gains statistically evaluable]

[P0.3: Overclaimed performance]
  -> [Rewrite Abstract: bound claims, separate architectural vs method gains]
  -> [Acknowledge BDD100K LocA gap]
  -> [Defensible narrative that survives reviewer scrutiny]

[P0.4: BDD100K trade-off unanalyzed]
  -> [Add per-class LocA/AssocA breakdown]
  -> [Identify root cause and propose mitigation]
  -> [Turns weakness into contribution]

     P0 items completed
         |
    Ready for P1 items (robustness experiments)
         |
    Ready for P2 items (polish and presentation)
```

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|---------------------|-------|---------|-------------|-----------------|-------------------|
| E1 | MOTR detection degradation under TALA | DanceTrack val, Table 1 (a-e) | mAP per decoder | mAP 42.5%→60.6% when tracking queries removed at inference | TALA causes detection bottleneck | Only mAP, no tracking-terminal rate |
| E2 | COLA + Shadow on DanceTrack | DanceTrack test, Table 2a | HOTA, DetA, AssA, MOTA, IDF1 | 65.3% HOTA (CO-MOT), 69.4% HOTA (CO-MOT+) | COLA+Shadow improves e2e-MOT | No variance, no significance test |
| E3 | Multi-class tracking on BDD100K | BDD100K val, Table 2b | TETA, LocA, AssocA, ClsA | 52.8% TETA, 56.2% AssocA | AssocA improves over TETer | LocA gap to MOTRv2 (-10.8 pts) unanalyzed |
| E4 | MOT17 benchmark | MOT17 test, Table 2c | HOTA, DetA, AssA, MOTA, IDF1 | 60.1% HOTA, 72.6% MOTA | Improves over e2e baselines | Trails non-e2e methods; cause unclear |
| E5 | Component ablation | DanceTrack val, Table 3a | HOTA, DetA, AssA, MOTA, IDF1 | COLA: +3.8% HOTA; Shadow: +2.6% HOTA; Both: +5.4% | Both components contribute independently | Confound: Shadow adds parameters |
| E6 | Hyperparameter: Phi/Psi | DanceTrack val, Table 3b | HOTA, DetA, AssA | Phi=max, Psi=min best | Max-cost selection works best | Only 5-epoch partial training; no full-test confirmation |
| E7 | Hyperparameter: initialization | DanceTrack val, Table 3c | HOTA, DetA, AssA | Inoise (Gaussian noise) best | Noise-based initialization best | Impact small (~1% HOTA difference) |
| E8 | Hyperparameter: N_S | DanceTrack val, Table 3c rows | HOTA, DetA, AssA | N_S=3 best | Moderate shadows (3) optimal | Results degrade for N_S>3; mechanism unclear |
| E9 | Attention weight analysis | DanceTrack val, Figure 3 | Attention weight % | D2T > 15% in decoders 3-6 | Detection queries attend to matching tracking queries | Correlational; IoU>0.7 confound |
| E10 | Efficiency comparison | DanceTrack test, Figure 4 | FLOPs, FPS, HOTA | 173G FLOPs, 19 FPS, 69.4% HOTA | Comparable to MOTRv2 with 38% FLOPs | FLOPs difference from YOLOX removal, not proposed modules |

### Research-Theme Gap Diagnosis

The paper provides moderate evidence for **new knowledge** (COLA design, shadow-set strategy), but the causal mechanism is unvalidated, reducing the theoretical contribution. **Reproducibility** is moderately supported by thorough Implementation Details, but lack of multi-seed variance reduces confidence. **Potential to change practice** is demonstrated through efficiency gains on DanceTrack, but MOT17 and BDD100K limitations suggest domain-specific tuning is needed.

### Proposed Research Experiments

**P0 Experiment: Causal validation via detection-query masking**
- Target Claim: COLA improves tracking because detection queries provide complementary features to tracking queries.
- Hypothesis: Masking detection queries at inference for layers 3-6 will cause a significant HOTA/AssA drop.
- Minimal Design: Compare (a) full CO-MOT, (b) CO-MOT with detection queries masked at decoder layers 3-6, (c) CO-MOT with random perturbation of detection queries. Report HOTA, AssA.
- Controls: Same backbone, same training, same N_S=3, same threshold.
- Metrics: HOTA, AssA, DetA.
- Success Criterion: (b) shows >3% HOTA drop relative to (a).
- Estimated Cost: ~2 GPU-days.
- Expected Quality Gain: Converts the attention-weight correlation into causal evidence.

**P0 Experiment: Multi-seed variance reporting**
- Target Claim: All quantitative results.
- Minimal Design: Re-run Tables 2a, 2b, 3a with 3 seeds each. Report mean ± std.
- Success Criterion: std < 0.5% HOTA for DanceTrack, < 1.0% for MOT17.
- Estimated Cost: ~12 GPU-days.
- Expected Quality Gain: Allows statistical assessment of all claims.

**P1 Experiment: Shadow vs one-to-many comparison**
- Target Claim: Shadow sets outperform standard one-to-many assignment.
- Minimal Design: Replace shadow initialization with Group-DETR-style group queries (K groups per object). Keep COLA fixed. Compare HOTA.
- Success Criterion: Shadow set achieves >=1% HOTA improvement over Group-DETR baseline.
- Estimated Cost: ~3 GPU-days.
- Expected Quality Gain: Quantifies the specific advantage of noise-initialized + max-cost shadow design.

**P1 Experiment: BDD100K localization analysis**
- Target Claim: CO-MOT's LocA gap is due to detection query specialization loss.
- Minimal Design: Report per-class LocA and AssocA. Add a variant with higher L1 loss weight for detection queries.
- Success Criterion: Narrow LocA gap to <5 points with no >1 point AssocA drop.
- Estimated Cost: ~2 GPU-days.
- Expected Quality Gain: Turns a weakness into a design insight.

### Experiment Upgrade Plan

```text
ASCII Diagram — Experiment Upgrade Plan

Stage P0 (Critical — before resubmission):
  [Causal masking experiment] -> [Multi-seed variance]
  -> [Strengthens core claims + statistical rigor]

Stage P1 (Important):
  [Shadow vs one-to-many comparison] 
  -> [BDD100K localization analysis]
  -> [Clarifies novelty + addresses blind spot]

Stage P2 (Quality):
  [Plugin portability: TrackFormer experiment]
  -> [Tracking-terminal aggregate statistics]
  -> [Broadens contribution scope + strengthens motivation]
```

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score: 5.5 / 10**

**Reasoning:** The paper identifies a genuine problem in e2e-MOT and proposes clean, computationally free solutions (COLA, Shadow sets). The diagnostic experiments (Table 1) are compelling, and the DanceTrack results (69.4% HOTA) are strong. However, the score is tempered by:

- **Causal mechanism validation gap (Severe):** The central claim that detection queries provide complementary features via attention is correlational only, with no causal experiment. This reduces the theoretical contribution.
- **Overclaimed narrative (Major):** "Superior performance" is contradicted by BDD100K (trails MOTRv2 on TETA) and by the unaddressed 10.8-point LocA gap. The FLOPs advantage conflates YOLOX removal with the proposed method.
- **Missing statistical rigor (Major):** No variance or significance tests across all experiments, making small gains (+1.9% HOTA, +2.0% TETA) hard to evaluate.
- **Moderate novelty:** COLA is an incremental modification of TALA; Shadow sets build on Group-DETR / H-DETR with noise-based initialization and max-cost selection. The specific novelties are reasonable but the paper overstates distinctiveness.

The paper is **fixable** — the core ideas are sound, and the recommended P0 experiments (causal masking, multi-seed variance, claim recalibration) would substantially strengthen it.

**Post-Revision Target: [6.5, 7.5] / 10**

If all P0 items (causal test, variance reporting, claim bounding, BDD100K analysis) are completed and the results support the current claims, the paper would achieve a score in this range. If P1 items (shadow vs one-to-many comparison, plugin portability) are also addressed, the upper end of the range is reachable.

### Evidence-Sufficiency Audit Summary

| Claim | Evidence Level | Verdict | 
|-------|---------------|---------|
| TALA causes positive-sample scarcity for detection queries | Level 2 (diagnostic mAP experiment, Table 1) | [Partially proven] — mAP evidence is strong but tracking-terminal rate is not quantified |
| COLA improves tracking via detection query feature sharing | Level 1 (attention-weight correlation, Figure 3) | [Partially proven] — correlational only; causal direction not established |
| Shadow sets improve association accuracy | Level 2 (ablation, Table 3a) | [Partially proven] — effect observed but not compared against one-to-many baselines |
| CO-MOT achieves superior performance | Level 1 (single-seed metrics) | [Partially proven] — DanceTrack strong, BDD100K/MOT17 mixed; no variance |
| Method is efficient (38% FLOPs of MOTRv2) | Level 2 (Figure 4) | [Proven] — but confounded by YOLOX removal |

### Objectivity Audit Summary

| Overclaim | Original Wording | Risk | Recommended Replacement |
|-----------|-----------------|------|-------------------------|
| Abstract | "superior performance" | Unqualified claim belied by BDD100K/MOT17 | "strong association improvement on DanceTrack and competitive results on BDD100K and MOT17" |
| Abstract | "only requires 38% FLOPs of MOTRv2" | Conflates architecture with method | "CO-MOT uses MOTR's backbone (173G FLOPs) without an external detector, achieving 1.4x faster inference than MOTRv2" |
| Introduction | "always yields a tracking terminal" | Absolute claim not supported | "frequently yields tracking terminals (see Table X for aggregate statistics)" |
| Section 3.5 | "significantly different from the one-to-many manner" | Overstates departure from prior work | "differs from one-to-many approaches in its noise-based initialization and max-cost representative selection" |
| Conclusion | "our method as a plugin" | Not validated on other architectures | "our method consistently improves MOTR; generalization to other e2e-MOT frameworks remains to be tested" |
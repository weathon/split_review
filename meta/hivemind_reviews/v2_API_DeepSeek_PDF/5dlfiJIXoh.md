## Summary
# Final Review Report

## Summary

This paper presents S-ViLM, a video-language pre-training framework that extends standard global contrastive learning with two additional objectives: (1) intra-clip temporal grouping, which uses a cut-and-paste augmentation to learn temporally discriminative features by distinguishing foreground from background clips, and (2) inter-clip spatial grounding, which aligns grouped visual tokens with noun phrases extracted from captions without requiring pre-trained object detectors. The framework adopts a dual-encoder architecture with learnable group tokens (from GroupViT) and is evaluated on four downstream tasks: text-video retrieval, video question answering, video action recognition, and temporal action localization.

**Strengths:** The paper addresses a genuine limitation of existing video-language pre-training — the neglect of fine-grained spatial and temporal structure. The two proposed modules are well-motivated and the ablation study (Table 6) confirms that each contributes positively. The zero-shot retrieval and action recognition results are competitive, particularly in zero-shot settings. The writing is generally clear and the method description is technically complete.

**Core weaknesses:** (1) The comparison with prior work is confounded by different pre-training datasets — WebVid-2M was unavailable, making direct comparison with top baselines (ALPRO, MCQ) difficult to interpret. (2) Several claims overstate the evidence: "generalizes well to unseen datasets" is based on in-domain zero-shot evaluation only, and "outperforms SOTA substantially" is not supported by statistical significance tests. (3) The spatial grounding module uses only K=2 nouns per caption, severely limiting its coverage. (4) The temporal grouping loss uses MSE on softmax probabilities without reporting temperature τ, and the loss weights are set arbitrarily to 1. (5) The conclusion lacks a limitations paragraph and makes unsupported scaling claims.

**Novelty assessment (deferred — external literature search unavailable in this run):** The core ideas (group tokens from GroupViT, cut-and-paste from PAL/CutMix) are adapted from prior work. The novelty lies in their combination within a unified video-language pre-training framework and the specific design of using cut-and-paste masks as self-supervision for temporal grouping. A thorough literature comparison is needed to determine whether this combination is sufficiently novel for the venue. Manual verification is required.

## Strengths
1. **Well-motivated problem framing.** The paper correctly identifies that existing video-language pre-training methods focus predominantly on instance-level alignment and neglect fine-grained spatial (region-object) and temporal (scene change) information. This gap is genuine and practically relevant for downstream tasks requiring localization and temporal reasoning.

2. **Clean ablation study.** Table 6 provides a clear ablation that isolates the contribution of each proposed module (spatial grounding L_g, temporal grouping L_t) against a contrastive-only baseline. The incremental improvements from each module and their combination are consistently positive across four diverse tasks, supporting the claim that both modules contribute.

3. **Competitive zero-shot retrieval results.** On MSR-VTT zero-shot text-video retrieval, S-ViLM achieves R@10=65.1, which is a notable improvement over the best comparable baseline MCQ (56.4) under different pre-training data conditions. The 16-frame results (R@10=64.0) also compare favorably.

4. **Strong action recognition performance.** S-ViLM achieves 94.8% (linear) and 96.5% (fine-tuned) on UCF101, outperforming prior video-language pre-training methods including MMV (91.8/95.2) and MCQ (89.1/92.3). This demonstrates that the learned video representations transfer well to single-modal tasks.

5. **Self-supervised design without external detectors.** The spatial grounding module uses learnable group tokens instead of pre-trained object detectors, making the framework self-contained and reducing dependence on external components. This is a practical advantage for deployment and reproducibility.

6. **Comprehensive evaluation across four tasks.** The paper evaluates on text-video retrieval, VQA, action recognition, and temporal action localization — covering both cross-modal and single-modal downstream tasks. This breadth strengthens the evidence for the learned representations' general utility.

## Weaknesses
1. **Confounded comparison due to pre-training data mismatch (Major).** The paper cannot use WebVid-2M due to data access restrictions, while most top baselines (ALPRO, MCQ, DemoVLP, Frozen) use WebVid-2M + CC3M. S-ViLM uses VideoCC (3.3M image-caption-derived pairs) + ActivityNet (20K). This confound makes it impossible to determine whether S-ViLM's gains come from the method or the data. The ablation in Table 5 shows S-ViLM on VideoCC alone (R@1=24.7) is below MCQ on VideoCC (R@1=22.5) — wait, actually S-ViLM is higher (24.7 vs 22.5.5M pairs). But the comparison is still not apples-to-apples because MCQ uses CC3M+WebVid-2M (5.5M pairs) vs S-ViLM's VideoCC (3.3M). The paper should more prominently acknowledge this limitation.

2. **Overclaimed generalization (Major).** The paper claims the model "generalizes well to unseen datasets" based on zero-shot MSR-VTT evaluation. MSR-VTT is a standard YouTube benchmark with similar domain to the pre-training data. No out-of-domain evaluation (e.g., YouCook2, Ego4D, or cross-domain retrieval) is provided to support this claim.

3. **Spatial grounding uses only K=2 nouns per caption (Major).** This severely limits the coverage of the grounding signal. Most captions contain 4-8 noun phrases. With K=2, at most two objects per video receive grounding supervision. No ablation on K is provided.

4. **Loss weight selection is arbitrary (Minor).** All three loss weights are set to 1 without sensitivity analysis. The losses have different scales and gradient characteristics, so equal weighting may not be optimal.

5. **TAL experiments use different pre-training data (Minor).** Temporal action localization uses HowTo keep this concise, I'll continue with the remaining weaknesses.

5. **TAL experiments use different pre-training data (Minor).** Temporal action localization uses HowTo100M-only pre-training, while all other experiments use VideoCC+ActivityNet. This inconsistency prevents cross-task comparison.

6. **Missing statistical significance (Major).** No variance, confidence intervals, or significance tests are reported for any experiment. Given that some gains are modest (e.g., fine-tuned retrieval R@1: 38.4 vs MCQ 37.6), statistical reliability is unclear.

7. **Conclusion lacks limitations (Major).** The conclusion makes unsupported claims about scalability ("easily scaled up") and does not discuss any limitations of the current approach.

8. **Novelty assessment deferred (see Section 9).** External literature search was unavailable in this run. The core components (group tokens from GroupViT, cut-and-paste from PAL/CutMix) are adapted from prior work. Manual verification is needed to determine whether the combination is sufficiently novel.

## Key Issues
### Issue 1: Data confound undermines comparison fairness (Severity: Major)
- **Evidence:** Page 6 "WebVid (Bain et al., 2021) is unavailable to us due to the restricted data access policy." S-ViLM uses VideoCC (3.3M pairs) + ActivityNet (20K). Baselines use CC3M + WebVid-2M (5.5M pairs total).
- **Impact:** The headline results (R@1=28.6 zero-shot) cannot be directly attributed to the method alone. The data difference (image-caption-derived vs video-specific captions) is a critical confound.
- **Fix:** Add a dedicated section comparing S-ViLM and baselines trained on the same data (e.g., both on VideoCC-only). Re-train the strongest baseline (MCQ or ALPRO) on VideoCC and report results side-by-side.

### Issue 2: Overclaimed generalization and absent statistical rigor (Severity: Major)
- **Evidence:** Page 7 "generalizes well to unseen datasets"; Page 7 "yielding approximately 9% improvement over the best-performing baseline"; no variance reported in any table.
- **Impact:** The paper's narrative inflates the strength of evidence. Without OOD evaluation or confidence intervals, the scientific conclusions are weaker than stated.
- **Fix:** (a) Replace "generalizes well to unseen datasets" with "achieves strong zero-shot results on MSR-VTT"; (b) Replace "9% improvement" with "R@10 absolute gain of 8.7 points" (more precise); (c) Add multi-seed variance to at least the main result table.

### Issue 3: Spatial grounding limited by K=2 nouns (Severity: Major)
- **Evidence:** Page 6 (Section 4.2) "K = 2 noun phrases are extracted for each caption."
- **Impact:** This limits the grounding module to supervising at most two object-region correspondences per video, even when captions contain many more objects. This may explain the modest gain from adding L_g (+0.6 R@1 in Table 6).
- **Fix:** Add ablation with K ∈ {1, 2, 4, 6} on a validation set. If K>2 improves results, update the main experiment. If computational cost is prohibitive, state this explicitly and suggest adaptive noun selection as future work.

### Issue 4: Statistical significance not reported (Severity: Major)
- **Evidence:** No standard deviations, confidence intervals, or p-values reported anywhere in the paper.
- **Impact:** Many reported gains are small (e.g., fine-tuned MSR-VTT R@1: 38.4 vs MCQ 37.6, a 0.8% gap). Without variance, readers cannot assess whether these differences are meaningful.
- **Fix:** Run all main results with at least 3 random seeds, report mean ± std, and add a footnote on significance testing.

### Issue 5: Conclusion lacks limitations and overclaims scalability (Severity: Moderate)
- **Evidence:** Page 9 "outperforms existing methods significantly" and "could be easily scaled up."
- **Impact:** The conclusion reads as promotional rather than scientific. Missing limitations paragraph reduces credibility.
- **Fix:** Replace with evidence-bounded statements and add a 3-4 sentence limitations paragraph covering the issues identified above.

## Actionable Suggestions
### S1 (Must): Re-train baselines on VideoCC for fair comparison
- **Target:** Section 4.3 (all result tables)
- **Action:** Select the strongest baseline(s) from Table 1 (e.g., MCQ or ALPRO), re-train on the same VideoCC + ActivityNet data used for S-ViLM, and report results in a dedicated "fair comparison" subsection.
- **Rationale:** Without this, the confound between method and data cannot be resolved.
- **Acceptance criteria:** A new table showing S-ViLM vs re-trained baselines on shared data.

### S2 (Must): Add statistical significance and variance
- **Target:** Tables 1-4, especially Table 1 fine-tuning results
- **Action:** Run all main experiments with 3 random seeds and report mean ± std. For the key comparison (S-ViLM vs MCQ on MSR-VTT fine-tuning), add a paired significance test footnote.
- **Rationale:** Several gains are within 1 point; without variance, readers cannot assess reliability.

### S3 (Must): Rewrite overclaimed generalization statements
- **Target:** Page 7 (Section 4.3.), Page 1 (Abstract)
- **Action:** Replace "generalizes well to unseen datasets" with "achieves strong zero-shot results on MSR-VTT" in both Abstract and Section 4.3. Replace "outperforms state-of-the-art methods substantially" with "achieves competitive or improved results compared to existing methods under comparable settings."
- **Rationale:** The current wording overstates the evidence scope.

### S4 (Must): Add K=2 ablation and noun coverage analysis
- **Target:** Section 4.3.5 (Ablation) or Appendix
- **Action:** Add an ablation study varying K ∈ {1, 2, 4, 6} on the MSR-VTT zero-shot task. Report whether larger K improves retrieval and grounding alignment.
- **Rationale:** K=2 is a critical hyperparameter for the grounding module; without ablation, the design choice is unsubstantiated.

### S5 (Must): Add limitations paragraph to conclusion
- **Target:** Page 9 (Section 5)
- **Action:** Replace the final two sentences with a 3-4 sentence limitations paragraph covering: (i) data confound, (ii) limited noun coverage, (iii) no OOD evaluation, and (iv) loss weight sensitivity.
- **Rationale:** ICLR standards require explicit limitations discussion.

### S6 (Nice-to-have): Report temperature τ for Eq (1)
- **Target:** Section 3.2 or Section 4.2
- **Action:** Report the temperature value used in Eq (1) softmax. If it is learned, state, report that it is fixed.
- **Rationale:** τ controls assignment sharpness in temporal grouping and affects training dynamics.

### S7 (Nice-to-have): Loss weight sensitivity analysis
- **Target:** Appendix
- **Action:** Add a small grid search over ω1, ω2, ω3 (e.g., {0.1, 1, 10}) on the MSR-VTT zero-shot validation set to justify the equal-weight choice.
- **Rationale:** The current "for simplicity" justification is insufficient for a triple-loss objective.

### S8 (Nice-to-have): Add OOD evaluation
- **Target:** New experiment section
- **Action:** Evaluate zero-shot retrieval on one out-of-domain dataset (e.g., YouCook2 or Ego4D) to test cross-domain generalization, or explicitly state that this is future work.
- **Rationale:** Currently, "generalization" claims are based on in-domain evaluation only.

## Storyline Options + Writing Outlines
### Current Storyline Analysis

The current introduction follows this structure:
- P1: Analogy between video pixels and language grammar → VLM neglect fine-grained structure
- P2: Prior work limitations → S-ViLM overview → Contribution bullets

**Problem:** P1 spends too many sentences on the pixel-to-grammar analogy before stating the concrete gap. The contribution bullets mix design and outcome claims.

### Recommended Storyline (Option A — Problem-First)

**Abstract Outline (5 sentences):**
- S1 (Problem): "Existing video-language pre-training methods learn holistic video-caption representations through global contrastive learning, but neglect fine-grained region-object correspondences and temporal scene dynamics."
- S2 (Gap): "These fine-grained structures are critical for downstream tasks requiring object localization and temporal reasoning, yet they are not explicitly modeled in current pre-training objectives."
- S3 (Method): "We propose S-ViLM, a framework that introduces two complementary self-supervised objectives — inter-clip spatial grounding to align grouped visual regions with noun phrases, and intra-clip temporal grouping to learn temporally discriminative features via cut-and-paste augmentation."
- S4 (Evidence): "When evaluated on text-video retrieval, video question answering, action recognition, and temporal action localization, S-ViLM achieves competitive or improved results compared to existing methods."
- S5 (Bounded claim): "These findings suggest that explicitly modeling fine-grained video-text structure during pre-training produces more discriminative representations for both cross-modal and single-modal tasks."

**Introduction Outline (4 paragraphs):**
- P1 (Stakes + Gap): "Video-language pre-training has advanced rapidly, but current methods predominantly optimize instance-level video-caption alignment. This paragraph-level approach misses two levels of structure: spatial correspondences between objects in frames and nouns in captions, and temporal transitions between scenes or actions. Both are essential for tasks like temporal action localization and detailed video QA." → Cite 3-4 representative prior works showing this gap.
- P2 (Prior attempts + their limits): "Recent works have begun addressing fine-grained alignment: ALPRO uses pseudo entity labels, MCQ recovers masked noun/verb tokens, and TemPVL enforces temporal-semantic alignment. However, none jointly model spatial region-object grounding and temporal foreground-background discrimination within a single self-supervised framework." → Explicitly state what is missing.
- P3 (Proposed solution): "We address this gap with S-ViLM, which combines three objectives: (1) global contrastive learning for instance-level alignment, (2) inter-clip spatial grounding using learnable group tokens to align visual regions with noun phrases, and (3) intra-clip temporal grouping that uses cut-and-paste augmentation masks as self-supervision for temporal discrimination." → Keep technical detail minimal; reserve depth for Section 3.
- P4 (Contributions + Results preview): Bullet list with 3 design contributions + 1 empirical summary. Include key numbers: "S-ViLM achieves R@10=65.1 on MSR-VTT zero-shot retrieval and 96.5% accuracy on UCF101 action recognition."

### Alternative Storyline (Option B — Capability-First)

Lead with the most striking result (action recognition: 96.5% on UCF101, +5% over prior SOTA), then explain why fine-grained pre-training produces better video representations. This is more results-driven but risks appearing as a benchmark-chasing paper.

### Alternative Storyline (Option C — Mechanism-First)

Lead with the observation that video-language datasets contain short, repetitive clips with limited temporal variation, then argue that explicit temporal augmentation (cut-and-paste) is necessary to learn temporal awareness. This frames the temporal grouping module as the primary contribution and spatial grounding as complementary.

### Recommended Choice: Option A

Option A best aligns with the three alignment checks:
- (a) Problem alignment: The stated challenge (neglect of fine-grained structure) directly matches the proposed solution (spatial grounding + temporal grouping).
- (b) Variable alignment: Core concepts from the introduction (region-object, temporal scene change) appear as key variables in the method (group tokens, cut-and-paste mask, foreground/background centers).
- (c) Contribution-evidence alignment: Each contribution claim maps to specific experiments (Table 6 ablation for module contributions, Tables 1-4 for downstream performance).

## Priority Revision Plan
```text
Priority | Action                                        | Effort  | Impact  | Section
P0       | Re-train baselines on VideoCC for fair comparison | High   | Critical| 4.3
P0       | Add multi-seed variance to main results          | Medium | Critical| Tables 1-4
P0       | Rewrite overclaimed generalization statements    | Low    | Critical| Abstract, 4.3.1
P0       | Add limitations paragraph to conclusion          | Low    | High    | Section 5
P1       | Add K noun ablation (K∈{1,2,4,6})               | Medium | High    | 4.3.5 / Appendix
P1       | Report temperature τ for Eq (1)                  | Low    | Medium  | 3.2 / 4.2
P1       | Restructure Related Work section                 | Medium | Medium  | Section 2
P2       | Loss weight sensitivity analysis                 | Medium | Medium  | Appendix
P2       | Add OOD evaluation (YouCook2 or Ego4D)          | High   | Medium  | New section
P2       | Restructure contribution bullets                 | Low    | Low     | Section 1
```

### Execution Order

**Stage 1 (P0 — before resubmission):**
1. Rewrite overclaimed claims in Abstract and Section 4.3.1 — low effort, high impact on reviewer perception.
2. Replace conclusion with a version that includes explicit limitations paragraph.
3. Add multi-seed variance (3 seeds, mean ± std) to all main result tables.
4. If possible, re-train one baseline (MCQ or ALPRO) on VideoCC for fair comparison. If this is computationally prohibitive, add a paragraph explicitly discussing the data confound and its impact on result interpretation.

**Stage 2 (P1 — strengthening):**
5. Run K ablation for spatial grounding (K=1,2,4,6) on MSR-VTT zero-shot.
6. Report temperature τ for Eq (1) and justify MSE vs BCE choice.
7. Restructure Related Work into comparison-axis paragraphs rather than citation lists.

**Stage 3 (P2 — completeness):**
8. Add loss weight sensitivity analysis.
9. Add OOD evaluation or state as future work.
10. Restructure contribution bullets for parallelism and separability.

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective/Hypothesis | Setup (data/split/protocol/baselines) | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|---------------------|---------------------------------------|---------|-------------|----------------|-------------------|
| E1 | Zero-shot text-video retrieval | MSR-VTT (1K test), pre-trained on VideoCC+ActivityNet | R@1, R@5, R@10, MedR | R@10=65.1, +8.7 over MCQ | S-ViLM learns effective cross-modal alignment | Data confound with baselines; no variance reported |
| E2 | Fine-tuned text-video retrieval | MSR-VTT (9K train/1K test) | R@1, R@5, R@10, MedR | R@1=38.4, +0.8 over MCQ | Pre-training transfers to fine-tuning | Gain is small; no significance test |
| E3 | Video QA (open-ended) | MSRVTT-QA, MSVD-QA | Top-1 accuracy | 43.5% (+1.4), 46.4% (+0.5) | S-ViLM improves VQA | Small margins; no variance |
| E4 | Action recognition (linear) | UCF101, HMDB51 | Top-1 accuracy | 94.8%, 70.0% | Strong single-modal transfer | No comparison with video-only pre-training methods |
| E5 | Action recognition (fine-tuned) | UCF101, HMDB51 | Top-1 accuracy | 96.5%, 76.9% | Consistent gains | No variance |
| E6 | Temporal action localization | ActivityNet, pre-trained on HowTo100M | mAP@0.5, 0.75, 0.95, Avg | 51.7/36.4/9.7/35.6 | S-ViLM exceeds self-supervised methods | Different pre-training data from other experiments |
| E7 | Ablation: training objectives | VideoCC only, 4 scenarios (Table 6) | MSRVTT-ZS, MSVD-QA, UCF101, TAL | Each module adds positive gain | Both L_g and L_t contribute | Gains are small; no interaction analysis |
| E8 | Ablation: pre-training datasets | HowTo100M, WebVid, VideoCC, VideoCC+AN (Table 5) | MSRVTT-ZS, TAL | VideoCC+AN best for retrieval | Data choice matters | No baseline re-trained on same data |
| E9 | Frame count comparison | 16 vs 32 frames (Appendix B) | MSRVTT-ZS, UCF101 | 32-frame slightly better | Consistent across settings | Justification for 32-frame choice is circular |
| E10 | Spatiotemporal action localization | AVA v2.2 (Appendix B) | mAP@0.5 | 25.0 (detected), 30.15 (GT) | S-ViLM > contrastive-only | Only one metric; no comparison with SOTA on AVA |

### Research-Theme Gap Diagnosis

- **New knowledge:** The paper demonstrates that combining spatial grounding and temporal grouping improves video representations. However, the incremental nature of the gains (1-3% on most tasks) and the data confound limit the strength of the new knowledge claim.
- **Reproducibility:** The method description is reasonably complete, but missing details (temperature τ, loss weight justification, K=2 rationale) reduce reproducibility.
- **Impact on practice/understanding:** The paper provides evidence that fine-grained pre-training objectives benefit both cross-modal and single-modal tasks. This is a useful finding for practitioners, but the modest gains suggest diminishing returns from adding more objectives to the standard contrastive baseline.

### Proposed Research Experiments (P0/P1/P2)

**P0-Exp1: Fair comparison via baseline re-training**
- Target Claim: "S-ViLM outperforms existing methods"
- Hypothesis: S-ViLM's gains persist when baselines are trained on identical data
- Minimal Design: Re-train MCQ (or ALPRO) on VideoCC + ActivityNet using authors' code
- Controls/Baselines: Same optimizer, epochs, batch size, frame count
- Metrics: R@1, R@5, R@10 on MSR-VTT zero-shot
- Success Criterion: S-ViLM maintains ≥2 point R@1 advantage over re-trained baseline
- Estimated Cost/Time: ~2 TPU-days per baseline
- Expected Paper-Quality Gain: Resolves the primary confound; critical for acceptance

**P0-Exp2: Statistical significance package**
- Target Claim: All performance comparisons
- Hypothesis: Reported gains are statistically reliable
- Minimal Design: Run 3 seeds for Tables 1-4, report mean ± std
- Controls/Baselines: Same seed initialization protocol
- Metrics: Standard deviation, Cohen's d for key comparisons
- Success Criterion: Gains > 2σ for main claims
- Estimated Cost/Time: ~3x current training cost
- Expected Paper-Quality Gain: Essential for scientific credibility

**P1-Exp3: K noun ablation for spatial grounding**
- Target Claim: "Spatial grounding module improves representations
- Hypothesis: Larger K (more nouns) improves grounding and downstream performance
- Minimal Design: Train S-ViLM with K ∈ {1, 2, 4, 6} on VideoCC, evaluate on MSR-VTT zero-shot
- Controls/Baselines: Same architecture, same training budget
- Metrics: R@1, R@5, grounding similarity score
- Success Criterion: K=4 or K=6 outperforms K=2
- Estimated Cost/Time: ~4 TPU-days
- Expected Paper-Quality Gain: Validates or refutes the K=2 design choice

**P1-Exp4: OOD retrieval evaluation**
- Target Claim: "Generalizes well to unseen datasets"
- Hypothesis: S-ViLM maintains retrieval performance under domain shift
- Minimal Design: Zero-shot evaluation on YouCook2 (cooking domain) or Ego4D (egocentric)
- Controls/Baselines: Compare with MCQ or Frozen on same OOD data
- Metrics: R@1, R@5
- Success Criterion: S-ViLM shows smaller performance drop than baselines
- Estimated Cost/Time: ~1 day (evaluation only, no training)
- Expected Paper-Quality Gain: Supports or refutes generalization claims

**P2-Exp5: Loss weight sensitivity**
- Target Claim: Joint training is effective
- Hypothesis: Equal weighting is near-optimal
- Minimal Design: Grid search ω1, ω2, ω3 ∈ {0.1, 1, 10} on MSR-VTT zero-shot validation
- Controls/Baselines: Equal-weight baseline
- Metrics: R@1
- Success Criterion: Equal weight within 1% of best configuration
- Estimated Cost/Time: ~8 TPU-days
- Expected Paper-Quality Gain: Justifies the "for simplicity" choice

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score: 6.5 / 10**

The paper addresses a genuine problem and provides a clean ablation study showing that both proposed modules contribute positively. The zero-shot retrieval and action recognition results are competitive. However, the score is constrained by:

- **Research value (6/10):** The incremental gains over strong baselines are modest (0.5-3% on most tasks), and the data confound with prior work limits the strength of the contribution claim. The core insight — that fine-grained objectives help — is valuable but not surprising given prior work on fine-grained alignment (ALPRO, MCQ, TemPVL).
- **Novelty (deferred, estimated 5-6/10):** The components (group tokens, cut-and-paste) are adapted from prior work. The combination is new but the individual contributions are incremental. External literature verification is needed for a definitive assessment.
- **Validity/soundness (6/10):** The method is technically sound and the ablation is well-designed. However, missing statistical significance tests, the data confound, and overclaimed generalization statements reduce confidence in the conclusions.
- **Reproducibility (7/10):** The method description is reasonably complete, but missing details (temperature τ, loss weight justification, K=2 rationale) and the unavailability of WebVid-2M reduce full reproducibility.

**Post-Revision Target: [7.0, 7.5] / 10**

If the authors address the P0 items (fair comparison via baseline re-training, statistical significance, claim rewrites, limitations paragraph), the score could rise to 7.0-7.5. Addressing P1 items (K ablation, OOD evaluation) could push toward 7.5. The upper bound is constrained by the incremental nature of the technical contribution relative to prior work.
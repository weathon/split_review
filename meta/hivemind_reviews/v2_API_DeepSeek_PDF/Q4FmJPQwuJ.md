## Summary
# Final Review Report

## Summary

This paper presents CrossTVR, a multi-grained re-ranker for text-video retrieval (TVR). The core idea is to introduce separate cross-attention modules at two levels — frame-level spatial attention for capturing fine-grained visual details (small objects, spatial layout) and video-level temporal attention for modeling motion and event dynamics — on top of an existing cosine-similarity retrieval pipeline. The vision encoder is frozen during re-ranker training, enabling scalability to large pre-trained models such as ViT-G with reduced memory cost.

The paper is technically sound in its architectural design and demonstrates consistent improvements across five benchmarks (MSRVTT, VATEX, LSMDC, ActivityNet, DiDeMo) when applied on top of TS2Net and CLIP-ViP. The frozen-encoder strategy and its associated memory savings (91% reduction vs. end-to-end ViT-G finetuning) are a practical strength.

However, the manuscript has several major weaknesses that need to be addressed before acceptance: (1) no variance/statistical significance is reported for any experimental result, making small-margin gains (0.2–0.4% in ablations) unverifiable; (2) the loss function uses non-standard notation and underspecifies the hard negative sampling procedure; (3) the scalability comparison (Table 9) is confounded by different GPU counts and batch sizes; (4) the narrative arc of the introduction and related work sections is dense and lacks clear differentiation from prior hybrid methods; and (5) novelty claims are expressed in vague terms with limited explicit differentiation from the strongest baselines. All novelty/comparison conclusions are deferred to manual verification due to Retrieval-Disabled Mode in this run.

## Strengths
1. **Architectural clarity of multi-grained attention.** The separation of frame-level and video-level cross attention with parameter sharing is a clean design that directly addresses the information loss problem in prior cross-attention TVR methods. The intuition that spatial details are best captured per-frame while temporal dynamics require cross-frame aggregation is well-motivated.

2. **Frozen-encoder practical efficiency.** By freezing the vision backbone and training only the cross-attention header, the method achieves substantial memory savings (91% reduction vs. end-to-end ViT-G finetuning in the reported setting). This pragmatic design choice makes scaling to larger encoders (ViT-G) feasible on a single GPU, which is a genuine practical contribution.

3. **Broad empirical validation.** The method is evaluated on five diverse benchmarks (MSRVTT, VATEX, LSMDC, ActivityNet, DiDeMo) spanning different video lengths, domains, and annotation styles. The consistent pattern of improvement — applying CrossTVR improves R@1 across all tested base methods and datasets — strengthens the claim of generality.

4. **Ablation completeness.** The ablation study (Tables 6-7) systematically isolates each design choice (video-level attention, frame-level attention, parameter sharing, hard negative mining) and compares against alternative design strategies (average pooling, CLS token, sum ensemble). This level of ablation is informative and helps validate the hierarchical multi-grained design.

5. **Qualitative validation.** The Grad-CAM visualizations (Figure 4) provide interpretability evidence that the frame-level and video-level attention modules capture distinct types of information (spatial objects vs. temporal actions), supporting the multi-grained design rationale.

## Weaknesses
1. **Missing statistical significance.** No experimental result in the paper includes variance, confidence intervals, or significance tests. Given that many improvements are small (0.2–1.4% in R@1 for several configurations), the reader cannot determine whether gains are systematic or due to random seed variation. This is the most critical weakness.

2. **Loss function notation and hard negative specification.** The video-text matching loss in Eq. (7) uses expectation notation ($\mathbb{E}$) in a non-standard way for minibatch training, and the hard negative sampling procedure is underspecified — it is unclear whether the sampled hard negatives replace all batch negatives or are treated as additional pairs.

3. **Scalability comparison confounds.** Table 9 compares CrossTVR (1 GPU, batch size 128) against CLIP4Clip (8 GPUs, batch size 48) without controlling for total compute (400 vs. 21 GPU-hours). The "91% memory reduction" and "58% training time decrease" are partly driven by different training configurations rather than architecture alone.

4. **Contribution framing is too broad.** The three listed contributions (Page 2) are described in generic terms ("comprehensive interaction", "widely applied", "scalability to larger models") without concrete differentiation from prior work. The third contribution contains a typo ("visual coder" → "visual encoder").

5. **Conclusion is incomplete.** The conclusion is only 4 sentences long, states "superiority" without qualification, mentions only one narrow limitation (retriever performance), and adds a generic broader-impact note about surveillance that is disconnected from the technical content. Important limitations — two-stage pipeline dependency, training cost overhead, no OOD evaluation — are omitted.

6. **Related work reads as a flat list.** The related work paragraphs cite 15+ papers in a single stream of consciousness without clear comparative axes or organized sub-sections. The differentiation between CrossTVR and specific prior hybrid methods (Miech et al., OmniVL) is not explicit.

7. **Inconsistent notation in equations.** The Frame Text Attention section uses $X_{\text{frame}}(t)$ in the equation but $X_{\text{spatial}}(t)$ in the text (Page 5), causing confusion. The token selection criteria ("first N tokens" vs. $N_Q$ queries) is ambiguous.

8. **Ablation gains are not validated.** Parameter sharing (0.2% gain) and hard negative mining (0.2% gain) contribute margins that are likely within noise without repeated experiments. The sum-ensemble baseline (Frame Video Sum: 49.1%) already captures most of the gain (CrossTVR: 50.0%), raising questions about whether the hierarchical design adds value beyond logit averaging.

9. **Novelty cannot be fully assessed without external retrieval.** Due to Retrieval-Disabled Mode in this run, all novelty and comparison claims are deferred to manual verification. The paper claims "state-of-the-art across all benchmarks" but some configurations (e.g., LSMDC with higher MnR) show mixed results.

10. **Informal language.** Words like "obviously" (Page 2) and phrases like "we contend that our cross attention module holds the potential to serve as a potent performance-boosting component" (Page 9) are inappropriate for academic writing.

## Key Issues
### Issue 1 (Critical): No statistical significance for any experimental result
**Severity:** Critical | **Fixability:** Full | **Confidence:** High

All Tables 1-7 report single-point estimates without variance, confidence intervals, or significance tests. The ablation gains of 0.2% (parameter sharing) and 0.2% (hard negative mining) are within typical seed noise for retrieval tasks. Even the main gains (1.4–8% R@1 improvements) could vary substantially across seeds.

**Fix:** Report mean ± std over ≥3 seeds for all tables. Add paired bootstrap significance tests (p < 0.05) for the main comparisons. This is a must-fix before acceptance.

### Issue 2 (Major): Loss function hard negative sampling is underspecified
**Severity:** Major | **Fixability:** Full | **Confidence:** High

Eq. (7) uses $\mathbb{E}$ notation inappropriately for a minibatch loss, and the hard negative sampling description does not specify how the sampled negative(s) interact with the cross-entropy loss — are they additional pairs or replacements? Without this, the training procedure cannot be independently reproduced.

**Fix:** Replace Eq. (7) with a standard cross-entropy loss formulation over the minibatch (see annotation on Page 6). Clarify whether hard negatives replace batch negatives or are supplementary.

### Issue 3 (Major): Scalability comparison is confounded
**Severity:** Major | **Fixability:** Partial | **Confidence:** High

Table 9 compares CrossTVR (1 GPU, batch 128, TS2Net base) against CLIP4Clip (8 GPUs, batch 48, end-to-end) without controlling for total GPU-hours or base method strength. The 91% memory reduction is partly an artifact of different training configurations.

**Fix:** Add a controlled comparison where CrossTVR is applied to CLIP4Clip (not TS2Net) with ViT-G and the same number of GPUs. Or convert Table 9 to report per-GPU-hour cost and specify the base method performance gap.

### Issue 4 (Major): Notation inconsistency in Frame Text Attention equations
**Severity:** Major | **Fixability:** Full | **Confidence:** High

The text uses $X_{\text{spatial}}(t)$ while the equation defines $X_{\text{frame}}(t)$. The token selection criteria is ambiguous (first N tokens vs. $N_Q$ queries). Missing tensor dimensions.

**Fix:** Use consistent naming. Clarify that only the $N_Q$ query tokens (not the concatenated text tokens) are averaged. Specify the output dimension explicitly.

### Issue 5 (Major): Ablation study lacks statistical validation
**Severity:** Major | **Fixability:** Full | **Confidence:** High

Incremental gains of 0.2% (parameter sharing, hard negative mining) are reported without variance. The sum-ensemble baseline (Frame Video Sum) achieves 49.1% vs. CrossTVR's hierarchical 50.0%, suggesting the hierarchical design adds only 0.9% over a simple logit sum.

**Fix:** Report multi-seed variance for the ablation rows. Add an analysis paragraph explaining whether the hierarchical design is justified vs. the simpler sum ensemble, given the added complexity.

### Issue 6 (Major): Conclusion is too brief and omits key limitations
**Severity:** Major | **Fixability:** Full | **Confidence:** High

The 4-sentence conclusion lacks structured findings, bounded claims, and a complete limitation discussion. The only stated limitation (retriever dependence) omits training cost, two-stage overhead, and lack of OOD evaluation.

**Fix:** Restructure conclusion into: (1) validated findings with bounded claims, (2) specific limitations (at least 3), (3) prioritized next steps. See annotation on Page 9 for a revised version.

## Actionable Suggestions
### S1: Add statistical significance reporting (Must, P0)
Add mean ± std over 3 random seeds to all main tables (Tables 1-7). For the primary comparisons (TS2-Net + Ours vs. TS2-Net), include a paired bootstrap significance test (p < 0.05). Report in a footnote: "All main results are averaged over three seeds. Bold indicates p < 0.05 under paired bootstrap against the base method."

### S2: Clarify the training loss and hard negative procedure (Must, P0)
Replace Eq. (7) with:
$$\mathcal{L}_{\text{tvm}} = -\frac{1}{|\mathcal{D}|} \sum_{(X,V)\in\mathcal{D}} \bigl[ y \log p(X,V) + (1-y)\log(1-p(X,V)) \bigr]$$
where $\mathcal{D}$ includes (a) all positive pairs in the batch, (b) all standard negative pairs, and (c) one hard negative text per video and one hard negative video per text sampled from the contrastive similarity distribution. Clarify whether hard negatives replace or supplement the standard negatives.

### S3: Control scalability comparison fairly (Must, P1)
Add a new row to Table 9: "CLIP4Clip + Ours (ViT-G)" on 1 GPU with batch size 128. This isolates CrossTVR's contribution independent of the base method. If this is computationally expensive, at minimum add a footnote stating: "CLIP4Clip trained on 8 GPUs vs. Ours on 1 GPU; total GPU-hours differ (400 vs. 21)."

### S4: Fix notation and add tensor shapes in equations (Must, P0)
In Section 3.1, unify naming to $X_{\text{frame}}(t)$ everywhere, specify $\text{Concat}(Q, X) \in \mathbb{R}^{(N_Q + N_X) \times d}$, and clarify that only the first $N_Q$ positions (the learnable queries) are averaged in Eq. (3). See the Mentor Revised Version in the annotation on Page 5.

### S5: Strengthen ablation analysis (Nice-to-have, P1)
Run the final CrossTVR configuration with 3 seeds to establish a variance baseline. If the standard deviation is ~0.3% (typical for TVR), then the 0.2% gains from parameter sharing and hard negative mining are not significant on their own. Either report this honestly or merge those components into a single ablation step.

### S6: Restructure conclusion (Must, P0)
Adopt the three-part structure: validated findings with bounded language, explicit limitations list (at least 3), and prioritized future work. See the Mentor Revised Version in the annotation on Page 9. Remove generic broader-impact statements about surveillance unless they are substantiated with concrete risk analysis.

### S7: Organize related work by comparison axes (Nice-to-have, P2)
Restructure Section 2 into three sub-paragraphs with explicit headings or topical sentences: (i) Dual-encoder methods and their efficiency-interaction tradeoff, (ii) Cross-attention methods and their computational challenges, (iii) Hybrid methods and where CrossTVR differs. For each category, state the specific limitation and how CrossTVR addresses it, rather than listing papers.

### S8: Remove informal language (Nice-to-have, P2)
Replace "obviously enhances" with "consistently improves across all evaluated benchmarks". Replace "we contend that... holds the potential to serve as a potent performance-boosting component" with "these results suggest CrossTVR can improve a range of cosine-similarity-based TVR methods".

## Storyline Options + Writing Outlines
### Current Storyline Diagnosis

The current introduction has three paragraphs with the following roles:
- **P1 (Page 1):** Taxonomy of three TVR approaches + CLIP context — reads as a literature list
- **P2 (Page 1-2):** Method description with premature technical details (T×N tokens, concatenation cost)
- **P3 (Page 2):** Frozen encoder motivation + two-stage architecture + contributions list

**Problems:** P1 does not establish stakes or practical motivation; P2 dives into token mechanics before explaining the core idea; P3 parallel structure between frozen encoder and two-stage design is confusing.

### Recommended Storyline (Option A — Best)

Use a four-paragraph structure:

- **P1 (The Gap):** "Text-Video Retrieval (TVR) is essential for video understanding and search, but existing methods face a fundamental tradeoff. Dual-encoder methods [...] sacrifice fine-grained interaction for speed. Cross-attention methods [...] support deeper matching but at prohibitive cost. Even hybrid approaches [...] lose spatial and temporal details because they aggregate frame tokens before cross-attention. This loss of fine-grained information — small objects, subtle motions, entity-level semantics — is the central limitation addressed in this work."

- **P2 (The Idea):** "We propose CrossTVR, a multi-grained re-ranker that preserves token-level detail by computing cross-attention at two complementary levels: frame-level attention for spatial details (per-frame, all tokens) and video-level attention for temporal dynamics (across frames, selected tokens). By keeping the full token set per frame and using parameter sharing, our design captures fine-grained information without the quadratic cost of attending to all T×N tokens jointly."

- **P3 (The Efficiency Mechanism):** "A key practical challenge is that large vision encoders (ViT-G) are expensive to fine-tune end-to-end. We freeze the vision backbone after the first-stage retrieval training and train only the multi-grained cross-attention header. This reduces GPU memory by 91% compared to end-to-end ViT-G fine-tuning and enables scalability to larger encoders on a single GPU."

- **P4 (Contributions):** List 3 specific, bounded contributions as described below.

### Revised Abstract Outline (S1-S5)

- **S1 (Problem + Domain):** "Text-video retrieval (TVR) requires aligning fine-grained visual details with natural language queries, yet existing methods lose spatial and temporal information by aggregating frame tokens."
- **S2 (Prior Limitation):** "Hybrid approaches that combine cosine similarity with cross-attention still pool frame representations, discarding token-level cues about small objects and subtle motions."
- **S3 (Method):** "We propose CrossTVR, a re-ranker with multi-grained cross-attention that separately models frame-level spatial interactions and video-level temporal interactions, preserving fine-grained information throughout."
- **S4 (Efficiency):** "By freezing the vision encoder and training only the cross-attention header, our method scales to large encoders (ViT-G) with 91% less GPU memory than end-to-end fine-tuning."
- **S5 (Result):** "On MSRVTT, VATEX, LSMDC, ActivityNet, and DiDeMo, CrossTVR improves R@1 by 2-8% over strong cosine-similarity baselines with minimal additional inference cost."

### Revised Contribution List

1. "We propose CrossTVR, a multi-grained re-ranker that separately computes frame-level spatial cross-attention (preserving token-level visual details) and video-level temporal cross-attention (capturing motion and event dynamics), enabling finer-grained text-video matching than prior single-level methods."
2. "As a plug-in re-ranker, CrossTVR consistently improves four diverse cosine-similarity-based TVR methods (CLIP4Clip, TS2Net, X-Pool, CLIP-ViP) across five benchmarks, demonstrating generality independent of the base retrieval model."
3. "By freezing the visual encoder and training only the cross-attention header, our approach reduces GPU memory by 91% compared to end-to-end ViT-G fine-tuning and enables practical scaling to large pre-trained models on a single GPU."

## Priority Revision Plan
### P0 — Must fix before acceptance

| Task | Effort | Impact | Section Affected |
|------|--------|--------|-----------------|
| Add statistical significance (3 seeds + bootstrap) | 3-5 GPU-days | Critical — without this, small gains are unverifiable | Tables 1-7 |
| Fix loss function notation and hard negative specification | 1 hour | High — enables reproducibility | Section 3.3 |
| Unify equation notation (X_frame vs X_spatial) and add tensor shapes | 2 hours | High — prevents implementation errors | Section 3.1 |
| Restructure conclusion with bounded claims and explicit limitations | 1 hour | Medium — improves scientific credibility | Section 5 |
| Remove informal/overclaiming language ("obviously", "potent") | 30 min | Medium — improves academic tone | Pages 2, 9 |

### P1 — Should fix (strong recommendation)

| Task | Effort | Impact | Section Affected |
|------|--------|--------|-----------------|
| Add controlled scalability comparison (same base method, same GPU count) | 2-3 GPU-days | High — validates claimed 91% memory reduction fairly | Table 9 |
| Run multi-seed ablation to validate 0.2% gains from sharing/hard mining | 1 GPU-day | Medium — may reveal noise vs. signal | Table 6 |
| Add R@1 for varying K in appendix and report inference time | 1-2 hours | Medium — supports K=15 choice | Appendix A |

### P2 — Nice-to-have (improves quality)

| Task | Effort | Impact | Section Affected |
|------|--------|--------|-----------------|
| Reorganize related work by comparison axes | 3-4 hours | Medium — improves positioning | Section 2 |
| Add pseudo-code for cross-attention module | 2-3 hours | Medium — aids reproducibility | Appendix |
| Clarify DSL post-processing impact (separate von Ours gains) | 1 hour | Medium — prevents conflating gains | Tables 1-5 |
| Add OOD robustness evaluation on at least one domain-shift benchmark | 3-5 GPU-days | Medium — strengthens generalization claims | New section |

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective / Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|----------------------|-------|---------|-------------|----------------|-------------------|
| E1 | Main results on MSRVTT | TS2Net/CLIP-ViP + CrossTVR (Base/Large); Table 1 | R@1, R@5, MnR (T2V, V2T) | 3-8% R@1 improvement over base | CrossTVR improves TVR performance | No variance; DSL post-processing confounded (marked with *) |
| E2 | Main results on ActivityNet | Same as E1; Table 2 | R@1, R@5, MnR | 8% (TS2Net) / 3.9% (CLIP-ViP) gain | CrossTVR generalizes to long videos | Base CLIP-ViP V2T not reported ("-") |
| E3 | Main results on LSMDC | Same as E1; Table 3 | R@1, R@5, MnR | 1.4-3.4% R@1 gain | CrossTVR works on movie data | Some MnR values increase (worse ranking); small gains |
| E4 | Main results on DiDeMo | Same as E1; Table 4 | R@1, R@5, MnR | 2.3-5.3% R@1 gain | CrossTVR handles short clips | Large model shows higher MnR (17.6 → 19.1) |
| E5 | Main results on VATEX | Same as E1; Table 5 | R@1, R@5, MnR | 2.2-5.0% R@1 gain | CrossTVR benefits multilingual data | No language-specific analysis |
| E6 | Qualitative analysis | Grad-CAM on MSRVTT examples; Figure 3-4 | Visual inspection | CrossTVR retrieves entities/actions missed by TS2Net | Fine-grained attention works | Only 2 examples; no quantitative metric |
| E7 | Ablation: components | TS2Net + incremental additions; Table 6 | R@1, R@5, MnR | Video: +1.4%, Frame: +1.2%, Sharing: +0.2%, Hard: +0.2% | Multi-grained design validated | No variance; 0.2% gains may be noise |
| E8 | Ablation: design strategies | Compare avg/CLS/video/frame/sum/hierarchical; Table 7 | R@1, R@5, MnR | Hierarchical best (50.0%); Sum ensemble 49.1% | Hierarchical > sum ensemble | 0.9% gap between sum and hierarchical is small without CI |
| E9 | Cross-method collaboration | CLIP4Clip + Ours, X-Pool + Ours; Table 8 | R@1, R@5, time | +2.5% (CLIP4Clip), +1.2% (X-Pool) | CrossTVR generalizes to other base methods | Only 2 extra methods tested |
| E10 | Scalability analysis | ViT-B vs ViT-G memory/time; Table 9 | R@1, memory, training hours | 91% memory reduction, 58% training time reduction | Frozen encoder enables ViT-G scaling | Confounded by GPU count and batch size differences |

### Research-Theme Gap Diagnosis

**New Knowledge.** The paper's primary claim is that separating frame-level and video-level cross-attention preserves fine-grained information better than single-level methods. The ablation study (Tables 6-7) supports this directionally, but the marginal gains from the hierarchical design over a simple sum-ensemble (0.9%) are not statistically validated.

**Reproducibility.** Reproducibility is partially impaired by (a) underspecified loss function, (b) missing tensor dimensions in equations, (c) no code release mentioned, and (d) no variance reporting.

**Impact on Practice.** The frozen-encoder scalability strategy is practically valuable and well-demonstrated, though the comparison needs fairer controls. The re-ranker design is generic and could benefit the broader TVR community.

### Proposed Research Experiments

| ID | Target Claim | Hypothesis | Minimal Design | Controls/Baselines | Metrics | Success Criterion | Cost | Expected Quality Gain |
|----|-------------|-----------|---------------|-------------------|---------|------------------|------|---------------------|
| P0-exp1 | Gains > seed noise | CrossTVR improvements are statistically significant | Run TS2Net + Ours(Base) with 3 seeds on MSRVTT | TS2Net base with 3 seeds | Mean R@1 ± std, bootstrap p-value | p < 0.05 for R@1 improvement | 1 GPU-day | Validates core claim |
| P0-exp2 | Hierarchical > sum ensemble | Hierarchical design adds value beyond logit averaging | Run Frame Video Sum + hierarchical CrossTVR with 3 seeds | Frame Video Sum (Table 7) | R@1 ± std, effect size | >0.5% gap with non-overlapping error bars | 1 GPU-day | Justifies architectural complexity |
| P1-exp3 | Controlled scalability | Memory savings are not an artifact of different configs | Apply CrossTVR on CLIP4Clip (not TS2Net) with ViT-G, 1 GPU, batch 128 | CLIP4Clip end-to-end ViT-G (Table 9) | GPU memory, training hours, R@1 | Memory <100 GB, R@1 improvement >3% | 2-3 GPU-days | Fair scalability comparison |
| P2-exp4 | OOD generalization | CrossTVR robust to domain shift | Evaluate TS2Net+Ours on Charades or YouCook2 without fine-tuning | TS2Net base on same OOD sets | R@1, R@5 drop vs in-domain | Drop <5% absolute | 1 GPU-day | Strengthens generalization claims |
| P2-exp5 | Component importance at scale | Frame-level vs video-level attention matter differently for long vs short videos | Vary frame count (8/16/32/64) and report per-level contribution | TS2Net base | Per-level R@1 contribution | Both levels contribute positively at all frame counts | 1 GPU-day | Provides deeper insight into multi-grained design |

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
### Final Score: 5.5 / 10

**Rationale:** The paper presents a clear architectural contribution (multi-grained cross-attention with frozen encoder) and demonstrates consistent empirical gains across five benchmarks. However, the score is constrained by several critical weaknesses: (1) no statistical significance reported for any result, making small-margin gains unverifiable; (2) reproducibility gaps in loss function specification and equation notation; (3) the scalability comparison is confounded by different training configurations; (4) novelty cannot be fully assessed without external literature retrieval (deferred to manual verification); and (5) the narrative framing and conclusion are underdeveloped. Research value is moderate — the frozen-encoder efficiency insight is practically useful, but the core methodological novelty (multi-grained vs. single-level attention) produces small incremental gains that need statistical validation.

### Post-Revision Target: [6.5, 7.5] / 10

If all P0 fixes are applied (statistical significance, loss function clarification, notation cleanup, conclusion restructuring, language polish) and P1 fixes partially addressed (controlled scalability comparison, multi-seed ablation), the paper could reach 6.5-7.5. Full resolution of OOD evaluation and stronger novelty differentiation would push toward 7.5.

---

### ASCII Diagram — Paper Structure & Evidence Map

```text
[Claim: Multi-grained cross attention improves TVR by preserving 
        frame-level spatial + video-level temporal details]
    |
    ├── Evidence 1: Main results (Tables 1-5)
    |       → Consistent R@1 gains across 5 benchmarks
    |       → Risk: No variance, DSL post-processing confounded
    |
    ├── Evidence 2: Ablation (Tables 6-7)
    |       → Each component adds positive gain
    |       → Risk: 0.2% gains (sharing, hard-mining) may be noise
    |       → Risk: Sum ensemble achieves 49.1% vs hierarchical 50.0%
    |
    ├── Evidence 3: Cross-method generality (Table 8)
    |       → Works with CLIP4Clip, X-Pool, TS2Net, CLIP-ViP
    |       → Risk: Only 4 methods, 2 with small gains (1.2%)
    |
    ├── Evidence 4: Scalability (Table 9)
    |       → 91% memory reduction vs end-to-end ViT-G
    |       → Risk: Confounded by GPU count / batch size
    |
    └── Evidence 5: Qualitative (Figures 3-4)
            → Visual attention maps show entity/action focus
            → Risk: Only 2-3 examples, no quantitative metric
```

### ASCII Diagram — Revision Strategy Roadmap

```text
[P0: Must fix before acceptance]
    ├── Add statistical significance (3 seeds + bootstrap)
    │       → Expected: Validates vs. seed noise
    ├── Fix loss function notation & hard-negative spec
    │       → Expected: Reproducibility ensured
    ├── Unify equation notation + add tensor shapes
    │       → Expected: Implementation errors prevented
    ├── Restructure conclusion with bounded claims
    │       → Expected: Scientific credibility improved
    └── Remove informal/overclaiming language
            → Expected: Academic tone restored

[P1: Should fix]
    ├── Controlled scalability comparison (same base/GPU count)
    │       → Expected: Fair validation of 91% claim
    └── Multi-seed ablation for 0.2% gains
            → Expected: Noise vs. signal resolved

[P2: Nice-to-have]
    ├── Reorganize related work by axes
    ├── Add pseudo-code for cross-attention
    └── Add OOD robustness evaluation
```

### ASCII Diagram — Related-Work Taxonomy Tree (Layered)

```text
Text-Video Retrieval (TVR) Methods
│
├── Branch 1: Dual-Encoder (Cosine Similarity)
│   ├── Leaf 1.1: CLIP-based adaptation
│   │   └── CLIP4Clip, CLIP2Video, TS2Net, CenterCLIP
│   └── Leaf 1.2: Interaction-enhanced cosine
│       └── HBI (hierarchical Banzhaf interaction)
│   Limitation: Shallow dot-product interaction;
│               loses fine-grained token-level alignment
│
├── Branch 2: Cross-Attention (Full Interaction)
│   ├── Leaf 2.1: Frame-level attention
│   │   └── X-Pool (scaled dot-product over frames)
│   └── Leaf 2.2: Token-level attention
│       └── CLIP4Clip-tightTransf
│   Limitation: O(T×N) cost; optimization difficulty;
│               frames pooled → token details lost
│
└── Branch 3: Hybrid (Two-Stage Re-ranking)
    ├── Leaf 3.1: Generic hybrid
    │   └── Miech et al., OmniVL
    └── Leaf 3.2: Multi-grained re-ranker (THIS PAPER)
        └── CrossTVR: Frame-level spatial + Video-level temporal
    Key Difference: Prior hybrid methods use single-level 
                    cross-attention; CrossTVR separates 
                    frame and video levels with parameter sharing,
                    preserving per-frame token information
    Novelty Risk: Unknown without external retrieval comparison
                  (deferred to manual verification)
```

### Page Coverage Audit

| Page | Section | Annotation Count | Coverage Status | Skip Reason |
|------|---------|-----------------|----------------|-------------|
| 1 | Abstract + Introduction (P1-P2) | 3 | Covered | — |
| 2 | Introduction (P3, Contributions) | 1 | Covered | — |
| 3 | Related Work | 1 | Covered | — |
| 4 | Method overview + Frame Text Attention | 1 | Covered | — |
| 5 | Equations (1-6), Video Text Attention, Frozen Encoder | 1 | Covered | — |
| 6 | Training (Loss, Inference) | 1 | Covered | — |
| 7 | Experimental Settings + Results (Tables 1-4 start) | 1 | Covered | — |
| 8 | Ablation Study (Tables 6-7) | 1 | Covered | — |
| 9 | Scalability + Conclusion | 2 | Covered | — |
| 10-13 | References | 0 | Skipped | Boilerplate references |
| 14 | Appendix A-B | 1 | Covered | — |
| 15-16 | Appendix figures | 0 | Skipped | Figure-only pages |

**Total annotations: 13 (main body) | Minimum required: 10 | Coverage: All substantive paragraphs covered**
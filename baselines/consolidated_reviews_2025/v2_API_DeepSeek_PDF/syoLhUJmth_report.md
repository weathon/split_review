## Summary
# Final Review Report

## Summary

This paper presents COMM (Combining CLIP and DINO with Multi-level Feature Merging), a fusion strategy for enhancing the visual branch of Multi-modal Large Language Models (MLLMs). The authors conduct a systematic comparison of four visual encoders — CLIP, DINOv2, MAE, and DeiT — as visual backbones in MLLMs. Key findings are: (1) CLIP's shallow-layer features benefit fine-grained grounding tasks while deep layers support global understanding; (2) DINOv2, a vision-only model without text-image pretraining, achieves competitive grounding performance when aligned via an MLP layer; (3) MAE and DeiT are less suitable as MLLM visual encoders. Based on these insights, COMM fuses CLIP and DINOv2 features using a learnable LLN-Layerscale multi-level merging mechanism. Experiments on REC, REG, POPE, VQA, and captioning benchmarks show consistent improvements over single-encoder baselines.

The paper addresses a relevant and under-explored question — whether visual encoder design choices significantly affect MLLM performance — and provides useful empirical evidence. The main contributions are the systematic encoder comparison and the simple fusion approach. However, the paper has several significant weaknesses: (1) the analysis experiments use only 9400 training iterations without variance reporting, limiting statistical reliability; (2) the main comparisons are confounded by higher input resolution (336×336 vs 224×224) used in COMM; (3) several strong baselines are omitted from comparison tables; (4) novelty claims ("first to extensively investigate") are unverifiable without external literature review; and (5) the Conclusion lacks explicit limitations. Despite these issues, the core empirical findings and the fusion method provide a solid incremental contribution that is likely publishable after thorough revision addressing the comparison fairness, statistical rigor, and scope definition.

## Strengths
**S1. Timely and relevant research question.** The paper addresses an important and under-explored question: whether the choice of visual encoder and feature depth significantly affects MLLM performance. Given that most MLLMs default to CLIP deep-layer features without systematic justification, this investigation is practically valuable for the community.

**S2. Systematic encoder comparison.** The paper compares four visually diverse foundation models (CLIP, DINOv2, MAE, DeiT) under the same MLLM training framework. The finding that DINOv2 — a vision-only model — can serve as an effective visual backbone when aligned with an MLP is non-trivial and practically useful. The layer-wise analysis (Fig. 2) showing that different depths suit different tasks (shallow → grounding, deep → global understanding) provides actionable guidance for MLLM design.

**S3. Simple and effective fusion design.** The COMM fusion strategy is conceptually simple (weighted multi-level feature merging + encoder concatenation) and achieves consistent improvements across multiple benchmarks. The ablation study on merging strategies (Mean, Layerscale, LLN-Layerscale) provides useful insights into which fusion mechanisms work best.

**S4. Broad experimental coverage.** The paper evaluates on REC (3 datasets × 8 splits), REG (3 datasets), POPE (3 splits), VQA (2 benchmarks), captioning (2 benchmarks), and MME (14 subtasks). This breadth demonstrates COMM's versatility across different vision-language task types.

**S5. Reasonable training efficiency claims.** The paper argues that COMM achieves competitive results with a 7B LLM (vs. 13B in Shikra) and less training data (vs. Qwen's 1.4B), which, if confirmed under controlled comparison, would be a practical advantage.

## Weaknesses
**W1. Analysis experiments lack statistical reliability (Major).** The layer-wise analysis (Section 3) and all ablations in Appendix A/B use only 9400 training iterations (batch size 16, 4 GPUs) with single-run results. No standard deviations, confidence intervals, or multi-seed experiments are reported. Given the observed performance differences are often small (e.g., 1-2% on POPE), single-run results cannot support reliable conclusions about encoder ranking or optimal layer depth. This is a fundamental methodological limitation that affects the credibility of the paper's main empirical claims.

**W2. Confounded comparison against baselines (Major).** The main experiments (Tables 2-5) compare COMM against Shikra and Qwen under unequal conditions:
- COMM uses 336×336 input resolution; Shikra and Qwen use 224×224. Higher resolution directly helps fine-grained tasks (REC, REG) and partially explains performance gains.
- COMM uses an MLP for DINOv2 alignment in its final configuration, while the analysis section uses only a linear projection for fairness. This asymmetry means the analysis results may underestimate DINOv2's potential.
- Training data composition, sampling strategy, and LLM fine-tuning recipe differ between COMM and the baselines.
No resolution-controlled ablation is provided to disentangle the fusion method's contribution from the resolution advantage.

**W3. Incomplete baseline coverage and unsupported SOTA claims (Major).** Table 5 (VQA/captioning) omits several stronger contemporary MLLMs such as LLaVA-1.5 and InstructBLIP. The claim "state-of-the-art performance on image captioning task" (Page 8) is not supported by the presented evidence, as the comparison set is incomplete. Similarly, the REC comparison (Table 2) would benefit from including more recent generalist MLLMs.

**W4. Unverifiable novelty claims (Major).** Contribution 1 states "We are the first to extensively investigate the effectiveness of different visual encoders for MLLMs." This "first" claim cannot be verified without external literature review (which is unavailable in this run). Given that multiple prior works have examined visual encoder variations in MLLMs, this claim may be overstated and should be softened to "to our knowledge" with concrete differentiation from prior analyses.

**W5. Missing limitations and overclaimed conclusions (Major).** The Conclusion (Section 6) does not discuss any limitations of the proposed COMM approach. Key limitations that should be acknowledged include: (a) COMM uses two frozen ViT-Large encoders, approximately doubling the visual compute cost compared to single-encoder MLLMs; (b) all evaluations are on in-domain benchmarks without OOD generalization testing; (c) the fusion strategy's sensitivity to training data scale is not explored; (d) the higher input resolution (336×336) is a confound that is not controlled.

**W6. Method description lacks key architectural details (Minor).** The MLP module used for DINOv2 alignment is described only as "an MLP layer" without specifying the number of layers, hidden dimension, or activation function. These details are deferred to the appendix, but critical specifications should appear in the main method section. The LLN-Layerscale normalization of α and β weights (whether softmax-normalized or unnormalized) is ambiguous.

**W7. Introduction narrative is structure-weak (Minor).** The introduction spends its first paragraph on generic LLM background before stating the paper's specific research question. The contribution statements are bundled unclearly (investigation + fusion method in one bullet). The "Buckets Effect" metaphor (Page 2) is undefined and not supported by evidence.

## Key Issues
### Issue 1: No statistical variance reported across any experiment (Critical for Validity)
All experimental results in the paper — from the layer-wise analysis (Section 3) to the main benchmark comparisons (Tables 2-5) and ablations (Appendix A/B) — are reported as single-run point estimates without standard deviations, confidence intervals, or significance tests. For a paper making empirical claims about encoder ranking and method superiority, this is a critical omission. Many reported gains (e.g., 1.44% on POPE vs Shikra, 0.3-point VQAv2 gain) could be within the noise range of a single training run. The analysis experiments using only 9400 iterations (vs. full convergence) compound this concern. **Required fix:** Re-run all main experiments with at least 3 random seeds and report mean ± std.

### Issue 2: Resolution confound invalidates direct SOTA comparison (Major)
COMM uses 336×336 input resolution while all baselines (Shikra, Qwen, InstructBLIP) use 224×224. Higher resolution directly improves fine-grained tasks by providing more pixels for object localization. The paper does not include a controlled ablation at 224×224 to isolate the fusion method's contribution from the resolution advantage. This means the claim "COMM outperforms Shikra by a large margin" conflates two independent factors. **Required fix:** Add a 224×224 version of COMM (or upscale baselines to 336×336) and report the resolution-controlled comparison.

### Issue 3: Unsupported SOTA and "first" novelty claims (Major)
Two classes of claims lack adequate support: (1) "state-of-the-art performance on image captioning task" (Page 8) is based on an incomplete comparison set that omits stronger models (LLaVA-1.5, InstructBLIP); (2) "We are the first to extensively investigate..." (Page 2) requires external literature verification that is unavailable in this review. **Required fix:** Replace "SOTA" with bounded comparative wording ("outperforms the baselines in our comparison set" and "to our knowledge, this is the first systematic comparison under controlled training conditions"). Remove or significantly soften the "first" claim.

### Issue 4: Conclusion lacks limitations and specificity (Major)
The Conclusion recaps the paper's contributions without mentioning any limitations, failure cases, or boundary conditions. Given the paper's ambition to guide future MLLM visual encoder design, this omission is significant. **Required fix:** Add a dedicated limitations subsection covering compute cost, resolution confound, lack of OOD testing, and unknown scaling behavior with training data size.

### Issue 5: Introduction narrative is not organized around the research gap (Minor)
The introduction spends its first paragraph on generic LLM background (applies to any MLLM paper), and the core research question ("is CLIP the best visual encoder for MLLMs?") is not stated until the second paragraph's midpoint. The contribution bullets bundle investigation and method together obscurely. **Required fix:** Restructure the introduction to front-load the visual encoder problem and use the first paragraph to establish why encoder choice matters for MLLM performance.

## Actionable Suggestions
### Suggestion 1: Add multi-seed variance and significance tests (Must, P0)
Re-run all main experiments (Section 5 results in Tables 2-5, Section 3 analysis in Table 1) with 3 random seeds and report mean ± std. For the main benchmark comparisons, add pairwise significance tests (e.g., McNemar's test for VQA accuracy, bootstrapped CIDEr confidence intervals for captioning). This is the single highest-impact change for improving the paper's credibility.

### Suggestion 2: Add resolution-controlled ablation (Must, P0)
Train COMM with 224×224 input resolution (matching Shikra and Qwen) and report a side-by-side comparison. Alternatively, retrain Shikra with 336×336 resolution under the same training recipe. At minimum, provide a table like:
| Model | Resolution | Avg REC | VQAv2 | COCO CIDEr |
|-------|-----------|---------|-------|------------|
| Shikra-7B | 224 | X | X | X |
| COMM-7B | 224 | X | X | X |
| COMM-7B | 336 | X | X | X |
This would allow readers to separate the fusion method's contribution from the resolution contribution.

### Suggestion 3: Replace unsupported "SOTA" and "first" claims (Must, P0)
- In Contribution 1 (Page 2), replace "We are the first to extensively investigate..." with "To our knowledge, this is the first controlled comparison of CLIP, DINOv2, MAE, and DeiT as MLLM visual branches under identical training conditions."
- In the captioning results (Page 8), replace "state-of-the-art performance on image captioning task" with "outperforms the generalist MLLMs in our comparison set on COCO and Flickr30k captioning."
- Add a caveat that "these results are single-run and should be interpreted with caution."

### Suggestion 4: Add limitations subsection to Conclusion (Must, P0)
Add the following limitations after the current conclusion paragraph:
**Limitations.** (a) COMM uses two frozen ViT-Large encoders, which approximately doubles the inference compute cost compared to single-encoder MLLMs. (b) The 336×336 input resolution contributes to observed gains; the fusion mechanism's independent contribution requires further controlled study. (c) All evaluations are on standard in-domain benchmarks; OOD and domain-shift generalization are not tested. (d) Results are based on single training runs; variance across seeds is not yet available.

### Suggestion 5: Improve introduction narrative and contribution clarity (Nice-to-have, P1)
Restructure the introduction as:
- P1: State the visual encoder problem in MLLMs directly: "Current MLLMs almost exclusively use CLIP's deep-layer features without questioning whether this is optimal."
- P2: Literature context: previous MLLMs use CLIP only, and region-level methods address symptoms (hallucination, poor grounding) without addressing the root cause (encoder design).
- P3: The paper's investigation: four encoders tested, key findings, and the proposed COMM fusion.
- P4: Contributions (three distinct bullets): (i) empirical findings about encoder/layer suitability, (ii) multi-level fusion mechanism, (iii) COMM architecture and results.

### Suggestion 6: Specify MLP architecture in main text (Nice-to-have, P1)
In Section 4 (Architecture Overview), add: "The MLP for DINOv2 alignment has 2 hidden layers with 4× the token embedding dimension and GELU activation, as determined by the ablation study in Appendix B."

### Suggestion 7: Add missing strong baselines to comparison tables (Nice-to-have, P1)
Extend Table 5 to include LLaVA-1.5, InstructBLIP, and any other contemporaneous MLLM that has reported results on VQAv2, COCO CIDEr, or Flickr30k CIDEr. If these models use different training recipes, include a footnote clarifying the comparison scope.

## Storyline Options + Writing Outlines
### Abstract Outline (Complete)

**S1 (Domain/Problem):** "Multi-modal Large Language Models (MLLMs) predominantly use CLIP as their visual encoder and extract features only from deep layers, without systematic analysis of how visual encoder choice affects downstream performance."

**S2 (Prior limitation/Gap):** "CLIP's global contrastive objective discards pixel-level information needed for fine-grained grounding and region understanding, while alternative vision encoders such as DINOv2, MAE, and DeiT have not been compared under controlled MLLM training conditions."

**S3 (Proposed investigation):** "We conduct a controlled study of four visual encoders — CLIP, DINOv2, MAE, and DeiT — as visual branches in MLLMs under identical training conditions."

**S4 (Key findings):** "Our analysis reveals that: (1) CLIP shallow layers benefit fine-grained tasks while deep layers support global understanding; (2) DINOv2, despite lacking text-image pretraining, achieves competitive grounding when aligned via an MLP; (3) MAE and DeiT underperform due to insufficient semantics or misaligned representation space."

**S5 (Method + Result):** "Based on these findings, we propose COMM (Combining CLIP and DINO with Multi-level Feature Merging), which fuses both encoders via a learnable LLN-Layerscale mechanism. On REC, REG, VQA, captioning, and object hallucination benchmarks, COMM shows consistent improvements over single-encoder baselines."

---

### Introduction Outline (Complete)

**P1 (Big Picture / Gap):** Replace generic LLM background with the visual encoder problem. Start: "Current MLLMs rely on CLIP's deep-layer visual features without questioning whether this design choice is optimal for fine-grained tasks." Then state the gap: "No systematic comparison of visual encoder families exists for MLLMs under controlled conditions."

**P2 (Prior Work / Why This Gap Matters):** Summarize MLLM development (Flamingo, BLIP-2, LLaVA, InstructBLIP, Shikra, Qwen) but organize by visual encoder usage, not chronologically. Explain that all use CLIP-only deep features. State the consequence: "This reliance limits fine-grained understanding and causes object hallucination, but prior work treats the symptom (by adding region supervision) rather than the cause (by evaluating alternative encoder designs)."

**P3 (Investigation Preview):** "In this paper, we address this gap by systematically comparing four visual encoders — CLIP, DINOv2, MAE, and DeiT — as visual branches in MLLMs. We find that shallow and deep features serve complementary roles, and that DINOv2, despite no text alignment, achieves strong grounding performance. These insights lead to COMM, a simple fusion strategy."

**P4 (Contributions):** Present as three distinct bullets:
- Empirical findings about encoder and layer-depth suitability for different MLLM tasks.
- Multi-level feature merging mechanism (LLN-Layerscale) that combines shallow and deep features.
- COMM architecture fusing CLIP and DINOv2, with consistent gains across 5 benchmark categories.

---

### Alternative Storyline Candidates

**Candidate A (Encoder-First):** Lead with the visual encoder analysis as the primary contribution. The fusion method is secondary — a natural application of the analysis findings. This would reframe the paper as primarily an empirical study with a method follow-up.

**Candidate B (Method-First):** Lead with the COMM fusion architecture as the main contribution, with the encoder analysis serving as motivation. This is closer to the current framing but would benefit from a stronger "why existing solutions are insufficient" setup.

**Candidate C (Problem-Solution-Impact):** Start with the practical problem (MLLMs hallucinate and fail at grounding), trace it to the visual encoder bottleneck, then present the analysis as diagnosis and COMM as the treatment. This narrative is more accessible to non-expert readers.

**Recommended: Candidate A with elements of C.** The paper's strongest contribution is the systematic encoder analysis, which is genuinely useful for the MLLM community. The COMM fusion is a natural downstream application of this analysis. Restructuring around the empirical findings would make the paper more distinctive and defensible.

## Priority Revision Plan
### P0 — Must Fix (Publication-Critical)

| # | Issue | Action | Expected Impact | Effort |
|---|-------|--------|----------------|--------|
| 1 | No variance/statistics | Re-run main experiments with 3 seeds, report mean±std, add significance tests | Directly fixes the most fundamental validity concern | 2-3 weeks GPU time |
| 2 | Resolution confound | Add 224×224 COMM ablation or 336×336 baseline; provide side-by-side comparison | Separates fusion contribution from resolution advantage; may change claimed gains | 1 week GPU time |
| 3 | Unsupported SOTA/first claims | Replace "SOTA" with bounded comparative wording; soften "first" to "to our knowledge" | Fixes factual overclaim and reviewer pushback risk | <1 hour text editing |
| 4 | Missing limitations | Add dedicated limitations subsection in Conclusion (compute cost, resolution, OOD, variance) | Improves scientific integrity and reduces adversarial review | <1 hour text editing |

### P1 — Should Fix (High Impact)

| # | Issue | Action | Expected Impact | Effort |
|---|-------|--------|----------------|--------|
| 5 | Missing strong baselines | Add LLaVA-1.5, InstructBLIP, and other strong MLLMs to comparison tables | Strengthens SOTA positioning; may change the paper's competitiveness narrative | <1 week (evaluation on existing checkpoints) |
| 6 | Introduction narrative weakness | Restructure intro to front-load the encoder problem (see Storyline Options) | Improves reader engagement and clarity of contribution | 1-2 days text editing |
| 7 | MLP details in main text | Add MLP architecture (2 layers, 4× ratio, GELU) to Section 4 | Improves reproducibility | <1 hour |

### P2 — Nice-to-Have (Quality Improvement)

| # | Issue | Action | Expected Impact | Effort |
|---|-------|--------|----------------|--------|
| 8 | Table 7 formatting | Fix alignment of MLP ablation table; consider splitting into two sub-tables | Improves readability | <1 hour |
| 9 | Training data mixture details | Specify exact data proportions and sampling strategy | Improves reproducibility | <1 hour |
| 10 | OOD generalization test | Add one OOD benchmark (e.g., COCO → nocaps, or cross-dataset REC) | Strengthens robustness claims significantly if consistent | 1-2 weeks (evaluation) |
| 11 | Conclusion strengthening | Add 2-3 specific future directions beyond "more powerful models" | Provides clearer guidance for community follow-up | <2 hours |

### Revision Strategy Roadmap (ASCII)

```text
[Issue 1: No variance/std]
    → [Fix: 3-seed re-runs + significance tests]
    → [Expected: confidence intervals for all claims]
    
[Issue 2: Resolution confound]  
    → [Fix: 224px COMM ablation table]
    → [Expected: separate fusion vs. resolution delta]
    
[Issue 3: SOTA/first overclaim]
    → [Fix: bounded wording + "to our knowledge"]
    → [Expected: claim-defensibility, reduced reviewer risk]
    
[Issue 5: Missing baselines]
    → [Fix: add LLaVA-1.5/InstructBLIP to Table 5]
    → [Expected: comprehensive comparison]
    
[Issue 6: Weak narrative]
    → [Fix: restructure intro P1-P4 per Storyline Options]
    → [Expected: clearer contribution positioning]
    
[Stage 1 (P0, now)]: Fix issues 1, 2, 3, 4 → re-run experiments + text edits
[Stage 2 (P1, next)]: Fix issues 5, 6, 7 → add baselines + restructure narrative  
[Stage 3 (P2, before submission)]: Fix issues 8, 9, 10, 11 → polish + OOD tests
```

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|---------------------|-------|---------|-------------|----------------|-------------------|
| E1 (Sec 3) | Layer-wise analysis: different CLIP/DINO/MAE layers have different task biases | Shikra architecture, Vicuna-7B, 9400 iter, 4×A800, linear projection alignment | REC accuracy, POPE acc, REG CIDEr | Shallow layers best for REC, deep layers best for POPE; CLIP optimal at layer 12 for REC | "Different layers exhibit varying biases towards local/global patterns" | Single run, 9400 iter only, linear projection for all (not MLP for DINOv2) |
| E2 (Sec 3) | Multi-level feature merging strategies for CLIP | Same setup as E1, 5 merging strategies tested | REC acc, POPE acc | LLN-Layerscale best; outperforms single-layer baselines | "Multi-level feature fusion improves representation" | No variance; only 2 tasks tested; no comparison of different backbone sizes |
| E3 (Sec 3) | DINOv2 as visual branch with MLP alignment | Same setup + MLP module for DINOv2 | REC acc, POPE acc, REG CIDEr | DINOv2 deep layers better than CLIP deep for REC | "DINOv2 shows promise as visual branch for MLLMs" | MLP vs linear comparison confounded; no analysis of convergence speed |
| E4 (Sec 5.1) | REC: COMM vs generalist/specialist MLLMs | Full COMM training (2-stage), 336×336, Vicuna-7B, 8×A800 | Accuracy on RefCOCO/+/g (8 splits) | COMM-7B outperforms Shikra-13B and Qwen-VL-7B | "Superior grounding ability" | Confounded by resolution; single run; data scale differs |
| E5 (Sec 5.2) | REG: region description generation | Same setup as E4 | CIDEr score | COMM outperforms Shikra and Kosmos-2; competitive with SLR | "Effective for fine-grained understanding" | Some scores have high variance (e.g., RefCOCO+ test-A: 44.26 for Shikra vs 54.95 for COMM) |
| E6 (Sec 5.3) | Object hallucination: POPE benchmark | Same setup as E4 | Accuracy on Random/Popular/Adversarial | COMM surpasses Shikra by 1.44% avg | "COMM alleviates hallucination" | Margins are small; no significance test |
| E7 (Sec 5.4) | VQA + Captioning | Same setup as E4 | VQAv2 acc, OK-VQA acc, COCO/Flickr30k CIDEr | COMM achieves competitive results | "Effectiveness of merging visual embeddings" | Missing strong baselines (LLaVA-1.5, InstructBLIP); resolution confound |
| E8 (App A) | DeiT & MAE as visual branches | Same as E1 setup | REC, POPE | DeiT very poor (18-25% REC); MAE acceptable but below CLIP/DINOv2 | "DeiT/MAE not suitable for MLLMs" | Only 2 layers tested per model; MLP alignment not tried for DeiT |
| E9 (App B) | MLP depth and expansion ratio for DINOv2 | Same as E1 setup with DINOv2 | REC, POPE | 2-layer MLP with 4× ratio best; deeper MLP hurts | "Non-linear MLP necessary for DINOv2 alignment" | Table 7 has formatting issues; no variance reported |

### Research-Theme Gap Diagnosis

1. **New knowledge (partially supported):** The empirical finding about shallow vs deep layer utility is genuinely useful and not well documented in prior MLLM literature. However, the lack of statistical rigor weakens the knowledge claim. The finding about DINOv2's viability as an MLLM backbone is interesting but may be known to practitioners working with DINOv2 for visual tasks.

2. **Reproducibility (partially supported):** The training recipe (2-stage, learning rate, optimizer) is described in adequate detail. However, the data mixture proportions are not specified, and the MLP architecture for DINOv2 is only given in the appendix. The use of "fewer iterations" for analysis experiments without convergence verification makes exact reproduction difficult.

3. **Impact on practice (partially supported):** The paper provides actionable guidance for MLLM practitioners (use shallow features for grounding, consider DINOv2 as a backbone). However, without multi-seed variance, the community cannot confidently act on the quantitative rankings.

### Proposed Research Experiments (P0/P1/P2)

| Target Claim | Hypothesis | Minimal Design | Controls/Baselines | Metrics | Success Criterion | Est. Cost | Expected Quality Gain |
|-------------|-----------|---------------|-------------------|---------|------------------|-----------|----------------------|
| **P0**: COMM gains are statistically significant | COMM outperforms single-encoder baselines beyond chance | Re-run COMM, CLIP w/ MFM, DINOv2 w/ MFM with 3 seeds on 3 key tasks (REC, VQAv2, COCO) | Same training recipe across all runs | Mean±std REC acc, VQAv2 acc, CIDEr; pairwise t-test or bootstrapped CI | COMM mean > baselines at p<0.05 on ≥2/3 tasks | 2-3 weeks GPU | Addresses W1 — critical for validity |
| **P0**: Resolution vs fusion contribution | COMM's advantage persists at 224×224 resolution | Train COMM with 224×224 input (same training data, same recipe) | (1) COMM-224, (2) Shikra-224 (original), (3) CLIP w/ MFM-224 | REC avg, VQAv2, COCO CIDEr | COMM-224 outperforms CLIP w/ MFM-224 and Shikra-224 | 1 week GPU | Addresses W2 — critical for comparison fairness |
| **P1**: COMM generalizes to OOD settings | COMM's fine-grained features improve OOD robustness | Evaluate POPE and REC models on cross-dataset/cross-domain test sets | Use same checkpoints as main experiments | POPE accuracy drop, REC accuracy on unseen categories | COMM shows <15% relative performance drop vs. in-domain | <1 week eval | Addresses robustness gap; supports "enhanced visual capabilities" claim |
| **P1**: Ablation of each component of COMM | CLIP features, DINOv2 features, and MFM each contribute positively | Ablate: remove DINOv2 (CLIP+MFM only), remove MFM (CLIP+DINO concat only), remove CLIP (DINOv2+MFM only) | Full COMM as reference | REC avg, POPE avg, VQAv2 | Each ablated variant underperforms full COMM | 1 week GPU | Quantifies each component's contribution |
| **P2**: Scaling behavior with training data | COMM's advantage grows or saturates with more data | Train COMM at 25%, 50%, 100% of Stage 1 training steps (25K, 50K, 100K) | CLIP w/ MFM at same data amounts | REC acc, VQAv2 acc | Gap between COMM and CLIP w/ MFM increases or stays stable | 1 week GPU | Tests whether COMM is data-efficient or data-hungry |

### Experiment Upgrade Plan (ASCII Diagram)

```text
Stage P0 (Weeks 1-3): Core validity fixes
├── [E1] Multi-seed re-runs (COMM + baselines, 3 seeds)
├── [E2] 224×224 COMM ablation
└── [E3] Significance tests on all main table entries

Stage P1 (Weeks 4-5): Completeness
├── [E4] OOD generalization evaluation
└── [E5] Component ablation (CLIP-only, DINO-only, w/o MFM)

Stage P2 (Weeks 6-7): Depth  
├── [E6] Data scaling curve (25% / 50% / 100% training)
└── [E7] Add missing baselines to Table 5 (LLaVA-1.5, InstructBLIP)

Expected outcome after all stages:
- Statistical reliability for all core claims
- Resolution-controlled comparison isolating fusion contribution
- Comprehensive baseline coverage
- OOD generalization evidence
- Component-level contribution analysis
- Training data scaling understanding
```

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score: 6.2 / 10**

The paper addresses a relevant question (visual encoder design for MLLMs) and provides useful empirical findings with a simple yet effective fusion method. However, the score is reduced by three critical weaknesses: (1) All results are single-run without variance, which fundamentally limits the reliability of the empirical claims — a critical issue for a paper whose main contribution is empirical analysis. (2) The main comparisons are confounded by higher input resolution used in COMM, making it impossible to isolate the fusion method's contribution. (3) Several strong baselines are omitted from comparison tables, and unsupported "SOTA" and "first" claims weaken the paper's defensibility. The paper's strengths — systematic encoder comparison, broad evaluation coverage, and the simple COMM design — are real but insufficient to overcome the methodological rigor concerns at the current stage.

**Score breakdown:**
- Research value / Contribution: 6.5/10 (useful empirical findings, incremental method)
- Validity / Soundness: 5.0/10 (no variance, confounded comparison, incomplete baselines)
- Novelty: 6.0/10 (encoder comparison is relatively novel; fusion method is incremental — deferred to manual verification due to Retrieval-Disabled Mode)
- Reproducibility: 6.5/10 (training recipe described but data mixture unspecified, MLP details in appendix)
- Presentation / Clarity: 6.5/10 (generally clear but introduction could be better structured)

---

**Post-Revision Target: [7.5, 8.2] / 10**

If the authors address the P0 issues (add multi-seed variance, resolution-controlled ablation, fix unsupported claims, and add limitations), the paper would achieve a solid 7.5-8.0. Adding P1 items (missing baselines, OOD tests, improved narrative) could raise this to 8.0-8.2. The main path to a higher score requires demonstrating that the COMM fusion mechanism contributes independently of the resolution advantage, and that the empirical rankings are statistically reliable. The paper's conceptual contribution — that visual encoder choice significantly affects MLLM fine-grained performance — is likely to stand after these fixes.
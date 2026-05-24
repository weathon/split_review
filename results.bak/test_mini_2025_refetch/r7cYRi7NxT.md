Now I have all the information needed. Let me write the final consolidated review.

## Summary

This paper introduces Hierarchical Side-Tuning (HST), a parameter-efficient transfer learning method that attaches a lightweight, pyramidal side network (HSN) to a frozen ViT backbone. The HSN uses cross-attention with linear complexity to ingest intermediate backbone features and generates multi-scale outputs suited for both recognition and dense prediction tasks. HST is evaluated on VTAB-1k classification (76.0%, 0.78M params), COCO detection/segmentation, and ADE20K semantic segmentation, achieving strong results that in some settings (Cascade Mask R-CNN) surpass full fine-tuning.

## Strengths

- **Novel and well-motivated architecture.** Unlike prior PETL methods that inject adapters into the backbone or prepend prompts, HST separates tunable parameters into a hierarchical side network with a feature pyramid. This design is particularly well-suited for dense prediction tasks, which require multi-scale representations — a natural fit that prior PETL work has struggled with. The architectural motivation is clearly articulated.

- **Strong dense-prediction results.** On COCO with Cascade Mask R-CNN (Table 2), HST achieves 49.7 box AP and 43.2 mask AP, outperforming full fine-tuning (48.7/42.2) for the first time among PETL methods. Gains over other PETL baselines (VPT, AdaptFormer, SSF, LoRA) are consistent and substantial — e.g., +2.8 AP^b over LoRA with Cascade Mask R-CNN, and +4.9 AP over SSF on Mask R-CNN 3×. These results are the paper's strongest evidence: the comparisons use the same detection heads for all methods, so the comparison is fair.

- **Clean, informative ablation studies.** Table 5 provides a clear progression from a bare HSN (72.1%/30.0 AP^b) to the full HST (76.0%/40.5 AP^b), isolating the contribution of each component. The large jump from HST.c to HST (+0.8%, +5.5 AP^b, +5.0 AP^m) cleanly demonstrates the importance of fine-grained injection. The finding that linear weight sharing reduces parameters from 1.10M to 0.78M without harming performance is non-trivial and well-documented.

- **Linear-complexity cross-attention.** Section 3.4 derives O(LdM) complexity for the Side block's cross-attention, noting that d, M ≪ L, yielding effective O(L) scaling. This is supported by efficiency measurements (Figures 7–8) showing training memory (~8.5 GB) below full fine-tuning (~10.5 GB) and competitive inference speed.

- **Consistent gains across multiple task families.** HST is evaluated on 19 VTAB-1k tasks (classification), COCO (detection + instance segmentation with 3 detectors), and ADE20K (semantic segmentation with 2 decoders). This breadth of evaluation — especially the dense-prediction component — exceeds most prior PETL papers, which focus primarily on classification.

## Weaknesses

### Major

- **Unexplained VTAB-1k full fine-tuning baseline.** The paper reports full fine-tuning at 65.57% average on VTAB-1k (Table 1). The VPT paper (Jia et al., 2022), which is cited as the source ("Full fine-tuning (2022)"), reports 68.9% for the same ViT-B/16 with ImageNet-21k pretraining — a 3.3% gap. This discrepancy is never acknowledged or explained. The headline claim ("10.4% improvement over full fine-tuning") is inflated relative to the established baseline; at 68.9% the improvement would be 7.1%, which is still impressive but significantly less dramatic. The paper must either reproduce full fine-tuning in its own setup and explain any differences, or adopt the standard reported baseline. Without this, the VTAB-1k comparison is unreliable and the paper's central quantitative claim is undermined.

- **No variance or error bars reported anywhere.** VTAB-1k uses only 1,000 training examples per task; results can fluctuate substantially across runs. Every other recent PETL paper on VTAB-1k reports standard deviations or multiple seeds. The absence of any variance reporting makes it impossible to assess whether the reported improvements over baselines (e.g., +2.9% over SSF, +3.75% over LoRA) are statistically significant or within noise. This is especially important given the small-data regime of VTAB-1k. At minimum, the aggregate average should include variance over 3+ runs.

### Minor

- **Classification head for VTAB-1k not explicitly specified.** The paper describes how HST generates multi-scale features via the HSN, but does not state what classification head is used for VTAB-1k tasks. Figure 2 shows a "CLS token" output, suggesting a standard linear classifier on the [CLS] token. However, this should be explicitly stated — if HST uses a different head architecture (e.g., pooling pyramid features + MLP) than the linear probes used by baselines, the comparison would be unfair. The ablation baseline "ViT-B w/. HSN" at 72.1% (Table 5) already exceeds the reported full fine-tuning (65.57%), which is suspicious and could indicate a decoder advantage. Specifying the head resolves this ambiguity.

- **Channel dimensions of HSN stages not disclosed.** The paper states that HSN has four stages with downsampling rates {4, 8, 16, 32} and aligns the number of Side blocks with ViT blocks (line 63), but never gives the channel dimension at each stage. This is needed to verify the 0.78M parameter count and to understand the capacity of the side network relative to the backbone.

- **Parallel computation claim is not substantiated.** The Introduction claims that "computations for the same level of the backbone network and HSN can be performed in parallel" (line 23), but the architecture description makes clear that each Side block i depends on the output of ViT block i. Pipelining (running Side block i concurrently with ViT block i+1) is possible but is not analyzed or measured. The paper would benefit from a latency breakdown showing actual parallelization gains.

### Trivial

None.

## Nice-to-Haves

- Add a control baseline on VTAB-1k where a frozen backbone is paired with a lightweight multi-scale decoder (without the side-network training) to isolate the architectural benefit of multi-scale features from the side-network tuning mechanism.
- Report FLOPs per stage for the HSN vs. the backbone to strengthen the efficiency argument.
- Discuss the counter-intuitive finding (Table 5) that linear weight sharing improves over multiple linear layers — is this a regularization benefit?

## Removed Points

- *"Computations can be performed in parallel claim is not supported"* — The paper's claim about parallelism (pipelining Side block i with ViT block i+1) is architecturally plausible. Demoting from a weakness to an unsubstantiated claim; moved to Minor Weaknesses with amended framing.
- *"Missing hyperparameters / reproducibility details / code"* — Removed per policy: hyperparameter details are deferred to appendix (which was stripped by the parser); this is standard practice.
- *"Missing related work"* — Removed per policy: I cannot verify missing citations without external sources.
- *"Poor writing/formatting"* — Removed per policy: formatting artifacts are parser issues.
- *"Inference FLOPs not reported"* — Moved to Nice-to-Haves.
- *"Side network with only linear head baseline needed"* — Moved to Nice-to-Haves.
- *Strength Finder's generic strengths* — Removed generic claims like "this paper addresses an important problem"; only kept concrete, evidence-grounded strengths.

## Novel Insights

The harsh critic's observation that the VTAB-1k "ViT-B w/. HSN" ablation baseline (72.1%) already exceeds the reported full fine-tuning (65.57%) by 6.5 points — before any LN-tuning, weight-sharing, global token, or fine-grained injection — is an insightful triangulation. This suggests that even the bare side network (with no proposed modules) provides a substantial decoder-like benefit on classification, which the standard [CLS]-token linear probe used by baseline methods does not have. This lends weight to the classification-head concern and implies that a nontrivial fraction of HST's VTAB-1k gain may come from architectural capacity rather than parameter-efficient tuning per se. The dense-prediction results, where all methods share the same detection/segmentation heads, are therefore the cleaner test of HST's tuning mechanism.

## Suggestions

1. **Address the full fine-tuning baseline.** Run full fine-tuning in your own environment with the same protocol (training schedule, optimizer, augmentations) used for PETL methods. Report the result and any discrepancy from the VPT (2022) reported value. If the number differs due to a different recipe, explain how and why.
2. **Add variance to VTAB-1k results.** Report mean and standard deviation over at least 3 independent runs for the aggregate average, and ideally per task.
3. **Explicitly describe the classification head.** State what head architecture is used for VTAB-1k (e.g., linear classifier on [CLS] token, or pooling multi-scale features + MLP). If HST uses a different head than baselines, acknowledge this and quantify its contribution.
4. **Report HSN channel dimensions.** Add the feature dimension of each of the four HSN stages to Table 5 or the architecture description.
5. **Soften the claim about full fine-tuning superiority on VTAB-1k** until the baseline is verified. The dense-prediction results (which use shared heads) are the paper's strongest selling point and should be given equal prominence.

## Score and Decision

**Calibration protocol:**

**Round 1 (Bracketing):** Three parallel queries against the human-review corpus.
- Low band (<3.5): retrieved papers with avg scores 2.5–3.0 (e.g., withdrawn papers with fundamental flaws). HST is clearly above these.
- Middle band (3.5–7.5): retrieved papers with avg scores 4.4–6.5 (Replacement Learning 4.4, PEL 5.25, Diffusion Few-shot 5.2, Proteus 6.5). HST sits within this band.
- High band (>7.5): retrieved papers with avg scores 8.0 (oral-level contributions like ViT Registers). HST is clearly below these.

**Round 1 bracket:** 5.0–7.0.

**Round 2 (Narrowing):** Two queries targeting the 4.5–7.0 and 5.0–7.5 ranges, retrieving PETL-specific anchors:
- **MLAE** (avg 5.33, Reject): LoRA variant evaluated only on VTAB-1k+FGVC. HST has broader evaluation and more architectural novelty → HST is stronger.
- **GLoRA** (avg 5.5, Reject): Unified LoRA framework, VTAB-1k + language. Comparable scope but less architectural novelty → HST comparable.
- **ADAPT** (avg 5.5, Reject): Adaptive prompt tuning for CLIP. Narrower scope → HST is stronger.
- **UniAdapter** (avg 5.75, Accept poster): Cross-modal adapter, very mixed reviews (8,3,6,6). Accepted after rebuttal → HST comparable but with a more concrete evaluative weakness.
- **Dense-JEPA** (avg 6.0, Reject): Self-supervised learning, strong eval, still rejected due to split reviews.
- **Lotus** (avg 6.4, Accept poster): Clean evaluation, well-received → HST is weaker (has the baseline issue).
- **Proteus** (avg 6.5, Accept poster): Clean paper, well-received → HST is weaker.

HST's core architecture is more novel than the LoRA variants (MLAE, GLoRA), and its dense-prediction evaluation is genuinely broader. However, it has a concrete evaluative weakness (unexplained VTAB-1k baseline) that these other papers do not share, and it lacks variance reporting. HST sits above the clearly rejected PETL papers (MLAE 5.33, GLoRA 5.5, ADAPT 5.5) but below the accepted papers with clean evaluations (Proteus 6.5, Lotus 6.4).

**Final score anchored at 5.5** — comparable to GLoRA (5.5, Reject) in overall quality but with different trade-offs: more architectural novelty and broader evaluation vs. a more significant evaluative weakness. The score is below UniAdapter (5.75, Accept) because UniAdapter's weaknesses were addressable in a rebuttal (clarifications), whereas HST's VTAB-1k baseline issue requires new experiments to resolve.

**Decision: Reject** — the paper presents a genuinely interesting architecture and strong dense-prediction results, but the unexplained VTAB-1k full fine-tuning baseline discrepancy, combined with the absence of any variance reporting, prevents acceptance in the current form. The core contribution is promising and the authors are encouraged to address these issues in a revision.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>
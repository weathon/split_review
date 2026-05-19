Now let me run the calibration search to bracket this paper appropriately.Based on round 1, my initial bracket is **5–7**. ProPETL and Conv-LoRA (both at 6.0) are the most topically relevant anchors. Now let me narrow within the bracket.Now I have enough information to write the final review. Let me synthesize everything.

---

## Summary

Hierarchical Side-Tuning (HST) introduces a lightweight Hierarchical Side Network (HSN) that ingests intermediate ViT activations at multiple depths and produces a multi-scale feature pyramid. This enables parameter-efficient transfer learning that is effective not only on image classification (VTAB-1K: 76.1% with 0.78M params, beating all PETL baselines) but also on dense prediction tasks (COCO Mask R-CNN: 43.9 AP^b, within 1.2 of full fine-tuning; ADE20K UperNet: 47.5 mIoU +MS) — substantially closing a gap where previous PETL methods lag full fine-tuning by 5–9 AP. The architecture is built around a Meta-Register token (with LN-tuning for distribution alignment), a Transformation Bridge with linear-weight sharing, and a Side Block using cross-attention with linear complexity.

---

## Strengths

- **VTAB-1K state-of-the-art with extreme parameter efficiency.** Table 1 shows HST-B achieves 76.12% average Top-1 accuracy with only 0.78M trainable parameters — +10.5% over full fine-tuning (65.57%), surpassing the previous best PETL methods (SSF 73.10%, NOAH 73.20%, AdaptFormer 73.10%). Gains are particularly striking on structured tasks (Clevr/count: +6.9%, dSprites/loc: +5.4%, SmallNORB/ele: +7.9%).

- **Substantial narrowing of the dense prediction gap.** Table 2 (Mask R-CNN 3×+MS) shows HST at 43.9 AP^b vs. full fine-tuning's 45.1 — a gap of 1.2 AP^b — while the best prior PETL method (LoRA-32) lags by 5.8 AP^b. On Cascade Mask R-CNN, HST actually exceeds full fine-tuning (+0.8 AP^b, +0.8 AP^m). This is a concrete and well-evidenced contribution.

- **Single Meta-Register token eliminates prompt-length search.** Table for Number of Meta-Register (abl:num_mr) shows 1 token (76.1% VTAB-1K, 40.3 AP^b) performs nearly identically to 32 tokens (76.2%, 40.4 AP^b), unlike VPT where prompt count requires per-task tuning. This is a clean design advantage with empirical support.

- **Linear-weight sharing reduces parameters and improves accuracy simultaneously.** HST.b (weight sharing, 0.78M) outperforms HST.a (no sharing, 1.10M) at 75.0% vs. 74.3% on VTAB-1K (Table abl:component). The shared layers enable implicit cross-layer feature fusion.

- **Linear-complexity cross-attention.** Eq. (3) uses Meta-Global tokens as K and V (only 2 tokens), yielding O(2Ld) complexity — linear in sequence length L — rather than the standard O(L²d). This is a concrete and verifiable efficiency advantage built into the Side Block design.

- **Robustness to pretraining strategy.** Under MAE pretraining (Table tab:fgvc), all other PETL methods (Adapter, Bias, VPT) fall substantially below full fine-tuning, while HST maintains the smallest gap — surpassing full fine-tuning on Stanford Dogs (86.4% vs. 84.6%) and Oxford Flowers (91.2% vs. 90.9%), and outperforming all PETL methods on every MAE-pretrained dataset.

---

## Weaknesses

### Fatal
None.

### Major

- **Section 4.4 ("Efficiency Analysis") is completely empty.** Lines 376–378 of the paper show the subsection heading is immediately followed by the next subsection with zero content in between. This is not a stripped appendix — it is a missing section in the main paper body. For a PETL paper whose core claim includes "improving training and inference efficiency" (Section 3.3) and "linear complexity" cross-attention, the absence of quantitative efficiency data (GPU memory, FLOPs, training time vs. LoRA/full fine-tuning) is a substantive omission. The efficiency claim remains entirely unsubstantiated.

- **Incomplete baseline comparison for ViT-L detection (Table 2).** The ViT-B comparison includes 6 methods (full fine-tuning, linear probing, VPT-deep, AdaptFormer, SSF, LoRA-32, HST), but the ViT-L section includes only 4 (full fine-tuning, linear probing, LoRA-64, HST) with no explanation for the absence of VPT-deep, AdaptFormer, and SSF. The paper's claim that "HST performs more satisfactorily on larger models" (Section 4.2) rests on an incomplete comparison, since it is unknown whether the missing baselines would perform differently at ViT-L scale.

### Minor

- **Parameter accounting for dense prediction entangles head/neck with backbone adaptation.** Section 4.1 explicitly acknowledges that "neck modules like FPN also adopt dimensions of [64, 128, 256, 384], which sets them apart from other methods where neck modules maintain ViT's dimensions, thus requiring fewer training parameters." This means a portion of HST's apparent PETL advantage in detection/segmentation comes from a lighter FPN head (since baselines must maintain ViT's 768-dim FPN), not solely from the PETL mechanism. The paper acknowledges this in one sentence but does not provide a decomposed parameter table (backbone-side vs. head/neck) that would allow readers to cleanly isolate the contribution of the PETL mechanism per se.

- **LN-tuning attribution in ablation is incomplete.** Table abl:component shows HST.a (+LN tuning alone) gains +2.2% VTAB-1K and +2.8 AP^b over the HSN-only baseline. The paper attributes this gain to enabling Meta-Register alignment. However, none of the ablation configurations test "LN tuning with no Meta-Register token" vs. baseline, making it impossible to separate whether the gain comes from LN-tuning improving frozen ViT transferability independently, or from LN-tuning specifically enabling Meta-Register integration.

### Trivial

- The observation that HST under MAE pretraining outperforms other PETL methods is presented in a single short paragraph and deserves more analytical depth (e.g., why does the hierarchical side network degrade more gracefully under self-supervised pretraining?).

---

## Nice-to-Haves

- **Scale-stratified detection AP.** A comparison of AP_S, AP_M, AP_L between HST and the best backbone-internal baseline (LoRA) would directly test the paper's multi-scale hypothesis — if gains concentrate in small-object AP (AP_S), this would strongly confirm that the hierarchical multi-scale design is the proximate cause of the dense-prediction improvement.

- **Extending MAE results to dense prediction.** Table tab:fgvc demonstrates HST's advantage under MAE pretraining for classification; extending this to detection or segmentation with MAE-pretrained ViT would sharpen the structural claim that separating adaptation from the backbone provides cross-pretraining robustness.

---

## Removed Points

*These points are flagged for removal; treat them with caution.*

- **"VTAB-1K vintage" framing concern (Harsh Critic):** The criticism that claiming "state-of-the-art in 13 out of 19 tasks" is "overstated without acknowledging the comparison set's vintage" is not a valid weakness — all venue papers compare to contemporaneous published baselines. Removed.

- **LN-tuning cosine similarity visualization thin evidence (Harsh Critic):** This is a minor presentation choice. Qualitative cosine similarity figures supporting the LN-alignment motivation are a reasonable form of evidence for a design decision. Removed as a weakness; absorbed into the minor ablation comment above.

- **Strength Finder claim about MAE CIFAR-100:** The Strength Finder states HST "achieves 79.7% on CIFAR-100 surpassing full fine-tuning (88.9%)." This is factually wrong — 79.7% < 88.9%. The accurate characterization is retained above (HST outperforms all PETL methods but is below full fine-tuning on CIFAR-100 under MAE).

- **"Strengthening the Paper on Its Own Terms" suggestions from Harsh Critic:** Scale-stratified AP and MAE extension are incorporated as Nice-to-Haves, not weaknesses.

---

## Novel Insights

The most under-exploited finding in this paper is the interaction between pretraining strategy and PETL method effectiveness. Table tab:fgvc shows that backbone-internal PETL methods (Adapter, Bias, VPT) all fail significantly under MAE pretraining while HST holds up. This is not just a robustness claim — it is a structural observation: when the pretraining features are not naturally aligned with discriminative classification cues (as in MAE's reconstruction-based pretraining), methods that insert lightweight parameters inside the backbone are unable to compensate. The hierarchical side network, by constructing its own feature hierarchy from intermediate activations rather than modifying backbone internals, appears to provide a form of isolation from pretraining idiosyncrasies. This deserves to be a first-class theoretical result rather than a secondary observation.

---

## Suggestions

1. **Complete Section 4.4.** At minimum: training memory and wall-clock time for HST vs. LoRA vs. full fine-tuning on Mask R-CNN; inference FLOPs/latency on COCO and VTAB-1K. The linear-complexity cross-attention claim should be quantified.
2. **Add all ViT-B baselines to the ViT-L comparison**, or state explicitly that certain methods were not run at ViT-L scale and why.
3. **Add a parameter decomposition table** for dense prediction settings showing (a) backbone-side parameters and (b) head/neck parameters for HST and each baseline, so the PETL mechanism contribution can be isolated from the head redesign effect.
4. **Add one ablation row**: HSN-only + LN tuning but with no Meta-Register token, to cleanly attribute the LN-tuning gain.

---

## Score and Decision

**Calibration:**

**Round 1 anchors:**
- WM5G2NWSYC (Projected Subnetworks, PETL, avg 2.0, Reject) — far weaker, no strong results
- TxIrMD6lAN (Incremental Learning with Adapters, avg 3.0, Reject) — different problem, weaker results
- YNbLUGDAX5 (ProPETL for Segmentation, avg 6.0, Accept) — same problem space, similar contribution scope
- Fb93MfxX7T (PETL empirical study, avg 4.75, Reject) — empirical study, no new method
- ezscMer8L0 (Conv-LoRA for SAM, avg 6.0, Accept) — PETL for segmentation, similar results
- bJx4iOIOxn (VPT analysis, avg 7.5, Accept) — analytical paper, broader theoretical contribution
- 2dnO3LLiJ1 (ViT Registers, avg 8.0, Accept) — significantly stronger, more rigorous, broader impact

**Round 1 bracket: 5.5–7.0**

**Round 2 anchors:**
- vJkktqyU8B (META, Memory Efficient ViT Adapter for Dense Predictions, avg 6.0, Accept) — most topically aligned; addresses same PETL-for-dense-prediction gap; also had efficiency analysis concerns from reviewers; HST has broader evaluation and stronger performance deltas
- YNbLUGDAX5 (ProPETL, avg 6.0, Accept) — same problem but restricted to segmentation; HST covers more benchmarks
- ezscMer8L0 (Conv-LoRA, avg 6.0, Accept) — PETL for single foundation model, narrower scope than HST

**Round 2 comparison:** HST is most similar to META (6.0), ProPETL (6.0), and Conv-LoRA (6.0) in terms of contribution scope, empirical strength, and gap patterns. HST covers more tasks and benchmarks than any of these, and its detection results are particularly impressive (within 1.2 AP^b of full fine-tuning). The empty efficiency section is a real gap analogous to efficiency concerns in the comparison papers, which did not prevent acceptance. The incomplete ViT-L comparison is a fairness concern not seen in the comparison papers but not fatal. On balance, HST is at the same tier as META, ProPETL, and Conv-LoRA — all solid 6.0 papers with strong empirical contributions and methodological gaps.

| Anchor | Score | Comparison to HST |
|--------|-------|-------------------|
| WM5G2NWSYC (Projected Subnetworks) | 2.0 | Much weaker — no strong results |
| Fb93MfxX7T (PETL empirical study) | 4.75 | No new method, weaker contribution |
| vJkktqyU8B (META adapter) | 6.0 | Most topically similar; HST slightly stronger empirically |
| YNbLUGDAX5 (ProPETL) | 6.0 | Same problem; HST broader scope |
| ezscMer8L0 (Conv-LoRA) | 6.0 | Narrower scope; HST broader |
| bJx4iOIOxn (VPT analysis) | 7.5 | HST weaker theoretically; analytical depth lower |
| 2dnO3LLiJ1 (ViT Registers) | 8.0 | Much stronger; broader impact, rigorous analysis |

**Final score: 6.0** — comparable to the three round-2 anchors that are the most topically aligned (META, ProPETL, Conv-LoRA). HST is not better enough than these to reach 6.5, given the empty efficiency section and incomplete ViT-L comparison; it is not worse enough to fall below 6.0, given the breadth and strength of its empirical results.

**Axis evaluation:**
- *Originality:* Moderate-high. Hierarchical side network for PETL is novel; combines known components (cross-attention injection, side tuning, feature pyramid) in a well-motivated way.
- *Importance of research question:* High. Bridging PETL to dense prediction is a genuine open problem.
- *Claims well-supported:* Moderate-high. Core empirical claims are well-supported; efficiency claims are not.
- *Soundness of experiments:* Moderate. Strong across most benchmarks; incomplete for ViT-L.
- *Clarity of writing:* Moderate. Section 4.4 is empty; parameter decomposition is unclear.
- *Value to research community:* High. Strong baselines on VTAB-1K, COCO, ADE20K under parameter-efficient conditions.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>
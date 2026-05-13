Now let me synthesize my review based on careful reading of the paper and the harsh/soft reviewer inputs.

## Summary

Hydra-SGG introduces a Hybrid Relation Assignment for one-stage DETR-based scene graph generation that combines One-to-One (Hungarian matching) and IoU-based One-to-Many relation assignment to address sparse supervision. It also proposes a Hydra Branch—an auxiliary self-attention-free decoder that shares parameters with the main decoder during training and is discarded at inference—which synergizes with One-to-Many Assignment by encouraging duplicate predictions. The method achieves 16.0 mR@50 on VG150 in just 12 epochs, claims SOTA on three benchmarks, and adds zero inference overhead.

## Strengths

- **Well-motivated core idea with clear quantitative backing**: The sparse supervision problem (only ~2.75% of queries are positive in RelTR) is concretely quantified, and Hybrid Assignment increases positive samples by 65.5% on VG150 train (Fig. 4a–b, §3.2). The One-to-Many assignment directly addresses this documented bottleneck.

- **Clean ablation showing contribution of both components**: Table 4a isolates Hybrid Assignment (+2.0 mR@50 over baseline) and Hydra Branch (further +1.1 mR@50), confirming both are non-redundant and genuinely additive rather than merely correlated improvements.

- **Zero inference overhead from Hydra Branch**: The auxiliary branch shares all parameters with the main decoder (Eq. 5–6) and is discarded at inference, yielding comparable model size (67.6M) and speed (5.3 FPS) to RelTR (63.7M, 6.5 FPS). This is a practical advantage.

- **Novel empirical finding about self-attention and duplicate predictions**: The Diversity Score analysis (ADS 6.6 with self-attention vs. 4.6 without, Fig. 4c) and qualitative visualizations (Fig. 4d–e) provide novel evidence that self-attention reduces duplicate relation predictions in DETR-based SGG, motivating the Hydra Branch design.

## Weaknesses

### Fatal
None.

### Major

- **The contribution of Hybrid Assignment cannot be cleanly separated from bundled DETR infrastructure improvements**: Section 5.1.4 (line 262) states the baseline and proposed models incorporate "anchor boxes, training techniques, and attention mechanisms as used in recent works [RelTR, DAB-DETR, DN-DETR, DINO]." These enhancements (anchor queries from DAB-DETR, denoising from DN-DETR, contrastive/query-denoising from DINO) are known to substantially boost DETR convergence and performance. The paper does not enumerate which specific techniques are included, and the compared prior methods (RelTR, SGTR, ISG, SpeaQ) predate or do not incorporate these enhancements. The baseline at 50 epochs (12.9 mR@50) already exceeds RelTR at 150 epochs (10.8 mR@50) by a large margin, suggesting the DETR infrastructure alone accounts for a significant share of the improvement. Without reporting a baseline without DINO/DN-DETR techniques, the paper cannot establish how much of the +3.1 mR@50 gain (and the convergence speedup) comes from Hybrid Assignment versus from these well-known architectural upgrades. This compromises the core claim attribution.

- **Convergence acceleration claim lacks matched-epoch baseline comparison**: The paper's central narrative is that Hybrid Assignment enables convergence in 12 epochs (vs. 150 for RelTR). However, Table 4a compares the baseline at *50 epochs* (12.9 mR@50) against Hydra-SGG at *12 epochs* (16.0 mR@50). The baseline's performance at 12 epochs is never reported. Given that the baseline already incorporates DINO-style improvements known to accelerate DETR convergence, it is plausible the baseline also converges much faster than the 150-epoch RelTR. Without the baseline learning curve or same-epoch comparison, the claim that *Hybrid Assignment* (rather than the underlying DETR infrastructure) drives the fast convergence is unsupported. This is directly fixable: report baseline mR@50 at 12 epochs and plot both learning curves.

- **R@50 is substantially below several compared methods, yet this trade-off is not discussed**: On VG150, Hydra-SGG achieves 28.4 R@50, which is notably below DSGG (32.9), SpeaQ (32.9), EGTR (30.2), and even RelTR (27.5). Meanwhile, its mR@50 (16.0) leads. This R↓/mR↑ pattern is characteristic of debiasing effects. One-to-Many Assignment may incidentally act as a debiasing strategy by providing supervision to rare predicates starved of positive assignments. The paper does not discuss this trade-off or its mechanism, presenting only the favorable metric. The abstract claims "state-of-the-art" without acknowledging the R@50 deficit.

### Minor

- **No ablation on the top-k parameter in One-to-Many Assignment**: The paper selects top-6 queries per ground truth (line 178) but only studies threshold T (Table 4c). Since top-k directly controls how many positive samples each GT receives, sensitivity to this parameter is important. Testing top-k ∈ {2, 4, 6, 8} alongside T would strengthen confidence in the method's robustness.

- **Shared prediction heads receive potentially conflicting gradient signals**: L_o2o (from the main decoder with self-attention) encourages diverse predictions, while L_o2m (from the Hydra Branch without self-attention) encourages duplicate predictions to the same GT. Both losses backpropagate through shared heads. The paper does not analyze whether this creates optimization tension. Even a simple gradient magnitude comparison or loss-weighting ablation would address this concern.

- **Epoch ablation shows incomplete convergence at 12 epochs**: Table 4d shows mR@50 goes from 16.0 (12 ep) → 16.1 (21 ep), a slight improvement. While the paper frames 12 epochs as "convergence," the model has not fully plateaued. The "converges in 12 epochs" statement is slightly overstated—though the marginal gain of 0.1 mR@50 may not justify 75% more training.

### Trivial
None.

## Nice-to-Haves

- Report baseline performance at 12 epochs alongside Hydra-SGG at 12 epochs, and ideally plot learning curves for both, to clearly establish convergence acceleration from Hybrid Assignment alone.
- Provide a control experiment applying Hybrid Assignment to the vanilla RelTR architecture (without DINO/DN-DETR enhancements) to cleanly isolate the assignment strategy's contribution.
- Include per-predicate mR breakdown to reveal whether One-to-Many Assignment specifically improves tail predicates, which would clarify whether the R↓/mR↑ pattern is an implicit debiasing effect.
- Explicitly enumerate which DAB-DETR/DN-DETR/DINO techniques are incorporated in the baseline model.

## Removed Points

*These points are flagged to be removed, treat them with caution.*

- **Criticism that DSGG's backbone is unverifiable/unfair**: The paper itself acknowledges this concern (line 271: "the backbone model employed by DSGG is not disclosed in their paper"), so the reviewer's point is addressed by the authors. However, this is about a competitor, not about Hydra-SGG's methodology, so it doesn't weaken the paper.

- **"50% of plausible but suboptimally matched queries" statistic is architecture-specific and may not transfer**: This statistic is cited from [kim2024groupwise] (SpeaQ), a published source. Questioning whether it transfers without evidence is speculative criticism.

- **GQA comparison has only three baselines and none are one-stage**: The paper reports results against available competitors on GQA. The absence of one-stage GQA methods reflects the state of the literature, not a methodological flaw in the paper. Criticizing incomplete baselines when the comparison is already limited by what exists is scope creep.

- **DS metric lacks variance or statistical testing**: Demanding statistical tests for a simple aggregate metric comparison (ADS 6.6 vs 4.6) is not standard practice in the SGG community. The qualitative visualizations (Fig. 4d–e) provide supporting evidence beyond the single number.

- **Request for confidence intervals or statistical testing on large benchmarks**: Not standard in the SGG field for benchmark evaluation.

- **Formatting/style nitpicks**: Removed per rules.

- **Missing proofs in appendix**: The parser strips appendices; these likely exist in the original submission.

## Novel Insights

The most insightful observation across the reviews is the R↓/mR↑ divergence and its potential interpretation as implicit debiasing. The paper's One-to-Many Assignment increases supervision for all matching queries, which by construction disproportionately benefits rare predicate categories that would otherwise receive few or no positive assignments under strict One-to-One matching. This provides an alternative (or complementary) explanation for why mR improves so dramatically while R does not: the method is shifting the model's prediction distribution toward rarer predicates. This is a genuinely interesting mechanism that the paper implicitly exploits but does not name or analyze, and formally studying it would reveal whether Hybrid Assignment is an accidental but effective debiasing strategy.

## Suggestions

- Report the baseline model's mR@50 at 12 and 21 epochs (same epoch counts as Hydra-SGG) to directly substantiate the convergence acceleration claim.
- Add a row in the ablation table for "Baseline (Vanilla DETR, no DAB/DN/DINO enhancements)" to isolate the contribution of the proposed assignment from infrastructure improvements.
- Discuss the R@50 vs. mR@50 trade-off explicitly, ideally with a per-predicate breakdown showing which categories benefit most from One-to-Many Assignment.

## Score and Decision

The paper presents a well-motivated and empirically effective approach to sparse supervision in DETR-based SGG. The core idea—hybrid assignment—is sound, the ablation demonstrates both components contribute, and the zero-inference-overhead Hydra Branch is a clever design. However, the paper has a significant attribution problem: the baseline bundles unenumerated DETR infrastructure improvements (DAB-DETR, DN-DETR, DINO), making it impossible to size the actual contribution of Hybrid Assignment versus well-known convergence tricks. The convergence acceleration claim lacks same-epoch baseline comparison, and the R@50 deficit versus prior work is undisclosed. These are major issues affecting core claims but do not invalidate the method—they undermine how confidently we can attribute the improvements.

**Originality**: High — the hybrid assignment and self-attention/duplicate-prediction insight are novel for SGG.  
**Importance**: High — sparse supervision is a real and significant bottleneck.  
**Claims support**: Moderate — the ablation supports the method works, but attribution is confounded by bundled enhancements.  
**Experimental soundness**: Moderate — missing matched-epoch baseline and top-k ablation weaken key claims.  
**Clarity**: Good — well-structured and clearly written.  
**Community value**: High — fast, effective one-stage SGG with zero inference overhead.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>
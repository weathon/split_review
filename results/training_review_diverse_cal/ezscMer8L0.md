Now I have all the verification I need. Let me produce the consolidated review.

## Summary

This paper proposes Conv-LoRA, a parameter-efficient fine-tuning (PEFT) method for SAM that inserts lightweight convolutional layers (managed by a Mixture-of-Experts gating mechanism for multi-scale selection) into LoRA's low-rank bottleneck. The method is evaluated across 14 binary segmentation tasks spanning medical, natural, agricultural, and remote sensing domains, plus multi-class semantic segmentation. Conv-LoRA consistently outperforms LoRA and six other PEFT baselines while adding only ~0.02M parameters (0.63% of total model parameters). The paper also provides analysis of SAM's local attention patterns and its degraded semantic capability due to binary-mask pretraining.

## Strengths

- **Consistent empirical improvement across diverse segmentation tasks with minimal parameter overhead.** Conv-LoRA achieves best or near-best scores on all 14 binary metrics in Table 1 (e.g., Kvasir $S_\alpha$: 92.0 vs. 91.2 LoRA; CAMO $F^\omega_\beta$: 84.0 vs. 82.8 LoRA) and on multi-class tasks in Table 2 (Trans10K hard mIoU: 84.37 vs. 83.95 LoRA), adding only 0.02M parameters beyond LoRA. The consistency across datasets from four domains and multiple task types is the paper's strongest empirical contribution.

- **Comprehensive evaluation with seven PEFT baselines and domain-specific comparisons.** The paper compares against BitFit, Adapter, VPT, LST, SAM-Adapter, SSF, and LoRA across binary and multi-class settings, establishing broad generality. Both domain-specific SOTA and "SAM trained from scratch" baselines are also included.

- **Useful analysis of SAM's properties.** The attention-distance analysis (Figure 3) provides evidence that SAM's segmentation pretraining shifts ViT attention from global to local patterns compared to MAE initialization. The linear probing experiment (SAM encoder 54.2% vs. MAE 67.7% on ImageNet-1K) quantifies SAM's degraded semantic capability. These insights are independently valuable for researchers working with SAM.

- **Ablation validates the motivation for multi-scale/adaptive design.** Table 4 shows the optimal single scaling ratio differs per dataset (ratio 4 best for Leaf; ratio 2 best for ISIC 2017), justifying the MoE-based dynamic selection mechanism over a fixed-scale design.

## Weaknesses

### Fatal

None.

### Major

- **Missing experimental comparison against Convpass, the most directly related prior work.** Convpass (Jie et al., 2022) also inserts convolutional operations inside a PEFT bottleneck adapter for ViT. The paper cites Convpass in Related Work and distinguishes itself by targeting SAM/segmentation and using multi-scale MoE, but it does not include Convpass as an experimental baseline. Without this comparison, it is impossible to determine whether the reported gains come from (a) the multi-scale MoE design specifically, or (b) the mere addition of convolution inside a LoRA-style bottleneck — which Convpass already demonstrated. This is the single most significant gap in the paper's novelty demonstration. Adapting Convpass to the SAM segmentation setting and comparing it directly would either strengthen the claim that MoE multi-scale adds value, or reveal that most of the gain comes from convolution alone.

### Minor

- **Headline empirical gains are modest and statistical significance is uncertain for individual metrics.** Improvements over LoRA are typically under 1 point (e.g., Road IoU: 62.2±0.21 → 62.6±0.36; CVC-612 $S_\alpha$: 90.7±0.04 → 91.3±0.69), and with only 3 runs, the reported standard errors are weak estimates of true variance, with some intervals overlapping. That said, the *consistency* across 14 metrics and diverse domains partially mitigates this concern — the language "clear performance boost" is slightly overstated but not baseless given the pattern of results. The authors could strengthen this by adding more runs or reporting bootstrapped confidence intervals, and by explicitly discussing effect size rather than relying on the pattern alone.

- **Claimed mechanism that Conv-LoRA "reinforces local prior" is not directly validated.** The paper shows that SAM's attention heads have shorter mean attention distances than MAE's (Figure 3), demonstrating that SAM's pretraining induces a local prior. However, it does not measure attention distances *after* finetuning with Conv-LoRA vs. LoRA to show that Conv-LoRA actually further shortens or sharpens local attention patterns. The mechanism is asserted but not directly tested — the performance improvements are consistent with it but don't isolate it.

- **Semantic recovery claim relies on indirect evidence.** The paper shows (a) SAM's encoder has weaker semantic features via linear probing, and (b) PEFT finetuning improves mIoU on multi-class tasks. This is reasonable circumstantial evidence, but multi-class mIoU improvement conflates better task-specific adaptation with genuine semantic recovery. A linear probing experiment on the encoder *after* PEFT finetuning would directly test whether Conv-LoRA recovers semantic classification capability in the encoder features.

- **MoE vs. multi-scale ablation has a confound.** Table 3 compares MoE (top-1 expert selection with learned gating) against multi-scale fusion (simple addition of all scales equally). The comparison conflates sparse dynamic selection with learned vs. unlearned weighting. A learnable weighted-sum baseline (e.g., attention-based fusion with comparable parameter count) would isolate whether the improvement comes from dynamic selection or simply from having a learned gating function. The efficiency advantages (1.54× speedup, 1.7 GB less memory) are clean and unaffected by this confound.

### Trivial

None.

## Nice-to-Haves

- Report inference FLOPs or throughput to support the "ultra-lightweight" efficiency claim beyond parameter count.
- Visualize the MoE gating behavior on example images (e.g., which expert is selected for small vs. large objects) to illustrate that dynamic scale selection works as intended.
- Analyze the design choice of applying convolution to the low-rank features (dimension $r$) vs. to the full-rank features after expansion — this could affect the strength of the injected local prior.

## Removed Points

These points are flagged to be removed; treat them with caution.

- *Criticism about statistical significance framed as fatal.* The reviewer's framing that improvements are "questionable" with only 3 runs is too harsh given that the consistency across 14 benchmarks from 4 domains is itself meaningful evidence. However, the underlying concern about small margins and weak variance estimates is legitimate — kept in Minor at the appropriate severity.

- *Strength Finder's claim that "attention distance analysis validates Conv-LoRA strengthens local prior."* The attention distance analysis (Figure 3) compares SAM vs. MAE, not Conv-LoRA vs. LoRA after finetuning. This overstates what the figure actually shows. The performance results indirectly support the claim, but the strength as written conflates two different analyses.

## Novel Insights

The most interesting observation that emerges from triangulating the paper's evidence against the reviews is that the paper's *diagnostic* insights about SAM (attention distance patterns, semantic degradation from binary-mask pretraining) are arguably as novel as the method itself. The method (convolution in LoRA with MoE) is an incremental extension of Convpass + LoRA. But the analysis showing that SAM's supervised pretraining induces local attention patterns — the opposite of what the ViT literature expects from supervised pretraining — and that PEFT finetuning can recover semantic capability is a genuinely useful finding for the growing community working on SAM adaptation. The paper's strongest contribution may ultimately be the demonstration *that* PEFT of SAM's encoder works (and why), rather than the specific Conv-LoRA recipe.

## Suggestions

1. **Add Convpass as an experimental baseline** adapted to the SAM segmentation setting. This is the single highest-leverage addition — it will either validate the multi-scale MoE design or clarify the actual source of gains.
2. **Run 5–10 trials or report bootstrapped confidence intervals** for the main comparisons, and replace "clear performance boost" language with a discussion of effect sizes.
3. **Measure mean attention distances after finetuning** (LoRA vs. Conv-LoRA) to directly test whether Conv-LoRA further localizes attention patterns, supporting the claimed mechanism.
4. **Add a learnable weighted-sum baseline** (same parameter count as the gating network) to the MoE vs. multi-scale ablation to control for the learned weighting confound.
5. **Perform linear probing on the encoder features after PEFT finetuning** on the target domain to directly validate the semantic recovery claim.

## Score and Decision

This is a solid empirical paper with a sensible method, thorough evaluation, and useful diagnostic insights about SAM. The main gap — missing Convpass comparison — is significant but not fatal, as the paper does provide evidence that convolution in LoRA helps SAM segmentation, and the multi-scale MoE ablation and efficiency analysis go beyond what Convpass demonstrated. The paper's core claims are supported by consistent (if modest) gains across a diverse benchmark. With the Convpass comparison and stronger mechanism validation, this could become a strong contribution.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>
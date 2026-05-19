Now I have all the information I need. Let me produce the consolidated review.

## Summary

This paper conducts a systematic investigation of four visual encoder families (CLIP, DINOv2, MAE, DeiT) as the visual backbone in Multi-modal Large Language Models (MLLMs). The key empirical findings are: (1) shallow CLIP layers provide useful fine-grained information for grounding tasks, (2) the vision-only DINOv2 model, when equipped with a non-linear MLP alignment, can surpass CLIP on fine-grained perception tasks, and (3) MAE and DeiT perform poorly as MLLM visual backbones. Building on these observations, the paper proposes **COMM**, which fuses multi-level features from CLIP and DINOv2 using a learnable LLN-Layerscale merging strategy. Experimental results across visual grounding, object hallucination, VQA, and image captioning show consistent improvements over several baselines.

## Strengths

- **Systematic comparison of multiple vision encoder families under a controlled protocol (Section 3):** The paper evaluates CLIP, DINOv2, MAE, and DeiT using the same training protocol, architecture (Shikra-based, Vicuna-7B), and limited iterations (9400). Figure 2 quantitatively documents layer-wise REC/POPE/REG curves for each encoder, showing that MAE and DeiT underperform while DINOv2 can match or surpass CLIP on grounding. This goes beyond prior work that only considered CLIP variants.

- **Clear evidence that DINOv2 + non-linear MLP alignment is effective for fine-grained tasks (Tables 1, 2):** Table 1 shows DINOv2 w/ MFM reaches 72.8 Avg REC vs. CLIP w/ MFM's 70.0, and DINOv2 alone (54.8) already exceeds CLIP alone (47.3) on REC. Table 2 systematically ablates MLP depth and expansion ratio, demonstrating that a 2-layer MLP with ratio 4 or 8 is necessary and that a single linear layer degrades performance substantially (e.g., RefCOCO test-A drops from 86.5 to 76.5).

- **COMM achieves strong results across multiple benchmarks (Tables 3–6):** COMM-7B outperforms Shikra-13B and Qwen-VL-7B-Chat on REC by 4.87% and 3.10% average accuracy respectively, despite using a smaller LLM and less training data. On VQAv2 dev, COMM (81.04) surpasses LLaVA-1.5 (80.0) at matched 336×336 resolution. On hallucination (POPE), COMM beats Shikra and InstructBLIP on the Popular and Adversarial splits.

- **Multi-level feature merging analysis provides actionable insights (Section 3, Figure 3):** The paper evaluates five merging strategies (Mean(half), Mean(all), Layerscale, LLN-Layerscale, Conv-Layerscale) and shows that LLN-Layerscale improves both grounding and hallucination resistance over single-layer features, and that shallow CLIP layers (around layer 12) are better for grounding than the deep layer 23 used by Shikra.

## Weaknesses

### Fatal

None.

### Major

- **Uncontrolled resolution confound in main REC comparisons (Tables 3, 5, 6).** The paper trains COMM at 336×336 resolution while citing Shikra results (224×224) and several other baselines at lower resolutions. The paper explicitly states "Instead of 224 × 224 resolution currently used by existing MLLMs, we use 336 × 336 resolution" (line 151). Higher resolution yields more visual tokens and is known to improve fine-grained tasks. The paper does not include a controlled experiment isolating the effect of resolution from the fusion method — e.g., evaluating a CLIP-only baseline at 336×336 or COMM at 224×224. This is partially mitigated by the VQA comparison with LLaVA-1.5 (which also uses 336×336, and COMM still wins 81.04 vs 80.0 on VQAv2 dev), and by Table 1 which likely uses the reduced 224×224 setup (caption: "fewer training iterations"). However, for the REC results (Table 3) — where the largest gains are reported — the resolution confound is a genuine concern that undermines the claim that the gains come from the fusion method rather than simply having higher-resolution inputs.

- **No ablation isolating the fusion contribution under the full training configuration.** Table 1 compares CLIP w/ MFM, DINOv2 w/ MFM, and COMM, but this appears to be from the reduced analysis setup (9400 iterations, 224×224) as indicated by the caption "fewer training iterations." The full training pipeline uses 100K+ steps and 336×336 resolution. Without a direct comparison of CLIP-only, DINOv2-only, and COMM under the full training setup, it is unclear whether the fusion advantage replicates at scale. The absence of this controlled comparison weakens the primary claim about the value of fusing both encoders.

### Minor

- **Ambiguous training configuration for Table 1.** The caption states "CLIP baseline use the 23rd layer features, which follows Shikra but with fewer training iterations" — suggesting the reduced setup (9400 iterations, 224×224). However, the table reports metrics (MME CS/PS, VQAv2, OK-VQA, COCO CIDEr, Flickr30k CIDEr) that go beyond the evaluation described in the analysis section (which only mentions REC, REG, POPE). This ambiguity makes it unclear whether the ablation results reflect the reduced or the full setup, and whether the observed improvements from MFM and COMM fusion would hold under the high-resolution full training used for the main results.

- **MLP architecture for DINOv2 alignment not specified in the method section.** Section 4 (Architecture) describes the fusion pipeline but does not state the MLP depth or expansion ratio used for DINOv2 alignment. These details only appear in the ablation study (Table 2). For reproducibility, the chosen configuration should be stated in the method description.

### Trivial

- **Notation for LLN module.** The paper uses the notation "Linear(LN(...))" while naming the module "LLN" (which originally suggests Linear-LayerNorm). The ordering (Linear after LN) is consistent but could be briefly clarified on first use to avoid confusion.

## Nice-to-Haves

- **Computational cost discussion.** Using two ViT-L encoders (CLIP + DINOv2) and processing all 24 layers from one and 6 from the other adds significant compute. Reporting inference speed, GPU memory, and total training time relative to single-encoder baselines would help practitioners assess the cost-benefit tradeoff.

- **Variance or confidence intervals for main results.** Several improvements are modest in absolute terms (e.g., VQAv2 dev: 81.04 vs 80.0 for LLaVA-1.5). Reporting standard deviations across runs would improve statistical rigor.

- **Limitations section.** The paper concludes without discussing limitations (e.g., higher resolution's contribution, increased model complexity, potential feature overlap between CLIP and DINOv2, generalization beyond evaluated benchmarks). Adding a brief limitations paragraph would strengthen the paper's depth.

## Removed Points

- **Missing citation of concurrent work** (e.g., LLaVA-1.5 experiments with CLIP variants, Muffin, Fuyu) — removed per the hard rule that missing related works should not be mentioned.
- **Claim that the analysis is "motivational rather than directly predictive"** — removed because the paper acknowledges the reduced setup is for diagnostic purposes and separately runs full-scale experiments; this is standard practice, not a flaw.
- **"The paper does not discuss the impact of the resolution choice on comparison fairness"** — subsumed by the verified resolution confound weakness above; kept as part of that weakness rather than as a standalone point.
- **"The qualitative examples (Fig. 6-8) are illustrative but do not add much beyond quantitative evidence"** — this is a matter of opinion; qualitative examples serve a different purpose and are standard in MLLM papers.
- **Request for sensitivity analysis of LLN-Layerscale weight initialization** — this is a fine-grained ablation request beyond standard practice.

## Novel Insights

The most interesting observation that emerges from the interaction of the reviews is that the resolution confound and the missing full-training ablation point to the same underlying gap: the paper's central architectural claim (fusion of CLIP + DINOv2 is beneficial) is best supported by Table 1 (reduced setup, 224×224), while the main results (Tables 3–6) combine the fusion change with a resolution change, making it impossible to attribute the gains to the fusion alone. This is a standard but consequential evaluation design issue — the controlled experiment needed to support the headline claim exists only in a lower-fidelity setting, and the high-fidelity results do not include the appropriate single-encoder controls. Fixing this with a single additional experiment (e.g., a CLIP+MFM baseline at 336×336 under the full training pipeline) would substantially elevate the paper's credibility.

## Suggestions

1. **Add a controlled experiment isolating resolution from fusion.** Train a CLIP+MFM baseline at 336×336 under the full training pipeline and report REC, POPE, and VQA results. Additionally or alternatively, train COMM at 224×224. This single addition would resolve the most significant concern about the evaluation.

2. **Clarify Table 1's training setup explicitly.** State whether it uses the reduced analysis setup (9400 iterations, 224×224) or the full setup. If the former, note this clearly in the caption and preferably add a companion table under the full setup. If the latter, explain why the analysis section states "fewer training iterations."

3. **State the MLP configuration explicitly in Section 4.** Add a sentence specifying the deployed MLP depth and expansion ratio used in the main experiments.

4. **Add a brief limitations paragraph** discussing computational cost, the role of higher resolution, and the generalizability of the approach.

## Score and Decision

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>
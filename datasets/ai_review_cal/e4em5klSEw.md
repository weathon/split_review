- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 6, 5, 5
Now I have all the information I need. Let me compose the final consolidated review.

## Summary

This paper proposes Diversified Multiplet Upcycling (DMU), a method to build a Mixture-of-Experts (MoE) CLIP model without training from scratch. The key idea is to use Multistage Contrastive Learning (MCL) to fine-tune only the FFN layers across multiple stages, producing a set of diverse expert FFNs that are then assembled into a sparsely-gated MoE (CLIP-MoE). Experiments on zero-shot retrieval, classification, and as a vision encoder for LLaVA-1.5 show gains over direct fine-tuning, Sparse Upcycling, and Long-CLIP, with very low training overhead (<2.5 hours on 8 A100s).

## Strengths

1. **Clear and well-motivated method with strong empirical validation of the core design.** The ablation study (Table 3/lines 281-282) directly demonstrates that adding MCL stages 1 and 2 improves retrieval substantially (e.g., COCO I2T R@1: 62.6 → 65.0, COCO T2I R@1: 43.4 → 46.8), while the routing analysis (Figure 5/Fig~1) confirms all experts receive non-trivial token assignments. This provides evidence that the MCL-extracted experts contribute complementary information.

2. **Significant retrieval gains over strong baselines with dramatically lower training cost.** On ShareGPT4V, CLIP-MoE outperforms Long-CLIP on all COCO and Flickr30k retrieval metrics (e.g., COCO I2T R@1: 65.0 vs. 62.8) while using less than half the training time (2.5 hours vs. 6 hours, Section 5.4). On COCO T2I, CLIP-MoE achieves 46.8 vs. Long-CLIP's 46.3 for R@1, and the advantage widens on Flickr I2T (60.5 vs. 53.4).

3. **Plug-and-play improvement as a vision encoder in LLaVA-1.5.** Simply replacing the CLIP vision encoder with CLIP-MoE improves performance on most MLLM benchmarks (Table 2): for the 7B model, 4 of 5 metrics improve (VQAv2, TextVQA, POPE, MMBench); for the 13B model, 3 of 5 improve (MME, POPE, MMBench) with one tie (VQAv2). This demonstrates practical applicability without downstream adaptation.

4. **Data efficiency highlighted through comparison with from-scratch training.** CLIP-MoE, trained on a 1M subset of Recap-DataComp, achieves comparable or better per-task gains than CLIP-Recap (trained on the full 1.3B dataset) on several retrieval metrics (Table 4), while using <2% of the training compute. For example, Flickr T2I R@1 gain: +12.8 (CLIP-MoE) vs. +11.9 (CLIP-Recap).

5. **Case study on MMVP-VLM illustrates the improved fine-grained understanding.** The examples in Figure 6 show CLIP-MoE correctly distinguishing camera perspective, orientation, and spatial relations that vanilla CLIP confuses, providing concrete visual evidence of the method's effect.

## Weaknesses

### Fatal
None.

### Major

1. **Factual error in Table 1 caption and bolding: CLIP-MoE does NOT "consistently outperform all baselines across all tasks."** On Recap-DataComp-1M for COCO text-to-image retrieval (T2I), Sparse Upcycling achieves higher recall than CLIP-MoE at all three cutoffs (R@1: 45.8 vs. 45.2; R@5: 70.9 vs. 70.2; R@10: 79.9 vs. 79.4). Yet the CLIP-MoE row is fully bolded (line 205) and the caption (line 214) claims consistent superiority. This is a clear factual inaccuracy. The authors must correct the bolding, qualify the caption to note the exception, and provide a brief discussion of why Sparse Upcycling succeeds on this specific task/dataset combination. While the overall thesis is still well-supported by the remaining 21 of 24 metrics where CLIP-MoE is best, this error undermines trust in the presentation.

2. **The MLLM evaluation (Table 2) does not isolate the contribution of the MoE structure from fine-tuning on better data.** The only comparison is LLaVA-1.5 (OpenAI CLIP) vs. CLIP-MoE-LLaVA-1.5 (CLIP-MoE trained on ShareGPT4V). The improvement could partially come from fine-tuning the vision encoder on ShareGPT4V's higher-quality captions, regardless of MoE. Adding variants with a Direct-Fine-Tuned CLIP and a Sparse-Upcycled CLIP as vision encoders would clarify whether the MoE structure itself provides additional benefit beyond what fine-tuning on better data alone achieves.

### Minor

1. **Expert diversity evidence is limited to routing statistics.** The routing analysis (Figure 5) shows all experts receive non-trivial token assignments (no column is entirely dark blue), and the ablation confirms that additional MCL stages improve performance. However, the paper does not provide a quantitative measure of feature dissimilarity between experts (e.g., cosine distance between expert output distributions, Jensen-Shannon divergence, or per-concept activation analysis). While the current evidence is *suggestive* of diversity, it is not definitive.

2. **The choice of key hyperparameters (4 experts, 3 clusters per modality, top-2 routing) is not justified or ablated.** The paper does not explore how different numbers of experts, cluster counts, or top-K values affect the trade-off between performance and efficiency. An ablation on expert count would strengthen confidence in the design choices.

3. **No statistical significance or variance is reported.** Given the small training dataset (1M samples) and the stochasticity of clustering-based fine-tuning, single-run results may not be stable. Reporting at least mean and std over a few seeds would improve reliability.

4. **The FFN-only fine-tuning restriction in MCL is not ablated against full fine-tuning.** The paper freezes all parameters except FFN layers during MCL stages, motivated by efficiency. However, an ablation comparing FFN-only vs. full fine-tuning for expert extraction would verify that this restriction does not limit the diversity or quality of the resulting experts.

5. **Inference cost reporting is limited to activated parameter size (1.7×).** Reporting FLOPs, latency on a standard GPU, and peak memory during inference would give a more complete picture of the practical overhead.

### Trivial
- Hyperparameter details for baselines (learning rate, optimizer, warmup, weight decay) are not disclosed, hindering reproducibility.
- The paper briefly notes that CLIP-Recap uses a larger text encoder (Section 5.7) but this caveat could be more prominent when comparing data efficiency.

## Nice-to-Haves

- A systematic accuracy evaluation on the full MMVP-VLM benchmark rather than cherry-picked examples would strengthen the fine-grained understanding claim.
- An ablation comparing the 4-expert MCL-initialized MoE against a 4-expert Sparse Upcycling MoE (4 copies of the same fine-tuned FFN) would directly isolate the effect of MCL's diversity from simply having more parameters.
- Testing on an additional architecture (e.g., ViT-B/32) would strengthen the model-agnostic claim.
- A discussion of limitations (e.g., reliance on high-quality caption data, extra complexity of multi-stage training, competitive baselines on some tasks) would improve completeness.

## Removed Points

These points were flagged by reviewers but are removed with justification:

- **"Baseline deterioration signals unfair comparison"** — REMOVED. The paper *does* analyze this phenomenon directly (lines 265), attributing it to overfitting on the smaller fine-tuning dataset (1M vs. 400M samples). The explanation is consistent with observations from Long-CLIP, which the paper cites. The baselines are trained under the same conditions; the degradation is a property of the setting, not an artifact of poor tuning. The critic's claim that "the paper does not analyze this" is factually incorrect.

- **"First to introduce sparsely activated MoE into CLIP" may be too strong** — REMOVED. The paper qualifies this with "to the best of our knowledge" and explicitly cites and distinguishes CuMo as focusing on vision representation rather than the full CLIP model. This is a proper citation practice, not a weakness.

- **Cherry-picked case study** — REMOVED. The paper explicitly labels it as a case study showing examples from MMVP-VLM. It is complementary to the quantitative results, not a substitute for them.

- **"The MCL framework originally fine-tuned the entire encoder"** — REMOVED. The paper's decision to freeze all but FFN is a deliberate design choice, and the ablation study provides empirical validation that it works (more MCL stages improve performance). Whether full fine-tuning would work differently is a speculation, not a demonstrated flaw.

- **Missing related works** — REMOVED per policy (cannot verify external references).

- **Various formatting/style nitpicks** — REMOVED per policy.

## Novel Insights

None beyond the paper's own contributions. The harsh critic and strength finder largely recapitulate the paper's claims rather than contributing new analytical insights.

## Suggestions

1. **Correct the factual error in Table 1.** Un-bold the COCO T2I entries on Recap-DC where Sparse Upcycling outperforms CLIP-MoE, and revise the caption from "consistently outperforms all baselines across all tasks" to a precise statement noting the exception or framing the claim at the dataset level.

2. **Add MLLM baselines with Direct Fine-Tuned CLIP and Sparse Upcycling CLIP as vision encoders** in the LLaVA-1.5 setup (Table 2). This is the single most impactful addition to substantiate that the MoE structure itself contributes beyond fine-tuning on better data.

3. **Include a systematic diversity analysis** — e.g., compute Jensen-Shannon divergence between expert output distributions across a held-out set, or show which experts fire for specific visual concepts (color vs. texture vs. shape).

4. **Add variance estimates** (mean ± std over 3 seeds) for the main results, and **disclose all hyperparameters** for baselines to improve reproducibility.

5. **Consider an ablation on number of experts** (e.g., 2, 4, 8) with associated compute/performance trade-offs to justify the choice of 4.

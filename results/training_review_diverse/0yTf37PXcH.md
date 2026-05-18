Now I have all the information I need. Let me construct the final consolidated review.

## Summary

This paper proposes Arcana, a multimodal LLM with two components: (1) **MM-LoRA**, which allocates separate LoRA parameters to visual and language tokens within the LLM decoder to reduce modality interference, and (2) **QLadder**, a query-based adapter that adds a small number of learnable visual tokens to the frozen CLIP encoder to enhance visual representation. Arcana is evaluated on standard VQA and LVLM benchmarks with competitive results and thorough ablations validating each component's individual contribution.

## Strengths

1. **MM-LoRA's decoupled modality learning consistently improves over standard LoRA.** The β/γ ablation (Table 5) shows that MM-LoRA with β=0.25, γ=0.75 outperforms standard LoRA on all four benchmarks (TextVQA: +0.6, ScienceQA: +2.1, MMBench: +1.0, MME: +40). The design is clean: it splits the LoRA rank between visual and language tokens while keeping total parameters constant via β+γ=1.

2. **QLadder enhances visual perception with minimal overhead, outperforming costly dual-encoder methods.** Table 9 shows QLadder (+64 tokens) surpasses MOF (+256 tokens, an additional DINOv2 encoder) on MMVP (27.6 vs 27.1), MMBench (66.3 vs 60.1), and TextVQA (58.8 vs 56.5). Table 8 reports only 0.582 GB extra memory and a 0.11 tokens/s speed drop — genuinely lightweight.

3. **Competitive overall performance with a small model and limited data (~2M samples).** Tables 1 and 2 show Arcana (Vicuna-7B, ViT-L) often matches or exceeds models with larger vision encoders or more training data (e.g., Qwen-VL-Chat, mPLUG-Owl2), achieving top scores on VQAv2 (79.5), MMBench (67.4), SEED-Bench (63.2), LLaVA^W (72.7), and POPE (87.1).

## Weaknesses

### Fatal

None. The paper's core claims — that MM-LoRA and QLadder improve multimodal performance — are supported by controlled ablations and are not invalidated by the issues below.

### Major

1. **Overclaimed novelty in the conclusion.** The paper states that QLadder "demonstrates for the first time that with limited multimodal training data, retaining the capabilities of a pre-trained model and adding a small number of visual encoders can still enhance the performance" (Conclusion, final paragraph). This is not accurate: BLIP-2's Q-Former (cited in the paper) and numerous subsequent query-based adapters already showed that lightweight learnable modules on frozen encoders improve performance with limited data. The "for the first time" framing inflates what is an incremental but well-engineered contribution. The narrative needs to be scaled back to match what is actually demonstrated.

2. **The language understanding evaluation (Table 3) does not isolate MM-LoRA's effect.** The paper compares Arcana against LLaMA-2, LLaMA-2-Chat, WizardLM, and Vicuna-v1.5 on BBH, AGIEval, and ARC, concluding these results "further highlight the superiority of our approach" for language understanding. However, Arcana is trained on multimodal data plus text-only ShareGPT data, while the comparison models come from different training recipes. Without an ablation that removes MM-LoRA (or substitutes standard LoRA) while keeping training data identical, the results cannot be attributed to MM-LoRA — they may simply reflect the inclusion of text-only instruction data in Arcana's training mix. This claim is unsupported in its current form.

3. **The MOF comparison (Table 9) lacks sufficient transparency about experimental control.** The paper compares LLaVA-v1.5 + QLadder against LLaVA-v1.5 + MOF (DINOv2 fusion). The paper states "we conducted detailed experiments to directly compare Q-Ladder with the MoF method," but the table simply cites the original MOF paper without clarifying whether these numbers were reproduced in-house with identical data, training pipeline, and hyperparameters. If taken from the original paper, differences in training data, schedules, and settings could confound the comparison. Since the claim that "QLadder maintains performance across benchmarks while MOF degrades" is central to motivating QLadder over dual-encoder alternatives, this opacity weakens the evidence.

### Minor

1. **Attention map visualization (Fig. 5) is qualitative evidence for a semi-quantitative claim.** The paper asserts that MM-LoRA causes "a significant increase in attention to visual tokens in the middle and subsequent layers" and QLadder leads to "increased attention to visual tokens across all layers." These claims are based on a single example's attention maps with no aggregation, no error bars, and no quantitative metric. While such visualizations are common for illustration, the claims are presented as empirical findings about model internals. This is a minor issue because the paper's core quantitative results do not depend on these visualizations.

2. **The "data engine" is mentioned as a contribution but never described or evaluated.** The conclusion (final paragraph) states "we designed a data engine that uses diverse visual annotation models and large language models to generate captions rich in visual information," but no description, ablation, or evaluation of this data engine appears anywhere in the method or experiments. The limitations section reads "we plan to leverage our data engine" as future work, suggesting it was not used in the reported experiments. Including an unevaluated design as a contribution in the conclusion is misleading.

3. **Dismissal of Partial-LoRA without experimental evidence.** The related work (Section 2) states that "experiments with MM-LoRA have shown that directly increasing the learning space for visual tokens in the decoder does not improve the model's performance," referencing Partial-LoRA from InternLM-XComposer2 but providing no direct experimental comparison. While the β=1, γ=0 row in Table 5 (visual-only LoRA degrading performance) is consistent with this claim, a direct comparison with Partial-LoRA's specific formulation would strengthen the argument.

### Trivial

None.

## Nice-to-Haves

- **Quantify attention patterns:** Aggregate attention weights across at least 100–200 examples, showing mean attention to visual vs. language tokens per layer with error bars, to turn Fig. 5 into a quantitative finding.
- **Direct Partial-LoRA comparison:** Include InternLM-XComposer2's Partial-LoRA as a baseline in the MM-LoRA ablation table.
- **Language ablation with controlled LoRA:** Compare Arcana vs. a version with standard LoRA (same rank, same training data) on BBH/AGIEval/ARC to isolate MM-LoRA's effect.
- **Clarify "multimodal decoder" framing:** The term suggests an architectural departure from standard Transformers, but MM-LoRA operates within unchanged Transformer layers. A more precise term like "modality-decoupled LoRA" would better describe the contribution.

## Removed Points

- **Strength Finder's claim #4 ("Natural language understanding is preserved"):** This conflicts with the verified weakness (Major #2) that the language evaluation does not isolate MM-LoRA's effect. The strength is based on the same uncontrolled comparison. Moved to this section per the rule that when a strength and verified weakness disagree, the weakness wins.
- **Harsh critic's claim that MM-LoRA is "simply LoRA applied separately to visual and language tokens":** While this is an accurate description of the mechanism, the reviewer overstated this as a structural flaw. The paper does not claim a fundamentally new Transformer architecture — MM-LoRA is presented as a LoRA-based design that enables modality-specific learning spaces, which it demonstrably does. The paper's own framing is nuanced enough on this point. The core criticism is better captured by the "overclaimed novelty" item above (Major #1).

## Novel Insights

None beyond the paper's own contributions. The key insight — that decoupling LoRA parameters by modality within the LLM (MM-LoRA) and adding lightweight query tokens to the frozen visual encoder (QLadder) both improve multimodal performance — is well-validated by ablations. However, neither individual component is conceptually novel: modality-separated adapters and query-based pooling on frozen encoders have both been explored. The paper's value lies in combining them in a resource-efficient package and providing clean ablations.

## Suggestions

1. **Remove or substantiate the "for the first time" claim.** Replace it with honest framing: "QLadder shows that even with limited training data, adding a small number of learnable queries to a frozen encoder can improve performance, complementing prior approaches that use additional encoders or full fine-tuning."
2. **Add a controlled language-understanding ablation** comparing Arcana (with MM-LoRA) against a version with standard LoRA (same rank, identical training recipe) on BBH, AGIEval, and ARC. If MM-LoRA genuinely preserves language ability, this ablation would demonstrate it directly.
3. **Clarify the MOF comparison:** State explicitly whether MOF numbers were reproduced in the same pipeline or cited from the original paper. If reproduced, provide the experimental details. If cited, note any differences in data/pipeline and consider re-running to ensure a fair comparison.
4. **Either remove the data engine from the conclusion or provide a description + ablation.** As written, it appears as an unevaluated contribution, which undermines trust.
5. **Add quantitative attention analysis** or soften the claims about "significant increase" to reflect the qualitative nature of the evidence.
6. **Consider adding a direct comparison with Partial-LoRA** to support the claim that visual-only LoRA underperforms.

## Score and Decision

The paper presents two well-ablated components that yield modest but consistent improvements over strong baselines. The ablations are its strongest asset — each component's contribution is cleanly isolated and validated. However, the paper is undermined by three issues that, while fixable, cannot be overlooked in their current form: (1) the novelty is overclaimed with an inaccurate "for the first time" statement; (2) the language-understanding claim is not supported by controlled evidence; and (3) a key comparison (MOF) lacks transparency about experimental control. These issues prevent the paper from being accepted as-is. With tempered claims, a controlled language ablation, and clarified experimental methodology, this work would make a solid incremental contribution.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>
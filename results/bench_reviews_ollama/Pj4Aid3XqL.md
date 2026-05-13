Now let me verify key claims from the harsh critic by re-reading the relevant sections more carefully.

The key claims to verify:

1. **LR schedule confound**: The paper says at lines 124-126: "We continue training starting from the last text-only learning rate value, if not too low, and continue training for 28B. For 0% and 100% the learning rate would be too low, thus we adopt a linear warmup-cosine decay with a maximum learning rate of 3×10⁻³." And at line 131: "Note: The points at 100% are marked with hollow circles to highlight that they are trained with a different learning rate schedule." And at line 128: "However, at 100% the learning rate schedule is different and could affect the results."

So the paper DOES acknowledge the LR confound, but still draws the conclusion at line 128: "suggesting that continued training is preferable to re-training a 100% fully pre-trained text model." The conclusion section (line 153) also says: "our work questions the traditional practice of separating text and image pre-training phases, demonstrating that a more integrated approach of incorporating image data during pre-training can yield superior downstream results."

The key question: Is the comparison confounded? Yes, the 80% checkpoint continues the existing cosine schedule while the 100% checkpoint gets a re-warmup. The paper acknowledges this in the figure note and in the text ("the learning rate schedule is different and could affect the results"), but still attributes the performance difference primarily to timing rather than LR schedule. This is a valid concern — the experimental design confounds two variables (timing of image introduction and LR schedule), and the paper's conclusion doesn't adequately control for this. The authors acknowledge it as a caveat but still draw strong causal claims.

However, the paper's claim has another interpretation: The paper is comparing "continuing training from an intermediate checkpoint" vs "the common practice of taking a fully pre-trained LLM and re-warming LR." In that sense, the comparison IS fair because that IS what practitioners do — they take a fully pre-trained LLM and re-warm. But the paper's claim goes beyond this practical comparison to make a mechanistic claim about when images should be introduced, which IS confounded.

2. **No comparison against standard VLM pipeline**: The paper at line 144 describes "Two-stage VLMs" including "Liu et al. (2024; 2023) (LLaVA and variants)" which freeze the LLM backbone. But the paper's own approach trains the full model during image-text pre-training (line 84: "The vision encoder can be kept frozen... or trained end-to-end"). This is a valid concern — the paper doesn't compare against the common practice of freezing LLM and only training the projection layer.

3. **No variance reporting**: The paper doesn't appear to report error bars or multiple seeds. This is a valid concern for a 2% improvement claim.

4. **729 visual tokens / 1024 sequence length**: Lines 86 confirms "Each image is encoded to 729 tokens, and we train all models for a sequence length of 1024." This is indeed a notable architectural choice — nearly 71% of each sequence consumed by a single image.

5. **28B token image-text stage**: Line 80 confirms "For a 1.4B model, this equates to around 28B tokens" — relative to the 4.3T text-only stage, this is very short.

6. **Sections 3.2-3.5 appear truncated**: Looking at lines 135-139, Section 3.2 starts but then jumps directly to Section 4 Related Work. The content of Sections 3.2-3.5 appears to be missing from the parsed version. However, per the rules, I should note that missing appendix/parsed sections are a parser issue, not an author issue.

Now let me formalize the review.

**Regarding LR confound**: This is a genuine major weakness. The paper's core claim is that introducing images at 80% is better than at 100%, but this comparison confounds timing and LR schedule. However, the paper does acknowledge this, and the comparison is also practically meaningful — practitioners DO start from fully-trained LLMs and re-warm. So the comparison is fair as a practical comparison but not as a clean mechanistic claim about timing being the causal factor.

**Regarding standard VLM baseline**: This is relevant but partially a scope issue. The paper is studying "when to introduce images in the pre-training pipeline," not specifically comparing against LLaVA-style approaches. However, the conclusion's claim about challenging "the traditional practice" would be stronger with this baseline.

**Regarding variance**: Valid concern for a paper claiming 2% improvements, but single-run evaluation is common in this space at this scale.

Let me now compose the final review.</think>Now I have a thorough understanding of the paper. Let me compose the final review.

## Summary

The paper investigates whether and when image data should be introduced during VLM pre-training, rather than following the common practice of first fully training a text-only LLM and then adding vision data in a second stage. By leveraging intermediate checkpoints of the DCLM-1B model (at 0%, 20%, 40%, 60%, 80%, and 100% of text-only pre-training), they train ~300 models across different configurations and evaluate on both vision-language and text-only tasks. Their key finding is that introducing images at ~80% of text pre-training (continuing the LR schedule) outperforms the common practice of starting from a fully pre-trained LLM (which requires LR re-warming), achieving roughly a 2% improvement on their aggregated "stable score" metric.

## Strengths

- **Systematic experimental design leveraging intermediate checkpoints**: Using intermediate DCLM checkpoints to study timing effects while controlling for data and compute is a clever and resource-efficient approach. The training of ~300 models across configurations (Introduction) enables meaningful ablation over multiple dimensions (checkpoint timing, image-text ratio, fine-tuning epochs).

- **Dual evaluation on both VL and text tasks**: The paper consistently tracks the trade-off between vision-language and text-only performance, which is important for understanding practical utility. Their "stable score" metric (subtracting random baselines before averaging, Section 2.2) is a reasonable standardization approach for comparing across tasks with different chance baselines.

- **Transparent about the LR schedule confound**: The authors mark the 100% points with hollow circles (Figure 4) and explicitly state "at 100% the learning rate schedule is different and could affect the results" (Section 3.1), rather than hiding this difference. This transparency allows readers to interpret the results appropriately.

- **Practically relevant finding**: The recommendation to use intermediate checkpoints to incorporate images during text pre-training cooldown is actionable and cost-efficient for practitioners who have access to intermediate checkpoints.

## Weaknesses

### Fatal

None.

### Major

- **Confounded comparison between timing and LR schedule**: The paper's headline finding—that 80% outperforms 100%—confounds two variables: (1) when images are introduced, and (2) whether the LR schedule is continued vs. re-warmed. The 80% checkpoint simply continues the cosine decay at its natural point, while the 100% checkpoint requires a fresh warmup because the LR has decayed to near-zero. The paper acknowledges this ("at 100% the learning rate schedule is different and could affect the results"), yet still attributes the performance difference primarily to *timing* of image introduction (Section 3.1: "suggesting that continued training is preferable to re-training a 100% fully pre-trained text model"; Conclusion: "demonstrating that a more integrated approach of incorporating image data during pre-training can yield superior downstream results"). Without a controlled experiment (e.g., testing multiple re-warming strategies at 100%, or extending the 100% continued schedule with matched LR), the causal mechanism remains ambiguous. This matters because the difference could be largely explained by well-known training dynamics (continuing a cosine schedule beats re-warming a converged model) rather than being a novel finding about multimodal training. The practical recommendation is still valid—using intermediate checkpoints is beneficial—but the mechanistic claim overreaches the evidence.

- **Missing comparison against the standard freeze-LLM VLM pipeline**: The paper claims to challenge "the traditional practice of separating text and image pre-training phases" (Conclusion), but its 100% baseline trains the entire model with a re-warmed schedule. The most widely-used VLM training recipes (LLaVA, Prismatic, etc.) freeze the LLM backbone during the image-text alignment stage and only train a small projection layer, which is a fundamentally different approach. The paper's related work even acknowledges this (Section 4: "McKinzie et al. (2024)... using a two-stage training strategy with a fixed, pre-trained language model"). Without comparing against this freeze-LLM-then-projection baseline, the paper cannot establish whether its proposed approach outperforms what practitioners actually do, weakening the practical significance of the claimed improvement.

### Minor

- **No variance reporting for a 2% improvement claim**: The abstract reports a 2% average improvement on the stable score metric across 6 tasks. With single runs per configuration and no error bars or statistical tests, it is difficult to assess whether this difference is meaningful versus noise. Given that 300 models were reportedly trained, reporting variance for the key comparisons would be feasible and would strengthen confidence in the results.

- **Architectural setting limits generalizability of ratio findings**: Each image produces 729 visual tokens within a 1024-token sequence, meaning a single image consumes ~71% of any sequence. The finding that 10–20% visual tokens is optimal (Sections 3.2–3.3) may be tightly coupled to this architectural choice, restricting generalizability to more standard settings (e.g., shorter visual token sequences or longer context windows). The paper does not discuss this interaction.

- **Very short image-text pre-training stage**: The 28B-token image-text pre-training is tiny relative to the 4.3T-token text-only stage. It is unclear whether the findings (particularly the optimal 10–20% visual token ratio) would hold at longer image-text pre-training durations more common in practice. The paper does not discuss this limitation.

### Trivial

- The parsed version of the paper appears to truncate Sections 3.2–3.5 (the content about image-text ratios and instruction mixing jumps from the Section 3.2 header directly to Section 4 Related Work). Since findings from these sections are referenced in the Introduction (e.g., "mixing together instruction fine-tuning during the image-text pre-training process actively hurts the model"), readers cannot fully verify these claims. *(Note: This is likely a parser artifact, not a paper issue.)*

## Nice-to-Haves

- An ablation disentangling timing from LR schedule (e.g., testing multiple re-warming strategies at 100%, or continuing training past the 100% point with a matched LR schedule) would definitively resolve the confound and substantially strengthen the paper.
- Comparison against a freeze-LLM baseline would clarify whether the proposed approach beats what practitioners actually deploy.
- Discussing how the 729-token visual representation interacts with the recommended 10–20% ratio would improve the generalizability argument.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"No comparison against the actual standard VLM pipeline"** (Harsh Critic #2): Kept as a Major weakness but weakened its framing. The critic called it a disqualifying "strawman" comparison, but the paper does compare against a real practice (re-warming a fully pre-trained LLM), even if not the most common one. The issue is about completeness of claims, not invalidity.

- **"Overclaimed scope" about challenging "traditional practice"**: Merged into the missing baseline comparison above; the paper's claim goes beyond its evidence but the core finding still has practical value.

- **"0-shot only evaluation is limiting"**: This is a design choice, not a weakness. The paper deliberately scopes to 0-shot evaluation (Section 2.2), which is standard for this type of pre-training study.

- **"Custom stable score metric makes comparison to other work difficult"**: The stable score is a reasonable normalization approach; criticizing a non-standard metric when the paper also reports individual task results (VQA-v2, ARC-easy) is minor at best. Removed as a standalone weakness.

- **"Sections 3.2–3.5 truncated, limiting ability to evaluate claims"**: This is a parser artifact, not a paper issue. Removed from substantive weaknesses but noted in Trivial as a parser issue.

- **Criticisms about the paper "incorrectly implying most two-stage VLMs train the entire model"**: The paper's related work section (Section 4) does acknowledge both approaches (freeze-LLM and full training). Removed as factually inaccurate.

- **Strength claim about "demonstrating advantage of mid-pretraining over re-warming"**: Removed from strengths as it is undermined by the LR schedule confound (the weakness takes precedence over this strength per the rules). The finding is a *practical observation*, not a clean mechanistic demonstration.

## Novel Insights

The paper's most interesting implicit finding is that the optimal time to introduce visual data coincides with the point in the LR schedule where continued training is still viable—suggesting that the practical benefit of intermediate checkpoints may be as much about avoiding LR re-warming pathology as it is about when visual data is introduced. This suggests an alternative interpretation: the real takeaway may not be "introduce images at 80%" specifically, but rather "avoid re-warming a fully converged LLM; use whatever intermediate checkpoint has sufficient LR remaining."

## Suggestions

- Run at least one controlled ablation at the 100% checkpoint testing different LR re-warming strategies (e.g., continued LR schedule past the cosine endpoint, larger warmup, etc.) to isolate the effect of timing from the effect of LR schedule. This single addition would dramatically clarify the paper's core claim.
- Add a single freeze-LLM baseline (projection-only training at the image-text stage, followed by full fine-tuning) to show whether the approach beats the dominant practical pipeline.
- Report standard deviations across at least 3 seeds for the 80% vs. 100% comparison and the optimal ratio comparison.

## Score and Decision

The paper addresses an important practical question with a creative experimental design and produces actionable findings. However, its central mechanistic claim—that introducing images at 80% is superior—is confounded by the LR schedule difference, which the paper acknowledges but does not resolve. The absence of the standard freeze-LLM baseline further limits the practical implications. These are addressable concerns (especially with one additional ablation), but as presented, the paper overreaches its evidence. The contribution is real—there is value in the systematic exploration and the practical recommendation—but the causal attribution needs qualification.

**Originality**: Moderate. The question is important and under-explored in open literature, but the core finding is confounded.

**Importance of research question**: High. When and how to introduce multimodal data has significant practical impact.

**Claims well-supported**: Partially. The practical observation is sound; the mechanistic claim is confounded.

**Soundness of experiments**: Moderate. Systematic exploration with 300 models, but confounded key comparison and no variance reporting.

**Clarity**: Good. Clear writing and transparent about limitations (hollow circles in figures).

**Value to community**: Moderate-to-good. Actionable guidance, though the "why" needs more evidence.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>
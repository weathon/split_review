- Decision: Reject
- Avg Score: 3.50
- Scores: 5, 3, 3, 3
Now I have all the information needed. Let me compose the final consolidated review.

## Summary

This paper proposes ModalPrompt, a prompt-based continual learning framework for Large Multimodal Models (LMMs). The method maintains per-task prototype prompts, selects and fuses them via similarity to CLIP-extracted dual-modality (image+text) features, and trains with a combination of language loss and prototype similarity loss. On the CoIN benchmark across 8 multimodal tasks, ModalPrompt achieves substantial improvements over MoELoRA and finetuning baselines, with +20% performance gains and only 0.27% trainable parameters.

## Strengths

- **Dual-modality guidance demonstrably improves over single-modality alternatives**: The ablation in Table 3 shows that using both image and text CLIP features for prompt selection yields higher average performance across all 8 tasks compared to using either modality alone. For instance, ImageNet accuracy jumps from 21.49% (image-only) and 13.41% (text-only) to 41.13% (dual-modality), directly validating the paper's core claim that multimodal supervision is crucial for LMM continual learning.

- **Prompt selection and fusion are both empirically necessary**: Table 4 ablates each component systematically. Without selection (concatenating all prompts), average ContinualT drops substantially; without fusion (selecting only one task's prompts), performance also degrades. Using both components together achieves the reported 55.0 average ContinualT, providing controlled evidence that the full framework delivers the claimed improvements.

- **Substantial margin over existing methods on a standard benchmark**: In Table 1, ModalPrompt outperforms MoELoRA by large margins on ContinualT (e.g., +23.49 on TextVQA, +35.72 on REC, +24.13 on VQAv2). The relative improvements are consistent and large across all 8 tasks, strongly supporting the paper's central performance claims.

- **Efficiency without task-proportional growth**: Table 5 shows ModalPrompt uses only 0.27% trainable parameters (vs. 4.73% for MoELoRA), achieves 1.42× faster inference, and reduces training time while using less GPU memory. This validates the paper's claim of refraining from computational expansion in proportion to the number of tasks.

- **Interpretable analysis of prompt selection behavior**: Figures 4–5 (described in text) show similarity heatmaps and selection probabilities that demonstrate the selection module consistently picks the correct task's prototype prompts and also leverages prompts from semantically similar tasks (e.g., VQA-related tasks), providing evidence that the dual-modality guidance promotes meaningful cross-task knowledge transfer.

## Weaknesses

### Fatal

None.

### Major

None. All identified issues are addressable with clarifications or minor corrections.

### Minor

- **Prototype loss equation has a likely typo (Eqn. 5)**: The prototype similarity loss is written as $\mathcal{L}_{\mathrm{Proto}}^t = [1-\mathrm{sim}(\boldsymbol{x}_\mathrm{p}^t, \boldsymbol{x}_\mathrm{instruct})] + [1-\mathrm{sim}(\boldsymbol{x}_\mathrm{p}^t, \boldsymbol{x}_\mathrm{instruct})]$, where both terms are identical and both reference only the text feature $\boldsymbol{x}_\mathrm{instruct}$ rather than one text term and one image term. The surrounding text explicitly states the intent is to "maximize the similarity with dual-modality features," and the ablation in Table 3 confirms the dual-modality approach works and outperforms single-modality variants. This is almost certainly a copy-paste error — one term should use $\boldsymbol{x}_\mathrm{v}$. The paper's claims are not invalidated by this typo, but it must be corrected.

- **Efficiency comparison should clarify whether CLIP text encoder overhead is included**: Table 5 reports inference speed (tokens/s) but does not explicitly state whether the CLIP text encoder forward pass (which is the only extra compute, as the paper notes at line 85 that the vision encoder is shared with LLaVA) is included in the reported timings. A clarification would make the efficiency analysis fully transparent. The likely impact is small (CLIP text encoder is ~63M parameters vs. the 7B LMM), but this should be stated explicitly.

- **TextVQA anomaly in the dual-modality ablation is not discussed**: In Table 3, the "Only Image" variant achieves 56.94 on TextVQA, while the full "Dual Modality" achieves only 56.40. The paper claims dual-modality "suits the best and largely improves the performance" but does not address this exception. While dual-modality is the best overall average and outperforms text-only on TextVQA (56.40 vs. 55.90), this specific case merits a brief explanation.

- **Very low BWT values warrant analysis**: The method achieves final BWT of 1.68 (Table 2), implying almost no forgetting across all 8 tasks. While this may be legitimate (since prompts are task-specific and frozen after training), the paper should discuss whether the approach primarily isolates tasks (each sample is routed to its own task's prompts) or actually achieves cross-task knowledge transfer, and how the reported similarity heatmap (Figure 5) supports the transfer interpretation.

- **Prompt selection complexity nuance**: The paper states "computational complexity is in proportion to the number of tokens other than the number of tasks." This is accurate for the prompt concatenation/processing stage, but the selection mechanism itself requires computing $O(T)$ cosine similarities per sample (one per task). While $T=8$ is small and this does not threaten the method's efficiency, the distinction should be acknowledged for completeness.

### Trivial

- Table 4 caption should more clearly distinguish the ablation conditions (no fusion vs. no selection) — currently it uses only checkmark symbols in the header without explicit row labels.

## Nice-to-Haves

- Adding prompt-based continual learning baselines (e.g., Progressive Prompts or related methods adapted to LMMs) would further strengthen the evaluation, though the existing comparison against MoELoRA and finetune is already sufficient to demonstrate the contribution.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Harsh Critic's "multi-task baseline is anomalously weak"**: The multi-task numbers are from the CoIN benchmark, not constructed by the authors. The paper's method *exceeds* the multi-task baseline by a large margin on several tasks — this strengthens the contribution, not weakens it. The claim of "comparable to multi-task" is actually an understatement. Moreover, the method's primary comparisons are against MoELoRA and finetune, which are the relevant baselines, and the improvements over these are large and consistent.

- **Harsh Critic's "no-fusion/no-selection variant is barely above random" (44.28 on ScienceQA)**: The critic misread the ablation table. The row with 44.28 uses *selection* but *no fusion* — it is not the "without both" variant (which is not shown). 44.28 is also well above the finetune baseline's 26.00 on ContinualT ScienceQA, so the characterization as "barely above random" is incorrect and the concern about a "degenerate configuration" is unwarranted.

- **Harsh Critic's concern that "CLIP overhead could be substantial"**: The paper explicitly notes (line 85) that the CLIP vision encoder is already used by LLaVA as part of the base LMM forward pass, so the *only additional cost* is the CLIP text encoder — a relatively small 63M-parameter forward pass on a short instruction string. This is far from the "considerably lower" inference speed the critic speculates about. The overhead concern is not "omitted"; it is partially addressed. A clarification would be nice but this is not a methodological gap.

- **Harsh Critic's note about cherry-picked qualitative examples**: Qualitative visualization (Figure 6) is standard practice in ML papers to illustrate model behavior. This is not a weakness; the paper does not make quantitative claims based on these examples.

- **Harsh Critic's note about missing Progressive Prompts and Pop baselines**: The paper mentions these methods in Related Work and cites them. While including them as baselines would be nice, the paper already compares against the state-of-the-art on the CoIN benchmark (MoELoRA) and naïve finetuning, showing large and consistent improvements. Missing additional baselines is not a flaw in an already thorough evaluation.

- **Strength Finder's strengths that conflict with verified weaknesses**: Not applicable — no verified weaknesses invalidate any of the strength finder's identified strengths.

## Novel Insights

None beyond the paper's own contributions. The reviews did not surface any genuinely novel observation about the work that the paper itself does not already articulate.

## Suggestions

1. **Fix the prototype loss equation (Eqn. 5)** so that one term uses $\boldsymbol{x}_\mathrm{v}$ and the other uses $\boldsymbol{x}_\mathrm{instruct}$, consistent with the paper's stated dual-modality objective.

2. **Add a clear statement** in the efficiency comparison (Table 5) about whether the CLIP text encoder forward pass is included in the reported inference timings.

3. **Discuss the TextVQA case** in the dual-modality ablation, explaining why image-only slightly outperforms dual-modality on that particular dataset.

4. **Add an analysis** of why BWT is so low — specifically, provide evidence on whether the model transfers knowledge or simply isolates tasks, perhaps by analyzing how often prompts from other tasks are selected and whether omitting them changes outputs.

5. **Acknowledge the O(T) cost** of the prompt selection similarity computation when describing computational complexity claims.

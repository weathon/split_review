- Decision: Reject
- Avg Score: 4.00
- Scores: 5, 3, 3, 5
Now I have a thorough understanding of the paper. Let me write the consolidated review.

## Summary
2-3 sentence summary of the paper's contribution.

The paper proposes Video Q-Former, a multimodal large language model for video understanding that introduces (1) an attentive pooling module to extract decoupled spatiotemporal features from videos, and (2) a spatio-temporal Q-Former with three mixture-of-experts video experts (spatial, temporal, summary) for semantic-aligned video representations. The model is pre-trained on 15M examples in two stages, instruction-tuned, and evaluated on zero-shot video QA, captioning, summarization, and text generation benchmarks.

## Strengths
- **Strong zero-shot video QA performance across multiple datasets (Table 2).** Video Q-Former achieves 70.1% on MSRVTT-QA and 77.4% on MSVD-QA, outperforming the second-best method by substantial margins. The comparisons use the Video-ChatGPT benchmark, which is the standard protocol for all baselines listed in the table.
- **Ablation confirms both architectural components contribute (Table 6).** On the MSRVTT captioning proxy task, replacing average pooling with attentive pooling improves CIDEr from 64.00 → 64.62, and replacing the original Q-Former with the spatio-temporal Q-Former further improves to 65.14. Each design decision is independently validated.
- **Ablation of video experts demonstrates the necessity of separate spatial and temporal modeling (Tables 7 and 8).** On ActivityNet-QA (temporal understanding) and MSRVTT captioning (spatial detail), using both SP-FFN and T-FFN jointly outperforms either expert alone, confirming that the MoE design is not redundant.
- **Competitive video summarization with less pre-training data (Table 5).** Video Q-Former outperforms VideoTeller by ~10 points on BLEURT on the Video-CSR dataset, despite not using the 0.5M video-text pairs that VideoTeller pre-trains on, demonstrating training efficiency on long-form video.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor
- **Unclear mapping from GPT score (0–5) to reported accuracy percentages (Section 4.3, Table 2).** The paper states that the Video-ChatGPT benchmark "employs ChatGPT to assess the accuracy of the model's prediction results and assigns a score ranging from 0 to 5." However, the results are reported as percentages (e.g., 70.1%). No description is given of how 0–5 scores are converted to accuracy percentages, making it difficult for readers to interpret the numbers or reproduce the evaluation. This does not invalidate comparisons (all baselines use the same benchmark protocol), but the missing conversion detail is a clarity gap.
- **Ablation uses a reduced training setup that does not match the full model (Section 4.7, Table 6).** The ablation is conducted after only 5 epochs pre-training on WebVid2M and 1 epoch finetuning on MSRVTT captioning, whereas the full model uses 15M examples across three datasets in a two-stage pre-training pipeline followed by instruction tuning. While reduced-setup ablations are common practice, the paper does not discuss whether the observed gains (0.8 BLEU-4, 2.1 CIDEr) are expected to transfer to the full setting. It also does not ablate the components on the zero-shot QA tasks where the largest improvements are claimed.
- **Query allocation is underspecified (Section 3.1).** The paper states "64 queries for the extraction of spatial and temporal features" without specifying how these 64 are split between spatial and temporal roles (e.g., 32+32, or all 64 shared across both). Combined with "one query for summarization," the total query count and routing are ambiguous.
- **No discussion of limitations or failure cases (Section 5).** The conclusion restates contributions but does not analyze scenarios where the model struggles, which would help readers gauge the method's true scope.
- **VideoTeller comparison in summarization may be confounded by ASR usage (Section 4.6).** The paper uses ASR text as a prompt for its model but does not state whether the VideoTeller baseline also uses ASR. If VideoTeller does not, the comparison partly reflects the ASR information advantage rather than the video modeling contribution.

### Trivial
- The FLOPs comparison (Table 1) is only against a naive per-frame Q-Former, not against the actual competing architectures (Video-ChatGPT, Video-LLaMA), which limits its informativeness.
- No ablation isolating the effect of instruction tuning (100K examples from Video-ChatGPT).

## Nice-to-Haves
- Reporting results without instruction tuning to isolate its contribution.
- Including confidence intervals or variance estimates for the GPT-based evaluation.
- Clarifying in the text whether the cross-attention mask (Figure 3) is applied during cross-attention or self-attention layers (currently described only in the figure caption).

## Removed Points
These points were raised in the inputs but are removed as they do not hold up against the paper as written:

- **"Invalid zero-shot video QA evaluation"** (Harsh Critic, Fatal): The critic claims the GPT-based scoring is incompatible with baseline metrics. However, the paper explicitly states it uses "the benchmarks established by Video-ChatGPT" — the same benchmark used to evaluate all baselines in Table 2. The comparison is an apples-to-apples evaluation within a standard benchmark. Removed.
- **"Inconsistent and exaggerated performance claims"**: The 13%/10% improvement refers to the margin over the second-best model (in percentage points), while the "nearly 1-point score increase" refers to a comparison with a specific baseline (VideoChat) that uses a different scale. These are different comparisons, not inconsistencies. Removed.
- **"Attentive pooling mechanism is unclear"**: The formulation CA(Q_s, x, x) where Q_s ∈ ℝ^{1×D} and x ∈ ℝ^{T×N×D} yields v_t ∈ ℝ^{T×D} because cross-attention is applied per-frame (treating T as a batch dimension over frames, with each frame having N patches as the sequence). This is standard and correctly described. Removed.
- **"Cross-attention mask not explained in text"**: The mask is described in Figure 3's caption ("spatial queries and temporal queries are limited to attending only to their corresponding features, while the summary query can attend to all features"). This is sufficient explanation for a figure caption. Removed.
- **"Missing related works"**: Removed per instructions (no external sources to confirm existence). Removed.
- **"No variance/confidence intervals"**: Single-run evaluation is standard practice for this class of benchmarks. Removed.
- **"Qualitative examples not systematic"**: Qualitative examples serve illustrative purposes; they are not presented as primary evidence. Removed.
- **"No comparison to most recent video LLMs"**: Removed per instructions (cannot independently verify existence/availability of specific models mentioned by the reviewer). Removed.

## Novel Insights
None beyond the paper's own contributions. The reviews do not surface any genuinely novel observation about the paper that the authors themselves did not articulate.

## Suggestions
1. **Clarify the evaluation metric conversion.** Explain how the ChatGPT 0–5 scores map to the reported accuracy percentages (e.g., is accuracy computed as average_score / 5 × 100, or is GPT asked for a binary correct/incorrect judgment per question?). Include the evaluation prompt (either in the main text or appendix).
2. **Strengthen the ablation by evaluating on zero-shot QA.** Run at least one ablation (attentive pooling vs. average pooling, with and without spatio-temporal Q-Former) on MSRVTT-QA or ActivityNet-QA under the final training setup, to confirm the components' contributions on the headline task.
3. **Specify the query allocation.** State explicitly how the 64 queries are divided among spatial and temporal roles.
4. **Add a limitations paragraph.** Discuss what types of video understanding the model still struggles with (e.g., very long videos, fine-grained temporal reasoning, counterfactual questions).
5. **Clarify the VideoTeller ASR baseline.** If possible, either confirm that VideoTeller also uses ASR (and cite the relevant section) or note the potential confound.

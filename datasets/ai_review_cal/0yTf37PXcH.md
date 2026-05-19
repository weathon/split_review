- Decision: Reject
- Avg Score: 5.40
- Scores: 6, 5, 3, 8, 5
Here is my consolidated review.

---

## Summary

This paper presents Arcana, a multimodal LLM with two architectural contributions: **MM-LoRA**, which assigns separate LoRA parameters to visual and language tokens within the LLM to reduce modality interference, and **QLadder**, a cross-attention adapter that injects learnable queries into a frozen CLIP image encoder to enhance visual representations without adding a second encoder. The paper evaluates Arcana on multiple VQA and LVLM benchmarks with competitive results and provides ablation studies isolating each component.

## Strengths

1. **MM-LoRA shows consistent gains over standard LoRA in controlled ablation.** Table `tab:mmlora` compares LoRA vs. MM-LoRA under matched conditions (same data, same compute). With β=0.25, γ=0.75, MM-LoRA improves ScienceQA by +2.1, MMBench by +1.0, and MME by +40 points over LoRA. The systematic sweep over β/γ ratios (1/0, 0.75/0.25, 0.5/0.5, 0.25/0.75, 0/1) removes any ambiguity about parameter cherry-picking.

2. **QLadder outperforms a full second encoder (MOF/DINOv2) with far fewer tokens — and avoids the degradation MOF causes.** Table `tab:additional_visual_encoder` shows that QLadder (64 added tokens) improves MMVP by +3.6, POPE by +0.6, MMBench by +2.0, and TextVQA by +0.6, while MOF (256 tokens from a second encoder) degrades MMBench by −4.2 and TextVQA by −1.7. This cleanly demonstrates QLadder's efficiency advantage and its ability to enhance visual grounding *without* sacrificing general visual understanding.

3. **Trivial computational overhead.** Table `tab:computation` reports that adding QLadder increases memory usage by only 0.58 GB and decreases inference speed by 0.11 tokens/s, confirming the practical efficiency benefit over dual-encoder approaches.

4. **Attention visualizations support the modality-decoupling story.** Figure 5 compares attention maps across baseline, baseline+MM-LoRA, and baseline+MM-LoRA+QLadder, showing increased attention to visual tokens in middle/later layers when MM-LoRA is used. This provides qualitative evidence for reduced modality interference.

5. **Systematic hyperparameter search for QLadder query count.** Table `tab:num_query` sweeps 16, 32, 64, 128 queries and identifies 64 as optimal, with performance degrading at 128. This careful tuning strengthens the empirical support.

## Weaknesses

### Fatal
None.

### Major

1. **Ablation baseline mismatch with published LLaVA-v1.5 numbers creates uncertainty about the source of gains.** The ablation (Table `tab:mmlora`) uses ShareGPT4V for pretraining while the original LLaVA-v1.5 uses LLaVA-pretrain. The LoRA baseline's ScienceQA score of 69.1 is *higher* than LLaVA-v1.5's reported 66.8, and its MME of 1460 is *lower* than LLaVA-v1.5's 1510.70. These gaps (especially ScienceQA being +2.3 with a *weaker* fine-tuning method) strongly suggest the richer ShareGPT4V pretraining data is already driving meaningful improvements. While the internal comparison (LoRA vs. MM-LoRA under identical conditions) remains valid, the absolute performance deltas attributed to MM-LoRA and QLadder in the ablation cannot be assumed to transfer to the standard LLaVA-v1.5 data pipeline. The paper states in line 240 that it "used only LLaVA-v1.5 data for these experiments" — but this refers to instruction data only, not pretraining data — and this ambiguity should be clarified.

2. **Data differences confound the main comparative results (Tables 1 and 2).** Arcana is trained on ShareGPT4V pretraining (~1.2M image-text pairs) and 934K diverse instruction data, whereas LLaVA-v1.5 uses LLaVA-pretrain (~558K) and ~665K instruction data. The instruction data composition also differs (Arcana includes region-aware QA, OCR QA, ShareGPT4V captions, etc.). Since the main results tables do not control for this, it is unclear how much of Arcana's advantage over models like LLaVA-v1.5 and mPLUG-Owl2 stems from the proposed architectural components versus the richer training data. The ablation attempts to control for this but is undermined by the baseline calibration issue above. A clean control — e.g., training a full LLaVA-v1.5 replication on ShareGPT4V data, or training Arcana on LLaVA-pretrain — would substantially strengthen the paper.

### Minor

3. **Limited differentiation from prior query-based adapters.** QLadder uses learnable queries + cross-attention, which is conceptually similar to the Q-Former (BLIP-2) and perceiver resampler architectures. The paper cites Q-Former in the related work (line 51) but does not explicitly state the key difference: QLadder is *inserted into the frozen CLIP encoder layers* to aggregate intermediate representations, whereas Q-Former sits between the encoder and LLM. This distinction should be clearly articulated, and an experimental comparison against a Q-Former variant under matched conditions would better position QLadder's contribution.

4. **The "data engine" is mentioned only in the conclusion (line 398) with no description.** If re-annotated caption data was used and contributed to results, it should be detailed in the method section with an ablation showing its effect. Without this, the reference feels like a dangling contribution.

5. **Language benchmark comparison (Table NLP) is of limited value.** Arcana is compared against text-only LLaMA-2 and Vicuna-v1.5, but Arcana was fine-tuned on additional text-only instruction data (ShareGPT). The fact that it outperforms these baselines is therefore not surprising and does not cleanly demonstrate "language preservation" from multimodal training — it could simply reflect exposure to more language data. The authors should clarify this confounding factor or present a comparison against Vicuna-v1.5 fine-tuned on the same text-only data.

6. **No discussion of failure cases.** QLadder improves MMVP from 24.0 to 27.6, but this still means the model fails on ~72% of fine-grained visual matching questions. A qualitative analysis of where MM-LoRA and QLadder still struggle would be more informative than additional aggregate benchmarks.

### Trivial

- Table `tab:visual_tuning` baseline numbers (TextVQA 58.1, MMBench 64.1) differ trivially from LLaVA-v1.5's reported numbers (58.2, 64.3) — within 0.1–0.2 points, which is negligible noise. This specific comparison raised by the reviewer is not a meaningful issue.

## Nice-to-Haves

- A comparison of GPU-hours or total FLOPs during training (not just inference) for QLadder vs. MOF would strengthen the efficiency claim.
- A controlled experiment showing shared vs. separate LoRA with identical rank and compute would directly validate the modality-interference motivation.
- Providing the OpenReview submission's appendix content (stripped by the parser) would address concerns about missing implementation details.

## Removed Points

These points were raised by reviewers but are removed (or demoted to minor) because they are factually incorrect, overblown, or misunderstand the paper:

1. **"Computation table should compare with vs. without QLadder"** — Factually incorrect. Table `tab:computation` already compares "Arcana (w/o QLadder)" vs. "Arcana (w QLadder)" side-by-side. This is exactly the right comparison. **Removed.**

2. **"The paper doesn't measure modality interference"** — The paper provides attention visualizations (Fig. 5) as evidence that MM-LoRA increases visual-token attention, which is a reasonable proxy. The claim that no measurement exists is overstated. **Removed.**

3. **"Arcana* results are inconsistent"** — Arcana* is better on 10/12 benchmarks and slightly worse on 2/12 (TextVQA −0.8, ScienceQA −1.7, MM-Vet −0.4). This pattern clearly favors Arcana*, and the small drops are within normal variation. **Removed** as noise that does not undermine the paper.

4. **"Choice of β and γ is arbitrary"** — The paper performs an ablation over β = {1, 0.75, 0.5, 0.25, 0} and identifies the optimum empirically. This is the opposite of arbitrary. **Removed.**

5. **Generic scope-creep criticisms** (e.g., requesting larger datasets, more models, "the evaluation lacks rigor" without specific anchoring). **Removed** per filtering rules.

6. **Formatting/style nitpicks and missing appendix content** (normal parser artifacts). **Removed.**

## Novel Insights

None beyond the paper's own contributions. The reviewer analyses largely confirm the paper's narrative (the ablation evidence is the strongest part) and sharpen the data-confound concerns that the paper partially acknowledges but underemphasizes.

## Suggestions

1. **Clarify the ablation pretraining setup.** State explicitly whether the ablation uses ShareGPT4V or LLaVA-pretrain for the pretraining stage. If the former, add an ablation that also uses LLaVA-pretrain to match the original LLaVA-v1.5 pipeline and allow direct comparison of absolute numbers.

2. **Add a controlled experiment training LLaVA-v1.5 on ShareGPT4V data** (or Arcana on LLaVA-pretrain) to isolate the contribution of architecture from data. This would resolve the main confound concern.

3. **Compare QLadder against a Q-Former baseline** under identical training conditions (same queries, same data, same LLM). This would clarify what, if anything, the "ladder" structure adds beyond the established query-based adapter paradigm.

4. **Describe the data engine** in the method section if it was used to generate training captions. Add an ablation showing performance with vs. without the re-annotated data.

5. **Add a failure analysis** for MMVP and similar fine-grained perception benchmarks. Showing where the model still fails (and why) would strengthen rather than weaken the paper.

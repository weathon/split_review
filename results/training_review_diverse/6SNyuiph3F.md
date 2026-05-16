Now I have a thorough understanding. Let me synthesize everything into the final consolidated review.

---

## Summary

This paper proposes using "chat vector" — the weight difference between LLaMA2 and LLaMA2-chat — to transfer chat capabilities (instruction following, safety, multi-turn dialogue) to continually pre-trained models in non-English languages (Traditional Chinese, Simplified Chinese, Korean). The method bypasses expensive RLHF by replacing it with a single vector addition in parameter space. Experiments on the Vicuna benchmark, toxicity prompts, and safety prompts suggest that CP+chat vector can match or exceed the standard CP→FT pipeline.

## Strengths

- **Computational efficiency with competitive results**: Adding the chat vector after continual pre-training yields instruction-following scores on the Vicuna benchmark competitive with the standard CP→FT pipeline, without requiring RLHF. For Traditional Chinese with a system prompt, LLaMA2→CP+chat vector (7.90) outperforms LLaMA2→CP→FT (7.03) and nearly matches LLaMA2-chat→CP→FT (7.58). This directly supports the paper's central claim that the chat vector can replace the expensive RLHF stage.

- **Cross-lingual generality**: The method is validated across three languages (Traditional Chinese, Simplified Chinese, Korean) using different base CP models (authors' own LLaMA2-CP, Chinese-LLaMA, Korean LLaMA). The consistent improvement from adding the chat vector across all three languages supports the claim that the approach generalizes beyond a single language or model.

- **Complementary effect with fine-tuning**: Applying the chat vector after fine-tuning further boosts performance — LLaMA2→CP→FT+chat vector scores 8.01, outperforming either component alone (7.90 and 7.03). This demonstrates that the two sources of instruction-following skill (learned via FT and transferred via chat vector) can be combined via simple addition.

## Weaknesses

### Fatal
None.

### Major

- **Unvalidated evaluation metrics for the target languages undermine confidence in the central results.** The paper relies on three unvalidated measurement instruments: (a) Perspective API, developed for English, applied to Traditional Chinese to measure toxicity — its cross-lingual reliability is unknown; (b) GPT-3.5 function calls used as a safety judge without any validation of its accuracy on Chinese safety classification; (c) GPT-4 is used to translate the Vicuna benchmark and the Real Toxicity Prompts into Chinese/Korean, then used again as the automatic evaluator, with a non-standard scoring procedure that treats GPT-4 answers as a perfect 10 (line 124). This creates a circular dependency where GPT-4 may prefer outputs resembling its own style, and translation quality affects both prompt intent and scoring criteria. No human evaluation or native-speaker cross-check is provided to validate any of these metrics. Since the paper's conclusions about instruction following, safety, and alignment are built on these measurements, this is the most significant weakness in the submission.

- **Multi-turn dialogue claim rests on a single anecdotal example.** The paper concludes that "chat vector empowers models with multi-turn conversation abilities" based on one case study in Figure 2. While the example is illustrative, it does not constitute sufficient evidence for a general claim. The paper's fine-tuning dataset explicitly contains only single-turn data (line 104), so the multi-turn capability is entirely attributed to the chat vector — but this attribution is supported by only one qualitative comparison.

### Minor

- **Cross-lingual baselines are not fully controlled.** For Chinese-LLaMA and Korean LLaMA, the paper compares chat-vector-augmented models against off-the-shelf baselines (Chinese-Alpaca, Korean LLaMA FT) trained on unknown data with different procedures and data sizes (line 142). There is no controlled condition where, e.g., Chinese-LLaMA is fine-tuned on the authors' own 80k dataset and then compared with and without chat vector. Performance differences could partially reflect data/training quality rather than the chat vector itself. (The core Traditional Chinese experiments are better controlled since the authors train their own models.)

- **English-language leakage is acknowledged but not adequately resolved.** The paper observes that adding the chat vector causes a high proportion of English responses for Chinese-LLaMA (Table 4). The proposed solution (scaling by 0.5) works for the FT+chat condition but degrades instruction following when applied to CP+chat directly. This is a significant practical limitation of the method, and no systematic analysis or principled solution is offered beyond the scaling trick.

- **The technical contribution beyond applying task vectors is limited.** The method follows directly from Ilharco et al. (2023) — the chat vector is simply a task vector applied in a new cross-lingual setting. The paper does not investigate what the chat vector actually encodes (language-agnostic instruction-following vs. English-specific conversational patterns), leaving the mechanism behind the cross-lingual transfer as a black box. While empirical application papers can be valuable, this limits the depth of insight.

- **Toxicity analysis selectively highlights favorable comparisons.** Table 2 (though not fully visible in the text) is described as showing that the CP+FT+chat vector condition has higher toxicity than CP+FT on several attributes, but the paper's narrative focuses on the CP vs. CP+chat comparison. A more balanced discussion of failure cases would strengthen the paper.

- **Ad-hoc dataset construction details.** The Real Toxicity Prompts are truncated "at the second comma" after translation (line 115), which is an arbitrary heuristic that may break natural sentence structure in Chinese. The 80k fine-tuning dataset is described at a high level without quality checks, deduplication, or prompt diversity analysis. These details do not invalidate the results but weaken reproducibility.

### Trivial
None.

## Nice-to-Haves

- **Human evaluation** of a subset of outputs for instruction following, multi-turn coherence, and language correctness in the target language by native speakers would validate the automatic metrics and substantially strengthen the evidence.
- **Statistical significance reporting** (confidence intervals or multiple runs) would help assess the reliability of the reported scores.
- **Ablation of the chat vector** (e.g., isolating attention vs. MLP layers, analyzing which components carry the chat capability) could deepen understanding of why the method works across languages.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **"Introduction overclaims restructuring from CP→SFT→RLHF to CP+chat vector because the paper still uses SFT."** — The paper's *core* method (CP+chat vector, lines 138, 156) genuinely does not use SFT/FT. The FT+chat vector condition is presented as an optional complementary variant. The framing is accurate for the main contribution.

2. **"Missing hyperparameters for reproducibility."** — Per the applicable rule, undisclosed training hyperparameters for continual pre-training and fine-tuning are considered a nitpick in this context.

3. **"No confidence intervals or multiple runs."** — Moved to Nice-to-Haves, as single-run evaluation is common in large-scale LLM experiments.

4. **"Missing baseline: prompting the CP model in English."** — This baseline does not address the paper's research question (chat capabilities in the target language) and falls outside the paper's scope.

5. **"Dataset quality checks not reported."** — The paper states the dataset composition (80k GPT-4 generated prompts, plus translation/summarization data). Exhaustive quality check reporting is beyond what is standard for papers of this type.

## Novel Insights

None beyond the paper's own contributions. The key empirical finding — that adding the LLaMA2-chat weight difference to a continually pre-trained non-English model can transfer instruction-following and safety behaviors — is practically useful but the paper does not provide mechanistic understanding of why it works across languages or what the chat vector captures.

## Suggestions

1. **Validate the evaluation metrics** with human evaluation on a subset (e.g., 100 examples per language) to establish that the GPT-4 scores and Perspective API toxicity classifications correlate with human judgments for the target languages.
2. **Add a fully controlled experiment** for Chinese-LLaMA and Korean LLaMA: fine-tune these existing CP models on the authors' own 80k dataset, then compare with and without chat vector under matched training conditions.
3. **Expand the multi-turn evaluation** beyond the single case study — even 20–30 multi-turn dialogues with quantitative metrics (e.g., consistency of entity recall across turns) would significantly strengthen this claim.

## Score and Decision

The paper addresses a practical problem (efficiently equipping non-English LLMs with chat capabilities) and presents a computationally attractive solution. The results across three languages are suggestive and the core idea is interesting. However, the evaluation methodology has significant gaps — the central metrics are not validated for the target languages, the multi-turn claim rests on one example, and some cross-lingual comparisons are not fully controlled. These weaknesses reduce confidence in the reported results but do not invalidate the overall contribution. The paper would benefit from substantial revisions, particularly human evaluation and more controlled experiments.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>
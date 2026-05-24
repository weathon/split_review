Now I have sufficient calibration. Let me write the consolidated review.

## Summary

This paper proposes a practical recipe for converting pre-trained autoregressive language models (GPT2, LLaMA2) into discrete diffusion language models (DiffuGPT, DiffuLLaMA). The adaptation uses three techniques: attention mask annealing (gradually removing causal masking), a shift operation aligning the diffusion output with next-token prediction, and a time-embedding-free architecture. The authors scale this approach up to 7B parameters — the largest DLM trained to date — using under 200B tokens of continued pretraining. They evaluate across language modeling, reasoning, commonsense, infilling, and code generation tasks, showing DiffuLLaMA achieves state-of-the-art results among all existing DLMs.

## Strengths

1. **First demonstration of 7B-scale diffusion language models.** DiffuLLaMA is the largest DLM trained to date, surpassing the prior maximum of 1.3B (Plaid 1B). Table 1 shows it achieves the best results among all DLMs on every evaluated task, including Lambada (70.9), HellaSwag (58.7), GSM8K* (63.1), and code infilling pass@1 (15.5 vs 2.9 for the next-best DLM). The training loss curve (Figure 2) shows a clean scaling trend with no saturation, indicating room for further improvement.

2. **Theoretical unification and a simple, effective adaptation recipe.** Section 3.2 formally shows that AR language modeling is a special case of discrete diffusion where the forward process deterministically masks tokens left-to-right. The adaptation recipe (Algorithm 1) bridges the two paradigms via two concrete changes — attention mask annealing and shift operation — that are simple to implement. The ablation (Table 3) confirms the shift operation is critical: removing it drops GSM8K accuracy from 45.4→33.5 (GPT2-S) and 49.7→34.5 (GPT2-M).

3. **Comprehensive evaluation beyond perplexity.** As argued in Section 4.2, prior DLM work relied almost exclusively on perplexity, which the paper correctly identifies as insufficient for assessing model capabilities. The evaluation covers 9 benchmarks across reading comprehension (TriviaQA), commonsense reasoning (HellaSwag, Winogrande, SIQA, PIQA), math reasoning (GSM8K), story infilling (ROCStories), and code infilling (HumanEval). This provides a substantially more nuanced picture of DLM capabilities and limitations than prior work.

4. **Open-source release.** The paper releases models (127M, 355M, 7B), adaptation code, fine-tuning scripts, and evaluation toolkits at a public repository, which will enable further community research on DLMs.

## Weaknesses

### Fatal
None.

### Major

1. **Ablation is performed on a proxy task rather than the actual adaptation pretraining.** The core methodological claims are about the adaptation pretraining, but Table 3 ablates the components on GSM8K symbolic finetuning. The paper acknowledges this ("Direct ablation on adaptation training is costly; hence, we conduct preliminary experiments to determine the adaptation recipes"), but this is a significant limitation: the paper cannot directly validate that mask annealing or the shift operation are necessary during the actual continued pretraining at scale. Moreover, the ablation shows mask annealing has minimal impact (DD 45.4 vs DD-w/o anneal 43.3), and the paper omits it entirely for the 7B model — which raises the question of how central it is to the claimed contribution. The primary evidence for the adaptation recipe's effectiveness thus rests on the overall results in Table 1 rather than on component-level validation under the actual training conditions.

2. **The infilling evaluation is framed as a competitive comparison when it should be a qualitative demonstration.** Table 1 reports AR models' infilling performance by feeding only the prefix and truncating at the oracle length — a setup the paper itself acknowledges "might result in an unfair comparison." Presenting these numbers in the same table alongside DLM infilling scores and using the resulting gaps to claim DLM strength is misleading. The AR numbers are reported in parentheses, which signals awareness of the issue, but the framing still implicitly invites a comparative reading. The paper would be stronger if these were clearly separated — e.g., in a dedicated table or section emphasizing that DLMs *enable* infilling natively, not that they *outperform* AR models at it.

### Minor

3. **"Competitive with their AR counterparts" is overstated for DiffuLLaMA.** The abstract and introduction claim the adapted models are "competitive with their AR counterparts." While DiffuGPT genuinely outperforms GPT2 on most tasks (5/7 for 127M, 4/7 for 355M), DiffuLLaMA underperforms LLaMA2 substantially on knowledge-intensive tasks (TriviaQA 18.5 vs 45.4, PIQA 63.3 vs 78.3, HellaSwag 58.7 vs 74.9). The paper discusses this gap (Section 4.3 attributes it to limited training tokens), which is reasonable, but the "competitive" framing is not supported by the aggregate results for the 7B model. A more precise characterization would distinguish the GPT2-scale findings from the LLaMA2-scale findings.

4. **Unconditional generation evaluation uses GPT2-large as the perplexity evaluator, which could favor models derived from GPT2.** Figure 3 evaluates perplexity using GPT2-large, which is consistent with prior work (SEDD also used GPT2-large), but DiffuGPT is adapted from GPT2 and trained on FineWeb, whose distribution is closer to GPT2's training data than SEDD's OpenWebText. This creates a potential confound. The paper does not discuss this or provide a control (e.g., an independent held-out LM for evaluation). The distinct 2-gram diversity metric partially addresses content diversity but not distributional bias.

5. **The attention mask annealing schedule is underspecified.** The paper states "10K-step attention mask annealing" and "sample the amount of context from the right side and progressively increase this amount" but does not specify the shape of the schedule (linear, stepwise, cosine). Reproducing the exact procedure would require guessing this detail. (This may be addressed in the appendix, which was stripped by the parser, but the main text should be self-contained on this point.)

### Trivial
None.

## Nice-to-Haves
- A controlled experiment validating the necessity of mask annealing and the shift operation during actual adaptation pretraining (e.g., at 355M scale on a data subset).
- A time-embedding ablation to validate the claim that it is unnecessary when adapting from AR models.
- Inference speed comparison against optimized AR decoding methods (e.g., speculative decoding) for a more complete picture.
- Reporting whether any test data was filtered out from the training corpora (data contamination check).

## Removed Points
- **Missing comparisons with MD4/RADD in Table 1**: Removed. The paper justifies this choice (Section 4.2: "MD4 and RADD are based on and compared with SEDD, so we mainly compare SEDD") and MD4 appears in Figure 3 for unconditional generation. This is a reasonable baseline selection.
- **Grammar/style nitpicks**: Removed per rules (parser artifacts).
- **Reproducibility concerns about missing appendix details**: Removed per rules (appendix was stripped by the parser).
- **Inference speed comparison with optimized AR (speculative decoding)**: Moved to Nice-to-Haves. It would strengthen the paper but is not a core flaw.
- **Time embedding ablation**: Moved to Nice-to-Haves. A reasonable suggestion but not a required experiment.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
1. Reframe the infilling results: separate them into a dedicated section or table that emphasizes DLMs' *capability* for native infilling rather than presenting them as a head-to-head comparison with AR models on a task they were not designed for.
2. Calibrate the "competitive with AR counterparts" claim to the evidence: note that DiffuGPT achieves this but DiffuLLaMA shows a larger gap, particularly on knowledge-intensive tasks, explain the likely cause (insufficient training tokens), and present this as a promising direction rather than a definitive result.
3. Validate the adaptation recipe components on actual adaptation pretraining (e.g., 355M on a 10B-token subset) to directly confirm their necessity.
4. Include a control evaluator (e.g., a non-GPT2-derived LM) for the unconditional perplexity measurement in Figure 3 to rule out distributional bias.
5. Specify the exact annealing schedule (shape, rate) either in the main text or in a clearly referenced appendix.

## Score and Decision

I performed calibration across multiple rounds. In Round 1, I identified the broad bracket: the paper is substantially stronger than the Latent Diffusion with LLMs paper (avg 3.0, reject) and the Reparameterized Discrete Diffusion paper (avg 5.5, reject), but below the Block Diffusion paper (avg 8.0, Oral). In Round 2, I narrowed to the range 5.5–6.5 by examining DiTTo-TTS (avg 6.25, Accept — comparable in experimental thoroughness but less novelty) and Text Hallucination in Diffusion Models (avg 6.0, Accept — comparable quality but different contribution type). The paper under review has a clearer methodological contribution than DiTTo-TTS and broader evaluation than Text Hallucination, but weaker ablation rigor and some overclaiming. This positions it at 6.0 — a solid Accept.

**Anchors used:**
- tyEyYT267x.md (Block Diffusion, avg 8.0, Round 1): Stronger theoretical grounding, more rigorous experiments, Oral acceptance. Our paper is below this.
- 1pTlvxIfuV.md (Reparameterized Discrete Diffusion, avg 5.5, Round 1/2): Mixed reviews, inconsistent results, insufficient ablation. Our paper is stronger.
- Xe6UmKMInx.md (Latent Diffusion with LLMs, avg 3.0, Round 1): Limited toy experiments, unclear method. Our paper is substantially stronger.
- hQvX9MBowC.md (DiTTo-TTS, avg 6.25, Round 2): Similar experimental thoroughness, accepted as Poster. Comparable quality.
- SKW10XJlAI.md (Text Hallucination in Diffusion, avg 6.0, Round 2): Solid analysis paper, accepted as Poster. Comparable quality.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>
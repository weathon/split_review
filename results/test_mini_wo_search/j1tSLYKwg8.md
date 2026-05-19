Now I have a thorough understanding of the paper and all reviewer claims. Let me produce the consolidated final review.

## Summary
The paper proposes a recipe to convert pre-trained autoregressive (AR) language models (GPT2, LLaMA2) into diffusion language models (DLMs) called DiffuGPT and DiffuLLaMA via continual pre-training. The adaptation uses attention mask annealing, a shift operation inherited from AR models, and a time-embedding-free architecture. The paper scales DLMs to 7B parameters for the first time, demonstrates SOTA results among prior DLMs, and evaluates on a broad set of tasks beyond perplexity. The core thesis — that AR models can be practically adapted into DLMs with modest additional training data — is sound and represents a practical advance.

## Strengths
- **First demonstration of 7B-parameter DLMs with SOTA among prior DLMs**: DiffuLLaMA (7B) outperforms prior DLMs (Plaid 1B, SEDD, MD4) across a broad set of tasks (e.g., HellaSwag 56.8 vs. 39.3 for SEDD, LAMBADA 65.1 vs. 47.7), significantly expanding the scale at which DLMs have been studied (paper §4.3, line 209).

- **Practical adaptation recipe that works with modest data**: DiffuGPT (355M) surpasses GPT-2 Medium on 7/8 tasks after only 30B–65B tokens of additional training, and DiffuLLaMA achieves nontrivial capability with 60B additional tokens despite starting from a 2T-token pre-trained base (paper §4.3, lines 209-213). The adaptation recipe is simple and reproducible.

- **Unified theoretical formulation connecting AR and diffusion objectives**: Section 3.2 explicitly shows that both AR and discrete diffusion losses are cross-entropy functions differing only by a reweighting term and a masking indicator (Eq. 8–9). This provides a principled foundation for the adaptation approach.

- **Inference speed advantage for long sequences**: DiffuLLaMA with 256 diffusion steps generates 1024+ token sequences faster than LLaMA2-7B with incremental decoding when using flash-attention 2, and the gap widens for longer sequences (Figure 5). This is a concrete efficiency result.

- **Comprehensive evaluation beyond perplexity**: The paper evaluates on 11 diverse tasks spanning reasoning, commonsense, infilling, math, and code, addressing a well-known limitation of prior DLM work that reported only perplexity (paper §4.2, lines 190-206).

- **In-context learning and self-consistency benefits at 7B scale**: DiffuLLaMA shows improvement from zero-shot to few-shot (e.g., TriviaQA improvement from 37.0 to 50.3) and benefits from self-consistency majority voting (hit@3 of 67.8 on TriviaQA), demonstrating that the adapted model retains ICL abilities from the base AR model (paper §4.4, lines 232-239).

## Weaknesses

### Fatal
None.

### Major
- **Missing mathematical justification for the shift operation under the ELBO**: The paper inherits the AR shift operation (output at position \(n\) predicts token \(n+1\)) but never derives whether this preserves the ELBO objective in Eq. 7. The standard DLM loss (Eq. 7) uses targets \(\mathbf{x}_0^n\) at position \(n\); with the shift, the target becomes \(\mathbf{x}_0^{n+1}\). The paper states only that it "align[s] prediction targets so that the diffusion model learns to recover the original signals" (line 152) without showing mathematically that this shifted objective recovers a valid ELBO. This is not a fatal error — the empirical results suggest the recipe works — but the paper's claim of principled derivation is incomplete without this justification. The reader cannot verify whether the shift is theoretically sound or merely a heuristic that happens to work.

- **Ablation study does not validate the actual pre-training procedure**: The ablation (Table 3) is conducted on a finetuning task (GSM8K-symbolic), not on the large-scale continual pre-training that constitutes the paper's main contribution. The paper itself acknowledges this limitation: "Direct ablation on adaptation training is costly; hence, we conduct preliminary experiments" (line 244). Additionally, attention mask annealing — presented as a core methodological innovation (Section 3.3) — was found to have "minimal impact" in this ablation and was omitted entirely for the 7B model (line 250). This weakens the empirical support for the claimed recipe's components.

- **Mask annealing omitted for the 7B model despite being a core contribution**: The paper presents attention mask annealing as one of three key adaptation techniques (Section 3.3, Figure 1), but for the main result (DiffuLLaMA 7B) it is omitted because it had "minimal impact" and was incompatible with flash-attention 2 (lines 184, 250). This raises the question of how essential the annealing actually is. If the 7B model directly uses bi-directional attention without annealing, the role of this component is unclear.

### Minor
- **Framing overstates DiffuLLaMA's competitiveness**: The abstract and introduction claim the models are "competitive with their AR counterparts." The paper's own results show DiffuLLaMA lags behind LLaMA2 on most non-infilling tasks (line 209: "DiffuLLaMA's performance still falls short of the LLaMA2 model"), and the training token disparity (60B vs. 2T tokens) is substantial. The contribution is better framed as: *after only 60B additional tokens, an adapted DLM retains substantial capability from the base AR model while gaining infilling and parallel generation abilities that AR models lack.* The paper partially acknowledges this in the main text but the abstract-level framing remains too strong.

- **No variance or statistical significance reported**: The paper reports only point estimates for all evaluation metrics (Tables 1-3) without standard deviations, confidence intervals, or multiple runs. This makes it impossible to assess whether reported differences (e.g., the small degradation from removing mask annealing in the ablation) are meaningful or within noise.

- **CoT performance drop attributed to "lack of instruction tuning" without evidence**: The paper speculates that the CoT performance drop "is likely due to the absence of instruction tuning, similar to the findings in LLMs" (line 238), but no experiment or citation supports this claim for diffusion models specifically. This is presented as an explanation rather than a hypothesis.

- **Mask annealing schedule underspecified**: The annealing schedule (how often the ratio is increased, at what rate, over how many steps) is not described. The paper only mentions "10K-step attention mask annealing" for DiffuGPT (line 173) but provides no details on how the context amount is sampled or progressively increased during those steps (line 148). This hinders reproduction.

- **Effective training tokens / data repetition not discussed**: A footnote states "effective training tokens exceed this count, meaning that we train for more than one epoch" (line 173, footnote), but the paper never reports how many epochs or discusses potential overfitting concerns from repeating data.

- **No memory comparison for inference**: The paper reports only single-batch latency (Figure 5), not memory usage. Diffusion models performing 256 steps of full self-attention may have substantially higher memory requirements than AR models with KV caching, which is relevant for practical deployment.

### Trivial
- **Unconditional perplexity evaluation uses GPT2-large as the evaluator**: The paper follows prior work (SEDD) in using GPT2-large to compute perplexity of generated text (line 225), but this may introduce bias since GPT2 is an AR model evaluating non-AR generation. The limitation is not discussed.

- **Infilling comparison acknowledged as potentially unfair but glossed**: The paper notes that AR baselines are not given suffix information for infilling tasks (line 213) but still claims DLM superiority. The paper acknowledges this briefly but the framing still emphasizes the DLM advantage.

## Nice-to-Haves
- **Data quality control experiment**: DiffuGPT uses FineWeb (improved over OpenWebText used by prior DLMs). An ablation controlling for data quality (e.g., adapting on OpenWebText) would strengthen the claim that the improvement comes from the adaptation method rather than better data.
- **Human evaluation of fluency**: The perplexity-by-GPT2 evaluation could be supplemented with a small-scale human evaluation or a more robust automatic fluency metric to strengthen the unconditional generation claims.
- **Batch-size throughput comparison**: Reporting throughput at batch sizes > 1 would make the inference speed comparison more practically relevant.

## Removed Points
These points were flagged by the reviewers but are removed with justification:

1. **"Plaid 1B comparison is strained because it wasn't designed for conditional generation"** — REMOVED. The paper already addresses this at line 216, attributing Plaid 1B's weakness on conditional tasks to the continuous-discrete gap and noting Plaid 1B excels at unconditional generation. The critic's point is already discussed in the paper.

2. **"Time-embedding-free design is not a new contribution because prior DLMs also omitted time embeddings"** — REMOVED. The paper frames this as a design choice for compatibility with AR model initialization, not as a novel invention. It cites prior work that made similar observations (he-etal-2023-diffusionbert).

3. **"Missing related work on CLLM and multi-token prediction"** — REMOVED per instructions ("Do not mention missing related works").

4. **"The model does not show signs of saturation — this means it's under-trained"** — REMOVED. The paper states this observation as a note about scaling (line 188), not as a weakness. The paper acknowledges the model could benefit from more training.

5. **"ICL evidence is thin"** — PARTIALLY REMOVED. The broader claim is weakened because the TriviaQA improvement from 37.0→50.3 and hit@3 of 67.8 (from Table 2) actually constitutes reasonable evidence for ICL capability. Only the specific concern about the CoT speculation being unsupported is retained (see Minor weaknesses above).

6. **"Perplexity-only evaluation limitation"** — REMOVED. This is a criticism the paper itself already makes in Section 4.2 and then goes on to address with its comprehensive evaluation benchmark.

## Novel Insights
None beyond the paper's own contributions. The reviews surface the following tension not fully explored in the paper: the shift operation that enables effective weight initialization from AR models may be at odds with the formal ELBO derivation for discrete diffusion. This suggests an interesting direction — understanding when and why a "misaligned" training objective can nevertheless produce valid denoising behavior — but it remains a question for future work rather than a novel insight from these reviews.

## Suggestions
1. **Mathematically clarify the shift operation**: Provide a precise derivation showing the exact loss being optimized with the shift (write the shifted version of Eq. 7 explicitly) and explain why it still recovers a valid denoising objective, or else acknowledge it as a heuristic and provide empirical analysis justifying its use.
2. **Reframe comparisons honestly**: In the abstract and introduction, replace "competitive with their AR counterparts" with a more precise statement about the tradeoffs (e.g., "competitive with GPT2 while retaining most of LLaMA2's capabilities despite using 30× less training data").
3. **Report variance**: Add standard deviations or confidence intervals for at least the main evaluation results (Table 1) by running each task with multiple random seeds or measuring variance across prompts.
4. **Move ablation to the actual pre-training scenario**: Perform smaller-scale ablations (e.g., adapting GPT2-small under different mask annealing schedules and with/without the shift operation) evaluated on held-out perplexity and a few downstream tasks, rather than only the finetuning proxy.
5. **Discuss limitations explicitly**: Add a limitations section acknowledging (a) the models are undertrained and not converged, (b) potential catastrophic forgetting evidenced by TriviaQA/PIQA drops, (c) the shift operation's ELBO alignment is heuristic, and (d) the training data epoch repetition and its implications.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>
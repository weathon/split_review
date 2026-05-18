Now I have all the evidence I need. Let me construct the final review.

## Summary

This paper proposes a recipe for converting pre-trained autoregressive language models (GPT2, LLaMA2) into diffusion language models (DiffuGPT, DiffuLLaMA) through attention mask annealing, a shift operation that preserves AR-style next-token prediction targets under noise, and a time-embedding-free architecture. The method is demonstrated at three scales (127M, 355M, 7B) using less than 200B training tokens. The paper includes a comprehensive evaluation across language modeling, reasoning, infilling, and in-context learning benchmarks, and releases trained models and code.

## Strengths

- **Practical adaptation recipe with clear design choices.** The paper identifies two concrete gaps between AR and diffusion modeling (causal vs. bidirectional attention; next-token prediction vs. masked-position prediction) and proposes targeted solutions: mask annealing to gradually transition from causal to bidirectional attention, and a shift operation to reuse the AR model's learned next-token prediction head. The ablation in Table 3 confirms both components contribute to performance. This is a practical, reusable recipe that others can apply.

- **Largest DLM demonstrated at the time.** Scaling DLMs to 7B parameters substantially exceeds prior DLM work (Plaid 1B, SEDD). The paper shows that the adapted 7B model exhibits in-context learning and math reasoning capabilities, moving DLMs beyond the small-scale feasibility demonstrations that preceded this work.

- **Comprehensive evaluation beyond perplexity.** Unlike prior DLM work that relied primarily on perplexity, the paper evaluates on 7+ benchmarks including reasoning (GSM8K), commonsense (HellaSwag, Winogrande), infilling (ROCStories, Humaneval), and in-context learning. Table 1 provides a useful benchmark for future DLM research.

- **Release of models and code.** The 127M, 355M, and 7B models are released, along with adaptation and evaluation toolkits, enabling reproducibility and follow-up work.

## Weaknesses

### Fatal
None.

### Major

- **DiffuGPT vs. GPT2 comparison is confounded by different training data.** The paper claims "DiffuGPT outperforms GPT2 in most tasks" as evidence for the diffusion architecture's competitiveness (Abstract, §4.3). However, DiffuGPT is continually pre-trained on FineWeb (a larger, more curated corpus than the GPT2's WebText), while GPT2 is evaluated *without any continued training on the same data*. The improvement could partly reflect the better pre-training data rather than the diffusion objective. No controlled AR baseline (GPT2 continued on FineWeb with the AR objective) is provided. The paper partially acknowledges this in the DiffuLLaMA vs. LLaMA2 comparison ("DiffuLLaMA's performance still falls short of the LLaMA2 model... attributed to the extensive amount of training tokens"), but the core claim about DiffuGPT's superiority over GPT2 is presented without the caveat that the data is not held constant. This undermines the headline claim about diffusion models matching or exceeding AR counterparts.

### Minor

- **Shift operation's effect on the diffusion process is not theoretically analyzed.** The shift operation trains the model at position *n* to predict token *n+1* under noise at position *n*. The paper asserts this "perceptually" still recovers original signals (Fig. 1 caption), but provides no analysis of whether the resulting model satisfies the standard forward-backward consistency of discrete diffusion (§5.2 of Austin et al.). Is the model truly denoising, or is it performing AR next-token prediction on a random subset of visible tokens? Some diagnostic evidence (e.g., whether predictions depend on right-side context, whether the model can infill masked tokens in the middle) would strengthen the claim.

- **Scaling analysis is not controlled.** The claim that "scaling diffusion language models results in improved performance" (§4.3) is based on comparing DiffuGPT 127M, 355M, and DiffuLLaMA 7B, which differ in base architecture (GPT2 vs. LLaMA2), training data (FineWeb vs. SlimPajama+Starcoder), and token budgets (≈30B vs. 65B). Performance differences could be driven by any of these factors. A proper scaling study would hold data and training budget fixed across model sizes. The paper's claim is observationally true but does not constitute a controlled scaling analysis.

- **Ablation limited to a single finetuning task.** The ablation of mask annealing and shift operation (Table 3) is conducted only on GSM8K finetuning. The authors acknowledge this ("Direct ablation on adaptation training is costly"), but without ablations on the core language modeling benchmarks, it is unclear whether both components are essential for general DLM capabilities or only for this specific downstream task.

- **Evaluation detail for multiple-choice tasks is underspecified.** For commonsense reasoning tasks (HellaSwag, etc.), the paper computes the diffusion loss (Eq. L_T) for each answer choice. But the loss involves sampling a noise time *t* and a corruption pattern; it is not specified how many noise samples are used per choice or whether the loss is averaged over multiple samples. This could introduce variance in the reported results.

### Trivial
None.

## Nice-to-Haves

- A controlled AR baseline (GPT2 continued on FineWeb with the AR objective) would cleanly separate the effect of the data from the effect of the diffusion objective.
- Qualitative examples of infilling behavior (e.g., showing that the model correctly uses right-side context when filling masked tokens) would help validate that the shift operation preserves bidirectional reasoning.
- An analysis of position-dependent effects during generation (e.g., whether early tokens are systematically worse since they are never generated in a non-shifted manner during sampling).

## Removed Points

- *Criticism that the unified objectives + adaptation connection is weak*: The paper clearly identifies two discrepancies (reweighting, indicator) between the AR and diffusion losses and maps them to adaptation components. This is logically sound.
- *Criticism that the paper claims a "scaling law"*: The paper only claims "scaling... results in improved performance," which is an observational claim, not a fitted scaling law. The harsh critic overstates the claim.
- *Criticism about missing qualitative examples/attention visualizations*: These are not required for a systems/empirical paper at this stage of the field. Moved to nice-to-have.
- *Criticism about DiffuLLaMA underperforming LLaMA2*: The paper explicitly acknowledges this and offers an explanation. This is not a weakness — it's honest reporting.
- *Some strength-finder strengths that were generic* ("addresses an important problem") have been dropped; only specific, evidenced strengths are retained.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

- **Add a controlled AR baseline.** Continue pre-training GPT2 (small and medium) on the exact same FineWeb subset using the same training budget and hyperparameters, but keeping the AR objective and causal mask. Report these alongside DiffuGPT. If DiffuGPT still outperforms this controlled baseline, the claim about the diffusion objective providing a real advantage would be substantiated. If not, reframe the contribution as "a recipe for obtaining a capable DLM that preserves most of the AR model's capabilities" rather than claiming superiority.
- **Run the ablation on at least 1-2 additional tasks** (e.g., HellaSwag zero-shot, LAMBADA) to confirm that mask annealing and the shift operation matter beyond GSM8K finetuning.
- **Clarify the evaluation protocol for multiple-choice tasks** — how many noise samples are used, and is the loss averaged or single-sample?
- **Provide a brief analysis** (empirical, even if not theoretical) showing that the model can use bidirectional context: e.g., compare perplexity/loss on sentences with and without right-side context provided.

## Score and Decision

**Calibration Anchors:**

| Anchor Path | Avg Score | Comparison |
|---|---|---|
| `/home/.../tyEyYT267x.md` | 8.0 | Stronger theoretical analysis and cleaner experiments, but smaller scale. This paper has more practical impact but weaker controls. |
| `/home/.../WNvvwK0tut.md` | 6.5 | Cleaner controlled scaling experiments (MDMs trained from scratch, scaling laws fitted), but only up to 1.1B. Our paper scales to 7B but has confounded comparisons. |
| `/home/.../sL2F9YCMXf.md` | 6.75 | Stronger theoretical contribution (EBM correction to diffusion); our paper has more comprehensive evaluation and larger models. |
| `/home/.../Qn4HEhezKW.md` | 5.0 | Very similar topic (adapting pre-trained models to diffusion). Our paper has more methodological novelty (mask annealing, shift operation) and clearer experimental presentation. |
| `/home/.../1pTlvxIfuV.md` | 5.5 | Reparameterized discrete diffusion, rejected on novelty concerns. Our paper has a more practical contribution and broader evaluation. |
| `/home/.../71mqtQdKB9.md` | 6.6 | SEDD paper — strong theoretical contribution (score entropy). Our paper is more applied/systems-oriented. |
| `/home/.../kCnLHHtk1y.md` | 3.0 | Not comparable (image generation for Chinese ancient buildings). |
| `/home/.../u08UxVNdIo.md` | 4.75 | Not comparable (LLM jailbreak). |

The paper presents a useful practical recipe for building DLMs at scale, with clear methodological contributions (mask annealing, shift operation) and the largest DLM demonstrated at the time (7B). However, the central empirical claim about DiffuGPT outperforming GPT2 is weakened by a data confound that prevents attributing the improvement to the diffusion architecture. This is a real limitation but does not invalidate the core contribution (the adaptation recipe and its ability to produce functioning DLMs at scale). Compared to the calibration anchors, the paper sits between the 5.0-level paper (which had similar goals but less novelty and clarity) and the 6.5-level paper (which had cleaner experiments). The confound in the headline comparison prevents a higher score.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>
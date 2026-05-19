- Decision: Accept
- Avg Score: 7.00
- Scores: 3, 8, 8, 8, 8
Here is my final consolidated review.

---

## Summary

Time-LLM proposes a framework to repurpose frozen large language models (LLMs) for time series forecasting without fine-tuning the backbone. The method has two key components: (1) **patch reprogramming** — time series patches are mapped via cross-attention over learned text prototypes (derived from the LLM's own embedding space) into representations compatible with the LLM; and (2) **Prompt-as-Prefix (PaP)** — natural-language prompts containing dataset context, task instructions, and input statistics are prepended to guide the LLM's processing. The frozen LLM transforms the reprogrammed patches, and a lightweight output projection produces the forecast. Evaluations across long-term, short-term, few-shot, and zero-shot settings show the method outperforms specialized forecasting models and prior LLM-based approaches.

## Strengths

- **State-of-the-art results without LLM fine-tuning.** Time-LLM achieves average MSE reductions of 12% over GPT4TS (which fine-tunes the LLM), 20% over TimesNet, and 1.4% over PatchTST in long-term forecasting (Section 4.1). In zero-shot, it exceeds LLMTime (same 7B backbone) by 75% (Section 4.4). These gains come from training only the reprogramming network (~6.6M parameters, 0.2% of Llama-7B), with the backbone frozen.

- **Prompt-as-Prefix is a well-motivated design that avoids the precision pitfalls of direct text generation.** The paper correctly identifies that generating high-precision numeric tokens through an LLM's decoder is fragile and requires task-specific post-processing (Section 3, Figure 3). PaP sidesteps this by using prompts as contextual prefixes that influence the LLM's hidden representations without requiring it to produce numeric text. Ablations confirm PaP's importance: removal causes an 8% degradation in standard tasks and over 19% in few-shot (Section 4.5).

- **Dramatic advantage in data-scarce regimes.** In 5% few-shot, Time-LLM achieves over 20% average MSE improvement over PatchTST, DLinear, and TimesNet (Section 4.3). In zero-shot, it surpasses the second-best baseline by 14.2% MSE reduction (Section 4.4). This demonstrates that the frozen-LLM reprogramming approach is particularly valuable where in-domain training data is limited.

- **Thorough ablations validating each component.** The ablation study (Section 4.5) systematically isolates the contributions of patch reprogramming (9.2% average degradation when removed, >17% in few-shot), PaP (8% standard, >19% few-shot), input statistics (10.2%), task instructions (7.7%), and dataset context (9.6%). The scaling law is also confirmed: full Llama-7B outperforms its 1/4-capacity variant by 14.5%.

## Weaknesses

### Fatal

None.

### Major

- **Zero-shot evaluation does not support the claimed "cross-domain" generalization.** The paper states that it evaluates "cross-domain scenarios utilizing the ETT datasets" (Section 4.4). The ETT family (ETTh1, ETTh2, ETTm1, ETTm2) are all electricity transformer temperature and load data at different temporal resolutions (1-hour vs. 15-minute). This is within-domain, cross-resolution transfer, not cross-domain generalization. A genuine cross-domain test (e.g., training on ETT and evaluating zero-shot on Weather or Electricity) is never presented. The paper's framing of "cross-domain adaptation" for its zero-shot experiments is overstated and should be corrected. This does not invalidate the method's value — the zero-shot results against LLMTime (a different, cross-domain comparison) are independently meaningful — but the claim as written is inaccurate.

### Minor

- **Interpretability analysis of text prototypes is suggestive but over-claimed.** The paper visualizes learned prototypes by projecting them to their nearest words in the embedding space and concludes that prototypes "learn to summarize language cues" like "short up" and "steady down" (Section 4.5, Figure 6). However, the prototypes are unconstrained learned vectors in ℝᴰ that are post-hoc matched to pre-trained word embeddings. There is no evidence that the LLM is processing anything resembling natural language semantics about time series patterns — the nearest-word projection is a visualization artifact, not a constraint on what the prototypes encode. The framing ("summarize language cues") implies more linguistic interpretability than is demonstrated. The paper should disclaim that these are post-hoc interpretations of learned latent vectors.

- **Computational cost of the frozen LLM backbone is under-characterized.** The paper emphasizes that only 6.6M parameters are trainable (0.2% of Llama-7B) and provides an efficiency table (Section 4.5). However, parameter efficiency does not equal computational efficiency: the full Llama-7B must be loaded in memory and forward-passed for every example, incurring substantial GPU memory (~14GB in FP16) and inference latency. The paper does not report wall-clock inference time, training time, or peak memory usage for the overall system, and does not compare these against the lightweight specialized models it outperforms. This makes it difficult for practitioners to evaluate the performance–cost tradeoff.

### Trivial

- Section 4.3 describes "few-shot" as 10% and 5% of training data, following the GPT4TS protocol. This is not a flaw, but the term "few-shot" in the LLM literature typically connotes very few examples (e.g., 5–10). The paper should clarify early that its few-shot setting means reduced-data (hundreds to thousands of steps), not the extreme low-data regime.

## Nice-to-Haves

- **Add a control experiment replacing the frozen LLM with a randomly initialized transformer of the same architecture.** This would directly test whether the pre-trained weights are responsible for the performance gain, which is the paper's core thesis. The ablation study shows that a smaller LLM hurts performance, but a randomized-backbone condition would be a cleaner causal test.

- **Report error bars / standard deviations across multiple runs.** All results are point estimates. Given sensitivity to random seeds in few-shot settings, reporting variability would strengthen the claims.

- **Compare against parameter-efficient fine-tuning baselines (e.g., LoRA/QLoRA) on the same LLM.** The paper mentions QLoRA in passing but does not run it as a baseline. A direct comparison between reprogramming and light fine-tuning of the same backbone would clarify the advantages of the frozen approach.

- **Characterize failure modes.** The paper presents uniformly positive results. Discussing settings where the LLM's prior knowledge might hurt (e.g., highly stochastic or non-stationary series that contradict patterns seen in text pre-training) would improve the paper's scientific rigor.

- **Quantify prompt engineering effort.** The prompts include dataset context, task instructions, and input statistics — these appear to require per-dataset hand-crafting. Reporting the effort or sensitivity to prompt wording would help assess practical deployability.

## Removed Points

These points were raised by reviewers but are excluded from the main weaknesses for the reasons stated:

- **"Missing tables prevent verification of results."** — Parser artifact; original submission contains them. Removed per instructions.
- **"Missing discussion of time series foundation models (TimesFM, Lag-Llama)."** — Removed per instructions (do not mention missing related works).
- **"The method processes each channel independently and cannot model cross-channel dependencies."** — This follows the standard PatchTST protocol (cited). Not a weakness of this paper specifically.
- **"No comparison with time-series-specific foundation models."** — The paper is about repurposing LLMs, not about building time-series-specific models. The scope is clearly stated.
- **"Formatting/style nitpicks"** — Removed per instructions.
- **Strength Finder: generic strengths like "the problem is important" or "the paper is well-written."** — These are too generic to include as specific strengths in a technical review.

## Novel Insights

Beyond the paper's own contributions, the most interesting observation from the review process is the tension exposed by the zero-shot evaluation: the ETT family is treated as "cross-domain" when it is actually within-domain at different resolutions. This reveals a broader gap in the time-series-for-LLMs literature — there is no established benchmark for truly cross-domain zero-shot transfer. The paper's otherwise strong evaluation would be significantly improved by defining such a benchmark (e.g., train on ETT, zero-shot on Weather/Electricity/Traffic). The fact that this gap exists across multiple papers in this area, not just this one, suggests the community needs a standardized cross-domain zero-shot forecasting protocol.

## Suggestions

1. **Reframe the zero-shot results accurately.** Replace "cross-domain scenarios utilizing the ETT datasets" with "across different temporal resolutions within the electricity transformer domain" and add a brief discussion acknowledging that genuine cross-domain zero-shot evaluation remains future work.
2. **Add a randomized-backbone control experiment** (randomly initialized Llama-7B, same architecture, frozen) to directly test whether pre-training matters, not just model scale.
3. **Report wall-clock inference time and peak GPU memory** alongside the parameter counts, and include at least one lightweight baseline for comparison.
4. **Add standard deviations** over 3–5 runs for at least the few-shot and zero-shot settings.
5. **Soften the interpretability claims** — describe the prototype visualization as a post-hoc matching to the nearest embedding, not as evidence that the LLM processes natural language semantics of time series patterns.

Now I have a thorough understanding of the paper and all the reviewer claims. Let me write the consolidated review.

## Summary

This paper presents a comprehensive empirical study of attention sink in autoregressive language models — the phenomenon where models allocate disproportionate attention to the first token. The authors systematically investigate how optimization (learning rate, weight decay, training steps), data distribution, loss function (prefix LM, windowed attention), and model architecture (positional embeddings, normalization placement, attention operation) influence the emergence of attention sink. The key findings are: (1) attention sink can be shifted to arbitrary positions by manipulating data distribution or loss; (2) the sink token acts primarily as a key bias storing surplus attention, with its value playing a non-informative role; and (3) the phenomenon stems from the normalization step in softmax attention — replacing softmax with sigmoid attention without normalization eliminates measurable attention sink in models up to 1B parameters while maintaining comparable perplexity.

## Strengths

- **Systematic, controlled empirical mapping of emergence conditions**: The paper isolates the effects of optimization steps, learning rate, weight decay, training data amount, prefix language modeling, window size, positional embeddings, and normalization placement on sink emergence (Figures 4–6, Tables 2, 10). This comprehensive treatment goes well beyond prior work (Xiao et al., Cancedda, Sun et al.), which largely described the phenomenon without investigating its enabling conditions. The controlled small-scale pre-training experiments (60M LLaMA-style models) are thoughtfully designed and clearly communicated.

- **Demonstrates attention sink functions as key biases, not value biases**: By introducing explicit key biases (K biases) and showing they shift sink away from the first token — while value biases alone do not — the paper provides a novel functional characterization (Table 4, Section 7.3). The finding that zero-valued V biases are sufficient (and that large V norms cause sink to revert, confirming a trade-off) cleanly distinguishes attention sink from register tokens in ViTs.

- **Identifies softmax normalization as the causal factor**: The crucial experiment: sigmoid attention *without* normalization eliminates attention sink, while sigmoid attention *with* normalization re-introduces it (Table 6). This directly isolates the sum-to-one constraint as the mechanism, not the exponential kernel or non-negativity. The result holds at 1B parameters — a welcome scaling check. This is the paper's most impactful empirical finding.

- **Extends analysis beyond the first token**: The paper shows sink can shift to other fixed positions (prefix tokens, learnable sink tokens, arbitrarily fixed tokens) by modifying data distribution or loss function (Table 10, Figure 5 middle), generalizing the phenomenon and showing it is not fundamentally tied to position index 0.

## Weaknesses

### Fatal
None.

### Major
None. The paper's core empirical findings are robust and well-supported by the experiments.

### Minor

1. **The proxy attention metric for non-softmax attention is not validated across attention types.** The threshold-based metric $\mathrm{Sink}^\varepsilon_1$ (with $\varepsilon=0.3$) is defined for softmax attention scores. For sigmoid and linear attention, the paper computes "proxy attention scores" using unnormalized similarity or absolute-value-normalized variants. The same threshold is applied without calibrating it to the different dynamic range and distribution of these proxies. The strongest claim — that sink "disappears" with sigmoid attention without normalization — rests partly on this metric. However, the concern is mitigated by converging evidence: the paper also reports that these models have no massive activations (Figure 8), a qualitative indicator independent of the proxy metric. The authors should either validate the threshold for each attention variant (e.g., with qualitative attention maps) or report additional measures (e.g., fraction of heads above random baseline).

2. **The "inner dependence" concept is descriptively useful but imprecisely defined.** The paper repeatedly claims that attention sink "(at least partially) stems from tokens' inner dependence on attention scores as a result of softmax normalization." The term "inner dependence" is never formally defined. The empirical evidence is strong — the normalization ablation (sigmoid with vs. without normalization) cleanly shows that the sum-to-one constraint drives sink — but the paper's preferred framing is somewhat underspecified. The contribution would be better communicated by directly stating the mechanistic finding (the sum-to-one constraint forces models to dump surplus attention mass somewhere) rather than invoking an undefined term.

3. **Scaling evidence is limited.** Most experiments use a 60M-parameter custom LLaMA model. The critical 1B sigmoid-attention experiment (Section 7.4) is a single configuration at a single scale. While the paper convincingly demonstrates sink in existing models from 14M to 70B (Figure 4), the *intervention* experiments (sigmoid/no-normalization, K biases) are only validated at small scales. The authors should either (a) explicitly discuss the possibility that sigmoid attention might exhibit sink at much larger scales (e.g., 7B+) as a limitation, or (b) provide more scaling checkpoints (e.g., 350M, 760M). This does not invalidate the results but limits their generality.

### Trivial

- The paper occasionally frames descriptive findings as explanatory. Phrases like "deep understanding" in the title and abstract set an expectation of mechanistic explanation that the empirical methodology (which is correlational/observational in many parts) does not fully deliver. The paper is better characterized as a "systematic empirical characterization" — which is genuinely valuable — than as a "deep understanding." This is a framing issue, not a content issue.

## Nice-to-Haves

- **Downstream task evaluation for sink-free models:** The paper reports comparable *validation loss* for sigmoid-attention models (3.10 vs. 3.07), but loss is not the only metric. Reporting standard benchmarks (e.g., on the Pile validation set) for the sink-free 1B model would increase confidence that removing sink does not silently degrade generalization.
- **A simple toy model or formal argument** illustrating why the sum-to-one constraint forces attention mass to concentrate on a fixed token (e.g., showing that under uniform or near-uniform queries, the only way to satisfy the constraint is to allocate surplus to a constant-position token with high-key-similarity). This would transform the "inner dependence" intuition into a crisp claim.
- **Calibration of the proxy metric** for sigmoid attention by showing qualitative attention maps (like Xiao et al.'s original "vertical" pattern figures) to confirm that near-zero $\mathrm{Sink}^\varepsilon_1$ indeed corresponds to the absence of a visible sink pattern.

## Removed Points

These points were raised by reviewers but are either factually incorrect, misread the paper, or violate the review guidelines:

- **"Non-informative value claim is over-reached" (Harsh Critic, Issue 1):** The paper uses "could be non-informative" (abstract) and "could be completely non-informative" (Section 7.3) — both are appropriately hedged. The K-bias experiment shows replacement with zero-valued V works, which *supports* the "could be" claim. The Table 5 control (large-norm V reverts sink to first token) does **not** contradict the claim; it simply shows a trade-off boundary, which the paper explicitly acknowledges. The critic reads a stronger definitive claim than what the text actually states.

- **"The paper does not factor out which property matters (normalization vs. kernel)" (Harsh Critic, Issue 2, part):** This is factually incorrect. The paper explicitly compares sigmoid attention **with normalization** (sink re-emerges) vs. **without normalization** (sink disappears) in Table 6. This directly isolates normalization as the causal factor, holding the sigmoid kernel fixed.

- **"Treatment of repeated tokens is confusing" (Harsh Critic, Other Observations):** The paper's account is coherent: when *all* tokens are identical, they *all* have massive activations, so attention is distributed evenly rather than concentrated on one token ("dispersing the attention sink"). There is no contradiction between "massive activations cause sink" and "uniform massive activations disperse sink" — the former describes a concentration phenomenon; the latter describes the case where the concentration mechanism has no unique target.

- **"Organization is occasionally disjointed" (Harsh Critic, Other Observations):** A pure presentation preference. The paper's structure (observational properties → intervention experiments) is logical for an empirical study.

- **"Formatting/style nitpicks":** References to two-column layout with inline tables and parser artifacts are not author errors.

## Novel Insights

Beyond the paper's own contributions, the most insightful pattern across the review process is that the paper's empirical methodology is its strength, not its weakness. The reviewer's criticisms that the paper lacks "deep understanding" or a "formal argument" are demands for a different kind of paper. The paper's actual contribution — a systematic, factor-by-factor empirical ablation of when sink emerges — is precisely the kind of work the community needs to move beyond anecdotes about attention sink. The most valuable result (normalization is the cause, separable from the kernel) is cleanly demonstrated by the sigmoid-with/without-normalization comparison, which the critic missed. The proxy metric concern is real but manageable, and the paper would be strengthened by a straightforward validation of it.

## Suggestions

1. **Validate the proxy metric** for non-softmax attention by either (a) showing qualitative attention maps for sigmoid-attention models to visually confirm the absence of a "vertical" pattern, or (b) reporting additional measures (e.g., fraction of attention to first token vs. uniform baseline) alongside the threshold-based metric.

2. **Replace the term "inner dependence"** with a more precise statement: e.g., "the softmax normalization forces attention weights to sum to 1 across all tokens, which creates pressure to allocate residual attention to a fixed-position token when no single token is semantically dominant."

3. **Add a scaling limitation paragraph** to the discussion explicitly noting that the sigmoid/no-normalization result is verified at 1B but may not hold at much larger scales (7B+), and that verifying this is future work.

4. **Tone down the "deep understanding" framing** in the title and introduction to better match the empirical/observational methodology. "A Systematic Empirical Study of When Attention Sink Emerges in Language Models" would be more accurate and less vulnerable to the criticisms levied in this review.

5. **Run a simple additional calibration** for the proxy metric: for the sigmoid-attention model, compute $\mathrm{Sink}^\varepsilon_1$ on synthetic data where you *know* the sink is present (e.g., by adding an explicit key bias) to verify the threshold captures it, and on data where you know it is absent (the trained model) to verify the threshold reports near-zero.

## Score and Decision

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>
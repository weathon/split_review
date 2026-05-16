Now I have a thorough understanding of the paper. Let me compose the consolidated review.

## Summary

This paper studies how weight decay affects token-level learning dynamics in language models. Using Apple OpenELM (270M, 3B) and Qwen2 (0.5B, 1.5B) models trained on the IMDB dataset, the authors show that increasing weight decay raises per-token cross-entropy loss for low-frequency tokens while high-frequency tokens remain largely unaffected, and that this effect is invisible in aggregated training loss. A theoretical analysis using the unconstrained features model (UFM) is provided to explain why frequency mediates the impact of weight decay.

## Strengths

1. **Reveals a genuine token-level bias of weight decay across multiple model architectures and scales.** Figures 1 and 5 explicitly show that increasing weight decay raises per-token cross-entropy for low-frequency tokens while high-frequency tokens are nearly unaffected, using four model variants from two families (OpenELM, Qwen2) ranging from 270M to 3B parameters with 5 seeds each and confidence intervals. This provides credible evidence that the phenomenon is not an artifact of a single architecture.

2. **Introduces and validates a per-token learning speed metric.** The AUC-based normalized metric (Section 3) provides a concrete, replicable quantification of how quickly individual tokens are learned, and Figures 4(b)-5(b) consistently show that the learning-speed gap between low- and high-frequency tokens widens with higher weight decay.

3. **Uses a token-balanced loss to expose the hidden degradation.** Figure 3 shows that while average training loss increases only slightly from λ=0.0 to 1.0 (0.051→0.068), the token-balanced loss rises sharply (0.066→0.163), directly illustrating why aggregated metrics miss the problem. This diagnostic is simple and potentially useful for practitioners.

4. **Adopts rigorous experimental methodology within the chosen setup.** Experiments use 5 random seeds, results are reported with mean±std, AdamW decouples weight decay from learning rate, and controlled hyperparameters strengthen reliability.

## Weaknesses

### Major

1. **All evaluation is conducted on training data only — no held-out or test set results are reported.** The paper repeatedly claims that weight decay "degrades" or "impairs" performance on low-frequency tokens (abstract, line 47, line 51, line 259, line 261), but every per-token loss and accuracy figure (Figures 1, 3, 4, 5, Table 1) is computed on the training split. The purpose of weight decay is to improve generalization; without measuring token-level performance on unseen data, one cannot distinguish between (a) a harmful bias that degrades real-world utility and (b) a form of regularization that prevents the model from overfitting to rare training-set tokens — which could actually be beneficial. This gap fundamentally limits the conclusions that can be drawn. (Verified: the paper contains no mention of test/validation sets or held-out evaluation.)

2. **The tokenizer is trained on the same small, domain-specific corpus used for training, coupling the frequency distribution to a single domain.** The paper uses IMDB alone (25k/75k samples) with a BPE tokenizer trained on that same corpus. IMDB movie reviews have a peculiar vocabulary (film names, slang, etc.). The token frequency distribution shown (e.g., 95% of tokens captured by top 0.01% of tokens) is dataset-specific. Without evidence from at least one other domain (e.g., Wikipedia, C4 subset) with a standard pre-trained tokenizer (e.g., GPT-2), the paper's claims about "language" broadly are not supported. The conclusion specifically warns about expanding vocabulary sizes in LLaMA-3/Qwen2/Gemma-2, but the experimental evidence does not test whether the phenomenon occurs with those tokenizers or on those data distributions. (Verified: Section 3 confirms only IMDB/IMDB-xl and a BPE tokenizer trained on IMDB.)

### Minor

1. **The experimental setup is far from representative of realistic LLM training, which the paper's framing invokes.** Context windows are very short (128 tokens for models <1B, 64 for larger models — line 81), training runs only 10k steps on a 25k-75k sample dataset (line 87), and training accuracy reaches ~98.8% with loss as low as 0.05, indicating heavy near-memorization. While studying phenomena in simplified settings is acceptable, the paper's rhetoric ("LLMs are widely deployed," "central dilemma for practitioners") implies relevance to realistic large-scale training that the evidence cannot support.

2. **The theoretical analysis has limited connection to actual transformer architectures.** The UFM framework requires d ≥ V (hidden dimension ≥ vocabulary size — line 225), which is violated by every practical transformer (e.g., d=768 vs V=32k). Features are treated as free parameters, ignoring all preceding layers and their training dynamics. The derivative ∂ℓ/∂λ (line 250) is presented without derivation or citation showing it follows from the stated optimization problem. The paper acknowledges these gaps in passing ("While the above formulation does not exactly match the practice") but then overclaims that the theory shows the effect is "caused by a fundamental issue" (line 252). The theory provides analogy and intuition, not a causal explanation for the transformer experiments.

3. **The practical significance of the effect is unclear.** Table 1 shows that moving from λ=0.0 to λ=1.0 increases per-token loss from 0.066 to 0.163, but per-token accuracy drops only from 98.80% to 98.71% — a 0.09% absolute decrease. Training loss rises from 0.051 to 0.068. While the relative change in per-token loss is large, the absolute performance degradation is tiny. The paper does not discuss whether this level of degradation matters for downstream tasks or real-world use.

4. **No analysis by token type (e.g., function words vs. content words, punctuation, subword tokens).** The paper bins tokens only by frequency. It is plausible that the "high-frequency" tokens that remain unaffected are mostly punctuation, stopwords, and common suffixes that are trivially predictable regardless of weight decay. Distinguishing meaningful rare content from noise would strengthen the claim.

5. **No comparison with other regularization techniques (e.g., dropout, label smoothing, token-reweighting).** The paper frames weight decay as uniquely problematic but does not test whether the bias is specific to weight decay or shared across regularizers.

### Trivial

- The derivative in the theoretical section (line 250) would benefit from a brief derivation or explicit citation.
- The restatable Proposition (lines 244-246) is stated but not derived; a reference to its proof in the cited work would suffice.
- No statistical significance tests are reported for the main comparisons.

## Nice-to-Haves

- **Test-set evaluation** (this is actually a Major weakness above, not just nice-to-have).
- Experiments on a more diverse dataset (e.g., a subset of C4 or Wikipedia) with a standard pre-trained tokenizer (e.g., GPT-2 BPE) to decouple token frequency distribution from dataset domain.
- An ablation showing how the gap between low- and high-frequency token loss scales with dataset size (the paper uses only 25k and 75k).
- Analysis of the effect on downstream metrics (e.g., perplexity on rare-word test sets or task-specific benchmarks).

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"Training for only 10k steps may be insufficient for convergence"** — The paper reports training losses as low as 0.051 (Table 1), indicating the models have effectively converged on the training data. This criticism contradicts itself (the same reviewer notes the model achieves 98.8% accuracy, which requires convergence). Removed as factually incorrect about the paper's actual results.

- **"The paper does not engage with existing literature on token frequency effects"** — Per instructions, missing related works are not to be mentioned as weaknesses since external verification is unavailable.

- **"The restatable environment is not filled"** — The proposition content IS stated (lines 245-246). The restatable environment is a LaTeX formatting choice, not a missing result. Removed as a formatting nitpick.

## Novel Insights

Beyond the paper's own contributions, the reviews surface one genuinely novel observation: the 0.09% accuracy drop (98.80% → 98.71%) despite a 2.5× increase in per-token loss (0.066 → 0.163) reveals that the effect is concentrated on a very small number of tokens where the model goes from "nearly correct" to "very wrong" in the logit space, even though classification accuracy barely changes. This suggests the phenomenon may be about confidence calibration on rare tokens rather than outright misclassification, which would have different practical implications than the paper's framing of "degraded performance."

## Suggestions

1. **Most important: add held-out evaluation.** Measure per-token loss and accuracy on a held-out test set (same tokenizer/dataset). If the effect persists on unseen data, the "degradation" claim is strongly supported. If it attenuates, the phenomenon is partly about overfitting regularization.
2. **Add at least one additional dataset** with a standard pre-trained tokenizer (e.g., use the GPT-2 tokenizer on a Wikipedia subset) to demonstrate the phenomenon is not an artifact of a dataset-specific tokenizer.
3. **Tone down the framing.** Replace "LLMs are widely deployed" rhetoric with a more measured description of what the controlled experiments actually show. Acknowledge the limitations of the setup explicitly in the paper.
4. **Provide a derivation or explicit citation** for the derivative in the theoretical section.
5. **Add a brief analysis of which token types** (function words, content words, punctuation) drive the observed effect.

## Score and Decision

The paper identifies an interesting and potentially important phenomenon — weight decay disproportionately affecting rare tokens during training. The empirical evidence within its chosen setup is credible and carefully executed. However, two major gaps prevent acceptance: (1) the complete absence of held-out evaluation (making it impossible to distinguish harmful bias from beneficial regularization), and (2) the single-domain, single-tokenizer design that does not support the paper's general claims about "language" and practical LLM training. The theoretical framework provides useful intuition but is not tightly coupled to the experiments. The paper has genuine merit as an empirical observation but requires substantial strengthening before it supports its stated conclusions.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>
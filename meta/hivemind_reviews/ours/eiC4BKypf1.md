## Summary
The paper introduces CENTaUR, a model that finetunes a linear probe on frozen LLaMA-65B embeddings to predict human choices in decision-making tasks. CENTaUR outperforms two domain-specific cognitive models (BEAST and a hybrid model) on negative log-likelihood across two datasets, reproduces human-like exploration patterns that raw LLaMA fails to exhibit, captures individual differences, and shows generalization to a related hold-out task. The core contribution is demonstrating that LLM embeddings, when adapted with a simple linear probe, can serve as effective feature representations for modeling human decision-making.

## Strengths
- **CENTaUR outperforms specialized cognitive models in predicting human choices.** On choices13k, CENTaUR achieves NLL = 48,002.3 vs. BEAST's 49,448.1; on the horizon task, NLL = 25,968.6 vs. the hybrid model's 29,042.5 (Figure 1c,e). This is the first demonstration that an LLM-embedding-based approach can surpass dedicated cognitive models in this domain.

- **Model simulations confirm that CENTaUR reproduces human behavioral patterns that LLaMA fails to capture.** CENTaUR's regret closely matches human regret (choices13k: 1.35 vs. 1.24; horizon: 2.38 vs. 2.33), while LLaMA deviates substantially (1.85 and 7.21). Critically, CENTaUR reproduces the horizon-dependent exploration effects (equal/unequal information conditions, Figure 2c–h) that are signature human behaviors identified by Wilson et al., which LLaMA entirely misses.

- **CENTaUR captures individual differences.** 52 out of 60 participants are best fit by CENTaUR, and a Bayesian random-effects model selection assigns it probability ≈ 1 of being the most frequent explanation. Even after incorporating random effects in the finetuned layer, CENTaUR (NLL = 23,929.5) still outperforms the hybrid model with the same random-effects structure (NLL = 24,166.0), showing that LLM embeddings carry information about individual variation.

- **Generalization to a hold-out task.** A model finetuned on two tasks (choices13k + horizon) achieves NLL = 4,521.1 on a held-out experiential-symbolic task, substantially better than LLaMA without finetuning (6,307.9) and random chance (5,977.7). It also qualitatively reproduces the human tendency to overvalue described (S) options over experienced (E) options (Figure 4).

## Weaknesses
### Fatal
None.

### Major

- **Fairness of the baseline comparison is not fully transparent.** The paper reports NLL for BEAST (choices13k) and the hybrid model (horizon task) but does not detail whether these baselines were fitted with the same cross-validation scheme, hyperparameter optimization, and evaluation folds as CENTaUR. BEAST and the hybrid model have free parameters (e.g., learning rates, exploration bonuses) that affect NLL. Without evidence that the baselines received comparable tuning care, the headline claim that CENTaUR "beats domain-specific models" is weakened. The NLL differences (~3% over BEAST, ~12% over the hybrid model) are modest enough that asymmetric fitting could account for them. The acknowledgements thank the BEAST authors for their help, but the paper should explicitly describe the baseline fitting procedure.

- **The framing overstates what has been demonstrated.** The title ("Turning large language models into cognitive models"), the claim of generalization to "an entirely different task" (line 80), and the discussion of a "domain-general model of human cognition" (line 100) go beyond what the evidence supports. CENTaUR is a black-box predictor (linear probe on frozen embeddings), not a mechanistic cognitive model with interpretable components. The hold-out task is a variant within the same family (description vs. experience), not a test from a different cognitive domain (e.g., memory, categorization, reasoning). The paper's Discussion acknowledges some of these limitations, but the framing elsewhere creates a mismatch between promise and delivery.

### Minor

- **No confidence intervals or error bars on the primary NLL comparisons.** The 100-fold cross-validation should naturally produce a distribution; reporting only point estimates (48,002.3, 49,448.1, etc.) prevents assessment of whether the differences are statistically reliable or could overlap given variability.

- **The hold-out generalization analysis is qualitative.** The key result (CENTaUR overvalues S-options) is shown via visual inspection of choice curves and indifference points (Figure 4). No quantitative metrics are reported (e.g., choice-curve correlation R², bootstrap tests for the overvaluation pattern). This weakens the strength of the generalization claim.

- **No ablation testing whether LLM embeddings are strictly necessary.** The paper does not compare CENTaUR against a linear probe trained on (a) random Gaussian features of the same dimension, (b) handcrafted summary statistics of the options (expected value, variance, etc.), or (c) a smaller LLaMA variant. Without such controls, it is unclear whether the LLM's representations are specifically valuable or whether any high-dimensional feature set with a linear probe would achieve similar results.

### Trivial

None.

## Suggestions
1. **Describe baseline fitting transparency.** Explicitly state how BEAST and the hybrid model were fitted (hyperparameter ranges, cross-validation scheme, number of random seeds). If the values were taken from previous publications, say so; if re-fitted, describe the procedure. This is the single highest-impact fix.

2. **Add error bars.** Report mean ± SE or a confidence interval for all cross-validated NLL values to allow readers to assess whether the reported advantages are reliable.

3. **Quantify the hold-out generalization.** Add a quantitative measure such as choice-curve correlation (R²) between human and model predictions, or a bootstrap test for the S-option overvaluation pattern.

4. **Add an ablation control.** Replace LLM embeddings with random features of the same dimension or with simple summary statistics to test whether the LLM's representations are specifically valuable.

5. **Tone down the framing.** Replace "entirely different task" with more precise language (e.g., "related but unseen task"), and qualify the "domain-general model" vision as aspirational rather than achieved. The paper's empirical contribution is strong enough to stand on its own without overclaiming.

## Score and Decision

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>

## Questions


## Decision
Accept

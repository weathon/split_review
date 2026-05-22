Now let me write the final review.

## Summary

LoLoRA is a hybrid LoRA variant that replaces backpropagation through the adapter matrix A with online local learning rules (HPCA, autoencoder) computed during the forward pass. This avoids storing the adapter's input activations for the backward pass, reducing memory relative to standard LoRA. The paper provides a theoretical analysis (Theorems 4.4–4.6) proving that under random-target assumptions, optimal A spans the top-r eigenspace of the input covariance — which justifies both EVA-style PCA initialization and online PCA updates. Experiments span GLUE (RoBERTa-large), math reasoning (LLaMA-3.1-8B on GSM8K), multimodal fine-tuning (LLaVA-v1.5-7B), and ablations on TinyLlama.

## Strengths

- **Rigorous theoretical foundation for A's optimal initialization** — Theorem 4.4 proves that under random-regression assumptions, any optimal A must be a nonsingular linear transformation of the top r eigenvectors of the input covariance. Theorem 4.5 further shows that any full-rank B gives the same expected loss, formalizing the A/B asymmetry that prior work (Zhu et al., Paischer et al.) only observed empirically. This is a clean, self-contained theoretical result that goes beyond the existing literature.

- **Clear algorithmic design with verifiable memory savings** — Algorithm 1 is explicit about freeing z after computing Az (line 6), and memory measurements in Tables 3 and 4 confirm the reduction: 26 GB vs 30 GB for standard LoRA on LLaMA-3.1-8B (~13% savings). The ablation (Table 6) systematically compares five local learning rules (HPCA, AE, HPCA no mean, SoftHebb, HPCA svd-first) and shows that only rules converging to the principal subspace (HPCA, AE) approach full LoRA performance, giving practical guidance.

- **Comprehensive experimental scope across multiple domains** — The paper evaluates on text understanding (8 GLUE tasks), mathematical reasoning (GSM8K), multimodal fine-tuning (LLaVA), and ablations on TinyLlama. This goes beyond many PEFT papers that test on only one or two setups.

## Weaknesses

### Major

- **Empirical results do not demonstrate a clear advantage over the simpler LoRA-FA (EVA) baseline.** The paper's own ablations (Tables 5 and 6) show that LoRA-FA with EVA initialization — a one-shot method that requires no online updates — achieves essentially identical performance to all online LoLoRA variants (e.g., r=8: 2.536 vs 2.535–2.536 perplexity). On math reasoning (Table 3), LoLoRA HPCA and LoRA-FA (EVA) both achieve exactly 82.9% accuracy. On multimodal (Table 4), LoRA-FA (EVA) achieves 1.070 loss vs LoLoRA HPCA at 1.075. The paper claims "HPCA consistently outperforms standard LoRA-FA in two out of three experimental setups," but this holds only against LoRA-FA with *uniform* initialization — the fairer comparison against EVA-initialized LoRA-FA shows no advantage, which undermines the practical motivation for the online adaptation.

- **Memory advantage over LoRA-FA does not exist.** Both methods avoid storing input activations for A's backward pass. Table 3 shows both at exactly 26 GB, and Table 4 shows LoLoRA at 24.1 GB vs LoRA-FA at 23.9 GB (LoLoRA is slightly *worse* due to its extra optimizer state, as the paper acknowledges in the conclusion). The narrative that LoLoRA "further reduces memory" is misleading: the savings are relative to standard LoRA, which LoRA-FA already achieves without any local updates.

- **Performance on the largest evaluation (GLUE) is consistently below standard LoRA.** On all 8 GLUE tasks, LoLoRA HPCA scores lower than standard LoRA (e.g., CoLA: 66.3 vs 69.6; MRPC: 89.9 vs 90.9; QQP: 90.6 vs 91.7). While some differences are within one standard deviation, the consistent direction of the gap across all tasks is concerning. The abstract's claim of "performance comparable to standard LoRA" is not well supported by this data.

### Minor

- **The practical advantage over LoRA-FA (EVA) is modest in scope.** The sole remaining benefit is avoiding a separate PCA pre-processing pass on training data. This is a legitimate operational convenience, but it is a relatively thin basis for a method paper. The paper would benefit from identifying and testing specific scenarios where online adaptation genuinely helps — e.g., non-stationary input distributions during training, or settings where a pre-processing PCA pass is infeasible.

- **Theoretical analysis assumes stationary targets and isolated submodules.** The paper acknowledges this limitation: "we considered each submodule isolated with stationary targets, which is not strictly the case in multilayer architecture." This means the theory justifies the *initialization* (matching EVA) but does not guarantee that online HPCA updates during training are beneficial over a frozen EVA initialization under non-stationary / multi-layer conditions — which is precisely where the empirical evidence is needed but lacking.

### Trivial

- None that carry evaluative weight beyond the points above.

## Nice-to-Haves

- Comparison against LoRA-FA (EVA) as the primary baseline in every experiment, not just in a subset — the paper currently contrasts LoLoRA against "standard LoRA-FA" (uniform init) in places, which sets up an easier comparison.
- A dedicated experiment with distribution shift during training (e.g., curriculum-style data ordering) where online adaptation could plausibly outperform a one-shot frozen initialization.
- Runtime/memory breakdown showing the cost of the additional optimizer state for local updates vs the savings from not needing a pre-processing PCA pass.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"Missing comparisons with X related work"** — removed per instructions (no external knowledge of what related works exist).
- **"Formatting/typo nitpicks"** — removed as these are parser artifacts, not author errors.
- **"The method may not scale to larger models"** — the paper already shows results on LLaMA-3.1-8B and LLaVA-7B, which are reasonable scales; this speculation adds nothing.
- **Harsh critic's claim that the method's advantage doesn't exist** — partially retained in modified form above (memory vs LoRA-FA is a fair criticism, but the "method's advantage" is nuanced: it exists vs uniform-init LoRA-FA and avoids the PCA pre-processing step).

## Novel Insights

Beyond the paper's own contributions, the review reveals a tension that the paper does not fully confront: the theoretical analysis elegantly explains *why* EVA initialization works and why local PCA updates should converge to a good subspace, but the experiments show that the *final* subspace reached by online updates is no better than what a one-shot PCA pre-computation gives. This suggests that for the tasks studied, the input distribution does not shift enough during fine-tuning to benefit from online adaptation. A paper that leans into this tension — identifying when distribution shift *does* happen and showing that online updates help precisely there — would be stronger than one that presents online adaptation as a general improvement.

## Suggestions

1. Reframe the contribution to honestly acknowledge that LoLoRA matches (not exceeds) LoRA-FA (EVA) in performance, and emphasize the operational advantage (no pre-processing PCA pass) rather than claiming "further memory reduction" or general performance improvements.
2. Add an experiment specifically designed to test online adaptation's benefits — e.g., training with data presented in an order where the input distribution shifts partway through, or tasks where the optimal subspace drifts.
3. Clarify throughout that "standard LoRA-FA" means uniform initialization, and prominently compare against EVA-initialized LoRA-FA in all main tables alongside standard LoRA.

## Score and Decision

**Calibration report:**

**Round 1 (Bracketing):** Searched three bands on topics related to LoRA fine-tuning and PEFT.
- Weak band (high_score=3.5): igGeaxOiFM (3.00, HoLoRA), 7X65yoKl3Y (3.33, ALLoRA), xi3sDtf8A0 (3.00, L-MSA), 49ti6LOUw5 (3.00, UnoLoRA) — these papers had trivial/insufficient methods or broken experiments.
- Middle band (3.5–7.5): cHyQT6Y1jY (5.75, cognitive-dissonance LLM), EQZMx8Lc0n (5.00, RoCoFT), n2VZtv8tqL (4.75), cJ9qoVZbPd (5.67).
- Strong band (low_score=7.5): STUGfUz8ob (7.60), TwJrTz9cRS (8.00, HiRA), Tzh6xAJSll (7.60), d8w0pmvXbZ (8.00).

Initial bracket: between 4.0 and 6.0.

**Round 2 (Narrowing):** Searched within (4.0,6.0) for LoRA variant with theoretical analysis.
- DM6Q45HWSk (4.75, EVA) — closely related: same data-driven PCA initialization idea but without theory or online updates. LoLoRA has stronger theory but similar empirical weakness.
- KxGGZag9gW (5.00, EigenLoRA) — another SVD-based LoRA variant with modest empirical gains.
- NXnNiT0fdp (4.75, GLoRA), X6xzYP2cMk (4.75).

Second narrowing for local/online learning in transformer fine-tuning: iP8ig954Uz (5.33, HART), Fx4fFBjn6j (5.33, DFA fine-tuning), cHyQT6Y1jY (5.75).

**Comparison to anchors:** LoLoRA's theory is stronger than EVA (4.75) which had no theoretical justification. Its empirical evidence is comparable to EigenLoRA (5.00) and RoCoFT (5.00) — all show marginal or inconsistent gains over simpler baselines. The paper is not as cleanly executed as the stubbornness paper (5.75) which had more insightful experiments. The paper is clearly above the 3.0–3.33 band where methods were trivial or fundamentally broken.

**Final score:** 5.0 — solid theoretical contribution and thorough experiments, but the core empirical claims are not convincingly supported by the evidence.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>
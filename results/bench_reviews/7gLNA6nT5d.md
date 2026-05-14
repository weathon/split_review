I've read the paper thoroughly and verified the reviewer claims against the text. Let me now produce the consolidated review.

## Summary

This paper integrates n-gram induction heads—hardcoded attention patterns that detect and attend to repeated n-gram subsequences—into transformer-based in-context reinforcement learning (ICRL). Building on Algorithm Distillation (AD), the authors show that n-gram layers reduce the amount of training data needed for generalization, decrease sensitivity to hyperparameters, and can be extended to pixel-based observations via vector quantization (VQ). Experiments in Dark Room, Key-to-Door, and Miniworld environments demonstrate that the n-gram model finds optimal hyperparameters in fewer random-search assignments than baseline AD and generalizes under low-diversity training data where AD fails.

## Strengths

- **Substantial reduction in hyperparameter search cost is clearly demonstrated.** Figure 2 shows that in Dark Room with 1K learning histories, the n-gram model finds near-optimal parameters in ~20 random assignments versus >400 for the baseline. This directly supports the claim that n-gram layers mitigate hyperparameter sensitivity, and the use of EMP over random search avoids cherry-picking.

- **Ablation studies confirm that n-gram hyperparameters do not significantly expand the search space.** Tables 1(a)–(b) show that varying n-gram length (1,2,3) and layer position ([1], [2], [1,2]) yields nearly identical EMP values (0.67–0.76), indicating minimal overhead from the new hyperparameters.

- **Permuted-mask experiment provides evidence that the n-gram mechanism itself is responsible for gains.** Table 1(c) shows that shuffling the n-gram attention matrix (simulating broken matching) yields EMP of 0.51, essentially identical to the baseline of 0.52. This rules out the hypothesis that mere additional parameters or VQ preprocessing alone drive improvement.

- **Rigorous evaluation protocol using Expected Maximum Performance (EMP).** The paper follows established methodology (Dodge et al., Kurenkov & Kolesnikov) by reporting EMP over random hyperparameter searches with fixed gradient steps and batch size, ensuring fair comparison and avoiding cherry-picking.

- **Extension to pixel-based observations is a non-trivial engineering contribution.** Adapting n-gram matching to images via VQ and showing positive results in two Miniworld environments demonstrates that the idea transfers beyond discrete state spaces.

## Weaknesses

### Major

1. **The headline "27× less data" claim is not experimentally substantiated.** The paper states that AD "needs 2048 goals and 2048 learning histories [17]" to converge, while the n-gram method succeeds with 100 goals, yielding a claimed 27× reduction. This factor is a cross-paper comparison to the original AD publication, which used different environment configurations and compute budgets. The paper does **not** run AD with 2048 goals in its own experimental setup to verify that AD can reach the same performance in these environments. Without that controlled experiment, the magnitude of data reduction is speculative. The qualitative finding—n-gram succeeds where AD fails under low-data conditions—is supported by Figure 4 and is a genuine contribution, but the precise 27× factor should not be presented as a validated result.

2. **The image-based experiments conflate VQ preprocessing with the n-gram mechanism.** The baseline AD receives raw pixels via a CNN encoder, while the n-gram method additionally uses a pre-trained VQ model to produce discrete tokens for n-gram matching. The permuted-mask ablation (Section 4.5) partially addresses this by showing that VQ tokens with *random* matching don't improve over baseline. However, this does not isolate whether VQ preprocessing alone (without any n-gram heads) provides a better latent representation that could also improve the baseline. A proper control would compare: (a) AD with CNN encoder, (b) AD with VQ encoder but no n-gram heads, and (c) the n-gram method with VQ. Without this, the image-based results do not cleanly attribute gains to the n-gram mechanism versus the discrete representation.

### Minor

3. **The 10K gradient-step budget may favor the n-gram method if the baseline converges more slowly.** Both methods are limited to 10K steps with equal batch size, which is a fair comparison *within* that budget. However, without learning curves or loss trajectories, it is unclear whether the baseline would eventually catch up given more steps. The observed advantage could partially reflect faster convergence rather than genuine robustness to hyperparameters. Reporting loss curves or running a longer-budget experiment (e.g., 50K steps) for a subset of configurations would strengthen the hyperparameter-robustness claim.

4. **Conditions differ between the ablation experiments (Table 1) and the main results (Figure 5), and the discrepancy is not explained.** In Table 1(a)–(b), EMP values for Miniworld-Dark are 0.67–0.76, far below the near-optimal ~0.96 shown in Figure 5. The paper notes that conditions differ (number of goals etc.) but does not reconcile the gap, making it hard for the reader to interpret the ablation results.

5. **Limited analysis of why n-gram matching works in partially observable environments.** In Key-to-Door (a POMDP), the "states only" matching strategy works well, but the same state (agent position) can occur both before and after collecting the key, making it ambiguous. The paper does not provide diagnostic analysis (e.g., attention visualizations, or analysis of whether the n-gram head implicitly uses reward tokens) to explain how the method resolves this ambiguity.

6. **Choice between transition-level matching `(s,a,r)` and state-only matching is not justified or analyzed.** Both are tested and both work, but there is no analysis of which strategy is most appropriate for each environment or how the choice affects performance.

### Trivial

- Table captions for the ablation results (Table 1) do not specify the experimental conditions (number of goals, learning histories), making it difficult to compare with the main results.

## Nice-to-Haves

- Train AD with more data (e.g., 2000+ goals) in the same Key-to-Door setup to validate the claimed 27× factor experimentally.
- Add a baseline with VQ encoder but no n-gram heads for the Miniworld experiments to isolate the n-gram effect from the VQ preprocessing effect.
- Report learning curves or loss trajectories for both methods to verify that any n-gram advantage is not merely faster convergence.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"The 27× figure is derived by comparing to AD's original training setup... The paper does not include an experiment where AD is trained with larger data"** — I kept this as a Major weakness but toned down the framing; the criticism is valid.
- **"It is not stated whether the transformer still receives the continuous image embeddings or only the VQ indices"** — The paper *does* state this: "During the evaluation, we only make a forward pass of the VQ model in order to get the latent vectors and indices for n-gram matching." Both are used.
- **"Hyperparameter space is not described in the main text (deferred to Appendix C)"** — Deferring detailed hyperparameter tables to the appendix is standard practice, not a weakness.
- **"The motivation for n-gram heads in RL is stated only at a high level"** — The paper explicitly cites the simplicity bias [6] and transient in-context ability [27] as motivation, which is reasonable for an empirical paper.
- **"27× less data... not supported by any experiment presented in the paper"** — I kept this as a validated weakness (see Major #1). The wording here is accurate but the point remains.

## Novel Insights

None beyond the paper's own contributions. The reviews converge on the paper's key finding—that hardcoded n-gram attention patterns improve data efficiency and training stability in ICRL—but both the reviewer and the strength finder identify the same central tension: the headline 27× claim is not experimentally validated, and the image experiments are confounded by VQ preprocessing. The most interesting observation emerging from the reviews is that the permuted-mask ablation (Table 1c) is actually a clever experimental design that partially addresses the VQ confound, even though a cleaner control is still needed.

## Suggestions

1. **Tone down the 27× claim** or replace it with a concrete statement about the empirical improvement observed in each environment (e.g., "up to 8× fewer goals in Dark Room, and qualitative generalization in Key-to-Door where AD fails"). The qualitative finding is strong enough on its own.
2. **Add a VQ-only baseline** for the Miniworld experiments: train AD with the same VQ encoder but without n-gram heads. This would cleanly separate the effect of discrete representation from the n-gram mechanism.
3. **Report learning curves** for a representative set of hyperparameter configurations to show that both methods have converged within 10K steps, or run a longer-budget experiment as a sanity check.
4. **Reconcile the discrepancy** between Table 1 and Figure 5 by explaining the different experimental conditions, or run the ablation under the same conditions as Figure 5.
5. **Add diagnostic analysis** (e.g., attention visualization) showing what the n-gram heads actually attend to, especially in the partially observable Key-to-Door environment.

## Score and Decision

**Calibration anchors** (all from the ICLR 2026 human-review corpus):

| Path | Avg Human Score | Comparison to this paper |
|------|----------------|--------------------------|
| `/home/wg25r/review_agent/human_reviews_2026/oBXfPyi47m.md` | 8.00 (Accept Poster) | Significantly stronger: comprehensive experiments, well-validated claims, no overclaimed results. |
| `/home/wg25r/review_agent/human_reviews_2026/odmeUlWta8.md` | 6.00 (Accept Poster) | Stronger: clear contribution, well-supported claims, though missing some baselines. Our paper has weaker empirical support for its headline claim. |
| `/home/wg25r/review_agent/human_reviews_2026/rb5eTktqbc.md` | 5.00 (Accept Poster) | Comparable: both have clear contributions but significant weaknesses. That paper had ambiguous contribution and limited improvement; this paper has an unvalidated headline claim and a confound. |
| `/home/wg25r/review_agent/human_reviews_2026/keCXNHOe4W.md` | 4.67 (Accept Poster) | Comparable: that paper was very simple with novelty concerns but accepted. This paper has more rigorous methodology but overclaims results. |
| `/home/wg25r/review_agent/human_reviews_2026/Rg8PBd9Ow2.md` | 4.50 (Accept Poster) | Comparable: that paper had serious theoretical issues but was accepted. This paper has cleaner experiments but an overclaimed central figure. |
| `/home/wg25r/review_agent/human_reviews_2026/C1ljauUDx5.md` | 3.50 (Reject) | This paper is stronger: clearer writing, more rigorous evaluation (EMP, ablations, controlled comparisons). |
| `/home/wg25r/review_agent/human_reviews_2026/axlhr1Y1Vf.md` | 3.00 (Reject) | This paper is stronger: sounder methodology and clearer empirical results despite the overclaimed 27× factor. |

Positioning relative to anchors: this paper is clearly stronger than the 3.0–3.5 rejected papers. It is comparable to the 4.5–5.0 accepted posters, with a similar level of methodological rigor but a notable overclaim (27×) that the accepted papers do not share. The paper makes a genuine contribution—n-gram heads improve ICRL data efficiency and stability—but presents an unvalidated headline number and has a confound in its image experiments. These issues are fixable but diminish the paper in its current form.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>
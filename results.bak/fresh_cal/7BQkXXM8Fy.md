Now I have a thorough understanding of the paper. Let me construct the final consolidated review.

## Summary

This paper presents a systematic empirical study of diffusion model design choices for offline RL planning. By training over 6,000 models, the authors isolate the effects of action generation, planning strategy, denoising network backbone (Transformer vs. U-Net), network depth, and guided sampling algorithms. They distill findings into a strong baseline called Diffusion Veteran (DV) and provide actionable practical tips. The paper's core value lies in the controlled component analysis rather than benchmark-maximizing.

## Strengths

- **Comprehensive empirical scale**: The paper trains over 6,000 models across multiple components and environments (Abstract, Section 4), enabling systematic control-variable analysis that no prior diffusion planning study provides. This scale directly supports the claim of a thorough investigation.

- **Counterintuitive finding about guided sampling backed by controlled experiments**: The paper demonstrates that Monte Carlo sampling with selection (MCSS) can outperform classifier guidance and classifier-free guidance in environments where the dataset contains enough near-optimal trajectories (Section 4.5, Figure 7). The supporting value-distribution analysis (Figure 7(b)) provides a concrete mechanistic explanation for this reversal of common practice (Janner et al. 2022, Ajay et al. 2022).

- **Separate action generation clearly superior in high-dimensional spaces**: Figure 3 shows that using inverse dynamics to compute actions from state plans ("separate") significantly outperforms joint state-action generation in Kitchen and AntMaze, while performing comparably in simpler Maze2D. The explanation — that modeling joint sequential distributions adds complexity in higher-dimensional action spaces (Section 4.1) — is grounded in the experimental gap.

- **Jump-step planning shown beneficial contra previous dense-step norm**: Figure 4 demonstrates that increasing the planning stride improves performance in most tasks. Section 4.2 notes this contradicts most prior work and relates the finding to neuroscientific timescale differences, providing a principled rationale.

- **Transformer backbone outperforms U-Net with attention analysis**: Figure 5(a) shows Transformer wins in 8 of 9 subtasks over comparable-parameter U-Nets. Figure 5(b) visualizes attention weights, revealing that the Transformer learns invariant temporal dependencies across stride: 6 attention steps × stride 4 ≈ 25 steps × stride 1.

- **Differentiation between diffusion planning and diffusion policy by task type**: Figure 8 empirically partitions domains: diffusion planning leads in Kitchen, Maze2D, AntMaze (long-horizon, sparse reward), while diffusion policy (DQL) leads in MuJoCo locomotion (short-horizon, dense reward). This provides a practical guideline for method selection.

## Weaknesses

### Fatal
None.

### Major

- **Unclear model selection protocol for DV baseline (potential test-set leakage)**: Section 3.2 describes a three-step procedure: "(1) Conduct a comprehensive search on the key components... to obtain the best results; (2) Evaluate the effect of each component using the control variable method." The paper does not clarify whether model selection (Step 1) used a held-out validation set or relied on performance on the final evaluation environments. In D4RL, the standard evaluation is on the environment simulator, and hyperparameter tuning commonly uses this metric — which makes the SOTA claim in Table 1 less clean than it appears. The paper should explicitly acknowledge this, describe any safeguards taken (e.g., separate validation tasks, fixed seed budgets, or early stopping criteria), or qualify the SOTA claim accordingly. This does not invalidate the study's main insights (which derive from controlled relative comparisons), but it tempers the absolute performance claim.

### Minor

- **Comparison between diffusion planning and diffusion policy paradigm rests on a single representative (DQL)**: Section 4.6 and Figure 8 compare DV against only DQL as the diffusion policy baseline. While DQL is a prominent method, claims like "diffusion planning outperforms diffusion policy in AntMaze, Kitchen, and Maze2D, whereas diffusion policy excels in MuJoCo locomotion" generalize beyond a single comparison. Validating against at least one additional diffusion policy method (e.g., Hansen-Estruch et al. 2023, Chen et al. 2023) would strengthen the claim that the observed pattern reflects paradigm-level properties rather than method-specific quirks.

- **Common deep learning hyperparameters not reported**: Section 3 states it excludes "common deep learning hyperparameters such as learning rates" from the study. While the paper's focus on component-level choices is legitimate, the specific values used (learning rate, batch size, number of denoising steps, noise schedule, optimizer, training iterations) are never reported for DV or any compared baseline. This harms reproducibility and makes it harder for practitioners to adopt DV as a baseline.

- **Adroit validation results stated without numerical support**: Section 4.7 says "results are consistent with our findings" for the Adroit dataset but provides no quantitative results. While the appendix may contain these (stripped by parser), the claim of cross-dataset generalization would be strengthened by at least qualitative summary numbers in the main text.

- **MCSS computational overhead not discussed**: Section 4.5 shows MCSS performing best, but unlike CG/CFG (which generate one sample), MCSS generates N candidate trajectories and evaluates them with a critic. This is N times more expensive at inference time. The paper does not acknowledge this trade-off, which is material for practitioners choosing a method.

- **Inverse dynamics model comparison results not shown**: Section 4.1 states "We tested both diffusion models and vanilla MLP as the inverse dynamics, and found similar performance between them" but does not report the supporting data or figure. Showing this would strengthen the claim that inverse dynamics choice is not critical.

- **Attention analysis is largely qualitative**: Section 4.3's analysis of attention patterns ("slashes," "vertical lines") is based on visual inspection of a single case study (Kitchen). While the invariant-length finding (6×4 ≈ 25×1) is a concrete quantitative observation, the broader claim about long-range dependencies would benefit from quantitative metrics (e.g., attention entropy, effective receptive field size).

- **Network size analysis varies only depth**: Section 4.4 (Figure 6) varies transformer depth while keeping width and number of heads fixed. The finding "deeper is not always better" is useful but incomplete without exploring whether wider shallow transformers could match deeper ones, or whether optimal depth correlates with task complexity.

- **No statistical significance testing for component comparisons**: While error bars are shown in figures, the paper does not perform significance tests for pairwise component differences. Given the large number of experiments, stating whether reported gaps are reliable across seeds would improve rigor (though single-run evaluation is common for D4RL benchmarks).

### Trivial
- The paper uses "offilne" (typo for "offline") in several places (lines 25, 27, 49, 52, 76, 188).

## Nice-to-Have

- **Direct validation of insights on other methods' codebases**: The paper's insights are demonstrated only within the DV framework. Taking a prior method (e.g., Diffuser or Decision Diffuser) and swapping one component at a time for the recommended choice would demonstrate that insights generalize beyond DV's specific hyperparameter configuration.

- **Causal test of the MCSS hypothesis**: Section 4.5's hypothesis linking MCSS effectiveness to dataset quality could be strengthened by artificially subsampling trajectories of varying quality from a mixed dataset and measuring when MCSS overtakes CFG, turning the correlational observation into a causal demonstration.

- **Computational cost vs. performance trade-off table**: For planning strategy and guided sampling, a table showing both performance and inference cost (GPU hours, wall-clock time) would help practitioners make informed trade-offs.

## Removed Points

These points were flagged by reviewers but are removed for the following reasons:

- **"Overfitting through test-set-based model selection" framed as fatal**: The harsh critic's framing that this "constitutes training on the test set" and "invalidates the paper's core claims" is too strong. The concern is real but it does not invalidate the paper — the study's main contribution is the component analysis (which uses relative comparisons, not absolute numbers), and D4RL evaluation protocol where hyperparameters are tuned on the simulator metric is standard practice across the field. Demoted from fatal framing to Major.

- **"Attention weights difficult to evaluate without the figure"**: The figure exists in the original submission (Figure 5(b)); the parser simply cannot render images. Not an author error.

- **"Hyperparameter details in appendix"**: The parser strips appendix sections from all papers. If hyperparameters are in the appendix, they exist in the original submission.

- **"Table 1 with variance and number of seeds may be missing"**: Table exists in the original submission and is referenced in the paper; parser artifacts do not make this a real weakness.

- **"Strength about solving an important problem"**: Generic. Removed per filtering rules. Similarly for other generic strengths.

- **"Strength about clarity of writing"**: While true, it is generic and not a specific evidence-backed strength.

## Novel Insights

None beyond the paper's own contributions. The reviews did not surface any novel observation that the paper itself does not make.

## Suggestions

1. **Clarify model selection protocol**: Explicitly state whether a validation set was used to select the DV configuration, or describe the search procedure and acknowledge the standard D4RL evaluation limitation.

2. **Add a hyperparameter table**: Even as a short appendix section, report learning rate, batch size, optimizer, noise schedule, number of denoising steps, training iterations, and other common hyperparameters for DV and baselines.

3. **Add a second diffusion policy baseline** (e.g., IDQL or EDP) to Section 4.6 to strengthen the planning-vs-policy paradigm claim.

4. **Report the inverse dynamics comparison data** referenced in Section 4.1 — even a brief figure or table.

5. **Add quantitative attention metrics** (e.g., attention entropy, effective receptive field) to complement the qualitative visual analysis in Section 4.3.

6. **Acknowledge MCSS computational overhead** in Section 4.5 and discuss the trade-off.

7. **Provide numeric results for Adroit** (Section 4.7) or clearly state they are deferred to the appendix.

## Score and Decision

This paper makes a solid empirical contribution to an under-explored area. The systematic study across 6,000 models yields practically useful insights that challenge common practices in diffusion planning. The weaknesses are real but addressable: the model selection ambiguity tempers the SOTA claim but does not undermine the component-level insights, and the remaining issues are presentation matters or scope limitations. The paper is well-written and the practical tips follow naturally from controlled experiments. I recommend acceptance with minor revisions.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>
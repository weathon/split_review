- Decision: Reject
- Avg Score: 3.00
- Scores: 3, 3, 3
Now I have all the information I need. Let me write the consolidated review.

## Summary

This paper proposes CFDG (Classifier-Free Diffusion Generation), a data augmentation method for Offline-to-Online RL that trains a single conditional diffusion model with classifier-free guidance to generate synthetic samples of both offline-like and online-like data during the online fine-tuning phase. The method is integrated with IQL, PEX, and APL and evaluated on D4RL locomotion and AntMaze tasks, reporting a ~15% average improvement over baselines and favorable comparison against prior data augmentation methods SynthER and EDIS.

## Strengths

- **Distribution analysis motivates the dual-generation design**: Section 3.1 presents a t-SNE visualization (Figure 1) comparing offline, online, and EDIS-generated data distributions, showing that offline data is more evenly distributed while online data is more dispersed. This analysis directly supports the paper's claim that separate augmentation of both data types is beneficial, rather than using a single generative model for only one type.

- **Single diffusion model with classifier-free guidance reduces computational overhead**: Section 3.2 describes how the method trains a single neural network to model both conditional and unconditional scores by randomly dropping the class label during training, then uses a linear combination for sampling (Algorithm 1). This avoids training a separate classifier and allows generating both data types from one model, a practical advantage over approaches requiring multiple models.

- **Integration with multiple O2O RL algorithms**: The method is tested across three distinct O2O RL algorithms (IQL, PEX, APL) covering two different data-usage paradigms (balanced replay and OORB), demonstrating versatility. Results in Table 1 show improvements on a majority of the 16 D4RL tasks evaluated.

- **Ablation study isolates the benefit of dual-type augmentation**: Section 4.3 compares CFDG generating only online data vs. generating both offline and online data across 4 tasks, with Figure 3 showing performance gains from augmenting both types, providing empirical evidence that the dual-generation design contributes to the method's effectiveness.

## Weaknesses

### Fatal
None.

### Major

1. **No variance reporting for main results (std/confidence intervals)**: All results in Table 1 are reported as point averages over 5 random seeds with no standard deviations, confidence intervals, or significance tests. The learning curves in Figures 2–3 state "Results are averaged over 5 random seeds" without specifying what any shaded regions represent. With only 5 seeds, the claimed "15% average improvement" could be within the noise of evaluation. The reader cannot determine whether CFDG reliably outperforms baselines or whether the difference is statistically significant. This is the most impactful weakness — it undermines the central empirical claim of the paper.

2. **Hyperparameter sensitivity acknowledged but not investigated**: The paper uses fixed values for critical hyperparameters: the generated offline-to-online ratio (8:2), total synthetic data ratio (r=1/3), and generation frequency (T_diff=10K or 100K). The conclusion (lines 227–231) explicitly states "the ratio of offline to online data can significantly impact performance in different environments" and that determining the optimal ratio "remains an open challenge." This is a direct admission that the reported performance is contingent on hand-chosen values that may not generalize. Without any sensitivity analysis, the reader cannot assess the method's robustness or rule out that the comparisons are skewed by suboptimal baseline configurations.

3. **Ablation does not isolate the classifier-free guidance component**: Section 4.3 identifies two main differences from prior methods: (i) classifier-free guidance and (ii) dual-type data augmentation. Yet the ablation only tests the second factor (online-only vs. both types), without comparing CFDG against a version using a standard unconditional diffusion model trained separately for each data type. The contribution of classifier-free guidance itself is therefore untested; the ablation conflates the benefits of the two design choices.

### Minor

1. **Comparison fairness with SynthER and EDIS not established**: The paper reports that CFDG outperforms SynthER and EDIS (Section 4.2), but provides no details on how these baselines were configured — whether they were re-tuned for the O2O setting, what hyperparameters were used, or whether the same data buffers and update schedules were applied. The paper only states that the base algorithms (IQL, PEX, APL) use the "original paper's implementation" (line 162), but this does not cover the SynthER/EDIS baselines. Without this information, the superiority claim is not fully substantiated.

2. **Limited ablation scope**: The ablation study (Section 4.3) is conducted on only 4 of the 16 tasks evaluated in the main experiments. While these are representative, the limited scope makes it difficult to assess whether the dual-type augmentation benefit generalizes across all task types.

3. **Missing key implementation details for reproducibility**: The paper mentions using the Elucidated Diffusion Model (EDM) framework (Karras et al., 2022) but omits specific architecture details (number of layers, hidden dimensions), training hyperparameters (learning rate, batch size, number of gradient steps per update), and sampling hyperparameters (number of denoising steps, guidance scale w, unconditional dropping probability p_uncond). These details are necessary for other researchers to replicate the method.

4. **Unclear definition of "15% average improvement"**: The abstract states a "notable 15% average improvement" while the body reports "IQL and PEX achieve a 15% average improvement" and "APL achieve a 11% average improvement." It is not specified whether this is relative or absolute improvement, nor over which exact set of tasks/benchmarks the average is computed.

### Trivial

- Minor typographical errors throughout ("offilne" for "offline" at lines 10, 12, 56, etc.) — parser artifacts, not author errors.

## Nice-to-Haves

- A brief discussion or small experiment showing that generated offline data increases state-action coverage or prevents value overestimation compared to replaying original offline data would strengthen the motivation for offline augmentation.
- Reporting wall-clock time overhead of diffusion training and sampling would be useful for practitioners evaluating the method.
- A quantitative measure of distributional similarity/difference (e.g., MMD, KL divergence) to supplement the qualitative t-SNE analysis.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Criticism about figures being missing** — The table and figures are embedded as images in the PDF; their absence in the parsed text is a parser artifact, not an author omission. The harsh critic's note that "Table 1 is missing from the parsed text" and "Figure 2 and 3: These are also missing" refers to the parsing output, not the original paper.
- **Criticism about "no error bars for learning curves"** — This is a restatement of Weakness #1 in the Major section above; including it here as separate removes duplication.
- **Strength about "consistent empirical gains" being presented as definitive** — The results exist but, as noted in Weakness #1, lack variance measures. The claim is tempered by the evidence gap rather than serving as an unqualified strength.

## Novel Insights

None beyond the paper's own contributions. The reviews did not surface any observation or connection that the paper itself does not already contain. The core insight — that separate conditional generation of offline-like and online-like data improves O2O RL — is the paper's own contribution.

## Suggestions

1. **Report standard deviations and effect sizes for Table 1** and specify what any shaded regions in learning curves represent (standard deviation, standard error, or min-max range). This is the single most impactful improvement.
2. **Conduct a sensitivity analysis on at least a subset of tasks** for the key hyperparameters: generated offline-to-online ratio, total synthetic data ratio r, and generation frequency T_diff. The paper already acknowledges these matter; analyzing them would turn a limitation into a demonstration of robustness.
3. **Add an ablation that compares CFDG against a version using a standard unconditional diffusion model** trained separately for each data type, to isolate the benefit of classifier-free guidance.
4. **Report implementation details for the SynthER and EDIS baselines** (how they were adapted to the O2O setting, whether they were tuned, key hyperparameters).
5. **Provide the diffusion model architecture and training hyperparameters** in the main text or supplementary material for reproducibility.

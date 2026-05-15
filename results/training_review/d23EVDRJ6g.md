I have thoroughly verified all claims against the paper. Let me now produce the consolidated final review.

## Summary

MotionDreamer proposes a localized generative masked transformer for one-to-many motion synthesis from a single reference motion. The method uses VQ-VAE tokenization with codebook distribution regularization (KL divergence against uniform prior) to mitigate codebook collapse, and a sliding-window local attention mechanism (SlidAttn) with overlap attention fusion (AttnFuse) to prevent the overfitting that standard transformers exhibit on single sequences. The paper reports state-of-the-art results on the collected SinMotion dataset (60 sequences), surpassing GAN-based (Ganimator), diffusion-based (SinMDM), and non-parametric (GenMM) baselines.

## Strengths

- **Sliding-window local attention (SlidAttn) with AttnFuse convincingly addresses the overfitting problem.** Table 3 quantitatively shows the standard transformer collapses (coverage 0%, diversity 0) while SlidAttn recovers to 72% coverage and meaningful diversity. Figure 6 provides qualitative evidence that AttnFuse produces natural transitions between patterns (e.g., "blackflip" → "handstand") whereas average pooling produces noise and unnatural transitions. This is the paper's strongest contribution.

- **Codebook distribution regularization demonstrably improves code utilization.** Table 2 shows that adding $\mathcal{L}_{\mathrm{token}}$ increases VQ perplexity (indicating more uniform code usage) and improves coverage and harmonic mean. Figure 5 provides qualitative confirmation that patterns are better preserved with regularization.

- **MotionDreamer achieves the best aggregate (harmonic mean) score** — 45.9 vs. SinMDM's 26.7 and GenMM's 20.6 in Table 1 — indicating the best overall balance of faithfulness and diversity. The individual metric scores also show MotionDreamer leading on most dimensions (though GenMM edges ahead on raw coverage).

- **Differentiable dequantization via sparsemax provides a measurable improvement.** Table 3 shows that adding it to SlidAttn further boosts coverage from 72.0% to 76.3% and harmonic mean from 36.5 to 45.9.

- **User study confirms perceptual advantages.** Figure 4 shows MotionDreamer receiving the highest average scores for coverage (3.9) and diversity (3.6), with competitive naturalness (3.4).

## Weaknesses

### Fatal

None.

### Major

None. No identified weakness threatens the core claims of the paper.

### Minor

- **Harmonic mean computation is underspecified, making the headline "19% improvement" ambiguous.** The paper presents a standard unweighted harmonic mean formula $HE = H/(1/x_1 + \cdots + 1/x_H)$ and states "$x_i$ is the standardized scores," but does not describe the standardization procedure (z-score? min-max? across what population?). Separately, the text mentions giving "the highest weight to metric (1) and lower weights to (2)–(5)" — but no weights appear in the formula, and no weighted harmonic mean formula is given. The individual metrics in Table 1 are interpretable independently, so this does not invalidate the paper's results, but the headline aggregate claim is not precisely reproducible as described.

- **Several key architectural hyperparameters are not reported.** The paper omits: codebook size $K$, downsampling factor $h$, window size $W$, stride $S$, number of transformer layers, number of attention heads, and the inference masking schedule (number of iterations, decoding procedure, how arbitrary length $L_g$ is achieved). While some of these can eventually be found in released code, the paper itself does not provide enough detail for independent reproduction.

- **VQ perplexity numbers cannot be interpreted without knowing codebook size $K$.** Perplexity = $\exp(-\sum p_k \log p_k)$ has a maximum of $K$ (uniform distribution). A perplexity of, say, 250 could indicate near-perfect utilization if $K=256$ or only ~50% utilization if $K=512$. Reporting $K$ alongside perplexity is necessary to assess how well the regularization works.

- **No error bars, confidence intervals, or significance tests are reported** for any quantitative results in Tables 1–3. Given the small dataset (60 sequences) and the inherent variance in one-to-many synthesis, this omission makes it difficult to assess the reliability of the reported differences.

- **AttnFuse ablation (Figure 6) is purely qualitative.** The paper argues AttnFuse outperforms average pooling, but provides no quantitative comparison (coverage, diversity, harmonic mean) for the fusion strategy specifically. The claim would be stronger with a supporting row in Table 3.

- **Applications section (especially beat-aligned dance) lacks any quantitative evaluation.** The beat-aligned dance synthesis (Section 4.5) is described with no comparison to baselines, no beat alignment accuracy metric, and no quantitative result — only a qualitative statement.

### Trivial

- **The five evaluation metrics (Coverage, Global Diversity, Local Diversity, Inter Diversity, Intra Diversity) are described in 1–2 sentences each without algorithmic detail.** However, the paper explicitly cites prior work (Li et al., 2022a; Raab et al., 2024) from which these metrics are adopted, which is standard practice. Full reproduction would require consulting those papers.

- **The inference process for the Local-M transformer is described in one sentence** ("progressively fill in a fully-masked template token sequence"). The paper references the generative masked modeling framework of Chang et al. (2022) for the masking schedule, so the broad strokes are clear, but details like iteration count and decoding are missing.

## Nice-to-Haves

- Evaluation on standard motion benchmarks (e.g., Human3.6M or AMASS subsets used in prior single-instance work) would improve comparability with future work.
- A larger user study (>20 participants, more reference motions) with inter-rater reliability metrics and statistical significance tests would strengthen perceptual claims.
- Codebook sensitivity analysis: showing how generation quality changes with different $K$, and reporting the count of dead/active codes.
- Ablation over window size $W$ and stride $S$ to show how these critical hyperparameters affect the faithfulness–diversity tradeoff.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **"The codebook regularization loss presents it as novel without comparison to alternative approaches such as online clustering or cosine similarity-based codebook learning."** — The paper does not claim to have invented KL divergence for codebook regularization; it presents it as a practical technique for the single-instance setting. The ablation (Table 2) compares with vs. without $\mathcal{L}_{\mathrm{token}}$ using standard baselines (EMA, codebook reset). Demanding specific alternative regularization methods is scope creep beyond what the paper sets out to do.

2. **"Whether the SinMotion dataset is publicly available"** — The paper states "Our implementation, learned models and results are to be made publicly available upon paper acceptance." This is a standard release commitment. Per hard rules, questioning release status of cited entities must be removed.

3. **"No standard deviation, confidence intervals, or significance tests"** — While noted (and kept as a minor weakness above), the claim that this omission is "serious" is overstated. Single-run evaluation on diverse benchmarks is the norm in this area; the paper follows community practice.

4. **"User study should have ≥50 participants, ≥10 reference motions, inter-rater reliability"** — These demands set a bar higher than standard practice for graphics/animation papers. The existing study (20 participants, 3 references, 3 samples each) is within the normal range. Moved to Nice-to-Haves.

5. **"The codebook regularization is presented as novel"** — The paper acknowledges it builds on common strategies (EMA, codebook reset) and adds KL divergence regularization. It does not claim fundamental algorithmic novelty of the KL technique itself.

6. **"The method is not compared to online clustering or cosine similarity-based alternatives"** — Scope creep. The paper compares against the relevant state-of-the-art baselines (Ganimator, SinMDM, GenMM), which are the existing approaches for single-instance motion synthesis.

7. **Strength Finder claim: "MotionDreamer achieves state-of-the-art quantitative results across ALL metrics"** — This is contradicted by the paper's own text (line 158): "GenMM reaches higher coverage but with limited diversity." MotionDreamer leads on most metrics and achieves the best harmonic mean, but GenMM leads on raw coverage. Corrected in the strengths above.

8. **The critic's claim that the harmonic mean issue is "structural" and "no amount of additional experiments on the same evaluation framework can fix it"** — Overblown. The formula is shown; the missing piece is the standardization procedure. This is resolved by specifying the standardization, not by re-running experiments.

## Novel Insights

Both reviewers independently identify the same core dynamic: the paper's genuine contributions (SlidAttn preventing overfitting, codebook regularization improving token utilization) are well-supported by the ablation studies (Tables 2 and 3), but the main quantitative evaluation (Table 1) rests on a metric construction (harmonic mean with unspecified standardization and ambiguous "weights") that is insufficiently documented. This creates an unusual situation where the paper convincingly shows that its method works via ablations, but the headline comparative claims against baselines are on shakier ground due to the opaqueness of the aggregate metric. The SlidAttn/AttnFuse architecture itself is the paper's strongest and most validated contribution; the codebook regularization and the quantitative benchmark comparison are secondary. A revision that clarifies the harmonic mean computation and adds the missing architectural details would substantially raise confidence in the remaining claims.

## Suggestions

1. **Specify the harmonic mean computation precisely:** Provide the exact formula (weighted or unweighted), describe the standardization procedure (what "standardized scores" means — e.g., min-max normalization across which set), and state the numeric weights if any are actually used. If no weights are used in the formula, remove the text about weighting metric (1) more heavily, or clarify that this refers to emphasis in discussion, not in the computation.

2. **Report all key architectural hyperparameters in the main text or a table:** codebook size $K$, downsampling factor $h$, window size $W$, stride $S$, number of layers, number of heads, embedding dimension $d$, and inference iteration count. Without these, the method cannot be reproduced from the paper alone.

3. **Add error bars or confidence intervals to Tables 1–3** to help readers assess the reliability of the reported differences.

4. **Provide a quantitative comparison for the AttnFuse ablation** (e.g., adding a "w/o AttnFuse" row to Table 3).

5. **Clarify the "19% improvement" phrasing:** 45.9 − 26.7 = 19.2 points absolute; this is ambiguous when stated as "19%." Specify whether this is absolute or relative improvement.

## Score and Decision

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>
- Decision: Reject
- Avg Score: 3.50
- Scores: 3, 5, 3, 3
Now I have a thorough understanding of the paper. Let me write the consolidated review.

## Summary

The paper proposes TSGM, a score-based generative model (SGM) framework for universal time-series generation covering both regular and irregular settings. The method combines an autoencoder (RNN-based for regular data; Neural CDE/GRU-ODE for irregular) with a conditional score network trained via an autoregressive denoising score matching loss, then generates samples recursively in latent space. Experiments on 4 datasets against 9 baselines under 16 settings (regular + 3 missing rates) show TSGM achieving the best or near-best discriminative and predictive scores.

## Strengths

- **First SGM-based universal time-series generator.** The paper is the first to adapt score-based generative models to time-series generation while explicitly handling both regular and irregular data within a single framework (Section 1, line 31: "We, for the first time, propose an SGM-based universal time-series synthesis method"). No prior work applies SGMs with autoregressive conditioning to this setting.

- **Flexible encoder/decoder framework for regular and irregular data.** The method supports RNN-based encoders for regular time-series and continuous-time methods (Neural CDE, GRU-ODE) for irregular data with minimal architectural changes (Section 3.2, lines 136–144). This is a practical strength: the core score network and training loss remain unchanged.

- **Strong empirical results across diverse settings.** TSGM achieves the best or near-best discriminative and predictive scores on 4 datasets under regular and 30%-missing irregular settings (Table 2), with the KDE plots (Figure 1) and t-SNE visualizations (Figure 3) providing qualitative evidence that TSGM covers the data distribution better than baselines. The paper reports mean and standard deviation over 10 seeds and includes sensitivity/ablation studies (Table 3).

- **Follows established community evaluation protocols.** The discriminative and predictive scores follow Yoon et al. (2019) and Jeon et al. (2022), the standard metrics accepted by the time-series generation community (Section 4.1.2). The baseline implementations use official released code.

## Weaknesses

### Fatal

None.

### Major

- **Unsupported theoretical claim in Theorem 3.1.** The paper asserts (line 184) that L₁ = Lscore, i.e., that the optimal parameters of the score network are identical whether the target is ∇log p(x_{1:n}^s | x_{1:n-1}^0) (the na¨ıve score) or ∇log p(x_{1:n}^s | x_{1:n}^0) (the denoising score). The standard denoising score matching lemma (Vincent, 2011) requires matching conditioning sets; here the network conditions on x_{1:n-1}^0 while the denoising target in Lscore conditions on the fuller x_{1:n}^0. These are different conditioning sets and the equivalence is non-trivial — no proof, sketch, or citation is provided in the main text. The paper cites this derivation as Contribution 2 (line 33: "We derive our own denoising score matching loss") and claims to "prove its correctness" (line 16), making this a significant gap in a stated contribution.

  *Why this is Major, not Fatal:* The *actual loss used in experiments* (Lscore^H, Eq. 11) is standard denoising score matching applied to per-step latent vectors h_n^s, conditioned on h_{n-1}^0, with target ∇log p(h_n^s | h_n^0). This is a reasonable training objective even without Theorem 3.1 — the gap is in the claimed chain from L₁ → Lscore → Lscore^H, not in the practical method itself. The empirical results are not invalidated, but the theoretical novelty claimed in Contribution 2 is unsupported as presented.

### Minor

- **Diversity claims rely on metrics that do not directly measure distributional coverage.** The quantitative evaluation uses discriminative score (binary classification accuracy) and predictive score (forecasting error). Neither directly measures sample diversity: a low discriminative score can arise even with mode collapse, and predictive score captures temporal consistency across samples but not diversity across generated trajectories. The paper's diversity claim ("state-of-the-art sampling diversity," abstract line 4) rests primarily on qualitative t-SNE and KDE visualizations (Figures 1, 3). This is partially mitigated because the evaluation follows standard community protocols (Yoon et al., 2019; Jeon et al., 2022), but a direct quantitative diversity metric would substantiate the claim.

- **Inconsistent reporting about which SDE variants are used.** Line 59 states: "we only use the subVP-based TSGM in our main experiments and exclude the VE and VP-based one." Line 202 states: "we only use the VP and subVP-based TSGM in our experiments and exclude the VE-based one." Table 2 and the surrounding discussion (line 250: "VP generates poorer data as the missing rate grows up") include TSGM-VP results. This inconsistency between "excluded" and "included" is confusing and should be corrected.

- **No statistical significance testing; some error bars overlap.** The paper claims "overwhelming performance" (line 248) without any statistical significance tests. For some comparisons, error bars overlap between TSGM and baselines (e.g., the Stock predictive score values reported in Table 2). Paired tests or bootstrapped confidence intervals would clarify which differences are reliable.

### Trivial

- Minor phrasing issues: "universial" (line 27) instead of "universal"; the sentence in line 150 has garbled characters ("trhece odnesctroudcetre du scionpgy") — these are likely PDF extraction artifacts rather than author errors.

## Nice-to-Haves

- Adding a direct distributional metric (e.g., MMD, 1-NN classifier-based diversity, or coverage score) would quantitatively substantiate the diversity claims.
- Presenting the full set of irregular results (50%, 70% missing) in the main paper would allow readers to assess performance trends across all missing rates without consulting the appendix.
- An ablation study isolating the encoder choice (RNN vs. Neural CDE vs. GRU-ODE) in the same setting would validate the "minimal changes" claim more directly.

## Removed Points

- **"The paper does not discuss hyperparameter tuning for baselines"**: Standard practice in this community to use official code defaults; not a meaningful weakness.
- **"Missing baselines like CSDI, DiffWave"**: Removed per instruction — missing related works should not be mentioned.
- **"50%/70% missing results relegated to appendix"**: The appendix was stripped by the parser; the results exist in the original submission.
- **"Not handling informative missingness"**: Scope creep — the paper explicitly handles random missingness, which is what it claims.
- **Strength Finder's "Theoretical derivation" claimed as a strength**: Conflicts with verified Major weakness #1; moved here because the weakness undermines it.
- **Strength Finder's generic statements** ("this paper addressed an important problem," "this paper targeted an interesting question"): Removed as superficial.

## Novel Insights

None beyond the paper's own contributions. The two reviews agree on the core strengths (first SGM for universal time-series, flexible framework, strong empirical results) and converge on the main weakness (unsubstantiated theoretical derivation in Theorem 3.1). The harsh critic's characterization of the theoretical gap as potentially "fatal" is overstated given that the practical loss used is standard DSM on latent vectors, but the critique correctly identifies that the claimed Contribution 2 is not supported as written.

## Suggestions

1. Either provide a rigorous proof of Theorem 3.1 (showing how the standard denoising score matching lemma extends to mismatched conditioning sets), or clarify that the training loss Lscore^H is standard denoising score matching applied to per-step latent vectors — remove the unsupported claim of a novel loss derivation.
2. Add a quantitative diversity metric (e.g., MMD or coverage-based) to substantiate the "state-of-the-art diversity" claim.
3. Resolve the VP/subVP/VE inconsistency: clearly state which variants are used in main experiments versus ablations.
4. Add statistical significance tests (bootstrap or paired tests) for the primary comparisons.

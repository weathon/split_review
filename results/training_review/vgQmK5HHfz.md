Now I have all the information I need. Let me construct the authoritative final review.

## Summary

The paper proposes a mutual information estimator combining the difference-of-entropies (DoE) formulation with block autoregressive normalizing flows (B-NAF). The key idea is to jointly estimate the marginal entropy H(X) and conditional entropy H(X|Y) within a single flow architecture by "deactivating" cross-connections between the X and Y subspaces. Experiments on Gaussian, cubic-Gaussian, and sparse-Gaussian benchmarks compare against discriminative estimators (MINE, SMILE, InfoNCE, NWJ, DEMI) and a separately-trained BNAF baseline.

## Strengths

- **Joint estimation demonstrably reduces bias for near-zero MI in non-linear settings.** On the cubic Gaussian task with small true MI, the separately-trained BNAF exhibits significant bias (consistent with the known shortcoming of generative models noted by Song & Ermon, 2019), while the proposed NDoE BNAF does not (Section 4.1, Figures 2–4). This directly validates the paper's central design motivation.

- **Consistently lower estimation error than discriminative methods across multiple settings.** Across Gaussian, cubic Gaussian, and sparse Gaussian benchmarks at dimensions 20–100 and sample sizes 32K–128K, NDoE BNAF achieves estimation error closer to zero than MINE, SMILE, InfoNCE, NWJ, and the standard DoE. The advantage is clearest for larger true MI values where discriminative methods severely underestimate (Figures 2–5).

- **Fair architectural comparisons.** The paper matches total hidden units between the flow-based model and discriminative MLPs (e.g., BNAF layer dimensions chosen to be roughly equivalent to 512 hidden units), and all methods are trained with the same number of epochs and consistent batch sizes (Section 4.1). This reduces confounding from model capacity differences.

- **The paper identifies and directly tests a known weakness of generative MI estimators.** Rather than ignoring the Song & Ermon (2019) critique that generative approaches have high bias near zero MI, the paper explicitly includes this scenario (cubic Gaussian, small MI) and shows its joint estimation approach mitigates the problem.

## Weaknesses

### Fatal
None.

### Major
- **The sparse Gaussian result directly contradicts the paper's central claim and is left unexplained.** On the sparse Gaussian benchmark, the paper reports that the *separately-trained* BNAF "outperformed NDoE, BNAF for larger MI" (Section 4.1). This means the separate estimation approach—which the paper's core contribution is designed to improve upon—works *better* than the proposed joint estimation method on a non-trivial benchmark. The paper offers no analysis of why this occurs, what the failure mode is, or under what conditions joint estimation helps vs. hurts. Because this result undermines the paper's central claim about the benefits of joint estimation, it demands thorough investigation and explanation.

### Minor
- **The joint training procedure is underspecified.** The paper states that cross-connections are set to zero via masking (Section 3), but the training protocol remains ambiguous. The text suggests a sequential process ("begin with a network that approximates H(X) and then optimize the off-diagonal weights") while also claiming simultaneous optimization ("Algorithm 1, which optimizes for H(X|Y) and H(X) simultaneously"). The exact training schedule (phases? alternating? joint objective with regularized masking?) is not clearly stated, and Algorithm 1—which should resolve this—is embedded in an image that was stripped. This makes the method harder to reproduce than it should be.

- **No error bars or variance measures reported despite 10 runs.** The paper states that all results are computed over 10 runs with different random seeds, yet none of Figures 2–5 display standard deviations, confidence intervals, or any measure of variability. Without this information, the reader cannot assess whether observed differences between methods are statistically meaningful.

- **Missing comparisons with the most relevant generative competitors.** The paper cites DINE (Duong & Nguyen, 2023) and Butakov et al. (2024) as related work—both are flow-based MI estimators—but does not compare against them experimentally. The conclusion explicitly defers these comparisons to future work. Since these are the most natural baselines for a generative-flow MI estimator, their absence weakens the empirical contribution.

- **Theoretical claims of consistency and unbiasedness are unsupported.** The abstract and introduction claim an "unbiased and consistent" estimator, and the conclusion states the method "converges to true mutual information as the number of samples increases." However, the paper provides no formal analysis, proof sketch, or reference establishing consistency of the joint neural estimator. The variational characterization (Lemma 2.1, Corollary 2.2) is standard DoE theory, not a consistency proof for the proposed architecture.

### Trivial
- The paper's notation for the baselines is slightly confusing: "BNAF" refers to separate estimation using two flows, while "NDoE, BNAF" is the proposed joint method. These are easily conflated.

## Nice-to-Haves
- Evaluation on non-Gaussian synthetic benchmarks from Czyż et al. (2023) to test whether the method generalizes beyond Gaussian-like distributions.
- An ablation study comparing separate BNAF vs. joint NDoE BNAF while controlling for total parameter count and compute, to isolate the effect of joint estimation from model capacity differences.
- Sensitivity analysis for key hyperparameters (learning rate, number of epochs, B-NAF depth).

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"Gaussian case is a near-trivial test"**: The paper tests cubic-Gaussian (non-linear) and sparse-Gaussian cases in addition to the standard Gaussian; the standard Gaussian serves as a basic sanity check and is standard practice in the literature. The cubic and sparse cases provide non-trivial evaluation. The criticism is overblown.
- **"Method is non-reproducible"**: This is too harsh. The paper provides the core mechanism (masking off-diagonal weights), architecture details (B-NAF layers, hidden dimensions), optimizer settings, and training hyperparameters. The underspecification is a real concern but does not render the method non-reproducible.
- **Strength Finder's claim about "theoretical foundation for consistency and unbiasedness"**: This is overstated. The paper provides variational characterizations (Lemma 2.1, Corollary 2.2) but no actual proof that the neural estimator is consistent. This "strength" conflicts with the verified weakness about unsupported theoretical claims; by the rule that weakness wins when a strength and weakness disagree, this claimed strength is dropped.
- **"Key baselines are missing" phrasing**: The reviewer criticized missing DINE/Butakov comparisons; this is kept as a minor weakness above, but the more aggressive phrasing ("unsubstantiated claims") is removed as overly harsh given the paper is transparent about deferring these to future work.
- **Formatting/style nitpicks**: Removed per instructions.
- **Criticism about missing related work**: Removed per instructions (cannot verify existence of missing works).

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a perspective on the method or the problem that the paper itself does not already articulate.

## Suggestions

1. **Analyze the sparse Gaussian failure mode.** This is the single most important issue. Investigate why separate BNAF outperforms the joint method for larger MI on sparse Gaussian. Is it an optimization difficulty (the joint objective is harder to optimize in sparse settings)? A capacity issue (the joint network's parameters are split between two tasks)? A structural issue (the block autoregressive assumption is less suitable for sparse dependencies)? This analysis could fundamentally reshape the paper's claims about when joint estimation is beneficial.

2. **Clarify the training procedure.** Provide a precise description (or pseudocode in the main text) of the training schedule: whether the two entropy terms are optimized simultaneously or in phases, how the masking is applied during training vs. evaluation, and what input is fed to the network when estimating H(X) alone.

3. **Add error bars to all figures.** Report standard deviations or confidence intervals from the 10 runs. This is essential for the reader to assess the reliability of the results.

4. **Compare against DINE and Butakov et al.** Either add these comparisons or explicitly justify their exclusion (e.g., if the comparison is technically infeasible or if the methods target different settings).

5. **Temper the theoretical claims.** Replace "unbiased and consistent" with a more precise statement: the estimator is unbiased provided the flow exactly models the target densities, and consistency depends on the flow's ability to approximate the true density (with appropriate citations to normalizing flow consistency results).

## Score and Decision

The paper tackles an important problem (MI estimation) with a reasonable core idea (joint estimation via block autoregressive flows). The empirical results on Gaussian and cubic-Gaussian benchmarks are promising, showing advantages over discriminative methods. However, the paper suffers from a significant unaddressed contradiction (sparse Gaussian result undermines the central claim), an underspecified training procedure, missing variance reporting, absent comparisons with key generative baselines, and unsupported theoretical claims. The core idea has merit but the current validation is incomplete.

Originality: 6/10 | Importance: 7/10 | Claims support: 4/10 | Experiment soundness: 5/10 | Clarity: 6/10 | Value: 5/10

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>
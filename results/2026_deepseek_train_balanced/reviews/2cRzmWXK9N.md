## Summary

This paper generalizes Direct Preference Optimization (DPO) from reverse KL divergence to a broader class of $f$-divergences including forward KL, Jensen-Shannon divergence, and $\alpha$-divergences. The key theoretical insight is that the normalizing constant $Z(x)$ cancels out in the Bradley-Terry model for any $f$-divergence satisfying $0 \notin \text{dom}(f')$, identified through KKT complementary slackness analysis. Empirically, the authors demonstrate that different divergences occupy distinct points on the alignment-diversity Pareto frontier, enabling controllable tradeoffs not possible with standard DPO.

## Strengths

1. **Clean theoretical identification of the $0 \notin \text{dom}(f')$ condition for generalizing DPO (Theorem 1, Table 1).** The paper pinpoints the exact condition under which the partition function $Z(x)$ drops out of the Bradley-Terry model for general $f$-divergences. By analyzing KKT complementary slackness to force $\alpha(y) = 0$, the paper proves that any $f$-divergence with $0 \notin \text{dom}(f')$ — including forward KL, JS divergence, and $\alpha$-divergence with $\alpha \in (0,1)$ — admits the same reward-policy reparameterization as DPO. Table 1 explicitly delineates which divergences satisfy the condition (✓) and which do not (✗, e.g., total variation, chi-squared), making the boundary of applicability precise. This is a genuinely non-trivial generalization that extends DPO's applicability.

2. **Systematic empirical characterization of the alignment-diversity tradeoff across divergences (Table 1, Section 5.2).** Table 1 on the Anthropic HH dataset provides a clean, quantitative demonstration that different divergences occupy different points on the alignment-diversity Pareto frontier: Reverse KL achieves the highest accuracy (67.19%) but lowest diversity, forward KL achieves the highest diversity at lower accuracy (54.30%), and JSD and $\alpha$-divergences interpolate between these extremes. Diversity is measured using four complementary metrics (predictive entropy, self-BLEU, distinct-1, distinct-2) at multiple temperatures, providing a thorough characterization.

3. **Honest scoping of the method's applicability (Table 1, Theorem 1).** The paper explicitly identifies which divergences can and cannot be handled by the framework, rather than overclaiming generality. The intellectual honesty of marking total variation and chi-squared as out-of-scope strengthens credibility for the divergences that are handled.

## Weaknesses

### Major

1. **No variance or statistical significance reported for any empirical result.** Table 1 reports accuracy differences as small as 67.19% vs. 66.80% (RKL vs. JSD) without confidence intervals, standard deviations, or significance tests. The IMDB experiments also report single-point frontier comparisons without error bars. For a top-tier venue, this is a meaningful gap — it is impossible to tell whether observed differences are systematic or due to noise, especially for the close comparisons (e.g., RKL vs. JSD).

2. **No evaluation on standard downstream capability benchmarks.** The paper does not measure whether alignment under different divergences degrades performance on standard LLM benchmarks (MMLU, HellaSwag, etc.). This is directly relevant to the paper's core thesis: if different divergences differentially harm general capabilities, the practical utility of the diversity-alignment knob is diminished. The absence of this evaluation weakens the practical claims.

3. **The Accuracy metric in Table 1 is not defined.** The paper reports "Accuracy (%)" on Anthropic HH but never specifies what this measures — whether it is preference prediction accuracy on a held-out test set, or an evaluation of generation quality. The Anthropic HH dataset is about helpfulness and harmlessness; without a clear definition, the reader cannot interpret what 67.19% accuracy means.

4. **Missing empirical comparison against the closest prior work (Go et al., 2023).** The paper discusses Go et al.'s $f$-divergence alignment approach in Related Work and claims that PPO with $f$-divergences "may cover" this method (line 223), but provides no direct empirical comparison. For a paper whose central claim is a practical improvement in alignment methodology, the lack of comparison to the most relevant prior method — one that also explores $f$-divergences for alignment — is a significant evidential gap. The argument that Go et al. depends on the RLHF pipeline is a methodological distinction; an empirical comparison would substantiate whether $f$-DPO's supervised nature actually yields practical advantages.

### Minor

1. **The PPO comparison on IMDB has an asymmetry that deserves more careful discussion.** PPO uses a ground-truth reward model (SiEBERT) and optimizes under the $f$-divergence penalty via RL, while $f$-DPO directly parameterizes the reward through the policy. The paper acknowledges this (line 231: "PPO utilizes the ground-truth reward during training") and introduces a PPO (loss) variant to address PPO's instability with non-KL divergences. However, the headline claim of "greater divergence efficiency than traditional PPO methods" is presented without explicitly noting that these are fundamentally different optimization landscapes — one has access to ground-truth rewards and must learn a value function, the other optimizes an implicit reward. The comparison is not unfair, but the framing could be more nuanced.

2. **The calibration theorem (Theorem 2) and its experimental validation are somewhat decoupled.** The theorem provides a bound on ECE difference in terms of $f$-divergence (with explicit forms for JS and KL in Remarks 1-2), which is theoretically sound. However, the experimental validation (Figure 10, line 297) merely shows that ECE increases over training and larger $\beta$ limits this increase — a trend that would hold for any method that constrains deviation from a reference model, not specifically validating the bound. The paper does not quantitatively check whether the actual ECE differences fall within the predicted bounds. The theory is useful, but the experiments do not directly validate it.

### Trivial

- The final paragraph of Section 4.3 (line 255) has apparent text artifacts from the parser ("preference.py}}").
- The sentence fragment "The results for temperatures $0.6$ and $1." appears to be cut off.

## Nice-to-Haves

- Report training time, memory usage, or sample efficiency to substantiate the claimed efficiency advantages over PPO.
- Ablation on $\beta$ for the HH experiments to show sensitivity to the regularization coefficient (the IMDB experiments fix $\beta = 0.1$ for $f$-DPO while sweeping it for PPO).
- A small human evaluation in addition to GPT-4 evaluation on MT-Bench, though GPT-4 evaluation is standard in the field.

## Removed Points

*These points were flagged during review but removed after cross-checking against the paper. Treat them with caution.*

- **"The RKL (DPO) comparison is absent from the paper's headline claims."** — Removed because RKL appears explicitly as a row in Table 1 (line 265). The critic's statement is factually incorrect.
- **"Domain restrictions on (f')⁻¹ for JS and forward KL would affect practical applicability."** — Removed because Theorem 1 gives $r(y|x) = \beta f'(\pi/\pi_{\text{ref}}) + \text{const}$, and the constant term absorbs any additive shift. The critic's analysis misunderstands how the constant handles domain constraints.
- **"MT-Bench results lack numeric results in text."** — Removed as a nitpick. The results are provided as a figure (Figure 9), which is a standard presentation format in papers. Further details are referenced to the appendix.
- **"No human evaluation."** — Demoted from weakness to nice-to-have. GPT-4 evaluation with >80% human agreement is standard practice in the LLM alignment literature.
- **"The calibration bound depends on unspecified ψ_f."** — Removed because the paper provides explicit bounds for JS divergence ($4\sqrt{2 D_{JS}}$) and KL divergence ($2\sqrt{2 D_{KL}}$) in Remarks 1 and 2. The critic's claim is factually incorrect.
- **"PPO comparison is structurally unfair"** — Weakened above. The paper is transparent about the setup and proposes PPO (loss) to address known instabilities. The criticism was overstated.

## Novel Insights

Both reviewers identify the same core tension: the theoretical contribution (Theorem 1) is genuinely elegant and non-trivial, but the empirical evaluation does not match the rigor expected for the practical claims made. The harsh critic's deep read of the KKT derivation and the condition $0 \notin \text{dom}(f')$ is correct and identifies this as the paper's strongest contribution. However, the harsh critic overreaches in several places (domain restrictions, calibration theorem being "generic"), while the Strength Finder correctly identifies that the systematic empirical characterization in Table 1 is the main piece of evidence that the framework delivers on its promise. The intersection of both reviews yields a clear picture: the theory is sound and useful, the diversity-alignment tradeoff is convincingly shown, but the paper overclaims on outperforming PPO and underdelivers on evaluation rigor (no variance, no downstream tasks, missing comparison to Go et al.).

## Suggestions

1. Add confidence intervals or standard deviations to Table 1 and the IMDB frontier results.
2. Clearly define the Accuracy metric in Table 1 (is it preference prediction accuracy on a held-out test set?).
3. Include an empirical comparison against Go et al. (2023) — either directly or by citing existing comparisons — to substantiate the claimed advantages of the supervised approach.
4. Evaluate on at least one standard capability benchmark (e.g., MMLU) to verify that the choice of divergence does not differentially harm general capabilities.
5. Revisit the framing of the PPO comparison to more explicitly acknowledge the different optimization paradigms.
6. Directly test the calibration bound by computing ECE and $f$-divergence values across training and checking whether the inequality holds.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>
Now I have thoroughly cross-checked all claims against the paper. Here is my consolidated review.

---

## Summary

This paper studies off-policy learning (OPL) in contextual bandits where the target reward is only partially observed. It proposes HyPeR (Hybrid Policy Optimization for Partially-Observed Reward), a method that leverages densely observed secondary rewards (e.g., clicks, dwell time) as control variates to reduce policy gradient (PG) estimation variance while maintaining unbiasedness. The paper also introduces a strategic weight-tuning procedure that intentionally deviates from the true objective weight to improve finite-sample bias-variance trade-offs. Experiments on synthetic data and the KuaiRec dataset show HyPeR outperforms target-reward-only baselines (r-IPS, r-DR) and secondary-reward-only baselines (s-IPS, s-DR) across varying observation probabilities, sample sizes, and reward correlations.

## Strengths

- **Principled PG estimator with unbiasedness and provable variance reduction.** Theorem 1 establishes unbiasedness of Eq. (10) under the full-support condition, and Theorem 2 provides variance comparison showing that when the conditional reward model \(\hat{q}(x,a,s)\) is more accurate than \(\hat{q}(x,a)\) at estimating \(q(x,a,s)\), variance is reduced relative to r-DR. This directly supports the core claim that leveraging secondary rewards reduces variance while preserving unbiasedness.

- **Data-driven strategic weight tuning that improves finite-sample performance.** Section 4.1 introduces a bootstrap-based procedure to tune the mixture weight \(\gamma\). Figure 4 (synthetic) and Figure 5 (KuaiRec) consistently show that HyPeR(Tuned \(\hat{\gamma}^*\)) outperforms HyPeR(\(\gamma=\beta\)) and all feasible baselines, validating the insight that an intentionally "incorrect" weight can improve the bias-variance trade-off.

- **Consistent empirical superiority across a wide range of challenging conditions.** Figures 1–5 show HyPeR(\(\gamma=\beta\)) and HyPeR(Tuned \(\hat{\gamma}^*\)) achieve the highest combined policy value in nearly all tested scenarios — including low observation probability, small sample sizes, and weak target-secondary correlation — which are precisely the regimes the paper targets. HyPeR(\(\gamma=0\)) also consistently outperforms r-DR, confirming that even the target-only component benefits from secondary rewards.

- **General problem formulation.** Section 2.3 and Section 3 formalize OPL with partially-observed target rewards and densely observed secondary rewards, with Table 1 providing concrete examples. This formulation is novel and captures a range of real-world settings (missing data, delayed rewards, censoring, data fusion).

- **Real-world validation on a fully-observed dataset.** The KuaiRec experiment (Section 6) uses a public dataset with actual user-item interactions and replicates the synthetic findings, demonstrating practical applicability beyond idealized simulations.

## Weaknesses

### Fatal
None.

### Major

- **Unacknowledged restrictive assumption about the observation mechanism.** The paper assumes \(p(o|x)\) — the observation indicator depends only on the context \(x\), not on the action \(a\) or the secondary rewards \(s\). This is stated in the data-generating process (Section 2.3, Eq. 3: \(p(o_i|x_i)\)). However, several of the paper's own motivating examples (Table 1), particularly e-commerce conversions observed only for clicked products and medical censoring that depends on treatment, involve observation mechanisms that depend on the action taken. When \(o\) depends on \(a\), the estimators in Eqs. (4), (5), and (10) — which use \(o_i/p(o_i|x_i)\) — are no longer unbiased. The paper claims this formulation "encompasses many realistic situations like missing data, delayed rewards, data fusion, multi-stage rewards, and censoring" without caveat, which overstates the scope. The synthetic experiments use constant \(p(o|x)=0.2\) (independent of both \(x\) and \(a\)), and the KuaiRec experiment also uses \(p(o|x)=0.2\) constant — so neither tests robustness to action-dependent missingness. This is a significant scope limitation that should be clearly discussed, including whether and how the framework could be extended (e.g., by modeling \(p(o|x,a)\)).

### Minor

- **Imprecise verbal statement of the variance reduction condition.** Theorem 2's variance expression (displayed equation before Theorem 2) is mathematically clear, but the verbal gloss "if \(\hat{q}(x,a,s)\) is better than \(\hat{q}(x,a)\) in estimating \(q(x,a,s)\)" (line 139) is too vague to serve as a crisp theoretical condition. Since \(\hat{q}(x,a)\) targets \(E[r|x,a]\) while \(\hat{q}(x,a,s)\) targets \(E[r|x,a,s]\), "better" is not defined on a directly comparable scale in the verbal formulation. The squared-error quantities in the equation are precise, but the text would benefit from stating the condition in closed form.

- **Missing imputation-based baseline.** A natural competitor is: train \(\hat{q}(x,a,s)\) on observed data, impute \(\hat{r}\) for unobserved instances, then run standard IPS/DR on the completed data. Such a baseline would help isolate whether HyPeR's advantage comes from its DR-style combination or merely from using \(s\) to estimate \(q\). The current baselines do not include this.

- **Unexplored sensitivity of the surrogate noise parameter \(\sigma_F\).** The synthetic F(s) aggregation (line 202) uses \(\sigma_F=0.4\) to simulate surrogate inaccuracy, but sensitivity to this parameter is not explored. Since the relative weakness of s-IPS/s-DR depends directly on how inaccurate F(s) is, this would be informative.

- **Bootstrap tuning procedure has limited theoretical justification.** The bootstrap-based weight tuning (Section 4.1) is a reasonable heuristic but its justification is incomplete: a bootstrap from \(n_{\text{train}} < n\) samples does not produce a dataset equivalent to \(n\) independent draws. The paper acknowledges potential overestimation issues from Saito & Nomura (2024) (line 179) but does not implement any correction or provide analysis of when the procedure is expected to work.

- **Validation estimator not specified for weight tuning.** The paper does not specify what estimator is used to evaluate policies during weight tuning (Eq. 14). If standard IPS/DR are used on the validation set, the paper itself notes they may overestimate and lead to poor selection.

### Trivial

- No dedicated limitations section. The conclusion mentions future work but does not systematically discuss the observation-independence assumption, surrogate misspecification, or other failure modes.

## Nice-to-Haves

- **Connection to surrogate/proxy methods in causal inference.** The structure of Eq. (10) resembles doubly robust estimation for missing data with a surrogate (e.g., Athey et al., 2019; Kallus & Mao, 2020). Discussing this connection would help readers understand its relationship to prior work on imputation and missing rewards.
- **Sensitivity analysis for action-space size.** The paper mentions varying action space size briefly; a dedicated experiment on action-space scaling would strengthen the analysis given that OPL variance scales with action space size.
- **Sharper theoretical analysis of the weight-tuning correction** from Saito & Nomura (2024) could be incorporated or discussed.

## Removed Points

These points were raised by reviewers but are excluded from the main weaknesses for the reasons noted:

- *"Introduction claim about 'advantage' needing clarification"* — The paper is clear that the advantage is in finite-sample performance through variance reduction; the critic's reading that this depends only on γ-tuning overlooks HyPeR(γ=0) which already shows improvement over r-DR.
- *"Delayed rewards timing depends on actions"* — This is a subset of the p(o|x) assumption issue already covered under Major.
- *"Missing related work on missing data in causal inference"* — Per review policy, missing related works should not be mentioned without external verification.
- *"Absence of action-space scaling experiments"* — Per review policy about missing appendix content (the parser strips appendices).
- *"Oracle-based normalization for policy values"* — This is standard practice for synthetic OPL experiments where the true data-generating process is known.
- *"Reproducibility details for KuaiRec action space"* — The paper provides a reasonable level of detail for a conference submission (100 simulations, described setup); remaining details are code-release items.
- *"σ_F=0.4 is arbitrary and s-IPS/s-DR made weak by design"* — This is a stylized synthetic setup where the noise is explicitly intended to simulate inaccuracy; the core comparisons (HyPeR vs r-DR) do not depend on this parameter, and varying λ (correlation) in Figure 3 already tests a spectrum of surrogate quality.

## Novel Insights

The reviews surface one genuinely novel observation beyond the paper's own contributions: the p(o|x) assumption creates an interesting gap between the paper's claimed generality (Table 1 examples) and its formal model. The motivating examples of e-commerce conversions and medical censoring involve action-dependent observation, which the current formulation does not cover. This is not a fatal flaw, but it identifies a concrete direction for extension — modeling p(o|x,a) or p(o|x,a,s) and analyzing how the guarantees degrade — that could substantially broaden the method's real-world applicability. The strategic weight tuning insight (using γ≠β to improve finite-sample performance despite bias) is a clever practical contribution that the reviews correctly identify as well-supported.

## Suggestions

1. **Acknowledge and discuss the p(o|x) assumption.** State clearly that the method assumes \(o \perp a \mid x\), discuss which motivating examples satisfy this and which do not, and sketch how the framework could be extended or how the estimators degrade when the assumption is violated.
2. **State the variance reduction condition precisely** in Theorem 2, e.g., as \(\text{Var}[\hat{q}(x,a,s) - q(x,a,s)] < \text{Var}[\hat{q}(x,a) - q(x,a,s)]\) or an equivalent closed-form condition.
3. **Add an imputation baseline** (train \(\hat{q}(x,a,s)\) on observed data, impute, apply IPS/DR) to clarify the source of HyPeR's advantage.
4. **Specify the validation estimator** used in the γ-tuning procedure (Eq. 14).
5. **Add a limitations section** addressing the observation-independence assumption, surrogate quality, and potential failure modes.

## Score and Decision

**Score:** 7.0

**Decision:** Accept

The paper presents a principled and empirically effective method for an important problem (OPL under partial reward observation). The main weakness is a scope limitation concerning the observation-model assumption that should be clearly acknowledged and discussed in a revision. The theoretical and empirical contributions are otherwise sound and the experiments are thorough. With better scoping and the suggested additions, this would be a strong contribution to the OPL literature.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>
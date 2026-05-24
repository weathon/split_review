Now I have a thorough understanding of the paper and both reviews. Let me produce the consolidated review.

## Summary

This paper revisits the multi-play multi-armed bandit with shareable arm capacities problem (MP-MAB-SAC), proposing a new reward model where arm capacity information resides only in the mean reward (constant variance). The contributions include: (1) tight sample complexity bounds for learning arm capacities under this model (Theorems 1–2), (2) the first instance-independent regret lower bound and a strengthened instance-dependent regret lower bound (Theorems 3–4), and (3) an algorithm PC-CapUL with regret upper bounds (Theorems 5–6) and experimental validation.

## Strengths

- **Tight sample complexity bounds for the new reward model.** Theorem 1 proves a lower bound of Ω(σ²/μ_k² log δ^{-1}) for learning a single arm's capacity, and Theorem 2 shows that ActInfCap matches this bound up to a universal constant. This is a clean, self-contained result that precisely characterizes the fundamental difficulty of capacity estimation when variance carries no capacity information.

- **First instance-independent regret lower bound for this setting.** Theorem 3 provides an Ω(σ√(TK)) minmax regret lower bound, which was absent in prior work. The paper correctly identifies that this bound has no dependence on arm capacities m_k, consistent with the sample complexity results.

- **Novel confidence intervals that are structurally tighter than prior work.** Lemmas 1–2 derive confidence intervals for μ_k and v_k = m_kμ_k where the UE estimation error appears in the numerator rather than the denominator (contrasting with Wang et al. 2022a). This is a concrete technical innovation that reduces the number of UE/IE rounds needed for convergence.

- **Algorithmic design with explicit coordination principles.** PC-CapUL (Algorithm 2) encodes four explicit design principles (preventing excessive UEs, balancing UE/IE, priority by larger empirical reward mean, stopping when converged) that go beyond naive confidence-bound approaches.

## Weaknesses

### Fatal
None.

### Major

- **The paper overclaims relative to prior work by conflating model changes with gap-closing.** The paper introduces a new reward model (Eq. 5, constant variance) that is explicitly different from Wang et al. (2022a)'s model (Eq. 1, variance scaling with allocation). The paper acknowledges this model change (lines 25–31: "reduce the capacity information... to the minimum"). However, it then repeatedly claims to "close the sample complexity gap of Wang et al. (2022a)" and "strengthen the instance-dependent regret lower bound of Wang et al. (2022a)." These claims are misleading because the gaps in Wang et al. (2022a) were between lower and upper bounds *for their model*. Proving tighter bounds for a different (harder) model does not close that specific gap. The paper would be more honest reframed as: "For this harder model where variance carries no capacity information, we establish the first tight bounds." The relationship to prior work should be a nuanced discussion, not a headline.

- **The regret lower and upper bounds do not match on the m_k dimension, despite being presented as matching.** Theorem 4 (instance-dependent lower bound) has no dependence on the arm capacity m_k: lim inf ≥ 2 Σ cσ²/μ_k² log T. Theorem 5 (instance-dependent upper bound) contains terms with Σ m_i² and m_k²: O(Σ (Σ 2304σ²m_i²/μ_i² log T) (μ_k-c)m_k + 1152m_k²/μ_k² σ² log T c N). The paper describes this as matching "up to some acceptable model-dependent factors," but m_k is a parameter that can be large (bounded only by N), and a quadratic dependence is not a constant factor. The lower bound suggests m_k is irrelevant to instance-dependent regret, while the upper bound makes it the dominant term. This gap is unreconciled and undermines the claim of matching bounds. Either the upper bound should be tightened, or the paper should honestly discuss why this gap exists and whether it is fundamental.

### Minor

- **Unfair experimental comparison against the primary baseline.** The baseline "Orch" (Wang et al. 2022a) was designed for the original reward model where variance contains capacity information. Testing it on the new constant-variance model does not fairly establish PC-CapUL's efficiency; it largely shows that an algorithm relying on variance information degrades when that information is removed. The variant PC-CapUL-old (which uses Wang et al.'s estimator within the PC-CapUL framework) is a more informative control, but the paper does not include a fair re-implementation of an algorithm designed for the constant-variance model. The paper acknowledges adapting baselines "from MAB" but gives no details of the adaptation.

- **Limited discussion of the constant-variance assumption's realism.** The paper motivates the model as "reducing the capacity information to the minimum" to derive "more fundamental" insights, and provides an LLM serving application. However, it does not discuss whether the constant-variance assumption (variance independent of the number of queries) holds in any real system — one might expect variance to increase with the number of queries due to independent per-query noise. This limitation should be acknowledged and discussed.

- **Scaling with cost c is mismatched between lower and upper bounds.** The instance-dependent lower bound (Theorem 4) has cσ²/μ_k², while the upper bound (Theorem 5) contains c only in one additive term (cN). It is unclear whether the algorithm's regret scales with 1/c (which would be problematic if c is small) or whether the lower bound's c dependence is loose. The paper does not address this.

### Trivial
None.

## Nice-to-Haves

- The paper could include a re-derived version of Orch or another baseline explicitly designed for the constant-variance model to make the experimental comparison fairer.
- Reporting capacity estimation accuracy and the number of UE/IE steps alongside cumulative regret would strengthen the empirical evaluation.
- A proof sketch or intuition for why the alternating schedule in ActInfCap achieves optimal sample complexity would help readers, though hard technical details are presumably in the (stripped) appendix.

## Removed Points

These points are flagged to be removed; treat them with caution:

1. **"PC-CapUL has a circular dependency"** (Harsh Critic, Missing Parts section). The critic argues that classifying actions as IE/UE using confidence bounds which themselves depend on that classification creates a circular dependency. This is a misunderstanding of adaptive algorithms: at each step, the confidence bounds are fixed (based on data up to the previous time step) and used to classify the *current* action — a standard practice in bandit algorithms. There is no circular dependency.

2. **"Proof sketches are absent"** and **"lower bound proof correctness not verifiable"** (Harsh Critic, multiple sections). The paper's proofs are in the appendix, which was stripped by the PDF parser. This is a known artifact; the original submission contains the proofs.

3. **"The paper never states this directly"** about the model change. The paper explicitly states the model change in lines 25–31: "first we reduce the capacity information in the reward to the minimum such that only the reward mean contains the capacity information. Formally, we propose a new reward function to achieve this goal: R_k(a_k) = min{a_k, m_k}μ_k + ε_k."

4. **"Abstract claims 'three folds' but paper is organized around only two main results."** The paper clearly organizes around three contributions: sample complexity (Section 4), regret lower bounds (Section 5.1), and the algorithm/upper bounds (Section 5.2). ActInfCap is used for sample complexity, and PC-CapUL handles regret — these are distinct.

5. **"Regret of Orch converges to 4×10^5 — implies per-round regret of hundreds, suspiciously large."** The paper explains that Orch's slower convergence is due to its "parsimonious and maladaptive strategy" and looser confidence intervals. Large per-round regret is expected from a poorly adapted algorithm. This is not a flaw in the paper.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the overclaiming relative to prior work and the m_k² gap between regret bounds as the central weaknesses, but these are observations about framing and technical gaps, not new insights about the methodology.

## Suggestions

1. **Reframe the contribution relative to prior work.** State plainly that the paper studies a strictly harder model (constant-variance reward) than prior work, and that the contribution is establishing the *first* tight bounds for this model. Replace "closing the gap of Wang et al. (2022a)" with "establishing tight sample complexity and regret bounds for the harder model, which imply that the prior gap was an artifact of the easier model's variance structure."

2. **Address the m_k gap in regret bounds.** Either tighten the instance-dependent upper bound to remove the quadratic m_k² dependence (perhaps with a refined analysis), prove a matching lower bound that includes m_k, or transparently discuss why the gap exists and whether it is fundamental. The current hedge ("acceptable model-dependent factors") is insufficient when m_k can be large.

3. **Re-do the experimental baselines fairly.** Include at least one baseline algorithm designed for the constant-variance model, or clearly describe how existing baselines were adapted for this setting. The comparison to Orch is not informative about the algorithm's efficiency for the claimed setting; PC-CapUL-old is a better control but alone is insufficient.

## Score and Decision

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>
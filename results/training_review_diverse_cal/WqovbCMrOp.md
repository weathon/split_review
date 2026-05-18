Here is my consolidated final review.

---

## Summary

This paper studies how temporal aggregation of time-series data affects the recoverability of causal relations by non-temporal (i.i.d.) causal discovery methods. It proposes two formal notions—*functional consistency* (for FCM-based methods like LiNGAM) and *conditional independence consistency* (for constraint-based methods like PC)—and provides theoretical conditions under which each holds or fails in the trivariate chain, fork, and collider settings. The main actionable finding is that partial linearity in the causal mechanism suffices to preserve conditional independence sets, making constraint-based methods more robust than FCM-based methods under aggregation. The results are supported by simulation experiments.

---

## Strengths

1. **First formal analysis of recoverability for general nonlinear aggregated data.** The paper proposes explicit definitions (functional consistency, conditional independence consistency) and characterizes conditions for each, going beyond prior work that considered only linear cases (Gong et al., 2017) or restrictive fixed-noise assumptions (Fisher, 1970). The framing itself—distinguishing between what FCM-based vs. constraint-based methods require from aggregated data—is a useful conceptual contribution.

2. **Identification that the collider structure naturally preserves conditional independence under aggregation.** Remark 1 shows that for a collider, the conditional independence properties ($\overline{X}\perp\!\!\!\perp\overline{Z}$ and $\overline{X}\not\perp\!\!\!\perp\overline{Z}\mid\overline{Y}$) are preserved in general nonlinear settings, unlike chain and fork. This is a new insight with practical value for practitioners choosing which structures to trust under aggregation.

3. **Partial linearity sufficient condition validated experimentally.** Corollaries 4–5 state that linearity in the edge entering/exiting the middle node ensures $\overline{X}\perp\!\!\!\perp\overline{Z}\mid\overline{Y}$, and the experiments (Table 1) show that partial linearity indeed recovers correct rejection rates for the key conditional independence while fully nonlinear settings fail dramatically (58% vs. 5% for column VI).

4. **Concrete experimental demonstration of identifiability collapse.** The Direct LiNGAM experiment (Figure 2) cleanly shows correct rate dropping from ~100% to random guess as $k$ increases from 1 to 30 in the linear non-Gaussian case, providing a compelling empirical backing for the paper's main concern.

5. **Clear explanation of why functional consistency fails.** Theorem 1 provides the specific form that $\hat{f}$ must take (conditional expectation), and the variance argument following Theorem 2 gives a concrete mechanism: the conditional variance $\text{var}[\sum f(X_i)\mid\overline{X}=T]$ must be constant in $T$, which is a stringent requirement unlikely to hold in nonlinear settings.

---

## Weaknesses

### Major

1. **The partial linearity sufficient condition (Corollary 3) is stated without a proof or proof sketch.** The paper's contributions section says "we prove that partial linearity is sufficient," yet the main text provides only an intuitive explanation ("roughly speaking, if the causal relationship is linear, then the information needed to infer X/Z from Y_{1:k} is completely included in Ȳ"). No formal argument, lemma, or derivation is given for why $f_Z(Y_t, Z_{t-1}, N_{Z,t}) = \alpha Y_t + N_t$ implies $\overline{Z} \perp\!\!\!\perp Y_{1:k} \mid \overline{Y}$. This is the paper's most actionable positive result, and leaving it unproven is a significant gap for a paper that presents itself as theoretical analysis. The experiments validate the claim empirically, but the theoretical claim remains unsupported.

2. **Several theorems restate definitions or known results rather than providing novel mathematical insight.**
   - Theorem 2 (the necessary and sufficient condition for the additive noise model) is essentially the definition of the additive noise model written as an independence condition.
   - Theorem 4 (General Case for Functional Consistency) states that for continuous support, functional representations exist in both directions—this is a known identifiability result that holds for the original (non-aggregated) model as well and does not add aggregation-specific insight.
   
   The paper's contributions are better characterized by the problem framing, the collider insight, and the partial linearity finding than by the formal theorems as stated. The gap between the claimed theoretical depth and the actual content of the theorems weakens the paper.

### Minor

3. **Theorem 1 (construction of $\hat{f}$) is a direct application of the Rao-Blackwell property.** The paper itself acknowledges this resemblance (line 149). While it is useful to write the explicit form, calling it a theorem overstates its novelty. It is more accurately a lemma or observation.

4. **The connection between the aligned model and the original VAR model at finite $k$ lacks quantitative guarantees.** The paper correctly states that its theoretical results apply to the aligned (instantaneous) model for any finite $k$, and that applying them to the original time-delay VAR requires large $k$ with the discrepancy $\frac{Y_{k+1}-Y_1}{g(k)} \to 0$. However, no bound is provided for how large $k$ needs to be for the approximation to be safe, nor is the rate of convergence characterized. This limits the practical applicability of the finite-$k$ results for real-world settings where the aggregation factor is known and moderate.

5. **The experiment table caption does not specify which structure (chain/fork/collider) is reported.** The text clarifies it is for fork structure, but the table itself and its caption lack this information, creating minor ambiguity for readers scanning the paper.

### Trivial

6. The text references "Table \ref{experiment result2}" but the table label is "experiment result" (without the 2). This appears to be a reference inconsistency.

---

## Nice-to-Haves

- **Error bounds for the alignment approximation:** Quantifying the discrepancy $\|\overline{Y}' - \overline{Y}\|$ as $O(1/g(k))$ would clarify when the aligned-model results are safe to apply to the original time-delay model.
- **Discussion of whether the partial linearity sufficient condition generalizes to chains/forks of arbitrary length** (more than three variables). The trivariate analysis is a good foundation; a brief comment on scalability would strengthen the practical guidance.
- **Make explicit that the LiNGAM experiment's failure mechanism is the Central Limit Theorem making summed non-Gaussian noises approximately Gaussian.** The paper mentions CLT briefly (line 135), but connecting it more directly to the experiment would tighten the narrative.

---

## Removed Points

These points from the original inputs were evaluated and removed with justification:

- *"The claim that results apply to 'any finite k' is only valid for the aligned model itself, not for the original VAR."* — The paper explicitly states this: "all the theoretical results in this paper consider the aggregation of the instantaneous underlying model" and "Only when we want to apply the results to the aggregation of the time-delay model do we need k to be large." The critic's concern is already addressed by the paper's own disclaimers. (Strawman weakness / misreading.)

- *"The LiNGAM experiment is unsurprising because the central limit theorem makes this obvious."* — Whether a result is "unsurprising" is a matter of taste, not a weakness. The experiment serves as a concrete validation of the theoretical concern, which is a legitimate role for an experiment. (Not a substantive weakness.)

- *"The non-stationary functional consistency result (Theorem 4) is essentially a restatement of the Darmois–Skitovič result."* — Darmois–Skitovič specifically concerns independence of linear forms implying Gaussianity; Theorem 4 concerns existence of bidirectional functional representations for continuous-support variables. The critic's specific reference is imprecise. However, the underlying point (that the result is general and not aggregation-specific) is valid and is retained as Minor weakness #2.

---

## Novel Insights

The synthesis of the reviews yields one insight not fully articulated in the paper: the asymmetry between the collider and chain/fork cases reveals a deeper structural principle. In the collider, each $Y_t$ is a collider that absorbs dependence between $X_t$ and $Z_t$, and $\overline{Y}$ is a descendant of multiple such colliders. Aggregation helps rather than hurts because conditioning on $\overline{Y}$ opens paths that are already open at each time step. In chains and forks, by contrast, $\overline{Y}$ is not a mediator but a common effect of all $Y_t$, so conditioning on it creates collider bias (it renders $Y_t$ dependent on each other), breaking the very independence one hopes to preserve. This asymmetry is fundamental and suggests that datasets dominated by collider-like substructures are systematically safer for constraint-based discovery under aggregation—a claim that could be tested empirically beyond the trivariate setting.

---

## Suggestions

1. **Provide a proof sketch for Corollary 3 (partial linearity).** Even a short derivation showing that if $Z_t = \alpha Y_t + N_{Z,t}$, then $\sum Z_t = \alpha \overline{Y} + \sum N_{Z,t}$, and since $\sum N_{Z,t}$ is independent of $Y_{1:k}$ (and thus of $Y_{1:k}$ given $\overline{Y}$), the result follows, would significantly strengthen the paper. Currently this is presented as a corollary without any supporting argument.

2. **Retitle the theorems that are straightforward consequences of definitions** (e.g., Theorem 2) as "Propositions" or "Observations" to better calibrate reader expectations about the paper's theoretical depth.

3. **Add a brief note on the rate of convergence** of the alignment approximation (e.g., $\overline{Y}' - \overline{Y} = O(1/g(k))$) to give practitioners a heuristic for when $k$ is "large enough."

4. **Explicitly state in the Table 1 caption** which causal structure (chain, fork, or collider) the results correspond to, rather than relying on the text alone.

---

## Score and Decision

**Originality:** The problem framing (distinguishing functional vs. conditional independence consistency for aggregated data) and the collider preservation result are novel. The theorems themselves have limited novelty.

**Importance:** The question is practically important—many real-world datasets are aggregates of higher-frequency processes—and the paper provides useful guidance (e.g., constraint-based methods may be more reliable than FCM-based under aggregation; avoid chains/forks without partial linearity).

**Claims support:** The central claims are partially supported. The experimental results validate the main conclusions, but the key theoretical claim (partial linearity sufficient condition) lacks the proof that the paper asserts it provides. The theorems that exist are generally correct but shallow.

**Soundness:** The problem setup and alignment argument are sound. The experiments are clean and well-designed. The theoretical gaps are in presentation/proof completeness, not in correctness.

**Clarity:** Generally well-written and clearly structured. The distinction between aligned model and original VAR is explained carefully. Minor labeling issues in the table.

**Value to community:** Useful as a cautionary analysis for practitioners applying causal discovery to aggregated data. The partial linearity finding provides concrete guidance.

**Overall:** The paper identifies a real and underappreciated problem, provides a useful conceptual framework, and delivers one practically actionable theoretical finding (partial linearity suffices for CI consistency). However, the finding is presented as a corollary without proof, and several of the formal theorems add less depth than claimed. The paper would benefit from either (a) adding the missing proof sketch for Corollary 3, or (b) reframing itself as primarily an empirical/position paper rather than a theoretical one.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>
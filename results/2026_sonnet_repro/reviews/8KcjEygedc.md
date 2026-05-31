Now let me do calibration searches to properly score this paper.The most relevant anchor is I9Dsq0cVo9 (avg 5.50, RMT + synthetic data + high-dimensional classification). Let me read it.Round 1 bracket: 5.0–7.0. Now let me narrow.Now I have enough to write the final review. Let me compile everything.

---

## Summary
This paper introduces a theoretical framework for data curation in high-dimensional binary classification using random matrix theory (RMT). The authors derive exact asymptotic test error formulas under both label-agnostic and label-aware pruning oracles, characterizing precisely when "keep hard" vs "keep easy" strategies are optimal. The core finding is that the interplay among generator quality (ρ), oracle quality (ρ*), and data scale determines the optimal pruning strategy, with "less is more" holding only in the large-data, strong-generator regime. The theory is validated on synthetic experiments and qualitatively on ImageNet, with an interpretive connection to LIMO/s1 LLM results.

---

## Strengths

- **Exact asymptotic test error characterization (Theorem 1, Eq. 9–11):** The closed-form formula via RMT deterministic equivalents provides a rigorous analytical machine to evaluate any pruning strategy q in terms of four interpretable scalars (p, γ, β, β̃). This is a genuine technical contribution extending prior work (Feng et al. 2025, Firdoussi et al. 2024) to the difficulty-based pruning setting.

- **Sharp condition for "less is more" (Theorem 2):** The paper gives a precise, verifiable bifurcation: for strong generator (ρ → 1) with good oracle (ρ* → 1), "keep hard" uniquely minimizes test error; for weak generator (ρ < 1), "keep easy" is uniquely optimal. This cleanly unifies what appeared to be contradictory empirical findings into a single principled framework.

- **Controlled simulation validates phase transition cleanly (Figure 1):** The 2×2 grid spanning small/large n and strong/weak generator demonstrates that only the large-data + strong-generator quadrant yields "less is more," with solid theoretical curves matching empirical results, including non-trivial minima at p ≪ 1.

- **Label-aware curation extension (Theorem 3):** Generalizing to oracles that filter both difficulty and label correctness (Eq. 6) is relevant to LIMO/s1 pipelines, and the paper shows the same test error formula applies with modified constants, unifying this case with the label-agnostic theory.

- **ImageNet crossover validates qualitative prediction (Figure 2):** A clear crossover from "keep easy" optimal (small n = 160K) to "keep hard" optimal (large n = 1.2M) is observed, consistent with the theoretical boundary prediction.

---

## Weaknesses

### Fatal
None.

### Major

- **LLM section (4.2) is post-hoc and unfalsifiable.** The paper claims in the abstract to provide "a principled explanation" and in the contributions bullet to give "a rigorous justification for why methods like LIMO and s1 succeed." However, ρ is never measured or estimated for any LLM in Section 4.2. The assignment of "strong generator" (for average AIME) vs. "weak generator" (for hardest AIME questions) is inferred retroactively from the observed outcome being explained, i.e., circular reasoning. Any binary experimental result (Table 1, Table 2) can be accommodated by post-hoc declaration of generator strength. No value of ρ, ρ*, or ρ_g is estimated from the LLM setting; no quantitative test is performed. This is an evidential overreach that misrepresents Section 4.2's actual content. The section should be framed as "a theoretical lens consistent with" or "a natural interpretation of" these findings—not a rigorous justification.

- **Apparent tension between Theorem 2B and Figure 3 (model collapse) is unresolved in the main text.** Theorem 2B states: weak generator (ρ < 1) → "keep easy" is uniquely optimal (Section 3.1, p. 4). Furthermore, the paper explicitly states at line 157 "This latter case [weak generator → keep easy] is particularly relevant for mitigating model collapse." Yet Figure 3 demonstrates model collapse prevention using "keep hard valid examples" — the opposite difficulty selection. The resolution likely lies in Theorem 3 (label-aware curation with Eq. 6), where the label-validity filter changes the analysis and "keep hard valid" may be optimal. But this reconciliation is never made explicit: the reader is left with contradictory guidance from Theorem 2B and Figure 3. Since model collapse is listed as one of the four main contributions, this gap needs to be addressed with at least a corollary of Theorem 3 explaining when "keep hard valid" is optimal under weak generators.

### Minor

- **No quantitative theoretical curves for ImageNet (Section 4.3).** The abstract states "we validate these theoretical claims with empirical results on ImageNet," but Figure 2 shows only direction-of-effect comparisons. The theory produces exact formulas; for the ImageNet setup (pre-trained ViT as generator/pruner), estimating ρ (via pseudo-label error rate) and plotting predicted test error curves would transform "qualitative agreement" into genuine quantitative validation. The current phrasing in the abstract overstates what is shown.

- **Finite-sample regime underexplored in the main text.** Theorem 2 is stated for the data-rich, unregularized limit (φ → 0, λ → 0, Eq. 12), yet Figure 1 shows "more is more" in three of four quadrants at finite n. The main text does not discuss when the asymptotic prediction from Theorem 2 is a reliable guide to finite-sample behavior, which is the practically relevant regime for many applications.

### Trivial

- **Terminology "exact scaling laws" does not match LLM scaling law usage.** The paper derives exact asymptotic test error in the proportionate scaling limit d/n → φ (RMT usage), while repeatedly invoking "scaling laws" in the sense of Kaplan et al. 2020 and Hoffmann et al. 2022 (power-law behavior in n with d fixed). This is standard in the RMT-in-ML community but may mislead readers from the LLM community expecting power-law curves.

---

## Nice-to-Haves
- Estimating ρ quantitatively from the ImageNet experiments (e.g., using pseudo-label accuracy as a proxy) and overlaying theoretical curves from Theorem 1 would significantly strengthen the empirical validation and demonstrate the formula's predictive power beyond the synthetic setting.
- An explicit corollary from Theorem 3 computing the optimal strategy in the model-collapse iterative setting (where both label-verification and difficulty pruning interact) would clarify when "keep hard valid" beats "keep easy valid" and resolve the tension with Theorem 2B.
- Section 4.2 would be substantially improved by any independent estimate of generator quality for easy vs. hard AIME problems (e.g., base model pass rate on held-out easy vs. hard problems as a proxy for ρ), transforming the post-hoc narrative into a testable prediction.

---

## Removed Points
*These points are flagged to be removed; treat them with caution.*

- **"Terminological mismatch is not catastrophic" (harsh critic)** — The terminology point is valid but only trivial; the harsh critic's label of "contributes to overstatement" is somewhat overstated itself. Retained as trivial.
- **Isotropic main results limiting** — The harsh critic flags that the main text restricts to C_g = Σ = I_d while Section 2.1 introduces covariate shift C_g ≠ Σ. The paper explicitly states at line 58–59 "More general results are deferred to the appendix." Removed as a weakness since the paper acknowledges this and provides the general case in the appendix.
- **Strength finder's "principled explanation of LLM results"** — Removed as a standalone strength because it conflicts with the verified Major weakness (post-hoc, circular reasoning). The framework is consistent with LLM results, not a rigorous explanation.
- **Strength finder's "curation prevents model collapse (Figure 3)"** as a standalone strength — Retained only in context: Figure 3 empirically demonstrates stabilization, but the theoretical justification for "keep hard valid" in this regime is incomplete in the main text.

---

## Novel Insights
The most intellectually precise contribution of this paper is the identification of generator quality ρ as the pivotal bifurcation parameter: not oracle quality (ρ*), not data scale (n) alone, but their *interaction* with ρ. The four-quadrant structure of Figure 1 shows that "more is more" is the default even for a strong generator if n is small, while the "less is more" regime is a narrow corridor requiring both large n and ρ → 1. This has a concrete practical implication: aggressive difficulty-based pruning (à la LIMO/s1) should only be applied when the base model already performs well—exactly the regime these methods operate in—whereas applying the same strategy with a weak base model will reliably hurt. The RMT framework makes this precise and quantitative in a way that prior empirical work cannot.

---

## Suggestions
1. **Reframe Section 4.2** — Replace "rigorous justification" and "principled explanation" with "theoretical lens consistent with" or "interpretive framework for." Add a sentence acknowledging ρ is not measured.
2. **Resolve Theorem 2B ↔ Figure 3 tension** — Add a corollary to Theorem 3 or a brief paragraph after Figure 3 explaining why label-aware "keep hard valid" is optimal here even under a weak generator; this is the right theorem to use for the model collapse setting.
3. **Add quantitative ImageNet theory comparison** — Even an approximate estimate of ρ from pseudo-label error rate would allow plotting predicted vs. observed crossover point.
4. **Clarify finite-sample guidance** — Add a brief discussion of when the φ → 0 asymptotic (Theorem 2) reliably guides finite-sample decisions.

---

## Score and Decision

**Calibration anchors:**

| Path | Avg Score | Round | Comparison |
|---|---|---|---|
| I9Dsq0cVo9 (RMT + synthetic data + binary classifier) | 5.50 | R1/R2 | Most similar work; paper under review is strictly more general, covering difficulty-based pruning on top of label verification, but has weaker empirical validation |
| MQXrTMonT1 (Feng et al. - Beyond Model Collapse) | 6.50 | R2 | Direct predecessor cited as Remark 1 special case; paper under review generalizes it with difficulty-based pruning and a broader framework, but practical experiments are less convincing |
| VB2WkqvFwF (Universal traits / RMT datasets) | 4.33 | R1 | Weaker theoretical contribution, no clean theorem; clearly below the paper |
| zxqdVo9FjY (Least squares regression / spiked covariances) | 4.80 | R1 | Narrower scope, no application to data curation; the paper under review is clearly stronger |
| et5l9qPUhm (Strong Model Collapse) | 8.00 | R1 | Deeper on a single question, with convincing GPT-2 validation; stronger empirical support |
| Tzh6xAJSll (Scaling Laws for Associative Memories) | 7.60 | R1 | More technically complete validation; the paper under review falls short in empirical rigor |
| Xr5iINA3zU (Collapse or Thrive?) | 5.75 | R2 | Broader scope but weaker theory; roughly comparable |
| WttfQGwpES (Theoretical STL generalization) | 6.67 | R2 | Theoretical analysis of self-consuming loops; comparable theoretical depth |

**Round 1 bracket:** 5.0–7.0

**Round 2 narrowing:** The paper under review generalizes I9Dsq0cVo9 (5.50) and MQXrTMonT1 (6.50) — both of which it cites and identifies as special cases — by adding difficulty-based pruning and deriving optimality conditions (Theorem 2). This generalization is genuine and theoretically clean. However, compared to MQXrTMonT1 (6.50), the empirical validation is weaker (qualitative ImageNet only, no practical NLP experiments), and the LLM connection is post-hoc rather than predictive. Compared to WttfQGwpES (6.67), the theoretical contribution is sharper (exact formulas vs. generalization bounds) but empirical validation is narrower. The two major weaknesses (post-hoc LLM claims, Theorem 2B ↔ Figure 3 gap) are fixable in revision and do not invalidate the core theoretical contribution.

**Final position:** Slightly above I9Dsq0cVo9 (5.50) and slightly below MQXrTMonT1 (6.50), anchoring closer to the upper end of this range given the generalization contribution, but pulled down by the overstatement in the abstract and the unresolved Theorem 2B tension. Score: **6.0**.

**Axis summary:**
- *Originality:* Good — unifies difficulty-based and label-aware pruning under a single RMT framework, with clean optimality conditions
- *Importance of research question:* High — data curation efficiency is central to modern LLM training
- *Whether claims are well-supported:* Mixed — core theory is well-supported; LLM claims are overstated
- *Soundness of experiments:* Adequate — synthetic experiments convincing; ImageNet qualitative only
- *Clarity of writing:* Good — clear exposition of a technical setup, with appropriate intuition
- *Value to the research community:* Solid — provides a rigorous analytical lens for empirically-observed phenomena

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>
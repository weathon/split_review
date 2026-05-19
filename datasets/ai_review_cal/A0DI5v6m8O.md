- Decision: Reject
- Avg Score: 5.50
- Scores: 6, 8, 3, 5
Now I have a thorough understanding of the paper. Let me write the consolidated review.

---

## Summary

This paper studies offline black-box optimization and makes two contributions: (1) a theoretical bound (Theorem 1) connecting the gradient discrepancy between a surrogate and the oracle to the optimization performance gap, and (2) MATCH-OPT, an algorithm that learns surrogate models by matching gradients using the fundamental theorem of line integrals (avoiding direct oracle gradient queries). Experiments on six real-world design-bench tasks show MATCH-OPT achieves the best mean normalized rank (MNR) compared to existing baselines.

---

## Strengths

- **Theorem 1 provides a novel, model-agnostic bound connecting gradient discrepancy to optimization performance.** The result (Eq. 7) shows that the worst-case performance gap is bounded by \( m\lambda\ell(1+\lambda\mu)^{m-1} \cdot \max_{\mathbf{x}} \|\nabla g(\mathbf{x}) - \nabla g_{\phi}(\mathbf{x})\| \). This is the first such bound in the offline BBO literature and directly motivates why gradient matching is the right objective. *(Verified: Section 3, Eq. 7–8.)*

- **The line-integral-based gradient matching loss (Eq. 10–12) is a creative and principled solution to a hard problem.** The key challenge is that oracle gradients are unobservable even at training points. By leveraging the fundamental theorem of line integrals, the loss transforms pairwise value differences into a signal that constrains the surrogate's gradients — without requiring any oracle queries beyond the static dataset. *(Verified: Section 4, Eq. 10–11 and surrounding discussion.)*

- **MATCH-OPT achieves the best overall mean normalized rank (MNR) across six diverse real-world benchmarks.** The paper states MATCH-OPT's MNR is "markedly lower than that of the second lowest MNR of COMS" at both the 100th and 50th percentiles, and Figure 3a shows it achieves the lowest MNR at almost every percentile. *(Verified: Section 5.3, Tables 1–2 descriptions, Fig. 3.)*

- **The synthetic OOD experiment (Figure 1) directly supports the gradient-matching thesis.** When test inputs deviate from the training distribution (smaller α values), MATCH-OPT shows significantly smaller gradient norm error than standard regression, while matching it at α=1.0. This controlled experiment isolates the effect of gradient matching on gradient estimation quality, connecting the algorithmic idea to a measurable improvement. *(Verified: Section 1, Fig. 1 description, lines 25–27.)*

- **The adoption of mean normalized rank (MNR) as the primary metric (Eq. 14) is methodologically sound.** MNR avoids the bias toward easy tasks that afflicts mean normalized performance, making cross-task reliability comparisons fairer. *(Verified: Section 5.2, Eq. 14 and surrounding discussion.)*

---

## Weaknesses

### Fatal

None.

### Major

- **Disconnect between the theoretical bound and the practical algorithm.** Theorem 1 bounds the performance gap by \(\max_{\mathbf{x}} \|\nabla g(\mathbf{x}) - \nabla g_{\phi}(\mathbf{x})\|\) — the maximum gradient discrepancy over the *entire input space*. The paper correctly notes this minimax program (Eq. 9) is intractable without oracle gradient access, then proposes a line-integral matching loss (Eq. 11–12) minimized on *synthetic monotonic trajectories* constructed from offline data. However, the paper never establishes — theoretically or empirically — that minimizing this specific loss (on these specific trajectories) actually reduces the bound from Theorem 1. The theory motivates *why* gradient matching matters, but it does not guide *which* gradients to match or *how* the chosen approximation relates to the bound. The paper frames the algorithm as "principled" and "inspired by" the theory, which is accurate, but the gap between the worst-case bound over the whole space and the tractable trajectory-based loss is significant and unaddressed. *(Verified: Section 3, Eq. 7–9; Section 4, Eq. 10–13. The paper does not provide a formal argument connecting Eq. 11–12 back to Eq. 7 or 9.)*

- **No ablation study isolating the effect of the gradient matching loss.** The algorithm has three components: (1) synthetic monotonic trajectories, (2) gradient matching loss, (3) regression regularizer. Without ablations — e.g., comparing MATCH-OPT to a standard regression surrogate trained on the *same synthetic trajectories* but without the gradient matching term — it is impossible to attribute the performance improvement to gradient matching per se. The core thesis of the paper is that gradient matching yields better surrogates, yet no experiment tests this claim directly. *(Verified: The experiments section (Section 5) compares MATCH-OPT to full prior methods, not to ablated versions of itself. No ablation is mentioned anywhere in the paper.)*

### Minor

- **Hyperparameter choices (κ=5, α=1) are stated without sensitivity analysis.** The discretization granularity κ is set to 5 based on "empirical inspections," and the regularization weight α is set to 1 with the justification of "same unit scale." However, the regression and gradient-matching losses have different functional forms (MSE vs. a squared line-integral residual), so the claim of unit-scale comparability is not self-evident. No analysis shows whether performance is robust to these values. *(Verified: Section 4, Eq. 12–13 and lines 168–174.)*

- **No statistical significance testing on MNR differences.** The paper reports that MATCH-OPT's MNR is "markedly lower" than the runner-up, but with only 6 tasks and 4 runs per task, no confidence intervals or significance tests are provided for the MNR comparison. The differences could arise from noise, especially on a rank-based metric with small N. *(Verified: Section 5.3 reports means and stds per task but no statistical comparison on MNR itself.)*

- **The synthetic trajectory generation is underspecified.** The description ("first bin the offline inputs based on their percentiles…sample one input from each bin") leaves open questions: How many bins? What if bins are empty or have very few points? How many synthetic paths p are generated? How are ties handled? These details are important for reproducibility and for understanding when the method might fail. *(Verified: Section 4, line 162. The description is qualitative only.)*

- **Performance on individual tasks is notably uneven.** The paper acknowledges MATCH-OPT is among top-3 on four of six tasks, which implies it is not top-3 on two tasks (TF10 and HOPPER). Figure 3b shows MATCH-OPT drops below other methods above the 80th percentile. While no method dominates all tasks, the "most reliable" claim is weakened by the algorithm performing worst on some tasks in the region that matters most for design optimization (high percentiles). *(Verified: Section 5.3, lines 221 and 227; Fig. 3b description.)*

### Trivial

None.

---

## Nice-to-Haves

- **Comparison to simpler gradient regularization baselines** (e.g., regression with a Jacobian norm penalty or gradient-difference penalty) would test whether the line-integral formulation is actually better than cheaper gradient smoothness regularizers, helping isolate the value of the specific proposed mechanism.
- **Confidence intervals on MNR** (e.g., via bootstrap across the 6 tasks) would strengthen the reliability claims.
- **Wall-clock runtime comparison** would contextualize the complexity analysis.
- **Analysis of failure cases** (why TF10 and HOPPER are hard for MATCH-OPT) would clarify the method's limitations and guide future improvements.

---

## Removed Points

*These points are flagged for removal; treat them with caution.*

- **"The proof is relegated to an appendix (not available)"** — Removed per Hard Rules: the parser strips appendix content from all papers; the proof exists in the original submission.
- **"Missing related works" about gradient-based regularization** — Removed per Hard Rules: the reviewer may not have complete knowledge of related works; the paper cites relevant baseline methods (COMS, ROMA, BONET, etc.).
- **"The bound is overly conservative and not actionable" (without evidence)** — The paper acknowledges the minimax program is intractable (lines 116–122) and proposes a tractable approximation; this is a limitation the authors are aware of, not a hidden flaw.
- **Strength Finder's specific numerical MNR claims (0.41, 0.54, etc.)** — These appear to be hallucinated; the tables are embedded images whose values cannot be verified from text. The review relies on the paper's textual description ("markedly lower") instead.
- **Generic formatting/style nitpicks** — Removed per Hard Rules.

---

## Novel Insights

The most striking signal from the cross-examination of the reviewer inputs is that the harsh critic and the strength finder essentially agree on the core contributions (novel theory, clever algorithm, best average MNR) but disagree sharply on interpretation. The harsh critic sees the theory-algorithm gap as structural; the strength finder sees it as a natural theory-to-practice pipeline. The truth is somewhere in between: the paper *does* connect theory to algorithm (the bound motivates gradient matching; the line-integral loss is a reasonable way to do gradient matching without oracle access), but it does *not* close the loop formally. This is a pattern common in ML papers where theory provides inspiration rather than tight algorithmic guidance — and the paper would benefit from being explicit about that relationship rather than claiming "theoretically-sound answers." The more consequential gap is the missing ablation, which is an experimental design issue, not a theoretical one. The empirical evidence *as presented* supports MATCH-OPT as a complete method, but not the specific claim that gradient matching (rather than the synthetic trajectory construction or the combination) drives the improvement.

---

## Suggestions

1. **Add an ablation study:** Compare (a) standard regression on raw data, (b) standard regression on synthetic trajectories (without gradient loss), (c) regression with a simple gradient-norm penalty, and (d) full MATCH-OPT. This would isolate the effect of the gradient matching loss and directly support the paper's central thesis.
2. **Formalize or reframe the theory-algorithm connection.** Either prove that minimizing the line-integral loss (Eq. 11) bounds the gradient discrepancy on a relevant subset of the input space (e.g., the convex hull of the data), or explicitly reframe the algorithm as a heuristic inspired by — but not derived from — the bound.
3. **Add hyperparameter sensitivity analysis** for κ and α, even briefly.
4. **Discuss the two failure cases** (TF10, HOPPER) to clarify when the method works and when it might not.
5. **Provide reproducibility details:** number of bins for trajectory generation, number of synthetic paths p, tie-handling strategy.

---

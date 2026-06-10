**Note:** I have read the paper in full. Below is the consolidated review.

---

## Summary

The paper initiates the study of Fair Submodular Cover (FSC), defining a new problem where the goal is to minimize solution cardinality subject to both a submodular function threshold and per-group proportional fairness constraints. It proposes a conversion framework that turns bicriteria algorithms for Fair Submodular Maximization (FSM) into bicriteria algorithms for FSC, and develops three new FSM algorithms (two discrete, one continuous) that pair with this framework. The continuous algorithm achieves a (1−O(ε), ln(1/ε)+1)-bicriteria ratio, matching the best-known guarantee for submodular cover without fairness constraints.

## Strengths

- **First formalization of Fair Submodular Cover (FSC).** The paper correctly identifies that fairness for the cover setting requires proportional constraints p_c|S| ≤ |S∩U_c| ≤ q_c|S| (since solution size is not predetermined), and that no prior work studies fairness for submodular cover. This fills a genuine gap (Lines 27–37).

- **Conversion framework with non-trivial adaptation.** Theorem 1 (Lines 158–161) shows that any (γ,β)-bicriteria FSM algorithm can be converted into a ((1+α)β,γ)-bicriteria FSC algorithm. The key technical challenge — that prior conversion approaches (Iyer & Bilmes, 2013) did not handle fairness constraints — is overcome by a new rounding procedure (Lines 138–150) that enforces both lower and upper per-group bounds after the FSM subroutine runs.

- **Continuous algorithm matches the best-known unconstrained guarantee.** Theorem 3 (Lines 267–271) gives a (1−7ε, ln(1/ε)+1)-bicriteria ratio, matching the best-known guarantee for submodular cover without fairness constraints (chen2024bicriteria, iyer2013submodular). This is the paper's strongest theoretical result — it shows fairness can be incorporated without asymptotic degradation in approximation quality.

- **Structural lemma for the β-extension of fairness matroids.** Lemma 2 (Lines 194–201) establishes a non-trivial combinatorial property: for any base T in the original fairness matroid and any base S in its β-extension, there exists a sequence E containing β copies of T such that S_i ∪ {e_{i+1}} stays feasible for M_β. This insight enables the bicriteria analysis for all three FSM algorithms.

## Weaknesses

### Major

- **Experiments do not validate the paper's own problem definition.** FSC is defined by proportional constraints p_c|S| ≤ |S∩U_c| ≤ q_c|S| (Equation (1)–(3)). However, the experiments report "fairness difference" = (max_c|S∩U_c| − min_c|S∩U_c|)/|S| (Figure 1 caption, Line 322) — a balance measure that is **not** equivalent to whether the defined p_c/q_c bounds are satisfied. The paper never states what p_c or q_c values were used in the experiment, nor does it check whether the output satisfies the proportional constraints. The radar plots show distributions are more balanced, but balanced ≠ proportional-constraint-satisfying. The core claim that the algorithms solve FSC is not directly validated.

- **Over-claim about experimental scope.** Contribution (iii) (Line 48) claims experiments "on instances of fair maximum coverage in a graph and fair image summarization." The experimental section (Section 5, Lines 276–324) only describes maximum coverage on the Twitch dataset. The figure label `fig:image-sum-central-exp` (Line 323) hints at image summarization content that is never described in the text. This claim is unsupported.

### Minor

- **Footnote error.** Line 38 states: "Similarly, if ∑ q_c ≥ 1, we can also prove that no feasible sets satisfy the constraint." This is incorrect. Summing the upper-bound constraints |S∩U_c| ≤ q_c|S| across groups gives |S| ≤ (∑ q_c)|S|, which implies 1 ≤ ∑ q_c is necessary for feasibility. The footnote should say "if ∑ q_c < 1." As written, it contradicts the paper's own assumption that ∑ q_c ≥ 1 is needed for feasibility.

- **Technical condition involving |OPT| is unverifiable.** Theorem 1 (Line 160) and Theorem 2 (Line 169) assume ∑_c min{q_c, |U_c|/(β(1+α)|OPT|)} ≥ 1, which involves the unknown |OPT| — the very quantity the algorithm guesses. The paper acknowledges this (Line 156: "essentially requiring that there be enough elements within each set U_c") but does not discuss what happens when the condition is violated, how to detect violations, or whether it holds for typical instances. For a paper initiating a new problem, this gap in the theoretical analysis limits practical applicability.

### Trivial

- None.

## Nice-to-Haves

- Adding natural baselines beyond the standard greedy algorithm (e.g., greedy + post-hoc fairness enforcement, or greedy with fairness-checking at each step) would allow a more informative assessment of the price of fairness.
- Reporting variance or confidence intervals for experimental results.
- Evaluating the continuous algorithm (even at small scale) since it is the paper's strongest theoretical contribution and is omitted from the experiments entirely.
- A dedicated limitations section discussing when the algorithms might fail or where the technical conditions (e.g., the |OPT|-dependent condition) might be violated.

## Removed Points

- *"The conversion theorem depends on unknown |OPT|, which is a methodological gap"* (harsh critic, Critical Issues #2) — The guessing framework is standard for submodular cover (Iyer & Bilmes 2013). The condition is a proof requirement about the existence of enough elements in each group. This is a real limitation but not a methodological gap; demoted to Minor.
- *"Weak baseline"* and *"No variance/confidence intervals"* — Valid suggestions for improvement but standard for a theory-first paper with illustrative experiments; moved to Nice-to-Haves.
- *"Bicriteria definitions are confusingly interleaved"* — Presentation preference, not a substantive weakness. Removed.
- *"Missing image summarization experiments"* — Retained as a Major weakness (over-claim); not removed.
- *Generic strengths from Strength Finder* (e.g., "this paper addressed an important problem") — Removed; only concrete, evidence-grounded strengths retained.
- *Strength about "empirical demonstration of fairness improvement"* — Partially retained but caveated by the metric mismatch weakness.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Re-run the experiments with explicit p_c, q_c values and report whether the output satisfies the proportional fairness constraints defined in the paper. This directly connects the experiments to the problem definition.
2. Either include the claimed image summarization experiments or retract the claim from the contributions list.
3. Fix the footnote error on line 38 (change "if ∑ q_c ≥ 1" to "if ∑ q_c < 1").
4. Acknowledge the |OPT|-dependent condition in Theorem 1/2 as a limitation and discuss conditions under which it can be expected to hold or circumvented.
5. Report at least basic statistics (e.g., mean/std across multiple runs) for experimental results.

---

## Score and Decision

The paper makes a genuine theoretical contribution: a new problem definition (FSC), a clean conversion framework, and a continuous algorithm matching the best-known unconstrained guarantee. These are non-trivial for a paper initiating a new problem. However, the experimental evaluation has two significant issues: (a) it uses a different fairness metric than the one defined in the paper, so the reader cannot verify that the algorithms actually solve FSC as defined; (b) the contributions claim image summarization experiments that are absent from the paper body. These are fixable issues, but in their current form they undermine the paper's completeness and self-consistency. For a top conference like ICLR, the paper needs stronger, properly-aligned experimental validation.

**MY FINAL SCORE:** <score>5.5</score>  
**MY FINAL DECISION:** <decision>Reject</decision>
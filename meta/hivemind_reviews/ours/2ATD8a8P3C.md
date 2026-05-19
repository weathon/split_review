Now I have enough information to produce the final consolidated review. Let me compile everything.

## Summary
2-3 sentence summary of the paper's contribution.

## Strengths
- strength 1 with evidence
- strength 2 with evidence

## Weaknesses

### Fatal
None

### Major
- weakness 1 — why it matters
- weakness 2 — why it matters

### Minor
- weakness 1 — why it matters

### Trivial
- weakness 1

## Nice-to-Haves
- suggestion that would improve but is not a core flaw

## Removed Points

## Novel Insights

## Suggestions

## Score and Decision

Let me now write the full review.

---

Let me now finalize my assessment of each critic claim against the paper:

**Critical Issue 1 (Marginal coverage):** The test checks if calibration errors ≤ (n+1)ε. The paper just says it "follows from learn-then-test." The critic claims this is not a valid p-value. However, the test is based on a standard binomial bound (Clopper-Pearson type) which is a known valid approach for marginal coverage guarantees in conformal prediction. The justification is too brief, but the claim isn't wrong per se. → Downgrade from Fatal to Minor.

**Critical Issue 2 (PAC union bound):** The critic is wrong. The algorithm stops at the first failure, so only the first invalid threshold matters. P(φ(Z, τ_0)=1) < δ → guarantee is 1-δ. No union bound needed. → REMOVE.

**Critical Issue 3 (Missing results):** Factually correct. Only SQuAD results shown. → KEEP as Major.

**Critical Issue 4 (No baselines):** Factually correct. No quantitative comparison to flat CP or any baseline. → KEEP as Major.

**Table 1 (ε=0.2):** Critic says this violates the coverage guarantee. Wrong — coverage guarantee is population-level, not per-example. → REMOVE.

**Proof direction error:** Paper writes "μ ≤ ε" when it should say "μ > ε" for an invalid threshold. But the inequality F(ℓ̂; n, μ) ≤ F(ℓ̂; n, ε) is still correct since ∂F/∂p ≤ 0. → Trivial typo.

**Related work novelty claim:** The paper says "first to adapt these techniques to provide PAC guarantees." Can't verify without reading Angelopoulos et al. → REMOVE per instructions (cannot independently verify).

**Strength 4 (empirical validation across three tasks):** Only SQuAD results are shown, so this "strength" conflicts with verified weakness. → REMOVE.

Let me finalize the score. Given:
- A reasonable, novel framework
- Correct theoretical guarantees (with minor presentation issues)
- A useful DAG+IP formulation
- **Incomplete evaluation**: results for only 1 of 3 tasks, no baselines
- No computational cost analysis

Score: 4.5, Decision: Reject

The paper's core idea has merit, but the evaluation is too incomplete to support the claims. A proper revision with full results and baselines could make this a solid contribution.Now I have all the information needed. Let me produce the final consolidated review.

---

## Summary

This paper proposes a general framework for conformal prediction in structured output spaces, where prediction sets are represented by interpretable structures (e.g., coarse labels in a hierarchy, intervals for dates) rather than flat label sets. The framework searches over candidate thresholds using statistical tests for either marginal or PAC coverage guarantees, and instantiates the approach for DAG-structured label spaces (hierarchical labels, intervals) via an integer program. The key idea is to generalize conformal prediction beyond simple classification/regression to settings where compact, interpretable prediction sets are desirable.

## Strengths

1. **First general framework for conformal structured prediction.** The paper formalizes a general setting (Section 2) where a user provides a search space of interpretable structures and an optimizer, and the framework constructs a conformal predictor with coverage guarantees. This is clearly distinguished from prior specialized approaches (Section 1, "existing approaches have all targeted specific domains and do not provide general algorithms").

2. **Clean DAG-based instantiation with integer programming formulation.** Section 4 provides a precise IP formulation (Eqs. opt1–opt6) for computing optimal prediction sets over DAG structures, covering hierarchical labels, intervals, and similar structures. The Boolean-to-linear constraint mapping (α→β, β→β', β→α∨β_parents) is well-conceived and directly implementable.

3. **Correct PAC guarantee with a clean proof.** Theorem 2 provides a PAC (training-conditional) guarantee for the sequential search algorithm. Despite a minor text error, the proof is logically sound: by focusing on the *first* invalid threshold and using the sequential stopping rule, it avoids the multiple-testing issue that a naive union-bound approach would require. The algorithm returns a valid threshold as long as the test correctly rejects this first invalid threshold, which occurs with probability ≥ 1-δ.

4. **Qualitative demonstration of interpretability benefit.** Table 1 shows concrete structured prediction sets (e.g., {[1979, 1980], [1997, 2019]}) vs. a flat set of six individual years, illustrating how structured sets can be more interpretable.

## Weaknesses

### Fatal
None.

### Major

1. **Evaluation results presented for only 1 of 3 described domains.** The paper describes three tasks (MNIST-digit numbers, ImageNet hierarchical classification, SQuAD-years QA) in Sections 5.1 and the introduction. However, quantitative results (coverage and size plots in Figures 1–3) are shown *only* for the SQuAD-years task. No coverage rates, set sizes, or any quantitative results are reported for MNIST or ImageNet. This makes the claim of a "general framework demonstrated across several application domains" unsupported by evidence. Without results on the other two domains, the paper does not demonstrate that the IP-based optimization scales to realistic problems (e.g., ImageNet has 1000 leaf labels) or works across qualitatively different DAG structures.

2. **No quantitative baseline comparisons.** The paper never quantitatively compares structured prediction sets against the obvious baseline: standard (flat) conformal prediction applied to the fine-grained labels. The only mention of a baseline is a single qualitative example (Table 1 caption) noting that standard CP gives "six years," but no comparison of sizes, coverage rates, or any other metric is provided. The paper's key practical motivation—that structured sets are more interpretable and potentially smaller—is therefore unquantified.

### Minor

3. **Marginal coverage guarantee is asserted rather than justified.** The marginal test (errors ≤ (n+1)ε) is stated and the theorem claims it "follows from the learn-then-test algorithm" (proof on line 109–111 is a single sentence). No derivation is given showing why this specific test yields a valid marginal guarantee, how it relates to the standard exchangeability argument, or what role learn-then-test's multiple-testing framework plays. The claim is likely correct, but the lack of justification is a gap in the paper's theoretical presentation.

4. **No discussion of computational cost.** The IP formulation for DAGs is described, but the paper does not report solution times or discuss computational complexity. For ImageNet with 1000 leaf nodes and a deep hierarchy, solving an IP for each test input (and for each candidate τ during calibration) could be expensive. The paper should at least acknowledge this limitation and report timings.

### Trivial

5. **Proof text contains a direction error.** In the PAC proof (line 147), the justification states "μ ≤ ε" when for the invalid threshold under consideration, μ > ε. The inequality F(ℓ̂; n, μ) ≤ F(ℓ̂; n, ε) is still correct (since the binomial CDF decreases with p), but the stated justification is wrong. This does not affect the proof's validity but should be corrected.

## Nice-to-Haves

- Report prediction set sizes for flat conformal prediction on the SQuAD task and compare numerically with the structured sets.
- Include a discussion of statistical power for the PAC test with small calibration sets (n=131), noting the conservativeness this induces.
- Ablate the effect of the number of candidate thresholds k on the coverage/size tradeoff.

## Removed Points

These points were raised by reviewers but are removed after verification:

- **"PAC proof missing union bound over multiple thresholds."** Removed. The proof is correct as written. The sequential search stops at the first invalid threshold; only that threshold's test result matters for the failure event. The critic's claim that "a passing test for any invalid threshold can lead to an invalid τ" misunderstands the sequential stopping rule—if τ_{i_0} (first invalid) is correctly rejected (φ=0), later thresholds are never tested.

- **"Table 1 ε=0.2 column violates the coverage guarantee."** Removed. The coverage guarantee is population-level (expectation over examples), not per-example. A single example missing the ground truth is expected with probability ε and does not constitute a violation.

- **"Marginal test formula (n+1)ε is uninterpreted and not standard."** Downgraded to Minor (see weakness 3 above). The test is a standard binomial bound; the issue is insufficient justification, not incorrectness.

- **"Related work novelty claim is misleading because learn-then-test already provides PAC guarantees."** Removed. Cannot verify this claim without reading Angelopoulos et al. 2022, and PAC (training-conditional) guarantees are distinct from the marginal guarantees learn-then-test primarily addresses.

- **Strength removed: "Empirical validation across three diverse tasks."** Removed. Results are only shown for one task (SQuAD), so this conflicts with verified weakness 1.

- **Strength removed: Generic strengths about the problem being important.** Removed per instructions (generic statements lacking specific evidence from the paper).

## Novel Insights

The most interesting structural observation across the reviews is about the relationship between the sequential search algorithm and the PAC guarantee. The algorithm's rule—stop at the first threshold that fails the test and return the previous one—implicitly avoids the need for a multiple-testing correction across the k thresholds. The proof only needs to bound the probability that the *first invalid* threshold passes its test, because if it correctly fails, the algorithm returns a valid (earlier) threshold regardless of what happens later. This is a clean observation, though it is already present in the paper's proof. Beyond this, no novel insight emerges beyond the paper's own contributions.

## Suggestions

1. **Complete the evaluation.** Report coverage and size results for the MNIST-digit and ImageNet tasks, analogous to Figures 1–3. Include at least one figure per task showing coverage vs. ε for marginal and PAC guarantees. For ImageNet, report the IP solution time per instance.

2. **Add quantitative baselines.** Compare structured prediction set sizes against flat conformal prediction (threshold on leaf-level scores) for all three tasks. If possible, also compare against Mortier et al. (2022) for hierarchical labels.

3. **Provide a proper derivation of the marginal guarantee.** Either derive it from exchangeability of the binary error indicators (standard split-conformal argument) or show the specific learn-then-test p-value computation and correction that yields the claimed result.

4. **Fix the typo in the PAC proof** (line 147: replace "μ ≤ ε" with "μ > ε").

## Score and Decision

The paper proposes a novel and well-motivated framework for structured conformal prediction, with a clean DAG/IP formulation. The theoretical guarantees are sound (modulo a minor presentation issue). However, the experimental evaluation is severely incomplete: only 1 of 3 tasks has quantitative results, and no baselines are provided. Without these, the paper's central claims of generality, effectiveness, and interpretability advantages over standard CP are unsupported. The contribution has clear potential but the current manuscript does not provide sufficient evidence to warrant acceptance.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>
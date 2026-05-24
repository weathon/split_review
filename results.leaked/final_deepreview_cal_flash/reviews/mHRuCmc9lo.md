Now I have all the information I need. Let me synthesize the final review.

**Initial bracket (Round 1):** The paper is clearly above the weak anchors (1.5-3.4) and below the strongest anchors (8.0). The middle band (3.5-7.5) is the plausible range, specifically the upper portion.

**Narrowing (Round 2):** Comparing directly to anchors:
- **X0epAjg0hd (5.67)** — Accepted, reassessing calibration metrics. Our paper has a more novel theoretical contribution (sharp transition result) and comparable presentation. Slightly stronger.
- **g6fYDGKeyB (6.00)** — Rejected, SBI calibration. Less directly comparable; our paper's theory is cleaner. Moderately stronger.
- **uuPkll6i7m (6.75)** — Accepted, certification of calibration under attacks. Strong theory + experiments; our theory is comparable but experiments are weaker. Slightly weaker.
- **iOMnn1hSBO (6.80)** — Accepted, decision-focused UQ. Novel framework + experiments; our theory is more theoretically deep. Comparable quality.
- **TId1SHe8JG (7.50)** — Accepted, higher-order calibration. Very strong complete theoretical treatment. Our paper is below this level.

**Final score: 6.5.** The theoretical contribution (sharp transition result, duality characterization) is genuinely novel and well-supported. The experimental section is under-documented, but this is illustrative rather than central. The paper sits above the 5.67-6.00 range and comparable to the 6.75-6.80 range, factoring in that the experiments are weaker than the theory warrants.

Now writing the review.

Let me think carefully about which weaknesses to include/remove.

The harsh critic gives two "Critical Issues":
1. Transparency of experimental construction — This is a real weakness. The paper says "altered to be worst-case... respecting ℋ-calibration constraints" but never describes how. KEEP as Minor.
2. Unspecified technical conditions for Theorem 3.1 duality — Real but minor since key results don't depend on it. KEEP as Minor.

The harsh critic also mentions "no measures of variability" — KEEP as Minor.
The harsh critic mentions "computational remarks" — Move to Nice-to-Have (scope).
The harsh critic mentions "approximate calibration" — Move to Nice-to-Have.
The harsh critic mentions "when decision calibration is not available" — Move to Nice-to-Have.

For the Strength Finder, I need to filter:
1. Sharp Transition to Plug-in Optimality — GENUINE, KEEP
2. Complete Closed-Form Characterization — GENUINE, KEEP
3. Novel Framework — GENUINE but generic phrasing, KEEP with specific details
4. Practical Pipeline Integration (Proposition 4.4) — GENUINE, KEEP
5. Simultaneous Optimality Across Multiple Decision Makers — GENUINE, KEEP
6. Empirical Validation — GENERIC/OVERSTATED given weak experimental documentation, REMOVE (the experiments are illustrative, not a core strength)
7. Clean Closed-Form for Bin-Wise Calibration — GENUINE, KEEP
8. Exceptional Clarity in Presentation — GENERIC, but the figures ARE effective. I'll keep it but tone it down.

Let me also check: "The differences between plug-in and robust are small enough that sampling noise could matter" - the harsh critic says this. Is this accurate? Looking at Table 1:
- Bike Sharing: Plug-in i.i.d. = 0.474, Robust i.i.d. = 0.463 (diff = 0.011)
- Worst-case for robust: Plug-in = 0.402, Robust = 0.410 (diff = 0.008)
- Worst-case for plug-in: Plug-in = 0.393, Robust = 0.412 (diff = 0.019)

These differences ARE small. Without error bars, we can't tell if they're significant. But the patterns are consistent across datasets. This supports the theory qualitatively even if individual numbers might have noise. I'll note this as a Minor weakness.

Now let me write the comprehensive review.## Summary

This paper develops a framework for decision-making under partial calibration guarantees (ℋ-calibration). It characterizes the minimax-optimal policy that maps forecasts to actions when the forecaster is only known to satisfy a set of moment constraints defined by a function class ℋ. The headline result is a sharp transition: once ℋ contains the decision-calibration indicators — just |𝒜| test functions — the optimal robust policy collapses to the simple plug-in best response, showing that full calibration is not necessary for decision-theoretic trustworthiness in a minimax sense. For weaker ℋ-classes, the optimal robust policy is tractably computable via duality, and the paper provides concrete instantiations for squared-loss-trained models and bin-wise recalibration, with illustrative experiments on two regression datasets.

## Strengths

1. **Sharp transition result (Theorems 4.1 and 4.2).** The finding that decision calibration — requiring only |𝒜| indicator test functions — suffices to make the plug-in best response minimax-optimal is the paper's most striking contribution. This is a genuinely non-obvious result that fundamentally simplifies the expected hierarchy and identifies a crisp, tractable target for trustworthy decision-making. The invariance argument (the adversary cannot reduce the utility of a_BR under decision-calibration constraints) is clean and clearly presented.

2. **Complete closed-form characterization for finite ℋ (Theorem 3.1).** The duality-based characterization yields an explicit, computable two-step procedure — compute q* via pointwise convex minimization, then best-respond to q*. This provides a unified technical engine from which all subsequent specializations are derived, and the pointwise computability is a practically useful property.

3. **Practical pipeline integration (Proposition 4.4).** The observation that any model with a linear final layer trained to squared-loss stationarity automatically satisfies a self-orthogonality ℋ-calibration condition identifies a "free" guarantee applicable to ubiquitous ML pipelines (linear models and neural networks with linear heads). This bridges the theory to practice without requiring algorithmic intervention.

4. **Simultaneous optimality across multiple decision makers (Corollary 4.3).** The corollary that a single decision-calibrated predictor allows every downstream decision maker to optimally best respond simultaneously is a strong and practically relevant consequence.

5. **Clean closed-form for bin-wise calibration (Proposition 4.5).** For the widely available post-hoc recalibration setting, the robust policy reduces to best-responding to the bin mean — a remarkably simple form requiring no additional optimization.

6. **Clear presentation.** The paper is well-organized, the "interpolating property" schematic (Figure 1) and "sharp transition" illustration (Figure 2) effectively anchor the abstract mathematical content in an intuitive visual narrative.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor
1. **Experimental transparency regarding adversarial distribution construction.** The paper reports adversarial performance under "worst-case distributions that respect the ℋ-calibration constraints" but provides no description of how these distributions are constructed — neither in the main text nor through a reference to the appendix. Without knowing whether the adversarial outcomes are generated by reweighting, solving the dual for q*, directly replacing the conditional mean, or some other procedure, the reader cannot verify that the constraints are actually satisfied or that the comparisons are apples-to-apples. The paper's core contribution is theoretical, and the experiments are clearly illustrative, but the missing details weaken what is presented as empirical validation.

2. **No uncertainty quantification in experiments.** The reported mean utilities in Table 1 lack any measure of variability (standard errors, confidence intervals, or bootstrap estimates). The differences between robust and plug-in policies are small (e.g., 0.008–0.019 utility difference on Bike Sharing), and without variability measures, sampling noise could be comparable to these differences. Bootstrap error bars would substantially strengthen confidence in the qualitative patterns the experiments are meant to illustrate.

3. **Unspecified technical conditions for Theorem 3.1 duality.** The derivation of the closed-form characterization relies on strong duality and a saddle-point property for an infinite-dimensional convex program, but the paper provides no indication of what technical conditions are needed (e.g., Slater-type conditions, constraint qualification, compactness in a suitable topology). While this does not affect the paper's core results (Theorems 4.1 and 4.2 are proved independently via direct invariance arguments), it limits the ability of readers to apply Theorem 3.1 to new ℋ-classes with confidence.

### Trivial
- The notation val(p) in Theorem 3.1 is defined but could be more clearly motivated as the value of the inner decision problem given a belief p. This is a minor presentational point.

## Nice-to-Haves
- A brief computational complexity remark (scaling with |ℋ|, d, and |𝒜|) would help readers gauge practical applicability of the duality-based procedure for larger ℋ-classes.
- A short paragraph summarizing how the main conclusions extend to the approximate ℋ-calibration setting (discussed in Appendix B, which was stripped by the parser) would help readers who cannot access the appendix.
- A discussion of practical strategies for identifying or selecting an appropriate ℋ-class when decision calibration is unavailable (e.g., using held-out data to test candidate test functions) would bridge the gap to deployment.

## Removed Points

These points were identified by the input reviewers but are removed for the reasons stated:

- **"Empirical Validation" claimed by Strength Finder** — The experiments are illustrative and consistent with theory, but the missing construction details and lack of error bars make "validation" an overstatement. The paper's primary contribution is theoretical; the experiments serve as a sanity check, not a core strength. Moved from Strengths.
- **"Novel Framework" (generic phrasing)** — While the framework is indeed novel, the Strength Finder's phrasing was generic. The substantive framework contributions are already listed in Strengths 1–5 above.
- **Missing related works** — Per Hard Rules, no related-work criticisms are retained, as I cannot independently verify the existence of unmentioned references.
- **Criticisms about the paper not discussing approximate ℋ-calibration in the main body** — The paper mentions Appendix B handles this; the appendix was stripped by the parser. This is not a weakness of the existing submission.
- **Demands for additional datasets or broader experimental scope** — The paper is a theoretical paper with illustrative experiments; requesting more datasets exceeds the stated scope.

## Novel Insights

The most interesting observation emerging from the review process is the following. The harsh critic's framing of the experimental transparency issue and the strength finder's praise of the experiments as "empirical validation" are in direct tension: the former identifies a genuine documentation gap, while the latter overinterprets what the paper actually provides. This tension highlights that the paper would benefit from either (a) fleshing out the experimental construction so the experiments can stand as genuine validation, or (b) explicitly downgrading the experiments to "illustrative numerical examples" and removing "empirical evaluation" language. The paper implicitly takes the second path (the experiments are clearly labeled as case studies), but the text surrounding them uses language like "evaluate the validity and practical consequences" which promises more than what is delivered.

Beyond this, a noteworthy observation: the self-orthogonality condition (Proposition 4.4) is a particularly elegant bridge between the theory and practice because it requires no post-hoc calibration step — it follows from first-order optimality of standard squared-error training. This means the framework's robust policy can be applied essentially for free to any linear-head regression model. The paper could emphasize this point more.

## Suggestions

1. **Document the adversarial construction.** Add 3–4 sentences explaining how the worst-case distributions are generated: e.g., "For the plug-in-tailored adversary, we solve the dual problem to obtain the worst-case q* given the plug-in policy a_BR, then set Y_test = q*(f(X_test)). For the robust-tailored adversary, we analogously use the robust policy's dual solution." This would resolve the most significant experimental transparency issue.

2. **Add bootstrap error bars or confidence intervals** to the reported utilities in Table 1 (even simple ±1.96 SE from 1000 bootstrap resamples would suffice). The patterns in the table are consistent with theory, but the small absolute differences make variability information essential.

3. **Add a brief remark about strong duality conditions for Theorem 3.1.** Even one sentence — "Under standard constraint qualifications (e.g., the moment constraints admit a feasible interior point in the appropriate function space), strong duality holds and the saddle point exists" — with a reference would improve rigor without needing to expand the proof section significantly.

## Score and Decision

**Calibration anchors used:**

| Anchor ID | Avg Score | Round | Comparison to this paper |
|-----------|-----------|-------|------------------------|
| WoJzHQIIUk | 1.50 | R1 (weak) | Much weaker; poorly-motivated minimax framework |
| ZBL26FX0FT | 3.00 | R1 (weak) | Weaker; calibration-focused but no decision-making framework |
| lvHHWDJCcr | 3.40 | R1 (weak) | Weaker; metric calibration, not decision theory |
| 7BDUTI6aS7 | 3.00 | R1 (weak) | Weaker; DRO with φ-divergence, less novel |
| XM7INBbvwT | 4.67 | R1 (mid) | Weaker; HCI study of calibration, less theoretical |
| X0epAjg0hd | 5.67 | R1 (mid), R2 | Slightly weaker; important calibration analysis but less theoretical novelty |
| g6fYDGKeyB | 6.00 | R2 | Comparable quality but different subfield; our theory is cleaner |
| dNunnVB4W6 | 6.25 | R2 | Weaker theoretical depth; calibration of linguistic expressions |
| uuPkll6i7m | 6.75 | R1 (mid), R2 | Slightly stronger; comparable theory + more complete experiments |
| iOMnn1hSBO | 6.80 | R2 | Comparable; decision-focused UQ with strong experiments |
| TTrzgEZt9s | 8.00 | R1 (strong) | Stronger; DRO with faster algorithm and thorough evaluation |
| stUKwWBuBm | 8.00 | R1 (strong) | Stronger; MARL with behavioral economics, complete empirical work |
| A3YUPeJTNR | 8.00 | R1 (strong) | Stronger; prediction-driven allocations with applied implications |
| UHPnqSTBPO | 8.00 | R1 (strong) | Stronger; LLM evaluation with provable guarantees |
| TId1SHe8JG | 7.50 | R2 | Stronger; higher-order calibration with complete theoretical treatment |

**Initial bracket (R1):** 5.0 – 7.5. The paper is clearly above the weak anchors (1.5–3.4) and below the strongest anchors (8.0). Within the middle band, it sits in the upper portion.

**Narrowing (R2):** Comparing to anchors in the 5–7.5 range, the paper's theoretical contribution (sharp transition, duality characterization) is stronger than the 5.67 and 6.00 anchors, comparable to the 6.75–6.80 anchors in theoretical depth, but notably weaker in experimental completeness. The 7.50 anchor (higher-order calibration) is a step above in both theory and experiments.

**Final score: 6.5.** This paper makes a genuinely novel theoretical contribution with a clean, well-presented framework and an actionable headline result. The weaknesses (experimental documentation, no uncertainty quantification, unspecified duality conditions) are real but do not undermine the core theory. With targeted revisions — particularly documenting the adversarial construction and adding error bars — the paper would be a strong, clean addition to the literature.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>
- Decision: Reject
- Avg Score: 4.00
- Scores: 3, 5, 5, 3
I have thoroughly reviewed the paper and both reviewer inputs. Let me now construct the consolidated review.

## Summary

This paper proposes B-PDF, an optimizer that integrates block coordinate descent (BCD) with the Hessian-informed zeroth-order optimizer HiZOO for LLM fine-tuning. By partitioning model layers into blocks and storing/updating diagonal Hessian estimates only for the active block, B-PDF reduces the memory overhead of second-order information from O(d) to O(d/D). Experiments on OPT-1.3B and LLaMA-2-7B show up to ~39% GPU memory reduction over HiZOO while maintaining competitive accuracy, and the method successfully enables Hessian-informed fine-tuning of LLaMA-2-7B on a single 48GB GPU where HiZOO encounters OOM.

---

## Strengths

1. **Clear, measurable memory savings.** Table 1 shows B-PDF uses 11.2 GB vs. HiZOO's 15.4 GB on OPT-1.3B (~27% reduction), and Table 2 shows 11.4 GB vs. 18.6 GB on SST-2 (~39% reduction). These numbers directly substantiate the paper's central memory-efficiency claim. The paper also provides a useful worked example: partitioning LLaMA-2-7B into 32 blocks reduces Hessian storage to under 1 GB (Section 3.2).

2. **Enables Hessian-informed fine-tuning on larger models under hardware constraints.** On LLaMA-2-7B (Table 4), HiZOO encounters out-of-memory on a 48 GB GPU while B-PDF runs successfully, achieving improved accuracy over MeZO (92.1 vs. 91.4 on SST-2) with comparable memory usage. This demonstrates practical scalability that goes beyond the base method.

3. **Competitive accuracy across multiple GLUE tasks.** Table 3 shows B-PDF matches or exceeds MeZO accuracy on 5 of 6 tasks (e.g., COLA 77.3 vs. 78.7, RTE 83.7 vs. 82.9, MRPC 69.0 vs. 67.9) while reducing memory, confirming that the memory savings do not come at the cost of degraded fine-tuning performance.

---

## Weaknesses

### Major

- **Stale Hessian for inactive blocks is unaddressed.** The method stores and updates diagonal Hessian estimates *only* when a block is active (abstract: "stored and updated exclusively for the active layers"; Section 4.1). When a block becomes active again after other blocks have been updated, its Hessian estimate was computed at a prior parameter configuration. The paper provides no analysis of how this affects convergence, no mitigation strategy (e.g., re-estimating on reactivation or an adjusted learning rate for stale blocks), and does not even acknowledge the issue. While BCD methods for first-order optimizers (BAdam, LiSA) face a similar issue, the Hessian preconditioner is the central mechanism by which B-PDF claims convergence improvements over MeZO, making the staleness more consequential. This is a significant gap in the paper's analysis.

- **Incomplete evaluation: no variance reporting and limited ablations.** (a) All experimental results appear to be single runs; no standard deviations or confidence intervals are reported for any metric. This is a standard expectation for empirical ML papers. (b) An obvious ablation is missing: comparing B-PDF against **BCD + MeZO** (blockwise zeroth-order without Hessian information) would isolate whether the Hessian provides any benefit beyond the BCD structure alone. The paper includes BCD+SGD for first-order baselines but no BCD+MeZO, which is the direct control for the Hessian component. (c) Multiple block sizes are not explored — the paper uses two active layers per iteration but does not ablate this choice (e.g., 1, 2, 4, 8, all layers) to characterize the memory-vs-accuracy trade-off.

- **Wall-clock speedup claim lacks precise explanation.** The paper states (Section 5.1, Figure 3 caption) that B-PDF finishes training faster than MeZO and HiZOO, attributing this to "the BCD strategy, which activates only a subset of layers ... thereby reducing computational demands." However, all zeroth-order methods require three (HiZOO, B-PDF) or two (MeZO) *forward passes through the entire model*, and the forward pass itself dominates runtime. The paper does not decompose *where* the per-step savings come from — e.g., cheaper perturbation vector generation (only for the active block's d/D parameters), cheaper Hessian estimate computation, cheaper parameter update — nor does it provide per-step timing breakdowns. The speedup may be real (Figure 3 suggests it is), but the mechanism is not clearly explained, making the claim harder to verify or reproduce.

### Minor

- **BCD block-selection strategies are listed but not empirically compared.** Equation 7 enumerates several strategies (ascending, descending, importance sampling, Gauss-Southwell-Diagonal, bandit methods), but the paper defaults to ascending order and provides no experimental comparison. The justification (line 151: other methods are too expensive) is reasonable but unquantified; even a small-scale comparison would strengthen the paper.

- **No comparison with BAdam/LiSA even on accuracy.** The paper correctly notes that BAdam and LiSA are first-order methods requiring more memory, so a memory-equivalent comparison is difficult. However, an accuracy comparison on the same tasks (where memory is not the constraint) would help contextualize B-PDF's quality relative to the broader BCD literature.

### Trivial

None.

---

## Nice-to-Haves

- Analyze the impact of Hessian staleness by comparing B-PDF against a variant that re-estimates the Hessian for the active block each time it is selected (fresh Hessian). Even a brief empirical study on one task would address the major concern above.
- Provide per-step wall-clock timing breakdowns (forward pass, Hessian computation, parameter update) to clarify the source of the observed speedup.
- Report results with standard deviations over at least 3 random seeds for the main comparisons.

---

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Critic's assertion that "per-step time should be nearly identical to HiZOO."** This is factually incorrect: it ignores that the Hessian estimate computation (diagonal update, Σ^{1/2}z multiplication, parameter update) applies only to the active block's d/D parameters, yielding meaningful per-step savings. The critic's framing that the speedup "contradicts the method's own computational profile" is unwarranted. The claim was downgraded to a Minor weakness about clarity of explanation, but the critic's stronger accusation was removed.

- **"MeZO achieving only 61.46% on SST-2... unusually low... inflates the gain."** The paper explicitly acknowledges (Section 5.2, line 196) that "limited batch size and hardware constraints... caused an accuracy drop from incomplete convergence." The critic's assertion that this "inflates the gain" overstates the issue, as the paper is transparent about the constraint.

- **"No comparison to Adam-based BCD methods (BAdam, LiSA) as baselines."** The critic's framing treated these as missing baselines, but they are first-order methods operating in a fundamentally different memory regime. The paper is scoped to zeroth-order, memory-constrained settings. The criticism is scope creep; it was downgraded to a Minor point.

- **Strength from Strength Finder: "Proposes flexible BCD block-selection strategies."** This strength is generic/superficial: the strategies are listed but not empirically compared, and the paper defaults to the simplest one (ascending order). The strength lacks substantive evidence.

---

## Novel Insights

None beyond the paper's own contributions. The reviews identify a genuine methodological gap (stale Hessian analysis) and call for sharper evaluation standards (variance reporting, ablations), but these are standard review observations rather than novel insights about the paper's content.

---

## Suggestions

1. **Address the stale Hessian directly:** Add a paragraph discussing the issue, and ideally a small experiment comparing against a "fresh Hessian" variant on one task. Even a negative result (no significant difference) would be valuable.
2. **Add BCD+MeZO as a baseline** to isolate the contribution of Hessian information vs. the BCD structure alone.
3. **Ablate block size** (active layers = 1, 2, 4, all) and report the resulting memory/accuracy trade-off in a compact table.
4. **Report standard deviations** over 3 seeds for all main results.
5. **Clarify the speedup mechanism** with a per-step timing breakdown or at least a clearer explanation in the text.

---

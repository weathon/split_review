Now I have all the information needed to write the consolidated review. Let me compose it.

---

## Summary

This paper establishes a first-order theoretical equivalence between activation steering (adding vectors at intermediate layers) and influence functions (re-weighting training data). It introduces Influence-Aligned Steering (IAS), a constructive mapping between the two, along with an alignment diagnostic ω that characterizes when steering can faithfully reproduce influence effects, a spectral optimality result for principled steering direction selection, and generalization bounds for low-rank steering corrections. The work offers a clean geometric unification of two previously disconnected interpretability methods.

## Strengths

- **Closed-form duality between activation steering and influence functions (Theorem 4.2).** The paper provides the first formal bridge showing that, to first order, any steering vector corresponds to a signed influence weighting over training data (and vice versa), with an explicit ℓ₁-minimal construction (Corollary 1). This is a genuinely novel theoretical link between two previously separate lines of interpretability research.

- **Alignment-based feasibility diagnostic ω (Theorem 5.1).** The cosine of the smallest principal angle between Im(**J**_h→y) and Im(**J**_ω→y) cleanly characterizes when steering can perfectly match influence effects. The no-free-lunch bound (Theorem 6.2) proves that when ω is small, no activation-space edit can replicate data re-weighting — a principled, pre-computable condition guiding practitioners' choice between steering and weight editing. Figure 2 verifies that ω increases with layer depth on GPT-2 Medium, providing a data-driven heuristic for layer selection.

- **Spectral optimality for steering direction selection (Theorem 5.3).** Under an ℓ₂ norm budget, the steering vector maximizing first-order logit change is the top eigenvector of a Fisher–influence matrix. This replaces ad-hoc direction construction with a principled spectral recipe, validated on ResNet-50/ImageNet (p=0.00498 against random directions, Figure 3).

- **Self-contained theoretical framework.** The paper develops the primal-dual perspective (Section 3), the core equivalence (Section 4), alignment bounds (Section 5), spectral optimality (Section 5.3), layer-wise composability (Lemma 5.4), and generalization guarantees (Section 6) in a coherent mathematical narrative.

## Weaknesses

### Major

- **Experimental validation is too thin to support the claimed practical contributions.** The paper promises a "single, efficient workflow for controllability and data provenance" (conclusion) and a practical mapping from steering vectors to causal training examples (Corollary 1, Section 4.1). Yet:
  - The only full evaluation is a single detoxification task on GPT-2 Medium (a small, 354M-parameter model), comparing two steering methods with no error bars, no statistical significance tests, and marginal absolute differences (toxicity 0.0164 for IAS vs 0.0150 for CAA; perplexity 13701 vs 13291). Importantly, CAA — a simple baseline — *outperforms* IAS on both metrics, which the paper does not discuss.
  - The data-provenance mapping, which the abstract and introduction highlight as the paper's most distinctive practical payoff ("map undesired behaviors back to causal training examples"), is **never demonstrated in any experiment**. There is no qualitative example, no verification that top-weighted training examples are causally relevant, and no comparison with alternative attribution methods (TRAK, TracIn, etc.).
  - The first-order equivalence experiment (Section 7.2) reports a cosine of 0.978 but a **slope of 1.50**, meaning actual logit shifts are 50% larger than predicted. The paper dismisses this as "consistent with the expected linear regime" without any discussion of the discrepancy — a slope of 1.0 would be expected from exact first-order theory, and 1.50 suggests a systematic bias (e.g., Hessian damping miscalibration, nonlinearity, or a flaw in the influence computation).

- **The central data-provenance claim is untested.** Corollary 1 (minimal ℓ₁ data re-weighting from steering) is presented as a core practical contribution: "Given an empirical steering vector, ρ_s pinpoints the fewest training examples to relabel/remove/examine to reproduce the behavioral change." No experiment validates this. Without this demonstration, the paper's most distinctive applied selling point remains a theoretical curiosity.

### Minor

- **Abstract and introduction overstate the generality of the equivalence.** The abstract states "any steering vector can be represented as an influence weighting over training data and vice versa" without qualification. The main text (Theorem 4.2) reveals this is conditional on a subspace-inclusion condition (Im(**J**_h→y) must contain the influence vectors' span), with a residual otherwise bounded by √(1−ω²). While it is common for abstracts to simplify, the gap between the unconditional framing and the conditional result is wider than typical, especially given that the condition is never verified empirically.

- **Scalability of computing ρ_s is not adequately addressed.** The paper's cost model (two Jacobian–vector products, a rank-d pseudoinverse) covers the IAS vector construction and the ω diagnostic. However, constructing ρ_s requires either forming the full set of per-example influence vectors {I(z→x)} (which itself requires a Hessian-vector product for every training point) or solving a large ℓ₁-minimization problem. Neither procedure is analyzed for computational cost or demonstrated at any scale. The paper acknowledges the Hessian dampening issue (citing Basu et al., 2021) but does not evaluate sensitivity to the damping parameter φ.

- **The slope discrepancy in the first-order experiment (slope 1.50) is unexplained.** As noted above, a slope significantly different from 1.0 suggests systematic deviation from the first-order theory. Potential causes (damping miscalibration, linearity breakdown at the chosen magnitude, numerical issues in the influence computation) are not investigated, and no control experiments (e.g., varying the steering magnitude μ) are reported.

- **Generalization bounds (Theorem 6.1) are a straightforward extension of existing work.** The paper explicitly states it "combine[s] Thm. 2 of Pinto et al. (2024) with the fact that IAS changes only a rank-k submatrix of the layer weight." The connection to the actual steering mechanism (vector addition, not a low-rank matrix update) is also tenuous. This section adds limited value to the paper's core contribution.

### Trivial

- The reported p-value for the spectral experiment (p=0.00498) uses a z-score of 3.55, which would correspond to a much smaller p-value under a normal approximation. Minor inconsistency in reporting.
- Table 1 uses bold for CAA's metrics despite IAS being the paper's method, which could confuse readers about which method is preferred.

## Nice-to-Haves

- A demonstration of the data-provenance mapping (Corollary 1): e.g., apply a detoxification steering vector, compute ρ_s, and verify that top-weighted training examples are indeed toxic or correlated with the targeted behavior.
- Error bars or confidence intervals on the main experimental results (Table 1, Figure 1).
- Experiments on a larger model (e.g., 7B scale) and on at least one additional task (sentiment control, fact-editing, or bias removal).
- An investigation of the slope=1.50 discrepancy, e.g., by varying the steering magnitude and plotting regression slopes.
- Comparison with recent steering baselines beyond CAA (e.g., representation engineering methods from Zou et al., 2023).
- A sensitivity analysis of the Hessian damping parameter φ.

## Removed Points

- *Criticism about "missing appendix/proofs in appendix":* The parser strips appendix content; these exist in the original submission. Removed per hard rules.
- *Criticism about "the paper claims 'two backward passes per input' but omits the cost of forming influence vectors":* The paper's cost model explicitly addresses this ("two Jacobian–vector or vector–Jacobian products per input, a rank-d pseudoinverse, and a small SVD"). The cost of forming full influence vectors across all training points is a separate issue acknowledged above. Removed as partially misreading the paper's cost claim.
- *Criticism that "the Hessian H_ω is introduced but never used":* The Hessian is used throughout the influence function formulation (lines 107-114, 152-160). Removed as factually wrong.
- *Strength Finder's claim that "practical workflow with verified first-order accuracy" is a strength:* The "workflow" is claimed but the data-provenance step is not demonstrated. The first-order accuracy claim is partially supported (cosine 0.978) but undermined by the slope 1.50 issue. Moved here as it conflates verified partial accuracy with an unverified end-to-end workflow.
- *Generic strengths from Strength Finder lacking specific citations or content:* Filtered per instructions.

## Novel Insights

Beyond the paper's own contributions, the reviews highlight an important gap between theory and applied claims in interpretability unification papers. The paper's core theoretical result — that steering and influence are first-order projections of the same sensitivity tensor — is genuinely novel and provides a clean geometric framework. However, the reviews collectively reveal that the paper substantially overclaims its practical utility: a theory paper that promises end-to-end data provenance but never traces a single steering vector back to a training example cannot claim to offer a "single workflow for controllability and data provenance." The ω diagnostic is the paper's most experimentally validated contribution; the spectral optimality result is promising but only validated on a single-class ImageNet test. The most interesting unresolved question — why the first-order logit shift has slope 1.50 rather than 1.0 — could point to important second-order effects that the paper's theoretical framework does not capture, and addressing it would strengthen a revision significantly.

## Suggestions

1. **Demonstrate the data-provenance mapping (Corollary 1).** This is the paper's most distinctive applied claim. Without it, the practical workflow narrative is unsupported. A simple experiment: apply a detoxification steering vector, compute ρ_s over a moderate-sized training set (e.g., 1k-10k examples), and show that the top-weighted examples are causally related to toxicity (e.g., by showing that removing them changes the model's toxic behavior, or that they have high toxicity scores).

2. **Investigate and explain the slope-1.50 discrepancy.** Run the first-order equivalence experiment at multiple steering magnitudes and plot the slope vs. μ. If the slope converges to 1 as μ→0, the theory holds and the current slope indicates mild nonlinearity at the chosen magnitude. If not, there is a systematic bias that needs correction.

3. **Add error bars and expand the model/task scope.** At minimum, report standard deviations or confidence intervals for the main detoxification experiment. Expand to one larger model (e.g., Llama-2-7B or GPT-2 XL) and one additional task (e.g., sentiment control or fact-editing on a counterfactual dataset).

4. **Tone down the practical workflow claims.** If the data-provenance demonstration is not added, reframe the paper as a theoretical contribution (first-order duality) with supporting diagnostic tools (ω, spectral direction), rather than claiming an integrated practical workflow. The abstract's unconditional framing should be qualified.

## Score and Decision

### Calibration Anchors

| Path | Avg Human Score | Comparison |
|---|---|---|
| `vzkEX2SwFD` (PID Steering) | 6.00 (Accept Poster) | Broader experiments across multiple models (Gemma2, LLaMA3, Qwen2.5) and tasks (toxicity, jailbreak, style). Stronger experimental support despite similar theoretical aspirations. |
| `XyQ5ui62mm` (Belief Dynamics) | 4.50 (Reject) | Also unified two control methods theoretically; criticized for "thin results" and limited diversity. Comparable experimental weakness, but this paper has stronger theoretical originality. |
| `EDPvNhTOLK` (DIF) | 6.00 (Reject) | Influence function paper with validated LOO experiments on CNNs. More thorough empirical validation despite mixed reviews. |
| `YEBpZVm70i` (BIF) | 5.50 (Accept Poster) | Experiments on Pythia-2.8B and Inception-V1 with strong baselines. Better empirical support. |
| `y3bTy8ao1N` (SteerCLR) | 4.50 (Reject) | Steering method with thin experiments and weak baselines (only CAA). Comparable experimental limitations. |
| `I3IeAZvxB4` (Painless Steering) | 3.33 (Reject) | Empirical-only steering paper; criticized for lack of theory. This paper's theory is substantially stronger. |
| `TwkcMNACXo` (f-INE) | 5.50 (Accept Poster) | Stronger experiments on Llama-3.1-8B with validation against ground truth. Better empirical rigor. |

### Assessment

The paper's theoretical core — the first-order duality between activation steering and influence functions — is genuinely novel and well-motivated. The ω diagnostic is a clean geometric contribution, and the spectral optimality result provides a principled alternative to ad-hoc direction construction. However, the experimental validation is far too thin to support the claimed practical workflow, and the paper's most distinctive applied contribution (data provenance via Corollary 1) is never demonstrated. The unexplained slope of 1.50 raises questions about the fidelity of the first-order approximation. Relative to accepted anchors (PID Steering at 6.0, BIF at 5.5, f-INE at 5.5), this paper has weaker experiments and unsupported applied claims. Relative to rejected anchors with similar experimental limitations (Belief Dynamics at 4.5, SteerCLR at 4.5), the theory is stronger. On balance, the paper falls between these bands — the theory is good enough to merit attention but insufficiently validated for acceptance in its current form.

**Score: 5.0**  
**Decision: Reject (borderline; would be competitive with strengthened experiments)**

Paper quality axis: **Originality 7/10, Importance 7/10, Claims support 4/10, Soundness 5/10, Clarity 6/10, Community value 6/10**

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>
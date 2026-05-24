Now I have enough information to write the consolidated review. Let me compare the paper against the calibration anchors and produce the final review.

## Summary

This paper extends the training-loss-curve (TLC) collapse phenomenon — where normalized loss curves from different model sizes align onto a single trajectory — from small-scale simplified settings to practical LLM training (300M–3.9B parameters). It identifies three controls governing collapse (AdamW timescale τ, tokens-per-parameter ratio TPP, and LR schedule), demonstrates collapse across the Celerity model family, and proposes two applications: deviation-from-collapse monitoring for early detection of training issues, and a collapse-based early-stopping method for hyperparameter tuning.

## Strengths

1. **Clean demonstration of TLC collapse at practical LLM scale.** Using the Celerity model family (300M–3.9B), the paper shows that normalized loss curves align tightly across model sizes when τ and TPP are fixed and the LR schedule is matched (Figure 1 middle, Figure 6). This directly addresses the open question from Qiu et al. (2025) about whether collapse persists under practical scaling recipes with weight decay, co-scaled batch size, and μP. The contrast with Llama-2 (Figure 1 left), where τ and TPP vary and curves do not collapse, makes the case convincingly.

2. **Principled explanation of τ's role via bias–variance decomposition.** The noisy-quadratic model (Eq. 3, Appendix B.3) provides a clean theoretical account of how τ controls the bias–variance trade-off: smaller τ yields faster initial decay but a higher variance floor, while larger τ averages more past gradients for better variance suppression at the cost of slower early progress. This explains the observed "fast-then-flatten" behavior and why LR decay inverts the ordering of τ-specific curves. The scale-invariance argument (curvature factor h cancels under normalization) is neatly tied to μP theory.

3. **Practical tools with demonstrated real-world utility.** The deviation-from-collapse diagnostic detected a numerical instability in the 1.8B run at ~60% of training — well before the raw loss curve showed an upward trend — enabling early repair and a successful restart (Figure 1 right, Figure 6 right). This is a genuine operational success story in a real large-scale training setting. The early-stopping method (Section 5) shows that by aligning partial curves to a small-scale surrogate, one can select the best hyperparameter after only 10–30% of training on λ sweeps (Figure 9), which could meaningfully reduce tuning compute.

4. **Introduction of Celerity as a community resource.** The Celerity model family, trained with consistent methodology and without annealing on benchmark subsets, is positioned as a clean baseline for the community. The compute-vs-parameter-efficiency analysis (Figure 5, Appendix C.1) is a thoughtful, data-driven design choice.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **The deviation-from-collapse diagnostic is demonstrated on a single case study.** While the 1.8B numerical instability example is compelling, the paper claims in the abstract that deviation-from-collapse "provides a sensitive, early diagnostic of training pathologies" — a general statement supported by just one
post-hoc example. No threshold or decision rule is proposed, there is no comparison to simpler signals (e.g., loss spikes, gradient norm anomalies) that might have caught the issue similarly early, and no evaluation on a second failure mode (synthetic or from prior work) to establish generality. The concept is valuable and the case study is informative, but the evidence falls short of the claimed generality.

2. **The early-stopping method is validated on λ (weight decay) sweeps only.** Figure 9 shows strong results for
tuning λ at two model scales, but the paper acknowledges (Section 5) that "cases where τ must vary" could strain the method. No experiments are reported for sweeps over η, B, or data mixing — axes where the power-law assumptions of the surrogate model (Eq. 4–5) are likely to be strained. This limits confidence in the method's claimed generality.

3. **Incremental novelty relative to closely related prior work.** The paper lists "Identifying the key factors influencing loss curve shape" as a main contribution. However, the role of τ was established in Bergsma et al. (2025a) (which showed optimal τ depends on TPP), the supercollapse phenomenon was introduced by Qiu et al. (2025) at small scale, and the μP framework is prior art. The paper's real contributions — empirical confirmation at LLM scale, synthesis of the factors, and practical applications — are significant, but the framing slightly overstates novelty. A more precise characterization (e.g., "unified empirical account and scale-up") would better reflect the paper's position in the literature.

4. **Slight tension between the "clean evaluation" philosophy and the benchmark comparison.** The paper criticizes the common practice of annealing on benchmark subsets as "mak[ing] evaluation problematic" (Section 4), then places Celerity on a Pareto frontier with models that use such practices (Figure 2). This is not a contradiction — the paper is making the reasonable argument that Celerity is competitive despite not using these techniques — but the framing is somewhat at odds with itself. The frontier comparison is standard practice, but the "Philosophy" paragraph creates an expectation of a different evaluation stance that the paper then does not fully follow through on.

### Trivial
None.

## Nice-to-Haves

- The deviation-from-collapse diagnostic would be stronger with a simple quantitative rule (e.g., "trigger if the rolling residual exceeds X for Y% of training") and a test on at least one additional failure scenario.
- Testing the early-stopping method on an η sweep at fixed τ would substantially bolster the generality claim.
- A discussion of the surrogate model's failure modes — e.g., what happens when the power-law assumptions for b(τ) and q(TPP) break down — would be valuable.
- The "choose current best" baseline in Figure 9 is a very weak comparator; a comparison to standard early-termination methods (e.g., ASHA, learning-curve extrapolation) would better situate the method.

## Removed Points

- **"Internal evaluation incoherence" (from Harsh Critic):** The critic argues that criticizing annealing while comparing against annealed models is contradictory. The paper's position is coherent — it criticizes the practice as making strict evaluation difficult while noting that Celerity is competitive despite not using it. This is a standard "competitive without tricks" argument, not a contradiction. Removed because the criticism misreads the paper's argument.

- **"Inflated novelty" framing as a critical issue:** The critic's point about prior work establishing the factors is partially valid, but it is presented as a structural flaw rather than the incremental-nature caveat that it is. Demoted to Minor weakness 3 above.

- **Generic strengths from Strength Finder:** The claim that "the paper is well-written and clear" (while true) is too generic to list as a distinct strength. The theoretical grounding claim (noisy quadratic model) is kept but contextualized — it is a clean exposition but not a deep theoretical result.

- **Strength Finder's claim about "identification of τ as a unifying control for curve ordering in batch-size sweeps":** This is well-supported by Figure 7 and is a genuinely useful finding. Kept as part of the general contribution framing rather than as a separate strength entry.

- **Strength Finder's claim about "Compute-vs-parameter-efficiency analysis to choose TPP":** This is well-reasoned but is a design choice for Celerity, not a core scientific contribution. Kept as part of Strength 4.

## Novel Insights

None beyond the paper's own contributions. The review process surfaced a few useful observations: (1) the tension between the "clean evaluation" philosophy and the conventional frontier comparison is real but not disabling — the paper would benefit from either leaning fully into the clean-baseline narrative or dropping the rhetorical critique; (2) the single-case-study validation of the diagnostic tool is the weakest link in an otherwise solid empirical chain; (3) the paper's position in the literature is best characterized as an empirical confirmation and synthesis at scale rather than a discovery of new factors.

## Suggestions

1. **Broaden the diagnostic validation.** If the authors have access to other training runs with known issues (even from prior literature or synthetic instabilities), demonstrating that collapse residuals catch them earlier than raw-curve inspection would transform a suggestive anecdote into a substantiated method.

2. **Add one experiment sweeping η at fixed τ** for the early-stopping validation. This is a small addition that would substantially strengthen the claim of generality.

3. **Reframe the novelty claims** to more precisely distinguish what is new (empirical confirmation at 3.9B scale, practical tools, the Celerity family) from what extends prior work (the role of τ from Bergsma et al., supercollapse from Qiu et al.). This would make the paper's contributions clearer and more defensible.

4. **Resolve the evaluation framing tension** by either (a) explicitly stating that the Pareto frontier comparison acknowledges the annealing confound and that Celerity's position on it despite this confound reinforces the paper's point, or (b) dropping the "problematic" language about annealing and presenting Celerity's evaluation as standard.

---

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>
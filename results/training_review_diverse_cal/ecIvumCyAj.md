Now I have all the information needed. Let me construct the final consolidated review.

## Summary

The paper proposes MoE-F, a stochastic filtering-based gating mechanism for dynamically combining pre-trained LLMs in online time-series prediction. By framing expert selection as a finite-state HMM and using the Wonham-Shiryaev filter, the method derives closed-form SDEs for optimal posterior weights (Theorem 1), which are then aggregated via Gibbs measures and updated via a perturbed transition matrix estimator. Experiments on a financial market movement task show substantial F1 improvement over individual LLM experts.

## Strengths

1. **Novel application of stochastic filtering to online MoE gating** — The paper identifies a genuine gap (static MoE gating vs. time-varying expert quality) and connects it to the Wonham-Shiryaev filtering framework. Theorem 1 provides explicit, simulation-free SDEs for each expert's posterior weight estimate, avoiding Monte Carlo sampling. This is a principled approach to a problem typically handled by heuristics or static training.

2. **Substantial empirical gains over individual experts** — Table 1 reports a 17% absolute F1 improvement (0.35 → 0.52) over the best single LLM on the NIFTY financial dataset, across a diverse set of 7 experts (Llama-2, Llama-3, Mixtral, DBRX, GPT-4o). Ablations with LoRA adapter variants (Table 2) show consistent improvements (0.28/0.36 → 0.43 F1), confirming robustness.

3. **Per-class performance decomposition reveals adaptive gating** — Table 3 shows that individual experts often collapse to one class (e.g., the "+nifty" adapter only predicts Neutral), while MoE-F achieves balanced F1 across all three labels, demonstrating that the filtering mechanism is actually doing dynamic reweighting rather than simply picking a single best expert.

4. **Plug-and-play design with theoretical support for regularization** — Algorithm 1 runs filtering in parallel and requires no expert retraining. Propositions 1 and 2 provide guarantees (invertibility, row-stochasticity, KL stability bound) for the perturbation used to regularize the transition matrix update.

## Weaknesses

### Fatal
None.

### Major

1. **The claim that the Q-update optimizes a lower bound is unsupported.** The Contributions section (line 68) states that "our gating mechanism... to update... Q... optimizes a lower bound for the expected performance of the online MoE (Theorem 1)." However, Theorem 1 contains only the filtering SDE for π_t^(n) and makes no statement about Q or any lower bound. No separate theorem, lemma, or proof is provided for this claim. The Q-update (Step 3) is described as a follow-the-leader heuristic combined with matrix perturbation and projection, which is a sensible procedure, but the paper attributes a theoretical optimality property to it without substantiation. This overclaim undermines the paper's stated contribution (II).

2. **No comparison against any ensemble or combination baseline.** The experiments (Tables 1–2) compare MoE-F only against individual LLM experts. Since the paper's central claim is that the *filtering mechanism* adds value, the experiments need to control for the benefit of *any* combination method. A uniform averaging ensemble, online Bayesian model averaging, exponential gradient weighting (Cesa-Bianchi and Lugosi, 2006), or even a static softmax over a rolling window of losses would serve as natural baselines. Without them, it is impossible to attribute the reported gains to stochastic filtering specifically rather than to ensembling in general. A 17% absolute F1 improvement over the best single expert is impressive, but it is unknown whether a simpler combiner would match or exceed this.

3. **The paper does not clearly establish whether the loss process ℓ_t^(n) satisfies the canonical Wonham-Shiryaev observation form.** The Wonham-Shiryaev filter requires the observation process to be a diffusion with drift h(w_t). The paper does derive the SDE for dL^(n) (lines 258–299) and defines helper functions A and B from its coefficients, and the innovations process normalization is given. However, the derivation skips the step of verifying that the normalized observation (dL − Ā dt)/B has the required form (unit diffusion, drift linear in the signal). A reader familiar with the framework would expect an explicit showing that the observation model maps onto the standard setup. The key connection is present in the algebra but is buried in dense notation, conditional compilation artifacts (e.g., `\ifthenelse`), and an opaque helper function section. This does not invalidate the result, but it makes the theoretical contribution harder to verify than it should be.

### Minor

1. **"Closed-form" is imprecisely used.** Theorem 1 gives an SDE, not a closed-form expression in the usual sense (e.g., like the Kalman filter recursion). The authors contrast with particle filters by noting the absence of Monte Carlo sampling, which is a meaningful distinction. However, the Euler–Maruyama discretization (Algorithm 1) introduces numerical error, and no convergence analysis or discretization bound is provided. The paper should clarify the specific sense in which "closed-form" is claimed (finite-dimensional, no sampling needed) and note the gap between continuous-time theory and discrete-time implementation.

2. **Metric computation in Tables 1–2 is under-specified.** Recall equals Accuracy in all entries, and Precision differs from Accuracy in several cases. These values are consistent with sklearn's "weighted" averaging (where weighted recall = accuracy but weighted precision ≠ accuracy in general), but the paper does not state which averaging scheme is used. This should be clarified to avoid the appearance of error. (Table 3's per-class breakdown confirms the numbers are not miscalculated.)

3. **The claim of being "the first viable online mixture of expert frameworks used in quantitative finance" (Conclusion) is overstated.** Online combination of forecasts (Bayesian model averaging, dynamic model combinations) has a long history in finance (e.g., Stock and Watson, 2004; Timmermann, 2006). While the paper's specific filtering-based approach is novel, the broader claim should be qualified.

### Trivial

- Equation (8) for P_t^α writes P_t^α = (1-α)P_t^α + αI_N, which is self-referential; the right-hand side should reference P_t, not P_t^α.
- The paper contains conditional compilation artifacts (`\ifthenelse`) and unresolved macros, which make the helper function definitions harder to follow.

## Nice-to-Haves

- Adding a comparison against uniform averaging and online exponential weighting would substantially strengthen the empirical contribution.
- Recasting the Q-update as a heuristic (or, if a proof exists, stating it explicitly as a separate theorem) would resolve the theoretical overclaim.
- A short paragraph or appendix showing the explicit mapping of dL^(n) to the Wonham-Shiryaev canonical form would improve verifiability.

## Removed Points

- **Eigenvalue condition for P_t^α (Critic Point about non-real eigenvalues):** The reviewer worried that P_t^α may have non-real eigenvalues. However, P_t^α = (1-α)1π̄^T + αI_N. For any v ⟂ π̄, P_t^α v = αv; for v = 1, P_t^α 1 = 1. So eigenvalues are {1, α, ..., α}, all real and positive regardless of α ∈ (0,1). The paper's conditional phrasing "if P_t^α has real eigenvalues" is unnecessarily conservative but not wrong; the reviewer's objection is factually incorrect for this matrix structure. **Removed.**

- **Criticism that "the paper provides no proof that ℓ_t^(n) can be written in canonical form":** Overstated. The paper explicitly computes dL^(n) in lines 258–299, identifying the drift-dependent term (involving w_t) and the diffusion term. The helper functions A and B are extracted from this SDE. The derivation is present, though dense and obscured by conditional compilation. **Downgraded to Major #3 above (a presentation issue, not a missing proof).**

- **Criticism about understanding the paper or format/typo issues:** Removed per rules.

- **Strength Finder strength about "clear differentiation from static MoE" kept**; **"theoretical guarantees for transition matrix update" kept** but relevance is limited since the Q-update optimality claim is unsupported.

## Novel Insights

The reviewers' discussion surfaces a tension that is useful for the authors: the strongest part of the paper (the Wonham-Shiryaev filtering derivation for expert weighting) is theoretically rigorous, while the weakest part (the Q-update optimality claim) is an overreach that would not be needed if the paper were framed more modestly. The follow-the-leader Q-update is a reasonable heuristic — the paper should present it as such rather than straining to attribute it to Theorem 1. Similarly, the absence of ensemble baselines is the most actionable empirical gap; the filtering contribution is distinctive enough that it would likely beat simple baselines, but the paper needs to demonstrate this directly. The per-class decomposition in Table 3 is arguably the paper's most compelling piece of evidence for true dynamic reweighting, and the authors should emphasize this more prominently rather than relying on the raw F1 improvement alone.

## Suggestions

1. Add at least one simple ensemble baseline (uniform averaging, exponential gradient weighting over a rolling window). If MoE-F outperforms these, the filtering contribution is validated.
2. Either prove the Q-update's lower-bound optimality or remove the claim. The follow-the-leader motivation is sufficient to justify the update.
3. Clarify Theorem 1's connection to the Wonham-Shiryaev canonical form in a short self-contained paragraph.
4. Specify the metric averaging scheme in Tables 1–2 (or include a note that weighted averaging is used).
5. Qualify the "first viable" claim in the Conclusion, or remove "first."

## Score and Decision

The paper introduces a genuinely novel approach — applying Wonham-Shiryaev filtering to online MoE gating — and provides a solid theoretical core (Theorem 1) supported by encouraging empirical results. However, the unsupported Q-update optimality claim and the absence of any ensemble/comparison baseline in the experiments weaken the paper's ability to deliver on its stated contributions. The core idea is promising and the primary filtering mechanism is sound, but the paper as presented does not fully substantiate its theoretical claims and does not establish that the filtering machinery outperforms simpler alternatives. A major revision could address both issues.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>
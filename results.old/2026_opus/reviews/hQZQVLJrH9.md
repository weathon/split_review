Now I have a complete view of the paper. Let me verify a few more specific concerns and then do calibration.Round 1 bracket: based on these anchors, this paper is between roughly 3.0 (Hessian-free IF, broken contribution narrative) and 5.0 (Conceptors paper, theoretical steering framework with empirical wins). The IAS paper sits closer to the lower end because: (a) its headline empirical comparison shows the method losing to the baseline (the Conceptors paper at least beats baselines), (b) it has multiple verifiable inconsistencies in theorem statements, and (c) one of its three advertised contributions (data attribution) has zero experimental evidence. Let me narrow further.# Final Consolidated Review

## Summary

The paper introduces Influence-Aligned Steering (IAS) and argues that activation steering and influence-function attribution are first-order duals — every steering vector corresponds to a signed influence measure over training data and vice versa. The contribution is largely theoretical: a duality theorem, an alignment diagnostic γ based on principal angles between Jacobian subspaces, a spectral-optimality recipe, a no-free-lunch bound, and a Rademacher generalization bound for low-rank steering. Empirical support is limited to a small GPT-2 Medium detoxification table, a linearity scatter plot, a γ-vs-layer-depth plot on GPT-2, and a ResNet-50 spectral-radius significance test.

## Strengths

- **Conceptually clean unification.** Phrasing the steering-vs-influence relationship as a primal–dual pair (Section 3) and identifying γ(x) = cos∠min(S_θ, S_h) as the single scalar that controls feasibility (Section 5.1) is a genuinely useful framing. Two previously disconnected tools are placed on a common geometric footing.
- **The alignment diagnostic γ is a self-contained, cheap contribution.** Theorem 5.1's bound √(1−γ²) on the relative steering error, computable from two small SVDs, is a defensible practical pre-check. Figure 2 (median γ from 0.64 at L0 to 0.94 at L11 on GPT-2 Medium) gives a concrete demonstration that γ behaves non-trivially across depth.
- **Generalization bound for low-rank IAS (Theorem 6.1).** A Rademacher term of αL√(2k/dn) for rank-k IAS, leading to vanishing excess risk as d, n grow, is the first generalization-style guarantee tailored to activation steering.

## Weaknesses

### Fatal
None. The conceptual core (steering–influence duality at first order, the γ diagnostic) is non-trivial and survives the criticisms. What is fatal-looking on first read (e.g., the inconsistent Eq. 2) is bounded in scope.

### Major
- **The only head-to-head empirical comparison shows IAS losing to CAA, and the paper does not acknowledge it.** Table 1: CAA reaches toxicity 0.0150 / PPL 13291, IAS reaches 0.0164 / 13701 (both worse), with CAA's numbers bolded as best. Contribution 3 ("the spectral recipe replaces hand-crafted vectors") implies IAS should outperform heuristic steering vectors; here the principled construction is beaten by the heuristic, and the text presents this as supporting evidence. The paper owes a direct discussion of why the optimality result does not translate to the only task it is tested on. Additionally, the absolute perplexities (~13–14k for GPT-2 Medium on WikiText) are several orders of magnitude above the usual ~20–30 range, which makes the numbers themselves hard to trust without clarification of the metric.
- **The data-attribution contribution has zero experimental support.** Contribution (i) in the intro and Section 4.1's "Practical payoff" claim ρ_s "pinpoints the fewest training examples to relabel/remove/examine." Section 7 contains no top-k retrieval study, no leave-one-out validation, no comparison to standard influence-function attribution. One of three advertised deliverables is wholly unevidenced.
- **Figure 1 contradicts what it is presented as confirming.** The paper writes "predicted and realized logit shifts are nearly collinear (cosine 0.978, slope 1.50)" as evidence for first-order equivalence. Cosine measures direction; the slope of 1.50 means realized shifts are 50% larger than the linear prediction — a systematic multiplicative bias, not the O(α²) scatter Corollary 2 predicts. The first-order claim is the load-bearing claim of the framework; the headline plot needs to show slope → 1 as α → 0 (or otherwise quantify the regime where the linearization is unbiased) to validate the framing.
- **Inconsistent / under-specified theorem statements.**
  - *Eq. (2):* The dual program derivation yields Δh* = J_{h→y}^⊤ λ* with λ* = −(J_{h→y}J_{h→y}^⊤)^† J_{θ→y}Δθ, i.e. Δh* = −J_{h→y}^† J_{θ→y}Δθ. The boxed formula drops both the pseudo-inverse and the sign, while Theorem 5.2 writes the correct projection form. The central construction reads differently in two places.
  - *Theorem 6.2:* "for every Δh and the corresponding Δθ, ‖J_{h→y}Δh‖/‖J_{θ→y}Δθ‖ ≤ γ(x)" is not well-formed without a normalization or matching constraint — Δh is unconstrained and the numerator can be made arbitrarily large. The informal "even an infinite-norm activation change cannot push further than factor ρ" reading requires a constraint the formal statement omits.
  - *Theorem 5.3:* Σ is an average over the training set, but the claimed maximum involves the per-input factor ‖∇_h f_θ(x)‖, the "expected first-order logit change" being maximized is not formally defined (over which distribution), and the link from a Σ-eigenvector to per-input logit shift J_{h→y}(x)s is not derived. The recipe and the formula appear to solve subtly different problems.
  - *Theorem 6.1 sketch:* "IAS changes only a rank-k submatrix of the layer weight" — IAS is defined as an activation-space additive perturbation, not a weight edit. The reduction to Pinto et al. (2024)'s low-rank-layer bound elides this step.
  - *Corollary 1 sketch:* "If another measure achieved the same shift with smaller ℓ₁ norm, one could scale ρ_s down and still match the shift" — scaling ρ_s scales the shift it produces; this is not the ℓ₁-minimality argument.
- **The "equivalence" framing is overclaimed.** The abstract states unconditional equivalence; the formal theorems either require the subspace inclusion Im(J_{θ→y}) ⊆ Im(J_{h→y}) (generically false when d ≪ P) or pay a √(1−γ²) residual that at the paper's own threshold γ ≥ 0.7 corresponds to ~71% relative error. The qualifications are buried while the framing in the abstract and conclusion ("projections of the same underlying sensitivity tensor") is unconditional.

### Minor
- **Figure 2 does not "support Theorem 5.1."** The theorem holds independently of any layer pattern; the figure shows the diagnostic is non-trivial, not that the bound is tight or empirically validated.
- **Figure 3 tests a different claim than Theorem 5.3.** Comparing spectral radius of X_c^⊤ diag(y) X_c for true vs. random labels probes whether class structure exists in the activation Gram matrix — not whether the spectral steering direction outperforms alternatives at logit shifting on actual inputs.
- **Lemma 5.4 is stated without a proof.** The right-hand identity √(1−(1−γ₁²))·√(1−(1−γ₂²)) = γ₁γ₂ is trivial; the substantive multiplicative-degradation claim relating two layers' subspaces is asserted but not derived.
- **Section 5.3's "two backward passes per input" cost claim does not extend cleanly to the spectral recipe**, which still requires (H+λI)^{−1} applied to per-example gradients and matches the cost of standard influence-function pipelines.

### Trivial
- The numbering in the abstract's contributions list and the body's labels (Contribution 3 etc.) is loose in places.

## Nice-to-Haves
- A calibration plot of γ vs. steering success across two architectures and several tasks would directly turn γ into a predictive tool, which is the paper's strongest defensible contribution.
- A leave-one-out (or Datamodels-style) verification of ρ_s: extract ρ_s from an IAS vector that suppresses a known behavior, and check that retraining without the top-ρ_s examples reproduces the effect. This is the experiment the data-attribution narrative needs.
- A scan over α showing slope → 1 as α → 0 in Figure 1 would convert the slope-1.50 finding from an awkward fact into a calibration of the regime where the first-order theory holds.
- A clean restatement of Theorem 5.3 separating (a) maximize ‖J_{h→y}(x)s‖ at fixed x and (b) maximize an expected shift over the training distribution would clarify what is being optimized.
- At least one steering benchmark beyond CAA on GPT-2 Medium where IAS is compared to contemporary steering methods.

## Removed Points
These points are flagged to be removed; treat them with caution.

- *Strength: "All quantities reduce to two JVPs per input."* Real for IAS at a fixed Δθ but not for Σ/spectral recipe; the strength is conditional and the major weakness on cost framing already covers it.
- *Strength: "first generalization guarantee for activation steering of which we are aware."* This rests on the Theorem 6.1 sketch that conflates activation perturbation with rank-k weight edit; the underlying weakness disagrees with the strength, so it is demoted.
- *Strength: "spectral optimality theorem (Theorem 5.3) ... maximizes expected first-order logit change."* The theorem statement is ambiguous about distribution and connection to per-input shift; the strength as written overstates what is established.
- *Strength: "Layer-wise composability Lemma 5.4."* Stated without proof; the substantive content is unsupported in-paper.
- *Critic claim: "deserves engagement with the broader literature on Jacobian-based attribution"* — removed per the hard rule against unverifiable missing-reference complaints.

## Novel Insights
None beyond the paper's own contributions. The paper's framing of steering and influence as primal–dual projections of a shared sensitivity tensor is genuinely a novel angle, but everything novel is already authored by the paper.

## Suggestions
- Reframe Table 1 honestly: if CAA wins, explain why (e.g., the optimality of Theorem 5.3 is for expected logit change, not for toxicity classifier scores; or the small-edit regime is not where CAA's hand-crafted direction loses).
- Sanity-check the perplexity column — either correct the numbers or specify the exact metric being reported.
- Reconcile Eq. (2) with Theorem 5.2; clean up Theorems 6.2 and 5.3 so quantities being optimized, normalization constraints, and the role of x are unambiguous.
- Add a steer→data experiment: ρ_s top-k validated against leave-one-out or Datamodels on a small task.
- Add an α-scan demonstrating slope → 1 to validate the first-order regime, and report γ alongside steering success on a multi-task suite.

## Evaluation along the requested axes

- **Originality:** Above average — the duality framing and γ diagnostic are novel.
- **Importance of the research question:** Solid — connecting steering and attribution is genuinely useful.
- **Whether claims are well supported:** Weak — the central first-order claim is contradicted by Figure 1's slope, the equivalence claim is conditional in ways the abstract hides, and one of three contributions has no experiments.
- **Soundness of experiments:** Weak — single small comparison that the proposed method loses, suspicious perplexities, vision experiment tests a different claim than the relevant theorem.
- **Clarity of writing:** Mixed — the geometric exposition is good; theorem statements are inconsistent in non-trivial places.
- **Value to the research community:** Modest — γ as a feasibility diagnostic is reusable; the rest needs more work before it can be relied on.

## Calibration

Anchors retrieved:

**Round 1 (bracketing):**
- `z1yI8uoVU3.md` (avg 3.00, Round 1, read in full) — steering evaluation framework; limited novelty and methodological gaps. Worse-than IAS on theoretical depth, comparable on empirical thinness.
- `wYVP4g8Low.md` (avg 3.00, Round 1) — Local Control Networks; not topically aligned.
- `WT2bL7sCM1.md` (avg 3.00, Round 1, read in full) — Hessian-free IF; contribution gap and weak baselines. Similar tier of problems as IAS, less ambitious theory.
- `InRaT76E2S.md` (avg 2.50, Round 1) — unrelated activation decay paper.
- `9wjGUN65tY.md` (avg 5.00, Round 1, read in full) — conceptor-based affine steering; theory + empirics that *beat* baselines. Better-than IAS on the empirical front.
- `wozhdnRCtw.md` (avg 7.00, Round 1) — instruction-following steering; broader empirics, much stronger than IAS.
- `p85TNN62KD.md` (avg 5.50, Round 1) — versatile IF for non-decomposable losses; more careful theory than IAS.
- `KjBG4JNOc2.md` (avg 6.20, Round 1) — influence measure for training robustness; much more thorough than IAS.
- `esYrEndGsr.md` (avg 8.00, Round 1) — influence functions for diffusion; out-of-reach for IAS.
- `PBjCTeDL6o.md` (avg 8.00, Round 1) — unlearning interpretations; stronger.
- `uHLgDEgiS5.md` (avg 8.00, Round 1) — trajectory-specific LOO influence; stronger.
- `AoraWUmpLU.md` (avg 8.00, Round 1) — activation functions in neural ODEs; unrelated topic but well-executed.

**Round-1 bracket:** between 3.0 and 5.0. IAS is more ambitious theoretically than z1yI8uoVU3/WT2bL7sCM1 but loses to its baseline (unlike 9wjGUN65tY).

**Round 2 (narrowing):**
- `X2gjYmy77l.md` (avg 4.00, Round 2, read in full) — controllability of LLMs as a dynamical system; ambitious theory with hand-wavy assumptions and confusing equations but no contradicting experiment. IAS is comparable in theoretical ambition; IAS has a clearer geometric picture but also a self-undermining headline experiment.
- `3iJ7eSj2rE.md` (avg 4.00, Round 2) — weak-strong LLM collaboration; not topical.
- `qKKwQvepx0.md` (avg 4.00, Round 2) — explainable steerable models; not topical.
- `fDaLmkdSKU.md` (avg 5.80, Round 2) — constrained learning; stronger and more carefully proved.
- `MY8SBpUece.md` (avg 5.50, Round 2) — non-linear feature learning theory; cleaner theoretical paper.
- `j7yeq2sOj3.md` (avg 5.00, Round 2) — flatness ↔ compression; cleaner theory.
- `eQggPqESBr.md` (avg 5.50, Round 2) — simplicity bias; cleaner theory.

**Final placement:** The closest matches in tone and execution are X2gjYmy77l (4.0, ambitious theory + confused equations + tepid empirics) and z1yI8uoVU3 (3.0, thin steering empirics). IAS has more theoretical content than z1yI8uoVU3 but has a self-undermining headline experiment that X2gjYmy77l lacks. It is clearly below the conceptors paper at 5.0 because that paper at least beats its baselines, while IAS does not. Sitting between X2gjYmy77l (4.0) and z1yI8uoVU3 (3.0), with the major weaknesses (lost headline experiment, missing attribution evidence, inconsistent theorems, slope-1.50 contradicting first-order framing) pulling toward the lower end: **3.5**.

MY FINAL SCORE: <score>3.5</score>
MY FINAL DECISION: <decision>Reject</decision>
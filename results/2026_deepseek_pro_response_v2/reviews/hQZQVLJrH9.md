Now I have a clear calibration picture. Let me write the final review.

**Round 1 Bracket:** 5.0–7.0 (between Conceptors at 5.0 and Instruction-Following Steering at 7.0)

**Round 2 Narrowing:** The paper is stronger than CONFST (5.50) in theoretical contribution but weaker than DataInf (6.00) and Diff-In (6.00) in empirical validation. The core data-tracing claim is undemonstrated.

**Final Score: 5.5**

---

## Summary
This paper establishes a first-order equivalence between activation steering and influence functions, constructing an Influence-Aligned Steering (IAS) vector that maps any parameter-space influence update to a minimum-norm activation perturbation and vice versa. The authors provide an alignment diagnostic γ(x) — the smallest principal angle between activation and parameter Jacobian subspaces — that bounds steering fidelity, a no-free-lunch result when γ is small, a spectral recipe for optimal steering directions, and a Rademacher generalization bound. Empirical validation is performed on GPT-2 Medium (detoxification, first-order equivalence, layer-depth γ) and ResNet-50 (spectral optimality).

## Strengths
- **Theorem 4.2 provides a genuinely novel closed-form duality between activation steering and influence functions.** The constructive mapping from steering vectors to signed influence measures over training data (Eq. 4), with the minimal-ℓ₁ measure in Corollary 1, unifies two previously disconnected paradigms. This is not a restatement of known results and has immediate practical implications for data provenance.
- **The alignment diagnostic γ(x) (Theorem 5.1) gives a principled, computable criterion for steerability.** The smallest principal angle between Im(J_{θ→y}) and Im(J_{h→y}) bounds the relative logit error by √(1−γ²). The no-free-lunch result (Theorem 6.2) formalizes the impossibility regime when γ is small, giving practitioners a pre-check before attempting steering — a crisp, actionable finding.
- **Empirical validation of first-order equivalence is clean and convincing (Figure 1).** Across 5000 prompt–token pairs at layer 8 of GPT-2 Medium, predicted vs. actual logit shifts achieve cosine 0.978, directly supporting the paper's central claim that the first-order theory is predictive in practice. The layer-depth ablation (Figure 2, γ rising from 0.64 to 0.94) corroborates Theorem 5.1.
- **Theorem 5.3 (Spectral Optimality) replaces hand-crafted steering vectors with a principled spectral recipe.** The top eigenvector of a Fisher-influence correlation matrix maximizes expected logit change under an ℓ₂ budget, with a power-iteration algorithm that scales to large models.

## Weaknesses

### Major
- **No empirical demonstration of data tracing, which is a core claimed contribution.** The paper claims (abstract, Corollary 1, Section 4.1) that IAS enables mapping steering vectors back to causal training examples via ρ_s — e.g., for "debugging bias or privacy leaks" (line 118). This is never tested: there is no experiment showing ρ_s identifies meaningful training examples. For a paper whose first stated contribution is "a constructive algorithm for mapping undesired behaviors back to causal training examples" (abstract, line 9), the absence of any such demonstration is a significant gap between claims and evidence.
- **Practical dependence on H^{-1} is glossed over.** The IAS construction (Section 3) and the spectral recipe (Theorem 5.3) both rely on Δθ = −ε H^{-1} ∇_θ ℓ(z,θ). Computing H^{-1} for models like GPT-2 Medium is the well-known bottleneck that has limited influence functions in practice since Koh & Liang (2017). The paper mentions damped inverses and Gauss-Newton approximations in passing but never explains how H^{-1}∇_θℓ is tractably computed for the experiments shown. The computational primitives claim (two JVP/VJP per input, line 56) only covers part of the pipeline; it omits the dominant cost.
- **The Rademacher bound (Theorem 6.1) has an unjustified connection to activation steering.** The theorem models the IAS-corrected model as f̃ = f_θ + αUV^T, treating steering as a rank-k weight matrix modification. But IAS adds a vector to activations, not to weights. The paper never derives how an activation-space perturbation translates to the UV^T form. The proof sketch merely cites Pinto et al. (2024) and asserts "IAS changes only a rank-k submatrix of the layer weight" (line 198) without establishing this equivalence.

### Minor
- **The detoxification experiment shows IAS underperforming CAA, and this is not discussed.** Table 1 shows CAA achieves better toxicity (0.0150 vs 0.0164) and better perplexity (13291 vs 13701) than IAS. The paper presents this neutrally without analysis. Since CAA is a simple contrastive heuristic while IAS is the paper's principled construction, the result warrants explanation.
- **The first-order equivalence reduces to a straightforward linear-algebra observation.** Both steering (Eq. 2) and influence (Eq. 1) produce logit shifts via linear maps. The core insight — that J_{h→y}Δh = J_{θ→y}Δθ can be solved for Δh given Δθ under image containment — follows from existing formalisms. The paper's value lies more in the geometric characterization (γ, spectral analysis) than in the equivalence itself.
- **The spectral optimality experiment (Figure 3) is minimal.** It tests only one class (horse) on one model (ResNet-50), comparing against random directions only. No comparison to existing steering methods, no demonstration that the spectral direction produces meaningful behavioral changes, and no multi-class or multi-model validation.
- **The γ diagnostic's practical value is asserted but not validated.** Figure 2 shows γ increases with depth, but no experiment demonstrates that using γ to select layers or decide steer-vs-edit actually improves downstream outcomes. The guidance "γ < 0.5 ⇒ skip steering" (line 206) lacks empirical backing.

### Trivial
- **Duplicate equation numbering.** Equation (2) is used for both the activation steering equation (line 60) and the IAS solution (line 84).

## Nice-to-Haves
- Extending empirical validation to additional model families (e.g., Llama, Mistral) and tasks beyond detoxification would strengthen generality claims.
- Demonstrating the data-tracing workflow — computing ρ_s for a steering vector and showing the top-weighted training examples are semantically relevant — would substantially strengthen the paper.
- Comparing IAS against weight-space editing methods (e.g., ROME, MEMIT) on tasks where γ is small vs. large would validate the steer-vs-edit decision framework.

## Removed Points
These points are flagged to be removed, treat them with caution.
- (None — the Harsh Critic input was empty/truncated, containing no review content to process.)

## Novel Insights
The paper's most genuinely novel insight is the geometric characterization of steerability via principal angles between Jacobian subspaces. While the first-order equivalence itself follows from linear algebra, the observation that a single scalar γ(x) — computable via two small SVDs — tightly bounds steering fidelity and determines when activation-space editing is provably insufficient (Theorem 6.2) is a crisp, actionable finding. This bridges two communities that previously operated independently and gives practitioners a principled go/no-go test.

## Suggestions
- Demonstrate the data-tracing capability with at least one qualitative example: given a steering vector that reduces toxicity, show the top-k training examples identified by ρ_s and discuss whether they are plausibly toxicity-related.
- Explain the H^{-1} computation strategy used in experiments, including any approximations (Gauss-Newton, conjugate gradient, LiSSA) and their associated costs.
- Either derive the connection between IAS activation edits and the rank-k weight modification in Theorem 6.1, or reframe the theorem as applying to a related but distinct setting.
- Discuss why IAS underperforms CAA on the detoxification task and what this implies about the practical value of the first-order framework.

## Calibration

**Round 1 (Bracketing):**
- `z1yI8uoVU3` (3.00): "Measuring Effects of Steered Representation" — rejected, evaluation framework. Our paper is substantially stronger.
- `WT2bL7sCM1` (3.00): "Revisit, Extend, and Enhance Hessian-Free Influence Functions" — rejected, weak contribution. Our paper is substantially stronger.
- `9wjGUN65tY` (5.00): "From Steering Vectors to Conceptors" — rejected, activation steering + theory. Our paper has more novel theoretical contribution and cleaner presentation. Our paper is stronger.
- `wozhdnRCtw` (7.00): "Improving Instruction-Following in Language Models through Activation Steering" — accepted, solid empirical work on activation steering. Our paper has less empirical depth. Our paper is weaker.
- `uHLgDEgiS5` (8.00): "Capturing the Temporal Dependence of Training Data Influence" — accepted, strong theory + experiments on influence functions. Our paper is clearly weaker.

**Round 2 (Narrowing):**
- `ZPkNrs6aNO` (5.50): "Effectively Steer LLM To Follow Preference via Building Confident Directions" — rejected, steering + theory with significant gaps. Our paper has more rigorous theory but comparable empirical limitations. Similar quality.
- `Jds4tiTo2a` (6.00): "Diff-In: Data Influence Estimation with Differential Approximation" — rejected, solid influence estimation with extensive experiments. Our paper has more novel theory but thinner experiments. Our paper is slightly weaker.
- `9m02ib92Wz` (6.00): "DataInf: Efficiently Estimating Data Influence in LoRA-tuned LLMs" — accepted, practical influence estimation. Our paper has more theoretical novelty but weaker empirical validation. Our paper is comparable or slightly weaker.

**Bracket:** 5.0–7.0 → narrowed to 5.5 given comparison with CONFST (5.5, similar empirical gaps but less theoretical novelty) and Diff-In/DataInf (6.0, stronger empirical validation compensating for less theoretical novelty). The paper's theoretical contributions are genuine but the empirical validation is too thin for the scope of claims made.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>
- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 5, 5, 6
Now I have a thorough understanding of the paper and can verify the reviewer claims. Let me produce the final consolidated review.

---

## Summary

This paper introduces TINY, a method that grows neural network architectures during training by detecting "expressivity bottlenecks" and optimally adding neurons to close the gap between the functional gradient and what the current architecture can express. The central contribution is a formal, computable definition of the expressivity bottleneck at each layer, together with a closed-form SVD-based solution for the input/output weights of added neurons that quantifies the expressivity gain. The method is compared to GradMax on CIFAR-100 with ResNet18 variants, showing advantages when starting from very small architectures (ResNet_{1/64}).

## Strengths

1. **Formal, computable definition of an expressivity bottleneck.** Section 3 defines Ψ^l (Equation \eqref{eq:mini_NG}) as the distance between the desired pre-activation update DV^l and the best achievable update DE^l given the current architecture. This operationalizes a notion of expressivity that can be computed from first-order derivatives, unlike mutual-information or VC-dimension based notions that are hard to estimate or do not directly guide architecture changes.

2. **Closed-form optimal neurons with quantified expressivity gain.** Proposition 2 gives an explicit SVD-based solution for the input and output weights of added neurons, with the expressivity gain quantified as Σ λ_k². This provides stronger theoretical grounding than GradMax (which only minimizes first-order loss without projecting the desired update), and avoids the redundancy issues of random kernel-based growth methods.

3. **Clear empirical advantage over GradMax from very small starts.** Table \eqref{tab:AccuracyInfiny} and Figures \eqref{fig:Pareto_WT} and \eqref{fig:TINYGradMaxgrowth} show that TINY substantially outperforms GradMax when starting from ResNet_{1/64}. For example, with Δt=0.25, TINY reaches 69.0±0.1 after extra training versus GradMax's 57.0±0.3 (Table \eqref{tab:AccuracyInfiny}), and TINY requires roughly half the extra training epochs to converge (Figure \eqref{fig:ExtraTrainingTG}). This demonstrates that the projection step matters when the initial architecture is severely under-parameterized.

4. **Ablation isolating initialization quality from gradient descent.** Section 5.2 and Figure \eqref{fig:Pareto_RT} compare TINY against random neurons with an optimal amplitude factor via line search, with no subsequent gradient descent. TINY consistently gains accuracy during growth while the random method stagnates, confirming that the derived neuron directions (not merely scaling or subsequent training) drive the expressivity gain.

## Weaknesses

### Fatal
None.

### Major

1. **Sign inconsistency in Proposition 2's loss-change formula.** Proposition 2 (line 317) states:
   ℒ(f_{θ⊕θ^{K,*}_{↔}}) = ℒ(f_θ) + (σ_l'(0)/η) Σ λ_k² + o(‖θ‖²).
   For any standard activation with σ_l'(0) > 0 and η > 0, this implies the loss *increases* when optimal neurons are added — the opposite of the method's intent. The Taylor expansion in Equation \eqref{eq:Loss_Taylor_order_1} (line 331) shows a negative sign:
   ℒ ≈ ℒ(f_θ) - (σ_{l-1}'(0))/(η n) ⟨DV^l, DE^l⟩_{Tr},
   which is the expected sign for a loss decrease. The paper claims "the expressivity gain and the first order in η of the loss improvement... are equal" — the expressivity gain (reduction in Ψ^l) is Σ λ_k², while the loss formula as written gives + (σ_l'(0)/η) Σ λ_k². These are not equal in sign or magnitude under standard conventions. This inconsistency needs resolution: either the sign is wrong, or the formula uses a nonstandard convention that must be explained.

2. **Experimental evidence is too narrow to support the abstract's broad claims.** The abstract claims to "match large neural network accuracy, with competitive training time, while removing the need for standard architectural hyper-parameter search." Each part is unsubstantiated relative to the evidence:
   - *Matching accuracy*: The best TINY result is 71.0±0.2, versus a reference ResNet18 at 72.9 — a ~2-point gap. For the more challenging s=1/64 start, the gap is 3–4 points.
   - *Competitive training time*: No wall-clock training times are reported anywhere. The method requires SVD computations at each growth step, and the overhead is not measured.
   - *Removing architectural hyper-parameter search*: The method still requires choosing the initial architecture scale (s), growth frequency (Δt), number of neurons per growth step, layers to grow, and all standard training hyperparameters.
   - Experiments are on a single dataset (CIFAR-100) with a single architecture family (ResNet18 variants) and only 2 runs per setting. This is insufficient to demonstrate generality or robustness for the breadth of claims made.

3. **Unverified claim about removing optimization issues due to thin architectures.** The Introduction (line 76–77) states the method "removes the optimization issues (local minima) that are due to thin architectures." No experiment compares TINY to training a thin network from scratch without growth for a comparable computational budget. Without such a baseline, the reader cannot tell whether the observed improvement comes from the growth mechanism itself or simply from additional training steps on a larger architecture.

4. **Decoupling existing and new parameters is acknowledged but not validated.** The transition from Equation \eqref{eq:eq_rajout} (joint optimization) to Equation \eqref{eq:probform} (decoupled) is noted as "generally not equivalent, though similar" (line 328), and the justification is deferred to the appendix. There is no empirical evidence that this decoupling is benign — no comparison between the decoupled and a jointly-optimized variant (even as an upper bound). For a method whose core contribution is optimal neuron addition, the optimality claim depends on the decoupling being reasonable, yet this is not tested.

### Minor

1. **Section 4 (greedy growth sufficiency) is not fully integrated with the algorithm.** The section proves that greedy one-neuron growth is sufficient in principle (Proposition \ref{prop:infinit}) but immediately acknowledges that finding the optimal neuron is NP-hard. The actual algorithm relies on linear correlations and may fail when these are exhausted. The paper discusses higher-order expansions and random neurons as fallbacks (lines 384–395), but neither is implemented or tested. This leaves a gap between the theoretical guarantee and the algorithm's demonstrated capability.

2. **The paper uses activations that may not satisfy the differentiability assumption.** The theoretical framework assumes differentiable σ_l with σ_l(0)=0 (line 100). ResNet18 conventionally uses ReLU, which is not differentiable at 0 and has σ'(0)=0 in the subgradient sense. For ReLU, the first-order term in Proposition 2 would vanish, leaving the loss change to higher-order terms not analyzed. The paper does not state what activation was used in the experiments or discuss how ReLU fits within the theoretical assumptions.

3. **No comparison against simply training the small network from scratch (without growth).** A baseline where ResNet_{1/64} or ResNet_{1/4} is trained from scratch for the same total compute budget as TINY's growth + extra training would disentangle the benefit of architecture growth from the benefit of more training steps on a growing architecture.

4. **No sensitivity analysis for key hyperparameters.** The paper fixes the number of neurons added per step (K), the frequency of growth (Δt — tested at only two values), and the choice of which layers to grow, without evaluating the impact of these choices or showing that the method is robust to them.

### Trivial
None.

## Nice-to-Haves

- Add at least one additional dataset (e.g., CIFAR-10 or a subset of ImageNet) and ideally another architecture family (e.g., a smaller CNN or MLP) to support the claim that the method is "generic for all architectures."
- Report wall-clock training times for TINY versus GradMax versus full-network training from scratch.
- Run 5+ seeds for each setting to improve statistical reliability.
- Add an ablation skipping the whitening step (S^{-1/2}) to measure its contribution.
- Add a dedicated limitations section.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. *"The complexity analysis is relegated to an appendix that was stripped from the review copy"* — **Removed.** The paper states the full algorithm and complexity analysis are in Appendices \ref{sec:fullalgo} and \ref{sec:complexity}. These sections exist in the original submission; they were stripped by the PDF parsing process, not omitted by the authors.

2. *"The paper offers no analysis of sensitivity to these choices"* — **Downgraded from the critic's framing.** The paper does test Δt at two values (0.25 and 1), which provides limited sensitivity information. This is kept as a minor weakness (point 4 above) rather than the stronger formulation the critic used.

3. *Strength finder's generic strengths about the problem being important* — **Removed.** The strength finder's points about the paper targeting an important problem or being well-motivated are generic and lack concrete anchoring in the paper's specific contributions.

## Novel Insights

The reviews surface a genuine tension in the paper's theoretical framing that goes beyond a simple typo. Proposition 2's loss formula has a sign that contradicts the intended loss decrease, and the relationship between the expressivity gain (reduction in Ψ^l) and the loss improvement is claimed to be equality but the formulas as written do not support this. This is not merely a presentation issue — it reflects either a missing minus sign, an unconventional definition of λ_k, or a more subtle derivation gap between Equation \eqref{eq:Loss_Taylor_order_1} (which has the correct sign) and the SVD-based formula in Proposition 2. The gap between the abstract's ambitious claims and the narrow experimental support is also noteworthy: the paper would be stronger if claims were calibrated to evidence rather than the reverse.

## Suggestions

1. **Fix the sign in Proposition 2** or explain the conventions under which the formula is correct. The most likely fix is that the loss formula should have a minus sign: ℒ(new) = ℒ(old) - (σ_l'(0)/η) Σ λ_k² + o(…). Clarify how this relates to the Taylor expansion in Equation \eqref{eq:Loss_Taylor_order_1} (line 331) and show the algebra bridging the two.

2. **Moderate the abstract and claims** to match the experimental evidence. Replace "matching large neural network accuracy" with "achieving accuracy close to that of a fixed large network" (or quantify the gap). Remove or hedge "competitive training time" unless timing measurements are provided. Replace "removing the need for standard architectural hyper-parameter search" with "reducing the burden of width hyper-parameter selection."

3. **Add a "training from scratch without growth" baseline** to isolate the benefit of the growth mechanism itself from the benefit of additional training steps.

4. **Test on at least one additional dataset** (CIFAR-10 would be minimal effort since the same codebase applies) to show the method is not dataset-specific.

5. **State the activation function used in experiments** explicitly, and discuss how ReLU (if used) fits within the theoretical framework requiring differentiable activations.

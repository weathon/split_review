## Summary

ShadowFM introduces two geometric flow matching methods — *Spherical Flow* (Riemannian flow on S²) and *Anisotropic Dirichlet Flow* (AD; probability-path flow with target/anti-target repulsion) — for learning Hamiltonian-conditional distributions of Pauli-6 classical shadows of quantum many-body states. The geometric motivation is grounded in the Bloch sphere isometry (CP¹ ≅ S²) and a clean toy experiment showing that spin-flip errors cause substantially larger observable reconstruction error than basis errors (Figure 2). The two methods together are tested against 1D TFIM, 1D Heisenberg, 2D Heisenberg, and real-time quantum dynamics benchmarks, showing improvements over flow-matching and kernel baselines in most configurations.

---

## Strengths

- **Geometric motivation is direct and well-evidenced.** Figure 2 (Section 3.1) demonstrates that spin errors (|X⁺⟩→|X⁻⟩) cause dramatically larger observable RMSE than basis errors at matched error rates, across both TFIM and Heisenberg. This directly motivates placing antipodal shadow outcomes far apart in the embedding, providing a principled foundation for both proposed methods rather than an ad hoc design choice.

- **Spherical Flow delivers consistent gains in most settings.** Tables 1, 3, 4, and 6 show that Spherical Flow improves over StatisticalFM by large margins: e.g., TFIM L=10 correlation at 100k shadows drops from 0.126 to 0.041 (Table 1), and Heisenberg L=30 correlation drops from 0.090 to 0.071 at 100k (Table 4). These are not marginal improvements.

- **AD Flow derivation is technically careful.** The anisotropic conditional probability path (Eq. 6), its associated velocity field (Eqs. 7–9), the closed-form expressions for C(xᵢ,t) and D(x̄ᵢ,t) via the continuity equation, and the reduction to standard Dirichlet flow when γ=0 are all clearly derived. The connection to prior CS-DFM work is explicit and the generalization is well-defined.

- **Phase transition dynamics captured accurately.** Figure 5a–b shows that Spherical and AD flow accurately track the derivative discontinuity in ZZ correlation and entanglement entropy near the TFIM critical point (c ≈ 0.5), while LinearFM and StatisticalFM visibly fail to capture the correct derivative, supporting the claim that geometric awareness helps in physically critical regimes.

- **Scaling with training data.** Figure 5c shows that ShadowFM variants exhibit superior scaling with M_train compared to baselines, matching the exact oracle scaling trend while maintaining lower absolute error — a practically important property.

---

## Weaknesses

### Fatal
None.

### Major

- **Spherical Flow regresses on TFIM L=30 correlation at high shadow count, with no discussion.** Table 2 shows Spherical achieving correlation RMSE of 0.153 at 100k generated shadows, compared to StatisticalFM's 0.120 — a 28% regression on the most data-rich setting for the larger chain. This directly contradicts the abstract's claim that "geometric consideration leads to more faithful sampling of shadows and more accurate prediction of observables." The paper contains zero discussion of this result. Critically, Spherical does improve on entropy for the same setting (0.069 vs. 0.125 for StatisticalFM), suggesting the failure is specific to correlation estimation, which warrants mechanistic analysis (e.g., whether concentrated shadow distributions near the phase transition interact poorly with the cross-polytope prior or the geodesic interpolation). Leaving a prominent failure case in Table 2 unaddressed weakens credibility.

- **AD Flow shows catastrophic failure on quantum dynamics entropy, undiscussed.** Table 5 (real-time Heisenberg evolution) shows AD entropy RMSE of 0.389/0.302/0.288 at 1k/10k/100k, compared to Spherical at 0.195/0.179/0.177 and StatisticalFM at 0.224/0.195/0.191. AD is over 60% worse than Spherical on entropy in this setting and barely better than the worst classical baselines. No explanation is given. The paper presents AD as a peer alternative to Spherical throughout, but this 63% gap at 100k is not a rounding artifact — it is a structural failure for this method in one of the paper's own benchmark settings.

- **Oracle hyperparameter selection for AD inflates reported results.** Section 4.1 explicitly states: "For our AD flow, we evaluate for γ ∈ {0, 0.05, 0.1} and report the best value." This means every AD entry in every table reflects test-set model selection, not a held-out evaluation. Section 3.2.2 describes γ as a "hyperparameter" set to 0.1, but the protocol in Section 4.1 contradicts this by selecting it post hoc from the test set. The gap between the "best γ" protocol and a fixed γ=0.1 protocol is unknown but could be non-negligible, particularly in settings where AD appears to just barely surpass Spherical (e.g., Table 4, Heisenberg L=30 at 100k: AD 0.066 vs Spherical 0.071 — a 0.005 margin that oracle selection could artificially inflate).

### Minor

- **No principled guidance for method selection.** The two proposed methods trade off across settings in an unpredictable pattern: AD wins on TFIM L=10 correlation, Spherical wins on TFIM L=10 entropy, Spherical wins on Heisenberg correlation and entropy, Spherical wins badly on quantum dynamics entropy while AD is competitive on correlation. A practitioner encountering a new Hamiltonian has no guidance on which method to use. Even a brief ablation or heuristic would help.

- **Inference cost absent.** The conclusion acknowledges that AD flow "requires precomputation of conditional velocity field involving integrals" as overhead at inference initialization, but no wall-clock or FLOPs comparison is reported. Given that inference cost directly affects practical usability — which is a stated motivation — this omission is notable.

### Trivial

None.

---

## Nice-to-Haves

- A targeted analysis of the Spherical Flow failure on TFIM L=30 correlation across coupling constant c — especially near the critical point c ≈ 0.5 — would be the most valuable addition. If the empirical shadow distribution becomes concentrated near a small subset of the octahedron vertices near the phase transition, geodesic interpolation could introduce artifacts; plotting the learned vs. true shadow marginals as a function of c would directly test this hypothesis.

- Replacing the test-set γ sweep for AD with a fixed γ (as already stated in Section 3.2.2) and separately reporting sensitivity curves would improve evaluation honesty without sacrificing reader insight into the repulsion coefficient's role.

- Experiments at larger 2D system sizes (e.g., 6×6) where DMRG becomes genuinely costly would strengthen the practical motivation for the approach; the authors mention this as future work, which is appropriate.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"Missing train/test protocol in main text" (harsh critic):** Section D specifying the train/test split is in the appendix, which has been stripped from the parsed text. The harsh critic notes this as a main-text gap, but this is an appendix-stripping artifact, not a true omission. Removed per the hard rule on absent appendix content.

- **"Cross-polytope prior choice is unjustified" (harsh critic, minor):** This is a valid precision question about the prior for Spherical Flow, but since the paper cites Cheng et al. (2024) as the motivation for this prior and the sensitivity to the prior is not shown to affect the main results, this is a speculative concern without a concrete anchor in the tables.

- **Strength Finder: "Phase transition captured faithfully while LinearFM/StatisticalFM fail":** Partially valid, but Figure 5 caption notes "While LinearFM and StatisticalFM fail to accurately capture the phase transition (abrupt change of derivative), DirichletFM and our spherical and AD flow succeed in accurately estimating them." The claim about StatisticalFM failing is in the main text. Kept as supporting context but not listed as a standalone strength because the paper's own tables show StatisticalFM performs comparably or better in some settings.

- **Strength: "Applicability to tetrahedral POVM" (Strength Finder):** Table 7 is referenced in Section 4.5 but the parsed text only contains the mention, not the table (appendix stripped). The qualitative claim of efficacy is reasonable, but numeric support is not verifiable from the main text. Retained as a note but not as a primary strength with specific evidence.

---

## Novel Insights

The paper's most genuinely novel observation — verified by the toy experiment in Figure 2 — is that the *type* of shadow error matters disproportionately: spin-flip errors (across the Bloch sphere) are an order of magnitude more harmful for observable reconstruction than basis-flip errors (within the same hemisphere), independent of the physical model. This asymmetry is not merely a motivation device; it constitutes a previously underappreciated structural fact about classical shadow estimation that directly implies embedding or transport designs should respect antipodal distance on S². The anisotropic Dirichlet flow framework (Eqs. 6–9) is a technically clean generalization of the Dirichlet flow that could find applicability in any discrete generative modeling problem where data elements have natural "anti-target" pairings — this pairing structure extends well beyond quantum shadows.

---

## Suggestions

1. **Address the TFIM L=30 Spherical regression explicitly.** Plot the Spherical vs. AD vs. StatisticalFM correlation RMSE as a function of coupling constant c near the critical point for L=30. This will likely reveal whether the failure is localized to c ≈ 0.5 (phase transition regime with concentrated shadow distributions) and make the current Table 2 results interpretable.

2. **Fix the AD evaluation protocol.** Use a fixed γ=0.1 for all tables (as described in Section 3.2.2) and add a single supplementary figure showing RMSE vs. γ for one representative setting. This turns an evaluation weakness into a strength.

3. **Provide a brief explanation of the Table 5 AD entropy failure.** Even a one-sentence hypothesis in the limitations paragraph would acknowledge that the result is known and prompt a future investigation, rather than leaving readers to wonder whether it was noticed.

4. **Report computational overhead.** Add a table or footnote comparing inference time of AD (with integral precomputation) vs. Spherical vs. StatisticalFM for a fixed system size. The conclusion already flags the cost; make it quantitative.

---

## Score and Decision

**Originality:** Solid — applying RFM on the Bloch sphere and introducing anisotropic Dirichlet flow for paired discrete data are both technically original contributions, even if both build directly on well-established frameworks.

**Importance:** Moderate — the work is useful for the quantum ML/shadow tomography community and the anisotropic Dirichlet flow could find broader applications in discrete generative modeling with paired structures.

**Claims supported:** Partially — the claim of "more faithful sampling across the board" is not uniformly supported (Table 2 Spherical regression, Table 5 AD entropy); the AD numbers are reported under oracle hyperparameter selection.

**Soundness:** Mostly sound — the method derivations are correct and the evaluation is thorough across multiple settings; the soundness is weakened by the evaluation protocol for AD and unexplained failure modes.

**Clarity:** Good — the paper is well-organized, figures are informative, and the mathematical derivations are clearly presented.

**Community value:** Moderate — provides a useful geometric framework for quantum state generative modeling that is likely to be extended.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>4</originality>
<importance>3</importance>
<claims_supported>3</claims_supported>
<soundness>3</soundness>
<clarity>4</clarity>
<community_value>3</community_value>
</subscores>
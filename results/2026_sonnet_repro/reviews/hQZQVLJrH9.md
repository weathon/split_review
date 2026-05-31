Now let me run calibration searches to anchor the score.Round 1 bracket: **3.0 – 5.5**. The conceptor paper (5.0, rejected) outperforms CAA empirically while IAS does not; the instruction-following paper (7.0, accepted) has more practical scale and demonstrated benefit. Let me narrow.Now I have enough information. Let me write the final consolidated review.

---

## Summary

This paper proposes **Influence-Aligned Steering (IAS)**, a framework that formally unifies activation steering and training-data influence functions via a shared first-order linearization. The core result (Theorem 4.2) asserts a constructive duality: any steering vector can be represented as a signed measure over training data, and any influence re-weighting maps to a steering vector inducing the same first-order logit shift. The paper also introduces a scalar diagnostic γ(x) — the cosine of the smallest principal angle between activation-reachable and parameter-reachable logit subspaces — as a feasibility certificate for when steering can substitute for influence.

---

## Strengths

- **Constructive steering–influence duality (Theorem 4.2, Eq. 4):** The mapping from any steering vector (αs) to a signed measure ρ_s over training data is constructive and closed-form. The converse direction (any influence re-weighting to a steering vector of matching ℓ₂ norm) is also explicit. This is a genuine conceptual contribution — prior work treated these two paradigms as orthogonal, and the first-order bridge is novel and clean.

- **The γ(x) diagnostic (Section 4.2, Figure 2):** The cosine of the smallest principal angle between Im(J_{h→y}) and Im(J_{θ→y}) is a computable, theoretically grounded feasibility check. Figure 2 concretely shows median γ rising monotonically from 0.64 at layer 0 to 0.94 at layer 11 on GPT-2 Medium, giving practitioners actionable layer-selection guidance ("pick the smallest layer with γ ≥ 0.7"). The alignment bound (Theorem 5.1) and no-free-lunch result (Theorem 6.2) together give a rigorous impossibility certificate when alignment is poor.

- **Generalization bound for low-rank IAS (Theorem 6.1):** The Rademacher complexity increase due to a rank-k IAS intervention is bounded by αL√(2k/dn), which vanishes with layer width d and sample size n. This gives formal grounding to the recommendation to use modest rank and magnitude.

---

## Weaknesses

### Fatal

- **Corollary 1 proof is logically incorrect.** The ℓ₁-minimality claim states that ρ_s with ‖ρ_s‖₁ = |α| is the unique minimum-norm measure reproducing the first-order logit shift. The proof sketch (lines 122–128) reads: "If another measure ν achieved the same shift with smaller ℓ₁ norm, one could scale ρ_s down and still match the shift, contradicting the definition of α as the steering magnitude." This argument is circular and wrong: scaling ρ_s by c < 1 scales the logit shift proportionally (the map is linear), so a scaled-down ρ_s does *not* reproduce the same shift. The affine-independence assumption is stated at the top of the corollary but is never used in the proof sketch. Under affine independence the decomposition might be unique (making minimality trivial), but that argument is entirely absent. As written, the proof of the key corollary is broken.

### Major

- **IAS is strictly dominated by CAA on both metrics in Table 1, with no explanation offered.** Table 1 shows CAA achieves toxicity 0.0150 and perplexity 13,291 on the detoxification task, while IAS achieves 0.0164 and 13,701 — both worse, with identical ℓ₂ magnitude and layer. IAS is presented as a *principled improvement* over hand-crafted steering (e.g., CAA); it failing to outperform CAA on the only language-model task is not a detail — it directly undermines the practical motivation. The paper offers zero diagnosis: is the gap due to the 50-example contrastive set being too small to build a reliable influence signal? The Gauss-Newton Hessian approximation being too crude? Layer 8 being suboptimal (γ = 0.64 at early layers)? None of these is explored, and a "proof of concept" that strictly loses on all metrics to the method it was designed to improve is an internal coherence problem.

- **The slope of 1.50 in Figure 1 indicates the first-order regime is not as tight as the framework assumes.** Section 7.2 reports cosine = 0.978 between predicted and actual logit shifts, and the paper calls this "consistent with the expected linear regime." But the slope is 1.50 — actual logit shifts are systematically 50% larger than first-order predictions. For a paper whose entire theoretical machinery rests on a first-order Taylor approximation being tight, a 50% magnitude underestimate is a material sign that second-order effects are significant at the perturbation magnitudes used in the experiment. The high cosine confirms good *direction* alignment, but magnitude matters for the quantitative guarantees (Corollary 2's O(α²) bound is cited without reporting α or showing the bound is tight).

### Minor

- **The "equivalent" framing in the abstract overstates the scope.** The abstract states "to first order, these techniques are equivalent" without qualification. The body correctly introduces the feasibility condition Im(J_{θ→y}) ⊆ Im(J_{h→y}) as Assumption (i) in Section 2 ("when stated"), and Eq. 3 bounds the irreducible residual when spans don't match. But at layer 0, median γ = 0.64, meaning the squared fraction of logit variation reachable by steering is only ~41%. Equivalence is very much conditional; the abstract should say so.

- **The ImageNet experiment (Section 7.4) compares only against random directions.** That the spectral direction from Theorem 5.3 lies far in the tail of the null distribution of random directions (z = 3.55, p = 0.005) confirms it is non-random — but non-randomness was never in doubt. The experiment does not compare to CAA-style contrastive directions, mean-difference directions, or any existing vision steering method, so it validates little beyond internal consistency.

- **Scale is limited to GPT-2 Medium (345M), yet the paper asserts the method "scales to billion-parameter models."** Section 1 (contribution 4) and Section 2's computational cost model both assert the approach scales to billion-parameter models via JVP/VJP primitives. This is plausible in principle, but no experiment at any larger scale (even 1B) is reported. The γ monotone-increase behavior, and whether IAS vs. CAA results hold, is entirely unexamined at scale.

### Trivial

None surviving filtering.

---

## Nice-to-Haves

- **Ablation of why IAS underperforms CAA:** Show whether increasing the contrastive set size (beyond 50 examples) or improving the Hessian approximation closes the gap. This would either diagnose the issue or reveal a more fundamental limitation.

- **Empirical validation of the steering → attribution claim (Corollary 1):** Insert a known-causal training document to induce a specific behavior, apply the ρ_s mapping, and check whether ρ_s recovers that document in its top weights. Without this, the data-provenance claim is purely theoretical.

- **Study of γ at larger scales (7B+):** The monotone increase of γ with depth on GPT-2 Medium is interesting, but whether it generalizes to larger models and different architectures is unknown and practically important.

- **Discussion of influence function fragility (Basu et al., 2021):** The paper cites this work in the reference list. IAS inherits the faithfulness of influence-function estimates; if influence scores are fragile in deep networks, the steering directions derived from them may be unreliable. Acknowledging and scoping this limitation would strengthen the paper.

---

## Removed Points

*These points are flagged as removed — treat them with caution as they may not reflect paper problems.*

- **"Primal–dual framing inflates the contribution" (Section 3):** The critic argues calling the pseudoinverse projection a "primal–dual pair in the convex-analysis sense" is inflationary. Removed — packaging a well-known optimization structure in a new context is legitimate presentation.

- **"Lemma 5.4 equality case is tautological":** The critic notes √(1−(1−γ₁²))√(1−(1−γ₂²)) trivially simplifies to γ₁γ₂. True algebraically, but the lemma's useful content is the multiplicative compounding bound γ₁₂ ≥ γ₁γ₂; the equality rewrite is for notational transparency. Removed as nitpick.

- **"Theorem 6.2 (No-Free-Lunch) is a trivial consequence of the definition of γ":** While the result is not mathematically deep, formally packaging it as a theorem with a consequence for practice ("skip steering when γ is small") is a legitimate contribution to clarity. Removed.

- **"The Spectral Optimality result (Theorem 5.3) is just the standard spectral norm bound":** This is partially true — the result is an application of known spectral theory — but the Fisher-influence matrix Σ and the power-iteration recipe are new derivations specific to this context. Weakened to nice-to-have acknowledgment.

- **"Strength: minimal-ℓ₁ data re-weighting from Corollary 1":** Removed from strengths because the proof of Corollary 1 is broken; the result cannot be credited as a clean strength until the proof is fixed.

- **"Strength: first-order equivalence verified at scale (cosine 0.978)":** Weakened — the slope = 1.50 means magnitude errors are substantial even if directionality is good, contradicting the framing of "remarkably accurate."

---

## Novel Insights

The most genuinely novel observation in this paper — and the one most deserving development — is γ(x) as a layer-selection and feasibility diagnostic that is both theoretically grounded (Theorem 5.1, Theorem 6.2) and empirically observable (Figure 2). The monotone increase with layer depth in GPT-2 Medium is an interesting empirical regularity. If this pattern is universal and its relationship to steering fidelity (not just first-order prediction but downstream task performance) can be established, γ would constitute a principled and computationally cheap tool for deciding when activation steering suffices versus when weight-level editing is necessary. The steering → data attribution direction (Theorem 4.2, Corollary 1), once its proof is corrected, also offers a novel practical workflow if validated end-to-end on a causal example.

---

## Suggestions

1. **Fix the proof of Corollary 1.** The scaling argument is wrong. Under the stated affine independence assumption, the decomposition in Eq. 4 may be unique — if so, state and prove this, which then makes ℓ₁-minimality trivial. If uniqueness does not hold, identify the correct argument.

2. **Diagnose the IAS vs. CAA gap in Table 1.** Run ablations varying: (a) the size of the contrastive training set (50 → 200 → 500 examples), (b) the Hessian approximation quality, (c) the layer index. Show whether the gap closes and under what conditions.

3. **Report both cosine AND slope for the first-order validation.** The current framing emphasizes cosine = 0.978 as success while glossing over slope = 1.50. Report both as meaningful, and discuss what perturbation magnitude keeps the slope within, say, 10% of 1.0.

4. **Add a causal attribution experiment.** Insert a synthetic document that induces a specific behavior, apply the ρ_s mapping, and verify recovery. This would transform Corollary 1 from pure theory to validated claim.

5. **Evaluate γ on at least one larger model (e.g., Llama-7B).** Even a single-model probe would substantiate the "scales to billion-parameter models" claim.

---

## Score and Decision

**Anchors retrieved:**

| Path | Avg Score | Round | Comparison |
|---|---|---|---|
| z1yI8uoVU3.md (Measuring steered representations) | 3.0 | R1 | Weaker: narrow evaluation focus, no theory |
| qJkCEcd50n.md (Influence manipulations) | 3.0 | R1 | Weaker: adversarial influence framing, no duality |
| WT2bL7sCM1.md (Hessian-free influence) | 3.0 | R1 | Weaker: incremental influence-function work |
| 9wjGUN65tY.md (Conceptor steering) | 5.0 | R1 | Similar: theoretical framework for activation steering; outperforms CAA; no proof errors |
| wozhdnRCtw.md (Instruction-following steering) | 7.0 | R1 | Stronger: multi-model empirical validation, clear practical gain |
| esYrEndGsr.md (Influence for diffusion models) | 8.0 | R1 | Much stronger: thorough empirical validation, new benchmark |
| uHLgDEgiS5.md (Trajectory-dependent influence) | 8.0 | R1 | Much stronger: novel problem formulation, strong theory + experiments |
| PBjCTeDL6o.md (Unlearning-based interpretation) | 4.6 | R2 | Similar tier: novel approach, limited validation |
| yeEWZ8qvlS.md (Signal vectors / interpretable directions) | 5.0 | R2 | Similar: interpretable direction discovery, mixed experimental results |
| N0MnPLK6r7.md (GNN interpretability unified) | 4.0 | R2 | Similar tier: unified framework, weak empirical support |
| R9W6fFlr8W.md (Primal-dual image reconstruction) | 5.0 | R2 | Less relevant topic; similar execution quality |

**Round 1 bracket:** 3.0 – 5.5.

**Round 2 narrowing:** The most directly comparable paper is the conceptor steering paper (9wjGUN65tY, 5.0, rejected). That paper also proposes a principled theoretical framework for activation steering, but it (a) empirically outperforms CAA on benchmarks, and (b) has no identified proof errors. The paper under review is *weaker* on both counts: IAS loses to CAA in Table 1, and Corollary 1's proof is broken. The signal vectors paper (yeEWZ8qvlS, 5.0, rejected) is lower-quality theoretical work with no proof errors. Given that the paper under review is below the 5.0 anchor on execution quality, and closer to the 4.0 anchor (N0MnPLK6r7) on "unified framework with insufficient empirical grounding," I place it at **4.0**.

The theoretical duality idea is genuinely novel and the γ diagnostic has real value, preventing a collapse to 3.0. But the incorrect proof of the paper's key practical corollary and the unexplained experimental failure of IAS vs. CAA are not cosmetic issues — they undermine both the formal and empirical claims of the paper.

**Originality:** Moderate-high — the first-order duality between steering and influence is a new conceptual connection.  
**Importance of research question:** High — connecting interpretability tools is practically valuable.  
**Claims supported by evidence:** Weak — core corollary proof is broken; main experiment shows the method loses to its comparator.  
**Soundness of experiments:** Below acceptable — limited scale, weak baselines in ResNet experiment, no explanation for CAA outperforming IAS.  
**Clarity of writing:** Good overall, though the abstract overstates scope.  
**Value to research community:** Moderate potential, not realized in current form.

**Decision: Reject**

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>
Now I have all the information needed. Let me synthesize and write the final review.

## Calibration Anchor Summary

**Round 1 — Topic-anchored (discrete diffusion test-time scaling):**
- Low band (<3.5): W4djmqKZC6 (3.0, Reject), JJH7m9v4tv (3.0, Reject) — weak papers with unclear contributions and poor experiments.
- Mid band (3.5–7.5): XsgHl54yO7 (6.5, Accept) — discrete guidance framework, broad evaluation; Ombm8S40zN (6.25, Accept) — DDPP for steering masked diffusion; 2fgzf8u5fP (3.8, Reject) — SVDD, rejected for inconsistent α setting and biased approximations; Hpu3KIX8Am (4.0, Reject) — Dreamguider, limited novelty.
- High band (>7.5): xDrFWUmCne (8.0, Accept), OlzB6LnXcS (8.0, Accept) — stronger papers with tighter evaluation and clearer claims.

**Round 1 — Weakness-anchored:**
- "no error bars": V163iNHVi7 (3.5, Reject) — poor presentation; vxBvr5ZpIu (5.5, Reject) — mixed reviews but ultimately rejected; CKqiQosLKc (3.75, Reject).
- "NFE metric limitation": Qyp3Rni2g1 (5.25, Reject), nXV3C8aKxZ (4.5, Reject), LxruQOI93v (5.0, Reject).
- "MCMC kernel not validated": l9GaXJnMJ8 (4.67, Reject), V163iNHVi7 (3.5, Reject), Va2IQ471GR (5.0, Reject).

**Round 2 — Narrowing (4–7.5):**
- MJNywBdSDy (5.75, Accept) — "Discrete Diffusion with Planned Denoising," most comparable: discrete diffusion method paper with novel planner-denoiser decomposition, accepted despite clarity and experimental questions.
- pq1WUegkza (7.0, Accept) — theoretical paper on discrete diffusion convergence, stronger theory focus.
- 0FbzC7B9xI (6.6, Accept) — iterative refinement for diffusion sampling, clean evaluation.
- wYmcfur889 (6.0, Reject) — data prediction denoising, rejected despite decent score.

**Round 1 bracket:** 4.0–6.5 (the paper is clearly stronger than the low-band papers scoring 3.0, but has notable weaknesses compared to the 6.5 anchor XsgHl54yO7)

**Round 2 narrowing:** The paper is close to MJNywBdSDy (5.75, Accept) in scope and quality — both propose new discrete diffusion sampling methods, both have some experimental gaps. The paper under review has stronger theoretical grounding (MTM convergence) and broader evaluation (2 language + 1 image backbone vs 1 language + 1 image), but the no-error-bars issue and NFE tension are more salient weaknesses than what MJNywBdSDy faced. I would place IterRef slightly below the 6.25–6.5 anchors (XsgHl54yO7, Ombm8S40zN) which had cleaner evaluation narratives, and slightly above or at the 5.75 anchor. Final score: **5.5**.

**What the low-band papers failed at:** Unclear/weak contributions, poor presentation, missing experiments, unsupported claims. The paper under review does NOT share these failures — its contribution is clear, the experiments are broad, and the presentation is adequate. This supports a score clearly above the 3.0–4.0 range.

Now the final review.

---

A note on the removed points: I need to carefully decide what to remove from both the Harsh Critic and Strength Finder inputs.

**From the Harsh Critic:**

Point 1 (no error bars) — KEEP as Major. Verified from the paper: no variance reported anywhere.

Point 2 (NFE tension with 8× claim) — KEEP as Major. The paper explicitly says "aggregating these into a single NFE value may obscure meaningful differences" (Section 3.3) and then uses NFE to claim "8× faster" (Section 4.2). Verified.

Point 3 (MCMC kernel not validated) — Move to Minor. The harsh critic overstates this. The denoising from x_s to x_t is done step-by-step (s-t steps), which IS in the model's training distribution (the model is trained for one-step denoising at all noise levels). The concern about distribution mismatch between re-noised states and forward-process states is a reasonable gap but not a fatal methodological flaw. I'll keep it but downgrade to Minor.

Section 4.2 post-hoc rationalization — This is a very minor point. The paper says BoN wins on CoLA because "LLaDA already generates linguistically well-formed text." This is speculative but it's presented as a plausible explanation, not a strong claim. I'll include this as part of a Minor weakness about speculative explanations.

**From the Strength Finder:**

Strength 1 (theoretical convergence) — KEEP. Proposition 1 is specific and grounded.

Strength 2 (consistent empirical improvements) — KEEP but with caveat about error bars. The evidence is in Figure 2 and Table 1.

Strength 3 (low compute effectiveness) — KEEP. Specific numerical claims.

Strength 4 (timestep analysis insight) — KEEP. Table 2, genuine insight.

Strength 5 (k vs N analysis) — KEEP. Table 3, clean ablation.

Strength 6 (practical efficiency) — This is somewhat borderline. The balancing function simplification IS a genuine technical contribution (makes MTM tractable). The pool reuse is more of an engineering detail. I'll keep it but frame it as part of the method contribution rather than a standalone strength.

Let me now write the full review.## Summary

This paper proposes IterRef, a test-time scaling method for discrete diffusion models that uses Multiple-Try Metropolis (MTM) with noising-denoising transitions to iteratively refine intermediate states toward reward-aligned distributions. The key technical contribution is the choice of a balancing function that simplifies the MTM importance weights to uniform and the acceptance ratio to a simple \(\min(1, \exp(\Delta r/\alpha))\), making the framework tractable. The method is evaluated on two language backbones (MDLM, LLaDA-8B) and one image backbone (MaskGIT) across multiple reward functions, consistently outperforming baselines (BoN, SoP, SVDD, FK). The paper also provides a convergence guarantee (Proposition 1) and ablation studies showing that later denoising steps benefit most from refinement and that iterative refinement (increasing \(k\)) is more valuable than adding more particles (increasing \(N\)).

## Strengths

- **Principled MCMC framework with tractable acceptance rate.** The derivation of the balancing function \(\lambda\) that yields uniform proposal weights and a simple reward-difference acceptance ratio (Eq. 3) is the strongest technical contribution. It makes MTM practically viable for discrete diffusion without expensive auxiliary computations, which is a genuine advance over heuristic guidance methods.

- **Convergence guarantee.** Proposition 1 provides a theoretical guarantee that the MTM chain converges to the optimal reward-aligned distribution \(p^*(x_t)\), placing the method on firmer footing than existing heuristic approaches to discrete diffusion guidance.

- **Consistent empirical improvements across diverse settings.** IterRef outperforms all baselines on every task and backbone tested — MDLM + 4 tasks (Figure 2a), LLaDA-8B + 4 tasks (Figure 2b), MaskGIT + CLIPScore (Table 1), and detoxification (Figure 5). The advantage holds across compute budgets, from very low (2T NFE) to high (32T NFE).

- **Well-designed ablations provide genuine insights.** The timestep analysis (Table 2) showing that later denoising steps benefit most from refinement — opposite to continuous diffusion — is a non-obvious finding. The \(k\) vs \(N\) study (Table 3) cleanly demonstrates that iterative refinement is more valuable than adding more particles at fixed compute, directly validating the core design choice.

## Weaknesses

### Major

1. **No variance or statistical significance reporting across all experiments.** Every quantitative result — the main scaling curves (Figure 2), MaskGIT table (Table 1), timestep analysis (Table 2), \(k\) vs \(N\) study (Table 3), and detoxification results (Figure 5) — is reported as a single point estimate with no error bars, standard deviations, or confidence intervals. The paper generates 300 samples per setting (15 prompts × 20 samples), which is sufficient for meaningful variance estimates. Without any measure of uncertainty, the reader cannot distinguish systematic improvements from noise, which undermines the empirical basis for comparative claims like "consistently outperforms" and "far surpassing."

2. **Tension between the headline efficiency claim and the metric used to support it.** The paper's prominent "8× faster" claim (abstract, Figure 1b, Section 4.2) is quantified entirely by NFE (number of function evaluations). Yet Section 3.3 explicitly states that aggregating generative-model and reward-model calls into a single NFE value "may obscure meaningful differences" because the cost structure differs across models (e.g., LLaDA-8B vs MDLM). A precise "8×" arithmetic claim (4T vs 32T NFEs) made with a metric the paper itself warns is potentially misleading for this exact comparison creates an internal inconsistency. The wall-clock analysis is relegated to the stripped appendix, so the main paper's efficiency claims rest on unresolved ground.

### Minor

3. **Validity of the noising-denoising kernel is not empirically examined.** The transition kernel \(K(x_t, x_t') = \sum_{x_s} q(x_s|x_t) p_\theta(x_t'|x_s)\) re-noises a clean intermediate state \(x_t\) to \(x_s\) and then denoises back. While the step-by-step denoising from \(s\) to \(t\) operates within the model's training distribution (one-step denoising at each noise level), the distribution of re-noised intermediates \(x_s\) may differ from the forward-process \(x_s\) the model was trained on. The paper provides no analysis or empirical validation that the kernel produces reasonable proposals. This does not invalidate the method — the MTM framework still provides convergence guarantees under the reversibility assumption — but it is a gap the authors should address.

4. **Speculative explanation for a failure case without supporting evidence.** When BoN outperforms IterRef on CoLA with LLaDA-8B, the paper attributes this to "LLaDA already generates a linguistically well-formed text, making reward-guided corrections on unstable intermediate states less effective" — a post-hoc rationalization without any supporting analysis (e.g., comparing intermediate state quality, reward model informativeness, or running controlled ablations). This is a minor point but weakens the empirical narrative.

5. **Limited discussion of reward over-optimization.** Given that the method explicitly maximizes rewards through iterative refinement, there is no analysis of whether generations degenerate or become adversarial at high compute budgets, which is a known concern in reward-guided generation.

### Trivial

None.

## Nice-to-Haves

- Add error bars / standard deviations to all figures and tables (highest priority).
- Either move wall-clock timing into the main paper to support the efficiency claim, or re-scope the claim to "up to 8× reduction in NFE" with clear caveats.
- Empirically validate the noising-denoising kernel (e.g., compare denoised samples from re-noised vs. original intermediates, or analyze proposal acceptance rates).
- Include a study of over-optimization / reward hacking as compute increases.
- Ablate the noise level \(s\) in the transition kernel (how many steps back to noise before denoising).

## Removed Points

These points from the inputs were filtered; they should be treated with caution:

- **"Methodological Gap — no guarantee p_θ produces reasonable conditional distributions on re-noised latents"** (Harsh Critic #3): Downgraded from implied fatal to Minor (see Weakness #3 above). The step-by-step denoising from \(s\) to \(t\) is within the model's training distribution. The concern about distribution mismatch is legitimate but not a fundamental invalidation — many MCMC methods operate under similar assumptions without individual empirical validation of the kernel.
- **"Writing quality / clarity"** critiques: No significant presentation issues found upon reading the paper; the writing is adequate by venue standards.
- **Reproducibility concerns** about missing appendix content: The parser strips appendix content; these exist in the original submission.
- **"Missing related works"**: Cannot be verified without external knowledge.
- **Strength Finder's "practical efficiency measures"** (balancing function, pool reuse): These are part of the method contribution, but framing them as independent strengths risks double-counting what is already captured by the tractable acceptance rate contribution.

## Novel Insights

The observation that later denoising timesteps (near \(0.1T\)) are the most important for refinement in discrete diffusion (Table 2) — contrasting with continuous diffusion where early steps determine content — is a genuinely novel and non-obvious finding. Combined with the demonstration that iterative refinement (\(k\)) beats particle count (\(N\)) at fixed compute (Table 3), these insights suggest that the community should think differently about test-time scaling for discrete vs. continuous diffusion models.

## Suggestions

1. **Add error bars to all quantitative results.** Bootstrap 95% confidence intervals or standard deviations across the 300 generations per setting. If the trends in Figure 2 and Table 1 hold with proper variance reporting, the paper's case becomes substantially stronger.
2. **Resolve the 8× claim.** Either: (a) move the wall-clock timing analysis into the main paper and base efficiency claims on actual runtime, or (b) add a clear justification that NFE is an appropriate proxy for the specific models and settings used (e.g., arguing that generative-model calls dominate the cost for the backbones tested), or (c) re-scope to "up to 8× reduction in NFE" with explicit caveats about the metric's limitations.
3. **Validate the transition kernel empirically.** A simple experiment — denoising re-noised intermediates at various \(s-t\) offsets and comparing the distribution of \(x_0\) predictions or acceptance rates — would directly address the kernel validity concern.
4. **Add a reward over-optimization analysis.** Show that diversity / naturalness of generations does not collapse as \(k\) or compute increases. The current KL regularization term \(\alpha\) provides theoretical protection, but empirical verification would strengthen the paper.

## Score and Decision

Based on calibration against human-reviewed anchors:

- The paper is clearly stronger than low-band papers (score ≤3) that had unclear contributions or missing experiments.
- Compared to the most similar accepted anchor (MJNywBdSDy, 5.75), this paper has broader experiments and stronger theory but notably lacks error bars and has an unresolved narrative tension around the NFE-based efficiency claim.
- Compared to the higher-scored discrete guidance anchors (XsgHl54yO7 at 6.5, Ombm8S40zN at 6.25), this paper has a cleaner theoretical contribution but falls short on evidential rigor.

The paper has a genuine contribution, a principled theoretical foundation, and extensive experiments showing consistent improvements. However, the complete absence of variance reporting and the tension in the efficiency claim are significant weaknesses that prevent it from being a strong accept. The paper should be accepted — the core ideas are sound and the direction is important — but the authors must address the major weaknesses before the paper is ready for publication.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>
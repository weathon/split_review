Now I have all the information needed. Let me write the final consolidated review.

## Summary

This paper proposes **IterRef**, a test-time scaling method for discrete diffusion models that uses Multiple-Try Metropolis (MTM) with noising-denoising transitions to iteratively refine intermediate states toward reward-aligned distributions. The approach is evaluated across three discrete diffusion backbones (MDLM, LLaDA-8B, MaskGIT) on text and image tasks with multiple reward functions, consistently outperforming baselines (BoN, SoP, SVDD, FK Steering) under matched compute budgets. The paper also provides a theoretical convergence guarantee (Proposition 1) under a reversibility assumption, and contributes the empirical finding that later denoising stages are more critical than earlier ones in discrete diffusion.

---

## Strengths

- **Novel and well-motivated methodology.** Formulating iterative refinement for discrete diffusion via the Multiple-Try Metropolis framework is genuinely new. The key design — a noising-denoising transition kernel combined with a balancing function that yields a simple acceptance rule \(\beta = \min(1, \exp((r(x_t') - r(x_t))/\alpha))\) — is clever, compact, and leads to a practical algorithm with clear compute knobs (\(k\) iterations, \(N\) particles, effective timestep set \(\mathcal{U}\)).

- **Strong and consistent empirical results.** Across MDLM, LLaDA-8B, and MaskGIT, and across multiple reward functions (Toxicity, Sentiment, CoLA, Perplexity, CLIPScore), IterRef consistently outperforms all baselines under equal NFE budgets. The advantage is particularly striking at low compute: on MDLM, IterRef at 2T–4T NFEs matches or exceeds what baselines achieve at 32T NFEs, yielding up to an 8× speed-up in test-time scaling (Figure 2a). The advantage holds in image generation as well (Table 1, +1.6–1.1 CLIPScore over the best baseline at matched budgets).

- **Empirically grounded insights about discrete diffusion dynamics.** Table 2 shows that applying IterRef at later denoising stages (0.1T) dramatically outperforms earlier stages (0.9T), directly contrasting with continuous diffusion where early steps dominate. Table 3 further demonstrates that increasing iterations \(k\) is more effective than increasing particles \(N\) at equal compute — a non-trivial finding that validates the iterative-refinement motivation.

- **Practical cost-reduction strategies grounded in theory.** The balancing function eliminates the need for explicit backward proposals, halving per-iteration cost, and pool reuse further reduces overhead (Section 3.3). These are principled consequences of the MTM framework, not ad hoc engineering.

---

## Weaknesses

### Major

- **Convergence guarantee rests on an unexamined assumption.** Proposition 1 explicitly requires that "\(q\) and \(p_\theta\) form a reversible Markov kernel." For the absorbing-state (masking) formulation used by MDLM, LLaDA, and MaskGIT, the forward process \(q\) is a pre-specified corruption and the reverse \(p_\theta\) is a learned neural approximation. The paper provides no argument — theoretical or empirical — that their composition satisfies detailed balance with respect to any distribution, let alone the target \(p^*\). The paper hedges with "under certain assumptions" in the introduction, but the central theoretical claim is presented as a key contribution ("we provide a theoretical guarantee that iterative refinement sampling converges to the target distribution"). This is not a fatal flaw — the empirical results stand on their own — but the theoretical framing overreaches relative to what is actually proved.

### Minor

- **Intermediate-reward approximation creates a gap between theory and practice.** Proposition 1 guarantees convergence for the exact intermediate reward \(r(x_t) = \alpha \log \mathbb{E}_{x_0 \sim p_\theta(\cdot|x_t)}[\exp(r(x_0)/\alpha)]\). In practice, \(r(x_t)\) is approximated by evaluating the reward on the one-step \(x_0\) prediction (a common heuristic also used by baselines). No analysis is given of how this approximation error affects the chain's stationary distribution or the acceptance ratio. The paper should at minimum acknowledge this gap and discuss its potential impact.

- **NFE-based comparison conflates different computational profiles.** As the paper itself acknowledges (Section 3.3), "aggregating these into a single NFE value may obscure meaningful differences" because generative-model calls and reward-model calls have different costs that vary with model scale. The wall-clock analysis in Appendix C.4 (not accessible) may address this, but the main text's efficiency comparisons (including the "8× faster" claim) rest entirely on NFE. The claim would be strengthened by presenting separate model-call counts or wall-clock results for at least one representative setting in the main paper.

- **The "8× faster" claim in Figure 1 is inconsistently anchored.** The Figure 1 caption states the claim is about "safety reward on LLaDA-8B (See § 4.5 for details)," but Section 4.5 (Figure 5) shows a consistent ~10 percentage-point toxicity gap, not an 8× NFE reduction. The explicit 8× calculation actually appears in Section 4.2 for MDLM on Toxicity (4T vs 32T). This inconsistency in the paper's own cross-referencing should be corrected.

---

## Nice-to-Haves

- A dedicated limitations section discussing when IterRef might underperform (e.g., when the base model is already well-aligned, as hinted by the LLaDA+CoLA result, or when the reward model is unreliable on noisy intermediate states).
- Ablation of the intermediate-reward approximation by comparing acceptance decisions under the one-step estimate versus a multi-sample Monte Carlo estimate.
- Exploration of per-timestep adaptive iteration counts \(k_t\) rather than a global \(k\).

---

## Removed Points

The following points from the input reviews were removed with justifications:

1. **"Criticism that the reversibility assumption is fatal/structural"** — The paper explicitly hedges the theory ("under certain assumptions"), and strong empirical results remain. The assumption is a real weakness but not fatal. Demoted to Major.
2. **"NFE comparison is 'evidentially insufficient' and the 8× claim is not justified"** — The paper acknowledges the NFE limitation in Section 3.3 and points to an appendix wall-clock analysis. The 8× claim (Section 4.2) is justified by the data: IterRef at 4T matches FK at 32T on MDLM Toxicity. The critic confused the 8× claim's context (MDLM, not Figure 5/LLaDA). Partially removed, with the remaining inconsistency noted above as Minor.
3. **"Missing appendices / missing reproducibility details"** — The parser strips appendices; they exist in the original submission.
4. **"Formatting/style nitpicks"** and **"typos"** — These are parser artifacts, not paper issues.

---

## Novel Insights

None beyond the paper's own contributions.

---

## Suggestions

1. **Reframe the theoretical claim.** Either (a) provide an argument or experiment that the reversibility condition approximately holds for the models used, or (b) downgrade the convergence claim to a heuristic that is well-motivated (MTM framework) and empirically validated. The empirical results are strong enough to carry the paper without overclaiming theory.
2. **Report separate generative-model and reward-model call counts** for at least one backbone scale (e.g., MDLM) in the main paper, to substantiate the NFE-based efficiency claims.
3. **Fix the inconsistent cross-referencing** of the "8× faster" claim between Figure 1, Section 4.2, and Section 4.5.

---

## Score and Decision

**Score calibration.** I compared the paper against calibration anchors drawn from three score bands:

| Anchor | Score | Round | Comparison |
|--------|-------|-------|------------|
| SSI-Corr (80rSu6iYo0) | 3.00 | R1 (low) | Much weaker: CIFAR-10 only, unclear novelty, limited baselines |
| Tilt Matching (tT7CXL3I9C) | 3.00 | R1 (low) | Much weaker: different topic, less empirical substance |
| Deterministic Discrete Denoising (CHtLFyDbZp) | 2.50 | R1 (low) | Much weaker: narrower scope, smaller experiments |
| Discrete SMC (7wbrFQvfdH) | 6.00 | R1 (mid) | Comparable: same area (discrete diffusion test-time scaling), similar empirical breadth. IterRef is more novel (MTM framework vs SMC) but has stronger theory-claim concerns |
| DriftLite (l01eG3Qikl) | 6.00 | R1 (mid) | Comparable: both address inference-time scaling. DriftLite has stronger theory but is for continuous diffusion. IterRef is more broadly evaluated |
| Diffusion Search (b7Ftp6U78i) | 6.00 | R2 (narrow) | Comparable: uses search/MCMC for diffusion. IterRef is cleaner methodologically, focused on discrete case |
| Proximal Diffusion Neural Sampler (XTHQqS7ObC) | 6.50 | R2 (narrow) | Slightly higher topic-wise but less directly comparable (training-based) |
| Flow Map Trajectory Tilting (lR8GufFQMb) | 5.00 | R2 (narrow) | Weaker: less empirical breadth, overclaiming concerns |

**Round-1 bracket:** 4.5–7.0. The paper is clearly above the 2.5–3.0 anchors and well within the mid band.

**Round-2 narrowing:** After reading the Discrete SMC paper (6.0, Accept Poster) and the Diffusion Search paper (6.0, Accept Poster) in full, IterRef compares favorably: it is more novel than the SMC paper (which some reviewers called "limited novelty"), and its method is cleaner and more targeted than the Diffusion Search paper. The main weakness — the unexamined reversibility assumption — tempers the score but does not invalidate the empirical contribution.

**Final score:** 6.0 — a solid accept-level paper with a novel method and strong empirical results, held back from a higher score by the gap between its theoretical claims and their justification.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>
Now I have sufficient calibration data. Let me compile the final review.

## Summary

This paper studies the trade-off between watermark strength and speculative sampling efficiency in LLMs. It introduces a continuous measure of watermark strength (expected KL divergence between watermarked and original distributions), formalizes the trade-off as a Pareto optimization problem, and proposes Algorithm 1 — a mechanism that replaces the random acceptance coin in speculative sampling with a pseudorandom variable. Theorem 4.1 proves that, for degenerate watermarks (e.g., Gumbel-max), the algorithm simultaneously achieves maximal watermark strength and maximal sampling efficiency. Experiments on Llama and Gemma model pairs show that the method improves detectability (TPR@FPR=1%) for both Gumbel-max and SynthID watermarks while preserving acceptance rates.

## Strengths

- **Quantitative watermark strength measure linked to detectability.** Definition 3.1 (WS as expected KL divergence) and Theorem 3.1 (connecting WS to the p‑value decay rate of the uniformly most powerful test) provide a principled, continuous foundation for analyzing watermark strength, moving beyond the binary definition used in prior work.

- **Complete Pareto characterization of the trade‑off.** Definition 3.2 casts the trade-off as a constrained optimization problem, and the derivation of explicit trade-off curves (Eq. 8/10, Figure 1) for Gumbel‑max, SynthID, and linear-interpolation classes gives a clear picture of how existing schemes populate the frontier.

- **Elegant algorithmic mechanism with a clean proof.** Algorithm 1 is simple and well-motivated: making the acceptance decision pseudorandom (line 8) rather than truly random renders the entire generation deterministic in the pseudorandom variables. Theorem 4.1 shows that under this algorithm, unbiasedness, maximal sampling efficiency (1 − TV(Q,P)), and maximal watermark strength (Ent(P)) are simultaneously achievable for degenerate watermarks — a direct contradiction of the previously claimed "inevitable" trade-off.

- **Empirical verification that efficiency is preserved.** The left panel of Figure 2 confirms that AATPS for Algorithm 1 closely matches standard speculative sampling across K∈{2,3,4} for both watermark schemes, with 95% confidence intervals overlapping the baseline.

- **Improved detectability demonstrated with error bars.** The middle and right panels of Figure 2 show clear improvements in TPR@FPR=1% for both Ars‑τ (Gumbel‑max) and Bayes‑MLP (SynthID) over the prior-based detectors, with the gap to the oracle shrinking at 200 tokens. ROC curves and per-token-time/perplexity tables in the appendix provide additional support.

## Weaknesses

### Major
- **Theory applies strictly to degenerate watermarks; experiments include a non-degenerate case.** Theorem 4.1 requires the decoder to be degenerate (a.s. point mass), which holds for Gumbel‑max but not for SynthID with finite rounds (m=30). The paper is honest about this gap (it states "our current work directly applies to unbiased degenerate watermarks" in the conclusion), and the SynthID experiments are presented as empirical improvements rather than provably optimal. Nevertheless, the central claim of "breaking the trade-off" is technically proven only for the Gumbel‑max case; the paper would benefit from sharper language in the abstract and contributions to distinguish the proven optimality from the empirical improvement.

- **Trade‑off curves (Figure 1) are illustrated only on simulated distributions and are not validated experimentally.** The Pareto curves derived in Section 3.2 use synthetic (Q,P) pairs described in Appendix C.1, and the experiments never revisit these curves — they instead measure detectability (TPR) as a proxy. Showing that Algorithm 1 lies on or above the empirical Pareto frontier in a real experimental setting would substantially strengthen the connection between the theory and the reported improvements.

### Minor
- **Missing SynthID detection baseline that isolates the benefit of uₜ.** For SynthID, Bayes‑MLP uses an MLP trained on (yᵖ, yᵀ, uₜ) while Bayes‑Prior uses a simple weighted average. A natural control is an MLP trained on (yᵖ, yᵀ) *without* uₜ, which would isolate whether the improvement comes from access to uₜ or from the nonlinear MLP fusion. The current comparison conflates these two factors.

- **Temperature choice limits generality.** Experiments use temperatures of 0.5 (Gumbel‑max) and 0.7 (SynthID) to "make the results more pronounced." Watermarking is often used at temperature 1.0 for creative generation; the paper should at least discuss whether the detectability improvements persist at higher temperatures.

- **Theorem 4.1's "sampling efficiency" claim and the bonus step.** Theorem 4.1(b) states SE = 1 − TV(Q,P), which Definition 2.1 defines as the expected acceptance rate. The algorithm's bonus step (line 16) adds an extra token when all K drafts are accepted, so the actual AATPS exceeds 1 − TV(Q,P) (as seen in the experiments). Clarifying that the theorem refers to the per-step acceptance rate (not AATPS) would avoid confusion.

### Trivial
- Tables 1 and 2 (PTT, LOGPPL) appear only in the appendix despite being referenced in the main text. Moving at least a summary of the efficiency/perplexity numbers to the main paper would better support the claims of preserved quality and latency.

## Nice-to-Haves
- Validate the theoretical Pareto curve (Definition 3.2) empirically by computing watermark strength and sampling efficiency for multiple watermark configurations and showing that Algorithm 1 lies above the empirical frontier.
- Investigate whether the detectability improvement holds at higher temperatures (e.g., temperature 1.0).
- Provide a theoretical analysis of how much uₜ contributes to detection improvement in a simplified setting (e.g., two-token vocabulary).

## Removed Points
- **"Fairness of detection comparison" (Ars‑τ calibrates τ on validation set vs. Ars‑Prior estimates p from rates).** This comparison is inherent to the two settings: the prior method lacks access to uₜ and cannot use τ‑based selection. The asymmetry is not a flaw — it reflects the fundamental difference between having uₜ and not having it. The improvement magnitude is large enough that any residual calibration effect would not erase the gap. *Removal justification: strawman weakness — the criticism misunderstands the inherent asymmetry between the compared settings.*

- **"The paper does not discuss overhead of training the MLP or calibrating τ."** The paper states the training set size (1,000 texts) and the MLP architecture (three-layer). Calibration is a grid search on a validation set. These are standard operations with negligible overhead. *Removal justification: trivial nongap — asking for documentation of trivial implementation details.*

- **"Missing related works" / reproducibility concerns about cited models.** The paper cites Gumbel‑max (Aaronson, 2023), SynthID (Dathathri et al., 2024), Llama, Gemma, EL15, C4 — all publicly released entities. *Removal justification: hard rule — do not question existence of cited references.*

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. In the abstract and contributions, clarify that the theoretical guarantee of "breaking the trade-off" (maximal WS and maximal SE simultaneously) applies to degenerate watermarks (e.g., Gumbel‑max; SynthID only in the m→∞ limit), and that the SynthID‑m=30 results are empirical improvements rather than provably optimal.
2. Move a concise summary of the Per Token Time and Log Perplexity results (at least the numbers from Tables 1 and 2) into the main paper body.
3. For the SynthID detection experiments, add an MLP baseline trained on (yᵖ, yᵀ) without uₜ to isolate the benefit of the pseudorandom acceptance variable.
4. Address the bonus step in Theorem 4.1 explicitly, noting that the proven SE is the per-step acceptance rate and that the bonus step adds a bounded extra term to AATPS.

## Calibration

| Anchor ID | Title | Score | Round | Comparison |
|-----------|-------|-------|-------|------------|
| jbfDg4DgAk | Sparse Watermarking in LLMs | 3.00 | R1 bracketing (low) | Much weaker: lacks theoretical depth and clean characterization |
| xFezgECSLa | On the Design and Analysis of LLM-Based Algorithms | 3.00 | R1 bracketing (low) | Not directly comparable, but significantly below |
| 4y3GDTFv70 | Latent Space Theory for Emergent Abilities | 3.25 | R1 bracketing (low) | Not directly comparable |
| yx8bU8T5ZN | Unified View of Delta Parameter Editing | 2.33 | R1 bracketing (low) | Not comparable |
| LdIlnsePNt | Watermarking using Semantic-aware Speculative Sampling (SEAL) | 6.00 | R1 bracketing (mid), R2 narrowing | Very topically similar; our paper has cleaner theory, more coherent narrative, and better experiments |
| eKGEsFdpin | I Know You Did Not Write That! (Sampling-based watermark) | 3.67 | R1 bracketing (mid) | Less theoretically grounded; below ours |
| 0koPj0cJV6 | Watermark for Black-Box Language Models | 4.60 | R1 bracketing (mid) | Solid but less ambitious in scope; below ours |
| E4LAVLXAHW | Black-Box Detection of Language Model Watermarks | 7.00 | R1 bracketing (mid), R2 narrowing | More comprehensive experiments but less theoretical novelty; slightly above ours |
| j7b4mm7Ec9 | Towards Lightweight Deep Watermarking Framework | 7.60 | R1 bracketing (high) | Image watermarking; less comparable |
| SnDmPkOJ0T | REEF: Representation Encoding Fingerprints | 8.00 | R1 bracketing (high) | Different task (IP protection); higher scope/impact |
| WJaUkwci9o | Self-Improvement in Language Models: The Sharpening Mechanism | 8.00 | R1 bracketing (high) | Different topic; higher |
| syThiTmWWm | Cheating Automatic LLM Benchmarks | 7.75 | R1 bracketing (high) | Different topic; higher |
| 9k0krNzvlV | On the Learnability of Watermarks | 5.75 | R2 narrowing | Accepted but more empirical and less theoretically deep; below ours |
| DEJIDCmWOz | On the Reliability of Watermarks | 6.00 | R2 narrowing | Accepted; solid empirical study but less theoretical contribution; slightly below ours |
| jlhBFm7T2J | Undetectable watermark for generative image models | 6.50 | R2 narrowing | Image domain; similar score level; our paper has stronger theory |
| 16O8GCm8Wn | Robust Watermarking Using Generative Priors | 6.40 | R2 narrowing | Image domain; less comparable |

**Round 1 bracket:** 5.5–7.5. **Round 2 narrowing:** After comparing with the SEAL paper (6.00, weaker theory/experiments), the Learnability paper (5.75, less theoretical depth), the Reliability paper (6.00, less theory), and the Black-Box Detection paper (7.00, above ours in empirical scope), plus the closely related 6.50 image watermark paper, the paper sits at **6.5**. It is a clear contribution with genuine theoretical advances and solid empirical support, but has a verifiable gap between the optimality theory (degenerate watermarks) and the headline empirical setting (SynthID with finite rounds).

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>
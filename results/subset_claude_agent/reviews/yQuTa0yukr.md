I have enough context from reading the paper. Let me now draft the review before calibration.Now let me run Round 1 calibration search.Round 1 bracket: The strong anchors (score >7.5) are on MCMC/sampling topics but quite different (Markov process simulation, SVGD theory, discrete diffusion). The middle anchors are more relevant—papers on neural network proposals in SA and CO solvers score 5.0–6.25. I'll place the initial bracket at **5 to 7**.

Let me read two relevant middle-range anchors.Round 1 bracket: **5 to 7**. The TAPT paper is clearly stronger than the wDE3clrYWR (score 5.0) analog — TAPT has exact validation benchmarks, cleaner algorithm, and the generalization result. But it's weaker than a clean accept-6+ paper due to the theoretical overclaiming and training cost exclusion. Let me narrow with Round 2 anchors.Excellent finds. Let me read the most topically similar anchors in full.Now I have sufficient calibration. Let me synthesize the final review.

**Calibration analysis:**
- **kXNJ48Hvw1** (6.67, Accept): Stacked RBMs for PT acceleration — most topically similar, has theoretical analysis, validated on 2D Ising, but no cross-instance generalization. TAPT is roughly comparable but gains on factorization generalization, loses on theoretical rigor.
- **BlSIKSPhfz** (6.0, Accept): Hybrid continuous-discrete ground state sampling — similar scope, accepted with unanimous 6s, comparable acknowledgment of limitations, no generalization to unseen instances.

TAPT sits between these two anchors. The factorization generalization result is genuinely stronger than anything in the stacked RBM paper. But the theoretical framing mismatch and single-instance spin glass weaken it relative to the theoretical analysis in the stacked RBM paper. Final score: **6.0**.

---

## Summary
IsingFormer/TAPT couples a decoder-only Transformer trained on equilibrium Boltzmann samples with Parallel Tempering (PT), using the transformer as a generator of global-move proposals and PT's Metropolis criterion as a verifier. The method is validated on 2D Ising sampling (with exact Kac-Ward benchmarks), 3D spin glass optimization (single instance), and integer factorization (with transfer to 190 unseen 16-bit semiprimes). The paper's central claim is that learned global proposals integrated into PT accelerate both sampling and combinatorial optimization, with the factorization result providing the strongest evidence for generalization across problem instances.

## Strengths

- **Rigorous 2D Ising validation with exact reference**: Free energy comparison uses the Kac-Ward determinant formalism (Section 3, Figure 2a), providing quantitative ground truth rather than proxy metrics. Temperature generalization to unseen β values (Figure 2a, yellow diamonds across 0.0–1.0) demonstrates structural learning rather than memorization.

- **Demonstrated conditional sampling advantage**: Figure 2(c) shows transformer-initialized Gibbs (1 update) closely matching exact energy variance under half-clamped boundary conditions, while pure Gibbs from random initialization deviates substantially. The paper explicitly cross-references the 10⁴-sweep Gibbs comparison in Appendix Figure 5, correctly contextualizing the claim that the transformer "replaces thousands of local MCMC updates."

- **Instance-level generalization across held-out factorization problems**: On 190 unseen 16-bit semiprimes (Figure 4c), TAPT outperforms PT on ~64% of test instances, providing genuine out-of-distribution evidence. This is the paper's strongest and most novel result.

- **Controlled ablation isolating periodic proposals**: Figure 3 compares PT, TAPT, and "warm start + PT," isolating that periodic transformer interventions yield a steeper descent slope beyond a single warm start. This cleanly partitions what the learned proposals contribute.

- **Honest and explicit acknowledgment of limitations**: Section 5.1 explicitly states training time is excluded from comparison and that "in the absence of generalization, this is a serious limitation." Section 4 discusses the MH correction path and why it is not implemented, rather than hiding the theoretical gap.

## Weaknesses

### Fatal
None.

### Major

- **Theoretical framing overclaims relative to the implemented algorithm**: The introduction (line 19) frames PT as a "principled verifier satisfying detailed balance and known stationary distributions," implicitly extending this guarantee to TAPT. However, Section 4 explicitly acknowledges that the implemented Metropolis criterion (Eq. 2) omits the MH correction needed for TAPT to actually inherit detailed balance. Without the full MH correction, TAPT's stationary distribution is not the Boltzmann distribution in general—it is an effective approximate optimizer whose bias depends on IsingFormer's imperfection. The acknowledgment in Section 4 is clear, but it is buried after the abstract, introduction, and Section 3 have already established the "correctness via verifier" framing. The mismatch between stated motivation and actual implementation is a real inconsistency that should be resolved by narrowing the theoretical claims upfront, or by implementing the MH correction in at least one controlled experiment.

- **Training cost excluded from 3D spin glass comparison**: The paper compares TAPT vs. PT in inference sweeps only, explicitly excluding transformer training time. For the spin glass case, training requires long-run MCMC at multiple temperatures to collect equilibrium samples—the same type of expensive MCMC TAPT aims to replace—yet no generalization is demonstrated across spin glass instances. Section 5.1 acknowledges this directly ("transformer training time is not factored into optimization performance and in the absence of generalization, this is a serious limitation"), yet the spin glass result continues to appear in the conclusion as evidence for TAPT's optimization effectiveness. The acknowledged limitation substantially weakens this particular evidence chain; the result is a demonstration of mechanism, not a practical optimization win.

### Minor

- **8-bit factorization is a degenerate test**: Figure 4(a) is labeled "Training Instances (all semiprimes)" because for 8-bit factorization there are exactly 21 distinct semiprimes and the model trains on all of them. This is a training-set performance plot, not generalization. The caption correctly labels it, but the text frames 8-bit alongside 16-bit as together supporting the generalization claim.

- **Acceptance rates across the β ladder are unreported**: The paper does not show how proposal acceptance rates vary with temperature or change during inference. Understanding the temperature-resolved acceptance profile is important for assessing when the generator's contributions matter, especially given that the coldest replicas receive no direct proposals and benefit only from swap propagation.

### Trivial
None.

## Nice-to-Haves
- Implement the MH correction in at least one controlled experiment (e.g., 2D Ising where exact is known). The paper notes the autoregressive architecture makes P_model(m) tractable—this would empirically characterize whether the bias from the uncorrected Metropolis step is negligible or consequential, strengthening the paper either way.
- Revise the abstract and introduction to scope theoretical claims earlier: frame TAPT as an approximate MCMC method capable of being made exact via MH correction, rather than implying inherited correctness guarantees.
- Provide a rough wall-clock accounting for the spin glass experiment (MCMC sweeps to generate training data vs. sweeps saved during inference) so readers can assess total cost.
- Include temperature-resolved acceptance rate statistics for at least one experiment.
- For Figure 4 scatter plots, include a plot of improvement magnitude (not just win direction) to assess whether the 64% win rate represents substantial net benefit or marginal wins offset by meaningful losses.

## Removed Points
*These points are flagged as removed — treat with caution.*

- **Harsh critic: "No comparison to variational neural annealing (Hibat-Allah et al., 2021)"** — Removed per hard rule: cannot verify external comparisons without access to those papers; the paper cites these methods in related work.

- **Harsh critic: "Figure 2(c) trivially bad Gibbs baseline"** — Removed. The paper explicitly cross-references the 10⁴-sweep Gibbs comparison in Appendix Figure 5 and explains the experimental setup correctly. The one-step comparison is the point of the experiment: showing transformer initialization quality for a single proposal, not competing against converged Gibbs.

- **Harsh critic: "E_gnd uncertainty propagation"** — Removed as speculative. The paper uses 100 SA chains with 10⁶ sweeps; any uncertainty in E_gnd would shift all residual energy curves equally and not affect relative comparisons.

- **Strength Finder: "Explicit algorithmic specification (Algorithm 1) as a strength"** — Removed as generic; providing a complete algorithm description is a baseline expectation.

## Novel Insights
The paper's key novel observation—implicit in the results but worth making explicit—is that the practical utility of TAPT is conditioned on whether the problem family admits instance-level conditioning through a shared structural template. When a family of Ising problems can be expressed via conditioning tokens over a shared circuit structure (as in factorization), training cost amortizes across many instances and TAPT delivers genuine generalization. When no such structure exists (as in arbitrary 3D spin glasses), TAPT degenerates to a single-instance method that must pay training cost without amortization. This instance-conditioned generalization, rather than the generator-verifier framing per se, is the paper's most distinctive and practically relevant contribution, and it points toward a productive future research direction: identifying what problem families have the shared structure necessary to make learned proposals useful beyond individual instances.

## Suggestions
- Implement MH correction as a single controlled ablation on 2D Ising and report whether the bias is empirically negligible — this directly resolves the main theoretical tension.
- Revise introduction language to qualify the "principled verifier" framing by clarifying upfront that TAPT as implemented is an effective approximate method that can be made exact via MH correction (which is not currently implemented).
- Either include training cost in the spin glass comparison or explicitly reframe the spin glass result as a mechanistic demonstration rather than an end-to-end optimization win.
- For the 8-bit factorization, remove the training-on-all claim from the generalization narrative or acknowledge it explicitly in the text, not just the figure caption.

---

## Score and Decision

**Anchor comparison:**
| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| OcTUquFXfx | 2.60 | 1 | Much weaker — no architecture quality, high-dimensional optimization only |
| wDE3clrYWR | 5.00 | 1 | Similar concept (neural proposals + SA) but weaker: only single domain, RL formalism unclear, no generalization |
| Kc3yoIL5oR | 5.25 | 1 | CO generalization paper but different framing, TAPT's physics validation is stronger |
| yEwakMNIex | 6.25 | 1 | Unified neural CO solver — broader scope but similar quality tier; TAPT's exact validation is stronger, but scope is narrower |
| kXNJ48Hvw1 | 6.67 | 2 | Most topically similar (stacked RBMs + PT for Ising), has theoretical analysis TAPT lacks, but no cross-instance generalization; TAPT's factorization result is stronger novelty-wise |
| BlSIKSPhfz | 6.00 | 2 | Hybrid continuous-discrete ground state sampling on Ising — similar scope, similar quality, accepted at 6.0 with comparable honest acknowledgment of limitations |
| 9EfBeXaXf0 | 6.75 | 2 | Parallel quasi-quantum annealing for CO — stronger CO results, but TAPT's exact physics validation is more rigorous |
| ybWOYIuFl6 | 6.00 | 2 | Boltzmann sampler paper — topically adjacent, comparable quality range |
| 8NiTKmEzJV | 6.25 | 2 | Non-equilibrium transport sampler — more theoretical, similar quality tier |

**Round 1 bracket:** 5–7  
**Round 2 narrowing:** TAPT sits between BlSIKSPhfz (6.0) and kXNJ48Hvw1 (6.67). The factorization generalization result in TAPT is a genuine contribution absent from BlSIKSPhfz (which accepted at 6.0), pushing TAPT above 6.0. However, kXNJ48Hvw1 scored 6.67 with a cleaner theoretical analysis, while TAPT's theoretical framing mismatch and single-instance spin glass result pull it below 6.67. Final score: **6.0** — a solid borderline accept. The factorization generalization result and rigorous 2D Ising validation warrant acceptance; the theoretical overclaiming and training-cost omission in the spin glass setting prevent a higher score.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>
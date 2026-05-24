Now I have a thorough understanding of the paper and the calibration landscape. Let me write the consolidated review.

---

## Summary

This paper introduces INFO-SEDD, a method for estimating mutual information (MI) and entropy for high-dimensional discrete data by extending continuous-time Markov chain (CTMC) diffusion models. The core idea is to express KL divergence via Dynkin's formula over CTMC forward processes, then use learned score functions to compute MI through either a joint-distribution formulation (INFO-SEDD-J) or a conditional formulation (INFO-SEDD-C). The method is evaluated on synthetic benchmarks, text summarization, and genomics, consistently outperforming variational and neural competitors.

## Strengths

- **Strong synthetic benchmark results (Table 1)**: INFO-SEDD recovers ground-truth MI with high accuracy and low variance across increasing MI and dimensionality (e.g., 39.11 ± 0.65 for true MI 40 at D=40), while all competing estimators (GAN-DIME, HD-DIME, SMILE, MINE, etc.) collapse or exhibit large biases as MI and dimensionality grow. This is compelling evidence that the method works where existing neural estimators fail.

- **Practical value in text summarization model selection**: INFO-SEDD-C achieves a Pearson correlation of 0.740 with human consistency ratings (Table 2), substantially higher than alternatives (e.g., KL-DIME 0.214). This demonstrates the method's utility as an automatic evaluation metric without requiring elaborate embedding engineering.

- **Elegant single-model design via absorbing state**: The choice of an absorbing transition matrix (Section 3, Eq. 6) allows a single score model trained on the joint distribution to also compute marginal scores, avoiding separate model training. This is both computationally efficient and theoretically principled.

- **Theoretical grounding with error decomposition (Eq. 7)**: The bound decomposes total error into estimation error and an exponentially decaying truncation bias, providing a clear theoretical framework for understanding the estimator's behavior.

- **Seamless integration with pretrained models**: The method is applied using existing architectures—MDLM-SMALL for text and CADUCEUS for genomics—with minimal architectural modifications, demonstrating practical deployability.

## Weaknesses

### Major

- **Unexplained divergence between INFO-SEDD-J and INFO-SEDD-C on text data**: The two variants should theoretically estimate the same MI, yet in the model selection experiments (Figures 2 and 3), INFO-SEDD-C produces MI estimates in the range 400–800 nats while INFO-SEDD-J produces estimates in the range 250–425 nats—roughly a factor of 1.5–2× difference. The paper discusses and explains the analogous discrepancy in genomics (Section 4.3: joint-distribution modeling of long DNA sequences plus a scalar label is considerably harder than conditional modeling), but the same divergence in the text domain goes unexamined. Because the paper's central claim is that INFO-SEDD provides *accurate* MI estimates, the fact that its own two formulations disagree sharply on real data directly weakens that claim. The consistency test (Figure 1) shows better alignment between the variants, suggesting the problem may be specific to the model selection setup, but this is not analyzed. A diagnostic experiment—e.g., applying both variants to a synthetic text-like setting with known ground-truth MI—would clarify which variant to trust in which regime and whether the divergence reflects bias in one variant or variance in both.

### Minor

- **Weak reference point for text consistency test**: The "empirical derivation" of ground-truth MI for text uses entropy rates from older studies (Takahira et al., 2016; Cover and King, 1978) to obtain an order-of-magnitude range (256–303 nats). The paper acknowledges this is only an order-of-magnitude estimate, but a stronger reference (e.g., a classifier-based proxy as used in the genomics experiment, or a small synthetic text dataset with tractable MI) would have made the consistency argument more convincing.

- **Motif discovery experiment is qualitative only**: The TATA-box example (Figure 5, Section 4.3) is a nice illustration but uses only INFO-SEDD-J and lacks quantitative comparison with existing motif-finding tools. Its value as evidence of practical utility is therefore limited to a proof-of-concept.

- **Derivation of the KL expression in Section 2.2 is compressed**: Equation (2) states that KL[p_0 ∥ q_0] = E[log(p_T/q_T)(X_T)] without fully unpacking why the initial-distribution term drops out (the justification—that both p_0 and q_0 converge to the same reference π—is mentioned later in passing). The transition via Dynkin's formula (Eq. 3–4) is sketched rather than developed. While the full derivation is presumably in the appendix, the main text's argument for the method's validity hinges on this step and would benefit from a more self-contained exposition.

### Trivial

- The paper describes INFO-SEDD as a "consistent" estimator (Section 3). The error bound (Eq. 7) includes neural-network approximation errors (ε_p, ε_q) that are not directly quantified, so "consistent up to an exponentially decaying truncation bias" is more precise than calling the estimator consistent without qualification. This is a phrasing nitpick rather than a substantive concern.

## Nice-to-Haves

- A synthetic experiment diagnosing the J/C discrepancy across varying dimensions, support sizes, and modeling difficulty regimes would help users choose the appropriate variant.
- A stronger reference for the text consistency test (e.g., a classifier-based proxy analogous to the genomics setup).
- Quantitative comparison with existing motif-finding tools for the genomics application.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Harsh critic: "baseline fairness / hyperparameter tuning"**: The critic speculates that "the paper provides little detail on how these baselines were tuned or whether equal effort was spent on their hyperparameter selection" and that "the real-data superiority could be partly an artifact of suboptimal baseline training." The paper states it uses the same backbone architecture for all methods with minimal tweaks; the synthetic experiments (Table 1) already demonstrate INFO-SEDD's superiority independent of real-data tuning concerns. This concern is speculative and not anchored in a specific failure demonstrated in the paper. Demoted out of the main review.

- **Strength Finder: "the problem is important" / "targets an interesting question"**: Generic framing without specific evidence, dropped.

- **Strength Finder: "seamless integration with pretrained models"**: Kept but merged into the single-model design strength since they are two sides of the same coin.

## Novel Insights

None beyond the paper's own contributions. The key insight—extending CTMC diffusion to KL divergence estimation via Dynkin's formula—is the paper's own contribution and is well-motivated.

## Suggestions

- Add a diagnostic experiment (synthetic, with known ground-truth MI) that applies both INFO-SEDD-J and INFO-SEDD-C across a range of dimensions and support sizes to characterize their respective bias and variance. This would either resolve the J/C discrepancy or define the regime in which each variant is reliable.
- For the text summarization consistency test, consider constructing a classifier-based proxy for ground-truth MI (as done for genomics) to strengthen the reference beyond the order-of-magnitude entropy-rate estimate.
- Clarify in Section 2.2 how the initial-distribution term is eliminated in the transition from the standard KL definition to the expectation at time T, rather than deferring the justification.

## Score and Decision

**Round 1 — Bracketing**: Searched for MI estimation and discrete diffusion papers across three bands. The most relevant anchor is MINDE (0kWd8SJq8d, avg 6.50, Accept), which proposes diffusion-based MI estimation for continuous data and is the direct predecessor of INFO-SEDD. Other anchors in the middle band include f-DIME (KC2MViQASx, 5.60, Reject) and SEDD (71mqtQdKB9, 6.60, Reject). High-band anchors (e.g., Learning to Permute, EO8xpnW7aX, 8.00) are diffusion papers on different problems. Initial bracket: **5.5–7.0**.

**Round 2 — Narrowing**: Retrieved anchors inside the bracket: f-DIME (5.60), Discrete Diffusion Schrödinger Bridge (tQyh0gnfqW, 5.67), CTMC Convergence (pq1WUegkza, 7.00), SEDD (6.60), Unlocking Guidance (XsgHl54yO7, 6.50). INFO-SEDD is clearly stronger than f-DIME (which had limited experiments and unclear contributions) and comparable to MINDE (6.50). The J/C discrepancy pulls INFO-SEDD slightly below MINDE, but the synthetic results, real-world applications, and theoretical grounding keep it well above the 5.5 rejection zone.

**Anchor comparison summary**:
| Anchor | Score | Round | Comparison |
|---|---|---|---|
| lt6xKGGWov | 2.33 | R1 | Much weaker; feature selection MI with limited novelty |
| hr4HTShC6l | 3.00 | R1 | Weaker; applied MI paper without novel estimation method |
| MNGMpHxi1I | 3.00 | R1 | Weaker; uncertainty measures, not MI estimation method |
| hv8l922Ad7 | 3.40 | R1 | Weaker; disentanglement metrics, different problem |
| vgQmK5HHfz | 4.83 | R2 | Weaker; normalizing flows DoE, less competitive results |
| hkL8djXrMM | 5.25 | R1 | Different focus; neural diffusion models architecture |
| dUCMO9lwSv | 5.25 | R1 | Different focus; latent abstractions in diffusion |
| KC2MViQASx | 5.60 | R1/R2 | INFO-SEDD stronger; f-DIME had limited experiments and unclear claims |
| tQyh0gnfqW | 5.67 | R2 | Different focus; Schrödinger bridge for graphs |
| PyHRUMxKbT | 5.75 | R2 | Weaker; InfoNet, less competitive and narrower scope |
| Ombm8S40zN | 6.25 | R2 | Different focus; steering masked diffusion models |
| 0kWd8SJq8d (MINDE) | 6.50 | R1 | Closest comparison; INFO-SEDD extends to discrete data, similar quality |
| XsgHl54yO7 | 6.50 | R2 | Different focus; guidance for discrete diffusion |
| 71mqtQdKB9 (SEDD) | 6.60 | R2 | Framework INFO-SEDD builds on; different problem (language modeling) |
| pq1WUegkza | 7.00 | R2 | Stronger; pure theory paper with rigorous convergence bounds |
| EO8xpnW7aX | 8.00 | R1 | Stronger; novel discrete diffusion for permutations with comprehensive experiments |

**Final score**: 6.0. The paper makes a genuine and well-executed contribution by extending diffusion-based MI estimation to discrete data via CTMCs, with strong synthetic validation and promising real-world applications. The J/C discrepancy on real data is a significant concern that the paper partially addresses for genomics but leaves unexplained for text, which tempers the strength of the accuracy claim. This is a solid paper that would benefit from the suggested diagnostic experiments.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>
Now I have enough information. Let me synthesize the final review.

---

## Summary

INFO-SEDD extends diffusion-based mutual information estimation (previously developed for continuous data in MINDE) to high-dimensional discrete data by leveraging Continuous-Time Markov Chain (CTMC) discrete diffusion and score models. The authors derive a KL divergence estimator via Dynkin's formula, propose both joint and conditional MI variants requiring only a single score model, and demonstrate strong empirical performance on synthetic benchmarks, text summarization, and genomics tasks including motif discovery.

## Strengths

- **Strong synthetic benchmark results.** Table 1 demonstrates that INFO-SEDD recovers ground-truth MI values with high accuracy across a wide range of dimensions and MI levels (e.g., $9.92 \pm 0.12$ for MI=10, $47.77 \pm 1.18$ for MI=50), while all competing neural estimators (GAN-DIME, SMILE, MINE, etc.) degrade substantially at high MI and high dimensionality. This directly validates the core claim of scalable MI estimation for discrete data.

- **Compelling real-world applications.** The text summarization consistency test (Figure 1) shows both INFO-SEDD variants tracking the expected linear dependence of MI on pairing probability, while competitors underestimate or behave inconsistently. In genomics, INFO-SEDD-C closely matches a classifier-based reference curve (Figure 4), and INFO-SEDD-J successfully identifies known TATA-box motif locations in Arabidopsis promoters (Figure 5) — a novel capability that exploits the estimator's native support for subset masking.

- **Practical single-model design.** By choosing absorbing-state rate matrices, the method computes marginal scores from a single model trained on the joint distribution (Equation 6, Appendix A.3). This reduces model count and complexity, and enables seamless integration with pretrained backbones (MDLM-SMALL for text, CADUCEUS for genomics) without training from scratch.

- **Theoretical error bound.** Equation (7) decomposes the estimator's error into a score-approximation term (linear in score error) and an exponentially vanishing truncation bias, providing a consistency guarantee.

- **Versatility.** The framework extends to entropy estimation (INFO-SEDD-H) and is demonstrated on Ising models (Appendix D), showing breadth beyond MI estimation.

## Weaknesses

### Fatal

None. The core empirical results and the estimator's practical value are well-supported.

### Major

- **The KL derivation in Equation (2) and surrounding text is mathematically problematic as presented.** The paper claims $\text{KL}[\vec{p}_0 \parallel \vec{q}_0] = \mathbb{E}[\log \frac{\vec{p}_0}{\vec{q}_0}(\vec{X}_T)]$ where $\vec{X}_T$ is the terminal state of a CTMC started from $\vec{p}_0$. The KL divergence is $\mathbb{E}_{\vec{X}_0 \sim \vec{p}_0}[\log(\vec{p}_0(\vec{X}_0)/\vec{q}_0(\vec{X}_0))]$, not an expectation over the terminal state $\vec{X}_T \sim \vec{p}_T$ of the initial density ratio evaluated at a different point. This step as written is not justified. The subsequent statement that "both $\vec{p}_0$ and $\vec{q}_0$ converge to $\pi$" also appears to contain a typo (it is $\vec{p}_T$, $\vec{q}_T$ that converge, not the initial distributions), and the claim that the term $\mathbb{E}[\log(\vec{p}_0/\vec{q}_0)(\vec{X}_0)]$ — which *is* the KL divergence — is "omitted" makes the derivation hard to follow. The intended approach is likely a path-integral representation analogous to the continuous-diffusion case (MINDE), where the terminal KL vanishes and the estimator captures the integral of score differences along the path. But the presentation of Equation (2) as stated does not constitute a valid derivation, and the text around it is confusing enough to undermine confidence in the theoretical development. This should be rewritten with a clear, step-by-step derivation connecting the definition of KL to the Dynkin-based integral estimator.

### Minor

- **Limited ablations on estimator components.** While the paper demonstrates overall performance, ablations isolating the effect of the absorbing-state choice, the score model quality, or the truncation time $T$ on estimator accuracy are absent from the main text (some appear in Appendix C, which is stripped). These would strengthen the empirical case for the specific design choices.

- **Text summarization correlation is moderate.** The Pearson correlation of 0.74 between INFO-SEDD-C MI estimates and human consistency judgments (Table 2) is promising but not decisive. The paper acknowledges that MI cannot capture hallucinated facts, but this limitation should be stated more prominently when claiming MI as a model-selection signal.

- **No runtime or computational cost comparison.** Given that INFO-SEDD requires simulating CTMC forward processes and evaluating score models, the computational cost relative to variational estimators would be useful for practitioners.

### Trivial

- The phrase "both $\vec{p}_0$ and $\vec{q}_0$ converge to $\pi$" on line 69 should read "both $\vec{p}_T$ and $\vec{q}_T$ converge to $\pi$."

## Nice-to-Haves

- A direct comparison with the continuous-diffusion MINDE estimator applied to embedded discrete data (the "embedding trick") would quantify the benefit of native discrete handling.
- A discussion of the relationship between the CTMC-based KL representation and the Girsanov-theorem approach used in MINDE would help readers bridge the continuous and discrete formulations.
- Runtime and memory comparisons against competing estimators.

## Removed Points

These points are flagged to be removed, treat them with caution:

1. **Harsh critic's claim that the derivation is "fatal" and the entire method is unsound.** While Equation (2) is indeed problematic as presented, the overall approach — expressing KL divergence as a path integral of score-function differences along a CTMC that converges to a shared reference distribution — is a natural discrete analog of the well-established continuous-diffusion estimator (Franzese et al., 2023a, MINDE). The derivation can be fixed by writing the correct relationship: $\mathbb{E}[\log(p_T/q_T)(X_T)] - \text{KL}[p_0 \parallel q_0] = \mathbb{E}[\int_0^T (\partial_t f + \mathcal{B}[f]) dt]$ via Dynkin, noting that as $T \to \infty$ the terminal term vanishes (since $p_T, q_T \to \pi$), and rearranging. This is a presentation/clarity issue, not a fatal mathematical error. Retained as a Major weakness requiring clarification rather than dismissal of the entire contribution.

2. **Strength Finder's claim of "Rigorous CTMC-based KL estimator derivation."** The derivation is not rigorous as presented — Equation (2) contains an unjustified equality. Reclassified and addressed under Major weaknesses.

3. **Strength Finder's generic claim about "effective use of pretrained discrete diffusion backbones."** While true, this is an implementation convenience rather than a core contribution. Moved to supporting context rather than listed as a standalone strength.

4. **Various formatting/spelling/typographical issues flagged by the parser artifacts.** These are parser issues, not author errors. Removed.

## Novel Insights

The paper makes a genuine contribution by showing that the absorbing-state CTMC framework — originally developed for generative modeling — can be repurposed for information-theoretic estimation on discrete data with a single trained score model. The key enabling insight (Equation 6) is that under the absorbing-state design, marginal score ratios can be recovered from a joint model by conditioning on the absorbing state in the complementary variable. This is clever and practically valuable, and to my knowledge is novel in the context of MI estimation. The motif-discovery application (Figure 5) is also genuinely novel: unlike classifier-based methods, INFO-SEDD can assess motif importance via subset masking without interference from correlated motifs, a capability that directly follows from the estimator's design.

## Suggestions

- Rewrite Section 2.2 with a clear derivation: (1) state the definition of KL, (2) apply Dynkin's formula to $f = \log(p_t/q_t)$ going *forward* in time, (3) use the fact that $p_T, q_T \to \pi$ to drop the terminal term, (4) arrive at the integral estimator. Do not claim $\text{KL} = \mathbb{E}[\log(p_0/q_0)(X_T)]$.
- Fix the typo "$\vec{p}_0$ and $\vec{q}_0$ converge to $\pi$" → "$\vec{p}_T$ and $\vec{q}_T$ converge to $\pi$."
- Add a short discussion comparing the CTMC-based KL representation to the Girsanov-based approach in MINDE for continuous diffusions.
- Include a simple toy example (e.g., two binary variables) with analytically computable MI to validate the estimator in a fully controlled setting where every quantity can be computed exactly.

## Score and Decision

Calibration anchors:
- **MINDE** (0kWd8SJq8d, 6.50, Accept): Closest analog — continuous diffusion MI estimation by the same group. INFO-SEDD extends this to discrete CTMCs with stronger applications but has a less clear theoretical derivation.
- **SEDD** (71mqtQdKB9, 6.60, Reject): Foundational discrete diffusion paper that INFO-SEDD builds upon. INFO-SEDD has more complete experiments and a clearer application framing, though SEDD was more foundational.
- **Convergence of Score-Based Discrete Diffusion** (pq1WUegkza, 7.00, Accept): Theory paper on CTMC diffusion convergence with strong proofs. INFO-SEDD is more applied and has weaker theory presentation.
- **Efficient Perplexity Bound in Discrete Diffusion** (Mri9WIfxSm, 6.75, Accept): Extension of SEDD with cleaner theory and experiments. INFO-SEDD is at a comparable level of contribution.

Round 1 bracket: 5.5–7.0. Round 2 narrowed to 6.0–6.5. The paper's strong empirical results and practical contributions are weighed against the problematic derivation presentation. I place it at 6.0 — comparable to or slightly below MINDE, reflecting the extension to discrete domains but penalized for the unclear theoretical derivation that needs revision.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>
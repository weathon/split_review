Now I have all the information I need. Let me compile my analysis and write the review.

**Calibration Summary:**

**Round 1 Bracket:** Between 4 and 6. The paper is clearly above the 3.00 low-band (weak papers with unclear contributions) but below MINDE (6.50, Accept) which had a sound derivation.

**What the low-band anchors and weakness-anchored hits failed at, and does the paper share any of those failures?** The low-band anchors (3.00) failed due to unclear contributions and weak experiments — the current paper does NOT share those failures. However, the weakness-anchored hit KC2MViQASx (5.60, Reject — MI via f-Divergence) was rejected because of "discrepancies between claims and content": it claimed theoretical properties that the math didn't support. The current paper SHARES this failure: Equation (2) makes an unsupported mathematical claim, undermining the theoretical guarantees.

**Final Score: 4.0, Decision: Reject**

The paper has a genuine mathematical error in its core derivation (Equation 2), which invalidates the claimed theoretical guarantees. The experiments are strong and the practical design is clever, but the theoretical foundation is broken as presented. This gap between claimed theory and presented math is the same failure mode that led to rejection of KC2MViQASx at 5.60 — and the current paper's error is more fundamental (an actually wrong equation, not just overstated claims).

---

Now let me write the full review.## Summary

INFO-SEDD proposes a method to estimate KL divergences and mutual information for high-dimensional discrete data using Continuous Time Markov Chains (CTMCs) and score functions from discrete diffusion models. The key ideas include: (i) using Dynkin's formula to express KL divergence as an integral of score-ratio terms, (ii) leveraging an absorbing-state diffusion so that a single score model trained on the joint distribution can also compute marginal scores, and (iii) exploiting the structured (token-level) decomposition of the state space for tractability. The method is evaluated on synthetic benchmarks, text summarization, and genomics, showing strong empirical performance.

## Strengths

- **Impressive synthetic benchmark results (Table 1).** INFO-SEDD achieves estimates extremely close to ground-truth MI across the full range (MI=10, D=10 through MI=50, D=50) with low variance, while every competing neural/variational estimator (GAN-DIME, HD-DIME, KL-DIME, MINDE, MINE, NWJ, SMILE) exhibits large bias or collapses entirely. This directly supports the claim that the method handles high-dimensional discrete data in regimes where prior approaches fail.

- **Consistency with reference trends on real text and genomics data (Figures 1, 4).** On the text summarization consistency test, both INFO-SEDD variants closely follow the expected linear relationship between MI and ρ, while competitors either saturate at low values or fail for parts of the range. On the HUMAN vs. WORM genomics dataset, INFO-SEDD-C matches the classifier-based reference MI trend. These sanity checks establish that the method remains reliable outside synthetic settings.

- **Practical utility demonstrated via model selection (Table 2) and motif discovery (Figure 5).** INFO-SEDD-C achieves a Pearson correlation of 0.740 with the "consistency" human metric for summarization model selection — substantially higher than the next best competitor (HD-DIME at 0.331). The motif discovery experiment in *Arabidopsis thaliana* correctly identifies the known TATA-box region, providing a concrete biological application.

- **Scalable design via absorbing state and structured state space.** The paper shows how to compute marginal scores from a single joint model (Equation 6) using an absorbing-state CTMC, and how the structured (per-token) decomposition of the transition matrix avoids the O(|χ|^{2D}) complexity. This is a genuine engineering contribution that enables the method to be applied to sequences of hundreds of tokens without the "embedding trick."

- **Sample efficiency (Appendix C.1.5–C.1.6).** The method maintains accuracy with as few as 10³ training samples and remains robust to changes in support size |χ| where competitors fail.

## Weaknesses

### Fatal

None.

### Major

- **The derivation of the core estimator in Equation (2) is mathematically incorrect as stated.**  
  The paper writes:  
  `KL[p0 || q0] = E[log(p0/q0)(X_T)] = E[log(p_T/q_T)(X_T)]`.  
  The first equality is not the definition of KL divergence (which should involve X₀, not X_T) and is not justified. The second equality claims `E[log(p0/q0)(X_T)] = E[log(p_T/q_T)(X_T)]` without any supporting argument. In general, `KL[p0 || q0] ≠ KL[p_T || q_T]` (the data processing inequality says the opposite — KL can only decrease along the forward process). The subsequent sentence "We omit the term E[log(p0/q0)(X₀)], as both p₀ and q₀ converge to π" is also problematic: it is p_T and q_T that converge to the stationary distribution, not p₀ and q₀ (the initial conditions). This confusion makes the theoretical claims of consistency and the error bound in Equation (7) unsubstantiated from the derivation presented in the main text.

  **Why this is Major, not Fatal:** The estimator in Equation (5) could still be valid under a correct derivation using Dynkin's formula on `f(x,t) = log(p_t(x)/q_t(x))` — a standard approach in the continuous diffusion literature (Song et al. 2021, Franzese et al. 2023). The paper's Equation (4) may be recoverable from the correct path measure decomposition. However, as written, the paper does not provide that correct derivation, and the reader cannot verify the theoretical foundation. The experimental results suggest the method works, but the claimed theoretical guarantees do not follow from the presented math.

- **The error bound (Equation 7) contains an undefined constant and its derivation cannot be verified from the main text.**  
  The constant `C₁*` appears in the bound without definition or explanation in the main paper. The bound mixes score approximation errors (ε_p, ε_q) with a "truncation bias" term, but without precise definitions of C₁, C₂, C₁* and a clear derivation (deferred to Appendix E, which is stripped by the parser), the bound is not self-contained and cannot be evaluated. This is especially concerning because the estimator's derivation is itself unsupported, so the bound inherits that uncertainty.

### Minor

- **The justification for dropping the boundary term is garbled.** The paper states "We omit the term E[log(p0/q0)(X₀)], as both p₀ and q₀ converge to π." The boundary term that should be dropped is `KL[p_T || q_T]` (which becomes negligible as both distributions converge to π for large T), not `E[log(p0/q0)(X₀)]`. This mistake in the text, while likely just a typo/notation mix-up, contributes to the overall theoretical confusion and needs correction.

- **Experimental comparison has an inherent capacity asymmetry.** INFO-SEDD leverages large pretrained diffusion models (MDLM-SMALL, CADUCEUS) that have been trained on the data distribution, while competitors receive embeddings and must learn from scratch with smaller heads. The paper claims the same backbone architecture is used, which is true for the transformer trunk, but the discrete diffusion model's score function already encodes substantial distributional knowledge that the embedding-based estimators lack. This is an advantage of the method, not a flaw, but it makes head-to-head comparisons less about the MI estimation module and more about the representation quality. The paper acknowledges sharing the architecture but does not discuss this inherent advantage.

- **Limited ablation on the core estimator choices.** The paper evaluates two variants (INFO-SEDD-J and INFO-SEDD-C) but does not ablate key design decisions such as: the effect of the time horizon T on estimation accuracy, the sensitivity to the choice of the absorbing rate function σ(t), or the impact of the score approximation error on the final MI estimate. These would strengthen the empirical understanding of the method's behavior.

### Trivial

- In Equation (2), the notation `log(p0/q0)(X_T)` is ambiguous — it is unclear whether this means evaluating the initial density ratio at the terminal state X_T (which is mathematically unusual) or whether it is a typesetting artifact. The equation needs to be rewritten unambiguously.

## Nice-to-Haves

- A corrected derivation in the style of the continuous diffusion literature (path measure decomposition via Girsanov/Dynkin) with careful handling of the boundary term `KL[p_T || q_T]` and its convergence to zero. This would restore the theoretical credibility that the current presentation lacks.
- Wall-clock runtime and memory comparisons with competitors, so practitioners can assess the practical trade-offs.
- An ablation varying T to empirically demonstrate that the truncation bias decays as claimed.

## Removed Points

These points were flagged during consolidation but removed from the main weaknesses for the reasons given:

1. **"C₁* is undefined"** — The paper defers to Appendix E for the full derivation. Since the appendix is removed by the parser (a known artifact, not an author omission), this criticism is about missing appendix content, which should not be counted as a weakness. The main text should define C₁*, but the appendix likely does so.

2. **"Missing related work"** — Per instructions, missing related work should not be mentioned as a weakness since you cannot verify whether the paper actually cites them.

3. **"The error bound is vacuous without concrete bounds on ε_p, ε_q"** — This is a common feature of abstract error bounds that depend on approximation errors. It is standard practice to state such bounds with generic constants and leave the specific estimation of ε_p, ε_q to the application. Not a genuine weakness.

4. **"The method relies on pretrained models"** — This is presented as a *feature* of the method (seamless integration with pretrained models), and the paper does not claim to train these models from scratch. Criticizing this as a weakness is scope creep.

5. **Pure formatting/style nitpicks, complaints about missing code, and reproducibility concerns about trivial implementation details** — Removed per the filtering rules.

## Novel Insights

None beyond the paper's own contributions. The reviews surface few observations that the paper itself does not already state or imply.

## Suggestions

- **Rewrite the derivation (Section 2.2) from a correct starting point.** Begin with `KL[p0 || q0] = E_{X₀~p₀}[log(p₀(X₀)/q₀(X₀))]`, then apply Dynkin's formula to `f(x,t) = log(p_t(x)/q_t(x))` to obtain `KL[p0 || q0] = KL[p_T || q_T] - E[∫(∂f/∂t + B[f]) dt]`. Then argue that `KL[p_T || q_T] → 0` as T → ∞ because both distributions converge to the same stationary distribution π. This fixes the mathematical foundation and makes the estimator's relationship to the true KL clear. Equation (4) should then be shown to approximate the integral term.

- **Define all constants (C₁, C₂, C₁*) in the main text or give explicit references to where they are defined.** The error bound should be self-contained enough for a reader to understand what each term represents without consulting the appendix.

- **Add a controlled experiment where all methods use an embedding of the same dimension** (rather than INFO-SEDD using token-level scores while competitors use learned embeddings) to isolate the effect of the estimator design from the representation quality.

- **Include an ablation on T** to empirically verify the claim that the truncation bias decays exponentially, and show how the estimation accuracy varies with T.

## Score and Decision

**MY FINAL SCORE: <score>4.0</score>**
**MY FINAL DECISION: <decision>Reject</decision>**

### Calibration Anchors

| Anchor | Avg Score | Round / Bucket | Comparison to this paper |
|--------|-----------|----------------|--------------------------|
| 0kWd8SJq8d (MINDE) | 6.50 | R1-topic-mid, R2-top(5.5–7.0) | Continuous diffusion MI estimator with sound derivation. Significantly stronger theoretically, though also had presentation issues. |
| KC2MViQASx (f-DIME) | 5.60 | R1-weakness, R2-top(5.5–7.0) | MI via f-divergence, rejected for discrepancies between claims and math. Shares the same failure mode as this paper, but with a less fundamental error. |
| vgQmK5HHfz (NF-DoE) | 4.83 | R2-low(3.5–5.5) | Normalizing-flow MI estimator, rejected. Weaker experiments, comparable theoretical clarity issues. |
| 4u0ruVk749 (DFITE) | 3.00 | R1-topic-low | Weak paper with diffusion for treatment effect estimation — far lower quality in both theory and experiments. |
| 5sPgOyyjG5 (FKEE) | 3.00 | R1-topic-low, R1-weakness | Feynman-Kac estimator with unclear contribution. Much weaker overall. |
| pq1WUegkza (Discrete Diffusion Convergence) | 7.00 | R1-topic-high | Strong theory paper about discrete diffusion convergence. Higher quality, no derivation errors. |

**Calibration rationale.** Round 1 bracketing placed the paper between 4 and 6. The low-band anchors (3.00) are much weaker (unclear contributions, weak experiments) — the paper under review does not share those failures. The weakness-anchored hit KC2MViQASx (5.60, Reject) was rejected for "discrepancies between claims and content" — the current paper *does* share this failure: Equation (2) makes an unsupported mathematical claim, so the theoretical guarantees do not follow from the presented derivation. MINDE (6.50, Accept) had presentation issues but a sound derivation, making it a clearly stronger paper. Round 2 narrowed the bracket to 4.0–5.0. The final score of 4.0 reflects that the derivation error is genuine and undermines the theoretical contribution, while the strong experiments and clever practical design keep the paper above the reject-without-merit range. The paper could become viable after a major revision that corrects the derivation and clarifies the theoretical claims.
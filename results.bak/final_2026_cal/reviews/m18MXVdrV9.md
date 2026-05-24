Now I have everything I need. Let me write the final consolidated review.

## Summary

This paper introduces INFO-SEDD, a family of estimators for KL divergence, mutual information, and entropy designed specifically for high-dimensional discrete data. The method leverages Continuous Time Markov Chains (CTMCs) with absorbing-state rate matrices and requires training only a single parametric score model (via the DWDSE loss) to jointly estimate MI between arbitrary subsets of variables. A theoretical error bound guarantees consistency up to an exponentially decaying truncation bias. The method is evaluated on synthetic benchmarks (where it achieves near-exact MI estimates while all seven competing estimators fail), text summarization model selection (achieving Pearson correlation 0.74 with the consistency metric, far ahead of competitors), and genomics (TATA-box motif discovery).

## Strengths

1. **Empirically dominant on high-dimensional discrete MI estimation.** Table 1 is the strongest piece of evidence: INFO-SEDD achieves mean MI estimates within ~2% of ground truth across MI values 10–50 and dimensions 10–50, with low standard deviation, while all seven competitors (GAN-DIME, HD-DIME, KL-DIME, MINDE, MINE, NWJ, SMILE) exhibit large bias, high variance, or both. This directly supports the core claim that existing methods fail on discrete data and INFO-SEDD succeeds.

2. **Single-model architecture for joint and marginal scores.** Equation (6) establishes that with absorbing-state rate matrices, marginal score ratios can be extracted from a score model trained only on the joint distribution. This property — which follows from the absorption probability being independent of the token value in absorbing CTMCs — eliminates the need to train two separate models and is crucial for scalability. Verified against the paper's text and standard properties of absorbing CTMCs (Lou et al., 2024; Campbell et al., 2022; Austin et al., 2021).

3. **Consistent real-world performance on text and genomics.** On text summarization, both INFO-SEDD variants produce MI estimates that follow the theoretical ρ-linear trend derived from literature entropy rates, while competitors severely underestimate MI. On genomics (HUMAN vs. WORM), INFO-SEDD-C closely tracks a classifier-based reference MI curve in the low-MI regime (0–0.7 nats), where competitors produce erratic estimates.

4. **Practical utility for model selection.** INFO-SEDD-C achieves a Pearson correlation of 0.740 and Kendall's Tau of 0.505 with the "consistency" human metric for summarization — far higher than the next best competitor (KL-DIME at 0.214 Pearson). This demonstrates that MI estimated by INFO-SEDD provides meaningful signal for downstream tasks.

5. **Principled motif discovery without per-window retraining.** The genomics TATA-box experiment shows that INFO-SEDD-J can identify the known motif region (−39 to −26 from TSS) using a single trained model and sliding-window MI evaluation. This avoids the prohibitive cost of training separate estimators for each window.

## Weaknesses

### Major

1. **The derivation chain in Equation (2) is not mathematically rigorous as written.** The paper states: KL[p₀ ∥ q₀] = 𝔼[log(p₀/q₀)(X_T)] = 𝔼[log(p_T/q_T)(X_T)]. The first equality is not a standard identity — if X_T is sampled from the forward process starting from p₀, its distribution is p_T, not p₀, so 𝔼_{X_T~p_T}[log(p₀/q₀)(X_T)] ≠ KL[p₀∥q₀] in general. The second equality (replacing p₀/q₀ with p_T/q_T) is also not obvious. The correct derivation would apply Dynkin's formula to f_t = log(p_t/q_t), yielding KL[p₀∥q₀] = 𝔼[f_T(X_T)] − 𝔼[∫(∂f/∂t + Bf) dt], then argue the boundary term vanishes as T→∞. The paper's text after Equation (4) says "We omit the term 𝔼[log(p₀/q₀)(X₀)]" which is not the right boundary term in the Dynkin expansion. This presentation error does not invalidate the method — the final estimator (Equation 5) and the formal error bound (Equation 7) provide a separate justification path, and the empirical results strongly corroborate correctness — but the derivation must be corrected for the paper to be self-contained and trustworthy. The authors should provide a clean, step-by-step derivation explicitly connecting the KL to the integral of rate terms via Dynkin's formula and showing the vanishing boundary term.

### Minor

2. **Constants in the error bound (Equation 7) are not defined in the main text.** C₁, C₂, σ̄(T), and the score approximation errors ε_p, ε_q are referenced but defined only in the appendix (which is stripped). While this is common practice for theoretical bounds, the main text would benefit from at least stating what these constants depend on (e.g., boundedness of score functions, neural network capacity) so readers can assess whether the bound is informative.

3. **No confidence intervals for correlation coefficients in Table 2.** With only 15 data points (one per summarization model), the Pearson correlation of 0.740 could be unstable. Bootstrapped confidence intervals or a simple sensitivity analysis would substantially strengthen this result. Additionally, the paper does not check whether a trivial baseline (e.g., summary length) predicts consistency equally well — this is important to establish that MI adds value beyond simple proxies.

4. **The "theoretical trend" for the text consistency test is acknowledged as approximate but could be presented more carefully.** The 256–303 nats range is derived from character entropy rates (Takahira et al., 2016; Cover and King, 1978) multiplied by summary length, which assumes independence of characters. The linear-in-ρ trend is a coarse approximation. While the paper does not overclaim, the phrasing "closely matches" could be tempered.

5. **No discussion of training computational cost relative to baselines.** For large D and |χ|, training a CTMC score model may be expensive. A comparison of training time, number of parameters, or inference cost relative to the embedding-based competitors would help practitioners assess the trade-offs.

### Trivial

6. The paper refers to Appendix A.3 for the proof of Equation (6) and Appendix E for the bound derivation. These appendices could not be verified due to parsing — this is a formatting artifact, not an author error, but ensuring the main text is self-contained for the key claims would strengthen the presentation.

## Nice-to-Haves

- A comparison with a non-parametric baseline (e.g., summary length) for the model selection task, to establish that MI adds value beyond trivial proxies.
- Ablation showing how the finite time horizon T affects the MI estimates in practice (to ground the theoretical truncation bias).

## Removed Points

The following points from the inputs are removed:

- **Criticism that Equation (6) is insufficiently justified / the marginal score extraction may not hold.** *Reason for removal: This criticism is factually incorrect. In absorbing CTMCs with independent rate matrices per component, P(Y_t=∅|Y_0=y_0) = 1−e^{-σ̄(t)} is independent of y₀, so p_t(X_t=x, Y_t=∅) = (1−e^{-σ̄(t)})·p_t^X(x) and Equation (6) follows directly. This is a standard property of absorbing processes established in Lou et al. (2024), Campbell et al. (2022), and Austin et al. (2021).*

- **Criticism about MINDE being designed for continuous data.** *Reason for removal: The paper acknowledges this explicitly and uses it as a point of comparison to show the "embedding trick" fails. This is not a weakness — it's a controlled experiment designed to demonstrate the limitation of continuous methods on discrete data.*

- **Criticism that the genomics experiment does not quantitatively compare against alternative MI estimators.** *Reason for removal: The experiment's purpose is to demonstrate motif discovery as a downstream capability of INFO-SEDD, not to benchmark MI estimation accuracy on this task. The paper notes that other estimators would need separate training runs per window, making the comparison impractical. The consistency test (Figure 4) already provides the quantitative comparison.*

- **Strength Finder's generic strengths about "important problem" / "useful benchmark" etc.** *Removed as generic, superficial, or not specific to the paper's concrete contributions.*

## Novel Insights

None beyond the paper's own contributions. The key technical insight — that absorbing CTMCs allow single-model extraction of both joint and marginal scores for MI estimation — is well articulated in the paper itself.

## Suggestions

1. **Rewrite the derivation leading from Equation (2) to Equation (4).** Provide a clean, explicit chain: apply Dynkin's formula to f_t = log(p_t/q_t), obtain KL = 𝔼[f_T(X_T)] − 𝔼[∫(∂f/∂t + Bf) dt], then argue that 𝔼[f_T(X_T)] → 0 as T→∞ because both p_T, q_T → π. This replaces the currently sloppy equalities with a rigorous argument and clarifies what is being approximated.

2. **Add confidence intervals to the correlation analysis (Table 2).** A simple bootstrap (e.g., 1000 resamples) would give the reader a sense of uncertainty for the 0.74 Pearson value.

3. **Define C₁, C₂, and σ̄(T) briefly in the main text** when introducing Equation (7), even if the full derivation stays in the appendix.

4. **Report computational cost** (training time, model size, inference time) for INFO-SEDD vs. each baseline.

5. **Verify that a trivial baseline (e.g., summary length) does not predict consistency as well as INFO-SEDD's MI.** This is a quick check that would substantially strengthen the model selection claim.

## Score and Decision

**Calibration anchors used:**

| Anchor ID | Avg Score | Round | Comparison |
|-----------|-----------|-------|------------|
| f70HHKXnEC | 2.00 | 1 (weak) | Weak paper withdrawn after review; INFO-SEDD is significantly stronger |
| mjLMdY0xul | 3.33 | 1 (weak) | Diffusion language model paper; INFO-SEDD has more extensive evaluation |
| IaeZcYpRxD | 3.00 | 1 (weak) | Rejected; INFO-SEDD has far stronger empirical support |
| y8Kzu9SKpv (InfoBridge) | 5.00 | 1 (mid) | Most similar: both use diffusion for MI estimation. INFO-SEDD has stronger empirical results (Table 1), native discrete support, and real-world applications, but InfoBridge has a cleaner derivation |
| 1taAXRcm21 (Discrete Unification) | 6.00 | 1 (mid), 2 (narrow) | Discrete diffusion theory paper with limited experiments. INFO-SEDD has more extensive experiments but less polished theory presentation |
| rAjHUNXybH | 7.33 | 1 (strong) | Strong theory paper; INFO-SEDD is not at this theoretical depth |
| EFYb8SsRi7 (Error Analysis) | 6.50 | 2 (narrow) | Rejected due to lack of experiments; INFO-SEDD has the opposite strength (strong empirical, weaker theory presentation) |
| 4uTZobABec (IEM) | 7.00 | 2 (narrow) | Clean theory + good experiments; INFO-SEDD is weaker on theory presentation |

**Round 1 bracket:** Between 3.5 and 7.5, narrowed to 5–7.  
**Round 2 narrowing:** Comparing directly to InfoBridge (5.00) — INFO-SEDD is stronger on empirical evidence and real-world applications but weaker on derivation cleanliness. Comparing to the discrete unification paper (6.00) — INFO-SEDD has stronger experiments but less polished theoretical exposition. The error analysis paper (6.50, rejected) was rejected for lack of experiments, which is not INFO-SEDD's problem. The main weakness (sloppy Equation (2) derivation) is real but fixable and does not invalidate the method.

**Final score:** 6.0 — solid accept. The paper delivers a genuinely useful new tool for MI estimation on discrete data, backed by extensive and convincing experiments. The derivation presentation needs fixing, but the core method is sound and the empirical validation is strong.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>
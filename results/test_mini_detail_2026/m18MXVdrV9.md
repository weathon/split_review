## Summary

This paper introduces INFO-SEDD, a method for estimating mutual information (MI) and KL divergences for high-dimensional discrete data using Continuous-Time Markov Chains (CTMCs). The key idea is to express the KL divergence as an integral that can be estimated via score functions learned by discrete diffusion models, and to use an absorbing-state design that allows a single trained score model to provide both joint and marginal estimates. The method is evaluated on synthetic benchmarks, text summarization (model selection via MI), and genomics (motif discovery), consistently outperforming variational competitors that rely on embedding tricks.

## Strengths

- **Novel and well-motivated approach.** The paper identifies a genuine gap — neural MI estimators for high-dimensional *discrete* data are underdeveloped, and the common "embedding trick" is unsatisfactory. Bridging discrete diffusion (CTMCs) with MI estimation is a timely and promising direction.

- **Clever absorbing-state design for single-model efficiency.** Equation (6) and the surrounding discussion show that by choosing an absorbing transition matrix, marginal score ratios can be obtained from a model trained only on the joint distribution. This is a clean theoretical insight that reduces training cost and directly supports the paper's claim of scalability.

- **Strong empirical results on synthetic benchmarks.** Table 1 demonstrates that INFO-SEDD consistently outperforms eight competitors (GAN-DIME, HD-DIME, KL-DIME, MINDE, MINE, NWJ, SMILE) across MI values 10–50 with dimensionality 10–50, achieving both the most accurate estimates and the lowest standard deviations (e.g., 39.11±0.65 vs. 33.97±3.32 for the next best at MI=40). The gap grows as MI increases, which is precisely where variational methods are known to fail.

- **Consistency on real-world text data.** Figure 1 shows that both INFO-SEDD variants follow the expected linear trend (MI ≈ 256–303 nats × ρ) across ρ=0.0–1.0, while competitors severely underestimate. This provides credible evidence that the method works on real high-dimensional discrete data, not just synthetic setups.

- **Practical utility demonstrated in two application domains.** The model selection experiment (Table 2, Figures 2–3) shows that INFO-SEDD-C achieves a Pearson correlation of 0.740 with consistency, higher than any competitor, demonstrating that MI estimates are useful for evaluating summarization models. The motif discovery experiment (Figure 5) localizes the TATA-box in *Arabidopsis thaliana* promoters at the biologically expected position (−39 to −26 relative to TSS), providing a concrete scientific application.

- **Theoretical consistency bound with error decomposition.** Equation (7) provides a formal bound that separates estimation error (scaling with score approximation error) from truncation bias (decaying exponentially with T), establishing that INFO-SEDD is a consistent estimator up to an exponentially decaying bias.

## Weaknesses

### Fatal
None.

### Major

- **Incomplete and potentially flawed derivation of the KL estimator in §2.2.** Equation (2) states:
  $$\text{KL}[\vec{p}_0 \parallel \vec{q}_0] = \mathbb{E}[\log \tfrac{\vec{p}_0}{\vec{q}_0}(\vec{X}_T)] = \mathbb{E}[\log \tfrac{\vec{p}_T}{\vec{q}_T}(\vec{X}_T)]$$
  where $\vec{X}_T \sim \vec{p}_T$ (the process is initialized from $\vec{p}_0$). As written, $\mathbb{E}[\log(p_0/q_0)(X_T)] = \int p_T(x)\log(p_0(x)/q_0(x))\,dx$, which is not generally equal to $\text{KL}[p_0\|q_0] = \int p_0(x)\log(p_0(x)/q_0(x))\,dx$. The paper does not justify why this equality holds. The subsequent justification for omitting a term ("as both $\vec{p}_0$ and $\vec{q}_0$ converge to $\pi$") is also unclear, since $\vec{p}_0$ and $\vec{q}_0$ are the *initial* distributions, which do not converge to anything — it is the processes $\vec{p}_t$ and $\vec{q}_t$ that converge to $\pi$ as $t\to T$. Because the paper advertises the method as principled and the derivation is central to the contribution, this gap is significant. The ≈ in Equation (4) may signal the authors are aware of an approximation, but the text does not clarify the nature of this approximation or its error. The derivation needs to be either corrected or clearly scoped as an approximation with a controlled error. (The appendix, which would contain the full derivation, is stripped from the review copy, but the main text must stand on its own for this core claim.)

- **The error bound constants are not interpretable from the main text.** Equation (7) introduces $C_1^*$, $\bar{\sigma}(T)$, $C_1$, $C_2$ without defining them in the main body. $C_1^*$ appears in the bound but only $C_1$ (without the asterisk) is mentioned in the preceding sentence. $\bar{\sigma}(T)$ is defined later in the entropy section (as $\int_0^t \sigma(s)ds$) but not in the context of the bound. This makes the bound a black box for readers who do not chase the appendix. While relegating proofs to the appendix is standard, the *meaning* of the key terms should be interpretable from the main text.

### Minor

- **The claim that competing estimators "take more epochs to converge" is unsupported in the main text.** The paper states this in §4.1 and references Appendix C.1.3, but the main text would benefit from a brief quantitative summary (e.g., "INFO-SEDD converged in X steps vs. Y steps for GAN-DIME").

- **The comparison to competitors in the text summarization experiment involves an asymmetry that is acknowledged but not discussed.** Competitors require learning an embedding lookup table on top of the same backbone, while INFO-SEDD works directly on tokens. The paper notes this (line 144) but does not discuss whether this asymmetry could affect the comparison. Given that the asymmetry adds parameters to the baselines (which might help or hurt), a brief discussion would strengthen the fairness analysis.

- **No quantitative comparison to existing motif-hunting tools in the genomics experiment.** The paper demonstrates that INFO-SEDD can localize the TATA-box, but does not compare against dedicated motif discovery methods (e.g., MEME, HOMER) or even simpler baselines. This would strengthen the claim that the method is "invaluable" for motif discovery.

- **The paper claims the method is "unique" (Conclusion), which is overstated.** There are other score-based approaches to discrete information estimation (e.g., extensions of MINDE), and the sentence should be qualified.

- **$C_1^*$ vs. $C_1$ notation inconsistency in Equation (7).** The text defines $C_1, C_2$ as boundedness constants, but the bound uses $C_1^*$ (with asterisk). This appears to be a notation issue.

### Trivial
None.

## Nice-to-Haves

- A discussion of when the factorized rate matrix assumption (single-token updates) might limit applicability, e.g., for data with hierarchical structure that cannot be captured by per-component transitions.
- A wall-clock time or training-step comparison between INFO-SEDD and competitors in at least one setting, to substantiate the "efficient" claim.
- A comparison to a simple discrete plug-in estimator (e.g., with Miller-Madow bias correction) to concretely show the degradation that motivates neural approaches.
- Guidance on when to prefer the J vs. C variants, beyond what is already stated (the paper does discuss this to some extent — §4.3 explains that C is better for low-dimensional labels).

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Synthetic data construction is opaque"** (Harsh Critic, Critical Issue #2): The paper states "full details are in Appendix C.1" and gives a brief description in the main text (§4.1). Deferring construction details to the appendix is standard practice. The speculation that the construction might "artificially favor" the proposed method is not grounded in any evidence from the paper and is removed.

- **"Competitors are disadvantaged by needing embedding lookup tables"** (Harsh Critic, §4.2): The asymmetry favors the baselines (they get additional learned parameters), not INFO-SEDD. Per the rules, criticisms about unfair comparison are removed when the asymmetry favors the baseline.

- **"KL-DIME and SMILE exhibit approximately linear correlation but get low MI values"** framed as a weakness: This is a result, not a weakness of the paper — it shows that INFO-SEDD outperforms these methods.

- **"The comparison methodology disadvantages competitors"** (Harsh Critic, §4.2): Already addressed above — the asymmetry favors baselines.

- **Generic/speculative concerns from the harsh critic** about the Dynkin formula derivation being "glossed over" or "assumed" without evidence: The specific claim about Equation (2) being incorrect is retained and verified. The sweeping claim that "the entire estimator rests on this representational claim" and that "the theoretical foundation is suspect" is retained in substance but the language is toned down to match what is verifiable from the paper.

- **Strength Finder's "Principled KL estimator from CTMC theory"** (Core Strength #1): This strength is overstated given the derivation issues in §2.2. The approach is *motivated* by CTMC theory, but the derivation as presented is incomplete. This strength is downgraded.

## Novel Insights

None beyond the paper's own contributions. The main observation that emerges from the reviews is that the paper's empirical contributions are substantially stronger than its theoretical exposition. The derivation of the core estimator (Equation 2 → Equation 5) is not clearly justified, yet the empirical results (synthetic, text, genomics) are consistent with the method being correct and effective. This suggests the derivation may be salvageable with a proper rewrite, but as presented the paper's claims outpace its mathematical justification.

## Suggestions

1. **Rewrite §2.2 with a clean derivation.** Start from a correct representation of the KL divergence (e.g., as a path measure ratio using Girsanov for CTMCs, or as a lower bound), clearly state whether the estimator is exact or approximate, and if approximate, bound the approximation error. The current Equation (2) is not justified and should be replaced.
2. **Define all constants in the error bound (Equation 7) in the main text.** $C_1^*$, $\bar{\sigma}(T)$, $C_1$, $C_2$ should be interpretable without reading the appendix.
3. **Add a brief quantitative convergence comparison** in the main text for at least one synthetic setting.
4. **Tone down the "unique" claim** in the conclusion and add a brief limitations paragraph discussing when the single-token-update assumption may be restrictive.
5. **Fix the $C_1^*$/$C_1$ notation inconsistency** in Equation (7).

## Score and Decision

### Calibration Anchors

**Round 1 — Bracketing (topic: "mutual information estimation discrete data diffusion"):**
- **Weak anchors (avg < 3.5):** f70HHKXnEC (2.00, Withdrawn), IaeZcYpRxD (3.00, Reject), x3c4um7jJX (3.00, Reject), liVX9If9k2 (2.50, Reject) — These are all clearly weaker than the paper under review (less novel, less empirical depth, or more limited scope).
- **Middle anchors (avg 3.5–7.5):** y8Kzu9SKpv (InfoBridge, 5.00, Accept Poster), 4uTZobABec (7.00, Accept Poster), dB6DYLpjw4 (5.33, Reject), 1taAXRcm21 (6.00, Accept Poster) — The paper under review is comparable to but slightly weaker than InfoBridge (5.00) due to the theoretical derivation gap, and clearly below the 6.00–7.00 anchors.
- **Strong anchors (avg > 7.5):** Ahdsg2nkNH (8.00), nCsF3Bsn2n (8.00), RDerF20JYT (8.00), qOyF214xmg (8.00) — The paper under review is not at this level.

**Initial bracket:** 3.5 – 6.0

**Round 2 — Narrowing (within bracket):**
- y8Kzu9SKpv (InfoBridge, 5.00, Accept Poster) — Most directly comparable paper. Both propose diffusion-based MI estimators. InfoBridge has stronger theoretical justification (the unbiasedness claim was well-received) but weaker empirical scope (standard benchmarks only). INFO-SEDD has weaker theory but broader real-world validation (text summarization, genomics, Ising models). Comparable overall, with INFO-SEDD slightly below due to the §2.2 derivation gap.
- GgPNq4pzsI (4.50, Accept Poster) — Evidence estimation via diffusion priors. Less directly comparable.
- azJnEkfqzp (Discrete Markov Bridge, 4.50, Reject) — Rejected for weak theoretical guarantees despite a promising idea. INFO-SEDD has stronger empirical evidence but a similar theoretical-weakness pattern. INFO-SEDD is somewhat stronger due to its broader experimental validation and practical utility demonstrations.
- 7wbrFQvfdH (Inference-Time Scaling Discrete Diffusion, 6.00, Accept Poster) — Has rigorous derivations and comprehensive experiments. INFO-SEDD is clearly below this level.

**Final calibration:** The paper is closest to InfoBridge (5.00) but with a more significant theoretical gap. It is stronger than the Discrete Markov Bridge paper (4.50, Reject) because its empirical validation is more extensive and includes real-world utility. I place it at 4.5 — this is a paper with a genuinely interesting idea and strong empirical support, but the core theoretical derivation needs substantial revision before the claims match the evidence.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>
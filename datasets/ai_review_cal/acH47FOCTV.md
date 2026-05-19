- Decision: Reject
- Avg Score: 5.50
- Scores: 6, 6, 5, 5
Now I have all the information I need to verify the reviewer claims. Let me cross-check each claim systematically.

**Verification of key critic claims against the paper:**

1. **DreamerV3 parameter count**: Paper states DreamerV3 has ~200M params (line 178). Critic says "DreamerV3 (~20M parameters)" — this is factually WRONG (confused with DreamerV2). **REMOVED.**

2. **Rainbow at 200M vs 20M**: The paper states: "For Rainbow, we simply report its score at 200 million training frames" and their method at 20M. The critic says no Rainbow at 20M is provided — this is factually correct. However, the paper also provides DreamerV2 and DreamerV3 at 20M, which the critic acknowledges as "more appropriate." This is a valid observation but the paper is transparent about the comparison.

3. **Runtime measurements**: The critic says "no runtime measurements... or wall-clock comparisons are provided" for the computational cost claim. I confirm: no runtime data appears in the paper. The paper says "negligible computational cost" (line 136) without measurements. Valid criticism.

4. **Confounding experiment**: The critic says it uses only two truncation lengths and no statistical significance test. The paper shows results across 5 games, 2 truncation lengths, 10 seeds. The critic says "the effect is tiny in most games" and the evidence doesn't support strong conclusions. The paper's language is actually hedged ("suggests," "may be"). This is a valid but somewhat overstated criticism.

Now let me produce the final review.

---

Let me think about the overall assessment:

**Originality**: The paper extends Off-policy DAE to POMDPs and proposes a latent dynamics approximation to avoid observation reconstruction. This is a conceptually clear extension with practical value.

**Importance**: Sample-efficient RL in partially observable environments is an important problem. The confounding issue identified is also practically relevant.

**Claims well supported**: The theoretical extension (Proposition 1) is clean and well-supported. The sample efficiency claims are supported by experiments on 5 Atari games with 10 seeds each. The computational cost reduction claim lacks runtime measurements. The confounding finding is supported by consistent but small effects.

**Soundness of experiments**: The Atari-5 subset is justified by Aitchison et al. (2023). 10 seeds with standard errors are reported. The protocol follows Dopamine/Machado et al. Standard practices.

**Clarity**: Well-written, clear structure.

**Value**: The method is useful and the confounding insight is practical. 

Score: I'd say about 7.0. The paper has clear contributions, the main claims are supported, and the weaknesses are relatively minor (missing runtime measurements, imperfect Rainbow comparison). It's a solid paper that would benefit from additional experiments but is not fatally flawed.

Decision: Accept.Here is my consolidated final review.

---

## Summary

This paper extends Off-policy Direct Advantage Estimation (DAE) to partially observable environments (POMDPs), showing that the theoretical decomposition of returns into policy advantage (A) and environment luck (B) generalizes naturally by replacing states with histories. To address the computational cost of enforcing the B constraint (which requires modeling transition probabilities), the authors propose learning a discrete latent dynamics model in a low-dimensional embedding space using a Winner-Takes-All / conditional VQ-VAE objective, avoiding costly observation reconstruction. They also identify and empirically demonstrate a confounding bias that arises when naively truncating trajectories in recurrent RL. Experiments on 5 Atari games show that the method scales with model capacity and achieves sample efficiency competitive with or better than DreamerV2/V3 and Rainbow.

## Strengths

- **Clean theoretical extension to POMDPs (Proposition 1, Appendix A).** The paper proves that Off-policy DAE generalizes to partially observable environments by replacing states with histories and transition probabilities with conditional densities of observations and rewards. The proof is concise and follows directly from reformulating a POMDP as an MDP over information vectors. This provides a principled foundation for DAE beyond the MDP setting.

- **Practical latent-dynamics approximation that avoids observation reconstruction (Section 3.1, Eq. 11–12).** The paper combines a Winner-Takes-All loss with a conditional VQ-VAE to model transitions in a low-dimensional embedding space rather than reconstructing high-dimensional pixels. This directly addresses the ~7× runtime overhead reported in prior Off-policy DAE work (Pan and Schölkopf, 2024). Shallow MLPs for the dynamics are shown to be sufficient, and end-to-end training is feasible.

- **Sample efficiency and scalability demonstrated on Atari (Table 1, Figure 3).** With a sufficiently scaled model (m=8, ~50M parameters), the method achieves scores comparable to DreamerV3 in 3/5 games using only 20M frames (DreamerV3 was trained for 200M frames) and consistently outperforms DreamerV2. The paper also shows that the off-policy correction (the B term) is critical for good scaling — disabling it degrades performance substantially.

- **POMDP correction (LSTM) outperforms frame-stacking (Figure 5).** The LSTM-based agent (which uses histories) outperforms the frame-stacking agent (MDP approximation) in 3/5 environments while matching it in the remaining two, with context length controlled across both settings. This provides direct evidence that the POMDP extension is beneficial over the standard MDP simplification.

- **Identification and empirical demonstration of confounding from truncated trajectories (Section 3.2, Table 2).** The paper identifies a subtle but commonly overlooked bias: when the behavior policy uses longer histories than the truncated training policy, the truncated variables can act as confounders. Across all 5 games and 2 truncation lengths, aligning the behavior policy's truncation with the target policy yields consistent (small) performance degradation, suggesting practitioners should be aware of this issue.

## Weaknesses

### Major

None.

### Minor

- **Imperfect Rainbow comparison for the sample-efficiency claim.** The paper reports Rainbow at 200M frames while the method is evaluated at 20M frames, then claims "can achieve similar performance while using only 10% of the training frames." Rainbow results at 20M frames are not provided, making it unclear whether Rainbow would already reach those scores after 20M. The paper does provide DreamerV2/V3 at 20M comparisons, which partially addresses this, and it transparently notes the asymmetric evaluation. Still, the central sample-efficiency claim would be better supported by including Rainbow at the same training budget.

- **No runtime or wall-clock measurements for the computational cost claim.** The paper motivates the latent dynamics approach by the high cost of observation reconstruction and claims that shallow MLPs achieve "negligible computational cost," but provides no runtime data (frames per second, epoch time, or parameter counts for the dynamics model vs. the full system) to support this. Since the computational cost reduction is listed as a core contribution, the lack of quantitative evidence weakens this claim. However, note that the paper's primary empirical claims are about sample efficiency, not computational efficiency.

- **The confounding experiment, while interesting, is supported by small effects without statistical testing.** Table 2 shows consistent performance drops across 5 games and 2 truncation lengths, but the relative differences are modest (1–6%) and no statistical significance tests are reported. The paper's language is appropriately hedged ("suggests," "may be"), but stronger evidence (e.g., paired tests, confidence intervals, or a third truncation length) would bolster the conclusion that "the ALE may be more partially observable than previously believed."

### Trivial

- Hyperparameter details (learning rates, optimizer settings, batch size, buffer size, burn-in length) are described in prose but would benefit from a single centralized table for reproducibility.
- The comparison in Figure 5 (LSTM vs. frame-stacking) is framed as "a comparison between the POMDP version of DAE and its MDP counterpart," but the LSTM agent additionally has the latent dynamics model, so the comparison is not a pure test of POMDP vs. MDP treatment of histories. The paper acknowledges this by controlling context length, but the framing could be more precise.

## Nice-to-Haves

- A direct comparison between the proposed latent dynamics approach and the original reconstruction-based CVAE approach (on a small scale) would more cleanly validate the computational cost reduction.
- An analysis of the learned latent dynamics quality (e.g., accuracy of next-embedding predictions, coverage of the discrete latent code) would strengthen the claim that the model captures environment stochasticity.
- Generalization to one or two non-ALE partially observable domains would increase the breadth of the empirical evaluation.

## Removed Points

The following points from the reviews were removed with justification:

- **Critic claimed that "the paper's largest model (50M parameters) is substantially larger than DreamerV3 (~20M parameters)."** The paper explicitly states DreamerV3 has ~200M parameters (line 178). The critic confused DreamerV2 (~20M) with DreamerV3. This is factually incorrect and removed.
- **Critic claimed the LSTM vs. frame-stacking comparison "conflates multiple changes" and is not an accurate POMDP-vs-MDP comparison.** The paper controls for context length (both use length-4 truncation for action selection) and states both use DAE objectives. The comparison is cleanly scoped to how histories are processed. The critic's framing mismatch concern is not substantiated.
- **Critic urged "marginal return per parameter" as a fairer scaling comparison.** This is not standard practice in the field and demands analysis outside the paper's stated scope.
- **Various reproducibility nitpicks about undisclosed hyperparameters** are standard for the field; the paper provides adequate architectural detail.
- **Strength Finder claimed "computational cost reduction via embedding-space dynamics" as a core strength without noting the missing runtime evidence.** This is still a valid architectural contribution (avoiding observation reconstruction), but the strength is retained with adjusted framing. The runtime-evidence gap is noted as a weakness instead.
- **Strength Finder's generic sycophantic strengths** (e.g., "addressed an important problem") were removed as insufficiently concrete.

## Novel Insights

The most interesting insight from the review process is the interplay between the two reviewed weaknesses: the missing Rainbow-at-20M baseline and the missing runtime measurements both stem from the same underlying issue — the paper overclaims what the experiments directly support. The Rainbow comparison implicitly compares across a 10× frame gap without controlling for the baseline at the same budget, and the computational cost claim is asserted without measurement. Neither flaw is fatal, but together they mean the paper's most attention-grabbing statements ("10% of the frames," "negligible computational cost") are the least well-supported. The paper's genuine strengths — the theoretical POMDP extension, the latent dynamics architecture, and the confounding insight — do not depend on these headline claims and would be better served by presenting them more cautiously.

## Suggestions

1. Provide Rainbow evaluation at 20M frames for the primary comparison tables.
2. Add a simple wall-clock or FPS comparison between the proposed latent dynamics approach and a reconstruction-based CVAE variant on a representative subset.
3. For the confounding experiment, include a brief statistical comparison (e.g., paired bootstrap confidence intervals across seeds) and discuss why even small effects are practically relevant.
4. Consolidate all hyperparameters (optimizer, learning rate, batch size, buffer capacity, burn-in length, gradient clipping, target network update frequency) into a single table in the main paper or appendix.

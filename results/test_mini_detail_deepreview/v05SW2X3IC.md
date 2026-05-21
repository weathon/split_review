Now I have all the information I need. Let me construct the final review.

## Summary

This paper proposes a learnable three-channel codec inspired by the Gray-Wyner network from information theory. The architecture uses one common channel and two private channels to disentangle shared from task-specific information in two-task compression settings. The authors provide theoretical bounds on lossy common information (Theorem 1), derive a practical optimization objective with a single hyper-parameter β controlling the transmit-receive tradeoff (Theorem 2, Eq. 12), and design a split/combine mechanism (Eq. 14) for the encoder. Experiments on synthetic data, colored MNIST variants, Cityscapes (segmentation+ depth), and COCO (detection+ keypoint) demonstrate that the method outperforms an independent-coding baseline and approaches the performance of a joint-coding upper bound.

## Strengths

- **Theoretical grounding for lossy common information bounds (Theorem 1, Eqs. 6–7).** The paper extends Wyner's lossless result to the lossy case, bounding Gács-Körner and Wyner common information via interaction information. This is a non-trivial adaptation that provides formal limits for the approach. (Section 3.1)

- **Principled optimization objective derived from theory (Theorem 2, Eq. 10 → Lagrangian in Eq. 12).** Under the assumption of deterministic functions, the Gray-Wyner objective reduces to entropy terms, yielding a clean loss function with a single tradeoff parameter β. This bridges the theoretical Gray-Wyner framework with practical neural network training. (Section 3.2)

- **Novel architecture with explicit common-channel masking (Eq. 14).** The split/combine mechanism — where private representations are split, matching elements are averaged, and non-matching elements are zeroed out — is an elegant and non-trivial design. The auxiliary loss (Eq. 15) with the γ hyperparameter and the strategy of controlling channel usage solely via β is a practical contribution. (Section 3.3, Figure 2)

- **Edge-case validation on controlled mutual information (Section 4.2, Figure 4).** The colored MNIST experiments with Dependent, Independent, and Mixture PMFs verify that the common-channel rate behaves as information theory predicts: high when tasks share information, low when they do not. This directly validates that the network isolates common information, not just that it compresses well.

- **Consistent BD-rate improvements on real vision tasks (Section 4.3, Figure 5).** On Cityscapes, the proposed method achieves a BD-rate improvement of ~120% over the Independent baseline in transmit rate; on COCO the improvement is ~64%. These are large, practically relevant gains.

## Weaknesses

### Major

- **No comparison against existing multi-task codecs from the literature.** The paper cites Chamain et al. (2021), Feng et al. (2022), and Guo et al. (2024) as prior work on multi-task codecs, yet compares only against a self-designed Joint baseline (one shared channel, no private channels). While the cited methods do not include private channels (so they solve a different problem), comparing against at least one published implementation would substantiate the claim of practical advantage. The Joint baseline is a reasonable conceptual comparison but does not anchor against existing engineering choices. The core contribution does not depend on beating these methods, but absent the comparison, the reader cannot assess whether the three-channel design offers real-world gains over existing practice.

- **Architecture ablation not conducted on real tasks.** The synthetic experiment (Section 4.1) compares Shared, Separated, and Combined encoder architectures, convincingly showing the Shared design is best. However, on the two real task pairs (Section 4.3), only the Shared architecture is evaluated against Joint and Independent. The reader cannot verify that the architectural choice is actually responsible for the gains on real tasks versus a simpler alternative. The optimal architecture on synthetic data may not transfer to large-scale settings.

### Minor

- **No statistical variance or multiple runs reported.** All experiments appear to be single runs with no error bars, confidence intervals, or multiple seeds. For deep compression models which are known to have training stochasticity, this limits the reliability of the quantitative claims. Most individual comparisons (e.g., Shared vs. Separated in Figure 3) would be more convincing with variance estimates.

- **Theorem 1 is an incremental extension.** The paper states it "extend[s] a result from Wyner (1975) in the lossless setting to the lossy case." While the extension is non-trivial (requiring careful handling of rate-distortion-achieving tuples), the structure follows the known lossless argument. The result is useful but not surprising. The paper does not empirically validate the bounds (e.g., by computing interaction information on the synthetic data and checking whether it falls between the two bounds).

### Trivial

- The Independent baseline's training details (joint vs. separate training of the two codecs) are not fully specified. This matters because joint training with a shared optimizer could affect the comparison. The code availability (github.com/adeandrade/research) partially mitigates this.

## Nice-to-Haves

- A sensitivity study on γ (Eq. 15) would clarify the claim that γ = 1 with β tuning is sufficient. The paper argues that "small γ might result in elements never matching" and "large γ can result in degenerate distributions," but does not show supporting experiments (e.g., a sweep of γ while holding β fixed).
- An analysis of common-channel utilization (e.g., fraction of non-zero elements in Y₀ after training) would help the reader understand when and how the common channel is actually used across different β settings.
- Empirical validation of Theorem 1's bounds on the synthetic data (computing interaction information for the transmit-optimal and receive-optimal tuples) would strengthen the theory-experiment connection.

## Removed Points

- **"The proof is in the appendix and cannot be evaluated here"** — Removed per the rule that appendix-stripping is a parser artifact, not an author error.
- **"The 81.58% BD-rate advantage is not directly traceable"** — Removed. The number is approximately traceable: Cityscapes transmit BD-rate vs. Independent = −83.78%, COCO = −82.99%, average ≈ −83.4%. The small difference from −81.58% is within rounding/multi-experiment averaging.
- **"The Joint method is not a previously published approach"** — Removed per the rule that the asymmetry favors the baseline (Joint is simpler, not more complex). Joint is a standard single-channel codec baseline.
- **Strength Finder: "Architecture justification via compatibility measure"** — Retained as a supporting strength (Section 3.3, Appendix C reference). The compatibility measure is a genuine theoretical argument for the design.

## Novel Insights

None beyond the paper's own contributions. The harsh critic and strength finder did not surface insights about the paper that the authors do not already articulate.

## Suggestions

1. **Add at least one existing multi-task codec as a baseline** on the real tasks (e.g., Guo et al. 2024 or a re-implementation of Chamain et al.). Even if the comparison is imperfect (different private-channel structure), it situates the contribution.
2. **Report results over 3–5 random seeds** with error bars on the rate-distortion curves. This is the single highest-impact improvement for experimental credibility.
3. **Add the Separated and Combined architectures** to the real-task experiments (Figure 5) to verify that the architectural choice matters at scale.
4. **Empirically validate Theorem 1** on the synthetic data by computing interaction information for the transmit-optimal and receive-optimal tuples and checking that they bound the interaction information of the β=3/2 tradeoff point.

## Score and Decision

**Calibration anchors used (all rounds):**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| `gIrVoQEDQv.md` (NCA compression) | 3.40 | R1 | Much weaker — flawed method, trivial experiments |
| `6j0GH40mFt.md` (Window attn compression) | 3.40 | R1 | Weaker — incremental architecture change, limited novelty |
| `hrXt6Fdl2P.md` (FV-NeRV) | 2.60 | R1 | Much weaker — unclear contribution |
| `f47c05mcOj.md` (Log-exp perturbations) | 3.00 | R1 | Much weaker — narrow scope |
| `x33vSZUg0A.md` (Taskonomy multi-task compression) | 5.33 | R1/R2 | Similar quality — both have strong framing but incomplete baselines. Current paper has stronger theory; Taskonomy paper has broader task coverage |
| `Piod76RSrx.md` (Slicing MI bounds) | 5.50 | R1/R2 | Similar — both have theoretical contributions with incomplete experimental validation |
| `aQ7qYnY2nF.md` (RL rate control) | 4.00 | R1/R2 | Weaker — limited novelty, missing baselines. Current paper has more theoretical depth |
| `bsnRUkVn63.md` (TTA compression) | 6.00 | R1 | Stronger — cleaner experiments with consistent scores. Current paper is less experimentally thorough |
| `CxXGvKRDnL.md` (Progressive diffusion) | 8.00 | R1 | Much stronger — full system with rigorous evaluation |
| `hrqNOxpItr.md` (Cross-entropy identifiability) | 8.00 | R1 | Much stronger — deep theoretical contribution |
| `bH6T0Jjw5y.md` (T-IB) | 8.00 | R1 | Much stronger |
| `Tzh6xAJSll.md` (Scaling laws) | 7.60 | R1 | Much stronger |
| `cbv0sBIZh9.md` (Diffusion multi-task) | 5.75 | R2 | Slightly stronger — cleaner experiments |
| `UB03wcP8RH.md` (Multitask contrastive) | 5.25 | R2 | Similar — comparable rigor |
| `yVGGtsOgc7.md` (Disentangling reps) | 5.80 | R2 | Slightly stronger — theoretical guarantees |
| `vdUYaN8Mt.md` (Rate-distortion-perception) | 5.50 | R2 | Similar — good theory, limited application validation |
| `VkWbxFrCC8.md` (RECOMBINER) | 6.67 | R2 | Stronger — thorough experiments |
| `jznbgiynus.md` (Language modeling is compression) | 6.00 | R2 | Stronger — clear, well-executed |
| `Dolm7rrrQd.md` (Bias in neural compression) | 4.25 | R2 | Weaker — analysis-only, no method proposal |
| `KgJwbsfN7G.md` (MambaVC) | 4.80 | R2 | Weaker — incremental architecture swap. Current paper has more novel contribution |

**Round 1 bracket:** 4.0–6.0. **Round 2 narrowing:** The paper compares best with the Taskonomy multi-task compression (5.33) and the Slicing MI bounds (5.50) papers in terms of overall quality level: all have real contributions coupled with notable experimental limitations. The paper is clearly stronger than the 4.00–4.80 papers and weaker than the 5.75–6.67 papers. After anchoring, the paper is most comparable to the 5.33 and 5.50 anchors.

**Final score: 5.0**

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Accept</decision>
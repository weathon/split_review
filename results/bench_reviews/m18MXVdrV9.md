Now I have enough to write the final review. Let me synthesize everything.

---

## Summary

INFO-SEDD introduces a method for estimating information-theoretic quantities (KL divergence, mutual information, entropy) on high-dimensional discrete data using Continuous-Time Markov Chain (CTMC) diffusion models. The key idea is applying Dynkin's formula to express KL divergence as an integral over the forward CTMC process, with the required probability ratios supplied by score networks trained via the DWDSE loss. An absorbing-state design allows a single score model to compute both joint and marginal scores, enabling scalable MI estimation and seamless integration with pretrained discrete diffusion backbones. The method is validated on synthetic benchmarks (where it dramatically outperforms variational competitors at high MI and dimensionality), text summarization model selection, genomics motif discovery, and Ising model entropy estimation.

## Strengths

- **Strong and convincing synthetic results (Table 1)**: INFO-SEDD produces estimates extremely close to ground truth at high MI and dimensionality (e.g., 47.77 ± 1.18 nats for MI=50, D=50) while all competitors collapse — GAN-DIME reaches only 17.27, HD-DIME 10.47, and variational methods saturate near log(batch_size). This is the cleanest evidence for the method's effectiveness, using identical MLP backbones for all methods, isolating the estimation methodology.

- **Elegant theoretical framework**: The connection between CTMC theory (Dynkin's formula) and KL divergence estimation is well-motivated. The error bound (Equation 7) cleanly decomposes estimation error into a term linear in score-network error plus an exponentially decaying truncation bias, and the consistency argument in Appendix E is properly laid out under reasonable boundedness assumptions.

- **Single-model efficiency via absorbing-state design**: The absorbing transition matrix (Section 3, Equation 6, Appendix A.3) allows a single score model trained on the joint distribution to compute marginal scores as well. This is a genuine practical contribution — it avoids training separate models and enables direct integration with pretrained discrete diffusion backbones like MDLM-small and CADUCEUS.

- **Meaningful real-world applications**: The text summarization consistency test (Figure 1) shows INFO-SEDD-C closely tracking the expected linear MI trend while competitors either saturate or fail. The model selection experiment (Table 2) demonstrates that INFO-SEDD-C MI estimates correlate meaningfully with human consistency judgments (Pearson 0.740, Kendall 0.505). The Ising model entropy estimation (Appendix D.1) accurately recovers analytical entropy across temperatures.

- **Well-organized and clearly written**: The progression from CTMC fundamentals through the estimator derivation to practical algorithms is logical. The distinction between joint (INFO-SEDD-J) and conditional (INFO-SEDD-C) variants is clearly explained, and pseudocode in Appendix B aids reproducibility.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **Motif discovery experiment lacks quantitative rigor (Section 4.3, Figure 5)**: The TATA-BOX identification in *Arabidopsis thaliana* promoters is presented as evidence for scientific discovery, but the experiment has no error bars, no null distribution test (e.g., shuffled sequences), no comparison to alternative motif discovery methods, and no statistical significance assessment. The MI values in the profile are small (0.02–0.12 nats), making it difficult to distinguish signal from noise without uncertainty quantification. The paper's core contributions do not hinge on this experiment, but the discovery claims should be appropriately tempered.

- **Model selection correlations use a small sample (n=15) without statistical testing (Table 2)**: The Pearson and Kendall correlations between MI estimates and human metrics are computed over only 15 models. At this sample size, correlation estimates have wide confidence intervals — for instance, the difference between INFO-SEDD-C's Pearson correlation of 0.740 and KL-DIME's 0.214 with consistency may or may not be statistically significant. Reporting confidence intervals or p-values would clarify which comparisons are reliable.

- **INFO-SEDD-J shows non-zero bias at ρ=0 in text consistency test (Figure 1)**: When texts and summaries are fully independent (ρ=0), MI should be zero, but INFO-SEDD-J produces non-zero estimates. The paper acknowledges this difference from INFO-SEDD-C but does not investigate the source of bias. This does not invalidate the method (INFO-SEDD-C works correctly at ρ=0, and INFO-SEDD-J's bias appears small relative to the MI scale at higher ρ), but understanding the bias source would strengthen the method.

- **Real-world experiments have an inherent pretraining asymmetry**: In the text and genomics experiments, all methods use the same pretrained backbone (MDLM-small, CADUCEUS) with similar parameter counts. However, INFO-SEDD's DWDSE training objective naturally aligns with the pretraining task, while competitors must adapt — they use embedding look-up tables and different loss functions. This asymmetry is inherent to the method's design (discrete-native estimation is the whole point) and does not invalidate the results, but it means these experiments conflate estimation quality with pretraining alignment. The synthetic experiments (identical MLPs, trained from scratch) already isolate the estimation advantage cleanly, so this is a caution about overinterpretation rather than a fatal confound.

### Trivial

- The truncation bias bound (Equation 7) is stated in terms of constants C₁, C₂ and →p_T(∅ᴰ) that are not numerically instantiated for the reported experiments. Computing these values would give readers confidence that the chosen T values adequately control bias.

## Nice-to-Haves

- A controlled text/genomics experiment where INFO-SEDD and competitors all train from scratch on the same backbone (no pretrained weights) would isolate the estimation methodology from pretraining effects in the real-world domains. However, this is a substantial undertaking and the synthetic experiments already serve this purpose.
- A null distribution test for the motif discovery experiment (shuffled sequences) would transform it from a qualitative demonstration to a proper validation.
- Extension to conditional MI or other information-theoretic quantities beyond MI and entropy would demonstrate the generality of the CTMC framework.

## Removed Points

These points are flagged to be removed — treat them with caution. They were present in reviewer input but found to be incorrect or invalid upon verification against the paper.

- **"Equation (5) is not a valid KL divergence estimator — DWDSE scores estimate reverse-time ratios while forward-time ratios are needed"**: This is factually incorrect. The DWDSE-trained score s_θ(X_t)_x estimates the ratio of forward-time marginal probabilities p_t(x)/p_t(X_t), which is exactly what Equation (5) requires. The change of variables from reverse to forward process in Appendix A.1 (line 2176: ←p_t = →p_{T-t}, τ = T - t) correctly transforms the integral. The harsh critic confused the time at which scores are evaluated in the reverse generative process (T-t) with what the scores represent (forward-time ratios at that time).

- **"The absorb-state factorization in Appendix A.3 assumes independence that fails for state-dependent finite-time CTMCs"**: This misunderstanding confuses the forward perturbation process with the learned reverse process. The factorization applies to the forward perturbation process which uses a fixed absorbing rate matrix Q_t^tok = σ(t)Q_absorb — each component independently jumps to ∅ at rate σ(t), making the factorization valid by construction. The learned score is only used during estimation, not during the forward process where the factorization is applied.

- **"Text/genomics experiments are fundamentally confounded — INFO-SEDD uses pretrained models while baselines train from scratch"**: The paper explicitly states that all methods use the same pretrained backbones (MDLM-small for text, CADUCEUS for genomics) with minimal architectural changes and similar parameter counts (Section 4.2, line 652-655; Section 4.3, line 849-851). The remaining asymmetry (INFO-SEDD's objective aligns better with pretraining) is inherent to the discrete-native vs. embedding-trick distinction that the paper sets out to evaluate.

- **"The claim that MINDE struggles with discrete data is unsubstantiated"**: Figure 1 and the text experiments show MINDE failing to provide meaningful MI estimates on discrete text data (~10⁻² to 10¹ nats, no linear trend). This is consistent with the paper's claim.

- **"The KL divergence between p_T and q_T term is omitted assuming T→∞, introducing unaccounted bias"**: The paper uses the ≈ symbol in Equation (4) precisely because of this approximation, and the truncation bias is explicitly analyzed and bounded in Equation (7) and Appendix E.2. This is correctly handled.

- **Formatting nitpicks, typo complaints, grammar issues**: These are parser artifacts, not present in the original submission.

- **Missing related works**: Cannot verify without external sources.

## Novel Insights

The key insight that distinguishes INFO-SEDD from prior diffusion-based MI estimators (like MINDE, which uses continuous SDEs) is that discrete CTMC diffusion with an absorbing transition matrix yields a structural property (Equation 6) enabling marginal score computation from a single joint model. This property has no continuous analog — in continuous diffusion, the marginal scores of a joint distribution cannot be recovered from the joint score alone. This makes INFO-SEDD uniquely suited to discrete data and is what enables the practical efficiency gains (single model, pretrained backbone integration) that the paper demonstrates.

## Suggestions

- Add confidence intervals to Table 2 correlation values (bootstrap over the n=15 models) so readers can assess which method comparisons are statistically meaningful.
- Add a shuffled-sequence null distribution to Figure 5 to distinguish the TATA-BOX MI peak from noise.
- In the main text (Section 2.2), make the change of variables τ = T - t explicit when going from the reverse-process expectation to Equation (4), rather than deferring it entirely to Appendix A.1. This is the conceptually critical step.
- Numerically compute the truncation bias bound for one representative experiment (e.g., compute →p_T(∅ᴰ) for the chosen T and report the bound) to give readers confidence that T is adequate.

---

**Anchor comparison for score calibration:**

- `/home/wg25r/review_agent/human_reviews_2026/y8Kzu9SKpv.md` (InfoBridge, avg 5.00, Accept Poster): Similar diffusion-based MI estimation paper. INFO-SEDD has more comprehensive experiments, a cleaner theoretical framework with explicit error bounds, and stronger synthetic results. **INFO-SEDD is noticeably stronger.**

- `/home/wg25r/review_agent/human_reviews_2026/JodkBXWgbA.md` (CPC Done Right, avg 6.00, Accept Poster): A crisp theoretical contribution fixing InfoNCE for MI estimation. Similar quality tier — clean idea, well-executed experiments. INFO-SEDD is more ambitious in scope and has more diverse applications, but CPC has fewer rough edges. **Comparable quality.**

- `/home/wg25r/review_agent/human_reviews_2026/dB6DYLpjw4.md` (FlashMI, avg 5.33, Reject): Pretrained hypernetwork for MI estimation. Limited to low-dimensional evaluation and lacks theoretical depth. **INFO-SEDD is clearly stronger.**

- `/home/wg25r/review_agent/human_reviews_2026/4uTZobABec.md` (IEM, avg 7.00, Accept Poster): Clean theory + practical application of score-based distance metric. More polished theoretically than INFO-SEDD and with stronger experimental validation in its domain. **IEM is somewhat stronger**, particularly in theoretical completeness.

- `/home/wg25r/review_agent/human_reviews_2026/rAjHUNXybH.md` (Computational Bottlenecks, avg 7.33, Accept Poster): A different kind of paper — rigorous computational theory. **Not directly comparable; represents a higher tier of theoretical contribution.**

- `/home/wg25r/review_agent/human_reviews_2026/f70HHKXnEC.md` (Information Flow in Diffusion, avg 2.00, Withdrawn/Reject): Fundamental problems with experimental validation and weak contributions. **INFO-SEDD is far stronger.**

INFO-SEDD is clearly above the 5.0 acceptance threshold (stronger than InfoBridge and FlashMI), comparable to CPC Done Right (6.0), but not at the level of IEM (7.0) in terms of theoretical polish. The synthetic results are genuinely strong, the absorbing-state design is clever, and the weaknesses are minor and addressable.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>
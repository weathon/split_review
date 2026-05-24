Now I have enough information to write the consolidated review. Let me put it all together.

## Summary
2-3 sentence summary of the paper's contribution.

## Strengths
- strength 1 with evidence
- strength 2 with evidence

## Weaknesses
### Fatal
### Major
### Minor
### Trivial

## Nice-to-Haves
## Removed Points
## Novel Insights
## Suggestions
## Score and Decision

Let me write this up.

Score: 6.0

Decision: Accept

Now let me list all anchors I've retrieved:

Round 1 (Bracketing):
- gIrVoQEDQv - "Unraveling Neural Cellular Automata for Lightweight Image Compression" - score 3.40 - reject, unrelated topic
- hrXt6Fdl2P - "FV-NeRV: Neural Compression for Free Viewpoint Videos" - score 2.60 - reject, unrelated
- S3zKrEQpRr - "Unleashing the Information Flow: Graph Neural Networks are Noisy Communication Channels" - score 3.00 - reject, unrelated
- 4JtwtT4nYC - "Multi-Task Reinforcement Learning with Shared-Unique Features" - score 3.00 - reject, unrelated
- YrxhSkfHh0 - "Fast and Scalable Method for Efficient Multimodal Feature Extraction" - score 3.33 - reject, unrelated
- DsMxVELk3K - "TextEconomizer" - score 3.00 - reject, unrelated
- x33vSZUg0A - "Which Tasks Should Be Compressed Together?" - score 5.33 - accept, directly related multi-task compression
- yVGGtsOgc7 - "Disentangling Representations through Multi-task Learning" - score 5.80 - accept, related
- 6Ey8mAuLiw - "On the Power of Multitask Representation Learning with Gradient Descent" - score 5.25 - reject, related
- xbXydoejvY - "CWPS: Efficient Channel-Wise Parameter Sharing" - score 4.75 - reject, related
- cbv0sBIZh9 - "Diffusion Models for Multi-Task Generative Modeling" - score 5.75 - accept, related
- xVBXz7wD2m - "GatedMTL" - score 5.25 - reject, related
- hrqNOxpItr - "Cross-Entropy Is All You Need To Invert the Data Generating Process" - score 8.00 - accept, unrelated
- bH6T0Jjw5y - "Latent Representation and Simulation of Markov Processes via T-IB" - score 8.00 - accept, unrelated
- CxXGvKRDnL - "Progressive Compression with Universally Quantized Diffusion Models" - score 8.00 - accept, unrelated
- gc8QAQfXv6 - "Unlocking the Power of Function Vectors" - score 9.00 - accept, unrelated
- STUGfUz8ob - "When can transformers reason with abstract symbols?" - score 7.60 - accept, unrelated
- agPpmEgf8C - "Predictive auxiliary objectives in deep RL" - score 8.00 - accept, unrelated

Round 2 (Narrowing):
- Piod76RSrx - "Slicing Mutual Information Generalization Bounds" - score 5.50 - reject, unrelated
- jznbgiynus - "Language Modeling Is Compression" - score 6.00 - accept, somewhat related
- afQuNt3Ruh - "Entropy Coding of Unordered Data Structures" - score 6.25 - accept, related
- x33vSZUg0A - already seen at 5.33
- eePww5u7J3 - "Swiss Army Knife" - score 6.40 - accept, related
- 3n4RY25UWP - "An Information Criterion for Controlled Disentanglement" - score 6.25 - accept, related
- Pe3AxLq6Wf - "What to align in multimodal contrastive learning?" - score 6.25 - accept, related
- kQCHCkNk7s - "AstroCompress" - score 6.25 - accept, related

Round 2b (extra refinement):
- bsnRUkVn63 - "Test-time Adaptation for Image Compression" - score 6.00 - accept, related
- jznbgiynus - already seen
- afQuNt3Ruh - already seen

My bracket: Round 1 I found the paper sits between the weak anchors (~3-5) and strong anchors (~8+). The most directly comparable anchor is "Which Tasks Should Be Compressed Together" at 5.33. That paper had more baselines but was less well-motivated theoretically. This paper has better theory and cleaner experiments but fewer baselines. I'd rate this paper as slightly stronger than that anchor, putting it around 6.0.

Comparing to the 6.0-6.4 range anchors ("Language Modeling Is Compression" at 6.0, "Entropy Coding of Unordered Data Structures" at 6.25, "Swiss Army Knife" at 6.40, "An Information Criterion for Controlled Disentanglement" at 6.25): these papers have cleaner empirical evaluations (more baselines, error bars) but are less directly related to the paper's contribution. The current paper's theoretical contribution (Theorem 1) and architecture are more substantial than many of these, but its empirical evaluation is weaker (missing baselines, no error bars). So 6.0 is a fair score.

Let me write the review now.Now I have all the information needed. Let me synthesize the final review.

## Summary

This paper proposes a learnable implementation of the Gray-Wyner network for multi-task compression, connecting classical information-theoretic constructs (Wyner's and Gács-Körner lossy common information) to a practical deep learning architecture. The key contributions are: (1) Theorem 1 extending Wyner's lossless bound on common information to the lossy case, providing bounds relating the two common information measures via interaction information; (2) a β-parameterized Lagrangian objective (Eq. 12) that navigates the transmit-receive rate tradeoff; (3) a novel architecture with an explicit "mask" mechanism and auxiliary loss that forces compatible common representations across branches; and (4) empirical validation on synthetic data, colored MNIST, Cityscapes, and COCO showing the method reduces redundancy compared to independent coding.

## Strengths

**1. Novel theoretical extension of lossy common information bounds.** Theorem 1 (Eqs. 6–7) extends Wyner's lossless result to the lossy setting, bounding Gács-Körner and Wyner common information via interaction information. This provides a principled foundation for the transmit-receive tradeoff that the rest of the paper operationalizes.

**2. Principled β-parameterized optimization objective.** The Lagrangian in Eq. 12, where β=1 optimizes transmit rate and β=2 optimizes receive rate, is a clean instantiation of the Gray-Wyner objective for neural networks. The controlled experiments (Figs. 3c, 3d) show that β=1.5 achieves competitive performance on both transmit and receive rates, confirming the theoretical prediction.

**3. Novel architecture with explicit common-channel alignment.** The matching operation (Eq. 14) and auxiliary loss (Eq. 15) are a clever mechanism to force the two branches to produce compatible common representations. The ablation study (Fig. 3b) shows the proposed Shared architecture systematically outperforms Separated and Combined alternatives across all β settings.

**4. Controlled edge-case validation.** The colored MNIST experiments (Fig. 4) with three PMFs (Dependent, Independent, Mixture) convincingly demonstrate that the codec adapts as theory predicts: fully dependent tasks use the common channel heavily (low transmit rate), independent tasks bypass it (low receive rate), and the mixture case falls between. This shows the architecture behaves correctly under extreme conditions.

**5. Strong BD-rate results on real vision tasks.** On Cityscapes, the Proposed (Transmit) achieves BD-rate +23.32% vs. the Joint baseline, compared to +143.69% for Independent coding. On COCO, the Proposed (Transmit) achieves +13.16% vs. +77.36% for Independent. These are substantial improvements that demonstrate the practical value of the approach.

## Weaknesses

### Major

**1. No SOTA multi-task compression baselines.** The paper surveys existing multi-task compression methods (Chamain et al., 2021; Feng et al., 2022; Guo et al., 2024) in Section 2 but does not include any of them in the experimental comparison. The "Independent" and "Joint" baselines are naive extremes — they bound the problem but do not answer whether the proposed GWN architecture offers a practical advantage over existing multi-task compression designs. Without SOTA comparison, the reader cannot distinguish between the strength of the method and the weakness of the chosen baselines. This is the most significant limitation, especially for the vision experiments (Section 4.3) where the practical claims are strongest.

**2. Centralized parallel evaluation vs. distributed sequential motivation.** The paper motivates a sequential query scenario (Introduction: transmit common info first, add private channels when new tasks are requested), but evaluates a fully parallel, jointly trained codec. The receive rate metric (2R₀+R₁+R₂) measures a weighted sum of jointly learned rates, not the system operating in the intended sequential protocol. The paper does **not** verify that the common channel can be transmitted alone and subsequently augmented with private channels without retraining. This creates a gap between the motivating narrative ("efficient distributed inference") and the evidence presented. (That said, the transmit/receive metrics do capture the theoretical costs of the sequential scenario, and validating the full sequential pipeline would strengthen but not invalidate the paper.)

**3. Theory–architecture assumption gap.** The theoretical development (Sections 2.1, 3.1) relies on strict Markov separability conditions (Eq. 1): Z₂↔X₂↔X₁ and Z₁↔X₁↔X₂. Yet Section 3.3 explicitly states the architecture "effectively removes the requirement for the conditions in 1" because each branch has access to both sources. The paper acknowledges this, but does not explain how the theoretical bounds (Theorem 1) carry over when the core assumptions are violated. This creates a coherence issue between the theoretical justification and the implemented system.

### Minor

**4. No statistical significance or error bars.** Single BD-rate values are reported without confidence intervals or multiple-run statistics. Given the sensitivity of learned codecs to hyperparameters, this limits the reliability of the quantitative comparisons. (This is common practice in the learned compression literature, but the omission is worth noting.)

**5. Unclear "single-task codec" baseline in Conclusion.** The claim of "a BD-rate advantage of -81.58% in transmit rate, against single-task codecs" does not specify which baseline this is compared to (from context, it appears to be the Independent method). The text should state this explicitly to avoid ambiguity.

**6. Depth RMSE scaling not described.** The paper states "The depth RMSE is scaled so its inverse is in a similar scale as the segmentation mIoU" (Fig. 5 caption) but does not describe the scaling operation, which is critical for interpreting Figure 5a's combined performance metric.

### Trivial

**7. The claim about β values outside [1,2] being "suboptimal" (Section 3.2) is presented as theoretical but is justified only by the structure of the Gray-Wyner region, not by a formal statement for the lossy case.**

## Nice-to-Haves

- **Validate the sequential query protocol**: Train the full codec, freeze the common encoder and decoders, then measure whether task 1 can be served from (Y₀, Y₁) and task 2 from (Y₀, Y₂) without retraining the common part. This would directly demonstrate that the Gray-Wyner decomposition is operational.
- **Include at least one SOTA multi-task compression baseline** (e.g., Chamain et al. or Guo et al.) on Cityscapes or COCO to position the practical performance.
- **Add ablation on β** (beyond the synthetic experiments) for the vision tasks showing sensitivity of the transmit/receive tradeoff.

## Removed Points

- **Criticism about the existence/release status of models/tools**: Removed per hard rule — the paper cites existing works; questioning release status is a reviewer knowledge gap.
- **"Typos, formatting artifacts, missing appendix content"**: Removed per hard rules — these are PDF parser artifacts, not author errors.
- **"The paper would need to include a user study"**: Not standard for this type of algorithmic contribution; removed.
- **Strength Finder's generic strengths** ("the problem is important", "this paper addresses an interesting question"): Removed as generic/superficial per filtering discipline.
- **Harsh critic's comment about "missing proofs in appendix"**: The appendix is stripped by the parser; these exist in the original submission. Removed per hard rule.
- **"The paper should discuss three or more tasks"**: The paper explicitly scopes this out (Section 5, "extensions to three or more tasks are possible but…"). Removed as scope creep.

## Novel Insights

The most interesting cross-cutting observation from the reviews is that the **mask mechanism** (Eq. 14) — which zeros out mismatched elements between Y₀⁽¹⁾ and Y₀⁽²⁾ while averaging matched ones — is simultaneously the paper's most novel architectural contribution and the source of its main theoretical tension. The mechanism is what makes the common-channel alignment work in practice, yet it is precisely the mechanism that violates the Markov conditions required for the theory. This tension suggests a natural direction for future work: can the mask be derived from, rather than imposed on, an information-theoretic objective? The paper's Theorem 1 bounds provide the "what" of the common information decomposition; the mask provides a "how" that works in practice; connecting the two more tightly would strengthen both.

## Suggestions

1. **Add SOTA baselines** — include at least one existing multi-task compression method (e.g., Chamain et al.) on the Cityscapes experiment to demonstrate practical advantage.
2. **Resolve the theory–architecture gap** — add a paragraph discussing how the theoretical bounds (Theorem 1) inform or approximately bound the architecture's behavior despite the relaxed assumptions.
3. **Clarify the "single-task codec" baseline** in both the figure captions and the Conclusion.
4. **Describe the depth RMSE scaling** operation used in Figure 5.

## Score and Decision

**Round-1 bracket (initial): 5.0 – 7.0**

After the bracketing pass, the most directly comparable anchor was "Which Tasks Should Be Compressed Together?" (avg score 5.33, reviews: 8/5/3) — a multi-task compression paper with more baselines but weaker theoretical foundations. The current paper has a stronger theoretical contribution (Theorem 1, the β-formulation) and cleaner controlled experiments, but weaker baselines. This placed it above 5.33 but below the 6.4–8.0 range of papers with more comprehensive empirical evaluations.

**Round-2 narrowing anchors used:**
- "Which Tasks Should Be Compressed Together?" (5.33) — weaker theory, more baselines; current paper is stronger.
- "Disentangling Representations through Multi-task Learning" (5.80) — different setting (disentanglement theory), mixed reviews; current paper has stronger applied validation.
- "Language Modeling Is Compression" (6.00) — perspective paper on LLM compression, different methodology; comparable in signal-to-noise ratio and novelty.
- "An Information Criterion for Controlled Disentanglement" (6.25) — similar in having strong theory + empirical gaps; current paper has stronger architecture contributions.
- "Entropy Coding of Unordered Data Structures" (6.25) — clean theory + thorough evaluation (benchmarks, error bars); current paper's theory is stronger but evaluation is less thorough.

The paper is clearly above the 5.0–5.5 range of papers with weak evaluations or no theoretical grounding. It falls a bit short of the 6.5+ range because of the missing SOTA baselines and the evaluation gap (sequential motivation vs. parallel evaluation). The theoretical contribution (Theorem 1) and the well-designed controlled experiments (synthetic data, colored MNIST) are strong and distinctive.

**Final score: 6.0** — a solid accept with real contributions, where the authors should address the SOTA baseline gap and the theory–architecture coherence issue in the final version.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>
Now I have all the evidence I need. Let me synthesize the final review.

## Summary

The paper proposes IRIS, the first reinforcement learning framework for autoregressive text-to-image generation that uses only an intrinsic reward — negative self-certainty (NSC) — without any external human labels, reward models, or domain-specific verifiers. The central finding is that, contrary to language reasoning where maximizing self-certainty helps, minimizing self-certainty (i.e., maximizing uncertainty) improves image generation quality by encouraging visually richer outputs. Experiments on Janus-Pro 1B/7B show IRIS achieves results competitive with external-reward methods (T2I-R1) on GenEval, T2I-CompBench, and WISE, while requiring no external supervision.

## Strengths

- **First intrinsic-reward RL method for T2I generation.** IRIS is the first framework to demonstrate that autoregressive T2I models can be improved via RL using only an intrinsic signal (NSC), without human preferences or domain-specific verifiers (Tab. 1, Fig. 3). This opens a new direction for scalable alignment of generative visual models.

- **Task-dependent behavior of self-certainty is convincingly demonstrated.** Figure 2 shows a clean, opposite trend: external-reward training *increases* text self-certainty in LLMs (math reasoning) but *decreases* image self-certainty in multimodal LLMs (T2I generation). This empirical finding is interesting in its own right and directly motivates the IRIS design.

- **Systematic and well-designed ablation study.** Figures 5–9 separately test: (a) training with/without semantic CoTs, (b) minimizing vs. maximizing image SC, (c) minimizing vs. maximizing text SC, (d) forward vs. backward KL, and (e) RL optimization vs. direct gradient ascent. All ablations consistently support the design choices, providing strong internal validity for the claims.

- **Competitive performance with zero external supervision.** On Janus-Pro-1B, IRIS improves GenEval (+9.1%), T2I-CompBench (+13.3%), and WISE (+28.8%) over the base model, and the overall scores are within 1–3% of the external-reward baseline T2I-R1 (Table 1). Given that IRIS uses no external signal, this is a meaningful achievement.

## Weaknesses

### Fatal
None.

### Major

- **Overclaiming in the central comparative claim.** The abstract states IRIS achieves performance "competitive with or superior to external rewards." The claim "superior to" is not supported by the overall averages in Table 1: on Janus-Pro-1B, IRIS scores *lower* than T2I-R1 on all three benchmarks (GenEval: 0.72 vs. 0.75; T2I-CompBench: 0.3793 vs. 0.3820; WISE: 0.37 vs. 0.38). The text at line 144 states "IRIS surpasses the T2I-R1 on 1B models in" with the qualifier ("categories biology, physics, chemistry within natural science of the WISE benchmark") separated by a page break — in context, this is a qualified claim about specific WISE subcategories where the advantage is actually marginal (Physics: 0.45 vs. 0.43; Biology and Chemistry: tied). The framing should be corrected to match the evidence: IRIS is *competitive with* external rewards, with particular strength in knowledge-based categories, while lagging on aesthetics and spatial relations.

### Minor

- **Limited architecture generality.** The method is only tested on Janus-Pro (an autoregressive model). The paper acknowledges this in Sec. 4.4 and states that diffusion/masked architectures are future work. While this honesty is appreciated, the title and abstract present IRIS as a general framework, yet the empirical evidence is limited to one architecture family.

- **Missing intrinsic-reward baselines.** The paper compares NSC against backward KL (entropy) in Fig. 8, showing forward KL is better. However, it does not compare against other natural intrinsic objectives such as token-level probability variance, diversity-promoting repulsion terms, or simple maximum-entropy regularization within the same RL framework. While the backward-KL comparison partially covers this space, additional baselines would strengthen the claim that the specific forward-KL formulation is necessary or optimal.

- **The "optimize without RL" ablation (Fig. 9) has an expected outcome.** The direct NSC maximization baseline lacks GRPO's advantage normalization and clipping. The paper acknowledges this, but the ablation compares an RL-trained model against a stripped-down variant whose collapse is unsurprising. A fairer comparison would apply some form of variance reduction to the direct optimization baseline.

- **No analysis of why minimizing text SC helps.** The paper speculates that minimizing text SC encourages diverse CoTs and exploration, but provides no quantitative evidence (e.g., CoT lexical diversity, entropy, or semantic usefulness metrics). This mechanism claim remains unsupported.

- **Regression on counting is not discussed.** On GenEval's counting category, IRIS drops from 0.50 (T2I-R1) to 0.41 on Janus-Pro-1B and from 0.55 to 0.52 on 7B. Understanding when and why NSC harms numerical reasoning would be instructive.

### Trivial

- Figure 2 plots text SC (range 31–38) and image SC (range 19–20.5) on separate y-axes, which is appropriate for showing trends but makes the visual "decrease" appear less dramatic. A normalized overlay would improve readability.

- The "IRIS surpasses T2I-R1" sentence is broken across a page boundary (lines 144 and 209-211), making the qualifier easy to miss.

## Nice-to-Haves

- Test IRIS on at least one non-autoregressive T2I architecture (e.g., a diffusion-based model) to support the generality claim.
- Add quantitative diversity analysis (e.g., LPIPS distance between samples from the same prompt) to verify the mechanism.
- Report the distribution of NSC values for good vs. poor images to illustrate the proposed signal.
- Include failure case analysis, particularly for the counting regression.
- Compare against a simple entropy-maximization baseline within the same GRPO framework to isolate the advantage of forward-KL.

## Removed Points

- **Fig 2 axis scale criticism**: The reviewer argued the axis scales make the decrease less dramatic. The paper correctly uses separate y-axes because text and image SC operate at different absolute scales; the direction of change is what matters. Removed as a nitpick.

- **Chat template correction criticism**: The reviewer argued that fixing the template makes baseline numbers unverifiable against prior work. This is a strength (careful experimental hygiene), not a weakness. Removed.

- **"Optimize without RL is a strawman"** (as a major weakness): The paper explicitly explains why GRPO works and direct optimization fails. The ablation is informative even if the outcome is expected. Moved to Minor.

- **Ablation evaluation using same reward models**: The paper explicitly states these models are used only as evaluation metrics, not training objectives. The main benchmarks (GenEval, T2I-CompBench, WISE) are fully independent. This is adequately addressed. Removed as a standalone criticism.

- **Missing appendix/references/proofs**: Parser-stripped content, not author errors. Removed per instructions.

## Novel Insights

None beyond the paper's own contributions. The key insight — that self-certainty should be *minimized* for T2I generation in contrast to *maximized* for text reasoning — is well articulated and empirically supported by the paper itself.

## Suggestions

1. **Correct the framing**: Replace "superior to" with "competitive with" in the abstract unless superiority on specific subcategories is explicitly qualified. The sentence about "surpassing T2I-R1 on 1B models" (line 144) should immediately reference the qualified subcategories rather than have the qualifier separated by a page break.

2. **Add intrinsic-reward baselines**: Include at least one additional intrinsic baseline (e.g., token-level entropy maximization with proper RL infrastructure) to demonstrate the advantage of the forward-KL NSC formulation.

3. **Analyze the counting regression**: Provide a brief explanation or visualization of why NSC training reduces counting accuracy. This would strengthen the paper's honesty about failure modes.

4. **Provide CoT diversity analysis**: Quantify whether minimizing text SC actually increases lexical diversity of the generated CoTs, to support the exploration mechanism claim.

5. **Tone down the generality claim**: Acknowledge more explicitly that IRIS is demonstrated only on autoregressive architectures, and clarify that generalization to diffusion/masked models remains open.

## Score and Decision

**Calibration anchors used** (all returned by `calibration_search`):

| Path | Avg Score | Comparison |
|------|-----------|------------|
| `/home/wg25r/review_agent/human_reviews_2026/Z9FjSaBuYt.md` (GoT-R1) | 4.50 | Accepted poster. Similar topic (RL for AR T2I). IRIS has stronger novelty (first intrinsic reward vs. applying GRPO to GoT). IRIS is stronger. |
| `/home/wg25r/review_agent/human_reviews_2026/GKWUbZsb29.md` (RL-RIG) | 4.00 | Withdrawn/rejected. Many methodological issues (no proper baselines, circular evaluation). IRIS is substantially cleaner. |
| `/home/wg25r/review_agent/human_reviews_2026/2nKaqVWaWh.md` (IntDiff) | 4.50 | Rejected. Intrinsic rewards for diffusion T2I but narrow animal domains, marginal improvements. IRIS has broader evaluation and cleaner motivation. |
| `/home/wg25r/review_agent/human_reviews_2026/HJ3vgg7TYQ.md` (RePrompt) | 5.00 | Accepted poster. RL for prompt enhancement. Both solid; IRIS tackles a harder problem (no external signals at all). Comparable quality. |
| `/home/wg25r/review_agent/human_reviews_2026/dtyTnqaKqn.md` (FocusDiff) | 5.00 | Rejected. Had confound issues (reward model = evaluator). IRIS avoids this confound. Cleaner methodology. |
| `/home/wg25r/review_agent/human_reviews_2026/hYMlDtplMf.md` (GCPO) | 5.50 | Accepted poster. Critical-token selection for RL in T2I. Strong empirical work. IRIS is a different kind of contribution but of comparable quality. |
| `/home/wg25r/review_agent/human_reviews_2026/4ik8Xe4N1s.md` (Uncertainty Preservation) | 1.50 | Rejected. Poor baseline implementation, many issues. IRIS is much stronger. |

IRIS sits well above the rejected papers (IntDiff, FocusDiff had specific confounds that IRIS avoids) and is comparable to the accepted-poster tier (GoT-R1, RePrompt, GCPO). The framing overclaim is real and should be corrected, but the core contribution — the first intrinsic-reward RL method for T2I, with a clean empirical finding about task-dependent self-certainty — is genuine and well-supported. The ablations are thorough, the limitations are honestly discussed, and the results show meaningful improvements given the zero-supervision setting.

Score: 5.0 — a solid paper with a genuine contribution and fixable framing issues.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>
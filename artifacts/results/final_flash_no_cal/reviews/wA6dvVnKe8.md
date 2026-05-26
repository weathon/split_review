Now I have all the information I need. Let me construct the final consolidated review.

## Summary

This paper proposes EDPA (Embedding Disruption Patch Attack), an adversarial patch attack targeting the embedding space of Vision-Language-Action (VLA) models, and a complementary adversarial fine-tuning defense for the visual encoder. EDPA operates using only the vision and language encoder parameters (not requiring the LVLM backbone, action space, or robot platform knowledge) and optimizes patches with two objectives: (i) maximizing discrepancy between clean and adversarial visual embeddings, and (ii) disrupting vision-language alignment. Experiments on the LIBERO benchmark across OpenVLA, OpenVLA-OFT, and π₀ show that EDPA drives failure rates to 100% on OpenVLA and substantially degrades other models, while the proposed defense reduces EDPA-induced failures by ~34 percentage points on OpenVLA with only a 1.6% clean-condition degradation.

## Strengths

1. **Attack effectiveness demonstrated across diverse VLA architectures.** EDPA achieves 100% failure rate on OpenVLA across all four LIBERO suites (Table 2) and substantially elevates failure rates on OpenVLA-OFT (e.g., 2.0%→52.3% on Object) and π₀ (e.g., 2.3%→39.5% on Object) (Table 3). This provides strong evidence that the embedding-level disruption strategy generalizes beyond a single model architecture.

2. **Substantially reduced attacker knowledge requirements compared to prior work.** Table 1 and Figure 1 clearly show that EDPA requires neither LVLM backbone access, action-space knowledge, nor robotic-manipulator knowledge — unlike UADA and UPA which need one or more of these. The attack operates purely on encoder-level representations and alignment, representing a meaningful reduction in the prior knowledge needed to mount an attack.

3. **Lightweight defense with favorable robustness-accuracy trade-off.** The adversarial fine-tuning scheme modifies only the visual encoder (leaving the LVLM backbone untouched) and reduces EDPA-induced failure rates on OpenVLA by an average of 34.2 percentage points across suites (Table 2). The clean-condition failure rate increases by only 1.6% on average, demonstrating a practical robustness-accuracy trade-off.

4. **Interesting visual analysis of generated patches.** Figure 2 shows that all generated adversarial patches (across EDPA, UADA, UPA) exhibit structural patterns resembling a robotic arm. The paper offers a plausible hypothesis — overfitting to limited camera viewpoints during data collection — that connects this observation to why multi-view models (π₀) show greater robustness.

5. **Comprehensive experimental scope for the attack.** The evaluation spans three VLA models (single- and multi-camera) and all four LIBERO task suites, with results averaged over three random seeds. This provides a solid empirical basis for assessing attack effectiveness.

## Weaknesses

### Major

1. **Missing ablation of the two attack objectives.** The attack combines a patch contrastive loss (Eq. 2) and an image-instruction alignment loss (Eq. 3) weighted by α₁=0.8. No ablation study is provided to disentangle their individual contributions. Without such an analysis, it is unclear whether both terms are necessary, whether one dominates, or whether a simpler objective (e.g., only maximizing embedding discrepancy) would perform comparably. Since the joint design is part of the paper's methodological contribution, this gap limits the reader's ability to assess its necessity and efficiency. The paper mentions hyperparameter sensitivity in Appendix C (stripped by parser), but a dedicated loss-term ablation should be part of the main experimental validation.

2. **Defense generality underexplored.** The adversarial fine-tuning defense is evaluated only on OpenVLA. While the paper notes that OpenVLA was the most vulnerable model and was therefore chosen for defense evaluation, this choice also means we have no evidence about whether the defense transfers to other VLA architectures (e.g., π₀). Given that the defense modifies only the visual encoder and is claimed to be a "drop-in replacement," demonstrating its effectiveness on at least one additional VLA model would significantly strengthen the contribution.

### Minor

3. **"Model-agnostic" terminology is imprecise and potentially misleading.** The paper describes EDPA as "model-agnostic," but the attack requires access to specific encoder parameters (vision and language) and the ability to backpropagate through them. While EDPA requires substantially less knowledge than UADA/UPA, it is not model-agnostic in the standard sense (e.g., applicable without any model-specific access). The paper does demonstrate the method across three different VLA architectures, which supports the claim that the attack *method* can be applied to different models — this is a genuine strength. But the terminology should be qualified to avoid implying black-box or zero-knowledge applicability.

4. **Adaptive attacks against the defense are not considered.** Because the defense modifies only the vision encoder and serves as a drop-in replacement, an adversary aware of the defense could generate patches specifically targeting the fine-tuned encoder. The paper does not discuss or evaluate this scenario, which limits confidence in the defense's robustness under a stronger threat model.

5. **Per-suite vs. universal patch ambiguity.** Results are reported per task suite, but it is not explicitly stated whether a separate adversarial patch was trained for each suite or whether a single universal patch was evaluated on each suite. The paper says "To construct a universal adversarial patch δ" (Sec. 3.2), which suggests one patch, but the per-suite structure of results and the separate fine-tuned models for OpenVLA per suite (Sec. 4.1) make this ambiguous. This should be clarified for reproducibility.

6. **Zero standard deviation for EDPA on OpenVLA (100.0 ± 0.0).** Reporting perfect results with zero variance across all four suites (Table 2) is unusual and merits a brief explanation. While this may simply reflect that the attack succeeded in every single rollout across all seeds, a clarifying note would be helpful.

7. **High residual failure rates for UADA/UPA in Goal and Long suites not discussed.** After defense, UADA still achieves 91.6% and 97.4% failure rates on Goal and Long respectively (Table 2), while UPA's residual rates are lower. This substantial variation across attack methods is not commented on, but could yield insights into which types of attacks the defense handles poorly.

### Trivial

8. **Ambiguous phrasing about encoder access.** The abstract states EDPA "requires only access to the VLA's encoder parameters" but does not specify that both the vision *and* language encoders are needed (the alignment loss depends on language embeddings). Table 1 lists "Encoder Parameters" without distinguishing vision vs. language. This is clarified in the method description but should be reflected earlier.

## Nice-to-Haves

- An ablation comparing the InfoNCE-style formulation (Eq. 2) against a simpler objective (e.g., maximizing cosine distance between clean and adversarial embeddings) would clarify the design rationale.
- Evaluating patch transferability across different encoder architectures (training on one encoder, testing on another) would help substantiate broader claims of model-agnosticism.
- Statistical significance testing (e.g., confidence intervals) for the defense's clean-performance degradation would strengthen the claim of minimal impact.
- A brief summary of the key findings from the hyperparameter sensitivity analysis (Appendix C) would benefit the main text.

## Removed Points

*These points were raised in the reviews but are removed after cross-checking against the paper:*

1. **"Section 5 hypothesis is speculative"** — Removed. The paper explicitly frames this as a hypothesis ("we propose a hypothesis") and offers it as a plausible interpretation, not a proven claim. Criticizing a labeled hypothesis for being speculative is invalid.
2. **"Attack should be tested in black-box setting (transfer across different encoders)"** — Removed as a weakness but retained as a nice-to-have. The paper's claim is that the attack *method* can be applied to different VLA models (which it demonstrates across three architectures), not that trained patches transfer between models. The request conflates method transferability with patch transferability.
3. **"Eq. (2) InfoNCE formulation needs justification vs. simple cosine distance"** — Moved to Nice-to-Haves. This is a design-rationale question, not a weakness.
4. **"Missing related works"** — Removed per instructions (no external sources to verify).
5. **"Reproducibility concerns about code not being released"** — The paper states "we will release our codebase upon acceptance of this paper," which meets standard expectations.

## Novel Insights

None beyond the paper's own contributions. The review process surfaces that the paper's key insight — disrupting VLA behavior by targeting the embedding/alignment space with *patches* (rather than pixel-level perturbations), and doing so with reduced system knowledge — is well-supported by the experiments. The observation that learned patches consistently resemble robotic arm structures (Figure 2) is interesting but the reviewers add no novel interpretation beyond what the paper already offers.

## Suggestions

1. **Add a dedicated ablation study** disentangling the two attack loss terms (Eq. 2 and Eq. 3). Report failure rates for α₁=0, α₁=1, and the chosen α₁=0.8 to show the contribution of each term.
2. **Evaluate the defense on at least one additional VLA model** (e.g., π₀) to support generality claims.
3. **Discuss adaptive attacks** — even a brief qualitative analysis of whether and how an adversary could adapt to the fine-tuned encoder would strengthen the defense analysis.
4. **Clarify whether patches are per-suite or universal**, and explain the zero standard deviation for EDPA on OpenVLA.
5. **Tone down "model-agnostic" to a more precise description** such as "reduced-knowledge attack" or "encoder-only attack."

## Score and Decision

This paper addresses an important and under-explored problem — adversarial robustness of VLA models — with a sensible attack design that reduces prior knowledge requirements compared to prior work, and a lightweight defense. The experimental evidence for attack effectiveness is strong across three models and four task suites. The main weaknesses are the missing ablation of the attack objectives (which prevents assessment of the design's necessity) and the defense being evaluated on only one model. These are substantial gaps but not fatal — they are addressable in revision. The paper's core contribution is solid and the experiments supporting it are largely convincing.

**MY FINAL SCORE: <score>7.0</score>**
**MY FINAL DECISION: <decision>Accept</decision>**
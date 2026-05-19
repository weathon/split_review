## Summary

This paper identifies divergent gradient directions between natural and adversarial objectives as an obstacle in robust fine-tuning (RFT), and proposes AutoLoRa to address this by routing the natural objective through a low-rank (LoRa) branch while the feature extractor handles only the adversarial objective. The paper also introduces automated schedulers for the learning rate and loss-term scalars. Results across six downstream tasks and two backbone families (ResNet and ViT) show consistent improvements over vanilla RFT and TWINS.

## Strengths

- **Novel and well-motivated architectural idea.** The core design—disentangling natural and adversarial optimization paths by assigning each to different parameter sets (LoRA branch vs. feature extractor)—is a creative application of parameter-efficient fine-tuning to the RFT problem. The gradient-similarity analysis (Figures 1a, 2a) provides concrete evidence that gradient divergence is a real issue in existing methods.

- **Consistent empirical gains across multiple settings.** AutoLoRa achieves higher PGD-10 and AutoAttack robust accuracy than both vanilla RFT and TWINS on all six downstream tasks (CIFAR-10, CIFAR-100, DTD-57, DOG-120, CUB-200, Caltech-256) with both ResNet-18 and ResNet-50 backbones, with t-test p-values reported below 0.05 (Section 5.1, Tables 1–2). The method also generalizes to ViT and DeiT backbones (Table 3).

- **Parameter efficiency and zero inference overhead.** The LoRA branch introduces fewer than 5% additional parameters relative to the feature extractor (Table 4) and is dropped at inference, incurring no extra latency—a practical advantage over other PEFT approaches.

- **Ablation on design choices.** The paper systematically ablates rank (Table 4), the sharpening parameter α (Table 10), and adversarial budget ε_pt (Table 8), supporting the default parameter choices.

## Weaknesses

### Fatal
None.

### Major

- **The core causal mechanism is asserted but never directly verified.** The entire paper is motivated by the claim that gradient divergence between natural and adversarial objectives harms robustness, and that AutoLoRa solves this by disentangling. However, the paper measures gradient similarity for vanilla RFT and TWINS (Figures 1a, 2a) but **never reports gradient similarity for AutoLoRa itself**. Without this measurement, the reader cannot tell whether the proposed disentanglement actually increases gradient alignment or whether the observed robustness gains come from other factors (the extra LoRA parameters, the KL distillation term, or the automated schedulers). This is a structural gap that leaves the paper's central thesis unsubstantiated.

- **Baseline comparison is too narrow for a "state-of-the-art" claim.** The paper compares only against vanilla RFT and TWINS (Section 5, line 132). While TWINS is the most directly related prior work, claiming SOTA requires comparison with a broader set of RFT methods—particularly those using parameter-efficient components (e.g., adapter-based RFT, prompt-based RFT, or other LoRA-based robust fine-tuning approaches). The performance gains (2–3% PGD-10) are modest enough that comparisons with additional methods are needed to establish whether the approach is genuinely SOTA.

- **Automated schedulers are not properly isolated from the disentanglement contribution.** The paper introduces two automated schedulers (LR and λ scalars) but only ablates the LR scheduler—and even that ablation is tested on **TWINS**, not on AutoLoRa itself (Table 9, Section 5.2). The λ scheduler receives no ablation at all within AutoLoRa. Consequently, it is impossible to disentangle whether the reported improvements come from the LoRA-based disentanglement, the schedulers, or their interaction.

### Minor

- **The "automated" claim is somewhat overstated.** The paper states that AutoLoRa "automatically converts a pre-trained FE into an adversarially robust model without the need for searching hyperparameters" (abstract), yet the default values for α=1.0, λ₂^max=6.0, and r_nat=8 were selected based on ablation experiments conducted on the same downstream tasks used for final evaluation (Tables 4, 10). The paper does not clarify whether these defaults were chosen on a held-out validation set distinct from the test tasks, nor does it demonstrate that the same defaults work universally without task-specific adjustment.

- **Standard accuracy trade-off not discussed.** In several cases AutoLoRa's standard accuracy (SA) is lower than TWINS's (e.g., CIFAR-10 ResNet-50: 80.91 vs 82.48; DTD-57: 60.96 vs 61.33, Table 2). The paper does not discuss whether the robustness gains come at a consistent cost to natural accuracy or whether the method's advantage persists under a fair accuracy-robustness trade-off analysis.

- **KL distillation term creates a shared gradient path.** The loss function (Eq. 5) includes a KL term connecting the adversarial logits (from the FE) to the natural soft labels (from the LoRA branch). This creates a gradient path through the FE that the paper's simplified narrative ("FE updated only by the adversarial objective") glosses over. The effect of this KL term is not analyzed.

### Trivial
None.

## Nice-to-Haves

- Training wall-clock time or FLOPs comparison for the LoRA branch overhead would be useful for practitioners.
- Measuring gradient similarity for AutoLoRa across multiple datasets would directly validate the core mechanism.
- A component-level ablation (LoRA disentanglement alone without schedulers, scheduler alone without disentanglement, and with/without the KL term) would clarify which ingredient drives the gains.

## Removed Points

**Removed (factually wrong or misunderstanding the paper):**
- "Figures 2a/2b are referenced but their content is not verifiable from the extracted text" — This is a PDF parser issue, not a paper problem. The paper contains these figures.
- The claim that TWINS "uses a dual BN (Xie et al., 2020; Wang et al., 2020) module" being questioned — This is correctly cited and described in the paper.

**Removed (nitpick about missing appendix content guaranteed to exist in original):**
- "The appendix may specify X but…" — The paper references an appendix with additional results; parser artifacts do not make it missing.
- "p-values in Table 7 (not shown)" — Parser issue; the table exists in the original.

**Removed (generic concern that lacks concrete anchor in the paper):**
- "The divergent gradients could be a symptom of other optimizer instabilities, not the root cause" — Speculative with no evidence that this is the case for these specific methods.
- "The observed robustness gains could come from any number of other factors—the extra parameters of the LoRA branch, the automated schedulers, or the KL distillation term—rather than from resolving gradient conflict" — This is already covered by the core mechanism issue (kept as Major weakness #1) and the ablation gap (kept as Major weakness #3). The duplicate framing is removed.

**Removed (strength that conflicts with verified weakness):**
- "Automated scheduler eliminates manual hyperparameter search" — Weakened by the factual gap that defaults were chosen via ablation on the evaluation tasks themselves. This strength conflicts with the verified weakness about the overstated "automated" claim.

**Removed (pure formatting nitpick):**
- "The claim about additional datasets being referenced but not verifiable from extracted text" — Parser artifact.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Measure gradient similarity for AutoLoRa** across multiple datasets and compare directly against vanilla RFT and TWINS. This single experiment would either validate or invalidate the paper's core thesis.
2. **Add at least 2–3 more baselines** from the broader RFT and PEFT robustness literature (e.g., adapter-based methods, other LoRA-based RFT approaches) to support the SOTA claim.
3. **Perform component-level ablations on AutoLoRa itself:** (a) LoRA disentanglement alone without schedulers, (b) LR scheduler alone, (c) λ scheduler alone, (d) without the KL distillation term. This would clarify which component drives the gains.
4. **Clarify the hyperparameter selection process.** If defaults were chosen on a separate validation set (e.g., a held-out subset of ImageNet), state that explicitly; otherwise, acknowledge that the method requires minimal but non-zero tuning and discuss sensitivity.
5. **Add a discussion of the standard-accuracy trade-off.** Report whether the robustness gains consistently come at a cost to natural accuracy and whether the trade-off is favorable compared to baselines.

---

## Score Calibration

**Round 1 bracket:** Between 4 and 6. The paper is clearly stronger than score-3 works (e.g., "Vulnerability-Aware PEFT" at 3.00, which had more severe limitations in scope and generalization), and clearly weaker than score-8+ works on unrelated topics (LLM training, multimodal reasoning).

**Round 2 narrowing:** I retrieved and read full reviews for papers in the 4.0–5.5 range. The most comparable anchor is **"Robust Fine-Tuning from Non-Robust Pretrained Models: Mitigating Suboptimal Transfer With Epsilon-Scheduling"** (avg score 4.67, Accept Poster). Like AutoLoRa, it addresses an RFT optimization challenge, proposes a scheduling heuristic, and was criticized for missing comparisons with other RFT methods. AutoLoRa has a more architecturally novel solution than the Epsilon-Scheduling paper, but also has a more severe evidential gap (unverified core mechanism). The **"Gradient Intrinsic Dimensionality Alignment"** paper (5.50, Accept Poster) has stronger validation and broader baselines — AutoLoRa does not match this level. The **"AdvCLIP-LoRA"** paper (4.00) represents a simpler "combination of LoRA + adversarial training" which AutoLoRa clearly surpasses in novelty.

**Final score:** 4.5 — The paper sits between the 4.0 (obvious combination) and 5.5 (well-validated) anchors. The idea is genuinely novel and the empirical results are consistent, but the evidential gaps (unverified core mechanism, narrow baselines, unsupported scheduler attribution) are significant enough that the paper does not reach the 5.0+ level.

**Anchors consulted:**

| Path | Avg Score | Round | Comparison |
|---|---|---|---|
| /home/wg25r/review_agent/human_reviews_2026/OsXr7S8X4x.md | 3.00 | R1 | Weaker; narrower scope, missing baselines |
| /home/wg25r/review_agent/human_reviews_2026/5TitVYbQQ2.md | 3.00 | R1 | Weaker; limited foundation model evidence |
| /home/wg25r/review_agent/human_reviews_2026/ZBaPU5FL0Z.md | 3.00 | R1 | Different topic (OP-LoRA optimization) |
| /home/wg25r/review_agent/human_reviews_2026/eWsyMMhSCb.md | 3.00 | R1 | Different topic (pruning LoRA) |
| /home/wg25r/review_agent/human_reviews_2026/Ef0nUFg3Jw.md | 2.67 | R1 | Different topic (spurious tokens) |
| /home/wg25r/review_agent/human_reviews_2026/TMKDVEOohD.md | 4.50 | R1, R2 | Similar topic; had theory flaws, autoLoRa has different but comparable weaknesses |
| /home/wg25r/review_agent/human_reviews_2026/neG0h10Be5.md | 4.00 | R1, R2 | Weaker; "combination of LoRA + adv training" with no novel insight |
| /home/wg25r/review_agent/human_reviews_2026/hUii0ju5aA.md | 4.40 | R1 | Different topic (LLM safety alignment) |
| /home/wg25r/review_agent/human_reviews_2026/ZCpjdiNhsP.md | 4.00 | R1 | Different focus (norm-bounded LoRA) |
| /home/wg25r/review_agent/human_reviews_2026/kObvnQ6pUx.md | 5.50 | R1 | Stronger; better validated, broader baselines |
| /home/wg25r/review_agent/human_reviews_2026/aIBFTh2ThF.md | 4.67 | R2 | **Closest anchor** — same topic area, similar weakness profile, accepted poster |
| /home/wg25r/review_agent/human_reviews_2026/lZgORA63ew.md | 5.50 | R2 | Stronger; broader validation, 15 datasets |
| /home/wg25r/review_agent/human_reviews_2026/WlOZ7y8Wrw.md | 4.50 | R2 | Different topic (adversarial transferability to SAM) |
| /home/wg25r/review_agent/human_reviews_2026/ij8xU2yCmX.md | 4.00 | R2 | Different topic (ReLoRA efficiency) |
| /home/wg25r/review_agent/human_reviews_2026/4ihxXIakoY.md | 4.67 | R2 | Different topic (discrete image tokenizers) |
| /home/wg25r/review_agent/human_reviews_2026/lL6htAaolp.md | 6.00 | R2 | Different topic (adversarial training for diffusion models) |
| /home/wg25r/review_agent/human_reviews_2026/JFaCPwvzGz.md | 4.50 | R2 | Different topic (adversarial distillation) |
| /home/wg25r/review_agent/human_reviews_2026/fBc9v8CVvm.md | 5.33 | R2 | Different topic (one-step generation) |

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>
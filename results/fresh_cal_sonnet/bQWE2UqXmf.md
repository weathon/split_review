Now let me run the bracketing calibration search to calibrate my score.Let me read a couple of the most relevant calibration anchors.Round 1 bracket: **5.5–7.0**. RAIDAR is clearly above the 3-range papers (limited contributions, unrelated), and below the 8+ range (highly polished, well-controlled). Let me narrow within the bracket.Now I have enough context. Let me write the final review.

---

## Summary

RAIDAR (geneRative AI Detection viA Rewriting) introduces AI-generated text detection via a rewriting edit-distance signal: LLMs prompted to rewrite text make more edits to human-written text than to AI-generated text, and this differential is captured by normalized Levenshtein distance features (invariance, equivariance, uncertainty). A logistic regression or XGBoost classifier trained on these features shows consistent F1 improvements over prior state-of-the-art detectors across six diverse domains. The key practical claim is black-box compatibility — the method requires only token-level output, not log-probabilities.

---

## Strengths

- **Novel, well-motivated signal.** The rewriting edit-distance observation is original and practically motivated: RAIDAR is the first method to operationalize the hypothesis that LLMs treat their own generated text as high-quality (few modifications) versus human-written text (many modifications). This is confirmed by clean histogram visualizations (Figure 2) showing clear distributional separation for all three measurement types across datasets.

- **Consistent improvements across six diverse domains.** Table 1 shows Invariance achieves 95.38 F1 on Code (vs. 67.39 DetectGPT / 65.97 Ghostbuster), 87.75 on Yelp Reviews (vs. 71.47 Ghostbuster), 64.81 on Student Essays (vs. 52.29 GPT Zero-shot), and 62.88 on Creative Writing (vs. 61.81 GPTZero). The gains are not an artifact of one dataset.

- **Genuine black-box compatibility.** The design requires only discrete text output, not log-probabilities. Section 3.2 and Table 5 both demonstrate real-world deployment with GPT-3.5-turbo as the rewriting model — something DetectGPT cannot replicate because GPT-3.5 does not expose probability scores. This is a real, practical advantage.

- **Short-input robustness.** Figure 6 shows 74 F1 at 10-word inputs on Yelp Reviews, outperforming GPTZero and Ghostbuster, which the paper notes "fail with shorter inputs."

- **Cross-generator detection.** Table 4 demonstrates that a GPT-3.5 rewriter can detect text from Ada (96.88), Text-Davinci-002 (84.85), GPT-4-turbo (80.00), and LLaMA 2 (98.46) in-distribution, and 91.43 OOD for Code, validating that the signal is not purely self-referential.

---

## Weaknesses

### Fatal
None.

### Major

- **Unexplained Yelp regression under multi-prompt training (Table 3).** When trained on multiple prompts for adversarial robustness, Yelp "No Adaptive Prompt" F1 collapses from 87.75 (single training prompt) to 58.04 (multi training prompt) — a 30-point regression on the *non-adversarial* test case. The paper dismisses this as "one exception" and attributes it to "larger data difference when prompted differently" (Section 4.3), but this is a conjecture, not an investigation. The multi-prompt training is supposed to be the robustness solution, yet it harms benign performance substantially on one domain. This is a real failure mode that undermines the robustness narrative: the method trades adversarial resilience for benign accuracy on at least one domain, and there is no analysis of when this tradeoff occurs or how to avoid it.

- **Model-quality asymmetry with DetectGPT is under-acknowledged.** Section 4.2 discloses that DetectGPT uses `facebook/opt-2.7B` as its scoring model while RAIDAR uses GPT-3.5-turbo for rewriting. The paper's core motivation is that GPT-3.5 cannot serve as DetectGPT's scoring model (no log-prob access), so this comparison is inherently constrained — not simply unfair. However, the paper does not clearly frame this constraint, and the headline gains partly reflect model-quality advantage rather than purely methodological advantage. The partial mitigation exists in Table 5, which shows that Ada-based RAIDAR (Code: 77.42, Creative: 62.50) still outperforms or matches DetectGPT (Code: 67.39), but the paper does not foreground this analysis when interpreting the main results. The framing should acknowledge explicitly that the comparison reflects the real-world deployable configuration — not a controlled ablation — and that Table 5 provides the matched-model-quality evidence.

### Minor

- **"Inherently robust on new content" overclaims.** The abstract states the method is "inherently robust on new content," implying zero-shot or training-free behavior. In fact, a logistic regression or XGBoost classifier must be trained on labeled examples (Section 4.3 confirms this). The OOD experiments in Table 2 do show reasonable feature transfer, but performance drops are visible (e.g., News: 56.87 OOD vs. 60.29 in-domain). "Features partially transfer out-of-distribution" is accurate; "inherently robust on new content" is not.

- **Selective OOD baselines.** Table 2 includes only Ghostbuster as a baseline in the OOD setting, while Table 1 also includes GPTZero and DetectGPT. The paper does not explain why these are omitted from the OOD comparison. Since OOD generalization is a key robustness claim, including or explaining the omission of all baselines strengthens credibility.

- **Self-referential component in main results.** The primary Table 1 uses GPT-3.5 to both generate test data and rewrite for detection. Table 4 shows that GPT-3.5 as a rewriter achieves 87.75 on GPT-3.5-generated Yelp text but only 65.80 on Text-Davinci-002-generated Yelp text — a 22-point gap. Some self-referential inflation in the headline numbers is real, though Table 4 demonstrates the method works across generators.

### Trivial

- **No statistical significance or variance reporting.** Given that several improvements are modest (e.g., News: 60.29 vs. 54.74) and the method involves stochastic LLM calls, reporting confidence intervals would help readers assess reliability of smaller margins.

---

## Nice-to-Haves

- An ablation testing whether LLMs also make fewer edits to high-quality *human* text (e.g., formal legal prose, Wikipedia) would help distinguish the "quality preference" hypothesis from the "distributional similarity" account. These predictions differ in adversarial implications.
- A clearer per-prompt sweep cost analysis: Figure 3 shows prompt variance is substantial and no single prompt dominates. A note on deployment-time prompt selection strategy would help practitioners.
- Investigating the Yelp multi-prompt regression more carefully (e.g., is it specific to short-text domains?) would sharpen the robustness guidance.

---

## Removed Points

*These points are flagged to be removed; treat with caution.*

- **"Fatal: DetectGPT comparison is structurally unfair"** (Harsh Critic): Partially valid framing but overstated as fatal. The asymmetry is inherent: GPT-3.5 cannot be used as DetectGPT's scoring model because it does not expose log-probabilities. The comparison reflects the real-world deployable configurations for each method. Table 5 provides matched-model evidence (Ada RAIDAR vs OPT-2.7B DetectGPT), which shows RAIDAR still competitive. Demoted to Major with reframing.

- **"GPTZero comparison is uninformative" (Harsh Critic)**: GPTZero is included as a commercial baseline — this is valid and expected in this literature. Its opacity is acknowledged in the paper. This is not a weakness.

- **"Code dataset is artificially easy"** (Harsh Critic): This is speculative. The paper does not claim the Code dataset is representative of the hardest possible detection scenario; it is one of six evaluated domains. The variation in difficulty across domains is expected and provides useful signal about where the method works well.

- **"The ArXiv generation scenario is artificial"** (Harsh Critic): This is a scope-creep critique. The paper states the abstract is generated from "title + first 15 words" — this is clearly documented and constitutes a defined experimental condition.

- **Strength: "Operates solely on word symbols without high-dimensional features, reducing spurious correlations"** (Strength Finder): Retained as part of black-box compatibility strength, but the claim about "reducing spurious correlations" is partially speculative — no ablation confirms that high-dimensional features have more spurious correlations on these datasets.

---

## Novel Insights

The paper surfaces a cross-model rewriting symmetry that goes beyond the obvious: not only does a model modify human text more than its own generated text, but *any* autoregressive model's rewriter appears to share this property across models it did not generate (Table 4 shows GPT-3.5 detecting Ada-generated text at 96.88 F1). This suggests the rewriting-based signal captures something about the distributional structure of auto-regressive generation in general — not a purely self-referential artifact. The three-way measurement framework (invariance, equivariance, uncertainty) operationalizes this structure from complementary angles, with each contributing discriminative power (Table 1 shows all three metrics produce competitive F1 independently).

---

## Suggestions

1. In the main results discussion, explicitly note that DetectGPT using OPT-2.7B vs. RAIDAR using GPT-3.5 reflects the real-world constraint (no log-prob access from GPT-3.5), and point to Table 5 as the model-matched comparison. This reframing costs no new experiments but dramatically strengthens the paper's credibility.
2. Investigate the Yelp multi-prompt regression (87.75→58.04) more carefully: is it domain-specific? Text-length-specific? Prompt-distribution-specific? Even a brief analysis would turn this from a weakness into a finding.
3. Revise the abstract's "inherently robust on new content" to more precisely describe OOD feature transfer.
4. Add a matched-model comparison row in Table 1 or a footnote: "RAIDAR with Ada achieves X on Code vs DetectGPT's Y" to preempt the asymmetry concern.

---

## Scoring

**Calibration anchors retrieved:**

| Path | Avg Score | Round | Comparison |
|---|---|---|---|
| `PdTe8S0Mkl.md` | 3.00 | R1 | Unrelated (ChatGPT vs human analysis); well below RAIDAR |
| `jbfDg4DgAk.md` | 3.00 | R1 | Sparse watermarking; below RAIDAR in novelty and evaluation |
| `7Ab1Uck1Pq.md` | 4.50 | R1 | Profiler (black-box origin detection); narrower scope, lower quality |
| `iARAKITHTH.md` | 4.25 | R1 | Binoculars (zero-shot detection); similar domain, rejected for inconsistent eval |
| `GRlKzhHl9Z.md` | 5.33 | R1 | Bayesian surrogate for DetectGPT; similar domain, rejected |
| `3fEKavFsnv.md` | 6.50 | R1+R2 | MMD-based detection; more theoretical, limited corpus, accepted |
| `wojnTvBXqt.md` | 5.50 | R2 | Learning2Rewrite (direct follow-on to RAIDAR); same core idea + fine-tuning, 21 domains, rejected |
| `EE75tyB5Ay.md` | 5.33 | R2 | ChatGPT detection generalization analysis; less novel, rejected |
| `E4LAVLXAHW.md` | 7.00 | R2 | Black-box watermark detection; different sub-problem, higher rigor |
| `rWjZWHYPcz.md` | 6.25 | R2 | PaLD (mixed-text detection); different task, accepted |
| `567BjxgaTp.md` | 6.75 | R2 | LLM lie detection via black-box; different problem, accepted |

**Round 1 bracket: 5.5–7.0**

**Round 2 narrowing:** The most directly comparable papers are `wojnTvBXqt.md` (5.50, Rejected — a direct follow-on citing RAIDAR, with extended evaluation over 21 domains but still rejected) and `3fEKavFsnv.md` (6.50, Accepted — technically richer but limited corpus). RAIDAR sits between these: it pioneered the idea (originality credit), covers 6 domains (more than MMD-MP's limited corpus), is technically simpler than MMD-MP, has fewer domains and less fine-tuning than Learning2Rewrite, and has real evaluation concerns (Yelp regression, overclaiming). RAIDAR is clearly stronger than Learning2Rewrite's anchors would suggest (it's the source paper, not the extension), but doesn't quite reach MMD-MP's technical rigor. The final score lands at **6.0**, slightly above Learning2Rewrite and slightly below MMD-MP.

---

**Axes summary:**
- **Originality:** High — first use of rewriting edit-distance for AI text detection
- **Research question importance:** High — black-box detection is practically crucial
- **Claim support:** Moderate — improvements are demonstrated but comparison framing and Yelp regression weaken some claims
- **Experimental soundness:** Moderate — good domain coverage, some evaluation concerns (model asymmetry framing, missing OOD baselines, no significance testing)
- **Writing clarity:** Good — method is clearly explained; introduction and abstract slightly overclaim
- **Value to research community:** Moderate-to-high — practical method with a novel insight that spawned follow-on work

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>
Now I have a thorough understanding of the paper and all the reviews. Let me compile the final consolidated review.

## Summary of Calibration

**Round 1 bracket (bracketing):** After initial search, plausible range is between 5.0 and 7.0.

**Round 1 anchors:**
- Weak band (<3.5): TJHB4ySVZM (3.40), oOa3ZCtMjJ (3.00), ZVOGMy8Sd8 (3.00), XHvguNJRbE (2.50) — all clearly weaker than IRIS (rejected papers, poor evaluation/novelty)
- Middle band (3.5–7.5): bO31lfEdos (5.00, rejected), kIP0duasBb (6.67, accepted), cJQ1K2fjpD (6.20, accepted), Let8OMe20n (6.00, accepted)
- Strong band (>7.5): OlzB6LnXcS (8.00), DJSZGGZYVi (9.00), agPpmEgf8C (8.00), u1cQYxRI1H (10.00) — all clearly stronger than IRIS (foundational or breakthrough work)

**Round 2 narrowing (within 5.0–7.5):** Read full reviews of bO31lfEdos (5.00), kIP0duasBb (6.67), cJQ1K2fjpD (6.20), Let8OMe20n (6.00), Ugs2W5XFFo (6.00), kGvXIlIVLM (7.00).

**Comparisons:**
- vs bO31lfEdos (5.00, rejected): IRIS has a more novel discovery, more thorough evaluation, better ablations. Clearly stronger.
- vs Let8OMe20n (6.00, accepted): Comparable quality. Both have novel contributions and good evaluation. IRIS's core discovery is arguably more interesting but its evaluation is on a single architecture.
- vs Ugs2W5XFFo (6.00, accepted): Similar level. Both propose self-supervised alignment methods for T2I with competitive results.
- vs cJQ1K2fjpD (6.20, accepted): Similar methodology (self-alignment without external data) and evaluation thoroughness. Comparable.
- vs kIP0duasBb (6.67, accepted): IRIS has a more novel finding (task-dependent self-certainty) but is tested on fewer settings (single architecture vs multiple tasks).
- vs kGvXIlIVLM (7.00, accepted): IRIS is notably weaker — less thorough evaluation, less clean theoretical framing, more overclaiming.

**Final score:** 6.0. The paper has a genuinely novel and interesting discovery, thorough ablations, and solid experiments. However, it has several framing overclaims and is tested only on one architecture. It sits comfortably in the accept range but is not an exceptional paper.

---

Now writing the full review.## Summary

This paper proposes **IRIS**, the first framework that applies reinforcement learning to autoregressive text-to-image (T2I) models using **only an intrinsic reward** — negative self-certainty (NSC), defined as the negative KL divergence between a uniform distribution and the model's output distribution. The key empirical discovery is task-dependent behavior of self-certainty: maximizing self-certainty helps language reasoning but *minimizing* it helps T2I generation, producing more visually rich images. Applied to Janus-Pro models, IRIS achieves performance competitive with T2I-R1 (which uses external reward models like HPSv2, DINO, GIT, and ORM) while requiring no human labels or domain-specific verifiers. Ablation studies systematically validate the design choices.

## Strengths

- **Discovery of task-dependent self-certainty behavior is genuinely novel and well-supported.** The paper demonstrates — both qualitatively (Fig. 1, across three generation tasks) and quantitatively (Fig. 2, tracking self-certainty over training) — that maximizing self-certainty impairs T2I generation while improving language reasoning. This directly contradicts prior findings in text-only models (Zhao et al., 2025b; Zhang et al., 2025a) and is the paper's most interesting contribution.

- **First intrinsic-only RL alignment method for T2I with competitive results.** The paper is the first to show that autoregressive T2I models can be aligned using purely intrinsic signals, without any external reward models or human-labeled data. Table 1 reports IRIS within 3–4% of the external-reward baseline T2I-R1 on GenEval (0.72 vs 0.75), T2I-CompBench Complex (0.3793 vs 0.3820), and WISE (0.37 vs 0.38), and even exceeds T2I-R1 on T2I-CompBench Color (0.7946 vs 0.7924). This demonstrates that intrinsic rewards can meaningfully substitute for external supervision.

- **Systematic and well-motivated ablation studies.** Four ablation sets (Figs. 5–9) each isolate a key design decision: with/without CoT, minimize vs. maximize text/image confidence, forward vs. backward KL, RL vs. direct optimization. Each provides clear quantitative evidence that the chosen configuration is optimal and that incorrect choices (e.g., maximizing image self-certainty) lead to rapid performance collapse. This substantially strengthens confidence in the method.

- **Identification and correction of a training-pipeline error in prior work.** Section 4.1 explicitly identifies a chat-template mismatch in the official T2I-R1 implementation (Janus vs. Janus-Pro use different templates), then corrects it. This demonstrates careful reproducibility practices and is a genuine service to the community.

## Weaknesses

### Major

- **"Superior to external rewards" is not supported by the overall results.** The abstract claims IRIS achieves performance "competitive with or superior to external rewards." Table 1 tells a more nuanced story: IRIS is slightly *lower* than T2I-R1 on almost every overall score (GenEval: 0.72 vs 0.75 for 1B, 0.77 vs 0.78 for 7B; T2I-CompBench Complex: 0.3793 vs 0.3820; WISE: 0.37 vs 0.38 for 1B, 0.48 vs 0.50 for 7B). The only exception is T2I-CompBench Color where IRIS leads 0.7946 vs 0.7924. "Competitive" is accurate; "superior" is not supported by the overall scores. The paper's core contribution — that intrinsic rewards can match external rewards without requiring them — is strong enough without this overstatement. This should be corrected throughout.

- **The claim that IRIS "enhances the reasoning capabilities of T2I models" lacks direct evidence.** The paper states (line 48) that IRIS "can significantly enhance the reasoning capabilities of T2I models" and attributes improvements on WISE and T2I-CompBench to "reasoning and planning capabilities." The only direct evidence of improved CoT reasoning is one example in Figure 4 (a bicycle with a meadow background). No quantitative analysis of CoT length, relevance, informativeness, or diversity is provided. The benchmark improvements could stem from the model learning to generate more visually varied images that happen to score higher, rather than from genuine improvements in compositional planning or reasoning. The "reasoning enhancement" framing is broader than the evidence supports.

### Minor

- **The "agnostic to model architecture or dataset" claim is too broad for the evidence provided.** The method section (line 48) states IRIS "is agnostic to the model architecture or dataset," but experiments only test Janus-Pro, an autoregressive multimodal LLM. Diffusion models (SD3, FLUX), masked models (Show-o), and other T2I architectures are not tested. Section 4.4 acknowledges this as future work, but the introduction and method sections present the claim without caveat. This is fixable by adding a scope qualifier.

- **The mechanism by which negative self-certainty improves image alignment is intuitive but not causally established.** The paper provides a plausible post-hoc explanation ("overly confident models generate uniform figures, less confident models generate visually rich images") supported by Fig. 2's correlation. However, the paper does not isolate whether NSC directly improves prompt alignment or whether it exploits a statistical correlation with the evaluation metrics (e.g., more diverse images score higher on HPSv2 and DINO for reasons orthogonal to prompt following). A direct analysis — e.g., measuring image diversity metrics (LPIPS, color histogram variance) alongside prompt alignment — would substantially strengthen the mechanistic claim.

- **No human evaluation.** The paper relies entirely on automated metrics (GenEval, T2I-CompBench, WISE, plus four reward models for ablations). While automated evaluation is standard in this field, the paper's central claim about producing "visually rich and colorful" images that are "better aligned with human preferences" would benefit from even a small-scale human preference study (e.g., 50 prompts comparing IRIS vs. baseline and T2I-R1). This limits confidence that the improvements translate to perceived quality.

### Trivial

- The theoretical justification for forward vs. backward KL (Section 3.2) uses the standard mode-covering/mode-seeking language, but this distinction was developed for target=data-distribution settings, not for target=uniform-distribution. The ablation (Fig. 8) empirically resolves the question, but readers unfamiliar with the prior work (Fang et al. 2024, Kang et al. 2025) could be confused.

## Nice-to-Haves

- A quantitative analysis of the generated CoTs (average length, entity coverage, diversity) would strengthen the reasoning claim without requiring new experiments, since the CoTs are already generated during training.
- Testing IRIS on at least one non-autoregressive T2I architecture (e.g., a diffusion model) would substantiate the generalizability claim.
- A held-out set of prompts designed to be sensitive to reward hacking (where high diversity but poor alignment would score well) would help establish that NSC genuinely improves alignment rather than exploiting evaluation metric correlations.
- Reporting whether the standard deviations in Table 1 come from multiple training seeds or multiple evaluation runs would improve reproducibility.

## Removed Points

These points were removed from the final review for the reasons stated:

1. *"Fig. 2 compares two different models so the comparison is not controlled"* — The paper presents this as an observation, not a controlled experiment. The comparison is illustrative of a trend, not a causal claim. Removed as a misunderstanding of the paper's intent.

2. *"The group size of 8 is small for GRPO"* — G=8 for advantage estimation is standard in GRPO-based methods (including DeepSeek-R1). The paper reports hyperparameters clearly. Removed as a generic methodological nitpick without specific evidence of instability.

3. *"Forward KL justification is muddled"* — The paper cites three prior works (Fang et al. 2024, Kang et al. 2025, Zhao et al. 2025b) for this design choice and validates it with a clean ablation (Fig. 8). Whether the theoretical framing is perfect is a presentation nuance, not a weakness in the method. Removed to avoid inflating the weakness count with a non-substantive point.

4. *"Y-axis ranges differ across plots"* — Pure formatting nitpick.

5. *"No discussion of training data prompts"* — The paper states it follows T2I-R1's protocol, and further details may be in the stripped appendix. Partially addressed.

6. *"No statistical tests for small differences"* — The paper reports standard deviations (with ± notation throughout Table 1). Most differences between IRIS and T2I-R1 exceed the noise (e.g., GenEval 0.72±0.01 vs 0.75±0.01). The point was removed as already addressed by the paper's reporting.

7. Several strengths from the Strength Finder were removed: generic statements about "addressing an important problem" or "well-written" without specific evidence. Only strengths with concrete, verifiable anchors were retained.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Tone down the "superior to" language throughout (abstract, introduction, conclusion) to accurately reflect that IRIS is competitive with but slightly below external-reward methods on most overall scores. The contribution is still strong without this overstatement.

2. Add a quantitative analysis of the generated semantic CoTs — at minimum, report average length, noun/entity counts, and diversity (e.g., distinct entities per prompt category). This would directly support the "reasoning enhancement" claim with minimal additional work since the CoTs are already generated.

3. Add a caveat to the "agnostic to model architecture" claim in the introduction and method sections, noting that experiments are conducted on autoregressive models and generalization to other architectures is future work.

4. Consider adding image diversity metrics (e.g., LPIPS variance across generations for the same prompt, color histogram entropy) to directly validate the "visually rich and colorful" intuition and provide mechanistic evidence for why NSC helps.

## Score and Decision

**Calibration report:**

All anchors retrieved across rounds:

| Anchor ID | Avg Score | Round | Comparison to this paper |
|---|---|---|---|
| TJHB4ySVZM | 3.40 | R1 (bracket, <3.5) | Much weaker — rejected paper on data augmentation for T2I |
| oOa3ZCtMjJ | 3.00 | R1 (bracket, <3.5) | Much weaker — rejected, GAN+CLIP for T2I |
| ZVOGMy8Sd8 | 3.00 | R1 (bracket, <3.5) | Much weaker — rejected, image captioning |
| XHvguNJRbE | 2.50 | R1 (bracket, <3.5) | Much weaker — rejected, innate-values RL |
| bO31lfEdos | 5.00 | R1 (middle), R2 | Weaker — RL for hallucination, weaker evaluation, rejected |
| kIP0duasBb | 6.67 | R1 (middle), R2 | Comparable/stronger — CLIP reward for VLM adaptation, tested on more tasks |
| cJQ1K2fjpD | 6.20 | R1 (middle), R2 | Comparable — token-level rewards for VLLM alignment |
| Let8OMe20n | 6.00 | R1 (middle), R2 | Comparable — confidence-aware reward for T2I fine-tuning |
| Ugs2W5XFFo | 6.00 | R2 (narrow) | Comparable — information-theoretic T2I alignment |
| kGvXIlIVLM | 7.00 | R2 (narrow) | Stronger — guidance-free AR generation, more thorough evaluation |
| OlzB6LnXcS | 8.00 | R1 (>7.5) | Much stronger — one-step diffusion (breakthrough) |
| DJSZGGZYVi | 9.00 | R1 (>7.5) | Much stronger — diffusion transformer training |
| agPpmEgf8C | 8.00 | R1 (>7.5) | Much stronger — predictive objectives in deep RL |
| u1cQYxRI1H | 10.00 | R1 (>7.5) | Much stronger — illumination harmonization (breakthrough) |

**Round 1 bracket:** Between 4.0 and 7.0 (after reading weak anchors at ~3 and middle anchors at 5–6.67).
**Round 2 narrowing:** Compared against bO31lfEdos (5.00), kIP0duasBb (6.67), cJQ1K2fjpD (6.20), Let8OMe20n (6.00), Ugs2W5XFFo (6.00), kGvXIlIVLM (7.00). The paper is clearly stronger than the 5.00 anchor, comparable to the 6.00–6.20 anchors, slightly weaker than the 6.67 anchor (which tests on more settings), and notably weaker than the 7.00 anchor (which has cleaner framing and more thorough evaluation).
**Final score:** 6.0. The paper has a genuinely novel and interesting core discovery, solid and reproducible experiments, and thorough ablations. The weaknesses are primarily in framing overclaims (superiority, reasoning enhancement, architecture agnosticism) rather than methodology. With toned-down claims and a quantitative CoT analysis, this would be a strong paper. In its current form, it is a solid accept.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>
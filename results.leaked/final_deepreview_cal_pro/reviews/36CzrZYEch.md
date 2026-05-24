Now I have a thorough understanding of both the paper and the calibration anchors. Let me compile the final review.

### Round 1 Bracket

Based on the round-1 anchors:
- **Low band (score < 3.5)**: FTpdQBoBd0 (3.00), Fk4Op9wpEp (3.00), 9LAqIWi3QG (3.00), oqRe1KvD17 (3.00) — All are clearly weaker than IRIS, which has a novel conceptual contribution, thorough experiments, and competitive results.
- **Middle band (3.5-7.5)**: kIP0duasBb (6.67), Let8OMe20n (6.00), vxutwN3xQN (6.00), 7pVIFJW2Hp (5.50) — IRIS is comparable to or stronger than the best of these.
- **Upper band (>7.5)**: SI2hI0frk6 (7.60), QEHrmQPBdd (8.00), gU58d5QeGv (8.00), N8Oj1XhtYZ (8.50) — These are high-impact architectural contributions or benchmarks with very strong execution. IRIS is not in this tier.

**Initial bracket: 5.5–7.0**

### Round 2 Narrowing

Round-2 anchors pulled from 5.0-7.5:
- eC2ICbECNM (6.00): Ctrl-U — uncertainty-aware reward for conditional image generation. IRIS has a more novel concept (purely intrinsic reward vs. uncertainty-weighted external reward), more comprehensive evaluation, and better ablations. **IRIS is stronger.**
- Ugs2W5XFFo (6.00): MI-TUNE — self-supervised MI-based T2I alignment. Similar spirit (avoiding external rewards), but IRIS has more benchmarks, more ablations, and a more general method. **IRIS is stronger.**
- cJQ1K2fjpD (6.20): FiSAO — self-alignment using vision encoder as verifier. Strong paper with similar "no external data" motivation. IRIS has comparable ablations and benchmarks; IRIS's cross-modal insight (text vs. image certainty) is more novel. **IRIS is comparable or slightly stronger.**
- sgAp2qG86e (6.25): JetFormer — autoregressive model. Different type of contribution (architecture). **Hard to compare directly but similar quality tier.**
- kIP0duasBb (6.67): RLCF — CLIP reward for TTA. Well-executed with 3 tasks. IRIS has a stronger conceptual contribution (no external model at all vs. using CLIP as reward). **IRIS is comparable.**

**Narrowed bracket: 6.0–6.5.** IRIS is clearly above the 6.0 cluster and comparable to the 6.2-6.7 range. I place it at **6.5** — a solid accept with some minor issues that can be addressed in revision.

---

## Summary

This paper introduces IRIS, a reinforcement learning framework for fine-tuning autoregressive text-to-image models using only an intrinsic reward signal — specifically, negative self-certainty (NSC), defined as KL divergence between a uniform distribution and the model's output distribution. The key insight is that, contrary to findings in text-based language reasoning (where maximizing self-certainty helps), minimizing self-certainty improves image generation quality and diversity. IRIS achieves results competitive with external-reward training (T2I-R1) across GenEval, T2I-CompBench, and WISE benchmarks without any human labels, domain-specific verifiers, or external reward models.

## Strengths

- **Novel and well-supported cross-modal insight:** The paper convincingly demonstrates that self-certainty plays opposite roles in text reasoning versus image generation. Figure 1 shows that lower self-certainty yields richer, more human-preferred images; Figure 2 shows self-certainty dropping on image tokens during external-reward RL while rising on text tokens; and Figures 6–7 provide clean ablation evidence that minimizing image SC improves performance while maximizing it causes collapse.

- **Effective purely intrinsic method with competitive results:** IRIS improves Janus-Pro-1B by 9.1%, 13.3%, and 28.8% on GenEval, T2I-CompBench, and WISE respectively (Table 1). Across all three benchmarks, IRIS closely matches or approaches the externally-rewarded T2I-R1 baseline without ever seeing an external reward signal. This is a genuinely significant result — eliminating the dependency on hand-crafted reward models for T2I alignment.

- **Thorough and informative ablation studies:** Section 4.3 systematically isolates each design choice (with/without CoT, text vs. image uncertainty, forward vs. backward KL, RL vs. direct optimization) across six figures. The direct-optimization-without-RL collapse (Figure 9) is particularly instructive and validates the GRPO-based approach.

- **Emergent semantic chain-of-thought:** IRIS spontaneously generates meaningful, descriptive semantic CoTs without any external signal (Figure 4), and training with CoTs consistently outperforms training without them (Figure 5). This demonstrates that the intrinsic reward alone can incentivize useful exploration behavior.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Overstated aggregate superiority claim.** The abstract states IRIS "achieves performance that is competitive with or superior to external rewards." While "competitive" is fully supported, the aggregate scores in Table 1 consistently show IRIS slightly trailing T2I-R1 on overall metrics (GenEval: 0.72 vs. 0.75; T2I-CompBench: 0.379 vs. 0.382; WISE: 0.37 vs. 0.38). IRIS does lead on some subcategories (Physics in WISE, Color in GenEval), so "superior" is true in those narrow cases, but the aggregate picture supports "competitive with" rather than "superior to." The genuine headline — achieving parity *without any external supervision* — is stronger and should be foregrounded rather than a contest of absolute numbers the method doesn't win.

- **Single-architecture evaluation.** IRIS is evaluated exclusively on Janus-Pro (1B and 7B), an autoregressive T2I model. The paper acknowledges in Section 4.4 that T2I model architectures are diverse (diffusion, masked modeling, MAE-style), but no experiments demonstrate whether the NSC reward generalizes across architectures. This limits confidence in the breadth of the claimed phenomenon, though the paper is upfront about this scope limitation.

- **Causal mechanism is underspecified.** The paper establishes a compelling correlation (low self-certainty ↔ better images) and shows that using NSC as a reward works, but does not probe *why* the effect occurs at a mechanistic level. The ablation showing direct NSC optimization collapses (Figure 9) hints at a non-trivial dynamic, but the paper does not analyze how token-level uncertainty distributions change through training or connect them to observable image properties. This does not undermine the method's validity, but deeper analysis would strengthen the contribution.

- **"Emergence of reasoning" claim is loosely supported.** Section 4.2 frames the generation of semantic CoTs as "emergence of long-form reasoning," but the evidence is primarily qualitative (Figure 4 and appendix examples). Improved benchmark scores demonstrate better image generation, not necessarily better *reasoning* in a compositional sense. The paper would benefit from separating visual quality improvements from claims about reasoning capability.

### Trivial

- **SC naming convention is counterintuitive.** Higher SC = KL(U||π) means the distribution is closer to uniform, i.e., *less* certain in the conventional sense. The paper acknowledges this (Equation 2 makes NSC = −SC explicit), but the inverted semantics may confuse readers on first pass. A brief clarifying note early in Section 3.2 would help.

- **Forward KL motivation conflates mode-covering with flatness.** The paper describes forward KL as "mode-covering" (which is correct for KL(π||U) — wait, actually KL(U||π) is forward KL from uniform to model; KL(π||U) is backward KL from model to uniform. Forward KL is indeed mode-covering in the sense that it penalizes the model for placing low probability where the reference (here, uniform) has mass, encouraging coverage of the full vocabulary. But "covering multiple plausible outcomes" is different from "driving toward a flat distribution." The conceptual motivation could be more precise, though the empirical choice of forward over backward KL is well-validated by Figure 8.

- **Single-run results without seed analysis.** The paper reports results from what appears to be a single training run per configuration. While standard deviations are reported for benchmark evaluation (multiple prompts/images), run-to-run training variance is not discussed. Given the small absolute differences between IRIS and T2I-R1, a note on training stability across seeds would strengthen confidence.

## Nice-to-Haves

- **Validate key ablation on an independent benchmark.** The ablation studies (Section 4.3) are evaluated exclusively using the four reward models (HPSv2, DINO, GIT, ORM) that were also used to train the T2I-R1 baseline. Spot-checking the most critical ablation (e.g., minimizing text+image SC vs. image-only SC) on GenEval or T2I-CompBench would eliminate any residual concern about metric bias, even though the main claims are already validated independently.

- **Computational cost comparison.** A brief note on the training throughput or memory footprint of IRIS relative to external-reward training (which requires running multiple reward models at each step) would strengthen the practical motivation for a purely intrinsic approach.

- **Deeper mechanistic analysis.** Show probability-mass histograms for image tokens in high-quality vs. low-quality samples, or track how token-level uncertainty distributions evolve over training. This would convert the correlation-based narrative into a more satisfying mechanistic story.

- **Test on additional T2I architectures.** Even a small-scale experiment on a diffusion-based model would test the generality of the NSC phenomenon across model families.

## Removed Points

These points are flagged to be removed — treat them with caution:

- **Harsh Critic's concern about ablation evaluation metrics introducing bias (Critical Issue 3):** The critic argues that using the same four reward models for ablation evaluation as were used to train T2I-R1 "can introduce an implicit bias." On closer inspection, this concern is misplaced. The reward models were used to *train* T2I-R1 — if anything, they are biased *in favor of* T2I-R1, not IRIS. IRIS never sees these rewards during training, so its strong performance on them is actually *more* convincing, not less. Furthermore, the main claims are validated on three independent benchmarks (GenEval, T2I-CompBench, WISE) that have no connection to the training of T2I-R1's reward models. The ablation evaluation strategy is standard and reasonable. **Removed — concern does not hold up under scrutiny.**

- **Harsh Critic's concern about reproducibility due to missing appendix:** The critic notes that "the reproducibility of the results is hampered in the main text by omitted details... These likely reside in the stripped appendix." Per the hard rules, criticisms about missing appendix content are to be removed since the appendix is stripped by the parser and exists in the original submission. **Removed.**

- **Harsh Critic's section note about Figure 2 generalizability:** "The statement is therefore much broader than the data." The paper compares one LLM (Qwen2.5-1.5B) and one multimodal LLM (Janus-Pro-1B). While the generalization claim could be more circumscribed, the paper also provides substantial within-domain ablation evidence (Figures 6, 7) on the T2I side. This is already captured in the minor weakness about single-architecture evaluation. **Merged — not separately listed.**

## Novel Insights

The most genuinely novel insight emerging from this work is the task-dependent nature of self-certainty as an optimization signal: maximizing self-certainty (pushing the output distribution toward peaked, confident predictions) benefits objective reasoning tasks like math, while *minimizing* self-certainty (encouraging flatter, less confident distributions) benefits subjective generative tasks like image synthesis. This is not merely an empirical curiosity — it is supported by converging evidence from both training dynamics (Figure 2) and controlled ablations (Figures 6, 7), and it suggests that different modalities within a single multimodal model may require *opposite* optimization pressures. This has implications beyond T2I generation for the design of unified multimodal training objectives.

## Suggestions

- **Reframe the headline claim.** The strongest message is that IRIS achieves parity with external-reward training *without any external supervision*, opening the door to scalable, domain-agnostic T2I alignment. Shift the narrative to emphasize this, and present the external-reward comparison as validation of effectiveness rather than as a contest for highest score.

- **Add a brief discussion of training stability.** Even a sentence noting whether results are consistent across 2-3 random seeds (or reporting that the training dynamics are stable based on qualitative observation) would address the seed-analysis concern.

- **Tone down "reasoning" language** in the discussion of CoT generation. The paper's evidence supports improved image quality and diversity, not necessarily enhanced compositional reasoning. A more precise framing would strengthen credibility.

## Score and Decision

**Anchor comparison summary:**

| Anchor | Score | Round | Comparison to IRIS |
|--------|-------|-------|-------------------|
| FTpdQBoBd0 | 3.00 | R1 | IRIS is substantially stronger |
| Fk4Op9wpEp | 3.00 | R1 | IRIS is substantially stronger |
| 9LAqIWi3QG | 3.00 | R1 | IRIS is substantially stronger |
| oqRe1KvD17 | 3.00 | R1 | IRIS is substantially stronger |
| 7pVIFJW2Hp | 5.50 | R1 | IRIS is clearly stronger |
| sJAlw561AH | 5.50 | R2 | IRIS is clearly stronger |
| UnuSBQjgqK | 5.75 | R2 | IRIS is stronger |
| Let8OMe20n | 6.00 | R1 | IRIS is stronger (more novel, more comprehensive) |
| vxutwN3xQN | 6.00 | R1 | Different type of contribution |
| eC2ICbECNM | 6.00 | R2 | IRIS is stronger (purely intrinsic, more benchmarks) |
| Ugs2W5XFFo | 6.00 | R2 | IRIS is stronger (more benchmarks, more ablations) |
| cQ25MQQSNI | 6.00 | R2 | Different type of contribution |
| cJQ1K2fjpD | 6.20 | R2 | IRIS is comparable (similar self-alignment concept; IRIS more novel insight) |
| sgAp2qG86e | 6.25 | R2 | Different type of contribution; comparable quality tier |
| kIP0duasBb | 6.67 | R1 | IRIS is comparable (stronger concept, similar execution) |
| SI2hI0frk6 | 7.60 | R1 | IRIS is below this tier |
| QEHrmQPBdd | 8.00 | R1 | IRIS is below this tier |
| gU58d5QeGv | 8.00 | R1 | IRIS is below this tier |
| N8Oj1XhtYZ | 8.50 | R1 | IRIS is below this tier |

**Round 1 bracket:** 5.5–7.0

**Round 2 narrowing:** IRIS is clearly above the 6.0 cluster (eC2ICbECNM, Ugs2W5XFFo, Let8OMe20n), comparable to cJQ1K2fjpD (6.20) and kIP0duasBb (6.67). IRIS offers a more novel conceptual contribution than kIP0duasBb but has some minor overstatement and scope limitations that keep it from exceeding the 7.0 threshold. **Final score: 6.5.**

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>
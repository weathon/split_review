Now I have all the information I need. Let me synthesize the final review.

**Calibration summary:**

| Anchor | Score | Round | Comparison |
|--------|-------|-------|------------|
| Confidence-aware T2I reward (Let8OMe20n) | 6.00 | R2 | Accepted. Addresses reward overoptimization; novelty is lower than IRIS. IRIS has clearer contribution and more thorough ablations. |
| MI-TUNE (Ugs2W5XFFo) | 6.00 | R2 | Accepted. Self-supervised MI-based alignment; considered somewhat simple/incremental. IRIS has stronger novelty. |
| Multi-reward editing (9RFocgIccP) | 6.00 | R1 | Accepted. Uses GPT-4o rewards; reliance on proprietary model is a weakness. IRIS avoids external models entirely, a strength. |
| Generative Models probing (xkR3bcswuC) | 5.75 | R1 | Rejected. Incremental, insufficient claim support. IRIS is clearly stronger. |
| FiSAO (cJQ1K2fjpD) | 6.20 | R2 | Accepted. Token-level rewards for VLMs; strong evaluation but clarity issues. Comparable to IRIS. |
| RLCF CLIP reward TTA (kIP0duasBb) | 6.67 | R2 | Accepted. Test-time adaptation with CLIP reward; good universality across tasks. Some reviewers noted incremental novelty. IRIS is similarly positioned. |
| Video grounding (G6dMvRuhFr) | 7.33 | R1 | Accepted. Thorough experiments across 30+ tasks; stronger evaluation scope than IRIS. |

**Round 1 bracket:** [5.75, 7.33]
**Narrowing:** IRIS is clearly above the 5.75 rejected paper and comparable to the 6.0–6.67 accepted papers. It has stronger novelty than the 6.0 papers but less comprehensive architecture coverage than the 7.33 paper. The paper's contribution is solid and well-supported; weaknesses are real but non-fatal.
**Final score: 6.5**

Now writing the review.## Summary

IRIS proposes the first reinforcement learning framework for autoregressive text-to-image generation that uses only an intrinsic reward — negative self-certainty (NSC), defined as the forward KL divergence between the model's output distribution and a uniform distribution. The central finding is that, contrary to text-domain LLMs where maximizing self-certainty helps, minimizing self-certainty improves image generation quality. Evaluated on Janus-Pro (1B and 7B) across GenEval, T2I-CompBench, and WISE, IRIS achieves scores competitive with external-reward baselines (e.g., GenEval 0.72 vs. 0.75, WISE 0.37 vs. 0.38 for 1B) without any human-labeled data or domain-specific verifiers. A thorough ablation suite validates the design choices (CoT, minimization direction, forward KL, RL-based optimization).

## Strengths

- **First intrinsic-only RL framework for T2I generation.** The core idea — using the model's own (negative) self-certainty as a reward signal — is clean, well-motivated, and demonstrably effective. This contrasts with the standard practice of maximizing self-certainty in text-domain LLMs (Zhao et al., 2025b; Zhang et al., 2025a), making the finding genuinely novel and the task-dependent behavior of self-certainty an interesting insight.

- **Competitive performance without any external supervision.** Table 1 shows that IRIS achieves scores close to T2I-R1 (which uses four external reward models) across all three benchmarks and both model scales. Given that IRIS uses no human preferences, object detectors, or VQA models, this is a compelling result that validates the intrinsic-reward approach.

- **Thorough and well-designed ablation studies.** Figures 5–9 systematically validate every component: the necessity of CoTs, the direction of self-certainty minimization (for both text and image tokens), the advantage of forward KL over entropy, and the importance of RL-based optimization over direct NSC maximization. The ablations are cleanly designed and the conclusions are consistent across all four evaluation metrics.

- **Methodological diligence in baseline correction.** The paper identifies and corrects a chat-template inconsistency in the official T2I-R1 implementation that affected Janus-Pro models (Section 4.1). This careful attention to experimental detail strengthens the reliability of the reported comparisons.

- **Consistent gains across two model scales.** IRIS improves both Janus-Pro-1B and Janus-Pro-7B, with the 7B model reaching GenEval 0.77, T2I-CompBench 0.3916, and WISE 0.48, demonstrating that the intrinsic reward signal remains effective at larger model sizes.

## Weaknesses

### Major
None.

### Minor

1. **Motivating observation (Fig. 2) is under-supported.** The claim that "RL alignment with external reward models decreases the self-certainty of the multimodal LLM in text-to-image generation" rests on a single training run with no error bars or multiple seeds. The absolute change in image self-certainty is small (~20.2 → ~19.0, roughly 6%). While this observation is *motivational* rather than central — the ablation studies (Figs. 6, 7) independently validate that minimizing SC is the correct direction — the paper's narrative relies heavily on this figure. Confidence intervals or multi-seed results would substantially strengthen it.

2. **Ablations evaluated on proxy metrics, not on the three main benchmarks.** Figures 5–9 use HPSv2, GIT, GDino, and ORM as evaluation metrics for the ablation studies. While these are independent (not used in training) and reasonable proxies, the paper's central claims rest on GenEval, T2I-CompBench, and WISE scores (Table 1). There is no evidence that the ablation trends (e.g., "minimizing image SC outperforms maximizing") hold on these benchmark pipelines. Given that the ablations validate fundamental design choices, confirming the key trends on at least one main benchmark would strengthen the conclusions. The paper's justification (the four metrics are "unbiased") is reasonable, but the gap remains.

3. **Limited architecture scope despite "agnostic" claim.** IRIS is validated only on Janus-Pro, an autoregressive multimodal LLM. The paper states IRIS "is agnostic to the model architecture" (Section 3.2), but this claim is unsupported — the method's effectiveness on diffusion models, masked modeling, or other T2I architectures is unknown. The paper acknowledges this limitation in Section 4.4, which is commendable, but the "agnostic" claim in the introduction should be tempered to match the empirical scope.

4. **Reasoning improvement claims are somewhat overstated.** The abstract states IRIS "significantly enhance[s] the reasoning capabilities of T2I models." The primary evidence is the WISE benchmark, where the 1B model improves from 0.28 to 0.37 (+32% relative) but the 7B model improves only from 0.46 to 0.48 (+4.3%). Moreover, IRIS's WISE scores (0.37/0.48) remain below T2I-R1 (0.38/0.50). The improvements on GenEval and T2I-CompBench reflect general generation quality rather than reasoning per se. The contribution should be framed primarily as improving generation quality without external supervision, with reasoning gains as a secondary observation.

5. **T2I-R1 baseline composition is not fully specified.** The paper lists the four external rewards (HPSv2, DINO, GIT, ORM) but does not state how they are combined into a single reward signal (e.g., weighted sum, product, learned combination). While the paper cites the original T2I-R1 paper — and the composition may be defined there — the reader cannot assess whether the baseline was fairly configured without cross-referencing. A brief description of the combination method would resolve this.

### Trivial

- Figure 2's y-axes have different scales (left: 31–38, right: 18.75–20.50), which slightly exaggerates the visual contrast between the two curves.
- Some notation inconsistencies (e.g., "T2I-R1" vs. "T2I-RI" in the text; likely a minor typo from the OCR process).

## Nice-to-Haves

- **Anchor Fig. 2 with stronger evidence.** Computing self-certainty at intervals across multiple independent training runs (with error bars), or providing a direct causal experiment (perturbing output distribution to increase entropy and measuring benchmark impact), would make the central observation more robust.
- **CoT diversity analysis.** The paper hypothesizes that minimizing text SC encourages more diverse semantic CoTs, but never measures CoT diversity (length, semantic variety, etc.). A simple analysis would directly validate this mechanism.
- **Ablation on GRPO group size G** and **sensitivity analysis on KL coefficient β** would further strengthen the method's grounding.
- **Human evaluation** (e.g., pairwise preference between IRIS and baseline on 50–100 prompts) would provide compelling evidence beyond automated metrics.

## Removed Points

The following points from the source reviews were removed for the reasons given:
- *Missing discussion of intrinsic rewards in vision/generation models* — Removed per rule: cannot cite missing related works without external sources to confirm existence.
- *Terminology nitpick about "self-certainty" vs. "confidence"* — Pure presentation preference, not a substantive weakness.
- *Criticism about the appendix being removed* — The paper text "Rest of paper (reference and Appendix) is removed" is a parser artifact, not an author omission.
- *Criticism about Fig. 1 having only 3 prompts* — This is a qualitative illustration, not a quantitative claim; the criticism asks for what is already provided as a motivating example.
- *Missing open-source release / code availability* — Speculation about future release status; also a reproducibility concern disputed by the rule that cited artifacts are assumed to exist.
- *Formatting/style nits* — Removed as parser artifacts.

## Novel Insights

The reviewers' perspectives converge on the paper's most interesting finding beyond its own claims: **the task-dependent behavior of self-certainty**. The paper shows that the same KL-based self-certainty measure that benefits language reasoning harms image generation, and vice versa. This creates an interesting tension: the intrinsic reward that works for text (maximizing SC) is the *opposite* of what works for images. The paper's ablations go further to show that this tension exists even within the same multimodal model — minimizing SC on image tokens helps while maximizing SC on text tokens hurts (or vice versa). This suggests that self-certainty is not a monolithic property but is modality-dependent, which has implications for designing intrinsic rewards in multimodal settings where different output modalities may require different regularization strategies.

## Suggestions

1. Add confidence intervals or multiple seeds to Fig. 2 to substantiate the motivating observation.
2. Confirm at least the key ablation trend (minimizing vs. maximizing SC) on one of the three main benchmarks (e.g., GenEval), even at a coarser granularity.
3. Soften the "agnostic to architecture" claim to match the empirical scope, or add a proof-of-concept on a second architecture (e.g., a diffusion model).
4. Specify the reward composition for the T2I-R1 baseline.
5. Tone down the "reasoning capabilities" claim in the abstract and focus on the primary contribution: improving T2I generation quality via an intrinsic self-uncertainty reward.

## Score and Decision

| Anchor | Avg Score | Round | Comparison to this paper |
|--------|-----------|-------|-------------------------|
| Confidence-aware T2I reward (Let8OMe20n) | 6.00 | R2 | Less novel contribution; IRIS has clearer novelty. |
| MI-TUNE (Ugs2W5XFFo) | 6.00 | R2 | More incremental; IRIS has stronger contribution. |
| Multi-reward editing (9RFocgIccP) | 6.00 | R1 | Relies on GPT-4o rewards; IRIS avoids external models. |
| Generative Models probing (xkR3bcswuC) | 5.75 | R1 | Rejected for insufficient support; IRIS is clearly stronger. |
| FiSAO VLM alignment (cJQ1K2fjpD) | 6.20 | R2 | Comparable strength; IRIS has better-controlled experiments. |
| RLCF CLIP reward TTA (kIP0duasBb) | 6.67 | R2 | Similar level; IRIS more novel, RLCF more task coverage. |
| Video grounding (G6dMvRuhFr) | 7.33 | R1 | More comprehensive evaluation; IRIS has narrower scope. |

**Round 1 bracket:** [5.75, 7.33] — clearly above the 3.0–3.4 weak band and below the 8.0 theoretical papers.

**Round 2 narrowing:** Compared against 6.0–6.7 accepted papers in T2I alignment and VLM adaptation. IRIS has stronger novelty than the 6.0 papers (first intrinsic-only RL for T2I, the task-dependent self-certainty finding) and competitive experimental rigor, but its architecture scope and ablation-benchmark gap limit it relative to the upper end of the bracket.

**Final score: 6.5**

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>
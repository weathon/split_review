## Summary

This paper proposes Forget-to-Focus (F2F), a two-stage protocol that first performs targeted unlearning on a general-domain "forget" set (with an optional retain set for stability), then fine-tunes on a target domain. The core idea is that suppressing irrelevant pretraining knowledge before fine-tuning can mitigate negative transfer and improve specialization. Experiments across five model scales (0.6B–72B), three domains (coding, math, medical), and multiple unlearning and fine-tuning methods consistently show that F2F outperforms standard fine-tuning and several baselines (e.g., HumanEval pass@1 improves from 31.71 to 42.07 for Qwen-0.6B, and from 71.12 to 78.50 for Qwen-72B).

## Strengths

- **Consistent performance gains across diverse models, domains, and methods.** Table 1 shows F2F (Unl_{GA+GD}+SFT) achieves the best or second-best pass@1 on HumanEval and MBPP across all five tested models (Qwen 0.6B, Gemma 2B, LLaMA 8B, LLaMA 13B, Qwen 72B), with substantial gains such as Qwen 0.6B HumanEval rising from 31.71 (SFT) to 42.07. The pattern holds across coding, medical, and math domains, strengthening confidence that the effect is real.

- **Systematic ablation on forget-set quality.** Table 3 compares BC-Select, BC-Mixed, and BC-Cosine forget sets across three domains and three models, showing that curated forget sets (BC-Select) consistently yield higher downstream performance (e.g., Qwen 0.6B MBPP 31.60 vs. 29.90 for BC-Mixed). This is rigorous analysis of an important design choice.

- **Scale analysis from 0.6B to 72B parameters.** The inclusion of results on Qwen-2 72B-Instruct, LLaMA-2 13B, LLaMA 3.1 8B, Gemma 2B, and Qwen-3 0.6B demonstrates that the protocol works across a wide range of model capacities.

- **Representational-geometry evidence.** Section 4.5 uses linear CKA and SVCCA heatmaps to show that F2F induces a more pronounced representational shift from the base model than standard fine-tuning, providing empirical evidence that unlearning reshapes internal representations.

## Weaknesses

### Major

- **Unsubstantiated calibration claim in abstract and conclusion.** The abstract states that F2F "improves calibration on medical QA tasks, reducing overconfidence and mitigating reliability issues that persist under standard fine-tuning," and the conclusion repeats that F2F "improves calibration on sensitive QA." However, the main paper contains **no calibration experiments, no ECE plots, no reliability diagrams, and no quantitative calibration results of any kind.** This is a specific, testable claim presented as a core contribution, with zero supporting evidence in the paper body. Either the claim must be removed or the evidence must be added. This is the paper's most serious overclaim.

- **Forget-set size impact is claimed but not tested.** The contribution list states that "both the size and quality of the forget set significantly impact fine-tuning performance." Quality is tested (BC-Select vs. BC-Mixed vs. BC-Cosine), but size is never ablated: the paper uses 100 samples for Qwen-0.6B and 1000 for larger models, with no within-model sweep over forget-set cardinality. A claimed finding is listed in the contributions but not experimentally demonstrated.

- **Abstract number inconsistency.** The abstract reports that F2F improves HumanEval pass@1 by "11.95% on Qwen 72B model compared to standard fine-tuning." From Table 1, the actual gain over SFT (standard fine-tuning) for Qwen-72B is (78.50 − 71.12)/71.12 ≈ 10.4%, not 11.95%. The 11.95% figure matches the gain over the *base model* (78.50 vs. 70.12), not over standard fine-tuning. This inconsistency should be corrected.

### Minor

- **Theory is disconnected from experimental validation.** The corollary predicts that "increasing the forget-to-retain ratio λ/σ tightens the starting distance for fine-tuning and hence improves both the iteration complexity and the final risk bound." Yet λ=1.0 and σ=0.5 are fixed in all experiments (except the GA-only variant where σ=0). Varying λ/σ would directly test this theoretical prediction; its absence makes the theoretical section feel like motivational scaffolding rather than a testable framework.

- **Fisher information and PCA-shift analyses are promised but absent from the main text.** The contribution list (§1) mentions "Fisher information, PCA-shift analyses" as part of the representational analysis, and the conclusion references them ("induces clear representational shifts (via CKA/SVCCA, Fisher, PCA)"). The main paper only presents CKA and SVCCA (§4.5). If these analyses exist in the appendix, the main text should at minimum summarize the key findings. As presented, this is a mismatch between claimed and delivered content.

- **DAPT baseline is underspecified.** DAPT is described as "continue unsupervised pretraining on domain specific text prior to task-specific fine-tuning" but the actual domain-specific text source is never identified (e.g., for coding: is it OpenCoder's training set? for medical: PubMed abstracts?). The quality of this baseline depends entirely on the data choice, and the reader cannot evaluate its fairness.

- **No error bars or variance estimates.** All tables report single-run point estimates. Several comparisons involve small absolute differences (e.g., Qwen-0.6B MBPP: F2F 31.60 vs. CurLoRA 31.00). Without variance estimates (standard deviations over multiple seeds), it is unclear whether these differences are reliable.

- **CKA/SVCCA interpretation is correlational.** The paper interprets F2F's larger representational shift as "more conducive to in-domain specialization" but provides no causal evidence linking the magnitude of CKA divergence to better fine-tuning outcomes. Lower similarity could also reflect representational collapse. This analysis would be strengthened by a control condition (e.g., random initialization) or probing experiments.

- **Table 2 heading is misleading.** The section is titled "F2F W/ FINE-TUNING VARIANTS" but the table reports only standard fine-tuning baselines (SFT, LoRA, CurlLoRA, DAPT) — none of which involve the F2F protocol. Rename or relocate for clarity.

### Trivial

- The conclusion claims F2F enables "stabler optimization" but no loss trajectories or gradient norm plots are shown. Adding fine-tuning loss curves would provide direct behavioral evidence for this claim.

## Nice-to-Haves

- A sweep over forget-set size (e.g., 100, 500, 1000, 5000 samples for a single model) would connect the "size" claim to actual data and provide practical guidance.
- Varying λ/σ would directly test the theoretical prediction and strengthen internal coherence.
- Fine-tuning loss curves (with vs. without unlearning) would provide direct evidence for the claimed optimization benefits.

## Removed Points

These points were flagged by reviewers but are removed for the reasons stated:

- **"Figure 3 y-axis scale is ambiguous"** — The figure captions and text adequately describe the results; this is a parser artifact in how the image was extracted.
- **"bfloat16 for Qwen-72B as a potential confound"** — The paper transparently states this in §3.4; it is documented, not hidden.
- **"Missing related works"** — The instruction prohibits including this criticism.
- **"Formatting/style nitpicks"** — Parser artifacts, not author errors.
- **"This reads as an interesting but incomplete empirical study"** (subjective framing from a reviewer) — Not a weakness, just an opinion; superseded by the concrete weaknesses above.

## Novel Insights

The most interesting observation not fully emphasized by the paper is that aggressive unlearning (GA-only, σ=0) can *improve* fine-tuning for larger models (LLaMA-8B) while *hurting* it for smaller models (Qwen-0.6B). This suggests an interaction between model capacity and the need for stability-preserving retention that the paper could explore more deeply — perhaps smaller models have less redundant representational capacity and thus benefit more from the retain set's stabilizing effect. This scale-dependent behavior is more valuable than the headline accuracy numbers and deserves a dedicated analysis.

## Suggestions

1. Either add calibration experiments (ECE, reliability diagrams) to the main paper, or remove the calibration claim from the abstract and conclusion.
2. Correct the abstract's 11.95% number or clarify which baseline it compares against.
3. Either add a forget-set-size ablation or correct the contribution list to remove the unsupported claim about size impact.
4. Summarize any Fisher/PCA analyses from the appendix in the main text, or remove them from the contribution list.
5. Specify the DAPT data source for each domain.
6. Add variance estimates (or at minimum, clarify the number of runs per experiment).

## Score and Decision

### Calibration Anchors

**Round 1 (bracketing):**
| Anchor ID | Avg Score | Band | Comparison |
|-----------|-----------|------|------------|
| ijwYWoChN9 | 3.00 | Low (<3.5) | Domain Shift Tuning — weaker, narrower experiments |
| ZbOSRZ0JXH | 3.00 | Low (<3.5) | Beyond Finite Data — weaker, less direct relevance |
| qgLyKwXVDs | 2.00 | Low (<3.5) | FreeLM — far weaker |
| 49ti6LOUw5 | 3.00 | Low (<3.5) | UnoLoRA — weaker |
| hkQOYyUChL | 4.25 | Mid (3.5–7.5) | Learning & Forgetting Unsafe Examples — narrower, less novel |
| 6ESRicalFE | 6.50 | Mid | LLM Unlearning via Loss Adjustment — cleaner paper, accepted |
| IhbZytsinc | 6.00 | Mid | Minifinetuning — similar domain adaptation scope, rejected |
| Nsms7NeU2x | 6.75 | Mid | How much can we Forget — stronger theory+experiments |
| gc8QAQfXv6 | 9.00 | High (>7.5) | Function Vectors for CF — far stronger, a different tier |
| 51WraMid8K | 8.00 | High | Probabilistic Perspective on Unlearning — far stronger |
| PBjCTeDL6o | 8.00 | High | Unlearning-based Neural Interpretations — far stronger |
| SPS6HzVzyt | 8.00 | High | Context-Parametric Inversion — far stronger |

**Round 2 (narrowing within 5.0–6.5 bracket):**
| Anchor ID | Avg Score | Comparison |
|-----------|-----------|------------|
| CIN2VRxPKU | 5.33 | Evaluating Deep Unlearning — rejected, comparable rigor issues |
| uDjuCpQH5N | 5.50 | Do Unlearning Methods Remove Information — rejected, comparable |
| J9Ofr1PmvX | 5.50 | UnSTAR — rejected with mixed reviews; F2F is slightly stronger empirically |
| tmsqb6WpLz | 5.75 | Dissecting learning and forgetting — accepted; F2F has more novel idea but more overclaims; comparable overall |
| Q1MHvGmhyT | 6.00 | A Closer Look at Machine Unlearning — accepted; F2F is weaker (more evidential gaps) |
| 8SPSIfR2e0 | 5.75 | Dissecting Language Models via Selective Pruning — rejected; similar quality |

**Initial bracket:** 5.0–6.5 after round 1. **Narrowing through round 2:** The paper is comparable to the 5.50–5.75 reject-level papers but weaker than the 6.00 accepted paper. Its core idea is stronger than the reject anchors, but its overclaims (calibration, forget-set-size, missing Fisher/PCA) are more numerous. **Final score: 5.5.**

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>
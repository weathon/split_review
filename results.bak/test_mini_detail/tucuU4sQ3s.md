Now I have everything I need. Let me compile the final review.

## Summary

This paper proposes NuSA-CL, a memory-free continual learning framework for CLIP that identifies an approximate null space of each weight matrix via SVD, constrains low-rank updates to that subspace via a persistent constraint, and then merges the update into the backbone. This enables fixed-parameter-budget adaptation across tasks without replay buffers, distillation, or growing module counts. Experiments on MTIL (11 datasets) and CIFAR-100 class-incremental benchmarks show NuSA-CL significantly outperforms other storage-free PEFT methods (LoRA, MiLoRA) and remains competitive with storage-based approaches at a fraction of the computational cost.

## Strengths

- **Principled method with theoretical motivation.** Lemma 1 proves that updates confined to the null space satisfy a bounded parameter-space interference bound, and Theorem 2 extends this to cumulative interference across tasks. While the bound is in parameter space (not function space), which the authors acknowledge, it still provides formal grounding that storage-free PEFT baselines (LoRA, MiLoRA) lack.

- **Clear and decisive performance-efficiency advantage in the storage-free regime.** On the MTIL benchmark (Table 1), NuSA-CL uses only 1.5M trainable parameters (10× fewer than LoRA's 15.7M, 40× fewer than MoE-Adapters' 59.8M), zero additional storage, and 1.21 GPU-hours (nearly 3× faster than MoE-Adapters' 3.42h), while achieving Transfer 68.6%, Avg 75.1%, and Last 82.8% — the best among all storage-free methods. The 5-shot results (Table 2) are also consistent, with NuSA-CL leading Avg (70.3%) and Last (75.4%) across all 11 datasets.

- **Scalability validated on long task sequences.** On CIFAR-100 with 50 sequential tasks (Table 3), NuSA-CL achieves Last accuracy 71.85%, outperforming ZSCL (67.36%) by 4.4 pp, with the gap widening at longer sequences. This directly supports the claim that null-space-guided updates do not saturate even after extensive adaptation.

- **Well-designed ablation studies.** The ablation of subspace choice (Fig 3a) convincingly shows the *Tail* (null-like) subspace yields the lowest forgetting across all ranks. The persistent constraint ablation (Table 4a) is critical: unfreezing the null space bases drops Transfer from 68.58% to 62.60%, confirming that strict confinement matters, not just initialization. The SVD efficiency analysis (Table 4b) is also compelling — <1 minute per task vs. ~81 minutes for InLoRA.

- **Null-space dynamics visualization provides mechanistic insight.** Figure 2 shows that NuSA-CL's effective rank steadily increases across tasks while LoRA and Full-FT remain static, providing direct spectral evidence that the method accumulates knowledge in previously underutilized directions rather than overwriting principal components.

## Weaknesses

### Major

None.

### Minor

1. **No variance or multiple-run statistics reported.** All tables present single numbers without standard deviations or confidence intervals. Given that continual learning results can be sensitive to dataset splits, task order, and initialization, it is difficult to assess whether reported margins (e.g., 68.6 vs. 66.2 Transfer in Table 1) are statistically meaningful. This is a standard expectation in benchmarking papers and should be addressed. (Confirmed by verifying Tables 1–4 in the paper — no std values appear anywhere.)

2. **Evaluation protocol for seen tasks in MTIL is underspecified.** The paper defines Transfer as zero-shot accuracy on unseen tasks, but it does not clarify how seen-task classification is performed for Avg and Last metrics. If zero-shot text prompts are used for all tasks (including seen ones), this should be stated explicitly. If task-specific heads are used, the description should note that these heads are not stored across tasks. The current ambiguity is relevant because storage-based baselines (MoE-Adapters, DIKI) can use per-task modules at test time — an asymmetric advantage in the comparison. (The paper's experimental setup section on page 5 describes metrics but does not specify the evaluation mechanism for seen tasks.)

3. **Only ViT-B/16 is tested.** The paper claims generalizability to larger models but only evaluates on ViT-B/16. While attention projections in larger CLIP variants (ViT-L, ViT-H) remain moderate in size (768–1024), the claim would be stronger with at least one additional backbone result. The paper's own conclusion notes SVD could become a bottleneck for substantially larger models but does not test this.

### Trivial

None.

## Nice-to-Haves

- A task-order sensitivity experiment (e.g., 3 random permutations of the 11 MTIL tasks) would address a natural concern about the method's robustness. The paper lists this as future work, but it would be a low-cost addition.
- A brief justification for why only attention projection matrices are adapted (and not MLP layers) would improve clarity.
- Presenting the long-sequence CIFAR-100 spectral analysis from the cited appendix in the main paper would strengthen the saturation claim.

## Removed Points

These points were considered but removed after verification against the paper:

- **"The theoretical motivation is weaker than the paper's framing implies"** — The paper explicitly qualifies the bound as "a local stability condition rather than a full function-level guarantee" (line 128). The paper does not overstate the theory; it states the limitation clearly. The strength of the method's support comes from both the theoretical bound and the empirical ablations, which is appropriate.

- **"Storage-based vs. storage-free comparison is not apples-to-apples"** — While the evaluation protocol for seen tasks is underspecified, the paper's main claim is about the *storage-free* setting (Tables 1–2 clearly bold only the top storage-free performer). The storage-based comparison is presented as context, not as a direct head-to-head. Removing this reduces noise.

- **"Why only attention projection matrices are adapted"** — This is a design choice common across PEFT literature. Asking for justification is scope creep; the paper's experiments validate the choice empirically.

- **"Missing related works"** — Per instructions, I cannot raise this without external sources.

## Novel Insights

None beyond the paper's own contributions. The reviews did not surface any perspective or connection not already present in the paper.

## Suggestions

1. Add standard deviations from at least 3 random seeds for all main results (Tables 1–3).
2. Explicitly state the evaluation protocol for seen tasks in MTIL — whether zero-shot text prompting or learned probes are used for Avg and Last metrics — ideally in a single sentence in Section 5.1.
3. Include results on at least one additional backbone (e.g., ViT-L/14) for a subset of the experiments to substantiate the generalizability claim.
4. Add a brief task-order permutation analysis (3 seeds × 3 orderings) as a table or supplementary figure.

## Score and Decision

**Score: 7.0** — This paper proposes a clean, principled, and well-validated method for memory-free continual learning of vision-language models. The null-space constrained adaptation with persistent constraint is genuinely novel, the experiments convincingly demonstrate superiority over other storage-free methods, and the ablations are thoughtful. The main weaknesses (missing variance, underspecified protocol, single backbone) are real but do not threaten the core contribution. In calibration terms, this paper is stronger than C-CLIP (avg 6.5, poster) and OVOR (avg 6.0, poster), and comparable to SD-LoRA (avg 7.5, oral) but with slightly less comprehensive theoretical analysis. The paper clearly merits acceptance.

**Decision: Accept**

### Calibration Anchors

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| /home/wg25r/review_agent/human_reviews/JIlIYIHMuv.md | 2.50 | R1 (weak) | LVLM-CL — poor presentation, missing comparisons, unclear method. Well below NuSA-CL. |
| /home/wg25r/review_agent/human_reviews/gNoqEdT2wO.md | 2.33 | R1 (weak) | Multimodal CIL benchmark — withdrawn, benchmark-only paper with limited contribution. Below NuSA-CL. |
| /home/wg25r/review_agent/human_reviews/ZaudLwn0Hm.md | 2.50 | R1 (weak) | Prototypical evolution for few-shot — withdrawn, confused scope. Below NuSA-CL. |
| /home/wg25r/review_agent/human_reviews/2L7KQ4qbHi.md | 3.00 | R1 (weak) | Concept forgetting — withdrawn, narrow contribution. Below NuSA-CL. |
| /home/wg25r/review_agent/human_reviews/sb7qHFYwBc.md | 6.50 | R1/R2 (mid) | C-CLIP — accepted poster. CL + LoRA + distillation. NuSA-CL has a more principled method and better efficiency. Slightly below NuSA-CL. |
| /home/wg25r/review_agent/human_reviews/9aZ2ixiYGd.md | 5.00 | R1 (mid) | Vision+Language Synergy — accepted poster but scores 3,3,6,8. Uses ChatGPT for descriptions (unfair advantage concern). Below NuSA-CL. |
| /home/wg25r/review_agent/human_reviews/QYgtZRTv3e.md | 4.50 | R1 (mid) | TIPS — withdrawn. Prompt-based method, limited novelty. Below NuSA-CL. |
| /home/wg25r/review_agent/human_reviews/EKfcngSxwD.md | 4.67 | R1 (mid) | Task Codebook — rejected. Limited novelty, MoE-like. Below NuSA-CL. |
| /home/wg25r/review_agent/human_reviews/gc8QAQfXv6.md | 9.00 | R1 (strong) | Function Vectors — oral. Deep forgetting analysis in LLMs. Different domain and contribution type. Above NuSA-CL. |
| /home/wg25r/review_agent/human_reviews/uAFHCZRmXk.md | 8.00 | R1 (strong) | Modality Gap — oral. Analysis paper about CLIP. Different contribution type. Above NuSA-CL. |
| /home/wg25r/review_agent/human_reviews/1aF2D2CPHi.md | 8.00 | R1 (strong) | Open-Vocab Customization — oral. Data-free distillation. Different contribution type. Above NuSA-CL. |
| /home/wg25r/review_agent/human_reviews/3i13Gev2hV.md | 8.00 | R1 (strong) | Compositional Entailment — oral. Hyperbolic VLM. Different contribution type. Above NuSA-CL. |
| /home/wg25r/review_agent/human_reviews/5U1rlpX68A.md | 7.50 | R2 (narrow) | SD-LoRA — oral. Decoupled LoRA for CIL. Similar problem setting, slightly stronger theoretical analysis. Comparable to slightly above NuSA-CL. |
| /home/wg25r/review_agent/human_reviews/FbuyDzZTPt.md | 6.00 | R2 (narrow) | OVOR — poster. Prompt-based CIL with outlier regularization. Good method but simpler contribution. Below NuSA-CL. |
| /home/wg25r/review_agent/human_reviews/MeB86edZ1P.md | 6.50 | R2 (narrow) | Hebbian Orthogonal Projection — poster. Orthogonal projection for SNNs. Related area but different domain (SNN vs VLM). Below NuSA-CL in relevance to VLM CL. |
| /home/wg25r/review_agent/human_reviews/dOAkHmsjRX.md | 7.50 | R2 (narrow) | Budgeted Online CL — spotlight. Different approach (layer freezing). Above NuSA-CL in terms of thoroughness of resource analysis. |
| /home/wg25r/review_agent/human_reviews/DJZDgMOLXQ.md | 6.50 | R2 (narrow) | Prediction Error-based CIL — poster. Different paradigm for CIL. Comparable acceptance level. |
| /home/wg25r/review_agent/human_reviews/nAs4LdaP9Y.md | 6.33 | R2 (narrow) | Federated Orthogonal Training — poster. Orthogonal projection in federated setting. Different setting but related technique. |

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>
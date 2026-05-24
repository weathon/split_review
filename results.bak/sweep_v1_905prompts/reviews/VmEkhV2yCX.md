Now I have sufficient calibration data. Let me synthesize the final review.

**Bracket determination**: Round 1 placed this paper between approximately 6.0 and 8.0. Round 2 narrowed the comparison to similar systematic studies: the "code data at which stage" paper (7.25, scores [5,8,8,8]) is the closest analogue. This paper is more comprehensive (includes RL phase, larger 8B models, more nuanced findings like the asymmetric principle and latent effects) but shares the same limitation of proprietary infrastructure. I place it at 7.0 — strong accept territory but below the most polished 8+ papers which typically have novel methodological contributions.

---

## Summary

This paper presents the first systematic study of where reasoning data should be placed across the full LLM training pipeline (pretraining → SFT → RL). Training 8B models from scratch for 1T tokens, the authors vary reasoning data along three axes — diversity, quality, and scale — and inject it at different pipeline stages. The central finding is that front-loading reasoning into pretraining creates a durable, compounding advantage (≈19% gain on expert benchmarks) that post-training alone cannot recover. The paper further establishes an asymmetric allocation principle: pretraining benefits most from diverse, large-scale reasoning data, while SFT is dominated by data quality. Additional findings reveal that high-quality pretraining data can have latent effects unlocked only after SFT, and that naive scaling of SFT data actively harms reasoning performance.

## Strengths

- **Compounding advantage from front-loading is convincingly demonstrated.** Table 3 shows M_LMQ+SFT_SHQ+RL at 56.66% vs M_base+SFT_SHQ+RL at 37.92% on expert benchmarks — an 18.74% gap that widens at each training stage. The "catch-up" test (Table 4) provides direct causal evidence: even 2× SFT epochs on the baseline (34.01%) cannot match the weakest reasoning-pretrained model (37.33%).

- **The asymmetric allocation principle is well-supported by crossed experiments.** Table 1 shows diversity matters in pretraining (M_LDQ at 64.09% vs M_SHQ at 54.98%), while Table 5 shows quality dominates SFT (M_res+SFT_SHQ at 44.99% vs M_res+SFT_LDQ at 31.54%). The fully-crossed design (4 base models × 3 SFT datasets = 12 models) provides rigorous evidence.

- **The latent effect finding is genuinely insightful.** Table 4 reveals that M_LMQ and M_LDQ have nearly identical pretraining scores (64.07 vs 64.09), but after SFT_SHQ, M_LMQ gains an additional +4.25% — a non-obvious result showing that high-quality pretraining data can encode dormant benefits activated only during alignment.

- **Comprehensive ablations strengthen every claim.** The paper includes experiments on: reasoning ratio sensitivity (10%/20%/40%), scaling strategy during SFT (2× LDQ vs targeted ALF*), architecture transfer (1.2B Transformer in Table 14), and both RL validation on the most challenging benchmarks (AIME24/25). This thoroughness is rare and valuable.

## Weaknesses

### Major

- **Reproducibility depends entirely on proprietary infrastructure.** The base pretraining corpus (NVIDIA 2025b), the LDQ dataset (Nemotron-Pretraining-SFT-v1 from NVIDIA 2025b), and the hybrid Mamba2+Attention architecture (NVIDIA 2025a) are all NVIDIA-internal resources. None are publicly available, and no model weights or code are released. While the experimental design is sound, independent verification or building upon these results is effectively impossible for the broader community.

- **The "catch-up" test is too narrow to fully support the strong claim.** The paper concludes that "SFT cannot compensate for a weak reasoning foundation," but only tests one form of catch-up: doubling SFT epochs on the same D_SHQ dataset. Alternative catch-up strategies (different SFT data mixtures, curriculum-based SFT, multi-stage SFT with increasing difficulty, SFT on D_LDQ or D_LMQ) could potentially close more of the gap. The claim would be more precisely scoped as "simply scaling the same high-quality SFT data cannot compensate."

- **RL evaluation is limited to a single model pair.** Only M_base+SFT_SHQ+RL and M_LMQ+SFT_SHQ+RL are compared in the RL phase (Table 3). This is just two out of the many possible combinations from the 4×3 design. While the results are striking, the reader cannot tell whether the compounding advantage holds across diverse pretraining conditions (e.g., M_SHQ vs M_LDQ after RL) or whether the ordering changes.

### Minor

- **The 1.2B architecture transfer experiment uses a different architecture** (pure Transformer, per the text "1.2B Transformer") from the main 8B experiments (hybrid Mamba2+Attention). This confounds architecture with scale — any discrepancy could be due to either factor. A same-architecture smaller model or a different-architecture same-scale model would cleanly disentangle the two.

- **The "first systematic study" claim is slightly overbroad.** The paper itself cites Gandhi et al. (2025), Wang et al. (2025), and Ai et al. (2025) who also inject reasoning data at early stages (mid-training). While this paper is clearly the most comprehensive, the novelty lies more in comprehensiveness and the specific asymmetric principle rather than being the first to study the question.

### Trivial
- None that are not parser artifacts.

## Nice-to-Haves

- RL evaluation on more model variants (e.g., M_SHQ vs M_LDQ backbones) would strengthen the claim that the front-loading advantage persists across all pretraining conditions.
- Testing additional catch-up strategies (different SFT data mixtures, multi-stage curriculum) would more definitively establish whether the gap is truly unclosable.
- The paper could benefit from a brief discussion of how the findings might change with even larger models (e.g., 70B+), since the 8B → 1.2B scaling already shows the pattern holds.

## Removed Points

- **Strength Finder generic strengths removed**: "This paper addressed an important problem" — too generic, no specific evidence tied to the paper's content.
- **Strength Finder "Rigorous catch-up test"** — kept as it is well-grounded in Table 4 data.
- No harsh critic inputs were provided to filter (the Harsh Critic section only contained the beginning of a paper read call, with no actual critique).

## Novel Insights

None beyond the paper's own contributions, which are themselves the most valuable output: the asymmetric allocation principle (diversity for pretraining, quality for SFT) and the latent effect of high-quality pretraining data are genuinely novel empirical discoveries that the paper earns through careful experimental design.

## Suggestions

- Release the model checkpoints (M_base, M_LDQ, M_SHQ, M_LMQ) under a research license to enable independent verification and further study. Even if the pretraining data cannot be released, the trained weights alone would be immensely valuable to the community.
- Expand the catch-up experiment to test whether alternative SFT strategies (different data mixtures, curriculum ordering, multi-stage fine-tuning) can partially close the gap, and adjust the strength of the "cannot compensate" claim accordingly.
- Extend the RL evaluation to cover at least the four pretraining conditions (base, SHQ, LDQ, LMQ) with the same SFT recipe to show the pattern holds across the full design matrix.

## Score and Decision

**Calibration anchors used (all rounds):**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| pXIbcRPxWR (Supervised Chain of Thought) | 2.50 | R1 weak | Much weaker — this paper is far more substantive |
| mfTM4UdYnC (LogicJitter) | 2.50 | R1 weak | Much weaker — no comparison |
| qgLyKwXVDs (FreeLM) | 2.00 | R1 weak | Much weaker |
| ZK1NnjpjEs (Improving LU via RL) | 3.00 | R1 weak | Much weaker |
| 506Sxc0Adp (Beyond Scale: Diversity Coeff.) | 4.00 | R1 mid | Weaker — narrower scope |
| kDakBhOaBV (Beyond Scale: Diversity Coeff. 2) | 4.00 | R1 mid | Weaker |
| oqsQbn4XfT (Diversity of Synthetic Data) | 5.80 | R1 mid | Weaker — significant methodology concerns |
| S6cBH99BhB (Enhancing Multilingual Reasoning) | 6.50 | R1 mid | Comparable — both are systematic studies, this paper is more comprehensive and uses larger models |
| eENHKMTOfW (Training Mice to Compete with Elephants) | 6.00 | R2 narrow | Weaker — narrower scope, less surprising findings |
| KIPJKST4gw (Code Data at Which Stage) | 7.25 | R2 narrow | **Most comparable** — similar research question, this paper is more comprehensive (RL phase, larger models) but shares proprietary limitations |
| 1hQKHHUsMx (What Kind of Pretraining Data) | 6.75 | R2 narrow | Slightly weaker — 80-query study vs full benchmarks |
| 3OyaXFQuDl (Smaller, Weaker, Yet Better) | 7.00 | R2 narrow | Comparable — different topic but similar rigor level |
| 07yvxWDSla (Synthetic continued pretraining) | 8.00 | R1 strong | Stronger — has a novel method contribution |
| f4gF6AIHRy (Combatting Dimensional Collapse) | 8.00 | R1 strong | Stronger — has a novel method contribution |

**Round 1 bracket:** 6.0 – 8.0  
**Round 2 narrowing:** Closest anchor is KIPJKST4gw (7.25). This paper is slightly more comprehensive in pipeline coverage but similarly limited in reproducibility. I place it just below that anchor due to the narrower catch-up test and the proprietary data constraints, yielding 7.0.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>
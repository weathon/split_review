Now I have enough calibration data. Let me finalize my assessment.

**Round 1 bracket: 6.5–7.5.** The paper is clearly above the reject zone (GE-PEFT at 4.5, CLIP Online CL at 3.8) and comparable to or stronger than the accepted papers in the 6.0–6.5 range (C-CLIP at 6.5, TiC-CLIP at 6.25, Spectral Regularization at 6.25). It has more methodological novelty and stronger ablations than C-CLIP, the most directly comparable anchor.

**Round 2 narrowing: 6.5–7.5 confirmed.** NuSA-CL has a more principled core idea (persistent null-space constraint) than C-CLIP (LoRA + contrastive loss), stronger ablations (subspace selection, persistent constraint, rank, ρ), better efficiency story (1.5M vs 15.7M params), insightful spectral dynamics analysis, and strong long-sequence results. Its weaknesses (missing CIFAR100 PEFT baselines, single backbone, theory overclaim) are similar to C-CLIP's weaknesses but not worse. The theory overclaim is partially mitigated by the paper's own acknowledgment.

**Final score: 7.0.** The paper is a solid accept — clearly above the 6.5 anchors with its more novel method and stronger analysis, but not quite at 7.5+ due to the missing PEFT baselines on CIFAR100 and single-backbone limitation.

## Summary
This paper proposes NuSA-CL, a memory-free continual learning framework for vision-language models that constrains low-rank weight updates to the approximate null space (low-energy subspace) of model parameters, identified via SVD. The update takes the form ΔW = U_n M V_n^T where only the small square matrix M is trained, giving 10× fewer trainable parameters than standard LoRA. Evaluated on the MTIL benchmark and class-incremental CIFAR100, NuSA-CL achieves competitive performance with storage-based methods while being storage-free and orders of magnitude more efficient.

## Strengths
- **Superior efficiency–performance tradeoff with concrete evidence**: Table 1 shows NuSA-CL uses 1.5M trainable parameters (40× fewer than MoE-Adapters' 59.8M, 10× fewer than LoRA's 15.7M), zero additional storage, 6.6 GB peak GPU memory, and 1.21 GPU-Hours, while achieving Transfer 68.6%, Avg. 75.1%, and Last 82.8% — competitive with storage-based methods that require external memory or expanding architectures.

- **Persistent null-space constraint validated via ablation**: Table 4a directly confirms the core design choice: unfreezing the null-space basis vectors U_n and V_n drops Transfer from 68.58% to 62.60% and Last from 82.79% to 77.32%, demonstrating that the persistent constraint (distinguishing NuSA-CL from prior SVD-guided adaptation like MiLoRA) is essential.

- **Null-space superiority directly tested**: Figure 3a shows the Tail (null-space) strategy yields 2.57% forgetting at r=128 vs. 4.44% for Top and 4.57% for Random, directly validating the central design hypothesis that low-energy spectral directions are the safest region for continual updates.

- **Scalability advantage grows with sequence length**: Table 3 shows NuSA-CL's lead over ZSCL in Last accuracy widens from 0.86% at 10 steps (74.51 vs. 73.65) to 4.49% at 50 steps (71.85 vs. 67.36), providing concrete evidence for long-term viability.

- **Best storage-free performance on 5-shot MTIL**: Table 2 shows NuSA-CL outperforms InflLoRA (which requires gradient projection memory) across all three summary metrics — Transfer (68.1% vs. 66.8%), Avg. (70.3% vs. 68.9%), and Last (75.4% vs. 74.8%) — despite being strictly storage-free.

- **Insightful spectral dynamics analysis**: Figure 2 provides novel visualization showing NuSA-CL progressively increases effective rank across tasks (e.g., vision encoder: 51.8% → 52.4%) while LoRA and Full-FT remain spectrally static, offering interpretable evidence that the method accumulates knowledge in underutilized dimensions rather than overwriting dominant components.

## Weaknesses

### Fatal
None

### Major
- **Missing PEFT baselines on CIFAR100 (Table 3)**: The class-incremental CIFAR100 experiments compare against CLIP zero-shot, Continual-FT, LwF, ICaRL, LwF-VR, and ZSCL — but not against LoRA, MiLoRA, or any other storage-free PEFT method. These are precisely the most directly relevant comparators for testing whether the null-space constraint helps over standard LoRA in the long-sequence regime. Given that LoRA and MiLoRA are already implemented for the MTIL experiments (Tables 1–2), including them in Table 3 would be straightforward. The 50-step result (71.85% Last) is the paper's most impressive long-sequence finding but loses persuasive force without the most relevant comparator class.

- **Single backbone size (ViT-B/16) only**: All experiments use CLIP ViT-B/16. The paper's central pitch includes scalability for real-world deployment, and Section 6.3 discusses larger backbones theoretically ("practitioners may adopt truncated or approximate SVD"), but provides no empirical evidence. The limitations section acknowledges "SVD step... could become a bottleneck for substantially larger models." Even a single experiment on ViT-L/14 would substantially strengthen the scalability claims that pervade the paper.

### Minor
- **Theory framing overstates what the mathematics delivers**: Section 4 is titled "Forgetting Control in Continual Learning" and Theorem 2 is labeled "Cumulative Interference Bound," framing that implies a forgetting guarantee. However, the bound (Eq. 6) measures ⟨W_{t−1}, ΔW_t⟩_F in parameter space — a measure of alignment, not a function-level forgetting bound. The paper acknowledges this ("should be viewed as a local stability condition"), but the section and theorem titles still overstate. The bound is also nearly a restatement of the construction: constraining ΔW to the null space makes it nearly orthogonal to the principal subspace by design. The empirical results are strong enough that modest theory, honestly presented, would be more persuasive.

- **Default ρ not stated in the method section**: The energy cutoff threshold ρ is a key hyperparameter that determines the null-space dimension (Eq. 1). Its default value (0.95) only appears implicitly as the bolded entry in Table 4b, not in Section 3 or Section 5.1. A reader implementing the method from Section 3 alone would not know the default threshold.

- **No variance or error bars reported**: No standard deviations or confidence intervals appear in any table. Continual learning results can be sensitive to task ordering and random seeds; reporting variance across multiple runs (at least for main results in Tables 1 and 3) would strengthen confidence in the findings.

### Trivial
None

## Nice-to-Haves
- Adding one experiment on a larger backbone (e.g., ViT-L/14) would directly address the scaling question.
- Reporting task ordering sensitivity, even briefly, would strengthen the practical deployment story.
- Explicitly stating training hyperparameters (learning rate, batch size, total training iterations per task) in the main text.
- Retitling Section 4 to "Parameter-Space Interference Analysis" to match what the math delivers, or deriving a function-level bound under Lipschitz assumptions.

## Removed Points
These points are flagged to be removed, treat them with caution.
- **Training hyperparameters not in main text**: The harsh critic notes learning rate, batch size are not stated in main text. The appendix (stripped by parser) likely contains these details — the paper explicitly references appendix tables. This is standard practice, not a flaw.
- **Strength Finder's claim of "honest theoretical framing"**: The Strength Finder lists this as a strength, but it conflicts with the verified weakness that the section title and theorem name overstate the result. The acknowledgment exists but is insufficient to offset the overclaiming framing. The weakness wins.

## Novel Insights
The spectral dynamics analysis (Figure 2) provides genuinely novel insight: NuSA-CL progressively increases effective rank across tasks while conventional methods remain spectrally inert, directly demonstrating that the method accumulates knowledge in underutilized dimensions rather than overwriting dominant components. This is a meaningful analytical contribution beyond benchmark performance. The null-space exhaustion analysis (available null directions remain >2× r_max after 10 tasks, and spectral properties stay stable after 50 CIFAR-100 steps) is also a useful empirical contribution that proactively addresses a natural objection to the approach.

## Suggestions
- Add LoRA and MiLoRA baselines to Table 3 (CIFAR100 experiments) — this is the single highest-leverage improvement.
- Either derive a function-level bound connecting parameter-space orthogonality to output stability under Lipschitz assumptions, or retitle Section 4 to match what the math delivers.
- Add one ViT-L/14 experiment to validate scaling claims.
- Report error bars on at least the main results (Tables 1 and 3).
- Explicitly state ρ = 0.95 in Section 3 or Section 5.1.

## Calibration Report

**Round 1 anchors** (all queries: "continual learning vision-language model CLIP PEFT parameter-efficient"):

| Path | Avg Human Score | Band | Comparison |
|------|----------------|------|------------|
| 5lUdTogEL3.md | 1.00 | Strong reject | Lifelong Re-ID, completely different domain |
| JIlIYIHMuv.md | 2.50 | Reject | LVLM-CL, weaker contribution, less comprehensive evaluation |
| WM5G2NWSYC.md | 2.00 | Reject | Projected Subnetworks, weaker experiments |
| G9Ea7mlqGO.md | 3.80 | Reject | CLIP Online CL, rejected, weaker method |
| 9aZ2ixiYGd.md | 5.00 | Weak accept | V&L Synergy, polarized reviews (8,6,3,3), prompt-based CL |
| NmiFwEP8K5.md | 4.50 | Reject | GE-PEFT, rejected for insufficient baselines and evaluation |
| sb7qHFYwBc.md | 6.50 | Accept | **C-CLIP**, most comparable — CL for CLIP, NuSA-CL is stronger |
| TLADT8Wrhn.md | 6.25 | Accept | TiC-CLIP, different scale (web-scale benchmarks) |
| Hcb2cgPbMg.md | 6.25 | Accept | Spectral Regularization, also spectral but different approach |
| mz8owj4DXu.md | 6.50 | Accept | SLM/JARe, language model continual learning |
| 3i13Gev2hV.md | 8.00 | Accept | Hyperbolic VLMs, different topic entirely |

**Round 2 anchors** (queries: "continual learning low-rank null space SVD forgetting", "catastrophic forgetting PEFT adapter continual learning"):

| Path | Avg Human Score | Band | Comparison |
|------|----------------|------|------------|
| u3dHl287oB.md | 5.67 | Borderline | Analytical CL model, theoretical focus |
| Ll8PmgD0IB.md | 6.00 | Accept | LMSP, local model space projection for CL |
| ScI7IlKGdI.md | 6.33 | Accept | Spurious Forgetting, different focus |
| MB53uAZKSc.md | 6.25 | Reject | TiC-LM, benchmark paper |

**Bracket: 6.5–7.5.** NuSA-CL is clearly above the reject zone and comparable to or stronger than the accepted C-CLIP (6.5), with more novel methodological contribution (persistent null-space constraint vs. standard LoRA + contrastive loss), stronger ablations, better efficiency, and insightful spectral analysis. Not quite 7.5+ due to missing CIFAR100 PEFT baselines and single-backbone limitation.

**Final score: 7.0.** Solid accept with addressable weaknesses.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>
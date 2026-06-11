## Summary

This paper introduces ConCuR, a curated dataset of 4,892 CUDA kernels paired with reasoning traces, and KernelCoder, a 32B model fine-tuned on this dataset. The core idea is that concise reasoning traces are more strongly associated with correct, high-performance kernels than long reasoning traces. The paper validates this through aggregate analysis (Figure 3) and an ablation study showing that the multi-criterion curation pipeline substantially outperforms single-criterion baselines. KernelCoder achieves strong results on KernelBench Level 1/2, particularly on correctness (Exec), using only 64 A100 GPU hours of training.

---

## Strengths

1. **Empirical finding that shorter reasoning is associated with correctness (Figure 3)**: The paper quantitatively shows that accuracy drops from ~0.65 for the shortest reasoning bins to ~0.04 for the longest, and that correct kernels have a median reasoning length ~2,000 tokens shorter than incorrect ones. This is a non-obvious finding that contradicts the common "longer reasoning = better" assumption in the reasoning model literature, and it directly motivates the paper's design choices.

2. **Ablation study cleanly demonstrates that the multi-criterion curation matters (Table 4)**: KernelCoder's combined criterion outperforms all single-criterion baselines (random, max-length, min-length, speedup-only) by large margins — e.g., Pass@1 Exec Level 1: 58% vs. 42% (next best), and Pass@1 fast₁ Level 2: 39% vs. 27% (next best). This provides direct causal evidence that the specific curation method, not just data quantity or any single factor, drives the gains.

3. **Dramatic training efficiency (Table 3)**: KernelCoder achieves 91/95 Pass@10 on Level 1/2 using only 4,892 samples and 64 A100 GPU hours, compared to Kevin's >600 H200 GPU hours and AutoTriton's 640 total GPU hours. This is a concrete, well-documented advantage that makes the practical contribution clear.

4. **Generalizability across base models (Table 5)**: Fine-tuning three different base models (Qwen3-8B, Qwen3-32B, QwQ-32B) on ConCuR improves all three substantially — e.g., Qwen3-8B Level 2 Exec rises from 53% to 89% at Pass@10. This shows the dataset's value is not tied to a specific architecture or training recipe.

5. **Novel use of ARL as a task difficulty metric (Tables 6–7)**: The paper proposes and validates average reasoning length as a difficulty indicator for kernel generation tasks. Performance consistently decreases from Easy to Hard subsets across five different models (e.g., DeepSeek-R1-0528: 94.6→87.8 Exec, Kevin-32B: 100→67.3 Exec), supporting the metric's validity.

---

## Weaknesses

### Major

1. **Headline performance claims are overstated relative to the evidence.** The paper states that KernelCoder "surpasses all frontier models, including DeepSeek-R1-0528" (line 177). However, the paper's own tables show that DeepSeek-R1-0528 beats KernelCoder on fast₁ Level 1 at Pass@1 (18% vs 17%, Table 1), and on Exec Level 2 (97% vs 95%) and fast₁ Level 2 (82% vs 68%) at Pass@10 (Table 2). Qwen3-Coder-Plus also beats KernelCoder on fast₁ Level 1 at Pass@10 (35% vs 32%). KernelCoder's strongest advantage is on correctness (Exec), where it leads consistently, but it does *not* dominate across all metrics as claimed. This misrepresentation is verifiable from Tables 1 and 2 and needs to be corrected. The results are still interesting — achieving comparable fast₁ at 32B vs 685B parameters with dramatically lower training cost — but the paper should say that, not claim unconditional dominance.

2. **Potential data contamination between training and evaluation is not addressed.** Kevin-32B (the model used to generate the ConCuR data) was trained on "180 problems of KernelBench" (Table 3, footnote). The resulting KernelCoder is then evaluated on KernelBench. The paper does not discuss whether these 180 problems overlap with the evaluation set (Level 1 and Level 2), how they were selected, or whether any tasks were excluded from evaluation due to this overlap. This is a standard methodological concern in this line of work. While KernelCoder's advantages over non-Kevin models (DeepSeek-R1-0528, Claude-4-sonnet) mitigate the concern somewhat — those models were never trained on KernelBench — the comparison against Kevin specifically could be affected, and the paper should address this directly.

### Minor

3. **Intra-task evidence for the conciseness claim is deferred to the appendix.** The paper claims "for the same task, CUDA kernels generated after shorter reasoning traces tend to be correct more frequently" (line 82) — a specific within-task claim. However, the main text evidence (Figure 3) is entirely aggregate across all tasks, which could be confounded by easy tasks requiring few tokens and having high accuracy while hard tasks require many tokens and have low accuracy. The paper acknowledges this confound (line 82–83) and references "detailed analyses (see Appendix B)" (line 84), but the appendix is not available in the submission. The aggregate evidence is suggestive but does not directly support the intra-task claim. (The ablation results in Table 4 provide downstream validation that the curation method works, which partially mitigates this concern, but the theoretical framing remains under-evidenced in the main text.)

4. **Anomalies in the difficulty division results are not discussed.** In Table 7, DeepSeek-R1-0528 achieves *higher* G_speedup on Medium (2.515) than Easy (1.869), and Qwen3-8B achieves *higher* G_speedup on Hard (0.675) than Medium (0.428). These inversions suggest the ARL-based difficulty ranking is not perfectly consistent across models, which limits the generality of the proposed metric. The paper should address these anomalies.

5. **Number of evaluation tasks per KernelBench level is not stated.** The paper reports percentages on KernelBench Level 1 and Level 2 but never states how many tasks are in each level. The difficulty division (Table 6) shows 37+114+49=200 tasks total across both levels combined, but the per-level breakdown is missing. Without this, the reader cannot assess the precision of the reported percentages.

6. **Overlap between the three parts of ConCuR is not clarified.** The curation has three parts (a: 3,934 samples, b: 414 samples, c: 544 samples = 4,892 total). The paper does not state whether these parts are disjoint or whether some samples satisfy multiple criteria. If there is overlap, the effective dataset size would be smaller than 4,892.

### Trivial

None.

---

## Nice-to-Haves

- A per-component ablation (removing each of parts a, b, c individually while keeping the other two fixed) would more directly validate the contribution of each curation component, complementing the existing comparison against alternative selection strategies.
- Reporting the within-task variance of speedup among the 5 generated samples per task would help interpret the 40.2% rate at which the shortest-reasoning kernel is also the fastest.

---

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **Criticism about Criterion (a) joint frequency not discussed** (Harsh Critic Issue 4): The critic questioned why 40.2% of tasks have the shortest-reasoning kernel also being the fastest, when r=-0.047 suggests independence. This is an interesting observation but does not constitute a flaw; if anything it supports that the paper's criterion has more signal than expected by chance. **Removed.**

2. **"Apples-to-oranges" comparison between SFT and GRPO**: The efficiency comparison in Table 3 is about resource cost across different training paradigms, which is a valid and informative comparison. **Removed.**

3. **No confidence intervals / statistical tests**: Single-run evaluation without error bars is the standard practice for this type of benchmark evaluation in the code generation literature (KernelBench, HumanEval, etc.). **Removed.**

4. **All evaluations on the same GPU setup (8 RTX 5090s)**: Internal consistency is expected and appropriate for a benchmark comparison. **Removed.**

5. **Missing dataset release info**: Conference submissions do not typically include release URLs. **Removed.**

6. **Missing related works**: Cannot verify from external sources. **Removed per instructions.**

7. **Formatting/presentation nitpicks**: Removed per instructions.

8. **Strength Finder generic strengths**: Strengths like "addressed an important problem" or "this paper targeted an interesting question" were removed as generic. Only concrete, evidence-anchored strengths were kept.

9. **Criticism about missing appendix content**: The appendix is stripped by the parser; it exists in the original submission. **Removed.**

---

## Novel Insights

None beyond the paper's own contributions.

---

## Suggestions

1. **Tone down the performance claims** to accurately reflect where KernelCoder leads (primarily on correctness/Exec) versus where it is competitive but not dominant (fast₁). Emphasize the efficiency advantage (32B, 64 A100 hours) over frontier models, which is the paper's strongest comparative claim.

2. **Address the data contamination question directly**: State whether Kevin's 180 KernelBench training problems overlap with the evaluation set, and if there is any overlap, report results with contaminated tasks excluded.

3. **Add intra-task evidence to the main text**: Show, for a few representative tasks, the distribution of reasoning lengths for correct vs. incorrect generations within the same task. A small multi-panel figure would be far more convincing than the aggregate plots alone.

4. **Report the number of tasks in each KernelBench level used for evaluation.**

5. **Clarify whether the three parts of ConCuR are disjoint or have overlapping samples.**

6. **Discuss the anomalies in Table 7** (DeepSeek-R1-0528 and Qwen3-8B G_speedup inversions) and explain what they imply about the generality of the ARL-based difficulty metric.

---

## Calibration Report

**Round 1 — Bracketing:**
| Path | Score | Round | Comparison |
|------|-------|-------|------------|
| 2HN97iDvHz (Data Center Scheduling) | 3.00 | R1 weak | Much weaker; unrelated topic |
| N18Z2MkMEa (FALCON) | 3.00 | R1 weak | Much weaker; lacks rigorous evaluation |
| mS7xin7BPK (LEGO-Compiler) | 3.40 | R1 weak | Much weaker; limited evaluation |
| m2kJuN1bKt (Reformer - GPU kernel selection) | 4.60 | R1 mid | Similar GPU kernel domain but weaker experimental validation |
| iM7MfzbF1B (MAGE - mapper generation) | 5.00 | R1 mid | Similar parallel programming domain; current paper is stronger |
| t8KLjiFNwn (Sparse Learning for SSMs) | 7.00 | R1 mid | Different topic; similar quality level |
| m2nmp8P5in (LLM-SR) | 8.00 | R1 strong | Stronger execution and cleaner evaluation |
| OI3RoHoWAN (GenSim) | 8.00 | R1 strong | Stronger; broader scope and thorough evaluation |

**Round 1 bracket: 4.5 – 7.5** (paper is clearly above Reformer/MAGE, clearly below GenSim/LLM-SR)

**Round 2 — Narrowing:**
| Path | Score | Round | Comparison |
|------|-------|-------|------------|
| maRYffiUpI (LLM-Assisted Code Cleaning) | 7.00 | R2 | Very similar (data curation for code gen); slightly cleaner claims, accepted |
| AqfUa08PCH (Training LMs on Synthetic Edit Sequences) | 6.50 | R2 | Similar contribution (synthetic data for code); accepted |
| ynguffsGfa (Curated LLM) | 6.33 | R2 | Similar (data curation); rejected; less direct domain relevance |
| 8KQzoD5XAr (CraftRTL) | 7.00 | R2 | Very similar (HDL code generation + synthetic data curation); accepted |
| ix7rLVHXyY (Learning Performance-Improving Code Edits) | 7.25 | R2 | Very similar (code performance dataset); more comprehensive evaluation |
| Fq8tKtjACC (Textbooks Are All You Need) | 6.00 | R2 | Similar emphasis on data quality; influential but rejected |

**Final score determination**: The paper is comparable to the accepted papers at 6.50–7.00 in terms of contribution size, but is held back by two significant unresolved issues: the overstated claims (verifiably contradicted by the paper's own tables) and the unaddressed data contamination concern. These issues are fixable but reduce confidence in the paper's current form. Hence the score of 6.0 — below the clean accepts (6.50–7.25) but above clearly weaker papers (4.60–5.00).

---

**MY FINAL SCORE: <score>6.0</score>**
**MY FINAL DECISION: <decision>Reject</decision>**
## Final Review

## Summary
This paper proposes ASPD, an adaptive serial-parallel decoding framework that accelerates LLM inference by identifying and concurrently executing parallelizable segments within responses. The method has two components: (1) a non-invasive data pipeline that automatically extracts parallel structures from autoregressive model outputs through rewriting, independence verification, integrity verification, and preference-based selection; and (2) an internal parallelization architecture using branch-invisible attention masks and shared position encodings to enable seamless serial-parallel transitions without KV-cache recomputation. Evaluations across general tasks, RAG, and mathematical reasoning demonstrate speedups while maintaining response quality.

## Strengths
- **Clean architectural mechanism for lossless serial-parallel transitions**: The attention mask design (Eqs. 1–3) enforces branch isolation during parallel decoding while allowing the main branch to see all branches, and the shared position encoding (Eq. 4) synchronizes position IDs across parallel branches. This ensures each branch experiences native autoregressive generation and merging requires no KV-cache recomputation. The ablation in §4.4.2–4.4.3 (Table 4) systematically validates design choices: Indep masks + Same-Seq positions yield the best score (7.64) at 104.21 TPS, substantially outperforming Shared masks (scores of 4.64 and 3.70) and Predict-based positions (score 6.75).

- **Principled multi-stage data pipeline**: The Non-Invasive Parallel Data Transformation Pipeline (§3.1) converts serial responses into parallel-formatted data through parallel rewriting (N=3 passes), independence verification, integrity/answer verification, and preference-based selection (DP and ABN metrics). Table 4 shows ASPD's pipeline achieves a score of 7.64 at 104.21 TPS, substantially better than APAR's rule-based approach (5.81 at 59.25 TPS) and PASTA's pipeline lacking independence verification (4.98 at 106.83 TPS).

- **Broad empirical validation across domains, models, and benchmarks**: On Vicuna Bench (§4.2, Table 1), V-ASPD scores 7.74 vs. V-Seq's 7.70. On RAG Bench (Figure 4c), ASPD maintains 1.46x speedup where SoT drops to 1.06x. On mathematical reasoning (§4.3, Table 2) with Qwen2.5-32B, ASPD matches or exceeds the Seq baseline on GPQA (65.66 vs 61.11) and AIME2024 (62.08 vs 58.75) while providing 1.04–1.17x TPS speedup versus Seq (Table 3). Cross-model generalization is demonstrated with both Vicuna-7B and Qwen2.5-7B (Table 1).

- **Iterative adaptive decoding**: The hybrid decoding engine (§3.3) uses six special tokens that the model learns during fine-tuning to autonomously decide when to enter/exit parallel mode, enabling multiple serial-parallel cycles within a single response — a capability absent in SoT's fixed two-phase approach or APAR's single fork-join.

## Weaknesses

### Fatal
None.

### Major
- **Headline speedup measured against the wrong baseline for general tasks**: The abstract and Section 4.2 report speedup ratios (1.30x–1.82x, up to 3.10x) relative to V-Ori (the untrained original Vicuna). However, V-Seq — trained on the same data but with parallel tokens removed — is also faster than V-Ori (visible in Figure 4). The speedup attributable specifically to the parallel decoding mechanism should be ASPD TPS / V-Seq TPS, but V-Seq's TPS is never tabulated numerically in the main text. The authors cannot decompose how much speedup comes from fine-tuning on curated data versus the parallel mechanism itself. Notably, Section 4.3 does this correctly for math benchmarks (Table 3 reports TPS relative to Seq), creating an inconsistency in reporting standards across sections. This is a significant framing issue because the abstract's headline claim ("1.82x on average") overstates the contribution of the parallel mechanism.

- **Self-contradictory ablation analysis in §4.4.2**: The text states "Our empirical evaluation shows that *Shared* masks consistently outperform *Indep* masks across both *Seq* and *Max* position id configurations" (line 239). However, Table 4 shows the opposite for quality: Seq+Indep scores 7.64 vs. Seq+Shared at 4.64, and Max+Indep scores 6.78 vs. Max+Shared at 3.70. On TPS, Shared wins for Seq (110.30 vs 104.21) but loses for Max (86.96 vs 89.45), so even the efficiency claim of "consistently outperform" is incorrect. The next sentence then concludes these findings "strongly validate our design decision to maintain strict branch isolation" — which is the Indep strategy. The paragraph is internally incoherent and undermines confidence in the ablation analysis. The data appear to support the correct conclusion (Indep is better), suggesting a drafting error where "Shared" and "Indep" were swapped, but as written the analysis is directly contradictory.

### Minor
- **PDOS is discussed as a close competitor in Related Work but absent from experiments**: PDOS (Yu, 2025, discussed in §2) is the prior work most architecturally similar to ASPD, also using internal masks and logits processors for parallel decoding. The related work frames PDOS's limitations, but PDOS never appears in experimental comparisons. Either a comparison should be included, or the paper should explain why direct comparison is infeasible.

- **Suspiciously uniform PPD across diverse datasets**: The data parallelism table in the introduction (lines 26-31) shows exactly 44% Proportion of Parallel Data for all four datasets (ShareGPT Vicuna, MRC, RAG, Math-220K), despite these covering entirely different domains. This uniformity across diverse data sources warrants either an explanation or a correction.

- **No discussion of worst-case behavior when parallelism fails to trigger**: The model autonomously decides when to enter parallel mode via learned special tokens. The paper does not report what fraction of test-time responses actually engage parallel decoding, nor the TPS in pure serial mode when parallelism does not trigger. For a method whose value proposition is speed, understanding the failure mode is important.

- **Internal MRC dataset used for generalization claims**: The paper cites results from an internal MRC dataset deferred to Appendix A.5 for cross-domain generalization claims. While the main results do not depend solely on this, the use of a non-public dataset weakens the generalization argument.

### Trivial
- **Percentage improvements framed against weak baselines**: Section 4.2 reports "14.55% and 24.78% improvement on MT Bench" against V-APAR and SoT respectively. These baselines have notably poor quality scores (4.88 and 4.48), inflating the apparent magnitude of improvement. The comparison against V-Seq and V-Ori is more informative and should be foregrounded.

## Nice-to-Haves
- The computational cost of the data pipeline (invoking Qwen3-235B-A22B multiple times per sample for a 220K-sample dataset) could be discussed as a one-time training cost, though it does not affect inference efficiency.
- Confidence intervals or multiple evaluation runs for LLM-as-judge scores would strengthen the reliability of quality comparisons, particularly for small score differences.

## Removed Points
These points are flagged to be removed, treat them with caution:
- **Harsh Critic claimed the position encoding equation has a problem with teacher-forcing during training** — REMOVED. During training with teacher forcing, the training data is pre-formatted with parallel structure, so P_t (tokens per step) is known a priori from the data. No actual problem exists.
- **Harsh Critic claimed the "Predict" scheme's dismissal was unjustified** — REMOVED. The data shows Predict at score 6.75, which is indeed the lowest among all position encoding approaches (Same-Seq 7.64, Same-Re 7.29, Same-Max 6.78). The paper's claim is factually correct.
- **Strength Finder claimed the method achieves "1.30–1.82x average speedup" as a core strength** — This is partially misleading (see Major Weakness #1 about the baseline) and has been downgraded.

## Novel Insights
None beyond the paper's own contributions. The paper's core insight — that attention masks and shared position encodings can enable seamless serial-parallel transitions without KV-cache recomputation in a single sequence — is genuinely novel, and the reviews do not surface additional insights beyond what the paper already articulates.

## Suggestions
- Re-center the general-task speedup analysis around V-Seq/Q-Seq as the baseline. Report V-Seq TPS numerically in the main text and compute speedup ratios as ASPD TPS / V-Seq TPS. This would give an honest decomposition of how much gain comes from the parallel mechanism vs. fine-tuning effects.
- Fix the contradictory paragraph in §4.4.2. Based on Table 4, the sentence should read that *Indep* masks outperform *Shared* masks on quality (with a speed-quality tradeoff to discuss), and the conclusion about strict branch isolation being optimal should follow directly from this.
- Either add a PDOS comparison or include a sentence explaining why direct comparison is not feasible (e.g., code unavailability, incompatible setup).
- Explain or correct the uniform 44% PPD across all four datasets.

## Score and Decision

### Calibration

**Round 1 (Bracketing):** Initial bracket formed at **5.0–6.5** based on comparison against:

| Anchor | Score | Round | Comparison |
|--------|-------|-------|------------|
| cf7NTWv1iW (Parallel Prompt Decoding) | 4.25 | R1 | ASPD clearly stronger — more novel architecture, broader evaluation |
| DSI/cJd1BgZ9CS | 5.00 | R1 | ASPD has broader empirical validation across more domains |
| PEARL/QOXrVMiHGK | 5.75 | R1 | ASPD more architecturally novel, more comprehensive ablation |
| ParallelSpec/SXvb8PS4Ud | 5.80 | R1 | Comparable novelty; ASPD better evaluated but has more presentation issues |
| SWIFT/EKJhH5D5wA | 6.25 | R1 | ASPD more novel, broader eval, but worse framing/analysis issues |
| HASS/T9u56s7mbk | 7.00 | R1 | ASPD doesn't reach this level of polish; HASS has cleaner evaluation and presentation |

**Round 2 (Narrowing):** Further comparison within the bracket:

| Anchor | Score | Round | Comparison |
|--------|-------|-------|------------|
| ParallelSpec/SXvb8PS4Ud | 5.80 | R2 | ASPD stronger due to more principled data pipeline and cross-domain evaluation |
| APE/yUC8pU508S | 6.20 | R2 | Comparable; ASPD has richer ablation, APE has cleaner presentation |
| FlashMask/wUtXB43Chi | 7.00 | R2 | Different area; ASPD doesn't reach this tier of execution quality |

ASPD is closest to SWIFT (6.25) and APE (6.20) in overall contribution quality — all feature novel architectural ideas with solid empirical validation but some presentation gaps. ASPD's framing issues (speedup baseline, contradictory ablation paragraph) are somewhat more significant than the weaknesses in those accepted papers, placing it slightly below them at **6.0**.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>
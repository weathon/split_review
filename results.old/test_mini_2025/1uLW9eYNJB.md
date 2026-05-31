Now I have all the information needed to produce the final consolidated review.

## Summary

The paper proposes Mixture of Shards (MoS), a parameter-efficient fine-tuning method for LoRA that combines inter-layer and intra-layer parameter sharing with four cheap differentiation strategies (subset selection, pair dissociation, vector sharding, shard privatization). The key insight — that pure sharing harms performance but cheap differentiation reverses the damage — is empirically validated and guides the design. MoS achieves approximately 8× parameter savings versus standard LoRA (19.99M parameters matching LoRA rank-64 at 159.91M) and outperforms baselines (LoRA, VeRA, Tied LoRA, ProLoRA) at fixed low parameter budgets across LLaMA2-7B, LLaMA2-13B, and LLaMA3.2-3B.

## Strengths

1. **Empirical demonstration of ~8× parameter savings.** Table 2 shows MoS (19.99M params, rank 16/32) achieving avg 37.63, closely matching LoRA rank-64 (159.91M, avg 37.53). This is a directly measured 8× reduction on the parameter-to-performance Pareto front.

2. **Identification and validation of the sharing–differentiation trade-off.** Section 2 (Table 1) cleanly shows: pure sharing underperforms LoRA on average (34.33 vs 34.98), while adding subset selection reverses the degradation and surpasses LoRA (36.12). This finding is not just stated as intuition but empirically demonstrated on six benchmarks, providing a principled motivation for MoS design.

3. **Outperforms all baselines under fixed low parameter budget.** At 5.00M params (Table 2), MoS (36.39 avg) outperforms LoRA (34.98), VeRA (34.00), Tied LoRA (35.26), and ProLoRA (36.03), with underlines showing best performance on 5/6 individual tasks.

4. **Scalability to larger models.** Table 3 shows MoS on LLaMA2-13B (avg 45.98) outperforms ProLoRA (45.04) and LoRA (43.92) on every evaluated task. Appendix B.3 (stripped from this version but referenced) extends to LLaMA3.2-3B with multiple seeds.

5. **Ablation quantifies each component's contribution.** The ablation (Table 2) reports performance drops from removing pair dissociation (–1.09), shard privatization (–1.09), and vector sharding (–0.41), providing direct evidence for the necessity of each strategy. This goes beyond typical ablation by ranking the relative importance of components.

## Weaknesses

### Fatal
None.

### Major

1. **Lack of variance reporting in main results.** The core comparisons in Tables 2 and 3 report single-point estimates with no standard deviations or confidence intervals. The key claims — e.g., MoS (5.00M) avg 36.39 vs ProLoRA 36.03; MoS (19.99M) avg 37.63 vs LoRA rank-64 (159.91M) 37.53 — involve differences of 0.3–0.7 points on tasks where per-sample variance is known to be substantial (especially on MMLU, BBH, and HumanEval). The paper mentions multiple-seed experiments in Appendix B.3 (LLaMA3.2-3B only), but the central 7B results lack any uncertainty quantification. This weakens the evidential support for the claimed superiority; readers cannot distinguish systematic advantage from noise.

### Minor

2. **Overclaimed "MoE-like routing" framing.** The paper repeatedly calls its index-based shard selection a "Mixture-of-Experts (MoE)-like routing mechanism" (abstract, §3, §5) and claims to be "the first to apply MoE-like mechanism for parameter savings in a single-task LoRA" (§1, §5). However, the index matrices are randomly initialized and **frozen** during training (§3.2: "randomly sampled during initialization, remains fixed during the finetuning process"). There is no learned gating, no dynamic selection, and no expert capacity allocation. This is a fixed random index-assignment scheme, conceptually closer to random feature selection than to MoE routing. This is a framing problem, not a technical flaw — the method's contribution does not depend on the MoE analogy — but it misrepresents the nature of the mechanism and invites unnecessary confusion with the large body of learned-routing MoE-LoRA literature. The authors should either remove the MoE language or qualify it precisely (e.g., "stochastic fixed-index shard selection").

3. **Exclusion of TyDi QA and HumanEval for LLaMA2-13B.** Table 3 evaluates only 3 tasks for the 13B model. The paper justifies this by stating "vanilla LoRA does not yield consistent improvements on the TyDi QA and Code benchmarks" (end of §4.3). This is a reasonable explanation, but it means 2/5 task categories are dropped on the larger model, making the 13B comparison less comprehensive than the 7B one. Reporting the results regardless (even if weak) would have been more informative.

4. **Ablation conducted at only one parameter budget.** The ablation of pair dissociation, vector sharding, and shard privatization is performed only at the 19.99M parameter budget (Table 2). It would be informative to also ablate at the 5.00M budget, where parameters are more constrained and relative component importance might differ.

### Trivial
None.

## Nice-to-Haves
- A brief measurement of training/inference overhead (wall-clock time per step or GPU memory) for the "nearly cost-free" routing operations would strengthen the efficiency claims.
- The principle validation in §2 (sharing vs differentiation) is shown on LLaMA2-7B only. Reporting the same comparison on a second architecture in the main paper (not just the appendix) would strengthen the generality claim.
- A comparison with a method that learns rank allocation (e.g., AdaLoRA) would broaden the baseline set, though the paper's focus on sharing methods makes this omission defensible.

## Removed Points

- **"High rank" claim misleading (§3.1): REMOVED.** The critic asserts that MoS's effective rank per layer is *r*, not the pool size, and that the "high rank" phrasing is misleading. However, §3.1 is explicitly describing **pure sharing** — the baseline from §2 — and the text says "pure sharing can raise the rank from 2 to 64." The paper never claims that MoS itself has rank 64. The context makes this perfectly clear. This is a misreading by the reviewer.

- **MoE claim is "fatal": DEMOTED to Minor (see above).** The critic labels this a critical/structural issue. The term "MoE-like" does qualify the claim, and the contribution does not depend on the MoE analogy being accurate. This is a framing improvement, not a fatal flaw.

- **Speculative criticism about missing appendix/proof content: REMOVED per instructions.** The parser strips appendix sections; criticisms of absent appendix content are invalid.

- **"Strawman weakness" about pure sharing test coverage: REMOVED.** The paper states Appendix B.2 covers LLaMA3.2-3B for the principle validation. The parser stripped this content.

## Novel Insights

The most interesting observation emerging from cross-referencing the reviews is that the strength of MoS lies in its *principled* design (derived from the sharing–differentiation trade-off experiment) rather than ad-hoc heuristics — this contrasts with many sharing methods that are motivated purely by empirical gains. The weakness profile suggests that the paper's main gap is in the *strength of evidence* (no variance), not in the correctness or novelty of the method itself.

## Suggestions

1. **Add variance reporting.** Run at least 3 random seeds for the main comparisons (5.00M and 19.99M budgets on LLaMA2-7B) and report mean ± std in Tables 2 and 3. This is the single most impactful improvement.

2. **Rebrand the "routing."** Replace "MoE-like routing" with "fixed random index assignment" or "static shard selection" throughout. Remove the claim of being "first to apply MoE-like mechanism for parameter savings" — the contribution stands on its own without this framing.

3. **Include the 13B results on TyDi QA and HumanEval** even if the LoRA baseline is weak, with a caveat. This would make the scalability analysis more complete.

4. **Extend the ablation to the 5.00M budget** to verify that the component-level findings generalize to more constrained settings.

---

### Calibration Anchors

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| `GdXI5zCoAt.md` (RaSA) | 7.00 | R1 | Rank-sharing LoRA extension, accepted poster. RaSA is cleaner with almost no reviewer weaknesses. MoS has broader evaluation but weaker evidence (no variance). MoS is slightly weaker. |
| `O6QZ4W6GXt.md` (ShareLoRA) | 4.20 | R1 | Simple similarity-based sharing, withdrawn/reject. MoS is clearly stronger in all dimensions. |
| `l0gZS0sAlf.md` (ELREA) | 5.80 | R2 | Ensemble of LoRA experts, accepted poster. Weaker evaluation than MoS; significant inference cost concerns. MoS is stronger. |
| `yOOJwR15xg.md` (MeteoRA) | 6.20 | R2 | Multi-task LoRA via MoE, accepted poster. Similar quality; MoS has stronger empirical results and broader individual-task evaluation. |
| `jFcNXJGPGh.md` (ComLoRA) | 6.00 | R2 | Competitive LoRA training, accepted poster. MoS has better baselines, more thorough ablation, and fewer substantive weaknesses. |
| `OALIb8oNfl.md` (Structural Integrity) | 5.75 | R2 | Different PEFT approach for 4D params, accepted poster. Less directly comparable. MoS has more focused evaluation. |

**Round 1 Bracket:** [5.5, 7.0] — clearly above rejection-range papers (3.0–4.2) and below oral-level papers (8.0+).

**Round 2 Narrowing:** Closer to MeteoRA (6.2) and ComLoRA (6.0) than to RaSA (7.0). MoS has broader evaluation than MeteoRA and fewer theory gaps than ComLoRA, but the variance gap prevents it from reaching RaSA's cleanliness. Final score calibrated at **6.5**.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>
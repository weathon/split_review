Now let me verify the Figure 3 data issue and read more context, then run calibration search.Now I have enough to write the final review. Let me compile everything.

---

## Summary

CANON (Conditional Advantage estimatiON) proposes decomposing the group-relative advantage in RLVR training for LLMs into two components: inter-group advantage (comparing responses against the mean of the opposite group, sorted by a training metric) and intra-group advantage (comparing within the same group). The key insight is that DR.GRPO is exactly a 0.5/0.5 blend of these two (Eq. 7), while controlling the mixture weight μ allows amplifying the metric's effect without presupposing a directional preference. Empirically, entropy-grouped CANON-Inter improves math reasoning by ~1.9 points, entropy-grouped CANON-Intra improves complex logic reasoning by up to 5.2 points, and length-grouped CANON-Eff establishes a new Pareto frontier in performance-vs-token-cost.

---

## Strengths

- **Clean algebraic decomposition.** Eq. 7 proves that DR.GRPO = 0.5 × CANON-Inter + 0.5 × CANON-Intra when groups are equally sized — a non-trivial identity that both explains and subsumes the prior method. This gives the μ parameter a principled interpretation and makes CANON a genuine generalization rather than a heuristic add-on.

- **CANON-Eff Pareto frontier.** Section 5.3 and Figure 4c are the paper's strongest results: sweeping α over {0.5, 0.7, 0.8, 0.88, 0.96} produces a Pareto frontier that strictly dominates all baselines (Clip Length, Length Reward +, Length Reward \*). The instability of Length Reward (+) (accuracy drops from 54.8 to 22.5 when its coefficient moves from 0.004 to 0.005) is a genuine and noteworthy finding, and CANON-Eff navigates this space stably. The 26.3% token reduction at 0.4-point accuracy drop (α=0.96) and 2.63× efficiency gain at low-budget (α=0.88) are specific and compelling.

- **Selective amplification validated empirically.** Table 4 directly tests whether CANON's gains come from merely amplifying the advantage signal (Numerical Scaling, Entropy Adv) or from the regrouping operation. Direct scaling fails to replicate CANON-Intra's logic performance (25.1/18.5 vs. 29.1), lending credibility to Theorem 2's selective-amplification claim even if the formal independence assumption is idealized.

- **Training dynamics reveal mechanistic differentiation.** Figure 2 shows measurable divergence between CANON-Inter (rapid reward increase, entropy decrease) and CANON-Intra (sustained entropy, later-stage reflection gains). Figure 2f showing reflection gain crossing zero for CANON-Intra at ~90 steps, coinciding with logic performance acceleration, provides a coherent mechanistic story.

- **Breadth of evaluation.** Three model families (Qwen-7B, Qwen-1.5B, Llama-8B), six math benchmarks, three ZebraLogic complexity tiers, and eight baselines under a unified protocol. Table 2's results across all three models are internally consistent.

---

## Weaknesses

### Fatal
None.

### Major

- **Figure 3's data table contains numbers inconsistent with Tables 1 and 2.** For Qwen-7B, the table labels DR.GRPO at Math=57.6 and Logic=39.2; Table 1 shows DR.GRPO at Math Acc=55.7 and Logic Acc=26.2 — the 57.6 is actually CANON-Inter's Math Acc, and 39.2 is the Mid-tier logic result, not the overall Logic Acc. For Llama-8B, the table labels DR.GRPO at 22.6 and 18.9; Table 2 shows DR.GRPO at 22.0 and 14.9 — the 22.6/18.9 values belong to the Cosin-First-Inter-Later-Intra (CANON-Dynamic) row. The round numbers for several entries (35.0, 45.0, 30.0) do not appear in any other table. The Figure 3 data table appears to use scaled radar-chart axis coordinates rather than actual performance percentages, but is formatted identically to real result tables without any such labeling. As written, readers will interpret these numbers as experimental outcomes, which they are not. The paper must either correct these numbers to match Tables 1/2 or explicitly label Figure 3's accompanying table as "illustrative axis coordinates, not absolute accuracy."

- **CANON-Dynamic results in Figure 3 mix per-model strategy selection with claims of uniform superiority.** Section 5.2 explicitly states: "we select strategy *Cosin-First-Inter-Later-Intra* for Qwen2.5-Math-7B and Llama3.1-8B, and strategy *First-Inter-Later-Intra* for Qwen2.5-Math-1.5B to draw Figure 3." This means the CANON-Dynamic point in Figure 3 is drawn from the best-performing strategy per model. While the paper does show Table 2 with both strategies, the fact that CANON-Dynamic's "outperforms DR.GRPO across all models and tasks" claim (Section 5.2 text) is based on this post-hoc selection is not stated prominently. Importantly, the concern is partially self-mitigated: Table 2 shows that the single *First-Inter-Later-Intra* strategy consistently beats DR.GRPO across all three models on both tasks without per-model selection (57.0/28.3 vs. 55.7/26.2 for Qwen-7B; 46.8/17.0 vs. 46.4/12.8 for Qwen-1.5B; 22.1/17.7 vs. 22.0/14.9 for Llama-8B). The authors should lead with this finding and de-emphasize the per-model selection version.

### Minor

- **Theorem 2's independence assumption is idealized.** The selective-amplification theorem requires P(o ∈ C₁ ∩ C₂ | q, θ) = P(o ∈ C₁ | q, θ) · P(o ∈ C₂ | q, θ). In practice, entropy and correctness (or length and correctness) are correlated during training, not independent. This weakens the formal guarantee. The paper should acknowledge this limitation explicitly; Table 4 provides reasonable empirical support in lieu of the theoretical ideal, but that should be stated as substituting for, not confirming, the theorem's assumptions.

- **AIME results reported without confidence intervals.** AIME 2024/25 each contain 30 problems; Avg@10 means 300 total examples. The reported swings are large relative to test-set size: CANON-Inter is 5 points above DR.GRPO on AIME24 (32.7 vs. 27.7) but 1.6 points *below* on AIME25 (18.7 vs. 20.3). These contradictions within a single method's AIME results suggest variance that a ±1σ band would clarify. The overall Acc column (averaging 6 benchmarks) is more reliable and should carry more emphasis.

- **CANON-Intra's math accuracy trade-off is understated.** Table 1 shows CANON-Intra (Entropy) at Math Acc=54.7, which is *below* DR.GRPO's 55.7. The paper's framing "both inter and intra improvements are desirable" glosses over this trade-off. The scheduling motivation in Section 5.2 implicitly acknowledges it, but the main results section should state it clearly.

### Trivial

None.

---

## Nice-to-Haves

- A null-metric control in the Table 4 ablation (e.g., random grouping or grouping by an irrelevant syntactic feature) would strongly validate that the gain requires a *meaningful* metric correlation, not just smaller-group variance reduction.
- Reporting all four scheduling strategy results per model in a single table (rather than only two) would allow readers to assess strategy robustness without per-model selection.
- Figure 5's label states "mu=0.5 (CANON-Intra)" and "mu=0.3 (DR.GRPO)" — per the paper's own formulation μ=0.5 is DR.GRPO (Eq. 7) and μ=0.0 is CANON-Intra. The figure legend appears to have a labeling error worth clarifying.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"Claim that CANON avoids presupposing direction is partly overstated" (scheduling imposes direction)**: The critic notes that the scheduling strategy "First-Inter-Later-Intra" implicitly presupposes that inter-group advantage should come first. This is a philosophical tension but not a factual error — the scheduling is a higher-level design choice, and CANON itself at the level of a given training step remains direction-agnostic. REMOVED as scope creep.

- **"Reflection gain analysis validity"**: The critic flags that reflection detection via pattern matching is a proxy. This is true but the analysis is explicitly interpretive (Section 6) and the proxy is standard in the LRM literature. REMOVED — not a substantive weakness.

- **Strength: "Evaluation is thorough — three model families, six benchmarks, eight baselines"**: KEPT above with specific evidence.

- **Strength Finder's generic praise** ("paper addresses an important problem"): REMOVED per instructions.

---

## Novel Insights

The most genuinely novel insight is the exact algebraic recovery of DR.GRPO as a μ=0.5 special case of CANON (Eq. 7) — this transforms what could have been an ad hoc "we tried two groupings" paper into a principled one. The second insight, that intra-group advantage's benefit on complex logic reasoning emerges only in the later stages of training (Figure 2f, reflection gain crossing zero at ~90 steps) and correlates with a measurable proxy (reflection gain), provides a mechanistic narrative for *when* and *why* exploration-encouraging objectives help. The CANON-Eff finding that even a tiny asymmetric weighting of the length group (α < 1) can stably traverse the efficiency-performance Pareto frontier — while a small perturbation in an additive length penalty causes catastrophic collapse — has practical implications for RLVR training recipe design.

---

## Suggestions

1. Correct or explicitly label Figure 3's data table — if it uses radar-chart axis coordinates, say so; if it is meant to display actual performance, reconcile the numbers with Tables 1 and 2.
2. Elevate the "First-Inter-Later-Intra achieves consistent gains across all three models without per-model selection" finding to the main text as the primary evidence for CANON-Dynamic.
3. Add ±1σ or 95% CI to AIME24/25 results; use the multi-benchmark Acc column as the headline number rather than individual AIME scores.
4. Add an explicit caveat on Theorem 2 noting the independence assumption is idealized and that Table 4 is empirical support rather than a formal substitute.

---

## Score and Decision

**Round 1 Bracket**: Papers on RL reward/advantage design for LLM reasoning scored:
- Weak (<3.5): 2.5–3.25 (general RL, not specific to RLVR)
- Middle (3.5–7.5): 5.17–5.67 (RL reward for LLM math, reward shaping, Q-shaping, LLM RLHF)
- Strong (>7.5): 8.0 (WizardMath, reward modeling theory papers — more impactful/novel)

Initial bracket: **5 to 7**.

**Round 2 Narrowing**: Most relevant anchors:
- F0GNv13ojF (5.17): Identifies reward-hacking with PRMs in RL training. Less comprehensive than CANON — fewer models, narrower method — but similarly incremental. CANON is better: cleaner formulation, broader evaluation, algorithmic novelty (not just empirical finding). *CANON > this anchor.*
- sNtDKdcI1f (6.00): Documents length-reward correlation in RLHF comprehensively. Descriptive rather than prescriptive; no new algorithm. CANON is more prescriptive and algorithmically richer. *CANON ≥ this anchor.*
- BGnm7Lo8oW (5.50): Pre-training-scale reasoning; broader scope claim, less evaluation. *CANON comparable or better.*
- DlqRpj68xe (5.67): Q-shaping for RL with LLMs. Interesting but niche. CANON has more thorough empirical coverage. *CANON ≥ this anchor.*

The Figure 3 inconsistency and per-model strategy selection are Major issues that depress the score relative to what a clean version would achieve. However, Table 2 shows the core claim survives these issues (First-Inter-Later-Intra beats DR.GRPO on all 3 models), and the CANON-Eff results are genuinely strong. The paper sits above the 5.17–5.67 cluster of anchors (more algorithmic, broader, theoretically grounded) but below the 6.5–7 range that would characterize a clean and impactful contribution. The presentation issues prevent confident acceptance.

| Anchor | Score | Round | Comparison |
|---|---|---|---|
| ZK1NnjpjEs | 3.00 | 1 | Much weaker; general NLU RL, no novel algorithm |
| VRRuYBaq9u | 3.25 | 1 | Unrelated domain (POMDPs) |
| 28TLorTMnP | 2.50 | 1 | Much weaker; simple alignment objective |
| BGnm7Lo8oW | 5.50 | 1 | CANON has narrower but cleaner contribution |
| F0GNv13ojF | 5.17 | 1,2 | CANON is more algorithmic, more thorough |
| RtOTTdWbZd | 5.25 | 1 | Different (RLHF with squared error loss), less thorough |
| sNtDKdcI1f | 6.00 | 2 | CANON is more prescriptive; Figure 3 issue comparable to presentation flaw there |
| DlqRpj68xe | 5.67 | 2 | CANON has broader eval and cleaner theory |
| 0er6aOyXUD | 5.40 | 2 | Less algorithmic, narrower scope |
| o2uHg0Skil | 6.25 | 2 | CANON has stronger empirical breadth, comparable theory |

**Final score: 5.5** (borderline reject). The contribution is real and the CANON-Eff results and DR.GRPO decomposition are genuinely valuable, but the Figure 3 data table inconsistency and under-disclosed per-model strategy selection represent fixable but real problems that currently prevent confident acceptance.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>
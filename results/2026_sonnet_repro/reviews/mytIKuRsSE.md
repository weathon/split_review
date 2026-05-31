Now let me run calibration searches to anchor the score.Now I have enough to write the final review. Let me synthesize.

---

## Summary

This paper introduces **Dual-level Noisy Correspondence (DNC)**, a practical but under-explored problem in Multi-Modal Entity Alignment (MMEA) where both intra-entity (entity-attribute) and inter-graph (entity-entity, attribute-attribute) correspondences can be noisy. To address it, the authors propose **RULE** (dually Robust Learning), which estimates correspondence reliability via a two-fold principle (uncertainty from Dempster-Shafer theory + consensus from marginal contributions), applies a Dually Robust Learning loss (DRL) for inter-graph alignment and a Dually Robust Fusion (DRF) module for intra-entity attribute fusion, and adds a Test-time Correspondence Reasoning (TTR) module powered by Qwen2.5-VL-72B-Instruct with chain-of-thought prompting. Experiments on five MMEA benchmarks with seven state-of-the-art baselines demonstrate consistent and often substantial gains under inherent, 20%, and 50% injected DNC.

---

## Strengths

1. **Novel and well-motivated problem formulation**: The paper empirically demonstrates that real-world MMEA benchmarks contain substantial noisy correspondences (>50% in ICEWS). Figure 1(b) directly shows that both vanilla adaptive fusion and concatenation methods degrade significantly under DNC, motivating the paper's scope.

2. **Reliable separation of clean and noisy pairs**: The combination of uncertainty (Eqs. 2–3, Dempster-Shafer) and consensus (Eq. 5) yields reliability scores (Eq. 1) that clearly distinguish clean from noisy correspondences in practice. Figure 3(b) shows clean pairs concentrated at high reliability while noisy pairs are predominantly at low reliability; Figure 4 shows the three subsets S_U, S_I, S_C forming distinct clusters in uncertainty–consensus space.

3. **Strong, broad empirical results**: Table 1 and Table 2 show RULE consistently outperforming all seven state-of-the-art methods across five benchmarks (ICEWS-WIKI, ICEWS-YAGO, DBP15K ZH/JA/FR-EN) under inherent, 20%, and 50% DNC, in both Non-name and All-attributes settings. The Non-name 50% DNC ICEWS-WIKI result (58.2% H@1 vs. 43.9% for best baseline) represents a particularly large margin.

4. **Ablation study validates each component**: Table 3 isolates the contributions: removing DRL drops Non-name H@1 from 58.2 to 31.6; removing DRF drops it to 50.4; removing TTR drops it to 56.5; using only uncertainty drops it to 53.5; using only consensus drops to 48.3. Each component is individually verified.

5. **Qualitative analysis corroborates fusion design**: Figure 5 shows that RULE assigns high reliability to clean attributes and low reliability to injected noise in both image and name modalities, directly confirming the DRF mechanism of Eq. 14.

---

## Weaknesses

### Fatal
None.

### Major

- **TTR uses a 72B MLLM unavailable to baselines, and this advantage is not clearly separated in the main tables.** The paper's statement "for fair comparisons, we adopt the same backbone (CLIP) for all baselines and our method" applies only to the attribute encoders; it does not address the Qwen2.5-VL-72B-Instruct used at test time in TTR. Looking at the ablation (Table 3) for the All-attributes 50% DNC ICEWS-WIKI setting: RULE w/o TTR achieves 94.0% H@1 while the best baseline (MEAformer, Table 2) achieves 91.9%—so the training-time components do outperform baselines even without TTR. However, TTR adds a further 3.7 points (94.0 → 97.7), and this gain is reported in the main Tables 1–2 as a single "Ours" row without identifying which margin comes from training-time contributions versus the 72B MLLM. The paper should clearly present RULE w/o TTR alongside the full RULE in the main comparison tables so readers can evaluate the training contribution and the MLLM augmentation separately. As it stands, the asymmetry remains unexplained and potentially misleading for researchers without MLLM access.

### Minor

- **Assumption 1 (marginal contribution criterion for correct entity-attribute correspondence) is stated but not empirically validated directly.** The paper claims that if attribute $x_i^m$ is correctly associated with entity $x_i$, then its marginal contribution $\Delta \geq 0$ (Eq. 6–7). The aggregate reliability distribution plots (Figures 3(b), 4, 5) show end-to-end effectiveness, but they do not report what fraction of the greedy $\pi^*$ selections correctly identify the clean attribute subset against ground truth. A direct validation (even in a small synthetic controlled experiment) of how accurately Eq. 7 recovers the true clean subset would meaningfully strengthen the methodological case.

- **No runtime or computational cost analysis for the TTR module.** TTR invokes a 72B VLM per candidate entity pair at inference time (Eq. 16, Section 2.5). For practical MMEA at scale, this cost could be prohibitive. The paper provides no per-query latency, total inference time, or discussion of whether this approach is feasible for the full ICEWS or DBP15K test sets. This limits the reader's ability to assess real-world applicability.

- **Ablation is conducted on a single dataset and noise level.** Table 3 covers only ICEWS-WIKI at 50% DNC. Whether the relative contributions of DRL, DRF, and TTR are stable at lower noise levels (inherent or 20%) or on DBP15K datasets (which have different scale and noise characteristics) is not shown. An additional noise level or dataset would strengthen the ablation.

### Trivial

None of consequence.

---

## Nice-to-Haves

- Show RULE w/o TTR in the main comparison tables (Tables 1–2) alongside the full RULE system. This would make the training-time contribution immediately legible and address the TTR fairness concern proactively.
- Provide a brief characterization (even one sentence) of the DNC measurement methodology from Appendix B in the main text, since the ">50% in ICEWS" claim is the paper's key motivating statistic.
- Report runtime for TTR, even a rough per-entity estimate, to help practitioners assess applicability.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Harsh critic claim: "MEAformer achieves 94.7 and RULE w/o TTR does not beat it."** This is a factual error. The 94.7 figure is MEAformer's *average H@1 across all five datasets* in the 50% DNC setting. The correct per-dataset comparison is: RULE w/o TTR (94.0%) vs. MEAformer (91.9%) on ICEWS-WIKI 50% DNC All-attributes. RULE w/o TTR does outperform the best baseline even without TTR. The severe version of this critique (fatal, structural unfairness) is unfounded; the concern is real but should be a Major, not a fatal flaw.

- **Attribute-attribute NC dependency**: The harsh critic notes that attribute-attribute NC is derived from the entity-entity and entity-attribute NC types (Section 2.1), and is not independent. While technically accurate, the paper acknowledges this explicitly in Section 2.4 ("inter-graph attribute associations emerge as the by-product…"). This is not a hidden flaw; it is how the formulation is designed. Removed as a non-issue.

- **Artificial noise interacting with inherent DNC**: The harsh critic raises that injecting noise on top of inherent DNC may produce an unrealistic combined corruption rate. While a valid methodological nuance, this applies equally to all baselines and does not selectively harm or benefit RULE. Removed per the rule on asymmetric comparisons.

- **DNC rate methodology from Appendix B not in main text**: The paper explicitly places detailed statistics in Appendix B. Per the hard rules, appendix sections are stripped from parsed PDFs and should not be criticized as absent. Removed.

- **Strength Finder claim about TTR as a "first method to enhance test-time robustness for MMEA"**: This is a plausible but unverifiable novelty claim. Kept as context but not independently verified.

---

## Novel Insights

The paper's most interesting structural observation—confirmed by the ablation—is that DRL and DRF together provide robust training-time performance (56.5% Non-name H@1 under 50% DNC vs. 43.9% for the best baseline) while TTR provides a further complementary boost at inference time. This separation of training-time robustness and test-time reasoning is a genuine design pattern for noisy multi-modal learning, and may generalize beyond MMEA. The consensus-based greedy attribute selection (Eq. 7) as a proxy for ground-truth correspondence during inference is a practical and theoretically grounded heuristic that could inform similar reliability-estimation problems in other cross-modal matching tasks.

---

## Suggestions

1. **Split Tables 1–2 or add a "RULE w/o TTR" row** to make the training-time contribution clearly evaluable against baselines independently of the 72B MLLM component.
2. **Add a direct validation of Assumption 1** in a synthetic experiment where the clean attribute subset is known: report the precision/recall of the greedy $\pi^*$ selector (Eq. 7) against ground truth to quantify when the assumption holds.
3. **Report TTR inference overhead**: at minimum, wall-clock time per entity or per test set, and discuss scalability implications.
4. **Include at least one additional noise level in the ablation** (e.g., inherent DNC or 20%) to confirm component contributions are stable across noise regimes.

---

## Score and Decision

**Round 1 bracket**: Based on weak anchors (~3.0), middle anchors (5.75–6.67), and strong anchors (~8.0), the paper clearly sits in the 5.5–7.5 range, likely 6–7 given its novel problem, broad empirical coverage, and the one notable methodological concern.

**Round 2 narrowing**: Key comparators:
| Paper | Avg Score | Decision | Comparison |
|---|---|---|---|
| NNUiUwQWx6 — Neuro-symbolic EA | 5.75 | Reject | Weaker: single-setting evaluation, denser theory, no novel problem |
| z3dfuRcGAK — Generative EEA | 6.67 | Accept | Comparable: novel perspective + theory, but less empirical breadth |
| ue1Tt3h1VC — Mixture of Modality Experts | 6.60 | Accept | Comparable: multi-modal MMKG with strong results, but narrower scope |
| ftGnpZrW7P — GRAM multimodal | 7.00 | Accept | Stronger: elegant unified theory across n modalities |
| jJCeMiwHdH — BioBridge | 7.00 | Accept | Stronger: cross-domain foundation model bridging |

The paper under review is clearly better than the 5.75 anchor (broader evaluation, stronger novelty of problem, more components). It is comparable to the 6.60–6.67 anchors: it has more empirical breadth and a clearer novel problem, but the 6.67 anchor (GEEA) also has theoretical analysis and entity synthesis as a bonus task. The TTR fairness concern (Major weakness) prevents reaching 7.0. The training-time contribution genuinely stands on its own (beating baselines without TTR), which prevents a lower score.

**Final placement**: 6.5 — between the 6.6–6.7 range anchors and the 7.0 anchors. The paper makes a genuine, well-supported contribution to a practical problem in MMEA, with one resolvable methodological presentation issue (TTR separation). This is a marginal accept.

**Axis evaluation:**
- *Originality*: Good — DNC problem formulation is novel; DRL/DRF/TTR pipeline is principled
- *Importance*: Good — noisy correspondence in MMEA is practically relevant given dataset construction realities
- *Claim support*: Good — Tables 1–2 with 5 datasets/7 baselines, Figure 3 ablation over noise levels, Table 3 component ablation
- *Soundness*: Good — methodology is technically grounded; Assumption 1 unvalidated but intuitive
- *Clarity*: Good — paper is well-structured with clear motivation
- *Community value*: Good — the DRL/DRF framework and the TTR idea are independently applicable

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>
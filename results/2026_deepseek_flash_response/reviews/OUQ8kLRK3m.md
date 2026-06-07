## Summary

DRE-Bench proposes a dynamic abstract reasoning benchmark for LLMs organized around a four-level cognitive hierarchy (Attribute → Spatial → Sequential → Conceptual) grounded in the Primi (2001) psychology framework. The paper introduces a code-verifiable generator-solver pipeline for producing task variants with controlled complexity, evaluates 11 LLMs, and finds that model performance declines across cognitive levels with all models failing at Level-4 conceptual tasks.

## Strengths

1. **Cognition-aligned hierarchy validated against human performance.** The four-level framework is grounded in the established Primi (2001) cognitive psychology hierarchy. Table 1 shows human accuracy declining monotonically across levels (77.51% → 70.38% → 65.05% → 47.33%), and the paper reports a t-test confirming statistical significance, validating the hierarchy's cognitive ordering.

2. **Code-verifiable data pipeline with guaranteed correctness.** Section 3.2 and Figure 3 describe a pipeline where LLM-driven code agents implement generators and solvers, verified by a tester before acceptance. The paper claims "100% reliability of the generated samples," substantiated by the code-verification mechanism — a notable improvement over prior dynamic benchmarks whose correctness is "difficult to verify."

3. **Dynamic complexity analysis discriminates genuine understanding from memorization.** Figure 4 shows that for Level-2 Move tasks, models with high accuracy remain robust as complexity increases while weaker models fail even on simple cases. For Level-3 Planning, all models consistently fail when planning depth reaches 2 steps. This stability-vs-decline pattern directly supports the claim that the benchmark can distinguish whether models truly master underlying reasoning rules.

4. **Clear evidence that all LLMs fail at high-level Conceptual cognition.** Table 1 shows near-zero performance on Level-4 tasks (best: o3-mini at 10.58%, Claude-3.7 at 7.96%, most models at 0%), while humans achieve 47.33%. This provides strong, quantified evidence supporting the paper's central claim that existing LLMs remain far from achieving human-like fluid intelligence.

5. **Discovery of systematic spatial orientation bias in LLMs.** Table 3 reveals that all tested models perform significantly better on vertical movement (up/down) than horizontal (left/right), and better on horizontal symmetry than vertical symmetry — a divergence from human cognition where these are treated equivalently. This finding is enabled by DRE-Bench's fine-grained multi-variant design and would not be detectable with coarser benchmarks.

## Weaknesses

### Major

1. **The headline claim that reasoning LLMs outperform general LLMs is contradicted by the paper's own data.** In Table 1, Claude-3.7 (categorized as a general LLM) achieves the highest accuracy on Level 3 (44.05% avg., vs. o1's 28.92% and DeepSeek-R1's 35.55%) and Level 4 (7.96% vs. o1's 2.65% and DeepSeek-R1's 0.53%). On Level 2, Claude-3.7 (58.43%) is competitive with o1 (58.88%) and DeepSeek-R1 (62.79%). The paper states in Section 4.2 that "reasoning-specialized models consistently outperform [general-purpose models] in terms of average cognitive level" and the Conclusion (Section 5) repeats "reasoning-oriented models outperform general LLMs." Neither statement is supported by the data — Claude-3.7 beats every reasoning model on the two highest cognitive levels. This is not a minor phrasing issue; it is a mismatch between the paper's central narrative and its empirical evidence. The data actually tells a more nuanced story (a general-purpose model excelling at high-level abstract reasoning) that the paper fails to engage with.

2. **The "dynamic evaluation" advantage is oversold relative to what is demonstrated.** The paper positions "dynamic evaluation" as a key advantage over static benchmarks like ARC, claiming it "helps avoid the data contamination issue." However, DRE-Bench as described provides "about 4K abstract reasoning cases" — a fixed dataset, not a protocol that generates new instances at test time. The generator-solver pipeline is a production methodology for creating the benchmark, not an evaluation protocol. The paper never specifies whether evaluators would use the pipeline to generate fresh instances during evaluation or would use the pre-generated ~4K cases. If the latter, the benchmark is as vulnerable to data contamination as the static benchmarks it criticizes. More importantly, the paper provides no evidence that the "dynamic" property yields different or more robust evaluations compared to static sampling.

3. **No direct quantitative comparison to ARC-AGI or other existing abstract reasoning benchmarks.** Despite positioning DRE-Bench as an advance over ARC-AGI and using ARC's limitations as a primary motivation, the paper provides no quantitative comparison. Do the same models that struggle on ARC also struggle on DRE-Bench? Does the cognitive hierarchy provide information beyond what monolithic ARC scores reveal? Without this comparison, the marginal contribution of DRE-Bench over existing resources is unclear. A benchmark paper should demonstrate what its benchmark reveals that prior benchmarks do not.

### Minor

4. **The human study format is underspecified, weakening the human-LLM comparison.** The paper does not specify whether humans received visual grids (as shown in Figure 2) or text-based grid representations (as presumably given to LLMs). This matters because the paper's own ablation (Table 2) shows that adding visual information does not help LLMs and sometimes hurts. Additionally, the paper describes human accuracy as "slightly higher" when the gap is enormous (Level-3: 65.05% human vs. 44.05% best LLM; Level-4: 47.33% human vs. 7.96% best LLM). The main value of the human study — validating the cognitive hierarchy via monotonically declining accuracy — stands regardless of format, but the direct comparison claim is undermined.

5. **Level-4 Conceptual tasks blur the fluid vs. crystallized intelligence distinction.** The paper motivates DRE-Bench by distinguishing fluid intelligence (abstract reasoning in novel situations) from crystallized intelligence (knowledge application). Yet Level 4 tasks (Gravity, Reflection, Expansion) explicitly require knowledge of physics concepts. The paper acknowledges this ("require... application of conceptual knowledge," line 121) but never discusses the tension with the fluid intelligence framing, nor does it consider that human performance on Level 4 (47.33%) likely depends on annotators' physics knowledge.

6. **No limitations section.** For a benchmark paper — where scope, coverage, and potential biases directly affect usability — the absence of a limitations discussion is notable. The paper does not discuss the brittleness of exact-match accuracy (which its own error analysis acknowledges can be misleading), distribution balance across levels, or potential for generator code leakage into training data.

### Trivial

7. **Duplicate o3-mini rows in Table 1.** Two rows labeled "o3-mini" with substantially different values (lines 148-149) make the table uninterpretable for this model. These likely correspond to different variants (e.g., o3-mini-high vs. o3-mini-medium) but are identically labeled.

## Nice-to-Haves

- Direct comparison to ARC-AGI on the same set of models to demonstrate DRE-Bench's differentiating value
- Variance or confidence intervals for model scores (currently only "three trials" are mentioned without statistics)
- Clarify which o3-mini variant corresponds to each row in Table 1
- A limitations section discussing scope and potential biases

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Questioning the existence/release status of cited models/tools/benchmarks** — removed per hard rules (the paper cites them; they exist).
- **Missing appendix content** — removed per hard rules (appendices exist in original submission; parser strips them).
- **Generic concerns about task design being "arbitrary"** — removed as speculation without specific evidence.
- **Claim about ARC-AGI-2 incorporating dynamism** — removed as insufficiently verified from the review input.
- **Strength Finder's generic strengths ("addresses an important problem", "well-written")** — removed as generic/superficial.
- **Criticism that `deepseek-R1 Avg-1` seems miscalculated** — the table formatting may cause parsing artifacts but the values as presented are what they are.

## Novel Insights

The systematic spatial orientation asymmetry (vertical > horizontal, horizontal symmetry > vertical symmetry) is a genuinely novel behavioral finding that would be difficult to surface with any existing benchmark, including ARC-AGI. The observation that visual information fails to improve, and sometimes harms, abstract reasoning in VLMs is also a non-obvious result worth highlighting. These insights demonstrate the kind of fine-grained analysis DRE-Bench can enable.

## Suggestions

1. **Fix the claim-evidence mismatch:** Reconcile the claims about reasoning vs. general LLMs with the actual data. Claude-3.7's strong performance at higher levels is an important finding that the paper should engage with — it may point to how general-purpose pretraining confers advantages that chain-of-thought reasoning alone does not fully compensate for.
2. **Clarify the evaluation protocol:** State whether DRE-Bench is a fixed dataset or a generative framework. If the former, adjust the "dynamic" framing accordingly. If the latter, describe how live generation works in practice and provide evidence that it actually prevents contamination.
3. **Add an ARC-AGI comparison:** Run overlapping models on both benchmarks to demonstrate DRE-Bench's differentiating value.
4. **Specify the human study format** in the main text and correct the "slightly higher" characterization.
5. **Add a limitations section** discussing the benchmark's scope, potential biases, and the fluid-vs-crystallized boundary issue at Level 4.
6. **Fix the duplicate o3-mini rows** and add model variant labels.
7. **Add confidence intervals or variance measures** for model scores.

## Score and Decision

**Calibration Method:**

*Round 1 — Bracketing*: Queried three bands (low: <3.5, middle: 3.5–7.5, high: >7.5) on abstract reasoning benchmarks and LLM evaluation. Low-band papers (avg 2–3) had fundamental execution problems — DRE-Bench clearly outperforms these. Middle-band papers (5.33–6.75) include similar benchmark contributions. High-band papers (8.0) are comprehensive, polished works — DRE-Bench is not at this level. Initial bracket: **4.0–5.5**.

*Round 2 — Narrowing*: Queried inside the bracket to find anchors in (4.0, 6.5), (3.0, 5.5), and (5.5, 7.5). Read full reviews of the most comparable papers (DyVal 6.50, ActionReasoningBench 6.75, LLMs Are Not Strong Abstract Reasoners 5.33, ARB 5.50, ∀uto∃∨∧L 6.33). Compared against each:

- **vs. "LLMs Are Not Strong Abstract Reasoners" (5.33)**: DRE-Bench has a stronger pipeline and theoretical grounding but suffers from a more serious claim-evidence mismatch. Comparable or slightly weaker.
- **vs. "ARB" (5.50)**: DRE-Bench has a more coherent design (cognitive hierarchy) but the claim-evidence issues are more severe than ARB's weaknesses. Comparable.
- **vs. "ActionReasoningBench" (6.75)**: DRE-Bench is clearly weaker — the ActionReasoningBench review critiques are about presentation and human baselines, whereas DRE-Bench's issues go to the accuracy of its central claims.
- **vs. "DyVal" (6.50)**: DRE-Bench is weaker — DyVal genuinely implements a dynamic protocol, while DRE-Bench oversells its dynamism.
- **vs. "ReCogLab" (5.00)**: Similar in framing (cognitive framework + dynamic generation) with similar execution concerns. Comparable.

The paper has genuine contributions (cognitive hierarchy, verification pipeline, spatial bias finding) that justify placement above the 2–3 band, but the verifiable claim-evidence mismatch on reasoning vs. general LLMs and the overselling of the "dynamic" property are substantive issues that distinguish it from cleaner papers at 5.5–6.0. Final score: **5.0**.

| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|------------|
| Improving AI via Novel Computational Models | NlY3XppPt3.md | 2.00 | 1 | Much weaker |
| Planning in Strawberry Fields | jOuHjFw71C.md | 3.00 | 1 | Weaker |
| Exploring Planning Capabilities of LLMs | koza5fePTs.md | 2.00 | 1 | Much weaker |
| Entering Real Social World | b1vVm6Ldrd.md | 3.00 | 1 | Weaker |
| LLMs Are Not Strong Abstract Reasoners | 28gMnEAgl9.md | 5.33 | 1, 2 | Comparable |
| ActionReasoningBench | NUD03NBDOE.md | 6.75 | 1, 2 | Stronger |
| ARB: Advanced Reasoning Benchmark | gsZAtAdzkY.md | 5.50 | 1, 2 | Comparable |
| The Labyrinth of Links | vJ0axKTh7t.md | 6.25 | 1 | Stronger |
| PhysBench | Q6a9W6kzv5.md | 8.00 | 1 | Much stronger |
| MMQA | GGlpykXDCa.md | 8.00 | 1 | Much stronger |
| LOKI | z8sxoCYgmd.md | 8.00 | 1 | Much stronger |
| MMIE | HnhNRrLPwm.md | 8.00 | 1 | Much stronger |
| ∀uto∃∨∧L | iv1TpRCJeK.md | 6.33 | 2 | Stronger |
| Assessing Knowledge-intensive Reasoning | iSTMsye6SD.md | 5.25 | 2 | Comparable |
| LLMs Meet Symbolic Provers | C25SgeXWjE.md | 6.25 | 2 | Stronger |
| Unlocking Structured Thinking | VOBhmsqQlQ.md | 3.50 | 2 | Weaker |
| ReCogLab | yORSk4Ycsa.md | 5.00 | 2 | Comparable |
| DyVal: Dynamic Evaluation | gjfOL9z5Xr.md | 6.50 | 2 | Stronger |
| LiveCodeBench | chfJJYC3iL.md | 6.25 | 2 | Stronger |
| Unveiling Code Reasoning | kN25ggeq1J.md | 5.67 | 2 | Comparable |

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>
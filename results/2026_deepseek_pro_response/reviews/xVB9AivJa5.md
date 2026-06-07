Now let me write the final review.

---

## Summary
This paper introduces Blueprint-Bench, a benchmark for evaluating spatial reasoning in AI models by requiring them to reconstruct 2D floor plans from ~20 apartment interior photographs. The benchmark evaluates three model paradigms — LLMs generating SVG, image generation models, and AI agents in Docker — using an automated two-stage scoring pipeline (CV extraction + graph similarity). Results on 12 models show most score in the 0.32–0.42 range against a no-vision baseline of 0.279, with humans at ~0.547, suggesting spatial reasoning from photographs remains challenging for current AI.

## Strengths
- **Cross-paradigm benchmark design**: The paper evaluates LLMs, image generation models, and AI agents on an identical spatial reasoning task, enabling direct numerical comparison across architectures that no existing benchmark provides (Section 2.2, Figure 5).
- **Automated, reproducible scoring pipeline**: The two-stage evaluation (CV extraction via HSV filtering, flood-fill segmentation, door detection → six-component graph similarity with explicit weights) produces objective scores without human judgment or LLM-as-judge (Section 2.3).
- **Human baseline with honest calibration**: Figure 7 places human performance (~0.547) in direct comparison with all models and explicitly notes that humans achieved perfect connectivity but were penalized for size-ranking errors — the reported human-AI gap is thus a lower bound (Section 3, lines 149–173).
- **Documented design alternatives**: Section 2.4 reports failed attempts at LLM-based room extraction and bidirectional nearest-neighbor wall-distance scoring, helping future work avoid known dead ends.
- **Agent trace analysis**: The qualitative analysis of agent behavior (Figure 8) reveals that Claude Code iteratively refined its drawings but claimed "Each room is fully enclosed" when this was false — surfacing a metacognitive failure beyond simple single-pass limitations.

## Weaknesses

### Fatal
None.

### Major
- **Central claim contradicted by the data**: The abstract states "most models perform at or below a random baseline" and the body (line 112) similarly claims "most do not outperform the random baseline." However, from Figure 5's table, 10 of 12 models score above the baseline (0.279): scores range from 0.32–0.42 for the majority, with only GPT-4o (0.15) and Nano Banana (0.18) falling below. The paper's headline narrative is contradicted by its own numbers. The authors appear to use "statistically perform better" (line 112) as a qualifier, but no formal statistical tests are reported to support a "most do not statistically significantly outperform" interpretation. This either needs retraction of the claim or reframing supported by actual tests.

- **Instruction-following confound in scoring without quantification**: The evaluation requires models to adhere to 9 strict formatting rules (3px black walls, 10×10px red dots, pure colors only, etc.). The paper acknowledges this tension in Section 2.4 ("Blueprint-Bench should test spatial intelligence, not instruction following") but does not resolve or quantify it. GPT-4o and Nano Banana score near zero explicitly because of poor instruction following (line 138), while GPT Image scores at baseline despite showing no spatial intelligence but following the rules. For these models, the score reflects formatting compliance rather than spatial reasoning. The paper argues the strict rules are needed for robust scoring — a reasonable tradeoff — but it does not quantify how much the confound affects model rankings or provide any analysis of whether rankings would change under more permissive evaluation. This matters because the benchmark's validity as a spatial intelligence measure depends on disentangling these two capabilities.

### Minor
- **Model categorization errors in results table**: The results table (lines 119–132) labels all models as "Image model" except the two agents. LLMs generating SVG (GPT-5, Claude Opus 4.1, Gemini 2.5 Pro, Grok 4, etc.) are mislabeled — they are not image generation models. This makes the paper's stated contribution of comparing "image generation models to their underlying LLMs" (line 39) harder to follow from the results alone.

- **Misleading baseline terminology**: The "random baseline" (line 69) is constructed by "generating typical floor plans using LLMs and image generation models without any image input" — this is a no-vision prior baseline, not a random baseline. A random baseline would involve randomly assigning connectivity and room sizes. The terminology is misleading.

- **No statistical tests reported**: The paper uses phrases like "statistically perform better" (line 112) and "not statistically better" (line 179) but reports no test statistics, p-values, or effect sizes. Given the tight score clustering (0.38–0.42 for top models), formal testing is needed to determine whether apparent differences are reliable.

- **Small human baseline subset**: Human performance is evaluated on only 12 of 50 apartments, limiting the robustness of the paper's primary comparative claim versus humans.

- **Arbitrary scoring weights without sensitivity analysis**: The composite score uses fixed weights (50/20/10/10/5/5) with no justification or sensitivity analysis showing whether model rankings are stable under alternative weightings.

### Trivial
- **"Epochs" undefined**: The paper references "across apartments and epochs" (line 112) without defining what an epoch means in this context.

## Nice-to-Haves
- Extend the human baseline to all 50 apartments.
- Add a sensitivity analysis for the scoring weights to confirm ranking stability.
- Explore more permissive format requirements coupled with VLM-based extraction to reduce the instruction-following confound.
- Report formal statistical tests (e.g., bootstrap confidence intervals) for model comparisons.

## Removed Points
These points are flagged to be removed, treat them with caution.

- **Harsh Critic: baseline value discrepancy as structural flaw** — The baseline shifts from 0.279 (all 50) to 0.322 (12-apartment subset). This is a natural consequence of subset selection, not a structural flaw. Different subsets yield different averages. Removed.

- **Harsh Critic: scoring protocol confound as fatal/structural** — The paper explicitly acknowledges this limitation (Section 2.4) and argues for the tradeoff. The confound primarily affects 2 of 12 models, and the paper identifies which models these are. Demoted from fatal to major — the real issue is lack of quantification, not that the confound exists.

- **Harsh Critic: model categorization as fatal** — The table mislabeling is real but the paper's text (Section 2.2) clearly distinguishes LLMs from image models. This is a presentation error, not a structural invalidation. Demoted to minor.

- **Strength Finder: "fills a documented evaluation gap" as standalone** — Merged into the cross-paradigm strength, as it's essentially the same point from a different angle.

## Novel Insights
The agent trace analysis (Figure 8) provides a concrete, interpretable insight: iterative refinement alone does not close the spatial reasoning gap because agents lack metacognitive awareness — Claude Code claimed "Each room is fully enclosed" when this was false. This suggests the bottleneck is not merely single-pass limitations but involves failures in spatial verification. This observation goes beyond standard benchmark reporting and suggests directions for future work on agent self-evaluation.

## Suggestions
- Reframe the central claim: the data supports "models extract some spatial signal but remain far below human performance" rather than "most are at or below random." This is both more accurate and more interesting.
- Fix the model categorization in the results table to distinguish LLMs (SVG generation) from image generation models.
- Add formal statistical tests to support claims about which models significantly outperform the baseline.
- Compute and report how much the size-ranking cascading penalty affects scores (e.g., by reporting connectivity-only scores alongside the composite).

---

## Score and Decision

### Calibration anchors

**Round 1 (Bracketing):**

| Anchor | Avg Score | Decision | Comparison |
|--------|-----------|----------|------------|
| SPACE (WK6K1FMEQ1) — spatial cognition benchmark | 6.75 | Accept | SPACE has 15 tasks, stronger cognitive science grounding, better execution. Blueprint-Bench is weaker due to sloppy results presentation and unresolved confounds. |
| FoREST (9Y6QWwQhF3) — spatial FoR benchmark | 4.25 | Reject | FoREST uses synthetic template data, unclear whether it tests spatial reasoning vs template matching. Blueprint-Bench is stronger with real data and concrete task. |

**Round 1 bracket: 4.5 – 6.5**

**Round 2 (Narrowing):**

| Anchor | Avg Score | Decision | Comparison |
|--------|-----------|----------|------------|
| STBench (oecFal31WP) — spatio-temporal benchmark | 5.75 | Reject | STBench has larger scale (60K QA, 13 tasks) but task meaningfulness questioned. Blueprint-Bench has more novel/creative task design but factual error in central claim. Comparable quality — Blueprint-Bench slightly weaker. |
| Labyrinth of Links (vJ0axKTh7t) — association benchmark | 6.25 | Accept | Better executed than Blueprint-Bench; no factual errors in results. Blueprint-Bench's cross-paradigm design is more novel but execution is sloppier. Blueprint-Bench is clearly weaker. |
| SR² (2seVGyWZOX) — 3D spatial reasoning method | 5.20 | Reject | Method paper, less comparable. Lower contribution margin. Blueprint-Bench is stronger as a benchmark contribution. |

Blueprint-Bench sits between STBench (5.75) and SR² (5.20). Its cross-paradigm design and concrete task are genuine strengths, but the central claim error and lack of statistical rigor pull it below STBench. The paper is clearly weaker than the accepted Labyrinth of Links (6.25) and SPACE (6.75).

**Final score: 5.5** — a borderline paper with real contributions that needs significant revisions to its claims and analysis before it can be accepted.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>
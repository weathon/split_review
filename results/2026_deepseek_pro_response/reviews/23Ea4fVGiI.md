Now I have a clear picture from round 2. Let me finalize the calibration.

**Round 1 bracket:** 4.0–6.0, based on:
- "Planning in Strawberry Fields" (3.00) — purely evaluative, no method. Our paper is clearly stronger.
- "Modular Agentic Planner" (4.50) — modular planning, proper ablations but novelty concerns. Comparable to our paper.
- "LLMs Can Plan Only If We Tell Them" (6.40) — AoT+, proper ablations, multi-domain, clearly better methodology. Our paper is below this.

**Round 2 narrowing:**
- "Tree-Planner" (5.25, Accept) — single-domain LLM planning with proper ablations. Our paper has a more dramatic result but weaker methodology.
- "Prefrontal Cortex-inspired Architecture" (5.25, Reject) — cognitive-inspired LLM planning, limited tasks, weak baselines. Very comparable framing to our paper (cognitive science → LLM planning). Our paper tests on a more rigorous benchmark (PlanBench) with more models, but shares similar ablation/comparison gaps.

**Final comparison:** Our paper sits near the PFC-inspired paper and Tree-Planner. The dramatic result (31.5% → 97.3%) and rigorous PlanBench benchmark pull it up; the missing JSON ablation, confounded comparison, and speculative claims pull it down. I place it at **5.0** — a borderline reject that could become an accept if the authors address the JSON ablation and soften the steering claims.

---

Now let me write the final review.

## Summary
This paper proposes using the Task-Method-Knowledge (TMK) framework — a knowledge representation from cognitive architectures — as a prompt structure for LLMs on planning tasks, evaluated on PlanBench Blocksworld. The key result is dramatic: under TMK prompting, o1's accuracy on Random Blocksworld jumps from 31.5% to 97.3%, and the typical difficulty ordering between Mystery and Random reverses (performance inversion). The paper hypothesizes that TMK's structured JSON format steers models from linguistic reasoning toward code-like symbolic manipulation.

## Strengths
- **Compelling performance inversion result in o1**: Under plain-text prompting, o1 scores 74.3% on Mystery vs. 31.5% on Random — the expected pattern where semantic cues help. Under TMK, this relationship flips: Random (97.3%) surpasses Mystery (83.3%). This 65.8pp gain and difficulty reversal is a genuinely striking empirical phenomenon unlikely to arise from trivial confounds.
- **Evaluation on a rigorous formal planning benchmark**: PlanBench uses automated planning validators (VAL, Fast Downward) requiring every action in the plan to be formally correct, not just the final state. This is a meaningfully stronger standard than typical LLM reasoning benchmarks.
- **Multi-model, multi-variant evaluation**: The paper tests across five OpenAI models (GPT-4, GPT-4o, o1-mini, o1, GPT-5) and all three PlanBench Blocksworld variants (Classic, Mystery, Random), producing a 5×3 result matrix that distinguishes broad effects from model-specific outliers.
- **Transparent engagement with negative results**: The o1-mini regression on Mystery (19.1% → 16.83%) is reported and discussed rather than hidden.
- **Principled methodology to address known prompting criticisms**: The paper explicitly addresses three common critiques — n-shot pattern matching, contradictory reasoning traces, and weak cross-domain performance — by using non-matching one-shot examples, full-plan evaluation, and a rigorous benchmark.

## Weaknesses

### Fatal
None.

### Major
- **No ablation separating TMK's conceptual framework from its JSON format**: The TMK prompt is delivered in JSON. The paper's own theory (Section 5.2.1) is that JSON steers models toward code-like reasoning. Without a comparison against a JSON-structured domain description that lacks TMK's specific task-method-knowledge decomposition, it is impossible to attribute the performance gains to TMK's conceptual structure rather than to structured formatting generally. This is essential to the paper's central claim that TMK specifically matters.
- **The "symbolic steering mechanism" claim is undersupported**: The paper claims (line 282) that the performance inversion serves as "empirical validation" of the steering effect, yet the conclusion (line 304) states "the cause of that increase is left to future work." The performance inversion is a single observation in one model (o1) and admits simpler explanations — e.g., the Random domain's opaque strings may be particularly confusing in English prose, and any structured format that cleanly separates identifiers from definitions would disproportionately help on Random. The paper provides no mechanistic evidence (reasoning trace analysis, probing, comparison against code-format baselines).
- **The core comparison is confounded by format and shot-count differences**: The TMK condition (one-shot, JSON-structured) is compared against plain-text baselines drawn primarily from the PlanBench leaderboard (zero-shot). The paper argues this is conservative because zero-shot allegedly outperforms one-shot for plain text, but the evidence is relegated to an OSF link. Even if true, the one-shot example provides output-format guidance that could interact differently with structured vs. unstructured domain descriptions. The comparison is not TMK vs. plain text; it is (TMK + JSON + one-shot) vs. (plain text + zero-shot).

### Minor
- **No statistical rigor reported**: Table 2 reports percentages to one or two decimal places with no confidence intervals, no instance counts per condition, no information about repeated runs. While the largest gains are dramatic enough to be unlikely noise, some differences are trivially small (e.g., o1-mini Classic: 56.7% → 57%, a 0.3pp gain; GPT-5 Classic: 99.3% → 99.7%) and cannot be meaningfully interpreted without variance estimates.
- **Single-domain evaluation**: The paper evaluates only on Blocksworld. The authors acknowledge this limitation honestly, but it limits generalizability claims.

### Trivial
- The enhanced extraction function (line 189) is applied to TMK results but its relationship to the extraction used for baseline results from the PlanBench leaderboard is not fully clarified.

## Nice-to-Haves
- A comparison against Chain-of-Thought prompting on the same models and instances would strengthen positioning relative to the literature the paper critiques.
- Reasoning trace analysis comparing TMK vs. plain-text outputs for code-like patterns would provide low-cost mechanistic evidence for the steering hypothesis.
- Expanding to at least one additional PlanBench domain (e.g., Logistics) would strengthen generalizability claims.

## Removed Points
These points are flagged to be removed, treat them with caution.

- **"GPT-5 baseline provenance is unclear"** (Harsh Critic): The paper states (line 193) that they ran PlanBench for newer models not on the leaderboard, and Table 2's footnote indicates provenance. Sufficiently clear.
- **"The TMK is author-designed, confounding framework with content quality"**: Inherent to any new prompting framework. Not a valid criticism.
- **"The paper omits relevant work on structured prompting (LLM+P, PDDL-based)"**: Cannot verify existence or relevance of specific uncited works.
- **"Key experimental parameters (temperature, instance counts) absent"**: Folded into the Minor weakness about statistical rigor.
- **"Formatting/style nitpicks about mermaid code redundancy"**: Presentation artifacts, not substantive.
- **"o1-mini regression explanation is post-hoc"** (Harsh Critic categorized as "less severe"): The paper is transparent that this is a hypothesis warranting further investigation (lines 211, 302). Not a weakness — honest engagement with an outlier.
- **"Zero-shot > one-shot evidence is in OSF, not main text"**: While true that the defense is OSF-linked, the paper does cite literature (Kojima et al., 2022) and provides reasoning in the main text. This concern is captured in the Major weakness about the confounded comparison.

## Novel Insights
The performance inversion pattern — where a structured domain description causes a reasoning model's relative difficulty ordering across domain variants to reverse — is a genuinely interesting empirical phenomenon. It suggests that prompt format can qualitatively change how a model processes a problem, not just add helpful context. This observation, if robust, has implications beyond TMK: structured prompting may be particularly valuable for tasks where surface-level linguistic features interfere with the underlying formal structure.

## Suggestions
- Run a JSON-structured domain description without TMK's task-method-knowledge decomposition as a minimal ablation. This is the single most important experiment to isolate TMK's contribution.
- Move the evidence for zero-shot > one-shot plain-text performance from the OSF link into the main paper, as the experimental design defense rests on this claim.
- Soften the causal language about "symbolic steering" and "empirical validation" to match the evidence level. The performance inversion is consistent with the steering hypothesis, not validation of it.
- Report instance counts per condition and note whether results come from single or multiple runs.

## Anchor Comparison

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| Planning in Strawberry Fields (o1 eval) | 3.00 | R1 | Our paper proposes a method, not just evaluation. Clearly stronger. |
| Modular Agentic Planner (MAP) | 4.50 | R1 | MAP has better ablations; our paper has more dramatic results. Similar tier. |
| Prefrontal Cortex-inspired Architecture | 5.25 | R2 | Both cognitive-inspired LLM planning. Our paper uses PlanBench (stronger benchmark) but has similar ablation gaps. Our paper is comparable or slightly weaker. |
| Tree-Planner | 5.25 | R2 | Better methodology (proper ablations). Our paper has more dramatic result but weaker experimental design. Our paper is slightly weaker. |
| LLMs Can Plan Only If We Tell Them (AoT+) | 6.40 | R1/R2 | Multi-domain, proper ablations, attention analysis. Clearly stronger methodology. Our paper is below this. |

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>
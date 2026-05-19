## Summary
# Final Review Report

## Summary

This paper introduces EconArena, a simulation platform that uses competitive economic games — beauty contests and second-price auctions — to evaluate large language models (LLMs) on three dimensions: rationality (proximity to Nash equilibrium), strategic reasoning (ability to improve with game history), and instruction-following (rule-breaking frequency). The study tests 9 LLMs (GPT4, GPT3.5, Claude2, Claude-Instant, PaLM2, Llama2, Baichuan2, ChatGLM2, ChatGLM3) across multiple environments (melee, rational, senior) and conditions (with/without history, varying game configuration).

**Core strengths:** The paper tackles a genuinely important problem — the need for dynamic, multi-agent evaluation of LLMs beyond static benchmarks. The game-theoretic grounding (unique pure NE) provides objective, quantitative metrics for rationality. The breadth of models tested (9 across proprietary and open-source families) is commendable. The rule-breaking analysis adds a practical dimension to evaluation.

**Core weaknesses:** The experimental methodology has several unaddressed confounds: unknown decoding parameters (temperature/sampling) across API-based models, lack of statistical significance testing for model rankings, and post-hoc causal speculation about observed patterns. Formal metric definitions are deferred to the appendix rather than presented in the main text. The contributions are stated with vague phrasing ("certain models") that reduces scientific precision. The conclusion lacks limitation awareness and future directions.

**Novelty note:** External literature verification is unavailable in this run (Retrieval-Disabled Mode). Novelty/comparison conclusions are intentionally deferred for manual verification. However, the core idea — using NE-deviation metrics from competitive games as an LLM evaluation framework — appears to have reasonable differentiation from prior work on LLMs in cooperative games and static benchmarks. This should be confirmed with targeted literature review.

## Strengths
1. **Timely and important problem.** The paper addresses a genuine limitation of current LLM evaluation — the static nature of most benchmarks cannot measure adaptive, multi-agent behavior. Proposing competitive games as a dynamic evaluation environment is well-motivated and practically relevant for the LLM agent community.

2. **Game-theoretic grounding.** Using games with unique pure Nash equilibria provides objective, quantitative metrics (deviation distance, payoff ratio) that are interpretable and comparable across models. This is a principled improvement over ad-hoc evaluation protocols.

3. **Broad model coverage.** The study spans 9 LLMs across proprietary (GPT4, GPT3.5, Claude2, Claude-Instant, PaLM2) and open-source families (Llama2, Baichuan2, ChatGLM2, ChatGLM3), enabling comparative analysis that is useful for practitioners.

4. **Multi-dimensional evaluation.** The paper evaluates three distinct capabilities — rationality, strategic reasoning (via history), and instruction-following (via rule-breaking) — within a single framework. This multi-faceted approach is more informative than any single metric.

5. **Open-source platform contribution.** The authors commit to releasing EconArena as a publicly available simulation package, which could serve as a useful community resource for standardized LLM evaluation in dynamic settings.

6. **Interesting empirical patterns.** Several findings are non-obvious and potentially valuable: the non-monotonic relationship between payoff changes and strategy space size (Claude2 vs GPT3.5 in varying configurations), the finding that history can hurt auction performance, and the high variance in instruction-following across models.

## Weaknesses
1. **Lack of statistical rigor in model comparisons.** The paper ranks LLMs by rationality (deviation distance) and payoff without reporting confidence intervals, standard deviations, or significance tests. Differences between top models (e.g., GPT4 vs Claude2 vs GPT3.5) could be within noise range. For a benchmark paper that positions itself as an evaluation tool, this is a major gap.

2. **Uncontrolled decoding parameters.** The authors explicitly admit uncertainty about whether LLM responses are sampled or greedily decoded, and no temperature/sampling parameters are reported. This confound can substantially affect output variance and bias rationality comparisons. Without reporting or controlling these settings, experimental results are not fully reproducible.

3. **Post-hoc causal speculation.** Several interpretations attribute observed patterns to model "sophistication" (e.g., GPT4's slower convergence explained as "already rationalizing about opponents") without supporting evidence. Other plausible explanations (e.g., lower context sensitivity, different output distributions) are not considered.

4. **Core metric definitions deferred to appendix.** The formal definitions of the key metrics (rationality ratio $r_i$, deviation distance $d$, strategic reasoning ratio) appear only in Appendix A.3, not in the main text. This forces readers to cross-reference to understand the evaluation methodology.

5. **Vague contribution language.** The contribution list in the introduction uses "certain models" four times without naming which models perform which tasks. This weakens the paper's scientific precision and impact.

6. **Defective figure rendering.** Several figures contain Unicode corruption artifacts (`/uni000000...` sequences) that render axis labels and legends unreadable. Figure 5 (convergence paths) particularly suffers from this, making its interpretation unreliable.

7. **Speculative causal explanation without controls.** The "spillover" explanation for GPT3.5's declining payoffs in larger strategy spaces is presented as a causal mechanism without any supporting ablation or control experiment.

8. **Conclusion lacks closure.** The conclusion is only 5 sentences, does not mention the open-source platform, does not acknowledge limitations (which are relegated to Appendix C), and proposes no future work directions.

9. **Limited game variety in main evaluation.** Only two game types (beauty contests and second-price auctions) are tested in the main text. While additional game types are mentioned as future work, the current scope limits generalizability claims.

10. **Unclear payoff scale interpretation.** Table 1 reports payoff values without explaining what constitutes a "good" payoff (e.g., 0.0 vs 1.0 vs 0.45). Readers cannot interpret the practical significance of reported differences without this context.

## Key Issues
### Issue 1 (Critical): Uncontrolled Sampling/Decoding Parameters
**Severity:** Critical | **Validity Risk:** High | **Fixability:** High

The authors state they are "not certain whether the responses to the given prompts are sampled out or greedily searched out from LLMs service provides" (Page 4, Experiment Results). This is a fundamental reproducibility gap. If GPT4 uses greedy decoding (temperature=0) and GPT3.5 uses sampling (temperature=0.7), their rationality differences could be artifacts of output stochasticity rather than genuine capability differences. **Required:** Report exact decoding parameters for each model; add temperature ablation for at least one model.

### Issue 2 (Major): Missing Statistical Significance
**Severity:** Major | **Validity Risk:** High | **Fixability:** High

Model rationality rankings are based on mean payoff and deviation distances without confidence intervals, standard errors, or significance tests (Figures 1-4, Table 1). Reported differences between GPT4, Claude2, and GPT3.5 could be within noise. **Required:** Add mean±std, report pairwise significance tests (Mann-Whitney U), and adjust claims if differences are not significant.

### Issue 3 (Major): Post-hoc Causal Speculation
**Severity:** Major | **Validity Risk:** Medium | **Fixability:** High

The paper attributes GPT4's slower convergence to it "being sufficiently sophisticated, has already been rationalizing about opponents" (Page 7, Section 4.3) without supporting evidence. The "spillover" explanation for GPT3.5's payoff decline (Page 6) is similarly unsupported. **Required:** Replace causal claims with evidence-consistent descriptions; add clear operational definitions for convergence.

### Issue 4 (See Weaknesses section for additional issues 4-10 — Core metric definitions in appendix, vague contribution language, figure rendering, restrictive conclusion, game variety, and payoff scale interpretation.)

## Actionable Suggestions
### S1 (Must): Report and control decoding parameters
**Location:** Page 4 - Experiment Results
Add a sub-table reporting temperature, top_p, max_tokens, and sampling strategy for each of the 9 LLMs. If certain APIs do not expose these parameters, state this explicitly and discuss implications. Then conduct an ablation experiment on at least GPT3.5 comparing temperature=0 (greedy) vs temperature=0.7 to quantify the effect of stochasticity on deviation distance and payoff variance.

### S2 (Must): Add statistical significance testing to all model comparisons
**Location:** Pages 5-8, Figures 1-4, Table 1
Report mean ± standard deviation for all payoff and deviation distance values. Run pairwise Mann-Whitney U tests between models (at least between GPT4, Claude2, GPT3.5). If differences are not significant, combine models into performance tiers rather than ranking individually. Add bootstrapped 95% confidence intervals to the payoff curves in Figure 3.

### S3 (Must): Remove or soften post-hoc causal speculation
**Location:** Page 6 (Section 4.2 spillover), Page 7 (Section 4.3 GPT4 sophistication)
Replace causal interpretations with descriptive statements. For the "spillover" claim: "The observed pattern shows Claude2's payoffs increasing and GPT3.5's decreasing across L→M→H. The mechanism behind this divergence is unclear and may involve model-specific sensitivity to numerical range, rather than a strategic spillover effect." For GPT4's sophistication: An appropriate replacement is "GPT4 improves less from history than GPT3.5 and Baichuan2, possibly because its baseline policy is already closer to NE, reducing the marginal benefit of additional context."

### S4 (Must): Move core metric definitions to main text
**Location:** Page 4 - Section 3.2
Move Equations (1)-(3) (rationality ratio, deviation distance) from Appendix A.3 into the main text. Ensure the beauty contest fraction example formats correctly as 2/3 and 16/3 rather than "2 3" and "16 3".

### S5 (Must): Replace vague contribution language with model names
**Location:** Page 2 - Introduction contribution list
Replace each instance of "certain LLMs" with the specific model names that support each claim, based on the experimental results. This is critical for scientific precision.

### S6 (Must): Expand conclusion
**Location:** Page 9 - Section 5
Restructure into three parts: (a) validated findings with specific model names, (b) at least 2 explicit limitations (unknown decoding parameters, limited game types), (c) 1-2 concrete future directions. Mention the EconArena platform availability.

### S7 (Nice-to-have): Fix figure rendering
**Location:** Pages 5-8, Figures 1-6
Replace Unicode-corrupted figure labels with readable text. Ensure axis labels, legends, and numerical annotations render correctly in the PDF.

### S8 (Nice-to-have): Explain payoff scale
**Location:** Page 7 - Table 1
Add a sentence or footnote explaining the payoff scale: what values 0.0, 1.0, and negative values mean in terms of game outcomes relative to Nash equilibrium.

## Storyline Options + Writing Outlines
### Abstract Outline (Complete)

The abstract should follow a tight 5-sentence structure that is self-contained:

**S1 — Problem & Domain:** "Evaluating large language models (LLMs) on static benchmarks does not capture their ability to behave rationally and adapt strategically in dynamic multi-agent environments."
*Role: Establish the problem and why it matters.*

**S2 — Gap & Motivation:** "Competitive economic games with known Nash equilibria (NE) provide objective quantitative metrics for evaluating these abilities, but existing LLM game-playing studies focus primarily on cooperative settings without NE-grounded metrics."
*Role: Identify the gap in prior work that this paper fills.*

**S3 — Method/Platform:** "We introduce EconArena, a simulation platform that uses beauty contests and second-price auctions to measure LLM rationality (via NE deviation distance), strategic reasoning (via payoff improvement with game history), and instruction-following (via rule-breaking frequency)."
*Role: State what was built and what it measures.*

**S4 — Key Results (with numbers):** "Testing 9 LLMs (GPT4, GPT3.5, Claude2, Claude-Instant, PaLM2, Llama2, Baichuan2, ChatGLM2, ChatGLM3) across 150+ sessions, we find that all models exhibit bounded rationality — GPT4 and Claude2 have the lowest mean NE deviation (0.12–0.14), while GPT3.5 achieves the highest win rates with history. Rule-breaking ranges from 0% (GPT4) to 100% (ChatGLM2), revealing large differences in instruction-following."
*Role: Present the most important empirical findings with concrete numbers.*

**S5 — Implication & Availability:** "EconArena is publicly available to serve as a standardized dynamic evaluation tool for the LLM agent community, complementing static benchmarks with behavioral metrics grounded in game theory."
*Role: State the broader impact and bounded claim.*

### Introduction Outline (Complete)

**P1 — Big Picture & Problem Stakes** *(currently generic DL intro)*
*Role: Open with the evaluation problem for LLM agents.*
*Target claim: LLM agents need evaluation methods that go beyond static benchmarks to measure adaptive behavior.*
*Transition to P2: Identify the specific capability gap — rationality and strategic reasoning in competitive settings cannot be measured by existing benchmarks.*

**P2 — Existing Work & Precise Gap** *(currently mixes economics games with method)*
*Role: Review existing LLM game-playing work and identify the gap.*
*Target claim: Prior work applies LLMs to cooperative or two-player games without quantitative NE-based metrics, and without measuring strategic reasoning through competitive interaction.*
*Transition to P3: State that this paper fills the gap with competitive games that have unique pure NE.*

**P3 — Proposed Approach & Core Idea** *(currently split across P2 and contribution list)*
*Role: Present the EconArena design and the core metric idea.*
*Target claim: By using games with unique pure NE (beauty contests and second-price auctions), we can compute deviation distance and payoff ratio as quantitative measures of rationality. By varying history and opponent types, we measure strategic reasoning.*
*Transition to P4: Preview the key results.*

**P4 — Key Results & Contribution List** *(currently uses "certain models" vaguely)*
*Role: Present 4 explicit findings with model names.*
*Target claim: GPT4 and Claude2 are most rational (lowest NE deviation); GPT3.5 has strongest combined rationality+reasoning (highest melee/senior payoffs); GPT4 converges fastest with history; rule-breaking differentiates instruction-following.*
*Transition to paper body: "We now describe the EconArena framework in detail."*

### Recommended Title Change

Current: "ECONOMICS ARENA FOR LARGE LANGUAGE MODELS"
Suggested: "EconArena: Evaluating LLM Rationality and Strategic Reasoning through Competitive Economic Games"
*Rationale: Adds specificity about what is evaluated (rationality, strategic reasoning) and how (competitive economic games). The current title only names the platform without communicating the research question or contributions.*

## Priority Revision Plan
```text
ASCII Diagram — Revision Strategy Roadmap

[P0: Fix reproducibility & statistical rigor]
   ├─ (1) Report decoding parameters for all 9 models
   ├─ (2) Add temperature ablation (GPT3.5: temp=0 vs 0.7)
   └─ (3) Add mean±std + significance tests for all rankings
   → Expected gain: Experimental results become reproducible and rankings become defensible

[P1: Clean up causal claims & metric definitions]
   ├─ (4) Remove/correct spillover and sophistication speculation
   ├─ (5) Move metric formulas (Eq. 1-3) from appendix to main text
   └─ (6) Fix fraction rendering (2/3, 16/3) in beauty contest example
   → Expected gain: Scientific precision and reader comprehension

[P2: Strengthen conclusion & presentation]
   ├─ (7) Expand conclusion with limitations, future work, platform URL
   ├─ (8) Replace vague "certain models" with model names in intro
   ├─ (9) Fix figure rendering (Unicode artifacts)
   └─ (10) Explain payoff scale in Table 1
   → Expected gain: Complete, polished manuscript ready for review
```

### Priority Matrix

| Priority | Low Effort | Medium Effort | High Effort |
|---|---|---|---|
| High Impact | S3 (soften speculation), S5 (model names), S6 (conclusion) | S2 (add significance tests to existing data) | S1 (decoding parameter control + temperature ablation experiment) |
| Medium Impact | S4 (move formulas), S8 (payoff scale) | S7 (fix figure rendering) | — |

**P0 items (Must, pre-submission critical):**
1. Report decoding parameters for each model (Page 4)
2. Add temperature=0 vs temperature=0.7 ablation for GPT3.5 (new experiment)
3. Add mean±std and significance tests to all model comparisons (Pages 5-8)
4. Remove post-hoc causal speculation (Pages 6-7)

**P1 items (Must, for revised submission):**
5. Move metric definitions to main text (Page 4, Section 3.2)
6. Replace vague "certain models" with specific names (Page 2)
7. Expand conclusion (Page 9)

**P2 items (Nice-to-have):**
8. Fix figure rendering (Pages 5-8)
9. Explain payoff scale (Page 7, Table 1)
10. Title revision to include problem + method + evaluation scope

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|---|---|---|---|---|---|---|
| E1 | Test LLM rationality in melee (no history) | 9 LLMs, beauty contests + auctions, 150 sessions | Mean payoff | GPT3.5 highest payoff in beauty contests; ChatGLM3 highest in auctions | C1 (LLMs are partially rational) | No significance tests; no variance reporting |
| E2 | Test rationality in rational environment | Single LLM vs 4 hard-coded rational agents | Deviation distance from NE | Claude2 and GPT4 lowest deviation in beauty contests; most models near-NE in auctions | C1 (no model is maximally rational) | Unknown decoding parameters confound comparison |
| E3 | Test adaptation to game configuration | 3 groups (L, M, H) varying strategy space/private values | Average payoff | Claude2 improves and GPT3.5 declines with larger space in beauty contests | C2 (LLMs adapt to dynamic environments) | "Spillover" explanation is speculative; no confidence intervals |
| E4 | Test adaptation to opponent types | Senior environment (5 strong LLMs), 20/60/100 sessions | Average payoff | GPT3.5 stable across sessions; Claude2 variable | C2 | No variance data; unclear payoff scale |
| E5 | Test strategic reasoning with history (rational environment) | Max 3 runs history, 6 runs/session | Deviation distance, convergence path | GPT4 lowest deviation; GPT3.5 fastest convergence in beauty contests | C3 (certain LLMs show stronger reasoning) | Post-hoc "sophistication" speculation; no quantitative convergence metric |
| E6 | Test strategic reasoning with history (melee) | Full LLM pool with history | Average payoff | GPT3.5 highest payoffs with history | C3 | Rule violations reduce sample size for auctions |
| E7 | Instruction-following (rule-breaking) | Track format violations across all experiments | Rule-breaking % | Llama2 80-90% violations; GPT4/Claude2 0% in beauty contests | C4 (rule-breaking reflects instruction-following) | Conflates format errors with rule comprehension errors |

### Research-Theme Gap Diagnosis

1. **New knowledge value — Medium.** The paper provides a novel evaluation framework, but the empirical findings are largely correlational and descriptive rather than mechanistic. We learn *that* certain LLMs deviate less from NE, but not *why* — is it training data, architecture, RLHF, or decoding strategy? The paper does not attempt to attribute causes.
2. **Reproducibility/reusability — Weak.** The uncontrolled decoding parameters and missing significance tests make it difficult for other researchers to reproduce the exact experimental conditions. The platform availability is a positive step, but without API parameter documentation, exact replication is not feasible.
3. **Impact on practice/understanding — Moderate.** The framework could influence how the community evaluates LLM agents, but the paper needs stronger evidence of validity (e.g., correlation with human performance, or with other reasoning benchmarks) before practitioners adopt it.

### Proposed Research Experiments (P0/P1/P2)

**Exp P0-A: Temperature Ablation (P0)**
- *Target Claim:* C1 (rationality ranking is robust to decoding strategy)
- *Hypothesis:* GPT3.5's rationality ranking is consistent under temperature=0 vs temperature=0.7
- *Minimal Design:* Run GPT3.5 in rational environment beauty contests under temp=0 (greedy) and temp=0.7, 50 sessions each
- *Controls/Baselines:* Same prompt, same session count, same opponent scripts
- *Metrics:* Mean deviation distance, variance across sessions
- *Success Criterion:* If deviation distances differ by <0.05, ranking is robust; if >0.10, decoding confound is confirmed
- *Estimated Cost/Time:* Low (API calls for 2 models × 50 sessions)
- *Expected Gain:* High — resolves the most critical reproducibility concern

**Exp P0-B: Statistical Significance Package (P0)**
- *Target Claim:* All model rankings
- *Minimal Design:* Recompute all reported means with ±std, run Mann-Whitney U tests between model pairs
- *Expected Gain:* High — makes rankings scientifically defensible

**Exp P1-A: Convergence Rate Quantification (P1)**
- *Target Claim:* C3 (convergence speed)
- *Minimal Design:* Define convergence as first run where |deviation| < 0.1 × baseline deviation, count runs to convergence for each model
- *Expected Gain:* Medium — replaces qualitative convergence description with quantitative metric

**Exp P2-A: Cooperative Game Extension (P2)**
- *Target Claim:* Generalizability of evaluation framework
- *Minimal Design:* Add one cooperative game (e.g., public goods game) to EconArena, test top-3 LLMs
- *Expected Gain:* Medium — demonstrates framework generality beyond competitive games

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score: 5.5 / 10**

*Score rationale: The paper addresses an important problem (dynamic LLM evaluation) with a principled game-theoretic approach and broad model coverage. However, the experimental methodology has significant gaps — uncontrolled decoding parameters, missing statistical tests, post-hoc causal speculation, and key metric definitions deferred to the appendix — that reduce confidence in the reported model rankings. The scientific precision of the contribution claims is weakened by vague language. The research value (new evaluation framework) is promising, but the current evidence is insufficient to fully support the claimed differentiation between models. The score prioritizes research value (moderate) and methodological rigor (needs improvement).*

**Post-Revision Target: [6.5, 7.5] / 10**

*If the authors complete all P0 items (decoding parameter reporting, temperature ablation, significance testing, removal of speculation) and P1 items (metric definitions in main text, specific model names in contributions, expanded conclusion), the paper would provide a reproducible, statistically grounded evaluation framework. The post-revision target reflects the ceiling imposed by the limited game variety (2 games) and the inherent API opacity of proprietary models, which P0/P1 fixes can substantially improve but not fully eliminate.*

### Summary of Scores by Dimension

| Dimension | Score (0-10) | Weight | Rationale |
|---|---|---|---|
| Research Value / Contribution | 6.5 | 30% | Novel evaluation framework with game-theoretic grounding; platform contribution is useful. Limited by only 2 game types and descriptive rather than mechanistic findings. |
| Validity / Soundness | 4.5 | 25% | Undermined by uncontrolled decoding parameters, missing significance tests, and post-hoc speculation. The core metric design is sound but the experimental execution has gaps. |
| Novelty | 5.0 | 20% | Reasonable differentiation from prior LLM game studies but external literature verification is deferred. The combination of competitive games + NE metrics + history-based reasoning appears novel in scope. |
| Reproducibility | 3.5 | 15% | Low — unknown API parameters, missing variance data, and figure rendering issues prevent independent replication. |
| Presentation / Clarity | 5.5 | 10% | Well-structured abstract and introduction (though vague). Key weaknesses: metric definitions in appendix, corrupted figures, and terse conclusion. |
Here is the final consolidated review:

## Summary

This paper introduces TMK (Task-Method-Knowledge) prompting, a structured prompting approach adapted from cognitive science, for improving LLM performance on planning tasks. Evaluated on PlanBench Blocksworld (Classic, Mystery, Random variants), the method shows notable gains, most strikingly with o1 improving from 31.5% to 97.3% on Random Blocksworld. The paper argues that TMK acts as a symbolic scaffold that steers models toward code-like reasoning pathways.

## Strengths

1. **Dramatic performance inversion for o1 on Random Blocksworld (Table 2).** The o1 model jumps from 31.5% to 97.3% on opaque symbolic tasks under TMK prompting — a 65.8 percentage point gain that far surpasses prior reported results on this variant. The difficulty ordering flips (Random 97.33% > Mystery 83.3%), which concretely indicates TMK is doing more than just adding context.

2. **Systematic three-variant experimental design (Table 1, Table 2).** The paper evaluates TMK across Classic, Mystery, and Random Blocksworld, which systematically strip away semantic cues. This provides a controlled test of whether TMK steers models away from linguistic pattern-matching — more informative than a single-domain evaluation.

3. **Explicitly addresses three documented criticisms of prior prompting-for-planning work (Section 5.1).** The paper identifies and shows how its methodology sidesteps criticisms about (i) n-shot pattern matching, (ii) CoT contradicting final answers, and (iii) lack of cross-model generality. It demonstrates one-shot plain text performs worse than zero-shot (so the example itself is not driving gains) and evaluates entire plans not just final answers.

## Weaknesses

### Major

1. **The performance inversion / symbolic-steering claim primarily rests on a single model (o1).** The paper's central mechanistic interpretation — that TMK "shifts the model's inference strategy away from linguistic approximation and toward formal symbolic manipulation" (Section 4.2) — is built on the o1 performance pattern. However, the full data in Table 2 tells a more complex story: o1-mini shows the *opposite* pattern (Mystery drops from 19.1% to 16.83% under TMK), GPT-4 and GPT-4o show floor effects (0% to ~4-5%), and GPT-5 shows ceiling effects (92.5-99.7% throughout). The inversion claim is essentially o1's story alone, and the paper's explanation for o1-mini's divergence ("capacity limitations," Section 4.2) is post-hoc speculation rather than evidence. This weakens the generality of the claimed mechanism.

2. **The causal explanatory claim outruns the behavioral evidence.** The abstract asserts that TMK "steers reasoning models away from their default linguistic modes to engage formal, code-execution pathways," and Section 5.2.1 develops a detailed mechanistic story about "steering between code execution and textual reasoning." The paper presents no observations of internal model states, reasoning traces, token-level patterns, or any other evidence that would distinguish code-execution pathways from linguistic ones. The behavioral evidence (accuracy on Blocksworld) is consistent with several alternative explanations — e.g., TMK simply provides more detailed domain knowledge in a well-structured format; the JSON format reduces ambiguity about what to output; the extraction leniency benefits Random more than Mystery. The mechanistic claim is asserted much more strongly than the evidence supports.

### Minor

3. **Ambiguous symmetry of the enhanced extraction function (Section 3.2).** The paper states that an enhanced extraction function "was applied for random blocksworld data set" to handle formatting variations, symbol insertions, and paraphrasing. It does not explicitly state whether this same lenient extraction was applied to both the TMK and plain-text baseline conditions. For models whose plain-text baselines were extracted from Valmeekam (2023), the original stricter validator may have been used. If the two conditions used different extraction strictness, the comparison is not fully controlled. This is a clarity issue that undermines confidence in the headline comparison.

4. **No measure of variance or statistical reliability (Table 2).** All results are reported as single percentage values with no indication of how many runs were performed, no error bars, no confidence intervals, and no discussion of stochasticity. LLM evaluation on planning benchmarks is sensitive to sampling temperature and random seed. The paper's central claims rest on specific numbers (31.5% → 97.3% for o1 on Random) without any indication of whether these represent a single pass or the mean of multiple trials.

### Trivial

None.

## Nice-to-Haves

- **Ablation of TMK components:** Is it the "Task" part, the "Method" part, the "Knowledge" part, or the JSON structure itself that drives improvements? A structural control (e.g., same JSON with irrelevant content) would test whether structure alone suffices.
- **Comparison with alternative structured prompts:** How does TMK compare to providing the same domain knowledge as a PDDL definition, a Python class, or a numbered list?
- **Qualitative analysis of outputs:** Do TMK-prompted outputs actually differ in structure from plain-text outputs?
- **Testing on non-OpenAI model families:** Establishing the effect is not specific to OpenAI's training distribution.
- **Computational cost analysis:** For o1-like models, does TMK affect the number of reasoning tokens or inference cost?

## Removed Points

These points from the harsh critic are removed with brief justifications:

1. "One-shot vs zero-shot confound" — The paper explicitly addresses this at length in Section 3.2 with three reasons, including the observation that one-shot plain text *underperforms* zero-shot. Deferring details to the OSF link is standard practice for papers with extensive result files. The confound is unlikely to threaten the conclusions.

2. "GPT-4 and GPT-4o plain-text scores on Mystery and Random (0% and 0.83%) are dramatically lower than any other model" — This is the reported data, not a flaw. The critic offers no evidence of evaluation pipeline differences.

3. "o1-preview row uses different extraction function / is not comparable" — The paper explicitly marks this with an asterisk and states "Results extracted from Valmeekam (2023)." This is transparent reporting, not a flaw.

4. "NA for o1-preview TMK is unexplained" — The table caption explains: "o1Preview has been deprecated and replaced by o1." This is sufficient.

5. "No discussion of limitations about extraction function or one-shot/zero-shot" — The Limitations section (5.3) is brief, but these issues are discussed at appropriate length elsewhere in the paper (Section 3.2).

6. Various formatting/style nitpicks — Removed per filtering rules (parser artifacts, not author errors).

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a novel framing or interpretation that the paper itself is missing.

## Suggestions

1. Clarify in the main text whether the enhanced extraction function was applied symmetrically to both TMK and plain-text baseline conditions. This single transparency fix would substantially increase confidence in the headline results.

2. Tone down the mechanistic claims (code-execution steering, symbolic manipulation) to match the behavioral nature of the evidence. The performance inversion for o1 is interesting on its own without needing a strong causal story about internal model pathways.

3. Add even basic variance information: report whether the numbers in Table 2 are from a single run or averaged across multiple runs, and if possible report results across 2-3 seeds for at least one key model to demonstrate stability.

4. Add a structural control experiment. A simple control — replacing TMK content with a similarly structured JSON describing an unrelated domain — would test whether the TMK structure alone suffices versus content + structure.

## Score and Decision

**Calibration anchors retrieved across rounds:**

*Round 1 — Bracketing (query: "LLM prompting planning blocksworld PlanBench"):*

| Path | Avg Score | Round | Comparison to TMK |
|------|-----------|-------|-------------------|
| kOZa5fePTs | 2.00 (Reject) | 1 | Exploring/benchmarking planning; much weaker contribution |
| cWrqs2lwCJ | 3.00 (Reject) | 1 | Backward planning; weaker results, no novel method |
| jOuHjFw71C | 3.00 (Reject) | 1 | o1 evaluation on PlanBench; limited contribution, TMK stronger |
| BW8O4wHgbo | 3.00 (Reject) | 1 | MAPF with LLMs; negative result paper |
| K3KrOsR6y9 | 6.40 (Accept) | 1 | AoT+ structured prompting; most similar. TMK more novel but less rigorous |
| NUD03NBDOE | 6.75 (Accept) | 1 | Action reasoning benchmark; different paper type |
| OPdmIxdkPb | 4.75 (Reject) | 1 | Query-efficient planning; TMK stronger |
| DZBFchnM3b | 3.67 (Reject) | 1 | Search problem benchmark; TMK stronger |
| Q6a9W6kzv5 | 8.00 (Accept) | 1 | Physics benchmark (VLM); different domain |
| OI3RoHoWAN | 8.00 (Accept) | 1 | Robotic simulation; different domain |
| DzGe40glxs | 8.00 (Accept) | 1 | Interpretability; different domain |

*Round 2 — Narrowing:*

Query 1 ("structured prompting LLM planning reasoning blocksworld PlanBench", 4.0–6.0):

| Path | Avg Score | Round | Comparison to TMK |
|------|-----------|-------|-------------------|
| BaMkS6E2Du | 5.50 (Reject) | 2 | SWAP structure-aware planning; TMK more novel |
| iNcEChuYXD | 4.50 (Reject) | 2 | MAP modular planner; TMK clearly stronger |
| 3UWuFoksGb | 5.50 (Accept) | 2 | Learning planning abstractions; different approach, similar score |
| UiLtbLsiPU | 4.50 (Reject) | 2 | Embodied task planning benchmark; different domain |

Query 2 ("LLM prompt engineering planning task decomposition cognitive", 5.5–7.5):

| Path | Avg Score | Round | Comparison to TMK |
|------|-----------|-------|-------------------|
| K3KrOsR6y9 | 6.40 (Accept) | 2 | AoT+ (same as above), TMK slightly weaker on rigor |
| qJ0Cfj4Ex9 | 6.20 (Accept) | 2 | Grounded action abstractions; TMK more directly applicable |
| EqcLAU6gyU | 5.60 (Accept) | 2 | Multi-agent planning; different focus |
| 22pyNMuIoa | 5.75 (Accept) | 2 | PromptAgent prompt optimization; different focus |

**Round 1 bracket:** 4.5–6.0 (above MAP at 4.50, below or comparable to AoT+ at 6.40).

**Narrowing reasoning:** The most directly comparable anchor is AoT+ (6.40, Accept), a structured prompting method for Blocksworld. TMK has a more novel approach (TMK from cognitive science is genuinely different from CoT/ToT/AoT variants) and more striking headline results (65.8pp gain vs. incremental improvements). However, TMK's evaluation is less rigorous: only one domain (Blocksworld), only OpenAI models, no ablation studies, ambiguous extraction function, no variance measures. Given these tradeoffs, TMK sits slightly below AoT+.

**Final score and decision:** The paper has a genuinely novel contribution with striking empirical results. The weaknesses (overclaimed mechanistic interpretation, limited evaluation scope, missing variance/ablation) are real but not fatal. This is a borderline Accept.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>
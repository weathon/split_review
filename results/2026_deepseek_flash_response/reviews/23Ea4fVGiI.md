Now I have a thorough understanding of the paper and the calibration landscape. Let me produce the final review.

## Summary

This paper proposes using the TMK (Task-Method-Knowledge) framework — a structured knowledge representation from cognitive science — as a replacement for the plain-text domain description in LLM prompts for planning tasks. The authors evaluate on PlanBench Blocksworld across multiple OpenAI models (GPT-4, GPT-4o, o1-mini, o1, GPT-5) and three domain variants (Classic, Mystery, Random). The headline result is o1 on Random Blocksworld improving from 31.5% (plain text) to 97.33% (TMK). The paper argues TMK functions as a "symbolic scaffold" that steers models toward code-execution-like reasoning pathways.

## Strengths

- **Performance inversion as evidence of a non-trivial effect**: The o1 Random result (31.5% → 97.33%) is genuinely striking, and the inversion where Random surpasses Mystery accuracy under TMK is a non-uniform pattern that goes beyond what generic context addition would produce (Table 2, Section 4.2). This is the paper's strongest empirical signal.

- **Good experimental precautions against pattern-matching confounds**: The paper explicitly addresses criticisms of prior prompting-for-planning work (Section 5.1) by using a random, non-matched one-shot example, verifying that zero-shot plain text outperforms one-shot plain text in PlanBench (so the example itself is not driving gains), and evaluating full-plan correctness via PDDL validation rather than answer-only matching. These design choices separate TMK's effect from the exemplar-matching confound.

- **Honest reporting of a counterexample**: The o1-mini model shows a decrease on Mystery Blocksworld under TMK (19.1% → 16.83%, Table 2). Rather than excluding this, the paper flags it and proposes a specific hypothesis (capacity limitations causing "semantic overload"). This transparency strengthens credibility.

## Weaknesses

### Major

- **Plain-text baselines are not rerun under matched conditions for all models, confounding the core comparison**: For GPT-4, GPT-4o, o1-mini, and o1preview, the plain-text accuracy numbers are taken from the public PlanBench leaderboard (Valmeekam, 2023) rather than rerun under identical conditions. This means the following are uncontrolled between the two columns: API version/model checkpoint, decoding parameters (temperature, top-p), problem selection, date of evaluation, and the evaluation pipeline itself (the paper states they added new extraction criteria for Random Blocksworld that differ from the leaderboard's criteria). For the smaller improvements (e.g., GPT-4 Classic 34.6%→39.7%, GPT-4o Random 0.83%→4.83%, GPT-4 Mystery 0%→3.8%), any of these uncontrolled factors could produce differences of the reported magnitude. The one genuinely impressive result (o1 Random: 31.5%→97.33%) may well be real, but the paper provides no way to distinguish a TMK effect from an API-version or decoding-parameter effect because the baseline was not rerun. The paper acknowledges this design choice (Section 3.2) and argues it is "conservative" (comparing against the higher of zero/one-shot), but this does not address the uncontrolled confounds. This is structural: the paper's central empirical comparison is not a controlled experiment.

- **No variance, trial counts, or statistical support**: The paper reports a single accuracy percentage per condition with no mention of how many problems were used per Blocksworld variant, how many independent runs were performed, or any confidence intervals or standard deviations. Many reported improvements are small in absolute terms (0–10pp), and since the models are stochastic, a single run could easily produce numbers differing by this much from random seed variation alone. Without multiple trials or any measure of variance, these numbers cannot be evaluated as evidence. This is a basic standard for empirical ML/planning research.

- **Central mechanistic claim is asserted beyond what the data supports**: The abstract states that TMK functions as "a mechanism that steers reasoning models away from their default linguistic modes to engage formal, code-execution pathways." The paper cannot support this claim with the presented data. The performance inversion (Section 5.2.1) is argued as "empirical validation" of this steering effect, but it is equally consistent with simpler explanations (e.g., the JSON structure happens to match the Random domain's opaque string format well, making parsing easier). No evidence about internal model processing is presented — no probing, no attention analysis, no comparison of reasoning tokens, no ablation comparing TMK to other structured formats (YAML, different JSON schemas). The "code-execution pathways" hypothesis is acknowledged as speculative in parts of Section 5.2.1, but the abstract and conclusions present it as a finding. This disconnect between the evidence and the framing is a significant overclaim.

### Minor

- **Only one planning domain tested**: The paper evaluates only Blocksworld. The limitations section acknowledges this (Section 5.3), but given that the paper's central claim is about a general mechanism ("symbolic steering"), testing on a single domain is insufficient. Many prompting techniques that work on Blocksworld do not transfer to other planning domains (e.g., Logistics, Sokoban). This limits the paper's contribution to a domain-specific finding.

- **No ablation isolating TMK structure from information content**: The paper claims the improvement comes from TMK's structure (JSON-like syntax activating code-execution pathways). But since the plain-text prompt's exact content is in the stripped appendix and cannot be verified, it is unclear whether TMK provides equivalent or greater information. Even if information is equivalent, an ablation comparing TMK-format to the same preconditions/effects written in well-structured natural language would be needed to support the structural claim. Without this, the mechanism is untestable with the presented data.

- **Mechanistic speculation in Section 5.2.2 is not clearly labeled**: The discussion invoking Bloom's taxonomy, cognitive load theory, and the worked example effect is interesting but entirely theoretical and untested. It is presented as part of the paper's explanatory framework rather than clearly demarcated as speculation.

## Nice-to-Haves

- Rerun plain-text baselines under exactly matched conditions (same model version snapshots, same temperature/decoding, same problem instances, same evaluation pipeline) and report variance. This is a prerequisite for the paper's core empirical claim to be interpretable.
- Add an ablation that controls for information content: write the same TMK knowledge (preconditions, effects, ontology) in well-structured natural language (not JSON) and compare.
- Report the problem set size per Blocksworld variant and the number of independent runs.
- Test on at least one additional PlanBench domain (e.g., Logistics) to support generalizability claims.

## Removed Points

These points were removed from the Harsh Critic and Strength Finder with brief justification:

- **Criticism about TMK providing "more information" than plain-text prompt**: The paper states the TMK prompt "replaces the domain portion of the PlanBench prompt" (line 169), suggesting equivalent information content. The critic's concern is based on the stripped appendix that cannot be verified; this is an issue with the parser, not the paper. Demoted from Major to Minor ablation suggestion in the main review.

- **Criticism that results are concentrated in one model-domain combination**: This is a descriptive observation about the pattern of results, not a weakness per se. The paper discusses this pattern. The relevant concern (limited domain) is already covered.

- **"Strengthening the Paper on Its Own Terms" section**: These are suggestions that have been incorporated into "Nice-to-Haves" and Weaknesses where appropriate (rerun baselines, add ablation, add variance).

- **Strength Finder's claim about "performance inversion cannot be explained by generic context addition"**: This is a reasonable observation but overstates what the data show. The inversion is consistent with multiple explanations (formatting convenience, easier parsing, etc.). Kept as a qualified strength but with this caveat.

- **Generic Strength Finder claims**: Claims about "addressing an important problem" or "interesting motivation" removed as too generic/superficial.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Rerun all plain-text baselines under matched conditions** — same model versions, decoding parameters, problem instances, and evaluation pipeline. Without this, the reported improvements are not interpretable as TMK effects.
2. **Report trial counts, problem set sizes, and confidence intervals** for all conditions.
3. **Add an ablation that controls for information content vs. structure** — write the same TMK knowledge as well-structured natural language (no JSON) to test whether the structure or the information drives improvements.
4. **Test on at least one additional PlanBench domain** (e.g., Logistics) to provide initial evidence of generalizability, given the paper's claims about a general mechanism.
5. **Reconcile the framing with the evidence** — scale back the mechanistic claims (abstract, introduction, conclusion) to match what the experiments actually show (performance improvements under TMK prompting, with plausible but untested hypotheses about mechanism).

## Score and Decision

**Calibration Anchors:**

*Round 1 — Bracketing:*
| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| koza5fePTs.md — "Exploring and Benchmarking Planning Capabilities" | 2.00 | R1 | Weaker: our paper has more novelty (new method vs. benchmark) |
| jOuHjFw71C.md — "Planning in Strawberry Fields" | 3.00 | R1 | Somewhat weaker: similar evaluation limitations, but our paper proposes a new method (not just evaluation) |
| sdpVfWOUQA.md — "Planning with MCTS" | 3.00 | R1 | Similar: method paper with some empirical issues, comparable scope |
| cWrqs2lwCJ.md — "Thinking Forward and Backward" | 3.00 | R1 | Similar: method paper on planning, comparable rigor level |
| K3KrOsR6y9.md — "LLMs Can Plan Only If We Tell Them" | 6.40 | R1 | Stronger: proper baselines, ablations, variance reporting, multiple domains |
| NUD03NBDOE.md — "ActionReasoningBench" | 6.75 | R1 | Stronger: well-designed benchmark with rigorous evaluation |
| Q6a9W6kzv5.md — "PhysBench" | 8.00 | R1 | Much stronger, different topic |

*Round 2 — Narrowing:*
| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| 85Ik12q2hP.md — "Do Think Tags Really Help?" | 4.00 | R2 | Slightly stronger: more rigorous experimental design (systematic sensitivity analysis), but less novelty. Our paper has worse experimental control. |
| MK6E6IgROl.md — "ProcBench" | 3.75 | R2 | Similar: benchmark paper with empirical evaluation, comparable overall quality |
| DZBFchnM3b.md — "Navigating the Labyrinth" | 3.67 | R2 | Similar: evaluation/benchmark with some novel aspects, comparable rigor |
| Glcsog6zOe.md — "Tree-Planner" | 5.25 | R2 | Stronger: better experimental design, proper baselines, though only one domain tested |
| 5COCYDObes.md — "Ask more, know better" | 5.00 | R2 | Stronger: more comprehensive evaluation framework |

**Round 1 bracket:** between 3.0 and 6.4, with our paper clearly in the lower half of this range (below "Do Think Tags" at 4.00).

**Round 2 narrowing:** The paper is similar to or slightly weaker than "Do Think Tags Really Help?" (4.00) — that paper had issues with limited novelty but at least had a controlled experimental design. Our paper has more novelty (TMK is new to LLM planning) but significantly worse experimental rigor (uncontrolled baselines, no variance). It is comparable to "ProcBench" (3.75) and "Navigating the Labyrinth" (3.67) in overall quality — papers with interesting aspects but substantive methodological limitations.

**Final score:** 3.5. The o1 Random result is interesting and may reflect a real effect, but the structural experimental flaw (uncontrolled baselines) combined with absent variance information means the paper cannot support its central claims as written. The mechanistic claims are also substantially overclaimed relative to the evidence. The paper would need major revisions (rerunning controlled baselines, adding statistical rigor, and scaling back claims) to be publishable at a top venue.

MY FINAL SCORE: <score>3.5</score>
MY FINAL DECISION: <decision>Reject</decision>
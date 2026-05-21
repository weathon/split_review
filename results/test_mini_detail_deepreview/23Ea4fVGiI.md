Now I have sufficient calibration context. Let me write the final consolidated review.

# Final Review

## Summary

This paper investigates whether prompting with a Task-Method-Knowledge (TMK) framework—a structured knowledge representation borrowed from cognitive science—improves LLM performance on PlanBench Blocksworld planning tasks. The headline finding is that TMK prompting lifts o1 on Random Blocksworld from 31.5% to 97.3%, a 65.8% absolute gain. The paper also reports a "performance inversion" where o1 under TMK performs better on opaque symbolic tasks (Random) than on semantically-cued ones (Mystery), and discusses this as evidence that TMK steers models toward formal, code-execution-like reasoning pathways. Experiments span GPT-4, GPT-4o, o1-mini, o1, and GPT-5 across Classic, Mystery, and Random Blocksworld variants.

## Strengths

- **Large, well-documented accuracy gain on o1 Random Blocksworld (31.5% → 97.3%).** Table 2 provides direct empirical evidence that TMK prompting produces a dramatic improvement on the hardest domain variant for the flagship reasoning model. This is the paper's central empirical finding and is clearly presented.

- **Evidence of a performance inversion pattern.** Section 4.2 and Table 2 show that under plain text, o1 scores higher on Mystery (74.3%) than Random (31.5%), but under TMK this flips (Random 97.33% > Mystery 83.3%). This pattern is more informative than a uniform gain—it suggests TMK changes *which* problems become easy/hard for the model, which is a genuinely interesting phenomenon worth reporting.

- **Explicit methodological safeguards against known LLM-planning criticisms.** Section 5.1 addresses three common criticisms (pattern-matching from n-shot examples, CoT contradicting the final answer, and failure to generalize across domains/models) and explains how the experimental design mitigates each. The one-shot example does not match the problem in length or block descriptions; the entire plan is validated, not just the final answer; and improvements are shown across multiple models and subdomains.

- **Detailed, reproducible TMK structure.** Figure 1 provides a concrete decomposition of the Blocksworld domain into Tasks (goals), Methods (mechanisms), and Knowledge (concepts/relations), making the prompting intervention transparent and reproducible.

## Weaknesses

### Fatal

None.

### Major

- **Ambiguity in the plain-text baseline comparison.** The paper compares TMK (one-shot) against "best of sampled Zero & One shot" plain text (Table 2). The one-shot plain-text numbers for each model and subdomain are not reported in the paper, so the reader cannot verify that the TMK improvement reflects the TMK structure rather than a difference between one-shot and zero-shot prompting. The paper provides reasoning (Section 3.2: zero-shot typically outperforms one-shot on PlanBench, so choosing the higher value is conservative) and references sample testing in an external repository, but this is not a substitute for presenting the one-shot plain-text numbers alongside TMK in the same table. This directly affects the interpretability of the claimed improvements.

- **Modified extraction criteria create potential comparability issues.** The paper states that the original PlanBench extraction code was updated for Random Blocksworld and that an "enhanced extraction function" was used to prevent certain formatting variations from being marked incorrect (Section 3.2). It is not clearly stated whether the *same* enhanced extraction was applied to both TMK outputs and the plain-text baseline outputs, or whether the plain-text baseline numbers were taken from the leaderboard (which used the original, stricter extraction). If the extraction conditions differ, the comparison could be structurally unfair to either condition. This ambiguity needs to be resolved.

- **Mechanistic claims outpace the evidence.** The abstract and introduction state that TMK "functions not merely as context, but also as a mechanism that steers reasoning models away from their default linguistic modes to engage formal, code-execution pathways." The experimental evidence for this claim consists of the performance inversion on o1, which is an interesting but purely observational pattern. The paper does not compare TMK to other structured prompts (e.g., a flat JSON schema without TMK semantics, or an HTN-style prompt), does not analyze model internals, and does not test whether the effect is specific to code-like structure. The mechanism is a plausible hypothesis placed in the discussion (Section 5.2.1), which is appropriate, but the abstract and introduction present it as a finding, creating a gap between framing and evidence. The paper would be stronger if the mechanistic language were restricted to the discussion and framed as a conjecture.

### Minor

- **Single-run evaluation with no variance reporting.** Accuracy numbers in Table 2 are reported as single percentages without confidence intervals, multiple runs, or measures of variance. While single-run reporting is common in the PlanBench literature, the paper's strong claims (especially the 65.8% gain on o1) would benefit from at least a small number of repeated trials to establish reliability. The absence of variance is not fatal given the large effect size on o1, but it weakens confidence in the smaller differences (e.g., GPT-5 Mystery: 98.1% vs. 98.3%).

- **No analysis of output quality beyond binary correctness.** The paper evaluates only whether the full plan is correct. No analysis of partial correctness, plan length, or where in the plan the model fails is provided. Such analysis could strengthen the mechanistic argument by revealing whether TMK changes the *type* of errors or merely reduces their frequency.

### Trivial

- The discussion of "code-execution pathways" (Section 5.2.1) would benefit from more precise language distinguishing the paper's observational findings from the speculative explanation.

## Nice-to-Haves

- **Controlled prompt comparison:** Adding a condition using a flat JSON that lists the same domain knowledge without TMK's hierarchical Task-Method-Knowledge decomposition would help isolate whether gains come from the specific TMK structure or from structured prompting in general.
- **Ablation of TMK components:** Testing whether all three parts (Task, Method, Knowledge) are necessary, or whether a subset suffices, would strengthen the attribution of improvement to the TMK framework.
- **Comparison to one additional structured framework** (e.g., an HTN-style prompt) would help benchmark TMK's relative effectiveness and address questions about whether the core contribution is the structured representation or the specific TMK decomposition.

## Removed Points

The following points from the inputs were removed with justification:

- **Harsh critic: "No comparison to other structured prompting techniques (HTN, JSON schema)."** — Moved to Nice-to-Haves. The paper's core claim is that TMK improves planning over plain text; demonstrating this does not strictly require comparison to every alternative structured prompt. The lack of comparison only affects the *mechanistic* claim, which is already addressed under the Major weakness on overclaiming.
- **Harsh critic: "No statistical rigor (confidence intervals)."** — Demoted to Minor. Single-run evaluations on PlanBench are the norm in the literature; requesting multiple runs with CIs exceeds standard practice in this subfield.
- **Harsh critic: claims about the one-shot example not matching the problem being fine but not justifying asymmetric comparison.** — The paper provides documented reasoning (Section 3.2) for the baseline choice, referencing literature and sample testing. The core complaint (numbers not shown) is already in the Major weakness.
- **Strength Finder: generic/superficial strengths** (e.g., "This paper addresses an important problem," "consistent improvements across models" beyond what's already listed) — Merged or removed. The listed strengths above are the concrete, evidence-backed ones.

## Novel Insights

None beyond the paper's own contributions. The pattern observations are the paper's own empirical results, and no reviewer produced a novel synthesis that transcends what the authors already state.

## Suggestions

1. Report one-shot plain-text numbers for each model and subdomain alongside TMK in the main table so the baseline comparison is transparent.
2. Explicitly state whether the enhanced extraction function was applied uniformly to both TMK and plain-text conditions (or discuss any differences).
3. Run each condition 3–5 times and report mean/range for at least the key o1 Random result.
4. Add a controlled condition using a structured JSON prompt that lists the same domain knowledge without the TMK hierarchy, to test whether the TMK specific structure is responsible for the gains.
5. Restrict mechanistic language ("code-execution pathways," "symbolic steering") to the discussion section and clearly label it as a hypothesis requiring further investigation.

## Score and Decision

**Calibration:**

*Round 1 (bracketing)* — Weak anchors (score < 3.5): "Planning in Strawberry Fields" (3.00, Reject), "Backward Planning" (3.00, Reject), "Exploring & Benchmarking Planning" (2.00, Reject). Middle anchors (3.5–7.5): "LLMs Can Plan Only If We Tell Them" (6.40, Accept), "ET-Plan-Bench" (4.50, Reject), "Do Think Tags Really Help" (4.00, Reject), "PuzzlePlex" (5.50, Reject). Strong anchors (> 7.5): "Take a Step Back" (8.00, Accept), "GenSim" (8.00, Accept). Initial bracket: 3.5–6.5.

*Round 2 (narrowing)* — Within (4.5, 6.5): "LLMs Can Plan Only If We Tell Them" (6.40, Accept) — stronger paper with cleaner baselines, ablation studies, and more rigorous evaluation; TMK paper is clearly weaker. "Structure-aware Planning" (5.50, Reject) — comparable in having interesting ideas but methodological concerns; TMK paper is slightly weaker due to baseline ambiguity and lack of ablations. "Tree-Planner" (5.25, Accept) — narrower scope (single domain, VirtualHome) but cleaner evaluation; TMK paper is comparable. "Query-Efficient Planning" (4.75, Reject) — mixed reviews (3,3,8,5) with methodological concerns; TMK paper is similar in quality and confidence level. Within (3.0, 5.5): "Do Think Tags Really Help" (4.00, Reject) — methodologically cleaner critical analysis paper but different genre; TMK paper has a stronger positive result but more evaluation ambiguities.

The paper's headline result (65.8% o1 gain) is genuinely striking, but the evaluation has enough unresolved methodological questions (baseline transparency, extraction comparability, mechanistic overclaiming) that it falls short of the acceptance bar at ICLR. It sits around "Query-Efficient Planning" (4.75) in overall quality — a paper with a real contribution that needs strengthening. The paper is substantially better than the 3.0-level papers (which had limited contributions or were mostly model evaluations) but not as solid as the 6.4-level paper (which had clean comparisons and ablations). A score of 4.5 reflects this: below the acceptance threshold but not fatally flawed.

**Final score and decision:**

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>
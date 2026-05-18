Now I have a thorough understanding of the paper. Let me produce the final consolidated review.

---

## Summary

This paper introduces Agent Workflow Memory (AWM), a method that induces reusable sub-routine workflows from past agent trajectories and integrates them into agent memory to guide future task-solving. AWM operates in two settings: *offline* (inducing workflows from a training set before inference) and *online* (inducing workflows from self-generated successes during streaming test queries without human supervision). Evaluated on WebArena and Mind2Web (covering 1000+ tasks across 200+ domains), AWM reports 51.1% and 24.6% relative improvements in success rate, and a 7.9% gain over SteP, which uses 14 human-crafted workflows. Ablation studies examine workflow induction methods, text vs. code representations, and environment abstraction choices.

## Strengths

- **Strong, well-controlled empirical results on two major benchmarks.** On WebArena, AWM improves over BrowserGym (re-run in the same setup with a controlled variant, BrowserGym$_{\it ax-tree}$) by 51.1% relative. On Mind2Web, it improves over MindAct by 24.6% relative in step success rate. These gains are substantial and come from a controlled comparison where the main baseline shares the same framework and action space.

- **Clean two-scenario framing (offline/online) that broadens applicability.** AWM works both when annotated examples are available (offline) and when they are not (online, purely from streaming test queries). This flexibility is clearly described and independently evaluated on the two benchmarks.

- **Demonstrated generalization across tasks, websites, and domains.** On Mind2Web, AWM outperforms baselines by 8.9–14.0 absolute points on cross-website and cross-domain splits, with margins widening as the train-test distribution gap increases. This directly supports the paper's central claim that reusable workflows help agents generalize.

- **Thorough ablation study of design choices.** Sections 6.1–6.3 systematically ablate workflow induction method (LM-based vs. rule-based), representation format (code vs. text), and environment abstraction (NL descriptions vs. filtered HTML), providing practical guidance for practitioners. The finding that LM-based abstraction outperforms concrete full-example induction (45.1% vs. 43.4% step SR) is informative.

- **No human supervision required.** The method induces workflows automatically without human-crafted examples or site-specific knowledge, unlike prior work such as SteP which relies on 14 hand-written workflows.

## Weaknesses

### Fatal
None.

### Major

- **The SteP comparison may not be controlled.** The paper claims AWM outperforms SteP (which uses 14 human-expert-written workflows) by 7.9% on WebArena, but does not state whether SteP was re-implemented in the BrowserGym framework or whether published numbers from a different base architecture and action space are used. Since this comparison is highlighted in the abstract, the paper should either re-implement SteP in the same framework or explicitly describe what differences remain. The core claim does not rest solely on this comparison (the controlled BrowserGym baseline already shows strong gains), but the SteP comparison as currently presented is not verifiable.

### Minor

- **The online success evaluator is not validated on these benchmarks.** The online setting (Section 3.3) uses an LM-based evaluator from prior work (Pan et al., 2024) to judge trajectory success; only predicted-successful trajectories feed into workflow induction. The paper provides no analysis of this evaluator's accuracy, precision/recall, or agreement with ground-truth success on WebArena or Mind2Web tasks. False positives could inject flawed workflows into memory; false negatives could prevent beneficial workflows from being captured. While using an existing evaluator is defensible, the online results depend on this component, and a simple oracle-ablation (or evaluator accuracy numbers) would significantly strengthen confidence in the method's own contribution.

- **Memory scaling characteristics are not discussed.** The paper notes that workflows are grouped by website to keep collections small, but does not report: (1) how many workflows are typically induced per website, (2) the average/median token length of workflow memory, or (3) whether context window limits are approached or exceeded during streaming inference on WebArena (which processes all tasks for a site sequentially). Without this characterization, it is unclear whether the method scales gracefully or whether the reported improvements partially reflect a net effect of helpful workflows plus context management artifacts. This is the kind of practical detail that separates a solid method from one whose deployment limits are unknown.

### Trivial

- In the environment abstraction ablation (Section 6.3, Table 3), the finding that NL descriptions + filtered HTML *hurts* performance is attributed to context length increase and HTML irrelevance (correct element missing 47% of the time). The reasoning is plausible but not systematically validated (e.g., no analysis of which tasks degrade, no ablation controlling for context length). This does not affect the paper's conclusions but leaves a minor loose end.

## Nice-to-Haves

- An oracle-evaluator ablation for the online setting (replacing the LM evaluator with ground-truth success labels) would directly disentangle evaluator quality from workflow induction quality.
- A human evaluation of a sample of induced workflows (are they sensible? do they abstract away irrelevant details?) would further validate the induction module.
- Reporting workflow counts and token-length distributions per website would address the memory scaling question.
- A learning curve showing cumulative success rate as workflows accumulate on WebArena (beyond the teaser figure for the "map" split subset) would substantiate the claimed "snowball effect" more broadly.

## Removed Points

The following points from the reviewer inputs are removed per the consolidation rules:

1. **Criticism that the Mind2Web results section (Section 4.2) is entirely in an included file stripped by the parser, and that the summary numbers are too coarse to verify.** The results sections are included via `\input{}` in the original submission; these were stripped by the PDF parser, not omitted by the authors. The text does explain what the distribution gaps mean operationally (cross-website and cross-domain splits, described in Section 4.2 context).

2. **Criticism about not seeing the workflow induction prompt in the main text.** The prompt is in the appendix (referenced as \S\ref{app:lm-induction-details}), which is standard practice. Appendix content was stripped by the parser.

3. **Generic or overly broad strengths from the Strength Finder** — All strengths in the original output were evidence-backed and specific enough to retain; none were removed.

4. **The "Other Observations" point about the environment abstraction analysis being "suggestive but not fully conclusive"** — This is retained as a Trivial weakness above rather than removed, since it is a reasonable observation but does not rise to a genuine flaw.

## Novel Insights

The two most interesting signals from the reviews are: (1) the tension between the paper's clean conceptual framing (offline/online workflow induction) and the uncharacterized dependencies in the online pipeline (the LM evaluator's accuracy, memory scaling) creates an empirical gap where readers cannot cleanly attribute the online gains to the workflow mechanism itself vs. auxiliary components; and (2) the ablation showing that NL environment descriptions outperform filtered HTML (and combining them harms performance) runs counter to the intuition that more information is always better for agents — this finding, if explored further, could have implications beyond this paper for how web agents should represent environment state in memory or demonstrations.

## Suggestions

- **Clarify the SteP comparison**: Explicitly state whether SteP was re-implemented in the BrowserGym framework or whether published results are cited, and quantify any architectural differences that remain.
- **Add an oracle evaluator ablation for the online setting**: Replace the LM evaluator with ground-truth success labels and report whether results change. This single experiment would substantially increase confidence in the online results.
- **Characterize memory usage**: Report the number of workflows per website, their total token length, and whether any context-limit issues arose during streaming inference on WebArena.
- **Show broader learning curves**: Extend the teaser figure's cumulative-success-rate plot to all WebArena sites, not just the "map" split, to support the "snowball effect" claim more convincingly.

## Score and Decision

The paper presents a well-motivated method with substantial empirical gains over controlled baselines and thoughtful ablation studies. The weaknesses are real but addressable: the SteP comparison needs clarification, the online evaluator should be validated, and memory scaling deserves analysis. None of these undermine the core contribution (the workflow induction mechanism itself, which is validated through multiple ablations and the controlled BrowserGym comparison). The paper makes a clear contribution to the web agent literature.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>
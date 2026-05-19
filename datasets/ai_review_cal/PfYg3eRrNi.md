- Decision: Reject
- Avg Score: 4.80
- Scores: 5, 6, 3, 5, 5
Now I have a thorough understanding of the paper. Let me synthesize the final review.

---

## Summary

This paper introduces Agent Workflow Memory (AWM), a method that induces reusable sub-routine workflows from agent trajectories (either from offline training examples or online from self-generated successes) and integrates them into the agent's memory to guide future actions. Experiments on WebArena (812 tasks) and Mind2Web (1000+ tasks across 200+ domains) show substantial relative improvements — 51.1% on WebArena and 24.6% on Mind2Web — along with strong generalization under cross-task, cross-website, and cross-domain distribution shifts (8.9–14.0 absolute point gains).

## Strengths

- **Significant and consistent empirical gains on two major benchmarks.** On WebArena, AWM achieves a 51.1% relative improvement over a strong autonomous baseline (BrowserGym with accessibility-tree-only inputs). On Mind2Web, the cross-task step success rate improves by 24.6% relative over MindAct. These results are reported with absolute numbers in the relevant sections (abstract, §4.1, §4.2).

- **Strong generalization across distribution shifts.** On Mind2Web's cross-domain and cross-website splits, AWM surpasses Synapse by 8.9–14.0 absolute points, with margins widening as the train-test distribution gap increases (§4.2, abstract). This directly supports the claim that abstract workflows generalize better than concrete retrieved examples.

- **Flexible operation in both offline and online (supervision-free) settings.** AWM induces workflows from canonical training examples (offline) or from self-generated successes judged by an LM evaluator (online, §3.3). The online mode requires no human-annotated trajectories, which is a practically useful capability.

- **Thorough ablations of design choices.** The paper systematically explores: (a) LM-based vs. rule-based induction (§6.1), showing LM induction yields a 2.8-point improvement on Mind2Web through abstraction; (b) text vs. code workflow formats (§6.2), finding both work well; (c) NL vs. HTML environment descriptions (§6.3), showing NL descriptions outperform filtered HTML. These experiments provide actionable design guidance.

- **Competitive with human-written workflows without human effort.** On WebArena, AWM (35.5%) outperforms SteP (32.9%), a method that uses 14 human-expert-crafted workflows, despite requiring no human-designed domain knowledge (§4.1).

## Weaknesses

### Fatal
None.

### Major

- **The headline WebArena improvement is against a weakened baseline, not the full published method.** The paper claims "improves over the top published autonomous method [BrowserGym] by 51.1% relative success rate" (abstract, §1). However, the actual comparison is against BrowserGym$_{\text{ax-tree}}$, a version the authors ran themselves with *only* accessibility tree inputs, whereas the published BrowserGym uses both HTML and accessibility tree (§4.1). The paper does not report the full, published BrowserGym score, so readers cannot verify whether AWM actually surpasses the true state-of-the-art. While the paper transparently explains this choice ("to keep a fair comparison with our method"), the abstract and introduction state the improvement without qualification. This is a framing issue that directly affects the headline claim. The authors should report the full BrowserGym score alongside the weakened version, or revise the claim to clearly state the comparison is against the accessibility-tree-only variant.

### Minor

- **Online success evaluator lacks validation on these benchmarks.** The online AWM relies on an LM-based evaluator ($L_{\text{eval}}$, from Pan et al., 2024) to judge trajectory success before inducing workflows (§3.3). No precision, recall, or agreement analysis with ground-truth evaluation is reported on WebArena or Mind2Web. If the evaluator has high false-positive or false-negative rates, the online results conflate the evaluator's quality with the induction mechanism's effectiveness. A simple validation (e.g., on 50–100 random trajectories) would calibrate the results.

- **No variance or statistical significance reported.** All experiments are single runs. While the paper uses temperature 0.0 "to ensure mostly stable model outputs," LM APIs still exhibit some nondeterminism. Standard deviations or multi-seed results (3–5 runs for key numbers) would strengthen reliability claims. This is standard practice for LM-based evaluations.

- **Abstract presents only relative improvements without absolute baselines.** The abstract states 24.6% and 51.1% relative improvements without giving absolute success rates, making it hard for a reader to assess practical significance at a glance. (For context: if the baseline were 1% and AWM achieved 1.2%, a 24.6% relative gain would be less impressive than if the baseline were 30% and AWM achieved 37.4%.) The absolute numbers appear later in the paper via tables, but the abstract should include them.

- **Workflow quality is not quantitatively assessed in the main text.** The paper references "an examination of quality" in the appendix (§3.3) but provides no main-text analysis of induced workflows (e.g., what fraction are correct, how many are redundant, how often they apply across multiple tasks). This would strengthen the claim that the induction process genuinely produces reusable routines.

### Trivial

- **Online task ordering is not controlled.** The online setting processes tasks in a fixed streaming order, and no robustness check with different orderings is reported. Results could vary with order, especially early in the streaming process when few workflows have been induced.

## Nice-to-Haves

- **Direct controlled comparison isolating the abstraction effect:** The paper's strongest thesis is that *abstract, reusable sub-routines* outperform *full concrete examples*. A cleaner experiment would take the same set of successful trajectories, present them as (a) full examples in context vs. (b) induced workflows, controlling for token budget. The current comparison between AWM and Synapse mixes retrieval method, prompting format, and memory design. An ablation isolating just the abstraction vs. concreteness dimension would strengthen the core claim.

- **Order-sensitivity analysis:** Running the online scenario with 2–3 different random orders of test tasks would demonstrate robustness of the streaming workflow induction process.

## Removed Points

- **"Uncontrolled advantage on Mind2Web"** (Harsh Critic point 2) — Removed. The paper states: "We integrate the element filtering adopted in both methods [MindAct and Synapse]." MindAct *introduces* element filtering as part of its standard approach, and Synapse also uses it. AWM thus has the *same* element filtering preprocessing as the baselines; the only difference is replacing retrieved examples (Synapse) or multi-choice format (MindAct) with workflows. The comparison is fair and the critic's concern is not supported by the paper's description.

- **"If the evaluator has low precision... then workflows are induced from erroneous trajectories"** — The harsh critic speculates about two failure modes (low precision causing bad workflows; low recall wasting trajectories) without evidence. The underlying concern (unvalidated evaluator) is retained as a Minor weakness, but the speculative scenario-building about specific failure modes is removed as noise.

- **"The paper should note whether it compares to the most recent relevant work"** — Removed as a missing-related-work critique. I cannot verify whether more recent methods exist, and the paper cites the relevant published state-of-the-art (BrowserGym, MindAct, Synapse, all from 2023–2024).

- **"The offline results are not reported clearly—the tables are placeholder inputs"** — Removed. The tables are included via `\input` commands that the PDF parser could not resolve. The original submission has these tables; the parser artifact does not reflect a paper problem.

- **"Section 5... 47% miss rate... should mention whether baselines use the same predictor"** — This is already addressed: MindAct introduces the relevance predictor and Synapse uses it. Mentioning the miss rate is the paper's own finding, not a weakness.

- **Various formatting/style nitpicks, speculation about missing appendices, and reproducibility complaints about hyperparameters** — Removed per hard rules.

## Novel Insights

None beyond the paper's own contributions. The harsh critic's observations about the potential overclaiming in the abstract's wording are useful but do not constitute a novel analytical insight — they are a straightforward reading of the mismatch between the abstract's framing and the experimental setup explained in §4.1.

## Suggestions

1. **Report the full BrowserGym score** (with both HTML + accessibility tree) alongside BrowserGym$_{\text{ax-tree}}$ in the WebArena results, so readers can see the true gap to the published state-of-the-art. If AWM still beats the full version, the claim is stronger. If not, revise the abstract's phrasing to accurately reflect the comparison.

2. **Validate the online success evaluator** by reporting precision and recall against ground-truth execution-based evaluation on a held-out set of 50–100 WebArena and Mind2Web trajectories.

3. **Report absolute success rates alongside relative improvements** in the abstract.

4. **Run key experiments with 3 seeds** and report standard deviations, particularly for the main WebArena and Mind2Web comparisons.

5. **Include a brief quantitative workflow quality analysis** in the main text (e.g., correct fraction, redundancy rate, cross-task applicability).

6. **Test the online setting with at least 2 alternative task orderings** to verify robustness.

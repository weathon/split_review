## Summary
The paper introduces Ambig-SWE, an underspecified variant of SWE-Bench Verified built by having GPT-4o summarize away details from already well-specified issues, paired with an LLM "user proxy" that holds the original full issue (plus file-location oracle access) and answers agent clarification questions. Across six proprietary and open-weight models, the authors decompose interactive resolution into three capacities — detecting underspecification, asking targeted questions, and integrating answers — and report that interaction recovers up to 74% of the resolve-rate gap to the Full setting, while detection and question-quality remain brittle.

## Strengths
- The decomposition into detect → ask → integrate is a useful conceptual frame that lets the paper attribute failures to specific sub-capacities rather than to "interaction" as a monolith.
- The three-setting (Full / Hidden / Interaction) design holds task identity fixed, enabling within-instance comparisons; Wilcoxon signed-rank tests are used for Hidden→Interaction and Interaction→Full gaps (§3.1, Table 4).
- Concrete behavioral findings backed by data: Qwen 3 Coder's resolve rate actually drops from 55.43% → 52.38% when given file locations (Table 1), and Claude Sonnet 3.5 vs. Haiku extract nearly identical information (cosine 0.136 vs 0.135) but differ 12.8 points in resolve rate (§5.2). These dissociations meaningfully separate "extraction" from "integration."
- Prompt-encouragement ablation (Neutral / Moderate / Strong, Table 2) shows Qwen 3 Coder remains at 100% FNR under all prompts — a sharp, replicable finding about training-induced rigidity that prompt engineering cannot fix.

## Weaknesses

### Fatal
None. Despite the construct-validity concerns below, the paper makes real, verifiable observations.

### Major
- **The Hidden condition is a GPT-4o paraphrase of the original, and the proxy holds the original plus oracle file locations (§2.1, §2.2).** The Interaction setting therefore largely measures how completely the agent can re-elicit text that GPT-4o procedurally deleted from a single ground-truth source whose location the proxy already knows. The "up to 74% recovery" headline is upper-bounded by proxy cooperativeness and oracle access rather than by clarification competence under realistic underspecification. The authors explicitly concede in §2.1 that synthetic Hidden issues lack distributional features of *natural* underspecified GitHub issues, but treat this as a scope caveat in §7 rather than as a threat to the central quantitative claims. A non-interactive control that injects the same total information (e.g., Hidden + appended Q/A transcript) is missing, so "interaction helped" cannot be separated from "more text was available."
- **RQ2 (detection) confounds underspecification with summarization style.** Hidden inputs differ from Full inputs in length, lexical detail, and LLM-paraphrased writing style. A model scoring 89% accuracy (Sonnet 4, Strong) could be detecting "this text was shortened by an LLM" rather than "key information is missing." There is no style-matched control (naturally short-but-sufficient, or long-but-underspecified) to decouple these, so Table 2's "detection accuracy" is not cleanly interpretable as detection of *missing information*. The Llama 3.1 "0.95 FPR" under Moderate/Strong prompting is also labeled a defect, but those prompts explicitly encourage interaction — the "false positive" label presupposes an operational ground truth about when interaction is necessary that the paper does not establish.
- **The cosine-distance "information gain" metric mechanically rewards verbosity.** §5.1 defines it as the embedding distance between the summarized task and the post-interaction concatenation; appending more text — relevant or not — increases distance. This is consistent with Qwen 3 Coder having both the highest cosine distance (0.179) and the most questions (6.02) without the best resolve rate. The complementary LLM-as-judge metric uses GPT-4o, the same model used as the user proxy, so the judge is grading transcripts whose answers it produced — at best a non-independent evaluator. The §5 conclusions about question quality, efficiency, and answerability rest on these two confounded measures. The authors already have a per-issue LLM-annotated diff between Full and Hidden (§2.1), which is a natural per-instance checklist of removed facts; using it would directly measure "fraction of removed facts recovered" rather than embedding drift.

### Minor
- Footnote 4 reveals Claude Sonnet 4's Hidden result is computed on 100/500 instances while its Interaction and Full results use 500/500, yet all three are plotted side-by-side in Figure 3 and feed the 89% "relative performance" figure in §3.2. The authors note significance still holds, but the asymmetry (and the 30-turn vs 100-turn budget asymmetry between models, §3.1) should at minimum be reflected with variance estimates and explicit caveats next to the headline numbers.
- §3.3 uses causal phrasing ("interaction improves effectiveness") for an observational comparison in which the Interaction condition strictly has more information than Hidden by construction; the interesting question — does *the act of clarifying* add value beyond simply having an equivalent amount of information? — is never tested.
- §5.3's claims about Claude's "exploration-first" strategy vs. Deepseek/Qwen "asking immediately" rely on Figure 4/Table 7 anecdotes; no systematic measurement of pre-question codebase exploration (e.g., file/grep tool calls before the first question) is provided.

### Trivial
- Figure 3 lacks confidence intervals / error bars even though significance tests are reported.

## Nice-to-Haves
- A naturally-underspecified slice (e.g., issues SWE-Bench Verified excluded as underspecified, with merged-PR descriptions as post-hoc oracle) to address the §2.1 distributional mismatch.
- Decompose the Interaction→Full gap into "proxy could not / would not answer" vs. "agent did not ask" vs. "agent did not integrate." The three-stage framing demands this and the data appear to support it.
- Re-run with a less generous proxy (no file-location oracle, terser answers) to estimate the sensitivity of the 74% headline to proxy cooperativeness.
- Use a judge model distinct from the user proxy (e.g., Claude as judge for GPT-4o-mediated transcripts).

## Removed Points
These points are flagged to be removed; treat them with caution.
- *Generic "important problem" strength from Strength Finder* — surface-level and not paper-specific.
- *Harsh critic's "self-grading loop" framing for LLM-as-judge* — kept the substance (judge identical to proxy producer) but softened from "self-grading" since the judge scores user-answer specificity, not its own generations directly; it is a non-independence concern, not literal self-grading.
- *Harsh critic's concern about the cross-model 30 vs 100 turn budget being a confound for the cross-model bar chart* — kept as a minor point rather than major: the per-model within-instance Hidden/Interaction/Full comparisons (which carry the headline 74% claim) are not affected because budget is held fixed within a model.

## Novel Insights
None beyond the paper's own contributions. The genuinely interesting observations — extraction–integration dissociation and rigid-protocol behavior in Qwen 3 Coder — are the paper's own.

## Suggestions
- Replace cosine-distance information gain with a recovery-rate metric computed against the §2.1 per-issue diff of removed details.
- Add a non-interactive "Hidden + transcript" control with a strong external Q/A generator to separate interaction-the-act from information-the-content.
- Add a style-controlled detection experiment (e.g., naturally short-but-sufficient issues; LLM-paraphrased Full issues with all facts preserved) so Table 2 isolates missingness from paraphrase style.
- Run a "no-oracle proxy" variant where the proxy does not have file paths, to bound how much of the 74% depends on navigational oracle access.
- Report confidence intervals (or paired bootstrap) on Figure 3 and clearly mark the 100/500 vs 500/500 split for Sonnet 4 Hidden.

---

### Evaluation along required axes
- **Originality**: Moderate. The detect-ask-integrate decomposition and the paired Hidden/Interaction/Full setup on SWE-Bench Verified are useful framings, but ambiguity/clarification benchmarks (e.g., active task disambiguation, ConvCodeWorld) cover adjacent ground.
- **Importance**: The research question — whether agents handle underspecified SWE issues via interaction — matters for deployment.
- **Support for claims**: Mixed. Within-instance Hidden→Interaction→Full deltas are real, but the "74% recovery" framing conflates oracle-cooperative re-elicitation with realistic clarification, and detection / question-quality metrics are confounded.
- **Soundness of experiments**: Adequate scale and significance testing, but missing key controls (non-interactive same-information control, style-matched detection, alternate judge).
- **Clarity**: Generally clear; limitations are acknowledged but understated.
- **Value to community**: A reusable artifact and qualitative findings (rigid Qwen behavior, integration ≠ extraction) are likely to be cited even if the headline metric needs re-grounding.

### Calibration anchors
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/JAMxRSXLFz.md` — Active Task Disambiguation with LLMs, avg 7.33, Accept. Closely related problem; that paper provides a formal Bayesian framing and information-gain treatment, which is methodologically more rigorous than Ambig-SWE's embedding-cosine proxy. The paper under review is below it.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/rpouyo09V0.md` — ConvCodeWorld, avg 6.00, Accept. Reproducible feedback environments for conversational code generation; comparable scope and ambition, with arguably cleaner construct (real feedback channels rather than synthetic paraphrase). Ambig-SWE is in the same neighborhood but its central construct has weaker validity.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/NiNIthntx7.md` — RefactorBench, avg 6.50, Accept. Handcrafted instructions of varying specificity for refactoring; addresses specificity rigorously without synthetic-paraphrase confound. The paper under review is below RefactorBench in construct cleanliness.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/MMwaQEVsAg.md` — Commit0, avg 6.67, Accept. Interactive feedback benchmark with cleaner specification semantics.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/c2C2NQKjZw.md` — Codev-Bench, avg 4.25, Reject. Benchmark paper rejected for not matching realistic developer scenarios; somewhat analogous to the construct-validity critique here but Ambig-SWE has stronger findings.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/pwIGnH2LHJ.md` — SWE-Bench+, avg 3.75, Reject. SWE-Bench analysis paper rejected for limited methodological contribution; Ambig-SWE is more methodologically substantive than this anchor.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/riTiq3i21b.md` — SWE-bench Multimodal, avg 5.00, Accept (split). New SWE-bench variant with construct concerns; closest peer in benchmark-extension framing. Ambig-SWE sits near this anchor.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/toqQYz2N2X.md` — TAG-EQA ambiguity benchmark, avg 4.00, Reject. Rejected partly for construct-validity issues in synthetic ambiguity; relevant cautionary anchor.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/zAdUB0aCTQ.md` — AgentBench, avg 6.20, Accept. Multi-environment agent eval; broader-scope benchmark accepted on coverage, comparable empirical-rigor bar.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/IWC6zUEVcL.md` — MCU generalist-agent benchmark, avg 4.00, Reject.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/FQepisCUWu.md`, `/Yol6nUVIJD.md`, `/GDd5H92egZ.md` — multi-agent evaluation papers in the 5–6 range, only loosely related.

Placement: stronger than the rejected benchmark anchors (SWE-Bench+, Codev-Bench, TAG-EQA) because the within-instance design, Wilcoxon analysis, and integration/extraction dissociation are real contributions; but below JAMxRSXLFz (7.33), RefactorBench (6.5), Commit0 (6.67), and ConvCodeWorld (6.0) because the headline metric is upper-bounded by an oracle-cooperative proxy on synthetic paraphrases, and the question-quality metric is volume-confounded. Closest to SWE-bench M (5.0) and a notch below AgentBench (6.2).

MY FINAL SCORE: <pineapple>5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>
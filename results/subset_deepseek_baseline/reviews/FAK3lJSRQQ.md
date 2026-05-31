## Summary

This paper presents ExLLM, an LLM-as-optimizer framework for large discrete-space optimization, primarily instantiated for multi-objective molecular design. ExLLM couples three components: (1) a single, evolving experience snippet that distills non-redundant cues from good and bad candidates, (2) a k-offspring sampling strategy that generates multiple candidates per query by exploiting autoregressive factorization, and (3) a feedback adapter that normalizes objectives, formats constraints, and incorporates textual hints. The method obtains a PMO aggregate score of 19.165 (first on 17/23 tasks, +7.3% over prior SOTA), sets new records on circle packing and stellarator design, and shows strong performance across several additional domains.

## Strengths

- **Extensive and diverse empirical validation.** ExLLM is evaluated not only on the established PMO molecular benchmark but also on circle packing, stellarator coil optimization, offshore jacket structural design, multi-objective routing, peptide design, and GPU kernel optimization. Demonstrating competitive or state-of-the-art results across such a wide range of problem types is a significant achievement.

- **Clear and well-motivated methodology.** Each component (evolving experience, k-offspring, feedback adapter) is motivated by a concrete limitation of existing approaches (memory bloat, exploration collapse, difficulty handling heterogeneous feedback). The design choices are explained with reasoning, and the ablation study (PMO w/o experience: 18.165 vs full: 19.165) quantifies the contribution of the experience mechanism.

- **Strong PMO results under controlled settings.** The five-objective experiment controls for initial population quality across three conditions and uses the same LLM backend (GPT-4o) for both ExLLM and MOLLEO. ExLLM achieves the best fitness and AUC in all settings and the best hypervolume in two of three. The PMO leaderboard improvement from 17.862 (MOLLEO) to 19.165 is substantial.

- **Practical generality.** The framework transfers to new domains with only a task description template and evaluation functions, requires no training or domain-specific tuning, and uses only moderate API cost (≈$7 per run for the five-objective task). The GCU kernel design competition result (top-10 placement, second prize) provides external validation.

## Weaknesses

### Fatal

None.

### Major

- **LLM backend specification for PMO is ambiguous.** The paper states “a fixed proprietary LLM” for ExLLM experiments but does not name the specific model used in the PMO benchmark. For the five-objective task, the paper explicitly states GPT-4o was used for both ExLLM and MOLLEO, enabling a fair comparison. However, it is unclear whether the same LLM backend was used for both methods on the full PMO suite. If ExLLM used a superior model, the reported gains could be partly attributed to the LLM rather than the framework. The ablation (ExLLM w/o experience) still outperforms MOLLEO, but this does not fully resolve the issue without knowing the underlying model.

- **Several reported “record” improvements are marginal and may lack statistical or practical significance.** The circle-packing results show ExLLM achieving 2.635983 vs. the previous 2.635977 for n=26—a difference of 6×10⁻⁶. For n=32 the improvement is from 2.937+ to 2.939+. While the paper acknowledges matching records for n=27–31 at reported precision, the claim of “new records” for the two cases would benefit from a discussion of the sensitivity and noise tolerance of these metrics. Similarly, the offshore jacket optimization reports a weight of 13.6 tons vs. a human baseline of 218 tons (a factor of 16) with stress 0.508 vs. 0.024; the context (typical design range, how the human baseline was set) is necessary to interpret this extreme reduction.

- **Reproducibility is limited by reliance on proprietary LLMs.** The method uses commercial closed-source models (GPT, Gemini) whose behavior can change over time. While this is a known limitation in the LLM-as-optimizer field, the paper could mitigate it by releasing the exact prompts and task templates (beyond the claim that templates will be released) and by reporting which specific model versions were used for each experiment.

### Minor

- **Diversity of top-100 molecules is consistently lower than some baselines** (e.g., Table 2: ExLLM diversity 0.494–0.603 vs. MARS 0.819–0.826). The paper correctly notes a fitness-diversity trade-off, but the impact of reduced diversity on practical downstream use (e.g., screening) is not discussed.

- **The k-offspring strategy’s diversity within a single call is not empirically verified.** The paper claims that autoregressive conditioning yields “diverse-but-plausible edits,” but no intra-sample diversity metric (e.g., pairwise Tanimoto distance among offspring from the same parent call) is reported. A potential failure mode—that the k outputs could be nearly identical—is not addressed.

- **The feedback adapter’s constraint-promotion rule is not ablated.** The paper states that promoting critical, variable constraints to explicit objectives improves stability, but no experiment isolates this effect. Similarly, the selection of injection probability p_exp=0.5 is referenced to an appendix ablation that is not available in the extracted text.

### Trivial

- In Table 2, the “ExLLM(ours)” column header contains a typo in the closing parenthesis style. This is a formatting issue with no bearing on evaluation.

## Nice-to-Haves

- Provide an open-source implementation along with the task templates and example prompts to improve reproducibility and ease of transfer.
- Report intra-offspring diversity (e.g., average dissimilarity among the k candidates from the same parent pair) to support the claim of diverse exploration.
- For each cross-domain application, include a brief description of how the task description template was written (example prompts) and how the evaluation function was designed.

## Novel Insights

None beyond the paper’s own contributions.

## Suggestions

- For the PMO experiments, explicitly state which LLM model (version) was used for ExLLM and whether the same model was used for the MOLLEO baseline (as was done for the five-objective task). If a different model was used, discuss the potential impact and justify the comparison.

- Add a small-scale robustness analysis for the circle-packing and stellarator results (e.g., reruns with different random seeds or LLM temperature settings) to confirm that the reported records are statistically reliable.

- Provide a concise explanation of the “human baseline” in the offshore jacket experiment: what design process it reflects, what stress limit is considered feasible, and why the weight difference is so large. This would help readers assess the significance of the improvement.

## Score and Decision

**Score: 8**

The paper presents a well-engineered LLM-as-optimizer framework with strong empirical support across a diverse set of challenging domains. The PMO results are a clear improvement over the previous state of the art, and the cross-domain transfer experiments convincingly demonstrate generality. The methodology is clearly described, and the ablations help isolate the contribution of each component. The main concerns—ambiguity about the LLM backend for PMO and the extreme nature of some engineering results—are addressable and do not invalidate the core contributions. Overall, the paper offers valuable and practical knowledge to the community.

MY FINAL SCORE: <score>8</score>
MY FINAL DECISION: <decision>Accept</decision>
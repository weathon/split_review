Now I have a thorough understanding of the paper. Let me write my review.

---

## Summary
This paper introduces **Ambig-SWE**, an evaluation framework built on top of SWE-Bench Verified that specifically targets LLM agents working on underspecified software engineering tasks. The authors construct an underspecified variant of 500 SWE-Bench issues using GPT-4o to strip key details, and then evaluate 6 LLMs (Claude Sonnet 4, Claude Sonnet 3.5, Claude Haiku 3.5, Qwen 3 Coder 480B, Deepseek-v2, Llama 3.1 70B) across three settings: fully-specified, underspecified non-interactive (Hidden), and underspecified with a simulated user proxy (Interaction). The contribution is decomposed into three research questions: (1) can models leverage interaction to recover lost performance, (2) can models detect underspecification, and (3) can models ask targeted clarifying questions — each evaluated with dedicated metrics.

---

## Strengths

- **Timely and practically important research question.** As LLM agents are deployed in real codebases and enterprise workflows, underspecified instructions are ubiquitous. The paper is well-motivated and occupies a clearly relevant niche at the intersection of SWE agents and interactive NLP.
- **Clean three-part evaluation decomposition.** Breaking the capability into detection, question quality, and task completion provides a diagnostically useful framework. Each sub-problem has its own experimental setup and metrics (FPR/FNR for detection, cosine distance and LLM-as-judge for question quality, resolve rate for task completion), which is more informative than a single end-to-end metric.
- **Breadth of model coverage and interesting contrasts.** Including both proprietary and open-weight models and pairing models of similar end-task ability but different sizes (Claude Haiku vs. Sonnet, Qwen 3 Coder vs. Claude Sonnet 4) reveals non-obvious insights — e.g., that coding ability and interaction quality are largely decoupled, and that Qwen 3 Coder extracts the most information per interaction yet performs worse with navigational details due to rigid protocol adherence.
- **Concrete actionable insight: exploration-first questioning.** The finding that Claude Sonnet achieves comparable information gain to Qwen 3 with ~50% fewer questions by exploring the codebase before asking is a specific, reusable design principle for agent developers. It is directly supported by evidence (Table 6, Figure 5, qualitative trajectories).
- **Scale of evaluation.** Running full SWE-Bench-style trajectories for 6 models across 3 conditions on 500 issues (with some models capped at 100 due to cost) is a substantial experimental effort.

---

## Weaknesses

### Fatal
None.

### Major

1. **Synthetic underspecification does not match the real distribution, and the impact is not quantified.** The paper is transparent that its generated underspecified issues differ from natural ones: natural issues have more code snippets, error messages, reproducibility information, external links, and conversational fragments, while the generated ones apply "more aggressive information removal" targeting those exact elements. The distributional analysis confirms this gap qualitatively, but the paper does not show whether model rankings or relative interaction benefits hold when evaluated on real underspecified issues. Since the benchmark's core claim is relevance to real-world agentic deployment, this gap undermines the transferability of conclusions. The dismissal — that external links are inaccessible to agents anyway — is reasonable but does not address the broader concern that agents trained or evaluated on this distribution may not generalize.

2. **The user proxy is unrealistically cooperative and has super-user knowledge.** The GPT-4o proxy is provided not only with the full issue text but also with the correct file locations that need modification (§2.3: "the proxy has access to file locations that need modification and can provide them when queried"). Real users reporting GitHub issues almost never know which files to edit — that is precisely why the agent needs to explore the codebase. This design choice inflates the measured benefit of interaction (particularly through navigational queries, which Table 1 shows can boost performance by ~20 percentage points for some models) and makes the simulated interaction substantially easier than real human interaction. The authors acknowledge the proxy may be "more cooperative than real users" but do not estimate the magnitude of this bias.

3. **Inconsistent experimental design for Claude Sonnet 4.** Sonnet 4 is only evaluated on 100/500 issues in the Hidden setting (footnote 4), while all other models use all 500. The paper notes the results are "still statistically significant," but this creates an apples-to-oranges comparison in Figure 3 and Table 1, and may skew summary statistics. The justification — excessive cost — is understandable but should be accompanied by analysis of whether the 100-issue subset is representative.

### Minor

1. **Detection experiment limited to 3 interaction turns.** The paper measures whether models choose to interact within the first three turns. This may undercount detection ability if some models prefer to explore the codebase first before asking, a strategy the paper itself identifies as superior (§5). The metric is conservative by design, but the limitation is not clearly flagged when claiming models "fail to reliably distinguish" specification levels.

2. **The 74% improvement figure is not precisely defined in the text.** The abstract and introduction emphasize "up to 74% over non-interactive settings" but the paper does not state whether this is relative improvement ((Interaction − Hidden)/Hidden) or some other metric. From Table values, Claude Haiku gives ~100% relative gain, Sonnet 3.5 gives ~64%, and Sonnet 4 gives ~54%. The headline figure appears to come from a specific model under a specific measurement convention that is never clearly specified. This is minor because the underlying table data are transparent, but the headline claim is somewhat misleading.

3. **No training or fine-tuning experiments.** The paper concludes that dedicated training (not just prompting) is needed, but proposes no approach or even preliminary evidence in that direction. As a pure empirical/benchmark paper this is acceptable, but reducing the scope of claims about "training approaches" would be cleaner.

### Trivial

- The figure captions contain parser-generated alt-text repeated twice in several places — not a paper flaw but a rendering artifact.

---

## Nice-to-Haves

- An ablation on user proxy fidelity: running a version where the proxy does *not* have file locations would isolate the effect of navigational information and make the benchmark more realistic.
- A comparison using real underspecified SWE-Bench examples (even a small held-out set) to validate that rankings from synthetic underspecification transfer.
- Efficiency metrics (e.g., number of turns, tokens consumed) reported consistently across all models and conditions — the current paper provides step counts only anecdotally.

---

## Novel Insights

The most genuinely novel insight beyond what the problem framing predicts is the **decoupling between interaction capability and coding capability**: Claude Haiku 3.5 recovers a similar fraction of full performance through interaction as Claude Sonnet 3.5, despite having far inferior raw coding ability, implying that interaction effectiveness is a trainable capacity somewhat orthogonal to code generation skill. Equally novel is the **exploration-first strategy** as a qualitatively distinct and empirically more efficient interaction pattern: pre-exploring the codebase before formulating questions yields comparable information with fewer questions, a concrete design principle not previously characterized in the SWE-agent literature. The **Qwen 3 Coder paradox** — that receiving correct navigational information *hurts* performance by triggering redundant re-exploration and crowding out informational queries — is a specific and surprising behavioral signature that has practical implications for agent training on SWE-Bench-style corpora.

---

## Suggestions

- Explicitly state the formula used to compute "74% improvement" in the abstract and main text so the claim is verifiable on first read.
- Report mean ± std (or confidence intervals) for resolve rates across the 500 issues to provide a clearer picture of variance than bar charts alone.
- Provide a version of the Interaction setting where the proxy does not know file locations, to make the benchmark applicable to real-world scenarios and to disentangle navigational from informational interaction benefits.
- Acknowledge more prominently that Qwen 3 Coder's 45.6% Hidden rate may be partially explained by data contamination and/or internal parametric knowledge, as this confounds the comparison with other models in the Hidden setting.

---

## Score and Decision

The paper asks a practically important question, builds a credible evaluation framework, covers an impressively broad set of models, and surfaces several non-obvious behavioral patterns. The three-part decomposition is a clean conceptual contribution. The main weaknesses — synthetic vs. natural underspecification gap, and the unrealistically cooperative user proxy with file-location knowledge — affect the external validity of the conclusions but do not overturn the core directional findings. The paper is an incremental but solid empirical contribution appropriate for a top ML venue.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>
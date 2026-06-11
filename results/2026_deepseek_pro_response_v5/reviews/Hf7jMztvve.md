Now I have a clear picture. Let me finalize my comparison across all anchors before scoring:

| Anchor | Score | Comparison to our paper |
|--------|-------|------------------------|
| "Tall Tales at Different Scales" | 3.67 | Our paper stronger: cleaner testbed, more focused claims, honest limitations |
| "Adversarial Testing in LLMs" | 3.67 | Our paper stronger: more creative methodology, broader model coverage |
| "Too Big to Fool" | 4.25 | Comparable: both have genuine contributions with scope/rigor limitations |
| "Truth or Deceit? Bayesian Decoding Game" | 4.25 | Less comparable (different approach), but similar tier of contribution |
| "Interpreting and Steering LLM with MI on SAEs" | 5.00 | Our paper weaker: that paper has a novel method + systematic experiments + quantitative results |
| "Applying SAEs to Unlearn Knowledge" | 5.25 | Our paper weaker: more systematic SAE methodology with thorough ablations |
| "SAEs Do Not Find Canonical Units" | 7.00 | Much stronger: novel techniques, rigorous experiments, clear quantitative results |

Our paper sits between "Too Big to Fool" (4.25) and "Tall Tales" (3.67). It has a more creative contribution than "Too Big to Fool" but more significant methodological gaps. The confounded comparison and thin steering experiments are real issues that prevent the paper from supporting its central claims. The paper is honest about limitations, which is a virtue, but honesty about gaps doesn't fill the gaps.

**Final score: 4.0**. The paper makes a genuine contribution with the Secret Agenda testbed and provides interesting preliminary evidence, but the headline claims about auto-labeling are overclaimed given the confounded comparison, and the steering experiments lack the rigor needed for a negative causal claim. It's a clear reject but with interesting ideas that could form the basis of a stronger paper.

Now let me write the final review.Now I have all the calibration data I need. Let me write the final review.

---

## Summary
This paper introduces "Secret Agenda," a behavioral testbed adapted from a social deduction game to study strategic deception in LLMs, paired with an insider trading compliance analysis using SAE architectures. Across 38 models from 7 families, strategic lying was universally elicitable. The paper claims auto-labeled SAE deception features fail to activate during lying and fail as steering targets — while unlabeled aggregate SAE activations discriminate compliance from engagement in insider trading scenarios.

## Strengths
- **Prompt variation testing with political confound control**: Five distinct game framings were tested (Fascist vs Liberal, Snails vs Slugs, Truthers vs Liars, Day vs Night, Pink vs Turquoise), with the latter two explicitly devoid of political terms. Deception persisted across all variants (38/38 main, 6/6 nature), demonstrating incentive-driven rather than politically-primed behavior (Section 5.3).
- **Positive control in feature steering**: Steering the "Bananas and banana-related concepts" feature successfully eliminates banana mentions, while steering any of 100+ deception-labeled features fails. This isolates the failure to auto-labeled deception features specifically rather than to the steering mechanism itself (Section 6.3).
- **Ecosystem-wide model coverage**: Experiments span 38 models across 7 families (Anthropic-Claude, Google-Gemma, Grok, Meta-Llama, OpenAI, Perplexity, Qwen), with every family producing lies at least once (Figure 1).
- **Dual-scale SAE replication**: t-SNE and heatmap analyses are conducted on both 8B Goodfire SAE and 70B Local SAE, with directionally consistent discriminative patterns across implementations (Section 7.2).
- **Honest limitations section**: The paper explicitly acknowledges small sample sizes, "at least once" framing, analytical asymmetry between testbeds, and the preliminary nature of findings (Section 8). This candor is a genuine strength.

## Weaknesses

### Fatal
None.

### Major
- **Confounded comparison undermines the central auto-labeling claim**: The paper's headline conclusion — that auto-labeling specifically fails — rests on comparing labeled-feature failure in Secret Agenda (Sections 6.1, 6.3) against aggregate-activation success in Insider Trading (Section 7). These are different tasks with different analysis methods, and the Insider Trading analysis itself uses both labeled (8B Goodfire) and unlabeled (70B) features. There is no within-task comparison isolating labeling methodology as the failure mode. The abstract claims "autolabel-driven interpretability approaches fail to detect or control behavioral deception," but the evidence shows only that *deception-labeled* features fail in one task, while labeled features for financial domains show discriminative signal in another. The paper acknowledges the analytical asymmetry (Section 8.3-8.4) but the abstract and conclusions overstate the finding.
- **SAE steering experiments lack systematic documentation**: Section 6.3 reports that steering "100+ deception-related features" failed to prevent lying, but does not specify: (a) how features were identified (search terms, manual curation), (b) how many trials per feature, (c) what "steered down all the way" means quantitatively, or (d) whether steering affected output fluency or coherence. The banana positive control is described in one sentence without specifying which "similar features" also worked as controls. The paper references supplementary materials (a Google Drive folder) for screenshots, but the main text lacks the methodological detail needed to evaluate the negative causal claim. As reported, these are anecdotes rather than a systematic experiment.

### Minor
- **Figure 1 invites cross-family comparison the data cannot support**: With n=2 for Grok and n=2-30 per family, the stacked bar chart presenting per-family lie/partial/truth counts invites quantitative comparison. The paper acknowledges this in Section 8.1 and Figure 1's note, but the visualization format undermines the stated "at least once" framing.
- **t-SNE analysis lacks quantitative metrics**: The claim of "clear separation" between refusal and engagement clusters (Figure 4) is based on visual inspection. No clustering metric (silhouette score, adjusted Rand index), classification experiment, or statistical test is reported. The heatmap analysis (Figure 5) provides some quantification via mean-difference ranking, but the t-SNE result remains subjective.
- **Premature results reporting in the background section**: Section 3 (line 40-41) states "Mechanistic audits with GemmaScope and Goodfire's Llama SAEs show autolabeled deception features seldom activate during these lies..." — this reports the paper's own findings as if they were established background knowledge, creating confusion about what is prior work versus contribution.
- **No coding protocol or inter-annotator agreement reported**: The Secret Agenda classification into truth/partial/lie categories was done manually (~160 examples, Section 8.3), but no coding scheme, inter-annotator agreement, or adjudication procedure is described.

### Trivial
None.

## Nice-to-Haves
- A within-task comparison applying the same aggregate-activation analysis (PCA → t-SNE) to Secret Agenda responses would isolate whether the labeled vs. unlabeled distinction or the task domain drives the result.
- Quantitative clustering metrics (silhouette score, linear probe accuracy) on the t-SNE analysis would strengthen the Insider Trading discriminative claim.
- Systematize the steering experiments: select a fixed set of top deception-labeled features, run a fixed number of trials per feature per direction, and report the probability of the model maintaining the lie quantitatively.
- Replace Figure 1's stacked bar chart with a simpler table showing per-model observations (model name, n trials, whether deception observed at least once).
- Move the results currently in Section 3 (line 40-41) to the results sections where they belong.
- Report regex patterns and examples for the Insider Trading response classification.

## Removed Points
These points are flagged to be removed, treat them with caution:
- **"Model isn't 'choosing' to deceive; it's being told to be the Fascist Leader"** — This is a definitional debate about what counts as strategic deception. The paper's operational definition addresses this, and role-assignment is the intended testbed design. Removed as a philosophical disagreement, not a methodological flaw.
- **"The paper never reports how many unique scenarios underlie the 149 prompts"** — The paper describes constructing 149 prompts from "different combinations of language patterns" from Scheurer et al.'s library. The concern is speculative and would apply generically to any prompt-combination approach. Removed.
- **"Regex classification may miss nuance"** — The paper defines three clear categories (Engagement/Helpful/Refusal). This is a generic concern about any automated classification scheme. Removed as a one-size-fits-all criticism.
- **"No comparison to simpler baselines for Insider Trading"** — The paper's claim is about whether SAE features discriminate, not whether SAEs outperform other methods. A bag-of-words baseline would be nice but its absence doesn't undermine the paper's claimed contribution. Moved to Nice-to-Haves.
- **Demand for compute time / efficiency analysis** — The paper doesn't focus on efficiency. Removed as a generic request applicable to nearly any paper.
- **Missing appendix / supplementary materials concern** — Per protocol, appendix and supplementary materials exist in the original submission and are not to be flagged as missing.
- **Formatting, typos, grammar issues** — The parser strips formatting; the original submission does not have these issues. Removed.

## Novel Insights
None beyond the paper's own contributions. The core insight — that auto-labeled deception features may not capture the neural mechanisms of strategic deception even when behavioral lying is clearly present — is specific to this work and worth further investigation.

## Suggestions
- Systematize the steering experiments with a fixed protocol: select a defined set of deception-labeled features, run equal trials per feature at specified steering strengths, report quantitative honesty rates, and apply the same protocol to the banana-style control features.
- Run a within-task comparison by applying the PCA → t-SNE analysis from Section 7 to Secret Agenda responses. This would directly test whether the labeled-vs-unlabeled distinction or the task domain drives the contrast.
- Replace Figure 1's stacked bar chart with a table showing per-model trial counts and whether deception was observed at least once, aligning presentation with the "at least once" framing.
- Add a linear probe or k-NN classifier on SAE features for Insider Trading to provide a quantitative discriminability metric alongside the t-SNE plots.

## Score and Decision

This paper has a creative and well-motivated testbed (Secret Agenda), honest limitations, and interesting preliminary findings. However, the central claim about auto-labeling failure is overclaimed — the comparison between the two testbeds is confounded across tasks and analysis methods, and the paper does not provide a within-task comparison to isolate labeling as the failure mode. The steering experiments, while including a clever positive control, lack the systematic documentation needed to support a negative causal claim. These are significant evidential gaps that prevent the paper from fully supporting its headline conclusions. The paper is a clear reject in its current form, though the core ideas merit further development.

**Calibration anchors:**

| Paper | Score | Round | Comparison |
|-------|-------|-------|------------|
| "Tall Tales at Different Scales" | 3.67 | R1 | Our paper stronger: cleaner testbed, more focused claims |
| "Adversarial Testing in LLMs" | 3.67 | R2 | Our paper stronger: more creative methodology |
| "Too Big to Fool" | 4.25 | R1/R2 | Comparable quality; our paper has more creative contribution but more methodological gaps |
| "Truth or Deceit? Bayesian Decoding Game" | 4.25 | R2 | Similar tier; different domain |
| "Interpreting and Steering LLM with MI on SAEs" | 5.00 | R2 | Our paper weaker: that paper has novel method + systematic quantitative experiments |
| "Applying SAEs to Unlearn Knowledge" | 5.25 | R1 | Our paper weaker: more systematic SAE methodology with thorough ablations |
| "SAEs Do Not Find Canonical Units" | 7.00 | R1 | Much stronger: novel techniques, rigorous experiments |

Round 1 bracket: 3.5–5.0. Round 2 narrowed this to approximately 3.75–4.5 by comparison with "Too Big to Fool" (4.25) and "Interpreting and Steering LLM with MI on SAEs" (5.00). Our paper is slightly below "Too Big to Fool" due to more significant methodological gaps in the SAE analysis, but clearly above the 3.67 papers.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>
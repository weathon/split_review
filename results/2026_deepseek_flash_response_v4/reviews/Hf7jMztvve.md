Now I have all the calibration information I need. Let me compile the final review.

## Summary

This paper investigates whether current SAE-based interpretability tools with auto-labeled features can detect and control strategic deception in LLMs. It introduces the Secret Agenda testbed (a social deduction game) that elicits deceptive behavior across all 38 tested models from 7 families, and combines this behavioral analysis with a mechanistic analysis using SAEs across two domains (Secret Agenda and Insider Trading compliance). The paper reports that auto-labeled deception features rarely activate during strategic lying and feature steering fails to prevent it, while unlabeled aggregate SAE activations show discriminative structure in the insider trading domain.

## Strengths

- **Broad model coverage for deception elicitation**: The Secret Agenda testbed spans 38 models across 7 families (Anthropic-Claude, Google-Gemma/Center, Grok, Meta-Llama, OpenAI, Perplexity, Qwen), demonstrating that strategic deception can be elicited across essentially all tested models. This breadth is a genuine empirical contribution — the demonstration that 38/38 models lie at least once under incentive pressure is an existence proof that is more comprehensive than most prior work.

- **Causal intervention via steering, not just correlation**: The paper goes beyond correlational SAE analysis by testing whether steering auto-labeled deception features actually changes behavior (Section 6.3). The finding that steering topical features (e.g., "bananas") suppresses associated outputs while steering deception features does not prevent lying is a genuinely interesting and non-obvious negative result. This asymmetry between topical and deception features provides suggestive evidence for a gap between auto-labeled features and deception mechanisms.

- **Cross-architecture replication in insider trading analysis**: The insider trading results are shown across both 8B (Goodfire API) and 70B (local) SAE implementations (Section 7.3), with "directionally consistent results in heatmaps and t-SNE visualizations." This cross-scale consistency suggests the discriminative signal is not an artifact of a single SAE architecture.

- **Explicit, self-bounding limitations**: Section 8 candidly acknowledges the small per-model sample sizes (n=2–30), the synthetic nature of the game transcripts, the asymmetric analysis depth, and the scope of negative claims (targeting auto-labeled features specifically, not SAEs in general). This transparency helps readers correctly interpret the findings as preliminary.

## Weaknesses

### Major

- **Confounded comparison between testbeds undermines the headline claim**: The paper frames a central contrast in the abstract and introduction: "autolabeled features fail" (Secret Agenda) vs. "unlabeled activations succeed" (Insider Trading). However, these two testbeds differ on *multiple dimensions simultaneously* — task domain (adversarial political game vs. structured financial compliance), SAE architecture (GemmaScope vs. Goodfire 8B/70B), analysis method (manual feature checking for specific labeled features vs. PCA→t-SNE on full activation vectors), and model family (Gemma 2 vs. Llama). The paper acknowledges this asymmetry in Section 8.3 as a resource constraint, but the abstract presents this as a clean finding about labeling methodology: "autolabel-driven interpretability approaches fail... while aggregate unlabeled activations provide population-level structure." This confound makes the headline comparison uninterpretable — the observed differences could equally be due to task difficulty, model family, or analysis method rather than labeling approach.

- **t-SNE-based discriminative patterns lack any quantitative validation**: The insider trading analysis (Section 7.2) reports "clear separation" between refusal and engagement clusters based solely on visual inspection of t-SNE plots (Figure 4). t-SNE is well-known to produce visually separable clusters from random noise under certain perplexity settings. No quantitative cluster quality metrics are reported (silhouette scores, Davies-Bouldin index) and no classification accuracy from a simple decoder trained on the activations is provided. Moreover, the top discriminative features are selected by ranking |mean_engagement - mean_refusal| — a procedure that will *always* find features that differ between two groups by construction, even under the null hypothesis. The listed features (e.g., "Securities market regulation," "Financial trading transactions") may simply reflect that the model activates financial-domain features when given financial prompts, a trivial finding that does not require any deception-related representation.

- **Feature steering experiments are critically underdocumented**: The steering experiments (Section 6.3) are central to Contribution 3 but are described at a very high level ("steered to -1 and to +1" via "Goodfire's SAE feature steering dashboard"). The paper does not specify: what the -1/+1 scale means relative to the feature's natural activation range, whether intermediate steering strengths were tested, whether post-steering activation values were measured to confirm the intervention actually changed feature activity, or whether steering was applied at individual token positions or across the whole generation. The supplementary materials (a Google Drive folder of web UI screenshots) do not constitute a reproducible experimental protocol. The paper's strongest negative claim — that steering "100+ deception-related features" (abstract) did not prevent lying — is presented without the methodological detail needed to evaluate it.

### Minor

- **Cross-model bar chart (Figure 1) implies quantitative comparability that sample sizes do not support**: Sample sizes vary from n=2 (Grok) to n=30 per model family. The paper acknowledges this limitation in a footnote and Section 8.1, correctly framing the core result as an existence proof (38/38 models lied at least once). However, the bar chart visually invites frequency comparisons across families (e.g., "Anthropic-Claude had 25 lies vs. OpenAI had 21 lies") despite the highly variable sample sizes and the paper's own admission that "error bars omitted due to insufficient trials for meaningful confidence intervals." A table of raw counts would communicate the existence result without suggesting frequency comparability that the data cannot support.

- **Section 6.1 feature activation analysis lacks detail**: The paper lists specific feature IDs (5665, 14971, 1741, 6442, 10248) that did or did not activate, but does not specify the activation threshold used, how many deception examples were examined per feature, or how these features were selected (a priori expectation vs. post-hoc search of the feature catalog).

### Trivial

- The paper cites news articles (Economic Times, Democracy Now!) and a speculative fiction website (ai-2027.com) alongside rigorous ML references. These are contextual citations and not central to the experimental evidence, but tighter sourcing discipline would strengthen presentation.

## Nice-to-Haves

- Applying the same PCA→t-SNE approach used in the Insider Trading analysis to the ≈160 manually classified Secret Agenda examples would enable a within-task comparison of labeled vs. unlabeled activations, eliminating the primary confound.
- Quantitative cluster validation for the insider trading t-SNE analysis (e.g., silhouette scores, held-out logistic regression accuracy).
- Reporting post-steering activation values to confirm that steering interventions actually changed feature activity.

## Removed Points

- **Harsh Critic's criticism about Sections 2–4 being too long**: These sections situate the work within the deception literature, which is appropriate for an empirical study on this topic. The suggestion to condense "to a paragraph" is excessive and this does not constitute a weakness.
- **Harsh Critic's point about missing inter-annotator agreement for response classification**: The paper notes (Section 8.3) that classification was done via "human or LLM judgment" with ≈160 examples. While inter-annotator agreement would strengthen the analysis, this is appropriately scoped for a preliminary study.
- **Harsh Critic's "questionable references" criticism**: Downgraded from the main weaknesses to a trivial note, as these are contextual references that do not affect the experimental evidence.
- **Harsh Critic's "missing prompt variation ablation" and "cross-scale consistency metric" items**: These are reasonable suggestions for strengthening but are not core weaknesses — the paper's main existence claim (38/38 models lie) does not depend on per-variant breakdown, and "directionally consistent" for the 8B/70B comparison is a valid qualitative claim.
- **Strength Finder's Core Strength 1 ("Paired negative-positive evidence")**: This strength directly conflicts with the verified confounded-comparison weakness. The paired evidence is not cleanly interpretable as a direct comparison, so presenting it as a strength would be misleading.

## Novel Insights

The most interesting observation that emerges from this paper, beyond its own stated contributions, is the asymmetry between steering topical/concrete features (bananas) versus deception features. The former are suppressible, the latter are not. This suggests that the failure of SAE feature steering for deception is not a general failure of the steering method but is specific to certain kinds of abstract, strategic behaviors. This asymmetry could be a productive direction for the SAE interpretability community to investigate: what distinguishes features that are steerable from those that are not? The paper does not explore the *why* of this asymmetry, leaving it as an open question.

## Suggestions

1. **Deepen the Secret Agenda SAE analysis**: Apply the same PCA→t-SNE approach used in the Insider Trading analysis to the ≈160 manually classified Secret Agenda examples. This would enable a within-task comparison of labeled vs. unlabeled activations, directly addressing the primary confound.
2. **Provide full steering documentation**: List all 100+ features tested with per-feature results, specify the steering protocol (scale meaning, token position, validation), and report pre/post steering activation measurements.
3. **Add quantitative cluster validation** for the insider trading t-SNE analysis (silhouette scores, held-out classification accuracy from a simple probe).
4. **Replace the cross-model bar chart (Figure 1)** with a table of raw counts to avoid visual implications of frequency comparability that the sample sizes do not support.
5. **Temper the abstract's framing**: Present the two testbeds as complementary but not directly comparable, and avoid implying that the contrast between them is attributable to the labeling methodology alone.

## Score and Decision

**Round 1 bracket**: Based on initial calibration, the plausible score range was 4.0–5.5. Low-anchor papers on deception/jailbreaking scored 1.4–3.0 (clearly worse). Middle-anchor SAE papers scored 4.0–7.0. High-anchor rigorous empirical papers scored 8.0 (clearly better).

**Round 2 narrowing**: Four anchors were examined in full.

| Anchor Paper | Path | Avg Score | Round | Comparison |
|---|---|---|---|---|
| Tall Tales at Different Scales (deception scaling trends) | YRXDl6I3j5 | 3.67 | R2 | Paper under review is stronger — cleaner experimental setup and more specific contributions |
| Too Big to Fool (deception resilience) | tet8yGrbcf | 4.25 | R2 | Roughly comparable — similar level of methodological strength, similar scope limitations |
| AI Sandbagging (strategic underperformance) | 7Qa2SpjxIS | 5.00 | R2 | Paper under review is weaker — Sandbagging has cleaner experiments and better-documented methodology |
| Applying SAEs to Unlearn Knowledge | ZtvRqm6oBu | 5.25 | R2 | Paper under review is weaker — SAE unlearning paper has clearer methodology even if less novel findings |
| Enhancing NN Interpretability with SAEs | NB8qn8iIW9 | 4.00 | R1 | Paper under review is slightly stronger — more interesting findings despite weaker methodology |
| Sparse Autoencoders Find Highly Interpretable Features | F76bwRSLeK | 4.80 | R1 | Paper under review is weaker — landmark SAE paper with stronger empirical support |

The paper is placed between "Too Big to Fool" (4.25) and "AI Sandbagging" (5.00), closer to the lower end due to the confounded comparison and underdocumented steering experiments, which are more serious weaknesses than those in either comparison paper.

**Final score**: 4.5

The paper addresses an important question and the Secret Agenda testbed is a genuine empirical contribution. However, the headline claim is structurally confounded, the steering experiments lack the documentation needed to evaluate their core negative result, and the t-SNE-based evidence is unvalidated. These issues are substantial but not fatal to the paper's existence-proof contributions. The paper would benefit from significant revision before being suitable for a top-tier venue.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>
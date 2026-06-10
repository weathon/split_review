Now I have sufficient calibration data. Let me write the final review.

**Comparison to anchors:**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| "How to Catch an AI Liar" (567BjxgaTp) | 6.75 | R1 | Stronger — clear metrics, generalization, rigorous methodology |
| "LLMs Often Say One Thing and Do Another" (RTHbao4Mib) | 6.25 | R2 | Stronger — novel benchmark with quantitative evaluation |
| "BeHonest" (ijFdq8uqki) | 5.00 | R1 | Comparable — both important questions, execution gaps |
| "Safety Alignment Shouldn't Be Complicated" (9H91juqfgb) | 5.00 | R2 | Comparable — interesting ideas, overclaiming, lack of rigor |
| "CASE-Bench" (y9tQNJ2n1y) | 5.25 | R2 | Comparable — safety benchmark with context-awareness |
| "Language Models Struggle to Explain Themselves" (o6eUNPBAEc) | 5.00 | R2 | Comparable — important negative result, moderate execution |
| "Mechanistic Unlearning" (vsU2veUpiR) | 5.25 | R2 | Comparable — mechanistic interpretability with mixed results |
| "Too Big to Fool" (tet8yGrbcf) | 4.25 | R1 | Paper under review is better — more novel negative result |
| "Tall Tales" (YRXDl6I3j5) | 3.67 | R1 | Paper under review is clearly better — more concrete setup |

**Round 1 bracket:** 4.0–6.0
**Round 2 bracket:** 4.5–5.5

The paper has an important research question and some genuinely useful findings (the named feature failures, the positive control for steering), but lacks quantitative metrics for its key depth analysis and makes unsubstantiated claims. It is comparable to other 5.0 borderline-reject papers like "BeHonest" and "Safety Alignment Shouldn't Be Complicated" — both address important questions with execution gaps. It is weaker than the 6.25+ accepted papers which have rigorous quantitative methodology. It is stronger than the 4.25 rejected "Too Big to Fool" which has less novelty.

---

## Summary
The paper presents "Secret Agenda," a social deduction game testbed that elicits strategic lying across 38 LLMs, and uses this alongside an insider trading compliance testbed to evaluate whether auto-labeled Sparse Autoencoder (SAE) features can detect or control deception. The core negative finding is that auto-labeled deception features (e.g., "deception and betrayal," "falsehoods in political speech") rarely activate during actual strategic lying and cannot prevent it via feature steering, while a topical control feature ("bananas") can be steered successfully. Unlabeled aggregate SAE activations show some discriminative structure for compliance vs. engagement in insider trading scenarios, but only through t-SNE visualizations without quantitative metrics.

## Strengths
- **Concrete positive control for feature steering (Section 6.3)**: Steering a "Bananas and banana-related concepts" feature successfully suppressed mention of those concepts, while steering deception-related features to extreme values (-1 or +1) did not prevent lying. This within-experiment contrast isolates the failure as specific to autolabeled deception features rather than a general steering artifact — line 106: "When we tried similar trials with the 'Bananas and banana-related concepts' feature... we were able to prevent mention of those associated concepts, however the same did not appear to hold for deceptive behavior."
- **Named, specific autolabeled features that failed (Section 6.1)**: The paper identifies exact features by ID and label — "14971: deception and betrayal", "1741: falsehoods in political speech", "6442: deception and manipulation", "10248: misinformation in news contexts" — and reports they were dormant during actual strategic lying (line 94). Only feature 5665 ("secrecy in interactions") reliably activated. This provides concrete, falsifiable evidence about the gap between autolabeled features and behavioral deception.
- **Systematic prompt variation testing (Section 5.3)**: Multiple game variants — Fascist vs Liberal, Snails vs Slugs, Truthers vs Liars, Day vs Night, Pink vs Turquoise, and shortened — insulate findings from political bias or specific terminology. Deception persisted across all variants.
- **Cross-scale SAE replication (Section 7.2)**: Both 8B Goodfire and 70B Local SAE implementations show directionally consistent discriminative patterns in t-SNE and heatmap visualizations for insider trading, providing some cross-architecture evidence.
- **Broad model coverage (Section 5.2)**: 38 models across 7+ families (Anthropic, Google, Grok, Meta, OpenAI, Perplexity, Qwen) with 38/38 showing deception at least once, demonstrating universality of the behavioral phenomenon.
- **Transparent limitations (Section 8)**: Unusually thorough acknowledgment of small sample sizes, analytical asymmetry, and scope of autolabeling claims. Section 8.4 explicitly clarifies the negative results concern autolabeled features, not SAE architectures themselves.

## Weaknesses

### Fatal
None.

### Major
- **Insider trading analysis relies entirely on visual inspection — no quantitative metrics (Section 7)**: The paper claims "unlabeled SAE activations successfully discriminate compliance" (Section 7.3) based solely on t-SNE scatter plots (Figure 4) and heatmaps (Figure 5). No classification accuracy, AUC, silhouette score, or linear probe is provided — confirmed by searching the entire paper for these terms with zero matches. The paper does compute |mean_engagement - mean_refusal| to rank discriminative features (line 161), but never reports the magnitude of separability in a falsifiable metric. t-SNE is notoriously sensitive to perplexity and initialization and can produce apparent clusters in random data. For the paper's most mechanistically detailed positive finding, this is a significant gap that prevents verification.

- **Conceptual conflation between the two testbeds (Sections 5–7)**: Secret Agenda measures intentional misrepresentation of faction identity — clear deception. Insider Trading measures whether a model executes trades on material non-public information vs. refuses — this is compliance/refusal behavior. The paper consistently frames both as "deceptive behavior" (Abstract line 9: "separated deceptive versus compliant responses"; Section 7.3: "aggregate activations successfully distinguish compliance behaviors"), but a model executing insider trades is not "deceiving" anyone; it is failing to refuse an unethical request. The contrast between "SAE features fail in Secret Agenda" and "SAE activations succeed in insider trading" is only interpretable if both measure the same construct. As framed, they measure different things, weakening the paper's central narrative about SAE limitations for deception detection specifically.

- **The "100+ deception-related features" claim is unsubstantiated (Abstract vs. Sections 6.2–6.3)**: The abstract claims "feature steering experiments across 100+ deception-related features failed to prevent lying." The body names approximately 5 specific features (5665, 14971, 1741, 6442, 10248) and mentions "tactical deception and misdirection methods" as a category. No systematic table of all features tested, search methodology, feature selection criteria, or distribution of results is provided. The experiments were conducted through a web UI dashboard rather than programmatically. Without knowing the full set tested and how, the negative result is anecdotal — an incomplete search could produce a false negative about SAE capabilities.

### Minor
- **Small per-model sample sizes limit behavioral conclusions (Section 5, Figure 1)**: With n=2 for some models, "38/38 models lied at least once" is a low bar. The paper cannot distinguish models that lie 100% of the time from those that lie 5% of the time. The authors acknowledge this (Section 8.1), but it limits contribution beyond prior work (Greenblatt et al., 2024; Meinke et al., 2024; Scheurer et al., 2024) that already established LLMs engage in strategic deception.

- **Classification methodology for Secret Agenda responses is undocumented (Section 5)**: The categories "truth", "partial or partial lie", "lie" appear in Figure 1, but the paper does not describe how responses were classified, by whom, whether multiple raters were used, or whether inter-rater reliability was assessed.

- **Discriminative features in Table 1 reflect domain content, not deception (Section 7.2)**: Features like "Quantity fields in structured data" (48374), "Securities market regulation" (10180), "Financial trading transactions" (17289) discriminate topic/content differences between engagement and refusal responses rather than encoding deception. This further supports the concern that insider trading analysis detects compliance patterns rather than deception.

### Trivial
None.

## Nice-to-Haves
- Adding a linear probe or silhouette score on SAE activations for the insider trading analysis would substantially strengthen the positive finding and replace purely visual claims.
- A complete table of all features tested in steering experiments with their auto-labels, search terms, and steering results.
- Increasing Secret Agenda sample sizes for even a subset of models (e.g., n=50 for 5 models across families) would enable rate estimation and meaningful cross-model comparisons.
- Separating the two testbeds' claims more clearly — Secret Agenda for behavioral elicitation of deception, insider trading for compliance/non-compliance detection — would sharpen the narrative.

## Removed Points
These points are flagged to be removed, treat them with caution.
- None removed from the harsh critic's points; all were verified against the paper text.

## Novel Insights
The most novel observation is the specific failure of named, autolabeled deception features (e.g., "deception and betrayal", "falsehoods in political speech") to activate during actual strategic lying, contrasted with the success of a topical positive control ("bananas") in the same steering setup. This within-experiment contrast — steering works for content features but fails for autolabeled deception features — provides concrete evidence that current autolabeling approaches have a specific gap for deception, not a general failure of the SAE steering mechanism. This is a genuinely useful negative result for the interpretability community, even if the broader insider trading analysis lacks rigor.

## Suggestions
- Add a linear probe or silhouette score on SAE activations for the insider trading analysis to replace purely visual t-SNE claims.
- Provide a complete table of all features tested in steering experiments with their auto-labels and results.
- Reframe insider trading analysis as compliance detection rather than deception detection to avoid conceptual conflation.
- Document the Secret Agenda classification methodology (who classified, how, inter-rater reliability).

## Score and Decision

**Round 1 bracket:** 4.0–6.0. The paper is weaker than "How to Catch an AI Liar" (6.75, well-executed with clear metrics) and "LLMs Often Say One Thing and Do Another" (6.25, novel benchmark with quantitative evaluation), but stronger than "Too Big to Fool" (4.25, marginal contribution) and "Tall Tales" (3.67, definitional issues).

**Round 2 bracket:** 4.5–5.5. The paper is comparable to "BeHonest" (5.00, important question with execution gaps), "Safety Alignment Shouldn't Be Complicated" (5.00, interesting ideas but overclaiming), and "Language Models Struggle to Explain Themselves" (5.00, important negative result with moderate execution).

**Final score:** 5.0. The paper sits squarely at the borderline: a genuinely important research direction with some concrete, useful negative findings (the named feature failures, the positive control), but undermined by the lack of quantitative metrics for its depth analysis, an unsubstantiated "100+" claim, and conceptual conflation between testbeds. It matches the pattern of other 5.0-reject papers that address important questions but whose execution doesn't clear the bar for a main conference contribution.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>
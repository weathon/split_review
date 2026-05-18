## Summary

This paper investigates the connection between pretraining data frequency and the formation of linear representations (specifically Linear Relational Embeddings, LREs) in language models. Using OLMo 7B, OLMo 1B, and GPT-J, the authors show that subject-object co-occurrence frequency in pretraining data strongly correlates with LRE quality (causality score, r=0.82), that this relationship holds across all pretraining stages independent of training step, and that LRE metrics can be used to predict term frequencies in a model's training data — even transferring across models. The core empirical finding — that frequency is a strong predictor of which relations develop linear structure — is novel, well-documented, and addresses an open question in mechanistic interpretability.

## Strengths

- **Establishes a strong, quantitative link between pretraining term frequency and LRE quality.** The paper reports a Pearson correlation of r=0.82 between subject-object co-occurrence frequency and causality scores across relations in OLMo 7B (Section 4.2), directly addressing why some relations form linear representations while others do not. This goes beyond the existing literature, which has noted the variation but not explained it.

- **Shows the frequency–linearity relationship holds across all pretraining stages, independent of training step.** Using 8 intermediate checkpoints, the paper demonstrates that relations whose average co-occurrence exceeds a threshold have high causality even at very early training steps (41B tokens), while low-frequency relations never develop them. This reveals that linearity depends on cumulative exposure rather than model maturity (Figure 2, Section 4.2).

- **Demonstrates that LRE metrics encode information about pretraining frequency that generalizes across models.** A random forest using LRE features predicts object frequencies within one order of magnitude at ~70% accuracy, and this signal transfers from OLMo 7B to GPT-J with maintained accuracy (Table 1), outperforming baselines based solely on log probabilities. While modest, this is a genuinely novel approach to probing training data.

- **Isolates linearity as a distinct signal from accuracy.** Section 4.3 shows that causality correlates more strongly with frequency (r=0.82) than 5-shot accuracy does (r=0.74), and identifies low-frequency relations with high accuracy but low linearity (e.g., "star constellation name": 84% accuracy, 44% causality). This nuanced finding rules out the trivial explanation that frequency simply improves all task performance uniformly.

- **Provides a careful error analysis** (Table 2, Section 5.4) showing interpretable patterns in where the regression succeeds and fails, giving practical guidance for future applications.

- **Releases a practical tool (Batch Search) for exact token-level co-occurrence counting** across pretraining batches, enabling per-checkpoint frequency analysis that was essential for the temporal findings.

## Weaknesses

### Fatal
None.

### Major
None. The paper's limitations are honestly discussed, and no flaw invalidates the core empirical finding.

### Minor

- **Relation-level confounds are not controlled.** The paper analyzes frequency and LRE quality at the relation level (averaging over all subject-object pairs within a relation). This conflates frequency with other relation properties that could explain linear structure — for example, whether a relation involves deterministic one-to-one mappings (e.g., "country-largest-city") vs. ambiguous many-to-many mappings (e.g., "star-constellation"). The paper mentions "star constellation name" as a low-frequency outlier but does not systematically test whether the frequency–linearity correlation survives controlling for relation type. A within-relation analysis (e.g., showing that among subject-object pairs sharing the same relation, higher-frequency pairs have higher linearity) would substantially strengthen the causal plausibility of the claim.

- **The frequency threshold claim is identified informally.** The paper reads thresholds of 1-2k co-occurrences (for OLMo 7B/GPT-J) and 4.4k (for OLMo 1B) from scatterplots and a single table without statistical tests, confidence intervals, or a formal changepoint detection procedure. The paper itself notes "we can not draw conclusions from only three models" — and that's the right caution — but the threshold framing in the abstract and introduction is more definitive than the evidence supports. This is a presentation issue, not a fatal one; the qualitative pattern (high-frequency → linear, low-frequency → not) is clear from the scatterplots.

- **A few phrasings imply a causal direction the design cannot support.** The Limitations section (Section 8) explicitly states "we can not draw causal claims about how exposure affects individual representations," which is commendable. However, the main text occasionally uses language that tilts toward causation — e.g., "the reason why some concepts form a linear representation while others do not, is strongly related to the pretraining frequency" (end of Section 4.3). The evidence is correlational, and the paper should consistently frame the relationship as a strong predictor/associate rather than an explanation.

- **The "unsupervised" framing of the regression is slightly imprecise.** The method trains on one model with known ground-truth frequencies and transfers to another — this is a zero-shot/transfer learning approach, not unsupervised learning. This is a minor terminology issue; the method's usefulness does not depend on the label.

- **The LRE fitting change is asserted without validation.** The paper relaxes Hernandez et al.'s requirement that examples must be correctly predicted to fit LREs (Section 3.1), stating "using examples that models predict incorrectly to fit Equation 1 works as well as using only correct examples" — but provides no comparison experiment. While this change is reasonable for cross-checkpoint comparison, a brief validation on the final checkpoint would increase confidence.

- **Scale comparison rests on one small model.** The claim about OLMo 1B requiring a higher threshold (4.4k vs. 1-2k) is confounded with architecture differences beyond scale. The paper acknowledges this ("Although we can not draw conclusions from only three models"), which is appropriate.

### Trivial
- None.

## Nice-to-Haves

- **Within-relation analysis:** For a few relations spanning a wide range of subject-object frequencies (e.g., "lead singer of" with well-known vs. obscure musicians), computing LRE scores for individual pairs would directly test whether frequency drives linearity even when relation structure is held constant.

- **Formal changepoint detection** on the frequency–causality scatterplots, or bootstrapped confidence intervals for the correlation, would place the threshold claim on firmer statistical ground.

- **Continuous error metrics** (e.g., Spearman correlation, RMSE in log space) for the regression task, alongside the coarse "within one order of magnitude" accuracy, would give a more complete picture of prediction quality.

- **Sanity check on Batch Search counts** against WIMBD counts for the full dataset, to validate that exact batch-level counting and document-level counting are consistent.

## Removed Points

The following points raised by the Harsh Critic are removed per policy:

- **Release verification / reproducibility concern about code availability.** The paper states it releases code and Cython bindings. Per hard rules, criticisms questioning the existence or availability of cited resources are removed.
- **"The paper should present correlation coefficients"** — The paper already reports Pearson r=0.82, r=0.66, and r=0.59 for different frequency types. This point is factually incorrect.
- **"Unsupervised is misleading" framed as a major weakness** — Kept as Minor terminology precision issue above; the critic's framing as a structural flaw is downgraded.
- **"The paper must be rewritten" about causal language** — Kept as Minor (a few phrasings could be tightened), but the paper already has a Limitations section that explicitly disclaims causal claims, so the "must be rewritten" framing is excessive.

## Novel Insights

Beyond the paper's own contributions, the reviews highlight an important methodological tension: the paper's most striking finding — that frequency thresholds predict linear representation formation — is simultaneously its most impactful result and its least rigorously supported one. The scatterplots are visually compelling, but the lack of within-relation controls means the paper cannot distinguish between "frequency drives linearity" and "frequency is a proxy for relation simplicity (deterministic mappings tend to both be simpler and mentioned more often)." This is not a fatal flaw — the correlation is real either way — but future work should prioritize controlled experiments (e.g., constructing counterfactual pretraining corpora where a specific relation's frequency is varied while holding all else equal) over scaling to more models. The regression application, while modest, points toward a genuinely interesting direction: using interpretability tools (LREs) to do data archaeology on closed models, turning a weakness (we don't know what linear representations mean) into a strength (their frequency-dependence lets us infer training data properties).

## Suggestions

1. Add a within-relation analysis for 2-3 relations with wide frequency ranges (e.g., "lead singer of," "country largest city") to show that frequency predicts linearity even when relation type is held constant.
2. Reframe threshold observations as descriptive findings ("relations exceeding ~1-2k co-occurrences consistently have high causality in these three models") rather than claiming a discovered threshold; add a Limitations callout that formal threshold estimation would require more data.
3. Replace or supplement one sentence in Section 4 (end) and the abstract that could read as causal — e.g., change "the reason why...is strongly related to" to "is strongly predicted by" — to match the correlational framing used elsewhere.
4. Validate the relaxed LRE fitting procedure against the original (correct-only) procedure on at least the final checkpoint.
5. Report Spearman correlation and log-space RMSE alongside the "within one order of magnitude" accuracy for the regression.

## Score and Decision

**Originality:** 7/10 — The question (why some relations form linear representations and others don't) is timely and directly follows from prior work on LREs. The frequency connection is novel.

**Importance of research question:** 8/10 — Understanding what drives linear representation formation is central to mechanistic interpretability. The application to data inference is a valuable bonus.

**Claims well-supported?** 6/10 — The core correlation is well-supported. The threshold and cross-model claims are partially supported with honest limitations. Some presentation could be more precise.

**Soundness of experiments:** 7/10 — The experimental design is reasonable for an observational study. The main gap is the lack of within-relation controls.

**Clarity of writing:** 7/10 — Clear prose; the caveats are present even if the abstract and introduction sometimes outpace them.

**Value to the community:** 7/10 — The finding is directly useful for interpretability researchers studying when linear representations should be expected, and the Batch Search tool has standalone utility.

**Overall:** This is a solid empirical paper that documents a genuine and previously unknown correlation between pretraining data frequency and the formation of linear representations in LMs. The limitations are honestly discussed, the evidence for the core claim is clear, and the paper opens a productive direction for future work. The weaknesses identified above are addressable and do not undermine the central contribution.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>
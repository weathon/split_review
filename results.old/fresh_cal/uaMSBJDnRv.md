I have now thoroughly verified all reviewer claims against the paper. Let me write the final consolidated review.

---

## Summary

This paper identifies and characterizes *likelihood displacement* in direct preference learning — the counter-intuitive decrease in preferred-response probabilities during DPO training. The authors demonstrate that this can be catastrophic (e.g., training a model to prefer "No" over "Never" can sharply increase the probability of "Yes"), provide a theoretical analysis linking displacement to embedding geometry, derive a diagnostic metric called the Centered Hidden Embedding Similarity (CHES) score, and show that CHES-based data filtering prevents unintentional unalignment in safety training (e.g., preventing a refusal-rate drop from 74.4% to 33.4% in Llama-3-8B-Instruct).

## Strengths

1. **Clean demonstration that catastrophic displacement occurs in a minimal setting.** Table 1 shows, across three model families (OLMo-1B, Gemma-2B, Llama-3-8B), that training on a single prompt with single-token responses causes probability mass to shift to opposite-meaning tokens (e.g., "No"→"Never" training increasing "Yes" probability). This directly refutes prior attributions to model capacity, multiple tokens, or SFT phase, isolating the phenomenon in a way prior work did not.

2. **Theoretical derivation of the CHES score and its causal link to displacement.** The informal Theorems 4.1 and 4.2 characterize how token unembedding alignment and hidden embedding geometry drive likelihood displacement, culminating in the CHES score (Definition 4.1). The paper provides the first formal characterization that specifies *why* similar preferences cause displacement, going beyond prior empirical observations.

3. **Empirical validation that CHES is predictive of displacement while alternative measures are not.** Figure 2 (UltraFeedback, Gemma-2B and Llama-3-8B) shows that ranking training samples by CHES percentile perfectly correlates with degree of log-probability decrease, whereas edit distance (suggested by prior work) and last-hidden-embedding inner product show no such correlation. This is clean, reproducible, and establishes CHES as a uniquely effective diagnostic tool.

4. **Demonstration that displacement causes unintentional unalignment and CHES-based filtering mitigates it.** Training to refuse unsafe prompts (Section 6.2) drops refusal rates from 74.4% to 33.4% for Llama-3-8B-Instruct (Figure 3a). Filtering out the 5% highest-CHES samples not only prevents the drop but increases refusal rates, outperforming both an SFT-augmented DPO and gold preference data. This shows practical, measurable value of the theory.

5. **Breadth of validation.** The paper consistently validates findings across OLMo-1B, Gemma-2B, and Llama-3-8B in the simple-setting experiments and CHES validation, and on Gemma-2B-IT/Llama-3-8B-Instruct for the unalignment case. The qualitative analysis (Figure 3b) bridges the theoretical score with human-interpretable data characteristics.

## Weaknesses

### Fatal

None.

### Major

None. The paper's core claims — that displacement can be catastrophic, that it is driven by embedding geometry, that CHES identifies contributing samples, and that filtering mitigates harmful effects — are all well supported by evidence. The issues below are evidential gaps or clarity concerns, not structural flaws.

### Minor

1. **CHES derivation sets coefficients to +1 despite a theoretical gap.** The paper acknowledges (line 340) that coefficients α⁻ and α⁺ are "mostly positive" and accordingly sets them to one to derive CHES. While the resulting metric is empirically validated (Figure 2), the theoretical connection between CHES and displacement remains *approximate* — the paper does not quantify how often coefficients are negative or whether negative coefficients can cluster in ways that reverse the CHES–displacement relationship. The paper is transparent about this approximation, but it weakens the claimed theoretical tightness.

2. **The safety experiments measure refusal rates but do not systematically characterize where probability mass goes.** The refusal rate drop (74.4%→33.4%) is striking, and the appendix provides qualitative examples of compliance. However, the paper does not quantify whether the increased probability of non-refusal responses is concentrated on *directly harmful completions* (which would be catastrophic) versus diffuse across benign non-refusals or evasive responses. A token-level or category-level analysis of where mass moves in the safety setting would strengthen the paper's central "catastrophic" narrative for this experiment.

3. **The comparison between CHES filtering and the SFT-augmented DPO baseline is underspecified.** The paper reports (Figure 3a) that filtering "goes beyond the improvement achieved when adding an SFT term," but the main text does not specify the SFT loss weight or how it was chosen. Without knowing whether this weight was tuned, it is unclear whether filtering is genuinely superior or simply better under one parameter setting. The details may reside in the (stripped) appendix, but the claim as presented in the main text cannot be fully evaluated.

4. **Length-normalized CHES is used in the key safety experiment but defined only in the appendix.** The paper applies a "length-normalized variant of CHES" (line 464) for the filtering experiments — the paper's most practically significant result — but the definition is deferred entirely to the appendix. Since the normalization scheme is crucial for reproducibility and interpretation, the main text should at least state the basic formula (e.g., dividing by number of token positions, response lengths, or some other normalization).

### Trivial

1. **Table 1 reports "the largest decrease in the preferred token probability during training"** rather than the endpoint probability. If the probability recovers after the nadir, the implication changes. The parenthetical ranges (e.g., 0.96→0.27) suggest the reported decrease is endpoint to minimum, but the wording is ambiguous. The paper should clarify endpoint behavior.

## Nice-to-Haves

- **Threshold sensitivity analysis for CHES-based filtering.** The paper notes that keeping up to 15% of samples yields similar results (line 496), but a full sweep (e.g., 1%, 5%, 10%, 20%, 50%) would strengthen the practical claim and help users understand what fraction of data can safely be kept.

- **Use of a second refusal judge** (e.g., Llama Guard) in the safety experiments to confirm that the refusal rate patterns are not judge-specific.

- **A brief statement of the length-normalization scheme in the main text** would improve reproducibility without requiring readers to consult the appendix.

- **More granular analysis of the safety experiment** to confirm that probability mass shifts to specifically harmful completions (catastrophic) rather than benign non-refusals.

## Removed Points

These points from the reviewers were considered but removed:

- *"The analysis of multiple training samples is brief and deferred to appendix"* — The parser strips appendix sections from all papers. The main text provides a standalone discussion (Section 4.2.3, lines 350–358) that is adequate for the paper's scope.

- *"The last-hidden-embedding baseline is weak"* — The paper presents this as a "natural candidate" baseline that happens to fail, which only strengthens the case for CHES. The baseline's weakness is not a weakness of the paper.

- *"The paper does not report statistical significance or variance"* — The paper reports min/max error bars across three runs (Figures 2, 3a), which is standard for this type of empirical work.

- *"The gold data comparison" framing concerns* — The paper's comparison with gold data is clearly presented as an informative reference point, not a practical recommendation.

## Novel Insights

None beyond the paper's own contributions. The reviews did not surface an insight about the paper that the paper itself does not contain.

## Suggestions

1. In the rebuttal/camera-ready, clarify the endpoint behavior for the Table 1 measurements — are the reported decreases endpoint-to-minimum, or do they reflect sustained drops? State explicitly whether the probability typically recovers.

2. Add a brief formula for the length-normalized CHES score in the main text (Section 6) so the key practical experiment is self-contained. Even one sentence (e.g., "divide the CHES score by the sum of the lengths of the preferred and dispreferred responses") would suffice.

3. Provide a systematic breakdown of where probability mass goes in the safety experiments. For the models whose refusal rate drops, categorize the most probable new responses into "directly harmful compliance," "evasive/non-harmful non-refusal," and "other." This would directly tie the safety results to the catastrophic vs. benign distinction that frames the paper.

## Score and Decision

MY FINAL SCORE: <score>8.5</score>
MY FINAL DECISION: <decision>Accept</decision>
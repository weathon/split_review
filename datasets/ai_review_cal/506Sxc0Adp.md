- Decision: Reject
- Avg Score: 4.00
- Scores: 3, 6, 1, 6
I now have all the information needed. Let me produce the final consolidated review.

---

## Summary

This paper extends the Task2Vec diversity coefficient (originally developed for vision) to natural language text, using GPT-2 as a probe network to compute Fisher Information Matrix embeddings of text batches. It measures the diversity coefficient on ten publicly available LLM pre-training datasets (C4, The Pile, etc.), compares them to conceptual reference datasets, and conducts interpretability experiments (pairwise distance distributions, GINC-controlled variation of latent concepts and vocabulary size) to validate that the metric behaves as expected. The paper also provides practical guidance on batch size and probe network configuration.

## Strengths

- **Controlled causal validation on synthetic data (GINC):** Section 3.4 shows the diversity coefficient increases monotonically with both the number of latent concepts (R² = 0.952, 0.898) and vocabulary size (R² = 0.993, 0.984) on the GINC synthetic dataset. This is not merely a correlation on real data — it is causal evidence that the coefficient responds to known, controllable sources of variation, which is a strong internal-validity check.

- **Interpretable structure in pairwise batch distances confirms semantic grouping:** Section 3.3 shows that the distribution of Task2Vec cosine distances between batches exhibits exactly the number of modes expected from combinatorial dataset pairings (3 modes for 2 datasets, 15 for 5). Furthermore, conceptually related datasets (e.g., Pile-CC and HackerNews) have lower cross-diversity than unrelated pairs (e.g., HackerNews and PubMed). This clean pattern is a convincing sanity check that the embeddings capture semantic content.

- **Practical hyperparameter sensitivity analysis:** Section 4 systematically tests the effect of batch size (128–1024) and four probe-network configurations (pretrained/random × fine-tuned/not), showing that diversity estimates increase with batch size with diminishing returns, and that random or non-fine-tuned networks produce diverging estimates. This provides actionable guidance for practitioners applying the method to new text datasets.

- **Relative diversity rankings across datasets are informative:** The paper's measurements reveal a sensible ranking — web-crawl datasets (C4, The Pile, Pile-CC: 0.23–0.25) are more diverse than specialized technical corpora (NIH ExPorter, PubMed, USPTO: 0.15–0.17). This differentiation is the genuinely useful empirical finding in the paper and shows the metric can distinguish datasets in a human-aligned way.

## Weaknesses

### Fatal
None.

### Major

- **The headline claim ("LLMs are pre-trained on formally diverse data") is overframed relative to what is actually shown.** The paper defines "formal diversity" as having a high diversity coefficient, measures it, and finds it is indeed well above a near-degenerate baseline. This is a real measurement, not a tautology — the coefficient could have turned out low — but the finding that web-scale text data is more diverse than a dataset of almost all `<eos>` tokens is not surprising or discriminative. What is informative is the *comparison across datasets* (C4 vs. USPTO, etc.), which the paper treats as secondary to the headline. The title and abstract overpromise by presenting the absolute measurement as a discovery, when the paper's real contribution is validation of the metric's behavior and the relative rankings.

- **No empirical comparison against any alternative diversity metric, despite making comparative claims.** Section 5 explicitly criticizes the Vendi Score (calling its aggregation "not clear," its computation O(n³) vs. O(n²)) and asserts "our method is likely more general and scalable." These are comparative claims without supporting experiments. The paper acknowledges this ("leave a detailed comparison with the Vendi Score as future work") but this acknowledgment does not remedy the evidential gap — a paper that positions a metric as useful for a new domain should include at least one head-to-head comparison to establish that the metric provides non-redundant or superior information. Without this, the reader cannot assess whether the Task2Vec coefficient captures genuinely different signal from cheaper alternatives.

### Minor

- **"Conceptual bounds" terminology is imprecise and may mislead.** The paper calls them "lower and upper bounds" (Section 2.2.4), but they are not mathematical bounds — they are two synthetic datasets chosen as intuitive extremes. A truly degenerate dataset (all identical sequences) would give a diversity coefficient of exactly 0, lower than the paper's "lower bound" (which yields positive cosine distances because the 2-token vocabulary allows some variability). The paper qualifies them as "conceptual" but the "more than half the upper bound" framing in the abstract and results suggests a precision that the reference points do not support. Renaming these "reference datasets" or "intuitive extremes" would be more accurate.

- **The downstream performance experiment is too preliminary to support the conjecture that diversity improves performance.** The paper (Section 6) presents a single experiment pre-training three GPT-2 models on datasets of varying diversity and measuring loss on diverse validation sets: only three data points, no confidence intervals, no control for dataset size, topic distribution, or other confounds. The paper itself calls this "preliminary" and says "more extensive experiments are needed to know so conclusively." This is appropriate caveating, but the experiment is then used to motivate the concluding conjecture that "the diversity coefficient can be used to build quality, diverse datasets for LLMs." If the paper's core contribution is metric validation, this experiment adds little; if the paper wants to assert practical utility, more evidence is needed.

- **No analysis of confounders like sequence length or tokenizer effects.** The diversity coefficient computation uses GPT-2's tokenizer and fixed sequence processing. Datasets vary in average sequence length, which could affect the FIM calculation (longer sequences yield more tokens for gradient computation). The paper does not check whether measured diversity differences are driven by length rather than content. Similarly, the effect of different tokenizers (which change the vocabulary and thus the "upper bound" reference) is not discussed. These are straightforward controls that would strengthen confidence in the findings.

### Trivial

- **Equation (1) samples tokens x̂_t from the fine-tuned model rather than using the gradient on actual data.** This is a methodological divergence from the standard Task2Vec approach (Achille et al., 2019) and from the typical definition of the empirical Fisher. The paper does not explain or justify this choice. If intentional, a brief justification is needed; if unintentional, the equation should be corrected.

## Nice-to-Haves

- A comparison against the Vendi Score (or another diversity metric) on the same datasets would substantially strengthen the paper, especially if it shows the metrics disagree and provides evidence for which ranking is more sensible.
- An analysis of the number of batches needed for stable diversity estimates (beyond "200 was used") would improve the practical guidance in Section 4.
- Reporting confidence intervals or bootstrap estimates for the dataset rankings in Table 1 would help assess whether differences between datasets (e.g., C4 vs. The Pile) are meaningful.

## Removed Points

These points are flagged to be removed — treat them with caution.

1. **From Harsh Critic: "The main empirical claim is tautological."** — The paper's measurement is not definitional; the diversity coefficient could have turned out low. The measurement is real. The underlying concern (overclaiming) is retained in Major weaknesses above, but the "tautological" framing is removed as it misrepresents what the paper does.

2. **From Harsh Critic: "Table 1 is not visible (parser artifact)."** — This is a parser rendering issue, not a paper problem. The table exists in the original submission as an embedded image.

3. **From Harsh Critic: "No code or data release mentioned."** — The paper references appendices that were stripped; standard for double-blind review. This is a reproducibility concern about artifacts that would accompany a camera-ready version, not a flaw in the scientific contribution.

4. **From Harsh Critic: "The criticism of Vendi Score is mostly opinion… reads as polemical."** — This is a stylistic judgment, not an evidential critique of the paper's content. The substantive issue (lack of comparison) is retained as a Major weakness.

5. **From Strength Finder: "Principled conceptual lower and upper bounds for diversity coefficient."** — This strength conflicts with the verified weakness about the bounds not being rigorous mathematical bounds. Since the weakness is grounded (the "lower bound" is not a true minimum), this strength is moved here.

## Novel Insights

None beyond the paper's own contributions. Both the harsh critic and strength finder surface essentially the same observations that the paper itself makes: the interpretability experiments (modes, GINC) are well-executed and build confidence in the metric; the headline claim is overblown; the lack of comparison to alternatives is a gap. No reviewer identified a structural flaw or unexpected interpretation that the paper's authors appear to have missed.

## Suggestions

1. **Reframe the paper's contribution honestly.** Replace "Demonstrates LLMs are pre-trained on formally diverse data" in the title and abstract with a framing that emphasizes what the paper actually contributes: extending Task2Vec to NLP, validating its behavior through controlled experiments, and providing a ranked measurement of existing pre-training datasets. The relative comparison across datasets (web-crawl vs. specialized) is the genuinely novel empirical finding.

2. **Add at least one comparison to an alternative metric.** If adding a full Vendi Score experiment is infeasible, even a small-scale comparison on 3–5 datasets would demonstrate whether the Task2Vec coefficient captures different information or provides better calibration than the alternative. Without this, the paper cannot substantiate even the qualified comparative claims in Section 5.

3. **Rename the "conceptual bounds" to "reference datasets" or "intuitive extremes."** This would eliminate the misleading implication of mathematical tightness while retaining their value as interpretability aids.

4. **Either remove the downstream pretraining experiment or substantially expand it.** As it stands (3 models, no controls, no confidence intervals), it is too thin to support any claim, even a conjectural one. Either cut it entirely (since it is not central to the paper's contribution) or add proper controls, multiple model sizes, and more granular diversity variations.

5. **Add a brief confounder analysis** checking whether the diversity coefficient is driven by sequence length or tokenizer choice, and report whether these factors correlate with the measured rankings.

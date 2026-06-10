## Summary

This paper proposes SemInfo, an information-theoretic objective for unsupervised constituency parsing that maximizes the information between constituent structures and sentence semantics (estimated via substring preservation statistics from an LLM paraphraser). The method operationalizes "semantic information" through a bag-of-substrings model over paraphrases, using maximal-substring frequency and inverse-document-frequency within a PWI framework. Applied to PCFG induction via a TreeCRF + REINFORCE formulation, the method reports average gains of 7.85 sentence-F1 across five PCFG variants and four languages, achieving new SOTA in English, Chinese, and French.

## Strengths

- **Strong and consistent empirical evidence**: SemInfo-trained PCFGs outperform LL-trained counterparts in 17/20 variant–language combinations (two-tailed t-test, p<0.05), with average gains of 13.09 (English), 6.02 (Chinese), 7.31 (French), and 4.92 (German) sentence-F1. The evaluation spans five PCFG architectures × four languages with three seeds each, which is unusually thorough.

- **Compelling correlation analysis**: Sentence-level Spearman correlations between SemInfo and sentence-F1 are ρ ≈ 0.6–0.9 across eight independently trained models, compared to ρ ≈ 0 for LL. Corpus-level analysis shows that LL's correlation with accuracy decays over training while SemInfo's remains strong. This provides a clear empirical explanation for why SemInfo is a better training objective.

- **Principled solution to the nested-substring counting problem**: The maximal-substring definition (Equation 4) correctly addresses the over-counting issue illustrated in Figure 2, where naive substring frequency inflates counts due to nesting. This is a genuine methodological contribution grounded in the observation that constituent substrings are nested.

- **Novelty and scope**: The paper is the first to formulate an information-theoretic training objective (rather than a decoding/reranking heuristic) using paraphrase-derived signals for PCFG induction, and demonstrates that the approach can be combined with existing PCFG architectures without architectural changes.

## Weaknesses

### Major

- **The training objective conflates SemInfo with entropy regularization, and no ablation isolates the source of improvement.** Equation 6 contains three components: the log-likelihood term log Z(x), a REINFORCE term with SemInfo as reward (with average baseline), and an entropy regularization term βH(P(t|x)). The LL-only baseline optimizes only log Z(x). Therefore, the comparison does not separate the effect of the SemInfo reward from the entropy regularizer. The observed gains could be partially or entirely due to entropy regularization encouraging exploration in the parser distribution — a standard technique. An ablation training with (LL + entropy regularization, no SemInfo reward) is necessary to attribute the 7.85-point improvement to SemInfo specifically. Without it, the headline claim that "SemInfo maximization improves parsing accuracy by 7.85 points" is not cleanly supported by the experimental design.

- **Critical hyperparameters and experimental details are missing, undermining reproducibility.** The number of paraphrase samples N (used in the Monte Carlo estimate of P(s|Sem(x)), Equation 171–174), the entropy regularization coefficient β (Equation 6), and the content of the "eight semantic-preserving prompts" (Section 4.1) are all unspecified. Since the method's core signal — the SemInfo values — depends on these parameters, the experimental configuration cannot be reproduced or independently verified. These are not trivial implementation details; they directly affect the quality of the SemInfo estimate and the optimization dynamics.

- **The method underperforms a simpler baseline on German without adequate analysis.** SemInfo-trained PCFGs underperform the MTD baseline (which uses SemInfo only at decoding time, without training) on German (Section 4.1). The paper offers a speculative vocabulary-shift explanation without supporting evidence. This is the one language where the method's core claim — that SemInfo is a useful training signal — is not supported, and the paper does not provide a diagnostic analysis (e.g., corpus-level lexical overlap, stemming side effects on German morphology) to understand why.

### Minor

- **The maximal-substring definition creates a blind spot for faithful paraphrases.** If a paraphrase preserves a large contiguous chunk of the original sentence verbatim, all shorter substrings within that chunk are excluded from being counted as maximal (by Equation 4). This means faithful paraphrases yield *fewer* maximal substrings for fine-grained constituents than loose paraphrases, creating an inverse relationship between paraphraser faithfulness and the metric's informativeness for smaller constituents. The paper does not discuss this trade-off or analyze how paraphraser diversity (8 prompts) mitigates or fails to mitigate it.

- **The theoretical framing overstates what is being measured.** The paper frames SemInfo as "information between constituent structures and sentence semantics" grounded in PWI. What is actually measured is substring preservation statistics of a specific LLM paraphraser (GPT-4o-mini) under particular prompts. While this is a useful and creative operationalization, the quantity conflates genuine semantic preservation, paraphraser-specific biases (e.g., preserving named entities or fixed expressions), and surface-form coincidence. The information-theoretic framing gives a veneer of rigor to what remains an empirical heuristic, and the paper would be stronger if it acknowledged this gap.

- **The snowball stemmer is applied uniformly across four languages with different morphological properties.** German has productive compounding and inflectional morphology; stemming could destroy morphological cues that indicate constituent boundaries. The paper does not discuss whether stemming is equally appropriate for all four languages or analyze its effect on the maximal-substring computation for morphologically richer languages.

### Trivial

- The normalizing constant C in Equation 5 is mentioned but its value or computation is not specified. Since SemInfo is used as a reward in REINFORCE (where additive constants cancel with the baseline), this likely does not affect results, but the omission is a blemish on an otherwise detailed exposition.

## Nice-to-Haves

- Repeating the sentence-level correlation analysis (Section 4.3) on models trained with the SemInfo objective (not just LL-trained models) would strengthen the claim that SemInfo is a useful training signal, not just a useful evaluation metric.
- Replacing GPT-4o-mini with an open-weight model (e.g., Llama 3) for at least one language would demonstrate that the method is not dependent on a specific proprietary API.
- A more detailed analysis of the German failure case (e.g., comparing corpus-level lexical overlap between training/test sets across languages, or ablating the stemmer for German) would strengthen the paper's overall claims.

## Removed Points

These points were surfaced by the reviewers but are removed here as they do not constitute valid weaknesses under the review criteria:

- *Statistical testing with n=3 has low power*: The reviewer notes this but acknowledges the effect sizes must be very large (consistent with reported gains). The fact that 17/20 conditions reach p<0.05 with n=3 speaks to the strength of the results, not a weakness. Removed.
- *Sentence-level correlation uses LL-trained models, not SemInfo-trained models*: This is a deliberate design choice — showing that SemInfo correlates with accuracy even on models trained with a different objective is stronger evidence of its utility as a metric. Removed.
- *Learning rate, batch size, training steps not specified*: Standard hyperparameters that would accompany code release; the paper states code will be released. Removed as a trivial reproducibility nitpick.
- *Constant C in Equation 5*: The critic acknowledges this "may not matter" since SemInfo is used for ranking. Removed from weaknesses; kept in Trivial for completeness.

## Novel Insights

The most interesting observation to emerge from synthesizing the reviews is the tension between the paper's two central claims — that SemInfo is both (a) a good *evaluation metric* for parsing accuracy (supported by the correlation analysis, which is robust and well-designed) and (b) a good *training objective* (where the evidence is weaker due to the conflated objective). The correlation analysis (a) is the paper's strongest contribution and could stand alone as a finding: semantic information estimated via paraphrases reliably tracks parsing quality. The training objective (b) is where the methodological ambiguity lies. A productive way forward would be to view the training results as a proof-of-concept that this signal *can* drive optimization, while being explicit that the gains may partly reflect known regularization benefits. This reframing would make the paper's contributions more defensible without diminishing their empirical value.

## Suggestions

1. **Critical: Add an ablation** training PCFGs with (LL + entropy regularization, no SemInfo reward) at the same β value used in the full method. This single experiment would resolve the most important ambiguity in the paper. If the ablation matches the full method's gains, the mechanism is entropy regularization; if not, the SemInfo-specific contribution is isolated.

2. **Specify all missing hyperparameters**: Report N (number of paraphrase samples), β (entropy coefficient), and disclose the eight paraphrase prompts in an appendix or the final version.

3. **Diagnose the German failure case**: Compute corpus-level lexical overlap metrics for German vs. other languages, or ablate the snowball stemmer on German to check for destructive interactions with the maximal-substring computation.

4. **Acknowledge the maximal-substring limitations**: Discuss how paraphraser faithfulness affects the metric, and ideally provide a controlled analysis comparing SemInfo under verbatim vs. loose paraphrasing conditions.

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Reject</decision>
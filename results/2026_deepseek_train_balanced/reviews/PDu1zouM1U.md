Now I have all the information I need. Let me write the final consolidated review.

## Summary
This paper applies the existing Pyramidal Recursive learning (PyRv) method — originally designed for subword-to-word composition — to compose word-level fastText embeddings into multi-word representations. The resulting PyRv+FT is evaluated on Croatian UPOS and DEPREL tasks, compared against a simple averaging baseline. The paper reports that PyRv+FT outperforms averaging on both tasks and beats single-word embeddings on DEPREL (77% vs 71%).

## Strengths
- **Convincing empirical gap between PyRv+FT and averaging on two tasks.** On DEPREL, averaging five word embeddings collapses accuracy to 34% while PyRv+FT achieves 77% — not only above averaging but also above the single-word baseline of 71% (lines 102–104). On UPOS, averaging three words drops to 61% while PyRv+FT retains 93% (lines 90–100). These are clear, large-margin improvements.
- **Per-class breakdown reveals which syntactic relations benefit from composition.** The analysis of punct, conj, and acl classes (lines 110–116) is informative: for conjuncts, single-word F1 is 0.03 (nearly impossible without context), averaging raises it to 0.32, and PyRv+FT reaches 0.64 — a 21.85× improvement over the single-word baseline. This granularity shows PyRv captures context-dependent relations qualitatively differently from averaging.
- **Positioning against three families of prior work.** The paper clearly distinguishes PyRv from averaging methods (Joulin et al., Arora et al.), syntax-dependent recursive models (Socher et al.), and supervised hierarchical models (Zhao et al.), noting PyRv is simultaneously hierarchical, unsupervised, and does not require parse trees (lines 34–38).

## Weaknesses

### Major

- **No comparison against any other learned composition method — the single strongest baseline is absent.** The paper compares PyRv+FT (a trained, learned composition function) only against mean averaging (a fixed operation with zero parameters). This does not establish that PyRv+FT is better than alternatives such as weighted averaging with post-processing (Arora et al., 2017, cited in the paper), recursive neural networks (Socher et al., 2013, cited), or even the original subword-level PyRv (Babić & Meštrović, 2024). The paper claims "superior ability" and claims to "introduce" a method, but without comparisons to other learned methods, the reader cannot tell whether PyRv+FT adds value beyond the fact that a trained function beats an untrained one. The paper itself acknowledges this gap only in passing in the conclusion ("future work could include comparison with more composition methods," line 150), but this does not excuse its absence from the main evaluation.

- **Method is critically underspecified.** The paper states that PyRv+FT is "trained on Croatian Wikipedia texts... for 10 epochs" (line 47) but provides no details about: (1) the PyRvNN architecture (layer count, hidden dimensions, activation functions), (2) the training objective (language modeling? reconstruction? classification?), (3) whether fastText word vectors are frozen or updated during training, (4) how the recursion order is determined for N input words, or (5) how variable-length inputs are handled. Since the paper's entire empirical contribution hinges on applying a specific method, failing to specify it makes the results difficult to interpret, reproduce, or build upon.

- **No train/validation/test split reported.** The hr500k dataset is described in terms of total counts (901 texts, 24,763 sentences, 499,635 tokens; line 56), but the paper never states how this data was partitioned. Without knowing the split, accuracy and F1 numbers cannot be interpreted — they could reflect any number of possible data divisions. This is a basic reporting requirement.

- **Downstream MLP trained for exactly one epoch without justification.** Line 65 specifies "each evaluation is conducted by training the MLP for one epoch." There is no convergence check, learning curve, or early stopping. If one epoch is insufficient for the classifier to learn from the averaged embeddings (because the input signal is weaker/more diffuse), this systematically disadvantages the averaging baseline. The paper provides no analysis of whether results have stabilized, making it unclear whether the reported numbers reflect genuine model quality or an arbitrary stopping point.

### Minor

- **No variance or confidence estimates.** All results are single points. There are no multiple runs, standard deviations, or significance tests reported. While this is not uncommon in small-scale NLP papers, the large gap in DEPREL (34%–77%) would benefit from some measure of reliability.

- **No rationale for N=3 (UPOS) vs. N=5 (DEPREL).** The paper chooses different context window sizes for the two tasks without explanation. This gives the appearance of selective reporting, especially given that UPOS is acknowledged to not benefit from context (line 88: "surrounding word context does not provide significant benefits for classification").

- **PyRv+FT is not tested with N=1.** With a single word, PyRv should pass through the embedding unchanged, ideally matching the fastText single-word baseline. Testing this would validate that the PyRv pipeline does not degrade single-word performance and would serve as a simple sanity check.

- **The qualitative analysis (Section 4.3) is shallow.** The visualization shows that phrases around prepositions "u" and "na" cluster together. This demonstrates the model has learned preposition-based grouping, but it does not probe what the hierarchical composition captures at different levels of the pyramid — which would be the natural analysis given hierarchical composition is the method's claimed strength.

- **Limited scope (single language, single task family).** All experiments are on Croatian UPOS and DEPREL. While this is stated up front, generalizability claims would be stronger with additional languages or tasks.

### Trivial

None.

## Nice-to-Haves
- A comparison with the original subword-level PyRv (Babić & Meštrović, 2024) would be the most natural baseline and would clarify whether word-level composition benefits from the PyRv architecture.
- An analysis of computational cost (parameters, runtime) relative to alternatives would strengthen the "lightweight" claim in the abstract.
- Testing multiple N values systematically (N=1, 2, 3, 4, 5) across both tasks would remove the appearance of selective N selection.
- Releasing the trained PyRv+FT weights and training code would aid reproducibility.

## Removed Points
These are points from the reviews that were filtered; treat them with caution.
- *"Tables are images that cannot be read from the text"* — This is a parser artifact from PDF extraction; the original submission has proper tables. Removed per hard rule.
- *"Abstract highlights only DEPREL and omits UPOS"* — A framing observation, not a substantive weakness. Removed.
- *"Code and trained models not mentioned as available"* — Reproducibility nitpick of the sort the instructions flag for removal.
- *"Averaging baseline degradation is not explained"* — The paper does offer an explanation ("loss of word order and syntactic structure," line 104). The critic's stronger claim that it is "not explained" is inaccurate.
- *"Missing related works"* — Removed per hard rule (cannot verify external sources).

## Novel Insights
None beyond the paper's own contributions. The most interesting finding — that PyRv+FT on DEPREL outperforms even single-word embeddings (77% vs 71%), while averaging the same context words collapses to 34% — is already presented in the paper. The reviews do not surface any genuinely novel reinterpretation of this result.

## Suggestions
1. Add at least one learned composition baseline — weighted averaging (Arora et al., 2017) is the most natural because it is simple, cited in the paper, and directly addresses whether PyRv's hierarchical recursion adds value beyond a smarter non-hierarchical approach.
2. Report the train/dev/test split used for the hr500k dataset and train the downstream MLP to convergence with early stopping, not a fixed one epoch.
3. Specify the PyRvNN architecture, training objective, and key hyperparameters in full. Without this, the paper's method is not reproducible.
4. Report results over at least 3 random seeds with standard deviations.

## Score and Decision

MY FINAL SCORE: <score>3.5</score>
MY FINAL DECISION: <decision>Reject</decision>
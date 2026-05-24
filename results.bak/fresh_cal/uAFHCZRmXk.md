All reviewer claims are verified against the paper. Now I will produce the consolidated final review.

---

## Summary

This analysis paper investigates two well-known phenomena in contrastive vision-language models (VLMs): the **modality gap** (separation of image/text embeddings) and the **object bias** (better performance on objects than attributes). Through a combination of large-scale correlational analysis (98 VLMs), controlled synthetic experiments on a novel Morpho-MNIST-derived dataset (MAD), and real-data experiments on CC12M, the paper identifies a **common root cause: information imbalance** between images and captions. It introduces two new metrics (RMG for the modality gap, MOAD for object bias), demonstrates that only a few embedding dimensions drive the gap, shows that object bias is a per-sample caption-presence phenomenon rather than a global frequency effect, and reveals a functional connection between the modality gap and logit entropy (suggesting the gap can be a feature, not just a bug).

## Strengths

- **Identifies a single unifying cause (information imbalance) for two previously disconnected phenomena.** The paper provides strong causal evidence using the synthetic MAD dataset where information imbalance is directly manipulated (varying the number of attributes in captions while keeping images fixed). Figure 6 (fig:miniCLIPall) cleanly shows that increasing shared information simultaneously reduces the modality gap, reduces object bias, and improves accuracy. This goes beyond prior work that treated these phenomena independently.

- **Introduces principled new metrics (RMG and MOAD) that address limitations of prior measures.** RMG (Eq. 2, line 178) accounts for intra-modality spread when measuring the gap, overcoming L2M's failure to consider the effective space used. MOAD (Eq. 3, lines 306–311) disentangles bias from task difficulty by measuring whether objects or attributes have greater influence on matching vs. non-matching similarity, and is generalizable to other concept pairs.

- **Demonstrates via large-scale analysis (98 VLMs) that the relationship between the modality gap and performance is confounded by model/embedding size.** Table 1 (tab:performance_correlations) reports Kendall-τ correlations showing that model size, embedding size, and dataset size dominate any direct effect of the gap. When controlling for confounders, a smaller gap does correlate with better performance — a nuanced finding that clarifies prior contradictory results.

- **Shows that object bias is a per-sample caption-presence bias, not a global word-frequency effect.** Figure 5a (fig:obj_attr_frequencies) demonstrates that attribute words appear *more often* than object words in LAION-2B captions, disproving the frequency hypothesis. The controlled MAD experiment (Fig. 5b, fig:caption_presence_bias) then shows that the model becomes biased toward whichever factor is always present in the caption, cleanly validating the per-sample presence explanation.

- **Provides a mechanistic understanding of the modality gap's functional role through the "bug or feature" experiment.** The fine-tuning experiment on CC12M (Fig. 7, fig:temp_rmg_ent_rel) shows that when temperature is frozen, the model increases the modality gap substantially to match the same logit entropy as a learnable-temperature model. This reveals the gap as a flexible mechanism for controlling entropy, supporting the carefully-scoped claim that the gap "can be interpreted as a feature."

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **The real-data caption truncation experiment (Sec. 6.1, lines 463–469) may confound information quantity with information type.** The paper drops contiguous parts of CC12M captions to create information imbalance. This manipulation could disproportionately remove attribute mentions (which tend to appear later in captions) relative to object mentions (which appear early). If so, the resulting imbalance is not purely about *amount of information* but also about *type of information removed*, which could affect object bias measures independently of information imbalance per se. The synthetic experiments control for this confound and provide the primary causal evidence, so this does not threaten the paper's core claims, but it would strengthen the real-data evidence to discuss or verify that truncation does not systematically alter object vs. attribute token frequencies.

- **The "strengthening the paper" suggestions in the harsh critic are real but minor:** probing the semantics of the gap-driving dimensions (whether they correspond to identifiable visual/textual properties) and evaluating whether reducing information imbalance actually improves real attribute recognition performance. These are acknowledged as directions for further work, not gaps in the current paper.

### Trivial

None.

## Nice-to-Haves

- A discussion of whether the two main gap-driving dimensions correspond to interpretable visual or textual properties (e.g., image brightness, text formality) would deepen understanding, though the paper's current evidence (that they exist and their removal disrupts neighborhoods) is sufficient for its claims.
- A real-data extension that enriches captions (e.g., using a VLM to add attribute descriptions) and directly measures the impact on attribute recognition would be the most direct validation of the paper's practical recommendations.

## Removed Points

- **Strength Finder's figure/equation number references (e.g., "Figure 3", "Equation (3)", "Figure 5a")** — These are out of sync with the paper's actual numbering (the relevant content is present in the paper under different figure numbers). The content described is accurate; the numbering discrepancies are extraction artifacts. Retained as strengths but without specific number references.

- **Generic strength formulations removed:** "this paper addressed an important problem" — dropped as generic. All retained strengths have specific, concrete content anchored to the paper's figures, tables, or equations.

## Novel Insights

The key insight that emerges from synthesizing the reviews is that the paper's main contribution is **explanatory unification with causal validation**: prior work documented the modality gap (Liang et al.) and object bias (Bravo et al.) as separate pathologies, but the paper demonstrates they share a common mechanistic origin in information imbalance, validated through controlled interventions. The additional finding that the modality gap plays a *functional* role in controlling logit entropy — such that models with frozen temperature *increase the gap* to compensate — reframes the gap from a pure artifact to a learned mechanism with a purpose. This last point is particularly novel because it reconciles the seemingly contradictory observations that the gap exists (suggesting a bug) yet correlates positively with performance at scale (suggesting it is harmless or even beneficial). The resolution: the gap is a flexible control parameter for entropy, and its presence is not inherently problematic — what matters is the underlying information imbalance.

## Suggestions

- **Address the caption truncation confound** in a camera-ready version: either add a control experiment verifying that truncation does not systematically change object vs. attribute token frequencies, or add a discussion acknowledging this as a limitation of the real-data experiment.
- **Optionally probe the semantics of the gap-driving dimensions** — even a brief analysis (e.g., correlation with image statistics or text formality scores) would strengthen the mechanistic story, though the paper's current evidence is already sufficient.

## Score and Decision

This paper makes a significant contribution to the VLM understanding literature. It moves beyond documenting effects to explaining their origin through careful causal experiments, introduces reusable metrics, and provides nuanced findings (e.g., that reducing object bias does not directly improve attribute performance because overall model improvement is a stronger driver). The only verifiable weakness is a minor potential confound in one real-data experiment that does not threaten the paper's core claims (which are primarily supported by the controlled synthetic experiments). The paper is well-written, appropriately scoped, and does not overclaim. It is ready for publication.

MY FINAL SCORE: <score>9.0</score>
MY FINAL DECISION: <decision>Accept</decision>
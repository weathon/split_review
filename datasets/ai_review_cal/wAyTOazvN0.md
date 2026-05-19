- Decision: Reject
- Avg Score: 5.75
- Scores: 5, 6, 6, 6
Now I have a thorough understanding of the paper. Let me produce the consolidated review.

## Summary

The paper proposes METERN, a framework for learning multiplex (relation-specific) embeddings on text-rich networks using a single shared pretrained language model encoder plus lightweight relation prior tokens. The key idea is to prepend relation-specific learnable tokens to the input text, allowing one encoder to produce different embeddings for different semantic relations (e.g., "cited-by," "same-author") while sharing knowledge across relations. The paper evaluates on nine tasks across five networks (academic and e-commerce domains) and reports that METERN outperforms baselines including single-embedding models (SPECTER, Vanilla FT) and multiplex GNNs (DMGI, HDMI).

## Strengths

1. **Empirical demonstration of semantic shift across relations (Figure 2, Section 3)**: The paper quantitatively shows that a BERT embedding fine-tuned on one relation (e.g., "cited-by") performs poorly when evaluated on another relation (e.g., "same-venue"), with PREC@1 varying from ~0.40 to ~0.82 across relation pairs. This directly motivates the need for multiplex (relation-specific) embeddings and is a clean, compelling experiment.

2. **Parameter-efficient architecture (Section 4.1, Table 6)**: METERN uses only 0.4% more parameters than Vanilla FT (110.1M vs. 109.7M) yet produces separate embeddings per relation, while maintaining comparable training time. The relation prior tokens ($m \ll p$) are a lightweight but effective design choice for capturing relation-specific signals without scaling the encoder.

3. **Interpretable learned relation-task correlations (Figure 3, Section 5.5)**: The attention-based mix-up mechanism automatically assigns different learned weights to source relations for different downstream tasks (e.g., "same-author" and "same-venue" for citation prediction; "cited-by" and "co-cited-by" for paper recommendation). This provides evidence that the mechanism works as intended and yields interpretable insights.

4. **Broad evaluation scope**: The paper evaluates on five datasets across two domains (academic and e-commerce) with nine downstream tasks, covering retrieval, classification, and regression settings. METERN consistently outperforms or matches baselines across most tasks, suggesting the approach generalizes.

## Weaknesses

### Fatal
None.

### Major

1. **Underspecified downstream evaluation protocol for baselines on classification/regression tasks (Tables 4–5)**. For the matching/retrieval tasks (Tables 1–3 and paper recommendation), the evaluation is straightforward (embedding similarity / nearest-neighbor). However, for the 5 classification and regression tasks (paper classification, citation prediction, year prediction, item classification, price prediction), the paper states that METERN "learns to select source relations" by training $Q_{\text{target}}$ parameters on downstream labels, but **never specifies how the single-embedding baselines (SPECTER, Vanilla FT, Sentence-Transformer, OpenAI-ada-002) or multiplex baselines (MTDNN, DMGI, HDMI) are adapted to these tasks**. The reader cannot tell whether:
   - A linear classifier is trained on top of frozen baseline embeddings
   - The entire baseline model is fine-tuned on the task
   - Hyperparameters are tuned separately per baseline-task pair
   
   Without this information, the comparisons in Tables 4–5 are not replicable, and METERN's advantage could partly stem from a more favorable adaptation protocol rather than better embeddings. The paper should specify (even in a brief table or paragraph) what classifier/regression head was used for each baseline and how it was trained.

2. **No variance or statistical significance estimates for any reported result**. All numbers in Tables 1–5 are single-point estimates. The paper repeatedly uses the phrase "significantly and consistently outperforms" — a statistical claim — without providing standard deviations, confidence intervals, or significance tests. This matters because some margins are small (e.g., on Geology citation prediction, the difference the critic identifies is 0.474 vs. 0.463). Without variance information, the reader cannot distinguish genuine improvement from noise. Adding error bars over multiple seeds (3–5 runs) for the main results would substantially strengthen the empirical claims.

### Minor

1. **Absence of an ablation quantifying the benefit of the learned selection mechanism (Section 5.5)**. The "learn to select source relations" module is a core contribution, but there is no comparison against simpler alternatives: (a) a uniform mixture of all source relation embeddings, or (b) manually picking the single best relation. Adding such an ablation would directly quantify the value of the learned attention weights and strengthen the method's motivation.

2. **The $w_r$ relation weight (Section 5.8) introduces dataset-specific tuning without a clear procedure**. The paper shows that tuned weights ($[1,2,2,1,1]$) improve over uniform weights ($[1,1,1,1,1]$) on Geology, but does not specify how these weights were selected (e.g., grid search range, validation criterion) or whether the same weights transfer to other datasets. This makes it unclear whether the weight tuning is a practical burden or a one-time calibration.

3. **Figure 2 (Section 3) motivation could be more precisely scoped**. The experiment fine-tunes BERT on one relation and tests on another — this demonstrates the failure of single-*relation* fine-tuning, not directly of single-*embedding* training on all relations simultaneously (the latter is what Vanilla FT does). The paper's argument is still valid (the Vanilla FT vs. METERN comparison in Tables 1–2 addresses this), but the text could clarify this distinction to avoid over-interpretation of Figure 2.

### Trivial
- The paper should specify for the direct inference tasks (Table 3) whether query and candidate documents are both encoded with the same relation prior tokens (this is implied but not stated).

## Nice-to-Haves

- **Ablation on the number of prior tokens $m$**: The paper assumes $m \ll p$ but does not show empirically that $m=1$ or $m=2$ is sufficient, or whether more tokens increase expressiveness.
- **Fine-tuned baselines for direct inference (Table 3)**: Adding a column where single-embedding baselines are fine-tuned on the downstream task would provide an additional reference point, though the current zero-shot comparison is already fair and informative as labeled.
- **Discussion of failure cases**: METERN does not outperform on cop prediction (Home, Sports) and has small margins on some tasks. A brief analysis would give a balanced view.

## Removed Points

- **"Unfair framing of direct inference comparison"** (Harsh Critic point #3): Removed because the comparison is correctly framed as zero-shot direct inference for all methods. METERN's advantage from having relation-specific embeddings is exactly the point being demonstrated; Table 3 is labeled "Direct inference with an evident source relation (no task-specific training)." The paper is transparent about the setting. Suggesting baselines be fine-tuned would change the evaluation from zero-shot to supervised, which is a different experiment (moved to Nice-to-Haves above).
- **"No analysis of negative sampling strategy"**: The paper explicitly states it uses in-batch negatives (Karpukhin et al., 2020). A deep analysis of false negatives is beyond the paper's scope and not standard practice for contrastive learning papers at this venue. Removed as scope creep.
- **"Missing appendix, missing proofs"**: The parser strips appendix sections from all papers. These exist in the original submission. Removed per instructions.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the same issues the paper acknowledges or could address, without adding unexpected analytical angles.

## Suggestions

1. **Add error bars (standard deviations over multiple random seeds) to all main tables** — this is the single highest-impact improvement for the paper's credibility. Even 3 seeds would help.
2. **Specify the downstream adaptation protocol for baselines in Tables 4–5** — a short paragraph or table describing the classifier type, training procedure, and hyperparameter tuning for each baseline-task pair is essential for reproducibility and fairness.
3. **Add an ablation comparing the learned selection weights against a uniform mixture and against the single best relation** to directly quantify the benefit of the attention mechanism.
4. **Clarify how $w_r$ weights are tuned** (search range, validation criterion) and whether the same weights are used across datasets or re-tuned per dataset.

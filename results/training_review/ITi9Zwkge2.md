I now have all the information needed to write the consolidated review. Let me compile it.

---

## Summary

This paper proposes HATFormer, a transformer-based encoder-decoder system (built on TrOCR) for historical Arabic handwritten text recognition (HTR). The contributions include: (1) a BlockProcessor that preserves aspect ratio and aligns image rows to ViT patch boundaries to avoid information loss from standard ViT resizing, (2) a custom Arabic BBPE tokenizer trained on an Arabic corpus for more compact text representation, (3) a two-stage training pipeline using synthetic printed Arabic data followed by fine-tuning with an overtraining strategy. On the Muharaf historical dataset, HATFormer achieves 8.6% CER (a 51% relative improvement over the 17.6% CER of the best prior baseline), with ablation experiments confirming each component's contribution.

## Strengths

- **Strong empirical result on the primary task.** HATFormer achieves 8.6% CER on the largest public historical Arabic handwriting dataset (Muharaf), a 51% relative improvement over the best published baseline (Saeed et al., 17.6%). This is a clear and practically valuable advance.
- **Controlled ablation study confirms the necessity of each proposed component.** Removing the BlockProcessor (+11.4% CER), the custom tokenizer (+10.9% CER), synthetic Stage-1 pretraining (+4.2% CER), and overtraining (+1.3% CER) all degrade performance. Starting from random weights yields 86.0% CER. The ablation provides quantitative evidence that each design choice contributes to the reported gains.
- **Cross-dataset evaluation demonstrates generalization.** When trained on historical Muharaf and tested on modern KHATT, HATFormer (27.5% CER) outperforms Saeed et al. (33% CER) by 16.7% relative, showing that the system learns transferable features.
- **Comprehensive evaluation scope.** The paper evaluates on three datasets (Muharaf, KHATT, MADCAT) with cross-dataset experiments, ablation, and a factor/sensitivity study covering synthetic data size, beam width, and length penalty.
- **Open-source commitment.** The authors plan to release the image processor, tokenizer, model weights, synthetic dataset, and source code, which would benefit the Arabic HTR community.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **The claim that the attention mechanism specifically addresses the three intrinsic Arabic challenges (cursive, context-dependent shapes, diacritics) is asserted but not directly tested.** The abstract states that HATFormer "captures spatial contextual information to address the intrinsic challenges of Arabic script through differentiating cursive characters, decomposing visual representations, and identifying diacritics," and contribution #2 claims the method "has proven effective by leveraging the attention mechanism to address three intrinsic challenges." However, no experiment isolates the role of attention in handling these specific challenges. The ablation study tests system-level components (BlockProcessor, tokenizer, synthetic data, overtraining), and the comparison against CRNN baselines is between full architectures, not a controlled test of attention. The attention maps (Figure 4) are mentioned but not analyzed in relation to the three challenges. The authors should either weaken these causal claims or provide a targeted experiment (e.g., comparing against a non-attention encoder under identical preprocessing/training).

- **The MADCAT result is described as "comparable" (4.2% CER) when the best baseline (Rawls et al.) achieves 1.5% CER — a nearly 3× difference.** The paper does explain that text normalization during evaluation likely accounts for much of the gap and that the system was not optimized for MADCAT (as it is not a historical dataset). However, "comparable" is an overstatement. The abstract's phrasing "attains a comparable CER of 4.2%" should be revised to "reports a CER of 4.2%" with an explicit caveat that direct comparison is complicated by evaluation protocol differences and that the system was not specifically tuned for this dataset.

- **Hyperparameters and variance for the retrained Saeed et al. baseline are not reported.** The paper states "For Saeed et al., we retrained their model on each dataset for a fair comparison" (line 172) and provides the dataset split for Muharaf (85-15-5). However, the specific hyperparameters used for retraining are not disclosed, and no variance/runs-over-seeds are reported. Since the headline 51% improvement depends on this comparison, reporting these details would strengthen reproducibility. (Dataset splits are reported; the critic's claim that splits are missing is incorrect.)

- **The tokenizer ablation leaves an implementation detail unclear.** When replacing the custom Arabic BBPE tokenizer with the ASCII-biased GPT-2 tokenizer (which has a different vocabulary size), it is not stated whether the embedding/output layer was re-initialized or fine-tuned. This is a minor clarity gap, but given the 10.9% CER swing, specifying this would remove ambiguity. (The broader concern that the ablation is "confounded" because vocabulary size changes is inherent to tokenizer comparisons and does not invalidate the ablation.)

- **No learning curves or convergence plots are shown for the overtraining strategy.** The paper claims that training past the validation loss plateau improves performance (1.3% CER), which is a non-standard practice worth visualizing. Showing validation CER and loss curves over time would make this claim more convincing and help readers adopt the technique.

- **The BlockProcessor is ablated only as a whole, not as individual sub-components.** The ablation shows a combined 11.4% CER increase, but it is unclear how much each sub-component contributes (horizontal flipping, height standardization to 64px, aspect-ratio-preserving padding). Component-level ablation would strengthen the design rationale.

### Trivial

- The 300% token count reduction for the custom BBPE tokenizer is claimed but not quantified in a dedicated table or figure. A brief comparison table would be helpful.
- The paper states "51% improvement" and "23--51% improvement" — these are different phrasings for the same calculation. Minor consistency issue.

## Nice-to-Haves

- Isolating the BlockProcessor components (flipping, height standardization, aspect-ratio preservation) in separate ablations.
- Showing synthetic image examples alongside real historical handwriting to illustrate the domain gap and font/augmentation choices.
- A character-level confusion matrix to reveal which Arabic challenges (diacritics, specific character confusions) remain unsolved.
- Reporting CER variance across 3–5 random seeds for the main result and key ablations.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Criticism that the paper "does not report the splits" for the retrained baseline.** The paper explicitly reports the Muharaf split (85-15-5) in line 165. This sub-point is factually incorrect.
- **Criticism that the tokenizer ablation is "confounded" because changing vocabulary size and sequence length invalidates the comparison.** Changing tokenizers inherently changes vocabulary size and sequence length — that is the entire point of a tokenizer ablation. This is not a confounding factor; it is the measured treatment. The only genuine concern (whether the model was re-initialized) is retained above.
- **Criticism that the paper does not provide controlled evidence isolating attention's role when comparing transformers to CRNN baselines.** The paper does compare the full transformer system against CRNN-based baselines and shows substantial improvements; while this is not a controlled ablation of attention per se, it is reasonable comparative evidence in the context of a system paper. The claim is retained as a Minor weakness because it is somewhat overstated, but the critic's framing that it is "unvalidated" is too severe.
- **Request for removing MADCAT from the main results table.** The paper transparently discusses the discrepancy and scope; keeping MADCAT as a secondary evaluation is reasonable for completeness. The issue is solely with the word "comparable," which is retained above.
- **Strength Finder's generic strengths that lack specific evidence.** All three core strengths from the Strength Finder are retained as they are well-supported by the paper. The additional supporting strengths are also retained.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface an angle or connection that the paper itself does not articulate.

## Suggestions

1. **Revise the attention mechanism claim.** Either provide a controlled experiment (e.g., transformer vs. CRNN with identical preprocessing/tokenizer) or explicitly reframe this as a motivating hypothesis rather than a verified contribution.
2. **Add a brief "limitations" or "discussion" section** that acknowledges the MADCAT gap without overstating comparability, the modest effect size of overtraining, and the scope (historical Arabic) of the claimed SOTA.
3. **Report variance** for the main Muharaf result and the Saeed et al. retraining comparison, ideally with 3 runs.
4. **Disclose retraining hyperparameters** for the Saeed et al. baseline.
5. **Provide learning curves** (validation loss and CER) for the overtraining strategy to visually demonstrate the plateau-and-improve phenomenon.

## Score and Decision

This paper makes a solid engineering contribution to an under-resourced problem (historical Arabic HTR). The primary result (8.6% CER on Muharaf, a 51% improvement) is strong and supported by thorough ablation experiments. The weaknesses are about overclaimed interpretations and missing implementation details — none threaten the validity of the core empirical result. With relatively modest revisions (toning down the attention claim, clarifying the MADCAT comparison, and adding reproducibility details), this paper would be a clean contribution. 

The paper is clearly above the acceptance threshold for a reputable conference venue. The core claims are supported, the experiments are thorough, and the practical value is evident.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>
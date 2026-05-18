Now I have all the information I need. Let me write the consolidated review.

## Summary

The paper proposes a zero-shot method for transferring continuous prompts across language models. The key idea is to encode source prompts as cosine-similarity vectors relative to shared anchor token embeddings, then search for target prompt embeddings whose relative representations match. The method requires no task supervision on the target model and no training of neural projectors. Experiments on the LAMA factual probing benchmark across BERT, RoBERTa, and ALBERT models show improvements over discretization and neural projector baselines, and multi-source transfer provides further gains.

## Strengths

- **Novel application of relative representations to cross-model prompt transfer**: The encode-then-search strategy avoids training a neural projector or requiring task supervision on the target model. This is a genuine advancement over prior work (Su et al., 2022) that requires parallel prompts or task signals. (Section 1, Section 3)

- **Consistent improvement over baselines across most source–target pairs**: Single-source transfer outperforms the neural projector baseline on nearly all pairs in Table 3 (e.g., BERTbase→BERTlarge: 31.40% vs. 12.49%; BERTbase→RoBERTabase: 17.68% vs. 14.36%). The method also beats manual prompting on several transfers from base models. This demonstrates that relative representations can bridge different embedding spaces. (Table 3, lines 191–195)

- **Empirical validation of the core intuition**: Figure 3 shows that as the matching loss in the relative space decreases during search, validation accuracy increases consistently across all source–target combinations. This directly validates the central claim that better relative-space alignment leads to better transfer. (Figure 3, lines 234–238)

- **Multi-source transfer shows promise**: Dual-source settings (BERTbase+BERTlarge, BERTbase+RoBERTabase) improve over single-source in several cases (e.g., BERTbase+BERTlarge → RoBERTabase: 27.60% vs. BERTbase alone 17.68%). The idea that aggregating prompts from multiple models can produce more robust task semantics is novel in this setting. (Table 3, lines 199–200, Section 3.4)

- **Ablation studies provide actionable guidance**: Analysis of anchor count (Figure 5a) shows performance improves with more anchors up to a point, and prompt length analysis (Figure 5b) shows robustness between 3–5 tokens. The normalization ablation (Figure 4) confirms its critical role in cross-model transfer. (Figures 4–5, lines 247–265)

## Weaknesses

### Fatal

None.

### Major

- **Evaluation is limited to a single task (LAMA factual probing), yet the paper's claims are broad.** The title refers to "Generalizing Task Semantics Across Language Models" and the abstract claims "task semantics in continuous prompts can be generalized across various language models." However, all experiments are on LAMA, which tests factual associations — a specific type of knowledge, not a broad range of "task semantics." Whether the method transfers to other tasks (sentiment classification, NLI, generation, etc.) is entirely unknown. This gap between claims and evidence is the paper's most significant weakness. The 41 sub-tasks within LAMA provide diversity within one task family, but they do not substitute for evaluation across different tasks. (lines 4–5, 115–117, 284)

- **No variance or statistical significance measures reported anywhere.** All results in Table 3 are point estimates. The multi-source improvements are often 1–2 absolute percentage points (e.g., BERTbase+RoBERTabase → ALBERTbase: 27.13 vs. best single 26.11; → ALBERTlarge: 26.54 vs. 24.72). Without standard deviations, confidence intervals, or significance tests, it is impossible to know whether these gains are meaningful or within noise. Since the method involves random initialization of target prompts and gradient-based optimization, variance could be non-negligible. (Table 3, lines 199–200, 218)

- **The neural projector baseline is under-specified, making the comparison hard to evaluate.** The paper describes the projector only as "a two-layer projector to map the source embedding space to the target one based on anchor words" (line 213). No loss function, number of training steps, regularization, learning rate, or architecture details (hidden size, activation) are provided. Without knowing whether this baseline was reasonably tuned, the claim of "largely outperforming" it is weakened. The method's advantage is genuine (consistent across pairs), but the magnitude should be interpreted with caution. The paper should also consider a simpler linear mapping baseline (standard in cross-lingual embedding alignment) to ensure the advantage is not merely due to overfitting in the projector training. (lines 212–213, 215)

### Minor

- **The shared-vocabulary requirement is a real boundary condition that is not discussed.** The method relies on a large set of shared tokens between source and target models (k=8,192 used; 17,230 shared in total). For BERT/RoBERTa/ALBERT — all BERT-family models using similar tokenization — this is feasible. But for transfer to models with fundamentally different tokenizers (e.g., GPT-2, LLaMA, T5), the overlap could be dramatically smaller. The paper's own ablation (Figure 5a) shows that performance degrades significantly at 512 anchors. This limitation on generality is neither acknowledged nor discussed, and no alternative anchor strategies (e.g., character-level, subword units, or pretrained multilingual embeddings) are considered. (lines 21, 70, 261)

- **The anchor selection method is not specified.** The ablation shows that using all 17,230 shared tokens hurts performance, so 8,192 anchors were used — but how were these 8,192 selected from the 17,230? Random sampling? By frequency? This is a reproducibility gap. (lines 124, 261)

- **The normalization step (Eq. 7) is critical but lacks intuition.** The ablation shows large gains from normalization (Figure 4), but the paper provides no explanation for why matching the mean and standard deviation of target word embeddings works. A brief discussion of why relative representations discard magnitude information and why the target model's layers are sensitive to embedding scale would strengthen the paper. (Eq. 7, lines 93–97, Figure 4)

- **The multi-source results are mixed and the paper does not explain negative cases.** While multi-source improves in many cases, there are exceptions: BERTbase+RoBERTabase → RoBERTabase (43.83%) is lower than RoBERTabase single-source (45.17%). The paper attributes the multi-source improvement to "a more robust view of task semantics" but does not discuss when or why it fails. (Table 3, lines 199–200, 218)

### Trivial

- The "zero-shot" terminology could benefit from clarification. The method avoids task supervision on the target model (which is the standard meaning), but still performs gradient-based search over prompt embeddings. A brief clarification distinguishing this from other uses of "zero-shot" in NLP would prevent confusion.

## Nice-to-Haves

- Report the number of gradient steps and wall-clock time for the target-side search to help readers understand the practical trade-off.
- Include a linear regression baseline (trained on anchor embeddings), which is standard in cross-lingual embedding alignment and would strengthen the baseline comparison.
- Conduct a sensitivity experiment where the anchor set is artificially reduced to simulate low-overlap scenarios (e.g., 200 tokens) to map out the method's boundary conditions.
- For the direct transfer near-0% results (Table 1), a brief explanation of why the same-dimension embeddings fail to transfer (e.g., differences in embedding space orientation, optimization landscape) would be helpful.

## Removed Points

- **"Method is not truly zero-shot because it requires gradient-based search on the target."** — Removed. The method does not require task supervision on the target model, which is the standard meaning of zero-shot transfer. The search is unsupervised (matching relative representations), not task-specific training.
- **"Appendix is referenced but stripped; we cannot assess whether it contains additional results."** — Removed per policy. The appendix exists in the original submission; the parser removed it.
- **"Direct transfer near 0% for base-to-base is surprising — more discussion needed."** — Downgraded to Nice-to-Haves. The paper already notes that continuous prompts are not directly transferable, which is sufficient context.
- **Strength Finder's "practical focus on tuning small models for large-model inference"** — Kept. It is a genuine framing that matches the paper's content.
- **"No results for multiple random seeds"** — This is already covered in the Major weaknesses under "No variance estimates" and does not need separate mention.

## Novel Insights

Beyond the paper's own contributions, the reviews surface an interesting tension: the method's best results come from smaller source models (BERTbase, RoBERTabase) rather than larger ones (BERTlarge, RoBERTalarge). This is explained by the paper as model-specificity in larger models' expressive embedding spaces (citing Khashabi et al., 2022), but it also reframes the practical value proposition — the method is most useful in the setting where the source model is cheap to tune and the target model is larger, which is precisely the asymmetric scenario of greatest practical interest. The correlation between relative-space matching loss and transfer accuracy (Figure 3) is a clean diagnostic that future work could use as a proxy for transferability without needing task labels.

## Suggestions

1. **Expand evaluation to at least one additional task family** (e.g., sentiment classification with [MASK] templates, or NLI). This would directly address the largest gap between claims and evidence. If the method succeeds, the claims become far stronger; if it fails, the claims must be scaled back to factual probing specifically.

2. **Report variance estimates for all main experiments** (standard deviations across at least 5 random seeds). This is essential for assessing the multi-source improvements and establishing reliability of the single-source results.

3. **Fully specify the neural projector baseline** (loss function, architecture, hyperparameters, training procedure) and consider adding a linear mapping baseline. This would solidify the comparison.

4. **Acknowledge and discuss the shared-vocabulary limitation openly.** Report the overlap statistics for the tested models and address what would happen with models using different tokenization schemes. This turns a blind spot into a known boundary condition.

5. **Specify how the 8,192 anchors are selected** from the 17,230 shared tokens (by frequency? randomly?) for reproducibility.

## Score and Decision

The paper proposes a clever and well-motivated method with a clean formulation. The core idea — using relative representations to bridge prompt embeddings across models — is novel and the initial results are promising. However, the evaluation is confined to a single task type (factual probing), no variance estimates are reported, and the neural projector baseline is under-specified. The broad claims in the title and abstract ("generalizing task semantics across language models") significantly outpace the evidence provided. The multi-source results, while suggestive, cannot be properly evaluated without statistical grounding. These are not fatal flaws — the core contribution is real — but they prevent the paper from being accepted in its current form. With broader evaluation and stronger empirical methodology, this could be a solid contribution.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>
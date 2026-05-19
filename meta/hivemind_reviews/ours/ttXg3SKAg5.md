Here is the consolidated review:

---

## Summary

The paper provides a theoretical explanation for the geometry of multi-modal contrastive representation spaces, characterizing the relationship between paired embeddings as a constant orthogonal modality gap plus Gaussian alignment noise (Proposition 1). Based on this characterization, the paper proposes C³ (Connect, Collapse, Corrupt) — a three-step method that subtracts per-modality means to remove the gap and adds Gaussian noise during training to handle alignment noise — enabling cross-modal tasks (image/audio/video captioning, text-to-image generation) to be learned from uni-modal data. Experiments show strong results across multiple modalities and embedding spaces (CLIP, ImageBind), with thorough ablations confirming each component's contribution.

## Strengths

1. **Principled theoretical explanation of the modality gap.** The paper goes beyond prior empirical observations (Liang et al., Zhang et al.) by providing a structured analytical account: Lemma 1 derives the gradient structure of the InfoNCE loss and proves that no gradient flows in ineffective dimensions, and the dimensional collapse analysis explains why the gap persists after optimization. The theory is further backed by a controlled synthetic experiment (1,000 synthesized embeddings, 200K optimization steps, Figure 4) that directly confirms the predicted behavior.

2. **Strong empirical results across diverse tasks and modalities.** The generalization table (Table 5 / tab:result_generalization) shows C³ achieving BLEU-1 74.0, METEOR 26.6, and ROUGE-L 54.0 on zero-shot image captioning, with consistent improvements on audio captioning (Clotho) and video captioning (MSR-VTT) using ImageBind embeddings. Each ablated variant (C¹, C²₁, C²₂) is outperformed by C³ in every modality, providing clear evidence that both gap removal and noise regularization are needed.

3. **Cleanly designed ablation analysis that directly validates the theoretical claims.** The ablation isolates each component: C¹ (no correction), C²₁ (collapse only), C²₂ (corrupt only), C³ (both). Across all three modalities in the generalization table, C²₁ and C²₂ each improve over C¹, and C³ further improves over both — directly supporting the two-part geometry (gap + noise) that motivates the two-part correction.

4. **Demonstrated value in low-data regimes.** The semi-supervised experiments (Figure 5) show that C³ pre-training on uni-modal data provides large gains over purely supervised ClipCap when fine-tuned on 1–5% of paired data (~10 BLEU-4 points at 1%), which is a practically important result.

## Weaknesses

### Major

None. The paper's central claims are supported by evidence, and the identified issues are addressable without undermining the core contribution.

### Minor

1. **Proposition 1 is presented more definitively than the evidence supports.** The proposition states the decomposition \(e_x - e_y = c_\perp + \epsilon\) with exact constant gap, exact orthogonality, and exact isotropic Gaussian noise. The paper provides analytical lemmas (gradient structure, stable region) that explain *why* such a geometry might arise, and empirical verification (Table 1) showing the approximation holds well (e.g., \(\cos(c^{(i)}, c^{(j)}) = 0.99\) for constancy, \(\cos(\epsilon_j^{(i)}, \epsilon_k^{(i)}) = 0.00 \pm 0.10\) for isotropy). However, the lemmas do not *deduce* the exact additive form — they support its plausibility. The paper would benefit from more clearly distinguishing between the analytically proven components (gradient behavior, stable region) and the overall geometric characterization (which is an empirically supported approximation, not a theorem). The current framing is not misleading, but the proposition label implies more rigor than is actually achieved.

2. **The inference-time handling of the corrupt step is underspecified.** The paper states that Gaussian noise is added during training (line 254: "we add explicit Gaussian noise to the input and decode y from e_y'' = e_y' + ε") and that during cross-modal inference the text encoder is replaced with the image encoder (line 268). It is not explicitly stated whether noise is also added at inference time. If noise is added only during training, there is a distribution mismatch between noisy text embeddings seen during training and clean image embeddings seen at inference — the paper should clarify this and justify why the mismatch does not harm performance. If noise is added at inference too, the procedure should be described.

3. **The variance of the Gaussian noise added in the Corrupt step is not reported.** The paper says "following [CapDec, LAFITE]" but does not specify the chosen \(\sigma^2\) values or whether they are tuned per task, tuned per dataset, or estimated from embedding statistics. Since the method's effectiveness depends on appropriate noise levels, reporting these values would improve reproducibility.

4. **The collapse step requires reliable per-modality mean estimation.** The paper notes that means are computed over the training set. For the semi-supervised few-shot experiments (1%, 5% of data), it is unclear whether the means are computed from the full training set or only from the available subset. If the full set is used, this should be stated; if the subset is used, mean estimation may be noisy with few samples.

### Trivial

- The qualitative analysis paragraph (after Figure 5, lines 284–285) is labeled as a hypothesis ("We hypothesize that...") which is appropriate, but it would benefit from quantitative backing (e.g., measuring hallucination rates).

## Nice-to-Haves

- A procedure to estimate the noise variance \(\sigma^2\) from the residual embedding statistics after mean subtraction, making the method less dependent on hyperparameter tuning.
- A discussion of whether the geometry (Proposition 1) holds for ImageBind embeddings in the same way as CLIP, or whether any differences exist.

## Removed Points

These points were considered and removed with justification:

1. **"The method's components are individually known"** — The paper is transparent about citing Zhang et al. (2023) for Collapse and CapDec/LAFITE for Corrupt. The contribution is the principled combination motivated by the geometric analysis, which the paper clearly states. This criticism misreads what the paper claims as novel.

2. **"Baseline comparisons inadequately described / tables missing"** — The tables (tab:i2t, tab:t2i) are included via `\input{}` LaTeX commands — separate files that the PDF parser did not capture. They exist in the original submission. The generalization table (tab:result_generalization) is fully present in the extracted text.

3. **"Lemma 1 is straightforward"** — Not a weakness. Supporting lemmas do not need to be novel to be useful.

4. **"Threshold γ is arbitrary"** — Standard practice for effective dimension estimation. The specific choice (γ=0.99) is reasonable and the analysis is not sensitive to the exact value.

5. **"Lemma 2 margin depends on hardest negative"** — This is inherent to the loss function, not a weakness of the paper's analysis.

6. **"Improvement from C²₁ to C³ is smaller"** — This is an observation about the results, not a weakness. If anything, it provides insight into the relative importance of each component.

7. **"Active learning baseline ambiguity"** — The paper is sufficiently clear: "fully supervised baseline (ClipCap)" trained on each subset.

## Novel Insights

Neither reviewer surfaced a genuinely novel insight beyond what the paper itself contributes. The paper's main insight — that the modality gap and alignment noise have distinct origins (dimensional collapse + lack of gradient in ineffective dimensions vs. stable region of the contrastive loss), and that each requires a distinct correction (mean subtraction vs. noise regularization) — is well-articulated in the paper itself.

## Suggestions

- In the revision, explicitly state whether noise is added at inference time and justify the choice (or report an ablation comparing both options).
- Report the noise variance values used in the Corrupt step, and ideally describe how they were chosen.
- Clarify whether per-modality means for the semi-supervised experiments are computed from the full training set or the fine-tuning subset.
- Consider softening the framing of Proposition 1 to more clearly indicate that it is an empirically validated characterization supported by analytical reasoning, rather than a formally proven theorem.

## Score and Decision

This is a well-executed paper with a clear contribution: a principled explanation of the multi-modal contrastive geometry that directly motivates a simple and effective method. The experiments are broad (four tasks, three modalities, two embedding spaces), the ablations cleanly validate the theory, and the results are strong. The weaknesses are minor — clarification of experimental details and a more precise framing of the theoretical contribution — none of which undermine the core claims. The paper should be accepted with minor revisions.

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>
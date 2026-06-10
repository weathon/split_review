Here is the final consolidated review:

---

## Summary

This paper proposes Item Language Model (ILM), which adapts BLIP-2's QFormer to bridge behavioral embeddings (from collaborative filtering) with language representations in LLMs (PaLM 2). It uses a QFormer with four training tasks — ITC, ITG, ITM (adapted from BLIP-2) and a newly added Item-Item Contrastive (IIC) loss plus User-Item Contrastive (UIC) loss — and evaluates on 24 language generation tasks from ELM using MovieLens 25M.

## Strengths

- **The QFormer adaptation for behavioral-to-language modality bridging is a sensible engineering approach that shows promise**: the paper reports that phase-1 QFormer pre-training enables a frozen LLM to match the performance of a fully fine-tuned ELM baseline (Table 3, line 146). If the numbers hold, this is a practically useful result.
- **The ablation chain (ILM-MLP → ILM-Qformer-random → ILM-Qformer → ILM-Qformer-fullyfinetune) provides graded evidence** that the QFormer architecture and its phase-1 pre-training each contribute positively beyond a simple MLP adapter.
- **The paper reports that combined semantic+behavioral embeddings outperform either modality alone** (Table 2), validating the core premise that bridging these modalities is beneficial for language generation with item understanding.

## Weaknesses

### Fatal
None.

### Major

1. **Insufficient novelty to meet ICLR standards.** The QFormer is adapted "as-is from BLIP-2" for three of four training tasks (ITC, ITG, ITM). The claimed novel contribution — the IIC loss (Eq. 1) — is a textbook margin-based contrastive loss (Hadsell et al., 2006) applied to co-interacted item pairs. Applying an existing architecture with a standard loss to a new input modality (CF embeddings) is an engineering adaptation, not a methodological contribution at the level expected by ICLR.

2. **No ablation isolating the IIC loss — the paper's sole claimed novel component.** The paper compares ILM-Qformer-random (no phase-1 pre-training at all, all four losses absent) against ILM-Qformer (all four losses active). This cannot disentangle the effect of IIC from the effects of ITC, ITG, and ITM (all inherited from BLIP-2). Without a head-to-head comparison of QFormer trained *with vs. without* IIC (keeping the other three losses identical), there is no evidence that the claimed novel addition provides any value whatsoever.

3. **Inconsistent framing between abstract and paper body.** The abstract claims "improved capabilities in recommendation domain," but Section 2 (Related Work) states "our work does not tackle the goal of having an LLM beat recommendation task benchmarks" and Section 1 states "Our goal is to improve upon language generation tasks." All 24 evaluation tasks are language generation tasks (descriptions, summaries, reviews). No standard recommendation metrics (HR@K, NDCG, Recall) are reported. The abstract's framing is misleading and contradicts the paper's own scope delimitation.

4. **Missing critical reproducibility details.** The paper reports no learning rate, batch size, number of training steps/epochs, optimizer, warmup schedule, compute budget, QFormer architecture (number of layers, hidden dimension, attention heads), or margin hyperparameter *m* for the IIC loss. The data construction procedure for co-interacted pairs and negative sampling strategy for IIC are unspecified. The work cannot be reproduced from the paper as written.

5. **Structurally incomplete.** The paper ends abruptly without a Conclusion, Discussion, or Limitations section. This is a significant deficiency for a conference submission — there is no discussion of what the method can and cannot do, no summary of findings, and no future outlook.

6. **Single-dataset evaluation.** All experiments use only MovieLens 25M. Despite claiming general applicability ("Our technique can be generally applied to any domain," line 42), there is no evidence of generality across different domains or datasets.

### Minor

1. **Misleading baseline description.** The paper states that ILM-MLP (one phase of training with frozen LLM) is "same as the ELM setup" (line 138). ELM uses two phases, including full LLM fine-tuning in phase-2. This is not "the same setup," and the paper compares ILM-MLP (a deliberately weakened configuration) against ELM's reported numbers, then attributes the performance gap to the QFormer architecture rather than the missing LLM fine-tuning.

2. **ELM numbers are the authors' reproduction.** The paper acknowledges that "the ELM paper does not release its model or evaluation code, hence we reproduce the ELM model" (line 152). This means the central baseline comparison cannot be independently verified against the original paper's numbers.

3. **No training cost evidence for the claimed efficiency advantage.** The paper claims that phase-1 QFormer training "allows us to skip finetuning the parameters of the LLM, achieving comparable performance at a lower training cost" (line 146), but reports no FLOPs, GPU-hours, or parameter counts to substantiate this.

### Trivial
None.

## Nice-to-Haves

- An IIC-only ablation (QFormer with vs. without IIC, holding ITC/ITG/ITM constant) would directly validate the claimed contribution and is essential for any resubmission.
- Including at least one standard recommendation task (e.g., top-K recommendation) would align the evaluation with the abstract's "recommendation domain" framing.
- Reporting confidence intervals or multiple-run variance would strengthen reliability claims.
- Adding at least one additional dataset/domain would support claims of generality.

## Removed Points

The following points from the input reviews were removed with justification:

- **"Tables are illegible images"** — Removed as a parser artifact; the original submission does not have this issue.
- **"Honest scope delimitation"** (as a strength from Strength Finder) — Removed because it conflicts with the verified weakness that the abstract's framing contradicts the paper's own scope delimiters. The paper says one thing in the abstract and another in the body.
- **"Novel item-item contrastive loss (IIC)"** (as a strong positive from Strength Finder) — Weakened from a core strength to background in the "insufficient novelty" weakness. The loss itself is standard.
- **"Well-structured ablation with four controlled conditions"** (as strength) — Weakened because the ablation does not isolate the IIC loss, which is the paper's claimed novel component.
- **The harsh critic's overarching claim that "the key baseline comparison against ELM is invalid on multiple grounds"** — Filtered. The paper's main ELM comparison is through ILM-Qformer (not ILM-MLP). The ILM-MLP condition is an ablation designed to show QFormer > MLP; it is not the primary comparison. The specific factual error about ILM-MLP being "same as ELM setup" is kept as a Minor weakness.
- **Generic claims about the problem being important** (from Strength Finder) — Removed as not specific to this paper's contribution.
- **Trivial formatting/style nitpicks** — Removed as potential parser artifacts.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Add a proper Conclusion section that summarizes findings, discusses limitations, and outlines future work.
2. Run an ablation study that isolates the IIC loss (QFormer with ITC+ITG+ITM vs. QFormer with ITC+ITG+ITM+IIC).
3. Report all training hyperparameters and architecture details to enable reproducibility.
4. Align the abstract's claims with what the paper actually evaluates (language generation tasks, not recommendation tasks).
5. Correct the misleading ELM comparison description (ILM-MLP is not "same as the ELM setup").
6. Add at least one additional dataset/domain to support claims of generality.

MY FINAL SCORE: <score>3.5</score>
MY FINAL DECISION: <decision>Reject</decision>
- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 5, 5, 5
Now I have all the verified information. Let me produce the final consolidated review.

---

## Summary

This paper proposes Selective Knowledge Transfer (SKT), a framework for few-shot continual learning with language models, and its instantiation Log-evidence Progressive Prompts (LePP). The key idea is to use transferability measures (specifically LogME) to identify and selectively aggregate the most relevant past prompts for the current task, rather than treating all previous tasks equally. Experiments on NLP continual learning benchmarks (4-task and 15-task streams) using BERT-base, T5-small, and T5-large backbones show consistent improvements over Progressive Prompts and other baselines, with particularly strong gains for smaller models.

---

## Strengths

1. **Clean, well-motivated methodology.** The two-stage selection-aggregation framework is clearly described. The use of LogME — a single-forward-pass transferability measure — to select relevant past prompts is principled and avoids the need to train separate task representations (Section 3.1). The idea that indiscriminate use of all past tasks causes interference is well-articulated and directly tested.

2. **Consistent empirical improvements, especially for smaller models.** Tables 1 and 2 show LePP outperforming baselines across multiple backbones and sample sizes. For T5-small with 10 samples, the gain over Progressive Prompts reaches 4.46%; for BERT-base with 10 samples, gains of 2.09–3.07% over the second-best method are reported (Section 4.3). These are practically meaningful margins.

3. **Thorough ablation studies that validate the core thesis.** Figure 3a-c provides strong evidence: (a) selecting the most transferable prompts outperforms random, most-recent, or least-transferable selection; (b) the method is robust across different transferability measures (PARC, TransRate, ETran); (c) using all prompts degrades performance compared to a selective subset, directly supporting the paper's central claim that selective transfer is beneficial (Section 4.4).

4. **General framework, not tied to a single PEFT method.** SKT is described as applicable to prompt tuning, adapters, and LoRA (Section 3.1, Discussions), making the contribution broader than a single algorithm.

---

## Weaknesses

### Fatal
None.

### Major

1. **No variance estimates reported for any result.** The paper states results are "averaged over 5 runs" (Tables 1, 2) but never reports standard deviations, confidence intervals, or per-run ranges. This is the single most important missing element: without error bars, the reader cannot distinguish a meaningful gain from run-to-run noise. This is especially problematic for T5-large, where gains are described as "additional boosts" but may be small in absolute terms. The authors already collect 5 runs — they simply need to report the variance.

2. **Unsubstantiated claim about image modality / CV experiments.** The contributions list states "we show that SKT can work with different data modalities including images" (Section 1, contribution 3), and the conclusion claims "Extensive experiments confirm our proposed framework can significantly leverage existing SoTAs for continual learning with NLP and CV" (Section 6). However, the entire experimental section evaluates only NLP benchmarks; no image-domain experiment is presented or referenced. If these experiments exist in a (stripped) appendix, a clear pointer is needed. If they do not, these claims must be removed or qualified.

### Minor

3. **"Minimal overhead" claimed without supporting measurement.** The abstract asserts that LePP works "with minimal overhead," and Section 3.1 argues efficiency from avoiding backward passes. However, LePP requires a forward pass of every previous prompt over the current task's training set plus LogME computation for each — for a 15-task stream at step 15, roughly 14 forward passes beyond what Progressive Prompts requires. No wall-clock time, FLOPs, or relative training time comparison is provided. The claim is likely true (forward passes over few-shot data are cheap), but it should be backed by evidence.

4. **Potential selection bias from same-data reuse.** LePP computes LogME scores using the current task's few-shot training set to select which previous prompts to aggregate, then trains the new prompt on the same training set. With few-shot data (10–100 samples per class), there is a risk that prompts whose features happen to fit noise in the small training set are preferred. The paper does not discuss this or attempt to control for it (e.g., via a held-out validation split for selection). This is a non-trivial concern given the small-data regime.

5. **"Aligning with human evaluations" claim is unsupported.** The abstract and introduction state that identified task correlations "align with human evaluations" (Section 1). Table 3 shows intuitive pairings (e.g., SST-2 and CR for sentiment) but presents no actual human evaluation study. The paper should either present such an evaluation or rephrase this as consistency with domain knowledge / common sense.

6. **No direct measure of forward transfer.** The paper's core thesis is about improving forward transfer through selective knowledge aggregation, but the only metric used is average accuracy (AA), which conflates forward transfer and forgetting resistance. A dedicated forward transfer metric (e.g., FWT) would more directly validate the claimed effect.

### Trivial
None.

---

## Nice-to-Haves

- **Alternative aggregation strategies.** The ablation only compares weighted sum vs. concatenation (Figure 3a). Learned aggregation or attention-based weighting could be explored or at least discussed.
- **Explicit analysis of computational overhead** as a function of task count, even a simple table showing per-task-step overhead, would substantiate the "minimal overhead" claim.

---

## Removed Points

- **"Marginal improvements for T5-large not framed honestly" (Harsh Critic #1):** The reviewer claims specific numbers (0.41%, 0.16% for T5-large with 20/100 samples) that cannot be verified because Table 2 is embedded as an image. The paper's text says "up to 1.73% higher" for T5-large and acknowledges "performance saturation," which is not dishonest framing. The more general concern about missing variance (see Major #1) is retained and appropriately covers this issue.
- **"Stronger than Progressive Prompts only in terms of K selection" (implied noise):** Not raised by any reviewer; no such removal needed.
- **Strength Finder's "autonomous discovery of task correlations" (unsupported):** This strength is retained but qualified - the paper does show discovery of intuitive correlations in Table 3; the issue is only with the "aligns with human evaluation" phrasing (covered in Minor #5).
- **Generic strengths about "addressing important problems":** The Strength Finder's strengths all have specific citations to paper content; none are purely generic.

---

## Novel Insights

None beyond the paper's own contributions. The reviews identify no perspective on the work that the paper itself does not articulate.

---

## Suggestions

1. **Add standard deviations or per-run ranges to all result tables.** The data is already being collected (5 runs); reporting it would dramatically increase confidence in the results.
2. **Either present the CV/image experiments or remove the claim.** If they exist in a stripped appendix, add a clear pointer. If they do not exist, remove the sentence from the contributions and the "CV" reference from the conclusion.
3. **Add a small table or paragraph quantifying computational overhead** — e.g., wall-clock time per task step for LePP vs. Progressive Prompts on the 15-task stream.
4. **Add a brief discussion of the selection-bias concern** (Section 3.1 or 4.4) acknowledging that the same training data is used for selection and training and explaining why this is not expected to cause harmful overfitting.
5. **Rephrase the "aligning with human evaluations" claim** to something like "align with intuitive notions of task relatedness" unless human annotations are actually collected.
6. **Add a forward transfer metric** (e.g., FWT or per-task accuracy at first evaluation) to directly measure the claimed mechanism.

---

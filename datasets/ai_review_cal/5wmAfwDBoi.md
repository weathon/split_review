- Decision: Reject
- Avg Score: 4.25
- Scores: 5, 3, 6, 3
Here is my consolidated review.

---

## Summary

This paper systematically explores the design space of vision-language models (VLMs) for GUI element grounding, investigating warming-up data type, fine-tuning curriculum, data scaling, and patch-feature compression. From controlled ablations, it derives four findings and distills them into a recipe used to build UI-Pro (2.8B parameters), which achieves strong UI grounding accuracy across five benchmarks. The paper fills a clear gap: prior UI-VLM work (SeeClick, CogAgent) fine-tuned existing models without this kind of systematic design-space analysis.

---

## Strengths

- **Systematic empirical exploration of an underexplored design space.** The paper conducts controlled experiments across four key axes (warming-up data type, Table 1; fine-tuning curriculum, Table 2; data scaling, Figure 4; patch-feature compression, Table 3). This is the first work to provide an empirically grounded recipe specifically for UI grounding VLMs, going well beyond the "fine-tune an existing open model" approach of prior work.

- **Optimal warm-up finding is non-obvious and actionable.** Table 1 shows that warming up with pure visual grounding on natural images (RefCOCO, VG) substantially outperforms VQA, chart QA, mathematical reasoning, and even the diverse ShareGPT4V-SFT mixture. The gap is large (e.g., FuncPred 61.2 vs. 51.0 for ShareGPT4V-SFT, vs. 12.9 for no warm-up). This is a concrete, transferable insight.

- **Simple-to-complex curriculum clearly maximizes data utility.** Table 2 demonstrates that ordering SeeClick (simple) before AutoGUI (complex) yields large gains over the reverse order (e.g., ScreenSpot 42.5 vs. 23.7, row 6 vs. row 7) and over mixing (row 6 vs. row 8). The effect is large and the analysis is clean.

- **Data scaling analysis provides practical guidance.** Figure 4 shows that scaling warming-up data from 0 to 5M and SeeClick data from 8.5K to 5.3M yields sustained improvements, challenging the assumption that domain-mismatched data would saturate quickly. The identification of 212K SeeClick as a "critical reflection point" is useful.

- **Convolution-based C-Abstractor convincingly outperforms alternatives for UI images.** Table 3 shows C-Abstractor leading across five benchmarks when compared with parameter-matched Merger, Resampler, and H-Reducer. The result is well-motivated (UI layouts have flexibly arranged icons/text, unlike document layouts where horizontal stripes suffice).

---

## Weaknesses

### Fatal

None.

### Major

None. The paper's core findings are sound and supported by its controlled experiments.

### Minor

- **Architecture gap between exploration and final model.** The exploration experiments (Sections 3.1–3.4) are conducted on an unspecified "LLaVA model with a pre-trained vision-language projector" — which particular LLaVA variant, LLM backbone, and ViT size are not stated. UI-Pro (Section 4) then uses Gemma-1.1-2B / LLaMA-3.2-3B as the LLM and CLIP ViT-L/14@336 as the visual encoder — a different configuration. While the findings (data type, curriculum, compressor choice) are plausibly architecture-independent, the paper claims a *general recipe* without testing whether any of the four findings transfer to the target architecture. The C-Abstractor finding is tested on the exploration base and then used in UI-Pro, but the data-related findings (warming-up choice, curriculum, scaling) are never verified on the Gemma/LLaMA-based setup.

- **Factual inaccuracy in model-size claims.** The abstract states UI-Pro "matches the performance of previous UI-oriented models that are nine times its size" (line 23). The largest UI-oriented baseline in Table 4, CogAgent (10.05B), is ~3.6× UI-Pro (2.8B), not 9×. The body text's "one-fifth the model size of CogAgent" (line 149) is also imprecise (actually ~1/3.6). The "nine times" figure is not supported by any model in the paper.

- **Disconnect between data scaling experiment and final data choices.** The scaling experiment (Figure 4) identifies 212K SeeClick as a "critical reflection point" (diminishing returns beyond it), yet UI-Pro uses 5.3M SeeClick — 25× more — without any justification for why such a large increase is warranted. Simultaneously, the final recipe uses only 125K AutoGUI (down from the 625K used in the scaling experiment's peak). The paper does not explain how these final data volumes were chosen or whether the scaling findings on the exploration base transferred to the final architecture.

- **No variance estimates for ablation experiments.** Tables 1–3 and Figure 4 report single-point accuracy with no error bars, standard deviations, or significance tests. Benchmarks like ScreenSpot have ~2400 samples, making variance meaningful. While single-run evaluation is common in this space, the paper's central claim of providing a reliable *recipe* would benefit from at least 2–3 runs for key comparisons (e.g., the warm-up effect in Table 1, the curriculum ordering in Table 2).

- **No inference-speed comparison for compressors.** Section 3.4 evaluates compressors by accuracy but does not report latency or throughput, despite the paper motivating compression partly by efficiency ("unbearably high computational budget," line 124). A practitioner choosing a compressor needs to know the accuracy–speed trade-off, not just accuracy.

### Trivial

- **Token-count confound in curriculum mixing experiment (Table 2).** Row 8 (mixed) trains on SeeClick + AutoGUI combined in a single stage, so the model sees fewer total tokens than row 6 (two separate stages). The performance gap could partially reflect training compute rather than curriculum alone. The paper should acknowledge this confound.

- **AutoGUI overfitting vs. catastrophic forgetting (Figure 4).** The paper attributes the plateau/decline at 625K AutoGUI to overfitting, but the sequential training design could also cause catastrophic forgetting of earlier stages. Discussing this alternative would strengthen the analysis.

---

## Nice-to-Haves

- A controlled experiment that applies the paper's recipe (warming-up + curriculum + C-Abstractor + same data) to an existing open VLM (e.g., LLaVA-1.6-7B) and shows improvement over that model's default training. This would isolate the recipe's effect from raw data scaling and architecture differences, making the "recipe" claim more airtight.
- Verification that at least one key finding (e.g., warm-up vs. no warm-up) transfers from the exploration base model to the UI-Pro architecture (Gemma/LLaMA + CLIP ViT-L/14@336).
- Qualitative failure analysis: examples where UI-Pro fails compared to baselines, to help users understand the recipe's limitations.

---

## Removed Points

These points from the inputs are filtered out under the review guidelines; they should be treated with caution:

- **Harsh Critic Issue 2 (SOTA comparison uncontrolled):** Removed. The criticism that the SOTA table does not isolate the "recipe" from the "data" is largely circular — the recipe includes the data choices. Showing that the full recipe yields SOTA results is the paper's claim, and the ablations in Sections 3.1–3.4 already isolate individual components. A controlled experiment applying the recipe to an existing open model would strengthen the paper but is not a weakness in the current comparison.
- **Reproducibility concern about undisclosed hyperparameters / training scripts:** Removed per guidelines — these are nitpicks about reproducibility details that are standard to defer to code release.
- **Section 3.1 baseline description:** The paper's description of the baseline is sufficiently clear; there is no significant issue here.
- **Missing failure cases / qualitative analysis:** Moved to Nice-to-Haves.
- **Missing error bars / significance for large-scale benchmarks where single-run is the norm:** Partially retained as a Minor weakness (the paper claims a reliable "recipe," making variance relevant), but downgraded from the critic's framing.

---

## Novel Insights

Beyond the paper's own contributions, the most genuinely useful observation from the review process is that the paper's strongest empirical claims (Table 1's warm-up finding, Table 2's curriculum finding) are large in magnitude and cleanly controlled *within* each sub-experiment, but the bridge from those sub-experiments to the final UI-Pro model is not fully closed — both the architecture and the data volumes change simultaneously. An insightful follow-up would be to test whether the recipe's data-related findings replicate on a stronger base model, since the warm-up effect might shrink for an LLM with better pre-existing spatial reasoning. The paper would benefit from explicitly discussing this scope limitation.

---

## Suggestions

1. **Correct the "nine times its size" claim** in the abstract to match the actual comparison (e.g., "with fewer parameters" or the specific ratio relative to CogAgent).
2. **Justify the jump from 212K to 5.3M SeeClick** in the final recipe, or include a controlled comparison showing that 5.3M yields meaningful gains over 212K on the UI-Pro architecture.
3. **Add variance estimates** for at least the two most impactful ablations (Table 1 and Table 2) to increase confidence in the recipe's reliability.
4. **Acknowledge the architecture gap** explicitly: the exploration uses a LLaVA base, and the paper should either test transfer of key findings or discuss this as a limitation of the current recipe claim.
5. **Report compressor latency/throughput** alongside the accuracy comparison in Table 3.

---

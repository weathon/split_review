## Summary

LayoutNUWA proposes treating graphic layout generation as a *code generation* task, converting layout elements into masked HTML code and fine-tuning a 7B LLM (LLaMA2 or CodeLLaMA) via a Code Instruct Tuning (CIT) pipeline with three modules: Code Initialization (quantization + HTML templates with masks), Code Completion (LLM fills the masks), and Code Rendering (HTML→layout). The paper reports substantial improvements over prior work — including >50% FID reduction on the Magazine dataset — and provides ablation studies showing that the code template, the instruction, and the code output format are all necessary for the strong results.

---

## Strengths

1. **Novel formulation with clear motivation.** The paper is the first to reframe layout generation (traditionally numerical tuple prediction) as a code generation task (Eq. 1 → Eq. 2, Section 3.1). The advantages — semantic insights, LLM utilization, and model scalability — are clearly articulated and grounded in the properties of HTML code. This is a genuinely fresh perspective on a well-studied problem.

2. **Consistent and large empirical gains across three datasets.** On the Magazine dataset (Table 1), LayoutNUWA-CL-DA achieves FID = 8.791 on C→S+P versus the best baseline (LayoutDM) at 19.206 — a 54% improvement. On RICO and PubLayNet (Table 2), LayoutNUWA achieves the best or second-best scores across nearly all tasks, demonstrating broad applicability.

3. **Ablation studies systematically validate the method.** Table 3 progressively strips away the code template and the instruction; performance drops sharply (e.g., mIoU 0.260 → 0.124, FID 9.741 → 16.324 on C→S+P). The "w/o template" variant also fails entirely in domain-agnostic training. Table 4 keeps the same LLM backbone (LLaMA2) but switches the output format from code to numerical values, causing catastrophic failure (78% failure rate for C→S+P). Collectively, these ablations provide strong evidence that the code representation and CIT pipeline are essential.

4. **Domain-agnostic training is a concrete benefit of the code representation.** Table 1 shows that LayoutNUWA-CL-DA (trained on all three datasets) generally outperforms LayoutNUWA-CL-DS (trained per-dataset), e.g., mIoU 0.312 vs 0.297 on C→S+P. Prior numerical methods could not mix domains because their fixed numerical formats are domain-specific. This is a genuine advantage enabled by the HTML-based representation.

5. **Near-zero failure rates demonstrate the necessity of CIT.** Table 5 shows that zero-shot LLaMA2 and CodeLLaMA fail 100% of the time on layout generation, and GPT-4 fails ~30%, while LayoutNUWA achieves 0.0–0.3% failure rates. This directly supports the claim that the CIT pipeline is necessary to unlock LLM capability for this task.

---

## Weaknesses

### Fatal
None.

### Major

1. **Confound between the method's contribution and the LLM's scale is partially addressed but not fully resolved.** The baselines (LayoutTrans, BLT, LayoutGAN++, MaskGIT, DiffusionLM, LayoutDM) are all small models trained from scratch on domain-specific data, while LayoutNUWA starts from a 7B-parameter LLM pre-trained on massive text and code corpora (including HTML with layout information). The reported gains could stem substantially from the LLM's pre-trained knowledge rather than the code representation or CIT.

   The paper *does* provide two relevant controls: (a) Table 4 keeps the same LLM backbone and swaps from code to numerical output, showing catastrophic failure (78% failure), and (b) Table 3 progressively removes CIT components under the same backbone. These are valuable but incomplete. Table 4's numerical variant uses a "Code Infilling" task (predict only masked numbers within an HTML template) that may be ill-posed for the autoregressive LLM in a way that a full-sequence numerical prediction would not be. A cleaner control — fine-tuning the same 7B LLM to directly output numerical layout tuples as a sequence (mirroring what the baselines do, but at the same model scale) — would more directly isolate whether the code representation or the LLM's scale drives the improvement.

   This concern does *not* invalidate the paper's core contribution (the CIT pipeline clearly enables effective LLM-based layout generation), but it does leave the reader uncertain about how much weight to assign to the code representation *per se* versus the scale of the backbone.

2. **Results exceeding "Real Data" on the Magazine dataset are not discussed.** In Table 1, LayoutNUWA-CL-DS achieves mIoU = 0.418 on C+S→P and FID = 5.385 on the same task, both *better* than the Real Data reference (mIoU 0.348, FID 6.695). The paper does not mention or explain this unusual situation. Since the Real Data metric is computed between a 5% validation split and the test set (the original validation set), the small dataset size (~4K layouts) may produce noisy reference values. Regardless, the lack of any discussion leaves this open to interpretation (overfitting, metric artifact, or data-split mismatch) and weakens the credibility of the evaluation.

### Minor

1. **No sensitivity analysis for k-means quantization.** The method quantizes position and size values using k-means (Section 3.2.1), but the number of clusters is never mentioned, ablated, or discussed. The results could be sensitive to this hyperparameter.

2. **Resource requirements are high (64 V100 GPUs) and not contextualized.** The paper does not compare training cost against baselines (hours, FLOPs, or GPU-days). While this does not invalidate the research, it makes it hard to assess the practical significance of the approach relative to much cheaper baselines.

3. **The related work discussion of LLM-based layout approaches is thin.** LayoutGPT (Feng et al., 2023) is cited as a generic transformer method (Section 2.1) but is actually an LLM-based approach for layout generation (using GPT-4/LLaMA with prompting). The paper does not discuss why LayoutGPT is not a comparable baseline or how LayoutNUWA differs from the line of work using LLMs for layout through prompting.

### Trivial
None.

---

## Nice-to-Haves

- A control experiment that fine-tunes the same 7B LLM on a straightforward numerical layout prediction task (e.g., predicting tuples sequentially) to isolate the effect of the code representation more cleanly.
- An analysis or explanation of the "better than real data" results on Magazine, e.g., by reporting error bars or discussing the impact of the 95/5% data split used for evaluation.
- Ablation on the number of k-means clusters and the permutation count K (Section 3.2.2).

---

## Removed Points

- **"The paper overclaims being the first to treat layout generation as code generation"** — The harsh critic raised this but did not provide any prior work that does the same thing. LayoutGPT and other LLM-based methods use prompting/planning, not direct code generation with HTML templates. Removed as unsupported.
- **"Missing comparison against LayoutGPT"** — LayoutGPT solves a different task (scene layout for text-to-image generation), not the conditional graphic layout tasks (C→S+P, C+S→P, Completion) studied here. The paper's baseline zoo is appropriate for its task scope. Removed.
- **"Baseline selection is dated / field has moved quickly"** — The baselines (LayoutDM, MaskGIT, DiffusionLM, etc.) are all from 2021–2023 and represent the standard set used in the layout generation literature. No more recent comparable method is available that uses the same evaluation protocol. Removed as unfounded.
- **"The ablation in Table 3 doesn't bridge the gap because baselines don't use LLMs"** — Actually, the purpose of Table 3 is to ablate CIT *internally*, not to bridge the gap with non-LLM baselines. That gap is partially addressed by Table 4. Removed because the criticism misinterprets the purpose of the ablation.
- **Strength Finder strengths about "important problem" and "good writing"** — Generic/superficial strengths removed. Concrete strengths about the >50% improvement, ablation studies, and domain-agnostic training are retained.

---

## Novel Insights

The most unexpected finding from the cross-review is that the paper's Table 4 control (code vs. numerical output with the same LLM backbone) is simultaneously the paper's strongest piece of evidence for the code representation and the target of the harshest criticism. The numerical variant fails at a 78% rate, which on the surface strongly favors the code format. But the critic correctly notes that the numerical variant's "Code Infilling" task design may be suboptimal — predicting isolated numbers within an HTML skeleton is different from the standard full-sequence numerical prediction used by baselines. This tension suggests that the real value of the code representation may lie not in the code format *per se* but in the *structure* it imposes (clear element boundaries, labeled attributes, logical ordering), which aligns naturally with how autoregressive LLMs generate text. A controlled comparison that varies the output format while keeping the prediction task structure constant would cleanly settle this question.

---

## Suggestions

1. Add a control experiment: fine-tune the same 7B LLM to output layout tuples as a plain numerical sequence (category → numerical values, without HTML framing), matching the baseline setup but at the same model scale. This would directly answer whether code format or scale drives the gains.
2. Add a paragraph discussing why the Magazine results can exceed the Real Data reference — explain the data split procedure, note the small dataset size, and optionally report standard deviations or error bars.
3. Add sensitivity analysis for the k-means cluster count and the permutation count K to the appendix.
4. Clarify the relationship between LayoutGPT and LayoutNUWA in the related work — LayoutGPT uses LLMs for prompting-based layout planning rather than fine-tuning, which is a meaningfully different setting that warrants explicit comparison/contrast.

---

## Score and Decision

**Calibration anchors** (all rounds):

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| `.../8QTpYC4smR.md` | 1.00 | R1 (low) | Systematic review paper; not comparable |
| `.../vwSxJEq8VO.md` | 3.00 | R1 (low) | ML pipeline synthesis; much weaker contribution |
| `.../KLUDshUx2V.md` | 3.40 | R1 (low) | Concept bank generation; different domain |
| `.../JQbqaQjV7D.md` | 3.00 | R1 (low) | LLM benchmarking; different task |
| `.../exKHibougU.md` | 6.00 | R1 (mid) | LLM-grounded Video Diffusion; accepted at 6. LayoutNUWA has stronger ablations but similar confound concerns |
| `.../uBhqll8pw1.md` | 4.00 | R1 (mid) | VLM 3D reasoning; rejected, overclaiming issues. LayoutNUWA is substantially stronger |
| `.../3bmjHYX42n.md` | 5.25 | R1 (mid) | Layout generation with human feedback; rejected. LayoutNUWA has broader scope and stronger evaluation |
| `.../jLLF5EbwI2.md` | 4.00 | R1 (mid) | Spatial fidelity in T2I; different task |
| `.../pwlm6Po61I.md` | 5.67 | R2 | SVG+LLM for visual understanding; rejected with identical confound criticism. LayoutNUWA has better controls and clearer contribution |
| `.../EKCubxFdOs.md` | 5.75 | R2 | LLaMoCo: instruction tuning LLMs for optimization code; rejected. Similar approach but LayoutNUWA has stronger novelty |
| `.../xBfQZWeDRH.md` | 6.50 | R2 | GeoDiffusion; accepted. Stronger in practical impact but comparable in rigor. LayoutNUWA slightly below |
| `.../dyG2oLJYyX.md` | 5.75 | R2 | DiffusionNAG; accepted. Different domain |
| `.../8q9NOMzRDg.md` | 5.80 | R2 | Reconstructive Visual Instruction Tuning; accepted. Different approach |
| `.../KIPJKST4gw.md` | 7.25 | R2 | Code data helps reasoning; accepted spotlight. More rigorous, different task |
| `.../sGpCzsfd1K.md` | 7.00 | R2 | ChartMimic; accepted poster. Benchmark paper |

**Round 1 bracket**: The paper sits between weak anchors (~3) and strong anchors (~8), with the most relevant mid-band anchors at 4–6.

**Round 2 narrowing**: The paper is clearly stronger than rejected anchors at 5.25–5.75 (layout feedback, SVG, LLaMoCo) due to more thorough ablations, clearer novelty, and broader evaluation. It is comparable to LLM-grounded Video Diffusion (6.0, accepted) and slightly below GeoDiffusion (6.5, accepted). The confound concern is real but partially addressed and not fatal.

**Final score: 6.0** — A solid paper with a genuine contribution and well-supported claims, above the acceptance threshold, but with a notable unresolved confound and an unexplained "better than real data" result that keep it from being a strong accept.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>
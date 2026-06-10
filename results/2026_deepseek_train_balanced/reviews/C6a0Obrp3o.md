## Summary

SingleInsert proposes a two-stage method for inserting a concept from a single image into Stable Diffusion v1.5. The core contribution is a set of three losses targeting the foreground-background entanglement problem: a foreground loss that restricts reconstruction to the masked concept region, a background loss that prevents the learned embedding from influencing background denoising, and a semantic loss that prevents language drift during finetuning without requiring generated class-specific datasets. The method also supports multi-concept composition without joint training.

## Strengths

1. **Background loss cleanly disentangles the learned concept from background, with strong ablation evidence.** The ablation (Table 2, Stage 1) shows that adding \(L_{bg}\) on top of \(L_{fg}\) raises ESR from 0.170 to 0.900 and CLIP-T from 0.227 to 0.291, while CLIP-I-b drops from 0.840 to 0.683. This directly validates the paper's central claim that foreground-background entanglement is the key bottleneck and that the proposed loss addresses it. The cross-attention heatmap visualization (Fig. 4) provides mechanistic evidence: without \(L_{bg}\), the "*" embedding correlates with background regions; with it, attention concentrates on the foreground.

2. **Semantic loss replaces Dreambooth's expensive class-prior dataset with a simple, effective regularizer.** Instead of generating 100+ class-specific images per concept (as Dreambooth does), the semantic loss (Eq. 6) minimizes the difference between finetuned and frozen model outputs under the class prompt. Table 2 (Stage 2) shows adding \(L_{sm}\) improves ESR from 0.655 to 0.810, CLIP-T from 0.251 to 0.316, and reduces CLIP-I-b from 0.591 to 0.465 — all from a single image with no extra data generation. This is both computationally cheaper and conceptually cleaner.

3. **Substantially higher editing flexibility than existing single-image methods.** On ESR, SingleInsert Stage 1 achieves 0.845 and Stage 2 achieves 0.825, versus the next-best method Textual Inversion at 0.695 (Table 1). Stage 1 also leads on CLIP-T (0.317) and DIV (0.776). This margin on editing flexibility is the paper's distinctive empirical result and directly supports the claimed advantage over prior work.

4. **Multi-concept composition without joint training.** SingleInsert can combine separately learned concepts (e.g., face, hair, clothes) at inference time (Sec. 4.5, Fig. 2), a capability not demonstrated by most comparable methods. Even closely related attributes (face and hair) are handled.

## Weaknesses

### Major

1. **The quantitative evaluation is limited in scale and lacks statistical rigor.** The main quantitative comparison (Table 1) uses only 10 face images with 10 samples each (100 total per method). No error bars, confidence intervals, or significance tests are reported anywhere. With such a small evaluation set, it is impossible to assess whether the reported margins (e.g., CLIP-I-f: 0.857 vs. BreakAScene's 0.835) are reliable or would hold under different random seeds or a larger sample. The paper defers quantitative results on non-face categories to the supplementary, yet the qualitative results claim superiority on complex concepts like hair and clothes — quantitative backing for these categories in the main paper would strengthen the generalizability claim substantially.

2. **ESR — the metric where SingleInsert shows its largest advantage — has its full specification deferred to the supplementary.** The paper states it designed "ten complex text prompts" and a scoring criterion for ESR (line 117), but provides neither the prompts nor the scoring rubric in the main text. Since ESR is the metric with the most dramatic margins (Ours Stage 1: 0.845 vs. TI: 0.695), the community cannot fully assess whether the prompt set is balanced, the scoring is automated or human-judged, or whether the metric captures editing flexibility broadly. At minimum, a representative subset of the prompts and a clear description of the scoring criterion should appear in the main paper.

3. **The masked evaluation protocol (CLIP-I-f/b, DINO-f/b) is underspecified.** The paper introduces foreground/background-separated similarity scores to better measure disentanglement, which is a reasonable idea. However, it does not specify how the segmentation mask is applied to *generated* images during evaluation: is the source-image mask rigidly overlaid on generated outputs, or is segmentation re-run on each generated image? These two protocols could produce systematically different scores, and the choice matters for interpreting the results. This gap weakens confidence in the masked metrics and the quantitative comparisons that rely on them.

### Minor

1. **The foreground fidelity cost of the background and semantic losses deserves clearer characterization.** In Table 2 (Stage 2), adding \(L_{bg}\) and \(L_{sm}\) on top of \(L_{fg}\) reduces DINO-f from 0.968 to 0.761 (-21.4%) while improving ESR from 0.420 to 0.810. This is a real trade-off, and while the paper acknowledges it as "a good balance," the magnitude of the fidelity reduction (especially on DINO-f) warrants more explicit discussion — particularly for readers considering fidelity-critical applications.

2. **No analysis of sensitivity to segmentation quality.** The method depends on GroundingDINO+SAM for mask extraction (line 115), but no ablation studies vary segmentation quality or show failure cases from imperfect masks. Since real-world usage may involve concepts that are hard to segment, this is a practical limitation worth addressing.

3. **Per-concept training cost is not discussed in context.** The paper states 50 iterations in Stage 1 and 100 in Stage 2 per concept (line 113), but does not compare this to methods like ELITE that learn a general encoder once. A brief discussion of training time per concept and whether the encoder could be trained once would help situate practical utility.

### Trivial

None.

## Nice-to-Haves

- Reporting standard deviations or confidence intervals from bootstrapping the 10-face set would substantially strengthen the quantitative claims.
- Including at least one non-face category in the main quantitative comparison (Table 1) would better support the claimed generality.
- A representative subset of ESR prompts in the main text would improve transparency of the paper's strongest metric.

## Removed Points

These points were considered but removed; treat with caution:

- **"Foreground fidelity cost understated (22-23% DINO-f drop)"** — The harsh critic compared the full method against the Stage 2 baseline (which has ESR=0.005, i.e., incapable of editing). This is a strawman comparison: a method that just reproduces the original image trivially scores highest on identity preservation but is useless for editing. The meaningful comparison is against other methods that also enable editing, where SingleInsert achieves DINO-f 0.609 vs. BreakAScene's 0.603 — essentially tied. A weakened version of this concern is retained as a minor weakness above (point 1 in Minor), focusing on the progression *within* the ablation rather than the baseline comparison.
- **"User studies only mentioned in passing"** — The paper explicitly states "We also attach user study results in suppl." (line 169). Deferring full user study results to the supplementary is standard for space-constrained submissions.
- **Various speculation about masked metrics penalizing methods that move the concept** — The harsh critic speculated at length about whether the masked evaluation penalizes methods that relocate the concept, but provided no evidence this occurs. The core valid concern (underspecified protocol) is retained in the Major section.
- **"Computational cost not discussed"** — The paper provides specific iteration counts (50 + 100) and hardware (single V100). This is retained as a minor point (Minor point 3) rather than treated as a major omission.

## Novel Insights

None beyond the paper's own contributions. The two inputs largely agree on the paper's strengths (principled loss design, strong ablation, superior editing flexibility) and weaknesses (thin evaluation, ESR specification deferred) — no reviewer-identified pattern emerged that the paper itself does not acknowledge or that requires reinterpretation of its findings.

## Suggestions

1. **Specify the masked evaluation protocol in full.** State explicitly whether the source-image mask or a newly computed segmentation is applied to generated images for CLIP-I-f/b and DINO-f/b. If the source mask is rigidly applied, acknowledge the limitation and consider re-running segmentation on generated outputs as a robustness check.
2. **Include ESR prompts in the main paper.** Even a table of the 10 prompts and a one-sentence scoring criterion (e.g., "success if CLIP similarity to prompt > threshold X, verified by human inspection") would substantially improve transparency.
3. **Add error bars to Table 1.** Report standard deviations (or confidence intervals) from bootstrapping the 10-face evaluation set.
4. **Quantify the foreground-fidelity/editing-flexibility trade-off explicitly.** In the ablation discussion, state the fidelity cost in concrete terms alongside the editing gains, so readers can calibrate expectations.

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>
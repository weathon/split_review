- Decision: Accept
- Avg Score: 6.40
- Scores: 6, 8, 6, 6, 6
Now I have all the information needed to verify the reviewer claims against the paper. Let me write the consolidated review.

## Summary

This paper introduces GSA-VLN, a new task where VLN agents operate in persistent environments and adapt over repeated navigation episodes, along with the GSA-R2R dataset (150 buildings, 600 paths each, 3 instruction styles) and the GR-DUET method (global topological graph with environment-specific training). The work addresses a real gap between one-shot VLN benchmarks and deployed navigation robots that remain in the same building.

## Strengths

1. **Novel task formulation fills a practical gap.** The paper formally defines GSA-VLN with an environment-specific memory bank (Eq. 1–4) and an unsupervised update mechanism, directly contrasting standard VLN and IVLN. The task is well-motivated and captures a genuine real-world deployment scenario (Sec. 3.2).

2. **GSA-R2R significantly expands evaluation diversity.** Table 1 shows GSA-R2R includes 150 evaluation scenes (vs. ≤90 in prior datasets), ~90k paths, 600 instructions per scene, and the largest unseen vocabulary (4,716). The explicit ID/OOD split (75 residential + 75 non-residential from 19 types via GPT-4 classification with manual verification, Sec. 3.3.1) enables robust generalization tests lacking in prior datasets.

3. **GR-DUET achieves clear improvements across all splits.** In Table 3, GR-DUET outperforms all non-leaking baselines on every GSA-R2R split (e.g., Test-R-Basic SR 70 vs. next best 58). The ablations (Tables 7–8) effectively isolate the contributions of pretraining strategies, augmented data, and graph construction mechanisms.

4. **Three-stage instruction pipeline generates diverse instructions.** The pipeline combining an EnvDrop speaker, VLM refinement with path visualizations, and LLM role-playing (SummScreen characters) is creative and well-described (Sec. 3.3.2). The t-SNE analysis (Fig. 4) visually confirms the OOD distribution of Scene/User instructions versus R2R training data.

## Weaknesses

### Fatal
None.

### Major

1. **Human evaluation of instruction quality is far too small to support the dataset's reliability claims.** The paper validates ~90,000 instruction–path pairs with only 20 instructions evaluated by 15 participants (Sec. 3.3.4, Table 2). The reported ~80% alignment and style percentages lack confidence intervals. For a dataset that will be used as a benchmark, this sample (≈0.02% of the data) is insufficient to establish that the instructions are consistently accurate and stylistically distinct across building types, instruction types, and path lengths. The paper states that "there is currently no automatic method to evaluate this alignment," which makes a larger-scale human validation all the more necessary.

### Minor

2. **Baseline comparison conflates architecture change with adaptation effectiveness.** Tables 4–6 compare GR-DUET (which modifies DUET's architecture with a global graph and changes pretraining/fine-tuning) against adaptation methods (TENT, SAR, Back-Translation) applied to **vanilla** DUET. This confounds two factors: the benefit of the architectural improvements and the benefit of the adaptation strategy itself. The paper would be stronger by either (a) applying TTA methods on top of GR-DUET's architecture (starting from its pretrained model) to show additive benefit, or (b) presenting separate comparisons: architecture-only vs. architecture+adaptation.

3. **The instruction-filtering stage may bias the dataset toward easier paths.** Stage 2 of the pipeline (Sec. 3.3.2) uses a navigation model's execution success as a proxy for instruction correctness. Instructions that are correct but difficult for the specific navigator could be erroneously flagged as "failed" and then aggressively rewritten by GPT-4, or the path itself could be discarded. This selection bias is not discussed. The paper should acknowledge this limitation and ideally characterize the difficulty distribution of retained vs. filtered paths.

4. **No dedicated limitations section.** The paper does not discuss limitations of the proposed approach. Notable omissions include: (a) GR-DUET's environment-specific fine-tuning requires ground-truth topological maps of target environments, which may not be available in all deployment scenarios; (b) the memory bank treats all past trajectories (including potentially erroneous ones) as unlabeled data without filtering or reweighting; (c) the α=50 threshold caps long-term memory after 50 episodes, which for 600 instructions per building means the graph is reset frequently.

### Trivial

- "Unsupervised learning" terminology (Sec. 1, line 17) is slightly imprecise — the agent learns from its own potentially errorful trajectories, not from pristine unlabeled data. Minor clarification would help.

## Nice-to-Haves

- **Larger, stratified human evaluation:** Scale to at least 200–300 instructions, stratified by instruction type and building type, with inter-annotator agreement reported.
- **Quantitative OOD analysis beyond t-SNE:** Compute Mahalanobis distance or energy-based OOD scores comparing R2R training instructions to GSA-R2R instruction types, with confidence intervals.
- **Ablation isolating global graph benefit without training changes:** Show what GR-DUET achieves when the global graph is added to DUET *without* the modified pretraining/fine-tuning, to isolate the graph memory benefit from the training strategy benefit.
- **Statistical significance on the R2R-Test column** in Table 3 to match the standard errors reported for GSA-R2R splits.

## Removed Points

- **Overstated distinctiveness from IVLN (Critic's Issue 3):** The paper directly acknowledges IVLN in the introduction and related work, explains the two key differences (long-horizon tours vs. scene adaptation; limited 6–100 paths vs. 600), and cites it explicitly. The claim "no prior works in VLN have addressed single-scene adaptation" is reasonable — IVLN addresses persistent environments for memory/tours, not model adaptation through unsupervised parameter updates. The paper's framing is not misleading.
- **Task definition vs. method mismatch (Critic's Section-by-Section note on Sec. 3.2):** The critic claims GR-DUET doesn't solve Equation 4. But the paper explicitly describes a pretraining stage that produces a general initial model, followed by environment-specific fine-tuning that adapts it — this is exactly what Eq. 4 describes. The critic misread the method.
- **α=50 threshold concern:** The ablation in Table 8 directly tests this and shows that performance peaks at α=50 and then declines. The paper explains the trade-off ("a small buffer cannot cover graphs adequately, while an excessively large buffer leads to inefficiencies"). This is already addressed.
- **"Unsupervised learning" as a fatal imprecision:** Learning from one's own trajectories without external labels is standard usage of "unsupervised learning." The possibility of noisy data does not make the term incorrect.
- **Missing related works on memory structures:** OVER-NAV and SG-Nav are already cited and discussed in the related work. The critic's suggestion to add them is based on a misreading.

## Novel Insights

The harsh critic's observation about the confound between architectural improvements and adaptation strategy in the baseline comparison (Weakness 2 above) is insightful and goes beyond what the paper discusses. It reveals a structural limitation in how the experimental evidence is organized: to claim that a particular *adaptation approach* is superior, one must control for the underlying architecture. The paper currently compares GR-DUET (architecture + adaptation) against DUET+TENT (adaptation only), making it impossible to attribute gains to the adaptation mechanism vs. the architectural changes. Additionally, the critic's point about the instruction-filtering bias (Weakness 3) is a subtle methodological concern that the paper overlooks — using navigation success as a quality filter introduces a confound between instruction quality and instruction difficulty, which could systematically shape the dataset's difficulty profile.

## Suggestions

1. **Scale the human evaluation** to at least 200–300 instructions stratified by instruction type and building type, with confidence intervals and inter-annotator agreement. If this is too expensive, pair it with an automatic evaluation (using a VLN model to execute each instruction and measuring path completion), then validate the correlation between automatic scores and human ratings on a moderate sample.

2. **Restructure the baseline comparison** into two separable analyses: (a) architecture comparison (DUET, HAMT, BEVBert, etc.) without adaptation, and (b) adaptation comparison *on a common architecture base*, e.g., apply TENT/SAR/BT to the GR-DUET pretrained model and to vanilla DUET separately. This would cleanly attribute gains.

3. **Add a Limitations subsection** discussing (a) reliance on ground-truth topological maps during GR-DUET fine-tuning, (b) potential noise from unlabeled errorful trajectories in the memory bank, and (c) selection bias from the navigation-model-based instruction filter.

4. **Provide confidence intervals or standard errors** for the human evaluation results in Table 2, and report variance for all main results where currently only means are given (e.g., R2R-Test column in Table 3).

5. **Quantify the OOD distribution** using a tractable score (Mahalanobis distance or energy score) on instruction embeddings, complementing the qualitative t-SNE visualization.

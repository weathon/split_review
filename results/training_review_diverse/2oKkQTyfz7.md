Now I have a thorough understanding of the paper. Let me write the consolidated review.

## Summary

This paper introduces GSA-VLN (General Scene Adaptation for VLN), a task requiring agents to adapt to persistent environments by accumulating experience over multiple episodes. The authors construct the GSA-R2R dataset, with 150 diverse buildings (75 residential/ID, 75 non-residential/OOD) and 90,000 instruction–trajectory pairs across three instruction styles (Basic, Scene, User) generated via a three-stage LLM pipeline. The proposed GR-DUET method — combining a global topological graph with environment-specific pretraining/fine-tuning — achieves state-of-the-art results across all GSA-R2R splits, while extensive benchmarking reveals that optimization-based adaptation methods (TENT, SAR, Back-Translation) consistently underperform relative to memory-based approaches.

## Strengths

1. **Novel task and large-scale dataset address a real gap in VLN evaluation.** GSA-R2R provides 150 evaluation buildings (75 residential, 75 non-residential) with 90,000 instruction–trajectory pairs across three instruction styles, far exceeding prior datasets in both environment diversity and instruction variety (Table 1). The t-SNE analysis (Figure 4) confirms that Scene and User instructions form an out-of-distribution cluster relative to training data, supporting the claim that the dataset enables OOD evaluation.

2. **GR-DUET achieves state-of-the-art results across all GSA-R2R splits, demonstrating clear performance gains from environment-specific memory.** On Test-R-Basic, GR-DUET reaches 82% SR / 72% SPL, outperforming DUET by 24 points SR; on Test-N-Basic, it achieves 73% SR / 63% SPL, a 25-point improvement over DUET (Table 3). This directly supports the central claim that maintaining a global topological graph with environment-specific training substantially improves navigation in persistent scenes.

3. **The three-stage instruction orchestration pipeline produces stylistically diverse instructions validated by human evaluation.** Table 2 shows ~80% alignment and the majority of instructions exhibit a clear speaking style (71–84% for Scene instructions). This provides direct evidence that the pipeline generates both ID (Basic) and OOD (Scene/User) instructions suitable for benchmarking scene adaptation.

4. **Systematic benchmarking of adaptation methods yields actionable insights.** Table 4 shows that memory-based methods (especially GR-DUET) consistently outperform optimization-based TTA methods in the GSA-VLN setting, while Tables 5–6 further demonstrate that TTA gains on Scene instructions (1% SR increase) do not transfer to User instructions. This negative result is informative for future work on scene adaptation.

5. **Ablation studies (Tables 7, 8) rigorously justify key design choices.** The combination of full-graph pretraining and PREVALENT-augmented fine-tuning yields a 12+ point SR improvement over either component alone (Table 7), and the "memory" graph construction strategy outperforms the "proportion" alternative (73 vs. 71 SR on Test-R-Basic with α=50, Table 8).

## Weaknesses

### Fatal
None.

### Major

1. **Framing mismatch between task definition and the proposed method.** The introduction (line 17) and task definition (Section 3.2, Equations 3–4) foreground parameter updates as a core requirement of GSA-VLN, stating that agents must "continuously update their model parameters to improve performance over time." Yet GR-DUET never updates model parameters during evaluation — it only maintains a global graph with frozen weights. The paper then finds that every optimization-based adaptation method tested (TENT, SAR, Back-Translation) *hurts* performance (Table 4), effectively dismissing the very mechanism the task definition emphasizes. This creates an unnecessary tension: the paper explores both memory and optimization branches, finds optimization harmful, and proposes an effective memory method, which is a coherent scientific narrative, but the framing still over-promises on parameter updates. The paper would be significantly stronger if the task were neutrally framed (e.g., "agents can leverage accumulated experience through memory or model updates") and GR-DUET positioned as a memory-based approach that avoids the pitfalls of optimization. The meta-learning objective (Equation 4) is never operationalized and could be removed or explicitly linked to the training procedure.

2. **Uncontrolled comparison of memory mechanisms.** The main memory baseline (TourHAMT) is built on HAMT, while GR-DUET is built on DUET. Table 3 shows DUET already outperforms HAMT on R2R (SR 69 vs. 65) and on every GSA-R2R split. Thus, the comparison in Tables 4–6 conflates the base model's strength with the memory method's contribution. The paper should compare GR-DUET against a version of DUET augmented with TourHAMT-style history embeddings, or against a version of HAMT augmented with the global graph. Without this controlled comparison, the claimed superiority of the global graph over history embeddings is not properly tested. (Note: the paper does show GR-DUET > DUET in Table 4, so the memory benefit relative to the same base model is supported; the specific architectural claim about global graphs vs. history embeddings is what lacks a controlled test.)

### Minor

3. **Human evaluation sample is too small to robustly validate the dataset.** The human evaluation of instruction quality (Section 3.3.4) uses 15 participants evaluating 20 randomly selected instructions out of 90,000 — a 0.02% sample. An 80% alignment rate on 20 instructions yields a wide confidence interval (~ ±18 percentage points). No breakdown by instruction type (Basic/Scene/User) is reported, even though Table 2 suggests User instructions are "less styled." The paper acknowledges there is "no automatic method to evaluate alignment," but a VLM-based automated alignment check could supplement the human evaluation and scale the validation. The dataset's reliability as an evaluation benchmark depends on this validation, and the current evidence, while suggestive, is thin.

4. **Environment ID/OOD classification is not validated against training data distribution.** The paper categorizes non-residential buildings as OOD based on the assumption that training data (R2R) is "most residential" (line 92). However, the paper never checks whether any of the 25 R2R training scans overlap in building type with its 19 non-residential categories (e.g., if an R2R training scan is an office, then testing on an HM3D office is not truly OOD). The filtering only excludes exact scan IDs, not building-type overlap. A simple analysis of the MP3D training set's building-type distribution would resolve this concern.

5. **No longitudinal analysis of adaptation over episodes.** The paper's core claim is that performance improves as the agent executes more episodes in a persistent environment. However, results are reported as aggregate averages over all episodes. Plotting SR (or a similar metric) against the number of previously executed episodes (e.g., in bins) would directly demonstrate the adaptation benefit and reveal whether improvement plateaus or decays. Currently, the claim of "improved performance over time" is supported only by the overall comparison between GR-DUET and methods without memory, not by a temporal breakdown.

### Trivial

- The justification for the 600-path threshold is not explained (why 600? how many environments were excluded?).
- The choice of five SummScreen characters for User instructions is described but not justified (why these five, and how representative are they?).
- No limitations section is included (e.g., reliance on LLM-generated instructions, HM3D's pre-computed graphs, computational cost of storing global graphs).

## Nice-to-Haves

- **Expanded human evaluation.** Even 100 instructions stratified by type (Basic/Scene/User) with multiple annotators would give a meaningful signal. Reporting per-type alignment and inter-annotator agreement would strengthen dataset validation considerably.
- **Controlled memory comparison.** Augment DUET with TourHAMT-style history embeddings (same architecture, same training data) to isolate whether the global graph is the specific mechanism driving improvement over history embeddings.
- **Longitudinal analysis.** A plot of success rate binned by episode number would directly demonstrate the temporal adaptation benefit that the task definition promises.
- **Discussion of optimization failures.** The negative results for TENT/SAR/BT (Table 4) are striking but receive only a one-sentence attribution. A deeper analysis (e.g., tracking entropy or loss over episodes) would help the community understand when and why parameter updates fail in this setting.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"Reset visited status contradicts long-term memory"** (harsh critic): The reviewer claims that resetting visited status at the start of each episode prevents cross-episode memory. This is a misunderstanding: the global graph preserves observations across episodes, while the visited-status flag is a within-episode tracking mechanism for action selection efficiency. The paper is clear about this. **Removed** (factually wrong).

- **"No code/dataset release"** (harsh critic): The paper does not mention release plans, but this section may have been in the appendix which the parser strips. Following the meta-review guidelines, criticisms about missing release statements from stripped sections are removed. **Removed** (may exist in stripped content).

- **"The paper should also cover Y/domain Z"** (harsh critic's framing criticisms about missing related works): Following guidelines, missing related works are not included as weaknesses. **Removed** (no external verification possible).

- **"What visual features are stored in graph nodes?"** / **"How are unseen nodes identified?"** (harsh critic): The paper states that nodes store positions {x,y,z} and visual observations O (line 206). These details are present. **Removed** (addressed in paper).

- **Formatting/style nitpicks** (e.g., "unsupervised learning is slightly misleading" in Section-by-Section Notes): Pure stylistic preference. **Removed** (style nitpick).

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Reframe the task definition** to encompass both memory-based and optimization-based adaptation neutrally (e.g., "agents can leverage accumulated experience through memory or model updates"), and clearly position GR-DUET as a memory-based approach. Remove or connect the decorative meta-learning objective (Equation 4) to actual training.
2. **Add a controlled ablation** comparing DUET+global-graph against DUET+history-embeddings (or HAMT+graph against TourHAMT) to isolate the architectural benefit of the global graph.
3. **Expand the dataset validation** with a larger human evaluation stratified by instruction type and supplemented by automated VLM-based alignment metrics.
4. **Add a longitudinal analysis** showing performance as a function of episodes executed.
5. **Add a limitations section** discussing known constraints (LLM instruction artifacts, HM3D bias, computational cost).

## Score and Decision

The paper tackles a genuinely important and underexplored problem, constructs a substantial and thoughtfully designed dataset, and provides extensive benchmarking. The proposed GR-DUET method is effective and well-ablated. The main weaknesses — a framing mismatch between the task definition and method, and a confounded memory-mechanism comparison — are significant but addressable with revisions. The dataset contribution alone is valuable to the community. I recommend acceptance conditional on addressing the major and minor weaknesses.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>
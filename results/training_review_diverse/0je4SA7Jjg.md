Now I have all the information needed to write the consolidated review. Let me construct it.

## Summary
2-3 sentence summary of the paper's contribution.

## Strengths
- strength 1 with evidence
- strength 2 with evidence

## Weaknesses
### Fatal
### Major
### Minor
### Trivial

## Nice-to-Haves

## Removed Points

## Novel Insights

## Suggestions

## Score and Decision

Let me write the review now.

---

Here is my reasoning before writing:

1. **No error bars**: The paper reports single RMSE values. This is a real weakness but is standard practice in many PDE/ML works where training is expensive. I'll keep this as a Minor weakness since it doesn't invalidate the results but limits statistical confidence.

2. **Parameter claim**: The paper claims improvement is due to cell features, not additional parameters. The control (deeper MGN) is weak because deeper networks face optimization difficulties. This is a Major weakness because it undermines a specific attribution claim.

3. **Over-smoothing claim**: Asserted but never directly tested via feature similarity or spectral analysis. The paper only has indirect RMSE evidence. This is a Minor weakness — it's a gap in supporting a stated motivation, not in the core results.

4. **Data scaling test**: The paper says "we report the results" but no results are shown (cut-off sentence, no table). This IS a Major weakness because sample efficiency with limited data is highlighted as a key advantage in the abstract and introduction, yet no evidence is provided.

5. **Black-Sea modest improvement**: 8.4% vs 43-93% on synthetic. This is factual but not a weakness per se — it just shows the method is more effective on certain data types. I'll keep as a minor observation.

6. **Miscellaneous minor issues**: "detecting discontinuities" never elaborated, FE algorithm ambiguity, missing experimental details, high GPU memory, etc. — all Minor or Trivial.

Score: I'll give 5.5. The core architectural ideas are interesting and the synthetic results are strong, but the paper over-claims significantly (data scaling, parameter attribution, over-smoothing) and has a notable missing result (data scaling test claimed but not shown). This needs substantial revision.## Summary

This paper proposes CeGNN, a graph neural network for spatiotemporal PDE prediction that introduces two architectural innovations: (1) **cell-embedded message passing** that incorporates triangular/tetrahedral cell features (centroid, area, relative positions) to upgrade aggregation from first-order (edge→node) to second-order (volume→edge→node), and (2) a **feature-enhanced (FE) block** that computes outer-product features with a learned mask and weight tensor to enrich node representations. The core contribution is methodological: reformulating message passing to include volumetric cell information alongside node-edge interactions. Experiments across five datasets (Burgers, FitzHugh-Nagumo, 2D/3D Gray-Scott, Black-Sea) show CeGNN achieves lower RMSE than MGN, MP-PDE, GAT, and FNO baselines, with 43–93% error reduction on synthetic PDEs and 8.4% on the real-world dataset.

## Strengths

1. **Cell-embedded message passing is a clean architectural innovation with empirical support.** The paper introduces learnable cell features into the GNN message-passing pipeline, reformulating it as volume→edge→node rather than just edge→node (Equations 5–7). The ablation (Table 4) confirms that removing the cell component consistently degrades performance across all datasets (e.g., 2D FN RMSE increases from 0.00364 to 0.00982 without cell), directly validating that the higher-order aggregation captures spatial dependencies that edge-only approaches miss.

2. **FE block consistently improves performance when plugged into multiple GNN architectures.** Table 3 (labeled "Effect" in the paper) shows that adding the FE block to MGN, MP-PDE, GAT, and GATv2 improves results across most settings, with particularly strong gains on MGN (e.g., 3D GS RD: RMSE drops from 0.01925 to 0.00721, a 62.5% reduction). This demonstrates the FE block's utility as a general-purpose enhancement module, not one narrowly tuned to CeGNN.

3. **State-of-the-art results across all five benchmarks.** Table 1 reports CeGNN achieving the lowest RMSE on every dataset, with error reductions of 43.4% (2D Burgers), 82.9% (2D FN), 91.4% (2D GS RD), 92.8% (3D GS RD), and 8.4% (Black-Sea) over the best baseline. Multi-step rollout visualizations (Figures 5–6) corroborate the quantitative results.

4. **Clean ablation isolating each component's contribution.** The ablation study (Table 4) separately tests "w/o Cell, FE" (MGN baseline), "w/o Cell" (MGN+FE), "w/o FE" (CellMPNN without FE), and the full model, showing that both components contribute positively and that their combination yields the best results. The feature-splitting analysis (Table 6/impact_of_window_size) provides practical engineering guidance for controlling FE block complexity.

## Weaknesses

### Fatal
None. The core architectural ideas (cell-embedded messaging, FE block) are sound and supported by the ablation studies. No weakness invalidates the paper's central claims.

### Major

1. **Data scaling results are claimed but entirely absent from the paper.** The paper states (Section 4.3, last paragraph): *"We also have performed a data scaling test and report the results (data size vs. ...). It can be observed that our model with a smaller amount of data has equal or superior performance compared with that of other methods (MGN and MP-PDE) with larger amounts of data."* No actual results — no table, figure, or numbers — appear anywhere. The sentence trails off in a typographically garbled form ("data size vs."), but the core problem is that **the claimed evidence does not exist in the submission**. Sample efficiency with limited data is highlighted as a key advantage in both the abstract ("particularly with limited datasets") and introduction. Presenting this claim without supporting data is a serious evidential gap that the authors must address.

2. **The claim that improvement is due to cell features rather than additional parameters is unsupported by the presented comparison.** The paper states (Section 4.3): *"We have verified that the improvement of our model performance is due to the innovative use of cell features rather than the introduction of additional parameters."* The evidence is Table 5: CeGNN (1.48M params) vs. MGN with 12 layers (1.44M params), where MGN-12 performs worse. However, deeper MGN with the same channel width may suffer from optimization difficulties (over-smoothing, harder training) that have nothing to do with parameter count parity. A proper control would match parameter count by increasing MGN's hidden dimension at the same layer depth, not by adding layers. As presented, the parameter confound is not resolved, and the strong claim of "verification" is unjustified. This should be downgraded to a circumscribed claim or supported with a proper matched-capacity experiment.

### Minor

1. **No error bars, confidence intervals, or multiple-run statistics are reported.** Every quantitative result in Tables 1–5 is a single number without variance estimates. While single-run reporting is common in PDE/ML due to training cost, the lack of any variance information means the reader cannot assess whether the reported improvements (especially the smaller 8.4% gain on Black-Sea) are significant relative to the noise floor. This does not invalidate the results, but it limits the strength of the quantitative evidence.

2. **The over-smoothing claim is asserted as a demonstrated property but is never directly tested.** The paper repeatedly states that the FE block "relieves the over-smoothness problem" (abstract, introduction, Section 3.1.1, conclusion). However, no experiment measures feature similarity across layers, performs spectral analysis, or compares feature diversity with/without the FE block. The ablation only shows that FE improves RMSE, which could be due to increased expressiveness, better optimization, or other factors. This is a gap between what is claimed and what the evidence supports. Removing over-smoothing from the stated contributions or adding a targeted diagnostic would resolve this.

3. **"Detecting discontinuities in space" is mentioned in the introduction but never elaborated.** The sentence *"Specifically, after detecting discontinuities in space, we introduce a learnable cell attribution..."* (Introduction, paragraph 3) suggests a specific preprocessing or detection mechanism for locating discontinuities, but neither the method section nor the experiments describe how this is done. This appears to be a remnant from an earlier draft and does not correspond to any component in the actual CeGNN architecture.

4. **The FE block algorithm has an underspecified tensor contraction.** Algorithm 1 Step 4: *"Multiply the masked states $\hat{\mathbf{h}}^{*l*} \in \mathbb{R}^{N\times D\times D}$ with the weight $\mathbf{W}^{l} \in \mathbb{R}^{D\times D\times D}$ to construct the final states $\mathbf{h}^{l} \in \mathbb{R}^{N\times D}$."* The indices being contracted are not specified (is this an einsum of the form `nij,ijk->nk`, a batched matrix multiplication, or another contraction order?). Given that a full tensor with $D^3$ parameters (~2M for D=128) is a significant design choice, the ambiguity prevents reliable reimplementation.

5. **Missing experimental reproducibility details.** The experimental setup (Section 4.3) specifies latent dimension (128), optimizer (Adam), and hardware (A100), but omits: number of training trajectories, rollout length for evaluation, learning rate and schedule, batch size, total training epochs, and whether early stopping was used. These details are necessary for reproducibility and contextualizing computational cost (Table 5 reports s/epoch but without total epochs, total cost is unclear).

6. **The real-world dataset improvement is modest and lacks contextualization.** CeGNN improves over MP-PDE on Black-Sea by only 8.4% (RMSE 0.60761 → 0.55599), contrasting sharply with the 43–93% gains on synthetic PDEs. The paper does not discuss why the method underperforms on realistic irregular-mesh data, nor does it describe the Black-Sea dataset source, resolution, or number of time steps. This limits the reader's ability to assess the method's practical utility.

7. **GPU memory usage of 45.87 GB is very high without discussion of alternatives.** The paper does not discuss whether lower-memory variants (gradient checkpointing, smaller batch size, reduced latent dimension) are feasible, or whether the method can scale to larger 3D meshes common in engineering applications.

### Trivial

1. The explanation for why the FE block degrades attention-based methods (Section 4.3, "Feature-enhanced effect") uses a simplified two-neighbor normalization example that does not account for multi-head attention or independent heads. The intuition is reasonable but the analysis is oversimplified.
2. The "w/o Cell, FE" ablation row (Table 4) matches MGN's numerical values, but the paper does not confirm architectural equivalence beyond removing those two components (e.g., encoder/decoder design differences).

## Nice-to-Haves

- A diagnostic experiment directly measuring feature similarity or node feature diversity across GNN layers with and without the FE block would substantiate the over-smoothing claim.
- A proper parameter-matched comparison (increasing MGN/MP-PDE hidden dimension at 4 layers rather than adding layers) would cleanly resolve the parameter-attribution question.
- Reporting multiple random seeds with standard deviations would significantly strengthen the quantitative evidence.
- Discussion of memory-efficient training strategies (gradient checkpointing, etc.) would address the practical usability concern.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Related work does not discuss whether prior work already incorporated cell/face-level features"** — The reviewer speculates that MP-PDE uses "cell" features in a different sense. Without confirming MP-PDE's architecture details, this is an unverifiable claim and the paper adequately characterizes prior work's scope and limitations. (Removed per rule: DON'T mention missing related works as you cannot confirm existence.)
- **"The paper would benefit from a controlled experiment for attention+FE explanation"** — This is a minor suggestion that does not affect the core contribution; the existing explanation (simplified as it is) provides reasonable intuition. Moved here as a wishlist item.
- **Strength Finder claim that the FE block "directly supports the claim that FE relieves over-smoothing"** — This conflicts with the verified weakness that over-smoothing is never directly tested. The weakness wins. The FE block's performance improvement is genuine, but the over-smoothing attribution is unsupported. The strength is retained in modified form above (Strength 2, without the over-smoothing characterization).

## Novel Insights

None beyond the paper's own contributions. The reviews surface the tension between strong synthetic-benchmark results and weaker real-world gains, and the gap between claimed and demonstrated evidence for over-smoothing and sample efficiency. These are useful diagnostic observations but do not constitute a synthesis that goes beyond what the paper itself provides.

## Suggestions

1. **Present the data scaling results in a proper table or figure** (RMSE vs. number of training trajectories for CeGNN and at least one strong baseline). This is non-negotiable: the paper claims sample efficiency as a key advantage but withholds the supporting evidence.
2. **Replace the deep-MGN parameter control with a proper matched-parameter comparison** (e.g., MGN with larger hidden dimension at 4 layers). If this is infeasible, soften the attribution claim from "verified" to "suggested by."
3. **Either add a diagnostic for over-smoothing** (average pairwise cosine similarity of node features across layers, with and without FE) **or remove over-smoothing from the list of demonstrated properties** and frame it as motivation only.
4. **Add error bars or at minimum report results for 3 random seeds** on the main benchmark (Table 1). If training cost is prohibitive, report results for a subset.
5. **Clarify the tensor contraction in Algorithm 1** (specify the einsum notation or contraction indices) and confirm whether the weight tensor is full-rank or factorized.
6. **Provide standard reproducibility details**: number of training trajectories per dataset, learning rate, batch size, training epochs, and rollout horizon.

## Score and Decision

The paper presents a sensible architectural contribution (cell-based message passing + outer-product feature enhancement) and demonstrates strong results on synthetic PDE benchmarks. The core ideas are worth exploring and the ablation study is well-designed. However, the evaluation has significant evidential gaps: (1) the data scaling experiment — which the paper itself highlights as a key advantage — is claimed but entirely absent, (2) the central attribution claim (gains are due to architecture, not parameters) rests on a flawed matched-parameter comparison, and (3) the over-smoothing alleviation claim is asserted without direct evidence. These are not minor fixable issues; they require additional experimentation or substantial rewriting to align claims with evidence. In its current form, the paper oversells what it demonstrates. With the recommended revisions, it could become a solid contribution.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>
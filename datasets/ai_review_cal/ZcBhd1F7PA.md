- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 5, 5, 5
Now I have all the evidence I need. Let me compile the final review.

---

## Summary

The paper proposes Hierarchical Multi-Grained Reasoning (HGR) for Object Concept Learning (OCL), a many-to-many mapping problem where objects have multiple attributes and affordances. HGR introduces (1) a coarse-to-fine hierarchical reasoning module that progressively refines prompt-based features from global image context to instance-level object regions, and (2) a counterfactual relation-enhancing module that uses a concept connection network with a counterfactual loss to strengthen causal links between attributes and affordances. Experiments on the OCL benchmark, NYUd2 scene understanding, and AGD20K affordance grounding show consistent improvements.

## Strengths

1. **Significant performance gains on the OCL benchmark.** The paper reports +8.1% mAP on attribute prediction and +3.9% mAP on affordance prediction over the prior state-of-the-art (Li et al., 2023b), as stated in the abstract and contributions (line 37). These are large absolute improvements on a benchmark of 185K+ instances.

2. **Ablation evidence that the coarse-to-fine prompt design is necessary.** Table 5 (discussed in lines 254-257) decomposes the prompt reasoning into global-only, instance-only, and the full two-step hierarchy. The full design outperforms both single-step variants, confirming that progressive coarse-to-fine localization is a key contributor.

3. **Ablation evidence that the counterfactual relation-enhancing module improves performance.** Table 4 (discussed in lines 191-248) shows that adding the concept connection network with counterfactual (CCC) on top of the base model with CHR and PVCE yields clear improvements, supporting the claim that counterfactual reasoning strengthens object-concept relations.

4. **Generalization to two additional tasks and datasets.** HGR outperforms prior methods on NYUd2 for multi-task scene understanding (Table 2) and on AGD20K for weakly supervised affordance grounding (Table 3), demonstrating that the approach is not narrowly tailored to the OCL benchmark.

5. **Qualitative evidence of progressive reasoning.** Figure 3 provides heatmaps from the coarse and fine prompt modules, showing that attention shifts from broad image regions to concept-specific object parts, supporting the claim that hierarchical reasoning operates as intended.

## Weaknesses

### Fatal

None. No verified criticism invalidates the paper's core claims.

### Major

1. **Backbone confound in main SOTA comparison.** The baselines in Table 1 (OCRN, DM-V, etc.) are taken from Li et al. (2023b), which uses a ResNet-based architecture, while the proposed method uses CLIP — a large pre-trained vision-language model. The paper does not re-implement any baseline with a CLIP backbone, so a portion of the reported 8.1%/3.9% gains may come from the stronger backbone rather than from the proposed reasoning modules. The ablation study (Table 4) uses "Vanilla CLIP" as a starting point and shows incremental gains, which helps, but the main headline comparison against OCRN et al. is uncontrolled. *Impact: the claim of SOTA superiority is not fully disentangled from backbone choice.*

2. **Underspecified counterfactual loss formulation.** The counterfactual loss in Eq. (line 134) appears truncated — only one case of the piecewise function (β_i=1) is visible, and the second case the paper refers to ("We design two loss functions L_cl according to the different affordance label") is not shown. The paper also does not provide quantitative evidence that the counterfactual module learns genuine causal structure rather than correlations — the evaluation relies on a qualitative example (Figure 5) and the overall mAP gain from CCC (Table 4), but no direct causal-effect measurement or controlled intervention analysis is reported. *Impact: the central counterfactual component is partially unreproducible and unvalidated in its causal claims.*

3. **No statistical significance or variance reporting.** Results are reported as single-run mAP values without error bars, confidence intervals, or multi-seed variance. Given the scale of the reported gains, this is not fatal, but it prevents assessing whether improvements are stable. The OCL benchmark's standard protocol may not require error bars, but reporting them would strengthen the evidence.

### Minor

1. **Ambiguity about ground-truth bounding box usage at test time.** Section 3.1.2 (line 89) states that "we employ ground-truth bounding boxes to crop the objects" during prompt formation, but does not explicitly clarify whether this step occurs only during training or also at inference. While the OCL benchmark (Li et al., 2023b) likely uses the same protocol for all methods (making the comparison fair), the paper should state the test-time procedure explicitly and discuss whether the method can operate without oracle boxes.

2. **Key metrics are not defined in the paper.** The evaluation uses S_ITE and S_{α-β-ITE} metrics (line 179) but never defines them. The reader must consult Li et al. (2023b) to understand what these measure. A self-contained paper should include brief definitions or cite the relevant equations.

3. **Missing specification of the layer index M.** The coarse-grained prompt uses intermediate-layer features F_M from "the M-th intermediate layer" of CLIP's visual encoder (line 79), but the value of M is never given. This harms reproducibility.

4. **The claim of "first to summarize OCL as a many-to-many mapping problem" (line 31) is overstated** given that Li et al. (2023b), which the paper cites as prior work, already frames the problem this way.

### Trivial

- The hyperparameter γ in the counterfactual loss (line 134) is mentioned but its value is not reported in the experimental setup (only λ₁=0.1 and λ₂=1 are given in line 154).

## Nice-to-Haves

- Re-implementing the strongest baseline (OCRN) with a CLIP backbone would cleanly isolate the contribution of the reasoning modules from the backbone improvement.
- A controlled experiment measuring the counterfactual loss's effect (e.g., showing that masking causally-linked attributes shifts affordance predictions in the expected direction) would strengthen the causal reasoning claim beyond overall mAP gains.
- Reporting multi-seed variance or confidence intervals would improve confidence in the results.

## Removed Points

- **Softmax_c ambiguity (Harsh Critic point):** The paper explicitly states "softmax_c indicates we make softmax operation across the column direction" (line 121). The reviewer claimed this was ambiguous — it is not. **Removed** (factually incorrect criticism).
- **"Tables are garbled" criticism:** The reviewer noted tables are garbled in the extracted text, which is a parser artifact; the original paper's tables are intact. **Removed** (parser issue, not paper flaw).
- **Ablation study "no numeric values" criticism:** The reviewer claimed "no numeric values are given" for the ablation. Table 4 is present as a rendered image in the original paper — the extracted text cannot display it, but the numbers exist. The Strength Finder confirms specific values (52.6/58.9 → 57.1/63.2). **Removed** (parser issue, not paper flaw).
- **Speculation about baseline GT box usage:** The reviewer speculated "If the baseline methods also use GT boxes... If they do not, then the comparison is fundamentally unfair." This is speculation about a fact not established in the paper. The OCL benchmark protocol likely standardizes this. **Removed** (speculative, not verifiable from paper).
- **"Could the metric be measuring a proxy?" type speculations:** The harsh critic's area-based sweep generated some speculative concerns with no concrete anchor in the paper. **Removed** per filtering discipline.

## Novel Insights

The most interesting observation across the reviews is that the paper's central tension is between two competing interpretations of its results: (1) the hierarchical reasoning + counterfactual modules genuinely advance OCL, or (2) the gains primarily reflect the stronger CLIP backbone. The reviewers polarized around these explanations without noting that the paper partially addresses this via its CLIP-based ablation (Table 4), which does show incremental improvements from each module. Neither reviewer pointed out that even if the 8.1%/3.9% headline gain is partly backbone-driven, the consistent cross-task improvements (NYUd2, AGD20K) and the progressive failure of single-step prompts (Table 5) provide independent evidence that the *reasoning design* contributes meaningfully. The real open question is how much of the gain is reasoning vs. backbone — the paper could resolve this cleanly with one controlled experiment.

## Suggestions

1. **Clarify the test-time bounding box usage** in a single sentence — state whether GT boxes are used only at training or also at inference, and if the latter, acknowledge the limitation and suggest future integration with a detector.
2. **Complete the counterfactual loss equation** and report the value of γ. Add a simple quantitative analysis (e.g., correlation between masked attributes and shifted affordance predictions) to validate causal learning.
3. **Re-implement at least one baseline (OCRN) with a CLIP backbone** to control for the backbone confound, or add a clear discussion of this limitation in the paper.
4. **Define S_ITE and S_{α-β-ITE}** briefly in the evaluation section for self-containedness.
5. **Report the value of M** (layer index) used for intermediate features.
6. **Add error bars or multi-seed runs** to at least the main table.

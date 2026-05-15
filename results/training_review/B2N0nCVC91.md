Now I have a thorough understanding of the paper. Let me produce the final consolidated review.

## Summary

This paper proposes FLIP, a flow-centric generative planning framework for robot manipulation. It uses dense image flow as a universal action representation — extracted from video without action labels — and combines three modules: a flow generation network (CVAE), a flow-conditioned video diffusion model (DiT with mixed conditioning), and a vision-language value function (adapted from LIV). These modules work together via hill-climbing beam search to plan long-horizon manipulation trajectories. The system is evaluated on planning success, long-horizon video generation quality, low-level policy guidance, and module-level ablations across simulation (LIBERO, FMB) and real-world (Bridge-V2, cloth folding) benchmarks.

## Strengths

1. **Novel and well-motivated use of dense image flow as a general action representation for planning.** The paper identifies a key bottleneck in interactive world models — finding an action representation that is both expressive (captures subtle motions across diverse robots/objects) and scalable (extractable from pure video). Dense point flows satisfy both criteria, and the paper is the first to operationalize them for model-based planning. This is a genuine conceptual contribution.

2. **Mixed conditioning mechanism for flow-conditioned video generation yields substantial gains.** The design combining cross-attention (for fine-grained flow/image conditioning) with AdaLN-Zero (for global language/timestep conditioning) is technically sound and produces large improvements over baselines: e.g., FVD of 27.62 vs. 92.76 (IRASim) on LIBERO-10 short-horizon generation (Table 4), and 35.62 vs. 206.28 on LIBERO-LONG long-horizon generation (Table 2). The ablation Ours-SC (pure AdaLN-Zero) confirms that the cross-attention mechanism is responsible for most of the gain.

3. **Simple but effective fix for value function fine-tuning on long-horizon videos.** The observation that LIV's frame-level time-contrastive loss produces jagged value curves on long, imperfect videos, and the fix of treating short video clips as "states" rather than individual frames, is a clever and well-reasoned modification. The smoothed value curves (Figure 5) are visually convincing, and the downstream planning benefit (Table 1: 100% vs. 78% on LIBERO-LONG compared to the no-value ablation) provides indirect validation.

4. **Broad evaluation scope across multiple benchmarks and settings.** The paper tests planning (Table 1), long-horizon video generation (Table 2), short-horizon video generation (Table 4), flow prediction (Table 5), low-level policy guidance (Figure 4), and interactive/zero-shot properties — across simulation (LIBERO, FMB, Language-Table) and real-world data (Bridge-V2, cloth folding). The breadth supports the claim that the framework is general-purpose.

## Weaknesses

### Fatal

None.

### Major

None that threaten the paper's core claims. The closest to a major concern is the limited baseline set for planning (Table 1), but this is mitigated by the fact that existing model-based planners (Dreamer, TD-MPC2) operate in fundamentally different output spaces (latent actions) and are not directly comparable to a video-space planner. The paper follows the evaluation protocol of prior work in this specific sub-area (VLP, IRASim).

### Minor

1. **Human evaluation for planning success lacks methodological rigor.** The planning results (Table 1) rely on human raters assessing generated video plans, but the paper reports no details on: number of raters, inter-annotator agreement, confidence intervals, or protocol standardization. Even though this follows conventions from prior work (VLP, IRASim), reporting basic statistics would substantially strengthen the evidence. The 100% success on LIBERO-LONG and Folding is also suspiciously high — it suggests the evaluation may not be sufficiently discriminating.

2. **Ambiguity about whether long-horizon video generation (Table 2) uses ground-truth or generated flows.** The paper explicitly states that the short-horizon dynamics evaluation (Table 4) uses "ground truth flows as conditions," but the long-horizon evaluation (Table 2) does not clarify this. The results text mentions "model-based planning can also help generate high-quality videos by concatenating short-horizon videos generated with rich flow guidance," which implies the full pipeline (predicted flows). This should be stated explicitly. If the flows are indeed generated, the comparison is fair but readers should not have to infer it.

3. **Value module improvement is only qualitatively demonstrated.** The key contribution of the value module fine-tuning (clip-based states) is supported only by visual value curves (Figure 5). A quantitative metric — e.g., correlation with ground-truth task progress, or planning success rate with/without the clip-based fine-tuning — would make the claim more convincing. The indirect evidence from Table 1 (name vs. name-NV) does not isolate the clip-based fine-tuning from other factors.

4. **Missing hyperparameter details harm reproducibility.** The paper does not specify several important parameters: the grid resolution \(N_q\), the number of history frames \(h\), the prediction horizon \(L\), the latent dimension of the flow VAE, the number of planning beams \(B\) and flow candidates \(A\) used in experiments, and the frequency of the beam-replacement operation (though the algorithm shows it occurs at every outer-loop step). These should be reported for all experiments.

5. **Weak scaling evidence.** The scaling experiment (Figure 8) appears to show only two data points per curve. A two-point "scaling curve" does not demonstrate a scaling trend. The claim that "increasing model size can consistently help achieve better performance" requires at least 3–4 points to be meaningful.

6. **No ablation of planning hyperparameters A and B.** The number of flow candidates \(A\) and beams \(B\) are likely to significantly affect planning success. The paper reports no sensitivity analysis for these parameters, making it hard to assess how robust the planning results are to these choices.

7. **Figure 2 (low-level policy) lacks error bars.** The bar chart reports success rates without quantifying variance. Given the paper's own mention of "high variance" for the video-guided variant, including error bars is especially important here.

### Trivial

- The algorithm description says "Periodically Replace" but the pseudocode shows the replacement happens at every outer-loop iteration — this is fine, but the prose could be more precise.
- The word "vale" appears in line 98 instead of "value."

## Nice-to-Haves

- A comparison on the long-horizon video generation benchmark where IRASim (or LVDM) is also given dense flow conditioning via the same cross-attention mechanism would isolate whether the improvement comes from the denser conditioning or from the planning/architecture. However, the ablation study in Table 4 (Ours-SC) partially addresses this by showing that even with flow conditioning, an AdaLN-Zero mechanism (similar to IRASim's conditioning) underperforms cross-attention.
- Demonstrating real-robot closed-loop execution on at least one benchmark would strengthen the "general-purpose manipulation" claim, though the paper's low-level policy experiments (Section 4.3) are a reasonable step in this direction.
- A quantitative analysis of the value module (e.g., correlation with ground-truth progress, or comparing LIV fine-tuning vs. clip-based fine-tuning directly via planning success rates) would make the value module contribution more solid.

## Removed Points

These points from the reviews were checked against the paper and found to be incorrect, overstated, or misattributed:

1. **"Unfair comparison — FLIP uses dense flow information that baselines cannot access" (Harsh Critic Critical Issue 1).** The comparison is between different *methods* with different conditioning modalities; this is standard for system-level evaluation. The flows in the long-horizon evaluation (Table 2) are generated by the planning pipeline, not ground truth. The paper's separate dynamics module evaluation (Table 4) explicitly uses ground-truth flows for a controlled comparison. Calling the comparison "fundamentally invalid" is an overstatement.

2. **"Missing comparison to Dreamer, TD-MPC2, UniSim, IVideoGPT" (Harsh Critic Critical Issue 2).** These methods operate in fundamentally different output spaces (latent actions vs. video plans). Comparing FLIP's video-based planning to Dreamer's latent-space RL would require non-trivial adaptation of one paradigm to the other. The paper compares against UniPi (text-to-video, same output modality) and a self-ablation, which is appropriate for its framing.

3. **"No ablate flow vs. video conditioning in video generation evaluation"** and **"Train LVDM/IRASim with dense flow conditioning"** (Missing Experiments from Harsh Critic). The ablation study in Table 4 (Ours-SC: same dense flow input but with AdaLN-Zero instead of cross-attention) already provides this controlled comparison — showing it's not just the presence of flows but the cross-attention mechanism that matters.

4. **"Requires language-annotated videos — significant data requirement"** (Section-by-Section Notes). The paper clearly states this requirement in the abstract and introduction. This is a stated design choice, not a hidden weakness.

5. **"Slow planning speed acknowledged but does not discuss other missing elements"** (Section-by-Section Notes). The paper explicitly discusses its two key limitations (planning speed, lack of 3D/physical information) in the conclusion. Demanding discussion of additional limitations (closed-loop execution, real hardware) extends beyond the paper's stated scope.

## Novel Insights

The review process reveals that the paper's most interesting aspect is the **"CVAE for flow as action proposals"** design choice: predicting delta scale and direction separately, which outperforms direct coordinate regression (Table 5). This connects to an underexplored question in generative planning — what structure of the action space (absolute vs. relative, scale vs. direction) is best for sampling-based search? The paper also surfaces a practical insight: that value functions for planning require smoothness on long time horizons, and that the unit of temporal contrast (frame vs. clip) can have a significant effect on smoothness. These observations are useful for future work on video-space planning beyond the specific system proposed.

## Suggestions

1. **Clarify the flow source in Table 2.** Add a sentence explicitly stating whether the long-horizon video generation uses the full planning pipeline (predicted flows) or ground-truth flows. If it is the full pipeline, make this explicit.

2. **Add basic rigor to the human evaluation.** Report the number of raters, inter-annotator agreement (e.g., Cohen's kappa or percentage agreement), and confidence intervals or standard errors for the planning success rates.

3. **Report key hyperparameters.** Add a table or appendix specifying \(N_q\), \(h\), \(L\), latent dimensions, \(A\), \(B\), and the training compute (model size, GPU hours) for all experiments.

4. **Provide a quantitative evaluation of the value module.** At minimum, report the planning success rate directly comparing LIV fine-tuning vs. the proposed clip-based fine-tuning (holding everything else equal), or the correlation between learned value and ground-truth progress.

5. **Strengthen the scaling experiment.** Add at least one more model size to demonstrate a trend, or present the scaling evidence more modestly (e.g., as a preliminary observation).

6. **Add error bars to Figure 2** (low-level policy results) and ideally to the main quantitative results (Tables 2, 4) by reporting results over multiple random seeds.

## Score and Decision

This is a solid paper with a genuinely novel approach (flow-centric planning), well-designed architectural components (mixed conditioning, CVAE for flow proposals), and reasonable empirical support across diverse benchmarks. The weaknesses are addressable in a revision and do not undermine the core claims. The main contributions — using dense flow as a planning action representation, the mixed-conditioning DiT, and the clip-based value fine-tuning — are clearly articulated and validated.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>
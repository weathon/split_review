## Summary

This paper proposes a multi-modal agent tuning method: a data synthesis pipeline (query → file → trajectory → verify) that uses GPT-4o mini to generate 20K multi-modal tool-usage trajectories (MM-Traj), and a fine-tuned VLM agent (T3-Agent). Built on MiniCPM-V or Qwen2-VL with LoRA tuning, the T3-Agent achieves strong improvements on the GTA benchmark (outperforming GPT-4/4o-driven Lego Agent) and competitive results on GAIA (best among open-source models).

## Strengths

1. **Scaled-up data synthesis pipeline with diversity.** The pipeline generates 23.5K initial data points, filtered to 20K with 15K files covering 9+ file types, 16 knowledge domains, and 10 tools (Section 3.6, Fig. 3). This substantially exceeds the scale and tool diversity of prior synthetic trajectory datasets (e.g., ~1K from Liu et al., 2024c, as noted in Section 2.1).

2. **Meaningful performance gains on GTA.** Tuning MiniCPM-V-8.5B with MM-Traj yields ~18%, 29%, and 24% absolute improvements on AnsAcc, ToolAcc, and CodeExec respectively over the untuned VLM (Section 5.2). The T3-Agent also outperforms the GPT-4/4o-driven Lego Agent on GTA, demonstrating that VLM trajectory tuning can compete with LLM-prompted agents.

3. **Generalization across architectures and benchmarks.** T3-Agent outperforms all open-source model-driven agents on GAIA validation (7% higher AnsAcc than Qwen2-VL-7B, the best open-source baseline), and the method is validated on two different VLM architectures (MiniCPM-V and Qwen2-VL).

4. **Verifier ablation quantifies quality-control benefit.** The ablation study (Section 5.5) shows that the two-stage verification pipeline contributes a 2.56% improvement on GTA and 0.73% on GAIA, providing controlled evidence that the verification steps are not extraneous.

5. **Human evaluation validates data quality filtering.** A user study with 30 raters scoring 600 random samples (Section 5.4) shows that MM-Traj data scores higher on both task quality and trajectory quality than data filtered out by the verifiers, supporting the verifier's effectiveness.

## Weaknesses

### Fatal

None.

### Major

1. **Abstract misrepresents the teacher model (GPT-4o vs. GPT-4o mini).** The abstract (line 4) states "we prompt the GPT-4o model" to generate queries, files, and trajectories. However, every concrete description of the method uses GPT-4o mini: query generation (line 63), file generation (line 72), trajectory generation via the zero-shot agent (line 79), query-file verification (line 88), and trajectory verification (line 90). GPT-4o and GPT-4o mini are distinct models with different capability ceilings. This discrepancy misleads readers about the quality ceiling of the generated data and erodes trust in reporting accuracy. The body is consistent — only the abstract is wrong — but at a top venue this is a significant reporting error that must be corrected.

2. **Headline performance claim ("10% better than GPT-4 driven agents") is unsupported as stated.** This claim appears *only* in the abstract (line 4). It is never mentioned or defined in the experiments section. The actual results show a mixed picture: on GTA (Section 5.2), T3-Agent beats the GPT-4/4o-driven Lego Agent on some metrics but has "lower CodeExec" and "worse AnsAcc" relative to the HF agent using GPT-4o mini. On GAIA (Section 5.3), the paper explicitly states "Compared with agents driven by closed-source models (e.g., GPT-4), our T3-Agent achieves worse performance." A claim in the abstract that selectively reports only the favorable benchmark without specifying context, and without appearing in the experimental section, is an overclaim.

3. **No ablation isolating MM-Traj's contribution from other training data.** The training recipe combines MM-Traj with Cauldron and open-LLaVa-NeXT datasets (line 167). The "untuned VLM" baseline is the base model without any training, so the observed 18–29% improvements cannot be attributed specifically to MM-Traj. A controlled comparison — e.g., training on Cauldron + open-LLaVa-NeXT alone vs. adding MM-Traj — is necessary to isolate MM-Traj's contribution. Without this, it is unclear whether the improvements come from MM-Traj or from the other two general VLM training datasets.

### Minor

1. **Self-verification loop in data quality control.** The same model (GPT-4o mini) is used to generate trajectories (Section 3.4) and to verify them (Section 3.5). A model that systematically makes certain errors will not reliably identify those same errors when asked to verify. The human evaluation (Section 5.4) shows that kept data scores higher than filtered data on average, which is useful directional evidence, but it does not measure per-item agreement between the verifier and human judges. An independent verification method or a per-item cross-validation would substantially strengthen the quality guarantees.

2. **Thin ablation scope.** The only ablation (Section 5.5) removes the two verifiers. No ablation examines: (a) the trajectory generation model (GPT-4o mini vs. a stronger model), (b) the scale of training data (5K vs. 10K vs. 20K), (c) the query-first vs. file-first ordering, or (d) the contribution of MM-Traj relative to Cauldron/open-LLaVa-NeXT. These would strengthen attribution of the method's specific design choices.

3. **Potential data contamination not discussed.** The image pool for MM-Traj draws from 8 source datasets including COCO, ChartQA, and TextVQA (line 56). The evaluation benchmarks GTA and GAIA contain images and multi-modal files. The paper does not discuss whether any source images or generated queries overlap with evaluation content, which could inflate results.

4. **User study details are sparse.** The human evaluation (Section 5.4) does not report whether the 30 raters each rated all 600 samples or a subset, does not report inter-annotator agreement, and does not specify the exact rating criteria beyond "task quality" and "trajectory quality." These details matter for interpretability.

### Trivial

None.

## Nice-to-Haves

1. **Comparison to alternative trajectory-synthesis methods.** The paper shows MM-Traj training beats untrained baselines, but not that MM-Traj is better than data from existing pipelines (e.g., MLLM-Tool, LLaVA-Plus, DEDER). Such a comparison would substantially strengthen the contribution.

2. **Error analysis of code executability.** The paper notes T3-Agent has lower CodeExec than some baselines. A breakdown of error types (import errors, API errors, argument errors, logic errors) would help identify where the method falls short.

3. **Discussion of tool alignment between training and evaluation.** Clarifying how the 10 tools in MM-Traj map to the tools required by GTA and GAIA would help interpret the results.

## Removed Points

These points were removed from the main review (with brief justifications):

- *"Prompt engineering faces limited reasoning abilities misrepresents baselines"* — Removed as a subjective framing opinion; the paper's motivation is reasonable.
- *"Trajectory verification is not execution-based"* — Partially incorrect. The paper checks code executability at collection time (line 79); the verifier is an additional LLM quality check. Absorbed into the self-verification point above with corrected framing.
- *"Tables cannot be read from the text"* — Removed as a PDF parsing artifact, not a paper problem.
- *Generic formatting/style nitpicks* — Removed per instructions.
- *Claims about missing appendix/proofs* — Removed per instructions (these are stripped by the parser).
- *Strength about "File-before-query generation"* — Content is correct (the paper's query-first approach is a valid design choice) but the label was confusing. Rephrased and merged into strengths.
- *Strength about "addresses an important problem"* — Removed as generic/superficial.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the usual tension between interesting pipeline design and insufficiently controlled evaluation, but do not produce a novel synthesis beyond what the paper already states.

## Suggestions

1. Correct the abstract to say "GPT-4o mini" instead of "GPT-4o," or if GPT-4o was actually used for some component, clarify precisely which.
2. Add a controlled ablation: train on Cauldron + open-LLaVa-NeXT alone and compare to adding MM-Traj, so the contribution of the proposed dataset can be isolated.
3. Add a per-item comparison between the LLM verifier's filtering decisions and human judgments to address the self-verification concern.
4. Tone down or precisely scope the "10% better than GPT-4" claim in the abstract to reflect that it applies only to GTA and specify the metric.
5. Add a data contamination analysis reporting whether source images or generated queries overlap with evaluation benchmarks.
6. Report inter-annotator agreement for the user study.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>
Now I have all the information needed. Let me write the final consolidated review.

## Summary

VideoPrompter proposes a training-free zero-shot video understanding framework that ensembles pre-trained models on both sides of the VLM pipeline: (1) a video-to-text model (Video-ChatGPT/VGPT) generates video descriptions that are fused with visual features, and (2) an LLM (GPT-3.5) generates language attributes, descriptions, and high-level action context to enrich classifier representations. Experiments across action recognition (4 benchmarks, 4 VLMs), retrieval (MSR-VTT), and time-sensitive tasks (Charades, synthetic dataset) show consistent improvements.

## Strengths

- **Consistent zero-shot gains across multiple video tasks and VLMs**: Table 2 shows VideoPrompter improves CLIP top-1 accuracy by +13.29% on HMDB-51, +11.05% on UCF-101, +2.15% on SSv2, and +4.64% on K400. Similar gains are reported for ViFi-CLIP, AIM, and Action-CLIP, confirming the plug-and-play claim.

- **Outperforms descriptor-based baselines with far fewer prompts**: Table 5 shows VideoPrompter (52.51% on HMDB-51) outperforms CUPL (50.44%) while using only 3 language descriptors plus one video-text description versus CUPL's 50 descriptions.

- **Training-free improvement on retrieval and temporal tasks**: Table 3 shows +3.11% R@1 improvement on MSR-VTT retrieval. Table 4 demonstrates a 10-point gain on the time-aware synthetic dataset and +1.4% on Charades, showing temporal understanding gains without additional training.

- **Careful ablations justify design choices**: Figures 3 and 4 demonstrate that (a) fusing video and video-text embeddings is optimal, (b) CLIP-based filtering of noisy descriptions improves accuracy, (c) higher diversity (temperature 0.5) improves results, and (d) VGPT and GPT-3.5 components are complementary.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **The "Tree Hierarchy of Categories" language overstates what is implemented.** The method groups classes into a single level of high-level action contexts (e.g., "playing sports" as parent of basketball, cricket, baseball). While this is a valid parent-child grouping (the prompt asks GPT-3.5 to create "parent and child classes"), calling it a "Tree Hierarchy" sets an expectation of deeper, multi-level structure that the actual implementation does not provide. The grouping is a useful contribution on its own — it would be more accurately described as "high-level action grouping" or "category clustering."

- **Dependence on the quality of a separate generative model (VGPT) is acknowledged but not deeply analyzed.** The paper applies CLIP-based filtering (Section 3.1.2) to discard poor descriptions, which partially addresses this concern. However, the overall pipeline's performance is bounded by VGPT's output quality and biases. A limitations paragraph discussing when VGPT descriptions are likely to fail (e.g., videos with rapid scene changes, unusual actions, or heavy occlusion) would strengthen the paper.

- **No discussion of practical deployment cost.** The method requires running VGPT (video-to-text) and GPT-3.5 (text-to-text) at test time for every video. The paper does not quantify inference overhead, API costs, or wall-clock time compared to baselines. While not fatal, this information would help practitioners assess trade-offs.

- **Evaluation lacks error analysis.** The paper does not break down where gains concentrate (e.g., object-manipulation vs. full-body actions, static vs. dynamic scenes). Such analysis would strengthen the claim that video-to-text descriptions provide complementary information.

### Trivial

- The phrase "Tree % parent-child Hierarchy" (line 35) contains a stray LaTeX comment artifact. In the compiled PDF this would appear as "Tree Hierarchy" — harmless but worth cleaning up in the source.

## Nice-to-Haves

- A comparison with simple text-based caption augmentation (e.g., back-translation) for retrieval would help isolate the source of gain from VGPT-based visual enhancement.
- An ablation showing performance with and without the high-level action context on SSv2 (where the paper notes GPT-3.5 puts all classes in one group, yielding no benefit) would transparently demonstrate the method's limitations.

## Removed Points

- **Negative classifier missing**: REMOVED because both mentions in the paper are LaTeX comments (`%`). The compiled PDF contains no claim about a negative classifier. The harsh critic read raw LaTeX source comments as content, which does not reflect the actual paper.
- **"Tree Hierarchy is not a tree" as a critical issue**: SIGNIFICANTLY WEAKENED from "critical issue" to minor presentation nitpick. The implementation IS a hierarchy (parent→child single-level grouping, prompted explicitly for "parent and child classes"). While the terminology is slightly inflated, the underlying structure exists and is correctly evaluated in Table 6. The criticism that there is "no hierarchy" is factually wrong.
- **"Fix the abstract" suggestion**: Based on the false premise that the abstract claims a negative classifier. The abstract in the compiled paper does not contain this claim.
- **Generic formatting/style complaints**: Removed.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface an angle or synthesis the paper itself missed.

## Suggestions

1. Replace "Tree Hierarchy of Categories" with more precise terminology such as "high-level action grouping" or "semantic category clustering" to accurately describe the single-level parent-child structure.
2. Add a limitations paragraph discussing when VGPT descriptions are likely to be unreliable and the computational/test-time overhead of the pipeline.
3. Include an error analysis (per-action-type breakdown of gains) to clarify where the method helps most.

## Score and Decision

The paper makes a solid empirical contribution: it demonstrates that simultaneously enriching both visual features (via video-to-text) and classifier features (via LLM) improves zero-shot video understanding consistently across multiple settings. The experiments are thorough, covering 4 action recognition benchmarks, 4 VLMs, retrieval, and time-sensitive tasks, with careful ablations. The two main criticisms raised by the harsh reviewer are invalid (based on misreading LaTeX comments as content). The remaining issues are minor and would not change the accept/reject calculus. The paper delivers what it claims, and the claims themselves are well-supported.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>
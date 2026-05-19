- Decision: Reject
- Avg Score: 3.75
- Scores: 3, 3, 3, 6
Now I have all the information I need. Let me construct the final review.

**Verification summary against paper:**

1. **No quantitative "no prompt" baseline**: CONFIRMED. Table 1 compares prompt variants against each other; no column for GPT-4o without 3DAxisPrompt on the same metric. The qualitative "standard GPT-4o" examples (Figures 1, 4) are not quantified.

2. **Small evaluation scale (20 scenes)**: CONFIRMED. Paper explicitly states "randomly selected 20 scenes from each test dataset" (line 121) and acknowledges API quota limitations. No error bars, confidence intervals, or significance tests.

3. **Missing point cloud text format specification**: CONFIRMED. Line 61 says "point cloud p^i provided in text format" but never specifies how many points, format, sampling, or how presented to GPT-4o. This is a reproducibility gap.

4. **No comparison to existing methods**: PARTIALLY TRUE. The paper says "No previous work has presented localization errors related to 3D spatial grounding" (line 125). Comparing against trained 3D detectors is outside scope, but a simple heuristic baseline would help.

---

## Summary

The paper proposes 3DAxisPrompt, a visual prompting method that adds 3D coordinate axes, object marks (from SAM), and 2D contours to multi-view rendered images to elicit 3D grounding and reasoning in GPT-4o without fine-tuning. It systematically investigates various visual prompt formats (axis-only, depth, multi-view, tri-view, 2D/3D marks), and evaluates across indoor/outdoor localization, route planning, robot action prediction, and coarse object generation using four datasets.

## Strengths

- **Systematic investigation of visual prompt formats for 3D understanding** (Sections 3.2–3.3): The paper provides the first structured exploration of how different 3D cues (axis-only, depth, multi-view, tri-view, AABB, OBB, 3D edge points, 2D contour) affect GPT-4o's 3D spatial reasoning. Table 1 provides a quantitative comparison across many of these formats, which is a genuine contribution to prompting methodology.

- **Quantitative evaluation across four diverse 3D tasks**: Tables 1 and 2 report concrete numbers for indoor localization (NRMSE for to-center and to-bbx distances), route planning (79% avg. success), outdoor localization (vehicle vs. vegetation), and robot action prediction (grasp/release). The attempt to quantify performance across such different tasks — indoor, outdoor, robotic — is a strength.

- **Ablation study isolating essential components** (Section 4.3, Figure 7): Removing axis ticks causes complete failure; removing axis labels increases to-bbx error by 37%; increasing observation images from 1 to 8 reduces error by 41%. These are clear, quantitative findings that directly inform understanding of what makes the method work.

- **Novel finding about tri-view vs. multi-view prompting** (Section 3.2): The paper discovers that tri-view images can trigger 3D spatial grounding in GPT-4o even without a text-format point cloud, while multi-view alone cannot. This is a specific, non-obvious empirical finding about MLLM capabilities.

- **Broad dataset coverage**: Uses ScanNet (indoor), nuScenes (outdoor), FMB (robotic manipulation), and ShapeNet (object generation), demonstrating applicability beyond a single domain.

## Weaknesses

### Fatal
None.

### Major

- **Missing quantitative "no prompt" baseline for the central claim**: The paper claims 3DAxisPrompt *elicits* 3D grounding in GPT-4o, but Table 1 compares different prompt variants against *each other* (Mark, Mark+2D Contour, Mark+3D Edge Points, etc.) — not against GPT-4o receiving the same task prompt, same images, and same point cloud text *without* the visual 3D axis/contours. The qualitative "standard GPT-4o" examples (Figures 1, 4) are suggestive but not quantified. The ablation study (Figure 7) removes axis *elements* (ticks, labels) but never removes the axis entirely. Without this control, the paper cannot demonstrate that the visual prompt is the cause of the observed 3D reasoning — GPT-4o might already achieve comparable performance on these tasks without the added axis. This is the single most important experiment missing from the paper.

- **Small evaluation scale with no statistical reliability**: All quantitative results are based on 20 randomly selected scenes per dataset (explicitly stated line 121). No confidence intervals, error bars, standard deviations, or significance tests are reported for any metric. With only 20 scenes, differences of 7% or 19% could fall within noise. For route planning (binary success/failure), a single failure shifts the rate by 5pp; the reported 79% average over an unspecified N is not interpretable without uncertainty quantification. The paper acknowledges the API quota limitation but does not qualify its conclusions accordingly.

- **Unspecified point cloud text input format**: The problem formulation (Equation 2, line 68) includes a text-format point cloud \(p^i\) as input. The paper states (line 61) that GPT-4o "can recognize the text file as the point cloud" but never specifies: (1) how points are formatted (raw coordinates? normalized? complete scene or sampled?), (2) how many points are provided, (3) the prompt template used to present this input, or (4) the coordinate system and range. This is a reproducibility gap. Moreover, the ablation study does not test what happens when the point cloud text is removed — so we cannot tell whether the *visual* 3D axis is driving performance or the explicit coordinate data is doing the heavy lifting.

### Minor

- **Absolute performance numbers are uninterpretable without any reference point**: For indoor localization, the best variant achieves 0.28 NRMSE (to-center) — but there is no baseline (e.g., predicting the scene center, random guessing, nearest-neighbor from point clouds) to contextualize this number. Even a simple heuristic baseline would help the reader judge whether 0.28 is impressive or trivial. The paper's justification ("No previous work has presented localization errors related to 3D spatial grounding") acknowledges the absence of MLLM-based 3D localization benchmarks but does not excuse the lack of a minimal interpretability baseline.

- **Several investigation findings rely on unquantified observations**: Section 3.2 reports that "depth compensation methods yielded unsatisfactory results" and "tri-view images successfully provoke 3D spatial grounding" — these are based on qualitative examination, not quantitative evaluation. The design decision to use multi-view over tri-view is justified only qualitatively (occlusion issues).

- **Coarse object generation experiment is purely qualitative** (Section 4.2, last paragraph): This task (ShapeNet keypoints → object skeleton) is presented as an additional demonstration but provides no quantitative evaluation, reducing its evidentiary value.

### Trivial
None.

## Nice-to-Haves

- A per-scene breakdown of results (e.g., scatter plot of predicted vs. ground-truth positions) would be more informative than aggregate NRMSE.
- A systematic failure analysis for route planning (what types of errors occur?) would strengthen the paper.
- A comparison of tri-view vs. multi-view *with and without* point cloud text would more rigorously justify the multi-view design choice.

## Removed Points

These points from the original reviews were removed or demoted. Treat with caution:

- **Criticism about no comparison to existing trained 3D localization methods (PointLLM, PointNet, etc.)**: The paper's scope is *zero-shot MLLM prompting without fine-tuning*. Comparing against specialized trained models would be asymmetric against the authors' method. However, the request for a simple interpretability baseline (e.g., scene center) is kept as a Minor weakness.
- **"Strengthening the Paper on Its Own Terms" suggestions**: These are constructive suggestions, not weaknesses, and are incorporated into Nice-to-Haves above.
- **Request for larger evaluation scale as a fatal flaw**: The paper acknowledges the API quota constraint. The issue is real but not fatal; it is covered under the Major weakness about evaluation scale and statistical reliability.
- **Criticism about "comprehensive" claim being unwarranted**: The paper does investigate many prompt formats (axis, depth, tri/multi-view, 2D/3D marks, AABB, OBB, edge points, contours) — "comprehensive" is a reasonable characterization for a single paper's exploration.
- **Formatting/style nitpicks, missing appendix concerns, and grammar/typo issues**: These are parser artifacts or non-substantive; excluded per filtering rules.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a clear structural gap (no quantitative "no prompt" baseline) but do not uncover contradictions or deeper patterns in the data that the paper itself missed.

## Suggestions

1. **Add a "no visual prompt" baseline**: For all quantitative tasks (indoor localization, route planning, outdoor localization, robot action prediction), compare 3DAxisPrompt against GPT-4o receiving the same task prompt, the same multi-view rendered images, and the same point cloud text — but without the 3D axis, marks, or contours overlaid. This directly tests the central claim.
2. **Ablate the point cloud text input**: Test performance with the full method, with the point cloud text removed, and with neither the visual prompt nor the point cloud text. This isolates whether the visual or textual 3D information is driving performance.
3. **Report error bars or per-scene distributions**: With only 20 scenes, report per-scene results, standard deviations, or at minimum the range. For binary metrics (route planning success), report exact binomial confidence intervals.
4. **Specify the point cloud text format**: Report the exact format (e.g., "x y z per line, N=1000 random samples, normalized to [0,10]"), the prompt template used to present it, and any preprocessing.
5. **Acknowledge the preliminary nature more clearly**: The paper currently concludes with confident language ("effectively perceive," "fine-grained perception and reasoning"). Given the small N and missing baseline, the conclusions should be tempered to reflect an exploratory/pilot study.

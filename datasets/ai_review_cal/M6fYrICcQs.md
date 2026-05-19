- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6
Now I have all the information needed. Let me write the consolidated review.

## Summary

This paper proposes the Chain-of-Region (CoR) framework, which combines traditional OpenCV-based techniques (connected components, contour detection, shape detectors) with VLMs to decompose scientific diagrams into regions, collect structural and semantic metadata per region, and feed that aggregated information into a VLM for question answering. The method is evaluated on the MMMU dataset's scientific diagram subset (5,210 images) using GPT-4o, GPT-4-turbo, and GPT-4o-mini as backbones. A separate segmentation analysis compares CoR's region masks against SAM2 on 100+ manually annotated samples.

## Strengths

- **Plug-and-play compatibility demonstrated across multiple backbones**: The paper applies CoR to three GPT-series models (GPT-4o-mini, GPT-4-turbo, GPT-4o) and reports that it yields consistent improvements over raw VLMs and standard prompting baselines (Section 4.1). This supports the claim that CoR integrates with pre-trained VLMs without retraining.

- **Segmentation advantage over SAM2 on scientific diagrams is quantitatively documented**: The paper reports margins of 20.8% (individual) and 13.0% (grouped) mIoU over SAM2 on manually annotated MMMU samples (Section 4.2). These margins are stated in the text and provide evidence that classical CV techniques are better suited for isolating fine visual elements in structured diagrams than a general-purpose deep segmenter.

- **Clear motivation and well-structured pipeline**: The paper identifies a genuine perceptual limitation of current VLMs on scientific diagrams (e.g., Figure 1's bar-value example) and presents a logically structured three-stage pipeline (initialize → split → merge) whose design choices are grounded in the observation that scientific diagrams have homogeneous colors and structured patterns (Section 3). The method description is accompanied by code snippets and a clear overview figure.

- **Sensitivity analysis on key hyperparameters**: The paper varies the recognition call limit and cluster number and reports that cluster count significantly impacts performance, with an optimum at moderate granularity (Section 4.1, Figure 4 description). This provides practical guidance for practitioners.

## Weaknesses

### Fatal
None.

### Major

- **Evaluation confound: CoR uses substantially more VLM calls than most baselines, and the benefit of region decomposition is not isolated from the benefit of extra model queries.**  
  CoR performs up to 10 VLM calls for structure recognition (Section 3.1.2), followed by B=5 per-region semantic extraction calls (Section 3.2), plus one final answer call — up to ~16 total VLM queries per diagram. By contrast, the Raw VLM, Zero-shot CoT, and Few-shot CoT baselines each use a single call. The SAM2 baseline partially controls for this by using the same B=5 per-region extraction calls, but CoR still has ~10 additional VLM queries for structure recognition that SAM2 does not. The paper acknowledges this difference (line 78: "recognition call limits (ex. 10) per diagram") and even notes that "the recognition call limit has a relatively minor influence on the final outcomes" (line 130), but this claim cannot be verified from the extracted text (Figure 4 is missing). Without a controlled experiment that isolates the effect of region decomposition from the extra VLM budget, the magnitude of CoR's specific contribution is unclear.  
  *Why it matters*: The core claim is that region decomposition via classical CV improves diagram QA. If most of the gain comes from giving the VLM more opportunities to refine its answer rather than from the quality of region decomposition, the paper's contribution is substantially weaker.

- **The segmentation evaluation is conducted on a biased sample that limits generalizability.**  
  The paper explicitly constructs the segmentation dataset from "instances where the raw predictions of GPT-4V (gpt-4-turbo) failed, thus representing challenging scenarios" (line 146). The sample is small (100+ images) and selected specifically for difficulty. While this is a reasonable strategy for a stress test, it inflates the apparent gap between CoR and SAM2 — on easy cases where SAM2 already segments adequately, the difference may be much smaller or even reversed. The paper does not report segmentation results on a random or representative sample from the 5,210-image main evaluation set, nor does it show that better segmentation quality causally translates to better QA accuracy in a controlled setting.  
  *Why it matters*: The segmentation analysis is presented as supporting evidence for why CoR outperforms SAM2 in QA, but the selection bias and small sample size weaken this link. A reader cannot assess whether the observed segmentation advantage holds broadly.

### Minor

- **The "white-box" and "cost-effective" claims are somewhat overstated.**  
  The paper frames CoR as a "white-box algorithm" employing "transparent, rule-based region separation methods" (Section 1, Claim 1). While the OpenCV components are indeed interpretable, the VLM-assisted structure recognition step (Section 3.1.2) is a black-box call whose internal reasoning is opaque. Similarly, the "cost-effective" claim (Claim 2) states that "operations... can be executed in milliseconds" on CPU, but this ignores the API cost and latency of up to ~16 VLM calls per diagram. These are real trade-offs that should be acknowledged alongside the claimed benefits.

- **The segmentation analysis is not directly connected to the QA results.**  
  The paper shows that CoR produces better segmentation masks than SAM2 (Table 2) and separately shows CoR outperforms SAM2 in QA (Table 1), but never demonstrates that the segmentation quality *causes* the QA improvement. A controlled experiment (e.g., using SAM2 masks processed through the same region decomposition pipeline vs. CoR masks) could establish this link, but none is provided. As it stands, the two evaluations run in parallel rather than supporting each other causally.

- **Several implementation details are underspecified.**  
  The exact prompt used for VLM-assisted structure recognition is not provided. The "offset" value in the region initialization code (Section 3.1.1) is not defined. The structured merge section mentions "mature OCR tools" and "heuristic rules" (Section 3.1.3) without specifying which tools or what rules. These details would be needed for exact reproduction, though the paper provides sufficient high-level description to convey the approach.

### Trivial
- The paper contains several minor grammatical issues (e.g., "Groundth Truth Details" in the section header, "ftiness" in line 160) but these do not affect comprehension.

## Nice-to-Haves

- **Ablation of CoR components**: The paper does not ablate individual design choices (skip the structured merge? skip the VLM recognition step? use a fixed rule instead of VLM for shape classification?). Such ablations would help attribute performance to specific components and strengthen the empirical contribution.

- **Failure analysis**: The paper's discussion of results is uniformly positive. An analysis of categories or cases where CoR does not improve (or underperforms) would help scope the method's applicability and be more scientifically balanced.

- **Statistical significance / variance reporting**: The paper reports single accuracy numbers without confidence intervals or statistical significance tests. Given that the MMMU evaluation set is 5,210 images, standard errors and significance comparisons across methods would strengthen confidence in the rankings.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Missing numerical tables (Table 1, Table 2, Figure 4)**: The harsh critic argued that the paper's core empirical evidence is absent because tables and figures appear as image placeholders. However, these are PDF extraction artifacts — the original submission contained proper numerical tables and figures. Per the review guidelines, formatting artifacts from extraction should not penalize the paper. The paper does include qualitative discussion of Table 1 and Figure 4 results in the running text (lines 126–133, 160).

- **Overstated novelty / "nearly forgotten techniques" framing**: The critic objected that connected components and contour detection are standard toolkit operations. This is a subjective stylistic judgment rather than a concrete flaw. The paper does not claim algorithmic novelty in the CV techniques themselves — it claims a *novel pipeline* combining these techniques with VLMs, which is a fair characterization.

- **Missing related work on chart extraction tools (PlotDigitizer, WebPlotDigitizer, etc.)**: The paper's scope is broader than chart extraction (general scientific diagrams), and the related work section adequately covers the VLM prompting and spatial understanding literature most directly relevant to the paper's framing. Demanding coverage of every related tool is scope creep.

- **Missing comparison with fine-tuned chart-specific models (ChartLlama, DePlot, MatCha)**: The paper explicitly scopes itself to plug-and-play methods that do not require fine-tuning (Section 2, line 40: "these approaches necessitate fine-tuning procedures... our method integrates traditional CV techniques with VLMs to more efficiently handle complex scientific diagrams"). Evaluating against fine-tuned models would be a different experimental setup and goes beyond the paper's stated scope.

- **Strength Finder's specific accuracy numbers from Table 1**: The Strength Finder reported specific numbers (GPT-4o: 56.2%→65.7%, GPT-4-turbo: 47.1%→62.1%, GPT-4o-mini: 46.1%→50.8%). These numbers are not present in the extracted text (they were in the inaccessible table image). Since they cannot be verified from the available text, they are treated as unconfirmed and not included as verified strengths in the main review. The paper's qualitative claim of consistent improvements across backbones is retained.

## Novel Insights

None beyond the paper's own contributions. The two reviewers' perspectives do not generate a novel synthesis beyond what the paper itself states.

## Suggestions

1. **Isolate the effect of extra VLM calls from region decomposition**: Add an ablation where CoR skips the VLM-assisted structure recognition step (uses only default detectors) and compare performance. Alternatively, give baselines a multi-step reasoning protocol that uses the same number of VLM queries as CoR. This would disentangle whether the gains come from better region masks or simply more model invocations.

2. **Report segmentation results on a random sample**: Complement the failure-case segmentation analysis with results on a random or representative subset of the MMMU diagram pool. This would address selection-bias concerns and establish the generality of the segmentation advantage.

3. **Link segmentation quality to QA accuracy**: Show a controlled comparison where CoR's final QA performance is evaluated using CoR's own masks vs. SAM2's masks (with all other pipeline stages identical). This would directly test whether better segmentation causes better QA.

4. **Report per-category breakdowns with statistical precision**: Provide full numerical tables with per-category accuracy, standard errors, and significance tests. Include average VLM call counts and estimated API cost per diagram to contextualize the "cost-effective" claim.

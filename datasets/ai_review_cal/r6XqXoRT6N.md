- Decision: Reject
- Avg Score: 4.20
- Scores: 5, 3, 5, 3, 5
Now I have all the information needed. Let me synthesize the final review.

## Summary

PCIG is a training-free framework that combines LLM-based prompt analysis, knowledge graph construction, controllable diffusion models (InstanceDiffusion), a visual text generation module (AnyText), and web-searched reference images to produce text-to-image outputs consistent with the input prompt across object, text, and factual dimensions. It categorizes objects into three types (GO, TEXT, PN) and applies different generation strategies for each. On the MHaluBench benchmark, PCIG achieves 89.55% overall accuracy, substantially exceeding the best prior method (InstanceDiffusion at 64.09%), with large gains on text hallucination accuracy (82.54% vs. 9.52%) and factual hallucination accuracy (77.78% vs. 8.33%).

## Strengths

- **Comprehensive taxonomy and modular handling of three distinct consistency challenges:** The paper defines attribute/object (AH/OH), scene-text (SCH), and factual (FH) hallucinations (Section 3.1) and maps them to three object categories — GO, TEXT, PN — each handled by a separate generation paradigm (Sections 3.2, 3.5). This systematic decomposition is a concrete design choice directly supported by the per-category performance breakdown in Table 1.

- **State-of-the-art overall accuracy on MHaluBench with large gains on text and factual hallucination:** PCIG achieves 89.55% overall accuracy (Table 1), surpassing InstanceDiffusion (64.09%) and DALL·E 3 (45.45%). The modular design delivers on its promise: text hallucination accuracy improves from 9.52% (InstanceDiffusion) to 82.54% and factual hallucination accuracy from 8.33% (MIGC) to 77.78%.

- **Ablation evidence isolating the contribution of the text generation module:** Table 2 shows that removing the text module drops TH Acc from 82.54% to 9.52%. Table 3 further shows that plugging the text module into GLIGEN, MIGC, and InstanceDiffusion boosts TH Acc by 68–73 percentage points. These controlled experiments provide strong quantitative evidence that the text module is both necessary and transferable.

- **Integration with multiple controllable diffusion backbones:** Table 3 demonstrates that PCIG's text module improves TH Acc significantly across GLIGEN, MIGC, and InstanceDiffusion. This shows the framework is not tied to a single base model and can serve as a plug-in for layout-to-image systems.

## Weaknesses

### Fatal
None.

### Major

- **PCIG does not improve over InstanceDiffusion on general objects (OH), yet the paper claims universal superiority:** OH accuracy for PCIG is 94.89%, while InstanceDiffusion alone achieves 95.62% (Table 1). The difference is marginal and within noise, and PCIG is actually *slightly worse*. The paper never acknowledges this, instead stating it "outperforms the baseline models in all metrics" (line 188). Since GO objects constitute the majority of MHaluBench prompts (137/220), the headline improvement is entirely driven by the TEXT and PN categories — which is fine, but the paper should frame honestly. The paper is essentially a pipeline for handling text and factual-object failure modes that prior layout-to-image models ignore, not a universal consistency enhancer.

- **Extremely small sample sizes for FH (n=18) and TFH (n=2) make the reported accuracies uninformative:** FH accuracy of 77.78% means 14/18 correct — a single misclassification changes the accuracy by ~5.6 percentage points. TFH accuracy of 50.00% means 1/2 correct — a single example determines 50 points. These numbers are reported without any uncertainty quantification. The conclusion that PCIG achieves "state-of-the-art" FH accuracy is unsupported by 18 examples. The paper should either collect a larger FH test set, present per-example results with confidence intervals, or substantially temper its claims.

- **No human evaluation:** The paper relies entirely on UniHD (an automatic hallucination detector from the same benchmark) to evaluate all generated images (line 96). The detector may have systematic biases, particularly since MHaluBench was designed for training/evaluating hallucination detectors. Human verification on a representative subset would substantially strengthen the evidence, especially given the small FH/TFH sample sizes.

### Minor

- **Vague description of PN image integration:** Section 3.5 states that for PN objects, retrieved images are "seamlessly integrated into the model's primary input stream" (line 80). The paper does not specify the technical integration mechanism — whether this means pasting the retrieved image at the bounding-box location, using it as a conditioning signal, applying inpainting, or something else. This is relevant for reproducibility and for understanding failure modes.

- **The "w/o KG extraction" ablation is underspecified:** The ablation locates objects "without relation extraction and knowledge graph construction" (line 224), causing OH accuracy to drop from 94.89% to 64.96%. But the paper does not specify *how* objects are located in this ablation (randomly? uniformly distributed? some heuristic?). Without this detail, it is unclear whether the drop is due to removing spatial reasoning or due to the specific fallback strategy used.

- **No systematic failure analysis:** The paper presents qualitative successes (Figures 3–5) but no systematic analysis of failure modes (e.g., do FH errors come from the search engine returning wrong images? from the diffusion model altering the pasted image? from the LLM misclassifying an object as GO vs. PN?).

### Trivial

- **No confidence intervals or uncertainty quantification:** Especially for the small-sample FH/TFH results, bootstrapped confidence intervals or raw counts would be informative.

## Nice-to-Haves

- The knowledge graph step's unique contribution could be further isolated by comparing against a baseline where GPT-4 produces bounding boxes directly (with the same object extraction but without triple/KG construction), rather than only comparing against completely removing spatial reasoning.
- A comparison against an end-to-end T2I model (e.g., DALL·E 3) followed by separate inpainting for text/factual objects would help isolate the benefit of the layout-first approach.
- Reporting average generation time would be useful for practical deployment assessment.

## Removed Points

**These points are flagged to be removed, treat them with caution:**

- *"Unfair comparison with layout-to-image baselines on TH and FH"* — REMOVED. The paper is transparent that baselines receive identical bounding boxes (line 128). Showing that existing methods cannot handle text/PN is informative baseline context, not an unfair comparison. The controlled experiment in Table 3 provides the fair apples-to-apples comparison. The GO-specific overclaiming (above) subsumes the valid portion of this criticism.
- *"Missing prompt templates make the method non-reproducible"* — REMOVED. The paper references prompt template figures (prompt_template, promptwokg_template, promptwooe_template) that were present in the original submission but stripped by the parser. Per policy, appendix/figures stripped by the parser are assumed to exist.
- *"The paper should acknowledge that layout-to-image baselines receive identical bounding boxes"* — REMOVED. The paper already explicitly states this on line 128.
- *"The paper should discuss that cost/latency of GPT-4 is a practical limitation"* — REMOVED. The Limitations section already acknowledges cost ($0.08/generation). Further discussion is a nice-to-have, not a weakness.
- *The Strength Finder's praise of the paper being "a concrete improvement over methods that treat all inconsistencies uniformly"* — KEPT, as it is specifically grounded in the paper's taxonomy.
- *"The conclusions about different LLMs are obvious"* — REMOVED. Showing empirical results for different LLMs is standard practice; obviousness does not make it a weakness.
- *Strength Finder claims about "Ablation study validating the knowledge graph and object extraction components"* — KEPT as a supporting strength but weakened by the underspecification noted in Minor weakness #2.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Restructure the evaluation around the three object categories: report OH accuracy on GO-only prompts, TH accuracy on TEXT-only prompts, and FH accuracy on PN-only prompts. This would honestly reflect what the framework contributes to each category and naturally clarify that the baselines are not designed for the TEXT and PN categories.
2. Explicitly acknowledge that PCIG does not improve over InstanceDiffusion on general objects, and frame the contribution as specifically addressing the TEXT and PN failure modes that prior layout-to-image models ignore.
3. Add human evaluation on a representative subset (e.g., 50 images covering all categories), or at minimum report agreement statistics between UniHD and human judgments.
4. Collect additional FH examples or report bootstrapped confidence intervals for FH and TFH results. At a minimum, report raw counts (e.g., "14/18 correct") alongside percentages.
5. Specify the exact mechanism for PN image integration and the exact fallback method used in the "w/o KG extraction" ablation.
6. Add a systematic failure analysis showing what types of errors remain (LLM misclassification, search-engine failure, diffusion-model alteration of pasted content, etc.).

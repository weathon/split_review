- Decision: Reject
- Avg Score: 4.25
- Scores: 5, 3, 3, 6
Now I have all the information I need from the earlier complete file read. Let me produce the final consolidated review.

---

## Summary

This paper identifies a performance bottleneck in 3D Multimodal LLMs where larger backbones (13B) underperform smaller ones (7B), and proposes Streamlining Preference Alignment (SPA), a post-training method that uses 3D-masked point clouds as negative samples in a contrastive-style loss to widen the probability gap between correct and degraded outputs. SPA is evaluated on object-level (ModelNet40 classification, Objaverse captioning) and scene-level tasks, and a new multiple-choice benchmark (3DCQA) is introduced. Experiments show SPA outperforms the base PointLLM model and two-stage post-training baselines (DPO, SimPO) on standard benchmarks.

## Strengths

1. **Identifies and documents the performance bottleneck in 3D MLLMs with concrete evidence.** Figure 1 empirically shows that the 13B PointLLM model achieves lower accuracy on ModelNet40 and lower captioning scores on Objaverse compared to the 7B model. This is a genuine finding that motivates the work, and Figure 3 further investigates it across encoder swaps and SFT epochs (Section 3.1). This goes beyond anecdotal observation.

2. **SPA outperforms existing two-stage post-training baselines (DPO/SimPO) on standard benchmarks.** Table 4 compares SPA against DPO and SimPO under both text-corruption and data-augmentation setups on the General benchmark. The comparison includes a "data augmentation" variant of DPO that uses the same 3D masking strategy, making it a relevant and strong baseline. SPA shows superior results, particularly for classification and captioning.

3. **Ablation experiments systematically validate the choice of 3D masking as the negative augmentation.** Table 2 compares 3D masking against random dropping and Gaussian noise at varying noise levels (12.5%–100%). The optimal noise level (25%–50%) is identified, and the paper provides a reasonable rationale grounded in FPS + KNN properties of the point cloud encoder. This is a clean ablation that supports the design choices.

4. **The loss derivation connecting the approach to contrastive learning is explicitly presented.** Equations 4–6 in Section 3.2 show the progression from a sigmoid-based formulation to a compact loss, and the connection to NCE-style objectives is drawn. Whether or not the "InfoNCE equivalence" phrasing is precise (see weakness below), the derivation itself clarifies the mechanism.

## Weaknesses

### Major

1. **The 3DCQA benchmark lacks validation.** The paper introduces this benchmark (Section 3.3) as a contribution, using Llama-3.1 to automatically generate multiple-choice questions from ground-truth captions. However, no human agreement study, no analysis of question quality/ambiguity, and no correlation check against established metrics (e.g., GPT-4 evaluation scores on captioning) is provided. The claim that the benchmark "reduces subjectivity" is unsubstantiated — LLM-generated questions introduce their own biases. This directly affects the interpretability of Table 3 results (scene-level evaluation on 13B PointLLM), which are used to support claims about SPA's benefits for grounding, navigation, and relational reasoning. While the paper's core claims on the General benchmark are not dependent on 3DCQA, the scene-level claims specifically are built on this unvalidated instrument.

### Minor

1. **The method is framed as "preference alignment" in a way that overclaims its connection to the RLHF/DPO literature.** The title and Section 3 consistently use terminology like "preference alignment" and "preference modeling." However, SPA uses original vs. masked point clouds as positive/negative pairs — no human preferences, reward model, or output preference pairs in the standard sense. The paper partially acknowledges this contrast in Figure 4's caption ("In contrast, SPA generates preference-aligned data via symmetric noise sample inputs"), but the framing throughout invites comparison to DPO/RLHF in a way the method does not deliver. This is a framing mismatch, not a technical flaw, but it should be corrected in the title/abstract.

2. **The core scaling claim — that SPA restores the expected 13B > 7B ordering — is not explicitly demonstrated in the discussion.** The paper's central motivation (Section 1, Figure 1) is that 13B underperforms 7B. Section 4.2 states SPA "significantly addresses the critical issue of LLM backbones with less than 7B parameters," which is confusingly worded given the actual bottleneck. The text discusses 13B results in Table 3 and Table 1 but does not have a clear statement or visualization comparing 7B+SPA vs. 13B+SPA on the same metrics. The data may be present in the tables (which are image-embedded), but the prose does not explicitly confirm that the scaling hierarchy is restored.

3. **The claim that the loss is "fundamentally equivalent to InfoNCE" is imprecise.** The derived loss (Equation 6) uses a single negative sample per positive, making it a binary NCE objective. InfoNCE standardly uses categorical cross-entropy over one positive and *multiple* negatives. While the spirit of the connection to contrastive learning is correct, this overstatement signals imprecision in theoretical framing.

4. **Key implementation details are underspecified.** The paper does not state (a) which parameters are updated during SPA training (full model vs. projector only?), (b) whether the full pipeline (encoder → projector → LLM) is run on the masked input or only a subset, and (c) how SPA weights are initialized relative to the base PointLLM checkpoint. These are needed for reproducibility.

### Trivial

- Line 142 contains the confusing phrase "LLM backbones with less than 7B parameters," which contradicts the paper's own framing of the bottleneck (13B > 7B). This appears to be a writing error or parser artifact.
- The claim that SPA is "plug-and-play" (Section 1) is only demonstrated on PointLLM with PointBERT encoder; no experiment on another encoder architecture is provided.

## Nice-to-Haves

- Conduct a human evaluation of 3DCQA (e.g., annotator agreement, correlation with existing captioning metrics) to validate the benchmark. This is the most impactful improvement the paper could make.
- Add an explicit table or figure showing 7B vs. 13B performance before and after SPA on the same metrics, directly confirming that scaling is restored.
- Test SPA on at least one alternative 3D encoder (e.g., PointNeXt) to support the "plug-and-play" claim.
- Describe DPO-DA baselines more precisely: does "data augmentation" for DPO use the same 3D masking? If so, this is a strong and relevant baseline that should be highlighted.

## Removed Points

- **"Mischaracterization of the method as preference alignment" (harsh critic's strongest framing):** Kept above as a minor weakness but downgraded from "critical issue" to "minor" because the paper *does* distinguish itself from human-preference alignment in Figure 4's caption ("...aligning models with human preferences using reinforcement learning... In contrast, SPA generates preference-aligned data via symmetric noise sample inputs"). The framing is imperfect but the paper is not deceptive.
- **Criticism that Section 3.1's reasoning ("increasing epochs mitigates gap, therefore issue is alignment") is weak:** Removed. The paper explicitly says "This strongly suggests the core issue is related to alignment" — this is appropriately hedged as a hypothesis supported by empirical observation, not a claimed proof.
- **Criticism that the bottleneck cause is asserted without direct evidence:** Removed. The paper presents multiple converging observations (encoder swaps don't fix it, SFT epochs partially mitigate it, post-training fixes it) and synthesizes them into a plausible hypothesis. The paper does not claim to have proven the root cause mechanistically.
- **Criticism about "unfair comparison" or speculation about DPO baselines:** The paper describes the DPO-DA mode as "harnessing the internal knowledge of the model in conjunction with SPA" and specifies the masking procedure. This is sufficient information for a baseline description.
- **Various formatting/style nitpicks and missing appendix content:** Removed per instructions (parser artifacts, missing appendix due to parsing).
- **Strength Finder's generic strengths (problem importance, "addressed an important problem"):** Removed. The retained strengths are all specific, concrete, and verifiable from the paper.

## Novel Insights

None beyond the paper's own contributions. The two reviews largely agree on the paper's strengths and weaknesses — the harsh critic accurately identifies the framing mismatch and benchmark validation gap, while the strength finder correctly highlights the bottleneck documentation and ablation rigor. The key novel insight from synthesis is that the paper has two separable contributions (the SPA method and the 3DCQA benchmark) with very different levels of validation: the method is reasonably well-supported on standard benchmarks, while the benchmark contribution is currently unvalidated and should not be weighed as a contribution until assessed.

## Suggestions

1. **Validate 3DCQA with human annotation** or at minimum show that accuracy on 3DCQA correlates with existing GPT-4 evaluation scores on the same data. Without this, remove or downplay the benchmark-as-contribution claim.
2. **Explicitly show the 7B vs. 13B comparison** with and without SPA in one focused table to confirm that scaling is restored (13B+SPA > 7B+SPA).
3. **Reframe the method** in the title and abstract — e.g., "contrastive streamlining for 3D MLLMs" — or clarify that "preference" refers to output preference over input degradation, not human preference.
4. **Add implementation details** to the main paper: which parameters are updated, whether masked inputs pass through the full pipeline, and weight initialization.
5. **Fix the phrasing on line 142** ("LLM backbones with less than 7B parameters") to accurately reflect the bottleneck.

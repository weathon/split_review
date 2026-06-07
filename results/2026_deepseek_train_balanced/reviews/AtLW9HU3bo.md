Here is the final consolidated review:

## Summary
This paper proposes E-STR, which extends image-text MLLMs to complex VideoQA by adaptively selecting question-critical (continuous) frames as the "key event" via a differentiable retriever, compressing remaining frames into compact general-context tokens, and inserting lightweight ST-Adapter and MLP-Adapter modules into the frozen image encoder to capture spatial-temporal representations. Evaluated on NExT-QA, Causal-VidQA, and STAR, the method shows improved accuracy over dense concatenation baselines while reducing FLOPs.

## Strengths
- **Differentiable key-event retrieval mechanism (Section 3.2, Table 5):** The paper introduces a fully differentiable pipeline (Gumbel-Softmax + transformation matrix H) for selecting a continuous block of question-critical frames. The ablation shows removing QKR reduces accuracy by -2.1%, directly confirming that the learned selection mechanism contributes meaningfully beyond any fixed-sampling baseline.
- **Favorable accuracy-efficiency Pareto improvement (Table 4):** E-STR achieves 71.7% on NExT-QA vs. 71.1% for Concat-32 (same backbone) while using 38% fewer FLOPs (9,673 vs. 15,616). This quantifies the method's stated goal — selective processing simultaneously improves accuracy and reduces computation.
- **Comprehensive component isolation (Table 5, Figure 4-5):** Each module (QKR, GCE, ST-Adapter) is ablated separately and each contributes positively. The frame-count and window-size ablations (Figures 4-5) show interpretable trends that align with the paper's claims about redundancy and temporal granularity.
- **Generalization across language model backbones (Table 3):** E-STR improves over vanilla concatenation baselines on NExT-QA when combined with Vicuna-7B, Vicuna-13B, and FLAN-T5-XL, demonstrating the method is not tied to a specific LLM.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor
- **Headline SoTA claims are not contextualized with the backbone-controlled comparison (Tables 1, 2 vs. Table 4):** The paper reports "+3.3% over SoTA on NExT-QA" in the abstract, introduction, and conclusion, but the SoTA-comparison tables (1, 2) do not include the same-backbone InstructBLIP baseline (Concat-32). The controlled comparison appears only later in Table 4, where the margin over Concat-32 is +0.6%. The gap between the headline (+3.3%) and the controlled margin (+0.6%) conflates the strength of the underlying MLLM backbone with the proposed method's contribution. The critic's claim that "~80% comes from the backbone" is speculative (prior SoTA methods might not achieve 71.1% on an InstructBLIP backbone), but the presentation nonetheless makes it harder for readers to assess the marginal value of E-STR. The controlled baseline should appear alongside SoTA comparisons.

- **No variance or significance reporting:** All results are reported as single-point estimates with no error bars, confidence intervals, or multiple-run statistics. The controlled improvement over Concat-32 is only 0.6% (71.7% vs. 71.1%). On a multi-choice benchmark, this margin could fall within random variation. Without variance information, the reliability of the core accuracy claim is unclear. (Note: the ablation study partially mitigates this by showing QKR removal causes a larger -2.1% drop, but the central comparison against the main baseline lacks this support.)

- **Spatial-only embeddings used for retrieval without explicit justification (Section 3.1-3.2):** The QKR computes attention using spatial frame embeddings **E**_S (from the frozen vision encoder branch) to select from the spatial-temporal features **V**_ST. The paper does not explain why the retrieval process ignores the temporal information present in **V**_ST. An implicit justification can be inferred — **E**_S remains aligned with the question embeddings **E**_Q because both come from the same contrastively-paired EVA-CLIP encoder — but this reasoning is never stated explicitly, and the design choice is not ablated.

- **Fixed event window size W=5 (Section 3.2, Figure 5):** The window size is set globally to W=5 based on average performance across all questions. Different question types (e.g., descriptive vs. causal) likely require different temporal extents. The paper does not discuss this limitation or explore adaptive window sizing. The fixed W does not invalidate the method (the selection still adapts _where_ the window is placed), but it limits the claimed adaptivity.

### Trivial
- Figure 5 (window-size ablation) would be more informative if it reported results for W=1 and W=2 as well, to show the full trend from single-frame to full-video selection.

## Nice-to-Haves
- A GFLOPs breakdown (vision encoding vs. connection module vs. LLM decoding) would help readers understand where the computational savings originate.
- An analysis of retriever precision (e.g., overlap with human-annotated key moments, if any exist on these datasets) would strengthen the claim that the retriever finds semantically "critical" frames rather than just reducing token count.

## Removed Points
These points were flagged in the reviewer inputs but are removed for the following reasons:
- **"80% of the SoTA gap comes from backbone":** Speculative calculation that assumes prior SoTA methods would achieve exactly the Concat-32 baseline on the InstructBLIP backbone — this is not verifiable from the paper. The factual core (controlled baseline absent from SoTA tables) is retained as a Minor weakness above.
- **"E-STR / E~STR naming inconsistency":** Parser artifact from PDF extraction; not a submission error.
- **"Softmax does not produce one-hot vectors" criticism:** Standard Gumbel-Softmax formulation; the paper's description follows standard practice and the technical imprecision ("obtained the one-hot") does not affect correctness.
- **"Missing analysis of where compute goes":** A nice-to-have, not a weakness.
- **Strength: "Dual-path vision encoder design":** This is a description of the architecture, not a demonstrated strength — the paper does not ablate or compare this design choice against alternatives (e.g., using V_ST for retrieval).

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
1. Include the same-backbone InstructBLIP baseline (Concat-32) in the main SoTA comparison tables (Tables 1 and 2), or explicitly decompose the total improvement into backbone-switch vs. method-specific components.
2. Report results over 3-5 runs with mean and standard deviation for the key comparisons, especially the E-STR vs. Concat-32 margin.
3. Add a brief justification (or ablation) for why spatial-only **E**_S is used for retrieval rather than the spatial-temporal **V**_ST features.
4. Discuss the fixed window-size limitation; consider a simple experiment showing performance broken down by question type (descriptive vs. causal/temporal) for different window sizes.

## Score and Decision
The paper presents a clean, well-motivated method with convincing ablation studies and a genuine efficiency-accuracy improvement. The core concern is that the headline accuracy claims significantly overstate the method's marginal contribution over its own backbone (the controlled margin is +0.6%, not +3.3%), and the lack of variance reporting makes this small margin difficult to assess. The efficiency contribution (38% FLOP reduction) is notable and better supported. For a top venue, the presentation should more honestly separate backbone effects from method effects.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>
## Human Reviewer 1

### Summary
This paper investigates how compression methods including quantization, distillation, and pruning, affect the reasoning abilities of large reasoning models (LRMs).

### Strengths
(1) The paper is clearly written, with a well-structured presentation that is easy to follow.

(2) The motivation is articulated in a clear and convincing manner.

(3) The study provides a comprehensive analysis and offers valuable new insights.

### Weaknesses
(1) The chosen reasoning models are all based on DeepSeek-R1 or its distilled variants, which may constrain the generality of the claims. It is unclear whether the findings would also hold for other reasoning models such as GPT-OSS-20B or GPT-OSS-120B.

(2) The proposed layer-importance locating method is not entirely convincing. For example, Figure 2 suggests that the first-layer weights are relatively unimportant, yet Table 3 shows that quantizing the 1_up component causes the largest performance drop on AIME 2024. This apparent contradiction raises concerns about the reliability of the identified importance scores.

(3) Minor concerns: the tick labels in Figure 2 are not clearly visible, and there is a typo in line 483 (“imrpving” → “improving”).

### Questions
(1) Can the findings in this paper also hold for other reasoning models such as GPT-OSS-20B/120B?

(2) Why quantizing the 1_up component causes the largest performance drop on AIME 2024 but still keeps relatively good performence on other tasks.  

(3) Does the identified important component also depend on the task type/task difficulties?

### Soundness
3

### Presentation
3

### Contribution
2

### Rating
4

### Confidence
3

---

## Human Reviewer 2

### Summary
This paper investigates how compression methods affect large reasoning models (LRMs), specifically focusing on DeepSeek-R1 and its variants. The authors benchmark compressed models on four reasoning datasets and employ mechanistic interpretability techniques (difference of means and attribution patching) to identify which weights are most important for reasoning capabilities. Key findings include: (1) weight count impacts knowledge memorization more than reasoning, (2) the MLP up-projection in the final layer is critically important for distilled LRMs, and (3) current quantization methods overly compress final-layer modules and MLP gate projections.

### Strengths
**Comprehensive scope.** The paper systematically evaluates three major compression paradigms (quantization, distillation, and pruning) on LRMs, addressing a timely and important research gap.

**Easy to read and well-structured.** The paper maintains a clear narrative flow with consistent notation, provides context for key design choices, and connects results to takeaways, which significantly improves readability.

### Weaknesses
**Limited model coverage.**
The analysis centers almost exclusively on DeepSeek-R1 and its distilled variants, which makes several findings read as DeepSeek-specific behaviors rather than properties of compression that generalize across LRMs. Validating the conclusions on additional open-sourced LRM families (e.g., QwQ variants) would strengthen the generalizability claims and help disentangle model-specific effects from compression-induced phenomena.

**Imbalanced treatment across compression methods.**
The paper allocates uneven coverage across the three compression families. Distillation is represented by off-the-shelf distilled checkpoints for black-box open-source models, quantization is explored with four distinct methods, while pruning is evaluated only with SparseGPT. This asymmetry makes the comparisons look method-specific rather than family-level and may hurt perceived fairness.

**Coarse knowledge vs. reasoning disentanglement.**
The paper infers that parameter count chiefly affects knowledge based largely on lower MuSiQue EM/F1 compared to other tasks. However, this single contrast is not sufficient to attribute effects to knowledge retention versus reasoning capability. MuSiQue itself blends multi-hop reasoning with retrieval-like knowledge and is sensitive to prompt/context choices. As a result, the “parameter count affects knowledge” conclusion feels somewhat overstated. More fine-grained experiments would strengthen the claim, e.g., RAG vs. closed-book ablations across model sizes or other synthetic tasks that decouple reasoning from memorized facts.

**Minor presentation issues.** There’s a typo (“imrpving”) in Section 6.

### Questions
See weaknesses above.

### Soundness
3

### Presentation
4

### Contribution
2

### Rating
4

### Confidence
3

---

## Human Reviewer 3

### Summary
This paper systematically studies the effective of different model compression strategies on the reasoning capability of LRM, by applying reasoning-diagnosis metrics such as the steering vectors. From extensive empirical studies the authors propose certain properties and locate certain modules in LRM that are most critical to reasoning, providing insights into future designs on compression methods.

After reading the paper, I am under the impression that the paper has meaningful motivation, supported by well-designed empirical studies with strong results, and the claims are well-presented. However, the paper 

1. Lacks methodological novelty and diversity in the analytical framework, using only one previously-proposed metrics. Some of the main claims of the paper, such as the localization of critical modules.
2. Could be further supported by more rigorous controlled study and evaluation metrics. 

Therefore I recommend weak reject, but with room for further improvement after obtaining more insights from the authors during discussions.

### Strengths
1. The motivation of the paper is meaningful, as the authors focus on the effect of compression methods to (hard) reasoning tasks, which is both critical and not well-studied.
2. From comprehensive experiments the authors provides valuable insights on the design of compression methods on LRMs, that is to pay attention to certain modules important to reasoning.

### Weaknesses
1. The paper makes, in my opinion, a quite strong claim on localizing the reasoning ability to certain model layers. The claim that later layer is more critical to reasoning/performances is intuitive, as they have greater impact on the final output, and could be sensitive to perturbations/compressions. However the authors do not go deeper into why certain deep layers are important to reasoning. 
2. For a systematic study, the authors should consider using a more diverse set of diagnosing tools, rather than only using one framework, as it would put the general applicability of the main claim under question.
3. In the paper, the locating of tokens related to certain reasoning behaviors seems not rigorous enough, as the authors only use GPT-4o to identify related tokens, which itself may have certain biases.
4. Some missing discussions on the layer/module-wise compression methods [1, 2], and identifying weights important to reasoning [3]

[1] Using Heavy-Tailed Self Regularization Theory for Improved Layer-wise Pruning of Large Language Models, https://arxiv.org/abs/2410.10912

[2] Outlier Weighed Layerwise Sparsity (OWL): A Missing Secret Sauce for Pruning LLMs to High Sparsity, https://arxiv.org/abs/2310.05175

[3] Principal Weights Emerge after Rank Reduction for Reasoning-Focused Supervised Fine-Tuning, https://arxiv.org/abs/2506.00772

### Questions
1. Could the authors add more discussions on recent works [1] on the principal weights of model weights that are related to reasoning performances. 
2. Since the choosing of tokens related to reasoning behaviors may be critical in the determination of reasoning-related modules, I wonder whether the authors have tried using other models (other than GPT-4o) to determine the tokens. In those cases, would the overall claims still hold? If so, it will strengthen the robustness of the findings.
3. The authors proposes that certain layers/modules are more important in reasoning process, which relates to the discussion on the imbalanced quality among layers/modules. Do the authors believe that module-specific compression methods could potentially address the problem of over-compressing the important layers? There are recent works discussing module-wise compression [1, 2]
4. For empirical evidence of layer importance (Takeaway 4.1 & 4.3, Fig. 2 & 3, etc.) it would be more intuitive if the authors could present the $I_{ml}^c$ metric for the base model (before distillation) to give the reader a better idea on how the importance of each module changes, rather than only presenting the $RI_{ml}^c$.

[1] Using Heavy-Tailed Self Regularization Theory for Improved Layer-wise Pruning of Large Language Models, https://arxiv.org/abs/2410.10912

[2] Outlier Weighed Layerwise Sparsity (OWL): A Missing Secret Sauce for Pruning LLMs to High Sparsity, https://arxiv.org/abs/2310.05175

[3] Principal Weights Emerge after Rank Reduction for Reasoning-Focused Supervised Fine-Tuning, https://arxiv.org/abs/2506.00772

### Soundness
3

### Presentation
3

### Contribution
3

### Rating
4

### Confidence
3

---

## Human Reviewer 4

### Summary
This paper presents a two-fold analysis of the effects of compression on Large Reasoning Models (LRMs), using DeepSeek-R1 as its primary case study. First, it provides a comprehensive benchmark of three major compression families—quantization, distillation, and pruning—evaluating their impact on performance across a diverse set of reasoning datasets (AIME 2024, FOLIO, Temporal Sequences, and MuSiQue). Second, and more notably, the paper employs mechanistic interpretability techniques (adapting difference of means and attribution patching) to identify which specific model components are causally important for reasoning. The authors find that current compression methods, particularly quantization, disproportionately harm these critical components. They validate this finding by showing that selectively protecting these components (e.g., the final-layer MLP) during quantization significantly recovers lost performance.

### Strengths
Novelty of Interpretation: The paper's primary strength is its application of mechanistic interpretability to the problem of model compression. It moves beyond standard "accuracy vs. bits/size" tables to provide a causal analysis of why and where performance degrades, which is a valuable contribution.

Actionable Findings: The analysis yields clear, actionable insights. The identification of the final-layer mlp.up_proj as a critical component for reasoning (in R1-distilled models) and the finding that popular quantization methods (AWQ, GPTQ) overly compress these final layers are important discoveries.

Strong Validation: The experiment in Section 5.2 is compelling. Demonstrating that protecting just 2% of weights (the final-layer MLPs) from quantization can recover 6.57% in average accuracy on a 3-bit model provides strong validation for the paper's entire interpretability pipeline.

### Weaknesses
Generalizability: The analysis is heavily centered on DeepSeek-R1 and its specific distilled variants (R1-Distill-Llama, R1-Distill-Qwen). It is unclear if the central findings (e.g., the high importance of the final-layer mlp.up_proj) are a general feature of all LRMs or an artifact of the specific distillation-with-SFT process used to create the R1 models.

Subjectivity in Methodology: The interpretability analysis (Section 2.2) relies on prompting GPT-4o to locate token sequences corresponding to four specific reasoning behaviors. This labeling process seems subjective and could introduce noise or bias. The robustness of the resulting steering vectors is highly dependent on the quality of this heuristic.

Underdeveloped Pruning Analysis: While pruning is introduced as one of the three main compression methods, it is quickly dismissed after benchmarking shows it performs poorly (e.t., at 50% sparsity). The subsequent mechanistic analysis focuses almost exclusively on distillation and quantization, making the pruning aspect of the paper feel incomplete.

### Questions
1. Can the authors comment on whether the "final-layer importance" finding is specific to the R1-distillation process? Have you tried applying your interpretability analysis to a standard, non-distilled model (e.g., base Llama 3) that has been fine-tuned for reasoning? Would you expect to see the same components identified as critical?

2. Could you elaborate on the validation process for the GPT-4o labeling of reasoning behaviors? How sensitive are the final importance scores (and the resulting conclusions) to potential inaccuracies or inconsistencies in this automated labeling process?

3. The paper notes (Takeaway 3.3) that pruning/distillation (reducing parameter count) hurts knowledge memorization (MuSiQue) more severely than reasoning (AIME, FOLIO). Quantization (reducing precision) seems to have a less detrimental effect on knowledge. Could you expand on this distinction? Why do you hypothesize that parametric knowledge is so much more sensitive to parameter count than to parameter precision?

I would like to improve my scores if authors can solve my questions.

### Soundness
3

### Presentation
3

### Contribution
2

### Rating
4

### Confidence
4

---

## Human Reviewer 5

### Summary
This paper studies how compression (quantization, distillation, pruning) impacts reasoning in LRMs (DeepSeek-R1 and distilled Llama/Qwen) via (i) a broad benchmark on AIME-2024, FOLIO, Temporal Sequences, and MuSiQue, and (ii) mechanistic analyses that compute behavior-specific importance for every linear module using difference-of-means and attribution-patching. Key claims include: 2.51-bit dynamic quantization of R1 attains near-R1 performance; the final-layer MLP up-projection is consistently most reasoning-critical; and protecting ~2% of weights (final-layer MLPs) recovers +6.57% average accuracy for 3-bit AWQ.

### Strengths
1、 Comprehensive scope across three compression families with clear head-to-head tables and multiple distilled sizes (70B/32B/8B/7B).

2、Fine-grained mechanistic lens (module-level DoM + attribution-patching) tied to four reasoning behaviors (backtracking, uncertainty estimation, example testing, adding knowledge).

3、 Actionable insight: the final-layer up-projection is most critical; selectively quantizing it alone (≈0.7% of weights) causes a large drop, while protecting final-layer MLPs at 16-bit raises a 3-bit model by +6.57% on average.

4、 Useful observations on collapse points (e.g., pruning ≥50% collapses; 3-bit baselines stress on harder tasks) and knowledge vs. reasoning separation (MuSiQue).

### Weaknesses
1、Robustness & Statistics. Behavior labeling robustness is under-specified (prompt/threshold/seed); key results lack rank-stability and uncertainty (variance, 95% CIs, significance).

2、Metric & Visualization Choice. RI plots zero out increases, risking masked compensations; provide justified alternatives (report both ↑/↓ and net change).

3、Coverage & Generalization. Pruning analysis is shallow (no mechanistic view beyond collapse); external validity is limited (mainly R1-distilled 8B/7B, few non-R1 families).

### Questions
1) Behavior-label robustness.
Vary the behavior taxonomy/prompt/thresholds and report rank stability (Kendall’s τ / Spearman ρ) with 95% CIs; include a leave-one-behavior-out analysis.
2) RI visualization choice.
Justify zeroing positive RI deltas and provide an alternative view that reports both increases and decreases, plus a net-change summary.
3) Selective protection trade-offs. Provide an accuracy vs. protected-ratio (0.5–5%) curve and the latency/memory overhead; compare protecting final-layer gate vs. up vs. both.
4) 2.51-bit dynamic quantization details.
Specify the skip policy (which layers stay high-precision), calibration set, and per-module bit-allocation histograms; compare to AWQ/GPTQ under identical calibration on quantization error, attribution-preservation, and end-task metrics.

### Soundness
4

### Presentation
3

### Contribution
3

### Rating
6

### Confidence
4
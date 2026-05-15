Now I have a thorough understanding of the paper. Let me write the consolidated review.

## Summary

This paper tackles Object Concept Learning (OCL)—recognizing attributes and affordances of objects—by proposing Hierarchical Multi-Grained Reasoning (HGR). The method has two main components: (1) a coarse-to-fine hierarchical reasoning module that uses learnable prompts to progressively localize concept-relevant visual information (global context → instance-specific), and (2) a counterfactual relation-enhancing module that leverages causality annotations and a graph network to strengthen attribute–affordance connections. Experiments on the OCL benchmark claim 8.1% and 3.9% mAP improvements over prior SOTA, with additional evaluations on NYUd2 and AGD20K.

## Strengths

1. **Well-motivated coarse-to-fine prompting design**: The paper identifies a genuine difficulty in OCL (many-to-many mapping) and proposes a structured two-step prompting pipeline (category-agnostic global context → instance-specific fine-grained) that mirrors human coarse-to-fine perception. This is validated by attention heatmaps (Figure 3) showing progressive localization, and by ablation (Table 5) where the full two-step hierarchy outperforms global-only or instance-only prompts, confirming that both stages are needed.

2. **Counterfactual relation-enhancing module is novel and ablated**: The idea of using causality annotations to construct a graph-based counterfactual loss for strengthening attribute–affordance connections is a conceptual advance over purely discriminative methods (e.g., Li et al., 2023b). Table 4 shows that adding the CCC module on top of the coarse-to-fine reasoning and visual concept extraction yields clear improvements (e.g., attribute mAP from 47.9% to 50.5%), providing evidence that each design choice contributes.

3. **Consistent empirical gains on the primary benchmark**: On the main OCL benchmark (Table 1), the method improves attribute mAP by 8.1% and affordance mAP by 3.9% over the previous SOTA (Li et al., 2023b). These are non-trivial margins on a task with 114 attributes and 170 affordances.

4. **Systematic ablation analysis**: Table 4 decomposes the method into three high-level modules (CHR, PVCE, CCC) and shows each contributes cumulatively. Figure 4 provides a sensitivity analysis on the number of concepts k, showing peak performance at k=10 and degradation at mismatched values, offering practical insight into the method's behavior.

## Weaknesses

### Fatal
None.

### Major

1. **Missing clarity on whether baselines use the same supervision signals (bounding boxes + causality annotations)**. The method uses ground-truth bounding boxes (Section 3.1.2: "we employ ground-truth bounding boxes to crop the objects") for fine-grained prompt formation, and causality annotations from the benchmark for the counterfactual loss (Section 3.2.2). The paper never states whether the primary baselines (e.g., OCRN from Li et al., 2023b) also have access to or use these signals. If they do not, the reported gains (8.1% attribute, 3.9% affordance) could partly reflect additional supervision rather than the hierarchical reasoning mechanism itself. The ablation (Table 4) does not isolate this factor—the CHR module itself includes bounding-box-based fine-grained prompts, so even the base improvement over vanilla CLIP conflates spatial supervision with the reasoning design. **Why this matters**: Without controlling for this, the core claim that the reasoning mechanism drives improvements is not robustly supported.

2. **Invalid or underspecified NYUd2 comparison**. The paper compares HGR against PSPNet, FastFCN, DeepLab V3, VarReg, and Cerberus on NYUd2 for attribute/affordance prediction (Table 2). These methods are designed for semantic segmentation, not attribute/affordance recognition. The paper provides no description of how they were adapted for this task, what evaluation protocol was used, or whether they receive the same supervision. Without this, the comparison on NYUd2 is uninterpretable and should be either properly specified or removed. **Why this matters**: It undermines the claim of cross-dataset generalizability and erodes confidence in the experimental rigor.

3. **Counterfactual loss is incompletely specified**. The loss is given as \(L_{cl} = \max\{0, \gamma - (\hat{y}_\beta - \hat{y}_{\beta mask})\}\) only for the case \(\beta_i = 1\). The paper states "We design two loss function \(L_{cl}\) according to the different affordance label to promise the \(L_{cl}\) should be a positive value" (line 137) but never provides the second formulation for \(\beta_i = 0\). This is not a minor omission—the loss function, which the paper emphasizes as a core contribution, cannot be implemented or reproduced as described. **Why this matters**: This is a basic reproducibility failure for a claimed methodological contribution.

### Minor

1. **Causality annotation usage not fully isolated**. While the CCC module's contribution is shown in Table 4, the module combines both the graph connection network and the counterfactual loss (which uses causality annotations). The paper does not ablate these separately, so it is unclear whether the benefit comes from the graph structure, the counterfactual supervision, or both. An ablation comparing "graph only" vs. "graph + counterfactual loss" would clarify this.

2. **"model cannot align" claim (Table 5 discussion) is not fully justified**. The paper claims the two-step prompt outperforms one-step methods because "the model cannot align the attribute and affordance prompts with image features solely from local regions." However, the gap between one-step and two-step could also be due to increased model capacity, more training iterations, or simply having two forward passes instead of one. The causal attribution to "cannot align from local regions" is an interpretation, not proven by the experimental design.

3. **Number-of-concepts analysis (Figure 4)** shows peak at k=10, but no justification is given for why 10 is the chosen value for main experiments or whether this choice was determined on the validation set. If k=10 was selected based on validation performance, this should be explicitly stated to avoid overfitting concerns.

4. **Train/val/test splits and evaluation protocols** are not reported. The paper says it "follows the OCL" protocol (line 179) but does not reproduce the split information. For a new method, this should be self-contained or at least summarized.

5. **Unclear what "HMa (Rumelhart et al., 1986)" refers to**. The citation Rumelhart 1986 is the PDP book (neural network foundations), but "HMa" is not a standard acronym. This makes it difficult for readers to understand what this baseline is.

### Trivial
None.

## Nice-to-Haves
- Reporting mean and variance over multiple seeds would strengthen confidence in the results, though single-run evaluation is common in vision benchmarks at this scale.
- Runtime comparisons between HGR and baselines would be useful since the hierarchical cascade and GRU updates add complexity beyond a single CLIP forward pass.
- Visualizing the learned adjacency matrix **A** to show whether it captures known causal relationships between attributes and affordances would strengthen the qualitative validation.

## Removed Points
- **"Related work section is cut off"**: This is a PDF parsing artifact, not an author error. The original submission does not have this issue.
- **"HMa is likely a typo"**: This is a minor naming/formulation issue. While "HMa" is not a standard acronym, this does not affect the paper's scientific validity.
- **"Contribution 1 is from Li et al. 2023b"**: The paper frames OCL as many-to-many mapping and cites Li et al. (2023b). The contribution is about proposing a reasoning method, not the framing itself. This criticism overstates the issue.
- **"No evidence that prompts diverge from category semantics"**: The paper's claim about CLIP focusing on categorical semantics is a standard observation in the prompt tuning literature. Demanding additional proof beyond the task-appropriate design is scope creep.
- **"Increased capacity argument for Table 5"**: While the critic's alternative explanation is possible, the two-step design is a self-contained architectural choice, and the paper provides qualitative evidence (Figure 3 heatmaps) supporting its interpretation. This criticism is speculative rather than substantive.
- Generic formatting/style nitpicks and grammar complaints.

## Novel Insights
The reviews collectively surface an important tension: the paper makes a genuinely novel architectural proposal (hierarchical coarse-to-fine prompting with counterfactual graph reasoning for OCL), but the experimental evaluation lacks the controlled comparisons needed to separate the contribution of the reasoning mechanism from the contribution of additional supervision signals (bounding boxes, causality annotations). This is a recurring pattern in vision-language papers that leverage pre-trained models like CLIP—the rich feature space makes it easy to achieve good results with multiple design choices, but hard to prove that a specific mechanism (rather than the combination of available priors) is responsible for the gains. The paper would significantly benefit from an ablation that strips away the extra supervision and tests whether the hierarchical prompting alone (without any bounding-box crops or causality labels) still outperforms baselines under equal conditions.

## Suggestions
1. **Run a controlled ablation without bounding boxes**: Evaluate HGR using only the coarse-grained prompts (global image only) to establish a baseline that does not use ground-truth bounding boxes. Then add fine-grained prompts using predicted boxes (from a standard detector) rather than ground-truth boxes to isolate the value of the hierarchical reasoning from the value of perfect spatial supervision.
2. **Specify the second counterfactual loss function completely**: Provide the full formula for \(L_{cl}\) when \(\beta_i=0\) so the method can be reproduced.
3. **Clarify the NYUd2 evaluation**: Either describe exactly how segmentation baselines were adapted for attribute/affordance prediction, or remove the comparison and focus on the well-specified OCL and AGD20K benchmarks.
4. **Ablate CCC components separately**: Show the contribution of the graph connection network alone vs. graph + counterfactual loss to isolate the effect of the causality annotations.
5. **State the dataset split and evaluation protocol explicitly** in the paper rather than relying on a citation.

## Score and Decision

**Assessment across axes**: The paper addresses an important and relatively new problem (OCL) with a creative approach that combines hierarchical prompting with counterfactual reasoning. The originality is moderate—prompt tuning and causal graphs individually are established techniques, but their synthesis for OCL is novel. The writing is generally clear. The main claims (SOTA results) are supported by numbers but the experimental design has meaningful gaps that prevent a clean attribution of the improvement to the proposed reasoning mechanism. The value to the community is real—the method and analysis (especially the concept count sensitivity) offer useful insights—but the reproducibility gaps and experimental confounds limit immediate impact.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>
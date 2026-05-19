## Summary
# Final Review Report

## Summary

This paper presents CoPrompt (Consistency-guided Prompt Learning), a fine-tuning method for vision-language models (CLIP) that addresses the overfitting problem in few-shot learning. The core idea is a cosine-distance consistency constraint that keeps the trainable model's embeddings close to the frozen pre-trained CLIP embeddings, preventing catastrophic forgetting of zero-shot capabilities. Three components work together: (1) consistency constraint on both image and text branches, (2) input perturbations (LLM-generated descriptive text and image augmentations) applied within the consistency loss, and (3) integration of multi-modal prompting with adapters. Experiments on 11 datasets show CoPrompt achieves 80.48% harmonic mean on base-to-novel generalization, improving over MaPLe by 1.93% and PromptSRC by 0.51%, and 67.0% on cross-dataset evaluation.

**Core contributions (C1-C3):**
- **C1**: Consistency-enforced fine-tuning that prevents overfitting and preserves zero-shot generalizability.
- **C2**: Use of LLM-generated text descriptions and image augmentations as perturbed inputs for stronger consistency regularization.
- **C3**: Combined prompting + adapter framework under a single consistency constraint, enabling more tunable parameters without overfitting.

The paper is technically sound, well-evaluated across multiple standard benchmarks, and the ablation study is thorough. However, several issues reduce confidence: (1) domain generalization results actually underperform prior SOTA (contradicting the abstract), (2) the 0.51% HM gain over PromptSRC lacks statistical significance analysis, (3) adapter architecture details are insufficient for reproduction, and (4) the conclusion lacks limitations discussion. Novelty claims cannot be fully verified without external literature retrieval (Retrieval-Disabled Mode active in this run).

## Strengths
1. **Clear Problem Formulation**: The paper identifies a well-defined problem—catastrophic forgetting of zero-shot capabilities during few-shot fine-tuning of VLMs—and proposes a principled solution (consistency constraint) that directly addresses the identified failure mode (embedding deviation).

2. **Comprehensive Evaluation**: Experiments cover three standard evaluation protocols (base-to-novel generalization, cross-dataset evaluation, and domain generalization) across 11 diverse datasets, following established benchmarks from CoOp/CoCoOp/MaPLe. This makes results directly comparable with prior work.

3. **Thorough Ablation Study**: The paper systematically ablates each component (consistency, input perturbations, adapters) and explores design alternatives (cosine vs MSE vs L1, GPT-2 vs GPT-3, simple vs hard augmentations, adapter placement, prompt layer depth). Table 4 and Table 5 provide a clear picture of each component's contribution.

4. **Practical Efficiency Focus**: The paper reports parameter counts (only 0.26M for adapters, 4.74M total learnable), training time overhead (~25% over MaPLe), and demonstrates that CoPrompt still outperforms MaPLe under a matched compute budget (80.01% vs 78.55% with equal training time). Inference costs are identical to MaPLe.

5. **Reproducibility Infrastructure**: Code is open-sourced on GitHub, training details are provided (SGD optimizer, 8 epochs, batch size 4, LR 0.035, 16-shot, 3 runs), and the appendix includes cross-backbone validation (EVA-CLIP).

6. **Conceptual Novelty of Consistency Mechanism**: The consistency constraint between a learnable and a frozen encoder (rather than two learnable encoders as in self-supervised learning) is a well-motivated design choice. The integration of LLM-generated descriptions as perturbed text inputs is a creative extension beyond prior perturbation-based regularization.

## Weaknesses
1. **Abstract Overclaim (Major)**: The abstract states CoPrompt "outperforms existing methods on a range of evaluation suites, including base-to-novel generalization, domain generalization, and cross-dataset evaluation." However, Table 3 shows CoPrompt (60.42%) performs below both Bayesian Prompt (60.44%) and PromptSRC (60.65%) on domain generalization. This is a factual error in the abstract that must be corrected.

2. **Missing Statistical Significance (Major)**: Key results (0.51% HM improvement over PromptSRC) are reported without confidence intervals or significance tests. The paper reports averaging over 3 runs (Appendix A.1.1) but no standard deviations appear in Table 1 or Table 2. With only 3 runs and small margins, the claimed improvements may not be statistically reliable.

3. **Insufficient Adapter Specification (Major)**: The adapter design is described only as "two linear layers with non-linearity in between" without specifying: hidden dimension ratio, nonlinearity type (ReLU/GELU), presence/absence of residual connection, residual mixing ratio α, or insertion position (post-encoder vs per-layer). This is insufficient for reproduction.

4. **Uncontrolled Ablation Comparison (Minor)**: Table 11 compares "MaPLe (12-layer prompt) + Adapter" at 77.61% against MaPLe's optimal 78.55% (9-layer prompt), but the 12-layer baseline is known to underperform even without adapters. The controlled experiment should use MaPLe's optimal 9-layer configuration with and without adapters.

5. **Missing Limitations Section**: The conclusion is only 4 sentences and does not acknowledge any limitations (domain generalization gap, λ sensitivity, hard augmentation degradation, potential failure cases). This reduces scientific completeness.

6. **Related Work as Sequential List (Minor)**: The related work section reads as a chronological list of methods rather than an analytical comparison organized by design axes (prompt modality, regularization approach, parameter efficiency). The differentiation from PromptSRC is mentioned briefly but could be clearer.

7. **Domain Generalization Not Analyzed (Minor)**: CoPrompt underperforms on domain generalization, but the paper provides no analysis of why—whether the adapters learn source-specific biases, or whether the consistency constraint is less effective under distribution shift. This is a missed insight opportunity.

8. **FLOPs Reporting Ambiguity (Minor)**: The claim "2x FLOPs" is not clearly defined (2x of what baseline? Per-step or total?) and actual FLOP numbers are not reported. Training time (+25%) is reported for only one dataset (Flowers102).

9. **Conclusion Reads as Abstract Repetition (Minor)**: The conclusion restates the method without synthesized insights, bounded limitations, or future research directions, reducing its value as a scientific closing section.

10. **Novelty Context Unverifiable (Deferred)**: Due to Retrieval-Disabled Mode, novelty claims (C1-C3) cannot be verified against external literature. This review marks novelty/comparison conclusions as deferred for manual verification.

## Key Issues
### Issue 1: Abstract/Claim-Evidence Mismatch on Domain Generalization
**Severity: Major | Validity Risk: High | Fixability: Easy**

The abstract claims CoPrompt "outperforms existing methods on... domain generalization," but Table 3 shows CoPrompt (60.42%) ranks below Bayesian Prompt (60.44%) and PromptSRC (60.65%). This is a direct factual contradiction. The paper's own contribution list (item 4) also claims "state-of-the-art for a range of evaluation suites" without excluding domain generalization. This overclaim reduces trust in the paper's objectivity.

**Root Cause**: The authors likely wrote the abstract to reflect the positive results on base-to-novel and cross-dataset evaluations, then added "domain generalization" as a blanket category without checking the numerical outcome.

**Fix**: Remove "domain generalization" from the list of outperformed evaluation suites in the abstract, introduction, and conclusion. Alternatively, rephrase to "competitive performance on domain generalization benchmarks."

---

### Issue 2: Missing Statistical Significance for Core Results
**Severity: Major | Validity Risk: High | Fixability: Medium**

The core claim—CoPrompt outperforms PromptSRC by 0.51% HM—is reported without confidence intervals, standard deviations, or significance tests. The paper states "average accuracy over 3 runs" in Appendix A.1.1 but Table 1 contains no variance information. With only 3 seeds and a margin of 0.51%, the improvement may not be statistically significant (a paired test across 11 datasets would clarify this).

**Root Cause**: Standard practice in the prompt-tuning literature (CoOp, CoCoOp, MaPLe) has not emphasized statistical testing, but as the field matures, significance reporting becomes necessary to distinguish genuine improvements from noise.

**Fix**: Report mean±std over 3 runs for all entries in Table 1 and Table 2. Add a paired Wilcoxon signed-rank test or bootstrap test comparing CoPrompt vs PromptSRC across 11 datasets. If p > 0.05, downgrade the claim to "competitive performance."

---

### Issue 3: Insufficient Adapter Architecture Details
**Severity: Major | Reproducibility Risk: High | Fixability: Easy**

The adapter is described as "two linear layers with non-linearity in between" without specifying: bottleneck dimension, nonlinearity type, residual connection structure, mixing ratio α, or position in the network. CLIP-Adapter (Gao et al., 2023) uses a specific architecture (bottleneck ratio 16, ReLU, residual with α=0.2), but CoPrompt does not confirm whether it adopts the same design. Without these details, the method cannot be reproduced.

**Root Cause**: The paper focuses on the consistency mechanism and treats adapters as a known component, but the specific design choices matter for the overfitting claim.

**Fix**: Add 2-3 sentences specifying the full adapter architecture, including: bottleneck dimension (e.g., d/16), activation function (ReLU), presence of residual connection (yes, with α=0.2), and position (post-encoder, on both text and image branches). These can be in Section 3.2 or the Appendix.

---

### Issue 4: Non-Trivial Claim About Prompt+Adapter Combination Has Weak Evidence
**Severity: Major | Validity Risk: Medium | Fixability: Medium**

The paper claims "prior works have not been able to successfully combine [prompts and adapters]" and attributes this to overfitting. The evidence (Table 11) compares "MaPLe (12-layer prompt) + Adapter" (77.61%) against MaPLe optimal (78.55%). However, the 12-layer prompt configuration is suboptimal even without adapters (MaPLe's optimal is 9 layers). The controlled comparison should be MaPLe (9-layer) vs MaPLe (9-layer) + Adapter to isolate the adapter effect.

**Root Cause**: The ablation was likely run with the 12-layer prompt to match the CoPrompt configuration, but this introduces a confound.

**Fix**: Add the controlled experiment: MaPLe (9-layer, 78.55%) vs MaPLe (9-layer) + Adapter w/o consistency. Report the HM in Table 11. If the drop persists, the claim is well-supported. If not, revise the claim.

---

### Issue 5: Missing Limitations and Weak Conclusion
**Severity: Minor | Scientific Completeness Risk: Medium | Fixability: Easy**

The conclusion is only 4 sentences, repeating the abstract without acknowledging limitations, negative results, or future work. Key missing elements: (1) domain generalization gap not discussed, (2) λ sensitivity not mentioned, (3) hard augmentation degradation not acknowledged, (4) no concrete future directions.

**Fix**: Expand to a 3-paragraph conclusion: validated findings with specific numbers, explicit limitations, and 2-3 concrete future research directions.

## Actionable Suggestions
### Suggestion 1: Correct the Abstract and Contribution Statements (Must)
- **Evidence**: Abstract claims outperformance on "domain generalization"; Table 3 contradicts this.
- **Action**: Remove "domain generalization" from the abstract's outperformance list. Change contribution (4) from "new state-of-the-art for a range of evaluation suites" to "new state-of-the-art on base-to-novel generalization and cross-dataset recognition."
- **Location**: Page 1 Abstract (lines 22-24), Page 2 Contribution list (lines 48-49).

### Suggestion 2: Add Variance Reporting and Significance Tests (Must)
- **Evidence**: Table 1-2 show no std/CI despite 3-run averaging.
- **Action**: Report mean±std for all entries in Table 1 and Table 2. Add a paired Wilcoxon signed-rank test (CoPrompt vs PromptSRC across 11 datasets) in the text. If p>0.05, soften the superiority claim.
- **Location**: Page 6-7, Table 1 and Table 2, plus the analysis paragraphs.

### Suggestion 3: Specify Adapter Architecture in Full (Must)
- **Evidence**: Section 3.2 Adapters paragraph — "two linear layers with non-linearity in between" is underspecified.
- **Action**: Add: "Following CLIP-Adapter, our adapter uses a bottleneck ratio of 16× reduction, a ReLU activation between down/up projections, and a residual connection with mixing ratio α=0.2: φ_a(w) = α·Up(ReLU(Down(w))) + (1-α)·w. The adapter is placed after the final encoder layer on each branch."
- **Location**: Page 5, Section 3.2 Adapters.

### Suggestion 4: Perform Controlled Adapter Ablation (Must)
- **Evidence**: Table 11 uses MaPLe (12-layer) + Adapter vs MaPLe optimal (9-layer).
- **Action**: Add a row: "MaPLe (9-layer) + Adapter w/o consistency" to Table 11. Run with 9 prompt layers (MaPLe's optimum) + adapters (no consistency). Report HM.
- **Location**: Appendix A.4, Table 11.

### Suggestion 5: Expand Conclusion with Limitations (Must)
- **Evidence**: Page 9, Conclusion is 4 sentences without limitations.
- **Action**: Add a 3-paragraph conclusion covering: (1) validated findings with specific numbers (80.48% HM, 67.0% cross-dataset), (2) limitations (domain generalization gap, λ sensitivity, hard augmentation degradation), (3) future work (adaptive λ, stronger domain regularization, scaling to larger backbones).
- **Location**: Page 9, Section 5.

### Suggestion 6: Improve Related Work Organization (Nice-to-have)
- **Evidence**: Section 2 is a chronological list.
- **Action**: Reorganize by design axes: (a) prompt modality (text-only vs multi-modal), (b) regularization strategy (none, gradient-aligned, self-regulation, consistency), (c) parameter efficiency (prompts only vs prompts+adapters). End each subsection with CoPrompt's positioning.
- **Location**: Pages 2-3, Section 2.

### Suggestion 7: Add Domain Generalization Analysis (Nice-to-have)
- **Evidence**: Section 4.4 reports results without analysis of why CoPrompt underperforms.
- **Action**: Add 1-2 sentences: "The slight underperformance on domain generalization may stem from the adapters learning source-specific biases. Future work could explore domain-adaptive regularization or adversarial feature alignment."
- **Location**: Page 7, Section 4.4.

### Suggestion 8: Clarify FLOPs and Report Peak Memory (Nice-to-have)
- **Evidence**: Section 4.6 mentions "2x FLOPs" without precise definition.
- **Action**: Report total GFLOPs per training step for CoPrompt vs MaPLe. Add peak GPU memory under equal batch size. Clarify that "2x" refers only to the additional frozen forward pass.
- **Location**: Page 9, Section 4.6.

### Suggestion 9: Improve Introduction Narrative (Nice-to-have)
- **Evidence**: Page 1, Introduction paragraph 1 begins without a clear gap statement.
- **Action**: Restructure as: (a) VLM generalization value, (b) fine-tuning challenge: zero-shot degradation, (c) existing methods (prompts, adapters) only partially solve this, (d) CoPrompt's consistency approach as the missing solution.
- **Location**: Page 1, Section 1 Introduction.

## Storyline Options + Writing Outlines
### Current Storyline Analysis

The current introduction follows this flow:
1. Paragraph 1: VLM generalization + fine-tuning challenge (compressed survey-style).
2. Paragraph 2: CoPrompt method description + three components.
3. Paragraph 3: Results preview (base-to-novel, cross-dataset) + contribution list.

**Weakness**: The introduction lacks a clear Big Picture → Gap → Solution → Evidence arc. The gap (overfitting causing zero-shot degradation) is mentioned in paragraph 2 rather than being established as the central problem in paragraph 1. The solution paragraphs mix method description with results, making the contribution less memorable.

### Recommended Storyline: Problem-Motivation-Solution-Evidence (P-M-S-E)

**Abstract Outline (4-5 sentences)**:
- S1 (Problem): Fine-tuning large vision-language models on few-shot downstream tasks causes catastrophic forgetting of their zero-shot generalization capability.
- S2 (Gap): Existing parameter-efficient methods (prompt tuning, adapters) still overfit on limited data, causing the model's representations to deviate from pre-trained features.
- S3 (Solution): We propose CoPrompt, which enforces a cosine-distance consistency constraint between trainable and frozen encoder outputs, combined with input perturbations (LLM-generated text, image augmentations) and a unified prompt+adapter framework.
- S4 (Results): On 11 benchmarks, CoPrompt achieves 80.48% harmonic mean on base-to-novel generalization (1.93% over MaPLe) and 67.0% on cross-dataset evaluation.
- S5 (Scope): Ablation studies confirm each component contributes to the gains. Code is available.

**Introduction Outline (4 paragraphs)**:

**P1 — The Fine-Tuning Generalization Problem** (Big Picture + Gap)
- Role: Establish why fine-tuning VLMs on few-shot data is valuable yet problematic.
- Key claim: Standard fine-tuning and even parameter-efficient methods degrade zero-shot capabilities.
- Evidence: Cite CoOp's observed zero-shot drop. State the root cause: overfitting causes embedding deviation from the pre-trained encoder.
- Transition: "To address this, we propose..."

**P2 — CoPrompt: Consistency as a Regularizer** (Solution intuition)
- Role: Explain the core idea before technical details.
- Key claim: A consistency constraint between learnable and frozen encoders prevents representation drift.
- Key design choices: (a) cosine distance rather than MSE, (b) perturbed inputs (LLM descriptions + augmentations) for stronger regularization, (c) unified prompt+adapter framework enabled by the constraint.
- Transition: "We now detail each component..."

**P3 — Technical Overview** (Architecture + Loss)
- Role: Brief technical bridge to Method section.
- Key equations/concepts: Multi-modal prompts, adapters, consistency loss L_cc, final loss L = L_ce + λL_cc.
- No need for full derivations here; those belong in Section 3.
- Transition: "We evaluate CoPrompt on three standard settings..."

**P4 — Results Preview + Contributions** (Evidence + Contribution)
- Role: Summarize key outcomes and contributions.
- Key claims: (1) 80.48% HM, outperforming on 8/11 datasets, (2) 67.0% cross-dataset, (3) competitive domain generalization.
- Contributions (3 items, no performance-only claims).
- Transition: "We first review related work before presenting the method."

### Alternative Storyline: Challenge-Response (C-R)

**P1**: The zero-shot generalization challenge — why it matters and why existing methods fail.
**P2**: Current best practices (prompts and adapters) and their individual limitations.
**P3**: CoPrompt's integrated response: consistency constraint as the enabling mechanism.
**P4**: Evidence that the integration works and how it compares.

This alternative trades technical depth for stronger contrastive positioning but may be easier for readers unfamiliar with the prompt-tuning literature.

### Selected Best Storyline: P-M-S-E

The Problem-Motivation-Solution-Evidence arc is selected because it:
(a) Ensures readers understand the research gap before solution details.
(b) Aligns the introduction variables with method variables (consistency → overfitting, embedding deviation).
(c) Directly maps introduced claims to experimental evidence (base-to-novel HM, cross-dataset, ablations).

### Concrete Revision for Introduction Paragraph 1

**Current version** (Page 1, paragraph under Figure 1): Opens with "Vision-language foundation models...have demonstrated excellent generalization capabilities. However, the sheer size...can make it challenging to fine-tune..." This is a generic observation that any VLM paper could use.

**Mentor Revised Version**:
"Vision-language models (VLMs) like CLIP achieve strong zero-shot performance by learning aligned image-text representations from web-scale data. However, adapting these models to downstream tasks with limited labeled data (few-shot learning) remains challenging: full fine-tuning destroys their zero-shot capabilities, while linear probing underperforms on specialized tasks. Recent parameter-efficient approaches—prompt tuning and adapter modules—add small learnable parameters while keeping the backbone frozen. Yet even these methods suffer from overfitting on scarce downstream data, causing the fine-tuned model's embeddings to drift away from the pre-trained encoder's feature space, which degrades the very generalization that makes VLMs valuable. This paper addresses this embedding drift problem directly."

### Concrete Revision for Introduction Paragraph 4 (Results + Contributions)

**Current version** (Page 2, lines 34-49): Combined results preview and 4-item contribution list.

**Mentor Revised Version**:
"We evaluate CoPrompt on three standard settings. On base-to-novel generalization across 11 benchmarks (Table 1), CoPrompt achieves 80.48% harmonic mean—improving over MaPLe by 1.93% and PromptSRC by 0.51%. On cross-dataset evaluation (Table 2), CoPrompt reaches 67.0% average accuracy, outperforming prior methods by 0.70-1.29%. Domain generalization results (Table 3) are competitive. In summary, this paper contributes: (1) A consistency-enforced fine-tuning method that learns from few samples without losing zero-shot generalizability. (2) A technique incorporating LLM-generated descriptions and image augmentations within the consistency constraint for stronger regularization. (3) A unified prompting and adapter framework enabled by the consistency constraint that prevents overfitting from increased parameter count."

## Priority Revision Plan
### P0 — Critical (Must fix before resubmission)

| Priority | Issue | Action | Location | Expected Impact |
|----------|-------|--------|----------|-----------------|
| P0 | Abstract overclaim on domain generalization | Remove "domain generalization" from outperformance claim; rephrase to "competitive" | Abstract, Introduction, Contribution (4) | Corrects factual error; restores trust |
| P0 | Missing adapter architecture details | Specify bottleneck ratio, nonlinearity, residual connection, α, position | Section 3.2 Adapters | Enables reproduction |
| P0 | Uncontrolled adapter ablation (12-layer vs 9-layer confound) | Add MaPLe (9-layer) + Adapter row to Table 11 | Appendix A.4 | Strengthens core claim |

### P1 — Major (Should fix before resubmission)

| Priority | Issue | Action | Location | Expected Impact |
|----------|-------|--------|----------|-----------------|
| P1 | No statistical significance for core results | Add std/CI to Table 1, Table 2; add paired significance test | Section 4.2, Tables 1-2 | Confirms 0.51% gain is real |
| P1 | Missing limitations section | Expand conclusion to 3 paragraphs with explicit limitations | Section 5 | Scientific completeness |
| P1 | Results paragraph lacks variance analysis | Add per-dataset discussion of significant/insignificant gains | Section 4.2 text | Honest reporting |

### P2 — Nice-to-have (Quality improvement)

| Priority | Issue | Action | Location | Expected Impact |
|----------|-------|--------|----------|-----------------|
| P2 | Related work is chronological list | Reorganize by design axes (modality, regularization, parameter type) | Section 2 | Clearer novelty positioning |
| P2 | Domain generalization not analyzed | Add 1-2 sentences explaining potential causes of underperformance | Section 4.4 | Insight value |
| P2 | FLOPs ambiguity | Report exact GFLOPs; clarify "2x" definition; add peak memory | Section 4.6 | Complete efficiency picture |
| P2 | Introduction narrative weak | Restructure as P-M-S-E arc (see Storyline Options) | Section 1 | Reader engagement |
| P2 | Hard augmentation explanation speculative | Add embedding distance analysis or reframe as hypothesis | Section 4.5 | Scientific rigor |

### Revision Order

```
Week 1: P0 fixes (abstract, adapter details, Table 11 controlled ablation)
  → Expected HM impact: corrects errors, strengthens core claim
Week 2: P1 fixes (statistical tests, limitations section, variance reporting)
  → Expected HM impact: confirms or adjusts claimed margins
Week 3: P2 fixes (related work, domain analysis, intro rewrite, FLOPs)
  → Expected HM impact: improves clarity and completeness
```

### Expected Outcome After All Fixes
- Corrected factual errors → Increased trust
- Reproducible adapter design → Higher reproducibility score
- Statistical significance established → Stronger evidence for claims
- Honest limitations discussed → Better scientific completeness
- Stronger narrative → Improved reader engagement

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|---------------------|-------|---------|-------------|-----------------|-------------------|
| E1 | Base-to-novel generalization | 11 datasets, 16-shot, base/novel split | Base Acc, Novel Acc, HM | 84.00/77.23/80.48 (Avg) | C1, C2, C3 | No std/CI; 0.51% HM over PromptSRC may not be significant |
| E2 | Cross-dataset evaluation | Train on ImageNet, test on 10 unseen datasets | Per-dataset Acc, Avg | 67.0% Avg | C1, C3 | Only one source dataset tested |
| E3 | Domain generalization | Train on ImageNet, test on 4 shifted variants | Per-dataset Acc, Avg | 60.42% Avg (below SOTA) | None (negative result) | Not analyzed; contradicts abstract |
| E4 | Main ablation (Cons., In.Pert., Adp.) | 6 configurations (Table 4) | HM | Cons+InPert+Adp=80.48%; w/o all=78.55% | C1, C2, C3 | Uncontrolled: w/o Cons uses 12-layer prompts, not 9 |
| E5 | Consistency modality analysis | Image-only, text-only, both | HM | Both=80.48%; Text-only=80.02%; Image-only=79.59% | C1 | No interaction analysis |
| E6 | Consistency criterion comparison | Cosine vs L1 vs MSE | HM | Cosine=80.48% best; MSE=79.33% | C1 | Small margins (0.08% over L1) |
| E7 | Text input perturbation | Same text vs GPT-2 vs GPT-3 | HM | GPT-3=80.48%; Same=80.09% | C2 | Small gain (0.39%); LLM choice irrelevant |
| E8 | Image input perturbation | Same vs Simple Aug vs Hard Aug (RandAug) | HM | Simple Aug=80.48%; Hard Aug=79.90% | C2 | Hard augmentation failure unexplained |
| E9 | Adapter placement | Text-only, image-only, both | HM | Both=80.48%; Text=80.35%; Image=80.10% | C3 | Marginal gains over text-only |
| E10 | Adapter depth | 1 vs 2 vs 3 layers | HM | 2-layer=80.48%; 3-layer=79.75% | C3 | No analysis of why 3 layers fails |
| E11 | λ sensitivity | λ ∈ {0, 0.01, 0.1, 1, 2, 8, 10} | Per-dataset Acc | Best at λ=8 (6/11 datasets) | C1 | EuroSAT optimal at λ=0.1 (different pattern) |
| E12 | Prompt layer depth | 3, 6, 9, 12 layers | HM | 12 layers=80.48% best | C1 | Contradicts MaPLe's finding (best at 9) |
| E13 | Training epochs | 3, 5, 8, 10 epochs | HM | 8 epochs=80.48% best | C1 | Overfitting after 8 epochs |
| E14 | Cross-backbone (EVA-CLIP) | CLIP-B/16 vs EVA-CLIP-B/16 | HM | CoPrompt + EVA = 80.75% | C1, C2, C3 | Small gain over CLIP (+0.27% HM) |
| E15 | Consistency on CoOp (transferability) | CoOp + consistency constraint | Base, Novel, HM | Novel: 63.22→64.87%; HM: 71.66→72.75% | C1 | Single baseline test |

### Research-Theme Gap Diagnosis

1. **New Knowledge**: The paper's primary knowledge contribution is that a consistency constraint between learnable and frozen encoders, combined with input perturbations, can prevent overfitting in few-shot VLM tuning. This is incrementally novel over PromptSRC's self-regulation and MaPLe's multi-modal coupling. **Gap**: The paper does not establish *why* cosine consistency works better than PromptSRC's self-regulation (KL-divergence on logits)—is it the angular objective, the dual-modality enforcement, or the adapter parameters? A mechanistic analysis is missing.

2. **Reproducibility/Reusability**: The code is open-source, but the adapter architecture is underspecified. The 2x FLOPs training cost and 1× inference cost are well quantified. **Gap**: No peak GPU memory or inference latency numbers are reported.

3. **Potential to Change Practice/Understanding**: If the consistency approach generalizes across VLM architectures and data regimes, it could influence how the community approaches few-shot adaptation. **Gap**: Only CLIP and EVA-CLIP backbones are tested. No experiments on larger backbones (ViT-L) or alternative VLMs (ALIGN, Florence). No experiments with varied shot counts (1-shot, 4-shot, 8-shot) to understand data efficiency.

### Proposed Research Experiments

#### P0 Experiment: Controlled Adapter Ablation
- **Target Claim**: C3 — combining prompts and adapters requires consistency constraint.
- **Hypothesis**: MaPLe (9-layer optimal) + Adapter without consistency will underperform MaPLe alone.
- **Minimal Design**: Take MaPLe's optimal 9-layer prompt configuration, add the same 2-layer adapters. Train with L_ce only (no consistency). Report HM on 11-dataset average.
- **Controls/Baselines**: MaPLe (9-layer, 78.55% HM), CoPrompt (80.48% HM).
- **Metrics**: HM on base-to-novel.
- **Success Criterion**: If HM < 78.55%, claim C3 is well-supported. If HM ≥ 78.55%, revise claim.
- **Estimated Cost/Time**: 1 V100 GPU-day.
- **Expected Paper-Quality Gain**: Stronger evidence for C3; removes confound from Table 11.

#### P1 Experiment: Statistical Significance Package
- **Target Claim**: C1 — CoPrompt outperforms prior SOTA (PromptSRC).
- **Hypothesis**: The 0.51% HM improvement is statistically significant.
- **Minimal Design**: (a) Report mean±std from 3 runs for all entries in Table 1. (b) Paired Wilcoxon signed-rank test: compute per-dataset HM differences between CoPrompt and PromptSRC across 11 datasets; test if median difference > 0.
- **Controls/Baselines**: PromptSRC (79.97% HM).
- **Metrics**: p-value, Cohen's d.
- **Success Criterion**: p < 0.05 → claim supported. p ≥ 0.05 → downgrade to "competitive."
- **Estimated Cost/Time**: Requires re-running 3 seeds on 11 datasets. ~2 V100 GPU-days.
- **Expected Paper-Quality Gain**: Establishes reliability; protects against irreproducibility.

#### P1 Experiment: Domain Generalization Analysis
- **Target Claim**: Understanding when CoPrompt underperforms.
- **Hypothesis**: CoPrompt's adapters learn source-specific biases that hurt robustness on certain distribution shifts.
- **Minimal Design**: (a) For ImageNet-A and ImageNet-R, compute per-class accuracy breakdown. (b) Measure cosine distance between pre-trained and learnable embeddings on each domain variant. (c) Compare with PromptSRC's embedding distance on same variants.
- **Controls/Baselines**: PromptSRC (60.65%), MaPLe (60.26%).
- **Metrics**: Per-dataset accuracy, embedding cosine distance.
- **Success Criterion**: Identify which shift types cause the largest embedding deviation and correlate with accuracy drop.
- **Estimated Cost/Time**: Pre-extracted embeddings from existing checkpoints; <1 day analysis.
- **Expected Paper-Quality Gain**: Insight into failure modes; enables future improvements.

#### P2 Experiment: Few-Shot Data Efficiency Curve
- **Target Claim**: C1 — works in few-shot setting.
- **Hypothesis**: CoPrompt's advantage over MaPLe/PromptSRC increases as shot count decreases.
- **Minimal Design**: Evaluate CoPrompt on base-to-novel at {1, 4, 8, 16} shots per class on a subset of 4 datasets (ImageNet, Caltech101, EuroSAT, DTD).
- **Controls/Baselines**: MaPLe, PromptSRC at same shot counts.
- **Metrics**: HM at each shot count.
- **Success Criterion**: CoPrompt shows larger relative gains at lower shot counts.
- **Estimated Cost/Time**: ~3 V100 GPU-days.
- **Expected Paper-Quality Gain**: Demonstrates data-efficiency advantage; strengthens C1.

#### P2 Experiment: Hard Augmentation Analysis
- **Target Claim**: C2 — understanding perturbation design.
- **Hypothesis**: Hard augmentations distort image embeddings beyond CLIP's text-aligned distribution, breaking the consistency signal.
- **Minimal Design**: For simple vs hard augmentations on 4 datasets: (a) compute average cosine distance between pre-trained and learnable image embeddings, (b) compute accuracy gap. (c) Test with lower-strength RandAug parameters.
- **Controls/Baselines**: No augmentation, simple augmentation.
- **Metrics**: Embedding distance, per-dataset accuracy.
- **Success Criterion**: Show correlation between embedding distance and accuracy drop.
- **Estimated Cost/Time**: 1 V100 GPU-day.
- **Expected Paper-Quality Gain**: Design guidance for perturbation strength; replaces speculation with evidence.

### ASCII Diagram — Experiment Upgrade Plan

```text
P0: Controlled Adapter Ablation (Week 1)
  [MaPLe 9-layer + Adapter w/o Cons.] ──> Compare vs MaPLe (78.55%)
       │
       ▼
  If HM < 78.55% ──> Claim C3 well-supported (retain)
  If HM ≥ 78.55% ──> Revise C3 (adapter alone may not cause overfitting)

P1: Statistical Significance (Week 1-2)
  [3-seed reruns + Wilcoxon test] ──> p < 0.05? ──> Keep superiority claim
                                        └─ p ≥ 0.05 ──> Downgrade to "competitive"

P1: Domain Generalization Analysis (Week 2)
  [Per-domain embedding analysis] ──> Identify failure modes
       │
       ▼
  Add 2-sentence analysis paragraph to Section 4.4

P2: Few-Shot Data Efficiency (Week 3)
  [1,4,8,16 shot sweep on 4 datasets] ──> Demonstrate data efficiency advantage

P2: Hard Augmentation Analysis (Week 3)
  [Embedding distance measurement] ──> Replace speculation with evidence
```

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
### Final Score: 6.5 / 10

**Scoring Rationale (Research Value + Novelty prioritized):**

- **Research Value (6/10)**: The paper addresses a well-motivated problem (zero-shot degradation during few-shot tuning) with a technically sound solution. The evaluation is comprehensive across 11 datasets and three protocols. However, the 0.51% HM improvement over PromptSRC is modest and may not be statistically significant. The domain generalization gap reduces overall confidence. The core mechanism (consistency constraint) is conceptually similar to PromptSRC's self-regulation, with the main differences being cosine distance vs KL divergence, additional adapters, and LLM-generated text. The incremental nature of these differences limits breakthrough-value impact.

- **Novelty (5/10)**: (Note: external literature verification was not possible in this run due to Retrieval-Disabled Mode; this score is based on manuscript-grounded analysis only and should be considered provisional.) C1 (consistency constraint) is the most distinctive contribution but shares conceptual overlap with PromptSRC's self-regulating mechanism. C2 (LLM + augmentation perturbations) is a practical extension. C3 (prompt + adapter combination) is enabled by the consistency constraint but each component individually is known. The combination is novel but incremental.

- **Soundness/Validity (7/10)**: The method is well-motivated, the ablation study is thorough, and the evaluation follows established protocols. However, missing statistical significance testing, the uncontrolled adapter ablation (12-layer vs 9-layer confound), and the abstract-domain generalization contradiction reduce trust.

- **Reproducibility (6/10)**: Code is open-sourced, and most training details are provided. However, the adapter architecture is underspecified (bottleneck dimension, residual connection, nonlinearity type missing), which would require guesswork to reproduce.

- **Presentation (7/10)**: The paper is clearly written and well-structured. The ablation tables are informative. Weaknesses: related work is a sequential list, conclusion lacks limitations, and the abstract contains a factual error regarding domain generalization.

### Post-Revision Target: [7.0, 8.0] / 10

If all P0 and P1 issues are resolved (abstract corrected, adapter specified, controlled ablation added, statistical significance established, limitations added), the score could rise to 7.0-8.0. Reaching 8.0 would additionally require resolving P2 items (stronger narrative, domain analysis, data efficiency experiments) and external literature verification confirming novelty claims.

---

### Page Coverage Audit

| Page | Annotation Count | Coverage Status | Skip Reason |
|------|-----------------|-----------------|-------------|
| 1 (Abstract + Intro P1) | 2 | Covered | — |
| 2 (Intro P2-P4 + Related Work start) | 2 | Covered | — |
| 3 (Related Work + Method start) | 1 | Covered | — |
| 4 (Method: Preliminaries + Consistency) | 1 | Covered | — |
| 5 (Method: Adapters + Figure 2) | 1 | Covered | — |
| 6 (Exp: Base-to-novel results) | 1 | Covered | — |
| 7 (Exp: Cross-dataset + Domain + Ablation) | 1 | Covered | — |
| 8 (Ablation: Analysis of components) | 1 | Covered | — |
| 9 (Sensitivity + Parameters + Conclusion) | 2 | Covered | — |
| 10-12 (References) | 0 | Skipped | Non-substantive (bibliography) |
| 13 (Appendix: Setup) | 0 | Covered via main-text reference | Setup details consistent with main text |
| 14 (Appendix: Ablations + backbone) | 1 | Covered | — |

**Total annotations: 13. Coverage: All substantive paragraphs in Abstract, Introduction, Method, Experiments, Conclusion, and Appendix are covered by at least one annotation.**

---

### ASCII Diagram — Paper Structure & Evidence Map

```text
[Problem: Few-shot VLM tuning → zero-shot degradation]
    │
    ├── [Claim C1: Consistency constraint prevents overfitting]
    │       └── Evidence: Ablation Table 4 (Cons-only: 79.50% vs w/o all: 78.55%)
    │       └── Gap: Standard deviation not reported; margin over baseline is 0.95%
    │
    ├── [Claim C2: LLM + augmentation perturbations improve generalization]
    │       └── Evidence: Table 5c (GPT-3 vs same text: 80.48 vs 80.09)
    │       └── Evidence: Table 5d (Simple aug vs same image: 80.48 vs 80.16)
    │       └── Gap: Hard augmentation degrades (79.90%); explanation is speculative
    │
    ├── [Claim C3: Prompt+Adapter combination under consistency works]
    │       └── Evidence: Table 4 (w/ all: 80.48, w/o adapter: 80.02)
    │       └── Evidence: Table 11 (w/o consistency: 78.45, MaPLe+Adapter: 77.61)
    │       └── Gap: Uncontrolled comparison (12-layer vs 9-layer MaPLe)
    │
    └── [Core Results]
            ├── Base-to-novel HM: 80.48% (1.93%↑ MaPLe, 0.51%↑ PromptSRC)
            ├── Cross-dataset: 67.0% (0.70-1.29%↑ over baselines)
            └── Domain gen.: 60.42% (0.23%↓ PromptSRC) ← Contradicts abstract
```

### ASCII Diagram — Revision Strategy Roadmap

```text
[Current Issues]
    │
    ├── [P0: Abstract overclaim] ──> Remove "domain gen." from claim list ──> Corrected abstract
    ├── [P0: Adapter underspecified] ──> Add bottleneck ratio, residual, α ──> Reproducible
    ├── [P0: Uncontrolled ablation] ──> Add 9-layer MaPLe+Adapter row ──> Clean evidence
    ├── [P1: Missing significance] ──> Add std/CI + Wilcoxon test ──> Reliable claims
    ├── [P1: No limitations] ──> Expand conclusion ──> Complete science
    └── [P2: Weak narrative] ──> Restructure intro as P-M-S-E ──> Stronger engagement
            │
            ▼
    [Post-Revision Quality]
        Validity ↑↑  Reproducibility ↑↑  Trust ↑↑  Narrative ↑
```

### ASCII Diagram — Related-Work Taxonomy Tree (Layered)

```text
VLM Few-Shot Tuning (Root)
│
├── Branch 1: Prompting Methods
│   ├── Leaf 1.1: Text-only Prompts
│   │   ├── CoOp (context vectors in text encoder)
│   │   ├── ProGrad (gradient-aligned prompt update)
│   │   └── KgCoOp (knowledge-guided context)
│   ├── Leaf 1.2: Multi-modal Prompts
│   │   ├── MaPLe (coupled image-text prompts)
│   │   └── PromptSRC (independent prompts + self-regulation)
│   └── Leaf 1.3: Bayesian / Distributional
│       ├── Bayesian Prompt Learning (variational inference)
│       └── ProDA (data-driven prompt distribution)
│
├── Branch 2: Adapter-based Methods
│   ├── Leaf 2.1: Text-only Adapters
│   │   └── CLIP-Adapter (bottleneck on text branch)
│   ├── Leaf 2.2: Vision-only Adapters
│   │   └── ViT-Adapter (dense prediction)
│   └── Leaf 2.3: Multi-modal Adapters
│       └── [Not established in prior work] ← CoPrompt targets this
│
└── Branch 3: Regularization / Consistency Methods (CoPrompt's branch)
    ├── Leaf 3.1: Self-Regulation (PromptSRC)
    │   └── KL-divergence between prompted and pre-trained logits
    ├── Leaf 3.2: Consistency Between Learnable and Frozen Encoders
    │   └── CoPrompt (cosine distance on embeddings + perturbations)
    └── Leaf 3.3: Combined Prompt + Adapter + Consistency
        └── CoPrompt (unique integration)
```

**Novelty Positioning**: CoPrompt sits at the intersection of Branch 1 (multi-modal prompting), Branch 2 (adapter methods), and Branch 3 (consistency regularization). Its primary novelty lies in demonstrating that the consistency constraint enables the combination of prompts and adapters (Branch 3, Leaf 3.3), which prior work could not achieve without overfitting. The secondary novelty is the use of LLM-generated perturbations in the text consistency branch (distinct from KgCoOp's embedding averaging).
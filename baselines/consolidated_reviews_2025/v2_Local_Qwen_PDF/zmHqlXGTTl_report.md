## Summary
This paper introduces LayoutSciPG, a new task for layout-aware scientific poster generation, along with a large-scale dataset (SciPG) containing over 10,000 paper-poster pairs. The authors propose a multimodal extractor-generator framework that jointly performs content extraction, abstractive paraphrasing, and flexible layout prediction using an adaptive memory mechanism. Extensive automatic and human evaluations demonstrate that the proposed method outperforms adapted baselines in text relevance and layout coverage, while highlighting remaining challenges in aesthetic design and element overlap. The work addresses a practical bottleneck in academic communication and provides a valuable benchmark for multimodal document generation.

## Strengths
1. **Practical Motivation and Clear Problem Formulation:** The paper addresses a highly relevant and practical problem in academic communication. The decomposition of the task into extraction, paraphrasing, and layout generation is logical and well-motivated.
2. **Large-Scale Dataset Contribution:** The introduction of the SciPG dataset with over 10,000 aligned paper-poster pairs is a significant resource for the community. The explicit element-level alignment provides high-quality supervision signals that were previously lacking.
3. **Unified Framework Design:** The proposed multimodal extractor-generator framework effectively integrates content selection and layout prediction. The use of an adaptive memory mechanism to handle long-term dependencies and GPU memory constraints is a thoughtful architectural choice.
4. **Comprehensive Evaluation:** The paper provides both automatic metrics (ROUGE, layout overlap/coverage, DreamSim) and human evaluations, offering a multi-faceted assessment of the generated posters. The ablation studies effectively validate the contribution of key components like the memory module and KL-divergence optimization.

## Weaknesses
1. **Ambiguous Mathematical Formulation and Loss Design:** The extraction loss function (Eq. 3) uses softmax normalization over all elements, implying a competitive selection mechanism. This is suboptimal for multi-label extraction where elements should be selected independently. Additionally, the coordinate system (normalized vs. pixel) and tensor shapes are not explicitly defined, reducing reproducibility.
2. **Weak Baselines and Evaluation Rigor:** The paper admits that "there are no established baselines" for the generation task, relying on an adapted slide-generation model (AdaD2P) as a proxy. This weakens the comparative evaluation. Furthermore, the optimization direction for the "Overlap" metric is ambiguous, and the human evaluation sample size (50 pairs) is relatively small.
3. **Dataset Splitting and Leakage Risks:** The dataset description mentions a random split but does not clarify whether conference/year boundaries are preserved. Random splitting of highly similar papers from the same venue could lead to data leakage, artificially inflating performance metrics.
4. **Generic Contribution and Conclusion Statements:** The contribution bullets and conclusion paragraph are somewhat generic, merely restating what was built without emphasizing the unique value proposition (e.g., explicit element alignment, unified paraphrasing-layout mechanism) or providing concrete future research directions.

## Key Issues
1. **Extraction Loss Formulation (Major):** The use of softmax in Eq. (3) introduces unwanted competitive dependencies between extracted elements. Switching to sigmoid activation with binary cross-entropy loss is necessary for independent multi-label extraction.
2. **Data Leakage Prevention (Major):** The random dataset split protocol must be clarified. Splitting by conference year or venue is required to prevent similar papers from appearing in both training and testing sets, which would invalidate the reported gains.
3. **Metric Direction Clarity (Major):** The "Overlap" metric direction is ambiguous. Explicitly stating whether higher or lower scores are better is essential for correct interpretation of Table 4.
4. **Baseline Justification (Major):** Relying solely on an adapted slide-generation model without a simple template-based or rule-based baseline weakens the evaluation. A stronger justification for baseline selection and the addition of a lower-bound baseline are needed.
5. **Alignment Quality Reporting (Major):** The appendix describes automatic alignment but lacks precision/recall metrics. Reporting alignment quality is critical to assure readers that supervision signals are reliable and not introducing significant noise.

## Actionable Suggestions
1. **Revise Extraction Loss:** Replace the softmax normalization in Eq. (3) with a sigmoid activation function and binary cross-entropy loss to enable independent element selection. Clarify the coordinate system (e.g., normalized to [0, 1]) in the method overview.
2. **Clarify Data Splitting Protocol:** Explicitly state whether the dataset is split by conference year to prevent data leakage. If not, re-run experiments with a leakage-preventing split and report the delta.
3. **Strengthen Baselines and Metrics:** Add a simple template-based baseline to establish a lower bound. Explicitly define the optimization direction for the "Overlap" metric (e.g., "lower is better").
4. **Report Alignment Quality:** In the appendix, add a manual verification sample (e.g., 100 pairs) reporting precision and recall for sentence and image matching. Discuss how unmatched elements are handled.
5. **Expand Conclusion:** Rewrite the conclusion to synthesize key quantitative gains, candidly discuss limitations (aesthetics, domain scope), and propose concrete future work (e.g., design constraints, cross-domain validation).

## Storyline Options + Writing Outlines
### Abstract Outline
- **S1 (Problem):** Scientific posters are essential for academic communication but require specialized design skills and significant time to create.
- **S2 (Gap):** Prior automated approaches decouple content extraction from layout generation, leading to rigid templates or misaligned content, and suffer from data scarcity.
- **S3 (Method):** We introduce LayoutSciPG and the SciPG dataset (11k+ pairs), proposing a unified multimodal extractor-generator framework with adaptive memory for joint paraphrasing and layout prediction.
- **S4 (Results):** Our method outperforms baselines by X% in ROUGE-L and significantly improves layout coverage, with human evaluations confirming higher text relevance.
- **S5 (Limitation/Future):** While effective, challenges in aesthetic design and element overlap remain, highlighting directions for future research.

### Introduction Outline
- **P1 (Motivation):** Establish the information overload challenge and the value of posters for quick comprehension. Highlight the dual requirement of content understanding and visual design.
- **P2 (Gap):** Critique prior work for decoupling extraction and layout, explaining how this leads to poor outcomes (e.g., loss of visual context, rigid templates).
- **P3 (Challenges):** Detail the three key challenges: multimodal extraction, joint paraphrasing/layout generation, and the need for large-scale aligned data.
- **P4 (Solution):** Introduce the SciPG dataset and the interactive generator with adaptive memory, emphasizing how they address the stated challenges.
- **P5 (Contributions):** List contributions focusing on impact: large-scale aligned dataset, unified framework overcoming template rigidity, and comprehensive validation revealing remaining aesthetic challenges.

## Priority Revision Plan
| Priority | Issue | Action | Expected Impact |
|---|---|---|---|
| P0 (Critical) | Extraction Loss Formulation | Switch from softmax to sigmoid/BCE loss in Eq. (3). | Enables independent element selection, improving extraction accuracy. |
| P0 (Critical) | Data Leakage Risk | Clarify split protocol; re-run with year-based split if needed. | Ensures reported gains are valid and not inflated by leakage. |
| P1 (Major) | Metric Direction Clarity | Explicitly state optimization direction for Overlap/Coverage. | Prevents misinterpretation of Table 4 results. |
| P1 (Major) | Baseline Justification | Add template-based baseline; justify AdaD2P adaptation. | Strengthens comparative evaluation and establishes lower bounds. |
| P2 (Minor) | Alignment Quality | Report precision/recall for automatic alignment in Appendix. | Assures readers of label reliability and training signal quality. |
| P2 (Minor) | Conclusion Expansion | Synthesize findings, discuss limitations, propose future work. | Improves scientific honesty and guides community next steps. |

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory
| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|---|---|---|---|---|---|---|
| E1 | MDE outperforms baselines in extraction | SciPG test set, NeuralExt/MSMO/AdaD2P | ROUGE, ImgP/R | MDE achieves highest scores | Yes | No variance reported |
| E2 | IG improves layout over AdaD2P | SciPG test set | Overlap, Coverage, Val, Ali, FD, DreamSim | Significant gains in coverage/validity | Yes | Overlap direction ambiguous |
| E3 | Ablation of generator components | Full vs. w/o KL/PT/DE/Memory | ROUGE, Overlap, Coverage | Memory module crucial for layout | Yes | Single-seed results |
| E4 | Topic-aware generalization | Train/test on CVPR/ICML/NeurIPS/ICLR | ROUGE, Overlap, ImgP/R | All-topic model best overall | Yes | Domain limited to CS |
| E5 | Human evaluation of poster quality | 50 pairs, 10 annotators | Text Relevance, Image Accuracy, Layout Aesthetics | Ours > Baseline, but aesthetics low | Yes | Small sample size |

### Research-Theme Gap Diagnosis
The current experiments validate core functionality but lack robustness evidence (multi-seed variance, OOD generalization beyond CS conferences) and causal isolation (matched-capacity controls for memory mechanism).

### Proposed Research Experiments
| Target Claim | Hypothesis | Minimal Design | Controls | Metrics | Success Criterion | Cost | Gain |
|---|---|---|---|---|---|---|---|
| Robustness | Gains are stable across random seeds | Run E1/E2 with 3 seeds | Same baselines | Mean±Std ROUGE/Coverage | Std < 1% | Low | Statistical reliability |
| Causal Attribution | Memory module drives layout gains | Matched-capacity w/o memory | Same params/epochs | Overlap/Coverage delta | Delta significant | Low | Isolates mechanism impact |
| OOD Generalization | Model transfers to non-CS domains | Test on arXiv physics/biology posters | In-domain baseline | ROUGE/Coverage drop | Drop < 10% | Medium | Validates external validity |

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score:** 6.5/10

**Rationale:** The paper addresses a practical and well-motivated problem with a solid dataset contribution and a coherent unified framework. The empirical results are promising and the ablation studies are informative. However, the score is moderated by critical issues in the extraction loss formulation, potential data leakage risks due to unclear splitting protocols, ambiguous metric directions, and weak baseline justification. These validity concerns prevent a higher score until addressed.

**Post-Revision Target:** [7.5, 8.5]/10

**Path to Target:** Resolving the P0 issues (switching to sigmoid/BCE loss, clarifying/enforcing leakage-free splitting) and strengthening the evaluation (adding a template baseline, reporting multi-seed variance) will significantly improve scientific rigor and confidence in the reported gains, justifying a strong acceptance score.
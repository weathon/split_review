## Summary
# Final Review Report

## Summary

This paper presents Toto, a causal transformer designed for generative pre-training from videos. The authors propose a straightforward autoregressive next-token prediction objective applied to quantized patch embeddings (using dVAE) and relative positional embeddings (RoPE). Models are pre-trained on over 1 trillion visual tokens from a mixture of image and video datasets, scaling up to 1 billion parameters. The paper evaluates Toto across a diverse suite of benchmarks, including image recognition (ImageNet), action recognition (Kinetics-400), action anticipation (Ego4D), video tracking (DAVIS), object permanence (CATER), and robotic manipulation (simulation and real-world). The authors also characterize the scaling behaviors of visual autoregressive models, observing a power-law relationship between compute and validation loss. The work positions itself as a large-scale empirical study establishing a strong baseline for autoregressive video understanding, demonstrating competitive performance with minimal inductive biases.

## Strengths
1. **Large-Scale Empirical Study:** The paper conducts a comprehensive and large-scale empirical investigation of autoregressive generative pre-training for videos. Pre-training up to 1 billion parameters on over 1 trillion visual tokens provides valuable insights into the scalability and effectiveness of next-token prediction in vision.

2. **Unified Image/Video Pre-training:** The use of relative positional embeddings (RoPE) and quantized patch tokens enables efficient joint pre-training on images and videos. This unified approach simplifies the training pipeline and allows the model to leverage the vast amount of available image data alongside video data.

3. **Diverse Downstream Evaluation:** The evaluation spans a wide range of tasks, including image recognition, action recognition, action anticipation, video tracking, object permanence, and robotic manipulation. This breadth demonstrates the versatility of the learned representations and their transferability to both perception and control tasks.

4. **Scaling Law Characterization:** The paper provides a clear analysis of the scaling behaviors of visual autoregressive models, revealing a power-law relationship between compute and validation loss. This contributes to the growing understanding of how vision models scale compared to language models.

5. **Reproducibility Commitment:** The authors plan to release models, training code, and evaluation code, which will facilitate further research and benchmarking in the community.

## Weaknesses
1. **Overly Self-Deprecating Framing:** The abstract and introduction contain statements such as "This paper does not describe a novel method," which undermine the perceived research value. The large-scale empirical study, scaling insights, and cross-task evaluation constitute significant contributions that should be framed positively.

2. **Incomplete Methodological Details:** The Approach section omits critical reproducibility details, including attention head dimensions, MLP hidden sizes, RoPE base values, and the exact data mixing strategy (token vs. sample proportion). The sequence construction for joint image/video training is fragmented across sections.

3. **Unexplained Empirical Findings:** The resolution ablation shows that coarse-to-fine pre-training (low-res pre-training + high-res fine-tuning) outperforms full-resolution pre-training, but the mechanism behind this success is not discussed. Similarly, the claim that VQGAN is "contaminated" with ImageNet labels lacks detailed justification.

4. **Unfair or Unqualified Comparisons:** Table 7 compares Toto-1b (75.3%) to AIM (82.2%, 3B params) without acknowledging the parameter disparity. The tracking evaluation (Table 10) claims to "outperform all methods" at 512 resolution but compares against smaller base models. The robotics gap (63% vs. 75% for MVP) is described as "comparable" without acknowledging the 12% absolute difference.

5. **Vague Observations and Terminology Errors:** The Ego4D action anticipation section states that self-supervision loss "improves overall performance" without quantifying the improvement. The conclusion incorrectly mentions "trajectory prediction" instead of "action anticipation." The conclusion also lacks a discussion of limitations and future work.

## Key Issues
1. **Reproducibility Gaps in Method Description:** The lack of explicit architectural hyperparameters (head dimensions, MLP ratios, RoPE base) and ambiguous data mixing ratios (token vs. sample proportion) hinder reproducibility. Reviewers cannot fairly compare or reproduce the model without these details.

2. **Insufficient Analysis of Key Findings:** The coarse-to-fine resolution success and the slower scaling exponent compared to language models are significant empirical observations. Without mechanistic explanations (e.g., RoPE extrapolation, regularization effects, visual redundancy), these findings remain descriptive rather than insightful.

3. **Overstated or Unqualified Claims:** Claims such as "first to show competitive performance on action recognition with autoregressive generative modeling" and "outperforms all methods" in tracking are risky without parameter-matched or compute-matched baselines. The robotics performance gap is downplayed, which may affect perceived honesty.

4. **Missing Limitations and Future Work:** The conclusion lacks a discussion of limitations (e.g., tokenization efficiency, scaling rate, domain-specific gaps) and future directions. This is a standard expectation for high-quality empirical studies and its absence weakens the paper's scientific rigor.

## Actionable Suggestions
1. **Rewrite Abstract and Introduction Framing:** Remove self-deprecating language. Emphasize the empirical contribution, scale (1T tokens, 1B params), and key findings (scaling laws, competitive performance). Provide a clear, enumerated contribution list at the end of the introduction.

2. **Expand Method Description:** Add a complete architecture table with head dimensions, MLP ratios, and RoPE base values. Clarify the data mixing strategy in terms of token proportion. Consolidate sequence construction details (start/end tokens, frame sampling, raster scan ordering) into the Approach section.

3. **Provide Mechanistic Analysis:** Explain why coarse-to-fine pre-training is effective (e.g., RoPE extrapolation, regularization). Discuss potential reasons for the slower scaling exponent compared to language models (e.g., visual redundancy, tokenization inefficiency).

4. **Qualify Comparisons and Claims:** Acknowledge parameter disparities when comparing to AIM. Qualify the tracking claim by noting model size differences. Explicitly acknowledge the 12% robotics gap vs. MVP and attribute it to domain-specific pre-training. Quantify the improvement from self-supervision loss in the Ego4D task.

5. **Add Limitations and Future Work:** Include a concise paragraph in the conclusion discussing limitations (tokenization efficiency, scaling rate, robotics gap) and future directions (improved tokenizers, larger-scale pre-training, multimodal extensions). Correct "trajectory prediction" to "action anticipation."

## Storyline Options + Writing Outlines
### Abstract Outline (Complete)
- **S1 (Problem/Domain):** Generative pre-training via next-token prediction has revolutionized language modeling and is increasingly applied to vision, but scaling to videos remains challenging due to long sequence lengths and inefficient tokenization.
- **S2 (Significance/Challenge):** Video data offers vast, unfiltered information for learning robust visual representations, yet existing autoregressive models struggle with context length and joint image/video training.
- **S3 (Prior Gap):** Current approaches rely on absolute positional embeddings and pixel-level tokenization, limiting scalability and computational efficiency.
- **S4 (Proposed Method):** We introduce Toto, a causal transformer that leverages relative positional embeddings (RoPE) and quantized patch tokens to enable efficient, scalable generative pre-training on mixed image and video data.
- **S5 (Key Result/Implication):** Pre-training up to 1 billion parameters on over 1 trillion visual tokens yields competitive performance across diverse benchmarks (image recognition, video understanding, robotics) and reveals clear scaling laws for visual autoregressive models.

### Introduction Outline (Complete)
- **P1 (Big Picture):** Establish the success of autoregressive generative pre-training in LLMs and its emerging potential in vision. Highlight the vast untapped potential of video data.
- **P2 (Concrete Gap):** Identify technical limitations of current autoregressive vision models: absolute positional embeddings restrict context length, pixel-level tokenization is computationally expensive, and joint image/video training is under-explored.
- **P3 (Proposed Solution):** Introduce Toto as a solution: a causal transformer with RoPE for seamless resolution/context extension, and dVAE tokenization for efficient discrete representation. Emphasize the unified training pipeline.
- **P4 (Evidence Preview):** Summarize the scale of pre-training (1T tokens, 1B params) and the diverse evaluation suite (ImageNet, Kinetics, Ego4D, DAVIS, robotics). Mention the scaling law analysis.
- **P5 (Contribution Summary):** Explicitly list three contributions: (1) Toto architecture with RoPE and dVAE for scalable joint pre-training, (2) large-scale empirical evaluation demonstrating competitive performance, (3) characterization of scaling laws for visual autoregressive models.

## Priority Revision Plan
| Priority | Action | Expected Impact | Effort |
|---|---|---|---|
| **P0** | Rewrite abstract and introduction to remove self-deprecating language and add explicit contribution list. | Improves perceived research value and clarity. | Low |
| **P0** | Expand Approach section with full architecture details (head dims, MLP ratios, RoPE base) and clarify data mixing/tokenization pipeline. | Ensures reproducibility and fairness. | Medium |
| **P1** | Add mechanistic analysis for coarse-to-fine resolution success and slower scaling exponent. | Transforms empirical observations into scientific insights. | Medium |
| **P1** | Qualify performance comparisons (AIM, tracking, robotics) by acknowledging parameter/compute disparities and domain-specific advantages. | Strengthens objectivity and defensibility. | Low |
| **P2** | Quantify self-supervision improvement in Ego4D task and correct "trajectory prediction" terminology. | Improves precision and rigor. | Low |
| **P2** | Add limitations and future work paragraph to conclusion. | Meets standard expectations for empirical studies. | Low |

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory
| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|---|---|---|---|---|---|---|
| E1 | Tokenizer comparison | ImageNet, 400 epochs, large model | Top-1 accuracy | dVAE and VQGAN perform similarly; dVAE has full token coverage | Tokenizer choice has limited impact | VQGAN contamination claim lacks detail |
| E2 | Resolution ablation | dVAE tokens, 128x128 vs 256x256 | Top-1 accuracy | Coarse-to-fine (128->256) outperforms full-res pre-training | RoPE enables resolution extension | Mechanism unexplained |
| E3 | Architecture comparison | GPT2, Mamba, Toto | Top-1 accuracy | Toto outperforms GPT2 and Mamba | Transformer with RoPE is effective | Limited architecture search |
| E4 | ImageNet recognition | Linear probing + fine-tuning | Top-1 accuracy | Toto-1b achieves 75.3% | Competitive generative representations | Parameter disparity vs AIM not discussed |
| E5 | Kinetics-400 action recognition | Linear probing + fine-tuning | Top-1 accuracy | Toto-1b achieves 74.4% | Effective for video understanding | "First to show" claim risky |
| E6 | Ego4D action anticipation | StillFast backbone, full fine-tuning | mAP | Toto-large achieves 2.70 overall | Useful for temporal reasoning | Self-supervision gain not quantified |
| E7 | DAVIS tracking | Zero-shot label propagation | J&F score | Toto-large (512) achieves 62.4 | Strong zero-shot features | Comparison against smaller models |
| E8 | Robotics (sim/real) | DAgger/BC, frozen features | Success rate | Toto-base competitive with MVP | Transferable to control tasks | 12% gap vs MVP downplayed |
| E9 | Scaling laws | Varying model sizes, optimal LR | Validation loss | Power-law relationship observed | Visual autoregressive models scale | Slower exponent vs GPT-3 unexplained |

### Proposed Research Experiments
| Target Claim | Hypothesis | Minimal Design | Controls/Baselines | Metrics | Success Criterion | Estimated Cost | Expected Gain |
|---|---|---|---|---|---|---|---|
| Coarse-to-fine mechanism | Low-res pre-training acts as regularizer; RoPE enables extrapolation | Pre-train at 128, fine-tune at 256/512 with/without RoPE base adjustment | Full-res pre-training, absolute pos emb | Top-1 accuracy | Isolate RoPE vs regularization effect | Low | Scientific insight |
| Robotics gap analysis | Domain-specific pre-training drives MVP advantage | Fine-tune Toto on 100DOH data vs frozen | MVP, Toto-base frozen | Success rate | Quantify data vs architecture contribution | Medium | Fairer comparison |
| Scaling exponent context | Visual redundancy/tokenization inefficiency slows scaling | Compare scaling with different tokenizers (continuous vs discrete) | GPT-3 scaling curve | Loss vs compute | Explain exponent difference | High | Deeper understanding |

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score:** 6.5/10

**Rationale:** The paper presents a valuable large-scale empirical study on autoregressive generative pre-training for videos, demonstrating competitive performance across diverse tasks and providing insights into scaling laws. The unified image/video training pipeline and the use of RoPE for scalable context extension are strong technical contributions. However, the score is moderated by several issues: overly self-deprecating framing that undermines research value, incomplete methodological details hindering reproducibility, unexplained empirical findings (coarse-to-fine success, slower scaling exponent), and unqualified performance comparisons that risk being perceived as cherry-picked. With targeted revisions to clarify contributions, expand method details, provide mechanistic analysis, and qualify comparisons, the paper's impact and defensibility would significantly improve.

**Post-Revision Target:** [7.5, 8.5]/10

**Breakdown:**
- **Research Value/Novelty:** 7/10 (Strong empirical contribution, but novelty is incremental over iGPT/AIM; scaling insights are valuable)
- **Validity/Soundness:** 6/10 (Method details incomplete, comparisons need qualification, analysis lacks depth)
- **Reproducibility:** 6/10 (Missing hyperparameters and data mixing details)
- **Clarity/Writing:** 6/10 (Self-deprecating framing, vague observations, terminology errors)
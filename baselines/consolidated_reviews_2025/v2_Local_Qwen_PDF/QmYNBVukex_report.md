## Summary
# Final Review Report

## Summary
This paper introduces GOT-D (Gradients of Optimal Transport for Data Selection), a principled data selection strategy for pre-fine-tuning large language models (LLMs). The authors identify a critical gap in existing distribution-matching methods: they overlook the model's existing pre-training knowledge, leading to redundant sample selection and marginal gains in low-budget regimes. By modeling the fine-tuned model's effective distribution as a weighted mixture of pre-training and fine-tuning data, the authors derive a theoretical upper bound on downstream loss using Optimal Transport (OT) distance. GOT-D leverages the gradient of the OT distance to select unlabeled samples that most effectively shift the pre-training distribution toward the target task. Empirically, the method demonstrates consistent performance improvements over strong baselines (DSIR, DAPT, TAPT/c) across detoxification, domain adaptation, and zero-shot tasks, while maintaining high scalability (selection within a single GPU hour). The theoretical grounding, clear problem formulation, and comprehensive empirical validation make this a strong contribution to efficient LLM adaptation.

## Strengths
1. **Clear Problem Formulation & Theoretical Grounding:** The paper correctly identifies that light fine-tuning creates an effective data distribution that is a weighted mixture of pre-training and fine-tuning data. Lemma 1 and Theorem 1 provide a solid theoretical foundation for why minimizing the OT distance between this mixture and the target distribution is optimal, distinguishing the approach from naive distribution-matching methods.
2. **Practical Scalability:** GOT-D leverages entropy-regularized OT and GPU-accelerated dual solvers to compute selection gradients for millions of samples within minutes. This addresses a critical bottleneck in prior data selection methods that rely on iterative re-training or expensive clustering.
3. **Comprehensive Empirical Validation:** The method is evaluated across diverse settings (detoxification, domain adaptation, GLUE, zero-shot) with models up to 2.7B. The consistent outperformance of strong baselines (DSIR, DAPT, TAPT/c), particularly in low-resource regimes, strongly validates the core intuition.
4. **Open-Source Contribution:** The authors provide open-sourced code, facilitating reproducibility and enabling the community to build upon this efficient pre-fine-tuning paradigm.

## Weaknesses
1. **Unbounded Strong Claims:** The abstract and results sections use phrases like "consistently surpasses" and "regardless of the data selection budget" without explicitly bounding these claims to the tested settings, baselines, and evaluation protocols. This reduces defensibility against stronger or differently tuned baselines.
2. **Abstract Lacks Clear Problem Framing:** The abstract leads with the solution rather than establishing the core problem and its practical stakes. It also omits a concise statement of the research gap, making it harder for readers to immediately grasp the motivation.
3. **Theoretical Abstraction of Mixing Coefficient:** In Lemma 1, the mixing coefficient $\lambda$ is introduced as an unspecified constant. Without relating $\lambda$ to practical hyperparameters (learning rate, epochs, dataset sizes), the theoretical bound remains somewhat abstract and less actionable for practitioners.
4. **Missing Limitations & Future Work:** The conclusion summarizes contributions but omits a discussion of limitations (e.g., reliance on proxy pre-training data, performance under severe domain shift) and concrete future directions, leaving the scope of claims appearing unbounded.
5. **Mechanical Narrative Flow:** The introduction uses parenthetical tags (e.g., "(tackling G3)") to map method features to design challenges. This style interrupts the narrative flow and makes the contribution statement feel like a checklist rather than a cohesive methodological advance.

## Key Issues
1. **Claim-Evidence Alignment in Results:** The results sections occasionally overgeneralize (e.g., "regardless of the data selection budget") or attribute gains to speculative correlations (e.g., initial low performance on CoLA/RTE) without rigorous testing. Bounding these claims to the tested settings and using cautious language will improve scientific credibility.
2. **Theoretical Grounding of $\lambda$:** The mixing coefficient $\lambda$ in Lemma 1 is critical to the low-data regime assumption but is left as an unspecified constant. Explicitly relating $\lambda$ to training dynamics (learning rate, steps, dataset sizes) would bridge the theory-practice gap and strengthen the reproducibility of the theoretical insights.
3. **Missing Limitations Discussion:** The absence of a limitations section in the conclusion leaves readers unaware of the method's boundaries (e.g., dependency on proxy pre-training data quality, potential degradation under severe domain shift). Acknowledging these constraints is essential for a complete scientific narrative.

## Actionable Suggestions
1. **Restructure Abstract:** Rewrite the abstract to follow a clear 4-5 sentence arc: (1) Problem & stakes, (2) Prior gap, (3) Proposed method intuition, (4) Bounded key results. Replace unbounded claims ("consistently surpasses") with precise, evidence-linked wording scoped to tested settings.
2. **Ground Theoretical Coefficients:** In Lemma 1, explicitly relate the mixing coefficient $\lambda$ to practical hyperparameters (e.g., $\lambda \approx \eta \cdot \text{epochs} \cdot N(D_U) / N(D_P)$). This bridges the theory-practice gap and clarifies why $\lambda \ll 1$ holds in low-budget regimes.
3. **Integrate Challenge Mapping Naturally:** Remove parenthetical tags like "(tackling G3)" from the introduction. Instead, weave the mapping between method features and design challenges directly into the prose to improve narrative flow and readability.
4. **Bound Empirical Claims:** In results paragraphs, replace overgeneralizations (e.g., "regardless of budget") with bounded statements (e.g., "under tested budgets"). Add cautious language for speculative correlations (e.g., "suggesting that principled pre-fine-tuning is most beneficial when...").
5. **Add Limitations & Future Work:** Append 2-3 sentences to the conclusion explicitly stating current limitations (e.g., reliance on proxy pre-training data, performance under severe domain shift) and outlining a concrete next step (e.g., extending to instruction-tuning regimes).

## Storyline Options + Writing Outlines
### Abstract Outline (Complete)
- **S1 (Problem & Stakes):** Fine-tuning large language models (LLMs) on emerging tasks often requires costly, domain-specific labeled data, limiting widespread adoption.
- **S2 (Prior Gap):** While recent data selection methods scale to language corpora, they typically prioritize samples matching the target distribution, overlooking the model's existing pre-training knowledge and yielding marginal gains in low-budget regimes.
- **S3 (Proposed Method):** We propose GOT-D, a principled selection strategy that uses gradients of the Optimal Transport distance to identify unlabeled samples that most effectively shift the pre-training distribution toward the target task.
- **S4 (Theoretical Grounding):** Under a low-data fine-tuning regime, we prove this approach minimizes a theoretical upper bound on downstream loss by accounting for the effective data distribution as a weighted mixture.
- **S5 (Bounded Results):** Empirically, GOT-D outperforms existing selection baselines across detoxification, domain adaptation, and zero-shot tasks with models up to 2.7B, while scaling to millions of samples within a single GPU hour.

### Introduction Outline (Complete)
- **P1 (Big Picture & Paradigm):** Introduce the two-stage fine-tuning paradigm (pre-fine-tuning on unlabeled data + targeted fine-tuning on labeled data) as a cost-effective alternative to full fine-tuning. Explicitly state the gap: naive selection wastes compute on redundant samples.
- **P2 (Prior Work Critique):** Discuss existing distribution-matching methods and explain why they fail in the low-data regime: they ignore the pre-training distribution, leading to selection of samples the model already knows.
- **P3 (Challenges & Method Intro):** List design challenges (effectiveness, efficiency, scalability, generalizability) and introduce GOT-D's core intuition: selecting samples that bridge the gap between pre-training and target distributions. Integrate challenge mapping naturally into prose.
- **P4 (Theoretical Preview):** Preview Lemma 1 and Theorem 1, explaining how the effective data distribution is a weighted mixture and how OT gradients provide an optimal selection direction.
- **P5 (Empirical Preview & Contributions):** Summarize key empirical results across diverse tasks, emphasizing consistent gains in low-resource settings and high scalability. Conclude with a concise contribution list.

## Priority Revision Plan
| Priority | Action | Expected Impact | Effort |
|---|---|---|---|
| **P0** | Restructure Abstract & Introduction to follow problem-gap-solution-evidence arc; remove mechanical parenthetical tags. | Improves narrative flow, reader engagement, and immediate clarity of contribution. | Low |
| **P0** | Bound strong claims in results sections (e.g., "regardless of budget") to tested settings; add cautious language for speculative correlations. | Enhances scientific defensibility and prevents reviewer challenges on overgeneralization. | Low |
| **P1** | Explicitly relate mixing coefficient $\lambda$ in Lemma 1 to practical hyperparameters (learning rate, epochs, dataset sizes). | Bridges theory-practice gap, strengthens reproducibility of theoretical insights. | Medium |
| **P1** | Add a concise limitations & future work paragraph to the conclusion. | Improves scientific credibility, acknowledges scope boundaries, and guides future research. | Low |
| **P2** | Include variance/confidence intervals for utility drop claims in detoxification experiments. | Strengthens statistical reliability of trade-off analysis. | Medium |

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory
| Exp ID | Objective/Hypothesis | Setup (data/split/protocol/baselines) | Metrics | Main Outcome | Claim Supported | Current Limitation |
|---|---|---|---|---|---|---|
| E1 | GOT-D reduces toxicity while preserving utility | GPT-2 base, OWTC candidate, RTP prompts, baselines: DSIR, RTP, Random | Exp. Max Toxicity, Toxicity Prob, PPL, Avg Acc | Significant toxicity reduction with minor utility drop | Yes | Utility drop lacks variance reporting |
| E2 | GOT-D improves domain adaptation under budget constraints | BERT-base, 8 datasets across 4 domains, 150K/50K budgets, baselines: DAPT, DSIR, TAPT/c | Macro/Micro F1 | Consistent gains, especially on low-resource datasets | Yes | Limited to BERT-scale models |
| E3 | GOT-D enhances general NLU (GLUE) | BERT-base, 8 GLUE tasks, 50K budget, baselines: DSIR, TAPT/c | Accuracy/MCC | Outperforms baselines, larger gains on initially low-performing tasks | Yes | Gains attributed speculatively to initial performance |
| E4 | GOT-D scales to larger models in zero-shot setting | GPT-2 XL (1.5B), GPT-Neo (2.7B), AGNews/BoolQ, 40K budget | Zero-shot Accuracy | Substantial improvements (up to 13.9%) over baselines | Yes | Evaluated on only two zero-shot tasks |

### Research-Theme Gap Diagnosis
The core research-value claims (new knowledge via OT gradient selection, reproducibility via open code, impact on cost-effective fine-tuning) are well-supported. However, the robustness of the method under severe domain shift and its applicability to instruction-tuning regimes remain untested. Additionally, statistical variance is missing for some utility/trade-off claims.

### Proposed Research Experiments (P0/P1/P2)
| Target Claim | Hypothesis | Minimal Design | Controls/Baselines | Metrics | Success Criterion | Est. Cost/Time | Expected Gain |
|---|---|---|---|---|---|---|---|
| Robustness under domain shift | GOT-D maintains gains when candidate data diverges from pre-training distribution | Select from out-of-domain corpora (e.g., code, scientific papers) for NLU tasks | DSIR, Random, Vanilla | F1, Accuracy | Gains > 50% of in-domain gains | 1 GPU day | Validates boundary conditions |
| Statistical reliability of trade-offs | Utility drop in detoxification is statistically bounded | Report mean±std over 5 seeds for PPL and Avg Acc | Same baselines | PPL, Avg Acc (with CI) | CI does not overlap with large drop | 0.5 GPU day | Strengthens defensibility |
| Extension to instruction-tuning | GOT-D improves instruction-following with limited labeled instructions | Pre-fine-tune on selected unlabeled data, then instruction-tune on 1K samples | DAPT, Random | AlpacaEval/MT-Bench scores | Higher instruction adherence | 2 GPU days | Broadens practical impact |

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score:** 7.5/10

**Rationale:** The paper presents a theoretically grounded and highly practical method for data selection in LLM pre-fine-tuning. The core intuition—shifting the pre-training distribution toward the target rather than merely matching the target—is novel and well-motivated. The theoretical derivation (Lemma 1, Theorem 1) provides a solid foundation, and the empirical validation across diverse tasks (detoxification, domain adaptation, GLUE, zero-shot) consistently demonstrates superior performance and scalability. The primary deductions stem from unbounded strong claims in the abstract/results, the abstract lack of clear problem framing, and the omission of a limitations discussion. These are writing and framing issues rather than fundamental scientific flaws, making the paper highly competitive.

**Post-Revision Target:** [8.5, 9.0]/10

**Path to Target:** Restructuring the abstract/introduction for clearer problem-gap-solution alignment, bounding empirical claims to tested settings, explicitly grounding the theoretical mixing coefficient $\lambda$, and adding a concise limitations section will significantly improve defensibility and narrative coherence. These revisions are low-effort but high-impact, directly addressing the key issues identified without requiring new experiments.
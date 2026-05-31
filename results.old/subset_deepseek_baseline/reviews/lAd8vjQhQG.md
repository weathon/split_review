## Summary

The paper investigates the strategic reasoning capabilities of LLMs in the imperfect-information card game Dou Dizhu. It introduces a duplicate round-robin tournament benchmark for fair evaluation, proposes a data construction framework with two mechanisms (globally optimal decision alignment via symmetric information and real-time in-game feedback augmentation), and uses curriculum learning to fine-tune a 4B-parameter student model. The authors claim their fine-tuned model significantly outperforms its baseline and larger models from the same family.

## Strengths

- The duplicate tournament format is a well-motivated design for neutralizing card-distribution stochasticity, making comparisons more skill-based.
- The idea of using post-hoc perfect-information validation and multi-agent feedback to filter training data is conceptually interesting and addresses a genuine challenge in imperfect-information games.
- The paper attempts to improve a small model through data-centric methods rather than scaling, which is a practically relevant direction.

## Weaknesses

### Fatal

- **Use of non-existent or unverifiable models and hardware.** The paper evaluates “GPT-5,” “DeepSeek V3.1-Think,” “Doubao-Seed-1.6-thinking,” and “Qwen3-Next-80B-A3B-Thinking”—none of which are publicly known or verifiable models. Training is reported on “RTX 5090 GPUs,” a GPU that has not been released. These details strongly suggest fabrication or speculative content, invalidating the entire experimental foundation and reproducibility claims.

### Major

- **Overclaiming relative to actual results.** The paper claims to “significantly enhance gameplay proficiency” and “approach the performance of top-tier LLMs,” yet the best fine-tuned 4B model achieves an average duplicate score of 17.25, far below the top SOTA models (GLM-4.5 at 32.75, GPT-5 at 22.20). The improvement over baseline is real, but the framing is misleading.
- **Lack of direct comparison to the SOTA models from the benchmark.** The comparative experiments only pit the fine-tuned model against other Qwen-family models, not against the frontier models (GLM-4.5, GPT-5, Gemini 2.5 Pro) that were benchmarked earlier. Without such comparisons, the claim of “approaching” top-tier performance is unsupported.
- **Data construction details are insufficient for replication.** The “globally optimal decision alignment” mechanism is described only at a high level; it is unclear how the model is prompted to re-evaluate under perfect information, how consistency is measured, and how the threshold for “golden sample” is set. The feedback augmentation similarly lacks precise scoring criteria and inter-annotator agreement.

### Minor

- The paper states that “decision accuracy” on a held-out validation set is used for early stopping, but it does not define how accuracy is computed for a multi-action game (e.g., exact match vs. per-decision correctness).
- The curriculum learning stages are described, but the rationale for the specific data volumes (85,079 victorious vs. 41,884 GOFA) is not justified.

### Trivial

- Figure 1 and Table 3 present the same data redundantly; one could be omitted.
- The paper uses “GOFA” as an acronym but does not spell it out in the main text (it appears in Table 2 caption).

## Nice-to-Haves

- A comparison of the fine-tuned 4B model against the top SOTA models (GLM-4.5, GPT-5) on the same benchmark would greatly strengthen the claims.
- Ablation of the two data curation mechanisms separately (globally optimal alignment alone, feedback alone) would clarify their individual contributions.
- Human evaluation or comparison against a rule-based Dou Dizhu AI (e.g., DouZero) would provide a more grounded baseline.

## Novel Insights

None beyond the paper’s own contributions. The core insight—that post-hoc perfect-information validation and multi-agent feedback can filter higher-quality training data for imperfect-information games—is sensible but not deeply analyzed or theoretically grounded.

## Suggestions

- Remove all references to non-existent models and hardware, or replace them with verifiable, publicly available models and hardware.
- Provide a direct comparison between the fine-tuned model and the top-performing SOTA models from the benchmark.
- Clarify the exact prompt templates and scoring rules used in the data curation mechanisms, and release them in the supplementary material.
- Conduct an ablation study that isolates the two data curation mechanisms to quantify their individual contributions.

## Score and Decision

**Score:** 1  
**Decision:** Reject  

The paper contains fatal issues that undermine its credibility: the use of non-existent models and hardware suggests fabrication, and the experimental results do not support the claimed level of improvement relative to top-tier models. Even if the core ideas have merit, the paper in its current form cannot be accepted.

MY FINAL SCORE: <score>1</score>  
MY FINAL DECISION: <decision>Reject</decision>
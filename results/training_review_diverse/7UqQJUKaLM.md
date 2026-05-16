Now I have a thorough understanding of the paper and can verify each reviewer claim. Let me produce the final consolidated review.

## Summary

The paper identifies a critical weak point in LLM evaluation pipelines — brittle RegEx-based key answer extraction — and proposes xFinder, a fine-tuned LLM that replaces RegEx for this task. The authors construct the KAF dataset (26,900 training / 4,961 test / 4,482 generalization samples) spanning four answer types (alphabet, short text, categorical, math) with responses from 10+ LLMs. Experiments show that even the smallest xFinder (0.5B parameters) achieves 93.42% extraction accuracy on held-out tasks vs. 74.38% for the best RegEx-based framework, and 97.61% judgment accuracy vs. 84.2% for GPT-4 — at 0.4% of the cost. The paper makes a well-supported case that improving the extraction module is a more reliable and cost-effective path to better evaluation than training full-scale judge models.

## Strengths

- **xFinder dramatically improves key-answer extraction accuracy over RegEx-based methods.** On the KAF generalization set (unseen tasks and models), xFinder-qwen1505 achieves 93.42% extraction accuracy, while the best RegEx-based framework (OpenCompass) reaches only 74.38% (Table 2). The gap is large and convincing across all four answer-type categories, especially on math where RegEx collapses to 4.87–51.37% while xFinder maintains 87.70–89.75%.

- **xFinder achieves higher judgment accuracy than both judge models and GPT-4 on the KAF generalization set.** With human-annotated ground truth, xFinder-llama38it reaches 97.61% judgment accuracy vs. GPT-4's 84.2%, JudgeLM-33B's 78.13%, and PandaLM's 51.9% (Table 3). This demonstrates that fixing extraction alone yields better overall evaluation reliability than full-fledged judge models trained for pairwise selection or scoring.

- **The paper quantitatively isolates the contribution of extraction errors to overall judgment unreliability.** Table 4 shows that RegEx-based frameworks have a gap of 14.32%–20.48% between extraction and judgment accuracy, whereas xFinder-llama38it reduces this gap to only 2.43%. This causal link — poor extraction inflates false judgments — is clearly demonstrated.

- **xFinder is highly efficient and cost-effective.** On a 200-sample evaluation, xFinder costs only $0.02 (~0.4% of GPT-4's cost) and runs in seconds vs. minutes for large judge models (Tables 5 & 6). This practical advantage makes reliable evaluation scalable.

- **The KAF dataset is a genuine resource contribution.** It is systematically constructed with semi-automated labeling (Self-Consistency with manual recheck), covers four task types from responses of 10+ LLMs across diverse prompt configurations, and includes separate test and generalization sets ensuring the generalization set uses entirely unseen tasks and models.

## Weaknesses

### Fatal
None.

### Major

- **The real-world evaluation (Section 5.3) demonstrates consistency between two xFinder variants but lacks ground-truth validation that xFinder's evaluations are actually more accurate than RegEx-based evaluations on these specific tasks.** The paper argues that "consistent rankings across different base models" plus "higher extraction accuracy on KAF" implies higher reliability in practice. However, without human-annotated ground truth for the 14 real-world tasks (or a representative subset), the reader cannot tell whether the consistent xFinder rankings are correct or merely consistently wrong. This gap weakens the real-world demonstration, though it does not undermine the core claims that are supported by the KAF experiments (which do have human ground truth).

### Minor

- **No confidence intervals or variance estimates are reported for any of the key accuracy results (Tables 1–4).** Given that differences between xFinder variants are often <0.5%, it is impossible to assess whether these differences are meaningful. Reporting bootstrapped confidence intervals or results across multiple fine-tuning seeds would strengthen the quantitative claims.

- **No inter-annotator agreement is reported for the human recheck of the KAF test and generalization sets.** The paper states "two rounds of manual labeling were conducted" but does not report agreement metrics (e.g., Cohen's κ), making it difficult to assess label quality.

- **The data augmentation techniques (Section 4.3) are not ablated.** The 50% option-alteration and 10% prompt-wrapping substitution are plausible choices, but their individual contributions to xFinder's generalization performance are unknown. An ablation would clarify what drives the gains.

- **The paper lacks a limitations section.** Notable omissions include: (a) xFinder is restricted to deterministic-answer tasks (multiple-choice, math) and does not apply to open-ended evaluation; (b) potential biases from the specific set of LLMs used for KAF response generation; (c) failure case analysis showing where xFinder still makes errors. Adding these would improve scientific integrity and help users calibrate their expectations.

- **The real-world evaluation (Section 5.3, Figure 4) relies on visual inspection of bump charts without rank correlation coefficients** (e.g., Spearman's ρ or Kendall's τ) to quantify ranking (in)consistency. Numerical measures would make the reliability comparison more rigorous.

- **The description of how RegEx baselines were applied to the KAF dataset is somewhat ambiguous.** The paper states it "set the mainstream frameworks with their RegEX extraction modules as baselines" but does not fully clarify whether RegEx patterns were applied post-hoc to the same fixed LLM responses or whether the frameworks' full pipelines (including their own prompting) were run, which would produce different LLM responses. The statement in Section 5.3 ("we replicated only the RegEx methods on each framework and ensured consistency in other settings") clarifies the intent for that section, but the earlier KAF experiments (Sections 5.1–5.2) would benefit from the same clarity.

### Trivial

- The claim of being "the first to conduct a systematic study" in reliable evaluation (Section 2) is somewhat overstated given prior work on judge models, EVOUNA, and the reliable evaluation concept itself (Augenstein et al., 2023). This is a minor framing issue that does not detract from the paper's actual contributions.

## Nice-to-Haves

- Human annotation of a subset of the 14 real-world tasks (e.g., 4 tasks × 100 samples each) to directly validate that xFinder's evaluations are more accurate than RegEx evaluations on actual benchmarks used by the community.
- Ablation study of the two data augmentation strategies to quantify their individual contributions.
- Rank correlation coefficients (Spearman's ρ) for the bump charts in Figure 4 to quantify ranking consistency numerically.
- Reporting of results across multiple random seeds or bootstrapped confidence intervals for the key accuracy numbers.

## Removed Points

These points are flagged for removal; treat them with caution.

- *"Overstated claim of being first systematic study"* — This is a minor framing issue. The paper's claim is qualified with "to the best of our knowledge," and the reviewer admits "this does not harm the paper." Moved from main weaknesses to here.
- *"Prompt engineering for judge models not discussed"* — The prompt templates for judge models are likely in the appendix (which the parser strips). Per policy, weaknesses about missing appendix content are removed.
- *"RQ3 supported only by a single example"* — The full RQ3 discussion is referenced as being in the appendix (which the parser strips); the in-text "(additional)" tag and appendix reference signal more content exists. Per policy, removed.
- *Some strength finder generic claims* — None present; all strength finder claims are specific and evidence-backed.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

- For a camera-ready version, add a limitations paragraph discussing xFinder's scope (deterministic-answer tasks only), potential biases in the KAF dataset, and representative failure cases.
- Add confidence intervals or bootstrapped variance estimates for the key accuracy comparisons in Tables 1–4.
- Clarify the baseline comparison methodology for Sections 5.1–5.2: explicitly state whether RegEx patterns were applied post-hoc to fixed KAF responses or whether the full framework pipelines were run separately.
- Consider annotating a small subset of the real-world tasks with human judgments to directly validate that xFinder's higher extraction accuracy translates into more accurate real-world evaluation rankings.

## Score and Decision

This paper makes a solid empirical contribution: it identifies a real problem in LLM evaluation (RegEx extraction failures), creates a dedicated dataset (KAF), and demonstrates that a small fine-tuned LLM (xFinder) dramatically outperforms both RegEx methods and larger judge models on extraction and judgment accuracy. The core claims are well-supported by controlled experiments with human-annotated ground truth on a held-out generalization set. The main weakness is that the real-world evaluation (Section 5.3) does not validate xFinder's accuracy directly — it only shows consistency between two xFinder variants — but this does not invalidate the paper's central contribution, which rests on the KAF experiments. The missing limitations section, variance estimates, and ablation studies are addressable weaknesses rather than structural flaws.

**Originality:** Good — replacing RegEx with a small fine-tuned LLM for answer extraction is a straightforward but effective idea.
**Quality:** Strong empirical methodology on the KAF dataset; the real-world evaluation is weaker.
**Clarity:** Well-written with clear problem definition, methodology, and results presentation.
**Significance:** The paper addresses a practical problem affecting virtually all LLM evaluation pipelines; the findings are actionable.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>
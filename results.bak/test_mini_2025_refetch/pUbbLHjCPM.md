Now I have sufficient context for calibration. Let me synthesize the review.

**Round 1 bracket:** The paper sits in the middle band (roughly 4–6.5), not in the weak band (<3.5, withdrawn/rejected with severe flaws) nor the strong band (>7.5, oral/strong accept).

**Round 2 narrowing:** Compared to the 5.60 anchor ("Weak to Strong Generalization") — accepted but with notable gaps similar to this paper — PTR has broader task coverage and tests on 2 model families, but has more underspecified methodology and weaker statistical reporting. Compared to the 5.00 anchor ("Self-rationalization") — rejected — PTR is clearly stronger. Compared to the 6.50 anchor ("Progress or Regress") — accepted — PTR has less rigorous evaluation. This places PTR in the 4.5–5.5 range.

**Final score: 5.0** — The core idea has merit but the experimental validation has significant gaps (underspecified method, no variance, weak open-ended evaluation) that prevent acceptance in current form.

Here is the consolidated review:

---

## Summary

PTR (Progressive Thought Refinement) introduces a two-stage framework for teaching LLMs to iteratively improve their own responses without external feedback or task-specific supervision. In stage one, a weak model generates initial thought sequences and a strong model produces refined answers, using collaborative selection and consistency filtering to build a high-quality refinement dataset. In stage two, a weighted thought-mask fine-tuning objective trains the model to produce better responses over successive iterations. Evaluated on ten diverse tasks across two model families (Qwen2-7B and Llama3-8B), PTR achieves average gains of ~3.9% (from 49.6% to 53.5%) with iterative refinement, while prompting-based and instruction-fine-tuning baselines degrade.

## Strengths

- **Weak-strong model collaborative selection for dataset construction (Section 3.1.2):** The paper introduces a principled strategy for selecting weak and strong model pairs (based on parameter count, version, and domain specialization) and validates significant performance differences via Wilcoxon tests (Appendix B.5). This avoids reliance on ground-truth labels or external feedback, directly addressing a key limitation of prior work that requires explicit supervision signals.

- **Generalization across ten diverse tasks without task-specific fine-tuning (Table 1, Section 4):** PTR improves average accuracy from 49.6% to 53.5% (Qwen2-7B) and from 55.8% to 58.6% (Llama3-8B) across tasks spanning knowledge reasoning (MMLU), code (HumanEval), math (GSM8K, MATH), comprehension (DROP), summarization (XSum), and complex reasoning (ARC, GPQA). The improvement spans multiple domains, showing that the model learns a general refinement capability rather than domain-specific tricks.

- **Robustness across prompts and model families (Table 2, Section 4.3):** PTR maintains iterative improvement across three different refinement prompts (e.g., GSM8K accuracy rises from ~75% to ~78–79% across all prompts) and works comparably on both Qwen2-7B and Llama3-8B, demonstrating the method is not brittle to instruction phrasing or architecture choice.

## Weaknesses

### Fatal

None.

### Major

- **Underspecified thought-mask mechanism and loss function (Section 3.2, Equation 3.4).** The paper states that the thought mask "calculates the loss based only on the accuracy of the refined final answer," yet Equation (3.4) includes two additional terms that depend on *all* thought steps: a consistency term (λ₂) across sequential thought steps and a confidence term (λ₃) over each individual step. The paper never specifies which tokens are actually masked during training, how the mask interacts with the three loss terms, or whether the λ₂/λ₃ terms are computed inside or outside the masked region. The text describing the loss as "emphasizing both the accuracy of the final answers and the logical consistency of the thought process" suggests the mask is not truly selective. This ambiguity makes the training objective impossible to replicate or fully evaluate without guessing at the implementation. Given that the thought-mask mechanism is the paper's primary methodological contribution, this is a critical gap.

- **Missing statistical significance for main results (Table 1, Table 2).** All reported results are single numbers with no confidence intervals, standard deviations, or multiple-seed averages. Given that many improvements are modest (~2–7% absolute) and some tasks show very small changes (e.g., GPQA from 23.2 to 25.6), it is impossible to determine whether these gains are statistically reliable. The Wilcoxon test mentioned in Appendix B.5 is about weak/strong model selection, not about the main results. Without variance estimates, the core empirical claims are under-supported.

- **Insufficient evaluation of open-ended tasks (Section 4.1, Figure 2).** The claim that PTR achieves "refinement beyond correction" — improving response quality beyond accuracy — is supported only by a single qualitative code example (Figure 2) and BGE-m3 similarity scores for XSum summarization. Similarity is a weak proxy for summary quality; standard metrics like ROUGE, BERTScore, or human evaluation are needed. The code example shows added error handling, which is a form of correctness improvement rather than evidence of "beyond correction." Without quantitative evidence on open-ended quality (human preference, factuality, coherence, or functional correctness of code beyond pass@1), this claim remains unsupported.

### Minor

- **Missing standard SFT baseline on the original WizardLM dataset.** The IFT baseline is trained on strong-model outputs from the PTR dataset, which already includes the refinement structure. A standard SFT baseline on the original WizardLM dataset (without the weak-strong refinement pipeline) would help isolate whether PTR's improvements come from the refinement training objective, the quality of strong-model outputs, or simply the additional 40k training examples. This would strengthen the paper's claim that PTR "teaches how to improve rather than what is correct."

- **Initial-iteration performance degradation not fully discussed.** PTR Iter.1 (after fine-tuning) underperforms the base model's first attempt on several tasks (e.g., Qwen2: PTR Iter.1 DROP 19.0 vs Base Prompt 20.9; XSum 45.9 vs 47.3). While the paper acknowledges this trade-off, the potential implications — that fine-tuning for refinement may harm standalone output quality — are not explored or discussed in the conclusion.

- **"Progress or Regress? Self-Improvement Reversal in Post-training" (avg 6.5, accepted poster):** More rigorous evaluation with variance reporting and broader metrics; PTR is weaker experimentally.
- **"Convergence Towards Stable Intrinsic Self-correction" (avg 5.4, rejected):** Had theoretical grounding but suffered from single-model evaluation and missing significance tests; PTR is comparable or slightly stronger in evaluation breadth.
- **"RAIN: Your Language Models Can Align Themselves without Finetuning" (avg 6.0, accepted poster):** Had clear method specification and human evaluation; PTR has a stronger dataset construction pipeline but weaker evaluation rigor.
- **"Weak to Strong Generalization for Multi-capabilities" (avg 5.6, accepted poster):** Similar topic (weak/strong models), similar issues with underspecified components; PTR has broader task coverage but comparable methodological gaps.
- **"Smaller, Weaker, Yet Better" (avg 7.0, accepted poster):** Rigorous compute-optimal analysis with clear comparisons; PTR is substantially less rigorous in experimental design.
- **"Self-rationalization improves LLM as judge" (avg 5.0, rejected):** Had iterative improvement mechanism but rejected for insufficient validation; PTR is somewhat stronger.

**Round-1 bracket:** 4–6.5 (between weak band <3.5 and strong band >7.5).

**Round-2 narrowing:** Compared to the 5.6 anchor (accepted but with gaps) and the 5.0 anchor (rejected), PTR sits at the boundary. It has broader task coverage than most comparable papers but is held back by underspecified methodology and weak statistical evidence.

**Final score: 5.0** — The core idea has merit, but the experimental validation has significant gaps that prevent acceptance in current form.
## Summary

EfficientQAT proposes a two-phase quantization-aware training framework for LLMs: **Block-AP** (block-wise training of *all* parameters — weights, step sizes, zero points) followed by **E2E-QP** (end-to-end training of only step sizes). The key practical claim is that this makes full QAT feasible for models up to 70B parameters on a single A100-80GB GPU (41 hours for Llama-2-70B at 2-bit), while outperforming prior uniform PTQ methods and matching vector quantization accuracy at 2-bit with hardware-friendly uniform quantization.

---

## Strengths

1. **Block-AP empirically outperforms prior partial-training variants.** The ablation (Table~\ref{tab:ptq_variants_comparisons}) directly compares training all parameters ($W$, $s$, $z$) against training only rounding parameters, clipping thresholds, or step sizes. The full-training strategy wins, and it does so with *less* memory than approaches requiring additional rounding-parameter copies. This is a clean empirical finding that validates the core design choice.

2. **Pushes uniform quantization to compete with vector quantization at 2-bit.** At 2-bit, EfficientQAT outperforms AutoRound by ~5% zero-shot accuracy on Llama-2-7B and exceeds AQLM (2×8 codebook). Though AQLM (1×16) and QuIP# score slightly higher, those methods introduce computational overhead that can reduce inference speed (Section 4.1, lines 120–121). EfficientQAT achieves competitive accuracy using hardware-friendly uniform quantization, which is a genuine practical contribution.

3. **Dramatic reduction in training resources.** Quantizing Llama-2-70B at 2-bit on a single A100-80GB in 41 hours (Table~\ref{tab:training_cost}) — 14% of AQLM's training time and 50% of DB-LLM's — while competing methods require 4+ GPUs for the same scale. E2E-QP for Llama-2-70B at 2-bit uses only 34.2 GB of memory (line 103). These numbers make QAT practical at scales previously infeasible.

4. **Principled engineering decisions backed by ablation.** The choice to train only $s$ (not $z$) in E2E-QP is justified by ablation (Table~\ref{tab:e2e-ft-variants}) showing similar performance but lower bit-width overhead when $z$ remains in low-bit format. The sample-size analysis (Figure~\ref{fig:train_val_loss}) shows the train-validation gap shrinking from 1.07 to 0.06 as training samples increase, providing concrete guidance. These ablations demonstrate methodological rigor.

5. **Consistent improvements across settings and model families.** Results are reported for Llama-1, Llama-2, and Llama-3 from 7B to 70B, across base quantization, instruction-tuning, and (in appendix) multimodal settings, against PTQ, QAT, and Q-PEFT baselines. The advantage is not confined to a single benchmark or configuration.

---

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Conceptual novelty is limited.** The paper frames Block-AP as "the first to enable direct training of all parameters in a block-wise manner" (line 28), which is technically accurate but describes a small design shift from prior block-wise methods (BRECQ, OmniQuant, AutoRound, CBQ) — those trained subsets like rounding parameters or clipping thresholds, while Block-AP trains $W$, $s$, and $z$ together. No principled argument is offered for *why* full training works better beyond the trivial observation that a larger search space can contain better solutions. Similarly, E2E-QP closely resembles PEQA (step-size fine-tuning) with the key difference being Block-AP initialization rather than RTN. The paper's contribution is primarily an *empirical* finding (full training > partial training during block-wise reconstruction) and a well-engineered combination of existing ideas, not a conceptual advance. This does not invalidate the paper — the practical results are real — but it limits the paper's strength for a top venue.

2. **Base quantization evaluation is narrow for the breadth of claims made.** The paper claims superiority "over the full landscape of PTQ, QAT, and Q-PEFT methods" but evaluates base quantization on only 5 commonsense QA tasks (WinoGrande, PIQA, HellaSwag, Arc-Easy, Arc-Challenge) and perplexity on WikiText2 and C4. While this follows the evaluation protocol of prior quantization papers (GPTQ, OmniQuant), the scope of the claim is broader than the evidence. Including MMLU or a reasoning benchmark (GSM8K) in the *base quantization* setting (not just instruction tuning) would strengthen confidence that the method preserves model capabilities beyond next-token prediction.

3. **No Llama-3 results at 3-bit or 4-bit.** Llama-3 results are only shown at 2-bit (w2g128) in the QAT comparison. Given that Llama-3 is a more modern family and the paper claims consistent advantage across bit widths, the absence of 3/4-bit Llama-3 results leaves a gap in the evidence.

4. **Instruction-tuning evaluation uses only MMLU (5-shot).** The instruction-tuning experiments (Section 4.2) evaluate only MMLU accuracy following prior work protocols (QA-LoRA, IR-QLoRA). However, instruction tuning is expected to improve generation quality and instruction following; evaluating on a generation benchmark (MT-Bench, AlpacaEval) would provide a more complete picture of the method's effectiveness in this scenario.

### Trivial
- The gradient expression in line 101 ($\frac{\partial \widehat{w}}{\partial s} = w_q - z$) implicitly uses a straight-through estimator for the quantization operation. While practitioners will recognize this, explicitly stating STE would improve precision.

---

## Nice-to-Haves
- Variance or error bars across runs would strengthen confidence in the results, though single-run evaluations are standard in this subfield.
- The paper could more clearly delineate cases where Block-AP initialization is critical vs. where RTN + E2E-QP would suffice — the ablation partially addresses this but unpacking the *why* would sharpen the contribution.

---

## Removed Points

These points were considered but removed with justification:

1. **"Comparison against PTQ methods flattens the efficiency-quality trade-off"** — REMOVED. The paper reports training cost alongside accuracy (Section 4.4, Table~\ref{tab:training_cost}), and comparing across paradigms is standard practice. The paper does not claim to match PTQ methods on compute — it claims better accuracy at low bits, which is a legitimate comparison. The critic's concern is addressed by what is already in the paper.

2. **"Missing multimodal evaluation in main paper"** — REMOVED per instructions: appendix content is stripped by the parser and exists in the original submission.

3. **"Very little data for training all parameters (raising overfitting concerns)"** — REMOVED. The paper directly addresses this in the ablation (Figure~\ref{fig:train_val_loss}, line 147), showing the train-validation gap shrinks with more data and that 4096 samples is a reasonable trade-off. The concern is preemptively answered.

4. **"Inference speed-up claims are inherited from the toolbox"** — REMOVED. The paper does not claim the speedup as its own invention; it attributes it to toolboxes (line 160: "Due to the leverage of standard uniform quantization, the quantized models of EfficientQAT can also achieve speedup through a lot of toolboxes"). This is correctly positioned as a benefit of uniform quantization, not a novel contribution.

5. **"No explicit STE mention"** — DEMOTED from the critic's method-section concern to Trivial. The gradient computation implicitly uses STE, and the description is sufficient for practitioners.

6. **"No statistical significance/variance reporting"** — MOVED to Nice-to-Have. Single-run evaluation is the norm in LLM quantization papers; demanding variance bars would hold this paper to a non-standard.

---

## Novel Insights

None beyond the paper's own contributions. The reviews surface the tension between the paper's strong empirical results and its limited conceptual novelty, but this is a framing observation, not a novel scientific insight. The merged review confirms that the paper's main value is a well-executed practical pipeline whose individual components are not conceptually novel.

---

## Suggestions

- **Broaden the base-quantization evaluation** to include at least one multitask benchmark (MMLU without instruction tuning) or a reasoning benchmark (GSM8K). This would better support the claim of superiority over the "full landscape" of quantization methods.
- **Add Llama-3 results at 3-bit and 4-bit** to demonstrate consistent advantage across all bit widths on modern model families.
- **Include a generation-based evaluation** (e.g., MT-Bench) for the instruction-tuning scenario to show the method preserves generation quality, not just factual knowledge.
- **Tone down the novelty framing** to match the contribution. The paper is strongest when positioned as a practical, efficient QAT pipeline validated by thorough experiments, rather than as a conceptual breakthrough. The phrase "to the best of our knowledge, Block-AP is the first" is defensible but invites scrutiny that the paper's main value does not rest on.

---

## Score and Decision

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>
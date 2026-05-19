Now I have all the information needed. Let me write the final consolidated review.

---

## Summary

This paper studies cross-prompt transferability in adversarial attacks on Vision Language Models (VLMs). It identifies a "non-stationary phenomenon" where attack success fluctuates during multi-prompt optimization, attributes this to overfitting, and proposes GrCPA — a method that zeros the *k* largest and smallest gradient values in the Attention and MLP blocks of the LLM during backpropagation. Experiments are reported on Flamingo, BLIP-2, LLaVA-1.5, and InstructBLIP with multiple task types and target answers.

## Strengths

1. **Problem diagnosis is clearly motivated.** The paper identifies a real practical issue — cross-prompt brittleness in VLM adversarial attacks — and provides evidence of the non-stationary phenomenon during optimization (Figure 1). It also tests and reports that single-modal transferability methods (MI-FGSM, Input Diversity, Variance Tuning) are ineffective or harmful for this setting (Section 1), which is a useful negative result.

2. **Simple, computationally lightweight method.** GrCPA's gradient regularization — zeroing the *k* extreme gradient values per token — modifies only a small fraction of gradients and does not change the optimization objective or architecture. This is a principled approach that is easy to implement on top of existing attacks (Section 3.3).

3. **Multi-model evaluation across diverse architectures.** The paper evaluates on four distinct VLMs (Flamingo, BLIP-2, LLaVA-1.5, InstructBLIP) covering different model families, showing the method is not architecture-specific (Section 4.1).

4. **Ablation studies isolate key design choices.** Table 5 (regularizing different modalities) shows that dual-modal regularization is necessary, and Table 6 (varying λ) tests the proportion of Transformer blocks to regularize, supporting the claim that high-level layer regularization is most effective.

## Weaknesses

### Fatal
None.

### Major

1. **Attack Success Rate (ASR) is never defined.** The paper reports ASR throughout (Tables 1–6, Figure 3) and states only "we report the Attack Success Rate (ASR) and facilitate the analysis by inducing the model to output specific text" (line 143). It does not specify whether success requires exact string match of the target answer, substring match, or semantic equivalence. This makes all quantitative results uninterpretable — a difference of 10 percentage points could reflect a brittle threshold artifact rather than a genuine improvement. This is a basic experimental reporting requirement for targeted attack papers.

2. **Method specification is ambiguous about which gradients are clipped.** The paper defines the gradient vector G ∈ ℝ^d "with respect to visual or textual tokens" (line 108) and says clipping is performed "on each token in both the Attention block and the MLP block" (line 114). However, it does not clarify whether G is the gradient of the loss with respect to the *token embeddings/activations* (intermediate feature maps) or with respect to the *Attention/MLP weights*. These are fundamentally different operations. The reference to "preserving low-level features" (line 116) and the analogy to Deng et al. (2023) on CNN feature maps suggest the former, but the paper should state this explicitly. Without this, the method cannot be reproduced.

3. **No ablation on the critical hyperparameter k.** The paper sets *k*=1 (line 141) but never tests *k*=0 (equivalent to no regularization), 2, 5, 10, or any other value. Since the entire method is zeroing the *k* extreme gradient values, the sensitivity of results to this parameter is essential information. A method that only works at a specific *k* value is fundamentally different from one that is robust across a range.

4. **No comparison to simpler regularization alternatives.** The core intuition is that large gradients cause overfitting. The paper never tests whether this specific form of gradient regularization outperforms simpler alternatives such as: gradient L2 norm clipping, gradient noise injection, or early stopping. Given the claim that existing methods (MI-FGSM, DIM, Variance Tuning) do not help, a direct comparison to PGD with these simple regularizers is needed to demonstrate that the specific *k*-extreme-zeroing mechanism, rather than *any* gradient smoothing, is responsible for the improvement.

### Minor

1. **CroPA's role in the comparison is ambiguous.** The paper identifies CroPA as the closest prior work (line 47) and calls GrCPA "orthogonal" to it (line 104), but the text describing Table 1 says "GrCPA outperforms previous SOTA methods" without explicitly listing which methods are compared. The prose discusses "both the baseline methods and our method" (line 156) without naming the baselines. This ambiguity could be resolved with a single sentence clarifying whether CroPA is included in every comparison.

2. **The LLaVA-1.5 experiments are reported incompletely.** Line 158 states "we also conduct experiments on LLaVA-1.5... but find weak transferability" with garbled/truncated text. If LLaVA was used only for validation and the results showed weak transferability, this should be stated transparently in a dedicated subsection with numbers, not as a fragmentary sentence. As written, it raises questions about whether the paper's claims are fully supported.

3. **Stability analysis (Table 2) uses only 5 checkpoints.** The method evaluates consistency across iterations 900, 925, 950, 975, and 1000. While this provides some signal, it captures only 5% of the final 100 iterations and says nothing about the full 1000-iteration trajectory. A more informative metric would be the variance of ASR or the oscillation frequency across the entire run.

4. **The "first to identify non-stationarity" claim is overstated.** CroPA (Luo et al., 2024a) already addressed cross-prompt brittleness in VLM attacks, and the non-stationary phenomenon is a natural property of adversarial optimization over multiple objectives. The paper does not formalize non-stationarity (e.g., with a variance measure over iterations), so the claim is more qualitative than stated.

5. **No discussion of limitations.** The paper does not acknowledge its white-box assumption, restriction to L∞ perturbations, the need for up to 100 prompts, or the focus on a single target answer per attack. These are standard scope boundaries but should be stated explicitly for practical interpretation.

### Trivial
- Some numerical values in the prose are given as isolated decimals (e.g., 0.34, 0.71) without stating which baseline method they correspond to (line 169).

## Nice-to-Haves
- Ablation on the extreme-count hyperparameter *k* would directly address the core weakness about the method's sensitivity.
- Reporting ASR with standard deviations or error bars across multiple runs would strengthen the empirical claims.
- A comparison against PGD with L2 gradient norm clipping would isolate the benefit of the specific regularization mechanism.
- Code release would significantly aid reproducibility.

## Removed Points

These points appeared in the reviews but were removed or demoted after verification against the paper:

- *"Tables are unrenderable image placeholders — no concrete numbers are given"* — **Removed** (parser issue). The tables would render in the original PDF. However, the underlying concern about missing confidence intervals and statistical details is partially retained in Minor #3 and Nice-to-Haves.

- *"Those methods [MI-FGSM, DIM, VT] are not included in the main comparisons — unfair comparison"* — **Removed**. The paper explicitly tests them and reports they decreased performance (line 30). Excluding methods that harm performance from the main comparison table is standard and appropriate. The asymmetry (if any) favors the baseline, not the author's method.

- *"Algorithm 1 is missing from extracted text"* — **Removed** (parser issue). Algorithms in the PDF are stripped by the text extractor.

- *"Missing related works"* — **Removed** per policy (cannot verify external references).

- *"No code or link is provided"* — **Removed** per policy (reproducibility concerns about code release are not valid weaknesses; the paper states all data is open-source).

- *"The evaluation is not comprehensive (only 1 dataset)"* — **Weakened**. The paper uses MS-COCO images with multiple prompt types (VQA-general, VQA-specific, classification, captioning). This is one image source but multiple task settings, which is reasonable for an attack paper. Not retained as a standalone weakness.

- *Strength Finder's claim about "Consistent outperformance across models and tasks"* — **Kept but qualified** by the Major weakness about undefined ASR metric. Without knowing how ASR is measured, the outperformance cannot be fully assessed.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a pattern of ambiguity in experimental reporting (undefined metric, underspecified method, incomplete baseline description) that is common in papers where the core idea is reasonable but the write-up does not provide enough detail for independent verification. This is not a specific novel insight but a cross-cutting characterization of the paper's main shortcoming.

## Suggestions

1. **(Critical)** Define ASR precisely: state whether it is exact string match, substring match, or semantic equivalence, and provide examples of what counts as success and failure.
2. **(Critical)** Clarify which gradients are being zeroed — gradient of the loss with respect to token *embeddings/activations*, or with respect to the *weights* of Attention/MLP layers. The paper must state this explicitly for reproducibility.
3. **Add ablation on k** (number of extreme gradients zeroed). Test k=0, 1, 2, 5, 10, and optionally as a fraction of the embedding dimension, to show sensitivity.
4. **Add a comparison to PGD with L2 gradient norm clipping** (or gradient noise injection) to demonstrate that the specific *k*-extreme-zeroing mechanism is necessary, not just any gradient smoothing.
5. **Clarify whether CroPA is included in every comparison** with a single explicit sentence (e.g., "In all tables, the baselines compared are Single-P, Multi-P, and CroPA").
6. **Fix the garbled LLaVA discussion** — either provide LLaVA results in a table or acknowledge that the method's transferability to LLaVA was limited and discuss why.

## Score and Decision

**Calibration anchors:**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| /home/wg25r/split_review/datasets/ai_review_cal/ywgwArtbDq.md | 3.00 | 1 (weak) | Geometric mask paper — similar score range, less method contribution but cleaner experiments |
| /home/wg25r/split_review/datasets/ai_review_cal/OE67D1Oatr.md | 3.00 | 1 (weak) | Backdoor attack — less clear contribution, comparable experimental gaps |
| /home/wg25r/split_review/datasets/ai_review_cal/S5JCqTJyKj.md | 3.00 | 1 (weak) | DABF backdoor — similar level of experimental incompleteness |
| /home/wg25r/split_review/datasets/ai_review_cal/ZbOSRZ0JXH.md | 3.00 | 1 (weak) | LLM domain extrapolation — better experimental control but similar overall score |
| /home/wg25r/split_review/datasets/ai_review_cal/10kBEqYKKN.md | 3.00 | 1 (weak) | Prompt geometry — systematic evaluation, clearer contributions |
| /home/wg25r/split_review/datasets/ai_review_cal/vF4RhEPGtb.md | 4.25 | 1 (middle) | TATM — similar topic (MLLM adversarial transferability), much more extensive evaluation (13 models, 9 baselines), better experimental rigor |
| /home/wg25r/split_review/datasets/ai_review_cal/iR5qF9N1Ge.md | 5.80 | 1 (middle) | MAA — far stronger empirical evaluation, proper ablations, consistent large margins |
| /home/wg25r/split_review/datasets/ai_review_cal/7OO8tTOgh4.md | 5.25 | 1 (middle) | MIE (VLM attack) — better ablation structure, clearer method specification |
| /home/wg25r/split_review/datasets/ai_review_cal/sbiU3WZpTp.md | 5.33 | 1 (middle) | LDM robustness — systematic module-level evaluation, more thorough |
| /home/wg25r/split_review/datasets/ai_review_cal/PdA9HAxO4w.md | 5.00 | 1 (middle) | C-PGC — broader VLP model evaluation, better experimental design |
| /home/wg25r/split_review/datasets/ai_review_cal/JnRvQ8CxLx.md | 4.00 | 2 (narrow) | IDEATOR — strong empirical support (94% ASR), clearer evaluation with identified limitations |
| /home/wg25r/split_review/datasets/ai_review_cal/04TRw4pYSV.md | 3.50 | 2 (narrow) | ModalPrompt — similar score, no major experimental gaps (only minor issues) |
| /home/wg25r/split_review/datasets/ai_review_cal/cP2W2PJtBj.md | 3.67 | 2 (narrow) | AntifakePrompt — stronger evaluation on 23 datasets, minor experimental issues |
| /home/wg25r/split_review/datasets/ai_review_cal/2yqAzFPT4F.md | 5.25 | 2 (narrow) | Zer0-Jack — strong empirical results with clear method, better experimental rigor |

**Round 1 bracket:** Plausible range 3.0–5.5, with the paper clearly below the MAA (5.80) and MIE (5.25) anchors on experimental rigor.

**Round 2 narrowing:** The paper is weaker than TATM (4.25) which has dramatically more extensive evaluation despite some metric concerns. It is weaker than IDEATOR (4.00) which has clean empirical validation of its core claims. The paper is comparable to ModalPrompt (3.50) in overall quality but with more serious experimental gaps (ModalPrompt's weaknesses were all addressable minor issues). GrCPA's undefined ASR metric and ambiguous gradient specification are genuine barriers to evaluation that go beyond the minor issues in the 3.50–4.00 anchors.

**Final score: 3.5.** The paper identifies a real problem and proposes a plausible solution, but the experimental presentation has too many gaps (undefined evaluation metric, ambiguous method specification, missing critical ablations) to support its claims at a level sufficient for publication. A substantially revised version addressing these issues could potentially reach the 5+ range.

MY FINAL SCORE: <score>3.5</score>
MY FINAL DECISION: <decision>Reject</decision>
- Decision: Reject
- Avg Score: 5.75
- Scores: 6, 5, 6, 6
Here is my consolidated review.

## Summary
This paper identifies "multilingual erosion" in MLLMs — the phenomenon where visual instruction tuning with English-centric data degrades non-English performance — and proposes Parrot, a method that uses cross-attention between visual features and text embeddings to drive a Mixture-of-Experts (MoE) module that converts English-biased visual tokens into language-specific ones. It also introduces MMMB, a new multilingual multimodal benchmark covering 6 languages and 12K questions. Experiments show Parrot-14B achieving SOTA on multilingual MMBench and MMMB, with particularly large absolute gains in Arabic, Turkish, and Russian (10+ points over LLaVA-NeXT), while using minimal non-English training data (~10K samples per language).

## Strengths
1. **Well-motivated, empirically grounded problem.** The pilot study (Section 4.2) concretely demonstrates multilingual erosion by comparing OpenAI-CLIP vs. Chinese-CLIP backbones on Chinese inputs, showing measurable improvements (MMBench-CN: 66.4→68.3, MMMB-zh: 62.4→66.1) from simply switching to a language-aligned vision encoder. This grounds the paper's central hypothesis in data rather than speculation.

2. **Clean, lightweight architecture for language-level visual alignment.** The design is principled and minimal: cross-attention (Eq. 1) using the [CLS] token as query against textual embeddings provides language-conditioned routing signals, and the MoE module (Eq. 2–4) converts English-biased visual tokens into language-specific ones. The residual connection (Eq. 5, `\alpha`-weighted) preserves original visual-semantic information. The architecture adds negligible overhead and enables training in 21 hours on 16×A100 GPUs.

3. **State-of-the-art multilingual results with dramatic data efficiency.** Table 1 shows Parrot-14B achieves best or second-best accuracy across all six languages on both MMMB and MMBench, outperforming LLaVA-NeXT-13B by large margins in Arabic (68.13 vs 45.36) and Turkish (64.33 vs 53.09). This is achieved with only ~12–17K non-English training samples per language (Table 0), directly supporting the claim that the MoE module efficiently aligns visual tokens to language-level inputs.

4. **Construction of MMMB benchmark addressing key gaps.** Section 3 identifies concrete limitations in existing multilingual benchmarks (outdated content, GPT-4-dependent evaluation, inconsistent cross-language samples, limited languages) and designs MMMB with six diverse language families, medium-difficulty problems, content consistency across languages, and a circular Yes/No evaluation strategy that reduces guessing bias. This fills a real need.

5. **Incremental data ablation demonstrates scalability without catastrophic forgetting.** Table 2 shows that adding each language's dataset (zh, pt, ar, tr, ru) incrementally improves performance in the corresponding language (e.g., Turkish from 52.1→59.7) while English remains stable (69.4–71.1). This validates that the MoE module can incorporate new languages without degrading existing ones.

## Weaknesses

### Fatal
None.

### Major
1. **Headline results do not isolate the LLM backbone from the proposed method.** The main comparison (Table 1) contrasts Parrot (Qwen1.5-7B/14B) against models using Vicuna, LLaMA-2, or older Qwen backbones. Qwen1.5 is known to have substantially stronger multilingual text-only capabilities than Vicuna or LLaMA-2, meaning the large gains in Arabic, Turkish, and Russian could partly stem from the backbone change rather than the MoE module. The ablation in Figure 3 (left) *attempts* to control for this by comparing: (baseline) → (+multilingual data) → (+MoE) — presumably all using Qwen1.5-7B — but (a) the paper never explicitly states that the baseline in that ablation uses Qwen1.5-7B, (b) the bar chart has no numeric labels, and (c) precise per-condition numbers are not reported in a table. This makes it impossible for readers to verify the magnitude of the MoE contribution. **Why it matters:** The paper's central claim is that the *MoE routing module* drives the improvements. Without a clean table showing (i) Qwen1.5 + standard MLP projector + English-only data, (ii) same + multilingual data, (iii) full Parrot, the contribution of the MoE module over simply using a stronger multilingual backbone remains unquantified.

2. **MMMB benchmark translation quality is not validated.** The paper describes translation for *training data* (GPT-4 + manual calibration, line 186) and for the MMBench extension ("translation via GPT-4, followed by manual verification," line 202), but does not clarify the translation process for the MMMB benchmark questions themselves. Since MMMB is constructed by selecting questions from ScienceQA, MME, and SEED-Bench (English-origin datasets) and covering six languages, the questions must have been translated. No human evaluation of translation fidelity (e.g., native-speaker verification of a sample) is reported. Without evidence that answer correctness and language-specific nuance are preserved across languages, the benchmark's core criterion of "content consistency across languages" (Section 3.2) is asserted but not confirmed. **Why it matters:** MMMB is a claimed contribution of the paper. If translation quality varies across languages, model ranking differences could reflect translation artifacts rather than genuine multilingual capability.

### Minor
1. **Broken cross-references.** The paper references "Figure~\ref{tab:llava-bench}" (line 208) and "Table~\ref{tab:ablation-mono}" (line 315), neither of which exists in the paper. The claim about "using less than 1% of the data compared to other multilingual MLLMs" (line 208) is left unsupported without a functioning reference.

2. **Ablation bar chart (Figure 3, left) lacks numeric labels.** The ablation comparing baseline vs. +multilingual data vs. +MoE is presented only as a bar chart without a labeled y-axis or numerical values. This undermines a key piece of evidence for the MoE module's effectiveness. The authors should report these numbers in a table.

3. **Expert routing analysis shown only for Chinese prompts.** Figure 3 (right) visualizes expert activation distributions for Chinese only. Showing this for all six languages would strengthen the claim that the router learns language-specialized representations rather than a single fixed pattern.

4. **No variance or confidence intervals reported.** Table 1 and Table 2 report single accuracy values with no indication of whether results are from a single run or multiple runs. Given the 2,000-question size of MMMB per language, binomial confidence intervals or mention of run count would help assess reliability.

5. **The baseline "LLaVA-1.5-finetune" row in Table 2 is ambiguous.** It is not explicitly stated whether this row uses Qwen1.5-7B (the paper's 7B backbone) with the full Parrot architecture (including MoE) trained only on English data, or a standard LLaVA-like MLP projector without MoE. The context suggests the former, but the ambiguity should be resolved.

### Trivial
- The radar chart in Figure 3 (middle) has no numeric labels, limiting its informativeness.

## Nice-to-Haves
- A brief analysis of failure cases (e.g., where Parrot confuses languages or reverts to English) would strengthen the evaluation.
- An ablation on the router input representation (using all patch tokens vs. [CLS] token only) would further justify the design choice, though the current choice is reasonable.
- Reporting both raw multiple-choice accuracy and circular Yes/No accuracy on MMMB would clarify the effect of the evaluation strategy.

## Removed Points
*These points were flagged during the review process but are removed (with justification) to avoid inflating the weakness count.*

- **"Missing comparison with Vicuna backbone"** — The critic suggests running Parrot with Vicuna as the LLM backbone to separate backbone from method. However, the paper's ablation (Figure 3, left) already controls for backbone by comparing across conditions within the same backbone (presumably Qwen1.5-7B). The paper's contribution is the architecture, not the backbone choice, and requiring a Vicuna variant is scope creep beyond what is needed to validate the method.
- **"Circular evaluation strategy doubles the penalty for small errors"** — This is a design trade-off, not a flaw. The paper explicitly motivates the strategy as reducing random guessing and choice bias (Section 3.3). The critic's concern is speculative and does not identify a concrete problem with the evaluation.
- **"Cross-attention should justify using [CLS] token vs. alternatives"** — The critic acknowledges this is a minor design decision. The paper's cross-attention mechanism is clearly described and the choice is reasonable; an ablation would be nice-to-have but not a weakness.
- **"Unfair comparison with baselines"** — Per the review guidelines, criticism about unfair comparisons is removed when the asymmetry favors the baseline, not the author's method. In Table 1, all comparisons use the same evaluation framework (VLMEvalKit) with consistent settings, and the paper's models are compared fairly against the reported baselines.

## Novel Insights
None beyond the paper's own contributions. The reviews did not surface any unexpected patterns, contradictions, or insights that the paper itself does not already articulate.

## Suggestions
1. **Add a controlled ablation table** that isolates the MoE contribution: report precise numerical results for (a) Qwen1.5-7B + standard MLP projector + English-only Stage 2 data, (b) same + multilingual Stage 2 data, (c) full Parrot (MoE) with the same multilingual data. Place this in the main paper, not just as a bar chart.
2. **Document the MMMB translation process** explicitly and include a small human evaluation study (e.g., "native speakers of each language verified 50 randomly sampled questions; GPT-4 translation preserved answer correctness in ≥95% of cases").
3. **Fix the broken cross-references** (tab:llava-bench, tab:ablation-mono) and add the supporting data/table that was intended to accompany the "less than 1% of data" claim.
4. **Add variance information** — at minimum note whether results are from a single run or averaged, and add binomial confidence intervals for MMMB results.
5. **Show expert routing distributions for all six languages** (not just Chinese) to demonstrate language-specialized behavior more comprehensively.

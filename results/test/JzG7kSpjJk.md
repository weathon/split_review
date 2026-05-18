Now I have a thorough understanding of the paper. Let me produce the final consolidated review.

## Summary

This paper proposes per-input-channel (per-IC) quantization for weight-only LLM quantization, where quantization groups are formed along the input channel dimension rather than the conventional output channel dimension. The key insight is that activation outliers affect specific input channels of the weight matrix, so grouping weights along the IC direction isolates outlier effects within individual groups. The paper further introduces AdaDim, a framework that adaptively selects per-IC or per-OC quantization per layer by minimizing reconstruction error. Experiments across LLaMA-V2 base models (up to 70B) and instruction-tuned models show consistent improvements over RTN and GPTQ baselines, with notable gains such as +4.7% MMLU on LLaMA-V2-7B and up to +10% on HumanEval.

## Strengths

- **Per-IC quantization and outlier isolation are well-motivated by structural analysis.** The paper provides a clear mechanistic argument (Figure 1) supported by sensitivity analysis (Figure 2) showing that activation outliers correlate with sensitive weight channels, and that per-IC grouping contains the outlier effect within individual groups. Table 1 validates this by showing that selectively applying per-IC only to outlier-affected modules (QKV, DOWN) improves MMLU by up to 0.67%, while naive all-layer application hurts.

- **AdaDim's adaptive selection yields consistent, non-trivial improvements across diverse settings.** Augmenting RTN with AdaDim produces a +4.7% MMLU boost on LLaMA-V2-7B, surpassing both AWQ and GPTQ (Figure 3). On instruction-tuned models, GPTQ-ada yields up to +10% on HumanEval (Table 4). Gains hold across INT3/INT4 precision and group size sweeps (Figure 4), and the adaptive method outperforms heuristic-based offline selection (Table 2), demonstrating the necessity of on-the-fly dimension choice.

- **The analysis of GPTQ update localization (Figure 6) provides an interpretable explanation** for why per-IC benefits weight quantization beyond simple error metrics — per-IC confines error-compensation updates to a small subset of input channels, minimally perturbing the weight distribution.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **The paper's central mechanistic claim (outlier isolation) is not fully disentangled from a granularity confound.** When the weight matrix is non-square (e.g., QKV projections where C_in ≠ C_out), per-IC and per-OC with the same group size produce different total numbers of quantization groups. The paper uses group size 128 for both but never tests whether a per-OC scheme with the *same number of groups* (by adjusting group size) achieves similar or better results. Thus, the reported improvements could partly stem from a change in grouping granularity rather than exclusively from the outlier-isolation mechanism. This does not diminish the practical value of AdaDim's empirical gains, but it means the explanatory narrative is stronger than the evidence directly supports. The paper could resolve this with a matched-groups ablation.

- **The GPTQ combination in Table 2 uses asymmetric reordering policies without sufficient justification.** Per-OC is tested with "static reordering" (hardware-efficient variant) while per-IC uses non-static reordering, with the paper stating only that per-IC is "already hardware-efficient." It is not explained *why* per-IC avoids the memory-contiguity problem that necessitates the static variant for per-OC, nor is it shown whether per-IC with static reordering would change the results. This asymmetry makes it difficult for the reader to assess whether the adaptive selection is genuinely superior or benefits from an inconsistent comparison setup.

- **The paper lacks a discussion of failure cases or limitations.** It mentions that naive application of per-IC to all layers hurts performance (Table 1), but does not analyze *why* — e.g., whether layers without outliers inherently benefit from per-OC's different noise structure, or whether certain architectural configurations are ill-suited for per-IC. A brief characterization of when per-IC is not beneficial would sharpen the contribution.

### Trivial
- The kernel latency results (Figure 7) are limited to a single layer of OPT-175B, and the paper transparently notes the kernel is not fully optimized. This is a preliminary demonstration, not a weakness per se, but the framing ("measurable speedups") slightly overstates what a single-layer measurement supports. The paper already self-qualifies this appropriately.

## Nice-to-Haves
- A comparison or conceptual discussion relating per-IC grouping to mixed-precision outlier isolation methods (e.g., SpQR) could help situate the contribution within the broader outlier-handling literature — though the existing comparison against AWQ and GPTQ is already adequate for a methods paper.
- An analysis of how many calibration samples are needed for the adaptive selection to stabilize, and whether per-layer choices are consistent across random seeds, would strengthen the practical guidance.

## Removed Points
- **"Not comparing against SpQR is an empirical gap"** — This is a scope-creep request. The paper compares against the two dominant weight-only quantization baselines (AWQ and GPTQ), which is appropriate for a methods paper presenting a new grouping scheme and adaptive framework. Comparisons against every outlier-handling method are not required. (Moved from weaknesses to Nice-to-Haves.)
- **"Kernel latency results overclaim speedups"** — The paper explicitly qualifies this as preliminary ("Due to time and resource limitations, we do not perform experiments with a fully optimized kernel"), so this is not a weakness — it is a transparent limitation. The critic acknowledges this is "fine for a methods paper." Retained in Trivial as a minor framing note.

## Novel Insights
None beyond the paper's own contributions. The reviews largely converge on the paper's stated contributions and raise concerns that the authors can address with additional ablations and clarifications.

## Suggestions
- Add a controlled ablation where the *number of quantization groups* is matched between per-OC and per-IC configurations for each linear layer. If the improvement persists under matched groups, the outlier-isolation hypothesis is strongly supported; if not, reframe the contribution around the practical benefits of adaptive dimension selection rather than specifically the isolation mechanism.
- Provide a clearer justification for the asymmetric reordering policies in the GPTQ combination: explain *why* per-IC avoids the memory-contiguity issue that requires static groups for per-OC, and ideally test per-IC with static reordering for completeness.
- Add a brief limitations section discussing when per-IC may hurt or be unnecessary (e.g., layers without outliers, small group sizes, or architectures with symmetric input/output dimensions).

## Score and Decision

This paper presents a well-motivated, clean idea validated extensively across multiple model families, tasks, and quantization settings. The empirical results are consistent and practically meaningful. The weaknesses are incremental and addressable: the mechanistic interpretation could be tightened, and the GPTQ ablation asymmetry needs clarification, but neither threatens the core contribution. The paper is a solid contribution to the LLM quantization literature.

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>
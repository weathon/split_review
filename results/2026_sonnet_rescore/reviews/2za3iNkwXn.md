---

## Summary

This paper investigates how compression (quantization, distillation, and pruning) affects Large Reasoning Models (LRMs), studied through both performance benchmarking and mechanistic interpretation. Using adapted difference-of-means and attribution patching, the authors compute per-module weight importance for four reasoning behaviors across compressed DeepSeek-R1 variants, arriving at three main findings: (1) weight count (not precision) governs knowledge memorization more than reasoning; (2) the MLP `up_proj` in the final layer is the single most critical component for reasoning in distilled LRMs; and (3) standard quantization over-compresses final-layer modules and MLP gate projections, and protecting just ~2% of weights in these modules recovers 6.57% average accuracy over a 3-bit baseline.

---

## Strengths

- **Comprehensive, multi-paradigm benchmarking (Table 1 & 2):** The paper provides a rare apples-to-apples comparison of dynamic quantization, distillation, AWQ, GPTQ, GPTAQ, ANY4/3, SparseGPT, and AlphaPruning on the same LRM families across four reasoning datasets of varying difficulty (AIME 2024, FOLIO, Temporal Sequences, MuSiQue). This fills a genuine gap in the literature, as prior works evaluate compression primarily on perplexity or simple commonsense tasks.

- **Causal validation of the final-layer `up_proj` as the critical component (Figure 2 & Table 3):** The paper identifies `32_up` as the globally highest-importance module across all four reasoning behaviors for R1-Distill-Llama-8B and confirms it on Qwen-7B (Figure 4). The importance is causally validated in Table 3: quantizing only this 0.7% of weights to 3-bit produces the largest average accuracy drop (Avg = 48.9%), substantially more than other components. This is a concrete, reproducible, empirically verified finding.

- **Selective protection as actionable, empirically validated guidance (Table 4):** The protection mechanism—retaining final-layer MLP modules in 16-bit while quantizing everything else to 3-bit—raises average accuracy by 6.57 percentage points over the unprotected 3-bit AWQ baseline and beats all 3-bit variants in Table 1 by at least 4.77 points. This directly converts the interpretability finding into a practical improvement.

- **Distillation effect as the origin of final-layer importance (Figure 2 lower / Section 4.3):** By comparing importance shift from R1-Distill-Llama-8B to its Llama-3.1-8B backbone, the paper shows that the strong role of final-layer modules emerges from the distillation fine-tuning, not from the pre-trained backbone. This is consistent across both Llama and Qwen (Figures 4–5), providing a mechanistic explanation for why distilled LRMs are structurally distinct from base models under compression.

- **Collapse-point analysis tied to benchmark difficulty (Table 2):** The paper shows that collapse point under SparseGPT sparsity directly correlates with task difficulty: AIME 2024 collapses first (between 40–50% sparsity for Llama-70B), followed by FOLIO and Temporal (between 60–70% sparsity). This structure is consistent across both Llama-70B and Qwen-32B.

---

## Weaknesses

### Fatal
None.

### Major

- **Finding 3's selective protection is validated on a single model (R1-Distill-Llama-8B only; Table 4).** The abstract claims findings "generalize across both R1 and non-R1 LRMs," and the paper shows that Qwen-7B exhibits similar over-compression patterns in Figure 6. However, no selective protection experiment is run on Qwen-7B, nor on any larger quantized model (32B or 70B). For the paper's most practically significant and quantitatively impressive claim—gains of up to 23.17% over state-of-the-art—a single model is a weak empirical foundation. If the gain is substantially smaller on Qwen-7B or vanishes at larger scales, the generalization claim in the abstract would not hold. Running the same protection on at least Qwen-7B (which has a 3-bit AWQ baseline in Table 1) would be straightforward and would strengthen the paper considerably.

### Minor

- **Table 3: The `1_up` anomaly undermines the validation logic without explanation.** The paper states that "the component rank generally correlates with the accuracy drop, except for `1_up`." But `1_up` is ranked *last* (least important) and yet causes an AIME 2024 accuracy of 6.7%—lower than `32_up` (the globally most important module) at 20.0%. The paper offers no mechanistic explanation. Since the entire validation of the importance-rank hypothesis in Section 4.2 depends on "the more important a component, the greater the accuracy drop," an unexplained reversal on the hardest benchmark for the least-important module is a genuine gap. It may reflect quantization sensitivity being distinct from importance (i.e., low-importance modules may be fragile to 3-bit quantization for reasons unrelated to their role in reasoning), but this distinction should be articulated.

- **Asymmetric importance-shift visualization (Section 2.3; Figures 2, 3, 6, 7).** Visualizing only decreases in relative importance is explicitly justified ("any increase in relative importance necessarily compensates for decreases elsewhere"), and additional justification is given in Appendix H. However, this design choice means the heatmaps cannot distinguish "compression diminishes module X's importance" from "compression amplifies module Y at the cost of X." The paper does not show whether modules whose RI *increases* under compression correspond to any functional change—if they do, the picture is incomplete. The justification is reasonable but the framing of attribution patching as providing "causal relationships" (Section 2.2) is stronger than the methodology strictly warrants given this asymmetry.

- **Finding 1 (weight count vs. knowledge): primary evidence conflates architecture and parameter count.** Section 3.3 draws the conclusion that parameter count governs knowledge more than reasoning primarily from the observation that R1-Distill-Qwen-32B has far lower MuSiQue scores than R1-Distill-Llama-70B. These models differ not just in size but in architecture and base model training. The paper's pruning evidence (Table 2, MuSiQue collapses earlier under pruning than AIME 2024) is cleaner and more persuasive, but the central claim is stated more broadly than this evidence alone supports. The conclusion should be qualified to reflect this.

- **Non-contrastive negative set in the difference-of-means formulation (Section 2.2).** By definition, D₋ is the set of *all* output instances, meaning D₊ ⊆ D₋. In standard contrastive difference-of-means, D₋ should be a matched set of instances definitively lacking the target behavior. Using the full output set as the negative means the steering vector measures the difference between a subset mean and the global mean rather than a clean contrastive signal. For high-frequency behaviors (e.g., backtracking), many D₋ instances will contain the behavior, diluting the contrastive signal. This is acknowledged implicitly by following prior work (Venhoff et al., 2025), but the potential downstream impact on importance score reliability is not discussed.

- **Single-pass evaluation makes the 2.51-bit R1 "best overall" claim fragile (Table 1, Section 3.1).** The 2.51-bit R1 achieves 76.7 on AIME 2024 vs. 73.3 for the original R1, but both are single-pass evaluations (†). AIME 2024 uses only 30 problems, so a 3.4-point gap is plausibly within run-to-run variance. The paper's claim that "2.51-bit R1 achieves the highest average accuracy overall" rests partly on this difference. The defensible conclusion is that 2.51-bit R1 is *close* to original R1, not strictly better.

### Trivial

- The paper does not provide standard deviations for the importance scores or for Table 4's protection result. Given the 3-pass evaluation, reporting variance for at least the key selective protection result (Table 4) would strengthen the quantitative claims.
- The paper defers pruning interpretability entirely to Appendix I (Section 5: "we choose to interpret the effect of pruning with greater caution and specify the details in Appendix I"), creating some structural imbalance since pruning is positioned in the abstract as one of three paradigms under study. The rationale (pruning causes aggressive collapse at 50%, making the interpretability less actionable) is reasonable, but a brief mention of the finding and its direction in the main text would be appropriate.

---

## Nice-to-Haves

- Running selective protection on R1-Distill-Qwen-7B and potentially R1-Distill-Qwen-32B would make Finding 3 substantially more robust.
- The difference in gate-projection compression layer ranges (layers 9–23 for Llama vs. layers 1–10 for Qwen) is noted but unexplained. Understanding whether this reflects architectural differences or training differences would enrich the interpretation.
- A brief quantitative summary of the non-R1 generalization results currently in Appendix J in the main body would strengthen the generalization claim in the abstract.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Harsh Critic: "Causal" framing in Section 2.2 is unjustified given the methodology.** *Removed from Fatal/Major.* The paper uses "causal" in the sense of attribution patching (a standard mechanistic interpretability technique), and Table 3 provides direct empirical validation. The framing is consistent with how attribution patching is typically presented in the literature. Retained only as a minor precision note under "asymmetric visualization."

- **Harsh Critic: Finding 1 is fatally confounded.** *Demoted to Minor.* The paper's pruning evidence from Table 2 (MuSiQue collapses earlier than AIME under pruning) provides an architecture-controlled data point. The cross-architecture confound is real but doesn't wholly invalidate the finding.

- **Harsh Critic: The `up_proj` finding is only tested on 8B/7B models.** *Demoted to Nice-to-Have.* The paper explicitly demonstrates the finding on both Llama-8B and Qwen-7B, and mentions generalization in Appendix J. The scope is clear; not testing all model sizes is a limitation but not a major flaw given the mechanistic validation in Table 3.

- **Harsh Critic: 2.51-bit R1 "highest accuracy overall" is not supported by a single-pass evaluation.** *Retained as Minor but not Major.* The paper makes a clear caveat that single-pass results carry the † marker, and the overclaim is soft ("still offer advantages").

---

## Novel Insights

The most genuinely novel observation in this work is the combination of (a) identifying the final-layer MLP `up_proj` as the dominant weight for LRM reasoning capabilities via attribution patching, (b) showing this importance is the *product of distillation* (not of the backbone), and (c) demonstrating that standard quantization systematically under-protects precisely this module. The connection between the interpretability finding and a concrete compression fix—restoring only 2% of weights yields disproportionate accuracy recovery—is a compelling end-to-end argument that distinguishes this paper from broader LRM benchmarking work. The finding that collapse point under pruning correlates with benchmark difficulty is also a clean, generalizable empirical observation with implications for evaluation methodology.

---

## Suggestions

1. **Run the selective protection experiment on at least R1-Distill-Qwen-7B** (3-bit AWQ baseline is available in Table 1). This single experiment would substantially strengthen the generalization claim for Finding 3.
2. **Provide a mechanistic explanation for the `1_up` anomaly in Table 3**, or explicitly state that quantization sensitivity may decouple from attribution-patching importance for early-layer modules, and flag this as a limitation of the importance metric.
3. **Clarify the non-contrastive negative set** in Section 2.2, particularly for high-frequency behaviors where D₋ substantially overlaps D₊.
4. **Include standard deviation or confidence interval for Table 4** to quantify the reliability of the 6.57% gain.

---

## Score and Decision

**Axis-by-axis assessment:**
- *Originality:* Moderate — adapting DoM + attribution patching to per-module compression analysis is novel; the benchmarking is incremental.
- *Importance:* High — compression of LRMs is a pressing practical problem.
- *Claims supported:* Mixed — benchmarking claims well-supported; Finding 3 generalization overclaimed; Finding 1 partially confounded.
- *Soundness:* Moderate — experiments are well-executed; interpretability methodology has documented limitations (asymmetric RI, non-contrastive D₋, Table 3 anomaly).
- *Clarity:* Good — the paper is readable and findings are clearly presented.
- *Community value:* High — actionable and practically relevant findings.

The paper's core contributions are real: the benchmarking fills a gap, the mechanistic finding on final-layer `up_proj` is empirically validated, and the selective protection experiment demonstrates practical payoff. The main weakness—that Finding 3 is validated on one model—is addressable, not structural. No fatal flaw invalidates the core claims as written.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>3</originality>
<importance>4</importance>
<claims_supported>3</claims_supported>
<soundness>3</soundness>
<clarity>4</clarity>
<community_value>4</community_value>
</subscores>
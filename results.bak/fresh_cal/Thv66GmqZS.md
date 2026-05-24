Now I have a thorough understanding of the paper. Let me verify the key claims against the actual text and produce the consolidated review.

---

## Summary

This paper proposes Bi-Share LoRA, a variant of LoRA that decomposes the adaptation matrix into three parallel low-rank components: a local (module-specific) component, an intra-layer shared component, and an inter-layer shared component. Three shape-transformation methods (Slice Sharing, Gate Transformation, Kronecker Extension) handle dimension mismatches when sharing across modules of different sizes. Experiments are conducted on Llama models (7B, 8B, 13B) on commonsense reasoning and MMLU benchmarks.

## Strengths

- **Empirical justification for parameter redundancy (Figure 1, Table 1):** The paper provides a data-driven motivation via entropy similarity analysis showing high redundancy both within and across layers, and a preliminary study (Table 1) showing that naive sharing degrades performance while the proposed joint configuration (local + intra + inter) improves it with fewer parameters. This grounds the design in evidence rather than intuition.

- **Contribution analysis validates the design (Figure 4b):** The paper ablates each sub-LoRA component individually across six commonsense reasoning datasets and shows that no single component dominates; the combination of all three produces the best results. This directly supports the core architectural decision.

- **Three practical shape-transformation methods with thorough ablations:** The paper introduces and evaluates three techniques (SS, GT, KE) for adapting shared parameters to modules of different shapes. Ablations cover slicing position (Table 4), gate initialization (Table 5), kernel initialization (Table 6), and shared matrix size (Tables 7–8), providing empirical depth to engineering choices.

- **Rank analysis (Figure 4a):** The paper validates theoretically (rank sum bound) and empirically (actual ranks achieved under SS, GT, KE) that decomposing into sub-LoRAs increases the combined effective rank without proportionally increasing parameters.

## Weaknesses

### Fatal
None.

### Major

- **No experimental comparison with existing parameter-sharing LoRA methods.** The paper discusses VeRA, Tied-LoRA, PRoLoRA, and VB-LoRA in Section 5.2 (Parameter Sharing of LoRA), positioning its contribution relative to them. Yet the experimental evaluation (Sections 4.2–4.3) compares only against "standard LoRA." The abstract claims improvement "compared to standard LoRA and other existing methods" (line 23), but no evidence against VeRA, VB-LoRA, PRoLoRA, or Tied-LoRA is presented in any experimental section. Without this context, the core claim of "enhancing the parameter efficiency of LoRA" is uncalibrated — a method that merely beats vanilla LoRA but is less parameter-efficient or worse-performing than VeRA or VB-LoRA does not constitute a meaningful advance. This is the single most important evidential gap.

- **The standard LoRA baseline configuration is unspecified.** The paper never states what rank the baseline LoRA uses, which modules it is applied to (q,v only? all attention + FFN?), or how its parameter count is calculated. Since Bi-Share LoRA uses three sub-LoRAs with ranks {r_local, r_intra, r_inter} that sum to a larger total rank (e.g., 2+4+16=22), the claim of using "44.59% of the parameters of standard LoRA" is uninterpretable without knowing the baseline's rank and module scope. The reported performance gains (0.33% on commonsense, 2.08% on MMLU) could be partially attributable to rank allocation differences rather than the sharing strategy itself. This undermines the primary quantitative claim.

### Minor

- **Mismatch between deployment motivation and evaluation.** The introduction motivates Bi-Share LoRA via memory overhead and inference latency when deploying multiple LoRA modules on a single server (lines 13–18). Yet no experiments measure actual memory usage, inference latency, throughput, or multi-task serving performance. The only metric reported is trainable parameter count, which is a proxy for storage but does not capture loading/switching overhead or batch inference costs. The stated practical problem is not evaluated, making the paper's framing feel disconnected from its evidence.

- **Inconsistent parameter-savings claim.** The abstract states Bi-Share LoRA uses "only 44.59% of the parameters of standard LoRA" (line 5), implying a ~55.41% reduction. The conclusion states the method "significantly cuts down parameter usage by 56.40%" (line 236). These differ by about 1 percentage point. While small, this inconsistency erodes trust in the numbers and suggests either a typo or a difference in experimental conditions between the two statements.

### Trivial
- The Gate Transformation method applies one-rank decomposition to the input/output gates (line 118), which the rank analysis (Figure 4a) shows caps the effective combined rank at local_rank + 2 (vs. the theoretical sum of 22). This is a known limitation stated in the paper; it's worth a brief theoretical discussion of when GT should be preferred over SS or KE despite this limitation.

## Nice-to-Haves
- Compare against at least 2–3 published parameter-sharing LoRA variants (e.g., VeRA, VB-LoRA) under identical settings to contextualize the improvement.
- Measure actual deployment metrics (peak memory during multi-task inference, LoRA weight switching latency) to match the stated motivation.
- Report variance or runs for the main results; the gains over LoRA are small (0.33%) and significance is unclear.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Missing Tables 2 and 3 (commonsense reasoning and MMLU results):** The harsh critic argues the main results are absent and the claims cannot be assessed. However, the extracted text jumps from Section 4.1 to 4.3, and the images/tables are parser-stripped artifacts that exist in the original submission. Per the review rules, parser-stripped content is not a paper weakness. The reviewer even acknowledges these tables "exist in the original PDF." *Removed as parser artifact.*

- **Missing related works / reproducibility concerns about cited methods:** The harsh critic implies some cited methods may not be verifiable. Per the rules, all cited references are assumed to exist. *Removed per Hard Rule.*

- **"Section 4 jumps from 4.1 to 4.3 without any content for 4.2" as a weakness:** This is a parser artifact; the original paper has Section 4.2. *Removed per formatting/parser artifact rule.*

- **Strength Finder's generic claim about "importance of the problem"** — the paper addresses a real problem (parameter efficiency in LoRA) but this is a generic strength that applies to any LoRA variant paper. *Removed as generic/superficial.*

- **Strength Finder's claim about "consistent gains across model scales"** — This conflicts with the verified weakness that the LoRA baseline is underspecified, making the gains hard to interpret. Per the rule "when a strength and weakness disagree, the weakness wins." *Removed due to conflict with verified weakness.*

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface any perspective on the method or results that the authors themselves do not already articulate.

## Suggestions

1. Add an experimental comparison table with VeRA, VB-LoRA, and PRoLoRA (or at least two of these) under identical training setups, reporting both accuracy and trainable parameter counts. Without this, the paper cannot demonstrate that its approach is superior to existing sharing strategies.
2. Specify the exact LoRA baseline configuration (rank, applied modules) used throughout the paper, and present a clear parameter-count breakdown for every method and variant.
3. Resolve the 44.59% vs. 56.40% discrepancy between the abstract and conclusion.
4. Add a small-scale deployment-motivation experiment (e.g., memory usage and latency for serving N concurrent LoRA adapters) to match the stated practical framing, or else reframe the motivation more narrowly around parameter efficiency.

## Score and Decision

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>
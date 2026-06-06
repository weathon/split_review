Now I have enough detail to write the meta-review. Let me synthesize the findings.

## Summary
TNT introduces a two-stage training paradigm for deep memory modules (Titans, TTT) that uses a hierarchical global+local memory with periodic local state resets enabling context parallelism, plus a Q-K projection to address compression-retrieval domain mismatch. Stage 1 maximizes throughput with large chunks; Stage 2 fine-tunes at smaller chunk sizes. The paper demonstrates up to 17× faster training-to-quality over baseline Titans while simultaneously improving language modeling perplexity and common-sense reasoning accuracy on 150M parameter models.

---

## Rebuttal Assessment

**Weakness:** No long-context quality evaluation
- **Author's response:** Acknowledge
- **Assessment:** Unconvincing as a rebuttal — The author concedes the gap outright and offers the Table 3 ablation (removing global memory: PPL 21.04→25.60) as "indirect but meaningful evidence" for long-range context utilization. However, this ablation is performed at 16K context and only tests whether the global memory contributes to perplexity on standard language modeling; it does not demonstrate long-range retrieval capability. The global memory uses C_G=2048 on a 16K sequence, covering at most 8 chunks of coarse context. Showing that removing this module degrades general LM perplexity does not establish that the model retrieves information across long ranges in any structured sense. The promise to add a limitations section does not fix the paper as submitted.
- **Score impact:** Weakness unchanged

**Weakness:** Contribution attribution (architectural vs. training paradigm)
- **Author's response:** Partially address
- **Assessment:** Partially convincing — The author's argument that the periodic reset and global memory are a coupled system by design (Section 4.1.1: "This causes local memory modules to lose the global context. To solve this, we introduce a global memory module") is legitimate and documented in the paper. The ablation evidence that "w/o global memory" yields PPL=25.60 (worse than Titans C=256 at 23.53) does confirm that the reset mechanism alone is harmful without compensating global context. However, the author's claim that "TNT Stage 1 with one local module has comparable parameter count to a Titans model with one memory module" is not demonstrated quantitatively. TNT Stage 1 adds a global module on top of the local module, meaning it has strictly more parameters than the Titans C=8 baseline. The reviewer's concern — can quality gains be attributed to the training paradigm vs. the extra memory capacity? — remains unanswered. No matched-parameter controlled ablation exists in the paper.
- **Score impact:** Weakness downgraded (from Major to Major but partially addressed)

**Weakness:** Stage 2's marginal empirical contribution overstated
- **Author's response:** Partially address (acknowledge overstatement)
- **Assessment:** Partially convincing — The author acknowledges the framing overstatement and correctly points out that the single-module ablation (Table 3: 21.04→20.86 PPL, 0.18 improvement) is cleaner and larger than the four-module multi-module case (23.13→23.09, 0.04 improvement) cited by the reviewer. This is verified in the paper. The author accepts the reviewer's reframing suggestion ("cheap inference-resolution calibration") and agrees to add variance statistics. That said, 0.18 PPL and 0.3% accuracy improvement remain modest gains even in the most favorable case, and significance remains unestablished.
- **Score impact:** Weakness downgraded (from Minor to minor; framing issue is largely acknowledged)

**Weakness:** Ablation uses weaker Titans baseline (C=256)
- **Author's response:** Partially address
- **Assessment:** Partially convincing — The methodological rationale is reasonable: the ablation tests TNT operating at large chunks (C_G=2048, C_L={8}), so comparing against Titans C=256 (the large-chunk Titans configuration) is more consistent than comparing against Titans C=8. This is a legitimate design choice that the paper could clarify. However, it doesn't eliminate the perception issue for readers who don't cross-reference Table 2. The author promises a cross-reference note.
- **Score impact:** Weakness downgraded (from Minor to trivial)

**Weakness:** Inference behavior at generation time underspecified
- **Author's response:** Partially address
- **Assessment:** Partially convincing — Section 4.2 does contain the relevant text (verified: "fine-tuning specializes the model for the ideal inference scenario: a local chunk size of one (C'_L = 1). This aligns with the standard prefill-and-decode paradigm..."). The paper's Eq. 6 formally defines the periodic reset behavior. However, what happens beyond S_L during autoregressive generation (local memory resets to W_init at each new S_L-length segment) is not stated explicitly in the paper for the generation case. The author's explanation in the rebuttal is logical and consistent with Eq. 6, but it is not in the paper itself. The author promises to add a clarifying paragraph.
- **Score impact:** Weakness downgraded (from Minor to trivial)

**Weakness:** Figure 2 uses 550M model while all experiments use 150M
- **Author's response:** Partially address
- **Assessment:** Partially convincing — The author's argument that Stage 2's effectiveness at 150M constitutes indirect evidence for the phenomenon's existence at 150M is reasonable (if Stage 2 didn't improve performance, the mismatch wouldn't exist). The promise to add a 150M equivalent figure is acknowledged but not in the paper.
- **Score impact:** Weakness unchanged (Trivial, stays Trivial)

---

## Strengths
- **Training acceleration robustly demonstrated.** Table 1: TNT C_L={64} reaches loss 3.20 in 1.12 hrs vs. 19.48 hrs for Titans C=8 (17.37×). Figure 4 confirms linear runtime scaling vs. quadratic for attention; 5.1× faster than Titans at 32K context.
- **Quality improvement alongside efficiency.** Table 2: TNT Stage 1 with four local modules achieves avg. PPL 23.13 vs. best Titans 25.07 and vanilla Transformer 23.58. Simultaneously outperforming on both dimensions is non-trivial.
- **Ablation validates each component.** Table 3: global memory removal (+4.56 PPL), Q-K projection removal (+0.97 PPL), multi-module scaling (stepwise 21.04→20.74→20.47→20.15). Meaningful quantitative differences.
- **Periodic reset enabling non-linear context parallelism is a novel contribution.** Breaking sequential inter-shard dependency by resetting to a learned W_init is a clean solution to a long-standing challenge for non-linear RNNs.
- **Q-K projection is principled.** Projecting queries onto the key subspace to address compression-retrieval domain mismatch is well-motivated and ablation-validated.

---

## Weaknesses

### Fatal
None.

### Major
- **No long-context quality evaluation despite long-context motivation.** All quality evaluations (Table 2) are at 16K context on C4, FineWeb, PG19, and standard commonsense benchmarks. No needle-in-haystack, passkey retrieval, SCROLLS, RULER, or analogous long-context benchmark appears. The ablation's "w/o global memory" perplexity degradation (21.04→25.60) is at most indirect evidence that long-range context is used; it is not a substitute for retrieval quality. The motivational claim that TNT enables "truly long sequences" remains empirically unsupported for the quality dimension. The rebuttal acknowledges this fully but provides no new evidence from the paper.

- **Contribution attribution is not fully isolable.** TNT adds both (a) the periodic reset mechanism and (b) a global memory module with additional parameters. No controlled comparison exists with matched parameter count and no reset. The author's argument that the components are coupled by design is legitimate but does not answer the question of how much quality gain is attributable to extra capacity vs. the training paradigm itself. The "w/o global memory" ablation (PPL 25.60) shows the system fails without global memory, but does not rule out that a Titans model with equivalent total capacity trained conventionally would achieve similar quality.

### Minor
- **Stage 2's empirical contribution is modest.** Even accepting the single-module case (21.04→20.86 PPL, 0.18 improvement), the effect is small. Authors acknowledge the framing overstatement and promise to add variance reporting. Rebuttal confirms the issue exists but reduces its severity.

### Trivial
- **Ablation baseline is the weaker Titans C=256.** Methodologically defensible but creates a misleading impression relative to best Titans C=8. Authors promise a cross-reference.
- **Inference behavior during long generation underspecified.** Authors' rebuttal provides a logical explanation (reset at S_L intervals during generation), consistent with Eq. 6, but not in the paper as submitted.
- **Figure 2 uses 550M model; experiments use 150M.** Minor scale consistency issue; Stage 2's effectiveness at 150M provides indirect confirmation.

---

## Nice-to-Haves
- At least one long-context retrieval benchmark (passkey, needle-in-haystack at 32K–128K) comparing TNT against Titans-C=128 (speed-comparable baseline)
- Controlled ablation: Titans with global+1 local module, matched parameter budget, fixed chunk size (no reset), compared against TNT Stage 1 with one module
- Error bars on Table 2 accuracy numbers
- Explicit clarification in Section 4.2 of generation behavior when sequences exceed S_L

---

## Novel Insights
The periodic-reset mechanism for enabling context parallelism in non-linear RNNs is the paper's most transferable contribution. Unlike parallel-scan methods (limited to linear recurrences) or chunked-attention hybrids (which change the architecture), TNT's insight is that the long-range dependency problem for non-linear RNNs can be decomposed: assign all cross-shard context to a dedicated global module that runs sequentially at a large chunk size, and free the local module to operate within independent, parallelizable shards. This conceptual separation — global module carries sequential dependency, local module resets and parallelizes — is architecturally clean and potentially applicable to any architecture with separable short-range and long-range processing needs. The Q-K projection as a running-sum low-rank projection for query regularization toward the key distribution is a secondary but practically useful insight.

---

## Suggestions
1. Add one long-context retrieval benchmark (passkey at 32K or 64K, or RULER sub-task) comparing TNT against the speed-comparable Titans-C=128 baseline.
2. Add an explicit paragraph in Section 4.2 describing reset behavior during autoregressive generation beyond S_L.
3. Report variance on Table 2 accuracy numbers and reframe Stage 2 as a "cheap inference-resolution calibration step."
4. Add a matched-parameter ablation: Titans with global+local memory configuration at equivalent total parameter count, trained without resets, compared against TNT Stage 1.

---

## Score and Decision

The rebuttal is largely honest: the authors acknowledge all major weaknesses rather than refuting them with new evidence. The efficiency contribution remains robustly supported. The two major weaknesses — absent long-context quality evaluation and unresolved contribution attribution — are acknowledged but not resolved by the rebuttal; both remain weaknesses of the submitted paper. Some minor weaknesses are downgraded by the rebuttal (Stage 2 framing acknowledged, inference behavior partially clarified in the rebuttal if not the paper, ablation baseline rationale reasonable). No new problems were surfaced.

The paper sits at the same position as before: a solid efficiency contribution with genuine quality improvements over Titans, but with a meaningful gap between its stated long-context motivation and its quality evidence. The rebuttal neither strengthens the case for raising the score nor exposes new reasons to lower it.

**Final Score: 6.0**

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>
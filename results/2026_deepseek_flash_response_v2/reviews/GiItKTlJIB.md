## Summary

This paper proposes a deletion-based probing framework to test how much LLMs depend on their chain-of-thought traces during physics problem solving. By intercepting CoT mid-generation and removing tokens under three strategies (end deletion, random deletion, physics-aware deletion), the authors find that accuracy remains stable under 40–60% deletion before degrading, while final answer length increases — a phenomenon they term "cramming." The paper evaluates three open-source models (Phi-4, Qwen-A3B, Magistral) on three physics benchmarks and reports that models attempt to reconstruct missing reasoning in final answers, revealing a gap between CoT usage and accuracy.

## Strengths

1. **Novel deletion-based probing methodology.** The paper introduces a systematic framework that intercepts CoT mid-generation and removes tokens before decoding (§3.2). This goes beyond standard accuracy-only evaluations by directly manipulating the reasoning trace. The three deletion strategies (end, random, physics-aware) provide complementary views of how deletion structure affects model behavior, a design richer than what most prior faithfulness studies employ.

2. **Empirical characterization of a specific compensatory pattern ("cramming").** The paper identifies an X-shaped pattern where, as CoT tokens are removed, final answer length rises sharply while accuracy initially remains stable (Figures 5–6, §4.1). This observation is concrete and measurable, with specific thresholds documented: ~40% for end deletion, ~60% for random deletion, and 70–80% for physics-aware deletion (§3.2). These thresholds provide a more detailed empirical account than prior work that simply checks whether CoT is necessary.

3. **Consistent patterns across diverse models and datasets.** The key observations hold across three distinct open-source models (Phi-4, Qwen-A3B, Magistral) on three physics benchmarks of varying difficulty (§3.2). This cross-architecture consistency strengthens the generality of the findings beyond any single model family or difficulty level.

## Weaknesses

### Major

1. **Unvalidated LLM judge as the sole accuracy metric.** The paper uses Claude-4 Sonnet as an automated judge to assign 0–1 scores based on "correctness, derivation accuracy, logic, formatting, and clarity" (§2.4). The physics benchmarks used have ground-truth answers (numerical values, symbolic equations), yet the paper never validates the judge against any objective correctness measure — no exact-match baseline, no Spearman correlation, no symbolic verification (confirmed by grep: no occurrences of "ground truth," "validate," "correlation," "spearman," or "exact match" in the paper). Without establishing that the judge's scores correspond to actual physics correctness, all quantitative claims — the stability thresholds in §3.2, the degradation curves, and the calibration study (§3.1) — rest on an opaque scoring function whose behavior is uncharacterized. The relative trends (accuracy degrades after a threshold) may be robust to moderate judge noise, but this must be demonstrated, not assumed. This is the paper's most significant evidential gap.

2. **Cramming evidence does not establish that reconstructed content is correct physics.** The cramming claim rests on two observations: (a) final answer length increases under deletion, and (b) bag-of-words overlap (Jaccard similarity, Manhattan distance) between deleted CoT content and final answers increases with deletion fraction (§4.1–4.2). Neither measure establishes *correct physics reconstruction*:
   - **Answer length** is a crude proxy. Longer answers could indicate repetition, confusion, or hallucination — not genuine reconstruction. The paper acknowledges that judge scores do *not* recover under deletion (§4.2), which undercuts the interpretation that longer answers are successfully compensatory.
   - **Bag-of-words metrics strip away mathematical structure.** Equations like "F = ma" and "a = F/m" share tokens and are lexically similar, but one is reversed. "F = ma" and "F = mv" also share tokens, but only one is correct. The metrics cannot distinguish faithful physics reconstruction from surface-level lexical coincidence.

3. **Information overlap metrics lack base-rate correction.** The paper computes overlap between "deleted CoT spans and regenerated answers" (§4.2). As the deletion fraction increases, the set of deleted tokens grows mechanically, so any text the model generates will have higher *chance* overlap with a larger deleted set. The paper does not control for this base-rate effect — e.g., by comparing overlap against a held-out CoT trace from a different problem at the same deletion rate. Without this correction, increasing overlap could simply reflect the growing comparison set rather than genuine reconstruction.

### Minor

1. **Missing dataset sizes for two of three benchmarks.** PhysReason is reported as 1,200 problems (§2.1), but the sizes of UG Physics and PhyBench are not given. Without this information, the statistical power of the experiments cannot be assessed, and it is unclear whether performance differences across datasets are confounded by large disparities in problem count.

2. **No control for truncation artifacts.** Deleting tokens mid-generation (especially under end deletion) may produce incoherent or broken text — sentence fragments, dangling equations — that confuses the model for reasons unrelated to removing reasoning content. A control condition deleting the same fraction of tokens from a non-reasoning passage inserted before the answer would help isolate the effect of breaking the reasoning trace from general text corruption.

3. **No statistical testing for key comparisons.** The headline claims about accuracy being "stable until 40–60% deletion" (§3.2) are reported descriptively with error bars but without formal statistical tests. Whether the observed degradation thresholds differ significantly across deletion strategies, models, or datasets is not assessed.

### Trivial

None.

## Nice-to-Haves

- Validating the Claude-4 judge against ground-truth correctness (exact match on numerical answers, symbolic equation matching) would significantly strengthen the paper's quantitative backbone.
- Using physics-aware reconstruction metrics (e.g., checking whether the correct numerical result or key equation appears in the final answer after deletion) would provide stronger evidence for the cramming interpretation than bag-of-words overlap.
- Adding a base-rate control for the overlap analysis (e.g., comparing against overlap with a different problem's CoT at the same deletion rate) would make the information overlap results interpretable.
- Reporting UG Physics and PhyBench sizes would improve experimental transparency.

## Removed Points

These points were flagged for removal from the Harsh Critic and/or Strength Finder after verification against the paper. Treat them with caution.

- **Critical Issue 3: "Conflation of dependence and faithfulness."** The harsh critic argues the deletion experiment tests only causal dependence while the paper draws conclusions about faithfulness. However, §4.3 explicitly connects the two, and this connection is standard in the literature (e.g., Lanham et al., 2023 also use deletion to probe faithfulness). The two concepts are related, and the paper's claims are appropriately scoped. *Removed as not a genuine weakness.*

- **"Magistrall vs Magistral typo":** The model name is spelled "Magistrall" in §2.2 (line 59) and "Magistral" elsewhere (abstract, figures). Per instructions, removed as a formatting/typographical issue.

- **"Overstates the gap" in introduction:** This is an opinion about framing, not a verifiable weakness about the paper's content. The paper cites relevant prior work and accurately characterizes the gap.

- **"5 prompts ambiguity":** The calibration section (§3.1) reports bootstrapping over 50 UG Physics questions with 5 re-runs, finding 5 prompts sufficient. While the phrasing is slightly ambiguous, this is a minor presentation detail that does not threaten any claim.

- **"40-60% threshold papers over variation":** The paper presents average trends with error bars. Summarizing a pattern with a range is standard practice. The variation visible in figures does not invalidate the overall pattern.

- **"Cramming implies intentionality":** The paper uses hedging language ("suggest that LLMs may draw on..." in §4.1) and acknowledges it does not probe internal mechanisms directly (§4.4). The term "cramming" is a descriptive label for the observed behavioral pattern, not a claim about intentionality.

- **Strength: "Domain-structured information overlap analysis"** from Strength Finder: The overlap metrics are simple bag-of-words measures that do not capture the structured nature of physics (equations, units, symbolic relations). This strength conflicts with verified weakness #2. *Removed.*

- **Strength: "Practical implication for early stopping"** from Strength Finder: This is a reasonable downstream implication but not a core strength of the paper's empirical contribution. *Removed.*

## Novel Insights

The most insightful observation emerging from the reviews is the base-rate confound in the information overlap analysis: because the set of "deleted spans" grows as the deletion fraction increases, rising overlap with the final answer is mechanically expected regardless of whether the model is genuinely reconstructing. This is not acknowledged in the paper and undermines a key piece of evidence for the cramming narrative. Beyond this, the reviews surface standard empirical concerns (judge validation, missing controls, statistical testing) that the paper should address but do not reveal fundamentally novel perspectives beyond what the paper itself contributes.

## Suggestions

1. **Validate the judge metric.** Report at least a Spearman correlation between Claude-4 scores and an objective correctness measure (exact match or symbolic verification) on a labeled subset. If correlation is high, the concern is addressed; if not, the paper should use the objective measure instead.

2. **Add base-rate control for overlap metrics.** Compare the reported overlap against overlap with a held-out CoT trace from a different problem at the same deletion rate, or normalize by the size of the deleted set.

3. **Strengthen the cramming evidence.** Instead of (or in addition to) bag-of-words overlap, check whether the correct numerical result or key equation appears in the final answer when it was deleted from the CoT. This would directly test physics-specific reconstruction.

4. **Include a truncation control.** Delete the same fraction of tokens from non-reasoning text inserted before the answer (not in the CoT) to isolate the effect of breaking the reasoning trace from general text corruption.

5. **Report dataset sizes for UG Physics and PhyBench.**

6. **Add statistical tests** for degradation thresholds across deletion strategies and models (e.g., confidence intervals on the crossover point).

---

## Calibration Details

### Round 1 (Bracketing)

**Queries:** All used "chain-of-thought faithfulness probing deletion LLM reasoning evaluation" with n=5 each.

| Path | Avg Score | Band | Comparison |
|------|-----------|------|------------|
| `pXIbcRPxWR.md` (Supervised CoT) | 2.50 | Weak | Much weaker — limited empirical scope |
| `jOuHjFw71C.md` (Planning in Strawberry Fields) | 3.00 | Weak | Weaker — narrow focus on o1 models |
| `JNZ3Om6NPS.md` (Inherent Limitations) | 2.00 | Weak | Much weaker — theoretical, little empirical |
| `v3DwQlyGbv.md` (Paramanu-Ganita) | 2.33 | Weak | Much weaker — small math LM |
| `RuY1r1PDdQ.md` (Instruction Following) | 3.00 | Weak | Weaker — different focus |
| **`1OyE9IK0kx.md` (Hardness of Faithful CoT)** | **5.00** | **Middle** | **Somewhat weaker — less methodological novelty** |
| **`awtd0XhzKQ.md` (FLARE)** | **5.75** | **Middle** | **Different contribution type, comparable quality** |
| **`w6nlcS8Kkn.md` (To CoT or not to CoT?)** | **6.67** | **Middle** | **Stronger — comprehensive meta-analysis, less evidential gaps** |
| `CIN2VRxPKU.md` (Deep Unlearning) | 5.33 | Middle | Different topic |
| **`rpbzBXdo4x.md` (Mind Your Step)** | **5.00** | **Middle** | **Comparable — similar evidential concerns** |
| `KIgaAqEFHW.md` (miniCTX) | 8.00 | Strong | Much stronger — polished, complete |
| `3bq3jsvcQ1.md` (Step Back) | 8.00 | Strong | Much stronger |
| `jOmk0uS1hl.md` (Training on Test Task) | 8.00 | Strong | Much stronger |
| `mMPMHWOdOy.md` (WizardMath) | 8.00 | Strong | Much stronger |
| `oYjPk8mqAV.md` (Magnushammer) | 8.00 | Strong | Much stronger |

**Round 1 bracket:** The paper sits between the weak band (2–3) and the strong band (8). Within the middle band, it is somewhat stronger than "Hardness of Faithful CoT" (5.00) and "Mind Your Step" (5.00) because of its novel methodology, but notably weaker than "To CoT or not to CoT?" (6.67) which is more comprehensive with fewer evidential gaps. **Initial bracket: 5.0–6.5.**

### Round 2 (Narrowing)

Queries: (1) "LLM evaluation metric judge validation physics reasoning benchmark" n=4, (2) "chain-of-thought deletion probing faithfulness robustness" n=4, (3) "empirical study CoT faithfulness LLM physics science" n=4.

| Path | Avg Score | Comparison |
|------|-----------|------------|
| `87YOFayjcG.md` (JudgeLM) | 5.25 | Different focus (training judges), comparable quality |
| **`u6jbcaCHqO.md` (SciBench)** | **5.60** | **Different contribution (benchmark), comparable quality level** |
| `jw2fC6REUB.md` (CURIE) | 6.40 | Stronger — cleaner evaluation, accepted |
| `WrBqgoseGL.md` (Putnam-AXIOM) | 5.80 | Stronger in execution, similar scope |
| **`asGQQc7gNo.md` (Factuality Enhancement)** | **6.67** | **Notably stronger — cleaner experiments, accepted** |
| `CIN2VRxPKU.md` (Deep Unlearning) | 5.33 | Different topic |
| `guyICBe4p1.md` (Truth-value judgment) | 5.67 | Different topic |
| `awtd0XhzKQ.md` (FLARE) | 5.75 | Different contribution type |
| `FP77VtEuaT.md` (3-SAT Reasoning) | 5.25 | Different focus, similar quality |

**Final score determination:** The paper is clearly stronger than the 2–3 band papers and clearly weaker than the 8.0 papers. Among the middle band, the paper is somewhat stronger than "Hardness of Faithful CoT" (5.00) due to its novel deletion framework and richer experimental design, but noticeably weaker than "To CoT or not to CoT?" (6.67) and "Is Factuality Enhancement a Free Lunch" (6.67) which have fewer evidential gaps. SciBench (5.60) and Putnam-AXIOM (5.80) are at a comparable quality level. The paper's novel methodology pushes it slightly above 5.0, but its significant evidential weaknesses (unvalidated judge, weak cramming evidence, missing controls) prevent it from reaching the 6+ range. **Final score: 5.5.**

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>
## Summary

This paper introduces a systematic deletion framework that intercepts chain-of-thought (CoT) traces mid-generation, removes tokens at controlled rates under three strategies (end, random, physics-aware), and measures downstream effects on accuracy, answer length, and lexical overlap. Evaluated across three open-source LLMs (Phi-4, Qwen-A3B, Magistral) and three physics benchmarks, the core empirical finding is that answer accuracy remains stable until approximately 40–60% of the CoT is deleted, while models compensate by producing longer final answers that reconstruct removed material — a pattern the paper terms "cramming." The paper argues that this reveals shallow and opportunistic reliance on CoT, and that accuracy-only evaluations are insufficient for scientific reasoning domains.

---

## Strengths

1. **Novel deletion framework applied to a structured scientific domain.** Intercepting CoT mid-generation and systematically sweeping deletion fractions (0–100%) under three explicit strategies is a clean, interpretable experimental design. Applying this to physics problem solving — where equations, units, and derivations provide a concrete grounding — is a legitimate and valuable extension of earlier CoT faithfulness work (Section 3.2, Figures 4–6).

2. **Empirical characterization of "cramming" is well-documented.** The X-shaped pattern in answer length versus deletion fraction appears consistently across all three models, all three benchmarks, and all three deletion strategies (Figures 5, 6, 11, C). This cross-validated behavioral phenomenon is a concrete empirical contribution that goes beyond prior accuracy-only evaluations.

3. **Multi-model, multi-benchmark design strengthens generalizability.** Three models spanning different architectures (dense 14B, 30.5B MoE, 24B) and three benchmarks of increasing difficulty (UG Physics, PhysReason, PhyBench) are tested under identical protocols. The qualitative consistency of findings across all nine model–benchmark pairs suggests the observed patterns are not artifacts of a single configuration (Sections 2.1–2.2, results throughout Sections 3–4).

4. **Physics-aware deletion provides domain-specific insight.** Tagging and selectively removing physics-structured content (equations, units) produces a larger accuracy drop than removing non-annotated content (Figure 3, Figure 14). This provides targeted evidence that structured scientific reasoning is especially critical for maintaining performance, which is a domain-specific finding that pure deletion of random tokens would miss.

5. **Convergence analysis for sample size calibration.** The paper verifies that 5 prompt runs per condition suffice to keep error bars below 10% via bootstrapping (Section 3.1, Figure 8 in appendix). This methodological discipline is not standard in the area and strengthens the reliability estimates.

---

## Weaknesses

### Fatal
None.

### Major

1. **Missing control condition weakens causal interpretation of the deletion intervention.** The paper frames retained accuracy under deletion as evidence that models "bypass" or "shallowly depend on" their CoT traces. However, forcing a model to continue decoding from a truncated or fragmented prompt is fundamentally a test of robustness to input corruption. The observed "cramming" (longer answers that fill the gap) is the behavior expected of any auto-regressive LM confronted with a broken context. Without a control that replaces deleted tokens with syntactically intact but semantically unrelated text (e.g., a shuffled version, or non-informative padding), the experiment cannot distinguish between (a) shallow reasoning bypassing and (b) general robustness to a broken prompt. The paper's interpretive claims about "faithfulness" are substantially weaker without this control. This does not invalidate the descriptive findings (accuracy retention under deletion is real), but it underdetermines the mechanism.

2. **No validation of the LLM-as-judge accuracy metric.** All accuracy/score results depend on a single LLM judge (Claude-4 Sonnet) using a 0–1 composite metric covering correctness, derivation accuracy, logic, formatting, and clarity. The paper provides no human validation, no inter-rater reliability check, and no analysis of the judge's sensitivity to answer length or structure. This is especially concerning because the paper's central behavioral finding ("cramming") involves longer answers. If the judge systematically favors or penalizes longer, more verbose outputs — a known bias in LLM judges — the Score metric is confounded with the very phenomenon the paper aims to characterize. A human-annotated subset (even 50–100 examples) or an alternative automated scoring approach would substantially improve confidence in the accuracy trends.

3. **Cramming is inferred solely from answer length without content verification.** The paper defines "cramming" as increased character count in final answers, and uses this as evidence that models "reconstruct missing reasoning steps." However, length alone does not establish that the lengthened answers contain correct physics reasoning rather than rambling, hedging, or incorrect filler. The paper does not sample or analyze whether the extended answers actually recover the missing equations, derivations, or units. Without content-level verification (human annotation or a structured rubric applied to a sample of high-deletion cases), the core phenomenon remains at the level of length change rather than verified reconstruction.

### Minor

4. **Overlap metrics are surface-level for a structured domain.** The Jaccard similarity and Manhattan distance operate on bag-of-words token sets. As the paper acknowledges, "E = mc²" and "Energy equals mass times the speed of light squared" have near-zero lexical overlap despite being semantically identical. Conversely, generic physics vocabulary (e.g., "force," "mass," "energy") can inflate overlap without indicating meaningful recovery of reasoning. The paper acknowledges this ("surface-level agreement") but then uses rising overlap to directly support the cramming narrative without treating the metric's weakness as a caveat on the findings. Metrics that capture equation structure (symbolic matching, dependency alignment) would be far more informative for a domain defined by mathematical manipulation.

5. **Accuracy of physics-aware deletion tagging is not reported.** The physics-aware deletion strategy relies on Claude-4 Sonnet to identify physics-structured spans for removal. The accuracy of this tagging is never evaluated. The results for this strategy are described as the "noisiest" with "flat overlap until late deletion," which could equally reflect noisy tagging rather than a distinct behavioral property. Reporting a simple precision/recall on a tagged sample would clarify whether the observed trends are domain effects or annotation artifacts.

6. **Framing overstates methodological novelty.** The introduction presents the deletion framework as "a new methodology" and "a novel evaluation paradigm." However, deletion-based probing of CoT faithfulness is well-established in the cited prior work (Lanham et al., 2023; Lyu et al., 2023), which performs perturbations — including deletions — of CoT traces and measures downstream effects. The paper's contribution is a legitimate and interesting extension (systematic deletion sweeps, application to a scientific domain, characterization of cramming), but it is not a new evaluation paradigm. Rescaling the framing to match what the paper actually delivers would improve accuracy without diminishing the value of the contribution.

### Trivial
- The paper sometimes refers to "PhyBench" in the text and "PhysBench" in figure captions (Figure 3). Minor consistency issue.

---

## Nice-to-Haves

- **Replace-deletion control:** The most impactful addition would be a condition where deleted CoT tokens are replaced with an unrelated but structurally intact passage (e.g., a weather report of comparable length and perplexity). If cramming still occurs, it is a text-completion artifact. If it does not, the phenomenon is specific to filling a semantic gap — still informative, and a much stronger signal.
- **Content validation of cramming:** A human-annotated analysis of 50–100 high-deletion examples, coding whether the extended answer actually recovers missing equations/derivations or is merely verbose, would substantially strengthen the paper's central claim.
- **Judge calibration study:** A human evaluation of even 100 examples to verify the LLM judge's scores correlate with human judgments of physics correctness.

---

## Removed Points

These points were raised in reviews but are removed from the main weakness list with brief justification:

- **"Statistical rigor — lack of significance tests" (Harsh Critic):** The paper reports standard errors and conducts a convergence analysis to calibrate sample size (Section 3.1). While formal hypothesis tests could add precision, reporting standard errors is standard practice in empirical LLM evaluation. This criticism is weak and removed.
- **"Fundamental confounding — the experiment is just testing robustness" (framed as fatal/structural by Harsh Critic):** This concern is retained above as a Major weakness because it weakens interpretation. It is removed from the Fatal tier because the paper's descriptive findings (accuracy retention, length increase) are real empirical observations regardless of the control question. The interpretive claims about "shallow dependence" are what is at stake, not the existence of the empirical patterns themselves.
- **Strength Finder's "Rigorous faithfulness analysis using lexical and frequency overlap":** The word "rigorous" overstates the strength of bag-of-words metrics for a structured domain. This strength is tempered in Strengths section above. The overlap analysis is retained as a supporting contribution with acknowledged limitations.
- **Any criticism about missing appendix content (proofs, figures, tables):** The parser strips appendix sections from all papers. These exist in the original submission and cannot be evaluated.
- **Reproducibility concerns about undisclosed hyperparameters or training logs:** Not relevant for an empirical evaluation paper where standard inference parameters are reported (temperature, top-p, nucleus sampling). The paper provides adequate detail for reproduction.

---

## Novel Insights

None beyond the paper's own contributions. The cross-validated documentation of the "cramming" pattern (longer final answers under CoT deletion, with X-shaped accuracy-length trade-off) is the paper's most genuinely novel empirical observation. The finding that this pattern is robust across three deletion strategies and three models is a useful contribution to the CoT faithfulness literature. However, the reviews do not surface a genuinely novel insight about the paper that the paper itself does not already articulate.

---

## Suggestions

1. **Add the replace-deletion control condition** (replace, don't delete, CoT tokens with unrelated text) and compare cramming behavior. This is the single most impactful experiment for strengthening the causal interpretation.
2. **Validate the LLM judge** on a human-annotated subset. A modest 50–100 example study would significantly increase confidence in all accuracy results.
3. **Sample and analyze the content of crammed answers** at high deletion levels. Code whether the lengthened responses actually recover correct physics steps or are merely verbose/incorrect. This turns "length increase" into a verified behavioral phenomenon.
4. **Tone down novelty framing** ("new evaluation paradigm" → "systematic extension of deletion-based faithfulness probing to scientific domains") to better match what is delivered.
5. **Add a symbolic-matching overlap metric** (e.g., equation structure alignment) alongside the bag-of-words metrics to better capture reasoning recovery in a mathematical domain.

---

## Score and Decision

### Calibration

**Round 1 (bracketing):** Searched for CoT faithfulness / deletion probing papers. Low-scoring anchors (avg 2.0–3.0) were papers with fundamental reasoning flaws or very narrow contributions. High-scoring anchors (avg 8.0+) were strong theoretical or comprehensive empirical papers. Mid-range anchors (avg 5.0–6.67) were most topically relevant. *Initial bracket: 4.5–6.5.*

**Round 2 (narrowing):** Retrieved additional anchors in the (3.5, 6.0) and (6.0, 7.5) bands.

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| pXIbcRPxWR (Supervised CoT) | 2.50 | R1 | Much weaker — purely theoretical, no experiments |
| lUyYX9VFgA (Code-of-Thought) | 3.00 | R1 | Narrower scope, less systematic |
| **1OyE9IK0kx (Hardness of Faithful CoT)** | **5.00** | R1/R2 | Most similar in topic; tests methods to improve faithfulness. Current paper has a more novel method (deletion sweeps vs. applying existing techniques) and richer empirical findings, but shares the weakness of unvalidated metrics. Current paper is somewhat stronger. |
| **rpbzBXdo4x (Mind Your Step)** | **5.00** | R2 | Studies when CoT hurts performance. Comparable quality — both have interesting empirical patterns but methodological gaps. Current paper has a more novel experimental design. |
| FP77VtEuaT (Can LLMs Reason? 3-SAT) | 5.25 | R2 | Theoretical framing, less applied. Comparable. |
| awtd0XhzKQ (FLARE) | 5.75 | R1/R2 | Proposes a neuro-symbolic method. Different type of contribution. |
| **w6nlcS8Kkn (To CoT or not to CoT?)** | **6.67** | R1/R2 | More comprehensive meta-analysis with carefully validated experiments. Current paper is weaker — less comprehensive, less validated metrics. |
| asGQQc7gNo (Factuality Enhancement) | 6.67 | R2 | Well-controlled experiments. Current paper is weaker. |
| GR0y0F3Ipd (MAPS) | 6.50 | R2 | Multi-modal physics. Different focus. |

The paper sits between the 5.00 anchors (methodological concerns limit confidence in interpretive claims) and the 6.67 anchors (comprehensive, well-validated). The most directly comparable anchor, "On the Hardness of Faithful CoT Reasoning" (5.00), is slightly weaker — the current paper has a more novel experimental protocol and richer findings. The 6.67 anchors are stronger on validation rigor. The paper's actual contributions (deletion framework applied to physics + cramming characterization) are real but the evidence base has gaps that prevent strong conclusions about CoT faithfulness.

**Final score: 5.5**

This paper has genuine empirical contributions (systematic deletion framework, cross-validated cramming characterization) but the evidence is weakened by three major issues: the lack of a control condition for the deletion intervention, an unvalidated LLM-as-judge metric, and cramming inferred from length alone without content verification. These gaps prevent the paper from making its interpretive claims stick, though the descriptive findings are useful. The paper would need the suggested experiments to reach acceptance level.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>
Now I have all the information needed. Let me write the consolidated review.

---

## Summary

This paper investigates *length volatility* in LLM long-form generation — the inconsistency in output length and structure when models are prompted with the same instruction multiple times. The authors introduce VOLTBench, a multi-dimensional benchmark using chapter-based tasks (story, code, dialogue, etc.) spanning up to 100K words to quantify volatility across 9 models and 4 training-free decoding baselines. They analyze attention traces to identify two internal failure patterns (Attention Collapse and Attention Instability), then propose SELB (Structural Enforcement via Logits Boosting), a training-free decoding intervention that forces section titles and suppresses early termination. SELB substantially improves length adherence and stability metrics, with mixed evidence on generation quality.

---

## Strengths

- **VOLTBench fills a genuine gap by measuring output stability rather than single-generation quality.** The benchmark evaluates models across multiple runs (N=5), multiple dimensions (language, complexity, format), and tasks spanning both unstructured (story, diary) and structured (code, math) generation, reaching up to 500 chapters / ~100K words. This multi-run stability evaluation is a meaningful departure from prior benchmarks that assess only single outputs, and the finding that even LongWriter-8B exhibits an LVC of 45.4% on a 100-section task provides compelling evidence that length volatility is a real, severe problem.

- **Comprehensive empirical baselining across 9 diverse models on a single benchmark.** The evaluation covers GPT-4o mini, Claude 3.5 Sonnet, DeepSeek-R1/V3, Qwen2.5 variants, Llama3.1-8B, Falcon3-Mamba-7B, and LongWriter-8B, plus training-free decoding baselines (Table 2). The systematic demonstration that *all* models fail to meet length targets beyond ~50 sections, and that fine-grained constraint adherence collapses past 100 sections (Section 4.3.1), provides a useful calibration of the current state of long-form generation.

- **SELB is simple, training-free, and demonstrably effective at enforcing length and structural adherence.** The method — boosting logits for section-title tokens at length thresholds and banning EOS/filler tokens — is straightforward to implement. Applied to Qwen2.5-7B, it boosts mean output from 445 to 15,651 words and reduces LVC from 17.0% to 14.02%. When applied to multiple base models (Qwen2.5-7B, Qwen3-8B, Llama3.1-8B), length curves closely track the target line (Figure 5), and the SELB-Hybrid variant (Appendix I) generalizes the approach to free-form generation achieving 97% MLA on a 20K-word novel task.

---

## Weaknesses

### Fatal

None.

### Major

- **The attention-trace analysis is too thin to support the claimed mechanistic insight, and the connection between probing and mitigation is tenuous.** Section 5 presents exactly two attention traces (one each for Qwen2.5-7B and Qwen2.5-3B on a single diary task with 40 sections) and identifies "Attention Collapse" and "Attention Instability" as internal failure patterns. No quantitative analysis is provided: no frequency statistics across seeds, tasks, or models; no correlational or causal tests linking attention patterns to output volatility; no control experiments. The attention metric \(\bar{\alpha}^{(t)}\) averages across all layers and heads, which is a coarse summary. Furthermore, SELB does not directly target these attention patterns — it mechanically forces section titles and blocks EOS tokens, an intervention that would work regardless of whether attention collapses or not. The paper claims it "targets identified internal patterns" (Abstract, Section 1), but this connection is not demonstrated.

- **Quality metrics do not show improvement over the base model, undermining the claim that SELB maintains or improves generation quality.** On the 100-section task (Table 2 vs. Section 6.3): base Qwen2.5-7B achieves UCA = 86.7% and SCA = 99.8%; SELB on the same model achieves UCA = 86.7% and SCA = 100%. The UCA is unchanged and SCA improvement is negligible (0.2 percentage points). The paper's quality claims rely on comparison to LongWriter-8B (different base model, UCA 66.7%, SCA 32.6%), but the direct same-model comparison shows SELB primarily improves length metrics — which it mechanically enforces — without detectable quality gains. This substantially weakens the paper's claim that SELB "maintains high generation quality" (Abstract) against a meaningful counterfactual.

- **The paper lacks comparisons to simple prompting-based structural enforcement and existing structured generation tools.** The benchmark's chapter-based format naturally lends itself to outline-based prompting (e.g., providing the model with a pre-specified chapter structure). Comparing SELB against such a baseline would clarify whether logit manipulation adds value beyond what the model can achieve when given the structure in the prompt. Similarly, structured generation libraries (e.g., Outlines, Guidance) that enforce JSON/section schemas through constrained decoding are not discussed or compared. These omissions make it difficult to assess whether SELB's forced-token approach is necessary or beneficial.

### Minor

- **The benchmark's length target uses minimum per-chapter word counts rather than exact targets, creating ambiguity in the MLA metric.** The instruction format specifies "a minimum of N words for each chapter" (Section 3.1), making \(L_{\text{constraint}}\) a floor. The MLA metric compares mean length to this floor, so models that exceed the minimum are not penalized, and the metric conflates length adherence with natural content expansion. This does not invalidate the benchmark — models still dramatically undershoot even the floor — but it makes MLA harder to interpret for models that do meet the minimum.

- **Lookahead Decoding is an odd choice as a length-control baseline and its inclusion is not justified.** Lookahead Decoding is a speculative decoding method designed for inference speed, not for length control or structural adherence. The paper (Section 4.1) describes it as "designed to optimize the generation trajectory by anticipating future probabilities" but provides no rationale for why it is a meaningful comparator for length volatility. Its inclusion as one of only four training-free baselines weakens the baseline set.

- **Baseline hyperparameters are not specified in the main paper.** The Reproduction Penalty, Entropy-Based Stopping, Length Constraint, and Lookahead Decoding baselines are described only in one sentence each (Section 4.1) without any hyperparameter details, adaptation methodology for chapter-based tasks, or sensitivity analysis. This limits reproducibility of the baseline results.

- **The free-form generation results (SELB-Hybrid) are described only in a few sentences (Section 6.4) and relegated to Appendix I.** This is the paper's primary evidence that SELB generalizes beyond chapter-based tasks, yet the main body provides no experimental details, no comparison to baselines on the same free-form task, and no quality evaluation beyond MLA and LVC. The abstract and conclusion give the impression that SELB broadly improves long-form generation, but the main-paper evidence is restricted to structured chapter tasks.

### Trivial

- The paper refers to Figure 2 in Section 5 when describing the attention analysis (line 246: "As shown in Figure 2"), but the relevant figure is Figure 4.

---

## Nice-to-Haves

- Human evaluation of output quality for SELB-generated text would substantially strengthen the quality claims, given that LLM-as-judge (UCA) is used for unstructured content at extreme lengths where judge models may lose context.
- Applying SELB to LongWriter-8B (same base model family as Llama3.1-8B) would provide a controlled comparison between the training-based and decoding-based approaches to long-form generation.
- Quantitative analysis of how frequently attention collapse/instability patterns occur across different seeds, tasks, and models would elevate the probing from anecdotal to systematic.

---

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"The benchmark design makes evaluation circular" (Harsh Critic Claim 1, partially):** The claim that the benchmark is *entirely* circular is overstated. The benchmark establishes real failure modes (models cannot produce required amounts of content), and SELB addresses these modes. The evaluation metrics do reward what SELB enforces, but this is true of any targeted mitigation. The *quality* metrics (UCA, SCA) are more independent. However, the core concern — that quality metrics do not improve over the base model — has been reframed as a Major weakness above rather than dismissed.
- **"SELB inevitably achieves near-perfect MLA, LVC, and FAD" (Harsh Critic):** This is true for the structural metrics, but it's the *point* of the method. The real question is whether quality is maintained, which we address separately. Removed as a standalone criticism because it's inherent to the method's design and not an evaluation flaw per se.
- **"The comparison with LongWriter-8B is unfair because base models differ" (Harsh Critic):** The paper *does* provide within-model comparisons (Qwen2.5-7B vs. Qwen2.5-7B+SELB in Table 2; Qwen3-8B and Llama3.1-8B with/without SELB in Figure 5). The LongWriter-8B comparison is supplementary. The criticism is weakened because the paper includes the appropriate controls. Removed.
- **"The paper provides no hyperparameters for baselines" (Harsh Critic, moved):** Kept above as a Minor weakness rather than removed, since it's a legitimate reproducibility concern.
- **"SCA is trivially maximized by forced structure" (Harsh Critic):** SCA measures content correctness via execution-based verification, not format adherence. A forced structure with incorrect code would score low SCA. The metric is more independent than the critic suggests. Removed as a standalone point.
- **"The benchmark lacks total number of distinct prompts, sampling mechanism details" (Harsh Critic):** These are minor methodological details that would be nice to have but don't undermine the core findings. Moved to Nice-to-Haves implicitly through the general reproducibility note.
- **Strength Finder: "Attention-trace analysis identifies reproducible internal failure patterns"**: The word "reproducible" is not supported by the evidence (only two examples). This strength has been dropped.
- **Strength Finder: "The benchmark's chapter-based structure scales to unprecedented lengths"**: This is accurate but already captured under the benchmark strength. No need to duplicate.

---

## Novel Insights

The paper's most novel empirical insight is the systematic demonstration that *all* current models — including those specifically fine-tuned for long-form generation (LongWriter-8B) — exhibit severe length volatility, with the failure rate crossing 50% at merely 50 sections and becoming universal beyond 100 sections. The observation that models exhibit two distinct failure modes (premature termination via persona reversion, and section skipping) is useful for the community. However, the attention-trace analysis does not rise to the level of novel mechanistic insight given its anecdotal nature.

---

## Suggestions

- **Decouple quality evaluation from length enforcement.** Report quality metrics at multiple length buckets (e.g., at 10K, 50K, 100K words) to show whether SELB degrades quality as length scales, rather than reporting a single aggregate score. This would provide a more honest picture of the length-quality trade-off.
- **Add a simple prompting baseline.** Compare SELB against giving the model a pre-written chapter outline in the prompt ("Chapter 1: [topic], Chapter 2: [topic], ..."). If the model can achieve reasonable results with a prompted outline, it raises the bar for what SELB needs to demonstrate.
- **Scale back the probing claims.** The attention analysis is better framed as an exploratory observation than as an "in-depth investigation" revealing causal mechanisms. Acknowledging its limitations would strengthen the paper's credibility.

---

## Score and Decision

**Anchor comparison:**

| Anchor | Avg Score | Comparison to Paper Under Review |
|---|---|---|
| ExpertLongBench (`nJvgBolRcR`) | 5.50 | Stronger: expert-validated benchmark with novel CLEAR evaluation framework; higher methodological rigor. This paper's benchmark is broader in dimensions but weaker in validation, and its probing/mitigation are less developed. |
| Beyond Fixed / DAEDAL (`Ic2A2gCseC`) | 6.00 | Stronger: simple, well-ablated method with clear efficiency gains; thorough hyperparameter analysis. This paper's mitigation is similarly simple but has less thorough ablation and weaker quality evidence. |
| Deco-G (`XMb9poL2Mo`) | 4.00 | Comparable: novel decoding framework with interesting idea but missing baselines and limited generalization evidence. Similar pattern of strengths (real technical contribution) and weaknesses (incomplete evaluation). |
| SagaScale (`bYpSLBk8H8`) | 3.50 | This paper is somewhat stronger: broader model coverage, more dimensions, and a mitigation component. SagaScale had fundamental QA pipeline flaws. |
| LIFESTATE-BENCH (`cGlvmqZlox`) | 3.00 | This paper is clearly stronger: larger scale, more models, more dimensions, and includes a mitigation method beyond pure benchmarking. |
| Attend or Perish (`jHPCXOi9LU`) | 2.50 | This paper is clearly stronger: more comprehensive empirical contribution and practical relevance. |

The paper makes a genuine contribution in establishing length volatility as a measurable, severe problem through VOLTBench and its multi-model evaluation. However, the probing is too thin to support mechanistic claims, the mitigation's quality evidence does not show gains over the base model, and key baselines are missing. The paper reads as a solid benchmark paper with underdeveloped probing and mitigation layers grafted on. This places it in the 4.0 range — a contribution with real empirical value but significant methodological gaps that prevent a higher score.

MY FINAL SCORE: <pineapple>4.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>
Now I have all the information I need to produce the consolidated review. Let me compile my findings.

**Calibration Summary:**

**Round 1 — Bracketing:** I first queried across three bands. The weak anchors (avg < 3.5) were four papers scoring 2.67–3.00 — mostly rejected papers on contamination/LLM evaluation with shallow contributions. The middle anchors (3.5–7.5) included papers scoring 4.67–5.50 on contamination topics. The strong anchors (avg > 7.5) were on unrelated LLM evaluation topics (multi-turn conversation, agent benchmarks, multimodal reasoning).
- **Initial Bracket:** 5.0 – 7.5. The paper is clearly above the reject-level 3.0 papers and above the 4.67 "Impact of Post-training on Data Contamination" paper (which had narrower scope, no detection evaluation, smaller models). It is below the unrelated 8.0 papers on different topics.

**Round 2 — Narrowing:** I queried inside the (4.5, 6.5) and (5.5, 7.5) bands for more contamination-specific anchors.
- **GFDSGlEks2 (avg 4.67, Reject):** Closest competitor — studies GRPO+SFT contamination, but only 2 models (0.5B–4B), no detection methods evaluated, no theoretical analysis. The paper under review is substantially stronger.
- **EjiJmiA6ea (avg 5.33, Accept Poster):** Proposes Self-Critique method for RL contamination detection. Method paper; the current paper is an analysis with a different contribution style.
- **grIvSXVJ65 (avg 6.50, Accept Poster):** "Preference Leakage" — identifies a contamination problem in LLM-as-a-judge with comprehensive experiments. Closest in style. The paper under review has broader scope (two stages, more detection methods, theoretical grounding) and comparable experimental rigor.
- **YlpaaYxx4t (avg 5.33, Accept Poster):** Proposes CoDeC detection method. Different contribution type.

The paper under review is stronger than the 4.67 and 5.33 anchors and comparable to the 6.50 anchor. I place it at **6.5**.

Now here is the consolidated review:

## Summary
2-3 sentence summary of the paper's contribution.

## Strengths
- strength 1 with evidence
- strength 2 with evidence

## Weaknesses
### Fatal
None.

### Major
None.

### Minor
...

### Trivial
...

## Nice-to-Haves

## Removed Points

## Novel Insights

## Suggestions

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>

Let me draft the review.Now I have all the evidence needed. Let me produce the consolidated review.

---

## Summary

This paper presents the first systematic study of benchmark contamination detection in the context of large reasoning models (LRMs), structured around two realistic contamination scenarios: Stage I, where contamination is introduced during SFT on the base model but can be concealed by subsequent GRPO/RL training; and Stage II, where contamination with CoT is applied as a final SFT step on an already-advanced LRM and barely leaves detectable evidence. The paper evaluates 10 detection methods across multiple benchmarks and base models, provides theoretical analysis attributing concealment in Stage I to PPO-style importance sampling and clipping, and concludes that existing detection methods are fragile in both scenarios.

## Strengths

1. **First systematic study of benchmark contamination in LRMs covering two critical training stages.** The paper structures contamination around two realistic points in the LRM development pipeline (pre-LRM SFT→RL and post-LRM final SFT), with explicitly designed contamination pipelines and empirical evaluation for each. This framing is novel and directly addresses the gap left by prior work, which studied contamination only in standard LLMs without considering the multi-stage training pipeline of reasoning models. (Section 1, Figure 1)

2. **Theoretical analysis identifying PPO-style importance sampling and clipping as the root cause of contamination concealment.** Theorem 3.1 (Section 3.2) decomposes the NLL gap into a mean drift term (μ) and a covariance term (β), and provides a formal argument that the covariance term driven by importance sampling and clipping contracts the member/non-member separability. This goes beyond previous empirical observations to offer a mechanistic explanation for the concealment phenomenon.

3. **Empirical demonstration that GRPO on clean data conceals SFT contamination evidence while preserving performance inflation.** Table 2 shows systematic AUROC drops across all 10 detection methods after GRPO (e.g., Min-K% dropping from 74.96% to 61.27%, Max-K% dropping from 69.83% to 52.35%). Figure 2 shows a monotonic decline with more GRPO steps, while Table 1 confirms that performance inflation persists (7.14% above the clean SFT baseline), ruling out the alternative explanation that the model simply forgets the contaminated data during subsequent training.

4. **Controlled ablation isolating the clipping mechanism.** Table 3 shows that removing the clipping term from GRPO and RAFT++ restores Loss-detector AUROC to near pre-RL levels (GRPO without clipping: 73.28% vs. with clipping: 61.26%), while plain RAFT (no importance sampling/clipping) does not reduce detectability (77.51%). This cleanly validates the theoretical prediction.

5. **Demonstration that CoT contamination on advanced LRMs leaves detection near random across diverse models.** Table 5 reports AUROC values close to 50% for nearly all method–benchmark–model combinations across four LRM families (DeepSeek-R1-Distill-Llama-8B, DeepSeek-R1-Distill-Qwen-7B/14B, OpenThink-7B). Figure 4 shows that the log-prob distributions of both members and non-members increase at a similar margin after contamination, empirically demonstrating why memorization-based detectors fail.

6. **Comprehensive evaluation across 10 detection methods and 6 hard reasoning benchmarks.** The paper spans generation-based, perturbation-based, reference-based, and reference-free detectors (LiRA, CDD, Min-K%, Max-K%, Loss, etc.) on benchmarks including GPQA, AIME24/25, OlympiadBench, and AMC23, covering both multiple-choice and free-form math problems across two base model families (Qwen2.5-7B, Llama-3.1-8B).

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

1. **The "near random guess" framing for Stage II is slightly imprecise for a few method–benchmark combinations.** The paper repeatedly states that "almost all detection approaches consistently perform near random guess" in Stage II. While the overall averages are low (e.g., LiRA averages 58.74% across benchmarks), individual cells reach moderate AUROC values (e.g., LiRA on AIME24 with DS Llama-8B: 75.33%; Min-K% on AIME24 with DS Llama-8B: 72.67%; Loss on AIME24 with DS Llama-8B: 73.56%). The broader conclusion that detection is substantially degraded stands, but the framing elides that some detection methods retain modest signal on specific benchmarks. The paper uses hedged language ("almost all," "most") but could more precisely report per-method averages (e.g., "the best method averages 62.6%") rather than saying "near random guess," which conflates values in the 50–65% range with truly random 50% performance. This is a precision issue, not a structural flaw.

2. **The generality claim about "a broad class of RL methods" is supported by a single mechanism demonstrated in two algorithms (GRPO and RAFT++).** The paper's theoretical analysis is specific to PPO-style clipping/importance-sampling objectives. The claim that "a broad class of RL methods may inherently exhibit similar concealment capability" (Abstract, Section 3.2.1) is couched with "may" and "suggests," and the ablation of removing clipping from GRPO/RAFT++ convincingly identifies the mechanism. However, the paper provides no empirical test of any additional RL algorithm without clipping (e.g., vanilla policy gradient, DPO variants). While the conclusion is a reasonable inference, the empirical support for the "broad class" framing rests on exactly two algorithms with the same clipping structure. One additional negative control (an RL method lacking this mechanism) or a more explicitly scoped claim would strengthen the paper.

3. **The theoretical analysis (Section 3.2) operates under strong simplifying assumptions that are not discussed as limitations.** The paper correctly notes that the analysis uses "a tabular setting for simplicity" and assumes "small natural gradient steps" and "no standard deviation in GRPO advantage." However, it does not discuss how these assumptions affect the generality of the theoretical conclusions or what would need to be relaxed to extend the analysis to neural networks with function approximation. The empirical ablation (Table 3) validates the qualitative prediction, which is good, but a brief limitations paragraph would prevent readers from over-interpreting the theoretical formality.

### Trivial

- The caption for Figure 2 in the parsed PDF describes itself recursively rather than providing the actual caption content — this is a parser artifact, but in the original submission the authors should ensure figure captions are self-contained.
- The paper's Stage II discussion about generalization vs. memorization (Section 4) is thoughtful but brief; a short paragraph tying this more explicitly to the distribution-shift literature could enrich the analysis.

## Nice-to-Haves

- **Confidence intervals or error bars for AUROC values.** Given that many Stage II values cluster around 50–60%, bootstrapped confidence intervals would clarify which results are meaningfully above chance. Not required (single-run evaluation is standard in this setting), but would strengthen the claims.
- **Clarification in the main text about the source of CoT trajectories for Stage II contamination.** The paper mentions SFT contamination with CoT but does not state explicitly in the main text whether CoT is generated by the same LRM (self-distillation) or an external source. This detail is likely in the appendix (removed by the parser), but a brief mention in Section 4 would aid readability.
- **Reporting the number of SFT steps or tokens used for the "extensive" contamination in Stage II** (Table 4/5) would improve reproducibility.

## Removed Points

The following points were identified by reviewers but removed per the filtering rules:

- **Criticism about "more GRPO steps" claim not being directly shown**: The paper says "we expect" (line 98), which is a prediction, not a conclusion. The critic's reading that this was presented as a definitive conclusion is incorrect. *(Removed: factually incorrect — the paper already frames it as an expectation.)*
- **Criticism about missing statistical significance / confidence intervals**: Moved to Nice-to-Haves, as single-run AUROC reporting without confidence intervals is standard practice in the LLM evaluation literature. *(Removed: demand for a standard not required by the community's norms.)*
- **Criticism about contamination data generator source for CoT**: The appendix (removed by parser) likely contains this. Not available to verify. *(Removed: parser artifact — appendix was stripped.)*
- **Various formatting/style nitpicks, spelling/grammar concerns**: These are parser artifacts from PDF extraction, not author errors. *(Removed: parser errors.)*
- **Strength from Strength Finder about logging being "the first systematic study"**: While the paper makes this claim and it appears valid given the literature reviewed, I note that "first" claims are inherently hard to verify. The strength is retained because the paper's two-stage framework is clearly novel relative to prior work on contamination in standard LLMs.
- **Strength about "the problem being important"**: Moved out as generic — the importance is implicit in the retained strengths.

## Novel Insights

None beyond the paper's own contributions. The reviews did not surface an observation about the paper that the paper itself does not make.

## Suggestions

1. **Tighten the Stage II language.** Replace "near random guess" with language like "most methods average 50–60% AUROC, with the best method (LiRA) averaging just 62.6% across benchmarks." Report per-method averages in the text to give readers a precise characterization.
2. **Soften or qualify the "broad class of RL methods" claim.** Explicitly scope the claim to "RL methods that use PPO-style importance sampling with clipping (such as GRPO and RAFT++)" and note that testing additional algorithms is left as future work.
3. **Add a brief limitations paragraph to Section 3.2** acknowledging the simplifying assumptions of the theoretical analysis and noting that extension to neural network function approximation is an open direction.
4. **Add bootstrapped confidence intervals** to the key AUROC tables (Tables 2, 3, 5) to quantify uncertainty, especially for Stage II results that are near chance.
5. **Include a sentence in Section 4's main text** specifying the source of CoT trajectories used for Stage II contamination.

## Score and Decision

**Calibration Anchors (all rounds):**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| WERLf030OU (LogProber) | 3.00 | 1 | Reject-quality contamination detection paper; much narrower scope and impact |
| Ubi631nNbI (DVD) | 3.00 | 1 | Reject; proposes a detection method for variant contamination; less comprehensive |
| pW7ORPqwzG (Epidemiology of LLMs) | 3.00 | 1 | Reject; benchmark paper on distribution knowledge, not directly about contamination |
| uDP3P9TTRA (LogiEval) | 2.67 | 1 | Reject; logical reasoning benchmark; different topic, lower quality |
| **GFDSGlEks2** (Impact of Post-training on Contamination) | **4.67** | 1,2 | **Most directly comparable — same topic (GRPO+contamination). Paper under review is substantially stronger: more detection methods (10 vs 0), theoretical analysis, larger models (7B/8B vs 0.5B–4B), two stages. Clear step up.** |
| WFGxFzFDmQ (Watermarking) | 5.00 | 1 | Reject; proposes benchmark watermarking. Different contribution type. |
| 29ETLxTQAN (CapBencher) | 5.50 | 1 | Reject; proposes benchmark release methodology with randomization. Different contribution. |
| **YlpaaYxx4t** (CoDeC) | **5.33** | 1 | **Accept (Poster); method paper for contamination detection via ICL. Under review is a different contribution type (analysis vs method) but comparable rigor.** |
| **EjiJmiA6ea** (Self-Critique for RL Contamination) | **5.33** | 2 | **Accept (Poster); similar topic (contamination in RL post-training). Method paper proposing Self-Critique. Under review has broader scope (2 stages vs 1, more detection methods).** |
| UKOqoULbZS (GFPO) | 6.00 | 2 | Accept (Poster); proposes GRPO variant. Different topic (RL optimization for conciseness). |
| d5qElNtXS5 (Info-GRPO) | 4.67 | 2 | Reject; proposes GRPO variant. Different topic. |
| **grIvSXVJ65** (Preference Leakage) | **6.50** | 2 | **Accept (Poster); identifies contamination problem in LLM-as-a-judge. Closest in style —problem-finding empirical study. Under review has comparable methodology breadth and stronger theoretical backing.** |
| cReExMQLiK (Micro-Benchmarking Reliability) | 6.50 | 2 | Accept (Oral); meta-evaluation of benchmarking. Different topic but similar empirical rigor. |
| QD0cuAmi9z (Benchmark Signatures) | 6.50 | 2 | Accept (Poster); benchmark overlap analysis. Different topic. |
| HyZwf1rt4s (AI Text Detection) | 6.00 | 2 | Accept (Poster); AI text detection in peer review. Different topic. |

**Round 1 bracket:** The paper clearly sits above the 3.0-level reject papers and above the 4.67 closely related contamination paper (which was weaker in scope, models, and depth). The upper bound was unclear from round 1 alone.

**Round 2 narrowing:** Against the 5.33 RL contamination detection paper (accepted poster), the under-review paper has broader scope, more detection methods, and theoretical analysis. Against the 6.50 Preference Leakage paper (accepted poster) — the closest stylistic match as a problem-finding empirical study — the under-review paper is comparable in empirical comprehensiveness while adding theoretical analysis. The paper is stronger than the 4.67 and 5.33 contamination anchors; it sits at or slightly above the 6.0–6.50 level.

**Final score:** 6.5. The paper's contributions are solid, timely, and well-supported. The weaknesses are minor and addressable. The paper does not have any fatal or even major flaws.

**MY FINAL SCORE: <score>6.5</score>**
**MY FINAL DECISION: <decision>Accept</decision>**
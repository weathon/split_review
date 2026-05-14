Now I have all the information I need. Let me compose the final consolidated review.

## Summary

This paper investigates whether LLMs exhibit a human-like inductive bias toward Information Bottleneck (IB) efficiency in semantic categorization. Using color naming as a testbed, the authors conduct two studies: (1) an English color-naming evaluation across 39 LLMs (6 families), finding that larger instruction-tuned models achieve better IB-efficiency and English-alignment; and (2) a novel Iterated In-Context Language Learning (IICLL) paradigm simulating cultural transmission, showing that some LLMs restructure initially random category systems toward greater IB-efficiency. The headline result is that Gemini 2.0 recapitulates the full range of near-optimal IB tradeoffs observed in human iterated learning, while other strong models (Gemma 3 27B, Qwen 2.5 32B) converge to low-complexity solutions.

## Strengths

- **Well-motivated theoretical framework.** The IB framework for semantic categories (Zaslavsky et al., 2018) is established and defensible, and applying it to analyze LLM color categorization is a natural and productive extension. The paper correctly identifies color as a uniquely rich domain due to available cross-linguistic data and cultural evolution experiments (WCS, Xu et al. 2013).

- **Comprehensive model survey.** Testing 39 models across 6 families with varying sizes, training stages, and modalities provides useful descriptive information about which models succeed or fail at English color naming. The analysis of Olmo 2's training trajectory (Appendix F) is a nice addition, showing that instruction-tuning drives the largest improvement in alignment.

- **Novel IICLL paradigm.** Extending iterated language learning to LLMs via in-context learning is a methodologically interesting adaptation. The careful replication of Xu et al. (2013)'s conditions (vocabulary sizes, chain length, stimuli) enables direct comparison between human and LLM cultural evolution, which goes beyond prior I-ICL work (Zhu & Griffiths, 2024).

- **Instruction-tuning finding.** The paper provides evidence that instruction-tuning (not just model scale) is critical for human-like color categories — base models of all sizes fail, while instruction-tuned variants of the same models often succeed.

- **Nearest-neighbor baseline.** Appendix M shows that Gemini's evolved systems outperform a feature-based NN classifier on IB-efficiency and human-language alignment in the most challenging condition (k=14), ruling out the trivial explanation that the results come from simple feature clustering.

## Weaknesses

### Fatal
None.

### Major

- **The central result depends on a single proprietary model.** The claim that LLMs exhibit a "human-like inductive bias toward IB-efficiency" is empirically demonstrated at this level only by Gemini 2.0 — a closed-weight model whose training data and architecture are unknown. Other strong open models (Gemma 3 27B, Qwen 2.5 32B) converge to low-complexity solutions. The paper is transparent about this ("only the model with strongest in-context capabilities"), but the abstract and title frame the finding as a general property of LLMs. This makes the headline result a single-model existence proof rather than a broadly-supported claim about LLM inductive biases. Replication with additional capable models (e.g., Llama 3.3 70B, GPT-4) would be needed to establish generality.

- **The IICLL paradigm's connection to Bayesian iterated learning theory is asserted but not established.** Section 2.3 correctly notes that Griffiths & Kalish (2007) showed that under specific conditions (Bayesian agents sharing priors/likelihoods), iterated learning converges to the prior distribution. However, the paper provides no argument that LLMs performing in-context classification with a sliding window of 10 interactions satisfy these conditions. The paper uses the IL framework as motivation, which is reasonable as an experimental paradigm, but the claim that IICLL "reveals inductive biases" in the formal Bayesian sense is not supported by the analysis. The paper would benefit from acknowledging this gap more explicitly and clarifying what kind of evidence IICLL can and cannot provide.

### Minor

- **No statistical inference.** The paper reports no confidence intervals, standard errors, or significance tests for any of the key comparisons — e.g., whether Gemini's final IICLL systems are statistically significantly more efficient than the NN baseline, or whether the differences between Gemini and other models are significant. Given the small number of chains (20 for humans, one per condition per model), this limits the ability to assess the reliability of results.

- **sRGB encoding confound is acknowledged but not resolved.** The paper shows in Appendix C that all models perform significantly worse with CIELAB inputs, and the main IICLL study uses sRGB coordinates. While the paper is transparent about this and cites prior work with the same observation (Marjieh et al., 2024), it remains a limitation: the results depend on a specific numerical encoding that the model may have statistical associations with from training data. This weakens the claim that the bias is *perceptually grounded*.

- **Missing prompt-following control for base models.** The paper notes that many base models fail to produce coherent category structure (Section 4.1), but does not check whether these models can follow the constrained classification prompt at all. Without this control, it is unclear whether failures reflect lack of color knowledge, inability to follow output format constraints, or other issues.

- **Limited analysis of why some models succeed and others fail.** The paper identifies instruction-tuning as a correlate of success but does not investigate the mechanism. Why does Gemini succeed where other instruction-tuned models fail? Is it data, scale, architecture, or something else? The paper rightly flags this as future work, but the question is central to interpreting the main result.

### Trivial

- The sliding window size (k=10) is justified by a brief exploration (Appendix K) comparing windows 0, 10, 20, 50. While this is sufficient for a design choice, a more systematic ablation would strengthen the paper.

- The non-color domain replication (mentioned in the abstract and Section 5) is reported as done with Gemini only, with no details. This is acknowledged as preliminary but the current evidence for domain generality is essentially absent.

## Nice-to-Haves

- **Prompt-following control experiment:** Testing all models on a simple constrained classification task (unrelated to color) to verify that base models failing at color naming can follow the required output format.

- **Systematic window-size ablation for IICLL** to quantify how much of the convergence to IB-efficiency is driven by the explicit memory mechanism vs. the LLM's internal processing.

- **Replication of IICLL with additional capable open-weight models** (e.g., Llama 3.3 70B, GPT-4o, Mixtral) to assess generality beyond Gemini.

- **Formal analysis of whether IICLL dynamics reflect learning vs. amplification of regularities**, e.g., by comparing the category systems produced by IICLL to the set of all possible partitions consistent with the training data.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Criticism that "the paper never rules out the trivial explanation that IICLL is amplifying structure already present in the training data."** — The paper explicitly addresses this via the nearest-neighbor baseline (Appendix M), showing Gemini outperforms it. The NN baseline comparison directly addresses this concern. Also, the IICLL process starts from *random* initial systems, so any structure is generated by the LLM.

- **Claim that "Section 1: LLMs are not trained for the IB objective is misleading because next-token prediction implicitly encourages compression."** — The paper acknowledges this in lines 339-340 ("neither humans nor LLMs are explicitly trained for optimizing the IB objective, suggesting that IB-efficiency may emerge to support intelligent behavior"). The paper's claim is about explicit IB training, which is accurate.

- **Criticism that the nearest-neighbor baseline is insufficient and a "random classifier" should be used.** — The NN baseline is a reasonable and standard baseline. The paper also initializes IICLL with random systems, so random classifier comparisons would add little.

- **Various formatting/style nitpicks.** — These are parser artifacts, not author errors.

- **Missing related work criticisms.** — Cannot confirm without external search capability; per instructions, do not mention these.

## Novel Insights

The harsh critic and strength finder converge on one genuinely novel observation not foregrounded in the paper itself: the finding that instruction-tuning is necessary but not sufficient for human-like IB-efficient categorization. Many instruction-tuned models (Gemma 3 27B, Qwen 2.5 32B) perform well on English color naming but still collapse to low-complexity solutions under IICLL pressure. This creates an interesting dissociation — English naming ability does not predict IICLL outcome — which suggests that the IICLL paradigm is measuring something distinct from linguistic knowledge. The paper does not dwell on this dissociation, but it is arguably as important as the Gemini result: it means that cultural evolution pressure (via IICLL) separates models along a dimension that standard evaluations do not capture.

## Suggestions

1. **Tone down the general claims.** Replace "LLMs exhibit a human-like inductive bias toward IB-efficiency" with more precise language: "some LLMs (in particular Gemini 2.0) exhibit..." or "the most capable instruction-tuned models can exhibit..." throughout the abstract and introduction. The current framing oversells the generality.

2. **Add statistical tests.** Report confidence intervals or bootstrapped estimates for the key comparisons in Figures 3 and 4. This is standard practice and would significantly strengthen the paper.

3. **Discuss the theory-practice gap in Section 2.3 more honestly.** Acknowledge that IICLL does not satisfy the formal conditions for convergence to the prior (Bayesian agents, shared likelihoods) and clarify that the IL framework is used as an *experimental paradigm* for studying bias amplification, not as a formal proof about the LLM's prior.

4. **Consider adding the dissociation between English naming and IICLL performance as a distinct finding.** This negative result (strong naming ≠ strong IICLL) is informative and would make the paper's contribution more nuanced and interesting even without additional model replications.

## Score and Decision

### Calibration Anchors

| Anchor Path | Avg Score | Comparison |
|---|---|---|
| `/home/wg25r/review_agent/human_reviews_2026/3YKeB9R1g9.md` (Scaling with Collapse) | 8.00 | Much stronger empirical support with clean, reproducible results across multiple scales. The current paper has a more interesting cognitive question but weaker evidence. |
| `/home/wg25r/review_agent/human_reviews_2026/rkthPeHvAX.md` (From Tokens to Thoughts) | 6.00 | Similar use of IB to compare humans and LLMs. That paper had 40+ models and was accepted as poster. Current paper has a novel IICLL paradigm but weaker central evidence (single-model dependence). Comparable overall quality but slightly weaker on evidence. |
| `/home/wg25r/review_agent/human_reviews_2026/nM2QhvybwI.md` (Cognitive models can reveal...) | 7.00 | Strong theoretical framing with clear, well-supported results across multiple models. Current paper has similar theoretical ambition but less robust empirical support. |
| `/home/wg25r/review_agent/human_reviews_2026/bIS0BbYjjd.md` (Is In-Context Learning Learning?) | 4.80 | Thorough empirical study (1.89M predictions) but narrower scope. Current paper has broader interest and a more novel paradigm, but similar evidential limitations. |
| `/home/wg25r/review_agent/human_reviews_2026/tvDlQj0GZB.md` (Learning is Forgetting) | 3.50 | IB framework applied to LLMs but limited novelty. Current paper has stronger novelty (IICLL) and empirical breadth. |
| `/home/wg25r/review_agent/human_reviews_2026/zy06mHNoO2.md` (Emergence of Machine Language) | 3.50 | Novel question but limited analysis. Current paper has more rigorous evaluation and stronger theoretical grounding. |
| `/home/wg25r/review_agent/human_reviews_2026/crjpuxuvs6.md` (What is the Color of RED?) | 3.00 | Interesting finding but limited novelty. Current paper has stronger theoretical contribution and broader scope. |
| `/home/wg25r/review_agent/human_reviews_2026/mnfqJQSd6B.md` (Color Names in Vision-Language Models) | 2.00 | Pure observational study of color naming with limited insight. Current paper goes much further with IB analysis and IICLL. |

### Calibration

The paper is stronger than the 2.00-3.00 band papers (pure color description studies) because it introduces a novel paradigm (IICLL) and a well-motivated theoretical framework (IB). It is comparable to the 4.80-6.00 band papers in terms of ambition and scope, but weaker than the 7.00-8.00 band papers in terms of evidence robustness. The central limitation — dependence on a single closed-weight model for the headline result — prevents it from reaching the 6+ range. Positioned against "From Tokens to Thoughts" (6.00) which had a similar IB-based comparison with 40+ models, the current paper has a more novel experimental paradigm but weaker central evidence. This justifies a score slightly below that anchor.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>
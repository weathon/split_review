---
job_id: ec037505-0250-4db8-a1db-dd3d6daeedaa
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: C6WWMryELL.pdf
paper: On Stable Long-Form Generation: Benchmarking and Mitigating Length Volatility
main_score_norm: 0.6
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is squarely within ICLR scope, covering LLM generation, benchmarking, decoding-time control, and analysis of internal attention dynamics for long-form generation.

## Minimum Quality
Pass ✅. The paper contains the core components expected for an ICLR submission, including abstract, introduction, related work, benchmark/method sections, experiments, quantitative results, and conclusion. While there are important issues in novelty, methodological specification, and overclaimed conclusions, these do not rise to the level of a desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden instructions, suspicious prompt injection, or manipulative text targeting automated reviewers in the provided paper content.

# Expected Review Outcome:
## Summary
This paper studies instability in long-form LLM generation across repeated runs, focusing on what the authors call length volatility. The paper introduces VOLTBench, a benchmark spanning structured and unstructured long-generation tasks across languages and instruction complexities, analyzes attention traces to identify failure patterns such as attention collapse and attention instability, and proposes SELB, a decoding-time logit modification method intended to enforce section structure and suppress early stopping or conversational derailment. Experiments report substantial gains in length adherence and reduced volatility on the proposed benchmark.

## Strengths
The paper targets a real and under-discussed problem. Much of the recent long-context literature emphasizes long-input understanding or single-run generation quality, while practical deployment also depends on whether repeated generations have predictable length and structure. Framing volatility across multiple runs as a first-class evaluation target is useful.

The benchmark design is broader than many prior long-generation evaluations. In particular, **Figure 2** gives a clear overview of the benchmark axes, namely task type, language, instruction complexity, and evaluation dimensions, and this helps the reader understand that the benchmark is not limited to a single creative-writing setup. I also appreciate that the paper includes both unstructured tasks and more objectively checkable structured tasks such as code/JSON/LaTeX generation, which makes at least part of the evaluation more automatable and less subjective.

The empirical evidence that current models struggle with long generation is fairly convincing at a high level. **Figure 1** is effective in communicating the core phenomenon: as the requested length grows, most models undershoot badly, and the variance also grows. This figure is one of the stronger parts of the paper because it visually motivates why measuring only one sample is insufficient. Similarly, **Figure 3** usefully decomposes volatility by language, complexity, and output format, rather than presenting a single aggregate score.

The paper includes concrete quantitative comparisons in tables, not only plots. For example, **Table 2** shows a sharp trade-off between length, volatility, and content quality on the 100-section setting. The table makes it easy to see that some models are “stable” only because they stop almost immediately, while others generate longer outputs at the cost of much higher volatility or worse structural correctness. That is a meaningful observation, and the paper does not entirely hide these trade-offs.

The proposed mitigation is lightweight and easy to understand conceptually. A training-free decoding intervention is attractive from a practical perspective, especially compared with methods requiring additional finetuning or RL. Even if the mechanism is somewhat heuristic, the simplicity is a genuine strength.

The attention-trace analysis is suggestive and at least provides a hypothesis-driven lens on failure modes. **Figure 4** is useful in this regard: the periodic spikes aligning with section boundaries, and the contrasting failure patterns for Qwen2.5-7B versus Qwen2.5-3B, give an interpretable story about losing constraint focus or jumping structurally. I am not fully convinced this establishes causality, but as a diagnostic tool it is interesting and better than purely anecdotal discussion.

## Weaknesses
1. **The main methodological contribution, SELB, is quite heuristic and much narrower than the paper’s framing suggests.**  
   The method in **Section 6**, especially **Equations (2) and (3)** on Pages 8 to 9, effectively forces section titles when a length threshold is reached and bans EOS / certain filler phrases before completion. This is a practical control trick, but it is much closer to structure forcing than to a general solution to long-form generation instability. The benchmark itself is heavily section-anchored, so the method aligns unusually well with the evaluation protocol. That makes it hard to tell whether the gains reflect a broad improvement in long-form generation, or simply a strong exploit of benchmark-specific formatting. This matters because the paper repeatedly presents SELB as mitigating the root causes of volatility, while the evidence more directly supports that it improves adherence in sectioned tasks.

2. **Generalization beyond explicitly sectioned tasks is not established in the main paper.**  
   The main claims and headline results are centered on chapter-based or section-based prompts. The free-form adaptation is moved to **Section 6.4** and relies on appendix-dependent details, but the main paper does not provide enough evidence that the underlying idea generalizes when there is no explicit structural scaffold to boost. This is important because the paper repeatedly motivates “long-form generation” broadly, including continuous open-ended writing, yet the main benchmark and the main method are both structurally biased. The gap between the problem statement and the demonstrated scope is nontrivial.

3. **The mathematical specification of SELB is incomplete and internally inconsistent in places.**  
   This is a notable issue because the paper does present the method in formal notation. In **Equation (1)**, the modified logits are written as
   \[
   s_t' = M\left(s_t, [x_{1:T_0}; y_{0:t-1}]\right),
   \]
   but then **Equations (2) and (3)** each independently define a quantity also called \(s'_{t,j}\). If \(M = M_{\mathrm{fail}} \circ M_{\mathrm{struct}}\), the paper should define the intermediate logits explicitly, for example
   \[
   \tilde{s}_t = M_{\mathrm{struct}}(s_t,\cdot), \quad s_t' = M_{\mathrm{fail}}(\tilde{s}_t,\cdot),
   \]
   rather than reusing the same symbol for two different updates. As written, the composition is underspecified.

   There are additional ambiguities. What exactly is \(V_{\mathrm{title}}^{(p+1)}\) for a multi-token title such as “Chapter 27” or “## Floor 18”? Is the boost applied to all title tokens simultaneously, only the next valid token in a prefix-constrained automaton, or to any token appearing in any valid title string? These are very different decoding behaviors. Likewise, \(\tau_p\) is described as section length, but the paper does not clearly state whether it is measured in words or tokens; elsewhere results are reported in words, while decoding operates over tokens. This matters for reproducibility and for interpreting how “target section length” is enforced.

4. **The attention analysis is interesting but still largely correlational, and some definitions are not well justified.**  
   In **Section 5** on Pages 7 to 8, the paper defines layer-step constraint attention by averaging attention to all tokens belonging to all constraints:
   \[
   \alpha^{(l,t)} = \frac{1}{|C|}\sum_{j\in C} a_j^{(l,t)}.
   \]
   This scalar is then averaged again across layers to form \(\overline{\alpha}^{(t)}\). There are at least three issues. First, averaging over all constraint tokens means the statistic depends on how many tokens were used to verbalize the constraints, which can vary across prompts and languages. Second, averaging uniformly over heads and layers may wash out the few heads that actually carry long-range instruction tracking. Third, the paper treats spikes and collapses in \(\overline{\alpha}^{(t)}\) as evidence for specific failure modes, but no controlled intervention is provided to show that these patterns are causal rather than epiphenomenal.

   Relatedly, there is a small but telling exposition error: on **Page 8**, the text says “As shown in Figure 2” when discussing the attention-trace failure signatures, but this is clearly referring to **Figure 4**. That kind of mismatch makes the analysis harder to trust.

5. **The evaluation of generation quality is weaker than the paper’s claims require.**  
   For unstructured tasks, **Section 3.2** defines UCA via LLM-as-a-Judge, with details deferred to Appendix C. In the main paper, there is little discussion of judge model choice, calibration, variance, rubric sensitivity, or agreement with humans. The prompt in Appendix C is generic and the evaluator is explicitly instructed to ignore response length, which may be reasonable in some contexts, but also risks rewarding outputs that are qualitatively decent yet fail the long-form requirement in substantive ways. This matters because the paper’s central message is not just “make outputs longer,” but “make them longer without sacrificing quality.” That conclusion needs stronger validation than a single automated judge rubric.

6. **Some results suggest the method can improve length while still failing structural adherence at larger scales, which weakens the strongest claims.**  
   The main text emphasizes large improvements on the 100-section task, but the broader results are more mixed. In the appendix tables, the method is strong at 50, 100, 200, and 500 sections, but not uniformly perfect on format adherence. For example, in **Table 31** the method averages 88 sections out of 100 with **FAD = 7.24**, and in **Table 32** it averages 147.2 out of 200 with **FAD = 5.00**. Those are still good relative to baselines, but they are not full task completion. Even more concerning, **Table 29** shows a 20-section setting where “Ours” appears to have the same **FAD (8.23)** and same mean section count **(15.25)** as LongWriter-8B, which is either a major anomaly or a likely table/reporting problem. If correct, it indicates SELB is not consistently reliable even at moderate scale; if incorrect, it raises concerns about result quality control. This point needs direct clarification.

7. **There are internal inconsistencies between the main narrative and some later figures/tables.**  
   For example, the main paper uses LongWriter as evidence of high volatility and poor robustness, which is supported in **Table 2**. But in later benchmark plots such as **Figure 12** and some task-specific descriptions in Appendix J, LongWriter is sometimes described as tracking targets surprisingly well, especially in certain languages/tasks. That may reflect true task heterogeneity, but the paper does not synthesize these differences clearly. Instead, it sometimes overstates “universal” conclusions while the detailed results suggest a more nuanced picture, including strong task dependence.

8. **The benchmark’s central volatility metrics are useful, but the paper does not justify some design choices enough.**  
   In **Section 3.2**, volatility is measured from only \(N=5\) runs. For a paper whose main thesis is about cross-run variability, that is a fairly thin estimate, especially for high-variance models. Also, **MLA**
   \[
   \text{MLA}=\max\left(0,1-\left|\frac{\mu-L_{\text{constraint}}}{L_{\text{constraint}}}\right|\right)\times 100
   \]
   clips performance at zero once the mean misses the target by more than 100%, which compresses very poor models together and may hide differences among severe failures. I do not object to the metric existing, but it should be motivated more carefully, perhaps alongside unclipped relative error. Since this benchmark is a core contribution, the metric design should be more thoroughly justified.

9. **The paper sometimes overclaims mechanism-level understanding from limited evidence.**  
   Phrases like “root causes,” “first systematic confirmation,” and claims that SELB “proactively suppresses tokens linked to known failure modes” read stronger than the evidence supports. The attention-trace observations and failure case studies are helpful, but they do not establish that attention collapse and instability are the main causal mechanisms across models and tasks. The paper would be stronger if it framed these as recurring correlates or diagnostic signatures, not definitive causes.

10. **Presentation is decent overall, but there are enough notation and writing issues to hurt confidence.**  
   There are several inconsistencies: “end-of-sentence token” on **Page 9** almost certainly should be EOS, not sentence-ending punctuation; the averaging formula on **Page 7** uses \(\sum_{l=1}^{L-1}\alpha^{(l,t)}\) while saying it averages over all \(L\) layers; model names vary in formatting; and the paper occasionally leans into assertive prose that outruns what the tables strictly show. None of these alone is fatal, but collectively they weaken what is otherwise a promising submission.

## Questions
1. In **Equations (2) and (3)**, how exactly is \(V_{\mathrm{title}}^{(p+1)}\) implemented for multi-token titles? Is SELB doing constrained prefix decoding, boosting a token set at each step, or matching regular expressions over token sequences? A precise decoding description would materially increase my confidence.

2. Please clarify whether \(\tau_p\) is measured in tokens or words, how \(\tau_{\max}\) is chosen, and whether it is fixed across tasks or tuned per task/model. If there is task-specific tuning, what data was used for it?

3. Can the authors explain the anomaly in **Table 29**, where “Ours” and LongWriter-8B appear to have identical **FAD = 8.23** and mean section count **(15.25)**? If this is a typo, it should be corrected. If not, it needs discussion because it materially changes the interpretation of SELB’s robustness.

4. The main paper relies heavily on LLM-as-a-Judge for unstructured quality. Can the authors provide stronger evidence that UCA correlates with human judgments, at least on a representative subset of outputs? Even a small human study or judge-agreement analysis would help.

5. In **Figure 4**, the attention patterns are compelling visually, but what is the quantitative criterion for calling a trace “collapse” or “instability”? Do these signatures predict failure ahead of time across many runs, or were the examples selected post hoc?

6. Since the benchmark emphasizes volatility across samples, why was \(N=5\) chosen in **Section 3.2**? Have the authors checked whether model rankings by LSD/LVC are stable when using more samples?

7. The method appears particularly aligned with section-structured prompts. How much of the gain remains if titles are less explicit, numbering formats vary, or section boundaries are semantically but not lexically specified?

8. Some later figures suggest substantial task dependence, especially for LongWriter and Qwen models. Could the authors better characterize where SELB helps most, and where the benchmark itself reveals task-specific strengths rather than universal instability?

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No major ethics concerns stood out from the main paper. The work is primarily about benchmarking and decoding control for long-form generation, and the paper does not involve human subjects or sensitive data in the main presentation.

## Soundness Rating
3: good. The empirical findings are mostly plausible and the paper contains substantial experimentation, but the formal specification of SELB is incomplete, the causal interpretation of the attention analysis is overstated, and key quality-evaluation choices are not fully validated.

## Presentation Rating
2: fair. The paper is readable and the figures are helpful, but there are notable inconsistencies in notation, equations, figure references, and the strength of claims relative to the evidence.

## Contribution Rating
3: good. Measuring multi-sample volatility in long-form generation is a useful contribution, and the benchmark plus lightweight decoding intervention are relevant to the community, even if the mitigation method is more heuristic and benchmark-aligned than the paper suggests.

## Overall Rating
6: Marginally above the acceptance threshold. But would not mind if paper is rejected.  
I see a meaningful contribution here, mainly in the problem framing and benchmark, and the paper presents enough evidence that volatility is real and practically important. However, the method is fairly heuristic, some mathematical details are underspecified, the strongest mechanism claims are too assertive, and the evaluation of “quality preserved” is not strong enough for a cleaner accept. So I land slightly on the positive side, but not comfortably.

## Reviewer Confidence
4: confident. I am confident in the overall assessment and checked the main equations, figures, and tables carefully, though some implementation-level details needed to fully verify SELB are not specified in the main paper.
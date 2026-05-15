Now I have all the information needed. Let me write the consolidated review.

---

## Summary

This paper proposes MA-RLHF, which integrates macro actions (sequences of tokens) into the RLHF framework for LLM alignment. Operating under the semi-Markov Decision Process (SMDP) formalism, the method groups tokens into macro-level units, reducing the number of decision points and aiming to improve credit assignment over long sequences. The paper evaluates MA-RLHF on summarization (TL;DR), dialogue (HH-RLHF), question answering (WebGPT), and code generation (APPS) across 2B, 7B, and (mentioned but results not in main text) 27B models, reporting consistent improvements in reward model scores, faster convergence (1.7×–2×), and favorable win rates against vanilla PPO in GPT-4 and human evaluations.

## Strengths

- **Consistent and substantial improvements across diverse tasks and model scales.** The paper reports RM score gains of +68% (TL;DR 2B), +30% (TL;DR 7B), +18% (HH-RLHF), and +8% (WebGPT 7B), along with 1.7×–2× faster convergence in training steps (Section 4.2, Table 2, Figure 2). The breadth across four tasks and two (arguably three) model sizes supports the generalizability claim.

- **Multi-evaluator validation beyond the reward model.** The paper supplements RM scores with GPT-4 and human pairwise evaluations (Figure 3), finding win rates of 74–86% for MA-PPO over vanilla PPO. The agreement analysis among RM, GPT-4, and human evaluators (Table 1, 74–76% RM–human agreement) provides triangulation that the RM-based improvements are not purely artifacts.

- **Principled framing via SMDPs and connection to existing methods.** The paper formalizes macro actions in the SMDP framework (Section 3.2) and explicitly shows that varying macro action length interpolates between token-level PPO (length 1) and RLOO/REINFORCE (length →∞), positioning MA-RLHF within a known continuum (Section 3.2.3).

- **Exploration of multiple termination strategies.** The paper investigates three termination conditions (n-gram, parsing-based, perplexity-based) for defining macro actions (Section 3.2.1), demonstrating systematic design exploration.

## Weaknesses

### Fatal
None.

### Major

- **The +68% RM score improvement on TL;DR (2B) is extreme and demands stronger explanation.** Such a large jump (0.84 → 1.41) raises the possibility of reward model exploitation—the policy may be learning statistical regularities of the *specific* RM rather than genuinely better alignment. The paper reports human evaluation (74% win rate on 50 instances) which partially mitigates this concern, but the sample is small and the confidence intervals around the 74% estimate are wide (a 50-sample binomial proportion at 74% has a ~95% CI of roughly 60–85%). Without a larger human study (≥200 instances) or held-out RM-free metrics (e.g., downstream task performance, output diversity/length/perplexity analysis to check for exploitation), the reader cannot rule out the possibility that the dramatic RM improvement is partially driven by RM gaming.

- **The human and GPT-4 evaluations lack statistical confidence measures.** The paper reports win-rate percentages on only 50 instances per task with no confidence intervals, p-values, or significance tests. With n=50, win rates near 50% (e.g., 52% and 56% for HH-RLHF human eval) are not reliably distinguishable from chance. This makes it difficult to assess which results are robust and which may be noise.

- **No quantitative code generation results appear in the main text.** The abstract claims "up to 30% improvement in code generation," and Section 4.1 describes the APPS dataset and pass@1/pass@5 metrics, but Section 4.2 (Main Results) only presents results for summarization, dialogue, and QA. The code generation results are deferred to the analysis section (stripped by the parser). While the full paper likely contains them, the main body as presented is incomplete on this point.

- **The "no additional computational overhead" claim is unsubstantiated.** The paper asserts that MA-RLHF does not increase computational complexity during training or inference (abstract, conclusion), but no wall-clock measurements are provided. The grouping process and macro-level advantage computation add non-trivial overhead (even if O(1) per macro step), and the 1.7×–2× faster convergence is measured in *training steps*, not wall-clock time. Since each MA-PPO step processes a full macro action (multiple tokens), the faster step-based convergence may or may not translate to faster wall-clock convergence.

### Minor

- **The specific n value for the fixed n-gram default is not reported.** Section 3.2.1 describes fixed n-gram macro actions as "the default setup" and gives possible values n ∈ {2,3,5,10} for the randomized variant, but never states which n is used in the main experiments. This makes it impossible to reproduce or assess sensitivity.

- **The parsing-based termination condition is impractical for online generation**, as it requires a full constituent tree of the generated text which is unavailable until the sequence is complete. (The paper uses fixed n-gram as default, so this is more a design exploration note than a flaw, but it warrants acknowledgment.)

- **The agreement table (Table 1) is computed on the same 50 instances used for win-rate estimation**, which is a small and potentially biased sample. The 74–76% agreement between RM and human does not necessarily validate the RM as a reliable proxy across the full test set.

### Trivial

- The paper contains the minor typo "Marco-Action RLHF" in the Section 3 heading (line 86) instead of "Macro-Action RLHF."
- The advantage notation $\hat{A}_\tau$ in the MA-PPO objective (line 146) is defined earlier in the text (lines 142–143) but the connection could be made more explicit to avoid ambiguity.

## Nice-to-Haves

- A larger human evaluation (≥200 instances per task) with confidence intervals would significantly strengthen the validation and address RM gaming concerns.
- Wall-clock training time comparisons (actual hours) would substantiate the "no additional overhead" claim.
- An analysis of output characteristics (length, diversity, perplexity) between vanilla PPO and MA-PPO would help determine whether the RM improvements reflect genuine alignment gains or distributional exploitation.
- Comparison to other credit-assignment methods (e.g., return-based baselines, longer discount factors) would clarify whether macro actions provide unique benefits beyond standard RL tricks.

## Removed Points

The following points from the reviewer inputs were removed as per the consolidation guidelines. They are documented here for traceability:

- **Missing analysis section (ablations, sensitivity to macro length):** The paper cites `\input{section/analysis}` (line 261). The parser strips sections pulled in via `\input`; this section exists in the original submission. Per policy, weaknesses about missing parser-stripped content are removed.
- **Equation (5) notation not defined:** The paper *does* define $\hat{A}_\tau$ (lines 142–143, 148). The reviewer's claim was factually incorrect.
- **Connection to Previous Methods not empirically tested:** The paper explicitly says "We provide further analysis on the impact of $|\omega_\tau|$ in \S\ref{sec:ma_analysis}" (line 161), which is in the stripped section. Removed.
- **Missing baseline hyperparameters (learning rate, KL coefficient, PPO epochs):** Per policy, nitpicks about "undisclosed hyperparameters" are removed as trivial reproducibility demands.
- **Theoretical motivation about temporal distance unsupported:** The paper provides the SMDP formalism (Section 3.2), defines macro-level value/advantage functions, and the KL penalty provides per-token reward shaping that gives macro-level advantage estimation grounding. The criticism oversimplifies the RLHF reward structure.

## Novel Insights

The harsh critic's most incisive observation is that the +68% RM improvement on TL;DR 2B is so extreme that it functions as a red flag rather than a selling point—in a field where RM gaming is well-documented, an improvement of this magnitude without a clear mechanism explanation is itself a weakness. Conversely, the strength finder correctly identifies that the paper does provide *some* non-RM validation (human and GPT-4 win rates), creating a genuine tension: the human evaluation is too small to fully validate the RM scores, but it is consistent enough to suggest the improvement is not purely artifact. The paper's central unresolved question is whether macro actions improve alignment or simply make it easier to exploit the RM's inductive biases (e.g., by producing longer or more fluent outputs that the RM prefers but humans do not). This is a well-motivated paper whose claims are probably directionally correct but whose quantitative strength claims are not yet convincingly supported.

## Suggestions

1. **Report the fixed n value and show sensitivity to macro action length.** This is essential for reproducibility and for understanding whether the method is robust—the single most actionable fix.
2. **Add confidence intervals or Bayesian credible intervals to all win-rate estimates** (human and GPT-4). At minimum, bootstrapped 95% CIs.
3. **Report wall-clock training times** for at least one task to substantiate the "no additional overhead" claim.
4. **Include a qualitative analysis of outputs** (case studies, length/perplexity/diversity statistics) comparing MA-PPO and vanilla PPO to help diagnose whether RM scores reflect genuine alignment gains.
5. **Include the code generation results prominently in the main table** rather than deferring them to the analysis section.
6. **Acknowledge the RM gaming concern explicitly** and discuss why the human evaluation, despite its limited size, provides evidence against pure exploitation.

## Score and Decision

**Originality:** 7/10 — Macro actions in RL are well-established, but applying them to RLHF for LLMs is novel and timely.

**Importance of research question:** 8/10 — Improving credit assignment in RLHF is an important practical problem.

**Claims well supported:** 5/10 — The broad experimental evidence is suggestive but weakened by small human evaluation, missing confidence measures, and the extreme +68% RM score that demands more scrutiny.

**Soundness of experiments:** 6/10 — Reasonably broad task/model scope, but lacks statistical rigor in human evaluation and wall-clock validation.

**Clarity of writing:** 7/10 — Well-structured and generally clear, though Section 3.2 could benefit from more explicit derivations.

**Value to the research community:** 7/10 — The idea is likely to inspire follow-up work on hierarchical credit assignment in LLM alignment.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>
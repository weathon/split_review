I now have a thorough understanding of the paper. Let me synthesize the final review.

## Summary

The paper investigates the role of the first reasoning step in multi-step math tasks. It first shows that smaller models (2B–8B) often possess the knowledge to solve problems but fail because they select an incorrect first reasoning step — demonstrated via oracle sampling experiments (Figure 1) and large gains when a correct first step is provided by a stronger LLM (Table 1, up to 3× improvement). The paper then proposes **QuestCoT**, a prompting strategy where the model generates a sub-question to guide its initial reasoning step before proceeding with the full chain. Across 7 models and 4 datasets (GSM8K, SVAMP, ASDiv, MultiArith), QuestCoT consistently outperforms standard Chain-of-Thought and sub-question decomposition (Subques).

## Strengths

- **Strong diagnostic experiment establishes the core claim (Figure 1, Section 3.1):** The paper shows that Mistral-7B's "answer exists in any sample" oracle accuracy rises from ~45% (1 sample) to ~90% (35 samples), narrowing the gap with GPT-4 from ~50 points to <10 points. This directly supports the claim that smaller models are capable but fail to consistently select the correct initial chain, providing clear motivation for the work.

- **Dramatic and monotonic gains from providing a correct first step (Table 1):** Across six smaller models, providing GPT-4's first-step guidance yields large improvements (e.g., OlMo-7B: 13.6% → 37.9% on GSM8K; 18.6% → 49.9% on SVAMP). The monotonic improvement with guidance model strength (LLaMA2-70B < GPT-3.5 < GPT-4) confirms the causal role of first-step quality, not just general assistance.

- **QuestCoT consistently outperforms CoT across models and datasets (Table 2):** Gains are observed on all four datasets across seven models, with the largest improvements on weaker 7B models (OlMo-7B: +5.8 GSM8K, +8.6 SVAMP, +5.0 ASDiv, +7.2 MultiArith). The broad evaluation (28 model–dataset combinations) strengthens the generality claim.

- **QuestCoT outperforms Subques at lower cost (Figure 3):** The comparison shows QuestCoT beats sub-question decomposition across all models, and the paper provides a reasoned explanation (multiple subquestions accumulate errors). The Venn diagram (Figure 4) further shows QuestCoT captures the strengths of both CoT and Subques.

- **Qualitative error analysis (Figure 5) provides mechanistic understanding:** The paper identifies specific failure modes of CoT (unnecessary calculations, missing real-world knowledge, context confusion) and shows concrete examples where QuestCoT resolves them, adding interpretability beyond aggregate metrics.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Few-shot exemplars drawn from the test set (Section 3.3, line 189):** The paper states "To compare CoT and QuestCoT, we used 4-shot prompting with prompts randomly selected from the test set." Drawing exemplars from the test set is non-standard and could inflate absolute accuracy numbers. **However, this does not invalidate the QuestCoT results** because both CoT and QuestCoT use the same exemplars — the relative comparison remains fair. The paper should clarify whether the same four examples were used for all test queries and ideally replicate with train-set exemplars.

- **No direct quantitative evidence that QuestCoT improves first-step correctness specifically:** The paper's central narrative is that small models fail because they start incorrectly, and QuestCoT helps them start correctly. Yet only final answer accuracy is reported. While the qualitative examples (Figure 5) illustrate this mechanism, adding a quantitative analysis — e.g., manually or automatically labeling whether the first reasoning action is correct for CoT vs. QuestCoT on a sample of outputs — would substantially strengthen the causal link.

- **No statistical significance or variance reported:** Given the modest gains for several models (e.g., +0.4–1.1 points for Gemma-2B, +0.4–1.2 for LLaMA3-8B) and the use of greedy decoding (single run), confidence intervals or bootstrap estimates would help assess reliability.

- **Answer leakage check is on training data, not test data (Section 4, line 212):** The paper checks 1000 samples from the GSM8K *training* set (finding 999/1000 no leakage). While the first-step is limited to one equation and problems require 2–8 steps, verifying on the actual test sets would be more rigorous. This is a minor concern — the paper's instructions and the multi-step nature of the problems already provide strong safeguards.

### Trivial

- **Section 3.1 (oracle experiment) interpretation:** The reviewer notes that high oracle accuracy could mean the correct chain appears stochastically rather than the model "understanding." While this is a philosophical nuance, the paper's actual claim ("smaller models can answer correctly but struggle to select the right chain") is well-supported by the data and does not over-claim.

- **Venn diagram (Figure 4) could report unique successes explicitly:** The paper reports overlaps (82 with CoT, 95 with Subques) but the absolute numbers of questions uniquely solved by QuestCoT are inferable but not stated. This is a presentation detail.

## Nice-to-Haves

- **Additional baseline comparisons:** Including self-consistency (used as motivation in Section 3.1) or Plan-and-Solve would further contextualize QuestCoT's effectiveness, though the current comparison against CoT and Subques is already adequate.
- **Token-cost vs. accuracy trade-off analysis:** The paper notes QuestCoT adds a token but does not quantify the overhead. A brief comparison of generation lengths would aid practitioners.
- **Manual validation of first-step quality on a subset** would directly tie the mechanism to the results.

## Removed Points

- **"Abstract misleadingly combines +24 point LLM-guidance gain with QuestCoT's smaller gains"** — Removed because the abstract clearly separates the two claims: the +24 points is attributed to "using a larger model to guide smaller models" and the QuestCoT gains are reported separately with their own numbers. No conflation.
- **"Section 3.1 interpretation is flawed"** — Removed because the paper's claim is simply that smaller models *can produce* correct answers (oracle exists), not that they "understand" in a deep sense. The evidence supports the paper's stated claim.
- **"Insufficient check for leakage undermines the entire LLM-guidance experiment"** — Downgraded from the reviewer's characterization. The paper provides a reasonable check (999/1000 no match, first step limited to one equation for 2–8 step problems) and the concern is a degree-of-thoroughness issue, not a fatal flaw.
- **"Missing confidence intervals" as a major weakness** — Moved to Minor. Single-run greedy decoding is standard in this literature; confidence intervals would strengthen but their absence is not a structural flaw.

## Novel Insights

The most interesting observation from the reviews is that the paper's strongest evidence comes from two complementary angles: (1) the oracle sampling experiment showing capability exists but selection fails, and (2) the controlled LLM-guidance experiment showing that fixing the first step alone produces large gains. Together, these provide a clean decomposition that isolates the "starting right" bottleneck from other potential sources of error (e.g., general reasoning weakness). This two-step argument structure — diagnose the bottleneck, then measure the effect of fixing it — is an effective empirical template for studying reasoning chain failures. The paper would benefit from tightening this connection in QuestCoT's evaluation: the method is introduced as a way for models to "learn to start correctly," but whether it actually achieves better first steps (not just better final answers) remains untested quantitatively.

## Suggestions

1. **Replicate the QuestCoT experiments with fixed exemplars drawn from the training split** (or held-out development set) to address the most significant methodological concern. Report whether the same 4-shot exemplars were used for all test queries.
2. **Add a direct analysis of first-step quality:** For a random subset of CoT and QuestCoT outputs, annotate whether the first reasoning action (equation or sub-question) is correct, and show the correlation with final accuracy. This would directly substantiate the claimed mechanism.
3. **Report results with variance** (e.g., bootstrap confidence intervals or repeated sampling at nonzero temperature) for the main QuestCoT results in Table 2, especially for models with small gains.
4. **Clarify the exemplar selection procedure** — whether the same four examples were used for all test queries or resampled per instance — for reproducibility.

## Score and Decision

This paper makes a clear and well-motivated contribution: it diagnoses a specific bottleneck in small-model reasoning (first-step selection) and proposes a simple, effective intervention (QuestCoT). The empirical evaluation is broad (7 models, 4 datasets) and the evidence for the core claim is supported by converging experiments. The most significant methodological concern (test-set exemplars) does not threaten the validity of the relative comparisons, and the remaining issues are addressable with minor revisions. I recommend acceptance.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>
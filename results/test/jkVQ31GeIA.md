Now I have all the information needed. Let me write the definitive consolidated review.

---

## Summary

This paper introduces Auto-RAG, a method that fine-tunes open-source LLMs (specifically Llama-3-8B-Instruct) to autonomously decide *when* and *what* to retrieve during iterative RAG. The core idea is to model the retrieval process as multi-turn dialogue where the LLM performs three types of reasoning (retrieval planning, information extraction, answer inference) in each iteration, generating queries when it identifies a knowledge gap and producing a final answer when it has sufficient information. The training data is synthesized automatically via a teacher LLM with correctness filtering, and the resulting model is fine-tuned with standard supervised learning. The paper claims strong performance across six QA benchmarks, though the experimental results section is not present in the provided (truncated) file.

## Strengths

- **Well-motivated reasoning structure for iterative retrieval.** The three-part decomposition (retrieval planning, information extraction, answer inference) models human cognitive strategies and provides a clear, reusable framework that moves beyond opaque reflection tokens or rigid retrieval schedules. The method includes sensible adjustments—omitting extraction when content is irrelevant—to avoid rote imitation (Section 3.1.1).

- **Fully automatic data synthesis pipeline.** Algorithm 1 describes an end-to-end process that generates multi-turn reasoning trajectories via a teacher LLM, filters by sub-answer relevance (when available), and retains only trajectories where the final answer matches ground truth. This eliminates the need for human annotation of training data for iterative retrieval behavior.

- **Graceful handling of retriever failures.** Algorithm 2 includes a parametric knowledge fallback phase: after T failed retrieval iterations, the model can generate self-produced documents and, as a last resort, fall back to its own parametric answer. This is a practical design choice that prevents infinite loops and makes the system robust to retriever limitations.

- **Interpretability through natural language reasoning.** Unlike methods that use binary reflection tokens (Self-RAG) or black-box sentence revision (FLARE), Auto-RAG expresses retrieval decisions in natural language, making the process transparent to users.

## Weaknesses

### Fatal

None.

### Major

None. The method is well-motivated and the pipeline is coherent. The most significant issues are at the minor level—none threaten the paper's core viability.

### Minor

- **The heuristic for detecting information needs during data synthesis is underspecified and fragile.** The paper uses predefined trigger words—"however," "no information," "find," "refine"—to determine whether the teacher LLM's reasoning expresses an information need (line 85, Algorithm 1 line 112). This is a hand-crafted, brittle design choice. The paper provides no analysis of how often these tokens appear in non-retrieval contexts (false positives) or how often information needs are expressed without these tokens (false negatives). While the reviewer incorrectly claimed this mechanism is also used at inference (Algorithm 2 actually detects queries/answers, not trigger words — lines 185-191), the data synthesis concern stands: if the teacher data is constructed using a noisy heuristic, the fine-tuned model inherits those noise patterns.

- **Uneven data quality across benchmarks due to sub-answer annotation dependencies.** Algorithm 1 preferentially selects queries whose retrieved documents contain a sub-answer. The paper acknowledges (line 146) that this targets datasets with sub-answer annotations (e.g., 2WikiMultihopQA), but for datasets without such annotations (TriviaQA, WebQuestions, etc.), the fallback is random query selection (Algorithm 1 lines 107-110). The paper does not report how often the sub-answer filter fired vs. the random fallback for each dataset, making it impossible to assess the actual training signal quality. If the random fallback dominates for most benchmarks, the claimed "principled" data filtering may be largely cosmetic.

- **The parametric knowledge fallback confounds attribution of gains.** The inference procedure (Algorithm 2) allows the model to fall back to self-generated documents and parametric knowledge after T iterations. This makes it difficult to determine whether performance gains come from improved iterative retrieval, from the parametric knowledge fallback, or from the model simply having memorized the answer. An ablation comparing Auto-RAG with and without the parametric fallback phase would clarify this, but is absent from the provided content.

- **Several implementation details are underspecified.** (a) The number of queries sampled per iteration (`Q_gen` in Algorithm 1) is not stated. (b) The retriever model, corpus, and top-k are not named. (c) The few-shot prompts used to elicit reasoning from the teacher LLM during data synthesis are not provided. (d) Training/inference compute costs and average retrieval calls per question are not reported. These gaps hinder reproducibility.

- **Maximum iteration caps (T=10 for 2WikiMultihopQA, T=5 for NQ) appear unmotivated.** The paper does not analyze sensitivity to these thresholds. If performance plateaus well before T for most examples, the caps are harmless but arbitrary; if performance is still improving at T, they may be truncating the process prematurely.

- **The "autonomous decision-making" claim rests on imitation learning.** The training data is generated by a teacher LLM and filtered by correctness; the student LLM is then fine-tuned on successful trajectories. This is a standard distillation pipeline that teaches the model to replicate behaviors that led to correct answers during data generation. Whether this equips the model with genuine context-sensitive decision-making (as opposed to pattern matching on reasoning trace formats) is untested—no out-of-distribution or distribution-shift experiments are described. This does not invalidate the approach (many successful methods use similar schemes), but the paper should be more measured in claiming "autonomous decision-making" vs. "learned imitation of a successful policy."

### Trivial

- The fallback mechanism (Section 3.3) is described but `T^{PK}` (the maximum parametric knowledge iterations) is defined in Algorithm 2's input but never empirically set or analyzed.
- The paper uses "Auto-RAG" to refer to both the method and the trained model, which is occasionally ambiguous.

## Nice-to-Haves

- A learned (or logit-based) detector for information needs during data synthesis would be more robust than the current trigger-word heuristic. Even a small classifier trained on the teacher's reasoning traces could reduce noise.
- Reporting the fraction of examples where the sub-answer filter succeeded vs. fell back to random for each benchmark would clarify how much of the training signal is actually principled.
- An ablation isolating the effect of the parametric knowledge fallback from the iterative retrieval signal would strengthen the evidence for the core claim.

## Removed Points

- **"Missing experimental results"** (Harsh Critic point #1): The provided paper file ends after the Method section (Section 3). This is a parser truncation issue — the original submission would contain Section 4 (Experiments). The paper's abstract and introduction explicitly reference experimental results on six benchmarks. I do not penalize the paper for a content-delivery limitation.
- **"Trigger words used at inference"** (Harsh Critic point #2, inference portion): The reviewer states trigger words are the "core gating mechanism" during both data synthesis and inference. This is factually incorrect for inference — Algorithm 2 (lines 185-191) checks whether $y_{t-1}$ contains a query string or a final answer, not trigger words. Trigger words are only used during data synthesis (Algorithm 1 line 112). The valid concern about data synthesis is retained in Minor weaknesses above.
- **Impossibility of disentangling retrieval vs. parametric knowledge** (mentioned as severe by reviewer): This is a valid concern but belongs in Minor, not as a structural flaw. Many RAG papers have this confounding factor; the paper at least attempts to address it with the explicit two-phase design. An ablation would strengthen the paper but its absence is not fatal.
- **Several generic Strength Finder claims** weakened/dropped: "Strong performance across diverse benchmarks" is a claim the paper makes, not a verified strength without results visible in the provided content. It is removed from Strengths to avoid circular reasoning.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface insights that the paper itself does not articulate. The critiques about fragility of the trigger-word heuristic and uneven sub-answer coverage are standard methodological concerns rather than novel observations.

## Suggestions

1. **Replace or validate the trigger-word heuristic.** Either train a lightweight classifier on the teacher's reasoning traces to detect information needs, or at minimum report precision/recall of the current heuristic on a held-out set of teacher outputs, with failure case analysis.
2. **Report sub-answer filter hit rate per dataset.** For each of the six benchmarks, report what fraction of training examples had a sub-answer match vs. random fallback. This is essential for understanding which benchmarks benefit from the principled filtering and which get noisy data.
3. **Add an ablation of the parametric knowledge fallback.** Compare Auto-RAG with and without the self-document generation phase (Algorithm 2, lines 194-202) to isolate whether iterative retrieval or parametric fallback drives performance.
4. **Disclose the retriever, query sampling count, and few-shot prompts.** Without these, the method cannot be reproduced or meaningfully compared against.
5. **Add an out-of-distribution evaluation.** Test the trained model on a benchmark or task format not seen during data synthesis to assess whether the "autonomous decision-making" generalizes beyond the imitation training regime.

## Score and Decision

The paper proposes a well-motivated and clearly described method for autonomous iterative RAG. The three-part reasoning structure, automatic data synthesis pipeline, and graceful fallback mechanism are genuine design contributions. The primary weaknesses are at the minor level: a fragile data-synthesis heuristic, uneven data quality across benchmarks, underspecified implementation details, and a confounded evaluation setup. None of these are fatal — they are addressable in a camera-ready revision or rebuttal. The method is sound, the writing is clear, and the contribution (training LLMs to autonomously reason about when and what to retrieve) is timely and relevant. Based on the method alone, the paper merits acceptance pending verification of the experimental results (which are absent from the provided file due to parser truncation, not author omission).

**MY FINAL SCORE: <pineapple>6.0</pineapple>**

**MY FINAL DECISION: <orange>Accept</orange>**
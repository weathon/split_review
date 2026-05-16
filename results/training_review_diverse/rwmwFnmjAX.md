Now I have all the information needed. Let me compose the final consolidated review.

## Summary

This paper addresses continual instruction tuning for Large Vision-Language Models (LVLMs). It introduces **COAST**, a benchmark spanning domain-incremental, capability-incremental, and dataset-incremental settings, and proposes **Continual LLaVA**, a rehearsal-free method that freezes the LVLM and learns "dual increment embeddings" — intrinsic embeddings selected from a low-rank pool via instruction similarity, and contextual embeddings that aggregate previous-task knowledge through a weighted sum. The paper claims substantial improvements over sequential training (13.06% absolute accuracy gain, 13.25% forgetting reduction on COAST-domain).

## Strengths

1. **Timely and well-motivated problem framing.** The paper clearly identifies a real gap: existing LVLM instruction tuning focuses on single tasks, while real-world deployment requires continual adaptation across shifting domains, capabilities, and datasets. The three-way categorization (domain, capability, dataset) is intuitive and provides a structured evaluation framework beyond prior dataset-incremental-only setups. (Lines 16–18)

2. **Conceptually clean and rehearsal-free method design.** The decomposition into intrinsic increment embeddings (task-specific, selected via similarity from a low-rank pool) and contextual increment embeddings (inter-task dependencies, aggregated with learnable weights) is well-motivated and logically maps onto the problem. The parameter-efficient, LoRA-style approach avoids the memory overhead of experience replay, which is a practical advantage. (Lines 20–22, Sec. 3.2)

3. **Articulated distinction from prior work.** The paper correctly notes that prior continual learning works for LVLMs are limited to dataset-incremental scenarios, and explicitly distinguishes its contributions from EMT and other works that address different problems (e.g., vision encoder classification rather than instruction following). (Lines 44–45)

## Weaknesses

### Fatal
None.

### Major

1. **Text-only selection of intrinsic increment embeddings may be insufficient for vision-language tasks.** The selection mechanism (Eq. 1–3, lines 78–88) relies entirely on Sentence-BERT embeddings of the *user instruction text*, ignoring the image content. For tasks where instructions are generic (e.g., "What is in this image?"), the same text could correspond to chart QA, medical QA, or scene understanding — tasks requiring fundamentally different visual capabilities. The paper does not discuss this limitation, provide analysis of when text-only similarity suffices, or offer any ablation comparing text-only vs. image-aware selection. Since the selection mechanism is the core means of routing to task-specific parameters, this gap undermines confidence in the method's robustness across all three incremental settings. The examples given (chartqa vs. medicalqa) rely on domain-specific language in the instruction, which supports the design in those cases, but the paper does not address cases where instructions are generic.

2. **No discussion of limitations.** The paper contains no limitations section and does not acknowledge any potential weaknesses of the approach (text-only selection, stop-gradient constraints on cross-task reinterpretation, sensitivity to pool size N or selection count M). This is a significant omission for a paper proposing both a benchmark and a method.

### Minor

1. **COAST benchmark description is underspecified in the main text.** While the three settings are named with illustrative examples (chartqa, documentqa, iconqa for domain; conversation, complex reasoning, detail description for capability), the paper does not provide: (a) the full list of datasets used per setting, (b) the number of tasks per setting and their ordering, (c) the evaluation metrics (average accuracy, forgetting, forward/backward transfer), or (d) how existing benchmarks were repurposed. The statement "we collect and re-purpose existing benchmarks" (line 17) is too vague for a benchmark claimed to "establish an assessment standard" (line 135). Some of these details may appear in the experiments section (`\input{exps/4_1_setting}`), but the main text should be self-contained enough for a reader to understand the benchmark without the experimental appendix.

2. **The alignment loss does not directly ensure task-relevant increment embeddings.** The first-stage loss (Eq. 6, line 115) only encourages proxy embeddings to be similar to the Sentence-BERT surrogate embedding. It does not enforce that the corresponding increment embeddings $\mP_n$ are actually useful for the task. The proxy embeddings could learn to mimic Sentence-BERT without providing discriminative low-rank information to the LLM.

3. **Stop-gradient on previous contextual embeddings limits cross-task reinterpretation.** By freezing previous-task embeddings via `sg(·)` (Eq. 4, line 98), the model cannot revisit or reinterpret earlier knowledge in light of new correlations discovered in later tasks. This is a design choice that could be probed in ablation, but is not discussed or justified beyond noting the gradient-blocking mechanism.

4. **Key hyperparameters (pool size N, selection count M) are not stated in the available text.** These are critical to understanding the method's capacity and computational cost but are absent from the method section.

### Trivial
None.

## Nice-to-Haves

- A table in the main text listing all COAST datasets, their sources, and per-setting composition would significantly strengthen the benchmark description.
- An analysis of cosine similarity distributions between instructions from different tasks, demonstrating that top-M selection consistently picks the correct task's proxies, would directly address the text-only selection concern.
- Reporting forward/backward transfer metrics in addition to average accuracy and forgetting would align COAST with standard continual learning evaluation practices.
- An ablation comparing text-only vs. image-aware selection (or justifying why text-only is sufficient) would strengthen the method's credibility.

## Removed Points

- **"Experimental evidence is not present in the extracted text"** — The experiments section is included via `\input{exps/...}` commands that the parser did not resolve. This is a formatting/parsing artifact, not an author error. The experiments exist in the original submission. Removed per rule on parser artifacts.
- **"The benchmark COAST is defined too vaguely" (as a fatal/major criticism)** — The paper describes three incremental settings with concrete examples; the full specification (dataset lists, evaluation protocols) would typically appear in the experiments section which is `\input`'d. Reduced to minor weakness about main-text self-containment.
- **"The adaptation to only the output linear projection is mentioned but not explained"** — The paper explicitly states "Our experiments in Sec.4.3 show that re-parameterizing all four linear projection layers is unnecessary" (line 104), referencing the ablation study. This is addressed in the paper.
- **Strength Finder claim about "Comprehensive empirical validation across multiple settings"** — This strength refers to content in the unverifiable experiments section and cannot be confirmed from the available text. Moved here as the claim may be valid but is not verifiable from the extracted content.
- Several generic Strength Finder statements about "significant performance gains" that cannot be verified without the experiments tables.

## Novel Insights

The most interesting observation that emerges from the reviews is the tension between the paper's conceptual elegance and a potential structural weakness. The dual-increment decomposition (intrinsic + contextual) is intuitively appealing and aligns well with the problem framing. However, the selection mechanism's reliance on instruction-text similarity alone creates a potential blind spot for vision-language tasks where instructions are underspecified. This is not a fatal flaw — in many of the paper's own examples (chartqa vs. medicalqa), the instruction text likely contains domain-specific language — but it represents a gap between the method's motivation (which emphasizes visual task requirements) and its implementation (which delegates discrimination to a text-only signal). A simple ablation or analysis of cross-task instruction similarity would resolve this tension. Additionally, the stop-gradient design means that the model commits to a fixed representation of each prior task rather than allowing continual refinement — a design choice worth examining given that real-world task boundaries are often fuzzy.

## Suggestions

1. **Add a direct analysis of the text-only selection mechanism.** Show cosine similarity distributions between instructions from different tasks to demonstrate that top-M selection correctly discriminates tasks. If there are failure cases (e.g., generic instructions shared across domains), discuss them and consider augmenting selection with visual features.
2. **Include a self-contained benchmark specification in the main text** — a table listing all datasets, their sources, per-setting composition, task ordering, and evaluation metrics (average accuracy, average forgetting, forward/backward transfer).
3. **Add a limitations section** acknowledging the text-only selection assumption, the stop-gradient constraint, and potential sensitivity to pool size N and selection count M.
4. **State key hyperparameters (N, M)** explicitly in the method section.
5. **Report the relative weighting of alignment loss and auto-regressive loss** in the two-stage training.

## Score and Decision

This paper addresses an important and timely problem with a well-motivated method and a novel benchmark. The conceptual framing is clear, and the dual-increment design is elegant. However, the text-only selection mechanism raises a significant concern about the method's robustness in the very setting it targets (vision-language tasks), and the absence of any limitations discussion or analysis of when selection succeeds/fails weakens the submission. The benchmark is promising but underspecified in the available main text. These issues are addressable and do not invalidate the contribution, but they prevent strong acceptance.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>
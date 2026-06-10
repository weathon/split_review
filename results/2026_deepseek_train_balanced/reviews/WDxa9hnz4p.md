## Summary

Auto-Demo Prompting (ADP) is a simple modification to batch prompting: instead of asking the LLM to output just answers, the prompt instructs the model to repeat each question before answering it. Because of the autoregressive generation loop, earlier question-answer pairs automatically become in-context demonstrations for later questions in the batch. The paper formalizes this connection (ADP ≈ Batch Prompting + Few-Shot Demonstrations), adapts a retrieval-based batch data selection method, and evaluates on five NLP tasks with GPT-4o and GPT-4o-mini.

## Strengths

- **Clean formal framing bridging batch prompting and few-shot prompting.** Algorithms 1–3 and Equation (1) (lines 75–125) lay out Few-Shot Prompting, Batch Prompting, and Auto-Demo Prompting side by side, showing how the autoregressive generation process converts earlier QA pairs into demonstrations. This is a conceptually clear and useful formulation that prior batch-prompting work did not articulate.

- **Consistent empirical improvement over standard batch prompting.** Across five tasks (BoolQ, GSM8K, SVAMP, RTE, QQP) and two model sizes, the ablation experiments (Figure 1) show ADP consistently tracking above standard batch prompting at the same batch size. A standout result: GSM8K with GPT-4o at batch size 16 reaches 95.7%, surpassing even the single-prompt baseline of 95.3% (line 193).

- **ADP with retrieval-based batch data selection can outperform single prompts at large batch sizes.** For RTE (GPT-4o-mini, batch size 48), ADP + retrieval-based selection achieves 89.5% vs. 88.8% single-prompt; for QQP (GPT-4o, batch size 32), it achieves 87.3%, 2.0% above the single prompt (lines 207–209). This demonstrates that ADP can turn batch prompting from a degradation-prone method into one that leverages many-shot effects.

- **Minimal prompt modification with measurable impact.** The method adds roughly two lines to the batch prompt instruction (line 127) and changes no other aspect of the pipeline, yet yields consistent gains. This contrasts with prior work requiring multiple inference passes (e.g., majority voting).

## Weaknesses

### Fatal

None.

### Major

- **No results table — the paper relies entirely on figures for its experimental evidence.** The "Results and Discussions" section (lines 192–223) contains zero tables. The only numeric values given in the body are a handful of isolated data points chosen to illustrate successes. Readers cannot inspect the full matrix of dataset × model × batch size × method without reverse-reading bar heights from Figure 1 and Figure 2. For a paper whose central claim rests on empirical validation across five tasks, two models, and multiple batch sizes, this is a significant evidential gap. Figures communicate trends; tables communicate precision, and both are needed at a top venue.

- **The "approximate equivalence" claim (ADP ≈ Batch Prompting + Few-Shot Demonstrations) is not directly tested against the natural baseline: few-shot prompting with gold demonstrations at the same N.** The paper's own formal framing (Equation 1) invites this comparison. Running ADP at batch size N against standard N-shot prompting with ground-truth demonstrations would quantify how much value the model's own generated demonstrations provide versus real ones, and would directly test the core hypothesis. Without it, the central theoretical claim remains an untested assertion about the mechanism.

### Minor

- **No variance or reliability estimates are reported.** Temperature is set to 0 (line 191), which eliminates sampling noise, but batch composition (especially for the random-batch conditions) introduces genuine variability. The claimed improvements are sometimes very small (e.g., 0.4% on GSM8K). Without multiple trials, standard deviations, or confidence intervals, it is impossible to assess whether these differences are meaningful or within the noise of batch composition.

- **Token cost is not quantified despite efficiency being a stated motivation.** The abstract claims "only a slight compromise in token usage," but no analysis of output token counts, wall-clock time, or API cost is provided. ADP roughly doubles output length (QA pairs vs. bare answers), which is a non-trivial increase especially for large batch sizes. The efficiency-accuracy trade-off the method claims should be directly measured.

- **Evaluation is limited to two models from a single provider (OpenAI's GPT-4o and GPT-4o-mini).** Whether ADP generalizes to other decoder-only architectures (e.g., Llama-3, Mistral) is untested. The method's effectiveness likely depends on how precisely the model follows the output-format instruction, which may vary across model families.

- **The batch data selection algorithm (Algorithm 4) is O(|D|²)** — it computes pairwise similarities between all data points. This scaling cost is not discussed as a limitation, even though it may be impractical for large real-world datasets.

- **The paper offers no analysis of cases where generated demonstrations are wrong.** If earlier answers in a batch contain systematic errors (e.g., arithmetic mistakes in a math problem), these could propagate to later questions. The paper cites Min et al.'s finding that incorrect labels in few-shot demonstrations cause minimal degradation, but that finding was for human-provided demonstrations, not for model-generated answers that could have correlated errors. This merits empirical investigation.

- **The claim of "formal theoretical analysis" (abstract, line 35) overstates what is provided.** The paper presents a notational comparison of conditional probability formulations (Algorithms 1–3), which is a formal description of the method, not a theoretical analysis in the sense of proving bounds, characterizing behavior, or deriving guarantees.

### Trivial

- The AGI speculation in the conclusion (line 240) is out of place for a paper about a prompt-formatting technique.
- The phrasing "consistently outperforms Batch Prompt in most experiments" (line 193) is mildly self-contradictory; "consistently" and "most" pull in opposite directions.
- The claim that ADP "eliminates the need to manually pack [demonstrations] into the input prompt" (line 31) could be read to suggest the questions themselves need not be packed, which is incorrect.

## Nice-to-Haves

- Few-shot prompting with gold demonstrations as a baseline (see Major weaknesses — this is the most important missing experiment).
- A small ablation on when/why generated demonstrations hurt rather than help (e.g., by manually corrupting early answers).
- Reporting the actual batch-data-retrieval cost (wall time or embedding count) to contextualize the O(|D|²) complexity.
- Testing on at least one open-weight decoder-only model to improve generality claims.

## Removed Points

These points from the reviewers are flagged for removal (treat with caution):

- **"BP notation appears garbled"** (harsh critic, line 95): The notation `F(a_n | BP + Q_{1:n}, {a_i}_{i=1}^{n-1})` is standard and correctly describes batch prompting — the model sees all questions upfront and previous answers. No verification issue found.
- **"Batch sizes differ with no justification"**: The paper explicitly justifies this: GPT-4o-mini has a 16k output limit while GPT-4o has 8k (line 191). The batch size choices directly follow from context length constraints.
- **"ADP outperforming single prompts is a misleading comparison"** (as a critical/fatal issue): This comparison is not misleading in context — the established finding is that batch prompting degrades with size, so showing ADP+batch-selection exceeds single-prompt accuracy is a genuine result. The paper also provides the fair comparison (ADP vs. standard batch prompting). The framing could be more precise, but this does not constitute a serious weakness.
- **"Missing related works"**: Not verifiable for inclusion; removed per instructions.
- **Reproducibility nitpicks** about undisclosed hyperparameters or implementation details: The paper describes the method completely — temperature=0, embedding model specified, batch sizes given. No critical detail is withheld.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a perspective that the authors themselves missed — the main novel lens (ADP connects batch prompting to few-shot through autoregressive generation) is the paper's own contribution.

## Suggestions

1. **Add a full results table** covering every dataset × model × batch size × method combination, including both ADP and standard batch prompting values. This is the single highest-impact change the authors can make.
2. **Run the missing few-shot baseline:** compare ADP at batch size N against few-shot prompting with N gold (ground-truth) demonstrations on the same questions.
3. **Report variance** by running the random-batch condition with at least 3–5 different random orderings and reporting mean and standard deviation.
4. **Quantify the token cost:** report average output tokens per batch for both ADP and standard batch prompting, and the resulting API cost (or wall time) per example.
5. **Test on at least one open-weight decoder-only model** (e.g., Llama-3-70B) to demonstrate generality beyond OpenAI's API.
6. **Add a brief error analysis** section examining cases where early incorrect answers affect later ones.

## Score and Decision

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>
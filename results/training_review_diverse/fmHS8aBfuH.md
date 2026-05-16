Now I have all the information I need. Let me produce the consolidated review.

## Summary

This paper proposes DIESEL, a lightweight, training-free inference guidance technique that reranks candidate tokens during LLM decoding based on cosine similarity between an off-the-shelf sentence embedding of partial completions and textual negative concepts. The method operates in three steps: candidate selection via Top-p sampling, semantic similarity scoring against predefined negative concepts using MiniLM (33M parameters), and token reranking via a weighted combination of original probability and safety score. Evaluations on AdvBench, TruthfulQA, and jailbreak scenarios across three 7B/8B models show DIESEL reduces unsafe responses with only ~1.5× runtime overhead (versus 186×+ for RAIN), though with a truthfulness cost (60%→51% on TruthfulQA).

## Strengths

- **Lightweight runtime overhead is convincingly demonstrated.** DIESEL adds only 1.46×–1.64× inference time across Llama 3, Mistral, and Vicuna, compared to RAIN's 186×–202× (Table 1). This directly supports the paper's core claim of a practical, real-time-capable method. The use of a 33M-parameter MiniLM (0.47% of a 7B model) for embedding is a well-motivated design choice that explains the low overhead.

- **Safety improvement on uncensored models is clearly shown.** On AdvBench with uncensored Llama 3, DIESEL reduces severity-5 responses from 313 to 215 (Figure 2), and the transition analysis (Figure 3) shows 94 responses move from severity 5 to severity 1. This provides concrete evidence that the method works as a standalone safeguard without fine-tuning.

- **Effectiveness as an additional defense layer against jailbreaks is validated.** Under GCG attacks on safety-aligned Mistral and Vicuna, DIESEL substantially reduces severity-5 responses while increasing score-1 (refusal) responses (Figure 4). This supports the claim that DIESEL can complement existing safety measures.

- **The core idea is technically clean and well-motivated.** Using natural-language textual descriptions of negative concepts (rather than requiring ML expertise to define safety boundaries) is a practical advantage. The three-step algorithm is clearly described, and the reliance on off-the-shelf components makes the method accessible.

- **Evaluation spans multiple models and settings.** Three LLMs (Llama 3, Mistral, Vicuna), two safety scenarios (standalone and jailbreak), a benign-prompt fidelity check (TruthfulQA), and a human evaluation provide reasonable breadth.

## Weaknesses

### Fatal

None. The paper's core claims—that DIESEL is a lightweight, training-free inference guidance method that measurably improves response safety—are supported by evidence. The weaknesses below concern overclaiming and evaluation gaps, not invalidated claims.

### Major

- **"Outperforms state-of-the-art techniques" (line 60) is overclaimed relative to the evaluation.** The paper compares DIESEL against only vanilla inference and RAIN (a single training-free baseline that performs anomalously poorly). While the paper scopes itself as a *training-free* method (line 309: "the only competitive inference guidance technique that does not involve model fine-tuning"), the unqualified claim "outperforms state-of-the-art techniques" suggests broader validation than what is presented. Missing comparisons to even simple baselines—such as a system prompt emphasizing safety, or a post-hoc output filter like Llama Guard—make it impossible to assess whether DIESEL is actually state-of-the-art among practical inference-time defenses. These baselines are lightweight to implement and would substantially strengthen the paper's claims.

- **The truthfulness degradation (60%→51% on TruthfulQA) is serious and understated.** Describing a 15% relative drop as maintaining "comparable levels of truthfulness" (line 358) is misleading. If DIESEL is intended for real-world safe deployment, reducing factual accuracy by this margin is a practical concern that deserves explicit discussion, not a gloss. The paper offers no analysis of what types of questions are most affected, whether the drop is concentrated in certain categories, or whether a lower α could mitigate it. Since the method is meant to "not interfere with benign prompt responses" (contribution list, line 65), this evidence gap weakens that claim.

### Minor

- **RAIN's near-floor performance relative to no defense raises configuration concerns.** RAIN performs worse than vanilla inference across all three models (Figure 2). The paper attributes this to model type mismatch and binary classification limitations (lines 319–322), but without verification that RAIN's hyperparameters (system prompts, search depth, etc.) were tuned reasonably for conversational models, the comparison is not a fair stress-test. This weakens the claim of "outperforming" RAIN specifically.

- **User study is underpowered for the weight it carries.** Twenty participants with no significance testing, no confidence intervals, and no comparison against any defense baseline besides vanilla inference provides only weak support for claims about practical effectiveness. The 80% preferability result is suggestive but not conclusive—especially since participants were comparing DIESEL responses only against vanilla responses, not against any existing safety method.

- **The "beyond safety" experiment lacks a baseline and has an unclear interpretation.** The horror-movie summarization task compares DIESEL-generated summaries against *original dataset summaries* (not against a control condition like "instruct the model to avoid horror elements"). Without a baseline, it is unclear whether DIESEL is adding value beyond what a simple instruction could achieve. Furthermore, the LLM-judge comparison against the *original* summary (from the dataset, potentially longer/different in style) confounds the measurement.

- **Hyperparameter α=0.98 is extreme and its sensitivity is not discussed in the main text.** A weighting of 0.98 on the safety score means the original token probability is almost entirely overridden. This almost certainly contributes to the TruthfulQA drop. The paper defers ablation to supplementary material (line 289), but the main text should at least discuss the severity of this choice and its implications for the quality/safety trade-off.

- **No variance or confidence intervals are reported for any main results.** The score distributions in Figures 2–4 and the TruthfulQA results are presented as point estimates without measures of variability. For a method that involves stochastic sampling (b=20 draws from Top-p), reporting variance across multiple runs or seeds is important for reliability.

- **No seed or run-level control is stated for the token sampling.** Since Step 1 samples b tokens from the Top-p distribution using multinomial sampling, results could vary across runs. Not stating whether random seeds were fixed or reporting variance across runs is a reproducibility gap.

### Trivial

- The paper uses "comparable" (line 358) to describe a 9-percentage-point truthfulness drop—this is a substantive mischaracterization, though noted above under Major.
- The figure captions and table labels are present but not self-contained; understanding detailed results requires reading the surrounding text.

## Nice-to-Haves

- Compare DIESEL against a system-prompt-only defense (e.g., "you must refuse all harmful requests") and a post-hoc output filter (e.g., Llama Guard). These are cheap baselines that would contextualize DIESEL's added value.
- Report an ablation of α (e.g., 0.5, 0.8, 0.95, 0.98) and b (e.g., 5, 10, 20, 50) in the main paper rather than deferring to supplementary material.
- Replace or complement the "beyond safety" experiment with a domain where filtering is unambiguously beneficial and where a simple instruction baseline exists (e.g., suppressing political slant in news generation).
- Report per-token safety score evolution over the course of generation in a case study, to illustrate how the method's effect changes as the prefix grows.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **"The ablation studies promised in the supplement are not available in the review."** — The parser strips supplementary material from all papers. The authors likely provide these in the full submission. Removed per rule: no criticism about missing appendix/supplement.

2. **"Inference time analysis comparing only to RAIN is a strawman — the paper should also report absolute times and compare to no defense."** — Table 1 already reports multipliers *relative to vanilla inference* (no defense). The comparison to RAIN is the relevant one since both are training-free inference guidance methods. The table clearly states "Values represent the inference time increase compared to a vanilla model." Removed as factually inaccurate.

3. **"No comparison to output filters like Llama Guard, Perspective API, or keyword blocking for inference time."** — Output filters operate post-hoc and are architecturally different from generation-phase guidance. The paper's runtime claim is about generation overhead, not end-to-end comparison with detection systems. Removed as evaluating against the wrong class of expectations.

4. **"The claim that SOTA needs definition"** — Line 309 specifies "the only competitive inference guidance technique that does not involve model fine-tuning," providing context. The overclaiming issue (line 60) is kept above as a real weakness, but not for lack of definition.

5. **"The binary classification criticism of RAIN is not demonstrated"** — The paper states this as a hypothesis (lines 319–322), not a demonstrated result. This is a reasonable speculation. Removed as an over-reading of a stated hypothesis.

6. **"Claiming that the paper should report inter-rater agreement for GPT-4o"** — LLM-as-a-judge is the established paradigm in this literature (cited by RAIN and SafeDecoding), and requiring human calibration for every use is not standard practice. Removed as evaluating against non-standard expectations.

## Novel Insights

None beyond the paper's own contributions. The reviews primarily surface evaluation gaps and overclaiming issues rather than offering new analytical perspectives on the method itself.

## Suggestions

1. **Narrow the claims to match the evidence.** Replace "outperforms state-of-the-art techniques" with "outperforms the only comparable training-free method (RAIN) while adding minimal overhead." Add at least one simple baseline (system prompt defense, or a post-hoc filter) to substantiate a stronger claim.

2. **Address the TruthfulQA drop honestly.** Either (a) show that a lower α (e.g., 0.5–0.8) recovers truthfulness while preserving most safety gains, or (b) explicitly reframe the contribution as a tunable safety/quality trade-off where users set α based on their tolerance for factual degradation.

3. **Report confidence intervals or variance** for the main safety score distributions and the TruthfulQA result. Run multiple seeds to establish stability of the sampling-based candidate selection.

4. **Strengthen the user study** by including at least one alternative defense (system prompt) and reporting statistical significance.

5. **Add a proper control to the "beyond safety" experiment** — compare DIESEL against a prompt instructing the model to "avoid horror elements" — to show the method adds value beyond what is achievable with a simple instruction.

## Score and Decision

This paper proposes a genuinely useful and well-engineered method. The core technical contribution—lightweight, training-free, textually programmable inference guidance—is clear and potentially impactful. The runtime efficiency result (1.5× overhead) is the strongest piece of evidence and is convincingly presented. However, the evaluation has two structural weaknesses that prevent acceptance in the current form: the overclaiming relative to insufficient baselines, and the understated truthfulness degradation. These are addressable with additional experiments. The paper is solid but not yet ready for publication.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>
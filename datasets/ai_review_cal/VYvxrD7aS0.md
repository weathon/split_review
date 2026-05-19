- Decision: Accept
- Avg Score: 6.75
- Scores: 6, 5, 8, 8
Now I have all the data I need. Let me produce the final consolidated review.

## Summary

The paper introduces ObscuraCoder, a suite of decoder-only Code-LMs (255M–2.8B parameters) pre-trained with a novel obfuscation-grounding objective. The key idea is to train on bidirectional translation between source code and stochastically obfuscated counterparts, mixing in standard autoregressive language modeling on each. The authors construct ObscuraX, a dataset of ≈55M source–obfuscated code pairs across seven languages, and show that models pre-trained with this recipe consistently outperform equally-sized causal LMs — and match or exceed several frontier models trained on 5×–22× more data — on CodeXGLUE defect detection, ReCode robust completion, and BigCodeBench library-oriented code generation.

## Strengths

- **Consistent and sizeable gains over equally-sized causal LMs on both syntactic and semantic benchmarks.** Table 1 shows ObscuraCoder 2.8B outperforms the matched CausalLM by clear margins on CodeXGLUE (syntactic understanding), ReCode (semantic robustness), and BigCodeBench (library-oriented generation). These gains hold across model sizes (255M–2.8B) and are achieved with the same total token budget (≈272B), providing clean evidence that the obfuscation-grounding objective drives the improvement.

- **Clear superiority over the DOBF de-obfuscation objective.** In the head-to-head ablation (Table 3), ObscuraCoder exceeds a decoder-only DOBF variant (trained on the same corpus with the same token budget) on all tasks, with the gap widening at larger model sizes. This demonstrates that the bidirectional translation objective (training on both source and obfuscated code, without masking the obfuscated form from the loss) is more effective than the identifier-map-only approach of prior de-obfuscation pre-training.

- **Informative negative result on post-hoc training.** The CausalLM-CP experiment (Table 3) shows that applying obfuscation translation as continued pre-training to an already-trained causal LM yields negligible or negative gains, while ObscuraCoder trained from scratch obtains significant improvements. This is a valuable finding that supports the paper's claim that early integration of obfuscation grounding during pre-training is critical.

- **Large-scale, multilingual obfuscation dataset.** ObscuraX (≈55M pairs across 7 languages) is the largest collection of its kind. The stochastic obfuscation procedure (varying \(p_{obf}\) up to 0.9, limiting to 150 members per syntactic category) is principled and the construction is described in sufficient detail to be reproducible.

## Weaknesses

### Fatal
None.

### Major

- **Import obfuscation is not isolated, so RQ2 cannot be definitively answered.** RQ2 asks whether *supplementing* identifier obfuscation with import obfuscation improves library-oriented code generation. The only evidence provided is that ObscuraCoder (which includes import obfuscation on ≈25% of samples) outperforms causalLM on BigCodeBench. There is no ablation comparing ObscuraCoder *with* versus *without* import obfuscation. The reader cannot tell whether the BigCodeBench gains come from the general obfuscation objective, the translation objective, or import obfuscation specifically. An ablation that disables import mangling (i.e., correct imports in 100% of obfuscated samples) is necessary to support RQ2.

### Minor

- **Abstract and conclusion claim demonstrated improvements on tasks not prominently featured in the main evaluation.** The abstract claims "improved capabilities in multilingual code completion" and "multilingual code commit summarization." The paper states it evaluates "five zero-shot and fine-tuning tasks" (Section 5), but only three tasks (CodeXGLUE, ReCode, BigCodeBench) are discussed in the visible main text. If the two remaining evaluations (likely the multilingual completion and summarization) are relegated to the appendix, the main paper would benefit from at least briefly summarizing them alongside the presented three tasks, so readers can judge the breadth of claims without consulting supplementary material.

- **The framing of obfuscation as "a way out of the code data bottleneck" is overstated.** The paper argues obfuscation "surmounts the code data-wall" and provides "a way out of the code data bottleneck" (Sections 1, 7). However, obfuscation as implemented is a transformation applied to *existing* code — it increases token diversity from a fixed source corpus but does not generate new programming constructs, idioms, or APIs. This is data augmentation, not a new source of independently meaningful code. The paper would be better served by framing this as a training-time regularizer or disentanglement objective that increases data efficiency, rather than as a solution to the scarcity of human-written code.

- **No ablation isolating the translation objective from the language modeling on obfuscated code.** The paper does not compare ObscuraCoder to a variant that trains on obfuscated code via standard causal LM only (no translation pairs). Such an ablation would distinguish whether the gains come from the *mapping* between source and obfuscated forms (the translation objective) or simply from adding obfuscated tokens to the training corpus and exposing the model to obfuscated representations during LM training.

- **No confidence intervals or variance reported.** Results are reported as single numbers without standard deviations across multiple seeds. This makes it difficult to assess whether the reported gaps (e.g., 70.0 vs. 67.5 on CodeXGLUE) are statistically meaningful. While single-run evaluation is common in large-scale pre-training papers, the fine-tuning results (3 epochs, LoRA) could reasonably be replicated a few times.

### Trivial

- The conclusion states ObscuraX is "≈119B-token," while Section 3 describes it as "≈55M samples." This is not a contradiction (samples vs. tokens) but the relationship between these two numbers could be clarified.

## Nice-to-Haves

- A sensitivity analysis on the obfuscation proportion hyper-parameter \(p_{obf}\) (varied up to 0.9 but not ablated) would be informative.
- A probing experiment (e.g., probing hidden states for syntactic vs. semantic information) would provide more direct evidence for the claimed disentanglement effect than downstream task performance alone.
- Clarifying whether the custom BPE tokenizer (trained on 5B tokens) is shared between ObscuraCoder and the CausalLM baseline, and how the obfuscation special tokens (VAR_n, FUNC_n, etc.) affect tokenization efficiency relative to models without them.

## Removed Points

These points were considered but moved here with justification:

- **"Missing results for multilingual code completion and code commit summarization" (Harsh Critic #1, framed as fatal):** The paper states it evaluates "five zero-shot and fine-tuning tasks." The results for these tasks are likely present in the appendix (which was stripped during PDF extraction). Per the review guidelines, criticisms predicated on absent appendix content that exists in the original submission are removed. The criticism is downgraded to a Minor weakness about presentation clarity in the main review above.

- **"Comparison to frontier models not properly controlled" (Harsh Critic #2):** The paper explicitly states (Section 5): "For fine-tuning tasks, **all models** are trained for three epochs using a cosine scheduler with a peak learning rate of 5e-5 using LoRA modules coupled with trainable embeddings." It further specifies "LoRA modules with rank 64 for classification tasks and 256 for open-ended generation." The critic's claim that the paper "does not specify whether the same LoRA fine-tuning protocol was applied" is factually wrong — the paper does specify this, using "all models." Removed as factually inaccurate.

- **"RQ3 (code completion side-effects) not addressed" (Harsh Critic additional note):** RQ3 asks about regression on code completion. The paper evaluates on ReCode, which is a **robust code completion** benchmark (as stated in Table 1: "semantic understanding for robust code completion on ReCode"). RQ3 is thus directly addressed by the ReCode results. Removed as factually inaccurate.

- **"The table is garbled and ambiguous" / "partially illegible due to garbled formatting":** Parser extraction artifacts, not paper problems. Removed per formatting artifact rule.

- **"The paper does not discuss synthetic data generation as an alternative":** Scope creep. The paper is not required to comprehensively review every alternative data scaling approach. Removed.

- **"Tokenizer as a potential confound" (tokenizer trained on 5B tokens vs. frontier models):** The tokenizer comparison is relevant to the internal CausalLM vs. ObscuraCoder comparison (both use the same tokenizer), not to the frontier model contextualization where different tokenizers are expected. The internal comparison is controlled; the external comparison is illustrative. Weakened from the harsh critic's framing.

- **Strengths dropped from Strength Finder:** Several generic/superficial strengths were dropped (e.g., "the paper addresses an important problem"). The strengths in the main review are those with concrete, verifiable evidence in the paper.

## Novel Insights

The most interesting insight that emerges from synthesizing the reviews — beyond what the paper itself states — is that the post-hoc training failure (CausalLM-CP) is arguably more informative than the main positive results. The fact that obfuscation grounding must be present from the start of pre-training, and cannot be effectively grafted onto an already-trained LM, suggests the objective shapes the model's internal representations in a fundamental way during early training rather than simply teaching a task-specific skill. This finding has implications for the broader question of when in training to introduce structured objectives for Code-LMs. The missing import obfuscation ablation is the single largest gap: without it, the paper's second research question is structurally unanswerable from the presented experiments, and the claimed benefit of import mangling for library-oriented generation remains a plausible but unproven hypothesis.

## Suggestions

1. **(Critical) Add an ablation without import obfuscation:** Train an ObscuraCoder variant where imports are correct in 100% of obfuscated samples and compare on BigCodeBench. This is the only way to directly answer RQ2.
2. **Add an ablation of the translation objective vs. LM-only on obfuscated code:** Compare to a variant trained on obfuscated code via standard causal LM (no translation pairs). This isolates whether the mapping between source and obfuscated forms drives the gains.
3. **Tone down the "data-wall" framing:** Reframe obfuscation as improving data efficiency and disentanglement rather than as a new source of data that "surmounts" the data bottleneck.
4. **Briefly mention the two additional evaluation tasks in the main text** (multilingual code completion and code commit summarization) alongside the three presented tasks, even if full results are in the appendix.

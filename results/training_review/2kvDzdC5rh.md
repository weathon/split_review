I have verified all claims against the paper. Now I can produce the final consolidated review.

## Summary

IntentGPT proposes a training-free framework for few-shot intent discovery that leverages LLMs (GPT-3.5, GPT-4, Llama-2) through three components: an In-Context Prompt Generator (automatically generates task prompts from a few labeled examples), Semantic Few-Shot Sampling (selects relevant examples via embedding similarity), and Known Intent Feedback (injects known and discovered intents into the prompt to enable reuse). The method is evaluated on CLINC and BANKING benchmarks, where 50-shot GPT-4 variants achieve competitive or superior NMI/ARI/ACC scores compared to prior unsupervised and semi-supervised methods that require extensive training.

## Strengths

- **Training-free paradigm with strong empirical results.** IntentGPT requires no fine-tuning and only 10–50 labeled examples per known intent, yet achieves results competitive with or exceeding methods that use full training sets and multi-stage fine-tuning (Table 1). IntentGPT-4 50-shot achieves the best NMI (96.06 on CLINC, 85.94 on BANKING) and ARI (84.76, 66.66) among all methods compared.

- **Novel prompting techniques with clear ablation support.** Known Intent Feedback (KIF), Semantic Few-Shot Sampling (SFS), and In-Context Prompt generation (ICP) each show measurable gains in the ablation study (Table 2). KIF alone raises NMI by over 10 points on CLINC for GPT-3.5 (80.12 → 90.26), and the full combination achieves the best results.

- **Model-agnostic framework validated across diverse LLM families.** IntentGPT is evaluated on GPT-3.5, GPT-4, and Llama-2, demonstrating consistent improvements over baselines. Even the 0-shot variant of IntentGPT-4 outperforms all prior unsupervised baselines, while Llama-2 50-shot surpasses several semi-supervised models.

- **Reduction in human annotation and engineering effort.** The system eliminates the need for manual prompt engineering (ICPG generates prompts automatically) and requires only a handful of labeled examples rather than full labeled datasets and multi-stage training pipelines.

## Weaknesses

### Fatal

None. The paper's core claims are supported by evidence; the methodological concerns raised do not invalidate the results or the contribution.

### Major

None. The issues below are addressable and do not undermine the paper's fundamental contribution.

### Minor

- **Evaluation protocol differs from baselines in a way that is not acknowledged or justified.** IntentGPT clusters *SBERT embeddings of generated intent names* (line 86), whereas the baselines cluster *utterance embeddings* (the standard protocol in this literature). These are different objects: utterance-level evaluation measures how well utterance representations separate by intent, while IntentGPT's evaluation measures how well generated intent names cluster. The paper claims to follow "the standard choice" (citing Zhang et al., 2021), but the standard choice clusters utterance embeddings. The paper (i) does not note this divergence, (ii) does not justify why the two protocols are equivalent, and (iii) does not evaluate IntentGPT under the utterance-level protocol for a direct comparison. This does not invalidate the results (IDAS also clusters generated text), but it makes the reported numbers less straightforwardly comparable than the paper suggests.

- **Results on several mentioned datasets are not reported.** The experimental setting (line 201) states that IntentGPT is evaluated on SNIPS, StackOverflow, and multilingual data, but no results for these datasets appear anywhere in the paper. This is incomplete reporting for a submission that makes empirical claims.

- **Ablation shows heavy reliance on Known Intent Feedback, and the relative contribution of individual components is modest.** The gap between the simplest LLM baseline (no features, NMI=80.12 for GPT-3.5/CLINC) and the best variant (NMI=93.07) is largely explained by KIF alone (jump to 90.26). The additional gains from FS, SFS, and ICP are incremental (cumulative ~3 points). While the ablation is honestly reported, the framing as "novel prompting techniques" overstates the marginal contribution of the non-KIF components. The paper would benefit from clearer language about which component drives the results.

- **No analysis of generated intent names or qualitative error analysis.** The paper does not provide examples of discovered intent names or analyze whether they are semantically coherent, correctly separated from known intents, or simply different phrasings of existing intents. Without this, it is difficult to assess whether the method genuinely discovers meaningful new intents or memorizes/renames known ones.

- **NDI metric on BANKING is far from ground truth.** For BANKING (77 ground-truth intents), the best IntentGPT variant achieves NDI=83 (close), but many configurations are far off (e.g., NDI=574 or 997 for some GPT-3.5 variants in Table 2). This suggests the method has difficulty controlling the number of discovered intents, which is a core requirement for the task.

### Trivial

- The sensitivity of the ICPG's `x=2` examples-per-known-intent parameter is not analyzed.
- The DBSCAN epsilon for automatic K determination in clustering (set to 0.5) is not ablated or justified beyond a single value.
- "Self-improvement" in the contributions list (line 30) is an overly strong descriptor for what is essentially updating a list of known intent names.

## Nice-to-Haves

- A direct utterance-level evaluation of IntentGPT (e.g., using the LLM's latent representations as features for clustering) would strengthen comparability with baselines.
- Qualitative examples of generated intent names and their alignment with ground-truth intents would help assess the method's discovery behavior.
- Results on SNIPS, StackOverflow, and multilingual datasets should be added or the mention removed.

## Removed Points

These points are flagged to be removed — treat them with caution.

1. **"No direct LLM baseline without the proposed components"** — Factually wrong. The ablation table (Table 2) includes rows with no features enabled (first row for each model: no KIF, FS, SFS, ICP, SKIF). For GPT-3.5 this yields NMI=80.12; for GPT-4, NMI=86.32. This IS the simple LLM baseline the critic demands.

2. **"Unfair baseline comparison due to privileged information"** — Overstated. Semi-supervised baselines (DeepAligned, SCL, DSSCC, LatentEM) are trained on labeled utterance-intent pairs and do have access to the known intent taxonomy through their training data. IntentGPT's use of intent names in the prompt is a difference in mechanism, not information access. The real concern (different evaluation protocols) is addressed separately above.

3. **"Mismatched evaluation protocols" framed as "structural" / fatal** — This is a legitimate methodological concern but not a fatal flaw. IDAS (a cited baseline) also operates on generated text. The metrics ultimately compare cluster assignments to ground truth, which measures the same thing (grouping utterances by intent). The paper should acknowledge the difference, but it does not invalidate the results or the core contribution. This point has been moved to Minor above with appropriate nuance.

4. **"Self-improvement [KIF] is not a learning mechanism"** — A semantic complaint about the word "self-improvement." The term is loosely used in the abstract but the method section accurately describes what KIF does (line 77-79).

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface any observation about the method or results that the paper itself does not already address or acknowledge.

## Suggestions

1. **Disclose and justify the evaluation protocol difference.** Explicitly state that IntentGPT clusters generated intent name embeddings rather than utterance embeddings, explain why this is a valid and equivalent evaluation for a method that produces textual intent names, and ideally provide a supplementary comparison under the utterance-level protocol.
2. **Add qualitative analysis of generated intent names.** Show examples of test utterances with their ground-truth and predicted intent names to help readers assess whether the LLM is genuinely discovering new intents or simply renaming known ones.
3. **Complete the reporting.** Add results for SNIPS, StackOverflow, and multilingual data, or remove the claim that these datasets were used.
4. **Tone down the "self-improvement" framing** and be more precise about what KIF contributes relative to other components.

## Score and Decision

The paper makes a useful contribution by demonstrating that frozen LLMs with carefully designed prompts can perform intent discovery competitively with trained models, using far less labeled data. The core claim — that an LLM-based, training-free approach can match or exceed prior trained methods — is supported by the experimental results. The minor weaknesses (protocol divergence, incomplete reporting, modest marginal gains from non-KIF components) are addressable and do not threaten the paper's validity.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>
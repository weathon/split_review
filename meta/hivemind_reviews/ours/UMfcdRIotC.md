## Summary
This paper proposes two approaches for model-agnostic explanations of NLP black-box models by approximating counterfactuals (CFs): (1) directly generating CFs using LLMs, and (2) a matching approach that learns a causal embedding space via a contrastive objective guided by LLM-generated CFs at training time. The paper also introduces a formal faithfulness criterion (Order-Faithfulness), provides a theorem connecting approximated CF methods to this criterion, and empirically validates both approaches on the CEBaB benchmark and a new stance detection benchmark. The main findings are that LLM-generated CFs achieve the strongest explanation quality, the learned causal representation model outperforms existing matching baselines, and Top-K aggregation universally improves all methods.

## Strengths
- **Strong empirical validation on a standard benchmark.** Table 1 (reported as the main results table) shows that generative CF methods (especially fine-tuned T5) achieve substantially lower error across all three metrics (L2, Cos, ND) and across all five explained models (DistilBERT, BERT, RoBERTa, Llama-2 7B, Llama-2 13B) compared to all matching baselines. The causal representation model consistently beats six matching baselines (Random, Propensity, Approx, PT RoBERTa, PT S-Transformer, FT S-Transformer), often by a large margin on L2 error.

- **Novel and well-motivated matching approach.** The causal representation learning method (§3.2) is principled: it uses six contrastive loss components to encode the desired ranking order (misspecified matches ≺ misspecified CFs ≺ valid matches ≺ generated CFs), and the ablation study (§5.1, Table 3) demonstrates that removing any component degrades performance under challenging candidate-set conditions. The finding that the method works even without human-annotated concepts (using LLM-predicted annotations, row 4 of Table 3) is practically valuable.

- **Universal Top-K improvement is a clean, reproducible finding.** The paper demonstrates (Table 1, bottom rows vs. top rows; Figure 2) that aggregating over K=10 CFs/matches reduces error for every examined method, including generative models. The "✓-shaped" error curve for the causal model (Figure 2) provides intuitive evidence that the learned similarity ranking is meaningful.

- **Comprehensive ablation study.** Section 5.1 systematically isolates the effect of the backbone encoder, filtering of misspecified CFs, removal of each contrastive component, and use of LLM-predicted (vs. human-annotated) concept values across three different candidate-set conditions. This establishes that only the full six-component loss with filtering is robust across all conditions.

- **New stance detection benchmark as a proof of concept.** Section 6 constructs a CEBaB-style benchmark for stance detection using GPT-4, enabling out-of-distribution evaluation (different topics between the candidate set and test examples). Table 5 reproduces the main findings from CEBaB, supporting the generalizability of the approach.

## Weaknesses
### Fatal
None.

### Major

- **The Order-Faithfulness theorem is not properly supported as stated.** The theorem (lines 213–215) asserts that approximated CF explanation methods are order-faithful "for every DGP G." The proof sketch (line 217) claims this follows from showing "the expected prediction of an approximated CF is equal to the interventional one." This equality would require the approximation to be unbiased — a condition that depends on the quality of the LLM generation or matching process. The paper acknowledges "reasonable assumptions" (line 99) but never states them. The theorem statement itself does not mention any assumptions, and the proof sketch provides no mechanism by which the equality would hold for arbitrary approximations across every possible DGP. This gap undercuts the theoretical pillar of the paper. The empirical contributions remain valuable, but the theoretical claim as presented is not rigorous.

### Minor

- **The "SOTA" claim over model-agnostic explainers relies on a transitive comparison.** The paper claims CF-generating LLMs are "SOTA model-agnostic explainers" (lines 27, 337), but the experiments compare only against matching baselines and the paper's own generative variants. Standard model-agnostic methods (LIME, SHAP, Integrated Gradients for concepts, Causal Proxy Model) are excluded based on a citation that "Approx outperforms all seven tested baselines" (line 324, citing CEBaB). While this is a reasonable reference to prior work, it is not a direct comparison. The SOTA claim would be stronger with a direct head-to-head comparison on at least one representative non-matching baseline.

### Trivial

- The paper is duplicated: §3 appears twice (lines 63–154 and 156–277) with slightly different text and structure. This appears to be a compilation artifact from the PDF extraction, not a content issue, but the redundant sections should be cleaned up. (Clarification: this is likely a parser artifact from the submitted PDF and not an author error; flagging it only in case the original submission also has this issue.)

## Suggestions
1. **Strengthen the theoretical claim.** Either state the explicit assumptions under which unbiasedness of the approximated CF holds (and acknowledge when these assumptions may fail), or weaken the claim to reflect that approximated CF methods are order-faithful *under the assumption that the approximation is unbiased* (or some specific error bound). The proof sketch needs to be expanded to a proper proof, even if in an appendix.

2. **Add one direct non-matching baseline.** Even a single representative from LIME/SHAP/CPM on one explained model would substantially strengthen the SOTA claim by removing reliance on the transitive comparison alone.

3. **Provide a small human evaluation for the stance detection benchmark.** A human-annotated subset of 50–100 CFs would address the circularity concern and make the benchmark more broadly useful to the community.

4. **Include the efficiency measurements in the main paper** (or at least summarize them briefly, e.g., "matching runs in X ms per example vs. Y s for generation") rather than deferring entirely to the appendix.

## Score and Decision

**Overall assessment:** This is a solid empirical paper with a novel method (causal representation learning for matching), a useful theoretical framing (order-faithfulness), thorough experiments on CEBaB (24 interventions × 5 models), an informative ablation study, and a new benchmark. The main weakness is the under-supported theoretical claim, which does not invalidate the empirical contributions but prevents the theory from being a clean strength. The contributions are significant enough for acceptance at a top conference.

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>

## Questions


## Decision
Accept

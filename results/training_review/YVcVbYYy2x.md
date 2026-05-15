Now I have a thorough understanding of the paper and can systematically cross-check each reviewer claim. Let me compose the final consolidated review.

---

## Summary

This paper introduces MeCo, a fine-tuning-free plug-in module that uses a learned linear probe on LLM internal representations (following the RepE framework) to detect a "meta-cognition" signal — i.e., whether the model can answer a query on its own or should invoke external tools/retrieval. A two-threshold decision strategy is then applied to override the model's raw Yes/No first-token output. The authors also contribute a new benchmark (MeCa) covering diverse tool-use and RAG scenarios. Experiments on Llama-3-8b, Llama-3-70b, and Mistral-7b show consistent accuracy improvements over a naive first-token baseline and a softmax-based $P_{\text{Yes}}$ baseline.

## Strengths

1. **MeCo consistently improves decision-making accuracy across models, benchmarks, and settings.** On Metatool without context, MeCo raises Llama-3-8b accuracy from 53.1 (Naive) to 65.9 and Mistral-7b from 51.5 to 63.4. Tables 1–3 show similar gains on the more complex MeCa benchmark and on adaptive RAG, and the improvements hold across both pre- and post-fine-tuning models and both with- and without-context prompts. This directly supports the paper's central empirical claim.

2. **Fine-tuning-free, low-cost integration.** The probe is trained via PCA on contrastive difference vectors from a small number of query–response pairs (the exact number is not stated, but the paper claims few are needed). No fine-tuning of the base LLM is required, and MeCo can be stacked on top of fine-tuned models for additional gains. This practical efficiency is a genuine advantage.

3. **A comprehensive new benchmark (MeCa) with human review.** MeCa-Tool covers 6 tasks with 7,000 queries, including multi-turn dialogues, provided-tool evaluation, and missing-tool scenarios, going well beyond Metatool's single-setting design. MeCa-RAG separately tests adaptive retrieval. Each query underwent human verification. This is a useful community resource if released.

4. **Unified treatment of adaptive tool use and adaptive RAG.** The paper treats RAG as a special case of tool use and validates the same MeCo trigger on both, demonstrating generality.

5. **Demonstrated transferability of thresholds.** Thresholds fitted on Metatool transfer to MeCa-Tool (Task1 and Task4) with only minor degradation, indicating robustness to distribution shift between benchmarks.

## Weaknesses

### Fatal
None.

### Major

- **No comparison to existing adaptive tool-use or adaptive RAG methods.** The baselines are only Naive (first token) and $P_{\text{Yes}}$ (normalized softmax). A substantial literature addresses the same "when to use tools/retrieval" problem: Self-RAG (Asai et al., 2023), FLARE (Jiang et al., 2023), Corrective RAG (Yan et al., 2024), Toolformer (Schick et al., 2024), and various uncertainty/confidence-based triggers. None are compared. The paper overclaims in Section 3 ("our experimental results demonstrate this policy's superiority over existing methods") but provides no evidence against any actual existing method. The contribution would be better framed as a new approach with encouraging initial results against simple baselines, not as a demonstrated advance over the state of the art. Without these comparisons, the reader cannot gauge whether MeCo's improvements are meaningful relative to what the field already offers.

- **No statistical testing or confidence intervals.** Accuracy numbers are reported as point estimates without standard deviations, confidence intervals, or significance tests. Given that the improvements over $P_{\text{Yes}}$ are often a few percentage points (e.g., ~3–4 points in several conditions), these could fall within noise. The process of fitting thresholds on hold-out data is sensitive to sample size, making variance reporting essential.

### Minor

- **The decision strategy (two-threshold override) is under-specified.** The paper states that two thresholds $l_{\text{yes}}$ and $l_{\text{no}}$ are "found based on the validation data" and applied to test data, but the exact decision function is not described. Is the meta-cognition score compared to the corresponding threshold to decide whether to override the model's first token? If so, what is the override rule (e.g., if token is "Yes" but score < $l_{\text{yes}}$, flip to "No"?) These details are needed for reproducibility. The paper also does not specify how the thresholds are optimized (grid search? on what metric?).

- **The contrastive instruction pairs ($T_f^+$ / $T_f^-$) for the meta-cognition probe are not concretely specified.** The paper gives an example template ("USER: ⟨instruction⟩⟨experimental/reference prompt⟩ ASSISTANT: ⟨output⟩") but never states what the meta-cognition-specific experimental and reference prompts actually are. This makes it impossible for readers to reproduce the probe training. (Note: this does **not** mean the probe is a "Yes vs. No token classifier," as one reviewer claimed — the method follows standard RepE contrastive-instruction training on the target model's internal representations, which is principled; the issue is only that the prompts themselves are not disclosed.)

- **GPT-4-generated training data and benchmark could introduce systematic biases.** Both the probe training data (Yes/No + explanation responses) and the MeCa benchmark queries/labels are generated by GPT-4. While MeCa underwent human review, the probe training data did not (as far as stated), and the same model (GPT-4) used for generation could imprint its own biases about tool necessity into both the training labels and the evaluation. A control experiment — e.g., human-annotated probe training data or cross-generation with a different model — would strengthen the evidence chain. The probe is trained on the *target model's* internal representations (not GPT-4's), so this is not a fatal confound, but it is a concern.

- **The probe accuracy comparison (Figure 3) is not controlled for task difficulty.** The meta-cognition probe achieves near-100% accuracy while honesty/confidence probes peak at 70–80%. The paper interprets this as the meta-cognition signal being "stronger" or "near-optimal," but the tasks differ substantially (binary classification of tool-necessity labels vs. distinguishing true/false statements). Without controlling for label difficulty, this comparison mainly shows the meta-cognition task is easier, not that the probe is inherently better.

- **Missing ablations.** The paper uses the "Yes/No + Explanation" prompting strategy but provides no ablation showing how this choice affects MeCo vs. baselines relative to other prompting strategies (e.g., CoT, Yes/No without explanation). The choice of layer range (-5 to -2) is justified by "our experiments show" but no supporting data is displayed.

### Trivial

- The sentence "the model always responds with 'Yes' or 'No' as the first token" is an oversimplification — some responses could begin with tokens like "I" (e.g., "I think yes..."). This seems to be a design choice (prompting forces Yes/No first), which should be stated explicitly.

- The paper says "only a small number of queries and responses are enough to train a probe with good performance" but never gives the exact number, making it hard to assess the method's data efficiency.

## Nice-to-Haves

- **Ablation: train the probe on randomly shuffled labels** to verify the probe captures something beyond dataset artifacts.
- **Learning curve analysis** showing probe accuracy as a function of training set size.
- **Qualitative case studies** showing queries where MeCo overrides the model's first token and changes the decision, with the meta-cognition score and hidden state visualization.
- **Comparison of MeCo scores to token-level entropy or other confidence measures** to clarify whether MeCo captures something distinct from output probability.
- **Cross-model probe transfer** (e.g., apply a probe trained on Llama-3-8b to Mistral-7b) to test whether meta-cognition representations are model-agnostic.
- **Latency/throughput measurements** to support the efficiency motivation in the introduction.

## Removed Points

- **Criticism that "the method does not measure meta-cognition" and "the probe learns a direction that separates Yes tokens from No tokens."** — This is factually incorrect. The paper follows standard RepE methodology: representations are collected under *different instruction conditions* ($T_f^+$ vs. $T_f^-$) for the same content, not from different token types. The probe learns to distinguish "meta-cognition-on" vs. "meta-cognition-off" internal states. The critic fundamentally misread the methodology. (The *vagueness* about the exact contrastive prompts is a valid minor issue, which is retained above; the core accusation of the probe being a token classifier is removed.)

- **Generic/scope-creep criticisms (e.g., "the paper does not explain why meta-cognition would correspond to a linearly separable direction")** — This is what the RepE literature (Zou et al., 2023) already establishes for concepts like honesty and confidence; the paper is applying the same framework. The question is not within the paper's scope.

- **Complaints about missing appendix content, missing proofs, or formatting/style nitpicks** — These are known parser artifacts or not relevant to evaluation.

- **Several "Missing Parts" items (human evaluation of probe, t-SNE plots, etc.)** — These are desirable but not standard requirements for an empirical paper at this stage.

## Novel Insights

The reviews surface an important tension that the paper does not fully resolve: the probe demonstrably captures *some* task-relevant signal in representation space (it works empirically), but the evidence does not establish that this signal corresponds to "self-assessment" or "meta-cognition" in any cognitively meaningful sense, as distinct from a learned correlation between hidden states and the tool-necessity label distribution. The paper would benefit from a more measured framing: MeCo is a representation-space classifier that improves tool-use decisions, not a window into the model's self-awareness. The methodological novelty — applying RepE probes to the tool-use timing decision — stands on its own without needing to invoke a strong cognitive interpretation.

## Suggestions

1. **Add comparisons to at least 2–3 existing adaptive tool-use or adaptive RAG methods** (e.g., Self-RAG, FLARE, or a simple uncertainty-threshold baseline) to contextualize MeCo's performance against the literature.
2. **Fully specify the two-threshold decision function** in both the main text and the appendix, including how thresholds are optimized (grid search? metric?) and the exact override logic.
3. **Report confidence intervals or standard deviations** for all accuracy numbers (e.g., via bootstrap resampling or multiple runs).
4. **Provide the concrete contrastive instruction pairs** ($T_f^+$, $T_f^-$) used for meta-cognition probe training, either in the main text or appendix.
5. **Tone down the "meta-cognition as self-awareness" framing** unless additional experiments (e.g., showing the probe correlates with human judgments of model capability, or that it generalizes across fundamentally different tasks) are added. The paper's technical contribution is strong enough without overclaiming the cognitive interpretation.
6. **Include a learning curve** showing probe accuracy vs. number of training examples to substantiate the "small number" claim.

## Score and Decision

The paper addresses a practically important problem with a clean, novel approach. The main technical idea — using RepE probes for adaptive tool-use decisions — is sound, and the empirical results consistently show gains over the tested baselines. However, the evaluation is significantly weakened by the absence of comparisons to existing adaptive methods in the literature and by the lack of statistical rigor. These gaps prevent a confident assessment of the method's relative value. The paper would be substantially stronger after adding such comparisons and addressing the reproducibility issues.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>
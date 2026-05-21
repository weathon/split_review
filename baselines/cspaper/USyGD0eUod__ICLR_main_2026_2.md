---
job_id: 6d422f83-9fd2-49c1-a37d-b5b711fa92b5
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: USyGD0eUod.pdf
paper: Automated Interpretability Metrics Do Not Distinguish Trained and Random Transformers
main_score_norm: 0.8
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, specifically interpretability of learned representations, sparse coding/SAEs, and evaluation methodology for representation learning in language models.

## Minimum Quality
Pass ✅. The paper contains the core components expected for an empirical interpretability study, including abstract, introduction, related work, experimental setup/results, a methodological analysis via toy models, limitations, and conclusion; while I have several substantive concerns, they do not rise to the level of a desk reject.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden prompts, instructions to reviewers, or other signs of prompt injection/manipulative content in the provided paper text.

# Expected Review Outcome:
## Summary
This paper studies a basic but important sanity check for sparse autoencoder evaluation: whether common SAE quality metrics and automatic explanation pipelines can distinguish trained transformers from randomly initialized ones. Across several Pythia model sizes and randomization variants, the authors find that reconstruction metrics and auto-interpretability scores are often surprisingly similar between trained and random models, and they argue that aggregate metrics alone are therefore insufficient evidence that SAEs have recovered learned, computationally meaningful features. The paper further proposes token-distribution entropy as a simple proxy for feature “abstractness” and presents toy-model analyses aimed at explaining why random networks might still yield sparse, interpretable-looking structure.

## Strengths
1. The core empirical question is well chosen and genuinely important. The paper asks for a sanity check that should arguably be standard in this line of work, namely whether interpretability metrics can separate trained models from strong nulls. This is exactly the sort of uncomfortable question the field needs more of.

2. The main empirical result is clear and useful. In **Figure 1** on **Page 4**, the overlap between the trained model and the randomized variants on fuzzing AUROC for Pythia-6.9B is visually striking, while the control stays near chance. That figure does a good job of supporting the paper’s central claim that high aggregate AUROC is not, by itself, enough to attribute discovered features to learned computation.

3. The multi-metric comparison in **Figure 2** on **Pages 6–7** is a strong part of the paper. Looking across explained variance, cosine similarity, \(L^1\) norm, fuzzing AUROC, detection AUROC, CE-loss recovered, and token-distribution entropy gives a broader picture than a single cherry-picked metric. I especially appreciated that the paper does not oversell the result as “SAEs do not work,” but rather as “these common aggregate metrics are not sufficient.”

4. The use of multiple randomization schemes is a meaningful design strength. The distinction among “Step-0,” “re-randomized incl. embeddings,” “re-randomized excl. embeddings,” and the Gaussian-embedding control is not just cosmetic. It helps separate effects of learned embeddings from effects of the architecture and activation statistics.

5. The paper includes a negative control that behaves as expected, which increases confidence in the experimental setup. In **Figure 2**, the black control curves are consistently much worse on auto-interpretability and reconstruction-related metrics, suggesting that the pipeline is not completely degenerate.

6. The paper is generally careful in the wording of its claims. The conclusion on **Pages 9–10** is appropriately scoped: the authors do not claim that SAEs trained on real models fail to recover meaningful features, only that current aggregate metrics cannot by themselves establish this.

7. The token-distribution entropy idea, although preliminary, is a useful attempt to move beyond pure aggregate auto-interpretability. The last row of **Figure 2** provides at least some evidence that trained-model features change with depth in a way not mirrored by randomized variants.

8. The toy-model section is not definitive, but it is helpful for intuition. **Figure 3** offers a plausible visual story for why random networks may preserve or even accentuate superposed structure, and **Figure 4** helps ground the SAE recovery discussion by showing a regime where the method can recover known generating features.

9. The paper is reasonably reproducible. It specifies model family, training tokens, buffer size, SAE architecture choice, expansion factor \(R\), sparsity \(k\), sampled number of features, and the explainer model used for auto-interpretability.

10. Even the only explicit table, **Table 1** on **Page 41**, is useful in one respect: it makes the experimental scale transparent. While this is not a results table, it does indicate that the authors actually ran a fairly substantial sweep rather than a tiny proof-of-concept.

## Weaknesses
1. The central empirical claim is important, but the paper leans very heavily on visual similarity of curves without enough statistical treatment. For example, the main conclusions from **Figure 1** and **Figure 2** are mostly qualitative, based on overlapping lines and broad trends. Yet the paper samples only 100 latents per SAE for auto-interpretability on the main experiments (**Page 4**), and uncertainty is only shown for Pythia-70M in Appendix Figure 17. This matters because the paper’s headline claim is essentially about failure to distinguish conditions. “They look similar” is not the same as “the metric lacks discriminative power.” I would have liked confidence intervals or formal tests for trained vs randomized gaps, at least aggregated over layers or models, in the main paper.

2. The paper sometimes slides from “similar aggregate scores” to a broader methodological indictment without quantifying the actual separability. For instance, **Figure 2** on **Page 6** indeed shows similar trends, but in several settings the trained curve is not identical to the randomized ones, and the degree of overlap varies by model size and layer. A stronger analysis would measure, for a given metric, how well one could classify trained vs random SAEs from that metric alone, or report effect sizes across layers. Without such quantification, some of the rhetoric feels a bit sharper than the evidence strictly supports.

3. The proposed “abstractness” proxy is interesting but underdeveloped. On **Pages 5–7**, token-distribution entropy is introduced as a proxy for whether a latent is concentrated on a small number of token IDs. This is plausible, but also very limited. High entropy can arise from many unrelated phenomena and does not necessarily imply semantic abstraction; low entropy can still correspond to meaningful morphemes, names, or structured concepts. The paper does acknowledge that entropy is not a direct measure of abstractness, but then leans on it fairly heavily in the conclusion. This matters because a large part of the paper’s interpretation of trained-vs-random differences depends on this single proxy.

4. The qualitative evidence for “trained features are more abstract” is weaker in the main paper than the claim suggests. The text on **Page 5** refers the reader to appendices for example features, and the main paper itself contains no side-by-side qualitative figure or main-text dashboard illustrating the qualitative distinction. Given how central this claim is to the paper’s narrative, some compact main-paper qualitative comparison would have been valuable. Right now, the paper’s strongest evidence is still the entropy proxy, not direct demonstration of richer feature structure.

5. The toy-model section is somewhat disconnected from the main empirical result. In **Section 4**, especially around the argument on **Page 7**, the paper suggests that random networks preserve superposition, and **Figure 3** provides a visual example. However, the formal statement is quite loose, and the experiments in **Figures 4–5** are not tightly linked to the transformer results. The toy MLP setup uses synthetic sparse-feature generation and GloVe embeddings, which are useful for intuition, but do not establish that the same mechanism is what explains the Pythia findings. So the mechanistic story remains speculative.

6. There is a concrete mathematical exposition issue in **Section 4.1** on **Page 7**. The notation
\[
x \sim \mathcal{N}(x; Dz, \Sigma)
\]
and later
\[
x' \sim \mathcal{N}(z; WDz, W\Sigma W^\top)
\]
appears malformed. Presumably the authors mean either \(p(x\mid z)=\mathcal{N}(x;Dz,\Sigma)\) or \(x\mid z \sim \mathcal{N}(Dz,\Sigma)\), and similarly \(x'\mid z \sim \mathcal{N}(WDz, W\Sigma W^\top)\). As written, the second expression incorrectly places \(z\) in the observation slot. This is not a fatal flaw, but it is exactly the kind of mathematical sloppiness that makes the explanatory section harder to trust. Since Section 4 is meant to give a principled rationale for the empirical findings, the notation should be fixed and made precise.

7. The evaluation is narrowly scoped to one model family and one data regime. The experiments are all on Pythia models trained on RedPajama activations. That is a reasonable starting point, but the paper’s framing is broader, as if it were diagnosing “commonly used SAE metrics” in general. The result may well generalize, but the paper does not demonstrate this. This matters because SAE behavior is known to depend strongly on tokenization, architecture, layer type, training distribution, and SAE variant.

8. The paper does not sufficiently disentangle whether the issue lies in the explainer/simulator pipeline, the learned SAE latents, or the activation data itself. This is a crucial scientific distinction. If random models yield token-level or substring-level latents that are easy for the LLM explainer to describe, then the result may primarily reflect limits of automatic explanation scoring rather than a deeper failure of SAE feature extraction. The paper gestures in this direction, but the experiments do not isolate it. For example, a comparison against trivial baselines such as token-ID features, substring features, or simple lexical probes would help determine whether the scores are mostly driven by shallow lexical regularities.

9. The CE-loss recovered metric is acknowledged to only make sense for the trained model (**Page 5**), which is fair, but this also weakens the comparative picture. One of the few clearly behavior-grounded metrics in the paper is unavailable for the random variants because the randomized models themselves are behaviorally meaningless. That leaves the main comparison dominated by reconstruction and explanation metrics, which are exactly the metrics under dispute. In other words, the paper convincingly shows a problem, but has limited access to stronger external anchors for what a “good” feature should mean.

10. Despite the importance of the result, the presentation of quantitative evidence could be stronger. **Figure 2** is dense and informative, but it also bundles many claims into a single visual summary, with no companion numerical table. A tabulated summary of average metric values by model size and variant, or slopes across depth, would make the paper easier to audit. The absence of a main-paper results table is noticeable; **Table 1** on **Page 41** is only about compute cost, not empirical outcomes. For a paper built around cross-condition comparisons, this makes the evidence harder to inspect carefully than it should be.

11. Some of the interpretation around model size is speculative. On **Page 5**, the paper suggests AUROC increases with model size because features become more specific as SAE size increases. That might be true, but the claim is not directly tested. Since model size, hidden dimension, SAE width, and feature granularity all change together, the interpretation is underidentified.

12. The control design is useful but not a perfect null for all claims. Replacing token embeddings at inference time with fresh Gaussian noise for each occurrence creates a deliberately destructive control, and the control appropriately fails in **Figure 1** and **Figure 2**. But this is a very easy negative control. It shows that the pipeline can detect total destruction of token identity, not that it can separate learned computation from shallow architectural or embedding-driven structure. So the control helps, but it should not be overinterpreted as validating the metric.

13. The paper cites qualitative examples in the appendix that seem to show many random-model latents are essentially single-token or short-fragment detectors, which is plausible and important, but this also points to a missing main-paper baseline. If many high-scoring random latents reduce to near-token detectors, the paper should compare against simple token or n-gram features directly. Otherwise the reader is left thinking, “yes, but perhaps the metric is just rewarding token specificity,” which is exactly the point the paper should nail down more explicitly.

## Questions
1. Can the authors quantify the degree to which each metric distinguishes trained from randomized SAEs, beyond visual curve overlap? For example, if one computes an effect size or a classifier AUROC for predicting “trained vs randomized” from metric values across layers, does fuzzing AUROC actually collapse to chance, or merely degrade substantially? This would make the headline claim much sharper.

2. Please provide uncertainty estimates in the main paper, at least for the auto-interpretability metrics. Since only 100 latents are sampled per SAE, I would like to know how much of the apparent overlap in **Figures 1–2** survives bootstrap confidence intervals or repeated latent sampling.

3. How much of the result is specific to the explainer model and prompt pipeline? The paper uses Meta-Llama-3.1-70B-Instruct-AWQ-INT4 on **Page 4**. If the same latent set is scored with a materially different explainer/simulator, do the trained and randomized variants remain similarly hard to distinguish?

4. Can the authors include a simple baseline using hand-constructed lexical features, such as token-ID indicators, substring features, or frequency-based token clusters? This would help determine whether the high-scoring random-model features are doing anything more than rediscovering shallow lexical regularities that the explanation model can easily verbalize.

5. For the token-distribution entropy measure, can the authors report the exact definition more formally in the main text? As written on **Page 5**, the distribution is “the total latent activation per token across the set of maximally activating examples,” but it would help to specify whether activations are normalized over examples, whether repeated occurrences are summed, and whether entropy is computed over BPE token IDs or decoded strings. A compact formula would improve clarity, e.g.
\[
p(t)=\frac{\sum_{i\in \mathcal{E}} a_i \mathbf{1}\{\mathrm{tok}_i=t\}}{\sum_{i\in \mathcal{E}} a_i}, \qquad H=-\sum_t p(t)\log p(t).
\]

6. In **Section 4.1**, please correct and clarify the Gaussian notation. I believe the intended statements are
\[
x\mid z \sim \mathcal{N}(Dz,\Sigma), \qquad x' = Wx \Rightarrow x'\mid z \sim \mathcal{N}(WDz, W\Sigma W^\top).
\]
If that is correct, the current notation should be fixed, because the present form is confusing and slightly undermines confidence in the derivation.

7. The conclusion emphasizes that trained features become more abstract with depth, whereas random-model features do not. Can the authors surface one concise main-text qualitative comparison, ideally as a figure, showing matched latents from a late layer of trained and randomized Pythia-6.9B? Right now this claim is plausible, but too dependent on appendix inspection.

8. How sensitive are the results to the choice of layer subsampling in larger models? For Pythia-1B and 6.9B, SAEs are not trained at every layer. Could this bias the apparent depth trends in **Figure 2**?

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
None.

## Soundness Rating
3: good. The main experiments are competently executed and support the core cautionary claim, but the evidence is more qualitative than I would like, and the explanatory mechanism plus “abstractness” analysis remain somewhat preliminary.

## Presentation Rating
3: good. The paper is readable and the figures are informative, especially **Figures 1–2**, but some claims rely too much on visually inspecting dense plots, the main paper would benefit from tabulated summaries, and there is a nontrivial notation issue in **Section 4.1**.

## Contribution Rating
4: excellent. I do not think the paper fully closes the story, but it identifies an important failure mode in current SAE evaluation practice and makes a timely methodological contribution that the community should take seriously.

## Overall Rating
8: Accept, good paper (poster). This is a useful and well-executed negative result with clear relevance to the ICLR community. I have several substantive reservations, mainly about statistical quantification, scope, and the preliminary nature of the “abstractness” analysis, but the central message is important, supported by the presented experiments, and worth disseminating broadly.

## Reviewer Confidence
4: confident. I am confident in the assessment and familiar with the broader area; I checked the main empirical claims and the mathematical exposition in the paper carefully, though I did not independently verify appendix-level implementation details.
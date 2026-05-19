Now I have all the information needed. Let me produce the consolidated review.

## Summary

This paper investigates whether the hidden states of autoregressive LLMs—collected during the prefill phase—encode domain-specific information. The authors compute layer-wise statistics of hidden state activations, observe visual clustering by domain across multiple architectures (Gemma-2B, Phi-3-mini, Llama2-7B, Mistral-7B), and show that these representations remain stable across prompt variations and after fine-tuning. They then train an MLP classifier on raw hidden states to route queries to domain-specialized models, reporting that this approach outperforms both individual fine-tuned models and baselines such as semantic routing and a DeBERTa-based classifier. The paper's core direction is interesting and practically relevant.

## Strengths

- **Consistent domain separation demonstrated across multiple LLM architectures**: Figure 2 shows standard-deviation traces for Gemma-2B, Phi-3-mini, Llama2-7B, and Mistral-7B that visually cluster by domain (Maths, Biomedical, Law, Humanities), while the encoder model DeBERTa shows no comparable pattern (Section 5.1, lines 104–127). This is shown across both MMLU queries and held-out datasets from a different distribution (Specialized Pool), providing evidence that the phenomenon is architecture-general and not merely a reflection of query surface form.

- **Evidence of robustness to prompt perturbations and fine-tuning**: Section 5.2 demonstrates that deeper layers (16+) maintain stable traces across 12 different prompt templates for the Phi-3-mini model, and Section 5.1 states that fine-tuned versions of Phi-3-mini and Llama2-7B retain similar separation patterns (lines 128). This supports the claim that hidden-state domain representations are not merely artifacts of superficial textual features.

- **Quantitative improvement in model selection routing**: Table 2 shows that an MLP trained on hidden states consistently outperforms the best individual domain fine-tuned models on 5 held-out datasets. The improvements are especially notable on GSM8K (+4.3 points over Phi-3-MATHS), MEDMCQA (+12.1 points over Phi-3-MEDICAL), and MATH (+9.8 points). This provides concrete evidence that the hidden-state representations carry actionable information for routing.

- **Layer-reduction analysis yielding practical insight**: Figure 4 shows that routing performance increases sharply when all 32 layers are used versus layer subsets, with layer 26 identified as an inflection point. This provides practical guidance for the computational trade-off between latency and accuracy (Section 5.4).

## Weaknesses

### Fatal
None.

### Major

- **The headline "12.3% accuracy improvement" is not defined or verifiable from the presented data.** The paper states this figure in the abstract, contributions list (line 24), and discussion (line 202), but Table 2 reports per-dataset accuracy numbers and no computation in the paper shows how 12.3% is derived. The per-dataset absolute improvements in Table 2 range from +1.0 (MMLU) to +12.1 (MEDMCQA). Whether 12.3% is an average across some subset of tasks, a relative improvement, or something else is never explained. The paper's central quantitative claim cannot be evaluated as stated.

- **The MLP classifier's input representation is underspecified, undermining reproducibility.** Section 5.3 states the MLP is trained on "raw hidden state traces from 4,000 random samples" (line 159), but never explains how the hidden states (shape: batch_size × dim × num_layers) are converted into a fixed-size feature vector for the classifier. Are all layers concatenated? Is mean pooling applied over the sequence dimension? Is only the last token's hidden state used (as in Section 5.1, line 110)? Without this information, the experiment cannot be reproduced, and it is unclear what the MLP is actually learning from.

- **The source and training details of the domain fine-tuned models used for routing are not specified.** The paper says "three fine-tuned versions of Phi-3-mini-3.8B on the following subdomains: Emotional, Mathematical thinking and Medical Data" (line 154), but does not state whether these were obtained from HuggingFace, fine-tuned by the authors, or what their exact training data and procedures were. This makes the main baseline ("domain fine-tuned models") a moving target and weakens the comparison.

### Minor

- **The qualitative trajectory analysis (Figure 2) lacks quantitative measures of domain separability.** The paper describes visual clustering trends but provides no quantitative metric such as silhouette score, nearest-centroid classification accuracy, or between-class variance ratio for the layer-wise statistics. While the downstream MLP classifier provides indirect quantitative evidence, a direct measure of domain separability on the aggregated traces would strengthen the core claim.

- **The mapping of Law and Humanities to the pretrained (not fine-tuned) model is not justified.** The paper routes Law and Humanities queries to Phi-3-PRETRAINED (line 156) but provides no analysis of why the domain-specific fine-tuned models underperform on these domains. This choice is acknowledged implicitly (the results show improvement even over the pretrained model), but the rationale for this mapping decision is absent, and it affects the interpretation of the routing results.

- **The claim that interpretations apply to "open-ended generative tasks" is overstated.** The evaluation datasets are predominantly multiple-choice (MMLU subsets, MEDMCQA, CaseHOLD) or short-answer math reasoning (GSM8K, MATH) with a single verifiable answer. These are not "open-ended" in the sense of dialogue, summarization, or unrestricted generation. The paper should qualify this claim or demonstrate applicability to genuinely open-ended tasks.

- **The Semantic Layer baseline uses a default threshold (0.5) without any tuning or ablation** (line 92). A simple grid search over the similarity threshold would clarify whether the baseline's poor performance is inherent or a configuration artifact. Additionally, the DeBERTa classifier is trained on MMLU domain labels and evaluated on datasets from different distributions, introducing a distribution shift that is not discussed.

### Trivial

None.

## Nice-to-Haves

- Reporting confidence intervals or variance across multiple runs (or seeds) for the routing results in Table 2 would clarify whether the observed improvements are stable or within noise.
- Specifying the exact MLP architecture (number of layers, hidden dimensions, activation function, train/test split of the 4,000 samples) would improve reproducibility.
- A simple ablation controlling for query length, domain-specific keywords, or token-level features would strengthen the claim that hidden-state clustering reflects genuine domain understanding rather than surface cues.
- Evaluating domain classification accuracy directly (e.g., nearest-centroid on the aggregated trajectories) would directly link the qualitative analysis to the quantitative results.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Criticism that Figure 2's visual separation "could be driven by superficial properties such as token length"** — While reasonable as a general concern, the paper partially addresses this by showing that patterns persist across the Specialized Pool (non-MMLU datasets with different distributions) and across prompt variations. The criticism is speculative rather than a documented shortcoming in the presented analysis.

- **Criticism that "fine-tuning not changing traces (4 further explores) is referenced but the appendix is stripped, so we cannot evaluate"** — Per hard rules, criticisms relying on missing appendix content are to be removed. The paper states these results exist.

- **Criticism that "only one model shown in Figure 3"** — The paper explicitly states that results for other models are in Section 6 of the appendix (line 148). The appendix is stripped by the parser; the original submission contains this material.

- **Criticism about "lack of comparison to a simple sentence-embedding baseline" (using the LLM's own final-token embedding)** — The paper already compares against the Semantic Layer (sentence-transformers/all-MiniLM-L6-v2) and the DeBERTa classifier, which are both embedding-based alternatives. Requesting a specific additional baseline is a reasonable suggestion but not a weakness of the current evaluation.

- **Criticism that "the MLP classifier uses raw hidden states... the paper never clarifies this inconsistency" with the mean/variance aggregation used for trajectory plots** — The paper defines the trajectory analysis using aggregated statistics (Section 3) and separately uses "raw hidden state traces" for the MLP (Section 5.3). While the MLP featurization is underspecified (a separate Major weakness above), the paper is not internally contradictory: the trajectory analysis and the MLP are different uses of the hidden states serving different purposes (qualitative visualization vs. quantitative classification).

## Novel Insights

The harsh critic correctly identifies that the paper's most important experiment—the model selection routing (Table 2)—is not tightly connected to the qualitative trajectory analysis. The relative success of the hidden-state MLP over both generic sentence embeddings and a fine-tuned encoder classifier is the paper's strongest finding, but it remains unclear whether this success is due to the specific layer-wise structure of autoregressive hidden states or simply to using a higher-dimensional, more expressive representation. The layer-reduction experiment (Figure 4) partially addresses this by showing that all 32 layers are needed for best performance, but the paper does not ablate what specific property of these hidden states (e.g., the last-token hidden state alone vs. full sequence token averages) drives the improvement. An ablation comparing: (a) last-token hidden state only, (b) mean-pooled token hidden states, and (c) a shallow probe trained on the full hidden state sequence would disentangle whether the advantage comes from the _pattern across layers_ (the claimed "trajectory") or from the _richness of the final-layer representation_.

## Suggestions

1. **Clarify the 12.3% figure**: Show explicitly how this number is computed (which datasets, whether absolute or relative, and which baseline). If it cannot be straightforwardly derived from Table 2, add a footnote or computation.

2. **Specify the MLP input featurization**: Describe exactly how hidden states (tensor of shape batch×dim×layers) are flattened, pooled, or otherwise transformed into the feature vectors fed to the MLP. This is essential for reproducibility.

3. **Add quantitative domain-separability metrics**: Compute a simple metric (e.g., silhouette score, or nearest-centroid classification accuracy) on the layer-wise mean/variance trajectories to directly quantify the visual separation in Figure 2.

4. **Provide details for the domain fine-tuned models**: State whether these are public HuggingFace checkpoints (and which), or describe the fine-tuning procedure (data, hyperparameters, number of steps) if created by the authors.

5. **Disambiguate the dataset construction**: Clarify whether the 5,000 samples from the Base Pool and the 5,000 from the Specialized Pool are disjoint, and how they are balanced across domains.

## Score and Decision

The paper presents an interesting direction—using LLM hidden states during prefill for domain-aware model routing—and provides genuine evidence of domain-clustering patterns that generalize across architectures and resist prompt perturbations. The routing results in Table 2 show consistent improvements over strong individual fine-tuned models, suggesting practical value. However, the paper is significantly weakened by: (1) an undefined headline quantitative claim (12.3%) that cannot be verified from presented data, (2) an underspecified MLP input representation that prevents reproducibility of the central experiment, and (3) incomplete description of the domain fine-tuned models used as baselines. These issues do not invalidate the core contribution but prevent the paper from making a clean, convincing case in its current form. Major revisions addressing clarity and completeness are needed.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>
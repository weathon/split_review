Here is my synthesized final review:

---

## Summary

This paper investigates whether LLMs internally encode domain-specific information in their hidden states during the prefill phase. By computing per-layer mean and standard deviation of hidden state activations across four autoregressive LLMs (Gemma-2B, Phi-3-mini-3.8B, Llama2-7B, Mistral-7B), the authors show that these statistics cluster by domain (maths, biomedical, law, humanities) and are robust to prompt variation and fine-tuning. They then use this signal for model routing, training an MLP on hidden states to select among fine-tuned variants of Phi-3-mini, reporting improvements over domain fine-tuned baselines.

## Strengths

- **Consistent domain-specific clustering across four LLM architectures (Figure 2):** The standard-deviation traces separate by domain for Gemma, Phi-3, Llama2, and Mistral, but not for DeBERTa, showing the phenomenon is not model-specific and is tied to autoregressive computation rather than being a universal property of any transformer. This is the paper's core empirical finding and is clearly demonstrated.

- **Practical routing application outperforms semantic-layer and DeBERTa baselines (Table 2):** The MLP trained on hidden states achieves the best routing accuracy across both closed-ended (MEDMCQA, CaseHOLD) and open-ended (GSM8K, MATH) benchmarks, validating that the clustering signal has practical downstream utility.

- **Robustness to prompt variation and fine-tuning (Section 5.1–5.2, Figure 3):** The domain traces stabilize after layer 16 across multiple prompt templates and different datasets within the same domain, and fine-tuning does not erase the separation. This strengthens the claim that the traces reflect stable properties of the pretrained model rather than superficial prompt artifacts.

- **Extension to open-ended generative tasks:** Unlike prior probing work that focuses on closed-ended classification, the paper evaluates on GSM8K and MATH, showing the method works for free-form reasoning (Section 5.3).

## Weaknesses

### Major

- **The central interpretative claim that LLMs "capture domain-specific knowledge" is confounded with surface-level token statistics.** The paper shows that hidden-state aggregations cluster by domain, but different domains use very different vocabularies (e.g., "plaintiff" vs. "diagnosis" vs. "derivative"). A bag-of-words classifier on token embeddings alone might produce the same separation. The paper never controls for this — e.g., by comparing the hidden-state separation to that of mean-pooled token embeddings, by permuting domain-specific tokens within queries and checking whether clustering collapses, or by controlling for perplexity/query length.  

  *Mitigation in the paper:* The DeBERTa encoder (fine-tuned to predict domain labels from the same tokens) does not show clean clustering, and different datasets within the same domain cluster together. These observations suggest the signal is not *purely* lexical, but they are indirect. The paper would need a direct control (e.g., a linear probe on token-only features) to justify the stronger interpretation that the model captures "domain knowledge" rather than domain-correlated token statistics.  

  *Why this matters:* The paper's main novelty claim is that hidden states reveal the model *understanding* domain. If the separation is largely explainable by vocabulary, the contribution reduces to "per-layer std of LLM hidden states is a useful routing signal" — still interesting and potentially useful, but the interpretative framing overreaches.

- **The routing evaluation has an unexplained logical gap.** The baseline for each dataset is the single best fine-tuned model (e.g., Phi-3-MATHS for GSM8K). If the MLP router correctly routes GSM8K samples to the math model, accuracy should match that model's standalone performance (reported as 53.80). Yet the router achieves 65.18 on GSM8K. This means the router is sending some math queries *away from* the math model toward other fine-tuned variants (medical, emotional, pretrained) that happen to perform better on those specific samples. The paper acknowledges the result is "counterintuitive" and speculates about overfitting, but never analyzes *which* samples are being rerouted, *which* alternative model wins, or *why*. This is a significant gap in the evaluation: either the routing is doing something genuinely novel (identifying that domain labels are a poor proxy for model competence at the sample level) or there is an artifact in how the baseline was computed. Without per-sample analysis, the headline result is uninterpretable.

### Minor

- **No statistical testing or variance estimation.** The paper reports point estimates for routing accuracy across five datasets (Table 2) and for layer-reduction experiments (Figure 4) without confidence intervals, error bars, or multiple seeds. Given the modest test-set sizes, it is impossible to assess whether the reported improvements are reliable or within the noise of a single run.

- **The routing experiments use only one base model (Phi-3-mini-3.8B) and its fine-tuned variants.** The abstract claims findings are "consistent across multiple LLM architectures," but this applies only to the clustering analysis, not the routing method. The paper should explicitly scope the routing claim to Phi-3.

- **The paper does not discuss the striking and consistent ordering of variance across domains (Law highest std → Humanities → Biomedical → Maths lowest) visible in every subplot of Figure 2.** This pattern holds across all four architectures and is clearly data-dependent, but the paper only notes that "differences in behavior were tied to the inherent characteristics of the datasets" without exploring what drives this ordering (vocabulary diversity, token length, response entropy, etc.). This is a missed opportunity for insight.

### Trivial

- The term "latent domain-related trajectories" overstates what is being measured — per-layer mean and standard deviation, aggregated across batch and dimension. While the paper defines the term operationally (Section 3), the rhetoric ("trajectories," "latent") suggests something more structured than two scalar statistics per layer.

- The claimed "12.3% accuracy improvement" (abstract/contributions) appears as "12% improvement" in the Discussion (line 202). These should be consistent, and the paper should clarify whether this is absolute or relative improvement.

## Nice-to-Haves

- **Add a token-level control:** Compute separation from mean-pooled token embeddings (or a simple bag-of-words classifier) and show the hidden-state separation is significantly larger. This would directly address the central confound.
- **Analyze individual routing decisions:** For the GSM8K and MATH results where the router beats the domain-expert model, show which alternative model was selected and characterize those samples linguistically or by difficulty.
- **Add error bars** via bootstrapping over test samples or multiple MLP training seeds.
- **Report actual inference cost** (latency or FLOPs saved) for the layer-reduction experiments in Figure 4, not just accuracy.

## Removed Points

- *"The DeBERTa comparison is weak by design"* — REMOVED because this misunderstands the purpose: DeBERTa is used as a strong encoder baseline for domain classification, which is a standard and informative comparison. The paper's finding that DeBERTa hidden states don't cluster while autoregressive LLMs do is itself an interesting result, not a flaw.
- *"Cannot be independently verified" / reproducibility concerns about model availability* — REMOVED per policy: all cited models have public checkpoints; questioning their existence is not permitted.
- *Various formatting/typo/stylistic nitpicks* — REMOVED as parser artifacts.

## Novel Insights

Beyond the paper's own claims, the most striking observation is the consistent *ordering* of variance by domain (Law > Humanities > Biomedical > Maths) across all four architectures. This ordering is clearly data-driven rather than model-driven, but the paper treats it as a throwaway detail. If this ordering correlates with some property of the domains (e.g., vocabulary diversity, answer entropy, or response length variability), it would suggest that the hidden-state variance is encoding something about the *uncertainty* or *distributional complexity* of the domain, not just domain identity. This is a potentially richer finding than the paper extracts.

## Suggestions

1. **Disentangle domain from vocabulary.** Add a baseline control that compares the hidden-state clustering against a simple classifier on token embeddings only (e.g., mean-pooled BERT or even TF-IDF). If the hidden-state separation is meaningfully stronger, the interpretation is much better supported.
2. **Analyze the counterintuitive routing results.** For the datasets where the router beats the domain-expert fine-tuned model, provide a confusion matrix or sample-level analysis showing where samples are being rerouted and to which alternative model. This could reveal that the router is doing something genuinely smart (e.g., detecting that some math problems are better solved by the general pretrained model) or that there is a confound in the baseline.
3. **Scope the generalizability claims precisely.** Clarify in the abstract and contributions that the multi-architecture consistency applies to the clustering finding, while the routing application is demonstrated on Phi-3-mini only.
4. **Add error bars or multiple-seed runs** for the key quantitative results in Table 2 and Figure 4.
5. **Discuss the variance ordering across domains.** Even a brief correlation analysis (e.g., with token length, vocabulary size, or perplexity) would add interpretability.

## Score and Decision

**Originality:** The core observation (hidden-state statistics cluster by domain) builds on established probing methods but extends them to generative LLMs and open-ended tasks, and the routing application is a novel use of this signal. The work is moderately original.  
**Importance of research question:** Understanding how LLMs internally distinguish domains is relevant to both interpretability and practical deployment (routing, model selection). The question is worthwhile.  
**Claims support:** The central interpretative claim is not fully supported due to the token-statistics confound, and the routing evaluation has an unexplained gap. The empirical observations are credible but the stronger interpretation overreaches.  
**Soundness of experiments:** The clustering analysis is well-executed across multiple architectures and datasets. The routing experiment is less rigorous: no statistical testing, no per-sample analysis, and a single model.  
**Clarity of writing:** The paper is generally clear, though the rhetoric sometimes overstates the findings.  
**Value to community:** The empirical finding that LLM hidden states cluster by domain and can be used for routing is likely useful to researchers working on LLM interpretability and efficient deployment. However, the value is constrained by the unresolved confounds and unexplained routing results.

**Overall:** The paper presents an interesting empirical finding with a potentially useful application, but the central interpretation is not adequately justified and the routing evaluation has a logical gap that makes the headline result hard to interpret. These issues are addressable with additional controls and analysis. The contribution is promising but not yet conclusive.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>
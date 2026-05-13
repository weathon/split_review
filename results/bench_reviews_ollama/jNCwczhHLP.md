Now I have a thorough understanding of the paper. Let me synthesize the final review.

## Summary

The paper introduces SLLM4CTR, a framework that improves LLM-based click-through rate (CTR) prediction through two plug-and-play components: (1) an adaptive temperature derived from batch-normalized cosine similarity between prompt embeddings and click embeddings, which modulates both training loss gradients and inference probabilities; and (2) a label matching loss based on determinant-based volume compaction of click/non-click representation spaces. The paper motivates the method through diagnostic analyses showing that fine-tuned LLMs exhibit sparse feature attribution and poor performance on tail items compared to traditional CTR models.

## Strengths

- **Clear problem identification with diagnostic evidence**: The paper identifies two concrete symptoms of LLM underperformance in CTR tasks—sparse feature attribution (Figure 2) and poor tail-item performance (Table 1, Figure 1)—providing a structured motivation rather than just proposing a method in search of a problem.
- **Novel adaptive temperature mechanism**: The design of using batch-normalized cosine similarity between prompt and click embeddings as a temperature that modulates gradients (Theorem 2) and inference probabilities is a genuinely creative approach. It connects feature-prediction alignment directly to confidence-weighted learning, and the paper explicitly discusses both training and inference effects (Section 4.1, line 129).
- **Consistent empirical improvements across datasets and backbones**: SLLM4CTR outperforms baselines on all three datasets (Table 2, Table 3) and generalizes to Llama-2-7B, Llama-3-8B, and other LLM-based CTR backbones like TallRec and ClickPrompt (Figure 4d), suggesting the method targets a general LLM limitation rather than a backbone artifact.
- **Lightweight design**: The method introduces no additional learnable parameters and adds minimal computational overhead (Figure 4c), and the label matching loss avoids explicit negative sampling—a practical advantage for sparse CTR data.

## Weaknesses

### Fatal
None.

### Major

- **Inference procedure for adaptive temperature is underspecified**: The temperature $T$ is defined as a softmax over the training batch $\mathbb{B}$ (Eq 2). The paper explicitly states the temperature "modulates the behavior of the LLM during both training and testing phases" and that "during testing, the temperature results in a lower click probability for less correlated samples" (Section 4.1). However, the paper never specifies how the batch $\mathbb{B}$ is constituted at inference time. If a single item is scored, the softmax denominator reduces to one term and $T$ becomes constant; if an arbitrary batch is used, the temperature scale is not calibrated. This is not merely an implementation detail—it is a fundamental ambiguity about how the claimed inference-time confidence calibration works, and the method as described is not fully deployable without this specification.

- **Cross-architecture attribution comparison has validity concerns, and the improvement on the diagnosed metric is marginal**: The primary motivation (Figure 2) compares integrated gradient attribution scores between LLMs and traditional CTR models (DeepFM, DCN, etc.). These architectures produce representations on fundamentally different scales through different mechanisms (one-hot categorical embeddings with explicit crossing vs. token embeddings with attention), making direct attribution comparison questionable. More critically, the paper's own data shows SLLM4CTR improves positive-attribution feature counts from 1→2, 4→4, and 1→3 across the three datasets (Figure 2 caption). The 4→4 result shows no improvement at all, and 1→2 and 1→3 are marginal gains. This undermines the claim that the method effectively addresses the diagnosed "limited feature utilization" problem.

- **Causal link from adaptive temperature to "increased feature utilization" is unsupported**: The paper claims that the adaptive temperature "encourages LLMs to focus on more features" (Section 4.1) because low-T samples get smaller gradients (Theorem 2). However, smaller gradients on low-confidence samples means the model learns *less* from those samples—the logical connection from "reduced gradients" to "increased feature attention" is not established. An equally plausible interpretation is that the method simply down-weights hard examples (a well-known curriculum/loss-weighting strategy), and the performance gains come from improved optimization rather than enhanced feature utilization. The paper provides no analysis of how attention patterns change with vs. without adaptive temperature, which would be the direct test of this claim.

### Minor

- **Ablation study incomplete across datasets**: Figure 4a presents the ablation study only on Book-Crossing. Given that the method contains two components whose contributions may vary by dataset, showing ablations on all three datasets would strengthen confidence that both components consistently contribute.

- **Notation inconsistency between $e_L$ and $e_{click}$**: The adaptive temperature formula (Eq 2) uses $e_L$ (the last token hidden state from Section 2.1), while the surrounding text refers to "click embedding" $e_{click}$. Section 2.1 defines $e_L$ as the last hidden state and separately discusses the head-layer projection vectors $w_{Yes}$ and $w_{No}$. Whether $e_L$ and $e_{click}$ refer to the same quantity or different quantities is never clarified, which could confuse readers attempting to implement the method.

- **The ablation variant labels "w/o Label Matching Loss-1" and "w/o Label Matching Loss-2" are referenced in Section 5.1 but never explained**, making it unclear what these two removal variants represent.

### Trivial
None.

## Nice-to-Haves

- Comparison against standard regularization baselines (dropout variations, weight decay, contrastive losses without volume compaction) to disentangle the label matching loss's "feature-to-click matching" effect from generic regularization benefits.
- Analysis of per-sample temperature distributions during training to verify the mechanism produces meaningful variation rather than near-constant values.
- Tracing how attribution scores change during training with SLLM4CTR (not just before/after) to strengthen the causal link between the mechanism and improved feature utilization.

## Removed Points

- "Theorem 3's volume derivation is not novel, just a standard result from random matrix theory / representation learning" — While the log-determinant volume bound is indeed related to classical results (e.g.,Determinantal Point Processliterature and representation learning volume preservation), the paper applies it in a specific novel context (compacting click/non-click representation spaces with probability-weighted volumes). Claiming the result itself is novel would be overreaching, but the *application* to this specific formulation is new. This critique would better be phrased as requesting proper acknowledgment of prior connections, which is a minor presentation issue.

- "The paper claims 'significant' improvements but AUC gains over ClickPrompt are only 0.005–0.01" — The paper itself cites (Mao et al., 2023) noting that "0.001 AUC performance improvement can be seen as significant" (Table 2 caption), consistent with CTR community standards. These gains are in fact considered meaningful in this domain.

- "The head/tail comparison ignores that traditional CTR models use learned ID embeddings capturing collaborative filtering signals unavailable to text-only LLMs" — The paper actually includes user ID and item ID in prompts (Section 2.2), and the comparison is between simply fine-tuned LLM and the proposed SLLM4CTR, not just LLM vs. traditional. The tail performance gap between SLLM4CTR and traditional baselines is indeed a valid observation, but the paper discusses this as a motivation for the method, not as a claim that LLMs should match traditional models on tails.

- "Zero vector baseline for IG on transformers with tied embeddings may introduce artifacts" — Using a zero vector as the integrated gradients baseline is a standard choice (Sundararajan et al., 2017), and while not perfect for transformers, this is an accepted practice and does not invalidate the relative comparisons within the paper.

- Reproducibility concerns about unspecified inference behavior for T — this is kept as a major weakness above (it's a methodological gap, not a reproducibility nitpick), but pure reproducibility complaints about unspecified hyperparameters are removed.

- Missing related works — removed per hard rules (cannot verify external references).

- Formatting/notation nitpicks — removed per hard rules.

## Novel Insights

The paper makes an interesting observation that batch-normalized cosine similarity between prompt and click representations can serve as a proxy for "confidence in feature utilization," creating a self-monitoring mechanism that requires no additional parameters. However, the strength of this insight is diminished by the fact that the causal story connecting smaller gradients for low-T samples to *increased* feature attention is asserted rather than demonstrated—existing theory and the paper's own Theorem 2 suggest the mechanism acts as a loss-weighting scheme that down-weights uncertain samples, which is a well-understood optimization technique repackaged as a "feature utilization" mechanism.

## Suggestions

- Explicitly define how the adaptive temperature $T$ is computed at inference time, and ablate different strategies (e.g., batch-of-candidates for a given user, fixed temperature, exponential moving average over training batches).
- Provide attribution analysis (Figure 2 equivalent) for SLLM4CTR across *all three* datasets, noting the marginal improvement case (4→4 features with positive attribution on Book-Crossing). Either explain why this is acceptable or acknowledge that the attribution mechanism doesn't always improve as claimed.
- To validate the "increased feature utilization" claim, analyze how attention patterns or attribution scores change during training, rather than comparing only before vs. after.

## Score and Decision

The paper identifies a real problem in LLM-based CTR prediction and proposes a creative and lightweight method with consistent empirical improvements. However, the inference procedure for the core mechanism (adaptive temperature) is undefined, the diagnostic framework motivating the entire method has validity issues and shows only marginal improvement on its own metric, and the causal link between the proposed mechanisms and the claimed improvements is asserted rather than demonstrated. These are significant gaps that the authors should address.

Originality: The adaptive temperature and volume-based label matching loss are creative contributions, though both connect to well-known ideas (loss weighting and representation compaction).  
Importance: CTR prediction with LLMs is a practically important problem.  
Claims support: Empirical improvements are consistent but the diagnostic and causal claims are insufficiently supported.  
Experiments: Adequate across datasets and backbones, but ablations limited to one dataset.  
Clarity: Generally good, with some notation inconsistencies.  
Community value: The diagnostic analysis and method could stimulate further work if the gaps are addressed.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>
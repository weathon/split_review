Now I have a thorough understanding of the paper and all reviewer claims. Let me write the consolidated review.

## Summary

This paper proposes **Self-Inject (MSI)**, a method for extending the context window of short-context LLMs by pairing two copies of the same checkpoint—a "lower" (compressor) and "upper" (decoder) model—connected via cross-attention limited to shallow layers. Compressed multi-grained context is stored in a binary tree structure supporting query-dependent retrieval. The method is evaluated on language modeling (perplexity up to 128K) and long-context understanding benchmarks (InfiniBench, LongBench), with reported efficiency gains of 2–3× over streaming and encoder-decoder baselines.

## Strengths

- **Self-injection architecture eliminates the need for hidden-space alignment pretraining.** Both submodules are initialized from the *same* off-the-shelf short-context LLM checkpoint, removing the separate alignment stages required by heterogeneous encoder–decoder approaches (e.g., CEPE's RoBERTa pretraining+warmup). The paper states this explicitly (§1, §4.2) and the payoff is visible in Table 2 where MSI outperforms CEPE on 4/4 dataset×length combinations despite CEPE's extra training stages.

- **Query-dependent context tree enables efficient multi-grained compression with strong retrieval accuracy.** The binary-tree structure stores coarse-to-fine representations, and the query-aware policy (cosine similarity) selects relevant branches for expansion. The ablation study (§4.4) confirms that removing the query-aware retrieval causes the largest performance drop on MD-QA (44.2→41.5), demonstrating its critical role.

- **Significant efficiency gains: 2× over streaming, 3× over encoder-decoder baselines while maintaining low memory.** Section 4.3 reports that MSI runs 2× faster than Activation Beacon and 3× faster than CEPE under the same 128K evaluation, and is the only method (besides the streaming baseline) that avoids OOM on a single A800 80GB GPU at 128K. YaRN fails at 128K. This stems from shallow-layer cross-attention and fully parallelized chunk encoding.

- **Strong extrapolation from 8K training to 128K evaluation without perplexity explosion.** Trained on only 8K-token sequences, MSI maintains stable perplexity up to 128K, outperforming all baselines on most settings (e.g., 3–10% lower perplexity than the best competitor on ArXiv, PG19, ProofPile, CodeParrot in the mixed dataset setting).

- **Top-tier results on long-context understanding benchmarks.** On InfiniBench's Math.Find, MSI surpasses the previous SOTA by 2.44 points (21.9% relative improvement); on En.MC by 1.34 points (4.1%). On LongBench, it outperforms or matches all baselines across all five categories.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Training data comparison clarity (RedPajama setting).** The paper excludes book3 from the RedPajama training data due to copyright and does not renormalize sampling probabilities (§4.1). It acknowledges that "perplexity without book3 gets a bit worse" (§4.2). What remains unclear is whether the baseline results in Table 1 (RedPajama setting) were obtained by retraining those models on the *identical* book3-excluded data, or whether numbers were carried from prior publications that included book3. The paper should state this explicitly. If baselines included book3 and MSI did not, the comparison is biased *against* MSI—but the direction and magnitude of the bias across different domains is not fully predictable. This does not affect the Mixed dataset results (Table 2) or the InfiniBench/LongBench results.

- **Inference-time overhead of tree construction and search not separately reported.** The method requires, for each chunk and each query token, a depth-first search that computes cosine similarities between hidden states via short forward passes through one self-attention layer (§3.2). The efficiency comparison (§4.3) reports end-to-end speed, which conflates tree-building and search costs with generation. While the end-to-end metric is practically meaningful, reporting the overhead separately (e.g., tree construction time as a fraction of total inference time for varying input lengths) would strengthen the efficiency analysis and clarify whether the tree search becomes a bottleneck at very long inputs.

- **Choice of M (number of injection layers) not justified.** M=4 is used for language modeling and M=16 for SFT (§4.1). The paper does not explain this asymmetry or provide an ablation showing whether these values are near-optimal or driven by memory/capacity constraints. Similarly, the decision to train only the top N−M self-attention layers (while cross-attention is fully tunable, §4.1) is claimed to yield "faster convergence" but is not supported by an ablation comparing it to full tuning or LoRA.

- **FlashAttention compatibility not stated.** The paper notes that Activation Beacon is incompatible with FlashAttention (§4.3), which contributes to its slower speed. However, the paper does not state whether MSI itself uses FlashAttention. If MSI does, the speed comparison should note this; if it does not, the efficiency claims are even stronger. This should be clarified.

- **Hyperparameter σ (splitting noise) not reported.** The random splitting noise magnitude σ is mentioned as a predefined hyperparameter (§3.2) but its value is not given, making reproduction harder. This is a minor reproducibility gap.

### Trivial

- **Figure 5 (efficiency) is referenced but the extracted text lacks its content.** This is a parser artifact; the figure exists in the original submission.

## Nice-to-Haves

- **Ablation on chunk size.** The paper ablates tree depth, compression ratio, injection layer strategy, and the three design components, but does not ablate chunk size, which may interact with tree depth and compression ratio.

- **Analysis of cross-attention key-length budget.** For β=8 and chunk size 1024 with 128 chunks, the cross-attention key sequence is 16K tokens. Reporting whether this causes memory spikes or requires attention to the key-length scaling would be useful.

- **Exploration of alternative compression ratio schedules.** The ratio α_w = 2α_{w+1} is used without exploring other decay schedules.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"Self-injection overstates novelty; weight tying is known."** The paper explicitly acknowledges the architecture "resembles general encoder-decoder architecture like T5" (Figure 1 caption, §3.1). The novelty is specifically about using the *same checkpoint* to initialize both submodules, which avoids alignment pretraining—a clear practical benefit, not an overstated claim.

- **"Omitted efficiency figure prevents verifying claims."** The text says "The results are visualized in Figure 5" (§4.3). The figure exists in the original submission; its absence here is a parser extraction artifact.

- **"Similarity-based retrieval details are missing (which layer, token-level vs. pooled)."** The paper specifies: "The hidden vector h at the last position of a sequence is embedded by either the lower or upper model. Specifically, this involves a short forward pass through one self-attention layer in the lower model for h_{x_φ} and the upper model for h_y" (§3.2). Both questions are explicitly answered.

- **"Missing related works."** Hard rule: do not mention missing related works without external confirmation.

- **"The book3 data issue is a fatal evidential flaw."** The paper is transparent about the exclusion, acknowledges its effect, and the direction of bias (if any) is against the proposed method. This is a clarity concern, not a fatal flaw.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Clarify baseline retraining status.** In §4.1 or §4.2, explicitly state whether all baseline results in Table 1 (RedPajama setting) were obtained by retraining the baselines on the identical book3-excluded data, or whether some numbers are taken from prior papers that included book3.
2. **Break down inference time** by component (tree construction/search vs. generation) for at least one representative input length to demonstrate that the tree search is not a scalability bottleneck.
3. **Report σ value** and ablate the choice of M (injection layers) for both LM and SFT settings.

## Score and Decision

The paper presents a well-designed method that combines several sensible ideas—shallow cross-attention with same-checkpoint initialization, tree-structured multi-grained compression, and query-aware retrieval—into a coherent system. The empirical results on language modeling and long-context benchmarks are promising, and the ablations convincingly validate most design choices. The main concerns (data comparison clarity, overhead breakdown, and a few missing hyperparameter details) are addressable and do not undermine the core contribution. The paper demonstrates genuine novelty in its self-injection architecture and delivers strong results across multiple evaluation settings.

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>
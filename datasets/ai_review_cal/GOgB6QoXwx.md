- Decision: Reject
- Avg Score: 5.25
- Scores: 6, 5, 5, 5
Now I have a thorough understanding of the paper and can evaluate the reviewers' claims against the actual content. Let me produce the final consolidated review.

## Summary

This paper presents LDMol, a latent diffusion model for text-conditioned molecule generation. The key innovation is constructing the latent space via contrastive learning using SMILES enumeration (multiple valid SMILES strings for the same molecule) to embed structural invariance, rather than relying on naive reconstruction-based autoencoders. The model achieves state-of-the-art results on the ChEBI-20 benchmark (BLEU 0.926, exact match 0.530, FCD 0.20) and demonstrates versatility on molecule-to-text retrieval and text-guided molecule editing without task-specific fine-tuning.

## Strengths

1. **State-of-the-art text-to-molecule generation results**: Table 1 shows LDMol outperforming all baselines across nearly every metric, including autoregressive models like bioT5+ and MolT5_large. The improvement is particularly notable on metrics that capture structural similarity: MACCS FTS (0.973 vs. 0.907), RDK FTS (0.950 vs. 0.835), Morgan FTS (0.931 vs. 0.779), and FCD (0.20 vs. 0.35). This directly supports the paper's central claim that a well-designed latent space enables diffusion models to surpass autoregressive models in text-conditioned molecule generation.

2. **Contrastive learning with SMILES enumeration yields structurally invariant latent space**: Figure 22 provides clean empirical evidence that the proposed encoder produces much smaller intra-molecule feature distances (~1.0) than inter-molecule distances (~15.0), while a β-VAE baseline shows nearly identical distances for both. This directly validates the core methodological claim that the encoder captures molecular structure beyond surface-level SMILES representation.

3. **Systematic ablation studies validate each design component**: Table 3 cleanly isolates the contribution of each architectural choice: removing contrastive learning collapses validity from 0.941 to 0.019; removing the compression layer drops validity to 0.022; omitting stereoisomer hard negatives reduces reconstruction accuracy from 0.983 to 0.891. This disciplined ablation gives confidence that each component is doing real work.

4. **Versatile downstream applications without retraining**: The paper demonstrates that the learned score function supports molecule-to-text retrieval (78.4% sentence-level accuracy on MoMu) and text-guided molecule editing (outperforming MoleculeSTM in 5/8 scenarios), both without task-specific fine-tuning. This versatility is a genuine strength of the diffusion modeling framework.

5. **Clear motivation for the latent space design**: The paper articulates why molecular latent spaces require different properties than image latent spaces (Section 3.1): SMILES tokens carry dense, interdependent information unlike relatively independent image pixels. This motivates the contrastive learning strategy rather than naive reconstruction.

## Weaknesses

### Fatal
None.

### Major

1. **Lack of explicit statement about SMILES canonicalization in evaluation**: The paper does not state whether canonical SMILES are used in training or evaluation. This matters because BLEU and Levenshtein distance are computed on SMILES strings — a correct molecule generated in a different valid SMILES form would be penalized. While the fingerprint metrics (MACCS, RDK, Morgan FTS) and FCD are structure-based and unaffected by SMILES ordering, the exact match ratio (0.530) is also string-based. The paper reports 98.3% reconstruction accuracy for the autoencoder, suggesting the decoder faithfully reproduces the input SMILES format, but the omission of an explicit canonicalization statement is a transparency gap that should be addressed to fully trust the headline numbers. This is a Major weakness (important to clarify) but not a fatal one — the multiple structure-invariant metrics (fingerprint similarities, FCD) already provide strong evidence that the model generates genuinely correct structures, not just matching strings.

2. **Retrieval method description is underspecified**: The retrieval procedure (scoring candidates by computing the diffusion loss between noisy latent and text condition) is described very briefly (lines 233-234). The paper does not provide an algorithmic description of how the scoring function is computed, nor does it discuss the substantial computational cost of running multiple forward passes of the diffusion model per candidate (n=10 or n=25). Without a controlled comparison using encoder embeddings directly (without the diffusion scoring), it is unclear how much of the retrieval improvement comes from the encoder vs. the scoring procedure. This makes it difficult to fairly compare LDMol's retrieval results to baseline methods that use standard embedding similarity.

### Minor

1. **No variance reporting for generation experiments**: The paper reports single-point metrics in Table 1 without variance across multiple sampling runs or training seeds. While this is common practice in the field, the claim about outperforming strong baselines would be strengthened by reporting standard deviations, especially given the paper's own observation that the output has stochasticity from random initial noise.

2. **Slightly overstated claim about natural language generation**: The abstract states results "suggesting a potential for diffusion models can outperform autoregressive models in text data generation," and the introduction says the approach "suggests the possibility of improving existing diffusion models for natural language." SMILES is a formal grammar with a canonical string per molecule — fundamentally different from natural language where multiple valid surface forms express the same meaning. The paper hedges with "potential" and "suggests the possibility," but this connection is sufficiently tenuous that it should be tempered or removed.

3. **Missing hyperparameter details for the diffusion model**: The paper mentions using DiT architecture and DDIM sampling with 100 steps and classifier-free guidance scale ω=2, but does not report DiT depth/width, number of diffusion timesteps T, noise schedule, or other architectural hyperparameters. This hurts reproducibility.

4. **ChEBI-20 test set size not reported**: The paper does not state how many test examples the benchmark metrics are computed over. While ChEBI-20 is a known dataset (3,300 test pairs in the original paper), this information should be provided for self-containedness.

### Trivial

- The sentence "we note that since our diffusion model sampling starts from randomly sampled noise from a prior distribution, the output from deterministic DDIM sampling still has stochasticity" (line 186) is slightly imprecise: DDIM is deterministic given the initial noise, but the overall process is stochastic because the initial noise is randomly sampled each run. The intended meaning is clear but the phrasing could be tightened.

## Nice-to-Haves

- A controlled comparison of diffusion-based retrieval vs. using encoder embeddings directly for retrieval, to isolate the contribution of the diffusion scoring function.
- Reporting wall-time or FLOPs for the retrieval procedure to contextualize the computational cost.
- Including the "naive AE + KL regularization" variant in the main Table 1 to give a clearer picture of where the contrastive learning provides genuine advantage over a straightforward continuous latent space.
- A discussion of failure cases or text conditions where LDMol struggles, beyond the brief mention of complex biological properties.

## Removed Points

These points from the inputs are flagged to be removed — treat them with caution:

- **"MolT5_large may not have been evaluated under exactly the same conditions"** (from Harsh Critic): This is speculative with no evidence from the paper. The paper cites original sources for baseline numbers. Removed as unsubstantiated.
- **"Why not use a symmetric encoder-decoder architecture?"** (from Harsh Critic): This is a design curiosity, not a genuine weakness. Using a standard autoregressive decoder for sequential SMILES generation is a well-motivated choice.
- **"DDIM is deterministic; the paper's statement is confusing"** (from Harsh Critic): The paper's point is that different random initial noise gives different outputs, making the overall process stochastic. The critic's framing reflects a misreading — the paper is not claiming DDIM itself is stochastic.
- **"Code or model weights are not promised"** (from Harsh Critic): Removed per meta-instructions — reproducibility concerns about code release are not required for paper acceptance.
- **Strengths that conflict with verified weaknesses or are generic/superficial**: Several strengths from the Strength Finder are retained as they are specific and evidence-grounded. Generic framing about "addressing an important problem" is absorbed into the summary rather than listed separately.

## Novel Insights

None beyond the paper's own contributions. The two reviews reinforce the paper's core narrative: the method is well-motivated and the results are strong, but the evaluation transparency (particularly around SMILES canonicalization) needs clarification. No reviewer raised an insight about the paper that goes beyond what the authors themselves articulate.

## Suggestions

1. **Explicitly state canonicalization policy**: Clarify whether canonical SMILES are used in training data and whether both generated and ground-truth SMILES are canonicalized before computing BLEU, Levenshtein, and exact match. If canonicalization was used, simply state this. If not, re-run with canonicalization and report the results.
2. **Provide an algorithmic description of the retrieval scoring function**: Include pseudo-code or a clear step-by-step description of how the diffusion loss is computed for each candidate, and how n iterations are aggregated.
3. **Report variance**: Report standard deviation over at least 3 different random seeds or sampling runs for the main generation metrics.
4. **Add DiT architectural details**: Report the depth, width, number of heads, and other hyperparameters of the DiT model.
5. **Temper the natural language claim**: Replace the language about "text data generation" and "natural language" with a more precise statement about formal grammar/string generation, or remove the implication entirely.
6. **Include dataset size**: Report the number of test examples in ChEBI-20 in the text or table caption.

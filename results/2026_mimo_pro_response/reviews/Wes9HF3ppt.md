Now I have enough data to finalize. Let me write the complete review.

## Summary

This paper introduces Insertion Language Models (ILMs), a new sequence generation paradigm where the model learns to insert tokens at arbitrary positions by jointly predicting both the insertion position and the vocabulary element. ILMs combine advantages of autoregressive models (sequential generation, variable-length support) and masked diffusion models (out-of-order generation, infilling) while avoiding their key limitations. The paper demonstrates strong results on synthetic planning tasks, competitive text generation, and flexible infilling.

## Strengths

- **Dramatic advantage on planning tasks with variable-length dependencies (Table 1)**: ILM achieves 100.0% and 99.1% exact match on Star_medium and Star_hard, while ARM drops to 75.0%/23.0% and MDM to 36.5%/21.0%. The paper provides a clear mechanistic explanation (Section 5.1.1): MDMs fail because absolute position prediction with variable arm lengths is "intuitively equivalent to solving the puzzle itself in a single pass," while ILMs use relative positions and iterative insertion. These results convincingly demonstrate a qualitative capability that neither competing paradigm possesses.

- **Well-designed approximate denoising objective (Section 3, Eq. 2)**: The paper identifies that the naive trajectory-marginalization objective has extremely high variance and proposes the target insertion distribution as a biased but low-variance alternative. The training procedure (Algorithm 1) requires only one extra CPU-side computation step compared to MDM training, making it practical.

- **Native infilling capability (Table 3)**: ILM outperforms MDM across all infilling evaluation sets. This is a structural advantage since ILMs insert tokens one at a time and learn a stopping classifier, naturally supporting variable-length infilling — something MDMs cannot handle when the number of tokens to fill is unknown in advance (the "conference" example from the Introduction).

- **Competitive text generation (Table 2, Figure 5)**: ILM achieves NLL of 2.14 (vs. ARM 2.11) on Stories and 4.67 (vs. ARM 3.94) on LM1B. The Prometheus LLM judge evaluation shows ILM outperforming MDM on coherence and consistency, with performance similar to ARM on the longer Stories dataset.

- **Principled experimental design**: All models use ~85M non-embedding trainable parameters, the same RoPE-based transformer backbone, same training steps, batch size, and learning rate (Section 5.3). The paper also includes the original Insertion Transformer as a baseline (Table 1, IT row), demonstrating that the dedicated stopping classifier substantially outperforms the EOS-based approach.

- **Efficiency advantage over MDMs (Figure 6)**: ILM achieves better NLL than MDM at comparable or lower per-token generation time, and MDM quality plateaus even with more sampling steps.

## Weaknesses

### Fatal

None.

### Major

- **Training-inference mismatch from the biased training objective**: The training objective (Eq. 2) predicts insertion distributions for all gaps simultaneously — effectively teaching the model to fill in all blanks at once from a single forward pass. At inference time (Algorithm 2), the model inserts one token at a time sequentially, conditioned on the current partial sequence. The paper acknowledges this is a biased approximation of the true sequential denoising objective (which has infeasible variance, per Appendix D), but provides no analysis of when this bias is benign: no ablation comparing against the unbiased objective, no theoretical justification for why the biased objective yields a good sequential policy, and no empirical analysis of how inference trajectories relate to what training implies. Since the core contribution — making ILMs trainable — hinges on this approximation, this gap weakens confidence in the method. This is a major rather than fatal weakness because the empirical results demonstrate the method works in practice; the issue is that the *why* is not analyzed.

- **Systematic under-generation confounds NLL-based text evaluation (Table 2)**: ILM generates dramatically shorter sequences than ground truth and ARMs: on Stories, ILM averages 119 tokens vs. ARM's 201 and ground truth's 205; on LM1B, 21 vs. ARM's 30 and ground truth's 28. Since NLL is computed per-token, shorter sequences tend to be simpler and more generic, which can lower per-token NLL regardless of actual generation quality. ILM's lower entropy (3.76 vs. dataset's 4.19 on Stories; 2.80 vs. 3.08 on LM1B) further suggests less diverse output. The paper acknowledges low entropy but does not address how the length mismatch affects comparability of NLL across models. The Prometheus LLM judge (Figure 5) partially compensates, but NLL remains the primary quantitative comparison.

### Minor

- **Unexplained LM1B gap with ARMs**: On Stories, ILM NLL (2.14) is essentially tied with ARM (2.11). On LM1B, the gap is 19% relative (4.67 vs. 3.94). The paper attributes the overall gap to "training token efficiency and scaling laws" (Section 5.3.1) without investigating why the two datasets produce such different outcomes. Potential explanations (different padding lengths: 128 vs. 1024, different training steps: 1M vs. 60K, different dataset characteristics) are not analyzed.

- **Undefined notation α_Duo in Table 3**: This notation appears in the infilling results table without definition in the main text. Presumably defined in the appendix (which is stripped in this version), but its presence without explanation in the main text creates confusion.

## Nice-to-Haves

- Analysis of stopping classifier behavior (e.g., stopping probability as a function of position) to clarify whether under-generation is fundamental or a tuning issue.
- Length-controlled evaluation: force all models to generate at the same length or evaluate NLL at matched lengths to disentangle quality from length effects.
- Training curves or downstream performance vs. training steps to substantiate the training efficiency claim.
- Discussion of computational scaling (quadratic cost in sequence length, cost of computing insertion distributions during training).

## Removed Points

These points are flagged to be removed, treat them with caution.
- None removed.

## Novel Insights

The paper's central novel insight is that insertion-based generation occupies a unique niche between ARMs and MDMs: by jointly predicting position and token, ILMs handle variable-length sequences with arbitrary ordering without MDMs' fixed-length constraint or ARMs' left-to-right constraint. The star graph experiments provide particularly clear evidence — the explanation that MDMs fail on variable arm lengths because absolute position prediction reduces to solving the entire puzzle is genuinely insightful and well-validated by the data. The zebra puzzle results (ILM: 90% vs. ARM oracle-order: 91.2%) further demonstrate that ILMs approach oracle ARM performance without needing oracle ordering, a result with practical implications for constraint satisfaction tasks.

## Suggestions

- Add an empirical study of the biased training objective's impact, even on a toy task, to validate the approximation.
- Control for sequence length when comparing NLL across models (e.g., truncate all outputs to a common length).
- Define α_Duo in the main text or add a footnote to Table 3.
- Analyze the stopping classifier to address systematic under-generation.

## Calibration Report

### Anchor Papers Retrieved

| Paper | Avg Human Score | Round | Comparison |
|-------|----------------|-------|------------|
| Scaling up Masked Diffusion Models on Text | 6.50 | R1 | Very relevant — MDM scaling paper, accepted. ILM is more novel but has weaker text evaluation. |
| Discrete Diffusion Language Modeling (SEDD) | 6.60 | R1 | Very relevant — discrete diffusion for language, rejected. SEDD has stronger theoretical contribution (score entropy) but less empirical breadth. |
| Steering Masked Discrete Diffusion Models (DDPP) | 6.25 | R1 | Relevant — steering MDMs. Accepted with lower score due to narrow focus. |
| Interpolating Autoregressive and Discrete Denoising Diffusion (SAD3-LM) | 8.00 | R1 | Most relevant — interpolates AR and diffusion. SOTA results on standard benchmarks, stronger evaluation, accepted unanimously at 8. ILM has comparable novelty but weaker text results. |
| Deterministic Diffusion for Sequential Tasks | 4.50 | R1 | Somewhat relevant — diffusion for sequential tasks, rejected. Limited novelty and weak baselines. ILM is substantially more novel and better evaluated. |
| Integrating Planning into Single-Turn Long-Form Text Generation | 4.75 | R2 | Somewhat relevant — planning + generation. Rejected. ILM is more technically sound. |
| ET-Plan-Bench | 4.50 | R2 | Somewhat relevant — planning benchmarks. Rejected. ILM is more novel. |
| Large Trajectory Models are Scalable Motion Predictors | 5.00 | R1 | Somewhat relevant — trajectory generation. Rejected. Decent work with unclear novelty. |

### Round 1 Bracket: 6.0–7.0

The ILM paper clearly exceeds the reject-tier papers (scores 3.0–5.0) in novelty, experimental rigor, and contribution clarity. The planning task results are exceptionally strong and represent a genuine qualitative advance over both ARMs and MDMs. However, the paper falls short of the 8.00 SAD3-LM paper, which achieves SOTA results on standard language modeling benchmarks, provides tighter theoretical analysis, and has a more complete evaluation. The text generation results for ILM are competitive but not SOTA, and the two major weaknesses (training-inference mismatch, under-generation confounding evaluation) prevent the paper from reaching the 7+ range.

Within the 6.0–7.0 range, the paper is most comparable to the MDM scaling paper (6.50) and SEDD (6.60). ILM is more novel than the MDM scaling paper (which primarily establishes scaling laws for existing methods) but has a weaker text evaluation than SEDD (which matches GPT-2 performance). The planning task results are a unique differentiator that neither of these papers has. Final score: 6.5.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: Accept
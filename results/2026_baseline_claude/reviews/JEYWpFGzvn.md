Now I have read the entire paper. Let me write the review.

---

## Summary

INFOTok is an adaptive discrete video tokenizer grounded in Shannon's information theory. The paper proves that existing fixed-rate tokenizers and data-agnostic adaptive approaches (like ElasticTok's uniform random masking) are provably suboptimal in expected token length. It then proposes an ELBO-based router that allocates tokens proportionally to a video's information complexity, paired with a transformer-based adaptive compressor that retains the most informative tokens. Empirically, INFOTok outperforms ElasticTok by a 2.3× compression factor at equivalent quality and reduces inference NFEs by 11×.

---

## Strengths

- **Rigorous theoretical grounding.** Theorem 2.2 formally shows that training with a data-agnostic uniform router leads to an expected token length that can be arbitrarily larger than optimal (by any multiplicative factor κ > 1) for sufficiently complex, imbalanced distributions. Theorem 3.1 proves near-optimality of the ELBO-based router under a reasonable approximation assumption. Together these constitute a principled, testable critique of ElasticTok-style methods.

- **Large, consistent empirical gains.** Table 1 shows FVD reductions of 40–60% and LPIPS reductions of 25–40% over ElasticTok at the same average BPP_{16} on both TokenBench and DAVIS, and Figure 4 shows the improvement holds across the full BPP_{16} range. The gains are not marginal.

- **11× inference efficiency improvement.** INFOTok requires exactly one additional decoder pass to compute ELBO, versus ElasticTok's binary search over 4096-token blocks (log₂(4096)−1 = 11 NFEs). This is a practical win for deployment, not just a benchmark artifact.

- **ELBO-based routing closely matches oracle.** Table 2 demonstrates that the ELBO router performs within noise of an exhaustive optimal search at every tested BPP_{16} level (e.g., PSNR 29.86 vs. 29.92 on TokenBench at 0.81), validating the theoretical claim empirically without cherry-picking.

- **Architecture-agnostic adaptive mechanism.** Table 3 (Right) shows that replacing the uniform masking in ElasticTok with the ELBO adaptive mechanism consistently improves PSNR and FVD whether applied to the Cosmos backbone or a pure ViT backbone, demonstrating genuine transferability of the core idea.

- **INFOTok-Flex unifies multiple compression rates into a single model.** Training with a mixture of β values yields a model that at inference matches per-β specialized models (Figure 4), providing practical flexibility without quality cost.

---

## Weaknesses

### Fatal
None.

### Major

1. **No downstream evaluation.** The paper is explicit about this limitation. However, for a video tokenizer the central downstream application is video generation (and secondarily, video understanding). Without at least one generation experiment—even at small scale—it is unknown whether ELBO-based token selection creates any distribution mismatch that harms autoregressive or diffusion decoders trained on the resulting token sequences. "Simple" scenes tend to receive fewer tokens; if a generator trains with this skewed distribution it may generalize differently than one trained on fixed-length sequences. The reconstruction proxy (PSNR/FVD) is necessary but not sufficient evidence for utility in practice. The authors acknowledge this, but the gap remains.

2. **The ELBO approximation drops the KL term in practice.** Section 3.1 states that "using the reconstruction error itself (without the KL term)…is sufficient, as the KL term is approximately proportional to the reconstruction error." This is a non-trivial simplification: the KL term in a discrete VQVAE/FSQ setting is not generally proportional to the reconstruction error, and removing it breaks the formal connection to log-likelihood that Theorem 3.1 relies on. The claim is justified empirically only indirectly (Table 2), but no ablation isolates the effect of including vs. excluding the KL term, leaving a gap between theory and implementation.

### Minor

1. **Restricted evaluation resolution.** All main results are for 256×256 video only, cropped to square. The paper notes multi-resolution generalization in an appendix, but the primary evidence base is narrow. It is unclear whether the ELBO signal remains well-calibrated at higher or non-square resolutions.

2. **"50% token savings" in Section 1 vs. the tables.** The introduction states "approximately 50% tokens without loss of reconstruction quality compared to state-of-the-art fixed-length tokenizers." The best support for this in the main body is INFOTok at BPP_{16}=0.56 achieving PSNR 29.27 vs. Cosmos-DV at 1.00 achieving 30.01—a 44% BPP reduction with a 0.74 dB PSNR gap, not identical quality. The 20% claim in the abstract is better supported (Table 1 vs. Cosmos-DV at equal quality). These two numerical claims are in tension and the larger claim should be stated with more precision.

3. **Mask overhead accounting.** The paper states the binary mask m ∈ {0,1}^N adds "approximately 5% overhead." This figure varies with N_x and codebook size C, and the calculation is not spelled out. For small compression rates where N_x « N_max the overhead could be significantly larger than 5%.

### Trivial

- BPP_{16} (bits per 16 pixels) is a non-standard metric unit; a brief calibration to standard BPP would help readers compare against non-paper numbers.

---

## Nice-to-Haves

- An ablation isolating the effect of the KL term in the ELBO router vs. using reconstruction error alone would close the theory-practice gap.
- A small-scale downstream generation experiment (e.g., class-conditional generation on UCF-101) would substantially strengthen the paper's claims.
- Analysis of how router variance (i.e., the spread of N_x values across videos) relates to video domain/category could be an illuminating qualitative result.

---

## Novel Insights

The paper's genuinely novel insight is that the standard training practice of sampling token length uniformly over {1,…,N} creates a training objective with no incentive to reduce expected token length—leading to a bias that is unbounded in theory. This observation is sharpened into a theorem (2.2) and then corrected by a specific fix: use ELBO as a complexity proxy for length selection. The secondary insight—that the same per-token ELBO values used for length selection can also be reused to decide *which* tokens to keep within the adaptive compressor—is elegant and practically zero-cost, since the ELBO forward pass has already been run. Together these insights convert an intuitive heuristic idea (adaptive tokenization) into a principled, information-theoretically grounded algorithm.

---

## Suggestions

- Run even a small-scale video generation experiment to validate that adaptive tokens from INFOTok are usable by a downstream model.
- Add an ablation comparing the ELBO router (full, with KL) against the reconstruction-error-only approximation actually used.
- Report the variance/distribution of N_x across videos within each dataset to illustrate how much the adaptivity activates on typical content.
- Clarify the mask overhead calculation with an explicit formula showing its dependence on N_x, N_max, and codebook size.

---

## Score and Decision

INFOTok presents a clean, theoretically grounded solution to a real problem in video tokenization. The core theoretical contribution—proving unbounded suboptimality of uniform routing and near-optimality of ELBO routing—is rigorous. The empirical gains over ElasticTok are large and consistent. The primary gap is the absence of downstream evaluation, and the theory-practice discrepancy from dropping the KL term deserves an ablation. Despite these gaps, the paper advances the field both theoretically and empirically.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>
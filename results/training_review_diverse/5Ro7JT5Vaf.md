## Summary

This paper presents TSGM, the first score-based generative model (SGM) framework for universal time-series synthesis that handles both regular and irregular time-series within a single architecture. The core methodological contribution is Theorem 3.1, which derives an autoregressive denoising score matching loss that adapts SGMs to sequential dependencies by conditioning on history via a pre-trained RNN-based autoencoder. The method is evaluated across 16 settings (4 datasets × 1 regular + 3 irregular missing rates) against 9 baselines, achieving state-of-the-art discriminative and predictive scores.

## Strengths

- **First SGM framework for universal time-series generation (regular + irregular).** The paper is the first to propose a score-based generative model that handles both regular and irregular time-series with minimal architectural changes (RNN for regular, Neural CDE/GRU-ODE for irregular). This is a genuine novelty supported by a clear problem formulation (Section 3.1) and empirical evaluation across 16 settings. The universality claim is well-motivated and delivered.

- **Principled theoretical derivation of an autoregressive denoising score matching loss.** Theorem 3.1 formally shows that the intractable score matching loss conditioned on history can be replaced by a tractable denoising score matching loss conditioned on the full current sequence without changing the optimal parameters. This is a non-trivial adaptation of the standard denoising score matching result (Vincent, 2011) to the sequential setting and is essential for connecting SGMs to autoregressive time-series generation.

- **Strong and consistent empirical results.** Table 2 shows TSGM (especially subVP) achieves the best discriminative and predictive scores on most datasets by large margins. For example, on the Stock dataset under the regular setting, TSGM-subVP achieves a discriminative score of 4.1 vs. the next best (GT-GAN) at 14.7. The results are consistent across regular and irregular settings (30%, 50%, 70% missing rates), and the sensitivity study (Table 3) shows stable performance across model depths and sampling steps.

- **Comprehensive and fair benchmarking.** The evaluation covers 9 baselines spanning VAE, GAN, flow, and other paradigms. Baselines that natively lack irregular-data support are adapted via GRU-D replacement, and all methods are evaluated under the same protocol across 16 settings. The evaluation metrics (discriminative and predictive scores) follow the established protocol from Yoon et al. (2019) and Jeon et al. (2022).

- **Interpretable visual evidence.** KDE plots (Figure 1) and t-SNE plots (Figure 3) visually confirm that TSGM-generated samples closely match the original data distribution, while baseline methods exhibit mode collapse or distributional shift. These plots provide intuitive support for the diversity and fidelity claims.

## Weaknesses

### Fatal

None.

### Major

- **Training-inference mismatch in the autoregressive generation pipeline is not addressed.** The conditional score network $M_\theta(s, \mathbf{h}_n^s, \mathbf{h}_{n-1}^0)$ is trained using ground-truth $\mathbf{h}_{n-1}^0$ from the encoder applied to real data. During generation (Section 3.4), however, $\mathbf{h}_{n-1}^0$ is itself a generated sample from the reverse diffusion process, which will differ from the training-time distribution due to autoencoder reconstruction error and accumulated drift. This is a well-known issue in autoregressive generative models (teacher forcing vs. free-running), and the paper neither discusses it, analyzes its impact, nor proposes any mitigation (e.g., scheduled sampling, noise injection during training). While this does not invalidate the method — many sequential models face this same gap and work well in practice — leaving it completely unaddressed weakens the claim that the loss derivation directly yields a correct generation procedure.

- **The autoencoder's role and its effect on generation quality are not characterized.** The generation pipeline depends critically on the pre-trained autoencoder: the score network operates on latent representations, and the final output is a decoding of sampled latents. Yet the paper reports **no reconstruction error** for the autoencoder, provides **no analysis** of whether the latent space is well-suited for diffusion, and includes **no ablation** that separates the SGM's contribution from the autoencoder's. A simple baseline — sampling $\mathbf{h}_n$ from a Gaussian prior and decoding directly, bypassing the score network — would isolate the score network's value. Without this, it is difficult to determine whether the claimed SOTA results come from the score network's capability or from a well-tuned autoencoder. The fact that baselines like TimeGAN and GT-GAN also use autoencoders makes the comparison fair at a relative level, but the paper's claim that the SGM is responsible for the quality leap is insufficiently supported.

### Minor

- **The medal aggregation in Table 1 is subjective and loses information.** Counting "medals" (best/2nd-best across metrics) discards effect size information. A model that loses narrowly on one metric but wins decisively on another is not well represented by a medal count. The full scores in Table 2 mitigate this somewhat, but the medal table as a summary presentation is not ideal.

- **The quality of adapted baselines for irregular settings is not verified.** Baselines that do not natively support irregular data have their RNN encoder replaced with GRU-D (Section 4.1.1). This is a reasonable adaptation, but the paper does not report whether the adapted baselines achieve reconstruction quality comparable to their original forms. If the GRU-D adaptation degrades baseline performance, the comparison may be unfair.

### Trivial

None.

## Nice-to-Haves

- A discussion contrasting the proposed autoregressive SGM approach with diffusion-based sequential generation methods in other domains (e.g., video, audio) and explaining why those methods do not directly apply to the time-series setting would strengthen the positioning.
- Variance estimates (mean ± std) for all evaluation scores would be useful. *Note: The paper states on line 240 that it reports mean and standard deviation from 10 runs, and the Strength Finder's citation of specific numbers like "4.1 (±0.0)" confirms that the table (embedded as an image in the PDF) does include standard deviations. The critic's concern about missing std devs is a parser artifact, not a paper deficiency.*
- A reconstruction error table for the autoencoder on each dataset would help disentangle the source of performance.

## Removed Points

- **Missing standard deviations in reported results.** *Removed because the paper explicitly states (line 240) that it reports mean and standard deviation from 10 runs. The table is embedded as an image in the PDF; the text parser cannot extract values from images. The Strength Finder cites specific numbers with ± notation (e.g., "4.1 (±0.0)"), confirming std devs are present. This criticism is based on a parser artifact, not an actual paper deficiency.*
- **The "first SGM" claim is not sufficiently justified by contrasting with other domains.** *Removed as a weakness. It is a strength, and the suggestion to add contrasts is moved to Nice-to-Haves.*

## Novel Insights

None beyond the paper's own contributions. The reviews largely converge on the paper's core claims rather than revealing unexpected angles.

## Suggestions

1. **Report autoencoder reconstruction error** for each dataset and include a baseline that samples $\mathbf{h}_n$ from a Gaussian prior and decodes through the autoencoder without the score network. This would isolate the SGM's contribution and substantially strengthen the evaluation.
2. **Address the training-inference mismatch** by either (a) adding noise to $\mathbf{h}_{n-1}^0$ during training to simulate the generation condition, (b) empirically measuring the distribution shift of $\mathbf{h}_{n-1}^0$ between training and sampling, or (c) at minimum, discussing this as a known limitation with justification for why it is acceptable in practice.
3. **Verify the quality of adapted baselines** by reporting whether the GRU-D adaptation achieves reconstruction fidelity comparable to the original RNN encoder.
4. **Replace or supplement the medal table** (Table 1) with a more informative summary that preserves effect sizes, or de-emphasize it in favor of the full score tables.

## Score and Decision

The paper proposes a technically coherent and genuinely novel adaptation of score-based generative models to time-series generation, with a solid theoretical derivation (Theorem 3.1) and strong empirical results across a comprehensive evaluation suite. The two major weaknesses — the unaddressed training-inference mismatch and the uncharacterized autoencoder contribution — are significant evaluation gaps but do not invalidate the core contribution. They are addressable in revision.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>
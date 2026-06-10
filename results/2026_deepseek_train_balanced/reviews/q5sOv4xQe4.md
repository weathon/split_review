## Summary

HART introduces a hybrid autoregressive framework for image generation that decomposes continuous image latents into *discrete tokens* (capturing overall structure, modeled by a scalable-resolution AR transformer) and *continuous residual tokens* (capturing fine details, modeled by a lightweight 37M-parameter diffusion module requiring only 8 sampling steps). This hybrid tokenizer bridges the reconstruction quality gap between discrete AR tokenizers and continuous diffusion tokenizers, achieving a reconstruction FID of 0.30 at 1024×1024 (vs. 2.11 for discrete-only VAR), which directly yields a 31% generation FID improvement while maintaining 4.5–7.7× higher throughput than diffusion models.

## Strengths

- **Hybrid tokenization reduces reconstruction FID from 2.11 to 0.30 on MJHQ-30K at 1024×1024, matching the SDXL tokenizer** (Section 5.2, Table 1). This 7× improvement directly addresses the paper's core motivation — discrete tokenizer quality limits AR generation — and means HART's generation upper bound is now comparable to diffusion models.

- **Residual diffusion requires only 8 sampling steps vs. MAR's 30–50 steps** (Section 3.2), a 4–6× reduction in diffusion overhead. Figure 6 further shows HART achieves a higher inception score with 3 diffusion steps than MAR achieves with 60 — a 20× runtime reduction for the continuous-token component. This is a concrete architectural advantage over the closest hybrid approach (MAR), not a generic claim.

- **4.5–7.7× higher throughput and 6.9–13.4× lower MACs than diffusion models at 1024×1024** (Section 5.2, Table 3), benchmarked on A100 with open-source models using recommended settings. HART achieves 3.1× lower latency than SDXL, 3.6× faster than PixArt-Σ, and 9.3× higher throughput than SD3-medium at 512px.

- **31% generation FID improvement over VAR at 1024px (7.85→5.38) on MJHQ-30K** (abstract, Section 4.3). The improvement is largest at 1024px, where the VAR discrete tokenizer's reconstruction fails most severely (rFID 2.11), directly tying the quality gain to the hybrid tokenizer design.

- **Alternating training strategy for the hybrid tokenizer is validated by ablation** (Section 4.3, Figure 6). Using separate decoders for continuous and discrete latents achieves similar continuous rFID but significantly worsens generation FID — a non-obvious design insight that the paper identifies and supports with evidence.

- **Token subsampling (discarding 80% of tokens during training) yields 1.4–1.9× training speedup** (Section 3.3) with claimed no degradation. This is a concrete engineering contribution reducing the practical cost of high-resolution training.

- **Scalable-resolution AR transformer using relative position embeddings enables direct 1024px generation without super-resolution** (Section 3.2, Figure 7), validated by faster convergence when finetuning from low-resolution checkpoints — a practical necessity given that doubling resolution quadruples the token count.

## Weaknesses

### Fatal
None.

### Major

- **Text-to-image generation results depend on proprietary training data.** The paper trains text-to-image models on "internal MidJourney-style synthetic data" (Section 4.1, line 113) that is not publicly available. This creates a confound between architectural contribution and data quality: an independent researcher cannot verify whether the observed quality gains come from HART's hybrid design or from training on higher-quality synthetic data than what is used for the diffusion baselines. The ImageNet class-conditioned experiments (trained on fully public data) provide cleaner evidence of the method's inherent value, but the headline text-to-image claims (MJHQ-30K FID, GenEval, DPG-Bench) rest on data that cannot be inspected or reproduced. The authors should either (a) report text-to-image results trained on fully public data alongside the proprietary-data results, or (b) elevate the ImageNet experiments as the primary evidence and position the text-to-image results as a scalability demonstration.

### Minor

- **Imprecise claim about prior AR work at 1024px.** The paper states "no existing AR model can directly and efficiently generate 1024×1024 images" (line 26), but later acknowledges that concurrent work Lumina-Next "achieves high quality 1024px image generation through AR modeling" (line 45) while characterizing it as using one-token-per-step prediction (line 81). The intended meaning — no AR model does both *directly* and *efficiently* — is correct, but the phrasing can be read as claiming no AR model can generate 1024px at all. The authors should sharpen this framing to avoid misleading readers.

- **80% token subsampling claim lacks quantitative support.** Section 3.3 (line 97) asserts that discarding 80% of tokens "does not result in performance degradation" but provides no ablation table or figure showing FID or other metrics across different subsampling rates. Given the aggressiveness of 80% subsampling, this claim needs empirical backing.

- **No quantitative comparison with DART.** DART (cited as concurrent work in Related Work, line 48) is the most closely related hybrid AR+diffusion approach, yet no quantitative or qualitative comparison is provided. While this is partially excused by concurrent timing, the paper's core claim of architectural advantage would be strengthened by establishing where HART's specific design (discrete tokens + residual diffusion) differs from DART's approach (autoregressive diffusion steps) and whether it empirically outperforms it.

### Trivial
None.

## Nice-to-Haves

- A limitations/discussion paragraph covering common failure modes of AR models (repetitive patterns, object coherence over long sequences, handling of rare prompts) would strengthen the conclusion.
- A brief discussion comparing HART's design choices to VQ-Diffusion (which applies diffusion in the *opposite* direction — on discrete latents) would help position the work within the broader hybrid modeling landscape.
- Reporting variance or confidence intervals for FID/IS/CLIP scores would further strengthen reproducibility, though single-run evaluation is the norm in this field.

## Removed Points

These points were removed during consolidation with brief justification:

1. **"Claim contradicts own Lumina-Next citation"** — The paper does not actually contradict itself; lines 26, 45, and 81 are consistent. Lumina-Next achieves 1024px generation (acknowledged), but using one-token-per-step prediction (inefficient). The phrasing is imprecise, not contradictory. Kept as a minor framing issue above.

2. **"No VQ-Diffusion discussion"** — The paper already mentions VQ-Diffusion in Related Work (line 47). Moving deeper positioning discussion to Nice-to-Haves.

3. **"No statistical significance / variance reporting"** — Single-run FID/IS evaluation without confidence intervals is standard practice in this field. Not a real weakness.

4. **"Efficiency numbers for baselines need more documentation"** — The paper specifies open-source models with recommended settings on A100 hardware (line 113). This level of documentation is adequate for a conference publication.

5. **"Scalable-resolution transformer implementation details too sparse"** — The paper specifies 2D rotary embeddings with citations and describes the conversion from absolute to relative PEs (lines 79-81). These are standard techniques specified at an appropriate level of detail.

## Novel Insights

The review process surfaces one insight not fully articulated in the paper: HART's design effectively exploits an asymmetry in the difficulty of learning structure vs. details. Discrete VQ tokens excel at capturing categorical/structural information (object shape, layout, semantics) but are poor at fine-grained texture and high-frequency details; continuous diffusion excels at the latter but is computationally expensive when applied to the full latent. By decomposing the latent along this *difficulty boundary* — assigning structure to cheap AR and fine details to a tiny diffusion MLP — HART achieves a Pareto improvement over both approaches. The key design insight validated by the ablation (Figure 6) is that the decoder must be trained to accept both discrete and continuous inputs (alternating training), or generative quality collapses even when reconstruction quality is maintained. This observation — that reconstruction quality alone is an insufficient proxy for generative quality in hybrid tokenizers — is practically important for future work.

## Suggestions

- **Primary actionable fix:** Train a text-to-image variant on fully public data (e.g., JourneyDB + LAION subsets) and report those results alongside the proprietary-data results. This would eliminate the confound and make the core architectural claims independently verifiable.
- Correct the imprecise framing in line 26 to something like "no existing AR model can both directly generate 1024×1024 images *and* do so efficiently enough to compete with diffusion models."
- Add an ablation table for the token subsampling rate showing FID at different subsampling percentages (e.g., 0%, 50%, 80%, 90%) to substantiate the claim of no performance degradation.
- Add a discussion or comparison table positioning HART relative to DART, even if the comparison is limited to architectural analysis or efficiency estimates.

## Score and Decision

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>
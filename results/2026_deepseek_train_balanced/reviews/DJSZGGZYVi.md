## Summary

This paper proposes REPA (REPresentation Alignment), a regularization that aligns the hidden states of diffusion transformers (DiT, SiT) with clean-image representations from a pretrained self-supervised encoder (DINOv2). The core idea is that learning good internal representations is a bottleneck in diffusion training, and providing external high-quality representations via a simple patch-wise similarity loss dramatically accelerates convergence and improves generation quality. On ImageNet 256×256, REPA-SiT-XL/2 reaches FID=7.9 in 400K iterations (no CFG), matching the vanilla SiT-XL/2 trained for 7M iterations — a ~17.5× iteration speedup — while also achieving competitive FIDs with classifier-free guidance.

## Strengths

- **Quantitative characterization of the representation bottleneck**: The paper does not merely assert that diffusion representations are weak — it measures them via linear probing accuracy and CKNNA (a kernel alignment metric), showing concretely that SiT/DiT representations lag behind DINOv2 (Figure \ref{subfig:sit_lin_eval}) and that alignment with DINOv2 is weak compared to other SSL methods (Figure \ref{subfig:sit_cknna_dino}), but improves with model size and training length (Figure \ref{subfig:sit_cknna_progression}). This provides a testable, falsifiable premise.

- **Dramatic and explicitly quantified training speedup**: The paper reports that REPA-SiT-XL/2 reaches FID=7.9 (no CFG) in 400K iterations, "exceed[ing] the FID of the vanilla SiT-XL at 7M iteration" (Section 4.3), giving a 17.5× iteration reduction. This is stated as a concrete comparison, not a vague efficiency claim.

- **Counterintuitive finding about early-layer alignment**: The paper discovers that aligning only the first 8 layers (rather than all layers) produces the best generation results, and offers a plausible hypothesis: early layers learn semantics while later layers capture high-frequency details (Section 4.2, "Alignment depth" paragraph). This architectural insight goes beyond the simple addition of a loss.

- **Robustness of the regularization weight λ**: Table \ref{tab:lambda} shows FID and IS across λ ∈ {0.25, 0.5, 0.75, 1.0}, with FID saturating after 0.5 (7.8–7.9). This demonstrates the method is not hyperparameter-sensitive, which is practically important.

- **Cross-architecture and cross-objective validation**: REPA is validated on both DiT (Improved DDPM objective) and SiT (linear flow-matching), and the component-wise analysis covers target encoder choice, encoder size, alignment depth, objective (NT-Xent vs. cosine similarity), and model scaling. The system-level comparison in Section 4.3 shows consistent improvements for both architectures.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **The 17.5× speedup compares iterations, and the additional compute cost of the external encoder is not discussed.** The paper frames the speedup purely in terms of training iterations (7M → 400K). The per-iteration cost of running DINOv2-g (~1.1B parameters) to extract clean-image features is never mentioned. In practice, these features can be precomputed and cached (they depend only on the clean image, not on noise), which would make the additional overhead negligible. However, the paper does not acknowledge this caching possibility or report any wall-clock timing data. A practitioner reading the headline "17.5× faster training" would benefit from knowing whether this holds in wall-clock time and under what conditions.

- **The SOTA claim is confounded with guidance interval scheduling.** The paper reports that REPA achieves state-of-the-art FID using "guidance interval" (Kynkäänniemi et al., 2024), which is a post-hoc sampling procedure applied on top of the trained model. The comparison baselines in Table \ref{tab:system_comparison} may or may not use guidance interval — the paper does not clarify this. Since guidance interval can independently improve FID, the additive contribution of REPA alone is not cleanly separated from the contribution of the inference-time technique. The paper reports two numbers (with and without guidance interval), but the SOTA framing would be stronger if it explicitly stated which baselines use which sampling procedure.

- **No discussion of limitations or scope.** The paper ends with a brief conclusion and contains no limitations, broader impact, or future work discussion. Several scope boundaries are material: (a) the method is demonstrated only on class-conditional ImageNet 256×256 generation — generalization to text-conditional generation, video, or other modalities is unaddressed; (b) the method requires a pretrained self-supervised visual encoder matched to the target domain (e.g., DINOv2 for natural images), which may not be available for out-of-distribution domains like medical imaging or satellite imagery; (c) the regularization introduces an additional hyperparameter λ and a trainable projection head h_φ, which, while not burdensome, should be acknowledged.

### Trivial
None.

## Nice-to-Haves
- Report wall-clock training time with and without REPA, and clarify whether DINOv2 features are cached or recomputed per-iteration.
- Train both REPA and vanilla models with and without guidance interval to isolate the additive contributions of each technique.
- Add a brief limitations paragraph acknowledging the scope boundaries noted above.

## Removed Points
These points were flagged by reviewers but are removed (or demoted) for the reasons noted:

- **"Vanilla SiT baseline FID (no CFG) is never stated"** — The paper references Table \ref{tab:wo_cfg}, which is included via `\input` in the main body (not an appendix). The table exists in the submitted PDF; its absence from the extracted text is a parser artifact, not an author omission. The critic's concern about cross-referencing is not a valid weakness given the table's presence in the submission.
- **"Undefined macros \bestfid and \bestfidinterval"** — Parser artifact from stripped LaTeX preamble. These resolve to actual numbers in the original PDF.
- **"Missing hyperparameters / reproducibility details"** — The paper states "We strictly follow the setup in DiT and SiT unless otherwise specified" (Section 4.1), which is standard practice for methods built on top of well-known architectures. Listing every training hyperparameter from prior work is not expected.
- **"Whether vanilla numbers are reproduced or taken from original publications"** — Nitpick that does not affect the paper's validity. The paper separately reports vanilla baselines for comparison.
- **"No error bars / variance"** — Single-seed FID reporting is standard in the diffusion model evaluation literature. The reviewer themselves noted this is acceptable.
- **Pure formatting/style nitpicks** — Removed per the filtering rules.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
- In the speedup claim, add a sentence clarifying whether DINOv2 features are precomputed and cached (making the per-iteration overhead negligible) or recomputed each step (adding a cost that should be reported in wall-clock terms).
- In Table \ref{tab:system_comparison}, add a column or footnote indicating which baselines use guidance interval, CFG, or other sampling techniques, so the SOTA comparison is unambiguous.
- Add a brief limitations paragraph to the conclusion discussing domain transfer, encoder requirements, and the additional λ hyperparameter.

## Score and Decision
The paper presents a clean, well-motivated method with thorough ablations and striking empirical results. The weaknesses are presentation and clarity issues, not structural flaws. The core contribution — that aligning diffusion transformer representations with external self-supervised encoders dramatically accelerates training — is well-supported and practically valuable.

MY FINAL SCORE: <score>7</score>
MY FINAL DECISION: <decision>Accept</decision>
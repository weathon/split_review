Now let me compile the final review with score and decision.

## Summary
DiSTAR proposes a zero-shot TTS framework that couples an autoregressive language model (AR drafter) with a masked diffusion model, both operating entirely in a discrete RVQ code space. The AR model drafts block-level token sketches while the diffusion model performs parallel masked infilling within each patch, enabling patch-wise parallelism without continuous-domain optimization issues. Key design innovations include embedding transplantation from the RVQ codebook, stochastic RVQ layer truncation for variable bitrate inference, and temperature-based decoding heuristics to address a diagnosed "tail-first bias." Experiments on LibriSpeech-PC and Seed-TTS show DiSTAR-medium (0.3B parameters) achieves the best WER among compared systems, with competitive SIM and UTMOS.

## Strengths
1. **Novel and well-motivated architecture**: Coupling an AR drafter with masked diffusion in the discrete RVQ domain is a creative synthesis that inherits the stability of discrete LM training while enabling patch-level parallelism. The discrete code space avoids optimization fragilities of continuous latents and preserves [EOS] token termination, eliminating the need for auxiliary duration predictors (Section 1, Section 3.1). This is a genuine architectural advance over both pure-AR discrete systems and continuous patch-diffusion systems.

2. **State-of-the-art WER with equal or fewer parameters**: In Table 1, DiSTAR-medium (0.3B) achieves the lowest WER on both LibriSpeech-PC (1.66%) and Seed-TTS test-en (1.32%), outperforming DiTAR (0.6B, 2.39/1.78), F5TTS (0.3B, 2.02/1.35), E2TTS (0.3B, 2.74/2.20), and IndexTTS (0.5B, 2.57/1.92). The parameter efficiency is particularly notable against DiTAR (2× fewer parameters).

3. **Inference-time RVQ layer pruning without retraining**: Stochastic layer truncation during training (Section 3.4) enables flexible bitrate/compute trade-offs at inference by simply pruning upper RVQ layers. Figure 2 validates a smooth SPK/WER trade-off across 2–9 RVQ layers, which is a practical advantage over systems requiring separate models for variable bitrates.

4. **Diagnosis and mitigation of "tail-first" bias**: Section 3.4 identifies a specific failure mode in RVQ masked diffusion (overconfidence at patch-end positions) and proposes three lightweight decoding heuristics. Table 3 shows WER improvement from 2.11 (vanilla sampling) to 1.99 (shaped sampling), validating this insight with empirical evidence.

5. **Best subjective results on Seed-TTS**: Table 2 shows DiSTAR achieves the highest SMOS (3.31) and the only positive CMOS (0.22) among compared systems, corroborating objective metrics with human judgments.

## Weaknesses

### Fatal
None.

### Major
1. **No variance estimates on main objective results (Table 1)**: All metrics in Table 1 (WER, SIM, UTMOS) are point estimates without confidence intervals or standard deviations. This is a significant evidential gap for a paper whose comparative claims hinge on small numerical margins. DiSTAR-medium's WER of 1.32 vs F5TTS's 1.35 on Seed-TTS (0.03 difference) or SIM of 0.67 vs E2TTS's 0.70 on LibriSpeech could invert under different test splits or random seeds. Table 2's subjective results include confidence intervals, making the omission in Table 1 more conspicuous.

2. **Unmatched inference cost comparison with DiTAR**: DiTAR, the most directly comparable system (same patch-level AR+diffusion paradigm, differing in continuous vs discrete representation), is evaluated at NFE=10 while DiSTAR uses NFE=24—a 2.4× advantage. The abstract claims DiSTAR "maintains the inference cost close to its continuous counterpart DiTAR," but this is not directly supported when NFE differs this much. While DiSTAR uses fewer parameters (0.3B vs 0.6B), a clean compute-matched comparison is needed to substantiate the efficiency claim.

3. **Overclaimed "state-of-the-art" framing**: The abstract states DiSTAR "surpasses state-of-the-art zero-shot TTS systems in robustness, naturalness, and speaker/style consistency." The paper's own data supports this claim fully only for WER (robustness). On SIM, DiSTAR-medium scores 0.67/0.66 vs E2TTS's 0.70/0.71—third best on both benchmarks. On UTMOS, DiSTAR-medium scores 4.27/4.05 vs IndexTTS's 4.35 and DiTAR's 4.15—not best. The body text (Section 4.2) is more measured ("on par with the best alternatives"), but the abstract's sweeping SOTA claim is not fully supported.

4. **Insufficient ablation of core architectural components**: The only ablation in the main paper (Table 3) compares decoding strategies, which does not isolate the paper's claimed architectural innovations. There is no component ablation showing: (a) performance without the masked diffusion module (AR-only patch-level prediction), (b) performance without the AR drafter (diffusion-only), or (c) the effect of stochastic layer truncation vs. fixed-depth training. Without isolating components, it is difficult to attribute performance specifically to the AR+masked diffusion coupling vs. overall model capacity.

### Minor
5. **Diversity claimed but not measured**: The abstract and introduction emphasize "rich output diversity" as a key advantage, but no quantitative diversity metric (e.g., DIST, self-BLEU, utterance-level acoustic variation) is reported. The only evidence is the existence of sampling options in Table 3.

6. **Incomplete subjective evaluation coverage**: Subjective evaluation (Table 2) is conducted only on Seed-TTS test-en. DiTAR and IndexTTS—the strongest objective competitors on UTMOS—are absent from subjective comparisons, making cross-referencing difficult.

7. **CFG training/inference asymmetry not fully explained**: Section 3.4 states CFG drops two conditioning signals during training (AR LM output and past-code window, probability 0.1 each), but at inference "CFG is applied only to the historical code with a guidance scale of 1.25." The rationale for applying CFG to only one signal at inference is not explained.

### Trivial
8. **Minor noise in Figure 2 RVQ pruning curve**: WER shows non-monotonic behavior (increases from 1.88 at layer 6 to 2.04 at layer 8, then drops to 1.98 at layer 9), and no error bars are provided.

## Nice-to-Haves
- Matching NFE between DiSTAR and DiTAR for a cleaner comparison, or providing FLOPs/latency numbers to substantiate the "comparable inference cost" claim.
- Component ablation removing the masked diffusion module (AR-only) or the AR drafter (diffusion-only) to isolate the benefit of the coupled architecture.
- Reporting diversity metrics (e.g., DIST-1/2/3, self-BLEU) for the different decoding strategies.
- Error bars on the RVQ pruning experiment (Figure 2).

## Removed Points
These points were raised by reviewers but removed after verification against the paper.
- "Missing contemporary baselines (VoiceCraft, VALLE)": The paper compares against a strong set of recent SOTA systems (IndexTTS, E2TTS, F5TTS, DiTAR). Including every prior system is not standard practice. Removed as scope overreach.
- Criticism that the abstract's criticism of continuous-latent approaches is "asserted rather than demonstrated": This is acceptable high-level motivation; detailed evidence is not expected in a motivation paragraph.
- Various formatting/style nitpicks: These are parser artifacts, not author errors.
- Claims about "cannot be independently verified" or reproducibility concerns about unreleased code/models: Per instructions, cited entities are assumed to exist.
- Point about token-level factorization in Eq. (1) vs. patch-level inference: The paper explicitly acknowledges this mismatch and explains it. This is standard for patch-wise generation and not a real weakness.
- Generic "evaluation lacks rigor" framing without concrete anchor: Removed per filtering discipline.

## Novel Insights
Beyond the paper's own contributions, the cross-review synthesis surfaces two observations. First, the tension between the paper's strongest evidence (WER SOTA at low parameter counts) and weakest evidence (SIM/UTMOS not leading) suggests the discrete RVQ domain may specifically benefit linguistic/content fidelity while compressing some acoustic detail relative to continuous-domain systems—a trade-off worth investigating as a property of the representation rather than the method. Second, the three decoding heuristics for "tail-first bias" are explicitly described as "lightweight decoding tricks" rather than architectural fixes, which is honest but also means the paper's main methodological novelty (AR+masked diffusion coupling) has a thinner evidence base than a reader might expect—the heuristics do important work and should be more carefully isolated.

## Suggestions
1. Add confidence intervals or standard deviations to Table 1 (run evaluations with multiple random seeds or report bootstrap confidence intervals).
2. Either evaluate DiSTAR at NFE=10 or DiTAR at NFE=24 to provide a compute-matched comparison.
3. Tone down the abstract's SOTA claim to match what the data actually shows (state-of-the-art robustness with competitive naturalness and similarity).
4. Add core component ablations (AR-only, diffusion-only) to isolate the contribution of the coupled architecture.
5. Report diversity metrics (DIST, self-BLEU) if output diversity is claimed as an advantage.
6. Clarify the rationale for the CFG training/inference asymmetry (Section 3.4).

## Score and Decision

**Calibration anchors consulted:**

| Paper | Avg Score | Round | Comparison |
|---|---|---|---|
| Simple-TTS | 3.00 | R1 lower | Much weaker evaluation, simple method → DiSTAR clearly stronger |
| Fox-TTS | 3.00 | R1 lower | Compared only to CosyVoice, very weak baselines → DiSTAR stronger |
| DiTTo-TTS | 6.25 | R1 middle | Extensive ablations, similar domain, but novelty concerns → DiSTAR has stronger novelty but weaker evaluation specifics → slightly below |
| CLaM-TTS | 6.40 | R1/R2 middle | RVQ-based TTS, strong novelty and evaluation → DiSTAR comparable but lacks error bars → slightly below |
| DiffAR | 5.75 | R1 middle | Autoregressive diffusion for raw speech → less directly comparable domain |
| MaskGCT | 5.25 | R2 lower-middle | Masked generation on discrete tokens, limited novelty → DiSTAR has stronger novelty, comparable evaluation → above |
| HALL-E | 6.40 | R2 middle | Hierarchical codec LM, only compared to VALL-E → DiSTAR compares to more baselines but has weaker variance reporting → comparable |
| Variational Speech LM | 5.50 | R2 lower-middle | Different approach, less directly comparable |

**Round 1 bracket:** Between 5.0 and 7.0. The paper is clearly above rejected-level papers like Fox-TTS (3.0) but has evidential gaps that prevent it from reaching the top tier.

**Round 2 narrowing:** Compared against MaskGCT (5.25), DiTTo-TTS (6.25), CLaM-TTS (6.40), and HALL-E (6.40). DiSTAR has stronger novelty than MaskGCT (5.25) but weaker evaluation specifics than DiTTo-TTS (6.25) and CLaM-TTS (6.40) — specifically the lack of variance estimates, unmatched NFE comparison, and thin component ablations. The most appropriate position is between these anchors, slightly below the well-established 6.25-6.40 papers due to evidential gaps.

**Final score: 6.0** — The paper presents a genuinely novel architecture with strong WER results and practical advantages, but the evidence is weakened by the absence of error bars on main results, an unmatched NFE comparison with the closest competitor, overclaimed SOTA framing, and insufficient component ablations. These are addressable in revision and do not undermine the core contribution.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>
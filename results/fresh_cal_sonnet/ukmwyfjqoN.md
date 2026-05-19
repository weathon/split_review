Now I have a thorough reading of the paper. Let me run the calibration search.**Round 1 Bracket**: Based on the anchors, the paper sits in the **4–6** range. It has a genuine engineering contribution (speed advantage, dual-branch design, new datasets) but multiple significant issues (draft annotations, inconsistent results across datasets, no temporal consistency metric, recurrent asymmetry, weak user study). It's clearly above the reject-at-2-3 tier but doesn't reach the strong accept tier. Let me narrow within 4–6.Now I have enough data to write the review. Let me synthesize everything.

---

## Summary

ReBotNet proposes a real-time video enhancement framework built on a dual-branch encoder: Branch 1 tokenizes stacked input frames as tubelets processed by ConvNeXt blocks → MLP-Mixer bottleneck to learn spatio-temporal features; Branch 2 extracts image-level patch tokens per frame via linear layers, also mixed by an MLP-Mixer to learn inter-frame temporal dependencies. A recurrent setup feeds the previously enhanced frame ($y_{t-1}$) alongside the current degraded frame ($x_t$). The paper also introduces two new video enhancement datasets (PortraitVideo, FullVideo) targeting video-call and streaming scenarios. The central claim is that ReBotNet matches or exceeds the PSNR/SSIM of transformer-based SOTA (RVRT) while running at real-time speeds (2.5× faster at matched FLOPs).

---

## Strengths

- **Genuine speed advantage at matched FLOPs.** Table 1 shows ReBotNet (L) achieving 19.98 ms latency vs. RVRT's 52.30 ms (~2.5×) with 363.76 GFLOPs vs. 396.29 GFLOPs. At the M regime, ReBotNet (M) achieves 15.02 ms vs. RVRT (M) at 35.93 ms. These gains are real and substantial, and the matched-FLOP evaluation framework is methodologically sound.

- **Superior PSNR on PortraitVideo across all regimes.** Table 1 shows ReBotNet (L) at 32.13 dB vs. RVRT at 31.92 dB on PortraitVideo, with the advantage persisting at the M regime (31.85 vs. 31.60). For the targeted video-call use case, the improvements are consistent.

- **Comprehensive ablation validating individual components.** Table 4 systematically shows each component's contribution: tubelet tokens alone (31.24), adding image tokens (+0.17), adding bottleneck mixer (+0.18), adding recurrent setup (+0.26), all at essentially constant latency (14.27→15.02 ms). This confirms the architectural choices are each individually beneficial.

- **Two new multi-degradation benchmark datasets.** PortraitVideo (113/20 train/test, 384×384) and FullVideo (132/20, 720×1280) fill a real gap in the literature, which focuses on single-degradation tasks. Both datasets target practical video-call/streaming scenarios.

---

## Weaknesses

### Fatal
None.

### Major

- **Draft annotations from internal co-author review remain in the submitted manuscript.** Visible throughout the text are unresolved markers such as `\al{...}`, `\rg{...}`, and `\jmj{...}`. Substantively, line 46 contains an unresolved comment about whether the datasets were released ("If we publish the data, it would strengthen this contribution..."), leaving the dataset contribution ambiguous. More importantly, lines 88 and 101 reveal a genuine conceptual tension: the paper alternately describes Branch 2 as extracting "spatial features" (Section 3.2: "extracts just the spatial features using linear layers") or "temporal information" (Fig. 2 caption: "learn temporal features") or both. The internal comment at line 101 — reviewer `rg` asking "I thought the second branch learns spatial features?" and `jmj` answering "yes, it extracts spatial features but that facilitates temporal mixing" — was caught but never resolved in the text. This creates genuine reader confusion about what Branch 2 conceptually contributes, and reveals the paper was submitted before author-side revision was complete.

- **Temporal consistency — the paper's stated central motivation — is never measured.** The abstract, introduction (line 31–32), Section 3.4, and the figure captions all claim that Branch 2 and the recurrent setup exist specifically to "improve temporal consistency." Yet the evaluation reports only per-frame PSNR and SSIM, averaged across frames. No temporal warping error, flow-based consistency, or perceptual temporal smoothness metric appears anywhere in the paper. A core architectural motivation that is argued for at length must have at least one supporting measurement.

- **Recurrent comparison is structurally asymmetric and unacknowledged.** ReBotNet receives its own previous *enhanced* output frame $y_{t-1}$ as a recurrent input (line 133: "we make use of current degraded frame $x_t$ and the previous enhanced frame $y_{t-1}$"). Competing recurrent baselines (BasicVSR++, RVRT) use degraded neighboring frames. This provides a systematically stronger conditioning signal. The +0.26 PSNR gain attributed to the recurrent setup (Table 4) is thus confounded: it is unclear how much is due to architectural design versus the advantage of conditioning on an already-restored frame. The paper neither acknowledges this structural difference nor controls for it with a matched ablation.

- **Quality improvements are inconsistent across datasets.** Table 1 is unambiguous: at the M regime, RVRT (M) outperforms ReBotNet (M) on FullVideo (33.59 vs. 33.45 PSNR). At the L regime, RVRT again outperforms ReBotNet (L) on FullVideo (33.79 vs. 33.65). The introduction's claim of "0.2 dB improvement over previous SOTA" (line 35) and Table 1's caption's claim of "outperforms most previous approaches" are selective — accurate for PortraitVideo but contradicted by FullVideo. The paper does not acknowledge this asymmetry.

### Minor

- **FPS comparison uses inconsistent configurations relative to the main table.** Figure 3 / Section "FPS and Peak Memory Usage" (line 326–330) compares ReBotNet (L) against the *default* implementations of prior methods. The main results table uses FLOP-matched configurations. These are different comparisons and the paper does not reconcile them. The real-time claim holds at matched FLOPs, but the FPS figure presents a comparison that conflates configuration and architecture.

- **First-frame inference behavior is stated only in a commented-out line.** Line 134: "During training, we use the ground truth frame as initial prediction... %During inference, we just duplicate the first frame for the initial frame prediction." The inference behavior is confined to a comment and never appears in the main text. The train/inference mismatch and its effect on scene transitions are not characterized.

- **Latency is measured only at 384×384, not at FullVideo's actual resolution.** Line 208 and line 326 confirm all latency numbers use 2 frames of dimension 384×384. FullVideo is 720×1280. Whether ReBotNet achieves real-time throughput at 720p is unreported, which is a gap relative to the paper's stated real-world use case for FullVideo.

### Trivial

- The RVRT (S) entry in Table 1 is empty ("- ") with no in-text acknowledgment beyond a single footnote. A brief inline note would help readability.

---

## Nice-to-Haves

- Adding a temporal consistency metric (e.g., temporal warping error or flickering metric) would uniquely validate both Branch 2 and the recurrent setup in a way PSNR cannot.
- A matched ablation where competing recurrent baselines also use their own previous *enhanced* output (rather than degraded input) as the recurrent signal would disentangle architectural gain from the "clean feedback" advantage.
- Reporting latency at 720p would make the real-time claim concrete for the FullVideo scenario.
- Confirming dataset release with a link (resolving the inline comment at line 46).

---

## Removed Points

*These points were raised but are removed per the filtering rules; treat them with caution.*

- **User study statistical validity (Harsh Critic).** The critic argues that CIs over n=3 raters are invalid, and that the CI appears computed over ~240 pairwise comparisons. Partially valid: 3 raters is small and the paper states "95% confidence intervals for paired samples" (line 229), which if computed over comparison pairs rather than raters would inflate precision. However, this is partially addressable and the user study is a supporting (not central) claim. Moved to Removed; it is a minor methodological concern, not a fatal one.

- **Headline speed figure staging (Harsh Critic).** The critic says Figure 3 is "staged" because it uses ReBotNet (L) vs. default implementations. The paper explicitly states this in line 326: "we consider...ReBotNet (L) configuration with original implementations for the previous methods." This is disclosed, and comparing to default implementations is standard for an FPS/memory figure (the main accuracy comparison is FLOP-matched). It remains a presentation inconsistency (noted as Minor above) but not a fabrication. Demoted from Major.

- **Train/test split overlap with TalkingHeads public splits.** Raised as a concern about possible overlap with literature splits. The paper says it uses video IDs from TalkingHeads for FullVideo but applies different pre-processing. No external source confirms this is actually a problem; removed per rules against speculation without grounding.

- **Strength: "User study showing perceptual preference" (Strength Finder).** The +0.08 result over RVRT with 3 raters provides no meaningful perceptual evidence against the closest competitor. This strength is weakened by the verified weakness. Removed from strengths; kept here for transparency.

- **Generic strength about "addressing an important problem."** Removed as non-specific.

---

## Novel Insights

The most structurally interesting observation — raised by the Harsh Critic and verifiable in the paper — is the clean-feedback asymmetry in the recurrent setup: ReBotNet conditions on its own enhanced output, while competing recurrent methods receive degraded inputs. This is not acknowledged anywhere in the paper and makes it non-trivially difficult to attribute the recurrent gain in Table 4 (Ablation). A study that gave all recurrent baselines the same "clean feedback" signal would be a genuine scientific contribution beyond what the paper currently presents. Additionally, the conceptual relationship between Branch 2 and temporal consistency is genuinely unclear in the submitted text: whether Branch 2 primarily extracts spatial features that enable downstream temporal mixing, or whether it directly models temporal dependencies, is never pinned down with precision.

---

## Suggestions

1. Resolve all `\al{...}`, `\rg{...}`, `\jmj{...}` annotations before resubmission; in particular, clarify the description of Branch 2 consistently (spatial extraction enabling temporal mixing) across abstract, figure captions, and Section 3.2.
2. Add at least one temporal consistency metric (e.g., temporal warping error) to quantitatively support the temporal consistency claims.
3. Acknowledge and ablate the clean-feedback asymmetry in the recurrent comparison.
4. Revise the claim of "0.2 dB improvement over previous SOTA" to be dataset-specific; acknowledge that RVRT outperforms ReBotNet on FullVideo.
5. State the first-frame inference procedure explicitly in the main text and include a brief analysis of its effect.
6. Report latency at FullVideo (720×1280) resolution.

---

## Score and Decision

**Anchor comparison:**

| Paper | Path | Avg Score | Round | Comparison |
|---|---|---|---|---|
| LVM-NET | bEvI30Hb2W.md | 3.00 | R1 (low) | Much weaker; fundamental novelty issues |
| VideoDiT | lvgsPjRtLM.md | 2.50 | R1 (low) | Much weaker; poorly executed |
| SCHEME | U4ekUAOLsM.md | 5.00 | R1 (mid) | Comparable; architectural mixer work, presentation gaps |
| VEnhancer | Ysdo3fyD4Q.md | 5.00 | R1/R2 (mid) | Comparable; video enhancement with some evaluation gaps |
| Live2Diff | YA1Ur2eGFl.md | 4.67 | R2 | Comparable; real-time video processing, presentation issues, some evaluation gaps |
| DiffIR2VR-Zero | qpDqO7qa3R.md | 5.25 | R2 | Comparable; video restoration, weaker in novelty but cleaner submission |
| SANA | N8Oj1XhtYZ.md | 8.50 | R1 (high) | Much stronger; comprehensive, clean, SOTA across multiple benchmarks |
| Vision-RWKV | nGiGXLnKhl.md | 8.00 | R1 (high) | Much stronger; thorough evaluation and analysis |

**Round 1 bracket**: 4–6.

**Round 2 narrowing**: ReBotNet is most comparable to Live2Diff (4.67) and VEnhancer/DiffIR2VR-Zero (5.0–5.25). ReBotNet has a more solid technical contribution than Live2Diff (more comprehensive evaluation, new datasets, matched-FLOP framework) but has the unusual problem of draft annotations in the submission that reveal unresolved conceptual confusion — something Live2Diff does not have. Compared to DiffIR2VR-Zero (5.25), ReBotNet has more novel architecture and clearer real-world motivation, but the submission-readiness issues and absent temporal consistency measurement pull it down. The major weaknesses — absent temporal evaluation of a stated design goal, unacknowledged recurrent asymmetry, inconsistent quality results across datasets, and the uncommonly visible draft state — collectively push toward the lower end of the 4.5–5.5 bracket. The paper has real substance but requires substantive revision to be convincing on its own terms.

**Final score: 4.5**

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>
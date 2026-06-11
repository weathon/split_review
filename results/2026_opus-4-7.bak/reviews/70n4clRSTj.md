## Summary
SpookyBench is a benchmark of 451 synthetic videos where content (words, object silhouettes, dynamic depth-map scenes) is encoded entirely in opposing motion patterns of binary noise — each individual frame is i.i.d. noise, and the content is only perceptible during playback. Humans achieve ~98% accuracy while 15+ open- and closed-source VLMs (Video-LLaVA, TimeChat, InternVL2/2.5, Qwen2/2.5-VL, LLaVA-NeXT-Video, GPT-4o, Gemini 1.5 Pro, Gemini 2.0 Flash) score a uniform 0% across categories, scales, prompting strategies, frame rates, and after fine-tuning, leading the authors to claim a fundamental "time-blindness."

## Strengths
- Stimulus construction (Algorithms 1–2, Figure 2) genuinely isolates motion-only information: every frame is i.i.d. noise, so spatial shortcuts are unavailable — a real gap relative to prior video benchmarks where most questions are answerable from a single frame.
- Breadth of evaluation is unusually large: Table 1 spans 15+ VLMs from 2B to 78B parameters and includes both direct and CoT prompting; the 0% result holds across all of them, making the headline gap hard to dismiss as anecdotal.
- Section 4.4 in-distribution fine-tuning of InternVL2.5-8B and Qwen2-VL-7B on 400 SpookyBench videos for 10 epochs still yields 0%, which credibly rules out the simplest "out-of-distribution" explanation.
- Evaluation protocol (§4.1) accepts multiple semantic equivalents and explicitly notes that no model produced any response matching any acceptable option, preempting concerns about overly strict matching.
- Human baseline (§4.2, Table 3) with 6 annotators, per-category accuracy, perceptibility ratings, and an FPS sweep (Table 4) provides a credible reference distribution.

## Weaknesses

### Fatal
None.

### Major
- **Overgeneralization of "time-blindness."** Because each frame is i.i.d. noise and standard VLMs encode frames through a frozen image encoder before any temporal fusion, the parsimonious explanation is that SpookyBench is adversarially matched to the frame-encoder bottleneck — a narrower claim than the paper's framing in §1, §3.3.2, and §5 about implications for "medical diagnostics," "autonomous vehicles reading road signs," and "temporal reasoning" generally. Standard video benchmarks test event order, causality, and duration; those are different competences from figure-from-motion against pure noise, and the paper's extrapolation is not supported.
- **The fine-tuning experiment does not warrant the "fundamental architectural inability" conclusion (§4.4).** LlamaFactory with 10 epochs on 400 videos typically updates the LLM head / LoRA adapters but leaves the visual encoder and frame sampler frozen — exactly the components §5 identifies as the bottleneck. A negative result here is consistent with adapter-style FT failing, not with architectural impossibility. The conclusion should be hedged to "standard adapter fine-tuning does not close the gap" unless a full / encoder-unfrozen FT with denser native frame count is added.
- **FPS sweep is confounded by internal frame subsampling (§4.3).** Most evaluated VLMs sub-sample to a fixed number of frames (8/16/32) regardless of input FPS, so the 1–30 FPS sweep largely modulates a property the encoder never sees, while effective temporal density is held nearly constant. The strongest alternative explanation — encoder-level temporal undersampling — is not separated from "no temporal mechanism." Notably, the human curve (Table 4) collapses to 0% at 1 FPS, i.e., humans also fail when temporal density drops to the regime VLMs effectively operate in, which is consistent with the alternative account.
- **Internal inconsistency in §3.3.2 / Figure 4.** The text says "Prompts performed best (40% accuracy)" and "words … jumped to 85.7% accuracy above this threshold," and Figure 4's table shows accuracy stepping from 0.00 at SNR≤2 dB to 1.00 at SNR≥3 dB, with the caption explicitly labeling this as "detecting words with direct prompting and chain of thought prompting" — i.e., a *model* curve. This directly contradicts Table 1's uniform 0% across all models and prompts. Either Figure 4 actually shows human accuracy (in which case the §3.3.2 narrative about "language models cannot identify text below certain thresholds" is reversed), or the high-SNR stimuli are easier than the main benchmark (in which case the headline "uniform 0%" needs qualification). As written, this is unreconciled.

### Minor
- **No positive control.** No architecture (e.g., 3D CNN, TimeSformer, optical-flow-conditioned model) is shown to solve SpookyBench, so it is not established that the task is solvable in principle by any learned system operating on compressed video tokens. A single existence proof would convert "everything fails" into "we have localized the missing ingredient."
- **Neuroscience material in §2.2 is decorative** — not used to design stimuli or predict where models fail.
- **SNR metrics (§3.3) are descriptive, not predictive.** Four SNR variants are computed per category but never used to predict per-video model behavior beyond the disputed §3.3.2 paragraph.
- **Architectural recommendations in §5 are generic** (recurrent processing, motion-contrast pathways, longer temporal windows) and not specifically favored by any experiment.
- **Failure-mode analysis is thin** — §5 says models "attempt to extract information from individual frames" but does not categorize refusals vs. hallucinations vs. noise descriptions, which would strengthen the diagnostic value.

### Trivial
None retained.

## Nice-to-Haves
- One positive-control architecture (flow-aware or pixel-level temporal model) showing the task is solvable.
- Re-run the FPS sweep while holding the number of frames the model actually ingests constant.
- A clarified, unambiguously labeled SNR-threshold curve specifying whose accuracy is measured, and reconciliation with Table 1.
- Tighten the rhetorical scope to "figure-from-motion against structured noise."

## Removed Points
These points are flagged to be removed, treat them with caution.
- "Extensible by design" strength — generic; the benchmark being procedurally generated is normal for a synthetic benchmark.
- "Important problem" framing strength — generic, not specific evidence.
- Harsh critic's framing of §2.2 as a fatal weakness — downgraded to minor; decorative motivation sections are common.

## Novel Insights
The most useful observation across the reviews is that the 0% likely localizes to the frozen frame encoder / frame subsampler rather than to "temporal reasoning" broadly: when every frame is i.i.d. noise, the per-frame embeddings are indistinguishable noise vectors, so any downstream temporal module receives no signal regardless of its sophistication. This reframes SpookyBench as a sharp probe of the frame-encoder bottleneck — a strictly more actionable diagnostic than the paper's current "general temporal blindness" framing.

## Suggestions
- Add a positive-control architecture (e.g., 3D CNN or VLM with optical-flow input) to demonstrate solvability.
- Decouple input FPS from the number of frames the encoder ingests in §4.3.
- Either run a stronger fine-tune (visual encoder unfrozen, denser native frames) or soften the "fundamental architectural inability" claim.
- Reconcile §3.3.2 / Figure 4 with Table 1 and clearly label whose accuracy is plotted.
- Narrow §1 and §5 claims to figure-from-motion against structured noise; drop the medical-imaging / autonomous-driving extrapolation unless evidence is added.

## Calibration

Anchors retrieved:
- R1, low band: LVM-NET (3.0), VideoGPT+ (3.4), MCTBench (3.0), Industrial LLM Benchmarking (3.0) — all reject, less compelling diagnostics.
- R1, mid band: TVBench (6.75, accept), ViLMA (6.0, accept), TemporalBench (4.2, reject), T3 (6.8, accept) — TVBench/ViLMA most topically similar.
- R1, high band: Visual Data-Type Understanding does not emerge from scaling VLMs (8.0, accept) — closest analogue: diagnostic benchmark exposing a VLM blindspot across many models. PhysBench (8.0), Multi-granularity (8.0), Two Effects One Trigger (8.0) less topical.
- R2: "Can We Predict Performance" (5.75), vVLM (5.0), ViLMA (6.0), ReForm-Eval (5.0), Vinoground (5.75, reject), TVBench (6.75), Boundary Denoising (5.75).

Round-1 bracket: 4.5–7. The paper's striking-gap empirical hook is closer to the "Visual Data-Type" 8.0 paper in spirit but with markedly weaker positive-control discipline and a clearer overclaim problem.

Round-2 narrowing: Vinoground (5.75, reject) is the closest comparator — a diagnostic temporal benchmark with a strong negative result on LMMs that was rejected partly for narrow scope and limited diagnostic depth. SpookyBench has a more striking gap and broader model coverage than Vinoground, but its overclaim, lack of positive control, and §3.3.2 inconsistency push it down. ViLMA (6.0) is more principled methodologically. The paper sits below ViLMA/TVBench but at or slightly above Vinoground.

Final: 5.5.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>
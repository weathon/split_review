## Summary
The paper proposes In-Context Watermarking (ICW), a black-box approach that embeds detectable signals in LLM outputs purely through instruction-level prompting, requiring no access to model logits or decoding. Four strategies of differing granularity (Unicode, Initials, Lexical, Acrostics) are paired with statistical detectors and evaluated in (a) a Direct Text Stamp (DTS) setting and (b) an Indirect Prompt Injection (IPI) case study for detecting LLM-generated peer reviews, with gpt-o3-mini achieving near-perfect ROC-AUC under both regimes.

## Strengths
- **Conceptual reframing is timely and well-motivated.** Moving watermarking from logits-level control to instruction-level control opens a legitimate gap (third parties without decoding access). The IPI peer-review case study makes this concrete and is the most novel contribution of the paper.
- **Capability dependence is empirically demonstrated.** Table 2 shows a sharp contrast: GPT-4o-mini largely fails on Initials/Acrostics (AUC ~0.57–0.59) while GPT-o3-mini achieves AUC ≥ 0.995, directly supporting the paper's "scales with capability" claim with concrete numbers.
- **Robustness against paraphrasing is real.** Figure 3 shows Initials/Lexical/Acrostics maintain AUC ~0.88–0.92 under paraphrase, outperforming YCZ+23 (AUC 0.557). Acrostics-as-watermark is a genuinely interesting empirical finding.
- **Text quality is preserved.** In Table 3, ICW variants score 4.28–4.81 overall vs. PostMark 2.997 and YCZ+23 3.865, with relevance scores close to unwatermarked output.
- **The paper is honest about scope** (Section 6 explicitly frames ICW as an "initial exploration" with capability dependence as a limitation).

## Weaknesses

### Fatal
None. The core empirical claims (ICW works on sufficiently capable LLMs in both DTS and IPI) are supported by Table 2/Figure 3 within the evaluated setup.

### Major
- **No unwatermarked-LLM-vs-human control for the detector.** The detectors compare LLM responses against ELI5 / human reviews. LLM text is already lexically and stylistically different from human text — without running the same detectors on *unwatermarked* o3-mini output vs. human text, the AUC numbers conflate the watermark signal with the baseline LLM-vs-human gap. This control is necessary for the headline detection claim to mean what the paper says it means.
- **Adversary-aware evaluation in IPI is deferred.** The IPI threat model is the headline contribution, yet the obvious adversarial defense — an "ignore prior instructions" prefix or any prompt-sanitization step — is acknowledged only as future work / Appendix D.1 rather than reported in the main text. Since this single move is the canonical defense, the paper's IPI claims would be substantially more convincing if those numbers were surfaced in the main results.
- **Key-secrecy is not analyzed for IPI.** The hypothesis-testing formulation in Section 3.1 requires `k` to be unknown to text-generators, but in IPI the watermark instruction (including the green letter/word list or acrostic key) is literally inside the PDF the reviewer downloads, so any reviewer who reads the raw text obtains `k`. The Initials spoofing footnote on p.6 acknowledges a fragment of this but does not address the structural issue: in IPI the detector's "secret key" is in plain view. This should at least be discussed formally.
- **No realistic PDF-ingestion pipeline tested in IPI.** Experiments concatenate the watermark instruction directly into text fed to the model (Eq. on p.4). Real reviewer workflows go through pdftotext / chat-app PDF upload, which can normalize or drop white-on-white text. Without testing whether the hidden instruction actually survives a realistic pipeline, the IPI motivation lacks end-to-end evidence.

### Minor
- **Cross-model evidence is thin.** The capability claim rests on two models (4o-mini → o3-mini) with a near-binary jump from "fails" to "near-perfect." Testing intermediate-capability models (e.g., other open-weight 7B–70B models, Claude/Gemini variants) would isolate which capability dimension — instruction following, long-context retrieval, or reasoning — actually drives ICW success.
- **`γ` from the Canterbury Corpus may be mis-specified for ELI5 / review text.** Initials ICW computes the z-statistic against `γ` derived from the Canterbury Corpus, but the evaluated corpora are ELI5 answers and ICLR reviews with different initial-letter distributions. A small validation that the null `γ` is well-calibrated on the actual human corpora is missing.
- **LLM-as-Judge sibling bias.** Using gemini-2.0-flash to judge o3-mini-generated text and baselines is a defensible choice, but cross-judge triangulation (or human evaluation on a subsample) would strengthen Table 3.
- **PostMark's quality scores (2.65 relevance, 2.49 clarity) are surprisingly low.** A sanity check or note explaining the PostMark configuration would lend more credibility to the head-to-head quality comparison.
- **Word-replacement attack disproportionately targets Lexical ICW.** Replacing only nouns/verbs/adj/adv is the operation Lexical ICW depends on, while Initials ICW exploits initial letters of *all* words, so it's relatively spared. The Initials > Lexical robustness ordering is somewhat an artifact of this attack design; an attack that targets initial-letter distributions (e.g., word reordering, sentence restructuring) would round out the picture.
- **Table 1 trade-off summary uses qualitative filled circles** rather than measurements, which weakens its value as a design guide.

### Trivial
- The acrostic null-distribution is estimated by resampling subsequences from the same suspect text (Section 4.2.4); this is unusual and would benefit from a brief justification of its FPR control properties.

## Nice-to-Haves
- A stealthier instruction-embedding study (e.g., instructions hidden as innocuous-looking sentences, comments, or footers) would convert the IPI scenario from a proof-of-concept into something closer to a deployable system.
- A formal analysis of what happens to the hypothesis test when the adversary observes `Instruction(k, τ)` (i.e., a key-secrecy threat model for IPI).
- A wider model panel (Llama-3-70B, Claude, Gemini) to better characterize the capability threshold suggested by the 4o-mini → o3-mini gap.

## Removed Points
These points are flagged to be removed; treat them with caution.

- **"Conferences secretly injecting prompts is unethical/IRB-fraught."** This is a normative concern the paper itself flags in a footnote and the Ethics Statement. It's not a methodological flaw in the paper and the authors discuss it transparently.
- **"Only two baselines (PostMark, YCZ+23, GPTZero)."** This drifts toward demanding broader related work coverage; the chosen baselines are reasonable representative black-box / post-hoc methods, and the paper does not claim exhaustive baseline coverage.
- **"Contribution is just transcribed steganography."** Stating prior steganography ideas (Unicode, green-lists, acrostics) is exactly the design space the paper aims to taxonomize for the new ICW setting. The contribution is reframing these into prompt-only watermarks plus the IPI case study, which is genuinely new — calling it "thin" overstates the case.
- **"No confidence intervals on T@1%F."** Single-run large-scale benchmark reporting is the norm in this subfield; this is a nice-to-have, not a substantive flaw.
- **Strength-finder claim that ICW is "model-agnostic, practical."** Partly conflicts with the verified weakness that the IPI scenario is not yet adversary-tested or pipeline-tested end-to-end. Kept only in weakened form.

## Novel Insights
The most genuinely novel insight is the reframing of watermarking as a *third-party prompt-engineering problem* rather than a model-owner decoding problem, combined with the IPI case study — embedding watermark instructions into the input document so that any downstream LLM consumer leaves a detectable trail. The capability-scaling empirical finding (sharp 4o-mini → o3-mini transition) is also worth highlighting: it suggests ICW is essentially gated on instruction-following quality, which is a forecastable axis. Beyond these, the per-strategy designs are largely transcriptions of classical steganography into the instruction-following idiom.

## Suggestions
- Run the unwatermarked-LLM-vs-human-text detector control to isolate watermark signal from the LLM/human distributional gap.
- Promote the "ignore prior prompts" adversarial result from the appendix into the main results table; if ICW collapses, say so plainly.
- Take at least one watermarked PDF through a real reviewer workflow (pdftotext, ChatGPT PDF upload, Claude file upload) and report whether the instruction survives.
- Add a formal key-secrecy section for IPI, since the document-embedded `k` is observable to the adversary.
- Expand the model panel beyond two OpenAI checkpoints to validate the capability-scaling claim.

## Overall Assessment
- **Originality:** Moderate. The ICW framing and IPI case study are novel and timely; the per-strategy designs reuse well-known steganographic motifs.
- **Importance:** Solid. AI-generated peer reviews are a real and growing problem, and a black-box, model-agnostic mechanism is genuinely useful.
- **Claim support:** Mixed. The DTS detection and quality claims are reasonably supported. The IPI motivation outruns the adversary-aware evidence, and the detection AUCs lack the unwatermarked-LLM control.
- **Soundness:** Adequate but not airtight; the missing controls and deferred adversarial evaluation are real gaps.
- **Clarity:** Good. The four strategies, detectors, and settings are clearly described.
- **Value to community:** Useful starting point for instruction-level watermarking research, particularly for the IPI use case, even if it's closer to a proof-of-concept than a finished system.

## Score and Decision

Anchor comparison (all anchors retrieved in the batch):
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/ujpAYpFDEA.md` (avg 7.5) — Prompt-crafted watermark identification; conceptually adjacent but more rigorous theory + experiments. The paper under review is less mature.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/E4LAVLXAHW.md` (avg 7.0) — Black-box watermark detection with rigorous stat tests; more comprehensive than this paper.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/DEJIDCmWOz.md` (avg 6.0) — Reliability-of-watermarks study, accepted; similar empirical character but broader robustness analysis.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/FDfq0RRkuz.md` (avg 5.5) — WASA source attribution; comparable scope, mixed reception; the paper under review has a cleaner motivating use case but thinner methodological depth.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/LdIlnsePNt.md` (avg 6.0) — SEAL semantic-aware watermarking; stronger theory.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/0KHW6yXdiZ.md` (avg 5.25) — End-to-end logit-based watermarking; comparable empirical-paper tier.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/ecbRyZZmKG.md` (avg 5.25) — Double-I watermark for fine-tuning; comparable mid-tier empirical paper.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/r6aX67YhD9.md` (avg 4.75) — RL-based watermark, rejected; weaker than paper under review.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/0koPj0cJV6.md` (avg 4.6) — Another black-box watermark, rejected; the paper under review has a more novel use case (IPI) but similar gaps in adversarial eval.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/eKGEsFdpin.md` (avg 3.67) — Sampling-based watermarking, weak baselines and rigor; the paper under review is clearly stronger.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/HexshmBu0P.md` (avg 5.33) — Diffusion watermarking recipe; comparable mid-tier execution.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/O08nfMzc93.md` (avg 4.5) — Image watermark attribution; similar tier.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/ETFfXGM3e4.md` (avg 5.5) — SAT-LDM image watermarking; mid-tier.

The paper under review is clearly better than the 3.67/4.6/4.75 cluster (it has a genuine novel framing, real empirical results, and honest scope), comparable to the 5.25–5.5 cluster (interesting idea, undercut by missing controls and deferred adversarial evaluation), and short of the 6.0+ accepted cluster (which has stronger theory, broader baselines, or more rigorous adversarial evaluation). It sits just below the median of mid-tier empirical watermarking submissions.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>
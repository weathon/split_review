Now let me look at the appendix discussion of attacks mentioned in the text:Now let me run calibration searches:Round 1 bracket: between 4.0 and 6.0. Let me read a couple of the closest anchors and narrow.Now I have enough calibration to write the final review. Let me synthesize.

## Calibration Summary

**Round 1 anchors retrieved:**
- jbfDg4DgAk.md (3.00, reject) — Sparse Watermarking — weak-band anchor
- vfEqSWpMfj.md (2.50, reject) — Word Importance — weak-band, off-topic
- z3DMFpaP6m.md (3.00, reject) — Entropy of LMs — weak-band, off-topic
- MV5j4Qpq7N.md (2.33, reject) — System-Prompt Attention — weak-band, off-topic
- eKGEsFdpin.md (3.67, reject) — Sampling-based watermarking — middle-low
- 0KHW6yXdiZ.md (5.25, reject) — End-to-End Logits Watermarking — middle band
- FDfq0RRkuz.md (5.50, reject) — WASA Source Attribution — middle band
- DEJIDCmWOz.md (6.00, accept) — On the Reliability of Watermarks — middle-high
- SnDmPkOJ0T.md (8.00, accept) — REEF Fingerprints — strong band
- j7b4mm7Ec9.md (7.60, reject) — Lightweight Watermarking — strong band
- syThiTmWWm.md (7.75, accept) — Null Models Benchmarks — strong, off-topic
- 84n3UwkH7b.md (8.00, accept) — Diffusion Memorization — strong, off-topic

**Round 1 bracket: 4.5 – 6.0**

**Round 2 anchors retrieved:**
- NvSwR4IvLO.md (4.67, reject) — "Can AI-Generated Text be Reliably Detected?" — important idea, weak evaluation; comparable in spirit to ICW's framing/evaluation gap
- 6p8lpe4MNf.md (5.50, accept) — Semantic Invariant Robust Watermark — clearer technical contribution and stronger evaluation than ICW
- hULJCP47PU.md (4.25, reject) — Two Halves Make a Whole — clearer fatal-ish soundness concerns
- YPIA7bgd5y.md (6.50, accept), wfLuiDjQ0u.md (7.00, accept) — off-topic ICL papers, accepted with stronger evaluations than ours

Comparing the ICW paper directly: it is more novel in *framing* than NvSwR4IvLO (which is a stronger paper but rejected for evaluation gaps), but its instantiations rest on known building blocks (Kirchenbauer-style biased vocab, Unicode insertion, acrostics) reframed as prompts. The evaluation has multiple genuine soft spots (saturated LLM-judge, Canterbury-Corpus null mismatch, content-blind robustness, no human readability study, deferred adversary analysis) that 6p8lpe4MNf does not share. The headline IPI numbers depend on a cooperative-or-oblivious adversary and a fragile white-text delivery channel. The paper sits slightly above NvSwR4IvLO (4.67) and below 6p8lpe4MNf (5.50). Final estimate: **5.0**.

---

## Summary
The paper introduces In-Context Watermarking (ICW): rather than perturbing the decoding process, a watermarking *instruction* is delivered to the LLM either as a system prompt (Direct Text Stamp) or covertly embedded inside an input document (Indirect Prompt Injection — motivated by detecting AI-generated peer reviews). Four instantiations are evaluated — Unicode insertion, Initials bias, Lexical (green-word) bias, and Acrostics — paired with bespoke statistical detectors. With a frontier model (gpt-o3-mini), all four reach ROC-AUC ≥ 0.995 in both settings; with gpt-4o-mini, three of the four collapse to near-chance.

## Strengths
- **Novel black-box paradigm that requires no decoding access** (§3.1, Eq. 1). Casting watermarking as prompt engineering is a genuinely new framing relative to in-process methods that need logits/sampling control, and it opens application surfaces (e.g., conference organizers) that previously had no watermark route at all.
- **The IPI case study is a meaningfully new application surface** (§3.2, Figure 2). Even setting aside how robust the delivery channel is, formally framing AI-review detection as an indirect-prompt-injection problem is original and likely to provoke useful follow-up work.
- **Strong detection numbers with a capable LLM** (Table 2): all four ICWs hit ROC-AUC ≥ 0.997 in both DTS and IPI with gpt-o3-mini; Unicode and Acrostics reach 1.000 in DTS.
- **Stronger paraphrasing robustness than the post-hoc baselines** (Figure 3, Paraphrase panel): Initials 0.887, Lexical 0.924, Acrostics 0.922 vs. PostMark 0.841, YCZ+23 0.557 — the regime that matters most for adversarial use.
- **Clean trade-off taxonomy across the four schemes** (Table 1), useful as a starting point for the subfield.

## Weaknesses

### Fatal
None — the paper does not collapse on any single verifiable claim.

### Major
- **The headline IPI scenario relies on a delivery channel (white text in PDF) the paper does not actually test.** §3.2 assumes the reviewer's PDF→LLM pipeline preserves invisible glyphs and that the LLM follows the smuggled instruction over the reviewer's own prompt. PDF-to-text extractors and OCR/screenshot pipelines used by real LLM apps regularly drop invisible text. The paper acknowledges defense study as future work (§3.2) but does not even sanity-check the *passive* failure modes (extractor dropping the payload), which would not require an adversary. Because the peer-review case study is the paper's main contribution, this is the weakest link in the load-bearing experiment.
- **The Acrostics scheme is, by construction, visible to a human reader.** Figure 1's own example shows a four-sentence response whose initials spell `MHAB`. For Initials with a small green-letter set, ~80% of a 300-word review starting with four letters reads unusually. The paper measures readability only with an LLM-as-a-judge that scores the unwatermarked baseline 4.982 / 5.000 / 4.994 (Table 3) — a saturated metric that cannot distinguish "still readable" from "obviously suspicious to a human editor." Since the deployment audience (conference editors) is precisely the audience most likely to skim and notice, the absence of any human-detection check leaves the covertness claim unsupported.
- **Effectiveness is sharply gated on a single tier of frontier model.** Table 2 shows Initials/Acrostics at 0.57–0.62 AUC on gpt-4o-mini in *both* DTS and IPI — essentially non-detection. Three of the four schemes therefore work only on one tier of model; Unicode (the fourth) is acknowledged to be trivially defeated by paraphrase or platform transit (§4.2.1). The "as LLMs improve, ICW will improve" conjecture is reasonable but does not retroactively make the current contribution broad.
- **The detection statistics use null distributions whose validity is not checked.** Initials ICW (§4.2.2) estimates γ from the Canterbury Corpus (Shakespeare, Bible, Lewis Carroll), then tests AI-written peer reviews against that null. AI-written ICLR reviews are unlikely to share the Canterbury initial-letter distribution, so the reported AUC partly reflects domain shift, not watermark signal. Acrostics ICW (§4.2.4) estimates μ and σ by resampling sentence-initial subsequences from the suspect text *itself* — the paper does not justify why a self-resampled null is statistically valid for the hypothesis being tested.

### Minor
- **Robustness is evaluated only against content-blind attacks** (deletion, synonym replacement, paraphrase). The actual adversary — a reviewer who can read their own review — is content-aware and can break Acrostics or Initials with one rewrite. The paper acknowledges spoofing in a sentence (§4.2.2) and defers adversary analysis (§3.2), which is reasonable scoping, but the only motivating application is adversarial.
- **No IPI baseline is included.** PostMark and YCZ+23 are inapplicable in IPI (the paper explains this correctly in §5.1), but the IPI columns of Table 2 still have nothing to compare against — even a trivial canary ("include `pineapple` in your response") would give the numbers a reference point.
- **Lexical ICW is in essence Kirchenbauer's green/red list reformulated as a prompt** (§4.2.3); the discussion correctly notes the LLM struggles with large green vocabularies, which is exactly the regime where the logit-bias approach succeeds. Framing this as a *limitation revealed by* the comparison would be more honest than presenting Lexical as a new mechanism.

### Trivial
- The IPI text occasionally conflates "watermark" (signal placed by the content producer) with "tripwire" (evidence that the input contained a hidden instruction). The distinction would be cleaner if stated explicitly.

## Nice-to-Haves
- A short qualitative figure showing one full Acrostics review and one full Initials review verbatim, so readers can judge naturalness.
- An in-domain empirical γ on unwatermarked AI-written reviews (replacing the Canterbury γ) for Initials.
- A small-scale extractor-pipeline test: feed the white-text-stamped PDF through 3–5 common pipelines and report payload survival rate.
- A human-readability study with a handful of editors, comparing watermarked and unwatermarked reviews.
- A brief ethics-statement passage on organizer-side prompt injection as a deployment practice.

## Removed Points
*These points are flagged to be removed; treat them with caution.*
- *"The IPI scenario depends on a fragile delivery channel that any modestly motivated reviewer can neutralize."* — The paper explicitly scopes detailed attack/defense study as future work in §3.2 and includes an "ignore prior prompts" sanity check in Appendix D. Demoted: kept the passive-failure variant in Major (extractor dropping the payload, which does not require an adversary), removed the active-attack framing.
- *"What is being detected in IPI is not a watermark in the traditional sense but a prompt-injection tripwire."* — Interesting framing point but not a flaw of the paper as written; the paper plainly labels the setting "Indirect Prompt Injection" and contrasts it with prior watermarking. Kept only as a Trivial clarity point.
- *"Organizer-side prompt injection invites broader misuse and the ethics statement does not engage."* — Reasonable nice-to-have but outside the paper's stated scope; demoted from a Major criticism to a Nice-to-Have.
- *Strength Finder claim that text quality is "comparable to unwatermarked LLM output"* — Conflicts with the Major weakness about saturated LLM-as-judge (4.982/5.000/4.994 ceiling). Dropped as a standalone strength.

## Novel Insights
None beyond the paper's own contributions. The clearest novel observation already lives in the paper: that ICW effectiveness is essentially a function of instruction-following capability, so today's "narrow and brittle" demonstration may broaden as models improve. Authors should lean into this conclusion rather than around it.

## Suggestions
- Replace the Canterbury γ with an empirical γ measured on unwatermarked AI-written reviews from the same model/prompt pipeline, and re-report T@1%F and T@10%F.
- Add a small adversary-aware IPI table: PDF passed through 3–5 common extractors (PyPDF2, pdfminer, OCR, the Claude/GPT file-upload paths), reporting payload survival rate before any "smart" adversary is introduced.
- Include at least one verbatim full Acrostics and one full Initials watermarked review in the body so readers can judge covertness directly.
- Replace (or augment) the LLM-as-judge with a small human-judgment study of, say, 10 editors over 20 reviews, asking only "does anything look anomalous?"
- Calibrate the language in §6 to acknowledge that the contribution today is narrow (one model tier, cooperative adversary, fragile channel) — the result is still interesting at that scope, and the honesty would strengthen rather than weaken the paper.

## Axis-by-axis assessment
- **Originality:** High. Reframing watermarking as a black-box, prompt-only operation, and pairing it with an IPI peer-review case study, is genuinely novel.
- **Importance of research question:** High. Detecting LLM use in peer review without provider cooperation is a real, urgent problem with no current solution.
- **Whether the claims are well supported:** Mixed. The detection AUC numbers are real for one model tier and one (cooperative) adversary model; the broader claims of practicality, covertness, and IPI deployability rest on assumptions the paper does not test.
- **Soundness of experiments:** Mixed. Detection setup is reasonable but the null-distribution choices for Initials and Acrostics are questionable, and the quality metric is saturated.
- **Clarity of writing:** Good. The four schemes and Table 1 trade-off summary make the contribution easy to read.
- **Value to the research community:** Worth a community read for the framing; the specific instantiations are mostly known building blocks repurposed as instructions, so the lasting contribution is the paradigm more than any one scheme.

## Score and Decision

The paper introduces a genuinely new paradigm and supplies non-trivial empirical results, but the load-bearing IPI scenario rests on unverified delivery assumptions, the covertness claim is not checked with humans, the null distributions for two of four detectors are questionable, and three of the four schemes work only on a single frontier model under a cooperative adversary. Against the round-2 anchors, this sits clearly above NvSwR4IvLO (4.67, reject) — its framing is more novel — but clearly below 6p8lpe4MNf (5.50, accept), which has a cleaner technical contribution and a more carefully justified evaluation. That places it at 5.0.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>
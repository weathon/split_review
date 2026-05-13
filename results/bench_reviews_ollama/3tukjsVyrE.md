Now I have a thorough understanding of the paper. Let me synthesize the final review.

## Summary

This paper proposes scaling speech-text pre-training by synthesizing interleaved speech-text data from text corpora via a "text-to-token" model that directly converts text to discrete speech tokens, bypassing the need for actual speech synthesis. Combined with a supervised 12.5Hz single-codebook speech tokenizer (derived from Whisper), they generate 600B tokens of synthetic interleaved data and pre-train a 9B SpeechLM on 1T total tokens, achieving substantial gains on spoken QA (13%→31%) and speech language modeling benchmarks over prior work, while using only 1/10 of Moshi's speech data.

## Strengths

- **Synthetic interleaved data method is a genuine and well-validated contribution.** The core idea—generating speech tokens directly from text via a learned text-to-token model rather than running TTS—is both elegant and scalable. The within-model ablation (Table 4/Section 4.3.1) showing consistent improvement from 0→100B→200B→600B interleaved tokens on Spoken QA (e.g., Web Questions S: 15.3%→23.1%→26.7%→31.0%) directly validates the method independent of base model choice.

- **Efficient and practical pipeline design.** The 25k tokens/sec generation speed on a single H800 (Section 2.2) and the span-corruption approach with configurable ratio η make billion-scale interleaved data generation tractable. The supervised 12.5Hz tokenizer with streaming support (block causal attention, causal convolutions) matching bidirectional ASR performance (Section 2.1) is a practical engineering contribution.

- **Comprehensive ablations on key design choices.** The frame rate ablation (6.25–50Hz), span corruption ratio (η=0.2–0.4), and data composition ablation all provide useful guidance. The finding that interleaved data consistently helps while other data types show capacity competition in smaller models (Section 4.3.1) is informative.

- **Strong results with far less speech data.** Achieving SOTA on Spoken QA with 700K hours vs. Moshi's 7M hours of natural speech demonstrates the value of leveraging text corpora for speech-text alignment.

## Weaknesses

### Fatal
None.

### Major

- **The headline SOTA claim (13%→31%) conflates base model quality with the method's contribution.** The 9B model (GLM-4-9B-Base) is compared against Moshi (7B, different architecture/data), TWIST (OPT-based), and Spirit-LM, which use different and potentially weaker base LLMs. While the 0→600B interleaved data ablation genuinely validates the method within the same architecture, the *absolute* 31% figure cannot be cleanly attributed to the synthetic data method alone without a text-only GLM-4-9B baseline on the same QA tasks to establish how much the base LLM already knows. The paper does note Moshi uses 10× more natural speech data, which contextualizes the comparison, but the framing in the abstract and introduction still implies the method alone drives the improvement. This does not invalidate the method but does overclaim relative to the evidence.

- **The text-to-token model's error rate on the actual pre-training data is unquantified.** The paper reports WER=3.20 on VCTK (clean read speech) for the text-to-token model but states only that "the WER for speech spans generated from the text pre-training data was higher" (Section 2.2), without providing the number. Since 600B synthetic tokens are the central data contribution and FineWeb-Edu contains content (code, math, tables) that is difficult to pronounce, quantifying this noise is important for assessing data quality. The fact that scaling interleaved data still improves results suggests this noise is tolerable, but reporting the number is essential for reproducibility and transparency.

### Minor

- **The abstract's "eliminating the need for parallel speech-text datasets" claim is slightly overbroad.** While correct for constructing *interleaved* data (Spirit-LM's bottleneck), the training pipeline still uses supervised ASR/TTS data as one of four data types (Section 2.3). The 1.5B ablation shows removing this supervised data actually *improves* performance, suggesting it may not be needed—consistent with the abstract's spirit—but the 9B model retains it. The claim is narrowly defensible but could mislead readers into thinking no parallel data is used at all.

- **Chatbot evaluation relies on GPT-4 scoring of transcribed speech without human evaluation.** For a system claimed as an "end-to-end spoken chatbot," GPT-4 scoring of transcribed text misses prosody, pacing, and naturalness. UTMOS and ASR-WER partially address speech quality, but human ratings of conversational speech quality would strengthen the chatbot claim. This is a common limitation in the field.

### Trivial
None.

## Nice-to-Haves

- A text-only GLM-4-9B-Base baseline on the Spoken QA tasks (with questions provided as text), to decompose how much improvement comes from base model knowledge vs. speech-text alignment.
- Reporting the specific WER of the text-to-token model on pre-training text spans (ideally stratified by content type), and testing robustness via filtered vs. unfiltered spans.
- Human evaluation of the spoken chatbot on speech-specific qualities (prosody, naturalness, conversational flow).

## Removed Points

- **Harsh Critic's claim about unfair baseline comparison as a disqualifying structural issue.** The reviewer frames this as if the paper is hiding confounds, but the paper openly lists baseline architectures, notes Moshi uses 10× more speech data, and provides the 0→600B within-model ablation that isolates the method's effect. The concern about attribution is real (kept as Major above), but the comparison is standard practice in the field and not "unfair"—these are published SOTA baselines.

- **Harsh Critic's concern about 9B ablation removing supervised data.** The authors provide a reasonable explanation (capacity competition in smaller models, alleviated in larger ones). Testing this at 9B would be informative but is not a methodological flaw—their explanation is plausible.

- **Harsh Critic's complaint about the 3-second wait for Moshi evaluation.** This is a standard protocol choice clearly documented in the paper; Moshi requires a greeting, and the wait accommodates this. Not a methodological flaw.

- **Harsh Critic's claim about the abstract being misleading about data usage ("not a purely synthetic approach").** The abstract specifically says "synthetic interleaved data derived from text corpora, eliminating the need for parallel speech-text datasets"—this is about the *interleaved data construction*, not claiming the entire approach needs no speech data. The unsupervised speech data (700K hours) is clearly described.

- **Strength Finder's claim about "large improvement over prior SOTA" as a standalone strength.** This is partially absorbed into the method validation but partially overclaimed given the base model confound (addressed in Major weakness above).

- **Strength Finder's generic claim about "efficient text-to-token pipeline."** While true, this is a design choice, not a separate strength—the scalability is the validated claim.

## Novel Insights

The most notable insight from the paper is the reversal of the traditional data-scaling paradigm for SpeechLMs: rather than collecting more natural speech (Moshi's 7M hours), the authors leverage the vast text corpora already available for LLMs by converting text to speech tokens directly. The finding that synthetic, potentially noisy (higher WER) interleaved data still yields monotonic performance gains as it scales (0→600B) suggests the alignment signal from interleaving is highly robust to token-level noise—a somewhat surprising result that supports the practical viability of this approach even with imperfect text-to-token models.

## Suggestions

- Add a text-only GLM-4-9B-Base baseline on Spoken QA (reading questions as text, answering in text) to decompose the contribution of interleaved pre-training vs. base LLM capability. This single experiment would substantially strengthen the attribution claims.
- Report the actual WER number for the text-to-token model on FineWeb-Edu text, even if just as a single aggregate number in the main text, to quantify the noise in the 600B tokens.
- Qualify the SOTA comparison in the abstract and introduction more explicitly (e.g., "with a stronger base LLM and 10× less natural speech data"), reserving the method-specific attribution for the ablation results.

**Evaluation on key axes:**
- **Originality:** High. The text-to-token approach for synthetic interleaved data is novel and addresses a real scalability bottleneck.
- **Importance of research question:** High. Scaling SpeechLMs with limited speech data is an important open problem.
- **Claims well supported:** Partially. The within-model ablation is strong, but the absolute SOTA claim conflates base model and method contributions.
- **Soundness of experiments:** Good. Ablations are thorough, but the missing text-to-token WER on pre-training data and lack of textual baseline for decomposing contributions are gaps.
- **Clarity:** Good. The paper is well-organized and the method is clearly described.
- **Value to research community:** High. The approach opens a practical direction for scaling speech-text alignment with text data.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>
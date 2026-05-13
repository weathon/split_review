## Summary
MMBench is a bilingual (EN/CN) multiple-choice VLM benchmark of 3,217 questions across a 3-level taxonomy with 20 leaf abilities, paired with two methodological contributions: a stricter "CircularEval" protocol (a question counts as solved only if the VLM is correct under all N circular shifts of choices) and an LLM-based choice extractor (GPT-4, 91.5% human alignment) for handling free-form outputs. Over 20 open-source and proprietary VLMs are evaluated, with fine-grained per-ability and EN/CN comparisons.

## Strengths
- **Granular, balanced taxonomy.** The 3-level / 20 leaf-ability structure with ≥125 questions per L-3 leaf (Sec. 3.3, Fig. 1) is more fine-grained than VQAv2/MME/SEEDBench and enables per-capability diagnosis rather than a single aggregate score.
- **LLM-extractor pipeline is empirically validated.** Sec. 4.1/Fig. 4 measures 91.5% human alignment for GPT-4 and Table 1 quantifies the accuracy gains attributable to extraction (e.g., +23.2% for VisualGLM-6B, +15.0% for Qwen-VL-Plus). This is the right kind of due diligence for an LLM-as-judge pipeline.
- **CircularEval meaningfully separates models.** Table 2 shows the protocol exposes large gaps that VanillaEval hides (e.g., OpenFlamingo v2 36.7% → 2.6%; LLaVA-v1.5-13B vs 7B gap widens from 2.1% to 4.7%), and Fig. 3 documents a real prediction-choice skew motivating it.
- **Bilingual EN/CN parallel design.** Translating questions/choices while holding the image fixed (Sec. 3.2, Sec. 5.3) enables a controlled cross-language comparison rare in VLM benchmarks, and uncovers that top models close the EN-CN gap to <2%.
- **Concrete falsifiable empirical claim.** The fine-grained comparison (Fig. API_cmp) localizing proprietary VLMs' advantage to structuralized image-text understanding and external-knowledge tasks—but not generic perception/reasoning—is specific and useful for the community.

## Weaknesses

### Fatal
None.

### Major
- **Circular dependency between filter committee and leaderboard.** Sec. 3.2 filters "wrong" questions by flagging items that *all* of a 5-VLM committee (GPT-4v, Gemini-Pro-V, Qwen-VL-Max, InternLM-XComposer2, LLaVA-v1.5-13B) fail, and then manually verifying/removing those. Those same five models are reported as the top performers in Table 2. Items that genuinely test capabilities none of these models possess are disproportionately routed into manual review and either rewritten or discarded, while items that one or two of them happen to get right are kept untouched. The paper does not report what fraction of "all-VLM-failure" items were kept vs. discarded, nor cross-validate the filter using a held-out model set. The headline ranking therefore cannot be cleanly separated from "agreement with the filter committee." A disjoint filter/evaluation split would defuse this; without it, the strongest claim ("objective" evaluation) is overstated.
- **CircularEval's claim to measure positional-bias robustness is not isolated from generic stochasticity.** Sec. 4.3 motivates CircularEval partly with Fig. 3's choice-distribution skew, but the Table 2 drops conflate three distinct sources: (a) positional bias, (b) per-pass stochasticity / partial competence, and (c) the simple fact that requiring N correct independent passes is a harder threshold (a uniformly random 4-way model drops from 25% to ~0.4%). Without a control that holds marginal-correct rate fixed while varying only choice order (e.g., N independent Vanilla samples with the *same* order vs. shuffled order), it is hard to claim the protocol specifically measures positional robustness rather than "stricter scoring." The drops are still informative for discriminability, but the mechanistic framing outruns the experiment.

### Minor
- **Same-family extractor/evaluatee concern not addressed.** The 91.5% extractor-vs-human number is an aggregate; the ablation across alternative extractors (GPT-3.5, InternLM2) does not specifically test whether GPT-4 is more charitable to GPT-4v phrasing than to, e.g., MiniGPT4 phrasing. A per-model alignment-rate breakdown would settle this and is cheap to produce.
- **No variance/CI on the headline table.** Several Table 2 rankings (LLaVA-v1.5-7B 63.4 / mPLUG-Owl2 63.5 / CogVLM-Chat-17B 63.6) are within plausible run-to-run noise; without seeds or confidence intervals, fine-grained rankings should not be over-interpreted.
- **"LLM plays a vital role" comparison conflates factors.** Sec. 5.2 cites switching LLaVA-v1.5-7B/13B → LLaVA-InternLM2-20B as evidence the LLM matters, but this confounds LLM scale, LLM family/lineage, and training data. The Vicuna 7B↔13B intra-family comparison in the same paragraph is the cleaner evidence; the cross-family claim should be hedged.
- **Bilingual asymmetry not flagged.** MMBench-CN translates the question/choice text but the images (including in-image English text) are unchanged, so it tests Chinese question-understanding, not Chinese OCR or Chinese-grounded imagery. The conclusion "VLMs have weaker Chinese bilingual capability" is therefore supported only on the language-of-question axis. Worth stating explicitly.
- **Taxonomy operationalization not measured.** The 20 L-3 leaf abilities are defined verbally (Appendix). No inter-annotator agreement is reported on which leaf a given question belongs to, so "20 fine-grained skills" is a labeling claim rather than a measured one.

### Trivial
- Content-moderation analysis (Table 3) with rejection rates of 0.1–1.8% is unlikely to alter rankings; the "upper bound" framing is more confirmatory than diagnostic.

## Nice-to-Haves
- Held-out filter validation: filter with models {A, B, C}, evaluate {D, E, F}, compare ranking stability.
- Image-overlap / contamination check against LAION/CC/COCO for the 80% web-sourced subset.
- Position-bias-only ablation: N independent Vanilla runs with fixed order vs. circularly shifted order, to isolate positional bias from generic stochasticity.
- Per-model and per-ability breakdown of the 91.5% extractor alignment.
- Release of sample-level filter discard statistics.

## Removed Points
*These points are flagged to be removed, treat them with caution.*

- (Harsh Critic) "More than 80% of questions from the Internet — no contamination check against pretraining corpora." Kept in Nice-to-Haves rather than as a weakness: this is a standard limitation of essentially all VLM benchmarks and is not unique to this work.
- (Harsh Critic) "Reproducibility/release status" framing on training/filter logs: nitpick on disclosure rather than substance.
- (Strength Finder) "The benchmark contains 3,217 carefully collected MCQs with at least 125 per L-3 ability" — kept but folded into the taxonomy strength; redundant as a standalone bullet.
- (Strength Finder) "Systematic data quality control reinforces reliability" — partially conflicts with the verified Major weakness about filter circularity; the weakness wins, so the framing here is too rosy.

## Novel Insights
None beyond the paper's own contributions. The most interesting empirical observation — that proprietary VLMs' lead is concentrated in structuralized image-text understanding and external-knowledge abilities, but not in generic perception/reasoning — is the paper's own.

## Suggestions
- Add a disjoint-set filter validation: re-run the "all-VLM-failure" filter with a held-out committee and report ranking stability vs. the current Table 2.
- Add an ablation that fixes the model's marginal-correct rate and varies only choice order, to isolate positional bias from harder-threshold effects in CircularEval.
- Report per-model alignment of the GPT-4 extractor (especially for GPT-4v outputs vs. open-source outputs) to rule out same-family bias.
- Report variance or at least two-run agreement on Table 2 for close rankings.
- Soften "LLM plays a vital role" cross-family claim or replace with the cleaner intra-family Vicuna 7B/13B evidence.
- Explicitly state that MMBench-CN tests Chinese question-language only, not Chinese-grounded image content.

---

**Axis assessment.** *Originality:* moderate — CircularEval and the LLM-extractor validation are concrete methodological contributions, even if not radical. *Importance:* high — the community needs fine-grained, automated VLM evaluation and MMBench is in active use. *Claim support:* mixed — the leaderboard and bilingual comparison are well supported, but the "objective" and "robust" headline claims outrun the experiments due to filter circularity and the under-isolated CircularEval mechanism. *Soundness:* generally solid engineering; the major concern is methodological framing more than execution. *Clarity:* good; the pipeline is described in enough detail to reproduce. *Value:* high — a useful diagnostic instrument with non-trivial limitations the authors should acknowledge.

## Score and Decision
The paper makes real, usable contributions and the issues raised are methodological framing problems rather than invalidating flaws.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>
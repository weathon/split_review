## Summary
The paper identifies that low-bit (4-bit) quantization of LLMs that have been "unlearned" can restore the supposedly forgotten knowledge — retention jumps from ~21% to ~83% on average across utility-preserving unlearning methods on MUSE (NEWS/BOOKS). The authors offer a quantization-bin-geometry argument for why this happens and propose SURE, a saliency-masked unlearning method with a larger learning rate that updates only modules with the largest forget-loss gradients, mitigating the recovery while preserving utility.

## Strengths
- **Clear, reproducible empirical phenomenon.** Table 1's combinatorial sweep over {GA, NPO} × {none, GDR, KLR} shows a consistent jump in forget-set knowledge retention after 4-bit RTN quantization (e.g., GA_KLR/BOOKS: 13% → 89%). The effect direction is uniform across the utility-preserving methods.
- **Generality across quantizers.** Table 2 shows GPTQ and AWQ (calibration-based) produce similar recovery as RTN, so the failure is not an artifact of one quantization scheme.
- **Precision-dependence aligned with the proposed mechanism.** 8-bit quantization does not exhibit the same recovery, consistent with the Δ_int8 ≪ Δ_int4 argument in Section 5.
- **Concrete remedy with multi-faceted utility evaluation.** SURE is evaluated not only on retain-set memorization but on MMLU, TruthfulQA, TriviaQA, and fluency (Table 3), giving a broader view of utility cost than typical unlearning papers.
- **Clean conceptual takeaway.** The paper articulates a real three-way tension: utility preservation → small weight changes → quantization-invariance, which is a useful framing for the unlearning community.

## Weaknesses

### Fatal
None.

### Major
- **The proposed mechanism is never directly measured.** Section 5's central claim is Q(f_unlearn) ≈ Q(f_target) because |Δw| < Δ_quant for most weights. The paper never reports per-weight (or per-layer) histograms of |Δw|/Δ_quant, nor the fraction of weights crossing a bin boundary before vs. after SURE. This is the experiment that would convert the plausibility argument into evidence — and it is trivial to run from the same checkpoints used in Section 4. Without it, the explanation is a geometric narrative consistent with the data, not a verified mechanism.
- **Breadth of the "catastrophic failure" claim is thin relative to the rhetoric.** All Section 4 results are on MUSE (NEWS and BOOKS); the Section 4.3 sentence about RWKU as "further evidence" is cut off mid-sentence in the parsed body. The base-model description (Section 4.1, "Retrained and Target Models") is a single footnote line, suggesting a single model family. A sweeping claim about "existing unlearning methods for LLMs" and a push to redefine benchmarks would benefit from at least one additional model and benchmark (TOFU/RWKU) carried through the same sweep.
- **SURE's main results are on a single dataset with no quantization-aware baseline.** Table 3 reports SURE only on BOOKS; the hyperparameter analysis (Table 4) is on NEWS. No comparison is made to obvious alternatives such as a weight-distance regularizer (penalizing ‖θ − θ_target‖ being smaller than Δ_quant) or quantizing during the unlearning loop. As stated, SURE is shown to beat "no SURE," not shown to be the right design choice within the space of quantization-robust unlearning.

### Minor
- **SURE's two mechanisms (large LR vs. module saliency mask) are not separated.** The paper motivates both jointly but never ablates them; it is unclear how much robustness comes from each.
- **Precision spectrum is dichotomized.** Only 4-bit and 8-bit are reported; given that 3-bit deployment is increasingly common, characterizing the recovery curve across bit-widths (3, 4, 5, 6, 8) would substantially strengthen the precision story.
- **Hyperparameter selection criterion under-specified.** Grid over LR, α, γ is reported but the criterion for picking the "best" config is not stated; with three hyperparameters and a single evaluation suite, there is some risk of selection on the target metric.
- **Section 4.4's interpretation of GPTQ/AWQ is muddled.** The paper argues GPTQ/AWQ fail because their calibration data is general rather than forget-aligned; if anything, forget-aligned calibration would be expected to make recovery worse for the defender, not better. The argument as written does not cleanly support the empirical finding.
- **MIA strength.** PrivLeak (Min-K%) is a relatively weak MIA; the privacy half of the threat-model story would be more convincing with a reference-model-calibrated MIA, especially on the quantized model.
- **Headline 21% → 83% averaging.** The exclusion of GA from the average (because utility collapses) is defensible but should be stated where the numbers first appear, not inferred from Table 1.

### Trivial
- A concrete qualitative example (a Harry Potter passage refused at full precision, then completed verbatim post-quantization) would make the practical threat vivid and is conspicuously absent.

## Nice-to-Haves
- Bin-crossing diagnostics: report, per method, the fraction of weights with |Δw| > Δ_int4 and > Δ_int8, and how SURE shifts this distribution.
- An ablation isolating "large LR alone" vs. "saliency mask alone" vs. SURE (both together).
- One additional base model (e.g., a Llama-2/3 variant of different size, or a Mistral-class model) carried through Table 1's sweep.
- A simple weight-distance-regularized unlearning baseline as a comparator for SURE.

## Removed Points
*These points are flagged to be removed; treat them with caution.*

- "Recovery is a near-tautological consequence of small weight updates, so the 'catastrophic failure' framing is hype." — The paper actually acknowledges this tension explicitly in Section 6.1 (objectives ii vs. iii). Whether the framing is "surprising" is editorial; the empirical contribution stands.
- "Comparing unlearning LRs to pretraining LRs is leading; fine-tuning LRs are also ~1e-5." — A fair editorial point but not a substantive flaw; the paper's argument hinges on weight-change magnitude, which is verifiable directly (see Major #1) regardless of how the LRs are framed.
- "Per-channel/per-group quantization gives smaller Δ and the paper doesn't address grouping." — Section 5 explicitly uses the per-block formulation from Equation 2 and the empirical results in Table 2 already include GPTQ/AWQ (group-wise); not a structural omission.
- Strength Finder's "addresses an important problem" / generic importance framings — dropped as non-specific.

## Novel Insights
None beyond the paper's own contributions. The genuinely useful observation — that utility-preserving unlearning produces sub-Δ weight updates which 4-bit quantization collapses back into the target's bins — is the paper's own.

## Suggestions
- Add a histogram (per layer or aggregated) of |w_unlearn − w_target| in units of Δ_int4 and Δ_int8, for each method, before and after SURE. This single figure would convert Section 5 from argument to evidence.
- Repeat Table 1 on at least one additional base model and on TOFU or RWKU end-to-end.
- Ablate SURE: (a) large LR only, (b) saliency mask only, (c) both; on both BOOKS and NEWS.
- Add a weight-distance-regularized unlearning baseline (penalize ‖θ − θ_target‖ < Δ_int4) as a comparator.
- Extend precision sweep to 3-bit; report the recovery-vs-bitwidth curve.
- Strengthen the privacy analysis with a reference-model MIA on the quantized model.
- Fix the truncated RWKU sentence in §4.3 and surface the base model / retrained model details in the main text.

---

**Axis evaluation.** *Originality:* moderately high — the quantization-as-knowledge-recovery framing is, to my knowledge of the paper's own positioning, new and well-motivated. *Importance:* high — low-bit deployment is standard and unlearning is a deployment-relevant problem. *Claim support:* mixed — the headline empirical claim is well-supported within MUSE, but the mechanistic claim and the "catastrophic failure of LLM unlearning" generality are oversold relative to the evidence. *Experimental soundness:* adequate but narrow — one benchmark family, one model family, SURE on one dataset, no quantization-aware baseline. *Clarity:* generally clear; Section 4.4's reasoning is muddled and §4.3 is truncated. *Value to community:* high — the phenomenon is important and the SURE direction is a reasonable starting point, even if not yet validated as the best response.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>
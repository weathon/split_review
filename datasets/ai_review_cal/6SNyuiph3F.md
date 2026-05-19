- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 6, 5, 5
Now I have thoroughly verified the paper content against the reviewer claims. Let me produce the final consolidated review.

## Summary

The paper proposes "chat vector" — the parameter difference between LLaMA2 and LLaMA2-chat (τ = θ_chat − θ_PLM) — and shows that adding this vector to a continually pre-trained (CP) model for a new language (Traditional Chinese, Korean, Simplified Chinese) improves instruction-following, reduces toxicity, and provides safety benefits. The authors frame this as restructuring the conventional CP→SFT→RLHF pipeline into CP + chat vector, claiming computational efficiency and that the resultant model "responds precisely in the target language."

## Strengths

- **Methodological simplicity and computational efficiency.** The chat vector is a single vector addition in parameter space (τ = θ_chat − θ_PLM, θ_new = θ_CP + τ). This is trivially cheap compared to even a single stage of the standard pipeline. The paper operationalizes the task-vector concept (Ilharco et al., 2023) for cross-lingual chat alignment, which is a practically useful extension.

- **Consistent cross-lingual improvement over CP+FT baselines.** Table 1 shows that adding the chat vector improves Vicuna scores across all three language settings: e.g., Korean LLaMA from 5.88 (FT only) to 6.97 (FT + chat vector), Chinese-LLaMA from 5.75 to 6.73. This is evidence that the approach generalizes beyond a single language.

- **Clear toxicity and safety improvements.** Table 2 shows that for Traditional Chinese LLaMA, CP+chat vector reduces toxicity from 10.99% (CP only) to 2.38%. Table 3 shows substantial reductions in unsafe rates across categories (e.g., Crimes & Illegal Activities from 72.0% to 9.5% for CP+chat vector). These are practically meaningful gains.

## Weaknesses

### Fatal
None.

### Major

- **Central claim is overclaimed and untested.** The paper repeatedly frames the chat vector as an alternative to the full RLHF pipeline ("restructuring the conventional training paradigm from CP → SFT → RLHF to CP + chat vector," abstract and introduction). Yet no experiment compares against a model that underwent RLHF for the target language. All baselines use only CP and FT (supervised fine-tuning). The closest comparison — llama2-chat → CP → FT — starts from an English RLHF model and then does CP+FT, which is not the same as doing CP→FT→RLHF in the target language. The observed improvements show that chat vector boosts CP+FT performance, but whether it "replaces" RLHF as an alignment method is never tested. This is a gap between framing and evidence.

- **Language-id drift on Chinese-LLaMA directly contradicts a stated contribution.** Contribution bullet 2 claims: "We find that the resultant model responds precisely in the target language, both in providing answers and declining inappropriate requests." However, Table 4 shows that adding the chat vector to Chinese-LLaMA produces 91% English responses on the Vicuna benchmark and 46% on Safety Prompts. Even with 0.5 scaling, English remains dominant (82% and 37%). This is a significant failure for a method whose contribution is precise target-language response. The paper acknowledges this only in Section 5.5 ("requires further research") without qualifying the contribution claim.

- **Language detection for Korean LLaMA is entirely missing.** Table 4 reports language proportions only for Chinese-LLaMA. The Korean LLaMA experiments are reported in Table 1 without any language-detection check. Whether the same English-drift failure occurs for Korean is completely unknown, which is a critical gap given that the Chinese-LLaMA results show the problem exists for at least one setting.

- **Inconsistent model sizes across languages weaken cross-lingual claims.** The Korean experiments use 7B parameters while the Chinese experiments use 13B. The paper's contribution bullets claim "versatility" across languages, but performance differences could be driven by model scale rather than language.

### Minor

- **Multi-turn dialogue evidence is anecdotal.** Only a single case study (Figure 2) is provided to support the claim that the chat vector enables multi-turn conversation. The paper's fine-tuning data contains only single-turn pairs, so any claim about multi-turn ability requires systematic evaluation (e.g., a translated multi-turn benchmark, or human evaluation of multiple examples).

- **GPT-4 evaluation circularity is not addressed.** GPT-4 generates both the reference answers (scored a perfect 10) and evaluates model outputs. The paper uses GPT-4 as scorer without discussing known biases (LLM-as-judge favoring outputs that resemble the judge's own style). Since the chat vector is derived from LLaMA2-chat which was partially guided by GPT-4 outputs (through RLHF), this could produce a confound.

- **No uncertainty estimates.** All tables report single-point scores without variance, confidence intervals, or multiple seeds. Given variability in LLM outputs and GPT-4 judging, robustness is unclear.

- **Translation quality of evaluation datasets is not checked.** Vicuna and Real Toxicity Prompts are translated via GPT-4, and the Chinese prompts in Real Toxicity Prompts are truncated at the second comma via an ad-hoc heuristic. Neither procedure is validated.

- **No computational cost comparison provided.** The paper repeatedly invokes "efficiency" (introduction, conclusion) but provides no GPU-hour, FLOP, or wall-time comparison against any alternative.

### Trivial

- Language detection uses "Lingua2" for the Vicuna benchmark but the paper does not report its accuracy for the target languages.

## Nice-to-Haves

- An analysis of what the chat vector encodes (e.g., per-layer contribution, probing experiments) would strengthen the paper's scientific contribution beyond the empirical demonstration.
- An ablation on the source of the chat vector (e.g., from a different base model or a different chat model) would test generality.
- A multi-turn quantitative benchmark (e.g., translated MT-Bench) would substantiate the multi-turn claim.

## Removed Points

- **"Chat vector smuggles RLHF through the back door"** — The paper explicitly states in Section 3.2 that LLaMA2-chat "undergoes instruction tuning and reinforcement learning with human feedback (RLHF)." The claim is about not needing to *re-implement* RLHF for each target language, not about RLHF never being done. The paper is transparent about this, and the criticism does not identify an error or omission.
- **"No analysis of why chat vector works"** — The paper is an empirical demonstration; theoretical analysis is not required for the claims made. Requesting it is scope creep.
- **Generic evaluation-rigor criticisms** (e.g., "the evaluation lacks rigor" without specific anchors in the paper) — filtered per discipline rules.
- **Missing appendix content** — Parser artifacts, not author omissions.

## Novel Insights

None beyond the paper's own contributions. The reviewer materials surface a clear tension: the paper demonstrates a method that works well for improving CP+FT models, but the claims about replacing RLHF are unsupported by the experiments, and the language-drift failure on Chinese-LLaMA works against the "precise target language" headline. The reviews do not uncover new scientific insight about why the chat vector works or when it fails.

## Suggestions

1. **Reframe the claims to match the evidence.** Drop or qualify the "replace RLHF" framing. The paper's real contribution — that chat vector improves cross-lingual chat capabilities over CP+FT baselines — is well-supported and does not need the overclaim. Say "chat vector as a cheap improvement over CP+FT" rather than "RLHF replacement."
2. **Check and report language detection for Korean LLaMA.** The language-drift issue on Chinese-LLaMA raises the strong possibility that Korean LLaMA also produces English outputs. Report this.
3. **Add an RLHF baseline if claiming RLHF replacement** — or, more practically, compare against a publicly available model that has undergone RLHF in the target language (e.g., a Chinese or Korean RLHF-aligned model if one exists).
4. **Qualify contribution bullet 2** to reflect that language precision holds for the main setup (Traditional Chinese LLaMA) but fails for Chinese-LLaMA, or analyze why the drift occurs and when it can be avoided.
5. **Include variance over multiple seeds or runs** for at least one key experiment.
6. **Provide concrete computational cost numbers** to substantiate the efficiency claim (GPU hours for CP vs. estimated cost of full RLHF pipeline).

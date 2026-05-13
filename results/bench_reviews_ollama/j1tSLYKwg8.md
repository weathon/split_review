## Summary
The paper proposes an adaptation recipe to convert pretrained autoregressive LMs (GPT-2 127M/355M, LLaMA-2 7B) into discrete diffusion language models via continual pretraining, using attention-mask annealing, a shift operation, and a time-embedding-free architecture. The authors release DiffuGPT and DiffuLLaMA checkpoints and evaluate on reading comprehension, commonsense, math, and infilling benchmarks, showing the adapted models outperform prior DLMs and are partially competitive with their AR base models.

## Strengths
- **Useful open artifacts at a new scale.** A 7B discrete-diffusion checkpoint adapted from LLaMA-2, plus 127M/355M variants, code, and eval toolkits, is a meaningful contribution to a subfield where models had been ≤1B (§4.1, contribution bullet 3).
- **Concrete and well-motivated shift-operation insight (§3.3).** AR-pretrained hidden states are aligned to the *next* token; naively applying a standard discrete-diffusion loss fights that alignment. Table 3 shows removing the shift drops GPT2-M+DD GSM8K-symbolic from 49.7 → 42.8.
- **Empirical case that DD > CD when adapting from an AR base (Table 3).** CD drops to 29.7, consistent with the paper's objective-unification argument in §3.2.
- **Broader evaluation than perplexity-only.** §4.2 explicitly criticizes perplexity-only evaluation of DLMs and assembles a multi-task benchmark, a useful step for the subfield.
- **Scaling trend evidence.** Loss curves (Fig. 2) and per-task numbers in Table 1 (e.g., Lambada 19.5 → 26.2 → 32.2 across 127M/355M/7B) show improvement with scale without saturation.

## Weaknesses

### Fatal
None. The release plus shift-operation finding is a real contribution; the issues below are framing/evidence problems rather than invalidating ones.

### Major
- **The "competitive with AR counterparts" framing is not supported for the 7B model.** The paper itself concedes "DiffuLLaMA's performance still falls short of the LLaMA2 model" (§4.3) and attributes this to insufficient training tokens, but provides no matched-compute AR control (LLaMA-2 7B continued-pretrained on the same 65B SlimPajama+Starcoder mix). Without that control, the "DiffuGPT outperforms GPT2" claim is also confounded with extra FineWeb pretraining. This is the most important missing experiment.
- **Infilling, the headline DLM-favorable result, uses an admittedly unfair AR baseline.** §4.3 explicitly notes "we do not provide the suffix information to the model, which might result in an unfair comparison." The infilling claim should be re-run against an FIM-trained AR baseline (sentinel-token FIM as in Bavarian et al., StarCoder, or CodeLlama) before being invoked in the abstract and contribution bullets.
- **Methodological recipe partially collapses under the authors' own ablation.** §4.5 reports "the mask annealing has minimal impact, so we choose to omit it for 7B adaptation," and the "time-embedding-free architecture" is essentially the absence of a component. The non-trivial methodological contribution reduces largely to the shift operation plus discrete-diffusion continual pretraining. The paper's three-part recipe framing overstates novelty.
- **Cross-family scoring asymmetry on multi-choice tasks.** §4.2 uses the per-token diffusion ELBO (Eq. L_T, with 1/t reweighting and mask indicator) to pick choices for DLMs, while AR models conventionally use length-normalized log-likelihood. These are not identical objectives; the paper does not show calibration across families or report the AR-style scoring for DiffuGPT. Multi-choice deltas of a few points could be scoring artifacts.

### Minor
- **Planning/self-correction motivation is not paid off.** §1 motivates DLMs via planning and self-correction limitations of AR (Bachmann et al., Xie et al., Huang et al.), but no experiment in §4 is a planning or self-correction benchmark; GSM8K-symbolic with task-specific fine-tuning is not a substitute.
- **ICL claim in §4.4 lacks AR baseline at the same prompting.** The zero-shot → few-shot improvement is read as evidence DiffuLLaMA can ICL, but LLaMA-2 7B numbers under the same prompting protocol are not placed beside DiffuLLaMA in Table 2's discussion.
- **Speed comparison setup under-specified (Fig. 4, §4.5).** §4.5 acknowledges AR uses KV-caching and is memory-bound but does not clearly specify the AR baseline configuration in the speed plot (KV cache on/off, precision, kernel). At T=256 with full bidirectional attention over 1024 tokens, "competitive" needs an apples-to-apples tokens/sec table at matched output quality.
- **Mask annealing's treatment is incoherent.** Table 3 ablates it as helpful for GPT-2; the 7B run omits it for engineering reasons and the text says it has "minimal impact." Either retain it and motivate it, or relegate it to an engineering note rather than a co-equal recipe ingredient.
- **Ablation scope (Table 3) is narrow.** GSM8K-symbolic alone is a thin surface for adaptation-recipe claims; at least one more task would strengthen generality of DD > CD on AR-initialized models.
- **Knowledge-loss explanation is unverified.** §4.3 attributes weak TriviaQA/PIQA to insufficient tokens for knowledge preservation; no probing of pre- vs post-adaptation factual recall is provided.

### Trivial
- The "unification" in §3.2 is acknowledged (line 119) to restate Austin et al. (2021)/Hoogeboom et al. (2022); it is framing, not a result, and could be presented as such to avoid overclaiming novelty in §3.

## Nice-to-Haves
- Side-by-side qualitative generations (DiffuLLaMA vs LLaMA-2-7B vs SEDD) at matched decoding budgets on CoT math and long-form text.
- Instruction tuning DiffuLLaMA (acknowledged as future work) would substantially firm up the ICL/CoT story.
- Sensitivity analysis of multi-choice accuracy to scoring rule (ELBO vs length-normalized LL or its diffusion analogue).
- A clean tokens/sec table at quality-matched generation with KV-cached, well-tuned AR baselines.

## Removed Points
These points are flagged to be removed; treat them with caution.
- *"GSM8K is reported after task-specific fine-tuning, so the comparison is about fine-tuning regime not the pretrained model."* — The paper is transparent that GSM8K is a fine-tuning setting (§4.2), and the fine-tuning protocol is identical across compared models; this is not a flaw.
- *Strength: "Thorough empirical demonstration that adapted DLMs are competitive with AR baselines."* — The 7B head-to-head is conceded to fall short of LLaMA-2; this overstates and conflicts with a verified Major weakness, so it is dropped per the strength-filter rule.

## Novel Insights
The genuinely useful observation in this work is the **shift-operation alignment**: AR-pretrained transformer outputs at position *i* are calibrated to predict token *i+1*, so when reusing AR weights as a diffusion denoiser, the loss must respect that off-by-one alignment rather than naively predicting the token at the masked position. The ablation cleanly substantiates it (49.7 → 42.8 on GSM8K-symbolic when removed) and the practical implication — *AR-to-diffusion adaptation is fundamentally a representation-realignment problem, not just an objective swap* — is the most transferable insight in the paper. Beyond that, the empirical finding that discrete diffusion adapts better from AR checkpoints than continuous diffusion (CD 29.7 vs DD 49.7 on GPT2-M) is a useful signal for future work choosing diffusion formulations for adaptation.

## Suggestions
- Add a matched-compute AR continual-pretraining control on the same 65B SlimPajama+Starcoder mixture; this is the single change that would convert the "competitive" framing from claim to result.
- Rerun infilling against an FIM-trained AR baseline (sentinel-token FIM or CodeLlama/StarCoder) and report both numbers.
- Report multi-choice accuracy under both diffusion-ELBO and length-normalized-LL scoring for at least DiffuGPT to defuse the protocol-asymmetry concern.
- Demote mask annealing in the framing (it didn't survive to 7B), and elevate the shift operation as the central methodological contribution.
- Either remove the planning/self-correction motivation from §1 or add a planning benchmark (e.g., Blocksworld, TravelPlanner) to support it.
- Replace the GPT2-large perplexity proxy in Fig. 3 with at least one supplementary human or LLM-judge evaluation of unconditional samples.

## Axis Assessment
- **Originality.** Moderate. The unification recap is not novel; the shift-operation insight and full-recipe adaptation to a 7B AR LLM are.
- **Importance of question.** High. Scaling DLMs from existing AR checkpoints is a practically valuable direction.
- **Claim support.** Uneven. Sub-claims about DLM > prior DLMs are well supported; "competitive with AR counterparts" at 7B and the infilling-superiority claim are not.
- **Soundness of experiments.** Partially sound; missing matched-compute control and fair FIM baseline are real gaps. Scoring asymmetry on multi-choice is a methodological concern.
- **Clarity.** Generally clear; the method section overstates the recipe's three-part structure relative to what survives ablation.
- **Value to community.** High as a resource paper: 7B DLM checkpoint plus code is a useful asset.

## Score and Decision
The paper has a real, transferable methodological insight (shift operation), a useful open 7B DLM artifact, and broader evaluation than prior DLM work. It is held back by the gap between framing and evidence at 7B, an admittedly unfair infilling baseline, and a recipe whose components partly disappear under the authors' own ablation. With reframing toward "useful DLM scaling recipe and open checkpoint" and one matched-compute control, this is solidly above the bar; as written, it sits just at it.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>
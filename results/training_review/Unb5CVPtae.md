Now I have all the information I need. Let me produce the final consolidated review.

## Summary

Time-LLM proposes reprogramming frozen large language models (e.g., Llama-7B) for time series forecasting by: (1) patching the input time series, (2) reprogramming patch embeddings via cross-attention over a learned set of text prototypes derived from the LLM's own word embedding space, and (3) prepending a Prompt-as-Prefix (PaP) containing dataset context, task instructions, and computed input statistics. The backbone LLM is kept entirely frozen; only a lightweight input transformation and output projection are trained (≈0.2% of total parameters). Experiments on long-term, short-term, few-shot, and zero-shot forecasting benchmarks are reported.

## Strengths

1. **Frozen-LLM reprogramming avoids expensive fine-tuning while maintaining strong performance.** Only ≈0.2% of total parameters (6.6M) are trainable. This is a genuine practical advantage over full or parameter-efficient fine-tuning approaches (e.g., GPT4TS, LoRA variants), and the ablation studies (B.1, B.2) confirm that both the reprogramming component and Prompt-as-Prefix contribute meaningfully to the final performance within the same backbone. *Evidence: Section 3, ablation results (lines 160, 175).*

2. **Prompt-as-Prefix (PaP) is a practical mechanism for injecting dataset context and input statistics without forcing the LLM to generate high-precision numeric tokens.** The paper identifies and ablates three components (dataset context, task instruction, input statistics), showing that removing PaP causes 8%+ degradation in standard settings and 19%+ in few-shot settings. The approach avoids the well-known issue of LLMs having poor numeric token generation precision. *Evidence: Section 4.5 ablation results (lines 160–161).*

3. **The core technical combination — patch reprogramming via cross-attention over text prototypes derived from the frozen LLM's embedding space — is novel.** Staying within the LLM's pre-trained token embedding space for the cross-attention keys/values is a principled design that distinguishes this work from approaches that directly edit inputs (Voice2Series) or fine-tune the backbone (GPT4TS, LLM4TS). *Evidence: Section 3 "Patch Reprogramming" (lines 70–79).*

4. **Competitive empirical results across multiple forecasting settings.** The method achieves strong performance against a broad set of baselines, particularly against non-LLM specialized models (TimesNet, DLinear) where the backbone-inequality objection does not apply. Performance in few-shot settings (5-20% improvements) is notable. *Evidence: Sections 4.1, 4.3.*

## Weaknesses

### Fatal
None.

### Major

1. **Uncontrolled backbone size invalidates the direct comparison with GPT4TS.** The paper uses Llama-7B as default backbone while GPT4TS (Zhou et al., 2023) uses a much smaller backbone (GPT-2). The headline claims of **12%** (long-term), **8.7%** (short-term), and **5–22%** (few-shot/zero-shot) improvements over GPT4TS are presented as evidence that *reprogramming beats fine-tuning*, but the comparison conflates method with backbone capacity. Without running GPT4TS (or a fine-tuning variant) with a Llama-7B backbone, or Time-LLM with a GPT-2 backbone, the reported gains cannot be attributed to the reprogramming methodology. The paper's own ablation (A.1–A.4) shows that Llama-7B outperforms its 1/4 variant by 14.5%, indicating that backbone scale alone produces large gains. *Evidence: Lines 110, 122, 157. The paper does not run this control.*

   **Why this matters:** It weakens the central quantitative claim that the proposed method is superior to fine-tuning approaches. The comparison with non-LLM baselines (TimesNet, DLinear, PatchTST) is less affected, but the most emphasized comparison (GPT4TS, called "particularly noteworthy") is confounded.

2. **Zero-shot evaluation is not genuinely cross-domain.** The zero-shot experiments (Section 4.4) train on one ETT dataset and test on another ETT dataset. All ETT datasets come from the same domain (electricity transformer temperature) and differ only in sampling frequency and station. This is a within-domain transfer test, not cross-domain. The paper explicitly calls this "cross-domain adaptation" (line 148), which overstates the generality of the result. A true cross-domain evaluation (e.g., ETT→Weather→Traffic) would be needed to support the claimed zero-shot generalization capability. *Evidence: Line 148: "evaluate on various cross-domain scenarios utilizing the ETT datasets."*

   **Why this matters:** It inflates the significance of the zero-shot results and sets an unrealistic expectation about the method's cross-domain transfer ability.

### Minor

3. **No variance or multiple-seed results reported.** The paper presents only single MSE/MAE values without error bars or standard deviations. While single-run evaluation is common practice in many time series forecasting benchmarks, the lack of any measure of dispersion is problematic for the few-shot and zero-shot experiments where higher variance is expected. The claimed improvements (e.g., 1.4% over PatchTST) could fall within noise. *Evidence: All result descriptions cite single values (lines 122, 131, 144, 151).*

4. **Ambiguity in the "text prototype" construction.** The paper states prototypes are obtained by "linearly probing E" (line 73) but does not clarify what this means — whether it is a learned linear projection, a selection of existing word embeddings, or a separate set of learnable vectors. The term "probing" in the representation learning literature typically implies a frozen feature extractor with a trained linear classifier, which does not match the usage here. This ambiguity harms reproducibility. *Evidence: Line 73: "maintain a small collection of text prototypes by linearly probing E."*

5. **Interpretability claims about text prototypes are anecdotal.** The paper claims learned prototypes map to words like "short up" and "steady down" (Figure 6) but provides only visual illustration without quantitative verification (e.g., nearest-neighbor analysis in the embedding space, human evaluation). The claim that prototypes correspond to meaningful linguistic concepts is unsupported. *Evidence: Lines 172–173, Figure 6 caption.*

6. **The "reasoning" benefit is asserted but never measured.** The paper motivates using LLMs for their "sophisticated reasoning and pattern recognition capabilities" (Section 1) and states PaP "augments the LLM's reasoning ability" (Section 3), but no experiment isolates or measures reasoning per se. The input statistics in PaP are computed deterministically — the LLM conditions on them without necessarily performing reasoning. This is a minor overclaim. *Evidence: Lines 14, 96.*

### Trivial
None beyond typical presentation issues addressable during revision.

## Nice-to-Haves
- Running GPT4TS (or an equivalent fine-tuning method) with the same Llama-7B backbone to isolate the benefit of reprogramming vs. fine-tuning.
- A genuinely cross-domain zero-shot experiment (e.g., train on ETT, test on Weather/Traffic).
- Reporting results with standard input lengths (T=96 or T=336) or explicitly confirming that all baselines were evaluated at T=512 under identical conditions.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **Criticism that T=512 is non-standard and invalidates comparisons.** The paper states it "cite[s] their performance from zhou2023one" (line 113). Zhou et al. (2023, GPT4TS) used T=512 in their evaluation protocol, so the comparison is consistent. The harsh critic's claim that baselines were "not designed or tuned for" T=512 is speculative — the paper cites published numbers from a source that used the same protocol. The criticism is weakened to a presentation clarity issue and moved here.

- **Criticism about missing tables and unverifiable results.** The tables (long-term, short-term, ablation) are present in the original submission but stripped by the parser. The hard rules direct removing weaknesses about missing appendix/tables.

- **Criticism about comparison with non-LLM methods (PatchTST, DLinear, TimesNet) being "orders of magnitude smaller."** Comparing a 7B-parameter method against smaller specialized models is standard practice; the backbone-inequality objection only applies to the GPT4TS comparison (another LLM method). This is scope creep.

- **Complaints about missing ILI results and other table-specific concerns.** These are parser artifacts; the tables exist in the original submission.

- **Request for full ablation tables with absolute values.** The paper reports relative percentages due to space; the absolute values are in the tables (which exist in the original submission).

## Novel Insights

The reviews surface a tension that the paper does not fully grapple with: the method's best performance comes from combining a large frozen backbone (7B parameters) with lightweight learned adapters, but the paper's central comparison against a smaller fine-tuned LLM (GPT4TS) is confounded by this backbone asymmetry. This suggests that the most honest interpretation of the results may be that (a) reprogramming a large frozen LLM is competitive with fine-tuning a smaller LLM, and (b) the PaP + reprogramming components provide meaningful gains over direct patching on the *same* backbone (as the ablations show). The paper would benefit from reframing its contributions around these internally-controlled comparisons rather than emphasizing the uncontrolled GPT4TS gap.

## Suggestions

1. **Run the controlled backbone experiment** — compare Time-LLM against GPT4TS (or a fine-tuned variant) using Llama-7B as the shared backbone. Alternatively, run Time-LLM with a GPT-2 backbone and compare with GPT4TS at comparable scale. This one experiment would either validate or substantially weaken the central claim.

2. **Design a genuinely cross-domain zero-shot evaluation** — train on ETT and test on Weather, Traffic, or Electricity. If the method performs well, this would be much stronger evidence for cross-domain generalization.

3. **Clarify the prototype construction** — replace "linearly probing E" with a precise description (e.g., "a learned linear projection of the embedding matrix" or "a set of V' learnable vectors initialized from E"). Provide the exact training details.

4. **Add at least one measure of variance** — even three seeds with mean ± std for the headline results (long-term forecasting, few-shot) would significantly strengthen the empirical claims.

5. **Report results at T=96 or T=336** (the standard in PatchTST/TimesNet) for at least the main datasets to facilitate direct comparison with the literature, and explicitly state that baselines from Zhou et al. (2023) were evaluated at identical input lengths.

## Score and Decision

**Originality:** 7/10 — The combination of text-prototype reprogramming with PaP is novel, though components draw on established ideas (prefix-tuning, cross-attention adapters).

**Importance of research question:** 8/10 — Adapting frozen LLMs to time series without fine-tuning is a timely and practically important direction.

**Claims support:** 5/10 — The headline claims against GPT4TS are confounded by backbone size; the zero-shot framing overstates cross-domain generality. Ablation studies are stronger but reported only in relative percentages.

**Soundness of experiments:** 6/10 — Good breadth (long-term, short-term, few-shot, zero-shot) but missing critical controls and variance reporting. Within-method ablations are a strength.

**Clarity of writing:** 7/10 — The methodology is clearly structured; the main weakness is ambiguity in the prototype construction description and imprecise language around "cross-domain."

**Value to community:** 8/10 — The frozen-LLM reprogramming approach is likely to be adopted and extended. The parameter efficiency is practically valuable.

The paper makes a genuine contribution with a novel technical approach and strong internal ablations. However, the most prominently featured quantitative comparisons are compromised by uncontrolled backbone size (vs. GPT4TS) and overstated domain generalization (zero-shot). These are addressable in a revision but reduce confidence in the paper's strong claims as presented.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>
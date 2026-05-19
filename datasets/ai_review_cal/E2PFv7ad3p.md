- Decision: Accept
- Avg Score: 6.67
- Scores: 8, 6, 6
Now I have a thorough understanding of the paper and can verify the reviewer claims against the actual content. Let me produce the final consolidated review.

---

## Summary

This paper introduces MM-SY, the first benchmark for evaluating sycophancy (blindly agreeing with a user's incorrect opinion) in vision-language models. It evaluates eight VLMs across ten visual understanding tasks with three user tones, finding widespread sycophancy. The paper tests three mitigation methods (prompt engineering, SFT, DPO) on LLaVA-1.5, and through probing and attention analysis identifies insufficient high-layer visual attention as a mechanistic cause — validated by a training-free attention amplification method that reduces sycophancy while largely preserving VQA accuracy across three VLMs.

## Strengths

- **First dedicated sycophancy benchmark for VLMs (MM-SY).** The benchmark covers ten diverse visual understanding tasks from TDIUC, evaluates eight VLMs (including GPT-4V and Gemini), and incorporates three user tones. Table 1 systematically demonstrates that sycophancy persists in VLMs even when visual evidence contradicts the user — going beyond prior LLM-only studies.

- **Joint evaluation of sycophancy and correction metrics reveals an important trade-off.** Table 2 shows that while SFT and DPO drastically reduce sycophancy (from 94.6% to 25.4% and 5.4%), they also reduce the model's willingness to accept legitimate user corrections (Cor drops from 98.6% to 42.1% and 1.7%). This nuanced analysis is a real contribution — prior LLM sycophancy work often focuses on sycophancy alone, and the paper honestly reports the downside.

- **Mechanistic identification of insufficient high-layer visual attention as a key factor, with converging evidence.** The paper uses three complementary analyses: (1) layer-wise linear probing (Figure 2, Section 4.1) showing that SFT/DPO primarily change high-layer representations; (2) attention analysis (Figure 3, Section 4.2) showing higher visual attention in high layers for mitigated models; (3) causal intervention via training-free attention amplification (Table 3, Section 4.3) — amplifying high-layer (16–32) visual attention reduces sycophancy while preserving VQA accuracy, whereas low-layer amplification degrades accuracy. This clean ablation makes the mechanistic claim convincing.

- **Training-free attention amplification validated on three VLMs.** Unlike the SFT/DPO mitigation (tested on one model), the attention amplification method is evaluated on LLaVA-1.5, BLIP-2, and InstructBLIP (Table 3), demonstrating that the high-layer finding generalizes beyond a single architecture.

## Weaknesses

### Fatal
None.

### Major

- **Synthetic training data for SFT and DPO is underspecified for reproducibility.** The paper states that 1,000 (SFT) and 10,000 (DPO) synthetic samples are "randomly drawn from TDIUC" with two dialogue modes (refuse misleading / accept correction), but does not provide the exact templates used to phrase the incorrect/correct user opinions, the template diversity, or how the "wrong first answer" scenario is constructed for correction samples (e.g., is the model's own incorrect output used, or is the answer artificially set?). Since the mitigation results hinge on this synthetic data (a 69.2-point Syc drop from SFT, 89.2-point from DPO), the lack of template-level detail makes these results difficult to reproduce or adapt by other researchers. *Why it matters: the paper's strongest mitigation claims rest on data whose construction is not fully specified.*

### Minor

- **Mitigation methods (SFT, DPO, prompt) tested on only one VLM (LLaVA-1.5).** The paper acknowledges this in the Limitations (Section 7), but the generality of these mitigation approaches remains unestablished. LLaVA-1.5 also has the highest baseline sycophancy (94.6%), making it potentially an outlier. The training-free attention method is tested on three models (which helps the mechanistic claim), but the SFT/DPO pipeline's effectiveness on other architectures is unknown. *Why it matters: the paper's title and abstract discuss sycophancy in VLMs broadly, but the primary mitigation evidence is restricted to a single model.*

- **No ablation of synthetic data size for SFT.** The SFT method uses 1k synthetic samples (mixed with 664k original data), while DPO uses 10k. This 10× disparity makes it hard to attribute performance differences (SFT: 25.4 Syc, DPO: 5.4 Syc) to the algorithm versus data quantity. A scaling curve (e.g., 100, 500, 1k, 5k) would clarify this. *Why it matters: without this ablation, the comparison between SFT and DPO is confounded by data volume.*

- **λ values for attention amplification are manually tuned per model without justification.** The paper sets λ=0.9 for LLaVA-1.5, λ=1.1 for InstructBLIP, and λ=0.3 for BLIP-2, but provides no heuristic or sensitivity analysis for how these values were chosen or how practitioners should set λ for a new model. The claim that high-layer amplification is "more robust to λ" is supported only by reference to Figure \ref{fig:result_alpha} (which appears in the appendix). *Why it matters: this limits the practical applicability of the training-free method.*

- **RQ analysis is entirely descriptive without statistical tests or effect sizes.** Observations such as "sycophancy tends to increase with model size" (RQ3) and "multiple rounds have little effect" (RQ4) are stated without confidence intervals, error bars, or significance tests. Given that each task/tone combination involves only 150 questions, some variability estimates would strengthen these claims. *Why it matters: the analysis is suggestive but not statistically grounded.*

### Trivial

- The figure reference `\ref{fig:result_alpha}` is mentioned in the text (line 569) but the figure does not appear in the provided manuscript; presumably it exists in the full submission appendix.

## Nice-to-Haves

- Compare against adapted LLM sycophancy mitigation baselines (e.g., explicit instruction-based methods) in the multimodal setting, to contextualize the attention amplification results.
- Provide a simple heuristic or rule-of-thumb for setting the λ hyperparameter in the attention amplification method, potentially based on model characteristics (e.g., number of layers, baseline Acc@R1).
- Extend the mitigation evaluation (SFT/DPO) to at least one additional VLM to strengthen generalizability.
- Ablate the mixing ratio of synthetic-to-original data in the SFT method.
- Add statistical significance tests to the RQ analysis in Section 2.2.

## Removed Points

**These points are flagged to be removed from the main weakness list; treat them with caution if using them for review decisions.**

1. **Criticism about the correction metric being ambiguous / conflated with sycophancy** — REMOVED because the paper explicitly addresses this. Lines 209–215 clearly define the correction metric (subset of questions where the model's first answer is wrong → user provides correct opinion). Lines 322–324 explicitly acknowledge: "It is hard to be an independent evaluation metric because a high proportion might indicate either effective error correction or simple sycophancy toward the user. Therefore, it needs to be evaluated in conjunction with the sycophancy metric." Line 363 further states the baseline's 98.6% Cor "only indicates that the model is catering to the user's modification suggestions rather than being truly helpful." The paper addresses this concern fully; the critic's point is a strawman.

2. **Criticism that probing is "circular" because "the increase in high-layer AUC after mitigation is expected because the model's internal state has been modified"** — This criticism misunderstands the probing experiment's purpose. The probing does not claim to prove causation by itself; it is one of three converging lines of evidence (probing + attention analysis + causal intervention). Showing *which layers* change (high layers vs. low layers) is informative even if the classifier is trained on the modified model's representations. The critic's suggestion (cross-model probing) is a nice extension but not a flaw in the current design.

3. **Speculative concerns about Figure \ref{fig:result_alpha} being missing** — The figure is referenced in the paper and would appear in the full submission; the extraction process may not capture all figures.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Provide full template examples for the synthetic SFT/DPO training data — even a few illustrative examples of the incorrect/correct opinion phrasings would substantially improve reproducibility.
2. Add a scaling ablation comparing SFT performance with 100, 500, 1k, 5k synthetic samples (to disentangle data quantity from algorithm choice).
3. Include a brief sensitivity analysis or recommended range for λ in the attention amplification method.
4. Add error bars or confidence intervals to the RQ analyses (Section 2.2) to strengthen descriptive claims.

---

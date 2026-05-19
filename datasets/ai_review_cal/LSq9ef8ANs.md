- Decision: Reject
- Avg Score: 4.60
- Scores: 5, 5, 5, 3, 5
Now I have a thorough understanding of the paper and can verify all claims. Let me write the consolidated review.

## Summary

The paper introduces VaQuitA, a framework for zero-shot video question answering that improves video-text alignment at three levels: (1) **Data Alignment** — CLIP-score-guided frame sampling that selects half the frames uniformly and half based on semantic similarity to the question; (2) **Feature Alignment** — a trainable Video Perceiver (based on the Perceiver Resampler) paired with a VQ-Former that uses inverted cross-attention (video features as queries, text features as keys/values); and (3) **Prompt Engineering** — adding "Please be critical" before the question at test time. The method is trained end-to-end (with frozen CLIP encoder and frozen LLM) on VideoInstruct-100K with LLaVA-1.5 initialization, and achieves strong results on MSVD-QA, MSRVTT-QA, and ActivityNet-QA.

## Strengths

- **Strong empirical results with consistent gains across datasets.** Table 1 shows VaQuitA outperforms all prior models on all three benchmarks. The ablation in Table 2 confirms that even the **Feature Alignment component alone** (without Data Alignment or Prompt Engineering) achieves 70.8% on MSVD-QA and 59.7% on MSRVTT-QA — substantially above the prior best (BT-Adapter at 67.0% and 51.2%). This indicates the core architectural design (Video Perceiver + VQ-Former) provides meaningful improvements.

- **Component-wise ablation validates each module's contribution.** Table 2 systematically ablates Data Alignment, Feature Alignment, and Prompt Engineering across all three datasets. The ablations show that each component contributes positively, with Feature Alignment providing the largest individual gain (e.g., +8.9% on MSRVTT-QA when comparing DA-only vs FA-only). This gives a clear picture of where the improvements come from.

- **Novel VQ-Former with inverted cross-attention is architecturally distinct.** The paper introduces a design where video features serve as queries and text features as keys/values — the opposite of the standard Q-Former (BLIP-2) or gated cross-attention (Flamingo). The rationale of using the question to guide which visual details to attend to is sensible and different from prior work.

- **Prompt discovery with controlled comparison.** Figure 4 compares "Please be critical" against several alternative prompts ("Let's think step by step," "Take a deep breath…," "Look carefully before answering," and no prompt) on ActivityNet-QA, showing "Please be critical" performs best. This is a reproducible finding.

- **Efficient training design.** Only the Video Perceiver and VQ-Former are trainable; the CLIP encoder and LLM (LLaMA-2 7B) remain frozen. This keeps the computational budget practical and the method accessible.

## Weaknesses

### Fatal
None.

### Major

1. **Uncontrolled baseline comparison confounds the reported gains.** The main results (Table 1) compare VaQuitA against numbers taken from prior papers (marked with * and †). VaQuitA uses **LLaMA-2 (7B) with LLaVA‑1.5 initialization**, while baselines like BT-Adapter use LLaMA and Video-ChatGPT uses LLaVA (not LLaVA-1.5). The paper does not re-implement baselines under the same training data, base LLM, and evaluation conditions. The reported gains of +7.6% on MSVD-QA and +17.4% on MSRVTT-QA could be partially or largely explained by the stronger base model rather than the proposed components. A controlled head-to-head comparison (e.g., replacing only the projection layer in Video-ChatGPT with the proposed FA module) is needed to isolate the method's true contribution.

2. **The VQ-Former's specific design is not ablated against simpler alternatives.** The Feature Alignment module combines a Video Perceiver (a standard Perceiver Resampler from Flamingo) with a VQ-Former. The ablation in Table 2 only ablates FA as a whole. It does not compare the VQ-Former's inverted cross-attention against: (a) a standard Q-Former design (text queries, visual keys/values), (b) gated cross-attention (Flamingo), or (c) a simple linear projection (as in Video-ChatGPT). Since the inverted cross-attention is presented as the paper's key architectural novelty, this omission means the reader cannot tell whether the VQ-Former design matters or whether the gains come entirely from the already-known Perceiver Resampler + any reasonable connector.

### Minor

3. **Prompt Engineering gains are very small on two of three datasets.** From Table 2, adding "Please be critical" to the full model yields: +0.2 accuracy on MSVD-QA, +0.1 on MSRVTT-QA, and +1.1 on ActivityNet-QA. Given the absence of error bars or multiple-seed runs, these marginal increments (especially 0.1–0.2%) are plausibly random variation or evaluation artifacts rather than genuine improvements. The paper claims the prompt "substantially enhances" video comprehension (abstract) and works "universally" (contributions), which overstates the evidence.

4. **The prompt comparison (Fig. 4) is only on ActivityNet-QA.** While Table 2 checks PE presence/absence across all datasets, the head-to-head comparison of different prompt variants ("Let's think step by step," etc.) is only conducted on ActivityNet-QA. It is unknown whether "Please be critical" dominates alternatives on MSVD-QA and MSRVTT-QA.

5. **Multi-round conversation claims are supported only by qualitative examples.** Two cherry-picked examples (Fig. 2, labeled as Fig. 1 in demo) show VaQuitA producing longer, more correct answers than Video-ChatGPT. No human evaluation, no automated metrics (e.g., relevance, consistency), and no benchmark comparison are provided. The claim of "top-notch multi-turn conversations" (contributions) is unsupported.

6. **No statistical significance or error bars for any quantitative result.** All numbers in Tables 1 and 2 are single-run without variance estimates. Given that GPT-based evaluation has inherent randomness (API version, temperature, stochastic decoding), confidence intervals or multi-seed runs would substantially strengthen the reliability of the reported improvements.

### Trivial
None.

## Nice-to-Haves
- An ablation comparing test-time data alignment (CLIP-guided sampling) vs. uniform sampling on full benchmark results, rather than a single appendix example.
- Discussion of potential overfitting to the CLIP similarity metric during data alignment (as noted, the same CLIP model is used for both feature extraction and similarity scoring).
- Computational cost comparison (parameter count, inference speed) relative to baselines.
- Failure case analysis to understand where VaQuitA still struggles.

## Removed Points

The following points from the harsh critic are removed with justification:

- **"The paper does not state whether the same GPT-3.5-turbo API version and evaluation script were used for all numbers."** — Removed because the paper explicitly states: "we employ Azure GPT-3.5-turbo API (March version) for evaluation, which is consistent with~\cite{maaz2023video}" (line 155). The paper is transparent about their evaluation setup for their own numbers. The broader point about cross-paper comparison is retained in Major weakness #1.

- **"The paper does not test alternative 'critical' prompts to isolate the specific phrasing"** — Partially inaccurate. The paper does test alternative prompts (Fig. 4 shows "Let's think step by step," "Take a deep breath…," "Look carefully before answering"). The critic's point about not testing *variations* of "critical" (e.g., "Be critical" vs "Be very critical") is valid but too narrow to constitute a standalone weakness; it is absorbed into the observation that the prompt ablation is limited to one dataset (Minor #4).

- **"The chart (Fig. 1) is potentially misleading if baselines were evaluated under different conditions"** — Removed as speculative. The chart visualizes the same Table 1 data and adds no new information. The core concern about comparison fairness is already captured in Major #1.

- All formatting/style nitpicks and reproducibility concerns about undisclosed hyperparameters — Removed per hard rules; the paper discloses training hyperparameters (batch size, learning rate, epochs, model dimensions) in line 152.

## Novel Insights

The most useful insight to emerge from the reviews is not present in the paper itself: the cross-attention inversion (video→query, text→key/value) could actually be detrimental for tasks where visual details are needed to ground the answer but the question is the main driver of what to attend to, and the paper's ablation design prevents testing this. Both the harsh critic's demand for a controlled comparison and the fact that FA alone already achieves strong results point to the possibility that the main practical contribution is simply adding a Perceiver Resampler (from Flamingo) before LLM integration, and the VQ-Former's specific attention pattern may add little value over a standard connector. The paper needs this ablation to make its novelty case.

## Suggestions

1. **Controlled baseline re-implementation.** Re-run Video-ChatGPT's simple projection under LLaMA-2 + LLaVA-1.5 with the same training data and evaluation pipeline. Then ablate in your VQ-Former on top. This would cleanly separate base-model effects from architectural innovations.

2. **Isolate the VQ-Former.** Compare VQ-Former (inverted cross-attention) against: standard Q-Former (text queries, visual K/V), gated cross-attention (Flamingo style), and a simple linear projection — all with the same Video Perceiver front-end. This is necessary to validate the claimed architectural novelty.

3. **Report error bars.** Run all experiments with at least 3 random seeds and report mean ± std, especially given GPT-based evaluation noise.

4. **Validate "Please be critical" across all datasets.** Extend the prompt comparison (Fig. 4) to MSVD-QA and MSRVTT-QA. Also test whether the effect replicates without the "Please" prefix (e.g., "Be critical").

5. **Strengthen multi-turn evaluation.** Provide at least a small-scale human preference study (e.g., 50 multi-turn conversations, rated by 3 annotators on correctness and relevance) to support the multi-turn capability claim.

6. **Tone down overclaims.** The language ("substantially enhances," "universally," "top-notch," "sets a new standard") exceeds what the current evidence supports, especially given the uncontrolled comparison and marginal prompt gains on two datasets.

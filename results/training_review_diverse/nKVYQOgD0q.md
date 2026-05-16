Here is my final consolidated review.

---

## Summary

This paper introduces Merged Preference Dimensions (MPD), a method for personalized LLM alignment that dynamically merges the next-token output probabilities of multiple black-box expert models (each specialized in one preference dimension like humor, conciseness, etc.) at the token level. A lightweight 160M-parameter Preference Control Model (PCM) learns to produce context-dependent merging weights as a function of the instruction, partial response, and user preference vector. The PCM is trained via online RL (REBEL) using Bradley-Terry-normalized rewards from individual preference-dimension reward models. Experiments on Tulu-7B with two datasets show that MPD achieves higher pairwise win rates (GPT4-evaluated and human-validated) than the weight-merging baseline Personalized Soup and prompting baselines.

## Strengths

- **Black-box personalization without model weight access**: Unlike prior weight-merging work (Jang et al., 2023; Ramé et al., 2023) that requires white-box access to expert parameters and identical architectures, MPD only needs the next-token probabilities of each expert. The paper explicitly states (§3.1) that individual experts "are frozen and can be treated as black-box models since only their output probabilities are needed," making the method applicable where expert weights are proprietary or unavailable.

- **Context-dependent dynamic token-level merging**: MPD computes different mixture weights for each token based on the preceding context and the full preference description (Eq. 1: α_θ(x, y_<t, ξ) varies per time step). The qualitative examples (Table 6) demonstrate concrete benefits: MPD avoids the repetitive metaphors and washed-out tones that plague Preference Prompting and Personalized Soup, confirming that dynamic weighting preserves individual preference dimensions better than static parameter merging.

- **Lightweight Preference Control Model (PCM)**: The PCM has only 160M parameters — 2% of the base Tulu-7B model (§4.2) — yet learns to orchestrate multiple large expert LLMs. This demonstrates that the core personalization intelligence can be offloaded to a tiny network, reducing training overhead and enabling faster re-training if new preferences are added (§4.6).

- **Bradley-Terry normalization of uncalibrated reward models**: Section 3.2 introduces a BT-based transformation (Eq. 2) that normalizes each dimension's reward to a [0,1] probability of beating a reference response. This solves the practical problem that separate reward models (e.g., for humor and conciseness) have different scales. The ablation in Table 4 confirms that removing this BT step reduces performance.

- **Consistent empirical superiority confirmed by both GPT4 and human judges**: Across two datasets (Koala and UltraFeedback) and all eight preference combinations, MPD achieves the highest average win rate (66.28% in Table 2). The human evaluation on 200 pairs with 20 raters (Table 5) yields statistically significant win rates (binomial test, p=0.05) that are even higher than GPT4's, validating that the personalization aligns with actual human perception.

- **Inference-time parallelism demonstrated**: Section 4.5 reports that with 32 simultaneous requests, MPD averages 10.48s per request, beating Personalized Soup's 13.25s. This is supported by the argument that output merging can batch shared preference dimensions across users, whereas parameter merging requires separate models for each distinct preference combination.

## Weaknesses

### Fatal

None.

### Major

None. The paper's core contribution — dynamic token-level output merging for black-box personalized alignment — is novel, technically sound, and supported by the experiments. The weaknesses below are addressable and do not invalidate the central claims.

### Minor

- **Baseline comparison is somewhat narrow relative to the breadth of related work discussed.** The paper evaluates against Personalized Soup (Jang et al., 2023), Preference Prompting, and Vanilla Prompting, but several methods mentioned in §2 (Related Work) — most notably Dognin et al. (2024), who train an encoder-decoder network to combine outputs from individually-trained SFT models, and Tan et al. (2024), who use LoRA for per-user personalization — are not included as experimental baselines. While MPD (Uniform) subsumes the simple output-interpolation baseline (Li et al., 2023), and Personalized Soup is the most directly relevant prior work in the same problem setting, the paper's claim to "match or surpass existing preference merging techniques" would be strengthened by comparisons to a broader set of multi-objective personalization methods. The absence does not invalidate the results but leaves the claim partially undersupported.

- **Efficiency and scalability analysis lacks critical detail.** The inference speed comparison (§4.5) reports 13.25s vs 10.48s per request for 32 simultaneous requests, but the paper does not specify: (1) the hardware used, (2) the distribution of preferences across the 32 requests (and thus how many distinct expert forward passes are needed), (3) the number of tokens generated, (4) whether these are averages with error bars/standard deviations, or (5) how the amortized one-time model merging cost for Personalized Soup was accounted for. Additionally, the claim that parameter merging is less scalable "as the number of preference dimensions increases" is not tested empirically — the experiments use only 6 dimensions and 8 composite preferences. A stronger analysis with varying numbers of dimensions and preferences would substantiate this claim.

- **PCM architecture details are underspecified for reproducibility.** The paper states that the PCM is "a LLaMA based model" with 160M parameters, and that its final linear layer is replaced with output dimension n (number of experts). However, it does not describe how the three inputs — instruction x, partial response y_<t, and preference vector ξ — are tokenized, encoded, and combined. For example: is ξ encoded as a text prompt, a fixed-length embedding, or a learned embedding? How are x and y_<t concatenated? Without this information, reproducing the method requires non-trivial guesswork.

- **Human evaluation protocol is partially underspecified.** The paper reports using 20 raters on 200 pairs (Table 5) and states that raters were "instructed...to rate based on the specified preference dimension." However, it does not clarify: whether raters saw both responses simultaneously or sequentially, how many raters evaluated each pair, whether raters were trained or calibrated on the preference dimensions, or how disagreements were resolved (if at all). These details matter for assessing the reliability of the human evaluation.

- **Statistical significance is not reported for the main results (Table 2).** While the human evaluation (Table 5) includes a binomial test, the primary pairwise win rates in Table 2 are reported without confidence intervals or significance tests. Given the modest evaluation set (100 prompts × 8 preferences), bootstrapped intervals would substantially strengthen the conclusions.

- **Modest scale of evaluation data.** The evaluation uses 50 instances from Koala and 50 from UltraFeedback (100 prompts total, yielding 800 comparisons across 8 preferences). The paper follows Jang et al. (2023)'s protocol, which is defensible, but the scale is small enough that variance is a real concern — reinforcing the need for significance testing above.

### Trivial

None worth listing separately.

## Nice-to-Haves

- An analysis of how the PCM's learned weights vary across generation steps (e.g., which experts get higher weight at the beginning vs. end of a response) would provide insight into whether the controller is doing something non-trivial beyond uniform weighting.
- Testing MPD with a larger number of preference dimensions (e.g., 4-5, yielding 16-32 preferences) would more directly validate the scalability claims.
- Discussion of why REBEL was chosen over PPO beyond "simplicity and superior performance" would help readers understand trade-offs.

## Removed Points

These points are flagged to be removed — treat them with caution:

1. **"Reliance on self-trained experts undercuts the black-box framing" (Harsh Critic Point 3).** Removed because the paper explicitly addresses this in §4.2: "Although we trained the models ourselves, we note that after training, for MPD, the expert weights are never accessed or updated, simulating a realistic scenario where expert models are black-box." The method genuinely only requires output logits/probabilities from any expert model. Training one's own experts to evaluate a method is standard practice in academic research and does not undercut the black-box claim — the method never uses weight access during inference or training of the PCM. The paper also acknowledges the tokenizer-compatibility assumption ("as long as the tokenizer is the same," §2), so the critic's concern about heterogeneous tokenizers is already scoped out by the authors.

2. **Cherry-picked qualitative examples.** Removed because selective qualitative illustration is standard practice in NLP papers and is not presented as systematic evidence. The paper's quantitative results (Tables 2, 3, 5) constitute the primary evidence.

## Novel Insights

None beyond the paper's own contributions. The reviews do surface a useful meta-point: that the paper's evaluation breadth (baselines, efficiency testing) lags behind the ambition of its claims — a common pattern in methods papers where the core idea is strong but the experimental surround could be tighter. This is a judgment about the evaluation scope, not a novel methodological insight.

## Suggestions

- Add at least one additional multi-objective personalization baseline from the related work (e.g., the encoder-decoder approach of Dognin et al., 2024, or the logit-interpolation baseline from Li et al., 2023 beyond the uniform version already tested) to broaden the empirical support.
- Provide hardware specs, preference distributions, token counts, and standard deviations for the efficiency benchmark.
- Specify the PCM input encoding in detail: how x, y_<t, and ξ are tokenized, concatenated, and fed into the LLaMA-based model. This is essential for reproducibility.
- Include bootstrapped confidence intervals or significance tests for the main pairwise win rates in Table 2.
- Clarify the human evaluation protocol (per-pair rater count, annotation interface, rater training, disagreement resolution).

## Score and Decision

The paper presents a novel, well-motivated, and technically sound method for personalized LLM alignment. The core idea — learning a lightweight controller to dynamically merge expert output probabilities at the token level — is clean and practically appealing. The empirical results consistently favor MPD over the baselines tested, with validation from both GPT4 and human judges. The weaknesses are real but addressable: a broader baseline set, more rigorous efficiency benchmarking, and fuller documentation of the model and evaluation protocols would strengthen the paper without changing its core contribution. The contribution warrants acceptance.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>
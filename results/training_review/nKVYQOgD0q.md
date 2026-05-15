Now I have all the information needed. Let me synthesize my findings and produce the final consolidated review.

## Summary

The paper introduces Merged Preference Dimensions (MPD), a method for personalizing LLM outputs by dynamically merging the output probability distributions of frozen expert models at the token level. A lightweight Preference Control Model (PCM, 160M params, ~2% of the base model) learns to produce context-dependent weights for combining expert distributions, trained with REBEL/PPO using dimension-wise reward models with Bradley-Terry normalization. The method requires only output logits from experts (not model weights), and experiments on Tulu-7B with 8 preferences across 6 dimensions show higher pairwise win rates against baselines including Personalized Soup.

## Strengths

- **Novel and well-motivated problem framing.** The paper clearly articulates the limitation of parameter-level merging (the "washed out humor" problem) and proposes a principled alternative: context-dependent, token-level output merging via a learned preference control model. This is a clean conceptual advance over uniform weight interpolation (Jang et al., 2023).

- **Architecturally modular and practical.** The PCM is small (160M parameters) and does not backpropagate through the expert models, keeping training lightweight. The method requires only output logits, not model weights, enabling use with black-box expert models — a genuine practical advantage over parameter-merging approaches.

- **Human evaluation confirms the trend.** The human evaluation on 200 pairs (Table 5) shows MPD preferred over Preference Prompting (64.0%) and Personalized Soup (62.0%), with binomial test significance at p=0.05. This provides some evidence that the improvements are not artifacts of the GPT-4 judge.

- **Inference efficiency insight.** The paper identifies and validates a non-obvious advantage: under concurrent serving (32 simultaneous requests), MPD is faster (10.48s/req) than Personalized Soup (13.25s/req) because expert forward passes can be shared across preferences that share dimensions.

- **Ablations validate design choices.** Table 4 systematically tests logit vs. probability merging, with/without BT normalization, and PPO vs. REBEL, confirming each component contributes to performance.

- **Consistency across two datasets.** MPD outperforms baselines on both Koala (Table 2) and UltraFeedback (Table 3) subsets, reducing concern about dataset-specific artifacts.

## Weaknesses

### Fatal
None. The paper makes a valid contribution; the core idea is sound. However, the experimental validation has significant gaps that prevent the paper from being acceptably strong in its current form.

### Major

1. **Missing statistical rigor in main results.** The primary results (Table 2) report win rates across 800 evaluations (100 prompts × 8 preferences) without any confidence intervals, error bars, or significance tests. With a modest sample of 100 distinct instructions, the headline 66.28% vs. 60.21% advantage over Personalized Soup could be within noise. The human evaluation uses a binomial test, but the main GPT-4 evaluation does not. Without quantifying uncertainty, the claim of "surpassing all baselines" is not fully supported.

2. **Limited evaluation scale and generalizability.** All experiments use only Tulu-7B as the base model. This leaves open questions about scalability to larger models (13B, 70B), different architectures (e.g., non-Llama families), and different expert training data distributions. The 100 distinct instructions, while doubling Jang et al. (2023), still represent a narrow test of generalization. The method is demonstrated in a single narrow setting, making claims of general "state-of-the-art" premature.

3. **Baseline comparison is too narrow.** The only preference-specific weight-merging baseline is Personalized Soup (uniform weight interpolation). While this is the most directly relevant prior work, the paper would substantially benefit from comparing against at least one more sophisticated merging strategy — either a learned-weight parameter-merging method (as in Guo et al., 2024; Wang et al., 2024a, which are cited but not compared against) or an output-interpolation baseline with context-independent but learned weights. Without such comparisons, the paper's claim of setting a "new state-of-the-art" (conclusion) goes beyond what the evidence supports.

### Minor

4. **Reference response not specified for BT normalization.** The Bradley-Terry reward formulation (Eq. 2) depends on a reference response y_ref, described only as coming from "a baseline LLM." Which baseline? How is the reference generated? This vagueness makes a core step of the training pipeline non-reproducible from the main text. The paper should specify the exact reference response source.

5. **Missing training hyperparameters in main text.** Batch size, number of RL iterations, learning rate, reward model specifics — these details are deferred to supplementary materials not available in the review. The reproducibility statement promises code upon acceptance, but the main text should include the essential training configuration.

6. **No per-dimension win rate breakdown.** Table 2 reports only average win rates across all 8 preferences. Dimension-level win rates would reveal whether MPD systematically improves certain preference dimensions more than others, or whether the improvement is uniform. This would also help verify that the PCM is actually learning to emphasize the requested dimensions rather than simply producing generically better text.

7. **Logit truncation robustness not tested.** The paper states that only "top output logits (or probabilities)" are needed, framing this as a practical black-box benefit. However, the method (Eq. 1) constructs a full vocabulary distribution via convex combination, which in principle requires the full distribution from each expert. No experiment tests performance under top-k or top-p truncation (e.g., k=10, 100). This gap between claimed access level and actual implementation should be examined.

8. **Human evaluation is small (200 pairs).** While the human evaluation is appreciated, 200 pairs across 20 raters yields limited statistical power. The mismatch between GPT-4 win rate on the subset vs. the full table (noted by the authors) also raises questions about subset representativeness. A larger human evaluation would strengthen confidence in the results.

### Trivial
None.

## Nice-to-Haves
- Ablation on PCM capacity (e.g., 50M vs. 160M vs. 500M parameters) to test whether the small model is actually sufficient or whether performance would improve with a larger controller.
- Extension to more preference dimensions (e.g., 4 pairs = 16 preferences) to test scalability.
- Systematic failure analysis showing cases where MPD loses to baselines, categorized by error type.

## Removed Points
These points are flagged by the reviewer(s) but are factually incorrect, scope-creep demands, or otherwise invalid.

1. **"12.5 prompts per preference"** — The reviewer miscalculated: 100 distinct instructions evaluated with all 8 preferences yields 100 evaluations per preference, not 12.5. The text says "800 prompts" meaning 100 instructions × 8 preference combinations. [Factually wrong]
2. **"REBEL objective requires summing over vocabulary"** — The reviewer misread Eq. 3. π_θ(y_t|x,y_{<t}) = Σ_i α_i · π_{M_i}(y_t|x,y_{<t}), where each π_{M_i}(y_t|...) is a scalar (the probability of the specific token y_t from expert i). The sum is over the 3 experts, not the vocabulary. This computation is trivial. [Factually wrong]
3. **"Method requires full next-token probability distribution over the entire vocabulary"** — The paper explicitly states: "All it requires access to is the top output logits (or probabilities) of each expert" (Section 1). The reviewer contradicted the paper's stated access requirement. The request for truncation-robustness testing is valid (kept as Minor #7), but the claim that the method requires full distributions is false.
4. **Request to compare against TIES-Merging / DARE / AdaMerging** — These are general model merging methods not designed for preference personalization, which is outside the paper's stated scope. The paper compares against the most directly relevant prior work (Personalized Soup) plus prompting baselines. Adding one more preference-specific baseline would strengthen the paper (Minor #3), but demanding general model merging methods is scope creep.
5. **"Cherry-picked qualitative examples"** — This is standard practice for qualitative analysis in LLM papers; not a valid weakness.
6. **"Inference efficiency comparison is unfair because pre-merging could be done offline"** — The paper explicitly compares the dynamic serving scenario (32 concurrent requests), where different users request different preferences simultaneously. In this realistic deployment scenario, pre-merging is not applicable because it would require storing 8 separate model copies. The comparison is appropriate for the stated setting.

## Novel Insights

The reviews surface one observation not fully articulated in the paper: the most interesting aspect of MPD may not be its absolute win-rate improvement (which is modest) but rather its architectural properties — the separation of preference direction (PCM) from generation capability (frozen experts) creates a system where the "preference interface" is a tiny, fast, independently trainable module. This is reminiscent of adapter-based personalization but operates at the output level rather than the weight level. The paper could lean harder into this design philosophy: the PCM is effectively learning a *behavioral controller* that routes between pre-existing skills, which is a fundamentally different paradigm from merging skills at the parameter level. This architecture also enables the batching efficiency result (shared expert forward passes) which is the strongest practical argument for the method.

## Suggestions

1. **Add confidence intervals to all win-rate tables.** Bootstrap resampling (over instructions) would be straightforward and dramatically improve trust in the results. Report 95% CIs alongside the point estimates.
2. **Add at least one more sophisticated preference-specific baseline.** Either a learned-weight version of Personalized Soup (e.g., weighting dimensions non-uniformly via a learned scalar per dimension) or comparison against Guo et al. (2024) / Wang et al. (2024a) on the same setup.
3. **Specify the reference response source** used for BT normalization (e.g., "responses from the base Tulu-7B model without preference prompting").
4. **Report per-dimension win rates** for Table 2 so readers can see which dimensions drive the improvement.
5. **Add a logit truncation experiment** (e.g., top-10, top-50, top-100) to validate the claimed black-box practicality.
6. **Test at least one additional model size** (e.g., 13B) to demonstrate generalizability beyond 7B.
7. **Provide the essential training hyperparameters** (learning rate, batch size, RL iterations) in the main text body or an appendix included with the submission.

## Score and Decision

**Originality:** High. Token-level learned merging for personalized LLMs is a novel contribution.

**Importance of research question:** High. LLM personalization is a timely and practically important problem.

**Claims well-supported:** Partially. The evidence points in the right direction but the evaluation is too narrow (one model family, 100 instructions) and lacks statistical rigor.

**Soundness of experiments:** Moderate. The methodology is sound, but the experimental scope is insufficient to fully validate the claims.

**Clarity of writing:** Good. The paper is well-structured and clearly written.

**Value to the research community:** Moderate. The PCM architecture is interesting and likely to inspire follow-up work, but the current validation is too thin for the paper to have high immediate impact.

The paper presents a genuinely interesting idea with a clean method and some promising results. However, the experimental evaluation has significant gaps: limited evaluation scale (100 instructions, one model family), no confidence intervals on main results, and an overly narrow baseline set. These issues prevent the paper from convincingly establishing its core claims. I recommend rejection, but note the idea is well above the threshold for further development and could form the basis of a strong submission with substantially expanded experiments.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>
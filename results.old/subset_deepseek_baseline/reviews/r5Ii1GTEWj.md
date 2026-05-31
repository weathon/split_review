## Summary

The paper proposes Motion-R1, a framework for text-to-motion generation that aims to infer latent user intentions and enforce physical consistency. It introduces a Motion2Motion dataset of 7,132 multi-turn text-motion dialogues annotated with reasoning chains, a JS-divergence regularized variant of Group Relative Policy Optimization (GRPO) for fine-tuning an LLM (Qwen2.5-3B) on motion description generation, and a low-level RL policy for kinematic feasibility. The authors present experiments primarily evaluating the LLM’s output quality (semantic similarity, keyword matching, skill Jaccard) on text generation tasks, with a qualitative comparison of a single skill (“kick the door”) against Anyskill.

## Strengths

- The motivation to move beyond single-turn commands and handle multi-turn dialogue with implicit intent is timely and relevant for applications in embodied AI and human-robot interaction.
- The construction of a dialogue-formatted motion dataset with explicit semantic annotations (ERA-CoT) is a potentially useful resource, though it remains small and unvalidated against existing datasets.
- The use of JS divergence in place of KL divergence within GRPO is a technically sensible modification that may improve training stability for structured generation tasks.

## Weaknesses

### Fatal

- **No evaluation of actual motion generation.** The paper claims to address “physically consistent latent-intent motion generation,” yet all quantitative experiments (Tables 1, 2, Fig. 4) measure only the LLM’s ability to produce text descriptions (actions and skills). There is no quantitative evaluation of the final motion sequences — no comparison with any text-to-motion baseline (e.g., MDM, MLD, Tender), no physical plausibility metrics (penetration, foot skating), and no user study on motion quality. Without this, the core contribution of “motion generation” is unsupported.

- **The low-level kinematic optimization is described but never validated.** Section 3.3 outlines an adversarial RL framework for physically plausible motion synthesis, but the paper reports zero experiments using this component. It is unclear whether it was actually implemented or whether the generated motions are physically consistent at all.

- **Claims of outperforming strong baselines are vacuous.** Comparisons in Tables 1 and 2 are against raw LLMs (Qwen2.5, Llama3.2) on text-only metrics. These baselines are not motion generation methods. The only motion-related comparison is a single qualitative example (Fig. 3) against “Anyskill” — a method that itself has severe limitations. No state-of-the-art T2M or physics-based motion generation method is evaluated.

### Major

- **The dataset is too small and not benchmarked.** With 7,132 samples, the Motion2Motion dataset is orders of magnitude smaller than standard T2M datasets (e.g., HumanML3D has ~14,000 text-motion pairs, BABEL has >50,000 action segments). The paper provides no analysis of dataset coverage, no comparison to existing datasets, and no ablation showing the necessity of the ERA-CoT annotation process.

- **Experimental protocol is insufficient.** Metrics like Semantic Similarity, Keyword Matching Rate, and Information Completeness are defined at a high level but the exact computation is not specified (which embedding model? which tokenizer for keyword matching?). The GPT-4-as-judge evaluation is a single model comparison lacking multiple trials or inter-rater agreement. The GSM8K experiment mentioned in the text is relegated to an appendix that is not provided.

- **Method description contains errors and inconsistencies.** The GRPO objective (Eq. 3) appears incorrect: it reads “min(πθ/πθ_old, 1-ε, 1+ε)” when the standard clipped surrogate is “min(πθ/πθ_old A, clip(πθ/πθ_old, 1-ε, 1+ε) A)”. The advantage formula (Eq. 4) uses only group-normalized rewards without any baseline or value function — standard GRPO does this, but the paper does not discuss why value networks are omitted. The reward function (Eq. 6) weights α+β+γ=1, but these are not reported or ablated.

- **Missing comparisons to the most relevant prior work.** The paper cites Anyskill, AvatarGPT, MotionGPT, and others, but does not compare against them on any common benchmark. The claim of being “the first attempt to explore the R1 paradigm for motion generation” is not contextualized: DeepSeek-R1’s RL recipe (rule-based rewards, GRPO) is applied nearly verbatim; the novelty lies in the motion domain, but the paper does not show that this recipe yields better motion than existing RL-based motion methods (e.g., physics-based character control with PPO).

### Minor

- The paper’s organization is confusing: Section 3.1.1 presents a “Dataset Overview” but the figures (word clouds, bar charts) are not properly referenced and add little information.
- Table captions are incomplete (e.g., Table 3 is described in the text but the table itself is not given a clear caption).
- Some references are cut off and the appendix is missing, making the paper feel incomplete.

### Trivial

- The word cloud in Fig. 2 contains repeated terms (e.g., “arranging” and “sitting” appear multiple times) suggesting a parsing or deduplication error.
- Figure 3 caption refers to “alternative models (up) vs. our model (low)” but the figure shows only green humanoids in a 3D scene; a clear visual explanation of what the reviewer should see is missing.

## Nice-to-Haves

- Release of the Motion2Motion dataset (currently promised) would be a useful resource if properly validated and scaled.
- A systematic ablation of the JS divergence versus KL divergence on a controlled reasoning benchmark (e.g., math or code) would strengthen the algorithmic claim.
- Integration with a physics simulator (e.g., Isaac Gym, MuJoCo) and reporting of standard metrics (success rate, foot contact, joint torque) would address the physical consistency claim.

## Novel Insights

None beyond the paper’s own contributions. The proposal of a dialogue-annotated motion dataset and the application of GRPO with JS divergence to motion description generation are incremental; the paper does not reveal any unexpected phenomena or provide a deeper theoretical understanding of motion synthesis.

## Suggestions

- **Move the experimental focus to motion generation.** Evaluate the complete pipeline (text → motion) using established T2M benchmarks (HumanML3D, KIT-ML) and physical plausibility metrics. Compare with at least one diffusion-based T2M method and one physics-based method.
- **Validate the low-level optimization** by showing that motions produced by the full pipeline are physically consistent (e.g., no ground penetration, foot skating below threshold) and that the low-level policy improves over a kinematic-only baseline.
- **Clarify the novelty.** Explicitly state which components of the GRPO modification are new and why they are necessary for motion, as opposed to being a direct application of DeepSeek-R1’s methodology.
- **Fix the GRPO objective** to use the standard clipped surrogate formula.
- **Expand and benchmark the dataset.** Compare its size, diversity, and annotation quality to existing motion-language datasets. Show that the extra ERA-CoT annotation leads to measurable improvements over simpler labeling schemes.

## Score and Decision

MY FINAL SCORE: <score>2</score>
MY FINAL DECISION: Reject
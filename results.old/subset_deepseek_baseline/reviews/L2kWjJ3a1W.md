## Summary

This paper proposes TG-DT (Text-Guided Decision Transformer), a framework for offline meta-reinforcement learning that achieves zero-shot generalization to unseen tasks using only natural language task descriptions, without requiring any test-time task-specific data or environment interaction. TG-DT learns a shared embedding space between text descriptions and behavioral trajectories via a dual alignment mechanism combining contrastive learning (TBC) and matching-based (TBM) objectives, then uses a text-conditioned Decision Transformer to generate actions. Experiments on MuJoCo and Meta-World benchmarks show competitive or better performance compared to baselines that require test-time access to task demonstrations.

## Strengths

- **Novel problem framing and practical motivation**: The paper addresses a realistic and important challenge—enabling agents to adapt to new tasks from natural language instructions alone, without test-time demonstrations or environment interaction. This is well-motivated by real-world robotics and household assistant scenarios.

- **Technically sound dual alignment mechanism**: The combination of contrastive learning (TBC) for cross-task separation and matching (TBM) for within-task quality discrimination is well-motivated and complementary. The design of hard negative mining within TBM (including intra-task mismatches based on trajectory quality) is thoughtful.

- **Comprehensive experimental evaluation**: The paper evaluates TG-DT on multiple benchmarks (Cheetah-dir, Cheetah-vel, Ant-dir, ML10, ML45) with three dataset qualities (Medium, Mixed, Expert) and includes ablation studies, robustness analysis, and t-SNE visualizations. Results show consistent performance across settings.

## Weaknesses

### Major
- **Zero-shot claim is partially undermined by test-time description construction**: The templated test descriptions include approximate values for "expected return" and "episode length" inferred from the training distribution. While the paper argues this prevents oracle leakage, these numerical cues effectively encode task-specific information (e.g., reward scale) that standard language descriptions would not provide. This weakens the "zero-shot from natural language" claim and may give TG-DT an advantage over methods that must infer such information implicitly.

- **Description-guided data sharing during adaptation is not zero-shot**: In Section 4, the data-sharing strategy uses K training trajectories to fine-tune the decoder at test time. Even though these trajectories come from similar training tasks (not the target task), this fine-tuning step constitutes a form of data-driven adaptation that goes beyond pure zero-shot inference. The paper should clearly distinguish between the zero-shot inference variant and this data-augmented variant in all main results.

- **Unfair comparison with baselines**: Several baselines (PDT, MDT, HDT, DPDT) are marked as requiring test-time interaction, but TG-DT receives text descriptions that carry explicit numerical task cues (expected return). The paper does not provide a baseline that receives the same text input, so it is difficult to attribute TG-DT's advantage solely to the alignment mechanism. A fair comparison would include a version of PDT or DT conditioned on the same text embeddings.

- **Limited evaluation of real-world language input**: The reliance on templated descriptions with metadata is a strong limitation acknowledged by the authors. However, the paper does not evaluate robustness to more natural, free-form instructions (e.g., "open the drawer halfway" without the episode length or expected return). This significantly limits the claimed applicability to human-like language.

### Minor

- **The t-SNE visualizations (Figure 4) are difficult to interpret quantitatively**: The authors report cosine similarity values (~0.34 and ~0.28) but do not provide a baseline comparison (e.g., random text-behavior pairs). The clustering appears somewhat loose, and it is unclear how well the alignment supports generalization.

- **Ablation results in Table 3 show suspiciously high values**: Cheetah-dir returns of 859–958 in Table 3 are much higher than the 549–598 range in Tables 1–2. This suggests a different evaluation setting (perhaps Expert dataset) that is not clearly labeled in the table caption. The inconsistency is confusing.

- **The description-guided data sharing ablation (Figure 5) uses K up to 3**: This is a very small number of trajectories. The paper should discuss why such a small K is used and whether larger K would harm performance.

### Trivial

- The paper mentions momentum encoders and soft targets but provides no ablation or implementation detail. This makes it hard to assess their contribution.

## Nice-to-Haves

- Compare TG-DT with a variant where the test-time description does not include numerical metadata, to isolate the effect of pure language.
- Add a baseline that feeds the same text descriptions into a standard DT or PDT to isolate the contribution of the alignment mechanism.
- Provide quantitative alignment metrics beyond cosine similarity, such as retrieval accuracy (text→trajectory or trajectory→text).
- Include experiments with more diverse, free-form test descriptions to assess robustness.

## Novel Insights

None beyond the paper's own contributions. The key insight—that dual contrastive and matching objectives can align language with temporally extended behavior for zero-shot meta-RL—is the paper's primary contribution.

## Suggestions

- Clearly separate the zero-shot (no fine-tuning) variant from the data-sharing variant in main results, or rename the data-sharing variant to "one-shot/ few-shot adaptation with language guidance".
- Provide a baseline comparison where the same text is used to condition a standard DT, to measure the gain from the alignment module.
- Discuss why the ablation study uses a different dataset quality than the main results—the discrepancy in Table 3 is confusing.
- Add a small experiment with free-form descriptions (without metadata) to demonstrate robustness.

## Score and Decision

The paper addresses a timely and practical problem with a well-motivated technical approach and thorough empirical evaluation. However, the zero-shot claim is partially undermined by the use of numerical metadata in test descriptions and the data-sharing adaptation step. The comparison with baselines also lacks a fair text-conditioned baseline. These issues are major but not fatal, as the core alignment methodology is sound and the experimental results are otherwise strong.

**Score:** 8

**Decision:** Accept

MY FINAL SCORE: <score>8</score>
MY FINAL DECISION: <decision>Accept</decision>
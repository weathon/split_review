## Summary

This paper investigates the reasoning capabilities of Large Language Models (LLMs) in dynamic games of imperfect information, using Dou Dizhu (a popular Chinese card game) as a testbed. The authors establish a duplicate round-robin tournament benchmark for fair evaluation of SOTA LLMs, then propose a novel data construction framework featuring two mechanisms—globally optimal decision alignment via symmetric information (post-hoc validation with full information) and real-time in-game feedback augmentation—to generate high-quality training data. By fine-tuning a 4B-parameter model (Qwen3-4B) on a structured curriculum using this curated data, they demonstrate significant improvements in gameplay proficiency, achieving a duplicate score of +17.25 compared to the baseline's -65.80.

## Strengths

- **Novel data construction framework**: The two proposed mechanisms—globally optimal decision alignment via symmetric information and real-time in-game feedback augmentation—are genuinely creative approaches to addressing the core challenge of imperfect information games. The "post-hoc validation" idea of revealing hidden information after a decision to verify its robustness is particularly elegant and well-motivated.

- **Rigorous evaluation methodology**: The duplicate round-robin tournament design is a principled approach to neutralizing the stochasticity inherent in card games, drawing from competitive bridge. This is a significant methodological contribution that enables fair comparison of strategic skill rather than luck.

- **Impressive empirical results**: The fine-tuned 4B model achieves a +17.25 average duplicate score (from -65.80 baseline), surpassing larger models like Qwen3-8B (-22.35) and Qwen3-14B (-34.85). The ablation study cleanly demonstrates the contribution of each component, with GOFA data providing a clear qualitative leap over victorious-only data.

- **Practical significance**: Demonstrating that a data-centric approach can elevate a small 4B model to outperform much larger models is valuable for cost-effective deployment of strategic AI agents.

## Weaknesses

### Fatal
None.

### Major

- **Insufficient comparison to specialized RL-based methods**: The paper compares only against other LLMs (both SOTA and Qwen family models). There is no comparison against specialized Dou Dizhu AI systems like DouZero (Zha et al., 2021) or other RL-based agents that have achieved superhuman performance. Without this comparison, it's unclear whether the proposed method actually advances the state of the art in Dou Dizhu gameplay or merely demonstrates that LLM fine-tuning can approach the performance of other LLMs. The paper claims to investigate "reasoning capabilities" but doesn't benchmark against the best available game-playing agents.

- **Limited evaluation of generalization**: The paper explicitly acknowledges this limitation but it remains a significant weakness. The entire framework is validated on a single game (Dou Dizhu). The claim that the "core concepts possess strong generalizability" is unsupported by any evidence. Without testing on at least one other imperfect information game (e.g., poker, bridge, or a simpler game), the broader applicability of the method remains speculative.

- **Potential data contamination concerns**: The SOTA LLMs evaluated (GPT-5, Gemini 2.5 Pro, GLM-4.5, etc.) may have been trained on data that includes Dou Dizhu strategies, rules, or even game transcripts from the internet. The paper does not address this potential contamination, which could inflate the apparent performance of these models and make the benchmark less meaningful as a measure of genuine strategic reasoning.

- **The "error" metric is misleadingly defined**: The paper defines "Error" as "a decision that violates the game rules" (Table 3 caption). However, the ablation study shows o4-mini has the lowest error rate (0.16) but the worst score (-43.65), while GLM-4.5 has higher errors (0.43) but the best score (32.75). The paper's interpretation that "reasoning ability and instruction-following capabilities may be in conflict" is plausible but under-explored. A model that makes fewer rule violations but plays terribly is not necessarily demonstrating a meaningful trade-off—it may simply be overly conservative.

### Minor

- **Limited analysis of the feedback mechanism**: The real-time feedback augmentation uses virtual opponents and teammates to evaluate moves, but the paper provides little detail on how these evaluations are calibrated or validated. Figure 4 shows a distribution peaking around 4-5 with a threshold at 6, but there's no analysis of whether this threshold is optimal or how sensitive results are to it.

- **Small number of benchmark deals**: The benchmark uses 200 unique deals across 20 tournaments. While the duplicate format mitigates variance, 200 deals is relatively small for a game with 54 cards and complex combinatorial structure. The paper doesn't provide confidence intervals or statistical significance tests for the reported scores.

- **Missing details on prompt engineering**: The paper mentions "dynamically generating prompts based on the game state" (Section 3.2) and refers to Section A.3 for details, but the appendix is stripped. The quality of prompts can significantly affect LLM performance in such tasks, and the lack of prompt templates in the main text makes it harder to assess the methodology.

### Trivial

- The paper uses "GOFA" as an acronym for "Globally Optimal & Feedback-Augmented" but this is not explicitly defined until Section 3.4, making earlier references slightly confusing.

## Nice-to-Haves

- Testing on at least one additional imperfect information game (e.g., simplified poker or a smaller card game) would substantially strengthen the claims of generalizability.
- Comparison against a specialized RL agent like DouZero would contextualize the results within the broader game-playing AI literature.
- Providing confidence intervals or statistical significance tests for the duplicate scores would improve the rigor of the benchmark results.
- Analysis of the types of errors made by different models (e.g., categorization of rule violations) could provide deeper insight into the reasoning failures.

## Novel Insights

The paper's most genuinely novel insight is that the information gap in imperfect information games can be leveraged as a training signal rather than treated as an obstacle. The "post-hoc validation" mechanism—where a model's decision under imperfect information is re-evaluated with full information revealed—creates a natural curriculum for learning robust strategic reasoning. This is conceptually distinct from standard approaches that either ignore the information asymmetry (treating it as a classification task) or rely on massive self-play. The insight that a decision's consistency across informational conditions is a proxy for its strategic quality is both elegant and practically useful. Additionally, the finding that a 4B model fine-tuned on carefully curated data can outperform much larger models (8B, 14B) in the same family is a valuable demonstration that data quality can compensate for model scale in strategic reasoning tasks.

## Suggestions

- Add a comparison against a specialized Dou Dizhu AI system (e.g., DouZero or a simple RL baseline) to contextualize the results within the broader game-playing literature.
- Test the framework on at least one additional imperfect information game (e.g., a simplified poker variant or Leduc Hold'em) to provide evidence for the claimed generalizability.
- Report confidence intervals or standard errors for the duplicate scores in Tables 3-5, and consider statistical significance tests for the key comparisons.
- Provide a more detailed analysis of the feedback score threshold (Figure 4) and its impact on final model performance.

## Score and Decision

The paper presents a novel and well-motivated data construction framework for improving LLM reasoning in imperfect information games, with strong empirical results on the Dou Dizhu benchmark. The duplicate tournament methodology is a genuine contribution to evaluation rigor. However, the lack of comparison against specialized game-playing AI systems and the absence of generalization experiments to other games limit the paper's impact and the strength of its claims. The work is solid and interesting but falls short of the transformative contribution expected for top-tier acceptance at ICLR.

MY FINAL SCORE: <score>6</score>
MY FINAL DECISION: <decision>Accept</decision>
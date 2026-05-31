## Summary

This paper introduces Strata-Sword, a hierarchical bilingual (Chinese-English) safety evaluation benchmark for LLMs that categorizes jailbreak attacks into three levels based on "Reasoning Complexity" (Basic Instruction, Simple Reasoning, Complex Reasoning). The authors define reasoning complexity through three dimensions (Logical Depth, Linguistic Ambiguity, Task Overhead), collect 15 jailbreak attack methods across these levels, and propose several novel Chinese-specific attacks (Character Disassembly, Lantern Riddle, Acrostic Poem). Experiments on 23 LLMs/LRMs show that attack success rates increase with reasoning complexity level, revealing different safety boundaries across models.

## Strengths

- **Novel and well-motivated hierarchical framework**: The decomposition of reasoning complexity into Logical Depth, Linguistic Ambiguity, and Task Overhead provides a principled way to categorize jailbreak attacks. This moves beyond existing benchmarks that treat all attacks as equal or simply focus on breadth/strength.

- **Bilingual coverage with linguistically-motivated Chinese attacks**: The introduction of culturally specific Chinese attacks (character disassembly, lantern riddles, acrostic poems) is genuinely novel and leverages unique properties of logographic writing systems that cannot be replicated in English. This is a substantive contribution to multilingual safety evaluation.

- **Comprehensive empirical evaluation across 23 models**: The experiments span open-source LLMs, open-source LRMs, and closed-source commercial models, providing broad coverage. The results consistently demonstrate the hierarchical relationship (L1 < L2 < L3) across model families, supporting the core claims.

- **Reveals non-obvious insights**: The finding that safety alignment shows cross-lingual imbalance (e.g., Llama safer in English, Qwen safer in Chinese) and that "safety scaling laws" exist within model families are actionable insights for practitioners.

## Weaknesses

### Major

- **Lack of rigorous validation for the "Reasoning Complexity" taxonomy**: The paper defines three levels based on three dimensions, but the categorization of specific attacks into levels appears somewhat ad-hoc. For example, why is "Opposing Response" Level 2 while "Script + Template Embedding" is Level 3 when both involve similar reasoning steps? The criteria for combining "two different factors defined for Level 2" to qualify as Level 3 is not precisely operationalized. Without inter-annotator agreement or formal validation of the complexity hierarchy, the levels feel somewhat arbitrary.

- **Confounding between attack content and reasoning complexity**: The basic instructions are from AdvBench (100 items), but Level 2/3 attacks are transformations of those same base instructions. This means more complex attacks inherently have different surface forms. The observed ASR increase could partially reflect that some transformations produce more effective attacks for reasons unrelated to reasoning complexity (e.g., template embedding makes the attack less detectable by surface-level classifiers). A controlled experiment varying only the reasoning complexity while keeping the attack mechanism constant would strengthen causal claims.

- **Limited novelty of English attacks**: While the Chinese-specific attacks are novel, the English Level 2 and Level 3 attacks are largely combinations/adaptations of existing techniques (CodeAttack, DrAttack, Text Shuffle, Template Embedding, etc.). The paper's main contribution for English is the hierarchical categorization, not new attack methods.

### Minor

- **Single evaluator model (QwQ-32B) for safety assessment**: Using a single LLM to judge safety of responses introduces evaluator bias. Prior work (e.g., on LLM-as-judge) shows that different evaluator models can disagree substantially. Using multiple judges or human validation on a subset would strengthen reliability.

- **Multi-round dialogue concatenation reduces ecological validity**: The authors acknowledge this (Section 5.3) but it's a genuine limitation—concatenating multi-turn dialogues into a single prompt does not replicate the dynamics of sequential interaction where each response builds on previous context.

- **Limited Chinese attack coverage**: While three Chinese-specific attacks are introduced, only 100 Chinese Level 3 instructions exist versus 200 English ones. This imbalance makes Chinese-specific conclusions less statistically robust.

### Trivial

- The bar chart in Figure 2 is visually crowded with text labels that are partially unreadable.

## Nice-to-Haves

- Human evaluation of a random subset of safety judgments to validate the automatic evaluator
- Ablation study separating the effect of reasoning complexity from surface-form features of attacks
- Analysis of which specific risk categories (legal violations, ethical issues, etc.) show different vulnerability patterns across complexity levels
- Release of the exact prompt template used for the QwQ-32B evaluator

## Novel Insights

Beyond the paper's own contributions, the most striking observation is the cross-lingual safety asymmetry: models that are English-dominant in training (Llama, Vicuna) show drastically different safety profiles between Chinese and English, whereas Chinese-pretrained models (Qwen, Oyster) show the reverse pattern. This suggests that safety alignment does not transfer well across languages even when the underlying model has multilingual capabilities, implying that alignment datasets must be carefully balanced across languages rather than relying on cross-lingual transfer. The fine-tuning comparison between Qwen3-8B and DS-Distill-Qwen3-8B is particularly illustrative: English safety improved dramatically while Chinese safety barely moved, directly showing the effect of training data language imbalance.

Another non-trivial insight is that Opposing Response attacks (Level 2) achieve high ASR despite low reasoning complexity—suggesting that "cognitive load" from dual-task framing matters more than pure reasoning depth. This challenges the paper's own framework since it implies that complexity dimensions may not be equally weighted.

## Suggestions

- Provide inter-annotator agreement scores for the attack categorization into levels, or use a formal complexity metric (e.g., minimum reasoning steps needed) to validate the hierarchy
- Run an ablation fixing the base instruction and varying only one complexity dimension at a time (e.g., keep content identical, change only the encoding format) to more cleanly attribute ASR changes to reasoning complexity
- Include human evaluation on a random 10% subset to validate the QwQ-32B safety judgments, with agreement statistics reported

## Score and Decision

The paper makes a genuinely novel contribution by introducing a principled hierarchical framework for reasoning complexity in jailbreak attacks, with particularly strong novelty in the Chinese-specific attacks. The experiments are comprehensive and the insights are useful. However, the lack of formal validation for the complexity hierarchy and potential confounds in the experimental design prevent the paper from achieving the highest tier. The contribution is solid and of interest to the safety community.

MY FINAL SCORE: 8.0<score>8</score>
MY FINAL DECISION: <decision>Accept</decision>
## Summary
The paper introduces **Strata-Sword**, a hierarchical safety benchmark designed to evaluate Large Language Models (LLMs) and Large Reasoning Models (LRMs) based on the "Reasoning Complexity" of jailbreak instructions. The authors categorize jailbreak attacks into three levels (Basic, Simple Reasoning, and Complex Reasoning) based on logical depth, linguistic ambiguity, and task overhead. A significant contribution is the inclusion of Chinese-specific attacks (e.g., character disassembly, lantern riddles) to account for language-specific reasoning challenges. Experiments across 23 models show that while most models handle basic attacks, they remain highly vulnerable to complex reasoning-based jailbreaks, and that LRMs (like DeepSeek-R1 or Oyster) show promise in defending against these sophisticated threats.

## Strengths
- **Principled Taxonomy:** The paper provides a clear and intuitive definition of "Reasoning Complexity" (Logical Depth, Linguistic Ambiguity, Task Overhead), moving beyond simple toxicity metrics to evaluate the cognitive boundaries of safety alignment.
- **Language-Specific Innovation:** The introduction of Chinese-specific jailbreak methods (Acrostic Poems, Lantern Riddles, Character Disassembly) is highly original. It addresses a gap in current safety research which is predominantly English-centric and ignores the unique logographic and cultural features of the Chinese language.
- **Comprehensive Evaluation:** The study evaluates a wide range of models (23 in total), including standard LLMs, specialized LRMs, and state-of-the-art closed-source models (GPT-o1, Claude 3.7), providing a robust snapshot of the current safety landscape.
- **Insightful Findings:** The observation that safety alignment often fails to scale with reasoning capability (i.e., a model can be "smart" but "unsafe" when that intelligence is turned against its own guardrails) is a crucial takeaway for the community.

## Weaknesses
### Fatal
None.

### Major
- **Evaluation Methodology for Multi-turn Attacks:** The authors state that for "Multi-Round Dialogue Attacks," they concatenated all turns into a single input for efficiency. This significantly undermines the validity of the "Logical Depth" claim for this specific attack type, as the model is not being tested on its ability to maintain state or be "led down a path" over time, but rather on processing a long, complex prompt. This likely explains the "relatively low efficacy" noted in Section 5.3.
- **Ambiguity in "Reasoning" vs. "Obfuscation":** While the paper frames the levels as "Reasoning Complexity," several Level 2/3 attacks (like Text Shuffle or ASCII) are arguably more about **pattern matching/robustness to noise** than logical reasoning. The distinction between a model failing because it can't "reason" through the harm and failing because the input is "Out-of-Distribution" (OOD) is not sufficiently disentangled in the analysis.

### Minor
- **Human Baseline/Validation:** There is no mention of whether the generated jailbreak instructions (especially the complex Chinese ones like Lantern Riddles) were validated by humans to ensure they are actually solvable/understandable by a human agent. If a human cannot decode the harmful intent, the model's "failure" to do so might be a sign of safety rather than a lack of reasoning.
- **Metric Sensitivity:** The use of QwQ-32B as the sole evaluator for ASR is a single point of failure. While common, a comparison with human labels or a second model (e.g., GPT-4o) would strengthen the reliability of the results.

## Nice-to-Haves
- A breakdown of ASR by harmful category (e.g., do models reason better about "Chemical Weapons" vs. "Bias"?).
- Discussion on the "Reasoning-Safety Tradeoff": does increasing safety reasoning complexity lead to higher false refusal rates (over-refusal) on benign complex tasks?

## Novel Insights
The most significant insight is the **asymmetry between general reasoning and safety reasoning**. The paper demonstrates that "Large Reasoning Models" (LRMs) are a double-edged sword: while they have the capacity to better understand and thus reject complex jailbreaks, their very ability to follow complex instructions makes them susceptible to "reasoning-based" attacks (like CodeAttack) that bypass shallow safety filters. Additionally, the paper highlights that **cross-lingual safety is not a zero-sum game**; models trained primarily on English data show a "safety gap" when faced with reasoning tasks in Chinese that exploit character-level structures, suggesting that safety alignment must be natively multi-lingual rather than just translated.

## Suggestions
- Clarify the "Multi-turn" experiment: If possible, re-run a subset in a true interactive format to see if the ASR changes significantly compared to the concatenated version.
- Provide a few examples of the "Lantern Riddle" and "Character Disassembly" attacks in the main text or a table to help non-Chinese speakers understand the "Reasoning Complexity" involved.
- Explicitly discuss the "OOD" factor: Is the model failing because it's reasoning, or because it's seeing a format (like shuffled text) it didn't see during safety training?

## Score and Decision
The paper is a strong contribution to the AI safety literature, particularly for its hierarchical approach and its focus on Chinese-specific vulnerabilities. The methodology is sound, and the experimental scale is impressive.

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>
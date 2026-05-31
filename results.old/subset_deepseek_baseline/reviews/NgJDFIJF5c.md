## Summary

This paper introduces **Strata-Sword**, a hierarchical bilingual (Chinese-English) safety evaluation benchmark for large language models (LLMs) and large reasoning models (LRMs). The authors decompose the "reasoning complexity" of jailbreak instructions into three dimensions (logical depth, linguistic ambiguity, task overhead) and categorize 15 attack methods into three levels: Basic Instruction, Simple Reasoning, and Complex Reasoning. They further contribute novel Chinese-specific attacks (character disassembly, lantern riddle, acrostic poem) and evaluate 23 models, revealing that safety failures increase with reasoning complexity and that language-specific vulnerabilities are systematically under-explored.

## Strengths

- **Novel and well-motivated dimension for safety evaluation.** Framing jailbreak robustness in terms of reasoning complexity is a fresh perspective that goes beyond topic breadth or attack strength, providing actionable insight into *why* models fail at different cognitive depths.
- **Bilingual and culturally adaptive design.** The inclusion of Chinese-specific attacks (character disassembly, lantern riddles, acrostic poems) is a significant contribution, demonstrating that language-specific reasoning complexity can expose vulnerabilities missed by English-only benchmarks. This opens a new research direction for multilingual safety alignment.
- **Comprehensive experimental scope.** The evaluation covers 23 models spanning open-source/closed-source, LLMs/LRMs, and safety-tuned variants (Oyster, STAIR, RealSafe). The results document clear scaling laws, temporal trends, and language-dependent safety gaps, offering concrete guidance for developers.
- **Clear operationalization of the hierarchy.** The three-level taxonomy is grounded in three explicit criteria, and each attack method is mapped with transparent reasoning, making the benchmark reusable and extensible.

## Weaknesses

### Fatal

None.

### Major

- **Single-judge evaluation bias.** The paper relies entirely on QwQ-32B as the safety judge. While using an LLM evaluator is common, a single judge may inherit systematic biases (e.g., over-refusal, under-detection of nuanced harm). Cross-validation with a second judge or a small human sample would strengthen reliability.
- **Limited benchmark scale.** 700 instructions total (100 per language-level subset) is relatively small for a benchmark intended to characterize safety boundaries. This limits statistical power for per-attack-type analysis and may miss rare failure modes. Expanding the instruction pool would increase robustness.

### Minor

- **Subjectivity in level assignment.** Some classifications (e.g., Opposing Response as L2, Script+Template as L3) are defensible but not formally validated (e.g., via inter-rater agreement). While the criteria are clear, a small human annotation study would bolster confidence.
- **Uncontrolled confound in Level 2 analysis.** The paper notes that Opposing Response and Template attacks have outlier-high ASR within L2, but does not control for the possibility that these attacks are simply more novel rather than more complex. The distinction between "novelty" and "complexity" is not disentangled.
- **The claim about LRMs' potential is under-supported.** Insight 5 states that LRMs "have the potential to defend against complex attacks" due to reasoning, but the results show distilled LRMs (e.g., DS-Distill-Qwen2-7B) have high ASR on L3 (69.7%). Only heavily safety-tuned variants (Oyster, STAIR) achieve low ASR, which is an artifact of safety training rather than reasoning capacity alone.

### Trivial

- None beyond parser artifacts.

## Nice-to-Haves

- Provide confidence intervals or standard deviations for ASR values to reflect variability across instructions.
- Include a comparison with existing benchmarks (e.g., HarmBench, StrongReject) to highlight what unique coverage Strata-Sword offers.
- Discuss potential overfitting risk: if models are trained on these specific attacks, the benchmark's discriminative power may degrade over time.

## Novel Insights

The central insight is that reasoning complexity is a neglected but critical axis for safety evaluation: many models that appear safe on direct harmful instructions fail catastrophically when the same intent is embedded in even simple reasoning or language-specific cultural formats. The finding that Chinese-character-level attacks (disassembly, acrostic, riddle) achieve high success rates across both Chinese-dominant and English-dominant models reveals a general weakness in current alignment: safety training does not generalize to reasoning over non-alphabetic linguistic structures. This suggests that language morphology itself can serve as an adversarial surface, a point that has been largely overlooked in the safety literature.

## Suggestions

- Validate the safety judge with a second LLM (e.g., GPT-4 or Claude) and report agreement rates, or include a small-scale human evaluation for Level 3 attacks.
- Expand the benchmark to at least 200 instructions per level per language to improve statistical power and enable more fine-grained analysis (e.g., per-topic robustness).
- For the Chinese-specific attacks, provide examples and explain how native speakers perceive the complexity, to strengthen the connection between linguistic theory and attack design.

## Score and Decision

**Score:** 8  
**Decision:** Accept  

MY FINAL SCORE: <score>8</score>  
MY FINAL DECISION: <decision>Accept</decision>
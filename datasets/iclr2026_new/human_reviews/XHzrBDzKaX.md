## Human Reviewer 1

### Summary
This paper introduces VISFACTOR, a benchmark that digitizes 20 vision-centric subtests from FRCT, a well-established cognitive psychology assessment. It covers four domains of human visual cognition: Visualization and Spatial Processing, Perceptual and Closure, Memory, and Reasoning. Additionally, it uses parametric generation to automatically construct unlimited, difficulty-controllable test cases for applicable subtests. Furthermore, evaluations of 20 frontier MLLMs based on VISFACTOR show that the best-performing model only achieves a score of 25.19%.

### Strengths
1. This paper presents the benchmark that grounds MLLM assessment directly in human cognitive factors, thereby infusing psychometric rigor into multimodal evaluation.
2. The paper digitizes all FRCT visual items, designs targeted item variants to avoid random guessing biases, and introduces controllable-difficulty item synthesis specifically for the most challenging subtests—addressing the limitation of finite original test items and enabling scalable, gradient evaluation.
3. Additionally, the paper reduces the average random guessing accuracy via targeted format optimizations (e.g., decomposed multiple choice, grouped consistency, and other rule-based strategies), effectively minimizing score inflation from luck and enhancing the reliability of evaluation results.

### Weaknesses
1. While a parametric generator and "controllable difficulty" design are introduced, the work lacks explicit verification that these difficulty gradients align with human cognitive standards—undermining the benchmark’s validity for mapping model performance to human-like visual reasoning.
2. Though formats like "decomposed multiple choice" reduce random guessing, they raise demands on models’ language logic. Subtle wording differences may cause errors from language misunderstanding (not poor visual reasoning), distorting assessments of true visual capabilities.
3. The dataset  lacks detailed specs for each type’s sample size and clear evaluation criteria—this ambiguity hurts result reproducibility and makes assessing sample statistical sufficiency difficult.

### Questions
1. The paper states that VISFACTOR is derived from FRCT, a well-established cognitive psychology assessment. Does it provide data or analysis to confirm that the performance of human participants on VISFACTOR is consistent with their performance on the original FRCT? 
2. The paper uses parametric generation to create unlimited, difficulty-controllable test cases. What methods or experiments were conducted to verify that these automatically generated cases can accurately distinguish differences in visual cognitive capabilities (e.g., between different MLLMs or between MLLMs and humans)?

### Soundness
2

### Presentation
2

### Contribution
2

### Rating
4

### Confidence
4

---

## Human Reviewer 2

### Summary
This paper examines the limitations of current evaluation methods for large language models (LLMs). Using the “castle in the air” metaphor, it argues that many benchmark results overstate genuine reasoning or understanding, presenting an illusion of competence. The authors introduce a mid-sized dataset (~50K examples) designed to better capture multi-dimensional reasoning and factual grounding. The dataset is constructed through a hybrid process—model generation, human verification, and automatic augmentation.

The paper presents experiments across several reasoning and factual tasks, analyzing model performance and alignment gaps. The results indicate that existing metrics often fail to reflect deeper reasoning quality, and that even top-performing models can exhibit superficial correctness.

### Strengths
1/ The work addresses a central issue in current LLM research—evaluation reliability and interpretability. Its focus on “illusory competence” is well-motivated and aligns with active discussions in the field.

2/ The dataset is thoughtfully constructed using human-in-the-loop curation and adversarial augmentation. This improves diversity and realism compared to purely synthetic benchmarks.

3/ Multiple LLMs are tested across reasoning, factual, and generative dimensions. The analysis includes both quantitative and qualitative components, highlighting systematic model weaknesses.

4/ The paper is well-organized, with logical flow from motivation to conclusion. The “castle in the air” framing adds conceptual coherence and readability.

### Weaknesses
1/ The discussion of reasoning lacks connection to existing cognitive or formal reasoning theories. This reduces the conceptual depth of the argument.

2/ Dataset statistics and evaluation setup could be more transparent—particularly regarding sample sizes per task, statistical significance, and model parameterization.

3/ Providing case studies that how state-of-the-art VLMs try to solve these tasks might bring more insight into the field.

### Questions
Please see the weakness section.

### Soundness
4

### Presentation
4

### Contribution
3

### Rating
8

### Confidence
5

---

## Human Reviewer 3

### Summary
The paper proposes VisFactor, a benchmark that includes 20 vision-centric subtests derived from the Factor-Referenced Cognitive Test (FRCT) battery to evaluate multimodal LLMs (MLLMs) on several human visual cognition factors: visualization and spatial processing, perceptual and closure, memory, and reasoning. The authors (i) digitize FRCT items and standardize text prompts, (ii) redesign response formats to reduce chance accuracy to about 2.9%, and (iii) implement parametric generators for a subset of subtests to control difficulty. They test 20 proprietary and open models and report low absolute scores, where the best model reaches ~25% overall with consistent failures on mental rotation, spatial relations, and figure-ground discrimination. They also analyze where models perform better (memorization with semantic content) and worse (abstract patterns), arguing that current systems rely on concept-label recognition rather than low-level perception.

### Strengths
1. The authors systematically reformulate FRCT items with clear prompts and JSON-formatted responses, making the tasks machine-readable and easy-to-use.
2. The "easy–normal–hard" variants add quantitative control over visual challenge and allow scaling to stronger models.
3. The inclusion of 20 subtests provides broad coverage of low-level and high-level visual cognition skills.
4. The finding that models perform well only when semantic cues exist but fail on abstract or spatial transformations reinforces the known conceptual–perceptual gap in MLLMs.

### Weaknesses
1. Incremental over existing works. The main idea that MLLMs struggle with spatial and perceptual reasoning is consistent with plenty of prior studies [1–4]. Authors claimed it is the "first benchmark that grounds MLLM assessment directly to human cognitive factors". The paper does not provide deeper diagnostic insight or a new analytical perspective in my opinion.
2. Limited psychometric validation. Since FRCT assumes factor independence, validating whether these factors transfer meaningfully to MLLMs (e.g., internal consistency or item-response correlation) is essential but missing.
3. No human baseline under identical protocol. Without re-collected human scores on the digitized tests, the paper’s claim of “human-level gap” is qualitative.
4. Possible data contamination and licensing concerns. FRCT items are not guaranteed to be public domain. The paper should clarify licensing or use only synthetic items. 
5. Overemphasis on reformatting. The benchmark is technically solid but largely an infrastructure contribution. The analysis section should provide more interpretation of why models fail: whether failures stem from vision backbone resolution limits or misalignment between textual and spatial representations.

[1] Fu et al., “BLINK: Multimodal Large Language Models Can See but Not Perceive,” ECCV 2024. \
[2] Cao et al., “What is the Visual Cognition Gap between Humans and Multimodal LLMs?,” COLM 2025. \
[3] Li et al., “Core Knowledge Deficits in Multimodal Language Models,” ICML 2025. \
[4] Zhang et al., “RAVEN: A Dataset for Relational and Analogical Visual Reasoning,” CVPR 2019.

### Questions
1. How did you validate that the digitized FRCT tasks still isolate the intended cognitive factors?
2. Can you report internal consistency (e.g., Cronbach’s alpha) or inter-item correlation to confirm psychometric reliability?
3. Are decoding settings (temperature, reasoning depth, chain-of-thought tokens) consistent across models?
4. Did you check overlap between FRCT images and web-exposed examples that could leak into pretraining corpora?
5. Have you confirmed legal licences to redistribute FRCT content, or will you release only generated data?
6. Can you show a small-scale human baseline to quantify the human–model gap?

### Soundness
2

### Presentation
3

### Contribution
2

### Rating
4

### Confidence
3

---

## Human Reviewer 4

### Summary
This paper introduces VISFACTOR, a benchmark that digitizes 20 vision-centric subtests from the Factor-Referenced Cognitive Test (FRCT) battery , a well-established human cognitive assessment. VISFACTOR spans four key domains: (1) Visualization and Spatial Processing, (2) Perceptual and Closure, (3) Memory, and (4) Reasoning.

The authors evaluate 20 frontier MLLMs, including both closed-source and open-source models . The best-performing model achieves a score of only 25.19%. Failures are consistent across tasks like mental rotation, spatial relation inference, and figure-ground discrimination, regardless of model scale or prompting strategy (CoT). Failure analysis suggests models succeed by relying on interpretable, concept-level representations rather than low-level visual patterns.

### Strengths
- The paper adapts a new benchmark from decades of cognitive psychology research (the FRCT), which is a highly novel and valuable approach.

- The experiment (Figure 3, Table 3) comparing model performance on the MA1 (memory) task using semantically rich images versus abstract figures provides a brilliant and convincing demonstration that models are "cheating" by mapping images to high-level concepts rather than performing low-level visual comparison and memorization.

### Weaknesses
- The paper's framing of MLLM failure in "human-like visual cognition" is weakened by the lack of a contemporary human baseline. The authors compare MLLM performance on a new digital protocol to historical norms from a paper-and-pencil task, which is an invalid comparison due to protocol changes (e.g., digitization, no time pressure). While acknowledged in Appendix C, this is a significant limitation. To substantiate claims about a "human-like" gap, the authors must establish a human "ceiling" by collecting baseline data using the identical VISFACTOR protocol given to the models.

- The paper fails to sufficiently differentiate VISFACTOR from the large body of existing work on abstract visual reasoning. The authors should provide a comprehensive comparison to benchmarks like ConceptARC, MaRs-VQA, and various Bongard Problem datasets. This comparison should articulate the unique cognitive abilities or reasoning types that VISFACTOR isolates which are not already covered by prior work, thus justifying its specific contribution.

- A concern is the benchmark's potential longevity. The authors do not include results from the most recent, publicly available SOTA models (e.g., GPT-5, Gemini 2.5 Pro). It is possible these models already perform at or near the human ceiling, which would render the benchmark "solved" and limit its utility for measuring future progress. The authors should test the strongest available models to demonstrate that VISFACTOR remains a challenging task and that its findings of MLLM "failure" are still relevant.

### Questions
See weaknesses for more details.

### Soundness
3

### Presentation
2

### Contribution
2

### Rating
4

### Confidence
4
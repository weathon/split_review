# The Decrypto Benchmark for Multi-Agent Reasoning and Theory of Mind

- Decision: Reject
- Scores: 5, 5, 8

## Abstract
We propose Decrypto, a novel interactive benchmark for evaluating coordination, competition, and theory of mind (ToM) reasoning capabilities in agentic, foundational AI models. Existing benchmarks often suffer from data leakage, saturation, and lack of interactivity, making it hard to measure the ability of intelligent systems to model other agents' reasoning. To overcome or alleviate these limitations, we introduce Decrypto, a multi-agent benchmark based on a popular, language-based board game and designed to be future-proof for large language models (LLMs). We validate Decrypto's effectiveness through comprehensive empirical evaluations of frontier LLMs, ablation studies, and human-AI cross-play experiments. We show that LLMs do not coordinate well with other LLMs or humans and perform strictly worse than the latter. Specifically, LLMs struggle to reason about the choices of others, even if they use the same underlying model, pointing to a fundamental limitation of current systems.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces Decrypto, an interactive benchmark for evaluating multi-agent reasoning and theory of mind capabilities in foundational AI models. It involves a language-based board game to test coordination, competition, and strategic reasoning. Results show that large language models (LLMs) struggle to coordinate with both humans and other LLMs, indicating significant limitations in theory of mind capabilities compared to humans.

### Strengths
1. The paper introduces a novel benchmark that specifically targets theory of mind capabilities, providing a unique approach to multi-agent reasoning evaluation.

2. It presents a benchmark designed to assess the performance of LLMs in both cooperative and competitive multi-agent environments, which is significant for advancing the field. The benchmark isolates language-based reasoning, offering a focused evaluation of LLMs without requiring complex symbolic or spatial reasoning, enhancing clarity.

3. The proposed benchmark allows for adaptability in difficulty levels, addressing saturation issues in other benchmarks and ensuring scalability for future models.

### Weaknesses
1. The method lacks rigor in controlling for potential confounding variables, which casts doubt on the validity of the observed differences in model performance across experimental settings.

2. The experimental design and descriptions lack precision, particularly in detailing how varying LLM architectures impact theory of mind capabilities, leaving key assumptions and decisions unaddressed.

3. Evaluation metrics appear inadequate, as they rely heavily on average turn length without addressing the potential noise introduced by differing prompt conditions, which may skew the results.

4. The ablation studies are limited in scope and fail to explore the interaction between vocabulary size and hint similarity thoroughly, leaving significant gaps in understanding model robustness. And the comparative analysis with baseline models is poorly justified, as it assumes without evidence that the chosen baselines are representative of the broader capabilities of specialist versus generalist agents.

### Questions
1. In the methodology section, could you clarify how you account for confounding variables when comparing the theory of mind performance across different LLM architectures? 

2. Your evaluation relies significantly on average turn length as a performance metric. Could you elaborate on the rationale behind choosing this metric and explain how you mitigate potential noise introduced by prompt variations? 

3. The scope of the ablation studies appears limited, particularly regarding the interaction between vocabulary size and hint similarity. Could you provide more detailed experiments that explore how these factors interact and influence model robustness? 

4. The selection of baseline models to represent “specialist” versus “generalist” agents seems insufficiently justified. How did you determine that these baselines are representative of broader capabilities within these categories?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes to use a game Decrypto, to evaluate coordination, competition, and theory of mind (ToM) reasoning capabilities in agentic, foundational AI models. They show experiments on LLMs, and human-AI cross-play.

### Strengths
Decrypto introduces a unique  framework for studying language understanding and communication. Unlike traditional benchmarks that rely on static inputs, Decrypto involves dynamic clue-based exchanges where the meaning evolves over time. This setup offers a more naturalistic challenge for AI models, better reflecting the way humans adapt language in interactive and often ambiguous contexts.

### Weaknesses
Looking at the design of the task and its inspiration from Piagets three mountains task , I think this paper falls short as a theory of mind benchmark. The original Piagets three mountains task, primarily tests spatial perspective taking. Likewise in Decrypto, the task only requires players to think about shifting between "clues" or coded language without attributing beliefs or knowledge to others. Since Eve and Alice know each others codes at the end of the round, it could become more of a pattern matching game rather than ToM. Can you please clarify this. The claim is central to the paper.

Also, Decrypto does not seem to require players to reason about or infer others' beliefs—particularly beliefs that could be mistaken or based on incomplete information. I mean, in Decrypto, players decode and interpret clues, but if the gameplay primarily revolves around interpreting words or phrases without attributing or understanding others' mental states (e.g., “they think that we think X”), it does not measure ToM in the way Gopnik and Astington define. Without this, Decrypto would align more closely with tasks focused on communication or strategy rather than Theory of Mind.


References :

Flavell, J. H. (1992). Perspectives on perspective-taking
Gopniks Children's Understanding of Representational Change and Its Relation to the Understanding of False Belief and the Appearance-Reality Distinction
Wellman, H. M., Cross, D., & Watson, J. (2001). Meta-analysis of theory-of-mind development: The truth about false belief

### Questions
Comments 
The paper is a bit hard to read, please try to improve writing
Table 1 is not referred anywhere in the paper!
Couldn't find ablation even though it is referred in the paper
Abstract ends abruptly!
L83: Decrypto isolates language-based reasoning and association, directly leveraging LLMs’ core training objective. Where is this explained?
line 191 values of GPT-4o in the left column are doesn't end, incomplete  sentence
There is no baseline where Humans are intercepted by Humans to know how difficult or easy is this task. I think this is important for the claim about the task evaluating ToM.

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors propose the Decrypto benchmark, a novel interactive evaluation framework for testing multi-agent coordination, competition, and ToM capabilities in AI systems.  Decrypto a popular (and very fun!) boardgame requires agents to reason about other agents' knowledge and decision-making while engaging in both cooperative and competitive gameplay. The benchmark is designed to be future-proof for large language models (LLMs) while avoiding common pitfalls of existing benchmarks like data leakage and lack of interactivity.

### Strengths
- I think it's fantastic and increasingly fruitful when studies leverage approaches from cognitive science to study AI, and in particular when they use boardgames to test (human and) AI capabilities because it provides a controlled environment, but one where you can arbitrarily scale complexity as needed. Decrypto in particular is a great game for testing cooperation, ToM, adherence to RSA, etc. (and is also a great game in general, though no bonus review points for that :-) ). Kelsey Allen et al. beautifully lay out the case for these kinds of studies in their NHB paper "Using games to understand the mind"
- The authors make a compelling case for using games as benchmarks, particularly for evaluating theory of mind capabilities, by drawing clear connections to foundational cognitive science work like the Three Mountain Problem
- The benchmark design thoughtfully eliminates common LLM failure modes (like numerical computation and tokenization issues) to focus specifically on reasoning and coordination abilities
- The empirical evaluation is comprehensive, including ablation studies, human-AI cross-play experiments, and detailed analysis of model performance across different roles
-The authors demonstrate that even state-of-the-art LLMs struggle with this benchmark despite its focus on language-based reasoning, revealing important limitations in current systems

### Weaknesses
 - The theoretical analysis of the benchmark's properties could be strengthened, particularly regarding what specific aspects of theory of mind and coordination are being tested. In particular, this may benefit from leaning on the Rational Speech Act literature
- The authors could expand on how the benchmark's difficulty scales with agent capabilities; while they mention it cannot be saturated, more formal analysis would be valuable
 - The human baseline data collection (9 games) seems limited given the importance of human comparisons in the results section. Crucially, I also don't see important details about the human data collection in the manuscript (what were the demographics of the human players, what was their prior experience with Decrypto, were they compensated for their participation, was the study cleared by IRB, what was the interface that humans saw, etc.)
- The authors could provide more detailed analysis of failure modes; what specific types of reasoning or coordination break down when LLMs perform poorly?
 - A discussion of potential gaming or adversarial strategies would strengthen the benchmark's robustness claims

### Questions
- How do the authors ensure that the keyword corpus provides consistent difficulty across different games?
- Were any metrics considered beyond win rates and game length for evaluating performance?
- Could the authors elaborate on how the benchmark tests different levels of ToM reasoning?
- How sensitive is agent performance to the specific choice of prompts and system messages?
- See weaknesses above for some additional questions

### Soundness
3

### Presentation
4

### Contribution
4

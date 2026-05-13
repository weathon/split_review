# PokéLLMon: A Grounding and Reasoning Benchmark for Large Language Models in Pokémon Battles

- Decision: Reject
- Scores: 3, 8, 3, 5, 6

## Abstract
Developing grounding techniques for LLMs poses two requirements for interactive environments, i.e., (i) the presence of rich knowledge beyond the scope of existing LLMs and (ii) the complexity of tasks that require strategic reasoning. Existing environments fail to meet both requirements due to their simplicity or reliance on commonsense knowledge already encoded in LLMs for interaction. In this paper, we present PokéLLMon, a new benchmark enriched with fictional game knowledge and characterized by the intense, dynamic, and adversarial gameplay of Pokémon battles, setting new challenges for the development of grounding and reasoning techniques in interactive environments. Empirical evaluations demonstrate that existing LLMs lack game knowledge and struggle in Pokémon battles. We investigate grounding techniques that leverage game knowledge and self-play experience, and provide a thorough analysis of reasoning methods from a new perspective of action consistency. Additionally, we introduce higher-level reasoning challenges when playing against human players. The implementation of our benchmark is anonymously released at: https://anonymous.4open.science/r/PokeLLMon.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces a benchmark, PokeLLMon, designed to assess the reasoning capabilities of large language models in interactive environments requiring extensive game-specific knowledge and strategic reasoning. Existing LLM environments tend to be limited by their reliance on commonsense knowledge, so PokeLLMon addresses this by incorporating the complex and dynamic gameplay of Pokémon battles, which require deep understanding of fictional knowledge not commonly found in LLMs. The authors empirically demonstrate that most LLMs, including open-source models, struggle in the Pokémon battle domain due to limited game knowledge and action consistency issues, which makes their benchmark challenging to current LLMs.

### Strengths
One of the main strengths of this paper is its comprehensive evaluation approach. The authors assess LLM performance across multiple dimensions, including game knowledge understanding, action consistency, and strategic reasoning. By using a variety of metrics—such as win rate, battle score, and newly introduced action consistency metrics like switch rate and consecutive switch rate—they provide a detailed analysis of how well models can handle the complex demands of Pokémon battles. Additionally, the evaluation includes comparisons against expert systems and human players, highlighting the models’ strengths and weaknesses in both controlled and real-world scenarios. This thorough approach offers valuable insights into the current limitations of LLMs and may encourage further research.

### Weaknesses
 - While the paper thoroughly evaluates existing LLMs with some modifications, it does not propose or implement a novel baseline that could help inspire further research. This limits the contribution of this work.
- The presentation of some figures in this paper is not clear. In Fig. 1, Fig. 2 and Fig. 4, the text is barely readable.
- Appendix B is empty with only a title.

### Questions
1. In Table 3, there are human players involved in the experiments, but they are "randomly-matched human players from game server". Do you think this result can be biased? I question the reliability of this result because different players may hold very different performance, and the server may match different players for you according to your recent performance. For example, the server may match your opponent according to your Elo score, so the level of your opponent is always close to your own level.
2. What is the process to generate multiple-choice questions for game knowledge examination? And what is the scale of this question dataset?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper introduces PokéLLMon, a new benchmark aimed at testing the grounding and strategic reasoning abilities of large language models (LLMs) within the complex and dynamic setting of Pokémon battles. This benchmark addresses two critical requirements for interactive environments: (1) the need for knowledge beyond what current LLMs contain and (2) tasks that require nuanced strategic reasoning. The benchmark is structured to expose LLMs to unfamiliar knowledge (such as Pokémon type effectiveness and move interactions) and to test their ability to reason and make decisions in adversarial gameplay.

### Strengths
1. The benchmark on Pokémon battles is nice. Those battles are complex even for human to complete. Adding Pokémon in a plus in the LLM benchmark for reasoning and game playing.
2. Clear analysis on evaluation including game knowledge examination, and game performance evaluation.
3. Comprehensive analysis on Reasoning, which is the focus on this benchmark, and introduce "Last Thought" to improve consistency.

### Weaknesses
1. The citation format makes it a little bit hard to read the whole paper. Would you mind changing that? Maybe like:
In other words, LLMs lack experiential grounding Mahowald et al. (2024); --> In other words, LLMs lack experiential grounding (Mahowald et al.,2024);
2. In section 5.2, since RFT and DPO are included, it's natural to consider the combination of PPO (Schulman et al., 2017) with a trained  reward model.

### Questions
1. For some reason, the link provided in the abstract says "expired".
2. Is it possible to include a variation of Voyager (Wang et al., 2023) in the section of reasoning? It would be too hard to construct a skill library for all the Pokémons. Maybe only for one or two Generation 1 Pokémon, like Pikachu and Squirtle? Both of them would have "Tackle", but Squirtle has "Water Gun" and Pikachu has "Thunder Shock".

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper introduces **PokéLLMon**, a new benchmark designed to evaluate the grounding and reasoning capabilities of Large Language Models (LLMs) in the context of Pokémon battles. The authors propose grounding techniques that leverage game knowledge and self-play experience, and they analyze reasoning methods from the perspective of action consistency.

### Strengths
1. **Grounding Techniques**: The exploration of grounding techniques that incorporate game knowledge and self-play experience is insightful and adds value to the research.
2. **Action Consistency**: Analyzing action consistency and introducing techniques to improve it are valuable contributions to the field of interactive LLMs.

### Weaknesses
1. **Code Accessibility**: The provided code link is not accessible, hindering the experiments' reproducibility and the validation of the results.
2. **Lack of Comparison**: The paper does not mention or compare with a similar work available on arXiv, titled "PokéLLMon: A Human-Parity Agent for Pokemon Battles with Large Language Models" (https://arxiv.org/abs/2402.01118).
3.  **Contribution Level**: The paper's contributions are relatively low for a top-tier machine learning conference. The work seems more suitable for workshops or tracks focused on datasets and benchmarks.

### Questions
1. The paper should include a comparison with the similar work mentioned in the review (https://arxiv.org/abs/2402.01118).
2. The author needs to discuss the generalizability of the method in this paper to other decision-making tasks.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces a new benchmark aimed at enhancing the grounding and reasoning capabilities of Large Language Models (LLMs) using the context of Pokémon battles. This benchmark, PokéLLMon, is designed to challenge LLMs with complex, dynamic, and strategic gameplay that goes beyond current models' capabilities by integrating rich, fictional game knowledge.

### Strengths
1. This application to a unique domain (Pokémon battles) itself is novel, as it combines elements of strategic game play with AI training in a way that is not commonly explored in LLM research.
2. The paper is underpinned by robust experimental setups, including comparisons with popular environments in LLM research, demonstrating the benchmark’s effectiveness in identifying gaps in current LLM capabilities regarding game knowledge and strategic reasoning.
3. The paper is well-structured, with a clear exposition of the problem area, the novelty of the PokéLLMon environment, and the methods used for evaluation.

### Weaknesses
1. The specificity of the Pokémon battle environment might limit the generalizability of the findings. While the paper demonstrates significant advancements within this particular domain, it may not be clear how these findings extend to other strategic or adversarial settings outside of gaming. The reliance on specific game mechanics, such as type matchups and move sets, could mean that the observed performance gains are not directly transferable to environments with different underlying rules or dynamics. This raises concerns about the broader applicability of the benchmark for evaluating general reasoning and strategic planning capabilities of LLMs.
2. The requirement for specific knowledge to effectively utilize the PokéLLMon benchmark could deter its use as a standard testing ground compared to more accessible or universally relevant environments. The need for researchers to familiarize themselves with the intricacies of Pokémon battles, including the vast array of Pokémon types, moves, and strategic nuances, could pose a significant barrier to entry. This could limit the adoption of the benchmark within the broader AI research community, particularly among those who may not have prior experience with or interest in the specific domain.

### Questions
1. While the paper provides empirical evaluations, there could be a need for deeper analysis regarding the failure modes of LLMs within this benchmark. Understanding why certain models fail or succeed under specific conditions can offer more nuanced insights into the models’ reasoning and strategic capabilities.
2. In the paper, 'In intense adversarial games, action consistency is an important indicator of performance.' and you give the reason 'LLM frequently switches Pokemon in consecutive steps and wastes chances to attack.' So I think action consistency seems to be narrow as a metric. And it could be better if you give more explanations or experiments to demonstrate its importance beyond the specific gaming task. Or I will take the comments that LastThoughts only conservatively imitates the previous steps to avoid wastes and is limited in LLM reasoning.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces a benchmark called PokeLLMon. The benchmark is based on adversarial gameplay of Pokemon battles, which aims at evaluating LLMs' reasoning and grounding ability. For grounding, the paper studies the effect of two methods, i.e., a retrieval-based method and a learning-based method. For reasoning, the paper also studies how different prompt-based test-time inference methods affect LLMs' reasoning performance. Lastly, they address that LLMs can be easily misdirected by human players' attrition and misdirection strategies.

### Strengths
Here are the strengths w.r.t to different dimensions:

Originality:
1. The paper is the first to propose a benchmark on evaluating LLMs' reasoning and grounding with the game of Pokémon.
2. The paper also finds a new perspective, i.e., action consistency, to evaluate LLMs' reasoning ability.

Quality:
1. The authors have done well-round evaluations and study w.r.t grounding and reasoning in the gameplay of Pokémon, including human evaluation.
2. For the study of grounding and reasoning, the authors have also incorporated various techniques, making their claims more convincing.

Clarity:
1. The paper is well-written and it is easy to follow the authors' ideas while reading.

Significance:
1. The paper studies an important topic, i.e., grounding and complex reasoning in adversarial gameplay for LLMs.

### Weaknesses
Here are some concerns of the paper:
1. The perspective of action consistency is a good point, whereas the actual implementation in the paper seems a bit superficial for me, i.e., the use of consecutive switch rate. Intuitively, a human player would not consecutively switch Pokémon, and for me it is more like a commonsense knowledge instead of something that requires reasoning ability. As is also mentioned in the paper, the LLMs may be easily biased by the prompt, which makes it more confusing whether the performance gain of the test-time inference methods are coming the boosts in LLMs' reasoning or solely coming the reduction of LLMs' biases. Apart from that, I think switch rate sounds more convincing than consecutive switch rate., and a simple sanity check can be forcing the LLMs' not to consecutively switch Pokémon.
2. The analysis in line 408-442 sounds weak and deviated to me. Instead of analyzing how those methods incorporate biases, I would prefer analysis of the actual boost/drop in reasoning ability. I think it would be good to carry out the experiments in a more constrained setting, where the biases can be mitigated.
3. The results in Table 5 are meant for showing that DPO and RFT can improve grounding. However, the table only reports win-rate and battle score, whose improvement may come from either boost in grounding or boost in reasoning. I think it'd be better to do some more studies on this, for example, carrying out knowledge examination on these tuned models.

### Questions
I also have some questions/suggestions for the author:

Suggestions:
1. Maybe an example of inadmissible action would be helpful for the readers that are unfamiliar with Pokémon, since in Table 3, most of the actions in $n=1$ and $n=3$ of the open-source LLMs are inadmissible.
2. typo: rejected sampling -> rejection sampling

Questions:
1. Have you tried incorporating basic rules in the system prompts? I couldn't find any in the appendix but based on my understandings, sometimes the LLMs not only lack of factual knowledge of a game but also fundamental rules/curriculums. Recent works on LLM playing text-based strategic games also follow this fashion [1,2,3]. It may be one of the most basic ways to ground LLMs to play strategic games.

```
[1] Wang, Shenzhi, et al. "Avalon's game of thoughts: Battle against deception through recursive contemplation." arXiv preprint arXiv:2310.01320 (2023).
[2] Light, Jonathan, et al. "Avalonbench: Evaluating llms playing the game of avalon." NeurIPS 2023 Foundation Models for Decision Making Workshop. 2023.
[3] Xu, Yuzhuang, et al. "Exploring large language models for communication games: An empirical study on werewolf." arXiv preprint arXiv:2309.04658 (2023).
```

### Soundness
2

### Presentation
3

### Contribution
2

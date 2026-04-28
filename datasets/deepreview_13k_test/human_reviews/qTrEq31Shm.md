# LongPO: Long Context Self-Evolution of Large Language Models through Short-to-Long Preference Optimization

- Decision: Accept
- Scores: 6, 5, 6

## Abstract
Large Language Models (LLMs) have demonstrated remarkable capabilities through pretraining and alignment. However, superior short-context LLMs may underperform in long-context scenarios due to insufficient long-context alignment. This alignment process remains challenging due to the impracticality of human annotation for extended contexts and the difficulty in balancing short- and long-context performance. To address these challenges, we introduce LongPO, that enables short-context LLMs to self-evolve to excel on long-context tasks by internally transfer short-context capabilities. LongPO harnesses LLMs to learn from self-generated short-to-long preference data, comprising paired responses generated for identical instructions with long-context inputs and their compressed short-context counterparts, respectively. This preference reveals capabilities and potentials of LLMs cultivated during short-context alignment that may be diminished in under-aligned long-context scenarios. Additionally, LongPO incorporates a short-to-long KL constraint to mitigate short-context performance decline during long-context alignment. When applied to Mistral-7B-Instruct-v0.2 from 128K to 256K context length, LongPO fully retaining short-context performance and largely outperforms naive SFT and DPO in both long- and short-context tasks. Specifically, \ourMethod-trained models can achieve results on long-context benchmarks comparable to, or even surpassing, those of superior LLMs (e.g., GPT-4-128K) that involve extensive long-context annotation and larger parameter scales.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper proposes LongPO, a novel approach for extending LLMs' context length through self-evolution and preference optimization. The method leverages the model's existing short-context capabilities to generate preference pairs, using responses from short and long contexts as chosen/rejected samples. The approach incorporates a short-to-long KL constraint to maintain short-context performance while improving long-context handling. The authors demonstrate improvements over baseline Mistral-7B-Instruct, achieving competitive performance with larger models like GPT-4 on long-context tasks.

### Strengths
1. **Novel Framework:**
   - Introduces an innovative self-evolution approach for long-context adaptation
   - Presents a theoretically sound extension of DPO for long-context scenarios
   - Successfully maintains short-context performance during adaptation

2. **Technical Merit:**
   - Well-justified short-to-long KL constraint
   - Clear theoretical foundations and derivations
   - Effective integration of NLL loss for training stability

3. **Results:**
   - Achieves competitive performance with larger models
   - Demonstrates effective preservation of short-context capabilities
   - Shows promising results without external annotation

### Weaknesses
1. **Insufficient Comparisons:**
   - Lacks direct comparisons with recent long-context methods 
    (e.g., "Effective Long-Context Scaling of Foundation Models", "LongLoRA")
   - No analysis against parameter-efficient approaches
   - Missing comparison with fine-tuning-free methods 
    (e.g., "LLM Maybe LongLM: Self-Extend LLM Context Window Without Tuning")

2. **Limited Analysis:**
   - Insufficient analysis of computational costs and training efficiency
   - No investigation of potential combinations with existing methods
   - Limited exploration of different model architectures and scales

3. **Practical Considerations:**
   - Missing discussion of memory requirements
   - Limited analysis of inference-time computational overhead
   - No investigation of scaling behavior with different model sizes


**Suggestions for Improvement**
1. Include comprehensive comparisons with recent long-context adaptation methods
2. Add analysis of computational requirements and scaling behavior
3. Investigate potential combinations with existing approaches
4. Provide more detailed ablation studies
5. Include practical considerations for deployment

### Questions
1. How does LongPO compare with recent methods like LongLoRA in terms of computational efficiency and memory requirements?

2. Could the authors provide comparisons with fine-tuning-free approaches and analyze the trade-offs?

3. Have the authors explored combining LongPO with existing position embedding extension methods?

4. What is the computational overhead during inference compared to other long-context adaptation methods?

5. How does the method scale with different model sizes and architectures?

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
This paper introduces a novel training method, LongPO, which can transfer the alignment capability on short-context to long-context scenarios.
By guiding the model to self-generate the training data and applying a DPO-based training objective, LongPO can greatly improve the model's performance on long-context tasks.
Experiments on the Mistral-7B model show promising results for the LongPO method.

### Strengths
The direction of this paper is correct; long-context alignment is essential for long-context models nowadays.

The method is simple yet efficient; LongPO transfers the model capability from short-context to long-context scenarios by utilizing the KL term.

### Weaknesses
**Method**:
I think the road of the overall approach is right, but the details should be improved. The method in this paper should be applied to the long-context models directly rather than doing both the context scaling and long-context alignment. The iterative self-evolving training is costly and complex, and it's better to directly use the positional extrapolation method (e.g., increase the value of RoPE base and conduct long-context post-training) to extend the context length and then utilize LongPO training to perform the long-context alignment.

**Experiment**: Lack of details for reproducing the experiment. For instance, what are the settings of SFT and DPO for Mistral in Table 1? How much data do you utilize? How long does the training take? There are many settings and details that should be reported since DPO-based methods are often difficult to implement.

**Writing**:
The derivation of RL formulas in the main body makes it difficult to understand the core idea the paper aims to present. I believe that if some of the derivations are included in the Appendix and only key formulas are retained in the main body, the readability will increase.

**Figure**:
There are too many marked arrows in Figure 2 without corresponding textual explanations. To be honest, this figure gives me a rough idea of what the author is doing, but the specific details are not clear.

### Questions
1. Why not utilize the open-source training data as the source data for generating the training data in your paper? I noticed that the authors utilize the Instruction Generation method to ensure the diversity of instructions. However, based on my experiments, the instructions generated from the model have a relatively low quality (especially from the Mistral-7B-Instruct-v0.2 model) compared to the open-source long-form instruction data, e.g., LongAlpaca, namespace-Pt data[1].

2. The experiments are mainly conducted on Mistral-7B-Instruct-v0.2, which already has a 32K context length. Why not conduct experiments on the short-context model (4K) like Llama-2 and the long-context model (200K) like Yi-200K?


[1] Here I provide the link for namespace-Pt data, which I think has a relatively high quality: https://huggingface.co/datasets/namespace-Pt/projects/resolve/main/long-llm.tar.gz

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper primarily talks about ways to reinforce the long-context capabilities of LLMs and proposes a novel method, called LongPO, that enables LLMs, which is solely good at short-context tasks in the beginning, to excel on long-context tasks by learning from self-generated short-to-long preference data. LongPO demonstrates promising long-context alignment performance, while retaining the effectiveness of dealing with short-context tasks. Furthermore, this work shows that large-scale human annotation for extended contexts is no longer necessary to excel the model’s long-context capabilities, which sheds light on doing long-context alignment solely with synthetic data.

### Strengths
- The idea of constructing short-to-long preference data is simple, straightforward, and easy to implement.
- The performance achieved by the proposed method is impressive compared to the baselines used in the paper, even surpassing some well-known proprietary LLMs.
- The proposed method, LongPO, is able to retain the short-context performance by adding a KL constraint term to the objective, which explicitly guides the model to minimize the deviation from its short-context output distribution.
- The paper is well written with related works being presented thoroughly to highlight its significant contribution.

### Weaknesses
- Though the construction process of preference data is pretty clear to me, I’m not fully convinced by the motivation that learning from these paired preference data, in which the longer one is dispreferred, enables the model to excel on long-context capabilities. And the authors haven’t provided good intuition or desired empirical evidence showing why doing preference optimization, where the dispreferred data contains the desired properties, is better than proper baselines, e.g., SFT with high-quality long-context data (in the paper, the SFT baseline is using either chosen short-context data or long-context data, in which the instruction is generated by short-context model).
- The paper doesn’t discuss the bottleneck/limitation of the proposed method. Is LongPO able to scale to much longer contexts, such as 512k, 1 million? When does this method plateaus the performance?

### Questions
Do you think some other ways of constructing preference data using simple and clever rules/metrics, eliminating the need for human annotation but ensuring one of chosen or rejected data has a long context, are able to achieve similar alignment performance as LongPO? For example, thinking of constructing a new preference dataset by sampling some short-context data from the chosen group of existing preference datasets as the new chosen data, and sampling other long-context data from the rejected group of existing preference datasets as the new rejected data.

### Soundness
2

### Presentation
3

### Contribution
2

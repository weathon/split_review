# Communicating Activations Between Language Model Agents

- Decision: Reject
- Avg Score: 5.25
- Scores: 6, 5, 5, 5

## Abstract
Communication between multiple language model (LM) agents has been shown to scale up the reasoning ability of LMs. While natural language has been the dominant medium for inter-LM communication, it is not obvious this should be the standard: not only does natural language communication incur high inference costs that scale quickly with the number of both agents and messages, but also the decoding process abstracts away too much rich information that could be otherwise accessed from the internal activations. In this work, we propose a simple technique whereby LMs communicate via *activations*; concretely, we pause an LM $B$'s computation at an intermediate layer, combine its current activation with another LM $A$'s intermediate activation via some function $f$, then pass $f$'s output into the next layer of $B$ and continue the forward pass till decoding is complete. This approach scales up LMs on new tasks with *zero* additional parameters and data, and saves a *substantial amount of compute* over natural language communication. We test our method with various functional forms $f$ on two experimental setups—multi-player coordination games and reasoning benchmarks—and find that it achieves up to $27.0$% improvement over natural language communication across datasets with $<$$1/4$ the compute, illustrating the superiority and robustness of activations as an alternative "language" for communication between LMs.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a novel approach to enable inter-agent communication among language model (LM) agents through direct activation sharing. The authors argue that using activation states for communication, instead of conventional natural language, enhances computational efficiency and performance. Specifically, the method involves grafting activation outputs from one model’s layer into another’s, combining the information through simple operations (sum, mean, replace) or a learned linear mapping. Empirical evaluations on coordination games and reasoning benchmarks demonstrate promising results, with the activation-based method achieving up to 27% higher accuracy than natural language communication while using only a quarter of the computational resources.

### Strengths
- Innovation in Communication Mechanisms: The paper presents a creative shift from token-based natural language communication to activation-based sharing between LMs. This direction is original and leverages intermediate model states, which theoretically encode richer representations than single-token outputs.

- Compute Efficiency: By bypassing the resource-heavy natural language decoding process, this method reportedly achieves substantial computational savings. This aspect is well-supported with theoretical compute models and validated experimentally.

- Experimental Validation: The experiments are thorough, covering two main setups—coordination games and reasoning tasks across diverse datasets. The paper also explores different activation fusion functions, providing a nuanced understanding of how these choices impact results.

### Weaknesses
 - Interpretability and Debugging Concerns: Activation sharing sacrifices transparency and interpretability, particularly since activations do not translate directly into human-readable information. While the authors acknowledge this, their response is inadequate, failing to consider how the complexity of debugging inter-agent communication is compounded when activations, rather than explicit language, are involved. The lack of interpretability extends beyond simple understanding; it hinders the ability to diagnose failures, identify the source of errors, and develop targeted improvements to the communication protocol. This is a significant practical limitation.

- Sparse Performance Gains on Some Tasks: The empirical results do not uniformly favor activation-based communication. In certain benchmarks, gains are minimal or inconsistent (as in Table 3, where Natural Language Debate occasionally matches or outperforms activation-based approaches). This variability weakens the paper’s claim that activation-based communication is a universal improvement. The inconsistent performance across different reasoning tasks raises questions about the robustness and generalizability of the proposed method, suggesting that its effectiveness may be highly task-dependent.

- Selection of Baselines: The paper uses Natural Language Debate (NLD) as the primary baseline. While relevant, it would have been more compelling if additional baselines were included, such as model merging methods or more advanced methods of multi-agent debate. Limiting comparisons may overstate the efficacy of the proposed approach. The absence of comparisons with other established methods for combining model outputs, such as ensemble techniques or knowledge distillation, makes it difficult to assess the true novelty and effectiveness of the proposed activation-based communication.

- Scalability and Real-world Applicability: The activation-based communication approach seems limited in real-world settings. Many existing LMs, especially proprietary ones, restrict access to activations, limiting the applicability of this approach in settings beyond research or open-source models. This restriction is addressed minimally, without discussing how activation-based communication could be practical for typical API-based LM access. The reliance on direct access to model activations severely restricts the practical deployment of this method, as most real-world applications rely on API access to large language models.

### Questions
- Choice of Activation Fusion Functions: Why were basic functions like sum, mean, and replace chosen over more sophisticated functions that might better capture semantic alignment between models?

- Choice of Layers of Activations to Fuse: What is the effect of the choice of layers to fuse and what is the strategy to choose?

- Behavior with Different Model Architectures: Have you considered whether this approach generalizes effectively across architectures with different layer configurations or attention mechanisms? The focus on models from a single family (LLaMA) may obscure limitations when used with other architectures.

- Application to API-accessible LMs: How does the proposed method scale to real-world environments where only API access is available, such as when interacting with black-box models?

- Missing Reference for LLM-based multi-agent communication: CAMEL: Communicative Agents for "Mind" Exploration of Large Language Model Society (NeurIPS 2023)

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a method for communication between two LMs using intermediate activations from two LMs A and B. Specifically, the paper proposes to take compute partial activations of two LMs upto layers k and j -- followed by a function that merges these two activations in the last token and assign that value to the last token of the second LM. The authors show various kinds of functional forms for activation merging with `replace` being the most effective. Results on synthetic and reasoning datasets show partial improvements over baseline methods although I believe additional experiment details are required to claim the effectiveness of the proposed method.

### Strengths
Strengths:
- The paper proposes a method that uses only last token modification between two LMs which is a more efficient communication technique compared to communicating in raw tokens. Section 3.2 of the paper presents a good analysis of the computational efficiency if the paper.

### Weaknesses
Weakness:
- This method uses the activation replacement only for the last token activation of the LM B with the last token activation of LM A. Therefore, the information of the entire prompt of the LM A, is compressed in the last token. I am not sure how this will be performing compared to natural language dialog especially in cases where the LM A response might incur a long response (with possibly chain of thought for intermediate answer computation). This is because the last token activation activation replacement cannot capture the nuanced response from CoT traces. This might explain the GSM8k performance where the proposed method does not perform well compared to NLD baseline since it requires intermediate steps for answer compuation.
- The experimental details are lacking to claim the effectiveness of the proposed method. For table 2 results on Countries and Tip Sheet, I could not find the details on how k=j=26 was chosen. Was a separate validation set used for choosing this value? Was the same set used to tune the hyperparameters of baseline methods?
- For learning the mapping parameter W, the authors report that since 3072 sentences were used from C4 dataset, the semantic similarity might not be similar to the evaluation tasks. Does learning W in-distribution help the performance? For example, train W on train set of GSM8k and evaluate it on the test set.

### Questions
Please see questions above. Additionally:
- Could you please comment on how this method would perform on reasoning tasks that require intermediate computations via chain of thought? For example, algorithmic tasks in BigBenchHard [1] might require intermediate CoT computations and I am skeptical that a single token replacement at the last token would capture the nuanced information in a complex CoT response.

[1] Suzgun, M., Scales, N., Schärli, N., Gehrmann, S., Tay, Y., Chung, H.W., Chowdhery, A., Le, Q.V., Chi, E.H., Zhou, D. and Wei, J., 2022. Challenging big-bench tasks and whether chain-of-thought can solve them. arXiv preprint arXiv:2210.09261.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes a new "model communication" method, which instead of facilitating debate using the output tokens of the models, does so using the intermediate communications of different models.

The paper motivates it's approach using compute and information-bottleneck arguments, particularly in that in communicating via activations, only one of the model's is required to undergo a full-forward pass, and that the information communicated is richer respectively.

The method shows good results, with the approach outperforming the baselines on coordination games across the board, and with either one of its variants (w and w/o a learnt linear mapping) outperforming the conventional debate baseline on 7 reasoning tasks.

Some interesting analysis is also shown to find the layer combinations for communication between the models, which converge to the same optimal numbers (k,j=26) for different tasks.

### Strengths
**Novel and Interesting Idea** \
This finding could also be related to recent model-merging literature where sharing activations between models both during training and inference improves performance. Multi-agent debate is an important field of study, and discovering new effective and computationally more efficient methods is useful.

I also appreciate the authors attempts to motivate their methods both with mathematical formulations for compute and with more theoretical arguments in terms of the informativeness of the intermediate activations vs. output tokens.

**Good results against reasonable benchmarks** \
The method did compare with the standard debate setup, and did so for both coordination and reasoning type tasks, and outperformed the baselines almost across all of them.

**Useful analysis on intermediate layer sharing** \
The analysis on which layer combinations are optimal (Figure 2) is interesting, and could inspire potential future lines of work in understanding intermediate model activations and communication.

### Weaknesses
1. The approach only works for different model weights. While it is true that the paradigm of debate between different models is interesting, it still is useful to support debate between identical models. One of the arguments of the method is efficiency, but in a practical setting, having  to load different model weights could be impractical.
2. The approach only works for 2 models. One of the key promises of debate is that it can scale model communication to many agents. This approach only showed communication between 2, which only scratches the surface of the larger debate landscape. It would be useful to show how this method compares with traditional debate between more agents, and perhaps attempt to scale the method to such settings.
3. The reasoning results are unclear and inconsistent. While one of the stated highlights of the method is that it is "task-agnostic," in the reasoning benchmark, two different variants of the method (with and w/o learnt linear projection communication bridge) seem to perform inconsistently when compared with each other. For example in some settings, one substantially outperforms the other (HS Psych, AC is much better,  Prof. Law, AC(W) is much better). It would be prudent to analyze and explain why these inconsistencies exist.

### Questions
1. For the reasoning tasks, why were the particular tasks chosen? Can you show results on the whole of MMLU? How about MMLU-Pro?
2. Why do you think AC vs. AC(W) works better for some tasks versus other?
3. Could this technique scale to more models favorably?

### Soundness
2

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper explores the idea of communication between language model agents via activations rather than in natural language. Specifically, activations from an intermediate layer of model A are merged into the activations of an intermediate layer (j) of model B and used as inputs for subsequent layers (j+1) of model B.

The paper presents two types of experiments: coordination games (where A and B have the model params) and collaborative reasoning (where A and B are different models with different sizes). In the former, the experiments show that AC (activation communication) is more effective than natural language communication. In the latter, the experiments find AC improving accuracy against both single model baselines and natural language debates (NLD).

### Strengths
Originality: Activation-based communication between LMs is a novel direction, to the best of my knowledge.
Quality: The paper shows modest quality vs. computation gains against the baselines.
Clarity: The motivations for activation communication are clearly explained.
Significance: Collaboration between multiple language agents is a potentially important direction.

### Weaknesses
[Clarity]
There is some ambiguity in the explanation of the grafting inputs and outputs (see Questions).

[Experiments]
The experiment set-up for the coordination game is not realistic—player A can simply send its text prompt to player B without incurring additional computation, since the models are identical. It would be more realistic if model A is smaller than model B in this case.

An additional baseline for collaborative reasoning is CoT with model B alone. This will illustrate whether the quality gains from A+B comes from additional inference computation.

A useful direction for experiments is to investigate the case of RAG, where the retrieved contents are processed by a small model A (whose activations are potentially pre-computed), while the response is generated by model B.

[Method]
The exploration of the methods seems insufficient. For example, could we use cross attention to incorporate activations from model A to B?

### Questions
In sec 3.1 "replace the activation of the last token"replace the activation of the last token (hB,j )tB ∈ R dB ←− f((hA,k)tA ,(hB,j )tB ) for some function f : R dA+dB → R dB ;"

Does this suggest that the inputs to `f` contain only the activations for the last tokens from A and B and the grafting only affects the activation of the last token of model B?

The computation complexity analysis seems to be contradictory: "here F(P, D) = O(P*D) for non-learned f and O(D^2) when f is the mapping matrix". O(D^2) implies that only the last tokens are used, while O(P*D) seems to suggest that the activations of all prefix tokens are used.

### Soundness
3

### Presentation
2

### Contribution
3

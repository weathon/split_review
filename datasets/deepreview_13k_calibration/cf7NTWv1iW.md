# Hardware-Aware Parallel Prompt Decoding for Memory-Efficient Acceleration of LLM Inference

- Decision: Reject
- Avg Score: 4.25
- Scores: 6, 1, 5, 5

## Abstract
The auto-regressive decoding of Large Language Models (LLMs) results in significant overheads in their hardware performance. 
While recent research has investigated various speculative decoding techniques for multi-token generation, these efforts have primarily focused on improving processing speed such as throughput.
Crucially, they often neglect other metrics essential for real-life deployments, such as memory consumption and training cost.
To overcome these limitations, we propose a novel parallel prompt decoding that requires only $0.0002$\% trainable parameters, enabling efficient training on a single A100-40GB GPU in just 16 hours. 
Inspired by the human natural language generation process,  \ppd approximates outputs generated at future timesteps in parallel by using multiple prompt tokens. This approach partially recovers the missing conditional dependency information necessary for multi-token generation, resulting in up to a 28\% higher acceptance rate for long-range predictions.
Furthermore, we present a hardware-aware dynamic sparse tree technique that adaptively optimizes this decoding scheme to fully leverage the computational capacities on different GPUs.
Through extensive experiments across LLMs ranging from MobileLlama to Vicuna-13B on a wide range of benchmarks, our approach demonstrates up to 2.49$\times$ speedup and maintains a minimal runtime memory overhead of just $0.0004\%$.
More importantly, our parallel prompt decoding can serve as an orthogonal optimization for synergistic integration with existing speculative decoding,
showing up to $1.22\times$ further speed improvement.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a parallel decoding algorithm which approximates future outputs in parallel during generation. They leverage multiple prompt tokens which allow for generating outputs at future timesteps. This approach is similar to prefix tuning, where they append trainable prompt tokens to to predict multiple timesteps in advance (although the future prompt tokens are appended at the end of the prompt). They also leverage a dynamic sparse tree search method that allocates a greater number of prompt tokens to more promising candidate sequences. Their method yields comparable results with other parallel decoding methods with fewer trainable parameters / shorter training time. They also outline how their method can be combined with speculative decoding to increase the efficiency gains from this approach.

### Strengths
- They present a prompt token-based method to adapt the model to perform parallel tree decoding. These tokens are appended to the end of the sequence and tuned to allow for predicting multiple tokens into the future by approximating tokens generated at future timesteps in order to recover missing conditional dependency information.
- Their hardware-aware sparse algorithm dynamically allocates more or fewer tokens to particular branches depending on their probability, and also incorporates hardware constraints when mapping out the tree
- They show significantly lower training time (and number of trainable parameters) relative to existing approaches like Medusa
- They present clear and comprehensive evaluation of their approach in terms of latency as well as memory usage (including inference efficiency as well as training time and memory considerations)
  - This evaluation also includes ablation of different components of their approach (eg. justifying the benefits of tree attention, as well as of their hardware-aware decoding algorithm)
- They also demonstrate that their approach is complementary with existing speculative decoding methods.

### Weaknesses
 - The inference-time speedups relative to other prior decoding approaches like Medusa are relatively minor
- Their approach requires fine-tuning, which may make it harder to adapt for different end use cases depending on training availability  (relative to speculative decoding methods)
- The memory savings at inference time of their approach relative to Medusa is smaller for larger models

### Questions
None (The methodology and evaluation was very clear)

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
1

### Rating Number
1

### Confidence
4

### Summary
This paper looks well written and nicely presented. 

Unfortunately its claim for novelty may be challenged, since the main idea of Parallel Prompt Decoding practically overlaps with one in BiTA paper (https://arxiv.org/html/2401.12522v2), published early this year. It uses the same core idea of learnable tokens fed to transformer model to generate speculative continuation. Below is a quote from BiTA paper method description:
"Thanks to the transformer architectures of LLMs, we leverage multiple learnable placeholder tokens known as mask tokens, empowering language models to generate subsequent consecutive future tokens beyond the last input token. During training and inference, the mask tokens are tasked with producing the probability of their next token in corresponding positions."

Now both papers have somewhat different optimisations applied to the core idea. To name a few: BiTA has learnable prefixes, and tree-based decoding. This paper has hardware-aware optimisation.  The speedup range is comparable, with BiTA claiming 2.54x for Vicuna 13B and this paper claiming 2.49x for the same model, though the measurement methodologies differ.

### Strengths
Some secondary contributions are deserving positive mention, namely hardware-aware optimisation.

Analysis of accuracy across token positions is helpful in determining the method's performance drivers

### Weaknesses
The paper's claim for novelty may be challenged, since the main idea of Parallel Prompt Decoding practically overlaps with one in BiTA paper (https://arxiv.org/html/2401.12522v2), published early this year. It uses the same core idea of learnable tokens fed to transformer model to generate speculative continuation. Below is a quote from BiTA paper method description:
"Thanks to the transformer architectures of LLMs, we leverage multiple learnable placeholder tokens known as mask tokens, empowering language models to generate subsequent consecutive future tokens beyond the last input token. During training and inference, the mask tokens are tasked with producing the probability of their next token in corresponding positions."

Besides an number of weaknesses are probed in the Questions section, namely:
- Lack of proper comparison with Eagle - see Questions section
- Absence of source code (UPD - code found)

The core idea of using learnable tokens appended to the input sequence for parallel decoding is substantially similar to BiTA. While the authors highlight differences in the specific implementation details, such as the ensemble attention mechanism and tree pruning, the fundamental concept of using trainable mask tokens to generate multiple tokens in parallel is shared. The paper does not adequately address this overlap, and the novelty claim is therefore weak. The differences, while potentially valuable, appear to be optimizations on top of a pre-existing idea rather than a fundamentally new approach. The paper would benefit from a more thorough discussion of the similarities and differences with BiTA, and a more nuanced claim of novelty.


### Questions
Unlike some other submission, this one has no implementation code.  I wonder if a private code repository could be provided for review purposes?

The paper is not making a complete comparison with SoTA methods like Eagle. Eagle is mentioned in related work and compared in Table 2 on training duration metric. However, for practitioners, the key metric would be the speedup. Extra RAM and training time may often not be the limited factors. Moreover, pretrained Eagle weights could be downloaded for popular models in seconds. See https://github.com/SafeAILab/EAGLE for the download links.

Could you provide results of your method for more modern models, like Qwen and Llama-3? While Vicuna has been a popular testing base for speculative decoding in the past papers, modern practitioners would be more interested in performance of the method with open source models which are in the top of popular benchmarks.

### Soundness
2

### Presentation
4

### Contribution
1

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper presents Hardware-Aware Parallel Prompt Decoding (PPD), a framework designed to accelerate large language model (LLM) inference by leveraging a guess-and-verify process inspired by speculative decoding. PPD introduces a sequence of trained placeholder embeddings, known as prompt tokens, enabling the LLM to generate multiple tokens in parallel within a single forward pass, improving resource utilization and benefiting throughput. These tokens are then verified simultaneously. Compared with changing the model, using pre-trained embeddings incorporates minimal memory and computation costs in both training and inference while achieving a high acceptance rate. 

To optimize performance across different hardware, the authors also implement both offline and online tree pruning strategies, ensuring efficient parallel processing on varied platforms. Evaluations on 1.4B, 7B and 13B models demonstrate that PPD delivers up to a 2.49x speedup over standard autoregressive models and a 1.07x improvement over the state-of-the-art Medusa framework, with only half of Medusa's training time requirements.

### Strengths
1. PPD effectively uses pre-trained prompt tokens as placeholders, allowing LLM to generate multiple tokens in parallel and significantly boosting throughput.
2. By using prompt tokens instead of changing the model, PPD achieves a state-of-the-art acceptance rate with minimal training overheads.
3. By merging the "Verify" and "Next Guess" steps into a single model execution, PPD improves processing speed and maximizes inference efficiency.
4. PPD incorporates both online and offline decoding tree optimizations, which help maximize performance across various hardware setups.

### Weaknesses
1. ***Modest Improvement over SOTA***: While PPD achieves a notable 2.49x speedup over autoregressive models, its 1.07x advantage over Medusa is less impressive. Given that training Medusa is a one-time effort, the slight difference in training time (1.24 vs. 0.52 hours) may not justify the switch for all use cases. Consider the guessing of Medusa only happens on the last stage, **LMHeads**, PDD introduces more decoding workload as each guess is generated through the entire model. This approach may not sustain speedup benefits on larger models or when handling multiple concurrent requests on hardware with high utilization.
2. ***Accuracy on Larger Models is Unclear***: The acceptance length of PPD decreases when moving from Vicuna-7B to Vicuna-13B, and accuracy lags behind Medusa’s. The paper also only presents cumulative accuracy compared with Medusa on 7B model. Further evaluation on larger models (>30B) would help determine if prompt tokens remain effective at greater scales. 
3. ***Limited Hardware-Awareness***: While PPD includes hardware-aware tree pruning, the optimization is based solely on forward latency for a single request (batch_size=1). The framework’s effectiveness in more congested or multi-request dynamic environments is unclear and warrants further testing. The evaluation is performed on A100 and RTX4090, which are not typical edge devices. The memory saving is also not significant compared with Eagle and Medusa on 7B model.
4. ***Possibly More Incorrect Guesses***: Though merging "Verify" and "Next Guess" improves hardware utilization, it also means the next guess is based on a set of unverified tokens (guessed in the last cycle). It will increase the distance between an accepted token and next token to guess, and cause additional unnecessary computations as only one of those branches is accepted in the end but PDD has decoded on all the branches. It is unclear if all baselines use a unified guess & verify phase, and if the unverified tokens introduce additional errors.

### Questions
1. Could you provide more details on how multi-EPT is trained and used?
2. Could you clarify the x-axis of Fig. 8(a)? It is explained as tree size in 5.4, but decoding 500 branches with just 2.6 average acceptance looks weird.
3. How to combine PDD with speculative decoding and get 1.22x speedup? Did you run draft model on the same GPU? Did you split the verify and next guess into two phases?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The main contributions of the proposed Parallel Prompt Decoding (PPD) method are as follows:

1. PPD introduces prompt tokens that are inserted during the decoding process and achieves a high acceptance rate for long-distance token predictions while preserving output quality. This approach was demonstrated to be parameter-efficient, only requiring tuning a fraction of the parameters.

2. PPD introduces a Hardware-Aware Two-Stage Tree Pruning algorithm, which incorporates a hardware-aware two-stage tree pruning technique that adaptively optimizes the prompt structure of PPD at runtime based on the available compute and memory resources. This allows for efficient deployment across various hardware platforms.

The initial stage is performed offline before the model is deployed. The goal is to reduce the number of prompt tokens in the tree to achieve an optimal tree size. Then the pruning consists of two phases:

1. Candidate Trees Construction: Building trees using only candidate tokens at varying depths, employing algorithms from previous works (e.g., Medusa and Sequoia) to maximize a specific function related to the tree structure.
2. Prompt Tokens Appending: Attaching the maximum allowable prompt tokens to each candidate token from the first step, thereby optimizing the tree structure for better performance.

### Strengths
PPD demonstrates substantial speed improvements, achieving up to 2.49× speedup with a minimal runtime memory overhead of just 0.0004%. It also shows potential for synergistic integration with existing speculative decoding methods, leading to further speed enhancements.

### Weaknesses
1. As shown in Figure 7b, most of the speedup is from the tree attention technique introduced in Miao 2024. The speedup without it seems to be very moderate.

2. Since the speedup mainly relies on the tree attention part, this casts doubt on the effectiveness of using prompt tokens instead of a more direct approach such as Medusa. While the author claims the method to be hardware-aware, there are no detailed studies on how hardware changes affect the workload and thus affect the results presented in the experiments.

### Questions
My concerns are listed above.

### Soundness
3

### Presentation
3

### Contribution
3

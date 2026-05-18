- Decision: Reject
- Scores: 6, 5, 6

## Merged Review

### Summary
The paper proposes a multi-agent framework named Mora that uses open-source modules (e.g., Llama, Stable Diffusion) to replicate Sora’s video generation capabilities. Key techniques include a self-modulation factor for inter-agent coordination, a data-free training strategy that synthesizes training data via large models, and a human-in-the-loop mechanism for data filtering. Evaluated on six video generation tasks, Mora achieves a Video Quality score of 0.800 on VBench text-to-video (surpassing Sora’s 0.797) and a perfect Dynamic Degree of 1.00 for image-to-video generation, outperforming several open-source baselines.

### Strengths
- Comprehensive system covering multiple visual tasks: text-to-image, image-to-image, image-to-video, and video connection, among others.
- Clear writing and well-described pipeline, making the framework easy to follow.
- Leverages off-the-shelf models (Llama, Stable Diffusion) to decompose video generation into subtasks, enabling a generalist approach.
- Data synthesis and human-in-the-loop filtering are used to improve training data quality.
- Code is partially shared in supplementary materials, supporting reproducibility.
- Experimental results show effectiveness, with Mora surpassing existing leading models on several VBench metrics (e.g., text-to-video Video Quality 0.800 vs Sora’s 0.797, image-to-video Dynamic Degree 1.00).

### Weaknesses
- **Limited novelty**: The core idea of using a language model as an agent to call pre-existing visual generation models is not novel. Neither the agent system nor the underlying generation models are contributed by the authors. The technical innovations (e.g., self-modulation) require clearer justification and differentiation from existing approaches. (R1, R2)
- **Self-modulated fine-tuning algorithm is unconvincing**: 
  - The approach is unconventional and lacks supporting citations.
  - Training on only 96 samples (Section 4.2) is insufficient for such a complex task; larger-scale experiments or justification are needed.
  - Training code is not released, making it difficult to assess the methodology based on theory and hyperparameters alone.
  - Visual results (Figures 9–12) show significant artifacts (blurriness, object deformation), raising doubts about the method’s effectiveness.
  - The modulation factor itself is not visualized; it is unclear how it changes during training, its range, or whether it converges. (R1, R3)
- **Data-free training strategy resembles distillation and may cause overfitting**: The approach uses large models to synthesize training data, but this can lead to overfitting to those models. A fair comparison with directly distilling a smaller model is missing; authors should show that the multi-agent system provides clear advantages over such a simpler baseline.
- **Missing quantitative analysis of agent success rates and inference efficiency**: Authors should report agent collaboration speed, accuracy, and robustness to justify the multi-agent approach’s benefits over single-model alternatives. (R1)
- **Inference speed and computational requirements are not discussed**: Compared to state-of-the-art models for each task, Mora’s speed and resource needs are unreported. It is unclear whether any optimizations are implemented to improve efficiency given the multi-component nature. (R2)
- **Potential error accumulation across components**: The framework chains multiple agents, which can accumulate errors. Empirical results or error-mitigation techniques are needed; no such analysis is provided. (R2)
- **Problem definition overemphasizes quality metrics**: The stated goal of maximizing quality metrics while ensuring diversity does not capture all relevant aspects of video generation. In an agent system, collaboration speed, accuracy, and robustness should also be evaluated. (R1)
- **No demo videos, GIFs, or project website**: The paper only shows sampled frames, making it hard to evaluate the temporal quality of generated videos. (R3)
- **Robustness to agent model choices is not tested**: It is unclear how sensitive overall performance is to replacing specific agents (e.g., swapping the text-to-image model for a different architecture). Systematic ablation or robustness analysis is missing. (R3)
- **Why does a multi-step pipeline outperform end-to-end generation?** The claim that combining open-source text-to-image, image-to-video, etc., beats end-to-end open-source models and replicates a closed-source system needs a clearer explanation—e.g., whether the modular design compensates for individual model weaknesses or synergy emerges from the agent collaboration. (R3, also related to novelty concerns in R1)
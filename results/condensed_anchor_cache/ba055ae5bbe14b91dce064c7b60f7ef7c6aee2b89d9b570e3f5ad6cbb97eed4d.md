- Decision: Reject
- Scores: 5, 5, 6, 6

## Merged Review

### Summary
The paper proposes SlowFast-LLaVA (SF-LLaVA), a training-free video large language model that uses a two-stream SlowFast input design. The Slow pathway extracts features at a low frame rate with high spatial detail (e.g., 12×24 tokens), while the Fast pathway operates at a high frame rate with larger spatial pooling (e.g., 6× downsampling) to capture motion cues. The method aggregates features without fine-tuning, enabling an image MLLM to handle videos. Experiments across 8 benchmarks (MSVD, MSR-VTT, NextQA, EgoSchema, etc.) show improvements over existing training-free methods and sometimes match fine-tuned video LLMs.

### Strengths
- **Simple and intuitive idea**: The SlowFast design is conceptually straightforward, inspired by action recognition, and requires no additional training or fine-tuning. (Reviewer 1, 4)
- **Extensive ablations**: The paper provides detailed ablation studies on multiple datasets, focusing on optimal selection of slow/fast resolutions and frame sampling. (Reviewer 1, 2)
- **Diverse evaluation**: Experiments cover 8 video benchmarks demonstrating effectiveness across different tasks (captioning, QA, reasoning). (Reviewer 3)
- **Good presentation**: The paper is well-structured and easy to read. (Reviewer 2, 3)
- **Motivation clear**: The goal of enabling LLMs to handle video inputs without training is reasonable. (Reviewer 3)

### Weaknesses
- **Limited novelty**: The idea of concatenating frame features has been explored in IG-VLM and PLLaVA; the SlowFast improvement is straightforward and incremental. (Reviewer 1)
- **Marginal performance gains**: Improvements over baselines are small (e.g., +1.1% on NextQA; adding the Fast path on top of a 12-frame Slow-only model yields only marginal gains, as stated in line 413). (Reviewer 1)
- **Training-free requirement is under-justified**: Existing methods like PLLaVA and VILA involve only lightweight fine-tuning but achieve better performance. Training-free should be justified by use cases, deployment flexibility, or ability to handle novel domains—this discussion is missing. (Reviewer 1, 2)
- **Incomplete comparisons**:
  - Missing comparisons with strong training-based methods (e.g., VILA). (Reviewer 1)
  - Missing evaluations on comprehensive video-MLLM benchmarks that require both spatial and temporal reasoning: MVBench, VideoMME, VideoVista, MLVU, LVBench (for long videos). (Reviewer 1, 2, 3)
- **Generalization to other image-LLMs not shown**: The method is only applied to LLaVA-NeXT. To be persuasive, it should be tested on other architectures such as BLIP2 (Q-Former), InternVL (pixel shuffle), Ovis (visual embedding table), and Aria (MoE). (Reviewer 2)
- **No analysis of token order and motion learning**: The model resembles a bag-of-words approach. It is unclear whether the order of input tokens matters, whether the model truly captures motion, or whether existing benchmarks actually require motion understanding. (Reviewer 1)
- **Missing ablation in Figure 5**: The results in Figure 5 do not include a baseline without the SlowFast design. (Reviewer 3)
- **Writing issues**: Excessive repetition; the paper is stretched to 10 pages. Table captions (e.g., Table 1) simply restate content without insight. Experiment descriptions repeat accuracy numbers without interpretation. (Reviewer 4)
- **Prompt engineering unexplored**: The impact of prompt variations on zero-shot adaptation is not investigated, which could add substantial value. (Reviewer 4)
- **Potential limitations**: 
  - The method cannot detect precise start/end times of events; fine-grained frame-level descriptions might help but are not explored. (Reviewer 3)
  - Offline feature computation could allow many more tokens, but this advantage is not demonstrated. (Reviewer 1, question)  
  - Zero-shot generalization to out-of-distribution datasets compared to video-trained models (e.g., PLLaVA, VILA) is not tested. (Reviewer 1, question)
- **Minority more positive**: Two reviewers (3,4) rated 6 and found the method effective and the evaluations fair, but still noted the above weaknesses. The other two (1,2) rated 5 and highlighted limited novelty and performance gain.
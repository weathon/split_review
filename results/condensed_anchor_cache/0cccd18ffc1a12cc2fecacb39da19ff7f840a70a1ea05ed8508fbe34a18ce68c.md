- Decision: Reject
- Scores: 5, 3, 3

## Merged Review

### Summary
The paper proposes DeSSeR, a training-free framework that decomposes segmentation into recognition, localization, and segmentation steps by sequentially combining MLLMs (e.g., GPT-4o, CogVLM) with a vision foundation model (SAM). It targets challenging zero-shot tasks: camouflage object detection, anomaly detection, and polyp segmentation. One reviewer (score 5, confidence 4) was substantially more positive, praising the clear logic, thorough experiments, and discussion of limitations. The other two reviewers (scores 3, confidence 4 and 3) were more critical, citing poor writing, limited novelty, missing baselines, and insufficient experimental validation of key claims.

### Strengths
- **Clear logical flow and motivation**: The paper progresses well from problem identification to solution, effectively guiding the reader (R1).
- **Thorough comparative experiments**: Abundant ablation studies and visualizations showcase the effectiveness of the proposed architecture (R1).
- **Dedicated scope and limitations discussion**: Adds depth to the evaluation and contextualization of findings (R1).
- **Training-free method**: Novelty in being training-free for challenging scenarios (R2).
- **Interesting analyses**: Provides analyses revealing abilities and properties of existing MLLMs and LVMs (R2).
- **Broad task evaluation**: Experiments on camouflage object detection, zero-shot anomaly detection, and polyp segmentation verify effectiveness across diverse tasks (R2, R3).
- **Strong zero-shot performance**: Achieves notable improvements over zero-shot baselines (R3). One reviewer (R1) noted ~10%+ improvement in challenging tasks.

### Weaknesses
- **Insufficient technical novelty**: The approach is a direct modular combination of existing models (MLLMs + SAM). The structural design lacks architectural innovation, and performance depends heavily on the chosen models (GPT-4o, CogVLM, SAM) rather than a novel contribution (R1, R3). The relevance to the ICLR community is questioned (R3).
- **Missing key baseline comparisons**: Comparisons are lacking with important relevant methods:
    - GLaMM: Pixel Grounding Large Multimodal Model (R1, R3)
    - SAM 2 (R1)
    - GSVA: Generalized Segmentation via Multimodal Large Language Models (R2)
    - Osprey: Pixel Understanding with Visual Instruction Tuning (R3)
    - LISA is included but is insufficient coverage (R1, R2).
- **Unvalidated claims on multi-instance grounding and target misses**: Section 3.2 states the method addresses these two issues, but no experiments directly demonstrate advantage over prior work. Table 6 uses the VisA dataset, which does not contain multiple targets in all images, making the evidence insufficient (R2, R3).
- **Missing hyperparameter ablation**: No evaluation of sensitivity to key hyperparameters: IoU threshold and gridding layout number (Algorithm 1). Robustness of these settings is not assessed (R2, R3).
- **Poor writing quality**: Numerous typos significantly hinder readability and clarity (R2, R3).
- **Missing appendix**: The paper states the final prompt is in the appendix, but no appendix is provided (R2).
- **Template and formatting issues**: Uses ICLR 2024 template instead of 2025; Figure 3 has small fonts that reduce readability (R1).
- **Missing evaluation on general visual grounding datasets**: Performance of DeSSeR on standard benchmarks (e.g., those from GLaMM, Osprey) is not provided, making generalizability unclear (R3).
- **Request for broader task/dataset validation**: Additional experiments on a wider range of tasks or datasets would strengthen the demonstration of generalizability (R1; overlaps with missing comparison/baseline concerns).
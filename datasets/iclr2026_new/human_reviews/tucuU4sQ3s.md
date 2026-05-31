## Human Reviewer 1

### Summary
This paper proposes NuSA-CL, a memory-free continual learning method that leverages orthogonal weight modulation to mitigate catastrophic forgetting. The approach updates model parameters only along directions orthogonal to previously learned subspaces, thus avoiding interference with past knowledge without storing any exemplars. Experiments on several vision and vision-language benchmarks show that NuSA-CL performs competitively among storage-free approaches but lags behind replay-based methods.

### Strengths
1.	Memory-free design.
The method achieves continual learning without any replay or exemplar storage, offering a clean and theoretically motivated direction for efficient CL.
2.	Strong performance among storage-free models.
Within the memory-free setting, NuSA-CL demonstrates solid results and stable learning behavior across multiple benchmarks.

### Weaknesses
1.	Limited performance.
The method performs worse than all storage-based models, showing limited competitiveness in practical CL scenarios.
2.	Simplicity vs. effectiveness.
The proposed approach is simple, but its results do not convincingly show that such a minimal mechanism can achieve strong continual learning.
3.	Scalability concern.
As also noted by the authors, under extreme lifelong settings the null-space directions may saturate. Without a clear advantage in scalability over storage-based methods, the claimed benefit of being memory-free remains modest.

### Questions
1.	What prevents NuSA-CL from surpassing any storage-based methods in performance, despite its theoretically clean orthogonal design?

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

## Human Reviewer 2

### Summary
NuSA-CL addresses continual learning (CL) by balancing stability (retaining old knowledge) and plasticity (adapting to new tasks). The core idea is a low-rank adaptation strategy that constrains task-specific weight updates to the model’s approximate null-space, minimizing interference with previously learned knowledge and preserving the model’s zero-shot learning ability. Unlike methods that rely on replay buffers or high-cost distillation, NuSA-CL requires minimal computation and memory, making it suitable for resource-constrained scenarios. Experimental results demonstrate that the framework not only maintains strong zero-shot transfer performance but also achieves competitive results on continual learning benchmarks.

### Strengths
1. Introduces the novel idea of updating in null-space directions (Tail), which is conceptually different from previous approaches that focus on Top singular directions or random subspaces. Combines multimodal adaptation and rank-limited updates, which is a creative integration addressing the stability–plasticity trade-off. 
2. Significance Tackles catastrophic forgetting, a central challenge in continual learning. Demonstrates practical low-cost, robust implementation suitable for large-scale models and multimodal tasks. 
3. The paper is well-structured, with clear motivation, methodology, and empirical validation. Extensive ablation studies and visualizations (e.g., subspace and rank analysis) make the mechanisms and design choices transparent. 
4. Strong experimental evaluation, including comparisons with Top/Random subspaces and analysis of rank choices. Shows robustness to hyperparameters and demonstrates practical feasibility with low SVD overhead.

### Weaknesses
1. The method assumes that tasks have sufficiently distinct distributions, enabling interference reduction via orthogonalization or projection. However, when tasks are highly correlated or share overlapping features, the model may struggle to separate old and new knowledge, leading to reduced stability and adaptability.
2. The experimental evaluation is limited to standard vision benchmarks (e.g., CIFAR, ImageNet subsets) with relatively few tasks, focusing only on class-incremental learning. The absence of experiments on more complex multimodal settings such as VQA or image-text retrieval limits the demonstration of generalizability.
3. The method’s performance is sensitive to key hyperparameters, including projection dimension, update ratio, and orthogonalization strength. The lack of an adaptive tuning mechanism may hinder robustness and scalability in real-world, dynamic scenarios.
4. In class-incremental tasks, the method has not been compared with other Parameter-Efficient Fine-Tuning (PEFT) approaches such as LPI, TAM, MoELora，or DIKI, limiting the completeness of its performance validation.

### Questions
1. Q: In class-incremental tasks, NuSACL has not been compared with other PEFT approaches such as LPI, TAM, MoELora, or DIKI. How does it perform relative to these methods in terms of both accuracy and memory efficiency?
2. Q: While NuSACL improves stability via orthogonal projection, catastrophic forgetting may still occur in challenging incremental protocols (e.g., many classes, highly overlapping features). Have the authors quantified forgetting under these extreme settings?
3. Q: Although the method is described as lightweight, how does it scale to large models (e.g., ViT-L/14 or multimodal transformers) where repeated SVD computations might be expensive?

### Soundness
2

### Presentation
2

### Contribution
2

### Rating
6

### Confidence
3

---

## Human Reviewer 3

### Summary
The paper proposes NuSA-CL, a memory-free continual learning method for VLMs (e.g., CLIP). It identifies a low-energy “null” subspace via SVD before each task, constrains low-rank updates to this subspace during training, then merges updates into the backbone to avoid parameter growth. Experiments on MTIL (full/5-shot) and CIFAR-100 CIL show strong performance and efficiency; analyses include rank/null-space dynamics, subspace/rank ablations, and core mechanism ablations.

### Strengths
1. Simple, natural idea: SVD-based separation of principal vs. null-like directions; persistent constraint prevents drift and reduces interference.
2. Truly memory-free and fixed-size: no replay, no task-specific modules; efficient and scalable.
3. Strong empirical results with comprehensive cost reporting; SOTA among storage-free baselines and close to storage-based methods.
4. Clear, informative ablations (Top/Tail/Random; rmax; persistent constraint; multimodal adaptation) and mechanism evidence (effective-rank, null-ratio trajectories).
5. Practical and robust: negligible SVD overhead; stable across energy thresholds; single-GPU training.

### Weaknesses
1. Theory is mostly motivational; tighter links between parameter-space bounds and function-level forgetting would help.
2. Long-horizon spectral drift and null-space quality: Although the method re-computes SVD per task, after many merges the spectrum will evolve. A more systematic study of whether low-energy subspaces gradually become “contaminated” (especially for highly correlated task sequences) and how to monitor/remedy this (e.g., periodic re-orthogonalization, spectral gating) would be valuable.
3. Merged updates limit reversibility; lightweight selective rollback is not explored.
4. Scalability guidance for larger backbones (ViT-L/H) would aid practitioners.

### Questions
See weaknesses.

### Soundness
3

### Presentation
4

### Contribution
3

### Rating
6

### Confidence
4

---

## Human Reviewer 4

### Summary
This work proposes NuSA-CL, a lightweight memory-free continual learning framework to address distributional shifts/novel tasks during real-world CLIP usage. NuSA-CL employs low-rank adaptation and null space constraint via SVD to constrain the update of parameters in a way that has low influence on previous knowledge. The experiments demonstrate its effectiveness among memory-free methods.

### Strengths
1. The theoretical motivation is clear and reasonable.
2. The experiments demonstrate a favorable result among memory-free methods. The analysis and discussions are comprehensive, showing the method's practicality and robustness.

### Weaknesses
1. Storage-free baseline models are not that strong. Then a question is: using null-space may constrain the model expressivity. Is it still able to trade off by increasing the memory cost to get a stronger performance? Or the null-space also constrain the performance upperbound?

### Questions
See weakness.

### Soundness
3

### Presentation
3

### Contribution
2

### Rating
6

### Confidence
4
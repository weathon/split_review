## Human Reviewer 1

### Summary
The paper proposes a new method of replay-free continual learning for CLIP-like vision-language models. The core idea is to retain the statistics of feature correlations called CCA certificates, consisting of top-k singular values and the corresponding subspace in the feature space during continual learning. Additionally, they propose to apply low-rank random projections to the CCA certificates, resulting in the quantities called PI-CCA. Also they propose to marginalize these quantities by perturbations in prompts. By leveraging the PI-CCA, it is expected that the proposed continual learning may be more efficient than explicitly leveraging actual data. Experiments show that the proposed method is superior to the existing replay-free methods in average.

### Strengths
- The paper is clearly written and easy to follow.
- The core idea of retaining correlation statistics seems simple and easy to implement.
- Experimental results show the superiority of the proposed method in average, compared to previous replay-free methods.

### Weaknesses
- The paper appears to violate the official format for submissions, which makes unclear whether the submitted content exceed the paper limit or not if the manuscript were appropriately reformatted.
- The proposed method seems to introduce some computational/storage burden by SVD and the PI-CCA quantities, compared to previous continual learning methods. Also, since retaining of statistic information can also be seen as some kind of replay, it should be compared with replay-based continual learning for fair evaluation.
- One of the motivation of the replay-free method has been privacy protection as discussed in Introduction, but it is unclear whether the proposed method can provably prevent the privacy leakage from the correlation statistics.
- In experiments, the superiority of the proposed method is only shown by averaged results, which may be dominated by a single task with high accuracy by luck.

### Questions
See weaknesses.

### Soundness
2

### Presentation
3

### Contribution
2

### Rating
6

### Confidence
2

---

## Human Reviewer 2

### Summary
This paper introduces PI-CCA, a replay-free continual learning framework for vision-language models (VLMs) that aims to preserve cross-modal alignment geometry during adaptation. The method proposes a compact CCA-based certificate that captures the top-k canonical correlations and subspaces of image-text embeddings, and enforces their consistency across tasks using spectral and subspace-angle losses. Additionally, prompt robustness is encouraged through averaging over prompt perturbations. The approach is evaluated on multiple VL-CL benchmarks and shows strong performance compared to replay-free baselines.

### Strengths
1. The proposed CCA certificate is compact, aligning well with the constraints of continual learning.
2. Extensive experiments across multiple benchmarks (MTIL, X-TAIL, VLCL, ConStruct-VL) demonstrate competitive performance, and the ablation studies are thorough.

### Weaknesses
1. The core components prompt perturbation averaging and subspace-angle preservation are not novel and have been extensively studied in prior work on representation similarity and prompt tuning. Their application to continual learning is incremental and lacks a strong theoretical or empirical justification for novelty. e.g., Orthogonal Over-Parameterized Training (CVPR20),  Controlling text-to-image diffusion by orthogonal finetuning (NeurIPS23) DeLoRA: Decoupling Angles and Strength in Low-rank Adaptation (arxiv 24) PAID: Pairwise Angular-Invariant Decomposition for Continual Test-Time Adaptation

2. The paper does not convincingly demonstrate that preserving CCA geometry is fundamentally more effective than existing regularization or distillation-based methods. The observed gains could be attributed to careful tuning rather than a conceptual breakthrough.

3. The prompt invariance mechanism is relatively simplistic (averaging projectors) and does not explore more sophisticated or adaptive strategies.

4. The method assumes access to a diverse anchor prompt set for certificate construction, which may not be feasible in real-world streaming scenarios.

### Questions
*The use of Frobenius norm between sketched projectors as a surrogate for subspace-angle preservation is intuitive, but can you justify its theoretical soundness? How does it compare to more principled metrics like principal angle distributions?

*The certificate update mechanism involves QR-based orthogonalization and EMA smoothing. Could you clarify whether gradients are propagated through these steps, and if not, how this affects learning stability?

### Soundness
2

### Presentation
3

### Contribution
2

### Rating
4

### Confidence
4

---

## Human Reviewer 3

### Summary
This paper proposes a continual learning method for vision language model.
The proposed method (PI-CCA) attempts to maintain the geometry of image-text alignment without using the past data during continual learning.
To this goal, PI-CCA penalizes the change of the covariance of embeddings of the mini-batch data, which is obtained through SVD.
Experiments demonstrate that PI-CCA outperforms baselines on multi-domain task incremental classification, cross-domain task-agnostic classification, and continual image–text retrieval.
Additionally, the paper evaluates PI-CCA through Ablation study including correlation between geometry and performance.

### Strengths
- This paper is well written. The related work section is well-organized, and the paper maintains a consistent focus on the problem from the introduction to the experiments.
- The proposed method appears moderately novel. The core idea might not be very surprising, but the details of the proposed method seems well designed.
- The experiments demonstrate that PI-CCA is superior, and the ablation study supporting the claim is also well-conducted.

### Weaknesses
- I think the explanation of the proposal method could be improved to be a bit easier to understand. 
The concept of a “certificate” is used, but since I am not familiar with continual learning, I do not understand the definition. An explanation of the term is necessary.

- There are no statistical tests for the main results. There is the following sentence:
"Each configuration is repeated with three different random seeds, and we report the mean and the standard deviation."
However, I cannot find the standard deviation.

- The proposed method is a collection of multiple ideas, and it might remain a bit unclear whether the core idea possesses the generality or universality to influence future research in a broad research area.

### Questions
What impact will the proposed method have in broader fields? 
Are there any ideas that could be applied to other areas of machine learning?

### Soundness
3

### Presentation
3

### Contribution
3

### Rating
6

### Confidence
2

---

## Human Reviewer 4

### Summary
- Proposes PI–CCA, a replay-free continual adaptation method for vision-language models that preserves cross-modal geometry via compact CCA certificates (spectral and subspace info).

- Uses LoRA adapters, EMA covariance updates, and sketched projections for constant memory.

- Adds a prompt-invariance term by averaging projectors over prompt perturbations.

- Shows strong results across VL-CL, retrieval, and structured concept tasks, with analyses linking geometry drift to performance.

### Strengths
- Directly preserves the alignment object (canonical spectrum + subspace) instead of indirect proxies (logits/similarity), giving a principled invariant to target during replay-free continual updates

- Compact, practical design: random orthonormal sketches, LoRA-only updates, and streaming EMAs give constant memory and low overhead, making the method compatible with large frozen backbones used in practice. Empirical Pareto plots show a usable knee (e.g., k=64,h=256) balancing mem/time and performance.

- multi-track evaluation (classification, retrieval, structured concepts, time-continual splits) and consistent ablations demonstrating which components matter (spectral & subspace terms are critical; prompt invariance helps retention). Results place PI–CCA at SOTA among replay-free baselines on their benchmarks.

### Weaknesses
- Certificate dependence on sketching and hyperparameters is described but the randomness/variance from sketch seeds and sketch types needs deeper quantification: how often does a small sketch RNG seed change final retention?

- Experiments focus on ViT-B/16 + LoRA; unclear how PI–CCA scales to much larger backbones or different adapter types (other LoRA ranks, full-finetune, or other PETs).

- Reproducibility caveat: paper promises to release code only at camera-ready due to commercial constraints. for reproducibility during review, providing a compact reference script or a verified pseudocode runner (or smaller toy logs) would greatly help reviewers reproduce core claims.

### Questions
- the paper uses synonym/template jitters and M=4. what happens for (i) larger M, (ii) structured paraphrase generators (back-translation ensembles), or (iii) adversarial prompt shifts?

- how sensitive are results to the initial certificate computed from the frozen model? if the initial certificate is imperfect (noisy prompts or limited anchor set), does PI–CCA converge to a useful invariant or can it get locked to a poor alignment?

### Soundness
3

### Presentation
3

### Contribution
3

### Rating
6

### Confidence
3
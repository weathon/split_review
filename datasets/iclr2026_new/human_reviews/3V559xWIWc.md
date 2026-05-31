## Human Reviewer 1

### Summary
This paper focuses on proposing a tree-aware loss function that explicitly incorporates the tree structure into draft model training to improve the speedup of current SPD. TALF aligns the draft model’s predictions with the target across all branches, mitigating the misalignment. They also improve the tree construction process in drafting with stopping at low further gains. The results show that they can deliver speedup over Eagle2 and HASS.

### Strengths
This paper is technically sound and easy to understand.

The experimental results show the effectiveness of the proposed method.

### Weaknesses
The paper lacks comparison to state-of-the-art methods such as Eagle3.

The paper focuses on generating tree structure and improve the overall MAT to speedup the large language model. However, they only conduct experiments with HuggingFace Transformers framework. Here comes a problem that the method may not have such speedup on the popular inference framework such as vLLM. In fact, HuggingFace Transformers framework does not optimize the speed of LLMs very well, which makes the ratio of the latency of tree generation process smaller. When using vLLM framework where the operations in LLMs are optimized very well, the tree generation process will take more time and reduce the speedup. The author should verify their method on such inference frameworks to show that their method is actually useful in reality.

### Questions
See weaknesses above.

### Soundness
3

### Presentation
3

### Contribution
2

### Rating
4

### Confidence
5

---

## Human Reviewer 2

### Summary
This paper presents a strong contribution to speculative decoding by addressing a clear training-inference mismatch in tree-based methods. The proposed TALF and SALF are novel, well-motivated, and demonstrate significant empirical improvements over state-of-the-art baselines. The work is timely, well-executed, and merits acceptance.

### Strengths
1. Novel and Well-Motivated Problem Formulation:​​ The paper convincingly identifies a critical yet overlooked issue: the misalignment between sequence-based training and tree-based inference in speculative decoding. The motivation is powerfully supported by empirical evidence showing the poor calibration of existing draft models on lower-ranked tokens.
2. ​Effective and Orthogonal Solutions:​​ The two contributions, TALF (training) and SALF (inference), address distinct parts of the pipeline and are shown to be complementary. 
3. ​Extensive and Convincing Empirical Validation:​​ The experiments are thorough, evaluating multiple models (Llama2-7B, Llama3-8B, DeepSeek-R1), diverse tasks, and different sampling temperatures.

### Weaknesses
1. Inadequate Justification for Omitting Feature Loss:​​ The decision to remove the feature regression loss in TALF, a key component of EAGLE and HASS designed to prevent feature drift, is not sufficiently justified. 

2. Limited Discussion on TALF Precomputation and Generalization:​​ The paper lacks details on the computational cost of precomputing draft trees with the target LLM for TALF training. Furthermore, it should be discussed whether fixing the tree structures from a static dataset (ShareGPT) might limit the draft model's ability to generalize to unseen prompt distributions or dynamic tree-building strategies during inference.

3. Ambiguity in SALF Threshold Interpretation:​​ While the SALF threshold is shown to be effective, its intuitive meaning is somewhat ambiguous. A more detailed interpretation of what the threshold value represents in terms of expected probability gain would aid in understanding and practical tuning.

### Questions
1. TALF Generalization:​​ The trees used for TALF training are precomputed on a specific dataset. How does the performance of a TALF-trained model generalize to prompts or domains significantly different from its training data? Is there a risk of overfitting to the specific tree structures generated from ShareGPT?

2. ​Feature Alignment Evidence:​​ Can the authors provide quantitative evidence to demonstrate that a TALF-trained model maintains feature alignment with the target LLM despite the removal of the explicit feature regression loss ?

3. Adaptive SALF Threshold:​​ The SALF threshold is a fixed hyperparameter. Have the authors explored making it adaptive based on runtime statistics to dynamically balance quality and overhead across different stages of generation or tasks?

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

---

## Human Reviewer 3

### Summary
This paper introduces TALF, a tree-aware training loss that aligns a draft model’s predictions with the target LLM across all nodes of a dynamically generated tree, and SALF, an inference-time tree-construction algorithm that stops expanding branches once the expected probability gain falls below a threshold; together they eliminate training-inference misalignment and cut drafting overhead, yielding 15–39 % end-to-end speedups over state-of-the-art speculative decoders without harming output quality.

### Strengths
1. The proposed TALF incorporates tree structure into training, improving alignment across all branches, especially low-probability ones. 
2. SALF reduces drafting overhead by early stopping, improving end-to-end latency without significantly hurting acceptance length. 
3. Together, the TALF and SALF work well with different LLMs (e.g., Llama-2, Llama-3, DeepSeek) and tasks (e.g., MT-bench, HumanEval, GSM8K).

### Weaknesses
1. As mentioned in Line.245, the target model is employed to fix the tree structure in advance. However, the draft model is used to generate the tree structure in SALF, which will incur the inconsistence between training and inference. The detailed computational cost of SALF is expected to provide and what about updating the tree structure after the training is stable (such as half of the total epochs) if the computational cost is acceptable.
2. SALF uses a manually set threshold (th=0.6 by default), which may need tuning for different models or tasks. In Sec. 4.4, th=0.5 is best for Deepseek-R1-Distill-Llama-8B. If th=0.6 is claimed to be better, proper experiments should be presented.

### Questions
Could the proposed method compared to Eagle-3 or combined with Eagle-3?

### Soundness
3

### Presentation
2

### Contribution
3

### Rating
6

### Confidence
5

---

## Human Reviewer 4

### Summary
The paper introduces an inference-aware drafter training method by supervision on the tree-decoded tokens of a drafter to align with the target model. Specifically, authors propose a new loss function (TALF) which is a cross-entropy sum for all tree nodes of the drfater model and the new tree-construction mechanism (SALF) which imposes conditional stopping-criterion for reducing the drafter overhead.

### Strengths
* The paper introduces inference-aware training of the drafter, which is novel and makes sense in SD literature given that latest method often depends on tree-decoding of the drafter. 
* Experiments are conducted with multiple models and datasets and results are solid.
* Presentation is clear and ablation are properly studied.

### Weaknesses
* **More advanced baselines** : Authors compare the TALF & SALF with EAGLE-2 and HASS. However, more recent methods like EAGLE-3 [1] improves the performance of EALGE-2 by a large margin, so the proposed method should be compared or combined with [1] ([1] also removes feature alignment loss which alignes with the argument in ln 254).  

* **Experiment details** : Some of the experiment setting is unclear or not fair. In ln 352, why taking different approaches for llama series and. Moreover, performance improvement along trained token numbers is lacking. 

* **Hyper-parameter sensitivity** : While the authors conducted some ablations on hyper-parameters, naive grid search for SALF threshold (Table 4) and choosing N, B in inference stage weakens the practicality of the algorithm in real serving scenario.

### Questions
* What's the size of the drafter models for the experiments? Can author provides the effects of size of the drafter?

* Can author show the scaling effect of the new training algorithm as in EAGLE-3 [1]?

* Can author provide experiment results on other GPU type if possible?

* How does the hyper-parameters N, B, $\tau$ are selected?

[1] (Li et al.) EAGLE-3: Scaling up Inference Acceleration of Large Language Models via Training-Time Test

### Soundness
2

### Presentation
3

### Contribution
2

### Rating
2

### Confidence
3
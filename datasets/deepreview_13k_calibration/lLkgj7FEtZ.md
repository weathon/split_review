# Differentially Private Steering for Large Language Model Alignment

- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 6, 6, 8

## Abstract
Aligning Large Language Models (LLMs) with human values and away from undesirable behaviors (such as hallucination) has become increasingly important. Recently, steering LLMs towards a desired behavior via activation editing has emerged as an effective method to mitigate harmful  generations at inference-time. Activation editing modifies LLM representations by preserving information from positive demonstrations (e.g., truthful) and minimising information from negative demonstrations (e.g., hallucinations). When these demonstrations come from a private dataset, the aligned LLM may leak private information contained in those private samples. In this work, we present the first study of aligning LLM behavior with private datasets. Our work proposes the \textit{\underline{P}rivate \underline{S}teering for LLM \underline{A}lignment (PSA)} algorithm to edit LLM activations with differential privacy (DP) guarantees. We conduct extensive experiments on seven different benchmarks with open-source LLMs of different sizes (0.5B to 7B) and model families (LlaMa and Qwen). Our results show that PSA achieves DP guarantees for LLM alignment with minimal loss in performance, including alignment metrics, open-ended text generation quality, and general-purpose reasoning. We also develop the first Membership Inference Attack (MIA) for evaluating and auditing the empirical privacy for the problem of LLM steering via activation editing. Our attack is tailored for activation editing and relies solely on the generated texts without their associated probabilities. Our experiments support the theoretical guarantees by showing improved guarantees for our \textit{PSA} algorithm compared to several existing non-private techniques.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper studies the private streering for large language models alignment via activation editing. Based on previous work that (update to complete the summary, no change for other comments) computing the activations of several layers could align model with human values, this work propose PSA to privatize the average of activations of each layers to protect the sensitive data with differential privacy. The evaluations include multi-choice and open-ended generations tasks ranging the alignment performance and the general capabilities. This work also did empirical privacy leakage estimation for the proposed method.

### Strengths
The experiments are thorough, measuring the alignment performance, text generation quality, general capability, and designing privacy evaluation.

### Weaknesses
1. One non-private baseline is missing. Wu et al. 2024 provides the non-private baseline both for setting $\sigma=0$ for their methods and original non-private method. It seems to me that this work only provides the non-private one while the $\sigma=0$ is missing. It would be helpful to understand the clipping impact. For example, it seems to me that the norm of the non-private activations steering is unknown and maybe it shows different distribution than the norms are all within 1. If so, it is unclear to me why the private version and non-private version has similar performance.

2. The technical contribution is limited. The non-private version is to compute the activation and average, and the private method proposed in this work is to privatized such mean value. I appreciate the experimental evaluation, and I think it would be helpful to provide the codebase to improve reproducibility. Besides, I wonder if there is any reference for the mean steering and other advanced steering (no new experiments for this result needed, more like a reference). It would be also better to provide the privacy parameters $\sigma$ to improve reproducibility.  For example, when stating $\delta=1/(5n)$, I wonder if it is $\delta=1/(5n)$ for the full model? If so, then each layer should allocate $\delta=1/(25n)$ with 5 layers as editing. Similarly, it is unclear the $\varepsilon=2$ in Table 2 is for the all five layers or just a single layer. Also, the privacy estimation seems to be very tight for PSA ($\varepsilon=1.6$ vs $\varepsilon=2$), while prior work like Nasr et al. 2021 needs to design gradient canary rather than input canary and train more than 10k models to achieve such tight analysis. As empirical privacy estimation only provides the the lowest $\varepsilon$, it would be helpful to provide the privacy parameters to understand the canary property in this case.

### Questions
See above.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper investigates the topic of differentially private (DP) inference-time alignment for large language models (LLMs). The proposed approach builds on existing "linear steering vector" methods, which use labeled data to compute a directional vector by contrasting mean representations of positive and negative samples, then add the directional vector to the test-time representation to steer outputs toward the desired alignment objective. The paper establishes a DP guarantee for this alignment process through DP mean computation. Experimental results demonstrate that this DP alignment method achieves reasonably good alignment performance (sometimes comparable to its non-private counterpart) with relatively low privacy costs on standard LLMs and benchmark datasets.

### Strengths
- The paper is clearly presented and easy to follow.
- The proposed approach is intuitive and straightforward to implement.
- Experimental results demonstrate promising outcomes, suggesting that this DP alignment method could be readily applied in practice.

### Weaknesses
 - The approach is a straightforward application of DP mean computation for the alignment vector, which limits the technical contribution of this work.
- Although the topic is novel and could be a promising area for further investigation, the current motivation lacks clarity, particularly around why alignment should be considered a privacy concern. This is especially relevant given that steering could largely be achieved with public (non-sensitive) data, and (non-DP) mean computation is generally regarded as a low-risk operation (as also evidenced in the experimental results).
- The experiments, while indicating potential, currently feel more like proof-of-concept tests rather than a comprehensive study that would meet the standards of a top-tier conference.

- While rigorous privacy guarantees are generally valuable, the authors could better motivate the topic or provide more natural application scenarios for DP alignment. As noted, (1) alignment could largely be achieved with public data, (2) non-DP linear alignment generally poses low privacy risk, as the "mean" operation aggregates population-level information, reducing individual influence, and (3) the threat model could be clarified further, with comparisons of attack performance under various scenarios to highlight potential privacy threats.

- The description in Section 6 could be more detailed. Adding a formal presentation, diagram, or pseudocode for the attack would improve clarity and self-containment. Additionally, more guidance on selecting canaries and evaluating sensitivity with different choices would be beneficial.

- To enhance the study’s completeness, the experiments could include sensitivity analysis to different clipping bounds (a key factor in practical DP applications), performance across varying epsilon/noise scales, results on diverse datasets across different modalities or semantics, and comparisons of alignment performance on public vs. private datasets (considering potential distribution shifts). Including results with language models of varying structures would also provide a broader perspective.

- Could the authors clarify how PCA steering is conducted (e.g., using labels in a supervised manner)? The notably low performance of PCA steering compared to other methods is somewhat surprising and warrants further explanation.

- In Figure 3, the "zero-shot" reference line appears to be missing for "AI Coordination" on "Llama-2 7B."

- The placement of qualitative examples for Sections C.6 and C.7 in the Appendix could be adjusted to improve readability.

### Questions
- While rigorous privacy guarantees are generally valuable, the authors could better motivate the topic or provide more natural application scenarios for DP alignment. As noted, (1) alignment could largely be achieved with public data, (2) non-DP linear alignment generally poses low privacy risk, as the "mean" operation aggregates population-level information, reducing individual influence, and (3) the threat model could be clarified further, with comparisons of attack performance under various scenarios to highlight potential privacy threats.

- The description in Section 6 could be more detailed. Adding a formal presentation, diagram, or pseudocode for the attack would improve clarity and self-containment. Additionally, more guidance on selecting canaries and evaluating sensitivity with different choices would be beneficial.

- To enhance the study’s completeness, the experiments could include sensitivity analysis to different clipping bounds (a key factor in practical DP applications), performance across varying epsilon/noise scales, results on diverse datasets across different modalities or semantics, and comparisons of alignment performance on public vs. private datasets (considering potential distribution shifts). Including results with language models of varying structures would also provide a broader perspective.

- Could the authors clarify how PCA steering is conducted (e.g., using labels in a supervised manner)? The notably low performance of PCA steering compared to other methods is somewhat surprising and warrants further explanation.

- In Figure 3, the "zero-shot" reference line appears to be missing for "AI Coordination" on "Llama-2 7B."

- The placement of qualitative examples for Sections C.6 and C.7 in the Appendix could be adjusted to improve readability.

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper addresses the challenge of aligning Large Language Models (LLMs) with human values and reducing undesirable behaviors, like hallucinations, by using activation editing—a method that adjusts model activations based on examples of desired and undesired behaviors. When these examples come from private datasets, there's a risk of leaking sensitive information. To address this, the authors introduce the Private Steering for LLM Alignment (PSA) algorithm, which ensures that activation editing respects differential privacy (DP).

### Strengths
S1: Activation editing techniques are appealing because they provide a lightweight alternative to costly iterative optimization, making it easier to adjust LLM behavior efficiently. Consequently, activation editing is emerging as a practical substitute for resource-intensive fine-tuning. However, concerns around potential data leakage risks introduced by these techniques are new, and the solution offered through differential privacy, presents an interesting approach to address these challenges.

S2: Evaluation on seven benchmarks with various open-source LLMs, showing strong alignment with minimal performance loss.

S3: A new Membership Inference Attack (MIA) was designed to empirically evaluate the privacy of LLMs undergoing activation editing.

### Weaknesses
Important details are missing (please refer to the following section: 'Questions').

### Questions
Q1: In Algorithm 2, $\sigma=\frac{2 \sqrt{2 \ln(1.25/\delta)}}{n\varepsilon}$, which implies that $\Delta_f=n/2$. Does this mean that $C_l$ is equal to $\Delta_f$, and thus equal to $n/2$?

Q2: What is the value of $\varepsilon$ per layer in $\sigma$?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper introduces a novel algorithm called Private Steering for LLM Alignment (PSA) to edit LLM activations with differential privacy (DP) for aligning LLMs. The paper provides background on a technique for "steering" LLM inference by editing the activations of a subset of layers. Usually the activations are edited using a learned vector per layer which are added to the activations of the corresponding layer. Usually this vector is learned from a dataset containing paired examples of the form (prompt, positive completion, negative completion). One method to learn this vector called Mean Steering is to take the mean of the difference of the activations on each layer for all the pairs in the dataset. The authors propose PSA which clips the contribution from each paired example and adds calibrated gaussian noise to obtained a private version of the learned vector using the Gaussian mechanism. This private vector per layer can then be used during inference as needed while protecting the privacy of the examples in the alignment dataset. The privacy of the inference can be somewhat controlled by choosing how many layers should the activation editing be applied to. 

The authors also conduct experiments to show the effectiveness of this algorithm compared to Mean Steering and another algorithm called PCA Steering. They align the model using a variety of datasets released as part of Anthropic's "Advanced AI Risk" evaluation. They measure alignment using previously defined benchmarks such multiple choice questions to choose correct behavior and using GPT-4 to rate open-ended text generation. The authors also measure general purpose text generation performance using GPT-4 for open ended text generation and MMLU. The study find that PSA performs similar to Mean Steering and better than PCA Steering for both alignment and general quality and it even outperforms the non-private versions on some benchmarks.

Finally, the study also evaluates empirical privacy of this technique. To test this, the authors propose a novel algorithm which adds a canary containing a prompt token and one of two completion token to the alignment dataset. During inference, the authors add the prompt token in the query and check whether the first completion token is present in the response. They measure the performance of this classifier to obtain an empirical epsilon for the algorithm and find that the algorithm is much more private empirically than the theoretical privacy guarantee.

### Strengths
- The paper introduces a novel algorithm for protecting the privacy of the alignment examples while using it for activation editing. Alignment in LLMs is a very important problem and alignment datasets are usually small and could easily leak any private information that is contained in them.
- The paper is easy to follow and the algorithm and experiments are well explained.
-

### Weaknesses
 - The algorithm is a very simple application of the Gaussian mechanism
- It's not clear how significant the experiments are as there are no error bars. For some of the evaluations, it is not clear how many examples were used.


### Questions
- Is it expected that alignment can improve the performance on MMLU? Many of the alignment numbers seem to be better than Zero-shot.
- For some of the datasets, it seems like the delta would actually be fairly large?

### Soundness
4

### Presentation
4

### Contribution
3

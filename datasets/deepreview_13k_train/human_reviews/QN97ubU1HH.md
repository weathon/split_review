# Model Extrapolation Expedites Alignment

- Decision: Reject
- Scores: 6, 6, 3, 3

## Abstract
The open-source community is experiencing a surge in the release of large language models (LLMs) that are trained to follow instructions and align with human preference.
However, further training to improve them still requires expensive computational resources and data annotations.
\textit{Is it possible to bypass additional training and cost-effectively acquire better-aligned models?}
Inspired by the literature on \textit{model interpolation}, we propose a simple method called \textbf{\methodname{}} to boost LLMs' alignment with human preference.
Utilizing a model that has undergone alignment training (e.g., via DPO or RLHF) and its initial SFT checkpoint, \methodname{} directly obtains a better-aligned model by \textit{\textbf{ex}tra\textbf{po}lating} from the weights of the initial and the aligned models, which implicitly optimizes the alignment objective via first-order approximation. %
Through experiments with twelve open-source LLMs on HuggingFace, we demonstrate that \methodname{} consistently improves off-the-shelf DPO/RLHF models, as evaluated on the mainstream LLM benchmarks AlpacaEval 2.0 and MT-Bench.
Moreover, \methodname{} exhibits remarkable scalability across various model sizes (from 1.8B to 70B) and capabilities.
Through controlled experiments and further empirical analyses, we shed light on the essence of \methodname{} amplifying the reward signal learned during alignment training.
Our work demonstrates the efficacy of model extrapolation in expediting the alignment of LLMs with human preference, suggesting a promising direction for future research.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
In this paper, the authors introduce EXPO, an efficient method for enhancing LLM alignment with human preferences. The core concept of EXPO is that the weights of a partially-trained model can serve as an intermediate result between its initial SFT checkpoint and a hypothetical, better-aligned model. By extrapolating the weights from the initial model toward the partially-trained one, EXPO can efficiently estimate the weights of a better aligned model without additional training steps. Experiments validate the improvement and data efficiency of this approach, showing consistent gains across various open-source LLMs of differing parameter sizes and multiple benchmarks.

### Strengths
+ The important task of efficiency of LLM alignment, and the interesting idea of extrapolating the LLM weights along the direction of the initial model toward the partially-trained one
+ Experiments are done on multimple open-source LLMs and bechmarks

### Weaknesses
 - Lack of enough theoretical analysis
- Some parameters seem difficult to fix (e.g., \alpha) 
- English should be improved

### Questions
- More in-depth discussion of the method is necessary (Why does it work? When does it fail? etc.), For example:  it would be helpful to discuss why extrapolation can enhance alignment while being ineffective for general training.

- Theoretical discussion is missing: there is no theoretically evidence provided to support on the factors contributing to its effectiveness

- Analysis on the selection choice and importance of \alpha across various model sizes

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
The paper introduces Model Extrapolation (EXPO), a novel method designed to expedite the alignment process for large language models. EXPO harnesses model extrapolation to substantially reduce the training overhead associated with traditional alignment methods, such as Direct Preference Optimization (DPO) and Reinforcement Learning from Human Feedback (RLHF). These traditional methods typically require substantial computational resources to fine-tune models to align with human preferences. By extrapolating weights between a supervised fine-tuning checkpoint and an intermediate, partially trained DPO model, EXPO achieves better model alignment with significantly reduced training time. The method is validated through experiments that show improved alignment performance using only 20% of the training steps required by conventional methods. EXPO consistently demonstrates performance gains across multiple open-source large language models (LLMs) on benchmarks such as AlpacaEval 2.0 and MT-Bench.

### Strengths
1.The paper provides theoretical explanation with comprehensive experiment results to show the eﬀectiveness of EXPO.
2. The paper presents thorough experimental results that span various model architectures and alignment techniques, highlighting EXPO’s flexibility and robustness.
3. The results suggest that EXPO could be beneficial, especially for LLMs, as it provides a computationally economical pathway to enhance alignment.

### Weaknesses
1. The core idea of EXPO seems to be a straightforward extension of existing model merge concept, primarily adjusting the interpolation parameter to a negative value (extrapolation). While the results are promising, this incremental shift from interpolation to extrapolation may be seen as lacking in true innovation.
2. Unlike interpolation, which typically operates within a bounded range [0,1], the extrapolation parameter α in EXPO operates within an open range [0, +∞). this open-ended range can complicate the search process, as the optimal value could vary widely depending on the model and training stage.
3. In addition to the open range above, the current manual search for α detracts from EXPO’s eﬃciency and scalability. The authors acknowledge this limitation and suggest future work on optimizing α automatically and adaptively. Having a better way to find the optimal α in this paper will make the innovation more solid.

### Questions
1. Given that α in EXPO operates over an open range [0,+∞), what strategies do the authors suggest for eﬀectively managing and narrowing down the search space for α?
2. The paper mentions that EXPO’s α search process takes less than 0.5 GPU hours, which appears eﬃcient. Could the authors provide a more detailed breakdown of how the search process unfolds? Specifically, how many steps or iterations are typically required, and what is the distribution of time spent in binary search versus grid search?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper presents a method called EXPO for improving the accuracy of language models fine-tuned with DPO/RLHF. The intuition is that model interpolation can produce a model with accuracy in between the original model and the reward-fine-tuned model. So, model extrapolation should be able to produce a model with greater accuracy. By partially training a model, then performing extrapolation, a more accurate final model can be obtained with less compute. The method searches along the line defined by M0 (the initialization for reward-fine-tuning (e.g. the SFT model)) and M1 (the partially-reward-fine-tuned model) to find a more accurate model. The paper presents results for a variety of open-source models.

### Strengths
- The paper studies a method for improving reward-fine-tuned models. This is an important problem in current LLM research.
- The paper is well-written and easy to understand. Figure 2 presents a clear indication of how the method works. Section 2 clearly presents the hypothesis, and the method is neatly summarized by equation 2.
- The results presented are significant. Table 1 demonstrates significant gains in Win Rate using the proposed method. Table 5 demonstrates that the results extend to other models. Table 6 demonstrates the algorithm extends to other alignment methods.
- The paper presents ablations to help understand the method. The ablation in Table 3 (extending the training regime or increasing the learning rate) is particularly important for understanding why the method differs in performance from simply extending training.

### Weaknesses
1) To me, there seems to be a disconnect between the theory presented in Section 2 and the results presented. The results seem to point towards different conclusions that contradict the theory.
  a) Line 192-193: Extrapolation strongly improves the results obtained by "DPO 100%". This is not predicted by the theory presented. The theory presented essentially states, "we can partially train an RLHF model, then predict the result of fully training. The resulting predicted model will achieve the accuracy that would have been obtained by full training". Instead, the results demonstrate that the extrapolation method results in strong gains even when M1 is a fully trained model. (This seems at first like a sign that M1 is undertrained, but this theory is rebuked in Table 3).
  b) Based on the theory, the extrapolated model M2 should be most accurate if the search for M2 occurs along the line between M0 and the "fully trained" M1. This line is approximated by training a proxy (e.g. $M_1 ^{20\%}$) and searching along the line between M0 and the proxy. But for some reason, this proxy yields *better* results than searching the line between M0 and M1 (22.7% win rate compared to 18.0% win rate). Thus, a misalignment of the search space is beneficial to the model. This seems like a clear sign that something not predicted by the theory is causing the benefits in accuracy.
  c) Given the above observations, it seems like the true gains in accuracy could be coming from the fact that ExPO models are selected using a method that finds the best-performing model on the UltraFeedback dev set as calculated by another reward model. If so, this is an interesting discovery in itself, but it's not what the paper focuses on (and it's just a theory that could be completely wrong). My point here is, it seems like the theory presented doesn't match the given results, and there's some other reason for the gains in accuracy.

Line 225-229: The authors are trying to show that $|α \delta \theta|$ is small. They argue that $\alpha$ decreases through training, then conclude that $|α \delta \theta|$ is small. But they do not discuss the fact that $\delta \theta$ is (presumably) increasing during training. This justification seems incomplete/incorrect to me. The argument that $|α \delta \theta|$ is small relies on the assumption that the magnitude of the product decreases, but the authors only show that one term in the product decreases. It's possible that $\delta \theta$ increases at a faster rate than $\alpha$ decreases, which would invalidate the argument. Furthermore, the authors do not specify what $|α \delta \theta|$ is small *compared to*, which is necessary for the Taylor approximation to be valid. The magnitude of $|α \delta \theta|$ needs to be small relative to other terms in the Taylor expansion, and it's not clear that this is the case.

Section 3.4: The authors successfully demonstrate in this section that length bias can be an issue for the method. But this does not prove that length bias is the only issue causing reduced accuracy when training for longer. Also, shouldn't the same logic (length bias being an issue) apply to the standard training procedure? Yet, training for the full recipe produces optimal results, as opposed to training for a fraction of training steps. Why is length bias only an issue for ExPO?

### Questions
The main issue that I'm looking to see resolved is in (1) above. The results of the paper are good, but there seems to be a mismatch between the theory and the method. It leaves me wondering if there's a different reason that the method works. See discussion in (1).

### Soundness
1

### Presentation
4

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper introduces **EXPO** (model extrapolation), a method to improve the efficiency of aligning large language models (LLMs) with human preferences. Instead of fully training models, EXPO extrapolates model weights from a partially-trained model, significantly reducing training time while improving performance. Through experiments, the method shows that models trained with fewer steps can outperform fully-trained ones, validated on benchmarks like AlpacaEval 2.0 and MT-Bench. EXPO is applicable to a wide range of LLMs, making alignment more efficient and less computationally expensive.

### Strengths
1. The paper tackles an important problem—reducing the computational cost of aligning large language models—which is crucial for scaling models efficiently.

2. The explanation of the method is clear and easy to follow, with helpful figures that enhance understanding.

3. The authors show EXPO’s ability to cut down alignment training costs, which supports their claim.

### Weaknesses
1. **Limited theoretical foundation**: The paper presents an interesting empirical finding with E X PO, but lacks a rigorous theoretical analysis of why it works. The discussion in Section 3.3 on why E X PO can work is somewhat speculative. A more formal theoretical treatment, perhaps drawing connections to optimization theory or analyzing the loss landscape, would strengthen the paper's contribution.

2. **Limited analysis of failure cases**: While some negative results are reported (e.g. for KTO algorithm in Table 6), there's little in-depth analysis of when and why E X PO fails. A more comprehensive error analysis would provide insights into the method's limitations.

3. **Limited analysis of extrapolation's impact on model calibration**: While the paper focuses on performance metrics, it doesn't investigate how E X PO affects the model's calibration. An analysis of how extrapolation impacts the model's uncertainty estimates and confidence calibration would be valuable, especially for safety considerations.

4. **Insufficient investigation of extrapolation instability**: The authors mention in Section 4.3 that extrapolating from pre-trained to SFT models can lead to model collapse, but they don't provide a rigorous analysis of this phenomenon.

5. **Lack of analysis on the impact of different λ values in DPO**: In Table 4, the authors test λ values of 0.001, 0.01, and 0.1, but don't provide a detailed analysis of how these different λ values affect the optimization landscape and consequently E X PO's performance. A more granular sweep of λ values and an analysis of how they interact with the optimal α could provide insights into the method's sensitivity to DPO hyperparameters.

### Questions
I encourage the authors to address the points raised in the weaknesses section and to conduct additional experiments where further investigation is required.

### Soundness
2

### Presentation
2

### Contribution
2

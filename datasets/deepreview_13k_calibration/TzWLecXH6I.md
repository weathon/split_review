# Towards Personalized AI: Early-stopping Low-Rank Adaptation of Foundation Models

- Decision: Reject
- Avg Score: 4.25
- Scores: 5, 6, 3, 3

## Abstract
Foundation models, such as Latent Diffusion Models and Generative Pre-trained Transformers, trained on broad data have shown impressive results in various downstream applications. Fine-tuning a pre-trained foundation model is an affordable way to customize it on small and personalized data. However, the non-AI experts often struggle with the hyperparameter configurations and sometimes encounter the overfitting issue without even realizing it. To mitigate this issue, we introduce a new monitoring metric (CS-Fluctuation) to facilitate early stopping the fine-tuning process. Specifically, we leverage Low-Rank Adaptation (LoRA) to fit the small scale of the personalized data while monitoring the cosine similarity of the parameter changes between the LoRA branch and its corresponding layer. When the changes become steady, we observe the onset of overfitting issue which becomes increasingly severe as fine-tuning progresses. Empirically, we leverage various types of personalized data to conduct customization experiments on both vision and language foundation models, which corroborates the effectiveness of CS-Fluctuation in early stopping the LoRA fine-tuning. The code can be found at the anonymous link: \url{https://anonymous.4open.science/r/EarlyStopLoRA-7467/}.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Foundation models have demonstrated impressive performance in a wide range of practical applications after being trained on extensive datasets. Fine-tuning these pre-trained models is a cost-effective way to adapt them to specific, smaller datasets, but non-experts often struggle with hyperparameter settings and risk overfitting without realizing it. To address this challenge, the paper introduces a novel monitoring metric called CS-Fluctuation, which aids in early stopping during the fine-tuning process. This approach combines Low-Rank Adaptation (LoRA) to fit personalized data while continuously monitoring the cosine similarity of parameter changes between the LoRA branch and its corresponding layer. When these changes stabilize, it signals the onset of overfitting, which becomes more pronounced as fine-tuning progresses. Empirical experiments with various types of personalized data on both vision and language foundation models confirm the effectiveness of CS-Fluctuation in early stopping LoRA fine-tuning.

### Strengths
Importance of the Research Problem: The paper addresses a significant issue in the field of AI, namely the challenge of personalizing foundation models. Personalized AI has become increasingly relevant in various applications, making the problem studied in the paper highly important.

Interesting Idea: The concept of early-stopping low-rank adaptation of foundation models is intriguing. It introduces a novel approach to the problem, which could have practical implications in improving the efficiency of personalized AI systems.

Experimental Validation on Multiple Datasets: The authors have conducted experiments on multiple datasets, demonstrating a comprehensive evaluation of their proposed method. This multi-dataset validation enhances the credibility and applicability of their findings.

### Weaknesses
Limited Contribution: While the problem studied is important, the paper may be lacking in terms of innovation. The proposed method, early-stopping low-rank adaptation, may need some inspiration from a theoretical perspective, highlighting how it offers a unique and innovative solution. Specifically, the paper does not provide a clear theoretical justification for why monitoring the cosine similarity of parameter changes is an effective indicator of overfitting. The connection between the stabilization of these changes and the onset of overfitting is not rigorously established, which weakens the claim of novelty.

Unclear Generalization of Metrics: The paper introduces certain metrics, but it's not clear how these metrics can be generalized to other AI applications or datasets. A more thorough discussion of the potential transferability and generalization of the proposed metrics would enhance the paper's impact. Also, it is interesting to explore the performance of CS-Fluctuation for other tuning techniques. The paper only demonstrates the effectiveness of CS-Fluctuation on LoRA, but it is unclear if the same approach would be effective for other fine-tuning methods, such as full fine-tuning or adapter-based methods. The lack of exploration of other tuning techniques limits the generalizability of the findings.

Lack of Real-World Application Discussion: The paper could benefit from a deeper discussion of real-world applications and scenarios where the proposed method might be particularly advantageous. Providing practical use cases and illustrating how the method could address real AI problems would add value to the research. Also, it is interesting to explore the performance of CS-Fluctuation for other tuning techniques. The current discussion of real-world applications is limited to generic examples, and it lacks specific details on how the proposed method would be implemented and what benefits it would provide in these scenarios. A more detailed analysis of practical deployment challenges and advantages would strengthen the paper.

### Questions
Limited Contribution: While the problem studied is important, the paper may be lacking in terms of innovation. The proposed method, early-stopping low-rank adaptation, may need some inspiration from a theoretical perspective, highlighting how it offers a unique and innovative solution.

Unclear Generalization of Metrics: The paper introduces certain metrics, but it's not clear how these metrics can be generalized to other AI applications or datasets. A more thorough discussion of the potential transferability and generalization of the proposed metrics would enhance the paper's impact. Also, it is interesting to explore the performance of CS-Fluctuation for other tuning techniques.

Lack of Real-World Application Discussion: The paper could benefit from a deeper discussion of real-world applications and scenarios where the proposed method might be particularly advantageous. Providing practical use cases and illustrating how the method could address real AI problems would add value to the research.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper introduces CS-Fluctuation, a novel metric for identifying the optimal point during personalized foundation model fine-tuning. This metric enables early stopping to prevent overfitting, especially when applying Low-Rank Adaptation to small datasets. Experiment results on vision and language models confirm CS-Fluctuation's effectiveness in generating high-quality images and accurate text predictions. This metric has the potential to assist non-AI experts in avoiding overfitting and reducing computational costs.

### Strengths
1. Originality: The paper introduces a novel monitoring metric and a fresh approach to pinpoint the turning point in the fine-tuning process, effectively preventing overfitting and reducing unnecessary computational expenses.

2. Quality: The paper provides a detailed algorithm description and comprehensive experimental results, thoroughly validating the effectiveness of the proposed metric and method, spanning both vision and language foundation models.

3. Clarity: The paper is well-structured and maintains clarity in the calculation of CS-Fluctuation. The diagrams illustrating the experiment setup and figures depicting the experimental results further enhance the paper's clarity.

4. Significance: This metric and approach hold particular significance, especially when dealing with limited training data or situations where objective test data is either unavailable or subject to high subjectivity.

### Weaknesses
I overall appreciate the novel idea and significant contribution of this paper, while still having some concerns in the implementation and experimental settings.

1. The proposed metric is effective exclusively for LoRA and doesn't extend to other fine-tuning methods.

2. Excessive moving window average operations may overly smooth results, potentially missing subtle yet important changes or trends. Specifically, the paper does not provide a sensitivity analysis of the window size, and it is unclear how this parameter was chosen. A smaller window might capture more rapid fluctuations, while a larger window would further smooth the curve, potentially obscuring the true turning point.

3. Selecting the second through as the turning point appears somewhat speculative and lacks sufficient mathematical and theoretical explanations or proofs. Its applicability in all cases remains uncertain, and the paper does not offer examples of failure cases. The paper should explore the theoretical underpinnings of why the second valley corresponds to the optimal stopping point, and provide empirical evidence to support this claim, including examples where this heuristic fails.

4. The datasets for experiments on diffusion models are supplied by the authors. Using widely recognized datasets might enhance the reliability and persuasiveness of the results. For example, using datasets such as ImageNet or CIFAR would allow for a more direct comparison with existing methods and provide a more robust evaluation of the proposed metric.

5. Experiments with language models exclusively involve LLAMA models, with no inclusion of larger or different types of language models. Additionally, only a portion of the MMLU dataset is used. The paper should include experiments on a wider range of language models, including larger models and different architectures, and use the full MMLU benchmark to ensure the generalizability of the results.

6. The paper lacks specific experiment details, such as image tags and the choice of optimizer. The paper should provide a detailed description of the experimental setup, including the specific hyperparameters used for training, the choice of optimizer, and the image tags used for the diffusion model experiments. This information is crucial for reproducibility.

7. In experiments with language models, some LoRA models fail to outperform the original, unfine-tuned models, calling into question the viability of fine-tuning large language models with such limited datasets. The paper should provide a more in-depth analysis of why fine-tuning fails in some cases, and explore strategies to mitigate this issue, such as using different learning rates or regularization techniques.

### Questions
Refer to Weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper aims to address the overfitting issue that arises when fine-tuning a pre-trained foundation model using Low-Rank Adaption (LoRA). Particularly, the authors proposed a new metric called CS-Fluctuation, based on the cosine similarity between the fixed model weight and the added trainable weight using personal data.

### Strengths
1. The proposed method CS-Fluctuation is very simple and kind of reasonable from the case study in this paper. 
1. The proposed method are demonstrated in various benchmark foundation models.

### Weaknesses
1. The proposed method lacks intuitive understanding and theoretical guarantee. It is hard to fully understanding why the proposed method is reasonable, especially why the metric is based on the cosine similarity between the model weights?
1. The scale of the metric ($\approx1e-7$) is too small and changes from data to data. Some normalization is needed for the metric. 
1. The experiment demonstration is monotonous, only CS-Fluctuation vs. training steps is showcased, more aspects about the proposed method should be presented to justify the claims. 
1. No qualitative comparisons. It hard to judge the superiority of the proposed method.

### Questions
1. In figure 1, what is the connection between Epoch and training steps? It seems the first two epoch is sufficient for model fine-tuning from the figure?
1. From the figure 3, it seems there is no clear signal which training steps is better. Why not early stop the method at the first $K$ epoch? set $K=2$ according figure 1.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes CS-Fluctuation, a monitoring metric for early stopping the fine-tuning of foundation models. This is a validation-independent criterion that can be useful in settings where there is a deficiency of validation data. The method has been tested on LDMs and LLMs.

### Strengths
- The paper is well organized and easy to follow.
- The motivation is straightforward and important
- Many qualitative examples are provided

### Weaknesses
 - No theoretical background or explanation on why CS-Fluctuation is a good indicator of overfitting. Why does this work?
- As CS-Fluctuation is a strictly empirical criterion, more quantitative experiments and analyses is needed to support the validity of this early-stopping method. Also, what happens if you vary N in the N-th valley early stopping? Specifically, how does the choice of N affect the trade-off between model performance and the risk of overfitting? A sensitivity analysis of N is crucial to understand the robustness of this approach.
- Qualitative examples are not enough to demonstrate whether the model has been overfitted or not. Many of the samples that the authors have labeled “Overfitted LoRA” does not seem to be particularly overfitted (e.g. Figure 3 top / middle’s center image, Figure 5 top / bottom 3rd, 4th image etc). Quantitative comparison on LDMs is necessary to make the authors’ claim convincing. It's unclear if the perceived degradation in image quality is due to overfitting or simply a consequence of the fine-tuning process itself. The authors should provide quantitative metrics, such as FID or CLIP score, to support their claims about overfitting in LDMs.

### Questions
- Does the Five-shot baseline in Table 3 refer to the case of using 5-shot samples as the validation set? If not, I would want to see a comparison of CS-Fluctuation based early stopping and the standard validation set based early stopping

### Soundness
1 poor

### Presentation
2 fair

### Contribution
3 good

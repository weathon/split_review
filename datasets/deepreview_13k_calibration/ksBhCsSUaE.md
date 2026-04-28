# Probabilistic Token Alignment for Large Language Model Fusion

- Decision: Reject
- Avg Score: 6.25
- Scores: 8, 6, 6, 5

## Abstract
With the drive of scaling laws, the size of large language models (LLMs) continues to grow, causing a burden when constructing stronger baselines from scratch. In response, we propose a more robust baseline by employing knowledge fusion under the model fusion paradigm. However, a key challenge in existing knowledge fusion approaches is their dependence on manually predefined alignment strategies, which may not generalize well across diverse contexts, leading to performance degradation in several zero-shot evaluation tasks. To address this challenge, we draw inspiration from distribution learning and propose the *probabilistic token alignment* method as a general and soft mapping solution for alignment, resulting in **PTA-LLM**. Our approach innovatively reformulates token alignment into a classic mathematical problem: *optimal transport*, seamlessly leveraging distribution-aware learning to facilitate more coherent model fusion. Apart from its inherent generality, PTA-LLM exhibits *interpretability from a distributional perspective*, offering insights into the essence of the token alignment task. Our approach is validated across diverse benchmarks and tasks using three prominent LLMs with distinct architectures—Llama-2, MPT, and OpenLLaMA. Empirical results demonstrate that probabilistic token alignment enhances the target model's performance across multiple capabilities.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper proposes a new method for aligning tokens when fusing models with different vocabularies. The method uses optimal transport to transfer the information from a source model’s logits to the target model’s logits for a given text. Dynamic token pairing allows a single token from the shorter token sequence to be mapped to multiple tokens in the other’s sequence. The transport plan minimizes the cost of transferring mass between the two logit spaces according using edit distance of tokens to determine transport cost. The most probable alignment is selected, and the token logits of the target model are adjusted toward their aligned source token logits. 

Positive evidence for the value of this method is provided through experiments on a variety of standard LLM evaluation datasets compared to reasonable baselines and related work. Analysis shows that the proposed method provides more stability than other fusion methods. A qualitative analysis of the proposed method shows a more compact and consistent representation compared to a competitive fusion method. Ablations provide information about the robustness and effect of hyperparameters.

### Strengths
This paper provides an interesting solution to the problem of mixing information from language models with different vocabularies. The performance gains from the proposed method are consistent versus the competing methods. Optimal transport is very fashionable right now, and the ICLR community may appreciate seeing it applied here.

### Weaknesses
The paper’s writing is at times grandiose. The introduction begins with a question about how to build better models without resorting to scaling, and then insists we reframe this question as one about model fusion. Some hedging here would help i.e. “one method for addressing question 1 is knowledge fusion”.

Sometimes, the paper is unclear. For instance: while optimal transport is general and can be applied to moving mass between a variety of spaces, it is most often applied in ML to moving probability mass. The current paper uses the standard ML terminology of “transferring probability” between distributions (e.g. line 272), but seems to be moving mass between logit spaces. Since logits are not probability distributions, the use of terms like “token distribution” and “probability mass” are a bit misleading. I’m not certain that moving mass in logit-space is the same as moving mass between probability spaces since the normalization terms in the source and target space are different. More careful writing could address this problem.

The paper argues the proposed method improves on earlier methods which rely on “surface level token correspondences” (line 153), but doesn’t the use of edit distance as a cost function for the transport plan also rely on surface level correspondences? Is this edit distance computed at the token level?

### Questions
The paper argues the proposed method improves on earlier methods which rely on “surface level token correspondences” (line 153), but doesn’t the use of edit distance as a cost function for the transport plan also rely on surface level correspondences? Is this edit distance computed at the token level?

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
3

### Summary
This paper proposes PTA-LLM, a knowledge fusion-based approach for language model fusion. Compared with FuseLLM, a pioneer knowledge fusion work, PTA-LLM changes the hard mapping of source and target vocabulary into soft mapping and uses an optimal transport method to calculate the optimal token alignment. Overall, the paper offers a sound and well-motivated solution to the core problem, token alignment, in knowledge fusion over heterogeneous source LLMs.

### Strengths
- Token alignment is the core issue of heterogeneous knowledge fusion. The paper offers a sound and well-motivated solution to this problem.
- The overall experimental results look good, though the improvements are not significant.

### Weaknesses
 - In practice, the Sinkhorn algorithm seems to be time-consuming. The limitations section should be better included in the main pages for a fair demonstration. I also have some concerns about the end-to-end training time on corpus other than MiniPile.
- What does the EM score for GSM stand for? Is it 1.90%? The score seems extremely low and does not align with other reported results.

### Questions
None

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper introduces PTA-LLM, a probabilistic token alignment method designed to align the distributions of various LLMs with different vocabularies. Inspired by the optimal transport problem, PTA-LLM employs distribution-aware learning to enhance more coherent model fusion. Experimental results across multiple benchmarks confirm the effectiveness of PTA-LLM.

### Strengths
- The paper is easy to read and presents its ideas clearly.

- The proposed PTA-LLM is general, stable, and interpretable. 

- The paper conducts a series of experiments to demonstrate the effectiveness of PAT.

### Weaknesses
 - The improvement in effectiveness seems insufficiently significant. In Table 1, the average gap between CLM is only about 1 point. Given the complexity of Model Fusion compared to ordinary CLM, this improvement may not adequately highlight the advantages of PTA. For example, PAT requires obtaining the probability distributions of all teacher models, which means incurring multiple forward pass costs. What would be the effect if these additional costs were used to train more data with CLM? In addition, Multiple experiments are needed for significance testing to demonstrate the effectiveness of PAT.

 - Why does llamda2 perform only 0.66 on GSM, while I saw that the original llamda2 paper did not report such a low score?

- Why is direct training for next token prediction not ideal? In theory, all models fit the training corpus through next-token prediction. Why does distilling the distribution of different models on the corpus outperform the next-token-prediction training objective itself?

- Knowledge fusion also keeps the CLM loss for training, using a parameter called lambda to control weight. How does the value of lambda affect the performance? Whether lambda need to be fine-tuned elaborately for improvement？

### Questions
- Why does llamda2 perform only 0.66 on GSM, while I saw that the original llamda2 paper did not report such a low score?

- Why is direct training for next token prediction not ideal? In theory, all models fit the training corpus through next-token prediction. Why does distilling the distribution of different models on the corpus outperform the next-token-prediction training objective itself?

- Knowledge fusion also keeps the CLM loss for training, using a parameter called lambda to control weight. How does the value of lambda affect the performance? Whether lambda need to be fine-tuned elaborately for improvement？

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces a novel approach PTA-LLM to fusing LLMs with different architectures by framing token alignment as an optimal transport problem. This distribution-aware method generalizes token alignment effectively, enhancing performance in zero-shot evaluation tasks and offering interpretability through a distributional lens.

### Strengths
This work addresses token alignment, a key challenge of knowledge fusion, by applying the classic mathematical optimization method of optimal transport to achieve a soft alignment. This approach also offers an interpretable analysis for token alignment.

### Weaknesses
1.This article focuses on token alignment for models with different structures but only tests three models, with OpenLLaMA and Llama2 having relatively high similarity. The experiment would benefit from including models with greater architectural diversity, such as Mistral and Qwen. Furthermore, the evaluation should extend beyond multiple-choice tasks to include generative tasks to fully assess the method's capabilities across different model architectures and task types.

2.In Table 1 of the main experimental results, PTA-LLM shows limited improvement over FUSELLM, with an average absolute gain of less than 0.5 points. Additionally, the experiment employs a zero-shot evaluation approach, which is challenging for the base models and may not fully reflect their capabilities; for example, the GSM dataset typically uses an 8-shot or 4-shot setup. In the zero-shot setting, the scores of the three base models remain very low. The marginal gains raise concerns about the practical significance of the proposed method.

3.In Section 4.3 on STABILITY, the authors selected certain tasks to compare the performance of PTA-LLM and FUSELLM, demonstrating that soft alignment offers greater flexibility and adaptability than hard mapping. However, the article does not analyze the characteristics and shared features of these advantageous tasks or assess the applicability of soft alignment in these cases, making it difficult for the explanation to convincingly support its hypothesis. A more rigorous analysis of why soft alignment is beneficial in these specific cases is needed.

4.In the ablation experiments of Section 4.5, the paper examines only two cases each for Optimal Transport Temperature, Combination Weight, and Token Alignment Window Size, which does not adequately reveal the impact trends of each factor. The limited exploration of the hyperparameter space makes it difficult to draw definitive conclusions about the robustness and sensitivity of the method to these parameters.

5.There are some typos in the paper：

Line 223: "Pt" -> "P_t"

Line 274: "Tt" -> "T_t"

Line 417:  "-17/07%" -> "-17.07%"

Line 430: "26.96" -> "36.96"

### Questions
See "Weaknesses".

### Soundness
3

### Presentation
3

### Contribution
2

# Revisiting Prefix-tuning: Statistical Benefits of Reparameterization among Prompts

- Decision: Accept
- Scores: 6, 6, 6, 8

## Abstract
Prompt-based techniques, such as prompt-tuning and prefix-tuning, have gained prominence for their efficiency in fine-tuning large pre-trained models. Despite their widespread adoption, the theoretical foundations of these methods remain limited. For instance, in prefix-tuning, we observe that a key factor in achieving performance parity with full fine-tuning lies in the reparameterization strategy. However, the theoretical principles underpinning the effectiveness of this approach have yet to be thoroughly examined. Our study demonstrates that reparameterization is not merely an engineering trick but is grounded in deep theoretical foundations. Specifically, we show that the reparameterization strategy implicitly encodes a shared structure between prefix key and value vectors. Building on recent insights into the connection between prefix-tuning and mixture of experts models, we further illustrate that this shared structure significantly improves sample efficiency in parameter estimation compared to non-shared alternatives. The effectiveness of prefix-tuning across diverse tasks is empirically confirmed to be enhanced by the shared structure, through extensive experiments in both visual and language domains. Additionally, we uncover similar structural benefits in prompt-tuning, offering new perspectives on its success. Our findings provide theoretical and empirical contributions, advancing the understanding of prompt-based methods and their underlying mechanisms.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper studies the role of reparameterization in the context of prefix-tuning within foundation models. The authors provide a theoretical study that demonstrates that reparameterization induces a shared structure between prefix key and value vectors in order to attain strong performance. They also include experimentation of language and vision-related models. Furthermore, they also tie the findings to mixture-of-expert approaches and prompt-tuning approaches.

### Strengths
* The paper is clearly written and includes useful foundational knowledge to help set-up the theoretical framework.
* The work studies both the case of when prompts contain shared structures and when they do not, providing extensibility to the framework
* The theoretical analysis builds usefully from a linear setting to a one-layer setting. 
* The work contains a broad set of experiments across multiple vision and language oriented datasets. In addition, the experiments study prefix tuning under different kinds of fine-tuning.

### Weaknesses
1. The beginning of Section 4 highlights the simplification of the theoretical analysis ("we focus only on the first head, namely, l = 1 in equation (6), and the first row of the attention in this head, namely, i = 1 in
equation (6)."). The work would be strengthened with greater discussion of how this simplification might provide limitation in the extensibility of the analysis
2. The work would be strengthened by discussion of how included results on somewhat small-scale set-ups (trained on ImageNet-21k or older versions of GPT-2) might translate to larger scale models and tasks.

### Questions
[Numbered per Weaknesses above]
1. The work would be strengthened by more thorough discussion of potential limitations of the problem simplification within the theoretical analysis section.
2. How does results presented in Section 5.2 translate to larger scale systems?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper investigates the reparameterization strategy in prompt tuning based on the mixture-of-experts model. By providing theoretical analysis on prompt learning and prefix tuning, the paper proves that the shared structure, e.g., reparameterization among prompts, helps considerably improve the sample efficiency of prompt learning. The experiments on both visual and language tasks demonstrate the theoretical analyses.

### Strengths
1. The paper provides detailed theoretical analyses of the reparameterization strategy for prompt learning.

2. The experiments on several tasks demonstrate the theoretical analyses.

### Weaknesses
1. Although the paper provides detailed theoretical proof of the effectiveness of the reparameterization strategy in prefix tuning, my main concern is about the technical contribution of the paper. Since both the reparameterization strategy and the mixture-of-experts are already investigated in previous works, the technical contribution of the paper seems a bit weak.

2. The theoretical analyses are provided based on the mixture-of-experts models. However, I didn't find the necessary connections between the MoE model and the reparameterization strategy on prefix tuning. Why do the proofs need to be analyzed on the MoE model? Do the proofs still be held without the MoE model? And is there any empirical results to demonstrate the proofs without the MoE architecture? Relying on the pretrained MoE model will also lead to increased costs.

### Questions
1. I found the notation $N$ in the paper confusing in the paragraph under equation 5. It is used for both the number of the input embeddings and the number of the experts. Does it means the numbers of the embeddings and experts should be the same? Otherwise, it is better to replace on of them with another notation.

2. What's the basic architecture of the MoE model in the paper? Is it also conducted by prefix tuning with the reparameterization strategy? How are the experts pretrained in the experiments?

3. In Figure 2, sometimes the simple-share method is better than the deep-share method. Any discussions on the selection of the methods?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This study primarily explores the theoretical foundations and effectiveness of prompt-based techniques, such as prefix-tuning and prompt-tuning. The authors point out that the key to achieving performance parity with full fine-tuning lies in the reparameterization strategy, demonstrating that this strategy implicitly encodes a shared structure between prefix key and value vectors. Through extensive experiments in both visual and language domains, the research empirically confirms that the effectiveness of prefix-tuning across various tasks benefits from this shared structure. Additionally, the authors find similar structural advantages in prompt-tuning as well.

### Strengths
1. Many existing studies have only applied prompt techniques in different domains without providing theoretical proof of their effectiveness. In contrast, this research explores the theoretical foundations and effectiveness of prompt techniques from the perspective of reparameterization and other angles.
2. The authors' theoretical analysis shows that the shared structure significantly improves the efficiency of parameter estimation, resulting in faster convergence compared to non-shared alternatives.
3. The authors also observed that when there is a lack of shared structure among prompt parameters, the performance of prompt learning is negatively impacted. This finding underscores the importance of shared structure in optimizing the learning process and provides theoretical support for future research on how to effectively design and utilize shared structures to enhance the effectiveness of prompt learning.

### Weaknesses
1. The lack of additional visualization results means that, despite the authors' analysis of the effectiveness of prompt techniques, there is a deficiency in more intuitive visual outcomes. As a reader, I am particularly interested in understanding which specific areas of the images the prompts cause the model to focus on.
2. The paper primarily discusses the benefits of reparameterization, but the discussion on its potential negative impacts or limitations may be insufficient.

### Questions
1. It is recommended that the authors include more intuitive visual analyses, such as which areas the prompt techniques guide the model to focus on, to help readers better understand the effectiveness of the prompt techniques.
2. To improve the reproducibility of the experiments, it is recommended that the authors provide a detailed account of the experimental setup, including hyperparameters and other relevant settings.

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
This paper explores prefix-tuning—a parameter-efficient method for adapting large pre-trained models to downstream tasks. Specifically, the study investigates the effectiveness of reparameterization in prefix-tuning and offers theoretical foundations for its success. Prefix-tuning, in contrast to traditional fine-tuning, involves modifying only a small subset of model parameters, thereby reducing computational cost and storage requirements. The authors demonstrate that reparameterization is not merely a technical optimization but encodes a shared structure between key and value vectors, enhancing sample efficiency. By empirically validating these theoretical insights across tasks in both visual and language domains, the authors provide a new perspective on prompt-based tuning.

### Strengths
1. Provides a novel theoretical perspective on reparameterization, bridging prefix-tuning and mixture-of-experts frameworks.
2. Demonstrates empirical improvements across multiple tasks and architectures, supporting the theoretical claims with robust data.
3. Enhances the understanding of prompt-based tuning mechanisms, potentially broadening their applications.

### Weaknesses
1. The study is limited to specific configurations, leaving questions on broader applicability to different model types and prompt architectures.
2. While theoretically sound, the real-world implications, particularly computational demands of the reparameterization method, could be explored in more depth.

### Questions
1. How does reparameterization improve sample efficiency in prefix-tuning, and what are the core theoretical principles underlying this claim?
2. What differentiates the shared structure induced by reparameterization in prefix-tuning from other parameter-sharing mechanisms, such as those used in multi-task learning?
3. How does the proposed shared structure model compare with traditional mixture-of-experts (MoE) frameworks in terms of theoretical benefits and efficiency?
4. The authors discuss potential memory overhead associated with the reparameterization method. What optimizations could address this issue in practice?

### Soundness
3

### Presentation
3

### Contribution
3

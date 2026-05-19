### Summary

This paper proposes a model-centric evaluation framework called OMNIINPUT, which evaluates the quality of an AI/ML model's predictions on all possible inputs. The framework constructs a test set by sampling from the model's output distribution and uses selective annotation to estimate the model's precision and recall. The experiments demonstrate that OMNIINPUT enables a more fine-grained comparison between models and provides new insights for training more robust, generalizable models.

### Soundness

2 fair

### Presentation

2 fair

### Contribution

2 fair

### Strengths

1. The paper introduces a novel model-centric evaluation framework, OMNIINPUT, which is a departure from traditional data-centric evaluation methods. This approach allows for a more comprehensive understanding of a model's performance across all possible inputs.

2. The framework is demonstrated to be effective in revealing differences in model performance that are not apparent with traditional evaluation methods. This can be particularly useful for identifying the strengths and weaknesses of different models and for guiding future research.

3. The paper provides a detailed explanation of the OMNIINPUT framework, including the use of an efficient sampler to obtain representative inputs and the output distribution of the trained model.

### Weaknesses

#### Some Related Works


#### comment

1. The paper acknowledges that the scalability of the OMNIINPUT framework is a limitation, particularly for larger input spaces and more complex models. However, it does not provide a clear path forward for addressing this issue, which could limit the practical applicability of the framework.

2. The paper relies on human annotation for the evaluation, which can be time-consuming and expensive. While the authors claim that the annotation effort is less than traditional methods, the process is still subjective and may introduce bias. The paper does not provide a detailed analysis of the potential impact of this bias on the evaluation results.

3. The paper does not provide a thorough comparison of the OMNIINPUT framework with existing evaluation methods. While the authors claim that their method is superior, they do not provide sufficient evidence to support this claim. The lack of a rigorous comparison makes it difficult to assess the true value of the proposed framework.

### Suggestions

The authors should address the scalability limitations of the OMNIINPUT framework more thoroughly. While the paper mentions that the framework is not yet scalable to larger input spaces and more complex models, it lacks a concrete plan for overcoming this challenge. The authors should explore potential solutions, such as using more efficient sampling techniques or developing methods for approximating the output distribution for high-dimensional inputs. For example, they could investigate the use of variational autoencoders or generative adversarial networks to learn a lower-dimensional representation of the input space, which could then be used for sampling. Furthermore, the authors should provide a more detailed analysis of the computational cost of the proposed method and compare it with existing evaluation techniques. This would help to clarify the practical limitations of the framework and identify areas for future improvement.

To mitigate the subjectivity and potential bias introduced by human annotation, the authors should explore alternative evaluation strategies. One approach could be to use a combination of human and automated evaluation methods. For example, they could use a pre-trained model to generate pseudo-labels for a subset of the data, which could then be used to train a model to predict the quality of the outputs. This would reduce the reliance on human annotation and make the evaluation process more objective. Additionally, the authors should provide a more detailed analysis of the inter-annotator agreement and discuss the potential impact of this agreement on the evaluation results. This would help to quantify the level of subjectivity in the evaluation process and identify potential sources of bias. The authors should also consider using multiple human annotators and averaging their scores to reduce the impact of individual biases.

The paper needs a more rigorous comparison with existing evaluation methods to demonstrate the value of the proposed framework. The authors should select a few representative evaluation methods and compare their performance with the OMNIINPUT framework on a range of datasets and models. This comparison should include both quantitative and qualitative analysis. For example, the authors could compare the precision-recall curves obtained using the OMNIINPUT framework with those obtained using traditional evaluation methods. They should also discuss the strengths and weaknesses of each method and identify the scenarios where the OMNIINPUT framework is most effective. This would help to establish the practical value of the proposed framework and provide a clear understanding of its advantages and limitations.

### Questions

1. How can the scalability issue of the OMNIINPUT framework be addressed to make it applicable to larger input spaces and more complex models?

2. What measures can be taken to mitigate the subjectivity and potential bias introduced by human annotation in the evaluation process?

3. How does the OMNIINPUT framework compare to existing evaluation methods in terms of effectiveness and practicality?

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

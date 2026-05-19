### Summary

The paper proposes OMNIINPUT, a model-centric evaluation framework designed to evaluate an AI/ML model's predictions across all possible inputs, including those that are typically human-unrecognizable. Unlike traditional evaluation methods that rely on predefined test sets, OMNIINPUT constructs a test set using the model's self-generated representative inputs and assesses model quality by examining the output distribution.

### Soundness

2 fair

### Presentation

2 fair

### Contribution

2 fair

### Strengths

1. The paper presents OMNIINPUT, a novel model-centric evaluation framework that shifts away from traditional data-centric approaches by evaluating AI/ML models across all possible inputs, including those beyond human recognition. This innovative approach is particularly significant for enhancing AI safety and reliability.

2. The paper demonstrates the practicality of OMNIINPUT through its application to various popular models and training methods, revealing new insights into model performance and generalizability.

### Weaknesses

#### Some Related Works


#### comment

1. The framework's focus on a binary classification task limits its applicability and does not fully leverage the potential of the proposed evaluation framework. The lack of experiments on multi-class classification tasks, which are common in many real-world applications, makes it difficult to assess the framework's generalizability.

2. The paper does not provide a detailed analysis of the computational resources required by the OMNIINPUT framework. The absence of information on memory usage, processing time, and hardware requirements makes it challenging to evaluate the practical feasibility of the framework, especially for large-scale models and datasets. A quantitative comparison of the computational overhead with traditional evaluation methods is missing.

3. The paper lacks a thorough discussion of the framework's limitations, particularly in terms of scalability. The current implementation seems to be limited to small-scale tasks, and there is no clear path outlined for extending the framework to handle large datasets or complex models. The absence of a discussion on how the framework would perform with high-dimensional input data or models with millions of parameters raises concerns about its practical applicability in real-world scenarios.

4. The paper does not adequately address the human annotation effort required for the OMNIINPUT framework. The reliance on human evaluators to label the generated samples introduces a subjective element, and the paper does not provide sufficient details on the number of annotators, their expertise, or the inter-annotator agreement. This lack of information makes it difficult to assess the reliability and reproducibility of the evaluation results.

### Suggestions

The paper should significantly expand its discussion on the limitations of the OMNIINPUT framework, particularly regarding its scalability. The current implementation appears to be confined to small-scale tasks, and the paper does not provide a clear path for extending the framework to handle large datasets or complex models. A detailed analysis of the computational resources required by the framework, including memory usage, processing time, and hardware requirements, is crucial for assessing its practical feasibility. The authors should also explore the use of more efficient sampling techniques, such as adaptive sampling or importance sampling, to reduce the computational burden. Furthermore, the paper should include a discussion on how the framework would perform with high-dimensional input data or models with millions of parameters. This would involve addressing challenges such as the curse of dimensionality and the computational cost of generating and evaluating a large number of samples. The authors should also consider the potential for parallelization and distributed computing to improve the scalability of the framework.

To address the concerns about human annotation, the paper should provide a more detailed description of the annotation process, including the number of annotators, their expertise, and the inter-annotator agreement. The authors should also explore the use of automated annotation techniques, such as using a pre-trained model to generate pseudo-labels, to reduce the human annotation effort. A comparison of the results obtained with human annotation and automated annotation would be valuable for assessing the reliability and reproducibility of the evaluation results. The paper should also discuss the potential for bias in human annotations and how this bias might affect the evaluation results. The authors should consider using multiple annotation rounds with different sets of annotators to assess the robustness of the evaluation results.

Finally, the paper should include a more comprehensive evaluation of the OMNIINPUT framework on a wider range of tasks and datasets. While the binary classification task is a good starting point, the paper should also demonstrate the applicability of the framework to multi-class classification tasks, regression tasks, and other types of machine learning problems. The authors should also consider evaluating the framework on more complex models, such as deep neural networks with millions of parameters. This would involve addressing challenges such as the computational cost of generating and evaluating a large number of samples and the potential for overfitting to the training data. The paper should also include a comparison of the OMNIINPUT framework with existing evaluation methods, such as cross-validation and hold-out validation, to demonstrate its advantages and limitations.

### Questions

1. Can the OMNIINPUT framework be extended to evaluate regression tasks, and if so, how would the methodology need to be adapted?

2. How does the OMNIINPUT framework perform when applied to large-scale datasets and complex models with millions of parameters? Are there any plans to enhance the framework's scalability?

3. What is the human annotation effort required for the OMNIINPUT framework, and are there any ongoing efforts to automate this process?

4. How does the OMNIINPUT framework compare to existing evaluation methods in terms of effectiveness, and are there any plans to conduct such comparative experiments?

### Rating

3: reject, not good enough

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

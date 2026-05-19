### Summary

The paper presents a novel framework, Neuro2Semantic, designed to reconstruct semantic content from intracranial EEG (iEEG) recordings. The authors introduce a two-phase training process that aligns neural signals with pre-trained text embeddings, enabling unconstrained text generation. The framework demonstrates strong performance with minimal neural data, significantly outperforming a baseline method in low-data settings. Additionally, the authors show that the model generalizes well to out-of-domain contexts, highlighting its potential for real-world applications in brain-computer interfaces and neural decoding technologies.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The paper is well-written and easy to follow.
2. The authors provide a comprehensive evaluation of the proposed framework, comparing it against a baseline method and analyzing its performance across various metrics.
3. The authors demonstrate the potential of the framework for low-data settings, which is a significant contribution to the field of neural decoding.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a thorough discussion of the limitations of the proposed framework, particularly in comparison to existing methods. A more detailed analysis of the framework's performance under different conditions, such as varying levels of noise or different types of semantic content, would be beneficial.
2. The authors should provide a more detailed explanation of the baseline method used for comparison. This would help readers better understand the significance of the proposed framework's performance.
3. The paper would benefit from a more in-depth analysis of the framework's generalizability to different datasets and tasks. The current evaluation is limited to a single dataset, which may not be representative of real-world scenarios.
4. The authors should discuss the potential ethical implications of using the framework for brain-computer interfaces, particularly in terms of privacy and potential misuse.

### Suggestions

The authors should include a more detailed discussion of the limitations of their approach, specifically addressing how the model's performance might degrade under different conditions. For example, the impact of varying levels of noise in the EEG signals, different types of semantic content (e.g., complex sentences, ambiguous words), and the presence of artifacts should be explored. A quantitative analysis of the model's performance under these conditions would be beneficial, perhaps by introducing controlled levels of noise or by testing the model on subsets of the data with varying semantic complexity. Furthermore, the authors should discuss the computational cost of their method, including the training time and the resources required for deployment. This would help potential users assess the feasibility of adopting the proposed framework in their own research or applications. The authors should also consider the potential impact of the model on individuals with specific neurological conditions or those who may use assistive devices. A discussion of how the model might interact with these systems and the potential ethical implications of such interactions is necessary.

To enhance the evaluation of the proposed framework, the authors should provide a more detailed explanation of the baseline method used for comparison. This explanation should include the specific algorithms, parameters, and training procedures used in the baseline. This would allow readers to better understand the significance of the proposed framework's performance and to reproduce the results. Furthermore, the authors should consider comparing their framework against a wider range of baseline methods, including both traditional and more recent approaches. This would provide a more comprehensive assessment of the framework's performance and its advantages over existing methods. The authors should also discuss the statistical significance of the results, including the use of appropriate statistical tests and the reporting of confidence intervals. This would help to ensure that the observed improvements are not due to random chance.

Finally, the authors should expand their evaluation to include additional datasets and tasks to demonstrate the generalizability of their framework. This could involve testing the model on different types of EEG data, such as MEG or EEG-EOG data, or on different tasks, such as speech recognition or motor imagery decoding. The authors should also consider evaluating the model's performance on datasets from different subjects or different experimental settings. This would help to assess the robustness of the framework and its potential for real-world applications. The authors should also discuss the potential limitations of their framework in these different scenarios and suggest possible solutions to address these limitations. The authors should also consider the potential impact of their work on the broader research community and the ethical implications of using their framework for brain-computer interfaces.

### Questions

1. How does the performance of the proposed framework compare to other state-of-the-art methods for neural decoding?
2. What are the potential ethical implications of using the proposed framework for brain-computer interfaces?
3. How does the proposed framework handle noisy or incomplete EEG data?
4. How does the performance of the proposed framework vary across different subjects or datasets?

### Rating

5

### Confidence

3

**********

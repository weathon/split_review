### Summary

This paper introduces ConvINT, a semi-structured intention framework designed to enhance conversational AI's understanding of user intentions. ConvINT is organized into four key aspects: situation, emotion, action, and knowledge, providing a holistic and fine-grained approach to intention analysis. The authors also propose a Weakly-supervised Reinforced Generation (WeRG) method to scale ConvINT annotations across large datasets. Experimental results demonstrate that integrating ConvINT with WeRG significantly improves LLMs' ability to comprehend user intentions, leading to better performance in downstream tasks like response generation and task completion.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The introduction of the ConvINT framework is a novel contribution to the field of conversational AI. By organizing user intentions into four key aspects, the framework provides a more comprehensive and nuanced understanding of user inputs compared to traditional structured or unstructured approaches.
2. The WeRG method is an innovative approach to scaling ConvINT annotations. By combining a small set of human-annotated instances with coarsely labeled data as weak supervision signals, WeRG effectively learns to generate high-quality annotations, addressing the challenge of scalability while maintaining precision.
3. The paper is well-structured and clearly written, making it easy to follow the proposed methods and experimental results. The authors provide a thorough explanation of the ConvINT framework and the WeRG mechanism, supported by detailed experimental evaluations.
4. The experimental results are robust and demonstrate the effectiveness of the proposed methods. The authors conduct extensive evaluations on multiple datasets and compare their approach with several baselines, showing significant improvements in both automatic and human evaluations.

### Weaknesses

#### Some Related Works


#### comment

1. The paper could benefit from a more detailed discussion of the limitations of the ConvINT framework and the WeRG method. For example, how do these methods perform in scenarios with highly ambiguous or context-dependent user intentions? Are there specific types of conversations or domains where the proposed methods might struggle?
2. The evaluation of the WeRG method primarily focuses on the quality of the generated ConvINT data. While this is important, the paper could also explore the efficiency and scalability of the WeRG method in more detail. How does the performance of WeRG scale with the size of the dataset and the complexity of the conversations? Are there any computational bottlenecks or practical challenges in deploying WeRG for very large datasets?
3. The paper could provide more insights into the practical implications of using the ConvINT framework and the WeRG method in real-world conversational AI systems. How can these methods be integrated into existing conversational AI pipelines? What are the potential benefits and challenges of deploying these methods in production environments?
4. The paper could benefit from a more thorough comparison with existing methods for conversational understanding and intention recognition. While the authors compare their approach with several baselines, a more detailed analysis of the strengths and weaknesses of the proposed methods compared to state-of-the-art techniques would be valuable.

### Suggestions

The paper should delve deeper into the limitations of the ConvINT framework, particularly regarding its ability to handle ambiguous or context-dependent user intentions. For instance, how does the framework perform when user utterances are sarcastic, ironic, or contain implicit meanings that require significant world knowledge to interpret? The authors should explore scenarios where the four key aspects (situation, emotion, action, and knowledge) might be difficult to disentangle or where the boundaries between them become blurred. Furthermore, the paper should investigate the framework's performance across different domains, such as customer service, healthcare, or social media, where the nature of user intentions and the conversational context can vary significantly. A more detailed analysis of these limitations would provide a more balanced view of the framework's applicability and potential areas for improvement. The authors could consider including examples of challenging conversational scenarios and discussing how the ConvINT framework might struggle in these cases, along with potential mitigation strategies.

Regarding the WeRG method, the paper needs to provide a more thorough analysis of its efficiency and scalability. While the quality of the generated annotations is crucial, the practical feasibility of using WeRG for large-scale datasets is equally important. The authors should investigate how the training time and computational resources required by WeRG scale with the size of the dataset and the complexity of the conversations. It would be beneficial to include a detailed breakdown of the computational costs associated with each step of the WeRG method, such as the weak supervision signal generation, the reinforcement learning process, and the annotation generation. Furthermore, the paper should discuss any potential bottlenecks or challenges in deploying WeRG for very large datasets, such as memory limitations or parallelization issues. The authors could also explore techniques to optimize the WeRG method for efficiency, such as using more efficient reinforcement learning algorithms or employing distributed training strategies.

Finally, the paper should provide more concrete examples of how the ConvINT framework and the WeRG method can be integrated into real-world conversational AI systems. The authors should discuss the potential benefits of using these methods in various applications, such as improving the accuracy of intent recognition, enhancing the quality of response generation, and enabling more effective task completion. It would be valuable to include case studies or examples of how these methods can be used to address specific challenges in conversational AI, such as handling complex user queries or adapting to changing user preferences. The paper should also discuss the potential challenges of deploying these methods in production environments, such as the need for continuous monitoring and retraining, and the potential impact of noisy or adversarial user inputs. A more detailed discussion of these practical implications would help to bridge the gap between the theoretical contributions of the paper and their real-world applications.

### Questions

1. How does the ConvINT framework handle user intentions that are not easily categorized into the four defined aspects? Are there mechanisms in place to deal with out-of-domain or novel intentions?
2. Can the authors provide more details on the human annotation process used to create the ConvINT labels? How was inter-annotator agreement measured, and what steps were taken to ensure the quality of the annotations?
3. The paper mentions using a small set of human-annotated instances for the WeRG method. How sensitive is the performance of WeRG to the size and quality of this initial set of annotations?
4. How does the WeRG method handle noisy or inconsistent weak supervision signals? Are there any mechanisms in place to filter out or correct errors in the weakly labeled data?
5. The paper focuses on improving LLMs' understanding of user intentions. How do these improvements translate to downstream tasks such as response generation and task completion? Can the authors provide more detailed examples of how ConvINT and WeRG enhance the performance of these tasks?

### Rating

6

### Confidence

4

**********

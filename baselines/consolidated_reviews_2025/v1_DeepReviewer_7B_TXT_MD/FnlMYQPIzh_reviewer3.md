### Summary

The paper introduces ConvINT, a novel semi-structured intention framework designed to address the limitations of existing structured approaches in understanding user intentions in conversations. ConvINT organizes user intentions into four key aspects: situation, emotion, action, and knowledge. To facilitate the generation of ConvINT data, the authors propose the Weakly-supervised Reinforced Generation (WeRG) method, which efficiently expands ConvINT annotations by leveraging a combination of coarse-to-fine labels and weak supervision signals. The effectiveness of ConvINT and WeRG is demonstrated through experiments on two conversational datasets, DuRecDial and ESConv, showing significant improvements in downstream tasks such as response generation and task completion.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The paper is well-written and easy to follow, with a clear structure and comprehensive background information. The motivation for ConvINT is well-articulated, highlighting the limitations of existing structured methods in capturing the complexity of user intentions. The authors effectively use illustrative examples to demonstrate the need for a more nuanced approach to intention modeling.
2. The proposed ConvINT framework offers a fine-grained and aspect-aware approach to intention understanding, which is a significant advancement over existing structured methods. By organizing intentions into four key aspects—situation, emotion, action, and knowledge—the framework provides a more comprehensive representation of user goals and behaviors. This aspect-aware approach is particularly valuable in real-world applications where user intentions are often multifaceted and context-dependent.
3. The WeRG method effectively leverages weak supervision signals to generate high-quality ConvINT data. The combination of coarse-to-fine labels and the reward mechanism allows for efficient and scalable data generation, making it feasible to apply ConvINT to large-scale datasets. The experimental results demonstrate the effectiveness of WeRG in generating high-quality ConvINT data, which is crucial for the success of the proposed framework.

### Weaknesses

#### Some Related Works


#### comment

1. The paper primarily focuses on the technical aspects of the ConvINT framework and WeRG method, with limited exploration of the practical implications and applications of the proposed approach. While the authors demonstrate the effectiveness of ConvINT and WeRG on two conversational datasets, they do not delve into the potential use cases of the framework in real-world applications. For example, the paper could benefit from a discussion on how ConvINT can be integrated into existing conversational AI systems, such as chatbots or virtual assistants, and how it can improve their performance in understanding user intentions. Furthermore, the paper lacks a discussion on the computational cost and scalability of the proposed method, which are important considerations for practical deployment.
2. The paper does not provide a detailed analysis of the limitations of the ConvINT framework and WeRG method. While the authors acknowledge the limitations of existing structured methods, they do not discuss the potential challenges and limitations of their proposed approach. For example, the paper could benefit from a discussion on the types of user intentions that are difficult to capture with ConvINT, the potential biases in the weak supervision signals, and the robustness of the framework to noisy or ambiguous user inputs. A more thorough analysis of these limitations would provide a more balanced view of the proposed approach and help guide future research in this area.

### Suggestions

The paper would benefit significantly from a more detailed exploration of the practical applications of the ConvINT framework. While the technical contributions are valuable, the lack of concrete examples and use cases limits the impact of the work. The authors should consider demonstrating how ConvINT can be integrated into existing conversational AI systems, such as chatbots or virtual assistants, and how it can improve their performance in understanding user intentions. For instance, they could show how the framework can be used to enhance the user modeling capabilities of a chatbot, allowing it to better anticipate user needs and provide more relevant responses. Furthermore, the authors should discuss the computational cost and scalability of the proposed method, providing insights into its feasibility for real-world deployment. This could include an analysis of the time and memory requirements of the WeRG method and the ConvINT framework, as well as a discussion of potential optimization techniques to improve its efficiency. A more thorough discussion of these practical aspects would greatly enhance the paper's relevance and impact.

In addition to the practical implications, the paper should also include a more detailed analysis of the limitations of the ConvINT framework and WeRG method. The authors should discuss the types of user intentions that are difficult to capture with ConvINT, such as intentions that are highly context-dependent or that involve complex emotional states. They should also address the potential biases in the weak supervision signals used to generate ConvINT data, and how these biases might affect the performance of the framework. Furthermore, the authors should discuss the robustness of the framework to noisy or ambiguous user inputs, and how it can be made more resilient to such inputs. A more thorough analysis of these limitations would provide a more balanced view of the proposed approach and help guide future research in this area. For example, the authors could explore the use of techniques such as data augmentation or adversarial training to improve the robustness of the framework.

Finally, the paper could benefit from a more detailed comparison with existing methods for intention modeling. While the authors mention the limitations of existing structured methods, they do not provide a comprehensive analysis of how ConvINT compares to other approaches in terms of performance, efficiency, and scalability. A more thorough comparison would help to contextualize the contributions of the paper and highlight the advantages of the proposed approach. This could include a discussion of the strengths and weaknesses of ConvINT compared to other methods, as well as an analysis of the trade-offs between performance and computational cost. Such a comparison would provide a more complete picture of the proposed approach and its place in the broader landscape of intention modeling.

### Questions

1. How does the ConvINT framework handle situations where user intentions are ambiguous or contradictory? Are there any mechanisms in place to resolve such conflicts, or does the framework assume that user intentions are always clear and consistent?
2. The paper mentions that the WeRG method leverages weak supervision signals to generate ConvINT data. Could you provide more details on the types of weak supervision signals used and how they are incorporated into the training process? How do these signals affect the quality and diversity of the generated ConvINT data?
3. The paper demonstrates the effectiveness of ConvINT and WeRG on two conversational datasets, DuRecDial and ESConv. Are there any plans to evaluate the framework on other datasets or in different domains? How do you anticipate the performance of ConvINT and WeRG to vary across different types of conversations or user behaviors?
4. The paper focuses on the technical aspects of the ConvINT framework and WeRG method. Could you discuss the potential practical implications and applications of the proposed approach in real-world scenarios? How do you envision the framework being integrated into existing conversational AI systems, and what are the potential benefits of such integration?

### Rating

6

### Confidence

4

**********

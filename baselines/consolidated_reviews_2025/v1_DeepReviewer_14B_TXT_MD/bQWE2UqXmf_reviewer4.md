### Summary

This paper proposes a method to detect AI-generated content by prompting LLMs to rewrite text and calculating the editing distance of the output. The authors find that LLMs are more likely to modify human-written text than AI-generated text when tasked with rewriting. The proposed method, RAIDAR, significantly improves the F1 detection scores of existing AI content detection models across various domains, with gains of up to 29 points. The method operates solely on word symbols without high-dimensional features, making it compatible with black box LLMs, and is inherently robust on new content.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper introduces a novel and interesting approach to detecting AI-generated content by leveraging the rewriting behavior of LLMs. The observation that LLMs are more likely to modify human-written text than AI-generated text when tasked with rewriting is insightful and forms the basis of the proposed method.
2. The proposed method, RAIDAR, demonstrates significant improvements in detection performance compared to existing methods across various domains. The gains of up to 29 points in F1 detection scores are substantial and highlight the effectiveness of the approach.
3. The method operates solely on word symbols without high-dimensional features, making it compatible with black box LLMs. This is a practical advantage, as it allows for broader applicability and avoids the need for access to internal model representations.
4. The paper provides a thorough evaluation of the proposed method on multiple datasets and across different LLMs. The experiments demonstrate the effectiveness and robustness of RAIDAR in various scenarios.

### Weaknesses

#### Some Related Works


#### comment

1. The paper could benefit from a more detailed discussion of the limitations of the proposed method and potential future research directions. For example, it would be helpful to discuss the potential challenges in applying RAIDAR to different domains or languages, and how the method might be adapted to address these challenges. Specifically, the paper lacks a discussion on how the method would perform on highly structured text, such as code or legal documents, where the rewriting process might not be as effective in distinguishing between human and AI-generated content. Furthermore, the paper should address the potential for adversarial attacks, where an attacker might craft text specifically designed to fool the RAIDAR method.
2. The paper could provide more insights into the reasons behind the observed behavior of LLMs when rewriting human and AI-generated text. While the paper presents the observation that LLMs are more likely to modify human-written text, it does not delve deeply into the underlying mechanisms that cause this behavior. A more thorough analysis of the linguistic or stylistic differences between human and AI-generated text that lead to this phenomenon would strengthen the paper's contribution. For instance, are there specific syntactic or semantic patterns that are more easily modified by LLMs in human-written text, and how do these patterns differ from those in AI-generated text?

### Suggestions

To address the limitations regarding the applicability of RAIDAR across different domains and languages, the authors should conduct experiments on a wider range of datasets, including those with highly structured text such as code or legal documents. This would involve not only testing the performance of RAIDAR on these datasets but also analyzing the reasons for any observed performance differences. For example, if RAIDAR performs poorly on code, the authors should investigate whether this is due to the lack of variability in code structure or the presence of specific patterns that are difficult for LLMs to modify. Furthermore, the authors should explore potential adaptations of the method to handle these challenges, such as incorporating domain-specific knowledge or using different rewriting prompts. Additionally, the paper should include a discussion on the potential for adversarial attacks and propose strategies to mitigate them, such as using ensemble methods or incorporating adversarial training techniques. This would make the method more robust and practical for real-world applications.

To gain a deeper understanding of the underlying mechanisms that cause LLMs to modify human-written text more than AI-generated text, the authors should conduct a more detailed analysis of the linguistic and stylistic differences between the two types of text. This could involve analyzing the frequency of specific syntactic structures, semantic patterns, or stylistic features in both human and AI-generated text and correlating these features with the extent of modification observed by LLMs. For example, the authors could investigate whether human-written text tends to have more complex sentence structures or more nuanced semantic relationships, which might make it more susceptible to modification by LLMs. Additionally, the authors could explore the use of interpretability techniques to understand which specific features of the text are most influential in the LLM's rewriting process. This would provide valuable insights into the nature of AI-generated text and could lead to the development of more effective detection methods.

Finally, the paper should include a more detailed discussion of the computational cost of the proposed method. While the authors mention that the method operates solely on word symbols, they do not provide a quantitative analysis of the time and memory requirements of the rewriting process. This information is crucial for assessing the practicality of the method, especially when dealing with large datasets or real-time applications. The authors should also discuss the potential for optimizing the method to reduce its computational cost, such as using more efficient rewriting algorithms or parallel processing techniques. This would make the method more accessible and useful for a wider range of users.

### Questions

1. How does the performance of RAIDAR vary across different domains or languages? Are there any specific challenges in applying the method to certain types of content?
2. Can you provide more insights into the reasons behind the observed behavior of LLMs when rewriting human and AI-generated text? What are the key differences between the two types of text that lead to this phenomenon?

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

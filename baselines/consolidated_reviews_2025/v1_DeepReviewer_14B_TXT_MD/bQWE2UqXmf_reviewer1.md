### Summary

The paper introduces a novel method for detecting AI-generated content by leveraging the behavior of LLMs during text rewriting. The authors observe that LLMs are more likely to modify human-written text than AI-generated text, as they tend to perceive AI-generated content as high-quality. The proposed method, named RAIDAR (geneRative AI Detection viA Rewriting), involves prompting LLMs to rewrite input text and calculating the editing distance between the original and rewritten text. The authors demonstrate that RAIDAR significantly improves F1 detection scores compared to existing models across various domains, with gains of up to 29 points. The method operates solely on word symbols, making it compatible with black-box LLMs and robust for new content.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper introduces a novel and insightful observation that LLMs are more likely to modify human-written text than AI-generated text when tasked with rewriting. This unique perspective forms the basis of the proposed detection method, RAIDAR.
2. RAIDAR demonstrates significant improvements in F1 detection scores compared to existing models, with gains of up to 29 points across various domains. This highlights the effectiveness and potential impact of the proposed method.
3. The method operates solely on word symbols without relying on high-dimensional features, making it compatible with black-box LLMs. This is a practical advantage, as it allows for broader applicability and avoids the need for access to internal model representations.
4. The authors conduct experiments across various domains, including News, creative writing, student essays, code, Yelp reviews, and arXiv papers. This demonstrates the generalizability of the method to different types of content.
5. RAIDAR is shown to be robust for new content and can detect AI-generated text from different language models, even those the model has not been trained on. This adaptability is crucial for real-world applications.
6. The paper is well-written and clearly explains the motivation, methodology, and experimental results. The figures and tables effectively illustrate the findings and comparisons with existing methods.

### Weaknesses

#### Some Related Works


#### comment

1. The paper could benefit from a more detailed analysis of the computational cost and efficiency of RAIDAR, especially when dealing with large volumes of text or real-time detection scenarios. Specifically, the paper lacks a discussion on the time complexity of the rewriting process and the subsequent edit distance calculation, which are both crucial for assessing the scalability of the proposed method. Furthermore, the paper does not provide a breakdown of the computational resources required, such as memory usage and CPU/GPU time, making it difficult to evaluate the practical feasibility of RAIDAR in resource-constrained environments.
2. While the paper mentions that RAIDAR is robust to new content, a more thorough investigation into its performance across a wider range of LLMs and evolving AI models would further strengthen its claims of generalizability. The paper should include experiments with a more diverse set of models, including those with different architectures and training datasets, to ensure that the observed detection performance is not specific to the models used in the study. Additionally, the paper should explore the method's sensitivity to variations in the output style of different LLMs, as this could impact the reliability of the edit distance metric.
3. The paper could explore potential countermeasures that AI developers might employ to make detection more difficult, such as fine-tuning models to produce text that is less distinguishable through rewriting. The paper should discuss how techniques like adversarial training or style transfer could be used to generate AI-text that is more resistant to RAIDAR's detection mechanism. This would provide a more comprehensive understanding of the limitations of the proposed method and its potential vulnerabilities.
4. The paper could benefit from a more detailed discussion of the limitations of RAIDAR, particularly in cases where the distinction between human and AI-generated text is subtle or where the content is highly technical or domain-specific. The paper should address the potential for false positives and false negatives, especially in cases where human-written text exhibits similar characteristics to AI-generated text, such as in highly structured or formulaic writing. Furthermore, the paper should explore the method's performance on content that requires specialized knowledge or terminology, as this could impact the reliability of the detection results.

### Suggestions

To address the lack of computational cost analysis, the authors should include a detailed breakdown of the time complexity for each step of the RAIDAR method, including the rewriting process and the edit distance calculation. They should also provide empirical measurements of the computational resources required, such as memory usage and CPU/GPU time, for different input sizes and LLMs. This analysis should be conducted on a variety of hardware configurations to assess the method's performance in resource-constrained environments. Furthermore, the authors should explore potential optimizations to improve the efficiency of RAIDAR, such as using more efficient rewriting models or employing approximation techniques for edit distance calculation. This would make the method more practical for real-world applications involving large volumes of text or real-time detection scenarios. The authors should also consider the impact of different rewriting prompts on the computational cost and detection performance, as this could provide insights into how to balance efficiency and accuracy.

To strengthen the claims of generalizability, the authors should conduct experiments with a more diverse set of LLMs, including models with different architectures, training datasets, and output styles. This should include open-source models, as well as proprietary models, to ensure that the observed detection performance is not specific to the models used in the study. The authors should also explore the method's sensitivity to variations in the output style of different LLMs, as this could impact the reliability of the edit distance metric. Furthermore, the authors should investigate the performance of RAIDAR on text generated by models that have been fine-tuned on specific domains or tasks, as this could reveal potential limitations of the method. The authors should also consider the impact of different rewriting prompts on the detection performance across different LLMs, as this could provide insights into how to improve the robustness of the method.

To address the potential countermeasures, the authors should discuss how techniques like adversarial training or style transfer could be used to generate AI-text that is more resistant to RAIDAR's detection mechanism. This should include an analysis of the potential vulnerabilities of the method and how these vulnerabilities could be exploited by adversaries. The authors should also explore potential defenses against such attacks, such as using ensemble methods or incorporating additional features into the detection model. Furthermore, the authors should discuss the ethical implications of using RAIDAR, particularly in cases where it could be used to falsely accuse individuals of generating AI-text. This would provide a more comprehensive understanding of the limitations of the proposed method and its potential vulnerabilities.

### Questions

1. Can you provide more details on the computational cost and efficiency of RAIDAR, especially when dealing with large volumes of text or real-time detection scenarios? How does the method scale with increasing text length and the number of documents to be analyzed?
2. How does RAIDAR perform across a wider range of LLMs and evolving AI models? Have you tested the method on newer models like GPT-4 or other advanced language models? How does the performance vary across different model architectures and training datasets?
3. What potential countermeasures could AI developers employ to make detection more difficult, and how might RAIDAR adapt to such changes? Have you considered the possibility of models being fine-tuned to produce text that is less distinguishable through rewriting?
4. What are the limitations of RAIDAR, particularly in cases where the distinction between human and AI-generated text is subtle or where the content is highly technical or domain-specific? How does the method perform on content that requires specialized knowledge or terminology?

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

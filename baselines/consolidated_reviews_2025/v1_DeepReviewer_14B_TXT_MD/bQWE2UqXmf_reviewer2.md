### Summary

This paper introduces a method for detecting AI-generated content by prompting LLMs to rewrite text and calculating the editing distance of the output. The authors find that LLMs are more likely to modify human-written text than AI-generated text when tasked with rewriting. The proposed method, RAIDAR, significantly improves the F1 detection scores of existing AI content detection models across various domains, with gains of up to 29 points. The method operates solely on word symbols without high-dimensional features, making it compatible with black box LLMs, and is inherently robust on new content.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The paper presents a novel and interesting approach to detecting AI-generated content by leveraging the rewriting behavior of LLMs.
- The proposed method, RAIDAR, demonstrates significant improvements in detection performance compared to existing methods across various domains.
- The method operates solely on word symbols without high-dimensional features, making it compatible with black box LLMs.
- The paper provides a thorough evaluation of the proposed method on multiple datasets and across different LLMs.

### Weaknesses

#### Some Related Works


#### comment

 - The paper could benefit from a more detailed discussion of the limitations of the proposed method and potential future research directions.
- The paper could provide more insights into the reasons behind the observed behavior of LLMs when rewriting human and AI-generated text.

### Suggestions

The paper's exploration of AI-generated text detection through LLM rewriting is promising, but it would benefit from a more thorough investigation into the method's limitations. Specifically, the paper should delve deeper into scenarios where the proposed RAIDAR method might fail or exhibit reduced performance. For instance, how does the method perform when the AI-generated text is heavily edited or paraphrased by a human? Does the method's effectiveness degrade when the input text is very short or very long? Furthermore, the paper should consider the impact of different rewriting prompts on the detection performance. A more detailed analysis of these edge cases would provide a more comprehensive understanding of the method's robustness and applicability. Additionally, the paper should explore the computational cost associated with the rewriting process, especially when dealing with large volumes of text. This would be crucial for practical applications of the method.

To enhance the paper's contribution, a more detailed analysis of the underlying mechanisms driving the observed rewriting behavior is needed. The paper should explore why LLMs tend to modify human-written text more than AI-generated text. Is it due to differences in the statistical properties of the text, or is there a deeper reason related to the way LLMs are trained? For example, do human-written texts contain more unique stylistic elements or less predictable structures that trigger more modifications during rewriting? Conversely, are AI-generated texts more homogeneous or optimized for LLM processing, leading to fewer changes? A deeper understanding of these mechanisms could lead to more robust and interpretable detection methods. The paper could also explore the use of different distance metrics beyond simple word-level edits to capture more nuanced differences in the rewritten text. This could potentially improve the detection accuracy and provide further insights into the nature of AI-generated content.

Finally, the paper should discuss potential future research directions that build upon the proposed method. For example, could the method be extended to detect AI-generated content in other modalities, such as images or audio? Could the method be used to identify the specific AI model used to generate the text? The paper should also consider the ethical implications of using such detection methods, particularly in the context of misinformation and fake news. A more comprehensive discussion of these aspects would strengthen the paper's overall impact and relevance. Furthermore, the paper should explore the potential for adversarial attacks on the proposed method and how to mitigate them. This would be crucial for ensuring the reliability and security of the detection system.

### Questions

- Have you explored the potential of using RAIDAR for other tasks, such as text summarization or paraphrase detection?
- How does the performance of RAIDAR vary with the length of the input text?

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

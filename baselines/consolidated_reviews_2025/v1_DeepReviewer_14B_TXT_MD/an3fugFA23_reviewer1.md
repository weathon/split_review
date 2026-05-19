### Summary

This paper proposes a probability distribution estimation (PDE) method to enable white-box text detection methods for proprietary language models (LLMs). Current white-box methods require full access to the model, which is often not available for proprietary LLMs. The PDE method estimates the full probability distribution of the model's output based on the top-K tokens and their probabilities. The authors demonstrate that PDE can extend white-box methods like Entropy, Rank, and Fast-DetectGPT to work with proprietary models, achieving good detection accuracy.

### Soundness

3

### Presentation

2

### Contribution

2

### Strengths

1. The PDE method allows white-box detection methods to be used with proprietary LLMs, which could lead to more robust and reliable detection of machine-generated text.
2. The authors evaluate their method on multiple datasets, languages, and source models, showing that PDE can improve the accuracy and robustness of text detection. The experimental results are relatively complete.
3. The method is relatively straightforward to implement and can be applied to various white-box detection methods.

### Weaknesses

#### Some Related Works


#### comment

1. The paper's assumption that the top tokens of proprietary LLMs will be available is uncertain, as providers may not offer this information. The feasibility of the proposed method hinges on the accessibility of top-token probabilities, which are not guaranteed by proprietary model APIs. The paper should more clearly acknowledge this dependency as a critical limitation.
2. The paper does not discuss the potential for attackers to circumvent the method by altering the probability distribution of the generated text. The method relies on the integrity of the probability distribution, which could be manipulated by an adversary to evade detection. The paper lacks a discussion of the method's vulnerability to adversarial attacks that modify the probability distribution.
3. The paper's writing needs refinement. For instance, the sentence in lines 93-96 is incomplete. The manuscript contains grammatical errors and unclear phrasing that detract from its readability and technical clarity. A thorough review of the text is necessary to ensure precision and completeness.

### Suggestions

The paper should explicitly address the reliance on the availability of top-token probabilities from proprietary models. The authors should discuss the implications if this information is not provided or is limited by the API. A sensitivity analysis of the method's performance with varying levels of top-token availability would strengthen the paper. Furthermore, the paper should explore alternative approaches or modifications to the PDE method that could mitigate the impact of limited access to top-token probabilities. This could involve investigating the use of lower-ranked tokens or exploring other model outputs that might be more readily available. The authors should also consider the practical implications of relying on proprietary APIs, which may change over time, and discuss the robustness of their method to such changes.

The paper needs a more thorough analysis of the method's robustness against adversarial attacks. The authors should investigate how the PDE method performs when the probability distribution of the generated text is altered. This could involve simulating different types of attacks, such as re-ranking the probabilities or using a different decoding strategy. The paper should also discuss the potential for adaptive attacks that are specifically designed to evade the PDE method. The authors should consider incorporating techniques to detect or mitigate adversarial attacks, such as using statistical checks or comparing the distribution to known patterns of human-generated text. A discussion of the limitations of the method in the face of adversarial attacks is crucial for a realistic assessment of its applicability.

Finally, the paper requires a careful review of its writing and presentation. The authors should ensure that all sentences are complete and grammatically correct. The technical concepts should be explained clearly and precisely, avoiding jargon or ambiguous terms. The paper should be structured logically, with a clear introduction, methodology, experimental results, and discussion. The authors should also ensure that all figures and tables are properly labeled and explained. A thorough revision of the text is necessary to improve its readability and technical clarity, making it more accessible to a wider audience.

### Questions

Please refer to the weakness.

### Rating

6

### Confidence

3

**********

# Use Sparse Autoencoders to Discover Unknown Concepts, Not to Act on Known Concepts

- Decision: Reject
- Scores: 6, 4, 5

## Abstract
While sparse autoencoders (SAEs) have generated significant excitement, a series of negative results have added to skepticism about their usefulness. Here, we establish a conceptual distinction that reconciles competing narratives surrounding SAEs. We argue that while SAEs are less effective tools for *acting on known concepts*, SAEs are powerful tools for *discovering unknown concepts*. This distinction cleanly separates existing negative and positive results, and suggests several classes of SAE applications. Specifically, we outline use cases for SAEs in (i) text as data, (ii) bridging prediction and explanation in ML-based science, and (iii) ML interpretability, explainability, fairness, and auditing.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
In this paper, the authors argued that sparse autoencoders (SAEs) should be employed as tools for discovering unknown concepts instead of acting on known concepts. The authors begin with a description of the architecture of SAEs and their ability to generate interpretable features. Then the authors described why SAEs underperform logistic regression or prompting on tasks like concept detection and model steering, while at the same time achieve positive results in tasks like hypothesis generation and biology of LLMs. The authors presume that negative performance involve tasks that pre-specify a concept, while positive results are shown when SAEs are used to enumerate and interpret unknown concepts. The authors attempted to explain the negative results by investigating why reconstruction-based representations lose information needed for steering. The authors also reviewed how SAEs have been used to generate hypotheses that predict engagement of news headlines or to explain LLM behaviours such as performing addition. Finally, the authors outlined potential applications of SAEs in fields such as text as data, bridging prediction and explanation, ML interpretability, explainability, fairness, and auditing.

### Strengths
- The paper clearly distinguishes “acting on known concepts” from “discovering unknown concepts”. It is significant as it might inspire future research.

- The survey in the paper is quite comprehensive, spanning from positive results to negative results.

- The position in the paper is timely and highly relevant to the machine learning community.

- The position is well-supported by related works and empirical evidence.

- The paper finishes with a discussion of potential applications, which is also helpful.

### Weaknesses
- The boundary between “acting on known concepts” and “discovering unknown concepts” should be further clarified by the authors.

- The authors did not conduct an in-depth analysis for the positive results. Aspects such as the stability of discovered concepts across random seeds and potential spurious correlations should be discussed.

- The potential applications describe in the paper are quite abstract, without concrete examples or guidelines.

### Questions
- Can you please provide comparisons between SAEs and other unsupervised methods?

- Are there hybrid approaches that combine SAEs with other methods that can help mitigate the problem of losing the information needed for steering?

### Presentation
3

---

## Human Reviewer 2

### Rating
4

### Rating Number
4

### Confidence
3

### Summary
This position paper argues that the utility of Sparse Autoencoders (SAEs) is task-dependent. It advocates the position that SAEs are powerful tools for discovering unknown concepts but are less effective for acting on known, pre-specified concepts. To support this claim, the paper reviews recent literature. It frames negative results—where SAEs underperform baselines in tasks like concept detection and model steering—as instances of acting on known concepts. Conversely, it highlights positive results in hypothesis generation and explaining LLM behavior ("biology of LLMs") as successful examples of discovering previously unknown concepts.

### Strengths
S1: This position paper makes an interesting point that Sparse Autoencoders (SAEs) are best for tasks that need concept discovery, not for tasks where the concepts are already known.

S2: This position is supported with literature showing where SAEs outperform other models and evidence where they aren't as strong. The paper also lists potential research areas where SAEs could be useful for discovering concepts.

S3: The topic is relevant and important to the NeurIPS community because figuring out the right way to use SAEs is a key issue in interpretability research.

### Weaknesses
W1: The paper could be improved by giving a broader introduction to related interpretability methods, like concept bottleneck models, and discussing the similarities and differences with SAEs to help readers better understand their place.

W2: The argument for why SAEs are not useful in concept detection isn't strong enough. Showing that a classifier using the original embeddings is more accurate doesn't necessarily prove SAEs are bad for this task, since the original embedding isn't interpretable. It isn't a fair comparison. An interpretable classifier built from SAE features could still be very beneficial, even if it's slightly less accurate (naturally due to how it was trained).

W3: The SAEs used in the cited papers have different implementations—some use token embeddings while others replace MLP neurons. It's not clear if these different training approaches affect the SAEs' representational power, which could make it hard to generalize the paper's main conclusion.

### Questions
Q1: How would you position the role of SAEs in comparison to other feature mining methods, like topic modelling, interpretable text embeddings or concept bottleneck models? What are the main pros and cons to consider?

Q2: Beyond the empirical evidence you provide from the literature, is there any theoretical or analytical analysis that supports your position that SAEs are not suitable for scenarios when concepts are already known

### Presentation
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes that SAEs as a discovery tool for building unknown concepts. By showing they can activate these newly discovered concepts to steer the model's output, they convincingly frame SAEs as a proactive tool for understanding models not just reactive one for fixing them.

### Strengths
1. The paper is well-written and easy to follow.
2. Encouraging to see empirical validation of concept control.
3. Makes a strong claim that SAEs are a primary tool for discovering new concepts.

### Weaknesses
1. Since the concept-based approaches originated from the vision domain, it would be beneficial to include experiments on image data.
2. Would strengthen the paper to provide mathematical justification.
3. The paper assumes the complex ideas can be decomposed into a linear concept, but this linearity assumption may represent an oversimplication.

### Questions
1. Would this claim also hold for image data?
2. Could you elaborate on the limitations of representing the model's internal state as a linear combination of features?

### Presentation
3

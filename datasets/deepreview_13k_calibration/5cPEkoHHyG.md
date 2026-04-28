# MetaInv: Overcoming Iterative and Direct Method Limitations for Inverse Learning

- Decision: Reject
- Avg Score: 3.67
- Scores: 5, 3, 3

## Abstract
Invertible neural networks (INNs) have gained significant traction in tasks requiring reliable bidirectional inferences, such as data encryption, scientific computing, and real-time control. However, iterative methods like i-ResNet face notable limitations, including instability on non-contractive mappings and failure in scenarios requiring strict one-to-one mappings. In contrast, analytical approaches like DipDNN guarantee invertibility but at the expense of performance, particularly in tasks demanding rich feature extraction (e.g., convolutional operations in complex image processing). This work presents a detailed analysis of the limitations in current invertible architectures, examining the trade-offs between iterative and analytical approaches. We identify key failure modes, particularly when handling information redundancy or strict bijections, and propose a meta-inverse framework that dynamically combines the advantages of both i-ResNet and DipDNN. Our framework adapts in real-time based on task-specific signals, ensuring both flexibility and guaranteed invertibility. Extensive experiments across diverse domains demonstrate that our hybrid approach outperforms existing methods in forward accuracy, inverse consistency, and computational efficiency. Our results highlight the utility of this meta-inverse strategy for critical applications where precision, stability, and adaptability are crucial.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper first provides a detailed analysis of the limitations in current invertible architectures, examining the trade-offs between iterative and analytical approaches. It then proceeds with proposing a meta-inverse framework that dynamically combines the advantages of both i-ResNet and DipDNN, by dynamically switching between them based on ask-specific signals.

### Strengths
A very detailed analysis of the limitations in current invertible architectures,

### Weaknesses
A rather short and not very extensive presentation of the switching algorithm and its associated challenges.

### Questions
What were the key challenges in developing the switching algorithm, and what were the main contributions here?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The authors propose a method, termed MetaInv, to dynamically choose between two approaches for inverse modeling depending upon which one is most appropriate for the problem.

### Strengths
1) Inverse problems are important, and therefore the general topic is significant

### Weaknesses
1) The presentation is often poor.  The introduction is often vague/unclear regarding existing methods and their weaknesses.  There are major mathematical typos:  e.g., the equation in Line 147 does not seem to be valid.  Although I can guess, the authors never describe what l_{2} is, and what exactly are we summing over in the equations from lines 139-155.  

2) The review of the literature on inverse modeling misses large portions of the literature. Some examples include (but may not be limited to) genetic algorithms, conditional Invertible neural networks, mixture density networks, and the so-called Tandem model.   The authors ought to mention some of these approaches and explain why they were not applicable for this study, or at least why they were not included in experiments.   The authors can find examples of these existing methods/publications in Ardizzone et al. "Analyzing inverse problems with invertible neural networks." arXiv preprint arXiv:1808.04730 (2018),    or publications that cite this one. 

3) The authors show that their method is beneficial for just two methods in the literature: DipDNN and iResNet.  This becomes interesting if the result of combining these two approaches with MetaInv yields a method that achieves state-of-the-art capabilities (e.g., inverse accuracy, or computational efficiency).  However, the authors only show that their MetaInv approach leads to better/comparable performance to DipDNN and iResNet.  Therefore it is unclear whether the result of all this work improves state-of-the-art in any way or just improves these two methods.  Although improvement over these two particular methods is still interesting as a proof-of-concept for the MetaInv idea, in my opinion it is not sufficiently significant/interesting for this venue.

### Questions
I welcome a response to comment (2) in the "weaknesses" section, although I request that the authors only respond if their response is clearly written, and addresses in a clear/compelling way (i) why so much existing work on inverse modeling was omitted from consideration, and (ii) why this work is still significant despite the exclusion of so much existin work.

### Soundness
1

### Presentation
1

### Contribution
1

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper analysed the limitations of two specific invertible models, i-ResNet and DipDNN, and proposed a selection mechanism to choose one of the two models for a task. The basis of selection is essentially selecting the best performing model, preferring one model if neither is good.

### Strengths
- The authors did a good review of two prior models and proposed an interesting comparison of the two models.
- The writing is easy to follow.

### Weaknesses
 - The work lacks strong motivation. Why two specific models were chosen to be analysed? Why do we need a single meta-model to work on tasks of a completely different nature? To me, it is quite obvious that we need different models for image data and physics data. The authors should provide a convincing argument to justify their work.
- It is not clear why only i-ResNet and DipDNN are chosen to be analysed. It would be better to aim for generalisable analyses that provide insight into a class of solutions. For example, the analysis could focus on the properties of invertible models with analytical inverses versus those with iterative inverses, rather than focusing on two specific architectures. This would provide a more fundamental understanding of the trade-offs involved.
- The main proposed algorithm (MetaInv) is not clearly described in the main text. More importantly, there is insufficient justification for the preference rules. The selection mechanism appears to be based on a simple performance comparison, but the rationale behind preferring one model over the other when performance is similar is not well-explained. This lack of clarity makes it difficult to assess the robustness and generalizability of the proposed approach.

### Questions
- "MetaInv" is in the title, but the algorithm is not in the main text. Is there a reason to put it in the appendix?
- In 3.1, Inv error, should x_i be y_i instead?
- Figure 8 is difficult to understand. Maybe provide a better description in the caption?

### Soundness
3

### Presentation
3

### Contribution
2

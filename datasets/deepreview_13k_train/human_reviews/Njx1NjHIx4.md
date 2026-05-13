# Formation of Representations in Neural Networks

- Decision: Accept
- Scores: 8, 8, 8, 6

## Abstract
Understanding neural representations will help open the black box of neural networks and advance our scientific understanding of modern AI systems. However, how complex, structured, and transferable representations emerge in modern neural networks has remained a mystery. Building on previous results, we propose the Canonical Representation Hypothesis (CRH), which posits a set of six alignment relations to universally govern the formation of representations in most hidden layers of a neural network. Under the CRH, the latent representations (R), weights (W), and neuron gradients (G) become mutually aligned during training. This alignment implies that neural networks naturally learn compact representations, where neurons and weights are invariant to task-irrelevant transformations. We then show that the breaking of CRH leads to the emergence of reciprocal power-law relations between R, W, and G, which we refer to as the Polynomial Alignment Hypothesis (PAH). We present a minimal-assumption theory demonstrating that the balance between gradient noise and regularization is crucial for the emergence the canonical representation. The CRH and PAH lead to an exciting possibility of unifying major key deep learning phenomena, including neural collapse and the neural feature ansatz, in a single framework.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
First of all, I apologize for the late review with the Authors, the AC, Senior AC and the PC.

This paper introduce the Canonical Representation Hypothesis (CRH), positing that in neural networks, as an effect of training, the representations, weights, and gradients (with respect to the representations) within a layer align with each other. 

This alignment is seen as an essential part of how neural networks form structured, invariant representations. 
The Authors introduce the CRH and support it with a theory that shows how this alignment emerge as a consequence of stationarity towards the end of training, through a balance of gradient noise and regularization.   

Additionally, they propose the Polynomial Alignment Hypothesis (PAH), which describes patterns in cases where CRH is broken, leading to specific scaling relationships in neural networks, of a different nature of scaling laws involving network performances.

This framework offers a new perspective on understanding important aspects of neural representations, unifying phenomena such as neural collapse and feature learning.

### Strengths
The CRH provides a new framework to interpret basic statistical aspects of how neural networks develop representations. The system of CRH equations generalize and organize into a coherent view previous, partial attempts to reveal alignment phenomena between representations, gradients and weights.  By relating CRH to neural collapse, the Authors offer a broader view that positions this phenomenon as a specific case of a more universal behavior in neural networks. 

The framework is very general, focusing on alignment rather than on specific network designs or loss functions. This  increases the potential impact of CRH on future studies, as it provides a general model for understanding basilar statistical aspects of representation formation.

The Authors present a detailed theoretical derivation supporting the CRH. The theoretical derivations adds credibility to their claims, encouraging further studies, in particular related to dynamics.

### Weaknesses
While this work aims at universality, the Authors are the first to recognize that their focus is on specific types of networks and tasks, commenting that further empirical tests across more diverse datasets and architectures are necessary to confirm the CRH and PAH in practice.

The weakness I found is that certain assumptions - which are critical for the theoretical foundation of CRH - may not hold in general, like the self-averaging conditions (Hypothesis A.1, A.2). I think the work woud benefit for an empirical assessment on how severe is the departure from self-averaging in a concrete, relevant case.

Furthermore, I found particularly difficult to follow Section B (THEORY AND PROOFS) of the Supplementary Materials. For example, I could not figure out, Lemma 1 in Section B, mainly because some of the "actors" in the scene (like the A tilde in eq. 21) were not presented first. But it may be also a lack of understanding from my side.

However, adding a few more explanations in this section would improve readibility.

### Questions
Please refer to the weakness section.

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
The authors propose an overarching theory for neural network learning which encompasses the alignment of representations, gradients, and weights throughout training. This framework uniquely combines a diverse set past work under a unified 'canonical representation hypothesis' (CRH) umbrella, and prove theoretically that the CRH does hold. Succinctly, they show that gradient nose 'expands the representation' and weight decay 'contracts it', and they must reach stationarity by balancing these terms. They then use this framework to make predictions about neural network training when each of the six elements of the CRH is broken, provided a set of 64 potential phases for neural network training.  

In conclusion,the paper is well written, organized, and situated in the literature. While I am not an expert in this domain, I therefore defer to other more informed reviewers to make statements about the novelty and accuracy of the authors' claims. Otherwise, the results appear impressive and impactful for the theoretical neural network community, and thus carry significant value.

### Strengths
- The paper is well written, and carefully presented to ensure correctness and clarity.
- The framework appears general, encompassing significant past work. 
- The theorems are general, avoiding reference to any specific loss function or activation functions, helping to explain their ubiquity. 
- The experimental results appear to strongly support the developed theory and appear both rigorous and extensive.
- The insights section is very much welcomed, and provides significant value to readers coming from outside the primary domain. 
- The limitations are clearly stated.

### Weaknesses
 - The authors state that the CRH holds better for later layers than earlier layers.

### Questions
- Can you explain the limitation of the theory exposed by Figure 7? Why do you believe that you see the three branches as opposed to one?

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper introduces six alignment relations to quantify and analyze model representations, collectively termed the Canonical Representation Hypothesis (CRH). This hypothesis proposes that neural networks naturally develop compact representations, with neurons and weights remaining unchanged by transformations that do not affect the task. The study theoretically examines conditions under which CRH holds and demonstrates that when CRH is disrupted, reciprocal power-law relationships arise among representations, weights, and gradients—a phenomenon referred to as the Polynomial Alignment Hypothesis (PAH). Together, CRH and PAH provide a potential unified theory that encompasses several significant phenomena in representation learning, such as Neural Collapse and the Neural Feature Ansatz.

### Strengths
First of all, congratulations on your ICLR submission! I’d like to commend the author for this great piece of research. Below is my review of the work:

**Originality**  
This paper introduces a unifying framework for studying neural network representations, with a notable emphasis on backward representation—a relatively unexplored area. 

**Quality**  
The paper is of generally high quality:
- It acknowledges its own limitations effectively.
- Experimental results are detailed and well-aligned with theoretical insights.
- Findings show that the theory holds across different types of networks.
- Two Mechanisms that disrupt alignment are identified. Quantification is provided via the Polynomial Alignment Hypothesis.

**Clarity**  
The paper is clearly written in good English and is well-structured. Figures are clear, informative, and effectively support the content.

**Significance**  
This paper offers a potentially unifying framework for studying neural network representations and identifying key alignment metrics that inform network alignment. It contributes to an active research area and presents predictions relevant to widely used models like ResNet and LLMs, enhancing its impact in the field. Furthermore, this research could have potential interdisciplinary applications such as neurosciences.

### Weaknesses
 **Originality**
Further clarifying how this work uniquely contributes to and advances the field would enhance its perceived originality.

**Quality**
No clear weakness in the quality.

**Clarity**
-  The term "hypothesis" may be somewhat misleading, as the proposed concept functions more as a measurement framework rather than a traditional hypothesis. Reframing it as such would emphasize its role in quantifying neural network representations without introducing potentially confusing terminology.
- The organization of the paper could benefit from refinement. Early references to later sections (such as mentioning Figure 9 before the relevant context is provided) disrupt the flow, and frequent shifts in reference to the later text and figures make the argument more challenging to follow.
- Providing more detailed explanations for terms such as "neural collapse" and "alignment" would enhance the paper's accessibility.
- Figure 4 lacks a colour bar for the weight decay parameter, which complicates the interpretation of results.

**Significance**
To improve the paper’s significance, it would be helpful to expand on the implications of the different alignment phases. For instance, as mentioned in the text, positive exponents between Za and Ha suggest that the layer enhances the principal components of Ha while diminishing lesser features, whereas a negative exponent indicates the opposite. Greater detail on these implications would improve interpretability, especially regarding how these phases contribute to understanding network behaviour. Additionally, exploring factors that lead to alignment breakdown would deepen the paper's contribution to interpretability in this area.

### Questions
- How might different initialization strategies impact the different observed alignment phenomena?
- Could the authors elaborate on how the phases correspond to observable behavioural or performance changes in the model? 
- Beyond the two mechanisms identified in the paper, could other factors contribute to the disruption of alignment? 
- How might the different alignments discussed in this paper relate to concepts from the rich and lazy learning literature? My understanding is that the neural feature ansatz describes and quantifies the rich regime by analyzing feature evolution. Could these alignments and phases potentially provide a way to further describe and quantify distinct learning regimes ( Specifically further define the different types of rich regimes)?

I hope this review will be helpful in the further development of the paper. I encourage the author to continue this research and incorporate the feedback provided. With improvements in structure, clarification of key concepts, and development of the practical significance of these hypotheses, this paper has the potential to earn a higher score.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper proposes and studies the 'canonical representation hypothesis'. They study the evolution of weights, representations and gradients in neural networks and establish that these quantities become aligned. The paper includes theoretical derivations and experimental measurements that study how the CRH is fulfilled or broken.

### Strengths
The paper makes an effort to be thorough in examining all possible combinations of the forward and backward alignment relations. Moreover, they include a significant number of theoretical results which distinguishes this paper from most work in machine learning.

### Weaknesses
Why should we be interested in the alignment of weights, gradients and representations? How does this contribute to the bigger picture of understanding why deep neural network work. If the authors provided a clear motivation there would be much more incentive to dig through the notation and derivations.

23: emergence + of

44: Furthermore, ... - this sentence makes no sense without more context

49: How does the CRH have anything to do with 'interpretable' solutions?

Related work, you might want to include: https://arxiv.org/abs/2007.00810

68: weight matrices evolve during training? This seems rather tautological, what is the point?

117: missing verb?

149: In practice, it is often not the case that stationarity is reached. Comment?

159-160: Can you explain?

217: Neural collapse / invariance to irrelevant features seems to be at odds with these works (https://proceedings.mlr.press/v139/zimmermann21a.html; https://arxiv.org/abs/2410.21869). Comment?

232: Why is this 'surprising' if it is exactly what the theory predicts?

### Questions
23: emergence + of

44: Furthermore, ... - this sentence makes no sense without more context

49: How does the CRH have anything to do with 'interpretable' solutions?

Related work, you might want to include: https://arxiv.org/abs/2007.00810

68: weight matrices evolve during training? This seems rather tautological, what is the point?

117: missing verb?

149: In practice, it is often not the case that stationarity is reached. Comment?

159-160: Can you explain?

217: Neural collapse / invariance to irrelevant features seems to be at odds with these works (https://proceedings.mlr.press/v139/zimmermann21a.html; https://arxiv.org/abs/2410.21869). Comment?

232: Why is this 'surprising' if it is exactly what the theory predicts?

### Soundness
3

### Presentation
3

### Contribution
2

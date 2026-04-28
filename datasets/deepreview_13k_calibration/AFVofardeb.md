# Representing Part-Whole Hierarchy with Nested Neuronal Coherence

- Decision: Reject
- Avg Score: 4.75
- Scores: 3, 6, 5, 5

## Abstract
Human vision flexibly extracts part-whole hierarchy from visual scenes. However, representing such hierarchical structure is a key challenge for neural networks. Most machine learning efforts addressing this issue have focused on slot-based methods, which may be limiting due to their discrete nature and difficulty to express uncertainty. Inspired by how neural syntax is organized in the brain, this paper presents a framework to represent the hierarchical part-whole relationship through hierarchically nested neuronal coherence, which has a continuous and distributed nature. At implementation level, we further developed a cortical-inspired hybrid model, the Composer, which dynamically achieves the emergent nestedness given images. To evaluate the emergent hierarchical structure, 4 synthetic datasets and 3 quantitative metrics are invented, which showed its ability to parse a range of scenes of different complexities. We believe this work, from representation, implementation to evaluation, advances a new paradigm for developing human-like vision in neural network models.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The authors propose a biologically-inspired framework for representing part-whole hierarchies using neuronal coherence, implemented through a spiking neural network architecture called Composer. The system uses denoising autoencoders and hierarchical time scales to generate emergent oscillatory dynamics that encode part-whole relationships. This paper is very similar to a prior submission to ICLR2024 (submission 297), which I also reviewed.

### Strengths
- Addresses the fundamental binding problem in an interesting way
- Better organized presentation compared to previous versions

### Weaknesses
 - The core technical contribution still feels unclear despite improved presentation
- The training methodology remains underspecified in the main text; crucial details are still relegated to a (very!) lengthy appendix
- The baseline comparison (Agglomerator) performs suspiciously poorly with little analysis of why
- The evaluation relies heavily on toy datasets with unclear path to real-world applications

### Questions
I commend the authors on improving this submission compared to last year's submission in terms of clarity and presentation. Yet the biggest flaw remains: it's a lot of prep work and dozens of pages of appendix to support a bespoke neural network that solves one very small, toy task. I would be more inclined to positively review this submission if it presented new results compared to last year's submission, especially presenting results on non-toy datasets.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors introduce a mechanism for representing the fact that objects have a kind of part hierarchy.   They implement this mechanism in a simple case and then evaluate it on some novel metrics for several simple synthetic datasets.

### Strengths
The idea is interesting. 

The metrics evaluated are probably a rich approach to model understanding.  The neuronal analysis is creative.

### Weaknesses
It's a bit simplified, and it's not obvious how the approach will apply in real-world datasets.


### Questions
How will this model be applied to much more complex cases in the real world?

### Soundness
3

### Presentation
3

### Contribution
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
In this paper, the authors propose a novel neurally inspired architecture named COMPOSER that learns to perform hierarchical grouping of images into its constituent parts and sub parts. The authors develop new datasets and metrics, evaluating on which they show that COMPOSER is able to produce emergent hierarchical grouping of scenes via neural synchrony.

### Strengths
* Hierarchical grouping of images is a marker of biological intelligence. Training a neural model that mimics this ability of humans in an interpretable manner is a very interesting research direction.
* The paper's figures are of great quality and aid the understanding of COMPOSER, which is quite an intricate architecture with many moving parts.
* The authors present elaborate analyses on their proposed datasets highlighting how neural synchrony enables hierarchical grouping from images.

### Weaknesses
 * **Lack of comparison to other comparable baselines**: The authors don't perform comparisons with other baselines, like Slot Attention, but they don't perform comparisons with these models (which have publicly available implementations) on the evaluation datasets. This is a major drawback as it is unclear how the proposed model is improving on existing art in neural perceptual grouping.
* **Overly simplistic evaluation datasets**: Several works exist which perform grouping on more complex naturalistic scenes (see [1]), yet the current submission evaluates models on very simple stimuli. It is possible the authors are evaluating on simple stimuli owing to the scalability issue of spiking neural networks, however, it is unclear how the current method is advancing over existing art. The lack of complex stimuli makes it difficult to assess the model's robustness and generalizability to real-world scenarios. The current evaluation setup does not adequately demonstrate the model's ability to handle the variability and complexity present in natural images.
* **On the compute efficiency of COMPOSER**: The authors must evaluate the compute and learning complexity of COMPOSER in comparison to prior art. Can there be a comparison on the number of FLOPS, model parameters or size between COMPOSER and other existing models?

### Questions
Please refer to my weaknesses section of the review.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposed a model called composer that can identify objects and their constituent parts in the pixel space. This model is based on two levels of interconnected spiking neurons and denoising auto-encoders (DAEs) representing whole/part levels. At each level, the DAE recovers the shapes remembered during pre-training from noisy states. Meanwhile, the coupling delay and refractory period of the spiking neurons make the neural activities move out of the steady state and transition to other potential steady states that the DAE could recover. The two levels representing the whole and parts are interconnected, enabling nesting, where the constituent parts of a whole object are identified. The author showed that the model can identify the objects, their constituent parts, and the nesting relationship in several synthetic datasets involving identifying simple shapes and their parts.

### Strengths
This paper studies and proposes a model that identifies and represents objects and their constituent parts. The model uses two levels of spiking neurons and denoising autoencoders to recover part-whole hierarchy in the dynamic neural states, a novel neural architecture for this problem. They showed with concrete evidence that this model could work and demonstrated it on four different synthetic datasets they developed. They also proposed clearly defined evaluation metrics -- the part/whole/nest score -- that measure how well spiking neurons represent the desired structure. According to these metrics, the composer model performs better than another method, Agglomerator, on their dataset.

### Weaknesses
While the theme of this paper is about representing the part-whole hierarchy, it doesn't explain why explicitly representing this hierarchy is an important question to solve. As also noted by the author, "real-world images typically lack explicit parsing structures." This makes me wonder whether it is a well-posed question that the brain or brain-like intelligent system needs to represent the part-whole hierarchy in an explicit manner. What problem in the real world may benefit from explicitly representing such a hierarchy? Maybe it is the ability to generalize out of distribution, the ability to reason, or something else. It would be helpful if the author could explain what makes 
explicitly representing part-whole hierarchy in the proposed model a desired approach. What new abilities does the system have that other methods do not have, and what problem does this model solve that other models cannot solve?

This also connects to my concern about the benchmark results in this paper, which showed that their method outperformed the previous SOTA model Agglomerator in the four tasks they evaluated. According to their metrics, the previous SOTA model Agglomerator only performed randomly or even worse than randomly in these tasks. However, these tasks involving identifying pre-defined simple shapes and their parts seem like very simple problems that various baseline methods, such as template matching, convolutional networks, or Bayesian inference methods, could solve. It would be helpful if the author could also show the results with these baseline methods and clarify if performances are gained from the composer model or to further explain why these baseline methods are unsuitable for the tasks they studied. 

Other minor points:
Figure 1 of the paper motivated that representing the part-whole hierarchy is challenging because the interpretation of the parts and wholes can be ambiguous. This paper has suggested multiple times that slot-based models are limited due to their inability to express uncertainty, and the composer model seems to resolve this problem. However, there isn't a metric in the paper that quantifies the uncertainty of their model, nor did they have a task to evaluate how the model resolves the ambiguous case motivated by Figure 1. It would be helpful if the author could explain how the model expresses uncertainty and how that could be validated in ambiguous cases motivated in Figure 1.

I hope this point could help. It is not a part of my decision assessment:
This paper presented a model inspired by the brain's structure and mechanisms, and motivated that this model could act as a data-driven biological model to understand the brain. However, I could not find any comparison to real behavioral or neural data in this paper. Along that direction, it would be great if future work could show more concrete, well-defined comparisons with real neural data in the brain or human/animal behavior if the model is intended as a model of the brain.

### Questions
1. The four tasks used in the benchmark seem like very simple problems that various baseline methods, such as template matching, convolutional networks, or Bayesian inference methods, could solve. How does this proposed model compare with these baseline models, or can the author clarify why these baseline models are unsuitable for these tasks?

2. What problem in the real world may benefit from explicitly representing part/whole hierarchy, and how does this proposed model make progress in solving those problems? What new abilities does the proposed model have that other existing methods do not have, and what problem does this model solve that other existing methods cannot solve?

3. How does this model represent uncertainty, and how do we quantify that? Why is representing uncertainty better than not representing it?

### Soundness
2

### Presentation
3

### Contribution
2

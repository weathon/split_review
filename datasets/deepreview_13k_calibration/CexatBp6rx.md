# Restyling Unsupervised Concept Based Interpretable Networks with Generative Models

- Decision: Accept
- Avg Score: 6.40
- Scores: 6, 6, 8, 6, 6

## Abstract
Developing inherently interpretable models for prediction has gained prominence in recent years. A subclass of these models, wherein the interpretable network relies on learning high-level concepts, are valued because of closeness of concept representations to human communication. However, the visualization and understanding of the learnt unsupervised dictionary of concepts encounters major limitations, specially for large-scale images. We propose here a novel method that relies on mapping the concept features to the latent space of a pretrained generative model. The use of a generative model enables high quality visualization, and naturally lays out an intuitive and interactive procedure for better interpretation of the learnt concepts. Furthermore, leveraging pretrained generative models has the additional advantage of making the training of the system more efficient. We quantitatively ascertain the efficacy of our method in terms of accuracy of the interpretable prediction network, fidelity of reconstruction, as well as faithfulness and consistency of learnt concepts. The experiments are conducted on multiple image recognition benchmarks for large-scale images. Project page available at \url{https://jayneelparekh.io/VisCoIN_project_page/}
  
\keywords{Interpretability \and Explainability \and Generative models}

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a new approach for inherently interpretable models by mapping the concept space to the latent space of a pre-trained generative model. In particular, this approach focuses on using this mapping to associate semantics with the concepts. To this end, the paper proposes the use of three adapter modules along with a pre-trained classifier and generator to achieve the goal. Appropriate losses and metrics are defined to train and evaluate the method. The experiments on standard large-scale benchmark datasets shows promise in the approach.

### Strengths
+ The idea of using the latent space of a generative model to map implicitly learned concepts of a neural network model is interesting.
+ The methodology is simple and effective.
+ The paper is well-written with a good treatment of relevant literature.
+ The method and experiments are well-documented for reproducibility.

### Weaknesses
- One fundamental concern (a part of which is briefly discussed in Appendix A): considering recent concept-based models that use LLMs for semantics, it can be argued that concepts can directly be interpreted through human-understandable language semantics. How important is visualization in such a scenario? Is it possible to show through some user studies that a user necessarily requires visualization beyond just language semantics in real-world applications? Without this, the premise of this work may be weak.

- A second major concern is the limited baselines used for experimental comparison. Many baselines seem missing: Label-free CBMs, LaBo, Posthoc CBMs, Sparse CBMs. It is not clear why some of these were not considered -- it may not be difficult to adapt some of them for comparison. Further, while some of them lack "visualizability", comparing the proposed method w.r.t. these baselines on other metrics is important for completeness of understanding.

- While the appendix reports many ablation studies, I found in general a lack of depth of analysis of the results, with a propensity of very brief analysis of multiple factors. I would have preferred seeing at least some of the important analysis being carried out in depth. In fact, I found the appendix hard to parse since there were too many studies, but with too little discussion on inferences and take-aways.

- One reference that is close to this work is: "Garg et al, Advancing Ante-Hoc Explainable Models through Generative Adversarial Networks, arXiv:2401.04647, AAAI-W'24". It may be good to compare the proposed work against this paper, since they have similar objectives esp the viewability property.

### Questions
Please see weaknesses above. Below are some additional questions:
* Are there any restrictions of what f and G should be pre-trained on? How close should those datasets be to the one being studied? Since interpretability is the focus of this work, it would be useful to know how semantically related these must be.

### Soundness
3

### Presentation
3

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
A primary limitation in human-understandable concept learning within intrinsic XAI approaches is the effective visualization of learned, unsupervised concept dictionaries, particularly for large-scale images. To address this challenge, the authors introduce VisCoIN, a novel, concept-based interpretable network that includes a concept translator, which maps concept vectors into the learned space within a generative model. Experimental results visualizing the learned concepts highlight the efficacy and practical value of the proposed approach.

### Strengths
- S1: The definition of viewability and the proposed method are clear, well-founded, and intuitive. Experimental visualizations of the learned concept effectively demonstrate its amplified appearance as the lambda value varies within the concept function, providing compelling evidence of the approach's effectiveness.

### Weaknesses
 - W1: The authors introduced an additional pretrained classifier f, and incorporated its output along with g(x) into the output fidelity loss, \( L_{of} \). The rationale behind this approach, however, requires clarification. It would be beneficial for the authors to validate the use of output fidelity loss \( L_{of} \), particularly in comparison to employing cross-entropy loss with ground-truth labels. Specifically, the output fidelity loss seems to be an unnecessary complication, as it introduces a dependence on a potentially flawed pretrained classifier f, rather than directly optimizing for the ground truth labels.

- W2: The auto-encoding objective is inherently insufficient for the acquisition of compositional representations, as the optimization of reconstruction quality does not necessarily entail the disentanglement of features at the object or concept level [1]. The integration of functions \(\Psi\) and \(\Omega\) can certainly be characterized as an auto-encoder architecture. In the main text and appendix, the authors present further applications that employ various functions \( f \) and \( G \). Nevertheless, it would be advantageous to explore modern architectures, such as transformers for \( f \) and diffusion models for \( G \). The current approach using a standard autoencoder may limit the model's ability to capture complex relationships between concepts, and exploring more powerful generative models could lead to more meaningful concept representations.

### Questions
Most of my major questions/concerns are listed in the Weakness sections.

### Soundness
3

### Presentation
3

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
This paper proposes a new system for concept-based interpretable networks, where the learned concepts are transformed to the latent space of a generative model. This transformation is learned, enforcing consistency by minimising the distance loss between the original image, and the image produced by the generative model using the concepts of the original image. This allows users to easily visualise the learned concepts, by generating images in a range for a particular concept.

### Strengths
- I agree with the idea that using examples from your training set that maximally activate a certain concept is not ideal, and the authors address this nicely. The concept visualisations generated are much simpler to understand than concept attribution maps and visualising image patches that maximise the concept.
- Leverages pretrained generative models rather than training an additional decoder, instead using a less complex concept translator, making the method more efficient. 
- The measure of consistency of concept visualisation is novel and seems appropriate as a proxy for human experiments.

### Weaknesses
 - Some of the reconstructions shown throughout the paper are quite far from the original image, and sometimes changing the image quite drastically, such as Figure 4b and more examples in the appendix. This is one benefit existing methods like concept attribution maps have, the concepts are highlighted on the original images rather than relying on a reconstruction. The quality of the reconstruction is not consistent, with some images being very close to the original, while others are significantly altered, raising concerns about the reliability of the concept visualization. The method's reliance on a generative model for reconstruction introduces a potential bottleneck, as the reconstruction is limited by the generative model's capacity to represent the input image.
- Some details in C1.1 on how reconstruction is performed with StyleGAN are important, for example the need for using a secondary, unconstrained representation $\Phi'(x)$, should be in the main text, as this suggests that reconstruction purely based off the interpretable concepts is not possible. This could be added in Section 3.2. The necessity of this secondary representation indicates that the learned concept space is not sufficient to fully capture the information needed for accurate reconstruction, which undermines the claim that the concepts are fully interpretable. The fact that the reconstruction relies on an unconstrained representation $\Phi'(x)$ suggests that the concept translator is not learning a complete mapping from the input image to the latent space of the generative model.

### Questions
- The authors state that the maximum $\lambda$ that is reliable is 3 or 4. Is this due to the magnitude of the concept seen by the translator network during training? And if so, couldn't think potentially be an issue when setting $\phi_k(x)$ to 0 when measuring faithfulness, as this might be outside of the range seen during training for a particular concept.
- $\Omega$ used is a very simple architecture, did the authors ever experiment using multiple layers to allow a more complex transformation?

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
3

### Summary
The paper proposes a new method of interpreting latent features which builds upon concept-interpretable neural networks (CoINs) and adds the new means of interpretation through mapping the latent features into the space of generative models. It helps address the known problem of interpretations of concepts-based models in a way that is complementary to the existing explanations, which often relates the concepts to the real data.

### Strengths
- Correctness: I checked the notation and did’t see any errors. 
- Reproducibility: the paper looks reproducible to me (see Question 3 below)
- Novelty: the method builds upon the existing CoINs methods but provides the new means of interpretation comparing to the original CoIN methods, and therefore is novel in this way. 
- Clarity: the outline of the paper is clear, however with some suggestions on the presentation
- Significance: this work complements previous work on concept-based interpretation. The approach is well-motivated by the need in providing more detailed interpretations of the vision recognition models and is, as the authors discuss in the introduction, well-grounded in the state-of-the-art. The significance of the work is mostly empirical, with the authors presenting both the advantages of the method and the evaluation protocol.

### Weaknesses
 - Clarity: There are a few questions below which could help clarify upon the relation between the method and the by-design approaches.



### Questions
1. It would be important to clarify upon the limitations regarding to the relation of the proposed method to the inherently-interpretable class of methods. Such methods are supposed to provide by-design explanation, where the output is causally related to the explanation. For example, concept bottleneck models (Koh et al, 2020),  ensure such by-design claim by making the prediction directly rely upon the intermediate concepts (i.e., first, we predict a  number of properties, and then infer the class solely on these properties).  In this work, I can identify two points where this by-design property could be broken: (1) I understand that the output depends upon the whole set of features, which means that the less-contributing features can still influence the prediction enough to change the label. Alternatively, one can select only a part of features, perhaps at a cost of accuracy (2) the matching between the latent space and the generative model is performed using a concept translator; it means that in some scenarios the mapping between the latent space and the generative model can be imperfect. One might find it useful, perhaps even at a cost of accuracy, to bridge these gaps and make the classification inherently-interpretable. It may be achieved, to address the by-design limitation (1), by only performing the prediction from the features which contribute the most and discard the rest, and provide by-feature explanations for these features. To address the limitation (2), one may think of learning the latent space in a way that it coincides with the generative model’s one (i.e., through distillation). I wonder if this model allows for this?
2. I see that the model is evaluated using ResNet-50 backbone. I wonder if it can generalise to the transformer-based architectures? In relation to this, would the authors clarify upon the computational overhead of the proposed method in comparison with the CoIN and the ResNet-based models?
3. Figure 4 states “Visual modifications of more local concepts indicated by red boxes” I am not sure I could  understand what it would mean and entirely follow how the red box visualisation works .

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors propose a method to map concept features to a generative model latent space to have a better interpretation of the learned concepts. They focus on concept-based interpretable networks (COIN) to build the visualization system. They evaluate the interpretation in terms of the accuracy of the prediction network (fidelity to output), the fidelity of the reconstruction (fidelity to input), and the fidelity and consistency of the learned concepts. They also propose the analysis of sparsity and viewability (capacity of reconstruction over concepts).

### Strengths
- Writing and Implementation Details: I appreciate the authors' attention to motivating and well-describing the methodology, including detailed implementation parameters in the main and supplementary texts.

- Improvement of general interpretability: the authors present an interesting approach to improve the interpretability of visual networks by learning sparse concepts that can be quantified and visualized.

- Numerous evaluation methods: an important aspect of this work is the aspect in which the methodology is evaluated, which configures an important validation of the proposition: prediction accuracy, fidelity to reconstruction, faithfulness, consistency, sparsity, and viewability.

### Weaknesses
 - Combination of two complex models to interpret and explain: Have you analyzed the problems to include the pre-trained generative network? Is there a bias that could change the visualizations even with the same feature extractor? It seems to me that you are including a new possible bias in the pipeline.
    
    As I understand it, the concept functions are learned along with the concept translator, but in doing so, the latent space of the generator affects the learning concept functions. Can this mean that the bias from both networks is present in these concepts? Are we explaining the feature extractor or the generative model?

- The number of concepts and their semantics: How was the size of the concept dictionary chosen? What happens with smaller K? You show some ablation studies, and then you decide on 64. What about smaller numbers of concepts? It would be interesting to see how the visualizations change depending on that number.

- Faithfulness and consistency: In the paper, the authors mention these evaluations as new, but faithfulness is commonly used as a technique of evaluation [1]. I also understand the approach used as feature (concept) removal. A suggestion to the authors is to also evaluate the effect of inserting only the top concepts into the generated image. Moreover, an interesting evaluation would be the one proposed in the paper of XRAI [2], to iteratively insert the top concepts and analyze the AUC of the accuracy curve. Regarding the consistency, I like this idea, I just have questions about the classifier used to separate the representations with and without the concepts, what is its architecture? Is it linear before decision? How many layers? Also, I would suggest an additional experiment: use a part label dataset like CUB-200 with bird parts and check if the most changed parts when removing a concept are the same for birds in the same class.

- Sparsity and Viewability: I don't see much discussion of these metrics other than the loss used during training. I would like to see at least some viewability analysis (qualitative) and possibly a human evaluation compared to the baseline approaches.

### Questions
Some questions are already presented in the weakness section.

Other questions:

→ Why does the bird head of the first row in Figure 4 also increase in size with the red eye? Is this related to another concept?

→ How did you determine the "name" of the concept? Is it a deduction?

### Soundness
3

### Presentation
3

### Contribution
3

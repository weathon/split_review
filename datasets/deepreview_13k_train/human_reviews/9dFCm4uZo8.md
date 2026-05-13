# Exploring Compositionality in Vision Transformers using Wavelet Representations

- Decision: Reject
- Scores: 5, 5, 6

## Abstract
Insights into the workings of the transformer have been elicited by analyzing its representations when trained and tested on language data. In this paper, we turn an analytical lens to the representations of variants of the Vision Transformers. This work is aimed to gain insights into the geometric structure of the latent spaces of each encoding layer. We use representation-similarity measures, and representation-visualization approaches to analyse the impact of training regimes on the latent manifolds learned. We then use our approach to design a test for quantifying the extent to which these latent manifolds respect the compositional structure of the input space. We restrict our analysis to compositional structure induced by the Discrete Wavelet Transform (DWT). Interestingly, our empirical analysis reveals that ViT patch representations give notions of compositionality with respect to the DWT primitives.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper presents experiments exploring the use of the Discrete Wavelet Transform (DWT) for evaluating compositionality within ViTs. 

The work is motivated by prior work (Andreas 2019) which proposed a general framework (Tree Reconstruction Error, TRE) for measuring compositionality as a homomorphism between the input space and a representation space. 

Because images do not have an obvious set of primitives in the same way that tokenized word vocabularies do in language spaces, this paper proposes to use DWT components as the primitive representation. 

In the first set of experiments, the paper argues that the naive addition of the DWT components will not necessarily yield a compositional representation, and instead proposes to learn a composition function, represented as a weighted sum of the components. 

Experiments applying DWT to the final layer of a ViT are also presented, showing that approximating the ViT representation as the weighted sum (under the learned composition function) of its inverse DWT components yields comparable performance to the model’s output under the original representation. 

I have concerns about the soundness of the experimental setup (see Weaknesses). Given the relaxation introduced in L214-215, it’s not clear to me that the provided experimental results can actually soundly support claims about compositionality since the homomorphism is no longer defined in relation to the input space. 

**Original Recommendation**:
I think the paper presents a compelling idea, but the paper could be greatly strengthened by improvements to clarity and substantiation of claims. I would value hearing the authors’ response to my concerns before finalizing my score, but in its current form I am recommending that the paper be rejected.

**Revised Recommendation (11/29)**: 
The authors have largely addressed my concerns, and so I have revised my overall score to 5. To conclude my score, I agree with some of the concerns that iA5z raised related to how compositionality is generally understood in the community through the lens of semantics rather than appearance, which I don't believe were completely sufficiently addressed. I think the impact of the paper could be stronger with some following changes which I believe would likely constitute a new submission rather than minor revisions: 
 
* (1) The framing of the paper could modified to better motivate why studying the type of compositionality presented is useful. Something that comes to mind is that text-based natural language is *already* an abstracted signal (and which is tied to semantics), perhaps it would make sense to contextualize this paper within compositionality literature for audio signals rather than text. 
* (2) The introduction of further experiments showing how this type of compositionality can be useful in downstream tasks would greatly help to further motivate this approach. For semantic based tasks, compositional representations tend to yield improvements in generalization capabilities of models -- can something analogous to this be shown for DWT based compositional representations? 

In other words, I think the motivation/contribution of the paper would be strongest if it could be shown either that the DWT representations are tied to semantic compositionality, or if not, that this kind of compositionality is still explicitly useful downstream.

### Strengths
* The paper presents a compelling idea — that DWT components could serve as primitives through which to study compositionality in ViTs.

### Weaknesses
Weaknesses:

**Clarity**: The paper can be unclear at times over specifics of what was done or how, I think that further elaboration from the authors throughout could help strengthen the paper.
* Figure 1: What does it mean here for the original image’s representation to be compared to the composed image representation? Does it mean that the maps we see in the figure are the result of of the comparison, or are these just the composed representations and the comparison was done outside of the figure? 
* Section 3.1 ViT: What was the ViT model used for this experiment? What was it pre-trained on? The section does not explicitly specify these experimental conditions. 
* L214-L215: What is the purpose of f_eta ? I understand that this is defined in Andreas 2019, but its definition is missing from this paper. I think explicitly defining it and its role would improve the clarity of this section. 
* Figure 3: What do the C’s and a’s represent? 
* Figure 4: What are LL, LH, HL, and HH? 
* In general, I think the clarity of the paper could be improved by an additional grammar/phrasing pass. 

**Soundness**: I have a few concerns regarding the soundness of the experimental setup, and I am unsure if the paper’s claims are supported. I would value hearing the authors' response to the following points/questions: 
* Section 3.1: I believe this section aims to show that simply adding the DWT wavelets with equal weights does not yield a correct composition. However, this claim is supported by showing results over a single image from a single ViT model. I believe this experiment would need a much larger sample size over images/models in order to make such a broad claim. 
* L216-217: The original compositionality formulation from Andreas 2019 is modified to shift the application of the encoder function from the input space to an arbitrary intermediate representation space within the model. If I’m understanding correctly, doesn’t this violate the core premise of the problem statement? The purpose of compositionallity tests is to find homomorphisms between the **input space** and the representation space, this is important because the input space comes from the data generating function. I’m not sure if it makes sense for this test to be defined for the transformation from one hidden layer to another. Minor, but I would suggest modifying the sentence “instead of drawing exact parallels, we tweak this statement to suit our analysis”, since the wording gives the impression that the formulation was modified to suit the narrative of the paper, rather than the needs of the original empirical question being asked.

**Conclusions/Takeaways**: I believe that the provided experimental results show that the representations of the final ViT layer can be represented as a linear combination of its inverse DWT components. However, given my concerns stated above with soundness, it’s not clear to me what this entails about compositionality.

### Questions
Please see questions under Weaknesses.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper examines a type of compositionality in the representations of vision transformers (ViT). Building on the compositionality concept proposed by Andreas (2019), the authors apply it to Discrete Wavelet Transform (DWT) representations. Empirical results suggest that the last layer of a transformer displays a certain degree of compositionality for a one-level DWT of the input.

### Strengths
* The paper is generally well-written.
* It builds on the well-established framework by Andreas (2019) for compositional representations.
* Wavelets are a common and natural basis for image representations in signal processing.

### Weaknesses
 * My main concern is that the presented results do not convincingly demonstrate compositionality. Rather than defining true combinations of wavelet primitive representations, it appears that the learned weights mainly select the low-pass filtered image (Table 3). Indeed, it is not particularly surprising that the images in Figure 5 perform similarly to the original images. The core issue is that the method does not demonstrate a meaningful combination of the high-frequency wavelet components. The learned weights seem to act as a filter, primarily passing the low-frequency information, which is essentially a downsampled version of the original image. This behavior does not align with the typical understanding of compositionality, where distinct components contribute to a richer representation.
* Compositionality is typically more valuable when components are semantic rather than appearance-based. It is doubtful that wavelets would exhibit compositional properties in the final layers of a model, where higher-level concepts are typically captured; instead, this is more likely to occur in lower-level layers. Furthermore, the idea that wavelets are a good basis for compositional representations is not really explored, and no other decomposition methods are considered or compared. The choice of wavelets as a basis for compositionality is not sufficiently justified. The paper lacks a discussion on why wavelets are expected to be a suitable basis for compositional representations, especially in the context of high-level features learned by the final layers of a vision transformer. The analysis would benefit from a comparison with other decomposition methods, such as DCT or a learned dictionary, to assess the suitability of wavelets for this task.

Minor:
* The organization of the paper could be improved, since details on the framework (Section 3.3) are presented after the initial discussion on quantifying compositionality (Section 3.1). Additional background on wavelet decompositions to clarify notation (e.g., LL, LH, etc., in Figure 4) would also be helpful.
* While it can be guessed, the exact meaning 'convex' and 'conic' relaxations is never explained. Other details could be clarified (see below)

### Questions
* Could the authors clarify why they believe their results demonstrate compositionality, why the DWT is considered a suitable feature decomposition, and why compositional behavior would be expected in the last layer?
* l.299: "The target is the final classification layer output of the original image" does this mean using an L2 loss?
* l.445: Why is the analysis conducted across different settings?

Minor:
* l.237 I believe $E_L$ should be $E_l$.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper investigates whether representations of pretrained ViT models are compositional. The authors use DWT as the primitives (that are composed), and learn the composition (g) rather than assuming additive composition. Experiments are conducted on the final layer's output representation, and a subset of ImageNet-1k is used.

### Strengths
1. The paper investigates a novel approach to a significant problem. Importantly the authors show that learning a composition is significantly better than composition by addition.
2. The authors investigate the learning of composition to some extent - trying variant such as conic, convex and unconstrained.

### Weaknesses
1a. I believe the author's experimental setup is not using sufficient data. For reference, papers such as ViT-NeT which explores interpretability of ViT uses three datasets each of which is 10-20k images total. I'd suggest authors scale up their datasets - if we choose to use ImageNet-1k, a test set of at least 10 images per class would be more convincing. Currently, with a 15% test fraction, each class gets 1-2 images. I hesitate to make conclusions based on such a small test set per class.

1b. No significant analysis is done on the test dataset, nor of the errors that composition leads to. It would be beneficial to provide some examples where composition lead to large error and some examples where the error is minimal. For example, Haar DWT is great when we have sudden transitions in signal - like sharp images. Perhaps blurrier examples or classes would cause larger error?

2. Authors do not inspect intermediate layers of ViT, which is a glaring hole to me - while it is true that most downstream tasks will use the penultimate layer of the ViT, I am still left wondering if all intermediate representations are composable, if its just some of them, is compositionality lost at some levels of the stack? I would recommend repeating the same analyses using intermediate layers’ representations.

### Questions
1. Could the authors clarify how compositionality with discrete wavelet transforms leads to better explainability? Some examples or related work would help. I can see some intuitive argumentation but I think it has not been articulated in the paper.

2. The observation that convex combination of sub-bands in image space alters pixel values significantly is interesting. Why does it not degrade accuracy? Is it because of normalization?

### Soundness
3

### Presentation
3

### Contribution
2

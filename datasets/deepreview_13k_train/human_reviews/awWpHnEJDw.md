# The Hidden Language of Diffusion Models

- Decision: Accept
- Scores: 6, 6, 6, 6

## Abstract
Text-to-image diffusion models have demonstrated an unparalleled ability to generate high-quality, diverse images from a textual prompt. However, the internal representations learned by these models remain an enigma. In this work, we present  \textsc{Conceptor}, a novel method to interpret the internal representation of a textual concept by a diffusion model. This interpretation is obtained by decomposing the concept into a small set of human-interpretable textual elements. Applied over the state-of-the-art Stable Diffusion model, \textsc{Conceptor} reveals non-trivial structures in the representations of concepts. For example, we find surprising visual connections between concepts, that transcend their textual semantics. We additionally discover concepts that rely on mixtures of exemplars, biases, renowned artistic styles, or a simultaneous fusion of multiple meanings of the concept.
Through a large battery of experiments, we demonstrate \textsc{Conceptor}'s ability to provide meaningful, robust, and faithful decompositions for a wide variety of abstract, concrete, and complex textual concepts, while allowing to naturally connect each decomposition element to its corresponding visual impact on the generated images.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper delves into understanding the internal representations of text-to-image diffusion models, which have shown significant prowess in generating high-quality images from textual concepts. The primary challenge addressed is deciphering how these models map textual prompts to rich visual representations. The authors introduce a method, "CONCEPTOR", that decomposes an input text prompt into a set of interpretable elements. This decomposition is achieved by learning a pseudo-token, which is a sparse weighted combination of tokens from the model's vocabulary. The goal is to reconstruct the images generated for a given concept using this pseudo-token. The method facilitates single-image decomposition into tokens and semantic image manipulation.

### Strengths
The authors propose a novel view to interpret the internal representations of T2I diffusion model, decomposing the input text prompts into a set of prototypes. Image manipulation can be implemented by simply adjusting the coefficients of these prototypes  

The method is general and flexible, as it can be applied to any T2I diffusion model without modifying the model architecture or training procedure. 

The writing is good and clear. The paper also provides empirical evidence to support the effectiveness and efficiency of the method.

### Weaknesses
The number of concepts (prototype) are limited, which can not prove whether the proposed method is effective on large-scale concepts.

The concept decomposing can be viewed as an inner interpolation between the concepts. What if the image are out of domain? Is it possible to show some cases? Can you provided some analysis the between the proposed method and interpolation method?

### Questions
See the Weaknesses.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper attempts to explore the correlations between different textual concepts, by exploring how well they can help reconstruct images of a certain concept with diffusion models. The method is a variation of textual inversion, by incorporating many words from a vocabulary and learning the weights of words (instead of embeddings a new word).

### Strengths
The idea of finding the correlations between different textual concepts is interesting. The authors presented some interesting results, such as "snake = twisted + gecko" (Figure 2).

### Weaknesses
My biggest concern is that it's unnecessary to use image reconstruction as a proxy to find the combination weights (Eq.3). This method can totally work in the CLIP text space only. I've tried to compute the textual similarity of the words presented in Figure 2:

Triplet: 'camel' and 'giraffe'  'cashmere'
- 'camel' vs 'giraffe': 0.834
- 'camel' vs 'cashmere': 0.774
- 'camel' vs 'giraffe' + 'cashmere': 0.872

Triplet: 'snail' and 'ladybug'  'winding'
- 'snail' vs 'ladybug': 0.768
- 'snail' vs 'winding': 0.816
- 'snail' vs 'ladybug' + 'winding': 0.855

Triplet: 'dietitian' and 'pharmacist'   'nutritious'
- 'dietitian' vs 'pharmacist': 0.878
- 'dietitian' vs 'nutritious': 0.874
- 'dietitian' vs 'pharmacist' + 'nutritious': 0.915

Triplet: 'snake' and 'twisted'  'gecko'
- 'snake' vs 'twisted': 0.869
- 'snake' vs 'gecko': 0.848
- 'snake' vs 'twisted' + 'gecko': 0.913

Triplet: 'reflections of earth' and 'sphere'    'civilization'
- 'reflections of earth' vs 'sphere': 0.761
- 'reflections of earth' vs 'civilization': 0.804
- 'reflections of earth' vs 'sphere' + 'civilization': 0.831

Triplet: 'fear' and 'scream'    'wolf'
- 'fear' vs 'scream': 0.892
- 'fear' vs 'wolf': 0.875
- 'fear' vs 'scream' + 'wolf': 0.926

We can see that for a triplet A,B,C, the similarity of A vs. (B+C) is always higher than A vs B or A vs C. That means similar semantic correlations already exist in the CLIP text embedding space. Intuitively, since CLIP text embeddings are to be aligned with image features, such similarities in the image features will propagate to the text embedding space.

Therefore, doing image reconstruction with T2I diffusion model is unnecessary. If we only mine such triplets from the CLIP text embedding space, then the contribution of this paper becomes quite small. Therefore, I suggest rejection.

### Questions
N/A

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper ‘Hidden Language of Diffusion Models’ designs an interpretability framework for text-to-image generative models. This framework relies on learning coefficients of word-embeddings such that the reconstruction loss in diffusion models is minimized with additional constraints to ensure sparsity of concepts which are selected.  Overall, the paper provides a simple framework to decompose concepts into sub-concepts to interpret diffusion models.

### Strengths
- The paper is extremely well-written and easy to follow throughout. Good job on this!
- The idea about learning the coefficients of the word-embeddings while minimizing the diffusion reconstruction loss is very simple and easy-to-implement while producing good interpretability understanding. It can be a good tool to interpret diffusion models through the lens of how concept dissection works in text-to-image generative models. 
- Given that there does not exist significantly good benchmarks on testing concept-decomposition and also baselines, the authors have done a satisfactory job of comparing with PEZ and other heuristic variants using BLIP-2. The ablations are also presented in depth.

### Weaknesses
Cons / Questions : 
- While the paper provides a good interpretability framework for image generation through the lens of concepts I have some doubts on it’s downstream application. Can the authors elaborate a little bit on how Conceptor can be used for a particular downstream application (e.g., bias mitigation given that Conceptor can detect biases?)
- Can the authors elaborate if the concept decomposition is an artifact of the particular CLIP text-encoder in Stable-Diffusion? Will one get similar concept-decomposition patterns if a different text-encoder is used (e.g., T5 like in DeepFloyd)? I would imagine this to be a positive answer, but might expect different patterns, so I believe it’s important to use Conceptor to understand this phenomenon.
- I am a little curious about how much the diffusion objective plays a role in concept-decomposition. For e.g., given the objective of reconstruction, I will expect the faithfulness metric of Conceptor to be better than other methods (e.g., PEZ). However, if you use the same idea with CLIP loss (replacing the reconstruction loss in Eq. (6) with L_clip), will you get similar decomposition? And will those decompositions transfer to diffusion models?  In fact, if you use CLIP's representation for a particular token as a ground-truth with optimizing for Eq.(3), you should get a reasonable reconstruction still, which can be a cheap baseline. Did the authors run this ablation?
- How can you extend your framework to more complex concept-decomposition? The current framework generates images corresponding to single concepts, but images are usually consisting of multiple concepts. In this scenario, how can one use Conceptor to understand sub-concepts? I think this is one experiment, the paper is lacking.

### Questions
Refer to the previous section. 

Overall, I feel that the paper is good but will like the authors to respond to the Cons/Questions.  The major question I have about this framework,(i)  is how can it be used to mitigate some of the issues in diffusion models (e.g., bias)?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper proposes to use a weighted linear combination of existing word embeddings to represent an image (i.e., weights are optimized through two MLP layers) such that it enables image decomposition based on a set of human understandable tokens using pretrained text-to-image diffusion model such as Stable diffusion models.

### Strengths
- the motivation of the paper is clear and well conveyed.
- the experiments are well-conducted and extensive.
- The approach enables human interpretable decomposition using a set of learnable weights and associated tokens, which has inherited the same outcome from the classic word2vec arithmetic paper [1].

[1] Mikolov et al., Efficient Estimation of Word Representations in Vector Space. ICLR 2013

### Weaknesses
 - lack of related previous work on image decomposition, which can be seen as a way to interpret models, such as FineGAN (Sing et al, 2019), GIRAFFE (Niemeyer etal, 2021), SlotAttention (Locatello etal, 2020), DTI Sprites (Monnier etal, 2021), GENESIS-V2 (Engelcke etal, 2021) and follow-up works. There also exists earlier/concurrent work that conducts image decomposition using text-diffusion models, so its worth discussing pros and cons but may not need comparison if works are concurrent.
- most of concepts shown in the paper are mainly objects, thus its ability to learn abstract concepts is not clear. For example, how does it perform on abstract concepts such as object relationships. Though, I tend to think that the model is rather limited in understanding complex concepts other than objects.
- The method essentially utilizes arithmetic with word embeddings which have been widely used in the past, so it doesn't seem to be novel enough. Applying this method to a text-to-image diffusion model doesn't show novelty from my perspective.

### Questions
- I'd love to see if u can optimize on electrician image and then try removing the brush concept, does it become a painter? 
- How long does this optimization process take for each image?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
2 fair

# How Many Van Goghs Does It Take to Van Gogh? Finding the Imitation Threshold

- Decision: Reject
- Scores: 5, 6, 5

## Abstract
\vspace{-0.5em}
Text-to-image models are trained using large datasets collected by scraping image-text pairs from the internet. These datasets often include private, copyrighted, and licensed material. 
Training models on such datasets enables them to generate images with such content, which might violate copyright laws and individual privacy. 
This phenomenon is termed \textit{imitation} -- generation of images with content that has recognizable similarity to its training images. In this work we study the relationship between a concept's frequency in the training dataset and the ability of a model to imitate it. We seek to determine the point at which a model was trained on enough instances to imitate a concept -- the \textit{imitation threshold}. 
We posit this question as a new problem: \textbf{F}inding the \textbf{I}mitation \textbf{T}hreshold (\taskname) and propose an efficient approach that estimates the imitation threshold without incurring the colossal cost of training multiple models from scratch. 
We experiment with two domains -- human faces and art styles -- for which we create four datasets, and evaluate three text-to-image models which were trained on two pretraining datasets. 
Our results reveal that the \textit{imitation threshold} of these models is in the range of 200-600 images, depending on the domain and the model. 
The \textit{imitation threshold} can provide an empirical basis for copyright violation claims and acts as a guiding principle for text-to-image model developers that aim to comply with copyright and privacy laws.git}. }

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper makes the following claims:
- Relationship between a "concept's" frequency in training dataset and the ability of a text to image model to imitate it. They find the threshold to be 200-600 images 
- Propose an efficient approach to estimate the imitation threshold 



I have the following questions and suggestions. I am willing to change my review based on the authors' response.

1. The paper does not define "concepts," assuming they are either self-explanatory or domain-specific. This assumption introduces potential bias or error in the paper's claims.
    - How distinct should concepts be from one another to qualify as separate concepts? How is the distance between concepts computed? For instance, many artists share "styles" due to shared lineage, schools, or subjects, which can significantly impact the imitation threshold. Broad art styles like "Avant-Garde," "Deco," or "Baroque" are loosely defined. Depending on how a concept is defined, the result of 200-600 images could vary significantly. 

    - Many concepts, such as art styles, overlap and are composite. For example, Cubism, Futurism, and Constructivism share many features, as do Realism, Photorealism, and Precisionism, or Expressionism, Fauvism, and Die Brücke. Furthermore, concepts like "cubist impressionism" merge cubism and impressionism. The paper does not provide details on defining a concept or its boundaries, making it difficult to justify the main motivation and claim of efficiently estimating the imitation threshold of a "concept." In cases of composite and overlapping concepts, learning one concept may transfer to another, leading to erroneous imitation thresholds. This makes it hard to justify the paper's main motivation and claim (L91-95, L21-25) of that of efficiently estimating the imitation threshold of a "concept". 


1. L148-151 - How do the authors make sure that the increasing number of samples of a particular concept is *causing* the models to learn to imitate? For example, how do we discount the case that if we train a diffusion model on 1 million concepts with each concept represented by 100 images (well below the imitation threshold of any individual concept), the model may still be able to imitate a particular concept due to an overall increase in general image generation understanding? Again, this relates to the main claim of the paper (L91-95, L21-25) of that of efficiently estimating the imitation threshold of a "concept." The paper seems to address a causal question without providing sufficient causal analysis.

1. The assumptions of the paper are too strict, which makes the method to be of much practical relevance. 
    - Particularly, the following two assumptions are idealistic: distributional invariance between the images of all concepts in a domain and no confounders between the imitation score and image count. Can the authors justify these assumptions? Further, can the authors show experiments upon loosening these assumptions? 
    - Can we introduce error bounds to account for the strict assumptions? This is important, especially since the abstract and introduction both try to answer a legal question (L24-25, L36-39) with a very prescriptive answer in the abstract, introduction, and results section (200-600 images in general and specific numbers like 364 and 234 images for different models in L342-355) without contextually mentioning the strict assumptions under which their analysis holds true or mentioning the error bounds. One gets to know the limiting assumptions, only when one reads the paper in details. While this may not be author's intention, but this gives a false assumption about the correctness/error bounds of the various imitation threshold numbers.


1. Another (strict) assumption not listed in the assumption section is L240-242 "prompts are distinct from the captions used in the pretraining dataset to minimize reproduction of training images". (Since the paper mentions the case of StabilityAI) Interestingly, In the famous New York Times vs. OpenAI lawsuit, the lawyers tested GPT, especially flouting this assumption. They start the prompt with the first few words of New York Times articles and let GPT complete the rest of the article [1]. Their case mentions many examples where exact reproduction is observed. This is an example of an imitation. How does the paper address such (actual) cases of imitations when discussing the "imitation threshold"?  Further, this assumption should be noted in the assumption section and when claiming prescriptive thresholds of 200-600 images.



1. In Sec-5.2, I could not understand why the same classifier couldn't be used as was trained in Sec-5.1 (potentially, along with the other classifiers the paper uses).




[1] https://nytco-assets.nytimes.com/2023/12/NYT_Complaint_Dec2023.pdf

### Strengths
Mentioned in the summary section

### Weaknesses
Mentioned in the summary section

### Questions
Mentioned in the summary section

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
4

### Summary
The paper formalizes and investigates a novel problem of Finding the Imitation Threshold (FIT), which aims to determine the imitation threshold for two representative image types: human faces and art styles. Comprehensive empirical analysis of Stable Diffusion models and their respective pre-training datasets reveals that the imitation threshold for these models ranges between 200 and 600 images, depending on the setup. The estimated thresholds have important implications for users and developers, potentially serving as a basis for copyright and privacy complaints.

### Strengths
* The investigated problem of imitation in text-to-image models is both prevalent and significant. 

* By introducing novel methods for estimating concept frequency, the proposed MIMETIC2 is carefully designed to minimize the influence of confounding factors. 

* This paper marks the first effort to provide precise estimates of the imitation threshold, offering implications that could benefit both technical advancements and policy-making.

### Weaknesses
* While this paper represents a novel attempt to determine the imitation threshold of concepts in text-to-image models, its technical implications are unclear. The memorization phenomena in LLMs [1] and VLMs [2], along with their training dynamics, are well-explored areas. Although the paper introduces concept frequency and imitation score estimation methods to establish a more precise threshold, it is not evident what technical insights this threshold provides. Apart from conceptual policy-making related implications (i.e., informing text-to-image model developers what concepts are in risk of being imitated, and serving as a basis for copyright and privacy complaints), how can this metric possibly be adopted to advance imitation mitigation strategies, such as those outlined in Appendix A? This is an important and practical issue that must be clearly explained.

* Additionally, the analysis presents conflicting explanations for threshold differences. In Line 347, the authors attribute the higher threshold in SD2.1 to its larger LAION-5B pre-training dataset, while in Line 350, they suggest differences in text encoders between SD2.1 and SD1.5 as the key factor. This raises an important question: what is the primary driver of these threshold differences—dataset size or text encoder architecture? Moreover, the paper does not explore other potentially influential factors, such as model size, which limits the comprehensiveness of the analysis.

[1] Kushal Tirumala, Aram Markosyan, Luke Zettlemoyer, Armen Aghajanyan. "Memorization Without Overfitting: Analyzing the Training Dynamics of Large Language Models." NeurIPS 2022.

[2] Jie Ren, Yaxin Li, Shenglai Zeng, Han Xu, Lingjuan Lyu, Yue Xing, Jiliang Tang. “Unveiling and Mitigating Memorization in Text-to-Image Diffusion Models Through Cross Attention.” ECCV 2024.

### Questions
Please refer to the Weaknesses section and address the concerns listed.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The author experimentally  explored the number of data samples required for a text-to-image model to generate outputs that exceed the imitation threshold for a given concept, meaning that truly convincing imitation can be considered to exist. The author proposed MIMETIC2 to address the high computational cost of existing approaches.

### Strengths
The authors try to determine the number of training samples required for a text-to-image model to truly imitate a specific concept, and the problem is well-motivated.

The manuscript has clear logic, from the definition of the problem, rigorous assumptions statement, and experimental verification.

The authors discuss the limitations of the current work in assumptions and problem simplification and clarify valuable future work

### Weaknesses
1. The findings are based on limited experiments, which constraints the insights of the results. Under the strict assumptions set by the author, giving quantitative relationship between Concept Similarity and Concept Frequency or an imitation threshold that generalizes to other datasets, such as Laion-400m [1], will be more meaningful. For example, if the quantitative relationship shows exponential decay or exponential increase, it would reflect the possibility of whether a small sample is sufficient to raise infringement issues in a social sense, giving the model trainer a guidance on data usage.

2. The experimental results show limited insights, the types of datasets and models are limited, and are tailored to meet the assumptions pointed out by the author. Although the author lists the challenges encountered in the experiment, such as outliers, there lacks a discussion about  feasible solutions. In general, the scenarios considered are too few and too strict, which is far from the practicality of achieving the goal of the paper demonstrated in Section 1, such as judging whether the infringement claim is established and guiding developers to avoid infringement.

3. It is recommended that the author add optimal approach to find the imitation threshold (Pearl (2009)) as a comparison to verify the correctness of the imitation threshold calculated by the proposed MIMETIC2 method.

[1] Schuhmann, C., R. Kaczmarczyk, A. Komatsuzaki, A. Katta, R. Vencu, R. Beaumont, J. Jitsev, T. Coombes, and C. Mullis (2021). “LAION-400M: Open Dataset of CLIPFiltered 400 Million Image-Text Pairs”. In: NeurIPS Workshop Datacentric AI. FZJ-2022-00923. Jülich Supercomputing Center

### Questions
1. I hope the author can further clarify the given experiment found that the imitation threshold is 200-600 images. Is it a generalized result in a wide range of scenarios, such as other datasets Laion-400m [1], so as to truly provide valuable guidance for judging whether the infringement claim is established and guiding developers to avoid infringement?

2. If the imitation threshold is not reached, can it be considered that there is no infringement?

3. Can the quantitative relationship between Concept Similarity and Concept Frequency be given? 

4. Add optimal approach to find the imitation threshold (Pearl (2009)) as a baseline comparison to verify the correctness of the MIMETIC2 method will be better to evaluate whether the improvement in time efficiency lead to a loss in accuracy of imitation threshold  estimation.

[1] Schuhmann, C., R. Kaczmarczyk, A. Komatsuzaki, A. Katta, R. Vencu, R. Beaumont, J. Jitsev, T. Coombes, and C. Mullis (2021). “LAION-400M: Open Dataset of CLIPFiltered 400 Million Image-Text Pairs”. In: NeurIPS Workshop Datacentric AI. FZJ-2022-00923. Jülich Supercomputing Center.

### Soundness
2

### Presentation
3

### Contribution
2

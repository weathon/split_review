# Semantic Memory Guided Diffusion Networks for Image-to-Long Text Generation

- Decision: Reject
- Scores: 5, 5, 5, 5

## Abstract
Automatic describing image with comprehensive textual content is often demanded by different real-world applications, which motivates image-to-text generation tasks such as image captioning. However, conventional tasks mainly focus on generating short text, which often fail to deal with challenging scenarios that long text is inevitable required to describe enriched and diversified visual contents. Therefore, a more generic solution, which should be able to generate text with arbitrary length (long text in most cases), is expected to overcome limitations from existing approaches such as inability to generate sufficiently comprehensive and complete textual content and ensure semantic coherence in it. To address such limitations, we propose a dedicated solution, semantic memory guided diffusion networks (SeMDiff), for image-to-long text generation (I2LTG), which explicitly captures salient semantics from the visual contents, and further record and calibrate them by memory networks to facilitate the text generation process. Specifically, we employ semantic concepts as the vehicle to deliver and process semantics embedded in images, where they are predicted from each image and enhanced in memory, then serve as the condition to guide diffusion networks for iterative generation. Experimental results on three public datasets and a new proposed one with more than 54K instances demonstrate the superiority of our approach compared to previous state-of-the-art solutions. Further analyses illustrate that our approach offers an effective diffusion-based solution with external guidance for long text generation under different cross-modal settings.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a new challenging task, image-to-long-text generation. To overcome the limitations of existing approaches such as the inability to generate sufficiently comprehensive
and complete textual content. The authors introduce a semantic memory-guided diffusion network (SeMDiff), which captures the essential semantic information of images through a semantic concept predictor, and enhances the semantic representation through a semantic conditional memory module. Afterward, a diffusion decoder module is employed to generate comprehensive and coherent long texts.

### Strengths
1. The problem of long-text generation this paper addressed is an interesting and important task.
2. The proposed method looks technical and sound.
3. The proposed new dataset COCO-LT is technically reasonable and maybe useful in the future.
4. The paper is well-organized and easy to read.

### Weaknesses
1. In section 2.2, the initialized matrix contains a series of semantic vectors to cover all possible concepts, but how to get the semantic vectors of these concepts is not mentioned. It is unclear if these vectors are pre-trained embeddings from a large language model or randomly initialized. The lack of clarity on this initialization process makes it difficult to assess the validity of the approach.
2. The statement of the semantic conditional memory is not clear. In section 2.3, the description of “the memory stores the information in aligning image and texts” is ambitious. What is the specific information here, and how it is obtained? The mechanism by which the memory module learns and stores image-text alignment is not sufficiently detailed. It's unclear how the memory vectors are updated and how they contribute to the diffusion process.
3. Although the purpose of the proposed approach is to solve the long text generation problem, I think it is still necessary to test on some short caption benchmarks, such as MS-COCO. This would provide a more comprehensive evaluation of the model's capabilities and allow for comparison with a wider range of existing methods.
4. The metric CIDEr is missed, which is a very important metric in the image captioning task. The absence of this standard metric makes it harder to compare the proposed method with other image captioning models.
5. I think the comparison in Table 2, 3 is not fair. Only SEMDIFF is transformer-based while others are all ResNet-101-based. There have been some other Transformer-based methods [1,2] for image captioning task are proposed. Among them, [1] is also a diffusion-based method. I think comparing with these approaches will further strengthen this paper. The comparison should include methods with similar architectures to provide a more accurate assessment of the proposed method's performance.

### Questions
1. In Table 4, the results of existing state-of-the-art solutions reported are zero-shot or fine-tuned, and SeMDiff is the zero-shot or fine-tuned? If the results of SOTA are zero-shot, how about the fine-tuned performance on these datasets?
2. The initialized matrix contains a series of semantic vectors of possible concepts, is it a fixed matrix in the whole training process? Or it will be different for different samples?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper targets the long image captioning generation. In this paper, a Semantic Concept Predictor is proposed to predict the key concepts in the text, and a set of memories is introduced to enhance the concept representations. The method is tested on different long captioning datasets and the results are promising.

### Strengths
The paper proposes an interesting structure to catch the key concepts and enhance them with auxiliary memories. 
The techniques are sound and easy to follow.

### Weaknesses
I think Experiments need to be improved. Some part of it is confusing. Table 2, shows the contribution of different components. We can find that the simple basic model ("Trans") provides a strong baseline, especially in LN, COCO-LT, and CC-SBU. This erodes the contribution of the proposed methods: As a simple baseline can achieve impressive performance, can the methods developed for MIMIC-CXR also be efficient on them? The authors did not explore this in the experiments. Also, some LLM are evaluated on them, while it is not sure if they are finetuned on the training sets. As a simple 6-layer transformer encoder-decoder can achieve 0.054 of BL4, it is confusing why the LLM like LLAVA achieves only 0.06 after finetuning. I think this is an interesting point the author needs to explore further in the paper. 

Checking Table 3, we can find the proposed method beats the SoTA methods in quite limited scales, like 0.412 vs 0.407 for B1, and 0.129 vs. 0.126 for B4. It is hard to tell if the proposed method is really better than the existing ones. One option here to prove their effectiveness is to adapt the proposed modules to the SoTA method. 

Section 4.2 investigates 3 different hyperparameters of the methods, while the size of the semantic concept set is also significant to be explored. Answering some questions like the following can make readers understand the method better: Is the semantic concept set the larger the better? Are the predicted concepts the more the better for the long captioning generation?

### Questions
Please refer to the weakness.

I am also confused about Fig. 15 and 16. It seems h^hat_0 is a probability of h^hat_1, h^hat_2, ... with other variables. While h is usually used as the "hidden state". I am not sure why h^hat_0 equals the products of a set of probabilities. it seems p(h^hat_0|h^s, h) would be more reasonable here. Please correct me if I have some misunderstanding.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this paper, the authors introduce SEMDIFF, a diffusion-based model equipped with memory networks tailored for I2LTG. Initially, SEMDIFF identifies main semantic concepts within images. It then leverages a memory network to convert these concepts into the diffusion networks to seamlessly integrate them, enhancing the long-text generation process. By doing so, SEMDIFF effectively tackles challenges like incoherence in non-AR text generation, particularly evident in lengthy texts by embedding external guidance within the diffusion iterative generation. The experimental evaluations are conducted on three public datasets, along with COCO-LT, which demonstrate the effectiveness of SEMDIFF over existing state-of-the-art solutions.

### Strengths
- The paper is overall organized, facilitating a smooth reading experience. Additionally, the inclusion of model overviews and illustrative figures for the components simplifies the understanding of the proposed method. 
 
- The experimental results well validate the approach. Notably, the paper not only presents comparisons with SoTAs, but also comprehensively study the effects of the modules in the framework with ablation studies. 

- The authors have included detailed hyperparameter settings in their implementation to enhance the reproducibility.

### Weaknesses
 - While the paper provides valuable insights, there are areas in the methodological presentation that could benefit from further rigor. Specifically:
    - The definition of $\mathbf{n}$ in Eq (12) is absent from the document. It is unclear if $\mathbf{n}$ represents a noise vector sampled from a standard normal distribution, or if it is a learned parameter. This ambiguity hinders the understanding of the diffusion process.
    - The cross-entropy loss, denoted as $\mathcal{L}_\text{CE}$, is not formally introduced. The paper does not specify which probability distributions are being compared, nor does it clarify how the loss is computed with respect to the outputs of the various modules. This lack of clarity makes it difficult to understand the training objective.

While the authors might perceive some of these notations and concepts as commonly understood within the field, it would enhance the clarity and comprehensiveness of the paper to formally define them. Furthermore, this would enhance the presentation clarity and explain these losses relate outputs from various modules, offering readers a more cohesive understanding of the methodology.
 

- While the authors have illustrated the effects of diffusion decoding across different timesteps through experiments, the results primarily lean towards a qualitative nature. For a comprehensive understanding, would it be feasible to provide quantitative assessments to delineate these differences? For example, reporting BLEU scores or other relevant metrics at different timesteps would provide a more rigorous analysis of the impact of the diffusion process.

- Some properties of diffusion models are not studied in the paper. For example, the guidance of diffusion models are known for enhancing the correlation between the generation and the semantic condition for better controllability. Does this properties further enhance in the case of long-text generation? It would be valuable to explore how the semantic guidance influences the generation quality and coherence of long texts.

- The diffusion models are also known for its computation complexity in the generation, as it requires thousands of NFE in the generation. How does it increase the model computation compared with baselines is not fully studied in the paper. A detailed analysis of the computational overhead introduced by the diffusion process, including a comparison with the computational cost of the baselines, is necessary for a complete evaluation of the proposed method.

- The configuration regarding the settings of diffusion models is not clearly presented in the paper. How do you choose the diffusion schedule? Do you take DDIM/ODE or DDPM/SDE steps in the reverse process? The specific choices of the diffusion schedule and the sampling method significantly impact the performance and efficiency of the model. The paper should provide a detailed explanation of these choices and their implications.

### Questions
Please refer to the Weakness.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces a diffusion-based text generation method I2LTG which uses semantic concepts extracted from training datasets to help with diffusion-based text generation. Semantic Concept Predictor predicts the relevant semantic concepts given initial semantic matrix and visual features. Then, Semantic Conditional Memory aggregates the semantic concepts through memory vectors and mechanism before feeding the memory responses to the diffusion decoder. Experiments show that the I2LTG model is able to achieve superior long-text generation performance, compared to existing works.

### Strengths
- Predicting semantic concepts as an intermediate representation for (long) text generation is an interesting and unique approach. It also makes good sense intuitively.
- Results are good.

### Weaknesses
 - The proposed method requires semantic concepts to be obtained from existing datasets. There is no indication that the validation/test set was not used. It would be cheating if the method indeed used validation/test set for extracting semantic concepts. There would be strong hints provided to the model.
- Not sure which visual backbone is used. Is it comparable to backbones used by other methods?

- In 2.3, the word "conditional" is not mentioned at all. What is the point of calling the corresponding component as Semantic "Conditional" Memory?

### Questions
- In 2.3, the word "conditional" is not mentioned at all. What is the point of calling the corresponding component as Semantic "Conditional" Memory?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

# Fair Text-to-Image Diffusion via Fair Mapping

- Decision: Reject
- Avg Score: 5.40
- Scores: 5, 5, 6, 5, 6

## Abstract
In this paper, we address the limitations of existing text-to-image diffusion models in generating demographically fair results when given human-related descriptions. These models often struggle to disentangle the target language context from sociocultural biases, resulting in biased image generation. To overcome this challenge, we propose Fair Mapping, a flexible, model-agnostic, and lightweight approach that modifies a pre-trained text-to-image diffusion model by controlling the prompt to achieve fair image generation. One key advantage of our approach is its high efficiency. It only requires updating an additional linear network with few parameters at a low computational cost. By developing a linear network that maps conditioning embeddings into a debiased space, we enable the generation of relatively balanced demographic results based on the specified text condition. With comprehensive experiments on face image generation, we show that our method significantly improves image generation fairness with almost the same image quality compared to conventional diffusion models when prompted with descriptions related to humans. By effectively addressing the issue of implicit language bias, our method produces more fair and diverse image outputs.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper discusses the problem of demographic bias in text-to-image diffusion models, which often produce biased images due to sociocultural biases in language. The authors propose a solution called "Fair Mapping," which is a model-agnostic and efficient method that modifies pre-trained text-to-image models to generate fair images. This is achieved by adding a linear mapping network that updates a small number of parameters, thus reducing computational costs and speeding up the optimization process.

### Strengths
1. The paper is well-written and easy to follow.
2. The method is intuitive and reasonable.
3. The experimental results seem promising.

### Weaknesses
1. This paper only considers bias within text embeddings and does not extend to biases that may be inherent in the diffusion model itself. This limitation is significant as it suggests that the system could be susceptible to manipulation if the text embedding model is altered. A more holistic approach that also scrutinizes and corrects for biases within the diffusion model could potentially offer a more robust and less vulnerable solution. Specifically, the method's reliance on modifying text embeddings leaves it open to adversarial attacks that could manipulate these embeddings to reintroduce or amplify biases. The paper does not explore the potential for such attacks or discuss methods to mitigate them, which is a significant oversight. Furthermore, the approach does not address biases that may arise from the diffusion process itself, such as biases in the sampling or generation stages, which are also critical to the overall fairness of the system.
2. The experiments are limited to biases related to gender and race, omitting other prevalent societal biases such as ageism, socioeconomic status and religious discrimination. This narrow focus limits the generalizability of the proposed method and its applicability to real-world scenarios where multiple forms of bias often intersect. The paper should at least acknowledge these limitations and discuss how the method might be extended to address other types of biases. For example, the current approach might not be effective in mitigating biases related to age or socioeconomic status, which may require different types of interventions or data augmentation strategies.

### Questions
Refer to the weeknesses mentioned above.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper addresses human-related bias in text-to-image diffusion models, and resolves the issue by proposing a novel fair mapping module which outputs a fair text embedding. Such a module can be trained on top of frozen pre-trained text encoder, and inserting the module during sampling successfully mitigates textual bias. Training the fair module involves two loss terms: (i) text consistency loss, which preserves semantic coherence, and (ii) fair distance penalty, which brings output embeddings within different sensitive groups close together. Further, the authors propose a novel evaluation metric, FairScore, which also plans to achieve the conditional independence of the text prompt and sensitive group information.

### Strengths
- The paper tackles a timely and practically-relevant problem supported by a fair amount of experiments. Building fair diffusion models is an area with limited prior research, making this work particularly valuable.
- The proposed method is simple yet effective, and pluggable without modifying the pre-trained model. 
- Overall, the paper is clearly written and easy to follow.

### Weaknesses
 - Although the paper covers a good amount of relevant previous studies, the paper lacks baseline experiments. For example, despite [1] focus on fair-guidance while this work focus on pluggable mapping module, the authors can calculate FairScore and compare w.r.t. training time, overhead memory, etc.  
- While the unfairness is largely resolved through the proposed mapping module, such a result may not come at a surprise since FairScore and the employed fairness loss term are quite similar. 
- The authors note that a detector network is employed to identify predefined sensitive keywords in the input prompts. There is no additional detailed explanation about the detector network.
- This method explicitly needs a labeled dataset to mitigate the demographic bias in diffusion models. However, in real-world scenarios, it may be challenging to identify and address all potential types of bias comprehensively. Further, there are remaining questions regarding whether it is feasible to (i) simultaneously eliminate multiple types of bias or (ii) sequentially address multiple biases without negatively impacting performance. If such challenges cannot be properly addressed, it would incur a significant amount of training time to erase all types of biases, and heavy memory cost to save all mapping modules corresponding to each bias type.

### Questions
- How many random seeds are used throughout the experiments? 

[1] Friedrich et al., “Instructing Text-to-Image Generation Models on Fairness.” 2023.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces a method that addresses diversity limitations of text-to-image diffusion models caused by language biases. The proposed approach, Fair Mapping, involves training a mapping network that tries to preserve the original semantics specified in the text while increasing the representation of sensitive groups in the generated images. The mapping network is lightweight as it operates on embeddings from a frozen text encoder. The authors evaluate their method on human-centric generation and demonstrate that Fair Diffusion improves upon biases rooted in occupations and emotions.

### Strengths
- The proposed method is simple and easy to understand.
- The mapping network is trained on top of a frozen text encoder, making it widely applicable to other text-conditioned models.
- The experiments demonstrate that Fair Diffusion reduces language biases and improves generation of more diverse people while maintaining the semantics outlined in the input prompt.
- Ablation studies are provided to highlight the significance of both loss terms in the training objective.

### Weaknesses
 - In Table 1, the delta in improvement of Fair Mapping over the baselines is relatively small for race. It is difficult to understand how much a 0.01 improvement actually looks like in terms of qualitative performance.
- The authors mention that the value of the loss weight hyperparameter can affect the visual quality. Including image quality metrics like FID would be helpful to quantify how much degradation is introduced because of the debiasing network.
- Some details that are necessary for clarity and context in the main paper have been moved to the appendix. For example, Human-CLIP is a newly introduced metric but the details are not discussed at all in the main paper. Additionally, no context for the human preference evaluations is provided (e.g., at the minimum, clarify whether higher or lower is better in Table 4).
- It is unclear why no evaluations are provided in the second row of Table 2 (L_{fair} only).

### Questions
- How is the mapping network initialized? In row 3 of Table 2, it is unclear why L_{text} alone would lead to more "fair" results since it is just trying to minimize the projected embedding to the original. Shouldn't the performance be the same as row 1 if the loss is optimized?
- Have the authors experimented with just optimizing d(v, v_j) rather than (d(v, v_j) - \bar{d(v, -)}) in Equation 2?
- For clarity, is there a separate Fair Mapping module for each occupation and emotion, or is there one shared across all?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces the concept of "Fair Mapping" to mitigate bias in text-to-image diffusion models. It addresses the issue of language-induced biases in these models, particularly when generating images based on human-related descriptions. To achieve this goal, in addition to maintain text consistency, the authors also introduce the fairness penalty to encourage unbiased output. By running a set of experiments, the authors show that their approach can significantly reduce the bias in the text embedding space, when compared with other diffusion techniques.

### Strengths
The paper introduces a novel method for integrating fairness into conventional diffusion models, offering a valuable means to mitigate language bias in various contexts. The writing in the paper is clear, accompanied by numerous helpful illustrations, making it an enjoyable read.

### Weaknesses
One weakness of the paper is that it doesn't clearly elucidate the significance of its results. For instance, it would be beneficial to provide a more in-depth explanation of why we should be concerned with the specific concept of fairness addressed in this paper and to outline potential practical applications of the findings. Moreover, in comparison to other works on fair data generation, it would be helpful to highlight the primary advancements made in this paper and explain their significance. Although I acknowledge that this paper primarily focuses on methodology, I believe that readers would greatly benefit from a clearer understanding of the motivation behind the research and its possible real-world applications. I should note that I am not an expert in this research area, so I may not fully grasp the significance of this work. It's possible that the contributions are evident to experts in this field, but making them more explicit would enhance the paper's accessibility.

### Questions
For the abstract and introduction, it would be helpful to provide more motivations and maybe mention the paper's possible applications. 

The related work seems a bit unclear to me. I am not familiar with this literature but I feel more detail is needed, especially about previous works on fair data, to understand the contributions of this paper.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper aims to address the demographic bias in existing text-to-image diffusion models. The paper proposes Fair Mapping, a lightweight module that transforms the input prompts to achieve fair image generation. The training process only involves an additional linear mapping network that projects the language embedding into an unbiased space for generation. The method leads to fairer and more diverse generated images.

### Strengths
* This work performs investigations on the bias of text-guided diffusion models and concludes that the main bias related to the generation comes from the language embeddings. This observation can potentially inspire future research in evaluating and relieving biases in text-to-image generation.
* This work proposes a lightweight mapping network that turns the input embeddings that may be biased into unbiased embeddings for generation. This module is simple and easy to understand, yet effective according to the qualitative and quantitative evaluation results.
* This work also proposes a fairness evaluation metric for text-guided human-related image generation, which allows comparing the bias reduction across different de-biasing methods. This could also be useful for future research.

### Weaknesses
 * This work assumes that the bias can be corrected with an appropriate text embedding, which in turn assumes that the diffusion model is able to generate the specified human characteristics with diverse demographic properties. However, it is possible that the bias in the association is so strong (due to insufficient or biased training data) that the model could not generate the correct image, despite being asked for a specific property. For example, if there are no female plumbers in the training set, the model may not be able to generate the specified image even if "female plumbers" are explicitly asked for in the prompt. Since the method only trains a linear projection head, it is unlikely to be able to generate unbiased images. This is a fundamental limitation, as the method's effectiveness is capped by the generative capacity of the underlying diffusion model, which may not be able to represent certain underrepresented demographics or combinations of attributes.
* The method relies on a set of predefined sensitive keywords to enable transformation. However, it is hard to make this set of keywords exhaustive, and since this is a matching-based method, the checks may be skipped if some typos are introduced. This reliance on exact keyword matching makes the system brittle and susceptible to circumvention. Furthermore, the method does not address the issue of implicit biases that may be present in the text prompts, which are not captured by the predefined keywords. For example, a prompt might not explicitly mention a sensitive attribute but still evoke a biased image due to the model's learned associations.
* The fair mapping method proposed by the work may lead to loss of details in the prompt, when compared with its baselines, as shown in Sec 4.4 that some facial expressions are not generated according to the text prompts. This indicates a trade-off between fairness and fidelity, where the debiasing process may inadvertently remove or alter important semantic information in the prompt, leading to a less accurate representation of the user's intent. This is a critical issue, as it suggests that the method may not be suitable for applications where precise control over image generation is required.

### Questions
The authors are encouraged to respond and address the weaknesses above.
* If the model itself cannot generate some image characteristics due to insufficient training examples (e.g.,"female plumbers" despite already clearly specified in the text), is the method still applicable?
* How is the set of keywords for activating the linear mapping model defined?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

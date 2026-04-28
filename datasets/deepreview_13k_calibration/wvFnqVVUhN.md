# Failures to Find Transferable Image Jailbreaks Between Vision-Language Models

- Decision: Accept
- Avg Score: 6.25
- Scores: 8, 6, 3, 8

## Abstract
The integration of new modalities into frontier AI systems offers exciting capabilities, but also increases the possibility such systems can be adversarially manipulated in undesirable ways. In this work, we focus on a popular class of vision-language models (VLMs) that generates text outputs conditioned on visual and textual inputs. We conducted a large-scale empirical study to assess the transferability of gradient-based universal image "jailbreaks" using a diverse set of over 40 open-parameter VLMs, including 18 new VLMs that we publicly release.
Overall, we find that transferable gradient-based image jailbreaks are extremely difficult to obtain. When an image jailbreak is optimized against a single VLM or against an ensemble of VLMs, the jailbreak  successfully jailbreaks the attacked VLM(s), but exhibits little-to-no transfer to any other VLMs; transfer is not affected by whether the attacked and target VLMs possess matching vision backbones or language models, whether the language model underwent instruction-following and/or safety-alignment training, or other factors.
Only two settings display partially successful transfer: between identically-pretrained and identically-initialized VLMs with slightly different VLM training data, and between different training checkpoints of a single VLM. Leveraging these results, we then demonstrate that transfer can be significantly improved against a specific target VLM by attacking larger ensembles of ``highly-similar" VLMs. These results stand in stark contrast to existing evidence of universal and transferable text jailbreaks against language models and transferable adversarial attacks against image classifiers, suggesting that VLMs may be more robust to standard gradient-based transfer attacks.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper investigates the transferability of gradient-based image jailbreaks across various vision large language models (VLLMs). Through comprehensive empirical analysis involving 40 diverse VLM architectures, the study aims to understand if adversarial images that prompt harmful responses in one or several models simultaneously can induce similar outputs in others. The adversarial images, jointly optimized on several VLLMs over a set of harmful requests and responses, should show some transferability following existing  work. However, this paper shows that even under some ideal setting, transfer of the adversarial images  is quite difficult.

### Strengths
1. The studied problem is of central interest to the community and the results are count-intuitive and interesting. 

2. The paper conducts extensive experiments and considers several many reasonable settings, making the conclusion convincing.

3. The paper is well-written and easy to follow. It clearly states its conclusions without making overblown claims.

### Weaknesses
1. The main conclusion of this paper is that image jailbreaks do not successfully transfer between VLMs. It is unclear whether this issue arises from limited transferability or from the content itself being harmful (thus triggering the safety alignment mechanisms of VLLMs). I would be interested in seeing the transfer results for non-harmful content. For example, VLLMs consistently generating the same text, regardless of the input text.

2. Missing discussion of overfitting. Regarding the ASR on the optimized dataset as the train metric and the transfer ASR as the test metric, finding a transferable image jailbreak is basically a generalization problem.
 For the text-only LLM attack, the optimization space is $V^N$ where $N$ is the length of the adversarial string and $V$ is the vocabulary size. Typically $N=20, V\in[32000, 160000]$, making $\sim10^{100}$ possibilities. For VLLM attack, the space is much large: $255^{HW}$ where $HW$ is the resolution of the input image, making $\sim10^{1000000}$ possibilities..  The likelihood of overfitting increases exponentially for the problem studied in this paper. One evidence is that the timescale to jailbreak does not change pretty much in different settings since   the optimization difficulties are the same for different settings. It is possible that 8 ensemble models are enough for text-only transfer but way far from enough for image transfer.  

(This is not a weakness, but rather some suggestions that may enhance the paper.) The generalization gap can be more effectively measured using probably approximately correct (PAC) learning theories. Existing research on transfer attacks for image classifiers and image MLLMs, some of which has already been cited, also demonstrates that strategies to reduce overfitting can improve transferability.

### Questions
1. Since the input texts in the dataset don’t refer to any images (only some harmful requests), will the attention mechanism simply ignore the input image and reduce transferability?

2. Does the order of the image and text input matter the transferability? GCG inserts the adversarial suffix after the original prompt, but some of the VLLMs listed in the paper insert the image before the text prompt.

3. Will the optimized jailbreak images follow some similar pattens?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper mainly investigates the transferability issue of image adversarial attacks among Visual Language Models (VLMs). The research findings show that the image adversarial attacks optimized for single or multiple VLMs are generally difficult to transfer to other VLMs that have not been attacked. Only when the attacking model is highly similar to the target model can partial successful transfer be observed.

This paper proposes a method to optimize image adversarial attacks by attacking a collection of multiple VLMs that are highly similar to the target VLM. The experimental results demonstrate that this method can significantly improve the success rate of attacks on the target VLM, making it close to complete success.

### Strengths
1. This paper conducts a large-scale empirical study on more than 40 different types of VLMs, including different vision backbones, language models, VLM training data, and optimization strategies, systematically investigating the transferability issue of image adversarial attacks. This investigative study provides materials for subsequent research work.
2. The research results show that it is generally difficult for general-purpose image adversarial attacks to transfer between VLMs. Only when the attacking model is highly similar to the target model can partial successful transfer be observed. This is a key observation results in research communities.
3. To improve transferability, this paper proposes a method to optimize image adversarial attacks by attacking a collection of multiple VLMs that are highly similar to the target VLM. The experimental results show that this method can significantly improve the success rate of attacks on the target VLM.

### Weaknesses
1. The definition of the "highly similar" VLM is not clear. Although the author briefly described what a highly similar VLM is in the paper, it doesn't necessarily mean that the models are highly similar. There are a lot of research works that are related to evaluate the similarity of NN, as [1-5] shown. Also some of them study the similarity of NN via the loss landscapes, which is similar to some in this paper.
I suggest that the author refer to these works to investigate the actual similarity of the models. And further explain the capabilities of transfer attacks in combination with quantitative analysis. 
Thus, my major concerns can be detailed as follows: 1) Provide a quantitative measure of similarity between VLMs, perhaps using techniques from the papers in [1-5]. 2) Analyze how this quantitative similarity measure correlates with the success of transfer attacks. 3) Does the current research contribute to the analysis of the similarity of VLMs?

2. According to Figure 9, it seems that only one photo was used when initializing with natural images. This may lead to biases in the test results. Although the author also conducted some experiments on initializing with random noise, it is also very necessary to carry out evaluations with more initializations using natural images. 
So, please conduct more experiments with multiple diverse natural image initializations. Analyze whether the choice of natural image initialization affects the transferability of attacks. If there are differences based on initialization, discuss the implications for real-world attacks.

### Questions
Please refer to the weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper analyses the transferability between VLM jailbreaks. In particular, previous work has demonstrated that image-level jailbreaks do not transfer between different VLMs. The paper analyses this finding on a suite of 49 prismatic and various other VLMS. Overall, they find that image-level jailbreaks do mostly not transfer between different VLMs and transfer is only possible if the models are very similar to each other (jailbreak created on an ensemble of very similar VLMs to the target model with the same architecture and training data).

### Strengths
- The paper's topic is relevant, as transferable attacks would enable black-box attacks on VLMs and make it easy to target many such models. Additionally, if obfuscation of model weights is a way to safe against image-level jailbreaks, this could make open-source models less safe than close-weights models.
- The main message of the paper—that VLM image jailbreaks do not transfer well—is clearly conveyed, and the empirical evidence suggests this isn’t simply due to a lack of effort. This finding also seems to be validated by earlier results from Bailey et al. (2023), Qi et al. (2024a), and Chen et al. (2024b).
- I appreciate the structure of the paper, especially the breakdown of transferability across different granularities. It effectively demonstrates that there is some transfer between very similar models but that this drops off surprisingly quickly as models become less similar (e.g., in training data, training scheme, or architecture). This is especially surprising given how well adversarial image attacks typically transfer across different image classifiers.
- The evaluation pipeline and experimental setup appear reasonable. The choice of using prismatic VLMs also facilitates the exploration of transferability, and I appreciate the inclusion of newer VLMs like Qwen.

### Weaknesses
 - Attack Methodology: The authors rely on a single attack using 50k steps with Adam, initializing from either random noise or a single image. I think 50k steps is excessive; it might make sense to check once if an increased number of steps helps, but from Figures 4, 5, and 6, there doesn’t seem to be any justification for going beyond 5k steps (except for a few control trials to demonstrate this). This is relevant since the authors state that "Due to computational limitations, we were unable to explore more sophisticated attacks". It just seems unreasonable to explore 50k steps for every attack instead of trying out a larger variety of optimizers, step sizes, weight decays, and so on. I believe that this is essential.
- Schlarmann et al. (2023) used APGD, a well-regarded method for evaluating adversarial robustness. Unlike the attack used in this paper, APGD is usually used with an epsilon constraint. Would it be possible to try out APGD to see if these attacks transfer? I believe it would be the strong baseline. It might also be interesting to ablate the attack radius epsilon in this context. Also, this paper uses 5k steps as well so it would be a lot faster to evaluate than the author's 50k attack. 
- I  don’t mind publishing negative results, and the literature generally supports the findings here (with Niu et al. (2024) as a notable exception). However, if the paper’s main contribution is to show that transferable jailbreaks are unachievable, it needs a more robust approach than a single attack. I consider this a must-have for this paper. This also relates to the 2 previous points.
- The authors start from a single image and use this to claim that starting from a natural image is no different than starting from pure noise
First, various datasets available online could serve as initialization sources, and starting from only one image isn’t enough to claim that noise and image initialization are equivalent.

### Questions
- Are the image pixel values clipped to [0,1] during both optimization and evaluation? Additionally, does the VLM see a uint8 representation during the final evaluation, or is the optimized example used directly in floating-point precision without discretization? If so, does this impact the results?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors study the transferability of adversarial attacks between Vision Language Models (VLM). Through a comprehensive experimental work, the authors show that adversarial attacks show limited transferability between VLM(s). This is unlike transferability on image classifiers and Language Models where attacks are more likely to transfer. As a result, this work indicates that VLM(s) are more robust to adversarial attacks. It also prompts the question: are there more transferable attacks against VLM(s)?

### Strengths
- The writing and presentation are clear. 
- The experimental work is comprehensive and impressive. 
- The problem is well motivated. 
- The conclusions are interesting and quite impactful.  
- Good care was put into accurately measuring the success of the attack.

### Weaknesses
 - In the setting where attacks partially transfer if models were identically initialized (3.3), how important is the identical initialization? It is unclear from reading the paper. Would the transferability break if the models were initialized differently?  
- Can the authors provide any intuition on why they think there was no transfer to the 2 stage model in Section 3.6 even when the ensembles are scaled? 
- Can the authors clarify what they mean by a jailbreak image? Is it a randomly initialized image that is then optimized adversarially? Moreover, is it one image for all prompts? If that is the case, could the authors comment if more images could improve the success of the attack, perhaps grouped per prompt topic? Furthermore, how about optimizing attacks based on relevant images to the topic rather than images that are pure noise? I don’t think additional experiments are required here, just clarifications that could be incorporated into future work.

### Questions
Refer to the weaknesses section. Overall, the work is experimentally strong and of practical importance. Therefore, I recommend acceptance.

### Soundness
4

### Presentation
4

### Contribution
4

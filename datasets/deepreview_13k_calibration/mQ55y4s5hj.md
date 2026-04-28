# Visually Guided Decoding: Gradient-Free Hard Prompt Inversion with Language Models

- Decision: Accept
- Avg Score: 5.75
- Scores: 6, 5, 6, 6

## Abstract
Text-to-image generative models like DALL-E and Stable Diffusion have revolutionized visual content creation across various applications, including advertising, personalized media, and design prototyping. 
However, crafting effective textual prompts to guide these models remains challenging, often requiring extensive trial and error. 
Existing prompt inversion methods, such as soft and hard prompt techniques, suffer from issues like limited interpretability and incoherent prompt generation. 
To address these limitations, we introduce Visually Guided Decoding (VGD), a gradient-free approach that leverages large language models (LLMs) and CLIP-based guidance to generate coherent and semantically aligned prompts. 
VGD utilizes the robust text generation capabilities of LLMs to produce human-readable prompts while employing CLIP scores to ensure alignment with user-specified visual concepts. 
This method enhances the interpretability, generalization, and flexibility of prompt generation without the need for additional training. 
Our experiments demonstrate that VGD outperforms existing prompt inversion techniques in generating understandable and contextually relevant prompts, facilitating more intuitive and controllable interactions with text-to-image models. 
VGD's compatibility with various LLMs, including LLama2, LLama3, and Mistral, makes it a versatile solution for enhancing image generation workflows.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
In this paper, the authors tackle the problem of hard prompt inversion for text-to-image generative models, which is to find a piece of text input to these text-to-image models that can yield images that consist of similar visual concepts in some reference images. Unlike prior methods, which generate soft tokens or completely incomprehensible prompts, the authors propose to combine the language priors in LLMs and CLIP similarity objective to generate human-readable prompts. The authors provide some qualitative and quantitative experimental evidence to demonstrate their claims on the tasks of single image prompt inversion and multi-image concept combination.

### Strengths
The authors propose a pretty creative way to conduct gradient-free text-to-image prompt inversion and incorporate language priors in the process. The qualitative results also show some obvious improvement on CLIP-I scores when used with Llava.

### Weaknesses
My main concern about this paper lies in the experiments. In general, I am not very convinced by their result that this method significantly improves upon the existing literature.
1. The authors mainly conduct qualitative comparison with PEZ and textual inversion, and not with CLIP-Interrogator, which is very misleading given that CLIP-Interrogator is the best performing baseline based on Table 1 and it can also generate prompts that have similar human interpretability in comparison to the proposed method when used with Llava or BLIP.
2. The authors mention PH2P in their literature review but did not use it as a baseline. From the PH2P paper it seems that they can also obtain similar human interpretability.
3. PEZ also has a variation that incorporates language fluency objectives (Section 5 in PEZ paper). Since this is the main contribution of this paper, the authors should consider comparing it with this variation too.
4. Authors should also consider (at least conceptually) compare with PRISM (https://arxiv.org/pdf/2403.19103), which is another prompt inversion method that uses VLM in their process and can achieve pretty good human interpretability.
5. The main contribution of this paper is to generate human readable prompts. However, the authors fail to provide a principle and quantitative way to measure this contribution. Metrics like perplexity can be easily implemented here.
6. The authors only compare performance on one text-to-image model and fail to demonstrate the generalizability of the inverted prompts on different text-to-image models.
7. The qualitative comparisons provided in this paper are very limited.
8. No limitation section or ethic statement. Given the potential malicious usage of this method (e.g. to generate inappropriate contents), I would encourage the authors to include these sections.

### Questions
It would be great if the authors can address the weakness mentioned above.

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
The paper presents a gradient-free method, Visually Guided Decoding, that integrates LLMs and CLIP-based guidance to generate coherent and interpretable prompts for text-to-image generation. Compared to traditional methods, VGD can create readable prompts by using LLMs and optimizing these prompts with visual cues by CLIP scores. Experiments indicate that VGD outperforms existing techniques in prompt quality and interpretability on several datasets.

### Strengths
- VGD produces coherent and human-readable prompts, facilitating user interaction and modification.
- The training-free method allows easy integration with different LLMs, enhancing adaptability.
- Demonstrates superior performance in generating contextually relevant prompts, as supported by both qualitative and quantitative results.

### Weaknesses
 - This paper does not analyze bad cases.
- The evaluation lacks depth, especially in semantic aspect evaluation. No human evaluation was conducted. Since image generation is a complex, semantically rich task, CLIPScore may not fully capture true image-prompt alignment, and its classification granularity is limited. Style transfer also requires human evaluation, but the paper only shows a few examples.
- The paper evaluates only semantics without assessing image quality. There should be a discussion on whether using LLMs to create prompts could cause prompts to deviate from the training distribution, potentially lowering image quality.

### Questions
In what scenarios might the method generate inaccurate prompts?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduce Visually Guided Decoding (VGD), a gradient method that utilizes LLMs and CLIP-based guidance to generate coherent and semantically aligned texts. The experiment demonstrate that VGD outperforms existing prompt inversion techniques.

### Strengths
1.  VGD generates fully interpretable prompts that enhance generalizability across tasks.

2. VGD is a gradient-free method which is more flexible

### Weaknesses
1. When apply to more complex open-source models with multiple text encoders like SDXL and SD3, as mentioned  in L220-222, the performance of the method would decline. What's more, when facing non-CLIP based models that utilize T5 as text encoders, the methods is quite limited.

2.The current experimental analysis also appears insufficient.  While the method in the paper shows superior performance compare to previous method, it also should include the experiments about the time and cost for more comprehensive comparison.

### Questions
1. When using different model architecture like SDXL and SD3 for image generation, how to deal with the problem mentioned in L220-222.

2. I would appreciate if you could conduct more experimental analysis about comparison between VGD and previous methods.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper introduces Visually Guided Decoding (VGD), a gradient-free approach that leverages large language models (LLMs) and CLIP based guidance to generate coherent and semantically aligned prompts. VGD further uses LLMs to produce human-readable prompts while employing CLIP scores to ensure alignment with user-specified visual concepts. Experiments demonstrate that VGD outperforms existing prompt inversion techniques in generating understandable and contextually relevant prompts.

### Strengths
- Nice written paper
- The proposed approach is gradient-free which can save time.
- Results in Fig 7 are good.

### Weaknesses
 - Comparisons are missing with existing relevant methods which improve T2I generation by refining prompts such as [1] and [2].
- The score in Table are not consistent as LLaVA 1.5 + CLIP Interrogator is outperforming baseline in many cases.
- CLIP can overly large similarity scores as is proved by many existing works. To get a sense of fine-grained similarity, other metrics should be tried.
- Authors have shown that when different CLIP model is used, the approximation no longer holds. This is obvious because Diffusion model uses CLIP-ViT-B/16 which is aligned with Diffusion latent space, Some other CLIP model will not be in the same space and will ultimately not give good results. While this ablation is good, however, this is not novel and not necessary.
- Overall, the paper is good, however, there are some concerns regarding the quantitative evaluations, missing comparisons with other existing works etc.

### Questions
- Are baselines also evaluated across 5 runs like the proposed method?

### Soundness
2

### Presentation
3

### Contribution
2

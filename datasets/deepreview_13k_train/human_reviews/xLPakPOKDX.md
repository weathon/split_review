# Causally Motivated Diffusion Sampling Frameworks for Harnessing Contextual Bias

- Decision: Reject
- Scores: 6, 6, 3, 5

## Abstract
Diffusion models have shown remarkable performance in text-guided image generation when trained on large-scale datasets, usually collected from the Internet. These large-scale datasets have contextual biases (e.g., co-occurrence of objects) which will naturally cascade into the diffusion model. For example, given a text prompt of ``a photo of the living room'', diffusion models frequently generate a couch, a rug, and a lamp together while rarely generating objects that do not commonly occur in a living room. Intuitively, contextual bias can be helpful because it naturally draws the scene even without detailed information (i.e., visual autofill). On the other hand, contextual bias can limit the diversity of generated images (e.g., diverse object combinations) to focus on common image compositions. To have the best of both worlds, we argue that contextual bias needs to be strengthened or weakened depending on the situation. Previous causally-motivated studies have tried to deal with such issues by analyzing confounders (i.e., contextual bias) and augmenting training data or designing their models to directly learn the interventional distribution. However, due to the large-scale nature of these models, obtaining and analyzing the data or training the huge model from scratch is beyond reach in practice. To tackle this problem, we propose two novel frameworks for strengthening or weakening the contextual bias of pretrained diffusion models without training any parameters or accessing training data. Briefly, we first propose causal graphs to explicitly model contextual bias in the generation process. We then sample the hidden confounder due to contextual bias by sampling from a chain of pretrained large-scale models. Finally, we use samples from the confounder to strengthen or weaken the contextual bias based on methods from causal inference. Experiment results show that our proposed methods are effective in generating more realistic and diverse images than the regular sampling method.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces a causally motivated approach to enhance image diversity and fidelity in large-scale diffusion models by addressing contextual bias, without the need for retraining or extensive data access. The proposed methods involve causality-inspired techniques to modulate the influence of contextual information during the diffusion process, thus balancing realistic image generation with diverse outputs. Through experiments on datasets like Visual Genome and COCO, the approach demonstrates significant improvements in metrics such as FID and LPIPS compared to standard diffusion models. This work contributes a novel framework for controlled image synthesis, enabling broader applicability of diffusion models in creative and diverse image generation tasks.

### Strengths
1. The paper introduces a novel, causally motivated approach to address contextual bias in diffusion models, which effectively enhances image diversity and fidelity without requiring retraining or extensive data.

2. The proposed methods are validated on multiple large-scale datasets, such as Visual Genome and COCO, demonstrating consistent performance improvements in key metrics like FID and LPIPS.

3. The framework is adaptable and efficiently addresses contextual bias within the diffusion process, broadening the application scope of diffusion models for diverse and controlled image generation.

### Weaknesses
1. There is a lack of robustness when the sampled confounder $𝐶′$ is semantically distant from the prompt $𝑌$, leading to generated images that may ignore the confounder altogether​. Besides, the framework’s dependence on predefined confounders may limit its flexibility when generating images outside of commonly biased contexts, reducing adaptability in less standardized environments. Specifically, if $C'$ represents 'a snowy mountain' and $Y$ is 'a beach', the model might generate just a beach, ignoring the confounder, or produce a nonsensical image. The reliance on a precomputed $p(C')$ also means the model cannot easily adapt to novel or rare contextual relationships not present in the training data, limiting its generalization capability.
2. The approach depends on complex causal graphs and sampling chains, which may lead to higher computational demands and slower generation times, limiting its scalability​. The interventional sampling method, involving multiple steps to sample $c'$ and then generate $X$, introduces significant overhead compared to standard diffusion models. This complexity is further compounded by the need to compute or precompute $p(C')$, which itself can be computationally intensive, especially for large datasets. The increased computational cost could make the method less practical for real-time applications or large-scale image generation tasks.
3. Some generated images may exhibit unnatural object combinations, particularly when weakening contextual bias, which might detract from the realism of the results​. For instance, attempting to remove the bias of 'a cat sitting on a mat' might result in a cat floating in the air or placed in an entirely inappropriate context, thus reducing the overall quality and realism of the generated image. This issue arises because the model, in its attempt to reduce contextual bias, may generate images that are not physically plausible or semantically coherent.
4. While the framework introduces techniques to adjust contextual bias, it does not provide a quantitative evaluation of how well these adjustments meet specific user-defined objectives or bias levels. There is no clear mechanism for a user to specify the degree to which they want to reduce or alter the contextual bias, and the evaluation metrics do not directly measure the effectiveness of these adjustments in meeting user intentions. This lack of control and quantitative evaluation makes it difficult to use the method for specific bias-related tasks.

### Questions
see weaknesses

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
4

### Summary
The authors propose two causally-motivated sampling frameworks for Latent Diffusion Models, which either increase or decrease their contextual biases. 

1. CB+ increases the bias by using an LLM to describe confounders (objects) in a scene, and conditioning LDM sampling on these confounders
2. CB- decreases the bias by "retrieving" confounders, marginalized over the distribution of unconditionally generated images. This attempts to retrieve confounders (objects) which are not explicitly co-occuring with the original scene, thereby increasing scene diversity.

The authors present results on Visual Genome and use COCO to sample confounders.

### Strengths
1. This is a relevant and important problem for the community, and I found it well motivated. I appreciate the nuance in stating contextual bias is “not inherently bad” (L57-58) and providing two frameworks to tweak the bias in both directions
2. There are many experiments examining specific aspects of the framework, e.g. its impact on realism and diversity of generated images (Tab.1, 4), adherence to the original prompt (Tab 3), qualitative results (Fig 5), and its complementary nature with other frameworks (Fig 6)
3. The CB- framework is a very interesting contribution - if one is able to learn a "good" confounder distribution, it may help adding more diverse contextual biases to generative models

### Weaknesses
1. Writing flow needs improvement. I found myself having to skip ahead to find where things were introduced or explained in the writing, and in some areas I was left with no clear answer (see below)
2.	What LDM is used for experiments (Fig 2, 4-6) ? Visually, it appears to be something similar to older versions of Stable Diffusion (e.g. 1.4, 2.1) From *L509*, it doesn’t seem to be SDXL throughout. This is very unclear and greatly detracts from being able to contextualize the results (some details in Weakness 3). Please explicitly add these details for all experiments.
3.	It appears that CB+ is replacing the contextual bias of the LDM with the contextual bias of the LLM (Gemini), and CB- is doing the same with a VLM (LlaVa). Assuming that the LDM is a slightly weaker model (see Weakness 2) detracts slightly from the FID comparisons Tab.1 – Gemini and LlaVA have: 1. much higher capacity (# params) 2. Much larger pretrain datasets than older Stable Diffusions, and thus their contextual biases may be of much higher quality. This makes it harder to make a fairer comparison. If all these results are with SDXL, a much stronger LDM, this is less of a concern (but this is unclear and should be specified)  
4.	How the retrieved confounder $c’$ is used practically in CB+ and CB- is very unclear (I understand the math from Eq. 3 and Eq. 7). Are you adding the nouns from $c’$ directly to the prompt $y$ to generate a new image $x$? From *L387*, it sounds like you do not do this. My understanding of CB- (mostly from *L386-395*) is that you generate 10K images from COCO test+val captions and extract a set of nouns from all these images. You then randomly add these nouns to the prompt *y* (since you are not conditioning *y | c’*). In my opinion, this is the primary weakness of this work. Please provide a step-by-step description of how $c'$ is incorporated in the image generation process in practice for both CB+ and CB-.
5. The captions of figures need to be more self-contained. It is quite hard to understand them without referring back and forth from the text.

### Questions
1. I have a simpler baseline to suggest instead of the multi-step sampling chain in Eq. 6: use a VLM on the original $(x, y)$ as: "*given this image, describe a list of common nouns that do not occur in this scene, but could be reasonably expected to co-occur and increase the diversity*" – this will give you $c’$. You can also check for errors by asking the VLM to extract nouns from the scene (which you already do, *L270*) and the CB- technique (*L237-241*) and removing them if they are extracted from the above prompt. It is unclear to me if the sampling chain would outperform this baseline, especially because while marginalizing over truly unconditional samples as in Eq 6 *will* increase scene diversity, but can give you objects that are very out of place (e.g. Fig 4, a tree in a bedroom, motorcycles in a kitchen, etc.) This is merely an alternate suggestion, but I would like to hear the authors' thoughts about why this may or may not work compared to CB-.
2. I am a little confused by Eq 6. The starting point is marginalizing the likelihood of prompt $y$ given image $x’$ over all unconditionally generated images $x’$, which you do with a VLM. To compute this, you need to marginalize over *all* possible unconditionally generated images, which is intractable. A reasonable empirical approximation is to get a large collection of (hopefully diverse) unconditional images and marginalize over them, which is what I believe you are doing? **(a)** How many images $x’$ do you marginalize over? Is it $10000$ as you write in Fig. 1 and is this from COCO test+val (*L387*)? Please provide these details explicitly in Sec 3.3 **(b)** Are these diverse enough to get the non-co-occurring conditionings you need to reduce contextual bias? I suggest a small comment or discussion towards this question.
3. I would like more information on using CB+ and CB- with other conditionings (*L472-L483*), as I find this quite interesting and practically relevant for the community – a more explicit description of how alternate conditionings (e.g. ControlNet content or DEADiff style) can be used complementary to CB+ and CB- would be helpful

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper addresses the issue of contextual bias in image generation within the framework of causal inference. By leveraging this formulation, the authors propose two methods to either strengthen or weaken the influence of contextual biases during the image generation process. These methods rely on utilizing LLMs or VLMs to modify text prompts. The authors suggest that these adjustments will lead to more diverse and realistic generated results.

### Strengths
This paper provides an interesting formulation for the problem of contextual bias in image generations in the context of causal inference. This provides a novel perspective for thinking about how contextual bias influences generated images.

### Weaknesses
1.	While this paper formulates the problem of contextual biases in image generation using causal graphs and confounders, this formulation is overcomplicated and unnecessary for addressing the problem at hand. Although the theoretical framing is interesting, the proposed method largely boils down to a refined form of prompt engineering.
2.	The major concern for this paper is the novelty of the proposed method. Retrieving co-occurring objects using LLMs and identifying objects appearing in images using VLMs is trivial and has been commonly practiced in the task of text-to-image generation. The integration of LLMs and VLMs for prompt engineering is widely known and not innovative.
3.	Dealing with contextual biases in image generation is not a particularly challenging task for modern diffusion models like Stable Diffusion, DALLE, and Flux. These models are highly capable of generating diverse and complex images based on input prompts. They can easily generate unconventional combinations like “astronaut riding a horse on Mars” with prompt engineering along, without the need for special techniques to bypass contextual biases.
4.	The experiment should include more challenging cases that truly require causal modeling to demonstrate the significance of the approach. Without such cases, the relevance of the method remains limited.

### Questions
Please refer to the concerns raised in the weaknesses section above.

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
4

### Summary
This paper examines the phenomenon where diffusion models tend to generate images with certain preferences due to biases inherent in the training dataset. By applying causal learning framework, the influence of confounding factors is either enhanced or mitigated, thus making the generated images lean more toward "commonsense" or "counter-commonsense" representations. Notably, the authors leverage another form of bias, that present in LLMs/VLMs, to sample and estimate the distribution of confounding factors. And my understanding is that the core of this paper is not the diffusion model itself but rather the use of LLMs and VLMs to distinguish between commonsense and counter-commonsense content.

### Strengths
This work insightfully recognizes that contextual bias is not inherently negative. Contextual bias can be a crucial component in generating natural scenes, and enhancing control over it is essential. Through causal graph modeling, combined with the robust reasoning capabilities of LLMs/VLMs, they automatically (a key point) adjust the "amount of embedded commonsense" in the generated image results without any explicit training.

The highlight of this work is its approach to embedding causal intervention mechanisms in generative models, enabling automated confounder estimation to implement do-operations. While the use of causal graphs in the CV field has been widely discussed, the authors' combination of these methods with generative modeling is novel and yields promising results.

### Weaknesses
1. Hallucination of Large Model (Especially in Vision Language Model)

The limitations section highlights the constraints of VLMs. It is important to note that VLMs often experience hallucination issues. For example, when both a horse and a donkey appear in an image, the VLM may incorrectly label both as “donkey.” This is not a “beneficial” bias (as the authors point out in the paper) but rather a “harmful” hallucination issue, leading to inaccurate probability estimation when applying the Do operator. 

Furthermore, how can we ensure that the commonsense knowledge (referred to as bias in the paper) embedded in LLMs/VLMs aligns with that in the Diffusion Model? After all, these models are trained on different datasets and strategy. If there is inconsistency in commonsense between them, then using LLMs/VLMs to estimate P(c) may not be an ideal approach.  For instance, if we aim to generate an image of a "bird," LLMs/VLMs might associate "bird" with "tree," while the Diffusion model may associate "bird" with "sky." In such cases, inconsistencies in bias arise. I believe expanding the discussion on this point could be beneficial to your work.

2.While the intervention mechanism is detailed, control over diffusion remains overly rough.

The core contribution of this paper is not in Diffusion itself but rather in using LLM/VLM combined with causal inference to extract a text segment "c" from the prompt. This prompt + "c" serves as a new conditional input for generation, with different "c" segments assigned distinct weights, ultimately leading to weighted summation on the latent space or score space. 

However, this approach relies heavily on text prompt conditioning, limiting its effectiveness in handling complex cases. For instance, even with highly detailed prompts, the SD model may occasionally ignore specified objects in the prompt [1], which constrains the capability of the proposed algorithm.  A insightful work in this area can be found in [2], which delves deeper into the mechanisms of diffusion latent space, enabling the generation of counterintuitive or "counter-commonsense" images. Moreover, for a weak diffusion model, its understanding of the prompt is quite superficial. Even if the method makes additional modifications to the prompt (such as adding many counterfactual entities), it may not accurately reflect in the generated images, as discussed in works like "Attend and Excite." This limitation is due to the model's inherent capabilities and the sampling method, and cannot be solely improved by modifying the prompt. Therefore, focusing solely on the text prompt seems too crude an approach.

[1] Chefer, Hila, et al. “Attend-and-Excite: Attention-Based Semantic Guidance for Text-to-Image Diffusion Models.” ACM Transactions on Graphics, vol. 42, no. 4, July 2023, pp. 1–10. Crossref, https://doi.org/10.1145/3592116.

[2] Um, Soobin, and Jong Chul Ye. "Don't Play Favorites: Minority Guidance for Diffusion Models." arXiv preprint arXiv:2301.12334 (2023).

### Questions
1.To estimate the distribution of confounding factors, this method requires multiple sampling rounds from LLMs and VLMs; for example, generating a single image may involve at least 10 VLM calls, which is time-consuming.  In line 282, the author mentions pre-sampling methods.  Could you clarify the time required for this preprocessing, the approximate space complexity, and provide a detailed breakdown of the steps taken to reduce computation time? This part appears somewhat unclear.

2.Would it be beneficial to include a deeper discussion on the connection between diffusion bias and LLM/VLM bias, as this is a central focus of your research? Exploring whether a gap exists, if it can be quantified, and supporting this with further literature could enhance the work.

### Soundness
3

### Presentation
2

### Contribution
2

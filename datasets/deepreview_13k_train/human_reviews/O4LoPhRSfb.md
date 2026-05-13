# Does Your Video-language Model Actually Understand the Language Input?

- Decision: Reject
- Scores: 5, 5, 5, 5, 6, 5

## Abstract
Driven by the wave of Large Language Models (LLMs), Video-Language Models (VLMs) have become a significant yet challenging technology to bridge the gap between video and text. Although previous VLM works have made significant progress, almost all of them implicitly assume that all the texts are predefined by the specific template. In real-world applications, such an assumption is impossible to satisfy, since predefining all the texts is extremely time-consuming and labor-intensive. Besides, these predefined text inputs are too strict and user-unfriendly, limiting their applications. It is observed that given a video input, texts with similar semantics lead to various performances. To this end, in this paper, we propose a novel text-augmented VLM method to improve video-text fusion by text rewriting. Specifically, we first generate various text samples from the original ones based on the pre-trained LLM to target specific text components. A multi-level contrastive learning module is designed to mine the coarse-grained language information. Moreover, we also propose an attribute-based text reasoning strategy to learn fine-grained textual semantics. Extensive experiments on many video-language tasks show that the proposed method can serve as the plug-and-play module to effectively improve the performance of state-of-the-art VLM works.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The authors assert that existing video-language models may not fully comprehend the language input, as evidenced by a significant drop in model performance when input texts are rewritten. However, their experiments suggest that this issue may be more attributable to domain-specific fine-tuning rather than a fundamental limitation of the models.

Regarding the authors' proposed solution, a more straightforward approach might involve leveraging video-based large-language models, which possess stronger domain generalization capabilities.



Overall, based on the current experiments, the paper's contribution appears to be limited to domain-specific small models. Please refer to the questions below for further suggestions.

### Strengths
- This paper has a clear motivation.
- The proposed method is significant for domain-specific models.

### Weaknesses
The observed phenomenon may be more attributable to domain-specific fine-tuning:
- The degradation is more pronounced in datasets with stronger text patterns. For instance, Charades-STA, constructed using text templates, exhibits the most significant performance degradation. This suggests that the phenomenon might stem from domain-specific patterns within the dataset, where models overfit to the specific phrasing and structure of the training text rather than learning generalizable semantic representations. The reliance on template-based text generation in datasets like Charades-STA makes the models vulnerable to even slight variations in input text.
- Models with larger pre-trained text encoders, such as BLIP-2 and InternVideo, experience less performance degradation. This indicates that larger models may have greater generalization capabilities when handling text input, likely due to their exposure to a wider range of textual variations during pre-training. This suggests that the issue is not a fundamental limitation of video-language models but rather a consequence of the training regime and model size.

According to the observation above, the authors' solution is limited to domain-specific small models
- Does this phenomenon diminish in larger models like Videochat [1] or Video-LLaVA [2]? While this is a promising and straightforward solution, it has not been considered as a baseline. The absence of a comparison with these larger models, which are known for their strong generalization capabilities, makes it difficult to assess the true contribution of the proposed method. It is crucial to determine if the proposed method offers any advantage over simply using a larger, more robust model.
- Does this phenomenon persist in zero-shot settings instead of supervised fine-tuning (SFT)? This is crucial for assessing the impact of the proposed methods. If the performance degradation is less pronounced or absent in zero-shot settings, it would further support the argument that the issue is primarily due to domain-specific fine-tuning rather than a fundamental limitation of the models themselves.

### Questions
If the phenomenon persists in large models or zero-shot settings and the authors' solution remains effective, I will consider raising my score.

### Soundness
2

### Presentation
4

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper focuses on the settings that, current LLMs rely on predefined text templates. The authors propose a new text-augmented VLLM method that uses text rewriting to improve video-text fusion. The method has three main parts:

* Text sample generation with pre-trained LLMs
* Multi-level contrastive learning for coarse-grained language processing
* Attribute-based text reasoning for fine-grained semantic understanding

The proposed approach can be actively integrated with existing VLLMs as a plug-and-play module, and experimental results demonstrate improved performance across multiple vision-and-language tasks.

### Strengths
* The authors carefully design a LLM-based text augumentation methods for video-language tasks. The language alignment following the augumentation is convicing.
* The authors conduct intensive experiments with many VLLMs across various benchamarks to prove the effectiveness of the method.

### Weaknesses
 * The storyline and frame of work seems somehow not that well-aligned. The authors poses the paper as "Does Your Video-language Model Actually Understand the Language Input?", but the analysis and findings don't fully address this core question, like in what aspects, the current VLM fails to understand the language inputs, and how the proposed method specifically addresses these understanding gaps. Some claims also need further justification, such as "predefined text inputs are too strict and user-unfriendly". For example, in video captioning tasks, I don't think there are some predefined template things, the labeler usually write natural captions just following some guidelines.

* Mostly, the paper compare the different components they proposed in their own methods. But there are lots of previous non-LLM data augmentation methods in NLP [1]. Some conventional methods, e.g., synonym/antonym replacement, back-translation, paraphrasing, may work as well. These baselines could provide valuable context for evaluating the method's effectiveness.

* The choice of benchmarks could be strengthened. For instance, in video captioning tasks, I think currently ActyNet-Caps, Charades should not be very comprehensive and convincing benchmarks. Some recent benchmark like VATEX [2] (tranditional video captioning, more longer and complex captions, multiple references for each video instead of 1) or YouCook2 [3] (dense video captioning, also with complex captions) could be better choices. There are also some recent benchmarks, specifically designed for evaluating Video-LLMs, are also missing (like Video-MME).

* This raises me another questions that I saw most of text cases in these paper are quite short, like in just a few words. I am not sure whether this method is scalable and extendable to longer and complex real-world texts. It would be better that authors give some more complex cases, and show the distribution on length of their augumented texts.

### Questions
Most of my questions and concerns are already listed in the Weakness section, here I leave some other questions:

* Some implementation details are not quite clear to me. The proposed methods can be integrated with any VLLMs, and for the main experiments, on which datasets the authors use their methods? For instance, for the ActivityNet Captions task, does the authors use the training dataset to get more augumented cases and fine-tune the open-source VLLMs? Please correct me if I misunderstood.

* The proposed methods can generate both positive and negative augumented texts for videos. It would be better to have the ablation study on the effectiveness of using negative texts, especially for tasks like captioning/generation.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper aims to close the video-text alignment gap using data augmentation techniques particularly designed for textual prompt input. 

The proposed method involves prompting LLMs to modify the anchor text to derive positive/negative text that is semantically simmilar/disimilar to the original one. The modification is done on both word-level and structure-level, and there is an attribute-level selection module deisgned to guarantees the quality of the generated textual labels. 

Given a triplet of (positive text, negative text, video embedding), the contrastive loss is calculated and minimized so that the cosine similarity between the visual and the positive/negative is maximized/minimized. In each sentence, the word with the highest constrastive loss is considered.

The authors validated the effectiveness of their augmentation technique extensively on three downstream tasks: 1) video sentence grounding, 2) video question answering, 3) video-text retrieval. The experiment results show enhanced performance on almost all tasks when paired with all relevent methods.

### Strengths
1. The paper is well-motivated. The significant issue of multi-modality misalignment between video and text has not been widely investigated.
2. The proposed method of using a contrastive loss to encourage VLM to distinguish between positively and negatively augmented textual prompts is sound and intuitive. The plug-in nature of the textual augmentation technique makes it applicable to all relevant methods in the area of VLM.
3. A significant amount of effort in this work is devoted to experiments, and the reported empirical results strongly back up the effectiveness of the method on all three tasks when paired with all VLM methods.
4. The ablation study offers a comprehensive look at the importance of each module. The analysis of the word type is quite insightful.

### Weaknesses
1. The approach lacks novelty. The idea of  1) using LLMs for data annotation and augmentation and 2) constrasting positives and negatives for representation learning has been well studied. 
2. Based on the context of video-text modality alignment, there is a need to have a discussion comparing it to the well-studied image-text setting. How is the misalignment in the image-text domain different from the video-text one? What particular considerations have been taken for it?
3. Further clarafication is needed for the methodology. Are both video encoder and textual encoder being updated? There is no gradient backpropagation indicated in Figure 2.
4. The approach to only minimize the constrastive loss on "the most discriminative word" is not properly justified. And the loss is definitely not "Weighted contrastive loss" as indicated in equation (4).
5. The ablation study on hyperparameters is missing.

### Questions
Please refer to the weaknesses above.

### Soundness
3

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
5

### Summary
This paper proposes a text-augmented Video-Language Model (VLM) method to improve video-text fusion. The key idea is to generate diverse sentences from the original ones using a pre-trained LLM, and then apply a multi-level contrastive learning module to mine both coarse-grained and fine-grained textual semantics. This approach is shown to effectively improve the performance of state-of-the-art VLM models on various video-language tasks.

### Strengths
1. The proposed method is intuitive.
2. The paper is easy to follow.
3. The current empirical results look strong.

### Weaknesses
1. The current review of existing work on video-language model is severely incomplete, which makes the motivation that "video language models don't understand language input" actually invalid. There are many existing methods [a,b,c,d,e] relying on text-based representation for video input and they have already shown great effectiveness in video language modeling, with strong pretrained LLM as the initialization. It is important for the current work to comprehensively review the progress in the community and position more clearly.

2. It is also important to compare with at least some of the existing methods. Currently the authors adopts a rather implicit approach of doing text augmentation. However, the existing methods [a,b,c,d,e] directly take text representation as input which shows great generalization and can even work in training-free setting [b,d,e].

3. Empirically, the motivation is not really validated in the current empirical results. It is not clear whether the proposed method improves the performance because it is more invariant to the text prompts or actually because the video information is better utilized through the decomposition to attributes. It is important to show more analysis on why the proposed method works.
- Check the dynamics of the model during training time in terms of the performance on training data and evaluation data.
- Check the cross-data evaluation performance.

### Questions
Please check weakness for details.

### Soundness
1

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
Vision-language models typically depend on massive datasets of image/video-text pairs. However, these text descriptions are often noisy and abbreviated, limiting the model’s performance. This work addresses these challenges by enhancing the text encoder's ability to produce consistent representations for semantically similar texts in real-world multi-modal datasets. Additionally, they integrate generated samples as supplementary data alongside the original training samples, utilizing a novel weighted contrastive loss to optimize their impact and ensure a balanced contribution to training.

### Strengths
1. This work conducts extensive experiments on popular architectures, including All-In-One and Just Ask, demonstrating substantial performance improvements.

2. Enhancing text diversity and knowledge is a valuable approach that has been partially overlooked in previous research, yet it proves highly effective in this study.

3. Beyond word-level and sentence-level augmentations, this work also introduces structure-level augmentation to further enrich the model's understanding.

### Weaknesses
1. This method leverages multiple off-the-shelf large language models to generate refined text representations. Bring additional training cost and data scale.

2. The dataset contains noisy and incorrect annotations, which may increase challenges by potentially amplifying misalignment when relying on LLMs to hypothesize connections.

3. A similar concept is utilized in retrieval-augmented methods, which also aim to enhance data quality by incorporating diverse sources.

### Questions
1. In Table5, if the running time include time consuming over text repharase by LLM? If not, can you include the baseline running time in this table also?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 6

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper introduces a text-augmented approach to enhance Video-Language Models (VLMs), addressing the limitations of strictly predefined text inputs in real-world applications. By generating diverse text samples and employing multi-level contrastive learning, the method captures both coarse- and fine-grained semantics for improved video-text alignment. Extensive experiments demonstrate that the proposed framework acts as a plug-and-play module, enhancing the performance of state-of-the-art VLMs across various video-language tasks.

### Strengths
1. The proposed method improves VLMs by allowing flexible, user-friendly text inputs rather than rigid predefined templates, making it more practical for real-world applications.
2. The framework is designed as a plug-and-play module, enabling easy integration into existing state-of-the-art VLMs and achieving notable performance boosts across diverse video-language tasks.
3. The organization of this paper is logical.

### Weaknesses
1. The text rewriting technique emphasized in this paper is widely used in many tasks, and using LLMs to modify text as a form of data augmentation seems overly simplistic. This approach has already become common knowledge across various research fields, which may weaken the novelty and contribution of the proposed method.
2. In Figure 1, simply presenting a few negative examples to suggest that previous methods cannot leverage their weak text encoders to learn discriminative textual representations lacks persuasiveness. It would be more convincing if the authors provided statistical data, such as the relationship between text representations and model output logits, to better validate their stated motivation.
3. Regarding Q1, one of my main concerns is that the proposed method appears to be a combination of existing solutions, _i.e._, LLM-based text rewriting and contrastive learning with positive and negative samples. Could the authors further discuss the innovation of their proposed approach?
4. Other issues:

(1) Line 93, '_we generate positive samples that lie relatively far from the anchor in the embedding space..._', Given that only certain attributes of the sentences were modified, it is unclear whether they truly diverge in the embedding space. It would be helpful to provide a distribution plot based on t-SNE to visualize this.

(2) Figures deserve further refinement, _e.g._, Fig. 4 (3) contains unnecessary coordinate points.

### Questions
Please focus on Weaknesses 1 and 3, and I encourage the authors to provide further discussion and clarification on these points.

### Soundness
3

### Presentation
3

### Contribution
2

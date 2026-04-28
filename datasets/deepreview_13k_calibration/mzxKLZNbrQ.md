# Youku-mPLUG: A 10 Million Large-scale Chinese Video-Language Dataset for Pre-training and Benchmarks

- Decision: Reject
- Avg Score: 5.50
- Scores: 6, 8, 5, 3

## Abstract
To promote the development of Vision-Language Pre-training (VLP) and multimodal Large Language Model (LLM)  in the Chinese community, we firstly release the largest public Chinese high-quality video-language dataset named \datasetname, which is collected from Youku\footnote{\href{https://www.youku.com}{https://www.youku.com}}, a well-known Chinese video-sharing website, with strict criteria of safety, diversity, and quality. \datasetname contains 10 million Chinese video-text pairs filtered from 400 million raw videos across a wide range of 45 diverse categories for large-scale pre-training. In addition, to facilitate a comprehensive evaluation of video-language models, we carefully build the largest human-annotated Chinese benchmarks covering three popular video-language tasks of cross-modal retrieval, video captioning, and video category classification. \datasetname can enable researchers to conduct more in-depth multimodal research and develop better applications in the future. Furthermore, we release popular video-language pre-training models, ALPRO and mPLUG-2, and our proposed modularized decoder-only model \modelname pre-trained on \datasetname. Experiments show that models pre-trained on \datasetname gain up to 23.1\% improvement in video category classification.%significant improvement. 
~
Besides, \modelname achieves a new state-of-the-art result on these benchmarks with 80.5\% top-1 accuracy in video category classification and 68.9 CIDEr score in video captioning, respectively. Finally, we scale up \modelname based on the frozen Bloomz with only 1.7\% trainable parameters as Chinese multimodal LLM, and demonstrate impressive instruction and video understanding ability. The zero-shot instruction understanding experiment indicates that pretraining with \datasetname can enhance the ability to comprehend overall and detailed visual semantics, recognize scene text, and leverage open-domain knowledge.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes Youku-mPLUG, a high-quality video-language dataset in Chinese, along with a human-annotated benchmark comprising three downstream tasks. The experiments on downstream tasks (i.e. Video-Text Retrieval, Video Captioning, and Video Category Classification) evaluate the video language comprehension and modeling abilities of models.

### Strengths
1.	Youku-mPLUG is currently the largest Chinese video-language dataset.
2.	The exploration of different architectures (like encoder-only, encoder-decoder, decoder-only) is well done.

### Weaknesses
1.	The zero-shot experiment is too simple. The authors should evaluate on video-text retrieval task using more models and other pre-train datasets quantitatively.
2.	The results in Table 5 are not convincing enough. The authors only compare one publicly available dataset VATEX and do not show a gap with current state-of-the-art results. 
3.	Incorrect paragraph spacing in the second and third paragraphs in “2 RELATED WORD” section.

### Questions
Data augmentation will almost certainly bring performance improvements to the model. Therefore, how to prove that Youku-mPLUG is superior to other dataset like CNVid-3.5M?

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors introduce Youku-mPLUG, the largest high-quality video-language dataset in Chinese. And present a human-annotated benchmark encompassing three downstream tasks: Video-Text Retrieval, Video Captioning and Video Classification. The authors also propose modularized mPLUG-video, a decoder-only model that is pre-trained on Youku-mPLUG, which gain a state-of-the-art result on theses benchmarks.

### Strengths
- This paper is going to release a 10 million Chinese video-language pretraining dataset and provide benchmarks on different model architectures, which is in great demand by the field.
    
- This dataset seems to be of high quality (hire well-educated people to double check the data) and well-curated (filtered 10 million Chinese video-text pairs out of 400 million raw videos).
    
- Propose a modularized decoder-only mPLUG-video model and achieves state-of-the-art results on these benchmarks.

### Weaknesses
 - The experiments are not very comprehensive. The selected baseline models in different downstream tasks is limited, two were selected only.
    
- No details about the selection of the original 400 million videos are provided.

### Questions
This paper mentions that currently existing large-scale Chineses video-language datasets are not publicly accessible. This also demonstrates that not only the collection and curation of large datasets are challenging, but the release process is also difficult. Could the authors provide their plans to prove that you can genuinely release this dataset and make it easily accessible to researchers, thus making a real contribution to the research community?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper argues that the development and application of Chinese VLP and multimodal LLM are lagging behind the English counterpart, due to the lack of a large-scale Chinese video-language dataset. Thus, they propose a new dataset Youku-mPLUG, which consists of 10 million Chinese video-text pairs for pertaining, and a dataset with 0.3 million videos for downstream benchmarks, including video-text retrieval, video captioning, and video category classification. Meanwhile, they investigate popular video-language models (e.g., ALPRO, mPLUG-2), and the new proposed model mPLUG-video. The model mPLUG-video consists of a trainable video encoder, a visual abstractor module, and a frozen pre-trained LLM decoder. Experiments show that models pre-trained on Youku-mPLUG gain on multiple tasks. Furthermore, by building on top of Bloomz, mPLUG-video can achieve impressive zero-shot performance with very few trainable parameter.

### Strengths
+ This paper proposes a large-scale dataset with 10 million Chinese video-text pairs for pertaining, and a dataset with 0.3 million videos for downstream benchmarks. Several off-the-shelf techniques have been used to ensure the high-quality of training videos.

### Weaknesses
 + The novelty of the new model mPLUG-video is limited. The proposed three modules, and partially efficient tuning are all well studied techniques in this area.

+ The improvements brought by the proposed mPLUG-video are limited.

+ One of the key contributions in this paper is the proposed new dataset. It would be better to demonstrate the high quality of the newly collected data. Based on the example shown in Figure 9, the text annotations look very noisy.

### Questions
In the first paragraph of the introduction section, the authors argue that existing methods of translating English to Chinese suffer intrinsic linguistic and cultural gaps. Could you give more explicit examples to show the harmfulness of these methods?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
- The paper introduces Youku-mPLUG, the largest public Chinese video-language dataset and benchmarks, collected from Youku, a Chinese video-sharing website, with strict criteria of safety, diversity, and quality.
- The paper also proposes mPLUG-video, a decoder-only video-language model that leverages a frozen large language model and a visual abstractor module to reduce the computation burden and improve the performance.
- The paper evaluates mPLUG-video and other models on three downstream tasks: video category classification, video captioning, and video-text retrieval. The results show that mPLUG-video achieves good results in video category classification and video captioning, and demonstrates impressive zero-shot video instruction understanding ability.

### Strengths
- The paper introduces a novel and large-scale Chinese video-language dataset and benchmarks, which can facilitate the research and development of video-language models for the Chinese language and culture. The paper also proposes a decoder-only model that leverages a frozen large language model and a visual abstractor module, which is a creative combination of existing ideas that reduces the computation burden and improves the performance.
- The paper is well-written and organized, with clear figures and tables. The paper provides details and analysis on the proposed method and dataset. 
- The paper explains the problem statement, the motivation, the challenges, and the gap in the existing literature clearly in the abstract and introduction. The paper also describes the dataset collection, annotation, and preprocessing process, and provides some statistics and examples of the data. The paper also explains the model architecture, training, and fine-tuning process, and provides some examples.
- The paper makes a significant contribution to the field of video-language modeling, especially for the Chinese language and culture. The paper presents a large-scale and diverse dataset that can enable various downstream tasks, such as video category classification, video captioning, video-text retrieval, and video instruction understanding. The paper also presents a state-of-the-art model that can achieve impressive results on these tasks.

### Weaknesses
 - After downloading the dataset, it was found that there were many duplicate clips from the same source and static clips. Does the situation exist where these 400 million video clips come from the same original video? If so, during the filtering process, how is the quality of the selected videos ensured given the lack of quantifiable performance measures, such as CLIP similarity?
- There is a lack of exploration into the status of text annotation in the dataset. Chinese and Latin languages such as English have significant differences in vocabulary, grammar, and sentence structure. The diversity of the text part of this dataset is not sufficiently demonstrated, and the text quality is slightly lower compared to the WebVid10M dataset. The paper should also compare the dataset with other existing video-language datasets, such as translated HowTo100M, WebVid10M or CNVid-3.5M[1], and discuss the advantages and limitations of the dataset.
- This paper only explores the zero-shot capability in instruction understanding. Why not further investigate the zero-shot performance in video classification, retrieval, and description?
- In instruction understanding, does VideoLLaMA also receive Chinese prompts? Has it been trained on Chinese instruction data? Comparing a MLLM trained on English datasets with one training in Chinese is unfair.
- During data collection, the online model achieved a performance of about 94% in video category classification. However, in Table 4, the model trained by Youku-mPLUG actually performs worse than the unfiltered online model.

### Questions
see weaknesses

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

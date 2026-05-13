# TEOChat: A Large Vision-Language Assistant for Temporal Earth Observation Data

- Decision: Accept
- Scores: 1, 5, 6, 8

## Abstract
Large vision and language assistants have enabled new capabilities for interpreting natural images. These approaches have recently been adapted to earth observation data, but they are only able to handle single image inputs, limiting their use for many real-world tasks. In this work, we develop a new vision and language assistant called \MODEL\ that can engage in conversations about temporal sequences of earth observation data. To train \MODEL, we curate an instruction-following dataset composed of many single image and temporal tasks including building change and damage assessment, semantic change detection, and temporal scene classification. We show that \MODEL\ can perform a wide variety of spatial and temporal reasoning tasks, substantially outperforming previous vision and language assistants, and even achieving comparable or better performance than specialist models trained to perform these specific tasks. Furthermore, \MODEL\ achieves impressive zero-shot performance on a change detection and change question answering dataset, outperforms GPT-4o and Gemini 1.5 Pro on multiple temporal tasks, and exhibits stronger single image capabilities than a comparable single EO image instruction-following model. We publicly release our data, models, and code: \CODE.

## Human Reviews

## Human Reviewer 1

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
The work attempts to develop the first vision-language model for temporal earth observation data (EOD). When an EOD is prompted with temporal images and NLP, the proposed model can perform tasks that need temporal reasoning,

### Strengths
This paper introduces TEOChat, which is the first unified model for temporal earth observation (EO) data
The authors create a novel EO dataset

### Weaknesses
It would be more convincing if the authors could provide more evidence on the diversity and representativeness of the dataset, as well as fine-tuning results on supervised datasets.

Why only a comparison with GeoChat is made, whereas many other similar works are available?

What is the performance for other RS captioning datasets such as UCM-CAPTIONS and SYDNEY-CAPTIONS datasets which are mentioned in RSGPT[1].

It will also be important to showcase the performance w.r.t other performance measures such as recall etc

[1] RSGPT: A Remote Sensing Vision Language Model and Benchmark

In addition, the architecture and concept are very similar to Video-ChatGPT which has never been discussed or compared. Also, there are RS-based VLM which target change detection (https://github.com/lzw-lzw/awesome-remote-sensing-vision-language-models) which will be important to compare.

### Questions
As mentioned in the weakness

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper introduces a instruction tuning dataset for temporal earth observation and a corresponding fine-tuned model trained on this data.

### Strengths
S1. Applications around geo-spatial data are important and have potential for great societal impact.

S2. Applying VLMs to video data is a timely direction.

S3. Additional evidence that state-of-the-art fine-tuning methods are broadly applicable to specific target domains.

### Weaknesses
W1. The introduction often reads as a related work section. Consider moving some of the contextualization of the field in the related work section and focus a bit more on the core story and contributions in the intro.

W2. While there is a long history of geo-spatial data in computer vision, the paper contribution does strike me a little narrow in scope. 

W3. Methodological novelty. The paper applies a fairly straightforward fine-tuning recipe. While the paper does not oversell the method, this combined with the narrow scope (W2) do make me a bit concerned.

W4. What are some broader applications of these agents? Is it possible to deploy these agents at scale to understand patterns in data that would be intractable for humans to otherwise deduce themselves?

W5. The task presented seem like important capabilities but not particularly difficult for specialized models to solve. How do baseline classifiers, referring expression, change detection, etc. algorithms perform on the tasks. What generalization capabilities can be expected in the proposed model that are not present in these baselines?

### Questions
Please address the weaknesses above.

### Soundness
3

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
4

### Summary
In this paper, the authors develop a novel vision and language assistant (TEOChat) to engage in conversations about temporal sequences of earth observation data. Their extensive experiments show that TEOChat can perform a variety of spatial and temporal reasoning tasks, achieving comparable or better performance than specialist models.

### Strengths
+ The paper develops the first vision-language model (VLM) for temporal EO data and introduces the first temporal EO dataset for multimodal instruction-tuning, expanding the application scope for VLMs.

+ The proposed method shows impressive zero-shot performance on several datasets, and outperforms foundation models (i.e., GPT-4o and Gemini-1.5 Pro) for modeling sequences of images.

### Weaknesses
 - While contributing a novel application and a new dataset is encouraging, the technical contribution of this paper is insufficient.  This  paper primarily focuses on employing Low-Rank Adaptation (LoRA) to fine-tune a LLaVA-1.5-like architecture, which allows the model to handle both temporal and Earth Observation (EO) data. This paper could benefit from a more in-depth analysis of why such a design for the framework was chosen.

-  Although the authors mention that their approach achieves impressive performance on various datasets (refer to Table 1), the analysis of these results lacks specificity. It is recommended to present relevant visualizations to demonstrate the hypothesis.

- While the study provides a valuable analysis of the proposed approach against existing benchmarks, it would be enhanced by incorporating more recent specialist methods into the comparative analysis.

- There are some typos in the paper. For example, Line 106: “To align the the EO imagery”, double “the”.

### Questions
My concerns are listed in the ''Weaknesses".

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
5

### Summary
The paper presents TEOchat, a vision-language model (VLM) explicitly designed for the temporal sequences of EO data. While existing temporal sequences models focus on natural images/videos and the EO VLMs focus mainly on single-images, TEOchat fills a gap by being the first to manage temporal EO data. Authors propose a new dataset called TEOchatlas with 554k examples of various single-image and temporal tasks instructions. TEOChat performs well in tasks such as change detection and temporal reasoning, outperforming both generalist and specialist VLMs designed for EO tasks.

### Strengths
* A VLM tailored for temporal EO data addresses an important gap in current literature. Prior VLMs could only work with either natural video/multi-images or single EO images.
* The dataset extends GeoChat datasets to the temporal domain. The temporal component of the TEOchatlas dataset is comprised of 4 datasets (fMoW, xBD, S2Looking, QFabric) that are converted to the following temporal tasks: Temporal Scene Classification, Change Detection, Spatial Change Referring Expression, Change QA, Region-based Change QA, Temporal Referring Expression and Region-based Temporal QA.
* The model is comprehensively evaluated across multiple datasets and tasks. TEOChat consistently performs well on both generalist and specialist models on tasks such as change detection, temporal scene classification, and change question answering.  Its performance on zero-shot tasks is also significant. 
* Ablations done on the type of projector initialization, its finetuning startegy, and choice of image/video encoder are comprehensive and justify the design choices.

### Weaknesses
 * Similar to video models like Video-LLaVa, the authors limit the sequences to a maximum of 8 images. For longer sequences, how this restriction can affect the model results? It is unclear how the model would perform with longer temporal contexts, especially given the potential for long-range dependencies in time-series EO data. The choice of 8 images seems somewhat arbitrary and could limit the model's applicability to datasets with longer sequences.
* TEOchat randomly sample 8 images without replacement from longer sequences, the choice of samples selected can significantly change the results. Can the authors report variance in results due to different random samplings? The impact of this random sampling on the stability and reliability of the results is not well-understood. Different random samples could lead to substantially different performance, especially if the temporal information is critical for the task.
* The statement "TEOChat also performs comparably to or outperforms a specialist model trained to perform specific tasks" seems quite a strong claim given the proposed model performs quite low in certain cases: e.g., xBD Loc. (IoU) and QFabric [2 and 5 images]. The model's performance on these specific tasks is significantly lower than specialist models, which contradicts the claim of comparable or superior performance. A more nuanced discussion of the model's strengths and weaknesses is needed.
* Table 1, I believe the GeoChat model is evaluated zero-shot given it cannot be trained with multiple images? This should be clarified clearly in Table 1 that the comparison is between a zero-shot model evaluation (not built for multiple images) and TEOchat that is specifically trained with multiple images. Similarly, as Table 2 shows, the VideoLLava is also evaluated zero-shot in Table 1, and compared with the version that is finetuned on the TEOchatlas dataset, I do not think its a fair comparison and authors should clearly mention that they are comparing zero-shot models with a supervised model. The comparison between zero-shot models and a fine-tuned model is not an apples-to-apples comparison. The performance gains may be primarily due to the fine-tuning process rather than the model architecture itself.
* Contribution 2 gives the impression that the 554k instruction set is this paper's contribution while over 55% of it is included from previous work GeoChat. It would be reasonable to clarify this and change the claim accordingly. The contribution of the dataset is overstated, given that a significant portion is derived from existing datasets. The novelty of the dataset needs to be more clearly defined.
* The model uses interleaved image identifiers among the visual tokens in the sequence input to the LLM (Figure 3). This differs from prior methods for modeling temporal sequences of natural images which commonly concatenate the tokens and leads to significant gains as per ablation study. However, it is not clear why the image identifier would help in bi-temporal datasets like xBD and S2Looking, since tagging two images should not make much of a difference. Can the authors explain this? The rationale behind using image identifiers, especially in bi-temporal datasets, is not clear. It's unclear how this approach helps the model understand temporal relationships between images.

### Questions
* A number of open VLMs now allow the processing of multiple images. Can the authors evaluate such options e.g., Qwen2VL, InternVL2 on temporal EO tasks explored in the paper?
* Some recent parallel works (e.g., CDchat https://arxiv.org/html/2409.16261v1) have also explored extending EO VLMs for change detection. Authors are encouraged to explain differences with them (although this is an Arxiv work, and comparing them is not mandatory).
* The VLM responses are textual, the metrics used for eval are accuracy, IoU and F1 measures. Its not clear how the textual outputs are parsed to obtain object coordinates, outputs classes etc. How robust is this process to avoid any errors due to incorrect parsing?
* How much the choice of low-image resolution affect the performance on localization tasks like detection when the objects are quite small. Authors use all the GeoChat data for training, including referring and grounding instructions, but do not compare single-image grounding tasks. It will be good to understand how the choice of vision encoder affects the performance on these tasks. 
* Why GPT4 and Gemini models were evaluated/compared on only two tasks? Analysis on the kind of cases where these models fail will be important.

### Soundness
3

### Presentation
3

### Contribution
3

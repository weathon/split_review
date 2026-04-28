# VIDEOPROMPTER: AN ENSEMBLE OF FOUNDATIONAL MODELS FOR ZERO-SHOT VIDEO UNDERSTANDING

- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 5, 6, 5

## Abstract
Vision-language models (VLMs) classify the query video by calculating a similarity score between the visual features and text-based class label representations. Recently, large language models (LLMs) have been used to enrich the text-based class labels %representations 
by enhancing the \emph{descriptiveness} of the class names. However, these improvements are restricted to the text-based classifier only, and the query visual features are not considered.
In this paper, we propose % Our proposed 
a framework which combines pre-trained discriminative VLMs with pre-trained generative video-to-text and text-to-text models.  We introduce two key modifications to the standard zero-shot setting. First, we propose language-guided visual feature enhancement and employ a video-to-text model to convert the query video to its descriptive form. The resulting descriptions contain vital visual cues of the query video, such as what objects are present and their spatio-temporal interactions. These descriptive cues provide additional semantic knowledge to VLMs to enhance their zero-shot performance. Second, we propose video-specific prompts to LLMs to generate more meaningful descriptions to enrich class label representations.  Specifically, we introduce prompt techniques to create a Tree Hierarchy of Categories for class names, offering a higher-level action context for additional visual cues, %and \(2)\) resolve ambiguities among fine-grained classes through a negative classifier.
We demonstrate the effectiveness of our approach in video understanding across three different zero-shot settings: 1) video action recognition, 2) video-to-text and text-to-video retrieval, and 3) time-sensitive video tasks. Consistent improvements across multiple benchmarks and with various VLMs demonstrate the effectiveness of our proposed framework. Our code will be made publicly available.
\begin{figure}[!htb]
    \makebox[\textwidth][c]{%
        \includegraphics[width=0.95\linewidth]{figures/figure_2_evolution_try9.pdf}
    }
    \caption{\textbf{(a)} The standard pre-training for zero-shot classification (e.g., CLIP 
    \citep{radford2021learning}). \textbf{(b)} Existing variants for enhancing zero-shot classification \citep{pratt2022does,menon2022visual} using GPT descriptions and attributes that improve text-based classifier features. \textbf{(c)} Our proposed framework to enhance both classifier and visual representations. It employs a video-to-text model to generate description of the query video, and these descriptive cues are combined with the visual information. A text-to-text generative model (GPT-3.5) is prompted for class attributes, descriptions, and action context to enhance the class diversity for the text-based classifier.}% Four types of prompts (attributes) are used to increase the descriptiveness of the class names.}
    \label{fig:introfig}
    \vspace{-1.5em}
\end{figure}

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a framework for zero-shot video understanding by using various foundation models including VLMs, i.e., CLIP, LLMs, i.e., GPT, and Video-to-Text model, i.e., VGPT. Experiments are conducted on three different problem settings and showing good results. Ablations are thorough and enough to justify the framework design choices. Written presentation is fair, but could be improved.

### Strengths
- The paper presents a set of experiments on various problem settings: action recognition, video-to-text and text-to-video retrieval, time-sensitive tasks and on different datasets.
- The ablations are solid and thorough.
- Experiments show strong improvement w.r.t baselines.

### Weaknesses
 - Since at least 3 foundation models have been used (CLIP, GPT, VGPT), how do we know if those models are trained with examples overlapped with the downstream datasets (e.g., HMDB-51, UCF101, SSv2, K400, MSR-VTT, Charades).

- The novelty seems moderate if not low. As the paper mentions the main contributions are 1) introducing video-to-text to enhance visual embeddings and 2) applications to videos.  

- The written presentation could be further improved:
     1) section 2.1 could be renamed to "Overview" and try to capture the big picture of the framework. The author(s) can refer back to Fig. 1 for the big picture (in the current flow of presentation, there is no big picture and it flows in with overwhelming many details and notations). Then sections 2.2 and 2.3 can be further followed up from 2.1 to provide detailed of components.
     2) table 6 is presented in page 7, yet never been referred from the text?

### Questions
- My main concerns are the leaking examples from downstream datasets to foundation models.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes to ensemble multiple large foundation models to enhance the zero-shot inference performance on video understanding tasks (namely VideoPrompter), including video action recognition, video-to-text and text-to-video retrieval, and time-sensitive (before/after) video tasks. The main architecture is based on CLIP, where classification can be performed by ranking the cosine similarity between visual and text representations, and the main idea is to enrich both the video and text embeddings. For the video part, the authors employ Video-Chat GPT (VGPT) (Maaz et al., 2023) to extract the text description of the query video and convert it into a video-to-text embedding with the text encoder in CLIP. The video-to-text embedding is then ensembled with the visual embedding encoded by the original CLIP visual encoder as the final visual embedding. For the text part, they prompt GPT-3.5 to rephrase the class names with parent context, language attributes, and language descriptions. All the descriptions are ensembled to generate the final text embedding. Experiments show that VideoPrompter can improve over plain zero-shot inference performance with CLIP and its variants.

### Strengths
1. The studied problem is interesting. Video understanding with large foundation models is of wide interest in the community.
2. The authors put together state-of-the-art large foundation models and improve the zero-shot inference performance on video understanding tasks.

### Weaknesses
1. The idea of generating more descriptions for class names and using high-level context is not new in prompting large foundation models (e.g. the prior works cited in this paper). This is model ensembling for enhancing zero-shot performance. Can the authors justify the main novelty of this paper?
2. VGPT is used to generate the text description of the query video, and which is then converted to an image-like text embedding. Why not just prompting VGPT for the downstream applications (e.g. action classification)? Comparison to this baseline is an important justification to the proposed method.
3. Several components are added to the solution, while the ablations are not sound enough. For example, how important are the three description types (parent context, language attributes, and language descriptions)?
4. The claim for the comparison to CUPL (Pratt et al., 2022) is not very clear (section 3.1.4). The authors claim that VideoPrompter only requires 3 text descriptions instead of 50 descriptions adopted in CUPL. However, VideoPrompter adopts a VGPT model while CUPL does not. Is using VGPT a better choice in terms of the cost?
5. The paper criticizes prior work that “these methods require access to the true distribution of the target task, which can be prohibitive in test-time adaptation and data-scarce environments”. However, the proposed method optimizes the selection of hyperparameters (e.g. temperature) directly on the target dataset (see Figure 3).
6. The high-level action context is restricted to a tree-type relation. However, some child classes may belong to multiple parent concepts. For example, “surfing” can belong to both “playing sports” and “water activities”.

### Questions
My questions are listed in the weakness section.

### Soundness
2 fair

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
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper introduces a novel framework for zero-shot video understanding. The proposed framework, named VideoPromoter, is built by enhancing the visual features as well as the class representations. Experimental results indicate that the proposed method could improve the zero-shot performance of various VLMs across multiple tasks.

### Strengths
1.	This paper studies an important problem of adapting pre-trained vision-language models to downstream tasks in zero-shot settings.
2.	The introduced method is lucid and holds promise for extension across a wide range of VLMs.
3.	The experimental results look good. VideoPrompter is able to increase the zero-shot performance of VLMs across multiple tasks.
4.	The paper is well-presented.

### Weaknesses
1.	The efficiency of VideoPrompter hasn't been thoroughly examined. Given that VideoPrompter appears to require generating 10 times the number of samples and the use of an additional text-to-video model, it could substantially raise the inference costs, both for evaluating existing VLMs and in practical applications. The paper does not provide a detailed analysis of the computational overhead of generating these multiple text descriptions per video, nor does it explore the trade-off between the number of generated descriptions and the resulting performance gains. This lack of analysis makes it difficult to assess the practical applicability of the proposed method, especially in resource-constrained environments.
2.	The selection of Video-ChatGPT as the video-to-text model seems arbitrary. Alternative models, such as Video-LLaMA [A], should be considered and discussed. The paper lacks a clear justification for choosing Video-ChatGPT over other available video-to-text models. A comparative analysis of different models, considering factors such as accuracy, computational cost, and suitability for the task, is needed to strengthen the paper's claims. Furthermore, the paper does not explore the potential impact of the video-to-text model's performance on the overall performance of VideoPrompter.
3.	An ablation study on the video-specific language descriptors is missing. The paper does not provide a detailed breakdown of the contribution of each component of the video-specific language descriptors (e.g., class attributes, class descriptions, action context). Understanding the individual impact of these components is crucial for optimizing the framework and gaining insights into the underlying mechanisms of the proposed method.

### Questions
See weakness.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The manuscript proposes an ensemble framework for video understanding based on pre-trained visual-language models, which involves utilizing LLM to enhance the descriptiveness of text labels and leveraging a video-to-text model to enhance video representations. The authors conducted comprehensive experiments on action recognition, video-text retrieval, and time-sensitive video tasks, demonstrating the effectiveness of the approach in zero-shot scenarios.

### Strengths
The experiments and ablation studies are conducted comprehensively, validated on different pre-existing architectures, and taken into account various types of video data.

Employing the video-to-text model (not limited to VGPT and caption models) is novel and worthy to explore in the video field. Fusing the text and video representations is depicted to be beneficial in bridging the gap between video and textual labels in the embedding space.

The manuscript provides a detailed explanation and examples of prompting the GPT to refine the simple textual label, which in turn enhances reproducibility.

### Weaknesses
In the 'video-to-text guided visual feature enhancement' (section 2.2), the adopted VGPT relies on CLIP-ViT-L and vicuna, where the computational cost of performing multiple inferences (including text embedding and filtering) far exceeds that of the basic video understanding model. This limits the practical value of the proposed approach. 

Except for CLIP, an image-language pre-trained model targeted specifically for the image field, the proposed approach shows relatively limited performance gain in other video-based models (ViFi-CLIP, AIM, ActionCLIP), considering the additional computational requirements.

The configurations of adopted pre-trained models (AIM, ActionCLIP, …) remain unclear, which datasets are these models pre-trained on (e.g. K400, K700, …)? For AIM, do the authors directly remove the classification layers?

### Questions
Are the high-level action contexts mentioned in the manuscript manually designed?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

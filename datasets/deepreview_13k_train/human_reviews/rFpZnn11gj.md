# PathGen-1.6M: 1.6 Million Pathology Image-text Pairs Generation through Multi-agent Collaboration

- Decision: Accept
- Scores: 8, 8, 8, 6

## Abstract
Vision Language Models (VLMs) like CLIP have attracted substantial attention in pathology, serving as backbones for applications such as zero-shot image classification and Whole Slide Image (WSI) analysis. Additionally, they can function as vision encoders when combined with large language models (LLMs) to support broader capabilities. Current efforts to train pathology VLMs rely on pathology image-text pairs from platforms like PubMed, YouTube, and Twitter, which provide limited, unscalable data with generally suboptimal image quality. In this work, we leverage large-scale WSI datasets like TCGA to extract numerous high-quality image patches. We then train a large multimodal model to generate captions for these images, creating PathGen-1.6M, a dataset containing 1.6 million high-quality image-caption pairs. Our approach involves multiple agent models collaborating to extract representative WSI patches, generating and refining captions to obtain high-quality image-text pairs. Extensive experiments show that integrating these generated pairs with existing datasets to train a pathology-specific CLIP model, PathGen-CLIP, significantly enhances its ability to analyze pathological images, with substantial improvements across nine pathology-related zero-shot image classification tasks and three whole-slide image tasks. Furthermore, we construct 200K instruction-tuning data based on PathGen-1.6M and integrate PathGen-CLIP with the Vicuna LLM to create more powerful multimodal models through instruction tuning.
Overall, we provide a scalable pathway for high-quality data generation in pathology, paving the way for next-generation general pathology models.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
PathGen-1.6M represents a significant advancement in pathology AI, introducing the largest high-quality pathology image-text dataset created through multi-agent collaboration. The approach leverages whole slide images from TCGA to extract representative patches and generate accurate, detailed captions, achieving 88-90% accuracy validated by pathologists. The resulting models, PathGen-CLIP and PathGen-LLaVA, demonstrate superior performance across various tasks including zero-shot classification, few-shot learning, and whole slide image analysis, outperforming existing models including GPT-4V. This work provides a scalable pathway for generating high-quality pathology data and developing more capable AI models for clinical applications.

### Strengths
- Well written introduction
- Good literature survey on LMMs and Pathology--CLIPs
- Brilliant idea on how to develop the revise LLM agent
- Representative patch selection using GPT-4 is an excellent idea
- Interesting approach to select patches through clustering but modulating the number of clusters as the square root of the size of a slide
- Strong evaluation pipeline across a range of tasks

### Weaknesses
 - It's an overkill to say that this is an agent based system. Agent based systems are autonomously operating on a set of predefined rules and behaviors, while this approach appears to be more of a sequential pipeline with different models performing specific tasks rather than truly autonomous agents interacting with each other.
- Lit survey on multi-agent architectures could be expanded
- Usage of GPT-4s internal knowledge about the morphology of an organ is a good idea but deters diversity of patches collected. Also unclear if those prompts are well represented in the CLIP training dataset. Additional details on how many prompts obtained for each WSI will help the reader. It's unclear if each patch is matched against 2 prompts (report and attribute based) or more?
- Added details on motivations for design choices such as including both prompt and image retrieval will help.
- The methods section needs more details and fleshing out the writing will help; I think this is also generally true for most of the paper
- While not the goal of the paper, it will help to include fully supervised baselines as well to educate the readers of the gap with CLIP like models
- Details on how the instruction tuning data was curated are not provided

### Questions
- How many real pathology report findings did you'll extract in section 3 and how did you verify the quality of it
- How do you evaluate the performance of the images retrieved for the prompts in section 3.1?
- How many prompts do you use for each WSI?
- How did you arrive at the design choice of using both prompt-based and clustering-based retrieval?
- Why chose a threshold of 0.88 for similarity?
- Is similarity computed globally in all the extracted patches across slides?
- Does the revision agent have a no-operation capability as well? What happens when a correct description is passed to the revision agent?
- What does first and second stage training in PathGen-CLIP mean?
- Why did you use different datasets for zero and few shot experiments? As an example, Camelyon is not included in zero-shot examples

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper proposes a new 1.6 million dataset of paired image-caption pathology data.
The authors propose a scalable way to construct the dataset using existing LMMs and refinement strategies.
They show this dataset is useful in developing a pathology specific CLIP model which performs better than existing domain specific and general purpose CLIP style models in zero-shot an few-shot problems
Finally they show that scaling dataset size and model size can lead to improvements in some tasks.

### Strengths
Originality:
The paper proposes a new way to generate quality image-caption pairs for pathology data. 
It uses existing publicly available pathology image-caption data and the ability of newer general purpose LMMs like GPT-4 to generate detailed descriptions to create an initial dataset for training a LLaVA style captioning model.
It then uses this captioning model in conjunction with a revision and summary agent to generate synthetic image-caption data.
This approach of using existing data and LMMs to build a model and refine its outputs using other agents is interesting and not explored in the context of pathology.
Given the large nature of WSI images and significant redundancy and similarity of image content, the authors propose ways to construct a dataset of diverse image patches

Evaluation:
The authors evaluate the model on various zero-shot and few-shot patch-level tasks and on WSI-level prediction tasks and compare its performance against various existing models. The results with GigaPath a vision encoder are promising and show we can use existing vision encoders and improve their language capabilities using the captioning data.
They also qualitatively evaluate a small subset of the generated captions using expert pathologists. 

Experiments:
The authors show various ablations around dataset construction which are valuable in understanding some of the limitations of using captioning models. The section scaling dataset and model size is interesting and shows some evidence around usefulness of scaling datasets and models using this approach.

All the data and models are publicly available which is great for the pathology community and this will also be the largest publicly available image caption dataset for pathology.

### Weaknesses
Clarity:
While I appreciate the authors covering a lot of ablations and experiments and describing the prompts, many of the design choices aren't clearly explained well. I've added some in the questions below.

Evaluation:
While the authors do compare with many older pathology VLM models, its unclear why they couldn't get access to the more recent CONCH which is publicly available on HuggingFace. 
For WSI tasks while its helpful they added Gigapath, they don't compare against better publicly available pathology vision encoders like 
H-Optimus.

Improvements:
Given the setup, its unclear how much of the improvements are coming from the new PathGen data and the refinement through revision agent, given they are one of the main contributions of the paper. i.e There isnt a comparison of the performance of the original PathGen-CLIP-L_init encoder with the improved PathGen-CLIP-L. Another comparison which would be useful is understanding with/out data generated using the revision agent.
It would be useful to highlight these as it helps understand how well such a setup can scale in generating synthetic data for iterative refinement. 
Quality and Scale of Initial Dataset:
Its also unclear how important the scale of the detailed caption dataset 30K used for training PathGenLlava and the quality of it. Does scaling the dataset size and having some refinement here help? Have the authors checked the quality of captions generated by GPT-4 here and can provide some insight.

### Questions
Dataset Construction:
Its unclear why and how the subset of 700K samples was choosen from existing datasets to create PathGen_init. 
For training the description agent, the authors mention using 10K initial image-caption pairs to generate 30K dataset, so are 3 captions generated per image?

Revision Agent:
What model is used for training the revision agent? Its also unclear what the inputs for revision agent are at inference? Does it take the generated caption and produce possible edits?


In figure 10, its unclear the w/ PathGen_init two stage performance doesnt vary when scale of PathGen data is varied? When scale is 0 it means all data is PathGen_init is that correct?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper introduces PathGen-1.6M, a large-scale dataset containing 1.6 million high-quality image-caption pairs extracted from Whole Slide Images (WSI).  It also developed a scalable approach for high-quality pathology image-text data generation by multiple agent models collaborating, paving the way for next-generation general pathology models.

### Strengths
1.	The paper presents PathGen-1.6M, a dataset containing 1.6 million high-quality image-caption pairs. Based on this dataset, the authors develop PathGen-CLIP, a pathology-specific CLIP model, which achieves substantial improvements across nine pathology-related zero-shot image classification tasks and three whole-slide image tasks.
2.	The authors propose a data construction pipeline that employs multiple LLM agents for description, revision, and summarization. This multi-agent collaboration approach generates more accurate image-caption pairs, validated through human evaluation.
3.	The experiments conducted in the paper are solid and well-executed.
4.	The release of the dataset, code, and model contributes significantly to the advancement of the pathology image research community.

### Weaknesses
1.	The Revise LMM appears to have limited utility, primarily providing editing capabilities such as additions, deletions, or modifications. It seems ineffective in addressing common pathological inaccuracies in the generated descriptions, such as misidentification of tissue types or overlooking subtle but critical diagnostic features. The revision process appears to focus on surface-level textual changes rather than deeper semantic corrections.
2.	Only evaluated in CLIP model. The paper lacks evaluation on other pre-trained vision-language models, which limits the generalizability of the findings. The dataset's utility for models with different architectures or training objectives remains unclear, and it is uncertain whether the observed improvements would translate to other models.

### Questions
1.	The writing of the paper requires improvement, as there are several shortcomings. For example, there is a typo in “PathGen-LLaVAdesp” in Section 4.1, and the conclusion summarizes, “we train two advanced models: PathGen-CLIP and PathGen-CLIP-L.” It appears there is an additional model, “PathGen-LLaVA,” which needs clarification.
2.	A significant concern arises regarding potential data leakage in the downstream tasks and benchmarks evaluated. To my knowledge, many tasks and benchmarks are derived from TCIA pathology data, which raises suspicions about the homogeneity of the constructed dataset.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
Built upon domain-specific WSI-Reports data from TCGA, this paper proposed the largest high-quality patch-text pairs dataset for Computational Pathology (CPath) by prompting LMM to generate text descriptions for pathology patches. To this end, a scalable data curation method is proposed by leveraging several LMM agents to describe, revise and summarize the generated descriptions.

### Strengths
1. To address data scarcity in CPath for pretraining large models, a scalable data curation method is proposed to expand the limited image-text dataset.
2. The largest patch-text pairs dataset is curated and used for pretraining to enhance the foundational power in CPath tasks.
3. The scalability to more WSI-only data is interesting, which has the potential to greatly expand the data scale for large pathology models.

### Weaknesses
1. To support the superiority of the proposed data construction method by introducing extra patch-level supervision, the performance of directly utilizing original report data along with patch images to pretrain a pathology foundation model should be presented.
2. During data construction, some representative patches were filtered out. These patches are supposed to align well with pathology reports, as they are retrieved based on the report data. To validate the extra contribution of generated patch descriptions, the proposed model should be compared with the one trained on these selected representative patches as well as its corresponding report data.
3. The model’s generalizability to out-of-domain data has not been validated. The authors tried to scale the model to non-WSI report paired data. However, these data are still from TCGA.
4. Some SOTA pathology foundation models are missing, especially in experimental comparison, such as UNI [1], CONCH[2], mSTAR[3] (which is also a CLIP-style model trained on TCGA data as well), etc.
5. Few-shot’s capability significantly relies on how well-aligned the vision and text spaces are. The proposed method is supposed to compare with VLM like CONCH, instead of vision-only GigaPath.
6. Details in EXPERT EVALUATION are missing. For example, how do authors define what correct or incorrect findings are?

Minor concerns:

- It is hard to recognize different models according to their colors. Please choose ones with higher contrast.
- The citation of GigaPath seems to be lost.

### Questions
1. In Step 5 of data construction, how do authors ensure that no essential details are lost?
2. How can be validated the effectiveness of each step in data curation? This should be discussed in the ablation study.

### Soundness
3

### Presentation
3

### Contribution
3

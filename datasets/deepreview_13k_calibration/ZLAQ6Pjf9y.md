# An X-Ray Is Worth 15 Features: Sparse Autoencoders for Interpretable Radiology Report Generation

- Decision: Reject
- Avg Score: 5.60
- Scores: 5, 5, 8, 5, 5

## Abstract
Radiological services are experiencing unprecedented demand, leading to increased interest in automating radiology report generation. Existing Vision-Language Models (VLMs) suffer from hallucinations, lack interpretability, and require expensive fine-tuning. We introduce SAE-Rad, which uses sparse autoencoders (SAEs) to decompose latent representations from a pre-trained vision transformer into human-interpretable features.
Our hybrid architecture combines state-of-the-art SAE advancements, achieving accurate latent reconstructions while maintaining sparsity.
Using an off-the-shelf language model, we distil ground-truth reports into radiological descriptions for each SAE feature, which we then compile into a full report for each image, eliminating the need for fine-tuning large models for this task. To the best of our knowledge, SAE-Rad represents the first instance of using mechanistic interpretability techniques explicitly for a downstream multi-modal reasoning task. On the MIMIC-CXR dataset, SAE-Rad achieves competitive radiology-specific metrics compared to state-of-the-art models while using significantly fewer computational resources for training. Qualitative analysis reveals that SAE-Rad learns meaningful visual concepts and generates reports aligning closely with expert interpretations. Our results suggest that SAEs can enhance multimodal reasoning in healthcare, providing a more interpretable alternative to existing VLMs.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes a novel radiology report generation framework (SAE-Rad) based on Sparse-Autoencoder (SAE). It decomposes latent image features into human-interpretable features, distils these features into radiological descriptions and compiles them into full report. The experiment results on MIMIC-CXR show the leading report generation performance and efficient training computation.

### Strengths
## Strengths
- The public dataset, codes, and implementation details are provided for reproducibility. 
- Method novelty of some improvements on gated-SAE, which achieves better sparcity and reconstruction quality. 
- Enhancing the model interpretability by SAE decomposing image latent features into radiological descriptions. 
- Comprehensive evaluation metrices and leading performance in MIMIC-CXR Chest X-ray report generation.

### Weaknesses
## Weaknesses and Questions
- The motivation of the method is still not well explained. In 4.1, the authors mention four differences between the gated SAE and SAE-Rad, but I do not find enough explanation about what is the advantage of these differences and why these differences are important for image-to-text generation. Specifically, the paper lacks a clear explanation of how the architectural changes in SAE-Rad, such as the modified loss function and gating mechanisms, directly contribute to improved performance in radiology report generation compared to standard SAEs. Furthermore, I would like to know whether the entire SAE-Rad framework enhances the general image-to-text generation tasks, or it is specifically designed for radiology report generation? If SAE-Rad is mainly designed for report generation, then the authors should also explain the specific advantages of the four differences in SAE-Rad and the sparse feature interpretability method in radiology report generation task.
- No ablation study about the improved SAE loss (Eq. 9). Since the authors make some changes in SAE loss, as described in Eq. 9 and the four differences, there should be some ablation studies showing the effectiveness of this novel SAE loss, compared with other losses used in SAE training. The paper should provide a detailed analysis of how each component of the modified loss function contributes to the overall performance, and compare it against standard SAE loss functions to justify the design choices.
- There is no discussion for the co-occurence issue in medical report generation. In medical images, multiple diseases or visual markers sometimes have high correlation and frequently shown up together in one image, so this may cause some false findings in the generated reports. Since the proposed SAE-Rad report generation model is based on image latent feature decomposition and activated feature descriptions, so it's important to understand if the feature representations of co-occurence visual markers are fully decomposed and disentangled before generating any feature interpretation descriptions from LLMs. Please provide discussions about the co-occurence issue and the potential limitations of it. The paper needs to address how the model handles the potential for spurious correlations in the latent space and how it prevents the model from generating reports that conflate co-occurring conditions.
- The number of comparison methods is not enough for a fully demonstration of the effectiveness of the proposed method. In Table 1, only CheXagent is compared in *Current study*, and MAIRA as upper bound. However, since radiology report generation using MIMIC-CXR has been widely explored in recent years, there are much more methods that could be used for comparison. I think the authors should provide more comparison results with some other recent leading methods for a stronger evaluation. The paper should include a more comprehensive comparison against a wider range of state-of-the-art methods, including both traditional and more recent deep learning approaches, to better contextualize the performance of the proposed model.
- The authors use RadFact as one of the evaluation metrics since it is robust without relying on pre-specified error types or specialized models. But in Table 1, SAE-Rad only gains 0.3 in RadFact compared to CheXagent, which is a marginal improvement, and also a large gap to the upper bound; in the same time, other clinical metrics show large increases. So how to explain this discrepancy in these metrics? Does it mean RadFact score is not sensitive enough? The paper should provide a more detailed discussion of the RadFact metric, including its limitations and potential biases, and explain why the observed improvement is marginal despite significant gains in other metrics. A sensitivity analysis of RadFact could also be beneficial.
- The proposed method is based on the sparse image features (feature directions and associated activations) extracted from SAE-Rad, but the clustering and distributions of the extracted features of all chest diseases/markers are not visualized or discussed. The sparse feature distribution in latent space is important to assess the feature clustering and latent space training, where feature directions of similar visual markers should be clustered closely while different visual markers should push apart their feature directions. I recommand the authors visualize the sparse feature representations of each diseases/markers using T-SNE demo to illustrate the sparse feature clustering. The paper should include a detailed analysis of the latent space, including visualizations of feature distributions and clustering patterns, to demonstrate the model's ability to disentangle different radiological findings.

### Questions
The proposed report generation method of the paper has some novelty in SAE and activated feature interpretability, and the result also shows leading generation performance. But some important differences of the method are not fully explained and evaluated, and some common issues in report generation such as co-occurence and latent feature clustering are not discussed, which weaken the insight of the paper. In conclusion, I think the paper is on the boarderline so I currently rate the paper as "borderline accept". I may adjust my rating based on the authors' reponse during discussion period.

### Soundness
2

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
5

### Summary
This work combined a SAE vision encoder, an LLM and the linked highest activating features, to generate radiology report. The authors used the public MIMIC-CXR dataset for this work.

### Strengths
The computational framework seems reasonable. Each component is pretty well established.

### Weaknesses
However, the originality of the methods is very marginal. The algorithmic or methodological innovation is low.

### Questions
Not sure why the authors did not other additional datasets for independent validation?

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
3

### Summary
•This paper introduces SAE-Rad, a methodology that uses SAEs to decompose latent vision transformer representations into features, some of which may be human-interpretable. These features are then used to adapt a pretrained LLM to directly generate radiology reports. Ablation studies are performed to evaluate the sparsity elements of the SAE and some qualitative evaluations of the report quality and counterfactual images is also performed.

### Strengths
•	The paper has a novel implementation of sparse autoencoders for the task of general text generation (radiology reports are the use case in this study).
•	The quality of the writing is high and the paper is quite easy to comprehend.  
•	Multiple examples are provided which helps building a better understanding of the model performance

### Weaknesses
•	It is a bit unclear whether the overall goal of the paper is to describe whether SAEs can be used to generate text or to develop a high-quality report generation model. If it is the former, then additional comparisons with more studies image captioning datasets would be better, including metrics such as CIDEr or SPICE. If it is the latter, then the qualitative reader study would have to be substantially improved, more domain-specific comparisons would be needed, and there could be more domain-specific metrics included. Currently, the paper straddles the area between both fields.
•	For the claim of modularity of image encoders and LLMs, quantitative comparisons would be needed to solidify this argument. Specifically, it is unclear how the choice of LLM impacts the overall performance or if the SAE features are truly invariant to the choice of LLM.
•	Metrics choice: Evaluating report quality is challenging, as is well pointed out. Besides RadFact, there are a few new approaches that are being used. The Rexval and Green scores could be particularly useful here, as they offer more fine-grained analysis of the generated text quality and clinical relevance. It would be beneficial to include these metrics to strengthen the evaluation.
•	Qualitative investigation shows that randomly selected feature modes depict to human perceivable concepts. This study would be stronger if a more rigorous analysis of these features were to be performed to better understand what the signifiance of these features is. For example, a quantitative analysis of the correlation between feature activation and specific image characteristics would be beneficial.
•	The ablation study uses the radfact score, which has not been extensively substantiated by the community. More common scores here may be better as comparisons since many other models are not benchmarked with this metric. It is difficult to assess the relative performance of the proposed model without more standard metrics.
•	The entire counterfactual section seems very abrupt and well not justified or explained. What is unsupervised segmentation? This section needs substantially more detail or needs to be removed. The lack of clarity makes it difficult to understand the purpose and validity of this section.
•	The reader study seems very superficial, unfortunately. 30 reports are too small to have concluding thoughts from. Were sentences evaluated or the whole results? What constitutes a significant error? Upon reading the appendix, it seems that only 10 reports are analyzed. It is impossible to draw any conclusions from this. Evaluating sentence by sentence also seems worse than evaluation of the whole report.

### Questions
•	Eq: 4 Is there an empirical technique for understanding what an optimal number for /pi_gate should be compared to /h_hate?
•	Difference between SAE and SAE-Rad #2: What would the impact of enforcing decoder sparsity be on the encoder itself? One could likely posit that it could further encourage encoder sparsity?
•	Difference between SAE and SAE-Rad #4: The choice of the L0 norm is seemingly heuristic? Could this be relaxed to have more firing features to better represent entangled concepts? I also wonder if there is something to be gained from exploring the relationships between this optimization paradigm and beta-vaes that expicitly force some level of disentanglement of feature sets.
•	How is set R(i) chosen when creating natural language representations of firing features? I suspect this would substantially depend on the size of R? Moreover, i wonder how representations learned from your SAE vary compared to the usual VAE-style methods. Are SAE grouped images also grouped with traditional VAEs?
•	Figure 2 is very interesting. Should we be able to hypothesize whether the learned firing features should be coarse grained (like devices/tubes) or fine grained (specific sided pleural effusion)?
•	In Figure 3, how is it that SAE-Rad does not include any comparisons with an image prior (the last two sentences in the ground truth report)?
•	Ablation study: are there specific differences in compute/performance with higher expansion factors? Moreover, what is unique about x64 that makes it better than 128 or 32?
•	What was the best performing model that was used? From the ablation it seems like the 64 features? If so, title of the paper should be edited.
•	What is the performance of MAIRA models with the same amount of data as SAERad?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper concentrates on the interpretability of VLMs for radiology report generation. It uses SAE to decompose visual features of an input image and exploits an LLM to distill the entire report into descriptions of SAE features. Finally, by compiling these descriptions, a full report can be obtained.

### Strengths
1.This work discusses the interpretability of VLMs in radiology report generation tasks that is a hot, interesting, and critical topic.

2.The authors provide an extensive analysis in the paper and appendix.

### Weaknesses
1.As far as storytelling is concerned, the motivation for using SAE for model interpretability is not clear to me in the abstract and introduction. I can find some clues in Section 3, but in general it is not obvious, especially to readers unfamiliar with the topic.

2.Overall, the readability of the paper needs further improvement.

3.In terms of methodology, SAE has been well studied in interpreting LLMs (see https://arxiv.org/pdf/2406.04093; https://openreview.net/pdf?id=XkMrWOJhNd). I understand that the focus of this work is on VLMs, and while I like the topic discussed in this paper, I have to say that it does not seem very novel to me. Also, I note that gated SAE from Rajamanoharan et al., 2024.

4.The following paper utilizes the idea of sparse learning (not limited to SAE) to interpret VLMs: https://arxiv.org/abs/2402.10376. The authors do not mention this work.

5.Regarding experiments, in my opinion, the current results are not very convincing, mainly because of the choice of competing methods. I understand that VLM-based methods should be main competitors. But the authors should also compare their model with other non-VLM approaches, because there are already many. I believe that the study of model interpretability should be based on the fact that the model can work well. In addition, there are more VLM-based, open-source methods for radiology report generation, e.g., RaDialog and R2GenGPT, which the authors have not considered. Note that many VLM and non-VLM approaches are open-source, and the authors can reimplement them and compute all the same metrics for them.

### Questions
My main concerns are the novelty of the paper (see Q3 and Q4) and the persuasiveness of experimental results (cf. Q5). In addition, it would be better if the authors can improve the readability of their paper, considering the readers unfamiliar with this topic. I am willing to raise my rating if the authors can address my concerns.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper introduces SAE-Rad, a framework for generating radiology reports using Sparse Autoencoders (SAEs) to decompose image representations into human-interpretable features. SAE-Rad uses a hybrid gated SAE architecture to balance reconstruction accuracy and sparsity, extracting meaningful medical features. The extracted features are transformed into detailed reports by a pre-trained large language model (LLM) without requiring further fine-tuning. Experiments on the MIMIC-CXR dataset show that SAE-Rad achieves competitive performance on radiology-specific metrics, outperforming models like CheXagent with fewer computational resources.

### Strengths
1.Experimental Section: (1) The qualitative analysis is comprehensive, effectively demonstrating the capabilities of our model. (2) The ablation study is thoroughly designed.

2.The methodology is straightforward and effective, with a clear motivation. This approach directly decomposes image class tokens from a pre-trained radiology image encoder into human-interpretable features, which are then compiled into comprehensive radiology reports.

### Weaknesses
1.The novelty of the method is not thoroughly demonstrated. While applying Sparse Autoencoders (SAE) in vision-language models (VLMs) represents an innovative effort, the use of SAEs to enhance the interpretability of large language models (LLMs) is already a well-established area. Examples include OpenAI's "Scaling and Evaluating Sparse Autoencoders", which extends SAEs to GPT-4, and Google DeepMind's "Gemma Scope: Open Sparse Autoencoders Everywhere All At Once on Gemma 2".
2.The comparison with existing methods is limited. Table 1 only compares three methods: CheXagent, MAIRA-1, and MAIRA-2, lacking a broader comparison with other open-source methods that generate reports using large language models (LLMs), such as R2GenGPT, RaDialog, and XrayGPT. Although these methods may not utilize the Clinical Metrics evaluation indicators employed in this work, they are open-source, and some provide pre-trained model weights. Why not attempt to replicate these indicators on these open-source methods?
3.The experimental results lack persuasiveness. Although the paper notes that NLG Metrics are not sufficiently comprehensive for evaluating radiological reports, the vast majority of report generation studies still rely on NLG Metrics as the primary basis for evaluation. However, the scores achieved by this work on NLG Metrics are not competitive; with a BLEU-4 score of 1.9, it falls significantly short when compared to other LLM-based radiological report generation efforts, such as RaDialog with a 9.5 and R2GenGPT with a 13.4.
4.The experimental dataset is limited. The quantitative comparisons are conducted using only one public dataset, MIMIC-CXR. However, two other commonly used public datasets for medical report generation are IU-Xray and openi. The paper R2GenGPT, XrayGPT incorporates the MIMIC-CXR and openi datasets.
5.The logical flow of the text is not clear enough. The introduction highlights the primary flaw of existing VLMs as the hallucination issue, yet the paper does not propose an effective method to eliminate hallucinations. Specifically, the introduction of SAE as a solution lacks persuasiveness. Additionally, the introduction states that 'the generated reports a VLM provides may not be faithful to the underlying computations of the image encoder.' Is there factual evidence to support this claim?

### Questions
1.Why not try replicating these indicators using the open-source methods mentioned above?
2.Why not explore two additional open-source datasets?
3.How can the hallucination issue discussed in the article be resolved?

### Soundness
3

### Presentation
2

### Contribution
3

# VEDIT: Latent Prediction Architecture For Procedural Video Representation Learning

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6, 6

## Abstract
Procedural video representation learning is an active research area where the objective is to learn an agent which can anticipate and forecast the future given the present video input, typically in conjunction with textual annotations.
Prior works often rely on large-scale pretraining of visual encoders and prediction models with language supervision. However, the necessity and effectiveness of extending compute intensive pretraining to learn video clip sequences with noisy text supervision have not yet been fully validated by previous works.
In this work, we show that a strong off-the-shelf frozen pretrained visual encoder, along with a well designed prediction model, can achieve state-of-the-art (SoTA) performance in forecasting and procedural planning without the need for pretraining the prediction model, nor requiring additional supervision from language or ASR. 
Instead of learning representations from pixel space, our method utilizes the latent embedding space of publicly available vision encoders. 
By conditioning on frozen clip-level embeddings from observed steps to predict the actions of unseen steps, our prediction model is able to learn robust representations for forecasting through iterative denoising \textemdash  leveraging the recent advances in diffusion transformers~\citep{peebles2023scalable}.  
Empirical studies over a total of five procedural learning tasks across four datasets (NIV, CrossTask, COIN and Ego4D-v2) show that our model advances the strong baselines in long-horizon action anticipation (+2.6\% in Verb ED@20, +3.1\% in Noun ED@20), and significantly improves the SoTA in step forecasting (+5.0\%), task classification (+3.8\%), and procedure planning tasks (up to {+2.28\%} in success rate, {+3.39\%} in mAcc, and {+0.90\%} in mIoU).

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces a novel pipeline,VEDIT, for procedural classifciation task using diffusion transformers without large-scale pre-training or additional language-based supervision. VEDIT leverages a diffusion transformer-based model to operate on latent embeddings derived from frozen, pretrained visual encoders. It is designed to predict the future steps in multi-step tasks (e.g., cooking, assembly) by iteratively denoising embeddings in the latent space, which are generated from observed steps. Authors conducted adequate experiments to demonstate that VEDIT achieves state-of-the-art (SoTA) results on various tasks like step forecasting, task classification, and procedure planning across multiple datasets (e.g., COIN, Ego4D-v2, CrossTask, and NIV).

### Strengths
Generally, the primary strength of this paper is the introduction of the novel diffusion-based representation learning method into the video understanding field. VEDIT achieves significant performance gains across multiple procedural tasks, such as step forecasting and task classification. 

**Clarity**: Most of this paper is well-written, with clear explanations and a solid grounding in relevant literature. 

**Originality**: The main idea of training the VEDiT using the CrossEntropyLoss from the downstream task for video representation learning is novel and has the potential to be applied to various temporal grounding tasks beyond classification. 

**Versatility**: VEDIT stands out for its versatility across tasks. VEDIT successfully handles multiple procedural learning tasks, including step forecasting, task classification, and procedure planning, proving its robustness in diverse scenarios.

**Quality**: The overall quality of the paper is high. The empirical results are well-supported by ablation studies, which explore the impact of different model components, and the paper presents a thorough comparison against state-of-the-art methods, showcasing the strengths of the proposed model.

### Weaknesses
There are some major concerns:
- While the approach of training VEDiT using CrossEntropyLoss from downstream tasks is novel, it remains challenging for the audience to understand why the diffusion model can learn with this design and the training pipeline. From the destination in L239-L241 and  L301-L303,  it seems the sampled Gaussian noise will be passed to $12 \times 24= 288 $ transformer blocks in a single forward pass, where $12$ is the number of transform blocks and $24$ is the denoising steps. It seems that the computing needs are much higher than baseline methods, and it may not support other inference parameters, including denoising steps and classifier-free guidance scales, since they are fixed in training. It isn't clear how well it works when reducing the sampling steps to lower steps to balance the computing cost and performance boost.
- Using diffusion models for video embedding prediction is time-consuming since it requires $N$ times longer inference time. However, authors didn't discuss the limitation in this paper.


In conclusion, these are concerns and weaknesses that could further improve the paper. However, the weaknesses outweigh the strengths. Consequently, I am leaning towards suggesting rejection of this paper. I am looking forward to the authors' rebuttal and clarification.

### Questions
I also have a variety of questions that did not significantly impact the rating for the paper:
- The paper demonstrated the advantage of using VEDiT on chunk-level classification tasks. Can the approach be extended to other temporal understanding tasks that predict start/end time? e.g., action grounding
- The paper entirely leverages flow-matching sampling with a fixed number of sampling steps. How's the model's performance with different scheduler/sampling parameters?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper aims to advance video representation learning by proposing a diffusion transformer specifically for procedural video representation. It demonstrates that a frozen, pretrained visual encoder paired with a prediction head can achieve promising performance across five procedural learning tasks.

### Strengths
1. The proposed method avoids the need for compute-intensive pretraining of the prediction model. It uses a pretrained, frozen visual encoder to capture robust visual representations, eliminating the need for additional supervision (e.g., language or ASR) commonly required in prior methods

2.The model's empirical evaluation demonstrates significant performance improvements on procedural video benchmarks like COIN, CrossTask, and Ego4D, showing gains in task classification accuracy and long-horizon action anticipation.

### Weaknesses
1.Lack of Sufficient Innovation: The VEDIT model's components lack distinct novelty. (1) VEDIT’s architecture is primarily a combination of existing techniques—pretrained visual encoders and diffusion transformers—rather than introducing new modules. (2) The method’s adaptation of diffusion transformers to work in the latent embedding space of video representations has been explored previously, as in PPDP.

2.Omission of Computational Cost Analysis: The paper does not address the computational cost of the method. Due to the iterative nature of the diffusion process, VEDIT incurs slower inference times than models that make predictions in a single forward pass. This characteristic may limit its use in real-time or low-latency applications.

3.Lack Disccusion of Multimodal Integration: By not incorporating textual data or language models, the method overlooks semantic information that could enrich the understanding of procedural steps, especially in instructional videos that include narration.

### Questions
See details in 'Weakness' section.

### Soundness
2

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
This paper deals with  Procedural Video Representational Learning, in which a model predicts steps in a underlying process (eg cooking a dish). The goal is to learn a representation that enables prediction and understanding of the semantics of step-by-step processes through videos, often egocentric or how-to videos. Most works in this space pre-train models on data from HowTo100M with extracted ASR captions which is time-consuming and expensive. This paper's contribution is (1) a novel architecture for the procedural video task based on diffusion / flow matching in latent state-action space and (2) a method that relies only on frozen pre-trained image encoders rather than explicit procedural weakly supervised pretraining. In doing so, they achieve SoTA results.

In general, I think this is a reasonably strong paper, and the only weakness to me is that the architecture has slightly limited novelty; it's not very clear to me exactly how this differs from a standard diffusion transformer. The use of a frozen encoder, while simple, works well and avoids having to do expensive ASR-based pre-training. The models are also scaled to high parameter counts and thus will be useful to the community.

### Strengths
1) The proposed architecture (diffusion in latent space between steps) is interesting. I think doing diffusion on the latent embeddings is a smart way to generate new embeddings that can be used for predicting final class embeddings. 
2) The results surpass existing SOTA and the ablations are comprehensive. The method also avoids relatively expensive pre-training on direct step data, making use of easily available visual encoders like SigLIP. The appendices are thorough and explain relevant design decisions for the proposed architecture.
3) The models trained are relatively large and will be helpful for the community if made available.

### Weaknesses
1) The models trained are quite large, with the largest having 1.77B parameters. Given that the improvement over SOTA is relatively minor in most cases, it's not clear that scaling this method really works - could you comment on why this might be the case?

2) The architectural novelty is a little limited. The idea of doing diffusion to produce intermediate embeddings isn't new (as is stated in the paper) and this paper differs from prior work mostly by using a frozen SigLIP encoder rather than one pre-trained on HowTo100M (if i am understanding correctly).

3) It's not super clear how the proposed VeDIT differs from standard diffusion transformer blocks except for the embedding concatenation - am I missing something? If so, could you explain further?

### Questions
1) It's stated the task is either predicting the label of unseen events in between two input events (procedure planning), or predicting the label of a future event.  In the case of procedure planning, how does the model know how many clips to generate?  It's not obvious from the system figure (Fig 2) how multi-clip generation works - does that require multiple runs of the entire diffusion model? Is this number fixed?

2) From an intuition standpoint, why is diffusion the right choice for generating an embedding given a set of input embeddings? Are there no faster alternatives? What was the reasoning behind this choice compared to other alternatives?

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
4

### Summary
This work questioned the necessity and effectiveness of pretraining by develop a SoTA method for forecasting and procedural planning without the need for pretraining the prediction model. The proposed model, VEDIT, leverage diffusion transformer and attentive classfier directly trained for downstream tasks. Empirical results showed that VEDIT outperform all baselines.

### Strengths
1. Nice presentation and well-designed figures.

2. Strong empirical performance: VEDIT outperform all baselines quantitatively on all three benchmarks.

### Weaknesses
1. Definition of pre-training: The most confusing point for me is that the authors claim the results of this work could challenge the necessity of pretraining. However, first of all, VEDiT itself uses a pretrained encoder. How is this different from what the authors define as pretraining? Secondly, isn’t the training of the diffusion part considered pretraining? I think the authors should make a stricter distinction and definition of pretraining to help readers clearly understand what they really want to refer to by "pretraining."

2. Training objective of DiT: If the training of the diffusion part isn’t considered pretraining, then what is the role of diffusion here? The authors should use mathematical formulas to clarify exactly what their loss function is; the current explanation is too vague. Additionally, starting from line 233, the description of diffusion training seems to suggest a possible misunderstanding of diffusion training.

3. Test-time training [1]:  This is just a suggestion, but based on the authors' model, I think that applying test-time training exclusively to the diffusion component could further enhance the model's performance during inference.

### Questions
All of my questions are listed in the weakness part.

### Soundness
2

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
4

### Summary
This paper proposes a procedural video representation learning framework that utilizes diffusion transformers to predict visual representation in embedding space. This framework can be effectively transferred to various downstream tasks.

### Strengths
1. This paper is well-motivated and easy to follow.

2. VEDiT does not require pre-training the representation space but consumes multiple clips by using pre-trained representation, which is more efficient and applicable, as better representation can improve VEDiT further.

3. Extensive experimental results on various downstream tasks demonstrate the effectiveness of the proposed method.

### Weaknesses
1. Question about fair comparison: Without pre-training, I think VEDiT seems to be a large header for the downstream task. I cannot find how the baseline TimeSFormer is evaluated, but if it is evaluated with a simple linear classifier, i.e., linear probing, it seems that VEDiT's performance gain is just from "training more parameters on the pre-trained representation".

2. Typo on page 2 ("fall back on on text annotations" -> "fall back on text annotations")

### Questions
Please answer the Weakness part.

### Soundness
3

### Presentation
3

### Contribution
3

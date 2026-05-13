# Mitigate the Gap: Improving Cross-Modal Alignment in CLIP

- Decision: Accept
- Scores: 6, 6, 6, 6, 8, 6, 6

## Abstract
Contrastive Language--Image Pre-training (CLIP) has manifested remarkable improvements in zero-shot classification and cross-modal vision-language tasks. Yet, from a geometrical point of view, the CLIP embedding space has been found to have a pronounced modality gap. This gap renders the embedding space overly sparse and disconnected, with different modalities being densely distributed in distinct subregions of the hypersphere. In this work, we propose AlignCLIP, in order to improve the alignment between text and image embeddings, and thereby reduce the modality gap. AlignCLIP increases the cross-modal alignment, and yields gains across several zero-shot and fine-tuning downstream evaluations by sharing the learnable parameters between the modality encoders and a semantically-regularized separation objective function on the uni-modal embeddings.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes the modality gap problems existing in CLIP and shows the multi-modalities distribusion characteristics. To handle this problem, They proposed a novel method named AlignCLIP. The proposed AlignCLIP mitigates the multi-modal gaps with sharing the parameters between all modalities. To align the text-image and image-image well, they also propose the intra-modality separation objective function. Then, they have provided extensive experiment evidance to prove the effectiveness of  AlignCLIP.

### Strengths
This paper shows the multi-modalities distribusion characteristics and proposes two novel idea to mitigate such modal gap. This is a clear and well-writen paper, easy to follow. The experiments for ablation is sufficient. This idea of AlignCLIP is reasonable.

### Weaknesses
1. Less evidance to prove the modality gap existing.
2. It seems this paper is not the first to propose modality gap problems.
3. I doubt that Sharing the parameter space between the vision and language encoders may cause each modality like text or image features not learning well.
4. The object function should consider more about the text modality.

### Questions
1. The authors have provided DOSNES projection of the CLIP-encoded image–text pairs from CC3M with ViT-B-32, I wonder how it will be with ViT-L-14 and other image-text datasets?
2.  are the existing CLIP-based methods performing the same phenomen like original CLIP ? 
3. The authors have mentioned that there are several works also studying the modality gaps, what is the difference between your findings and these works?
4. Sharing the parameter space between the vision and language encoders may cause each modality like text or image features not learning well, can you provide the parameter comparison between CLIP and AlignCLIP?
5. The proposed object function may cause the learning direction preferring the image based tasks, can you provide more evidance to prove it ?
6. The authors should provide more comarison experiments between existing more recent SOTA methods and AlignCLIP in each task settings.

### Soundness
2

### Presentation
4

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
The paper proposes a method to mitigate the modality gap in the representational space of CLIP. The authors introduce two modifications to CLIP (termed AlignCLIP) to achieve this: (1) Sharing the weights of the vision and text transformers in CLIP (termed ‘SharedCLIP’), and (2) using a new Intra-modality separation loss, which encourages separation between images in CLIP space while respecting some of the semantics of the similarities between the images.

The paper’s experiments study the effects of the modifications on a range of downstream tasks, and demonstrate that the AlignCLIP reduces the modality gap and improves zero-shot image classification, linear probe accuracy, robustness to distribution shifts, and multi-modal retrieval accuracy.

### Strengths
**Well motivated paper:** Understanding and mitigating the modality gap is an important direction in CLIP and its variants, which are ubiquitously used in many applications

**Clearly written:** Clear flow of ideas, motivations well explained

**Comprehensive ablation studies:** The authors suggested two directions (SharedCLIP + IMSep loss) for attempting to reduce the modality gap, and the effects of both SharedCLIP and SharedCLIP + IMSep loss were tested. Further, the impact of enforcing intra-modality separation on images, texts and their combination was tested individually. Finally, the effect of the rescaling mechanism to control separation of similar images in the batch was also tested individually.

### Weaknesses
 **Potentially limited applicability:** The approach of AlignCLIP is only applicable where transformer architecture can be used for both modality encoders. This may limit the applicability to other multimodal models with a modality gap using non-transformer architectures: The authors could measure the performance of the proposed IMSep loss without the SharedCLIP architecture, as the IMSep loss could be applied to any non-transformer architecture. (See Question 2)

**Unfair comparison to baselines:** I appreciate the authors’ efforts to have a comparison with popular baselines in Table 7. However, as far as I understand, the numbers for CLIP, CyCLIP, and DFSep in Table 7 were taken from the DFSep paper [1] . However, important hyperparameters that are used to train CLIP, CyCLIP, and DFSep in [1] are different to what the authors used to train SharedCLIP and AlignCLIP in their paper. As a result, these comparisons may not be fair. For instance, authors in [1] trained their models for 64 epochs using batch size of 128, and used 1024 dimensional features. Whereas authors of this paper trained for 30 epochs using 512 batch size, and 768 dimensional features. Further, CLIP models in [1] used ResNet-50 as the image encoder, whereas the authors of this paper used ViT-B-16 backend.

- I would recommend that the authors either re-implement CyCLIP and DFSep using the same hyperparameters as in their experiments, or repeat their experiments using the same hyperparameters as used in CyCLIP and DFSep in [1].
- In either case, these differences should be clearly stated in the paper.

### Questions
1. **Why did the authors use “photo of {caption}” prompt in multi-modal retrieval, instead of just the caption itself?**
Were there any intuitions the authors had about this approach? 

2. **Did the authors check performance using just the IMSep loss, without using the architecture of SharedCLIP?**
This would allow the approach to be used regardless of encoder architecture. 

3. **Did the authors track how the learnable temperature parameter changes during training in AlignCLIP?** Low temperature is known to be an important factor in the emergence of the modality gap.  Therefore, it would be interesting to note the trend and/or the final value of learned temperature in AlignCLIP.

### Soundness
3

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
4

### Summary
This paper proposes AlignCLIP to reduce the modality gap in CLIP embedding space. The method leverages a shared transformer to align the image and text embeddings. An additional loss function is also introduced to separate semantically distinct unimodal embeddings. Experimental results show that the proposed method can reduce the modality gap and improve the performance on downstream tasks.

### Strengths
1. Investigating the multimodal embedding space of vision-language models is an interesting topic.
2. The proposed framework seems easy to implement while still being very effective.

### Weaknesses
1. The technical contribution appears limited, as prior work has also leveraged the shared transformer framework [1, 2]. While the authors extend this to include all parameters, the core idea of sharing parameters across modalities is not novel. The incremental gain from sharing all parameters, as opposed to a subset, needs more rigorous justification and analysis. Specifically, it's unclear if sharing all parameters consistently leads to better performance or if it's highly dependent on the specific dataset and task.

2. The stated goal of this work is to reduce the modality gap within the CLIP embedding space. So basically, the approach should rely on the pre-trained CLIP embedding space. However, the proposed method utilizes a single-encoder framework, which is completely different from CLIP’s two-tower architecture. This raises questions about whether the obtained embedding space is relevant to the CLIP embedding space. The paper does not adequately address how the learned single-encoder embedding space aligns with or relates to the original CLIP space, especially given the architectural differences. The paper should provide a more detailed analysis of the structural similarities and differences between the two embedding spaces and how this impacts the modality gap.

3. To my knowledge, the effect of the modality gap on downstream task performance remains an open question. In some cases, a larger modality gap can actually improve performance on certain datasets [3]. This paper could be strengthened by including a more in-depth discussion or insights. The paper should include a more nuanced discussion on the relationship between the modality gap and downstream task performance, acknowledging that reducing the gap is not always beneficial. It would be useful to explore scenarios where a larger gap might be advantageous and discuss the potential trade-offs.

### Questions
please see the weaknesses.

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
4

### Summary
This paper introduces AlignCLIP, a variant of the CLIP model aimed at reducing the modality gap between image and text embeddings in cross-modal learning. The authors propose two main modifications: SharedCLIP, which shares the learnable parameters of vision and language encoders, and Intra-Modality Separation (IMSep), an additional objective that regularizes the distances within each modality based on semantic dissimilarity. Through extensive experiments, the authors demonstrate improvements in cross-modal alignment and zero-shot performance, with AlignCLIP consistently outperforming baseline CLIP on a range of benchmarks.

### Strengths
- The authors address a meaningful challenge in multimodal learning, i.e., the modality gap, which affects alignment quality in embedding spaces.
- The paper evaluates performance on various benchmarks (e.g., zero-shot classification and retrieval tasks) and robustness against distributional shifts, making the findings broad in scope.
- Visualizations, like the DOSNES projection and alignment score plots, effectively show the improvements in modality alignment and embedding spread across models.

### Weaknesses
 - Both SharedCLIP and IMSep primarily extend existing contrastive learning techniques. Sharing parameters between encoders is a known approach, and the IMSep loss largely repurposes InfoNCE without substantial modifications. The paper’s novelty, therefore, is limited.
- Empirical comparisons with relevant baselines are lacking, as AlignCLIP is only compared with the original CLIP (and SharedCLIP, also introduced in this paper), omitting several cited "naive" approaches for modality gap reduction.
- For example, the paper repeatedly claims that naive alignment approaches "likely" negatively impact downstream zero-shot performance and backs up this with a theoretical argument, but no qualitative or quantitative results are provided to show that this is indeed the case.
- Table 7 also compares AlignCLIP with two other CLIP variations, but from what I understand, these variations were not designed to mitigate the modality gap.
- In L198-200, the text claims the denominator gets strongly minimized, but the next sentence in L200-202 says it is not strongly minimized. This seems to be a mistake.
- L269 says "In AlignCLIP, we set $\alpha=1$ and $\beta=0.5$", $\beta$ is never introduced in the paper. Moreover, in appendix A.2, it says $\alpha=0.5$ was used, which contradicts this line.

### Questions
- The paper states that naive shifts harm downstream performance due to distorted relative distances. Could the authors provide empirical evidence or experiments to support this claim? e.g., Liang et al. (2022)
- The choice of hyperparameters, such as the weight of the IMSep objective in total loss($\alpha$), appears arbitrary. Did the authors conduct sensitivity analyses on these hyperparameters, and if so, could they report their findings?
- While alignment scores improve, does this necessarily translate to enhanced downstream performance? Could the authors discuss specific cases where improved alignment directly correlates with task gains?
- How significant are the alignment improvements in practical, real-world applications? For instance, does better alignment consistently yield qualitatively superior results in retrieval scenarios?
- Do you expect your method to scale easily to larger backbones (e.g., ViT-L or ViT-H) using a dataset like LAION-400M instead of CC12M?
- How is the pre-trained sentence encoder (SBERT) used to calculate semantic distance? Is it robust across various domains and vocabularies in the dataset?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper proposes AlignCLIP, a solution to the text-image alignment issue in CLIP. Specifically, AlignCLIP (1) shares encoder parameters and (2) enhances cross-modal alignment without disrupting embedding distances by introducing IMSep. IMSep particularly adjusts the unimodal embeddings, placing semantically similar image embeddings close but dissimilar image embeddings apart. Experimental results demonstrate substantial improvements in zero-shot classification, robustness to distribution shifts, and multi-modal retrieval, highlighting AlignCLIP's superior alignment and performance over existing CLIP models.

### Strengths
- AlignCLIP effectively addresses the text-image alignment issue in CLIP, offering meaningful performance gains over existing methods.  

- I like the idea of IMSep, adjusting unimodal embeddings for enhancing cross-modal alignment. 

- The method has been verified under various tasks-- especially achieving gains both in zero-shot classification and retrieval seem meaningful.

### Weaknesses
 - I am not very confident in the evaluation settings. Are all competing models trained on the same dataset? If not, how is performance comparability ensured?

- The ideas are interesting; however, this still falls within contrastive learning. Could you strengthen the value of your method by connecting it to existing work? While I believe your approach is new, a clearer link to prior work would enhance its contribution.

### Questions
Please see the above weakness.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 6

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces AlignCLIP, a novel training strategy that aims to improve the cross-modal alignment of CLIP-like models by addressing the modality gap between image and text in the shared embedding space. The authors propose to share the learnable parameters between the vision and language encoders to align the two modalities more closely, and to add an Intra-Modality Separation objective function that pushes semantically dissimilar image embeddings apart. Authors train from scratch CLIP, a SharedCLIP (with shared learnable parameters between the vision and language encoders), and AlignCLIP on CC12M. Extensive experiments demonstrate that AlignCLIP improves zero-shot classification, robustness to distribution shifts, and multi-modal retrieval tasks compared to the original CLIP.

### Strengths
- AlignCLIP demonstrates significant improvements to the original CLIP, with measurable gains in downstream tasks such as zero-shot classification and robustness to distribution shifts.
- The IMSep objective adds a novel approach to handling intra-modality representations, ensuring that semantically dissimilar image embeddings are spread apart without affecting semantically similar pairs.
- The paper provides both quantitative and qualitative analyses (I really appreciate Fig. 5), providing clear insights into improvements in retrieval tasks and the reduction of the modality gap.

### Weaknesses
 - AlignCLIP’s performance on fine-tuned retrieval tasks shows marginal improvements over SharedCLIP, with SharedCLIP sometimes even outperforming AlignCLIP (see Tab. 5).
- Ablation studies on the key components, while present, could be expanded. In particular, it would be interesting to explore how much the "Pre-trained Sentence Encode" improves the performance and the benefits of using the ImSep loss component. I am afraid that the smaller improvements in such cases could arise just from using an additional pre-trained encoder (i.e. SBERT all-mpnet-base-v2) at training time.

**Additional Consideration**. I noticed several significant errors within the method section Sec. 3.1 and the method figure (Fig. 2) that impact its reliability. In particular, the figure shows:
- *Conv2d Applied to Image Patches*: I believe this is an error stemming from a misunderstanding of the common CLIP practice of using a Conv2d with a stride equal to the image patch size (that is equivalent to applying a standard linear layer to the flattened patches). So depicting a Conv2d after the patches, as the authors proposed, seems incorrect.
- *Max Pooling Applied to Text Embeddings*: Similarly, I suspect that applying max pooling to the text token patches is another mistake. The authors stated: "Following the original CLIP, we use max-pooling for text embeddings." (line 165). However, I believe this results from a misunderstanding of OpenAI's CLIP implementation, which uses an argmax operation to select the EOS token.
These errors impact the clarity and accuracy of the figure and may mislead readers regarding the model architecture.

### Questions
- Q1. How would AlignCLIP perform with different backbone architectures besides ViT-B-16? Is the performance consistent with other vision transformers?
- Q2. Could you explain why AlignCLIP’s retrieval performance only marginally improves over SharedCLIP in certain settings? Are there any specific modifications you plan to address this?
- Q3. Conducting an ablation study of CLIP using the ImSep loss would be insightful. If such experiments haven't been performed yet, evaluating whether this approach might outperform or underperform compared to AlignCLIP in zero-shot classification and cross-modal retrieval could offer meaningful comparisons.
- Q4. While mitigating the modality gap is a promising approach to enhancing cross-modal alignment, it might be worth discussing its effectiveness given that the standard definition of the "modality gap" [1]—the difference between the centroids of the two modalities—can be zero even if individual image-text pairs aren't perfectly aligned. Clarifying why this approach remains effective under these conditions could strengthen the understanding of its impact.

[1] Mind the Gap: Understanding the Modality Gap in Multi-modal Contrastive Representation Learning (https://arxiv.org/abs/2203.02053)

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 7

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper proposed a novel method named AlignCLIP to address a recognized problem -- modality gap, for the CLIP network. The improved components include (i) a shared transformer and (ii) an intra-modality separation module. The proposed method surpassed the existing methods in most cases.

### Strengths
1. Technical solid paper with clear stated motivation and well organized content.
2. The proposed Intra-Modality Separation module is novel and is benefit to the community.
3. The proposed method surpassed the existing methods in most cases.

### Weaknesses
1. The idea of shared transformer is less novel. From my understanding, since the shared transformer for CLIP has been proposed by You et. al., then extending it to the projection layer is just an incremental improvements. The paper should discuss why the extension to the projection layer is necessary comparing to the existing methods. For example, in terms of "extend the sharing to the extent possible" in line #168m, what should we do if using CLIP-ResNet instead of CLIP-ViT.
2. Since the paper claims the (i) SharedCLIP (ii) IMSep module. It is not clear that which module contributes more on the overall performance. Since the SharedCLIP is strongly dependent on transformer structure, while IMSep module is more related to the general multi-modality contrastive learning task, therefore, the IMSep moduel has better expansibility for various model structures. Therefore, an ablation study on this is necessary, i.e. (original_CLIP+)SharedCLIP vs original_CLIP+IMSep, if I missed this experiment, please point it out during the rebuttal.
3. It's necessary to add some discussion for Table.5, regarding the COCO T->I. It seems the SharedCLIP works better in the T->I scenario, but what reason cause the degradation while adding IMSep? Some discussion and analysis regarding why this degradation occurs would be benifit for researchers to understand the limitation of the proposed model, for example, is it due the complexity of COCO dataset itself, or due to the IMSep while performing T->I. How is the performance while applying original_CLIP+IMSep only on T->I?

### Questions
Please see weakness.

### Soundness
3

### Presentation
4

### Contribution
3

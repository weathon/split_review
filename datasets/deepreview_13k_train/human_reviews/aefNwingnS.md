# Scaling Channel-Invariant Self-Supervised Learning

- Decision: Reject
- Scores: 3, 6, 5, 3, 5

## Abstract
Recent advances in self-supervised pre-training of foundation models for natural images have made them a popular choice for various visual systems and applications. Self-supervised strategies have also shown promise in non-RGB scientific imaging domains such as in biology, medical and satellite imagery, but their broader application is hampered by heterogeneity in channel composition and semantics between relevant datasets: two datasets may contain different numbers of channels, and these may reveal distinct aspects of an object or scene. Recent works on channel-invariant strategies report substantial advantages for those that account for variable channel compositions without sacrificing the ability to jointly encode channels; yet, how these strategies behave at scale remains unclear. We here show that, surprisingly, trained across large-scale microscopy datasets, independent-encoding of channels consistently outperforms joint-encoding methods by a substantial margin. We explore this result along an extensive set of experiments and open-source a new general purpose feature extractor for fluorescent microscopy images, DINO BoC, that sets a new state-of-the-art across challenging benchmarks, including generalization to out-of-distribution tasks and unseen channel combinations at test time.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper proposes solutions for the challenge of handling varying number of channels, in particular for microscopy images where the number of channels can be different in each dataset. The authors use three main self-supervised approaches on DINOv2, with Bag of Channel approach performing the best across the benchamrks used.

### Strengths
- The problem statement and related work are well-written, and the problem is relevant
- The experimental section is reach. The authors provide results and comparisons on several datasets and benchmarks
- The code is going to be publicly released for future uses.

### Weaknesses
The main weakness of the paper is the limited contributions. The best performing method, which the authors call Bag of Channels, was proposed by (Xun et al, 2024). This paper only applies this method on DINOv2. Although the experiments and comparisons, alongside introduction of the Hierarchical Attention Model is valuable, these contributions could be a better fit for other conferences/journals rather than ICLR. The application of the Bag of Channels approach to DINOv2, while showing good empirical results, does not introduce a novel methodological contribution. The core idea of processing channels independently was already established, and the adaptation to a different backbone architecture and self-supervised learning strategy is an incremental step rather than a significant leap. The Hierarchical Attention model, while presented as a contribution, does not seem to be a core component of the best-performing method (Bag of Channels) and its impact is not thoroughly explored or justified, making it seem somewhat redundant in the context of the paper's main findings. The experimental results, while extensive, primarily serve to validate the performance of an existing method on a new architecture, rather than demonstrating a novel approach or insight.

### Questions
The experiments are performed on datasets with 2-5 channels,
- Is there any correlation between the number of channels and the method performances?
- Why didn't you use datasets with more channels (as stated in L38, up to 8 channels)?

### Soundness
3

### Presentation
3

### Contribution
1

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work study different channel invariant strategies to train vision transformers for self supervised learning. These approaches are study in the context of fluorescent microscopy images where different datasets carry different combination of channels. Channel invariance allows for self-supervised pretraining using a combination of all existing datasets which translates to better pretrained models. Authors also proposed hierarchical attention as a novel way to train channel invariant models.

### Strengths
* Paper is well written and technically sound
* The work address a significant problem for applying machine learning to microscopy images at scale
* Proper evaluation of the different approaches is coducted

### Weaknesses
 * It is not clear how the bag of channels approach claimed as yours is different to Microsnoop form Xun et al.
* The proposed hierarchical attention approach rarely beat the bag of channel approach 
* Work only tested on a single application domain.

### Questions
* Do you expect this approach to work for other application domains with image modalities of different number of channels with limited channels matching across datasets like it is often the case in remote sensing?
* Figure 2 legend can be improved by adding more details to it.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The paper proposes a self-supervised learning method for heterogeneous multi-channel images. The proposed method uses DINO v2 as a backbone and integrates bag of channels and hierarchical attention into Channel ViT. The work is evaluated on microscopy images extensively.

### Strengths
1. The experiments on microscopy datasets are extensive and the reported numbers provide empirical understandings.

### Weaknesses
Major Concerns:
1. The title describes a generic method for multi-channel images, but the paper focuses only on microscopy images. Considering that different multi-channel images may exhibit different behaviors, the title seems to be a bit big. The authors shall either broaden their experiments to include other types of multi-channel images, or narrow the title and framing to focus specifically on microscopy images.
2. The title states this work focuses on self-supervised learning. However, after reading the whole paper, the method is not generic. On the contrary, it seems to be designed based on DINO v2. No discussion on the choice of DINO v2 at all.  The authors shall provide a clear justification for choosing DINO v2 as their base method. Additionally, please discuss how your approach might generalize to other self-supervised learning frameworks, or explain why your method is specific to DINO v2.
3. The contributions on self-supervised learning is not clear to me. In my opinion, the paper seems to be a multi-channel variant of DINO v2, which is an incremental work. But, the paper tries to tell a different story. If this work is about self-supervised learning while leveraging multi-channel images, please specify why this work differs from studies of self-supervised learning on RGB images. If this work focuses on adapting existing self-supervised learning works on multi-channel images, please clarify it from the title to introduction. 
4. The technical writing is a bit hard to follow. The presentation of the method proposed is unclear. The paper spends quite some space the background while the methodological details are provided in the appendix. It is recommended to reorganize the related works and method sections to show key methodological results.

### Questions
1. How does this method work on multi-channel images such as remote sensing or multi-spectral images?
2. Does this method work on other self-supervised learning framework?
3. Follow the same logic, will better self-supervised learning backbone show better results?

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper presents a large set of SSL experiments in the microscopy imaging domains and scales existing methods with the existing DINOv2 approach for channel-variant images.

### Strengths
The paper addresses an important problem related to channel-varying images in microscopy imaging and conducts an extensive set of experiments, including OOD generalization, within this domain. The trained models generally outperform the existing literature.

### Weaknesses
1) The paper's title, "Scaling Channel-Invariant Self-Supervised Learning," suggests broad applicability across various imaging domains. However, the experiments are limited to fluorescent microscopy images despite the relevance of channel-invariant features in other fields, such as medical and satellite imagery, as also acknowledged by the authors in the abstract. Prior work on channel-invariant learning has demonstrated applications across diverse image domains [1], including satellite imaging. A broader experimental scope of imaging domains (e.g., see [1]), rather than larger datasets on a single one, would align the paper’s claims with the actual generality and applicability of channel-invariant self-supervised learning across relevant fields. 

2) Contribution (i), which involves selecting DINOv2 and integrating it with the Bag of Channels approach (an existing SSL algorithm combined with a known channel-invariant module), is challenging to consider a meaningful contribution on its own since the combination of these methods lacks substantial technical novelty, as it doesn’t introduce new mechanisms or address specific challenges unique to this approach. 

3) The technical novelty (contribution (ii)) is limited, as the proposed Hierarchical Attention module appears to be a combination of existing methods (Channel-ViT and Bag of Channels) with the addition of extra "channel" tokens and corresponding attention masking. Furthermore, the clarity of presentation of the technical contribution needs improvement, as I explained in the next point. It is also unclear to me the motivation behind introducing DINO HA since, in Tables 1, 2, and 3, the best method is usually DINO Bag of Channels and not DINO Hierarchical Attention. What is the purpose of proposing two methods, with one clearly better than the other? 

4) The technical presentation of contributions (i) and (ii) is somewhat unclear and misleading. More precisely, the main technical section 3, which is named "Problem Formulation" (renaming needed), should instead focus on the description of the introduced modules and clearly discern the contributions of the paper (sections 3.3 (?) and 3.4) against the already existing strategies (i.e., sections 3.1, 3.2, 3.5). To clarify the contributions, it would help to split Section 3 into two sub-sections (Preliminaries vs Methodology) to help the reader better grasp the actual contributions. I would also suggest a better design of Figure 2, e.g., in a single panel, highlighting the differences between previous and proposed work. 

5) The related work section concerning SSL with microscopy images and section 4.1 are comprehensive but verbose and would need some summarization and re-writing.

### Questions
Unfortunately, while the paper tackles a relevant problem and demonstrates better performance through a large set of experiments, the contribution is limited by a lack of generalizability across (untested) imaging domains and, most importantly, by insufficient technical novelty.

See the weaknesses section to improve the technical presentation of the contributions. I am open to hearing the feedback from the authors on the rebuttal period.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
Some applications of ML (such as biology, medicine, remote sensing) feature different channels across datasets. This channel robustness challenge is under-explored in ML since natural imagery applications do not often face this challenge — they consistently use 3 channels (RGB). This paper focuses on fluorescent microscopy images to investigate channel robustness. (I'm using channel robustness to mean generalizing to missing channels and new channels.) A prior work, Channel-ViT tokenizes channels separately and can be robust to missing channels (similar to remote sensing models like SatMAE and Presto). This paper introduces a ViT architecture called DINO-HA. This paper thoroughly benchmarks Channel-ViT, DINO-HA, and DINO-BoC (Bag of channels) using large backbones (ViT-L) and large pretraining datasets. This paper finds that DINO-BoC often outperforms Channel-ViT, evaluated as a frozen feature extractor.

### Strengths
- This paper is well written
- Extensive experiments are performed. Specifically, using ViT-Large models, two different SSL algorithms, different pretraining datasets, and several in-distribution and out-of-distribution test sets.
- From my reading, the core finding is that a "bag of channels" approach can often outperform models that allow inter-channel reasoning. This is interesting and surprising.

### Weaknesses
 - Channel-ViT (the baseline) beats DINO-HA on 17 of 26 test sets on page 8. And DINO-BoC beats Channel-ViT on 16 of 26 test sets on page 8. I'm not convinced that DINO-HA is valuable to the community beyond these fairly negative results. 
- I do not consider DINO-BoC to be a novel method. It process channels separately using a ViT, then concatenates embeddings.

I recognize this is an applied paper and the bar for ML novelty is lower, however I question the value to the broader ICLR community. That being said, the experiments are extensive and the findings are interesting.

### Questions
As far as I can tell, DINO-BoC concatenates channel embeddings to form the full-sample embedding using the CLS tokens. This embedding is a D * N-dimensional vector (where D is the ViT width and N is the number of channels). And the full-sample embedding of Channel-ViT is a D-dimensional vector, taken from the CLS token. Although in the appendix it says the CLS token is concatenated across the last 4 layers for linear probing.

Can you please clarify how you build full-sample embeddings for each of the three methods? If Channel-ViT's embeddings are indeed D-dimensional and DINO-BoC are D * N-dimensional, I'd like to see results when they have the same sized embeddings. This can be done by taking the mean between channels (for DINO-BoC) to achieve D-dimensional embeddings. This can be done by concatenating the mean-pooled patch representations for Channel-ViT to achieve N * D-dimensional embeddings (specifically, you'd pool the patches for each channel, then concatenate these pooled channel-wise embeddings).

### Soundness
4

### Presentation
4

### Contribution
2

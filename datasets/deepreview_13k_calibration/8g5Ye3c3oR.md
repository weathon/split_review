# Dancing with Discrepancies: Commonality Specificity Attention GAN for Weakly Supervised Medical Lesion Segmentation

- Decision: Reject
- Avg Score: 4.50
- Scores: 5, 3, 5, 5

## Abstract
Increasing weakly supervised semantic segmentation methods concentrate on the target segmentation by leveraging solely image-level labels. However, few works notice that a significant gap exists in addressing medical characteristics, which demands massive attention. In this paper, we note: (i) Lesion regions typically exhibit a sharp probability distribution pattern while healthy tissues adhere to an underlying homogeneous distribution, which deviates from typical natural images; (ii) Boundaries of lesion foregrounds and structural backgrounds are blurred; (iii) Similar structures frequently appear within specific organs or tissues, which poses a challenge to concentrating models’ attention on regions of interest instead of the entire image. Thus we propose a Commonality-specificity attention GAN (CoinGAN) to overcome the above challenges, which leverages distribution discrepancies to mine the knowledge underlying images. Specifically, we propose a new form of convolution, contrastive convolution, to utilize the fine-grained perceptual discrepancies of activation sub-maps to enhance the intra-image distribution, making lesion foregrounds (specificity) and structural backgrounds (commonality) boundary-aware. Then a commonality-specificity attention mechanism and the GAN-based loss function are devised to jointly suppress similarity regions between different labels of images and accentuate discrepancy regions between different labels of images. This isolates lesion areas from the structural background. Extensive experiments are conducted on three public benchmarks. Our CoinGAN achieves state-of-the-art performance with the DSC of 71.69%, 84.73%, and 78.32% on QaTa-COV19, ISIC2018, and MoNuSeg datasets, making a significant contribution to the detection of pneumonia, skin disease, and cancer. Furthermore, the visualized results also corroborate the effectiveness of CoinGAN in segmenting medical objects.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper proposes a weakly supervised semantic segmentation (WSSS) method for lesion segmentation. The main contributions of the paper are two modules: one is called contrastive convolution which focuses on the discrepancies between lesion and healthy structures to reduce the uncertainties in boundaries, the second one is a dual attention mechanism called CSA which learns inter image discrepancy with adversarial training. The experiments are performed on 3 public datasets and the method is compared to generic sota WSSS methods and to methods specific for some medical images, along with the ablation studies. Additionally, the paper demonstrate that WSSS methods that work well on natural images do not perform well on medical datasets. The results show that the proposed method achieves significant improvement.

### Strengths
- The idea presented in the paper is interesting.
- The method is validated on sufficiently large datasets and compared with various SoTA methods.
- The results demonstrate that the method achieves remarkable improvement.

### Weaknesses
I think the major weakness of the paper is the unclear description and lack of some important details:
- Average buffer and SElayer are crucial components of the proposed architecture; however, the details of these components are not provided in the paper. Please explain how do these components work in detail.
- x_p and x_h used in Figure 2 are not defined in the paper. To my understanding, one of them is the pathological image and the other is the healthy one. However, my understanding brings more questions regarding the datasets used in the experiments. For example, QaTA-Cov19 is a pneumonia benchmark which does not contain healthy images. Where are the healthy images used in this experiment coming from? This question is also valid for the other datasets. Please clarify.
- It is not very clear to me how does the proposed method predict segmentation masks from image-level annotations. As far as I understand, the method converts the pathological images to the healthy ones by removing the pathologies. Are the segmentation masks obtained by taking the difference between the original image and the converted one? Furthermore, if the network introduces artifacts or blurs in the healthy regions during the conversion process, how are these false positives addressed? It's crucial to understand how the method ensures that only the anomalous regions are modified and not the healthy parts of the image, as this is a common issue with generative models.

### Questions
- How are Average buffer and SElayer components work?
- From which datasets are the healthy images used in the experiments coming from?
- How does the the algorithm predict segmentation masks from image-level annotations? Is it the region obtained after subtracting the input image and its translated version to an healthy image? If so, does this subtraction reveals any false positives? How are they removed, if any?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper presents a method for weakly supervised medical lesion segmentation. The authors make two observations about the characteristics of lesion regions in the images and propose a GAN-based method that aims to exploit these characteristics to improve segmentation quality. The method is evaluated on three public benchmark datasets and compared with several state-of-the-art baselines. The paper also includes an ablation study.

### Strengths
* The observation-based approach to design the method is interesting. From what I understood from the observations, this might be an interesting direction of research.

* The evaluation is fairly extensive, with comparisons on multiple datasets and with a number of alternative methods.

* From the results, it seems that the proposed method outperforms the other methods in the experiments.

### Weaknesses
While the ideas behind the method could be interesting and the evaluation seems fairly extensive, I must admit that I found the paper very hard to follow.

From the Introduction, the assumptions and the general idea of what the method does remain unclear to me.

* Why do we need a GAN to learn from image-level labels? If we want to classify, detect, localize, segment something, why do we need a GAN? I don't think this is explained.

* The arguments about intensity and distributions are unclear. The terms are not defined (what exactly is a "sharp and high-intensity anatomical distribution" and how does this relate to the problem?). The assumptions also seem quite specific to these datasets and applications: does a high intensity always correlate with malignancies?

* The method apparently studies a "distribution shift" that is "driven" by a "GAN-based adversarial loss function", but from the Introduction it is unclear to me what this distribution shift indicates, and how it would benefit a weakly supervised segmentation model.

The description of the method is very technical and, at least for me, did not help to clarify what the method is intended to do and how it works.

Combined with the writing and word choice, which is often vague and imprecise, I found the presentation of the paper insufficient. There may be interesting ideas in the method -- apparently, it does improve performance -- but the paper did not help me to understand what they are and how they work.

### Questions
Some suggestions for improvement, highlighting some of the parts that I found unclear:

* Page #1 (Introduction):
  > a diverse array of computer vision tasks, e.g., autonomous driving Jiang et al. (2024), robotics Panda et al. (2023) and medical diagnosis Huang et al. (2024).

  These are oddly specific references for such a general statement.

* Page #1 (Introduction):
  > On the contrary, some weak supervision alternatives, e.g., image-level labels He et al. (2024), points Gao et al. (2024), and bounding boxes Cheng et al. (2023), are effortless to obtain.

  I understand they are cheaper/easier to obtain, but they are not "effortless".

* Page #1 (Introduction):
  > Image-level WSSS is extremely challenging since these image-level labels solely indicate the presence or absence of the target object without specifying any location information.

  Doesn't that also depend on the type of label? It could be the size of the object, or the severity, for example. It doesn't have to a binary present/not present.

* Page #2 (Introduction):
  > Our insight is that medical segmentation hinges on pronounced discernible information, image-level supervision is vulnerable to some medical challenges pointing to an unstable convergence but the inherent discrepancy information encapsulated within the images can assist in further diving into the whole discriminative regions.

  I have no idea what this sentence is meant to say, or what the subfigures on the left are supposed to show.

* Page #2 (Introduction):
  > but such models may not grasp what makes medical segmentation overflow and bad uncontrollable shape.

  This is grammatically incorrect, and I find it hard to understand what is meant here. What does "overflow" mean? And "bad uncontrollable shape" of what? Uncontrollable by whom?

* Page #2 (Introduction):
  > As in Figure 1 (Right), sharp regions (high-intensity distribution) typically indicate a lesion that deviates from normal tissues (homogeneous distribution). The anomalous distribution shifts (high → low) may excavate valuable knowledge gaps.

  I have no idea what this means. Is this supposed to say that high-intensity pixels always indicate disease? (That might hold for this application, but isn't true in a general sense.)

  What are "anomalous distribution shifts" and what does it mean that they "excavate" knowledge gaps?

* Page #2 (Introduction):
  > GAN

  Why do we need a GAN to learn from image level labels? Wasn't the goal to classify, detect, or localize something?

* Page #2 (Introduction):
  > by suppressing inter-image strong-related areas and accentuating weak-related areas.

  Related to what?

* Page #2 (Introduction):
  > The CSA mechanism is designed to explore inter-image structural anomalies

  What are "inter-image structural anomalies"?

* Page #2 (Introduction):
  > Finally, a GAN-based adversarial loss function drives the distribution shift.

  Why does the distribution shift need to be driven? What does that mean? And wouldn't we want to reduce a distribution shift?

* Page #4 (Motivation & Overview):
  > The second answer is that the output structure lacks the constraints of background information, that is, the ignorance of common knowledge makes a free boundary.

  This is quite vague. What "background knowledge" and how would this "common knowledge" prevent a "free boundary" (and what is that anyway)?

* Page #5 (Contrastive Convolution (C-Conv) Module):
  > Thus we propose a new form of convolution, C-Conv, to address the above ambiguous elements.

  What "elements" does this refer to? What is an "ambiguous element"?

* Page #5 (Commonality-Specificity Attention (CSA) Mechanism ):
  > the CSA mechanism is proposed to delve into the inter-image distribution discrepancies

  The verb "delve" is really vague: what does CSA mechanism do with the discrepancies? Does it try to reduce them? Does it make them stronger? Does it use them for something else?

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
CoinGAN is designed for weakly supervised semantic segmentation (WSSS) in medical imaging. Key to CoinGAN is its use of a new convolution technique, contrastive convolution (C-Conv), and a dual attention mechanism (commonality-specificity attention.

### Strengths
The paper introduces a new form of convolution that helps accentuate fine-grained perceptual discrepancies within activation sub-maps, aiding in better delineation of lesion boundaries. A dual attention mechanism is used to suppress similarities in structural backgrounds across images while highlighting unique lesion characteristics.

### Weaknesses
1. The paper lacks a discussion on its generalizability across diverse medical imaging modalities and less common diseases.
2. The paper should provide a more detailed comparison with existing weak supervision methods, particularly those that do not use GAN architectures. Specifically, the comparison should delve into the architectural differences and training methodologies of these methods, not just reporting performance metrics.
3. The paper lacks a detailed error analysis that could help identify the specific conditions under which the model performs poorly. This analysis should include a breakdown of failure cases, such as specific lesion types or image characteristics that lead to poor segmentation.
4. In my opinion, CoinGAN's performance is not acceptable since many semi-supervised models [1] can achieve much better performance with limited annotation. The paper needs to justify the need for a weakly supervised approach when semi-supervised methods can achieve superior results with similar annotation costs.

### Questions
1. Can the model adapt to other forms of medical imaging data, such as MRI or CT images?
2. Since the author claims to use image-level annotation, I can understand that the label of the COVID dataset is normal and abnormal. However, the author needs to explain the use of the MonuSeg annotation.
3. How is the model's robustness to inaccuracies and variability in image-level labels?

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
This paper introduces a novel approach to weakly-supervised medical image segmentation that integrates C-conv for intra-image discrepancy learning, effectively reducing boundary uncertainty. Additionally, it employs CSA mechanisms for inter-image discrepancy learning. The proposed method demonstrates state-of-the-art performance across three public benchmarks.

### Strengths
The idea of utilizing two convolutional layers with different receptive fields to enhance boundary detection is intriguing. The improvement over baseline models is substantial.

### Weaknesses
1. The discussion of motivation lacks depth. Three major challenges underpin this method:
a.	The intensity distribution of pathological images differs from that of healthy images, allowing classification networks to shortcut the learning process and overlook detailed spatial information.
b.	Lesion boundaries often appear ambiguous.
c.	Images frequently share similar anatomical structures.
Regarding the first challenge, most generative method-based approaches effectively address this issue [1-4]. For the second challenge, numerous studies have integrated boundary-aware modules into medical image segmentation [5-7], yet the authors do not discussion about existing literature. Specifically, methods like BoundaryCAM [5] and those using boundary detection operators like Sobel [6] are relevant, as are boundary-aware CNN architectures [7]. As for the third challenge, it is unclear why it is categorized as a challenge in the context of this work; the presence of similar anatomical structures should be a helpful prior, not a hindrance, for segmentation.
2. As a GAN-based method, the authors primarily discuss and compare their approach with CAM-based methods, neglecting comparisons with other GAN-based or diffusion-based techniques. Additionally, the domain-specific baselines referenced in the paper appear somewhat outdated. The lack of comparison with recent diffusion models, which have shown promise in weakly supervised segmentation, is a significant oversight.
3. The paper is not easy to follow. Especially the method part, which is difficult to understand and contains numerous ambiguities and unclear points (refer to the questions for specifics). The descriptions of the C-Conv module and the CSA mechanism lack sufficient detail, making it hard to grasp their precise functionality and interaction.

### Questions
1.	From my understanding, C-Conv detects the boundary and subsequently removes the local representation at that boundary. Could this lead to a loss of valuable information? Additionally, might this approach impact boundaries of certain sturctures within the foreground or background, not just the boundary between the foreground and background?
2.	In 272, what is the size of the reference samples and how they are selected and dynamically replaced?
3.	What distinguishes the proposed average buffer from traditional prototypes or memory banks?
4.	It seems that the generator only produces latent representations of the healthy distribution. How are the segmentation mask and the transformed healthy modality in Figure 6 generated?

### Soundness
2

### Presentation
2

### Contribution
2

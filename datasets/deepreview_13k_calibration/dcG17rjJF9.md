# Large Language Model for Lossless Image Compression with Visual Prompts

- Decision: Reject
- Avg Score: 5.67
- Scores: 8, 8, 5, 6, 6, 5, 5, 3, 5

## Abstract
Recent advancements in deep learning have driven significant progress in lossless image compression. With the emergence of Large Language Models (LLMs), preliminary attempts have been made to leverage the extensive prior knowledge embedded in these pretrained models to enhance lossless image compression, particularly by improving the entropy model. However, a significant challenge remains in bridging the gap between the textual prior knowledge within LLMs and lossless image compression.
To tackle this challenge and unlock the potential of LLMs, this paper introduces a novel paradigm for lossless image compression that incorporates LLMs with visual prompts. Specifically, we first generate a lossy reconstruction of the input image as visual prompts, from which we extract local and global features to serve as visual embeddings for the LLM. The residual between the original image and the lossy reconstruction is then fed into the LLM along with these visual embeddings, enabling the LLM to function as an entropy model to predict the probability distribution of the residual.
Extensive experiments on multiple benchmark datasets demonstrate our method achieves state-of-the-art compression performance, surpassing both traditional and learning-based lossless image codecs. Furthermore, our approach can be easily extended to images from other domains, such as medical and screen content images, achieving impressive performance. These results highlight the potential of LLMs for lossless image compression and may inspire further research in related directions.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors address the problem of lossless image compression by proposing a framework that leverages a Large Language Model as the entropy model to estimate the distribution of residuals between the original image and its lossy-compressed counterpart. Extensive ablation studies demonstrate the framework’s advantages over previous methods.

### Strengths
Building on previous work that uses Large Language Models (LLMs) as entropy models for lossless compression, the authors argue that the limited performance gains over traditional (non-learning-based) methods stem from differences between the textual features captured by pre-trained LLMs and the intrinsic characteristics of image pixels. To address this, they propose inputting visual embeddings into the LLM to enhance performance. The concept is clearly presented, the argument is compelling, and the experiments are thoroughly conducted.

### Weaknesses
The authors acknowledge the time-consuming nature of their proposed approach. However, it is important to note that this issue arises not only from the autoregressive structure of the method but also from the additional computational load introduced by the visual embeddings compared to previous approaches. A comparison of this aspect would be insightful. The authors also address the role of lossy compression within the framework. They conducted an ablation study on the quantization parameter of BPG for lossy compression, showing that this parameter does not affect the overall performance. However, further explanations of this effect would be valuable.

### Questions
N/A

### Soundness
3

### Presentation
4

### Contribution
4

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
The authors present a system that utilizes the pattern recognition ability of LLM's to extract accurate probability models to perform lossless entropy coding of real world images. To improve the performance, they introduce a host of methods and tricks, following it up with appropriate ablations. This results in a system that beats standard methods like PNG, JPEG-XL in image compression.

### Strengths
- Instead of directly encoding the image pixels like previous works in this domain, they use off the shelf lossy compression models and encode their residuals. To achieve this, they obtain embeddings for the entire image (global), patches (local) and use it as "prompts" to the language model, along with a GMM (Gaussian mixture model) to accurately model the underlying distribution.
- The proposed system might appear to be a hodge·podge of different tricks, but each one contributes meaningfully towards arriving at the solution. This is highlighted in their extensive ablation study.
- The flow of the paper is good. I like the simplicity of the approach - with no unnecessary additions or jargon which has become the bane of our community.

### Weaknesses
 - The most obvious weakness of such a system would be the required compute. Hence, I think a mention about the MACs for encoding and decoding would be good. I wonder if the authors tried any Quantized LLM's for this task - something that is known to be small and occupy much smaller footprints. Eg: [Phi 3 mini](https://huggingface.co/QuantFactory/Phi-3-mini-128k-instruct-GGUF) or even [BitNet](https://github.com/microsoft/BitNet).
- For a system that relies on an LLM for most of the heavy lifting, I am a tad bit disappointed to not see a study that ablates on them. I am particularly intrigued if there is any correlation between LLM size and their encoding ability.
- On similar lines, I would love to see ablations on image encoding as well. It would be helpful to try out different image encoders, starting with something basic like JPEG.

### Questions
Is there a particular reason for choosing BPG as the image encoder, when you could have started with something cheap like JPEG (maybe at quality 50) ?

### Soundness
3

### Presentation
3

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
This paper presents a lossless image compression method that utilizes an LLM for entropy coding. Specifically, it employs a two-layer design where the first layer encodes the input image using lossy compression. The residual between the original image and its lossy reconstruction is then losslessly coded in the second layer using the LLM as an entropy model, with the lossy reconstructed image generating visual prompts for the LLM. To enable the LLM to better handle the distribution prediction task for entropy coding, LoRA is adopted to adapt the pre-trained LLM model.

### Strengths
Using LLMs for entropy coding in image compression is a relatively new topic. Experimental results show that the proposed method achieves better coding performance compared to the prior work that also adopts LLMs for entropy coding.

### Weaknesses
1. According to Table 2, it appears that after applying the global prompt, the additional improvement from using the local prompt is minimal, providing only a 0.8% gain. Furthermore, although the paper emphasizes the importance of optimized embedding, Table 2 shows it provides only a modest 0.4% additional gain.

2. The comparison of complexity with baseline methods (e.g., model size, encoding/decoding MACs, or runtime) is not provided.

3. The practicality of using an LLM as an entropy model is questionable, as the complexity is significantly higher than that of traditional codecs in all aspects. Furthermore, according to Tables 1 and 3, without adopting LoRA, the coding performance of the proposed method is only on par with JPEG2000, achieving better performance only with LoRA. However, LoRA fine-tuning is not novel and it also makes the LLM task-specific. As shown in Section 4.4, unlike the baseline method by Delétang et al., which does not require retraining, this approach lacks generality and necessitates retraining of the introduced components for different data domains, resulting in increased training time and storage demands.

### Questions
1. In Table 1, the authors mention that they reimplement the method from Delétang et al. However, why is only the Kodak dataset's result provided in Table 1? What about the results for the other three datasets?

2. It is unclear why ImageNet2012 is used for training stage 1 while DIV2K is used for training stage 2, rather than employing the same dataset throughout.

3. The motivation of using GMM is unclear. Typical learned image codecs usually utilize Gaussian distribution.

4. The model appears to be trained using 16x16 patches. Would the performance improve if the training patch size were increased?

5. It would be interesting to report results with lower or larger QP values. For instance, if the lossy branch utilizes an extremely low number of bits, resulting in poor quality of the lossy image and significant loss of original image information, can the total still remain at 3.2 bpsp? How much information can the visual embedding provide in that scenario?

### Soundness
3

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
2

### Summary
The paper proposes to update the framework for LLM conditioned image compressions with an image or vision embedding that is fed also to the LLM, resembling in the "An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale", https://arxiv.org/abs/2010.11929. The paper argues gains at the range of +34% when optimized embeddings and both local/global prompts are employed.
The model optimizes the joint entropy to measure the discrepancy between estimated and original (reference) signal. The model is trained in two stages and LLaMA3-8B is used for the language model. The first stage of training leverages ImageNet2012 with freezed LLMs and for the second stage the LLm is tuned using Lora. The model is evaluated on DIV2k, CLIC mobile validation, CLIC pro and kodak images datasets. The proposed method shows superior performance to the baseline methods.

### Strengths
The paper is well organized and well-written.
The experiments considers various perspectives including an ablation study.
The formulation and idea is relatively simple and straight forward.
The architecture is very similar to transformer-based encoders for image and video coding

### Weaknesses
Looks a bit incremental and confusing with transformer based architectures for visual data.

### Questions
- How does the method compares to JPEG-AI?
- The architecture resembles a transformer based methods for visual data coding, could you elaborate the differences?

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
3

### Summary
In this submission, the authors present a method for lossless image compression with LLMs. The main difference between the proposed one and existing LLM-based method (Deletang et al. 2023) lies in the input to LLM. Specifically, the authors show that supplying visual prompts, i.e., a lossy reconstruction, to the LLM for fine-tuning its compression capacity on the probabilistic modeling of residuals is helpful for the performance, leading to an advantage compared to modern and NN-based lossless image compression frameworks.

### Strengths
1. The design of supplying visual prompts and modeling only residuals is interesting and reasonable. Modeling residuals is usually easier.
2. The performance gain over the baseline is obvious. And the effectiveness of main designs, e.g., global and local prompts, embedding optimization, is proven to be positive through ablation results.

### Weaknesses
1. Although the experiments results on DIV2K, CLIC, Kodak are promising, the number of training images (DIV2K train split) seems limited to me. Is the method still effective if we try to extend it to larger datasets, e.g., ImageNet?

2. Since the results of the main competitor (Deletang et al. 2023) are reproduced on Kodak benchmark, why are the results are missing on other evaluation datasets?

3. How does the model size influence the compression rate? According to Deletang et al. 2023, the model size influences the compression rates in a non-monotonous way.

### Questions
1. How does the method perform on larger datasets?

2. Why the results on other evaluation benchmarks are missing for Deletang et al. 2023.

3. A chart like Fig. 2 in Deletang et al. 2023 is appreciated to show the trend of compression rates versus model size.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 6

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper presents a framework for lossless image compression by leveraging Large Language Models (LLMs) combined with visual prompts. The approach generates a lossy reconstruction of an input image, extracts local and global visual features from this as prompts, and uses the LLM to predict the probability distribution of residuals for entropy coding. This visual prompt-based strategy allows LLMs to perform better on image compression tasks, even outperforming traditional codecs and several state-of-the-art learning-based methods. The framework shows notable adaptability across different image types, including medical and screen content images, demonstrating its generalization capability.

### Strengths
1. The paper explores a unique application of LLMs in the field of image compression, addressing the challenge of adapting LLMs from their textual foundations to image processing.
2. Incorporating lossy reconstructions as visual prompts effectively bridges the gap between textual and visual data, enhancing the LLM’s ability to predict distributions in image compression.
3. The method is validated on multiple datasets (DIV2K, CLIC, Kodak), achieving state-of-the-art compression performance. 
4. Extensive ablation studies clarify the contributions of visual prompts, embedding optimization, and finetuning (using LoRA), offering a thorough analysis of each component’s impact on compression efficacy.

### Weaknesses
1. The pixel-by-pixel autoregressive encoding process is time-consuming, potentially limiting practical applications where computational efficiency is critical.
2. The framework’s performance is influenced by the choice and quality of the initial lossy codec. While BPG is used by default, there may be variability in performance if alternative lossy codecs are applied.
3. The proposed method’s reliance on large models and multiple GPUs could hinder scalability, especially for use cases in resource-constrained environments.
4. The code of "Large Language Model is Compression" is released. Why the auther use the reproduced preformance as the baseline?

### Questions
See weakness.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 7

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents an approach to lossless image compression by integrating Large Language Models (LLMs) with visual prompts to enhance compression performance. Traditional lossless compression techniques, also those based on deep learning, struggle to utilize the rich prior knowledge in LLMs, which is predominantly textual. This study mitigates this limitation by introducing a framework that combines lossy image reconstructions as visual prompts to the LLM, which are used to extract local and global visual features. These features, alongside the residuals between the original and lossy images, guide the LLM in predicting probability distributions for the residuals, effectively functioning as an entropy model.

### Strengths
- The research direction *LLM-based image compression* is interesting. 
- From the experimental results, the proposed method did achieve SOTA compression performance.

### Weaknesses
 - Although the proposed method demonstrates improved performance, its design elements appear largely incremental, limiting the overall novelty. From the paper’s descriptions, the main factor contributing to the superior results over [1] seems to be the retraining of modules within the LLM, whereas [1] uses these modules in their pretrained state.
- Following this, it remains unclear what the primary differences are between this method and that of [1]. Although the authors briefly mention where [1] differs, they do not provide enough detail for readers to clearly distinguish their approach from prior work.
- Regarding Figure 2, how does the Decoder process unfold? Couldn’t we use the bits encoded by the Arithmetic Encoder directly, then decode them using the Arithmetic Decoder, and simply add the decoded residual to the lossy reconstruction to obtain the final image? It’s unclear why the lossy image and patches need to be passed back through the LLM in the Decoder. Additionally, the purpose of the dotted arrows in the figure could be clarified, as the visual explanation is somewhat confusing.
- How well is the proposed method expected to generalize across different datasets? For instance, if the LLM is fine-tuned on dataset A, how does it perform when applied to compress images from dataset B?
- Why was a large language model (LLM) chosen instead of a vision-language model? Given the fundamental differences between text and image modalities, it seems questionable to use an LLM trained solely on text data to handle image compression.

### Questions
Please refer to the weakness part above.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 8

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper introduces a LLM-based entropy model for lossless image compression. Specifically, it adopts the notion of scalable coding to encode an input image into a base layer and an enhancement layer. The base layer is coded in a lossy manner using BPG while the enhancement (residual) layer is coded losslessly with the proposed LLM-based model. Its key contribution lie in learning visual embeddings tailored for image compression.

### Strengths
(1) The idea of using LLM for entropy coding is novel and presents a new research direction. 

(2) The ablation studies are extensive and complete, showing the potential of LLM for lossless image compression in various domains, including natural, screen, and medical image content.

### Weaknesses
(1) It is unclear how much gain the lossy base layer contributes to the final coding performance, although the authors argue with the results in Table 4 that the base layer has a limited impact. But, I doubt this is true. What if there is no base layer at all? The performance of the proposed method without the base layer needs to be explicitly evaluated, as the current results do not sufficiently isolate the contribution of the LLM-based lossless coding component. The choice of QP for the base layer is also a concern, as an inappropriate QP could significantly impact the performance of the overall system. The authors should provide a more thorough analysis of the interaction between the base layer QP and the final coding performance.

(2) Obviously, querying a LLM is not cheap. The decoding time and MAC/pixel are not presented. The computational cost of the proposed method is a significant concern, especially given the use of a large language model. Without a detailed analysis of the encoding and decoding time, as well as the computational complexity in terms of MAC/pixel, it is difficult to assess the practical feasibility of this approach. The authors need to provide a comprehensive evaluation of the computational overhead associated with their method.

(3) If the LLM is not fine-tuned (i.e. LoRA is not applied), the proposed method (bpsp = 3.19) performs only comparably to JPEG 2000 on the Kodak dataset (and worse than some traditional codecs). Turing the LLM into a specific entropy coding model does not sound practical. The practical utility of fine-tuning a large language model for a specific task like image compression is questionable. The authors should discuss the implications of this approach, considering the computational resources required for fine-tuning and the potential limitations of a task-specific LLM.

### Questions
(1) In Table 4, I wonder how the proposed method would work if there is NO base layer at all. 

(2) From Table 2, it appears that the major coding gain of the proposed method comes from providing the LLM with local and global prompts. In the variant with "disabled optimized embeddings" (gain=-33.7%), I wonder if the visual embeddings z_g and z_l still need to be learned and optimized. Moreover, from the same table, additionally optimizing embeddings offers rather limited gain. This appears to contradict the claim that learning better embeddings for the image compression task is essential. It is unclear what embeddings are additionally optimized. Does the setting "Optimized Embeddings" refer solely to the "residual embedding layer"? This needs to be clarified. 

(3) In Table 2, it is counterintuitive that global prompts bring more gain than local prompts. Local prompts should ideally capture better local statistics. 

(4) In Figure 1, the proposed method has two types of embedding layers: the textual and visual embeddings. What are the differences between these two. Does the textual embedding refer to the embedding needed to convert a residual sample into z_r? This part is rather ambiguous.  

(5) Since the input image encoded by the LLM is a residual image, the samples of a residual image usually have an uni-modal distribution. The necessity of GMM is questionable. 

(6) The decoding time (or even the kMAC/pixel) of the proposed method should be compared with that of the competing baselines. 

(7) In Table 1, the results without LoRA should be included. Applying LoRA to fine-tune LLM would turn the LLM into a specific entropy coding model for coding images. In Deletang et al, the LLM does not appear to be fine-tuned. Fine-tuning LLM to make it a specific one for image coding does not sound practical.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 9

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This work leverages LLM for lossless image compression. The main contribution is the visual prompts with global and local information for LLM. The lossy reconstruction encoder-decoder is introduced to generate lossy reconstruction embeddings and residual embeddings in residual compression. The proposed method works well on several benchmark datasets and can also be applied to other image domains such as screen content images and medical images.

### Strengths
1. The method combines traditional lossy reconstruction and LLM, showing an effective way for lossless image compression. 
2. The results look good, the proposed method outperforms all other works across different datasets.

### Weaknesses
1. The main contributions of this paper are the visual prompts of lossy reconstruction and the residual compression via LLM, both of which use only existing techniques (e.g., visual prompts and LoRA) and thus the novelty is limited. Moreover, I didn't see the "visual prompts" module in all figures, please clarify it in at least one of these figures.
2. What is the arithmetic coding? The authors should provide some background on it (or at least add it somewhere in the appendix). Otherwise it would be very confusing for people who haven't worked in this area.
3. The proposed method requires an additional lossy encoder-decoder in compression, which increases the training cost and also lowers the inference time. The authors should provide a comparison of model complexity and training/inference time.
4. How do you design the Residual embedding layer? Pixel values as indexes or other ways? Please clarify it in Sec.3.1, Line 250-251. In addition, what's the mean of "use pixel values as indexes", is that an image histogram embedding?
5. Although this method introduces the spatial information as a part of embeddings for LLM, the output is still a 1-D distribution. Maybe the authors can extend it to 2-D spatial distribution and optimize it with 2D entropy?
6. By introducing BPG as the lossy reconstructor, this method seems to have an additional compression vector (i.e., larger bits than other models). The experiments might be unfair. The authors should explain more about it.
7. It's unclear why increasing the quantization parameter (QP) in BPG leads to higher bit-per-pixel (bpsp) for residual compression, as shown in Table 4. A larger QP should reduce the complexity of the residual, not increase it.
8. The comparison in Table 1 is insufficient. Since the method of Deletang et al. is non-trainable, a more appropriate baseline would be a version of that method fine-tuned for image compression, which would provide a fairer comparison for the proposed approach.

### Questions
1. In Figure 1, the existing LLM-based pipeline doesn't have trainable parameters. It seems strange because most visual embeddings are not naturally aligned with text embeddings in LLMs.
2. In Table 1, the method proposed by Deletang et al. performs the worst. Why?
3. In Table 2, the Global prompt seems to be the most effective component. Can the authors also show the cosine similarity of global embeddings in Figure 4?

### Soundness
2

### Presentation
3

### Contribution
2

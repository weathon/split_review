# ElasticTok: Adaptive Tokenization for Image and Video

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6

## Abstract
Efficient video tokenization remains a key bottleneck in learning general purpose vision models that are capable of processing long video sequences. Prevailing approaches are restricted to encoding videos to a fixed number of tokens, where too few tokens will result in overly lossy encodings, and too many tokens will result in prohibitively long sequence lengths. In this work, we introduce ElasticTok, a method that conditions on prior frames to adaptively encode a frame into a variable number of tokens. To enable this in a computationally scalable way, we propose a masking technique that drops a random number of tokens at the end of each frames's token encoding. During inference, ElasticTok can dynamically allocate tokens when needed -- more complex data can leverage more tokens, while simpler data only needs a few tokens. Our empirical evaluations on images and video demonstrate the effectiveness of our approach in efficient token usage, paving the way for future development of more powerful multimodal models, world models, and agents. Video examples of using ElasticTok can be found on our website: 
\href{http://largeworldmodel.io/elastictok}{largeworldmodel.io/elastictok}

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
- The paper presents an approach to dynamically assign different number of tokens per different image/video depending on the input complexity.
- During training, a random mask is applied to the encoded image tokens, and the unmasked tokens are used to reconstruct the image. - For training the video pipeline, similar random masking is applied at per block (stack of 4 images) levels, with the masking function being independent per block.
- During inference, an iterative search is performed over a different number of tokens to be masked, and the max mask that satisfies the required constraint (reconstruction loss < target reconstruction loss) is selected.
- Interesting results – analyzing the performance of image/video reconstruction quality and fine-tuned VLM performance at different token counts.

### Strengths
- The paper studies an interesting topic of adaptive tokenization for images and videos. As mentioned, such adaptive tokenization is crucial for long-context tasks.
- While similar adaptive and compression architectures have been studied in the past, the application to auto-encoding of images and videos is a novel contribution. Related works in adaptive representations and compression are well covered.
- Results include interesting analysis of token requirement for reconstruction and VLM tasks.

### Weaknesses
 - The paper writing needs improvement –
    - **A background section on Ring attention** (Liu et al., 2024b) paper should be the first paragraph of the method section since Ring attention is a big component of the proposed approach. Most important are the **details of the autoregressive video model**.
    - Algorithm 1 and 2 says variable "x" (output of PatchifyRearrange) shape is B $\times$ L $\times$ D, what exactly is L ? From the next line ($N_b$ = the number of blocks), it seems that "x" should be of shape: B $\times$ ($\frac{L}{B}$) $\times$ D i.e. number of tokens per block $\times$ number of blocks $\times$ feature dim. Please clarify this and **define all variables**.
    - The captions of Tables 1 and 2 and the corresponding paragraph writing can be improved. It seems that table 1 is for image dataset and table 2 is for video dataset, but this is not mentioned anywhere. Please clarify and **fix these writing issues**.

- Questions regarding masking strategy: Encoders / Tokenizers like VAE and VQGAN map tokens to patches and also assign 2D positional encodings to each patch. Thus, in some sense, each token (although captures enough receptive field via convolution or self-attention) is responsible for the reconstruction of the corresponding patch. Architectures like MAE mask random patches/tokens, performing a local task of inpainting (because at least some token is unmasked in the vicinity of a masked token). But the proposed approach always masks the leftmost tokens meaning that a fixed section of the image is always masked, irrespective of the content complexity of that particular section of the image. This raises questions on the choice of masking and doubts about the efficacy of the trained model. Visualizing what the leftmost tokens capture could help understand the issue. Details about position encodings would also be great.

- Does the encoder take the sampled mask as input? While the text says so, the architecture figure shows that the mask is applied after full-length encoding.

- For image reconstruction, searching for the mask at inference time makes sense, but for video level, searching for masks seems too computationally expensive. The only possible approach seems neural regressive in that case. More details on the neural regression approach would be great, including details on whether the neural masking approach is independent per frame, or it takes into account the context like the autoregressive video encoder.

- For video training, independent per-block mask sampling will lead to a combinatorially large number of masking choices per video, with a majority of them being not very useful for training. For example, strong masking of the first frame, and no masking of the immediate next frame might be a waste if there is no motion from one frame to another. Thus, a next-frame masking strategy should also have better inductive biases in order to train larger models efficiently.
- More details about the video dataset will be great. Will the exact video dataset be released to support the reproduction of the proposed approach?
- It seems that all paper results are from the continuous model. Results or ablations from the quantized FSQ model would be appreciated.

Initially, my understanding—due to the lack of masking details in the original submission—was that the encoder learns fixed-length embeddings, which are later masked. Therefore, as the authors mentioned in the related work, ElasticTok appeared to be an application of the Matryoshka approach to image/video reconstruction.

However, based on the authors’ latest response, it seems the encoder is run repeatedly for different sampled masks at test time. This approach appears highly inefficient and results in wasted computational flops (doesn't seem a scalable approach for video going forward, if for each frame the whole encoder needs to be run again and again to find optimal mask).

Why not adopt a single embedding, as in the Matryoshka approach, and perform masking directly on the encoded output? This would serve as an important baseline for comparison, and I would appreciate it if the authors could provide results for this approach.

### Questions
My main concern are weakness points highlighting lack of clarity or details over the left-most token masking strategy. This raises concerns regarding efficacy of the trained model. But I feel the authors should be able to address this easily both in text and by visualizing the tokens.

The second concern is that independent per frame or per block masking strategy doesn't seem to be a scalable or efficient training approach. Intuitive understanding of the authors and maybe some statistics of the masking done during training could help alleviate these issues.

Rest, writing should be improved and this should be also fixable.

### Soundness
3

### Presentation
1

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes ElasticTok, a method for adaptive image/video tokenization that encodes visual data into variable-length tokens.  During training, the method drops a random number of tokens at the end of the token encoding. During inference, ElasticTok can use a variable length of tokens according to the need. Experiments show the advantages of the proposed method compared with the baseline.

### Strengths
1. This paper proposes an effective way to compress the number of tokens adaptively.

2. The length of used tokens aligns well with human intuition: when the image is more complex, more tokens are used.

3. The proposed method can effectively represent long videos with up to 2-5x fewer tokens.

### Weaknesses
1. Lack of comparison. The proposed method should be compared with other state-of-the-art token compression methods considering the compress rate, reconstruction quality, and downstream task performance. Specifically, the paper should benchmark against methods that employ learned compression techniques, such as those based on vector quantization or other forms of latent space compression, not just fixed-length tokenizers. It is important to understand how ElasticTok performs relative to methods explicitly designed for compression, not just against standard tokenization baselines.

2. Loss of details in reconstruction. From the demos, the reconstruction quality is not very satisfactory. For example, the loading icon on the cellphone has totally disappeared/distorted. This suggests that the method may be discarding important high-frequency information during the tokenization process. A more rigorous analysis of the types of details lost, and under what conditions, is needed. The paper should also explore whether this loss of detail impacts downstream task performance.

3. More analysis of the drop in image quality when using the elastic token compression is desired. Consider measuring the quality drop between the original image and the reconstructed image using PSNR/SSIM. Furthermore, the paper should investigate how the degree of compression (i.e., the number of tokens dropped) correlates with the degradation in reconstruction quality. It would be beneficial to provide a curve or table that shows this relationship, allowing readers to understand the trade-off between compression and quality.

### Questions
See Weakness. 

Besides, the applications of elastic token compression are still not so convincing to me. Are there more applications that clearly benefit from using elastic token compression than from using other compression methods?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a video representation learning approach that learns a compressed representation via an autoencoder. Randomly dropping the last few tokens of each frame during training encourages important information to stay in the first few tokens. This allows users to dynamically adjust the number of tokens used during inference, balancing the trade-off between faster inference and higher output quality based on the task's requirements.

### Strengths
Exploiting temporal coherence to learn a more compact video representation is a well-motivated problem.
Figure 4 does indeed show that the dropout strategy can reduce the number of tokens as intended, although it requires a computationally exhaustive search to find the right number of tokens for each frame.

### Weaknesses
The "neural regression" evaluation (Table 4) does not seem very helpful. If I understand correctly, the error rate is the rate the regressor failed to correctly predict the optimal number of tokens found by the exhaustive search. It would have been good to also show the reconstruction accuracy. Also it would have been good to show the total inference time or FLOPS for each search method. It can be architecture-dependent but how much computation can be saved using fewer tokens in the decoder should be more carefully presented considering claims about efficient computation. The paper lacks a clear analysis of the trade-off between the computational cost of the regressor itself and the savings it provides in terms of reduced token processing. The computational overhead of the regressor, especially during inference, needs to be quantified and compared against the gains from using fewer tokens. Furthermore, the evaluation of the regressor's performance is limited to predicting the number of tokens, without assessing the quality of the resulting representation when using the predicted token count. It's crucial to evaluate how the regressor's errors impact the downstream task performance, not just its ability to match the exhaustive search.

### Questions
I think it might be helpful to mention which search method was used for each evaluation (e.g. in Figure 4). I was assuming exhaustive search was used for most if not all of them.

I could not find details on how the regressor is fine-tuned. Does it see the context of the entire video? Does the regression loss change the encoder weights?

Experiment suggestion: a heuristic-based regressor baseline (e.g. use the amount of motion as a proxy to determine the number of tokens needed)

Citation suggestion: "Adaptive Computation Time for Recurrent Neural Networks" by Alex Graves

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
3

### Summary
This paper presents a method to encode images or videos with variable length tokens which can then be decoded in a manner that minimizes a reconstruction loss (or any other target loss). This is achieved by dropping (or masking) some portion of tokens during training and inference. The method assumes a fixed maximum token length l and chooses to use the first k (k<=l) tokens for encoding purposes. In case of longer videos, a block processing mechanism is adapted where a different number of tokens are used for each block.

### Strengths
- The idea of using adaptive token lengths for image/video encoding (or other sequential data) is valid especially since there is a desire to generate/analyze longer sequences of data.
- The paper is well written, it's easy to follow. The authors have also shared code.
- Provided experiments are reasonable with each experiment evaluating a clear aspect of the proposed approach.

### Weaknesses
 - For me the biggest limitation of the method seems like although the paper claims to "adaptively" select the number of tokens given the input, it seems the current proposed strategies (e.g., binary search, trying to match a threshold etc.) still require various computation and hence might limit the applicability in certain scenarios. For example, adaptive token lengths might potentially be most useful in long generation tasks but it's not clear yet how one can adaptively decide how many tokens to generate. Specifically, the overhead of determining the optimal k for each input, especially with methods like binary search, could negate the benefits of reduced token usage, particularly in real-time applications or when dealing with very long sequences. The paper does not sufficiently explore the computational cost of this adaptive selection process, nor does it provide a comparative analysis against fixed-length encoding with similar computational budgets.
- As the authors also mention in their limitations, the current masking strategy is pretty naive in the sense that it always uses the first k tokens. This may or may not be ideal depending on the input content. The reliance on left-aligned masks is a significant limitation, as it assumes that the most important information is always located at the beginning of the sequence. This is unlikely to be true for complex visual data, where crucial details might be distributed throughout the sequence. The method lacks a mechanism to identify and prioritize the most informative tokens, potentially leading to the loss of critical information when tokens are dropped.

### Questions
For Fig.4 comparisons, do the authors first search for the ideal token length for each input for their method?

In Table3, if I understand correctly the baseline is trained with 50% of tokens and the method is trained with varying number of tokens. How is the inference done? Do both methods use 50% of tokens during inference?

### Soundness
3

### Presentation
3

### Contribution
2

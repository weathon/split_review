# LANTERN: Accelerating Visual Autoregressive Models with Relaxed Speculative Decoding

- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 6, 6, 8

## Abstract
Auto-Regressive (AR) models have recently gained prominence in image generation, often matching or even surpassing the performance of diffusion models. However, one major limitation of AR models is their sequential nature, which processes tokens one at a time, slowing down generation compared to models like GANs or diffusion-based methods that operate more efficiently. While speculative decoding has proven effective for accelerating LLMs by generating multiple tokens in a single forward, its application in visual AR models remains largely unexplored. In this work, we identify a challenge in this setting, which we term \textit{token selection ambiguity}, wherein visual AR models frequently assign uniformly low probabilities to tokens, hampering the performance of speculative decoding. To overcome this challenge, we propose a relaxed acceptance condition referred to as LANTERN that leverages the interchangeability of tokens in latent space. This relaxation restores the effectiveness of speculative decoding in visual AR models by enabling more flexible use of candidate tokens that would otherwise be prematurely rejected. Furthermore, by incorporating a total variation distance bound, we ensure that these speed gains are achieved without significantly compromising image quality or semantic coherence. Experimental results demonstrate the efficacy of our method in providing a substantial speed-up over speculative decoding. In specific, compared to a na\"ive application of the state-of-the-art speculative decoding, LANTERN increases speed-ups by $\mathbf{1.75}\times$ and $\mathbf{1.76}\times$, as compared to greedy decoding and random sampling, respectively, when applied to LlamaGen, a contemporary visual AR model. %in greedy decoding and from $0.93\times$ to $1.64\times$ in random sampling,

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
In this paper, the authors propose LANTERN, a sampling strategy to speed up the image generation without losing too much quality. The method is implemented by accumulating probabilities from nearby tokens of the current sampling token. The authors further propose a thresholding technique to prevent the accumulated distribution deviating too much from the original one. Experiment results seem to be effective, however, the analysis is intuitive and empirical without deep insights.

### Strengths
- The proposed method is intuitive and easy to follow.

- Experimental results seem to verify the proposed method in terms of speeding up image generation without significant quality loss.

### Weaknesses
 - There is a gap between the introduction and methodologies in writing. The related works are deferred to the appendix and problem definition and preliminaries such as Speculative Decoding are missing, resulting in difficulties in understanding the problem and challenge for readers who are not exactly working on this domain. On the other hand, Section 2.1 and 2.2 have some overlaps about the experiments and observation, which can be more concise.

- The evaluation seems to be insufficient. For the testing data, it is ideal to use the same setting as the vanilla baseline (i.e., LlamaGen) rather than just 100 captions from MSCOCO. The statement “Since measuring speedup with more than 100 samples shows no significant difference, we use 100 captions for efficiency” is not very convincing to me. In addition, other models are suggested for evaluation as well including other variations of LlamaGen.

- Some analyses in experiments are not sufficient. In sampling, the authors only mentioned that when $\delta$ is small, using larger k results in speeding up without significant degradation in performance, yet the reason for it is less explored. Section 4.3.2 also lacks further analysis why using TVD is better than JSD except some empirical results.

### Questions
- See the weakness.
- The claim of interchangeability in Section 3.1 is only empirically explored via a few examples. Are there some theoretical insights or statistics supporting this claim?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The work presents a novel approach to enhance the efficiency of image generation using Auto-Regressive (AR) models, which traditionally suffer from slow sequential processing. The authors introduce LANTERN, a method that leverages speculative decoding with a relaxed acceptance condition to significantly speed up inference while maintaining image quality. By utilizing a smaller drafter model to predict multiple tokens simultaneously, LANTERN addresses the challenges of token selection ambiguity inherent in visual AR models. The results demonstrate notable improvements in speed and efficiency compared to baseline methods, highlighting the potential of LANTERN to advance the capabilities of AR models in generating high-quality images.

### Strengths
The methodology of this paper is clear and comprehensible, and the research question it addresses is interesting. Although the overall approach is relatively straightforward, I believe the findings are still valuable.

### Weaknesses
1. My primary concern is that the paper lacks an evaluation of the image generation quality. The authors present several generated images, but these images are stylistically very similar and exhibit poor consistency with the accompanying generated text. Some images even contain clear visual errors. I recommend that the authors conduct a more comprehensive assessment of image generation quality to better demonstrate the effectiveness of the proposed method.

2. The problem the paper aims to address is the low Mean Accepted Length that occurs when applying speculative decoding to AR image generation models. Specifically, although speculative decoding is used, a large number of predictions generated by the lightweight model are rejected, forcing the larger model to regenerate many tokens. As a result, the expected efficiency gains from speculative decoding are not realized. While the authors present a complete exploration from two perspectives, I still feel that, given the inherent ambiguity in token selection, improving the acceptance rate alone might suffice. A large set of tokens could be considered acceptable. This raises the question: Is speculative decoding still necessary in such a case? What would the quality and efficiency be if tokens were instead randomly generated within certain constraints?

### Questions
Please see the weaknesses.

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
3

### Summary
This paper proposed speculative decoding for AR Image generation, AR models tend to assign uniformly low probabilities across a wide range of tokens, making it difficult to select the most appropriate token during decoding.

To solve this problem, the author introduce LANETERN (Latent Neighbor Token Acceptance Relaxation), leveraging the interchangeability of the tokens and relaxing the acceptance for decoding. 

The benefits of LANETREN can be found at generating speed with comparable quality.

### Strengths
1. The motivation behind the author’s proposed approach is straightforward: in standard sampling processes, an excessively high token rejection rate can significantly slow down generation. The author suggests a more relaxed policy to mitigate this issue, thereby improving generation speed.

2. To mitigate the distributional shift introduced by the lenient sampling approach, the author proposes a constraint rule for sampling based on total variation.

3. Through extensive ablation experiments, the author demonstrates how the lenient sampling scheme influences sampling speed and elucidates the specific roles of various hyperparameters within this scheme.

### Weaknesses
My main concern lies in whether the metrics employed in the experimental section sufficiently capture the effectiveness of the proposed approach, particularly in Table 3 and Section 4.2.3. For evaluating basic generation quality, would it be possible to provide precision and recall (P/R) instead of FID? This change could allow for a clearer view of how LANTERN and limited distribution divergence affect and restore distribution. Additionally, since LlamaGen is used as the base model, could the authors include some modern image quality scores, such as PickScore or HPS, to better quantify aesthetic quality loss?

In summary, the author presents a promising sampling scheme for AR models, which improves sampling speed at the cost of some image quality.

The primary concern is that the author’s experiments lack sufficient evidence to demonstrate that the loss in image quality is within an acceptable range. Given this limitation in quality, I believe the impact of the work may be constrained. Therefore, I am inclined to recommend rejection.

### Questions
see weakness. 

In summary, the author presents a promising sampling scheme for AR models, which improves sampling speed at the cost of some image quality.

The primary concern is that the author’s experiments lack sufficient evidence to demonstrate that the loss in image quality is within an acceptable range. Given this limitation in quality, I believe the impact of the work may be constrained. Therefore, I am inclined to recommend rejection.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper tackles the challenge of transferring speculative decoding from LLMs to autoregressive image generation models. The authors observe that the nature of image data causes image tokens to exhibit selection ambiguity, resulting in high rejection rates and poor acceleration effects in speculative decoding. Hence  they propose using the proximity set of image tokens as proxies to speculate on accepting a predicted image token, and introduce a combinatorial optimization strategy for selecting the set to ensure image quality remains intact.  Extensive experiments confirm significant acceleration with minimal quality loss.

### Strengths
The paper's structure and presentation are well-crafted. It identifies the phenomenon of "token ambiguity" and provides a viable solution. Extensive experiments, particularly the ablation studies, demonstrate the effectiveness and scalability of the method. It offers valuable insights for research on inference acceleration in AR text-to-image generation. Although the idea of using a set to proxy a single point has been extensively researched, the authors have elegantly applied it to the sampling decision process and achieved excellent results. 
 Simplicity yet effectiveness is crucial.

### Weaknesses
1.For a specific image token, the algorithm for finding its proximity set , specifically "Find the neighborhood (i.e., Appendix B, Line 9)," lacks detailed discussion on efficiency. For example, for each quantized image token, are the corresponding sets A and B precomputed or dynamically calculated during inference? How much time does this part take? Specifically, the paper should detail the computational complexity of finding the k-nearest neighbors in the latent space for set B, and the subsequent filtering process for set A. It's crucial to understand if this neighborhood search involves an exhaustive search over the entire latent space or if any approximate nearest neighbor techniques are employed. Furthermore, the paper should analyze the memory footprint of storing these proximity sets, especially for large vocabularies.

2.In Line 105, there might be a misstatement. EAGLE-2 is an acceleration decoding method, not a drafter.

3.To demonstrate the generalizability of the observation of "token ambiguity," i.e., that this phenomenon is present in most AR image generation models, the paper should include experiments on a broader range of AR image generation models beyond just LLaMAGen. This would enhance the experimental completeness and provide stronger evidence for the generality of the observed issue. It is important to see if the degree of token ambiguity varies across different architectures and training procedures, and how this impacts the performance of the proposed method.

### Questions
1.There's a suggestion that the authors could provide the details of "Find the neighborhood" in Appendix A.

2.A suggestion is (since the experimental section of the current paper is already sufficient, this is just a gentle suggestion) that the authors could discuss more about the differences in token ambiguity between text generation and image generation. For example, in LLaMAGen, what common properties do tokens within the same set have? What are the patterns in the sizes of sets A and B corresponding to different image tokens? These discussions could help in designing further algorithms.

3.Could validation experiments be conducted on other AR models? This is also a optional suggestion aimed at enhancing the generalization and robustness of the method.

### Soundness
3

### Presentation
3

### Contribution
3
